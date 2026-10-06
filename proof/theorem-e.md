# Theorem E and descending common links

The notation and Lemmas 2.1–3.1 below are used in [the fixed-point model](fixed-point-model.md) and [the induction](induction.md).

## 1. Statement and conventions

Let $`X`$ be a nonempty connected flag simplicial complex, with an arbitrary set of vertices. All simplices are finite. Write $`N(v)`$ for the open graph neighborhood and $`N[v]=N(v)\cup\{v\}`$ for the closed neighborhood. When $`d(u,w)=2`$, put

```math
I(u,w)=N(u)\cap N(w).
```

An **apex** is a vertex $`x\in I(u,w)`$ such that $`I(u,w)\subseteq N[x]`$. Let $`c:X^{(0)}\to W`$, where $`W`$ is well ordered, satisfy

```math
\text{(N2)}\qquad d(u,w)=2\Longrightarrow
\text{there exists an apex }x\text{ with }c(x)<\max\{c(u),c(w)\}.
```

This also supplies (N1), the existence of an apex without the inequality. These are precisely the competition paper's conventions: Definition 2.1, printed pp. 3–4 of the competition version. In particular, neither all apices nor the selected witnesses are required to have the inequality, and no global selection map is assumed.

**Theorem E.** If a finite group $`G`$ acts on $`X`$ by simplicial automorphisms and $`c(gv)=c(v)`$, then the geometric fixed-point space $`\lvert X\rvert^G`$, with the subspace topology of the weak realization, is nonempty and contractible.

There is no local-finiteness, finite-dimensionality, finite-fiber, or countability assumption. The complexity need not be injective. We will not break ties equivariantly.

For an initial segment $`D\subseteq W`$, let $`X_D`$ denote the full subcomplex on the vertices with value in $`D`$. Strict and non-strict sublevels have the corresponding notation. The common link of a nonempty face $`\sigma`$ means the full subcomplex on vertices outside $`\sigma`$ adjacent to every vertex of $`\sigma`$.

## 2. Sublevels without breaking ties

**Lemma 2.1 (sublevel geodesics).** If $`p,q\in X^{(0)}`$, there is a geodesic from $`p`$ to $`q`$ every vertex of which has complexity at most $`\max\{c(p),c(q)\}`$. Consequently every nonempty initial sublevel is connected and isometrically embedded in the graph of $`X`$.

**Proof.** Let $`n=d(p,q)`$. The cases $`n\leq1`$ are immediate. For each geodesic of length $`n\geq2`$, sort its $`n-1`$ interior complexities into a nonincreasing tuple. The set of attained tuples has a least element in lexicographic order: a finite lexicographic product of well orders is well ordered, and the attained tuples form a subset of that product. Choose a geodesic with least tuple.

If an interior vertex $`v_i`$ has maximum interior complexity $`M>\max\{c(p),c(q)\}`$, its neighbors $`v_{i-1},v_{i+1}`$ have complexity at most $`M`$. They are distinct and nonadjacent, since otherwise the geodesic would shorten. Thus they are at distance two. Axiom (N2) supplies an apex $`x`$ with

```math
c(x)<\max\{c(v_{i-1}),c(v_{i+1})\}\leq M.
```

Replacing $`v_i`$ by $`x`$ gives a walk of length $`n`$. It is a geodesic: a repeated vertex or a shortcut would contradict $`d(p,q)=n`$. Its sorted interior tuple is strictly smaller, because one occurrence of $`M`$ has been replaced by a value below $`M`$, while all other entries are unchanged. This is a contradiction even when several interior vertices have value $`M`$. Hence the chosen geodesic has the claimed bound. An initial sublevel containing its endpoints contains the whole geodesic. ∎

**Lemma 2.2 (sublevel heredity).** Every nonempty initial sublevel, with the restricted complexity, is an exchange complex. If the initial segment is $`G`$-invariant in the evident sense, the restricted group action preserves its complexity.

**Proof.** Fullness gives flagness, and Lemma 2.1 gives connectedness. If vertices of the sublevel are at distance two there, they are nonadjacent in $`X`$, and their common neighbor in the sublevel shows that their distance in $`X`$ is two. The apex supplied by (N2) lies in the sublevel by downward closure, and it is an apex of its smaller two-interval. The group statement follows from $`c(gv)=c(v)`$. ∎

**Lemma 2.3 (minimum layer).** The vertices of minimum attained complexity form a clique, possibly infinite.

