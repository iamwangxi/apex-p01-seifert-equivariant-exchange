# Literature comparison and computational evidence

The result proved in this repository is [Theorem E](theorem-e.md): fixed-point contractibility for finite complexity-preserving actions on arbitrary exchange complexes. Its [Seifert-surface application](seifert-application.md) is conditional on the competition paper's stated geometric inputs. The comparison below identifies what is already known and what this proof establishes without constructing projections. It does not certify that every possible implication from existing criteria has been excluded.

## Competition version and author version 2

The target is Apex Intelligence's *Contractibility of the complex of incompressible Seifert surfaces: the knot case of Kakimizu's problem*, competition version of 11 September 2026. Its introduction, printed p. 2, explicitly leaves the equivariant extension untreated. Definition 2.1, pp. 3–4, imposes an existential lower-apex condition. Theorem B, p. 4, proves nonequivariant contractibility; its proof refines complexity to an injective order using Lemma 2.2. Such a refinement generally destroys invariance under a group that permutes vertices of equal complexity.

G. Pan, C. You, J. Zhou and Y. Chen, arXiv:2609.09224v2 (12 September 2026), §8.4, printed pp. 67–68, likewise do not prove fixed-space contractibility. They already observe that a finite invariant simplex of least-complexity apices has a fixed barycenter. This repository claims no novelty for that observation. The proposed additional arguments are the descending common-link lemma, the fixed-face upper-fiber calculation, and the universal transfinite induction in the weak topology.

The seven-vertex example in v2, Proposition 7.3 and Remark 7.4, printed pp. 59–60, does not refute dismantlability. Vertex 6 is universal and dominates every other vertex. The example shows that deletion in reverse order of the supplied complexity need not be a dismantling order: vertex 6 cannot be deleted first. It leaves open other orders and projection constructions.

## Przytycki–Schultens: the minimal-genus complex

Przytycki–Schultens, *Contractibility of the Kakimizu complex and symmetric Seifert surfaces*, published in 2012, prove Theorem 1.5 for any subgroup of the mapping class group preserving the homology class and the homotopy class of the boundary data: the fixed space of $`MS(E,\gamma,\alpha)`$ is empty or contractible. The locally checked edition is arXiv:1004.4168v2, printed p. 4; Theorem 1.2, p. 3, supplies an invariant simplex for finite subgroups. These statements concern their minimal-genus complex and their specified group/data conventions.

Their §9, printed pp. 21–23 of that preprint, uses minimal invariant simplices as vertices of a model for the fixed space. Definition 9.1 and Lemmas 9.2–9.3, p. 22, construct a projection and establish adjacency and strict distance descent. Definition 9.4 and Theorem 9.5, p. 23, place finite subcomplexes inside finite convex ones with dismantlable graphs. The present result, restricted to finite complexity-preserving actions on exchange complexes and applied to $`IS(K)`$, does not extend their arbitrary-subgroup range.

Their preprint, printed p. 5, also explicitly notes that its finite-group invariant-simplex conclusion passes from $`MS`$ to $`IS`$ through the inclusion. Thus for groups satisfying its data conditions, $`IS`$ nonemptiness is already known; the proposed application concerns contractibility of the full $`IS`$ fixed space.

Their remaining-questions discussion, printed pp. 4–5, describes the obstacle to extending their method to all incompressible spanning surfaces: the additional operation in the connectivity construction was not known to give a well-defined map on isotopy classes. Existence of exchange witnesses does not resolve that projection problem.

## Hensel–Osajda–Przytycki: exact hypotheses

The checked original is *Realisation and dismantlability*, arXiv:1205.0513v1, 2 May 2012, 33 printed pages. The journal article is *Geom. Topol.* 18 (2014), 2079–2126. All theorem numbers and pinpoint pages here refer to arXiv v1; the journal version was not compared.

In HOP's Definition 2.1, printed p. 4, $`N(\rho)`$ includes $`\rho`$. To avoid conflict with the open-neighborhood convention used in [Theorem E](theorem-e.md), write these HOP neighborhoods as $`N[\rho]`$ here. Domination means $`N[\rho]\subseteq N[\pi]`$ with $`\pi\ne\rho`$, allowing equality of neighborhoods.

**Definition 2.6, printed pp. 5–6.** For a fixed vertex $`\sigma`$, a dismantling projection assigns each $`\rho\ne\sigma`$ a nonempty finite set $`\Pi_\sigma(\rho)`$ of pairs of vertices; the two entries of a pair may coincide. Let $`\Pi_\sigma^*(\rho)`$ be the union of the entries of these pairs. The conditions are:

1. For every finite vertex set $`R`$ with $`R\setminus\{\sigma\}\ne\varnothing`$, some $`\rho\in R\setminus\{\sigma\}`$ is exposed: there is a pair in $`\Pi_\sigma(\rho)`$ such that, for both its entries $`\pi`$,
   $`\displaystyle N[\rho]\cap R\subseteq N[\pi].`$
2. There is no finite cycle $`\rho_0,\ldots,\rho_{m-1}`$ with $`\rho_{i+1}\in\Pi_\sigma^*(\rho_i)`$, indices taken modulo $`m`$.

These are fixed finite projection values, required to work across all finite sets $`R`$. Lemma 2.7, p. 6, makes a finite graph with such a projection dismantlable. Definition 2.8 and Corollary 2.9, p. 6, give dismantlability for finite induced subgraphs on projection-convex sets.

**Theorem 1.4, printed p. 2; proof pp. 26–27.** A finite dismantlable graph's flag realization has a nonempty contractible fixed set under every finite automorphism group. No preserved exchange complexity is required.

