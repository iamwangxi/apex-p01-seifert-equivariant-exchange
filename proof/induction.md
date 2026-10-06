# Transfinite proof of Theorem E

This proof uses [Lemmas 2.1–3.1](theorem-e.md) and [the fixed-point model and topological tools](fixed-point-model.md). The [Seifert application](seifert-application.md) is conditional on the geometric inputs stated there.

## 6. Proof of Theorem E by universal transfinite induction

Replace the codomain by the attained values and identify this well order with its ordinal order type $`\kappa`$. This operation preserves all equalities of values, the group action, and (N2). It does not refine the fibers.

For each ordinal $`\eta\geq1`$, prove the following **universal** statement: for every exchange complex whose attained complexity order has type at most $`\eta`$, and every finite complexity-preserving group action, its weak geometric fixed space is nonempty and contractible. Universality is necessary because a descending common link is not generally a sublevel of the original complex.

### Base: order type one

Lemma 2.3 makes $`X`$ an infinite or finite clique complex. The invariant orbit barycenter and the equivariant affine contraction following that lemma give the statement.

### Successor: order type $`\beta+1`$, with $`\beta\geq1`$

Assume the universal statement for types at most $`\beta`$. Let the largest value be $`\alpha=\beta`$, let $`A=X_{<\alpha}`$, and put

```math
P=P_G(X),\qquad
Q=\{\tau\in P:\tau\cap A^{(0)}\ne\varnothing\}.
```

By Lemma 2.2, $`A`$ is an exchange complex with restricted $`G`$-action and order type $`\beta`$. Thus $`\lvert\Delta P_G(A)\rvert`$ is nonempty and contractible by induction and (4.1).

The map

```math
r:Q\longrightarrow P_G(A),\qquad r(\tau)=\tau\cap A^{(0)}
```

is well defined and order preserving. The inclusion $`j:P_G(A)\to Q`$ satisfies $`rj=\mathrm{id}`$ and $`jr\leq\mathrm{id}_Q`$. Therefore $`\lvert\Delta Q\rvert`$ is nonempty and contractible.

We apply the upper-fiber lemma to $`i:Q\hookrightarrow P`$. Fix $`\sigma\in P`$; its fiber is

```math
Q_{\geq\sigma}=\{\tau\in Q:\sigma\subseteq\tau\}.
```

If $`\sigma\in Q`$, it is the least element of this fiber, so the fiber has contractible realization. Otherwise every vertex of $`\sigma`$ has value $`\alpha`$. It is a nonempty finite $`G`$-invariant face in the top layer. Define

```math
R_\sigma=\{\sigma\cup\rho:\rho\in P_G(L_\alpha(\sigma))\}.
```

For $`\tau\in Q_{\geq\sigma}`$, the nonempty face $`\rho=\tau\cap A^{(0)}`$ lies in the common link: its vertices are lower, and all are adjacent to all vertices of $`\sigma`$, because they occur in the face $`\tau`$. Its invariance follows from invariance of $`\tau`$ and $`A`$. Hence

```math
q_\sigma(\tau)=\sigma\cup(\tau\cap A^{(0)})\in R_\sigma
```

is a well-defined order-preserving retraction and $`q_\sigma(\tau)\subseteq\tau`$. The possibility that $`\tau`$ contains extra top-layer vertices causes no difficulty: the map explicitly removes them. The inverse order isomorphisms

```math
P_G(L_\alpha(\sigma))\ \leftrightarrow\ R_\sigma,
\qquad \rho\mapsto\sigma\cup\rho,\quad \theta\mapsto\theta\setminus\sigma
```

are valid because lower vertices are disjoint from $`\sigma`$, and flagness makes any lower common-link face together with $`\sigma`$ a face of $`X`$.

By Lemma 3.1 this common link is a nonempty exchange complex. Since $`\sigma`$ is $`G`$-invariant, its stabilizer is all of $`G`$. Its attained values form a subset of $`\beta`$, hence have order type at most $`\beta`$. The universal induction hypothesis gives contractibility of $`\lvert\Delta P_G(L_\alpha(\sigma))\rvert`$. Therefore $`\lvert\Delta Q_{\geq\sigma}\rvert`$ is nonempty and contractible.

All upper fibers have now been checked. The fiber lemma gives $`\lvert\Delta Q\rvert\simeq\lvert\Delta P\rvert`$, and (4.1) gives nonempty contractibility of $`\lvert X\rvert^G`$.

### Limit: order type $`\lambda`$, with $`\lambda`$ a nonzero limit ordinal

Assume the universal statement for every smaller order type. Write $`X_\gamma=X_{<\gamma}`$, for $`0<\gamma<\lambda`$. Each $`X_\gamma`$ is a nonempty exchange complex by Lemma 2.2 and its fixed space is contractible by induction. Its invariant-face order complex is a subcomplex of that for $`X`$.

Let $`F\subseteq\Delta P_G(X)`$ be a finite subcomplex. Its finitely many vertices represent finitely many finite faces of $`X`$. The union of their vertex supports is finite. Since $`\lambda`$ is a limit, choose $`0<\gamma<\lambda`$ strictly larger than every value in this union. Then

```math
F\subseteq\Delta P_G(X_\gamma).
```

The inclusion of $`F`$ into $`\Delta P_G(X)`$ is nullhomotopic by the contraction of the intermediate stage. There is also a fixed point in the minimum layer. Apply Lemma 5.1 to $`Z=\lvert\Delta P_G(X)\rvert`$, and then (4.1). This proves the limit statement in the weak topology, including uncountable order types and non-locally-finite complexes.

The cases of smaller order type at a successor or a limit are already included in the previous induction hypotheses. Transfinite induction therefore proves Theorem E. ∎

**Dependency ledger.** Section 2 uses the well order, graph connectedness, and (N2). Section 3 additionally uses the full apex property and flagness. Section 4 uses finite-face barycentric subdivision, weak CW topology, and the explicitly stated poset fiber theorem. Section 5 uses compact containment in a finite CW subcomplex and cellwise extension. Section 6 uses finite-group orbit barycenters only for the nonempty minimum-layer base; it never assumes that a top face has a fixed vertex or that its common link has a fixed vertex.