**Proof.** This sublevel is nonempty and connected by Lemma 2.1. If two vertices in it were nonadjacent, an initial three-vertex segment of a geodesic in that sublevel would have endpoints at distance two in $`X`$. Axiom (N2) would give a vertex below the minimum attained value, a contradiction. ∎

The minimum layer therefore spans the complex of all finite subsets of its vertices. A finite group orbit in it is a finite invariant simplex; its barycenter is fixed. Indeed the fixed space of this entire layer is contractible: if $`b`$ is that barycenter, the affine homotopy

```math
H(z,t)=(1-t)z+tb
```

stays in the layer and is $`G`$-equivariant. Each support is contained in a finite simplex. The homotopy is continuous for the weak topology, as checked on the closed-simplex prisms; the product of a CW complex with the finite CW interval has this CW product topology. This argument does not treat an infinite clique as an infinite-dimensional *closed simplex*.

## 3. Strictly descending common links

**Lemma 3.1.** Let $`\alpha`$ be a nonminimum attained value, and let $`\sigma=\{v_1,\ldots,v_k\}`$ be a nonempty finite face all of whose vertices have complexity $`\alpha`$. Set

```math
L_\alpha(\sigma)=X_{<\alpha}\cap\bigcap_{v\in\sigma}\mathrm{lk}_X(v),
```

interpreted as the full complex on the strictly lower common neighbors. Then:

1. $`L_\alpha(\sigma)`$ is nonempty;
2. its graph has diameter at most two and it is an exchange complex;
3. the setwise stabilizer $`\mathrm{Stab}_G(\sigma)`$ acts on it and preserves the restricted complexity.

**Proof of nonemptiness.** First any vertex $`v`$ of value $`\alpha`$ has a strictly lower neighbor. Choose $`p`$ below $`\alpha`$ and a geodesic $`v=v_0,v_1,\ldots,v_n=p`$ bounded above by $`\alpha`$, using Lemma 2.1. If $`n=1`$, use $`p`$. If $`n\geq2`$, the vertices $`v_0,v_2`$ are at distance two and (N2) supplies a common neighbor $`a`$ with

```math
c(a)<\max\{c(v_0),c(v_2)\}=\alpha.
```

Thus $`a`$ is a lower neighbor of $`v_0`$. Notice that the first vertex of the original geodesic could have value $`\alpha`$; we have not silently replaced a non-strict bound by a strict one.

Start with a lower neighbor $`a`$ of $`v_1`$, and suppose it is adjacent to $`v_1,\ldots,v_j`$, with $`j<k`$. If it is adjacent to $`v_{j+1}`$, keep it. Otherwise $`a`$ and $`v_{j+1}`$ are at distance two, witnessed by $`v_1`$, since $`\sigma`$ is a clique. Choose an apex $`x`$ of their two-interval with

```math
c(x)<\max\{c(a),c(v_{j+1})\}=\alpha.
```

Every $`v_i`$, $`i\leq j`$, belongs to that two-interval. The apex property makes $`x`$ equal or adjacent to each such $`v_i`$; equality is excluded by their complexity $`\alpha`$. Also $`x`$ is adjacent to $`v_{j+1}`$. Replace $`a`$ by $`x`$. After finitely many steps this gives a lower common neighbor of all of $`\sigma`$.

**Proof of heredity and connectedness.** Let $`a,b`$ be nonadjacent vertices of $`L_\alpha(\sigma)`$. Any $`v\in\sigma`$ witnesses $`d_X(a,b)=2`$. Axiom (N2) supplies an apex $`x`$ with

```math
c(x)<\max\{c(a),c(b)\}<\alpha.
```

Every vertex of $`\sigma`$ belongs to $`I_X(a,b)`$, so $`x`$ is adjacent to all of them: equality is again impossible. Thus $`x\in L_\alpha(\sigma)`$, and $`a,x,b`$ is a path inside the common link. This proves diameter at most two and connectedness. Its two-interval is a subset of $`I_X(a,b)`$, so the same $`x`$ is an apex of the smaller interval and has the required inequality. Fullness gives flagness. Finally any group element preserving $`\sigma`$ setwise preserves the common link and the strict sublevel. ∎

Only (N2), the full apex property, flagness, connectedness, and the well order have been used. Replacing “apex” by “an arbitrary common neighbor” would not justify this lemma.

