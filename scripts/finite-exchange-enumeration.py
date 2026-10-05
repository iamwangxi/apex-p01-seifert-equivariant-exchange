#!/usr/bin/env python3
"""Exact extension census through eight vertices, then a nine-vertex census.

Coverage lemma: a finite exchange graph admits an injective exchange order;
deleting its largest vertex leaves a connected exchange graph. Thus extending
one representative of each (n-1)-vertex exchange graph by every neighborhood
covers every n-vertex exchange graph up to isomorphism. Eight-vertex parents
are deduplicated by exact isomorphism within invariant-signature buckets.

At nine vertices every extension is checked for dismantlability. Only a
nondismantlable extension needs the exact exchange-order solver. A completed
run with no such exchange graph excludes counterexamples through nine
vertices. Incomplete runs explicitly retain the unprocessed parent count.
"""
from collections import Counter
from datetime import datetime, timezone
import importlib.util
import json
from pathlib import Path
import time

import networkx as nx


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('small_exchange_checks', HERE / 'small-complex-check.py')
exchange = importlib.util.module_from_spec(spec)
spec.loader.exec_module(exchange)


def extend(nb, mask):
    old_n = len(nb)
    ret = list(nb) + [(1 << old_n) | mask]
    for u in exchange.vertices(mask):
        ret[u] |= 1 << old_n
    return ret


def nx_graph(nb):
    g = nx.Graph()
    g.add_nodes_from(range(len(nb)))
    g.add_edges_from(exchange.edges_of(nb))
    return g


def main():
    start = time.monotonic()
    stop = start + 1200
    report = {
        'started_utc': datetime.now(timezone.utc).isoformat(),
        'max_vertices': 9, 'time_budget_seconds': 1200,
        'coverage_argument': 'Tie-break any finite exchange rank. Removing its largest vertex leaves an exchange graph by sublevel heredity. Extend all lower-order isomorphism representatives by all nonempty neighborhoods.',
        'atlas_7_exchange_parents': 0,
        'eight': Counter(), 'nine': Counter(),
        'eight_complete': False, 'nine_complete': False,
        'nondismantlable_exchange_examples': [],
        'limitations': ['Counts of extension candidates include isomorphic duplicates.',
                        'Nine-vertex exchange graphs are not counted: exchange-order solving is required only for candidates failing dismantlability.',
                        'This is a finite-size result, not a proof for arbitrary finite graphs.']}
    target = HERE / 'finite-exchange-enumeration-results.json'

    def save():
        report['elapsed_seconds'] = round(time.monotonic() - start, 3)
        target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    def example(nb, rank, origin):
        report['nondismantlable_exchange_examples'].append({
            'n': len(nb), 'edges': exchange.edges_of(nb), 'rank': rank, 'origin': origin,
            'intervals': [{'pair': [u, w], 'common': list(exchange.vertices(common)),
                           'apices': list(exchange.vertices(apex)),
                           'lower_apices': [x for x in exchange.vertices(apex)
                                           if rank[x] < max(rank[u], rank[w])]}
                          for u, w, common, apex in exchange.interval_constraints(nb)]})

    parents = []
    for g in nx.graph_atlas_g():
        if len(g) != 7:
            continue
        nb = exchange.graph_data(7, g.edges())
        rank = exchange.exchange_rank(nb)
        if rank is not None:
            parents.append(nb)
    report['atlas_7_exchange_parents'] = len(parents)
    assert len(parents) == 382
    save()

    buckets = {}
    reps = []
    for parent_i, nb0 in enumerate(parents):
        for mask in range(1, 1 << 7):
            report['eight']['extension_candidates'] += 1
            nb = extend(nb0, mask)
            if exchange.interval_constraints(nb) is None:
                continue
            report['eight']['N1_candidates'] += 1
            rank = exchange.exchange_rank(nb)
            if rank is None:
                continue
            report['eight']['exchange_candidates'] += 1
            g = nx_graph(nb)
            # WL is only a bucket index; exact isomorphism performs deduplication.
            sig = (tuple(sorted(dict(g.degree()).values())), nx.weisfeiler_lehman_graph_hash(g))
            bucket = buckets.setdefault(sig, [])
            if any(nx.is_isomorphic(g, h) for h in bucket):
                continue
            bucket.append(g)
            reps.append(nb)
            report['eight']['unlabelled_exchange_graphs'] += 1
            if exchange.dismantling(nb) is None:
                example(nb, rank, f'eight-parent:{parent_i}:mask:{mask}')
            else:
                report['eight']['dismantlable_unlabelled_exchange_graphs'] += 1
        report['eight']['parents_processed'] = parent_i + 1
        if parent_i % 30 == 0:
            save()
            print('eight parents', parent_i + 1, 'representatives', len(reps), flush=True)
        if time.monotonic() >= stop:
            break
    report['eight_complete'] = report['eight']['parents_processed'] == len(parents)
    if not report['eight_complete']:
        report['stopped_because'] = 'time budget during eight-vertex census'
        save()
        return
    save()
    print('Eight complete', dict(report['eight']), flush=True)

    report['nine']['total_parents'] = len(reps)
    for parent_i, nb0 in enumerate(reps):
        for mask in range(1, 1 << 8):
            report['nine']['extension_candidates'] += 1
            nb = extend(nb0, mask)
            if exchange.interval_constraints(nb) is None:
                continue
            report['nine']['N1_candidates'] += 1
            if exchange.dismantling(nb) is not None:
                report['nine']['dismantlable_N1_candidates'] += 1
                continue
            report['nine']['nondismantlable_N1_candidates'] += 1
            rank = exchange.exchange_rank(nb)
            if rank is not None:
                example(nb, rank, f'nine-parent:{parent_i}:mask:{mask}')
                report['nine']['nondismantlable_exchange_candidates'] += 1
        report['nine']['parents_processed'] = parent_i + 1
        if parent_i % 100 == 0:
            save()
            print('nine parents', parent_i + 1, '/', len(reps), flush=True)
        if time.monotonic() >= stop:
            break
    report['nine_complete'] = report['nine']['parents_processed'] == len(reps)
    report['nine']['unprocessed_parents'] = len(reps) - report['nine']['parents_processed']
    report['finished_utc'] = datetime.now(timezone.utc).isoformat()
    save()
    print(json.dumps({'eight_complete': report['eight_complete'],
                      'nine_complete': report['nine_complete'],
                      'eight': report['eight'], 'nine': report['nine'],
                      'counterexamples': len(report['nondismantlable_exchange_examples']),
                      'elapsed_seconds': report['elapsed_seconds']}, ensure_ascii=False), flush=True)


if __name__ == '__main__':
    main()
