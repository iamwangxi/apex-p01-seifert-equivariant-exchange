# Invariant geometric data and conditional Seifert application

The abstract fixed-point result is [Theorem E](theorem-e.md), proved in [the induction](induction.md). Source versions and comparison limits are in [the literature discussion](literature.md) and [bibliography](../sources/bibliography.md).

## 7. Invariant geometric data for actual knot symmetries

**Geometric-data proposition.** Let a finite group $`G`$ act smoothly on the pair $`(S^3,K)`$, with no requirement to preserve either ambient or knot orientation. There are a $`G`$-invariant knot exterior $`E`$, an invariant flat metric $`h`$ on $`\partial E`$, an invariant longitudinal foliation $`\mathcal J`$, and an invariant smooth metric on $`E`$ that on an invariant inward collar has the exact form

```math
g=dr^2+(1-r)^2h.\qquad\text{(7.1)}
```

The boundary foliation is real analytic in the compatible flat affine atlas; the collar metric is real analytic there. In particular these data lie in the warped-collar scope of equation (2) of the competition paper, with a flat boundary metric.

**Construction.**

1. Average any smooth ambient metric over the finite group. The resulting positive-definite metric is invariant under orientation-preserving and orientation-reversing elements alike. A sufficiently small normal tubular neighborhood of $`K`$, using its normal exponential map for this invariant metric, is invariant. Its complement $`E`$ has invariant torus boundary. Equivariant tubular neighborhoods are the standard input here; the invariant normal exponential construction supplies this one directly.

2. Average any boundary metric to obtain an invariant smooth torus metric $`q`$. Use the convention $`\Delta_q=\mathrm{div}\mathrm{grad}`$. Gauss–Bonnet gives $`\int_{\partial E}K_q\,d\mu_q=0`$. Standard Poisson solvability on a closed connected Riemannian manifold yields a unique smooth solution

   $`\displaystyle \Delta_q u=K_q,\qquad \int_{\partial E}u\,d\mu_q=0.`$

   Each $`g\in G`$ is an isometry of $`q`$, so $`u\circ g`$ solves the same normalized equation. Uniqueness gives $`u\circ g=u`$. The conformal curvature formula

   $`\displaystyle K_{e^{2u}q}=e^{-2u}(K_q-\Delta_q u)`$

   makes $`h=e^{2u}q`$ flat and invariant. This step uses a scalar Poisson equation and its uniqueness, rather than an average of flat metrics. It also applies when a group element reverses the orientation of the torus, because curvature, the Laplacian, and the Riemannian measure have the required isometry naturality.

3. A compact flat torus is $`\mathbb R^2/\Lambda`$, and a torus isometry lifts to an affine Euclidean isometry $`z\mapsto Az+b`$, with $`A\Lambda=\Lambda`$. The preferred longitude is the primitive generator, up to sign, of

   $`\displaystyle \ker\bigl(H_1(\partial E;\mathbb Z)\longrightarrow H_1(E;\mathbb Z)\bigr).`$

   The inclusion commutes with every element of $`G`$, so this rank-one primitive kernel is preserved. If $`\ell\in\Lambda`$ represents its generator, then $`A\ell=\pm\ell`$. The affine isometry consequently preserves the foliation by the images of affine lines parallel to $`\ell`$. Since $`\ell`$ is primitive, these leaves are embedded closed preferred longitudes. Their leaf parameter is a circle, giving a compact smooth family of boundary curves. The Euclidean local charts have analytic affine transition maps; in these charts the foliation is analytic. They define a compatible real-analytic structure on the boundary, and their product collar charts give the analytic local data used in the boundary argument.

4. Average a smooth inward transverse vector field near the boundary. All its summands are inward transverse along the boundary, so their average is also inward transverse; its flow gives an equivariant collar. In these coordinates $`g(r,z)=(r,gz)`$, so $`r`$ is invariant. Prescribe (7.1) on a sufficiently small collar, with its width less than one. Take any invariant interior metric obtained by averaging. An invariant cutoff depending only on $`r`$, equal to one near the boundary and zero before the other end of the collar, blends it with (7.1). A convex combination of two positive-definite forms is positive definite, so the result is a smooth invariant metric retaining the exact smaller collar. The same formula extends to a two-sided collar across the boundary.

