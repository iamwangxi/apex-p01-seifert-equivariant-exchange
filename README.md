# Fixed-point contractibility for exchange complexes and incompressible Seifert surfaces

**Theorem E proves that every finite complexity-preserving simplicial group action on an exchange complex has a nonempty contractible geometric fixed-point space.** The realization has the weak topology; vertices and dimensions may be arbitrary, and complexity may have ties. **Corollary E′ applies to actual finite smooth symmetries of a nontrivial knot, conditional on the same external analytic inputs (U), (E), and (Fin) used in the target paper's Theorem A.**

## Target and contribution

This package accompanies a proposed **breakthrough contribution (valuable generalization)** to Apex Intelligence's *Contractibility of the complex of incompressible Seifert surfaces: the knot case of Kakimizu's problem*, the **11 September 2026 competition version**, 48 printed pages. Target PDF SHA-256:

`34f17d7d99780d3fd3626d9e5d7b35d6aa76661c404f191b6df341b300c0c06f`

The competition introduction, printed p. 2, leaves the equivariant extension untreated. The authors' later arXiv:2609.09224v2, §8.4, pp. 67–68, still supplies no fixed-space contractibility proof. Its invariant-apex barycenter observation is already known and is not claimed as this package's contribution.

The proof preserves the original complexity without breaking ties. Its central additional lemma says that the strictly lower common link of a nonempty finite face of equal, nonminimum complexity is a nonempty exchange complex of diameter at most two. The proof then models the fixed set by chains of invariant faces, computes the relevant upper fibers, and uses universal transfinite induction. All topological arguments use weak CW realizations, including at uncountable limit stages.

## Exact scope and comparison limits

An exchange complex is nonempty, connected and flag, with a well-ordered complexity such that every distance-two pair has an apex adjacent or equal to every member of its two-interval, and some such apex has complexity strictly below the larger endpoint value. No global or equivariant apex selection is assumed.

The theorem has no local-finiteness, countability, finite-dimension or finite-complexity-fiber assumption. It concerns **finite groups preserving complexity**; it does not extend Przytycki–Schultens's arbitrary-subgroup result for the minimal-genus complex. Hensel–Osajda–Przytycki have a finite dismantlable-graph fixed-point theorem and an infinite criterion requiring finite dismantling projections, equivariance, no infinite cliques and, in the invariant-clique alternative, synchronisation. Those projection data are not supplied by the exchange axioms. This package does not prove that appropriate projections cannot exist or that all coverage by previous criteria has been excluded.

The exhaustive computation finds **all finite exchange graphs with at most nine vertices dismantlable**. HOP's finite theorem therefore already covers that finite-size fixed-point conclusion. The computations suggest possible coverage of the general finite case but do not prove it; the finite case is not presented as a novelty claim. For groups satisfying PS's data conventions, its finite invariant simplex already passes from $MS$ to $IS$ (checked preprint p. 5); the proposed application contributes contractibility of the entire $IS$ fixed space.

The Seifert application constructs invariant geometric data within the target's exact warped-collar scope. It does not independently reprove the target's external area-minimization assertions or certify all its internal analytic arguments. A fixed point yields a finite invariant simplex of isotopy classes, not an individual invariant embedded surface or an equivariant simultaneous realization. A finite mapping-class subgroup needs a separate realization step before the metric construction applies.

## Repository guide

- [proof/theorem-e.md](proof/theorem-e.md): statement, conventions, sublevel geodesics without tie refinement, minimum layer and strictly lower common links (§§1–3).
- [proof/fixed-point-model.md](proof/fixed-point-model.md): the fixed-face model, a directly proved upper-fiber lemma and the finite-inclusion contractibility criterion (§§4–5).
- [proof/induction.md](proof/induction.md): base, successor and limit steps of universal transfinite induction and a dependency ledger (§6).
- [proof/seifert-application.md](proof/seifert-application.md): invariant geometric data and conditional Corollary E′ (§7).
- [proof/literature.md](proof/literature.md): checked comparison with the competition version, v2, Przytycki–Schultens and HOP, with computational evidence and novelty limits.
- [scripts/README.md](scripts/README.md): reproduction commands, dependency versions, measured run times, expected outputs and computation limits; both Python scripts and their result JSON are in that directory.
- [sources/bibliography.md](sources/bibliography.md): source editions, actually checked statements and printed pages, public acquisition routes and verification limits.
- [README.zh-CN.md](README.zh-CN.md): corresponding Chinese overview.
- [LICENSE](LICENSE): CC BY 4.0 for original prose; MIT for code.
- [MANIFEST.sha256](MANIFEST.sha256): SHA-256 of every other repository file.

Both computation scripts were fully rerun. All non-timing result fields agree with the originally recorded results: 474 atlas exchange graphs, 25,686 exchange graphs among 60,000 random attempts, 34,007 fixed-space homology checks, and all 818,295 nine-vertex extension candidates processed. These checks are independent evidence, not the proof of Theorem E.

From the repository root, `shasum -a 256 -c MANIFEST.sha256` (macOS) or `sha256sum -c MANIFEST.sha256` (GNU coreutils) checks the packaged bytes. A computation rerun overwrites the result JSON and changes their hashes. The manifest certifies bytes, not mathematical correctness.

## Review status and AI disclosure

A separate fresh-context GPT-6.1 Sol adversarial review found no mathematical break in the abstract proof or invariant-data construction. Its two literature corrections and two clarification suggestions have been incorporated: HOP coverage remains unresolved, exact projection conditions are stated, the full analytic input statements are retained, and PS already supplies nonemptiness for its data-preserving groups.

GPT-6.1 Sol, in OpenAI Codex under human direction, developed the proof, ran the computations where applicable, and drafted this text; a separate GPT-6.1 Sol session in a fresh context performed an adversarial review. Claude planned the work, checked key steps against the sources, and reviewed and edited the final text. No human expert has certified the work.

## License

Original prose is licensed under **CC BY 4.0**, to the extent applicable rights exist. Attribute it to the **apex-p01-seifert-equivariant-exchange contributors**, link the license, indicate changes, and include the public repository URL and version when available. Code in `scripts/` is licensed under **MIT**. External publications and NetworkX retain their own rights. See [LICENSE](LICENSE).
