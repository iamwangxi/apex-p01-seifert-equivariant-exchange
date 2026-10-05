# Bibliography, editions and checked locations

Public links below identify source editions or bibliographic destinations. No third-party full text or PDF is redistributed. Pinpoint pages refer to the specified printed edition, never to extracted-text line numbers. Only the listed statements and relevant excerpts were checked; this list does not claim an independent audit of each cited work's full proof.

## Target competition paper

**Apex Intelligence.** *Contractibility of the complex of incompressible Seifert surfaces: the knot case of Kakimizu's problem*. Official competition version, **11 September 2026**, **48 printed pages**.

Acquisition: the official competition PDF, `seifert-surfaces.pdf`, SHA-256 `34f17d7d99780d3fd3626d9e5d7b35d6aa76661c404f191b6df341b300c0c06f`.

Checked locations:

- Introduction, p. 2: equivariant extension left untreated.
- Definition 2.1, pp. 3–4: open neighborhoods, two-intervals, full apex property, and existential strict descent.
- Theorem B and Lemma 2.2, p. 4: nonequivariant theorem and tie refinement.
- §2, p. 6: weak topology and the compact-image/finite-subcomplex step.
- §3, equations (2)–(3), p. 6: the warped collar and boundary convexity conventions.
- Theorems 3.1–3.3, p. 7, and Remark 3.4, pp. 7–8: (U), (E), (Fin), and the boundary-regularity dependency.
- Definition 4.1, p. 8: vertices, isotopy and simplex conventions.
- Definition 4.7 and Lemma 4.8, pp. 10–11: genus–area complexity and well ordering.
- Statements of Theorem 5.1 and Proposition 5.2, p. 13: exchange lemma and lower apices. The underlying exchange proof is used as the target paper's internal argument, not newly certified here.
- §6.1, proof of Theorem A, pp. 19–20: assembly of connectedness, flagness, well ordering and the exchange axioms from the stated inputs.
- Definition A.1 and equation (27), p. 23: the piecewise-smooth membership convention explicitly retained in the fixed-boundary clause of (E).

The Seifert application explicitly assumes these same external analytic statements for the constructed invariant geometric data. The repository does not independently reprove sliding-boundary existence, compactness or all of Appendix A.

## Author version 2

**G. Pan, C. You, J. Zhou and Y. Chen.** *Exchange complexes and contractibility of the complex of incompressible Seifert surfaces*. [arXiv:2609.09224v2](https://arxiv.org/abs/2609.09224v2), **12 September 2026**.

Acquisition: arXiv v2 PDF. SHA-256 `f3e9b5f1364886c3d88081c5082caffdd4fce5cd7ec8c529ab96fbeeb8becf64`.

Checked: §7.3, Proposition 7.3 and Remark 7.4, printed pp. 59–60 (the given exchange order versus graph dismantlability); §8.4, printed pp. 67–68 (invariant geometric data, the fixed-barycenter observation, and absence of a fixed-space contractibility proof). The competition submission is directed at the earlier hash-identified version. No claim of verifying the v2 analytic developments is made.

## Przytycki–Schultens

**Piotr Przytycki and Jennifer Schultens.** *Contractibility of the Kakimizu complex and symmetric Seifert surfaces*. *Transactions of the American Mathematical Society* **364** (2012), no. 3, 1489–1508.

Checked edition and acquisition route: [arXiv:1004.4168v2](https://arxiv.org/abs/1004.4168v2), **2 June 2010**. PDF SHA-256 `fd27c311f7cc937d54bb7c8e2530a172eeafa6f7e26a1cb0fe98f6aaeb755cb2`. Journal bibliographic data identify the published work; the following are **preprint printed pages**, not verified journal pinpoint pages.

Checked: introductory data and complex conventions, p. 2; Theorem 1.2 and Corollary 1.3, p. 3; Theorem 1.5 and remaining questions, pp. 4–5; the fixed-space construction in §9, pp. 21–23, especially Definition 9.1 and Lemmas 9.2–9.3, p. 22, and Definition 9.4 and Theorem 9.5, p. 23. Their result covers any subgroup preserving their specified homology and boundary data and concerns the minimal-genus complex. No broader orientation or data convention is silently substituted.

## Hensel–Osajda–Przytycki

**Sebastian Hensel, Damian Osajda and Piotr Przytycki.** *Realisation and dismantlability*. *Geometry & Topology* **18** (2014), 2079–2126.

Checked edition and recorded acquisition route: [arXiv:1205.0513v1](https://arxiv.org/abs/1205.0513v1), **2 May 2012**, [version-specific PDF](https://arxiv.org/pdf/1205.0513v1), 33 printed pages. PDF SHA-256: `384fca19ac32813f2912111671f89bf940f3c6ed0f0387d2973b338517439685`.

Checked original statements: Definition 2.1, p. 4 (closed-neighborhood domination); Definition 2.6, pp. 5–6 (finite pair-valued projections, exposed-vertex and acyclicity axioms); Lemma 2.7, Definition 2.8 and Corollary 2.9, p. 6; Theorem 1.4, p. 2, and its proof in §9, pp. 26–27; Definition 9.1 and Proposition 9.2, p. 27 (synchronisation, no infinite cliques, equivariance, and the two alternatives for a fixed vertex or invariant clique).

Theorem numbers and pages refer to arXiv v1; the journal version was not compared. Other theorem numbers and all pinpoint pages in this package refer to arXiv v1. The complete hypotheses, rather than an earlier secondary summary, are used in [the comparison](../proof/literature.md). The countable-exhaustion sentence in the proof of Proposition 9.2 on p. 27 is recorded there as insufficient by itself at arbitrary cardinality; no counterexample to the printed statement is claimed.

## Topological and geometric background

The upper-fiber lemma is the poset version of Quillen's Theorem A; a direct carrier proof is included in [fixed-point-model.md](../proof/fixed-point-model.md), so no unverified theorem number or source page is needed. That file also proves the finite-inclusion criterion by cellwise prism extension. The remaining CW background is weak realization, barycentric subdivision, the CW product with the interval, and compact containment in a finite subcomplex; the latter two are also used in the target's §2, p. 6.

The invariant torus construction uses standard scalar Poisson solvability on a closed connected Riemannian manifold, the conformal curvature formula, and the affine description of flat-torus isometries. These are used at standard-statement level, with the invariant-data argument written out in [seifert-application.md](../proof/seifert-application.md). No separately checked textbook edition or pinpoint page is claimed for them. This does not upgrade the target's external area-minimization inputs to independently verified theorems.

## Computational source

**NetworkX 3.2.1**, its included graph atlas, graph isomorphism routines and Weisfeiler–Lehman graph hash. Acquisition: an already installed dependency, used offline. [Version-specific documentation](https://networkx.org/documentation/networkx-3.2.1/reference/generated/networkx.generators.atlas.graph_atlas_g.html) identifies the atlas API. No documentation lookup was performed during packaging.

The public code contains the exchange-order, dismantling and homology algorithms and was fully rerun. Weisfeiler–Lehman hashes are only bucket labels; exact isomorphism determines duplicates. See [scripts/README.md](../scripts/README.md) for environment and reproducibility details.
