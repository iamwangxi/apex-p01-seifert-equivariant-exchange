# Reproducing the finite computations

Both scripts run offline with **Python 3.9.6** and **NetworkX 3.2.1**, the environment used for the recorded outputs. They use the already installed NetworkX atlas; no external graph download is needed. NetworkX is the sole third-party dependency. To provision a separate environment, install `networkx==3.2.1` before running these commands.

From the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/small-complex-check.py --random-per-n 20000 --seconds 900
PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-exchange-enumeration.py
```

Each script writes its corresponding result JSON beside itself, replacing any previous result. Running them therefore changes the recorded timestamps and run times and invalidates the precomputed manifest for those regenerated JSON bytes. The mathematical counts below should remain identical in the stated environment. To check the published package before rerunning, use `shasum -a 256 -c MANIFEST.sha256` from the repository root, or `sha256sum -c MANIFEST.sha256` on systems with GNU coreutils.

## Small-complex census and fixed-space homology

[small-complex-check.py](small-complex-check.py) writes [small-complex-results.json](small-complex-results.json). The random seed is **20261005**. The atlas stage exhausts unlabelled graphs on 1–7 vertices. Exact subset dynamic programming tests exchange-order existence on full ambient two-intervals; a separate search deletes dominated vertices using closed neighborhoods. Direct permutation search independently checks the order solver on all 143 connected atlas graphs with at most six vertices.

The standard command completes 20,000 random attempts for each of 7, 8 and 9 vertices. The `--seconds` budget bounds the random stage, measured from the start of the whole run; the atlas stage completes first. Any interrupted random size records `time_limit_reached`, so reduced sample sizes must not be described as the full 60,000-attempt run.

The `census` entries record all graphs, connected graphs, apex-existence graphs, exchange graphs, dismantlable exchange graphs, and attempted compatible groups. The `random` entries are attempt counts, not counts of distinct isomorphism classes. `fixed_checks` counts distinct graph/orbit-partition cases. The fixed model is the orbit clique complex, with its face poset explicitly verified against the invariant-face poset. Reduced homology is calculated over $`\mathbb F_2`$. Zero homology does not establish contractibility.

Expected complete-run results: **474** atlas exchange graphs, all dismantlable; **25,686** exchange graphs among **60,000** random attempts, all dismantlable; **34,007** fixed-space checks; empty `fixed_failures` and `nondismantlable_exchange_examples`. The positive and negative controls appear in `self_checks`. The v2 seven-vertex example is also checked and a dismantling certificate is emitted.

This package's complete rerun took **33.259 seconds**. Expect tens of seconds to a few minutes, depending on hardware and load. Time fields are measurements, not determinism claims.

## Exact extension census through nine vertices

[finite-exchange-enumeration.py](finite-exchange-enumeration.py) imports the first script by a path relative to its own location and writes [finite-exchange-enumeration-results.json](finite-exchange-enumeration-results.json). It examines all nonempty-neighborhood extensions of the 382 seven-vertex exchange representatives. Eight-vertex representatives are deduplicated by exact isomorphism. It then tests all extensions of those representatives for a nondismantlable exchange graph.

Coverage is justified in [proof/literature.md](../proof/literature.md): nonequivariant tie refinement and sublevel heredity reduce every finite exchange graph to a smaller exchange parent. No refinement is used in the equivariant proof.

Expected complete-run results: **48,514** eight-vertex extension candidates; **3,209** unlabelled eight-vertex exchange representatives, all dismantlable; **818,295** nine-vertex extension candidates; **457,564** satisfying apex existence; **20,203** nondismantlable candidates, none admitting an exchange order. Require `eight_complete` and `nine_complete` to be true, `nine.unprocessed_parents` to equal zero, and `nondismantlable_exchange_examples` to be empty.

The nine-vertex stage does **not** count all nine-vertex exchange graphs. It invokes the order solver only for candidates that fail dismantlability. Candidate counts include isomorphic duplicates. A built-in **1,200-second** budget can leave a partial run, explicitly marked incomplete; partial output does not support the nine-vertex exclusion.

This package's full rerun took **66.564 seconds**. Expect roughly a minute to several minutes in the stated environment. All non-timing fields of both regenerated JSON files agreed with the originally recorded results. These finite-size checks do not prove general finite dismantlability, exhaust all group actions, or establish an infinite-complex theorem.

## License

Code in `scripts/` is licensed under MIT; original prose in this README is licensed under CC BY 4.0. See [LICENSE](../LICENSE). NetworkX retains its own license.
