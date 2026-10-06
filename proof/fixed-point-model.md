# Fixed-point model and topological tools

Continue from [Theorem E and common links](theorem-e.md). These tools are used in [the transfinite induction](induction.md).

## 4. A topologically exact model of the fixed space

For a complex $`Y`$ with a $`G`$-action, write

```math
P_G(Y)=\{\tau:\tau\text{ is a nonempty finite face of }Y,\ g\tau=\tau\text{ for every }g\in G\},
```

ordered by inclusion. Its order complex has as simplices the nonempty finite strict chains. Then there is a canonical homeomorphism

```math
\lvert\Delta P_G(Y)\rvert\ \cong\ \lvert Y\rvert^G.\qquad\text{(4.1)}
```

**Proof, including topology.** The usual subdivision map sends the vertex corresponding to $`\tau`$ to its barycenter and is affine on each chain simplex. It is a $`G`$-equivariant homeomorphism $`\lvert\mathrm{sd}Y\rvert\to\lvert Y\rvert`$ for weak realizations: on each finite original simplex it is the usual finite subdivision homeomorphism, and the two weak topologies glue these maps and their inverses.

A point in $`\lvert\mathrm{sd}Y\rvert`$ lies in the relative interior of a unique finite chain simplex. If it is fixed, this chain is preserved setwise by $`G`$. The cardinalities of its faces strictly increase, so no element of $`G`$ can permute different members of the chain. Each face in the chain is therefore invariant. Conversely the barycenter of an invariant face is fixed, so every chain of invariant faces is fixed pointwise in the subdivided realization. The fixed set is consequently the realization of the indicated subcomplex of $`\mathrm{sd}Y`$.

The subspace topology on a CW subcomplex agrees with its own weak CW topology. Thus the preceding set equality is a homeomorphism, not just a bijection. No compactness or local finiteness was used. ∎

We will also use two precise topological tools.

**Poset homotopies.** If order-preserving maps $`f,g:A\to B`$ satisfy $`f(a)\leq g(a)`$ for every $`a`$, their realization maps are homotopic. This is the nerve homotopy of the pointwise natural transformation; equivalently it is defined by the standard prism subdivision. In particular, a retraction $`r:A\to B\subseteq A`$ with $`r(a)\leq a`$ gives a homotopy equivalence of realizations.

**Upper-fiber lemma (the poset form of Quillen's Theorem A, proved here).** Let $`f:A\to B`$ be order preserving between set-sized posets. If for every $`b\in B`$ the order complex of

```math
\{a\in A:b\leq f(a)\}
```

is nonempty and contractible, then $`\lvert\Delta f\rvert`$ is a homotopy equivalence. This is the upper-comma-category version. It applies to arbitrary posets, not only finite or locally finite ones. Realizations here are weak CW realizations of order complexes.

**Direct proof.** We first record an elementary carrier construction. Suppose each nonempty simplex $`s`$ of a complex is assigned a nonempty contractible subspace $`C_s`$ of a target, and $`C_t\subseteq C_s`$ whenever $`t`$ is a face of $`s`$. Choose an image point for each vertex in its carrier. Inductively extend across each simplex: its boundary is already mapped into $`C_s`$, and contractibility of $`C_s`$ supplies the extension. Weak topology gives a continuous map on the whole realization. Moreover, any two maps carried in this manner are homotopic through carried maps: on the boundary of each simplex prism, the previously defined side homotopy and the two end maps lie in $`C_s`$, so contractibility supplies the prism extension. The CW product theorem for the interval gives continuity. Both statements work without local finiteness.

Write $`F_b=\{a\in A:b\leq f(a)\}`$. For a chain $`s=(b_0<\cdots<b_k)`$ of $`B`$, use the carrier $`C_s=\lvert\Delta F_{b_0}\rvert`$ in $`\lvert\Delta A\rvert`$. If a face omits $`b_0`$, its new minimum is larger, and its carrier is a subspace of $`C_s`$; the other faces have the same carrier. The construction gives a map $`u:\lvert\Delta B\rvert\to\lvert\Delta A\rvert`$ carried by these contractible fibers.

For a chain $`s=(b_0<\cdots<b_k)`$, both $`\lvert\Delta f\rvert u`$ and the identity are carried by $`\lvert\Delta B_{\geq b_0}\rvert`$, a cone with least vertex $`b_0`$. The homotopy part of the construction yields $`\lvert\Delta f\rvert u\simeq\mathrm{id}`$.

For a chain $`t=(a_0<\cdots<a_k)`$ of $`A`$, the image chain under $`f`$, with repetitions removed, has minimum $`f(a_0)`$. Thus both $`u\lvert\Delta f\rvert`$ and the identity are carried by $`\lvert\Delta F_{f(a_0)}\rvert`$. These carriers are contractible by hypothesis and are nested on faces, since $`f`$ is order preserving. The same construction yields $`u\lvert\Delta f\rvert\simeq\mathrm{id}`$. This proves the asserted homotopy equivalence directly. ∎

## 5. The infinite-limit tool without a Whitehead invocation

We use the standard CW fact that every compact subset is contained in a finite subcomplex. This is the compactness fact used in the competition paper, §2, printed p. 6 of the competition version. The following implication replaces its separate Whitehead step.

**Lemma 5.1 (finite inclusions suffice).** Let $`Z`$ be a nonempty CW complex. If the inclusion of every finite subcomplex $`F\subseteq Z`$ is nullhomotopic in $`Z`$, then $`Z`$ is contractible.

**Proof.** Every map $`S^n\to Z`$, $`n\geq0`$, has compact image in a finite subcomplex, so it is nullhomotopic. In particular, all points of $`Z`$ can be joined by paths, by applying this to maps of $`S^0`$.

Choose a vertex $`z_0`$. Define a prospective contraction to equal the identity on $`Z\times\{0\}`$, the constant $`z_0`$ on $`Z\times\{1\}`$, and $`z_0`$ on $`\{z_0\}\times[0,1]`$. For each other zero-cell choose a path to $`z_0`$. Inductively suppose it is defined on $`Z^{(n-1)}\times[0,1]`$, with the prescribed end maps on all of $`Z`$. For each characteristic $`n`$-disk, the existing map on the boundary of its prism $`D^n\times[0,1]`$ is a continuous map $`S^n\to Z`$. It is nullhomotopic by the first paragraph, hence extends across the prism. Choose an extension for each cell. These extensions agree on the prescribed boundaries. They define a continuous map on $`Z\times[0,1]`$ by the weak CW topology and the CW product theorem for the interval. This is a contraction, fixing $`z_0`$. ∎

This does not require compatible contractions of the different finite subcomplexes. Compatibility is supplied by the prism extension argument. No formalization of this fixed-point theorem is claimed.