**Definition 9.1, printed p. 27.** A family $`\{\Pi_\sigma\}_\sigma`$ is synchronised if, for every clique $`\Delta`$, any sequence satisfying $`\rho_{i+1}\in\Pi_{\sigma_i}^*(\rho_i)`$ with arbitrary $`\sigma_i\in\Delta`$ eventually enters $`\Delta`$ and stays there.

**Proposition 9.2, printed p. 27.** Let $`H`$ act by automorphisms on a graph with **no infinite cliques**. Assume a $`\sigma`$-projection for every vertex $`\sigma`$ and an $`H`$-equivariant family of these projections. Its flag fixed space is contractible if either:

1. $`H`$ fixes a vertex; or
2. $`H`$ preserves a clique setwise and the projection family is synchronised.

Synchronisation is required in the second alternative, not in the first. The group $`H`$ in this proposition need not be finite. Its proof constructs finite invariant projection-convex subgraphs and applies Corollary 2.9 and Theorem 1.4. On printed p. 27 it exhausts the union of invariant-clique vertices by a countable sequence of finite sets, although the printed statement includes no countability hypothesis. That exhaustion alone does not handle arbitrary cardinality. This is a scope limitation of that proof sentence, not a counterexample to the printed proposition. The transfinite argument here does not rely on it.

The exchange axiom only asserts that each distance-two pair has some lower apex. It supplies neither a finite projection value for every ordered pair of vertices nor the exposed condition for all finite $`R`$, the projection acyclicity, or synchronisation. The proof here does not verify these HOP hypotheses or impose the absence of infinite cliques. Thus Proposition 9.2 is not a direct application on the data provided by the exchange structure. We neither prove that suitable projections cannot exist nor claim that the exchange hypotheses are strictly weaker than HOP's. A further construction could reveal overlap; a complete novelty assessment must account for that possibility.

For finite exchange graphs, the computations below show dismantlability through nine vertices. Accordingly HOP Theorem 1.4 already covers the finite fixed-point conclusion in that size range. The data suggest that HOP may cover all finite exchange graphs, but this is an inference: the general finite dismantlability implication has not been proved here. The finite case is not presented as a new result independent of HOP.

## Reproducible evidence

The [small-complex script](../scripts/small-complex-check.py) checks all nonempty unlabelled graphs on at most seven vertices in NetworkX's atlas. For every ambient distance-two pair it calculates the entire two-interval and all its apices. Subset dynamic programming solves the existential exchange-order constraints. A separate dominated-vertex deletion search solves dismantlability; neither solver assumes the conclusion of the other.

The numbers of exchange graphs by vertex count 1 through 7 are respectively **1, 1, 2, 5, 16, 67, 382**, totaling **474**. All are dismantlable. Independent direct permutation search agrees with the order solver on all **143** connected atlas graphs on at most six vertices, using a separate set-based neighborhood calculation.

With seed **20261005**, the script also checks **60,000** random graphs on 7–9 vertices; **25,686** admit an exchange order and all of these are dismantlable. Half the random attempts use graphs invariant under a sampled permutation made of two- or three-cycles. Group tests include sampled cyclic actions and full automorphism groups when an invariant ranking is found. There are **34,007** distinct graph/orbit-partition checks with nonempty fixed spaces and zero reduced $`\mathbb F_2`$ homology. This number counts neither distinct isomorphism classes of graphs nor all possible group actions.

For a tested group, an invariant face is a union of those vertex orbits which themselves form cliques, subject to the union being a clique. The orbit clique complex has a face poset isomorphic to the poset of nonempty invariant faces. The code explicitly verifies that correspondence; it calculates homology on the smaller orbit triangulation, whose barycentric subdivision is the fixed-face order complex. It does not substitute the graph induced by pointwise fixed vertices. Controls detect the nonzero first homology of the pentagon, the empty fixed face poset of its rotation, the geometric fixed point of an edge with swapped endpoints, failure of the apex axiom on a square, and the second homology of the octahedral sphere.

The [extension census](../scripts/finite-exchange-enumeration.py) exhaustively excludes nondismantlable exchange graphs through **nine vertices**. Its coverage uses two mathematical facts, independent of equivariance: a finite exchange order can have its ties broken (competition Lemma 2.2, p. 4), and deleting the largest vertex leaves a connected exchange graph by sublevel heredity ([Lemma 2.2 here](theorem-e.md)). Therefore every next-size exchange graph is an extension of some previous-size isomorphism representative by a nonempty neighborhood.

From the **382** seven-vertex representatives, all **48,514** extensions are tested. Exact isomorphism, with degree and Weisfeiler–Lehman signatures used only for bucketing, leaves **3,209** eight-vertex exchange representatives; all are dismantlable. The script then tests all **818,295** extensions of those representatives. Of **457,564** candidates satisfying the apex-existence axiom, **437,361** are dismantlable. The remaining **20,203** candidates all fail the exact exchange-order solver. Both stages finish with **zero unprocessed parents** and **zero nondismantlable exchange examples**.

The nine-vertex stage does not count all nine-vertex exchange graphs: it solves exchange-order existence only for candidates that fail dismantlability. Candidate counts can include isomorphic duplicates. Reduced homological acyclicity is a counterexample filter, not a proof of contractibility. No conclusion about infinite graphs or general finite dismantlability follows from the census.

Both public scripts were rerun in preparing this package. All non-timing fields in their output JSON agree with the originally recorded results. Commands, versions, run times and output meanings are in [scripts/README.md](../scripts/README.md). Theorem E is proved independently of the calculations.
