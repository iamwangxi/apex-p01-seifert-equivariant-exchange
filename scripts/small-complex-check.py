#!/usr/bin/env python3
"""Offline exact small-graph census and seeded symmetric random checks.

All output stays beside this script. No downloads, subprocesses or Git calls.
An exchange order is found by subset dynamic programming, not by assuming
dismantlability. Fixed-face homology is computed over F_2 via the orbit
triangulation: its face poset is exactly the poset of invariant nonempty faces.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
from functools import lru_cache
from itertools import combinations, permutations
from pathlib import Path
import json
import random
import time

import networkx as nx


def vertices(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def graph_data(n, edges):
    nb = [1 << i for i in range(n)]
    for u, v in edges:
        nb[u] |= 1 << v
        nb[v] |= 1 << u
    return nb


def connected(nb):
    if not nb:
        return False
    seen = 1
    while True:
        nxt = seen
        for u in vertices(seen):
            nxt |= nb[u]
        if nxt == seen:
            return seen == (1 << len(nb)) - 1
        seen = nxt


def interval_constraints(nb):
    """Return all ambient distance-two pairs and their *full* apex sets."""
    constraints = []
    for u, w in combinations(range(len(nb)), 2):
        if nb[u] & (1 << w):
            continue
        common = nb[u] & nb[w]
        if not common:
            continue
        apex = 0
        for x in vertices(common):
            if common & ~nb[x] == 0:
                apex |= 1 << x
        if not apex:
            return None
        constraints.append((u, w, common, apex))
    return constraints


def exchange_rank(nb, blocks=None):
    """Exact existence of an exchange rank constant on specified orbit blocks.

    Singleton blocks cover *all* injective orders, hence all possible exchange
    complexities on a finite graph (by the tie-breaking lemma). For orbit
    blocks, each new block must have witnesses in strictly earlier blocks.
    """
    constraints = interval_constraints(nb)
    if constraints is None or not connected(nb):
        return None
    blocks = blocks or [1 << i for i in range(len(nb))]
    total = (1 << len(blocks)) - 1
    unions = [0] * (1 << len(blocks))
    for s in range(1, len(unions)):
        b = s & -s
        unions[s] = unions[s ^ b] | blocks[b.bit_length() - 1]

    @lru_cache(None)
    def solve(s):
        if s == total:
            return ()
        old = unions[s]
        for i, block in enumerate(blocks):
            if s & (1 << i):
                continue
            new = old | block
            if any(new & (1 << u) and new & (1 << w)
                   and (block & ((1 << u) | (1 << w)))
                   and not (apex & old)
                   for u, w, common, apex in constraints):
                continue
            suffix = solve(s | (1 << i))
            if suffix is not None:
                return (i,) + suffix
        return None

    order = solve(0)
    if order is None:
        return None
    rank = [0] * len(nb)
    for r, i in enumerate(order):
        for v in vertices(blocks[i]):
            rank[v] = r
    assert verify_rank(nb, rank)
    return rank


def verify_rank(nb, rank):
    constraints = interval_constraints(nb)
    return connected(nb) and constraints is not None and all(
        any(rank[x] < max(rank[u], rank[w]) for x in vertices(apex))
        for u, w, common, apex in constraints)


def dismantling(nb):
    """Exact search over every dominated-vertex deletion; output certificate."""
    @lru_cache(None)
    def solve(s):
        if s and s & (s - 1) == 0:
            return ()
        for u in vertices(s):
            nu = nb[u] & s
            for w in vertices(s ^ (1 << u)):
                if nu & ~(nb[w] & s) == 0:
                    suffix = solve(s ^ (1 << u))
                    if suffix is not None:
                        return ((u, w),) + suffix
        return None
    return solve((1 << len(nb)) - 1)


def orbit_blocks(n, generators):
    parent = list(range(n))
    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    for p in generators:
        for i, j in enumerate(p):
            parent[root(i)] = root(j)
    blocks = {}
    for i in range(n):
        r = root(i)
        blocks[r] = blocks.get(r, 0) | (1 << i)
    return sorted(blocks.values())


def is_clique(nb, s):
    return all(s & ~nb[u] == 0 for u in vertices(s))


def rank_f2(columns):
    pivots = {}
    for col in columns:
        while col:
            i = col.bit_length() - 1
            if i not in pivots:
                pivots[i] = col
                break
            col ^= pivots[i]
    return len(pivots)


def reduced_homology(faces):
    by_dim = {}
    for s in faces:
        by_dim.setdefault(bin(s).count('1') - 1, []).append(s)
    if not faces:
        return {-1: 1}
    top = max(by_dim)
    ranks = {0: 1}  # augmentation C_0 -> F_2
    for d in range(1, top + 1):
        rows = {s: i for i, s in enumerate(by_dim.get(d - 1, []))}
        columns = []
        for s in by_dim.get(d, []):
            col = 0
            for v in vertices(s):
                col ^= 1 << rows[s ^ (1 << v)]
            columns.append(col)
        ranks[d] = rank_f2(columns)
    return {d: len(by_dim.get(d, [])) - ranks.get(d, 0) - ranks.get(d + 1, 0)
            for d in range(top + 1)}


def fixed_check(nb, generators):
    n = len(nb)
    for p in generators:
        assert sorted(p) == list(range(n))
        assert all(bool(nb[u] & (1 << v)) == bool(nb[p[u]] & (1 << p[v]))
                   for u in range(n) for v in range(n))
    blocks = orbit_blocks(n, generators)
    admissible = [s for s in blocks if is_clique(nb, s)]
    invariant_faces = [s for s in range(1, 1 << n)
                       if is_clique(nb, s)
                       and all(sum(1 << p[v] for v in vertices(s)) == s
                               for p in generators)]
    orbit_faces = []
    correspondence = {}
    for t in range(1, 1 << len(admissible)):
        s = 0
        for i in vertices(t):
            s |= admissible[i]
        if is_clique(nb, s):
            orbit_faces.append(t)
            correspondence[t] = s
    assert sorted(correspondence.values()) == invariant_faces
    # Inclusion is preserved in both directions: the order complexes coincide.
    for t, s in correspondence.items():
        for i in vertices(t):
            t0 = t ^ (1 << i)
            if t0:
                assert correspondence[t0] & ~s == 0
    betti = reduced_homology(orbit_faces)
    return {'orbits': [list(vertices(s)) for s in blocks],
            'invariant_face_count': len(invariant_faces),
            'orbit_face_count': len(orbit_faces),
            'reduced_betti_F2': betti,
            'nonempty_acyclic': bool(orbit_faces) and all(b == 0 for b in betti.values())}


def edges_of(nb):
    return [[u, v] for u, v in combinations(range(len(nb)), 2)
            if nb[u] & (1 << v)]


def sample_symmetric(n, rng):
    p = list(range(n))
    shuffled = list(range(n))
    rng.shuffle(shuffled)
    cycle_size = rng.choice((2, 3))
    for start in range(0, n - cycle_size + 1, cycle_size):
        cyc = shuffled[start:start + cycle_size]
        for i, v in enumerate(cyc):
            p[v] = cyc[(i + 1) % cycle_size]
    edge_orbits, unseen = [], set(combinations(range(n), 2))
    while unseen:
        e = min(unseen)
        orbit = set()
        while e not in orbit:
            orbit.add(e)
            e = tuple(sorted((p[e[0]], p[e[1]])))
        unseen -= orbit
        edge_orbits.append(orbit)
    prob = rng.uniform(.25, .90)
    edges = [e for orbit in edge_orbits if rng.random() < prob for e in orbit]
    return graph_data(n, edges), p


def self_checks():
    # Distinguish an N1 cycle from an exchange graph, and detect nonzero homology.
    cycle = graph_data(5, [(i, (i + 1) % 5) for i in range(5)])
    assert interval_constraints(cycle) is not None
    assert exchange_rank(cycle) is None and dismantling(cycle) is None
    assert fixed_check(cycle, [])['reduced_betti_F2'][1] == 1
    assert not fixed_check(cycle, [[1, 2, 3, 4, 0]])['nonempty_acyclic']
    # A transposed edge has no fixed vertex, but has a geometric fixed point.
    edge = graph_data(2, [(0, 1)])
    check = fixed_check(edge, [[1, 0]])
    assert check['nonempty_acyclic'] and check['invariant_face_count'] == 1
    # A four-cycle has no apex in its opposite-vertex two-interval.
    square = graph_data(4, [(i, (i + 1) % 4) for i in range(4)])
    assert interval_constraints(square) is None
    # A higher-dimensional positive homology control: the octahedral sphere.
    octa = graph_data(6, [(u, v) for u, v in combinations(range(6), 2)
                          if (u // 2) != (v // 2)])
    assert fixed_check(octa, [])['reduced_betti_F2'][2] == 1
    # Independent direct permutation search checks the order DP on all <=6
    # vertex atlas graphs. This verifier uses Python sets, not mask constraints.
    brute_count = 0
    for g in nx.graph_atlas_g():
        n = len(g)
        if not 1 <= n <= 6:
            continue
        nb = graph_data(n, g.edges())
        if not connected(nb):
            assert exchange_rank(nb) is None
            continue
        open_nb = [set(g.neighbors(v)) for v in range(n)]
        independent = []
        n1 = True
        for u, w in combinations(range(n), 2):
            if w in open_nb[u]:
                continue
            common = open_nb[u] & open_nb[w]
            if not common:
                continue
            apices = {x for x in common if common <= open_nb[x] | {x}}
            if not apices:
                n1 = False
                break
            independent.append((u, w, apices))
        exists = False
        if n1:
            for order in permutations(range(n)):
                rank = {v: i for i, v in enumerate(order)}
                if all(any(rank[x] < max(rank[u], rank[w]) for x in apices)
                       for u, w, apices in independent):
                    exists = True
                    break
        assert (exchange_rank(nb) is not None) == exists
        brute_count += 1
    return ['C5: N1 true, exchange-order impossible, H1(F2)=F2',
            'rotated C5: fixed-face poset empty',
            'transposed edge: geometric fixed point, no fixed vertex',
            'C4: N1 false', 'octahedral sphere: H2(F2)=F2',
            f'order DP agrees with direct permutation search on all {brute_count} connected atlas graphs with <=6 vertices; disconnected graphs rejected']


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--random-per-n', type=int, default=20000)
    parser.add_argument('--seconds', type=int, default=900)
    args = parser.parse_args()
    start = time.monotonic()
    deadline = start + args.seconds
    rng = random.Random(20261005)
    result = {'seed': 20261005, 'field': 'F2', 'max_vertices': 9,
              'started_utc': datetime.now(timezone.utc).isoformat(),
              'self_checks': self_checks(), 'census': {}, 'random': {},
              'fixed_checks': 0, 'fixed_failures': [], 'nondismantlable_exchange_examples': [],
              'scope': 'All NetworkX atlas graphs with 1..7 vertices; exact order and dismantling DP. Seeded random 7..9 vertex graphs. No inference from acyclicity to contractibility.'}
    fixed_cache = set()

    def check_group(nb, gens, rank, origin):
        assert verify_rank(nb, rank)
        assert all(rank[v] == rank[p[v]] for p in gens for v in range(len(nb)))
        key = (tuple(nb), tuple(orbit_blocks(len(nb), gens)))
        if key in fixed_cache:
            return
        fixed_cache.add(key)
        check = fixed_check(nb, gens)
        result['fixed_checks'] += 1
        if not check['nonempty_acyclic']:
            result['fixed_failures'].append({'n': len(nb), 'edges': edges_of(nb),
                                            'rank': rank, 'generators': gens,
                                            'origin': origin, 'check': check})

    def record_graph(nb, rank, origin):
        certificate = dismantling(nb)
        if certificate is None:
            example = {'n': len(nb), 'edges': edges_of(nb), 'rank': rank,
                       'origin': origin,
                       'intervals': [{'pair': [u, w], 'common': list(vertices(common)),
                                      'apices': list(vertices(apex)),
                                      'lower_apices': [x for x in vertices(apex)
                                                      if rank[x] < max(rank[u], rank[w])]}
                                     for u, w, common, apex in interval_constraints(nb)]}
            if len(result['nondismantlable_exchange_examples']) < 5:
                result['nondismantlable_exchange_examples'].append(example)
        check_group(nb, [], rank, origin)
        return certificate is not None

    for atlas_id, g in enumerate(nx.graph_atlas_g()):
        n = len(g)
        if not n:
            continue
        counts = result['census'].setdefault(str(n), Counter())
        counts['all_unlabelled_graphs'] += 1
        nb = graph_data(n, g.edges())
        if not connected(nb):
            continue
        counts['connected'] += 1
        if interval_constraints(nb) is None:
            continue
        counts['N1'] += 1
        rank = exchange_rank(nb)
        if rank is None:
            continue
        counts['exchange'] += 1
        counts['dismantlable_exchange'] += record_graph(nb, rank, f'atlas:{atlas_id}')
        # At most 16 cyclic subgroups, plus the full automorphism group.
        # Collecting all automorphisms here is exact (n<=7, at most 7!).
        autos = [tuple(m[i] for i in range(n))
                 for m in nx.algorithms.isomorphism.GraphMatcher(g, g).isomorphisms_iter()]
        candidates = [[p] for p in autos[:16]] + [autos]
        for gens in candidates:
            blocks = orbit_blocks(n, gens)
            invariant_rank = exchange_rank(nb, blocks)
            if invariant_rank is not None:
                check_group(nb, gens, invariant_rank, f'atlas:{atlas_id}')
                counts['compatible_group_attempts'] += 1
    print('Atlas complete:', result['census'], flush=True)

    for n in (7, 8, 9):
        counts = Counter()
        for i in range(args.random_per_n):
            if time.monotonic() >= deadline:
                counts['time_limit_reached'] += 1
                break
            counts['attempts'] += 1
            if i % 2:
                nb, p = sample_symmetric(n, rng)
                counts['symmetric_attempts'] += 1
            else:
                prob = rng.uniform(.20, .95)
                nb = graph_data(n, [e for e in combinations(range(n), 2)
                                    if rng.random() < prob])
                p = None
            if not connected(nb):
                continue
            counts['connected'] += 1
            if interval_constraints(nb) is None:
                continue
            counts['N1'] += 1
            rank = exchange_rank(nb)
            if rank is None:
                continue
            counts['exchange'] += 1
            counts['dismantlable_exchange'] += record_graph(nb, rank, f'random:{n}:{i}')
            if p is not None:
                invariant_rank = exchange_rank(nb, orbit_blocks(n, [p]))
                if invariant_rank is not None:
                    check_group(nb, [p], invariant_rank, f'random:{n}:{i}')
                    counts['compatible_nontrivial_group_attempts'] += 1
        result['random'][str(n)] = counts
        print('Random', n, dict(counts), flush=True)

    # Reproduce v2 Proposition 7.3; its top vertex is not deletable first.
    seven = graph_data(7, [(i, (i + 1) % 6) for i in range(6)]
                       + [(0, 2), (2, 4), (4, 0)] + [(6, i) for i in range(6)])
    assert verify_rank(seven, list(range(7)))
    result['v2_seven_vertex_example'] = {
        'rank': list(range(7)), 'edges': edges_of(seven),
        'dismantling_certificate': dismantling(seven),
        'top_6_dominated': any(seven[6] & ~seven[w] == 0 for w in range(6)),
        'all_lower_vertices_dominated_by_6': all(seven[u] & ~seven[6] == 0 for u in range(6))}
    result['elapsed_seconds'] = round(time.monotonic() - start, 3)
    result['finished_utc'] = datetime.now(timezone.utc).isoformat()
    result['limitations'] = [
        'Random tests do not exhaust n=8 or n=9.',
        'Only sampled subgroups, and rank assignments found by the block-order solver, were tested.',
        'Reduced F2 homology is a counterexample filter; zero homology is not a proof of contractibility.',
        'The fixed order-complex computation uses the explicitly verified orbit-face-poset isomorphism; it does not enumerate every subdivision chain.',
        'No claim about infinite graphs follows from this census.']
    target = Path(__file__).with_name('small-complex-results.json')
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'fixed_checks': result['fixed_checks'],
                      'fixed_failures': len(result['fixed_failures']),
                      'nondismantlable_exchange_examples': len(result['nondismantlable_exchange_examples']),
                      'elapsed_seconds': result['elapsed_seconds']}, ensure_ascii=False), flush=True)


if __name__ == '__main__':
    main()