5. Its boundary is strictly convex in the competition paper's convention: with inward normal $`\partial_r`$ and $`\mathrm{II}(X,Y)=\langle\nabla_XY,\partial_r\rangle`$, one has $`\mathrm{II}=h`$ at $`r=0`$, and trace mean curvature $`2`$. The paper's Hessian computation is $`\mathrm{Hess}r=-(1-r)h`$ on tangential vectors. These are precisely its equations (2)–(3), §3, equations (2)–(3), printed p. 6 of the competition version. ∎

**Scope of the analytic inputs.** The competition paper states (U), (E), and (Fin) in Theorems 3.1–3.3, printed p. 7, with Remark 3.4 on pp. 7–8. Its recorded hypotheses are compactness, the relevant irreducibility conditions, strictly convex smooth boundary, a compact boundary-curve family, and connected incompressible surfaces with one boundary component on the boundary torus. The construction above preserves those hypotheses and the exact collar. It also supplies the flat analytic longitudinal coordinates; it does not introduce a new invariance assumption into the area-minimization theorems. Here (E) means both the fixed-boundary and sliding-boundary clauses. Its fixed-boundary minimizer retains the membership convention of Definition A.1 and equation (27), printed p. 23. (Fin) means the stated $`C^1`$ compactness for each fixed surface type under an area bound, with finitely many open-and-closed isotopy-class blocks. (U) includes universal disjointness of the minimizers, rather than just existence of a disjoint choice. This spells out the original input statements without adding geometric assumptions.

This is a scope check of the competition paper's stated inputs, **not** an independent reproof of its cited sliding-boundary existence and compactness assertions. In particular, no outstanding issue in those assertions is removed by averaging a metric.

**Conditional corollary E′.** Let $`K`$ be a nontrivial knot and $`G`$ an actual finite smooth symmetry group of $`(S^3,K)`$. For the invariant data above, assume the same external geometric input statements (U), (E), and (Fin) used to establish the competition paper's Theorem A. Use its internal boundary-regularity and exchange arguments within the same warped-collar scope. Then

```math
\lvert IS(K)\rvert^G\text{ is nonempty and contractible in the weak topology.}
```

**Proof.** A diffeomorphism of the pair restricts to one of the invariant exterior. Conjugating ambient isotopies shows that it acts well definedly on isotopy classes. It carries connected orientable incompressible spanning surfaces to such surfaces: any compressing disk for the image pulls back to one for the original. It preserves collections of disjoint representatives, hence vertices and simplices as defined in the competition paper, Definition 4.1, printed p. 8. If orientations are included in the convention, orient the image surface to match the chosen orientation of $`K`$; the sign of the induced action on the knot orientation is multiplicative, so this still defines a group action. No orientation sign affects genus, area, incompressibility, or disjointness.

For a vertex $`v`$, let $`\mathcal F(v)=\{F\in v:\partial F\text{ is a leaf of }\mathcal J\}`$. Each group element gives a bijection $`\mathcal F(v)\to\mathcal F(gv)`$, and is an isometry of the metric, so

```math
\mathrm{genus}(gv)=\mathrm{genus}(v),\qquad
A(gv)=\inf_{F\in\mathcal F(gv)}\mathrm{Area}(F)
=\inf_{F\in\mathcal F(v)}\mathrm{Area}(F)=A(v).
```

Thus $`c(v)=(\mathrm{genus}(v),A(v))`$ is invariant. Its attained values are well ordered under the same (E) and (Fin) input, by Definition 4.7 and Lemma 4.8, printed pp. 10–11. The competition paper's internal arguments give (R1) through Appendix A and the exchange conclusions through Theorem 5.1 and Proposition 5.2, printed p. 13 (the exchange proof continues in §5); these conclusions are not extra axioms in this corollary. The exchange structure and the flag and connectivity properties are those assembled in the proof of Theorem A, §6.1, printed pp. 19–20. Apply Theorem E. This corollary reuses that internal implication from the stated external inputs; this argument does not independently reprove every analytic step of the paper. ∎

A fixed point corresponds to a finite $`G`$-invariant simplex, and hence to a finite invariant collection of isotopy classes admitting disjoint representatives. It does not by itself give an individual $`G`$-invariant embedded surface, nor a simultaneous equivariant realization of that collection. Those stronger conclusions are not asserted. If only a finite subgroup of a mapping class group is given, an additional realization theorem is needed before the averaging construction can be used.

