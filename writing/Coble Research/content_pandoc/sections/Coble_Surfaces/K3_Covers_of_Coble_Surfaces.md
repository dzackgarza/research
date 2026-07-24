# K3 covers

::: {.remark ref="rmk:k3-cover-invariants" title="On relation to K3s"}

Let $\cL \da \OO_S(-K_S) \in \Pic(S)$; By [@DK25 Prop. 9.1.1], taking a section $s\in H^0(\cL ^{\tensor 2})$ with $Z(s) = C$ yields a branched double cover $f: X\to S$ where $X$ is a smooth K3 surface.
Let $\sigma$ be the involution generating the deck transformations of this cover.
Then the fixed locus $\mathrm{Fix}(\sigma)$ is a union of $n$ smooth rational curves which are precisely $f^{-1}(C_i)$ where $C_i$ are the irreducible components of $C$ in $S$.
By [@CDL25 Def. 5.4.3], the preimages $f^{-1}(C_i)$ are disjoint $(-2)$-curves and $\Pic(X)$ is a 2-elementary lattice with invariants of the form
$$
(r,a,\delta)_1 = (10+n, 12-n, \delta)_1
.
$$
By [@CDL25 Def. 5.4.3, Eqn. 5.3.1], the ramification divisor $R$ is explicitly of one of the following forms:

1. $R=\emptyset$ if $(r,a,\delta) = (10, 10, 0)$,

2. $R$ is a sum of two elliptic curves if $(r,a,\delta) = (10, 8, 0)$,

3. $R$ is the sum of a single rational curve and $n-1$ other disjoint $(-2)$-curves otherwise.

It is also known that $\delta=1$ unless $n=8$, c.f. [@CDL25 Table 5.1]. Thus if $S$ is a terminal Coble surface of K3 type with $n=1$, the ramification locus of the K3 cover is a single smooth rational curve, and we obtain a lattice with invariants
$$
S_{\Co} \da (11, 11, 1)_1 \cong \gens{-2} \oplus E_{10}(2)
$$
with orthogonal complement
$$
T_{\Co} \da S_{\Co}^{\perp \lkt} = (11, 11, 1)_2 \cong \latI_{2, 9}(2) \cong \gens{2} \oplus E_{10}(2)
.
$$
The lattices $S_{\Co}$ and $T_{\Co}$ will be of fundamental importance in constructing the Hodge-theoretic period domain for Coble surfaces, yielding a coarse space for the corresponding moduli space; the identifications above are derived in the section on period domains.
:::

::: {.proposition ref="prop:coble-invariant-lattice"}

Let $f: X\to S$ be the K3 double cover of a terminal Coble surface of K3 type with $n = 1$, and let $\sigma$ be the covering involution.
Write $\Pic(S) = \gens{H, E_1, \ldots, E_{10}} \cong \latI_{1, 10}$, where $H$ is the pullback of a line and the $E_i$ are the exceptional curves of $S = \Bl_{p_1, \ldots, p_{10}} \PP^2$, so that $H^2 = 1$, $E_i^2 = -1$, and $H\cdot E_i = E_i\cdot E_j = 0$ for $i\neq j$.
Then $f^*: \Pic(S)\to \Pic(X)$ is injective, its image
$$
S_\Co \da f^*\Pic(S) = \gens{f^*H, f^*E_1, \ldots, f^*E_{10}}
$$
is the invariant lattice $H^2(X, \bZ)^\sigma$, and
$$
S_\Co \cong \gens{2}\oplus\gens{-2}^{10} = \latI_{1, 10}(2) = (11, 11, 1)_1
.
$$
:::

::: {.proof}

**Injectivity and the twist by $2$.** If $f^*D = 0$ then $2D = f_* f^* D = 0$, and $\Pic(S)\cong\latI_{1, 10}$ is torsion-free, so $D = 0$; thus $f^*$ is injective.
As $f$ has degree $2$, one has $f_* f^* = 2$, and the projection formula gives, for all $D, D'\in\Pic(S)$,
$$
\qty(f^*D \cdot f^*D') = D \cdot f_* f^* D' = D\cdot 2D' = 2\qty(D\cdot D')
.
$$
Applied to the orthogonal basis $H, E_1, \ldots, E_{10}$, this shows that $f^*H, f^*E_1, \ldots, f^*E_{10}$ have Gram matrix $\operatorname{diag}(2, -2, \ldots, -2)$, so that $S_\Co \cong \gens{2}\oplus\gens{-2}^{10} = \latI_{1, 10}(2)$, of signature $(1, 10)$.
This recovers, by the projection formula, the twist-by-$2$ described geometrically in \cref{rmk:k3-cover-twist}.

**Rank of the invariant lattice via Lefschetz.** The lattice $S_\Co$ is $\sigma$-invariant, so $S_\Co\subseteq H^2(X, \bZ)^\sigma$.
The fixed locus $\mathrm{Fix}(\sigma) = R$ is a single smooth rational curve (the case $n = 1$), so $\chi(R) = 2$.
On the K3 surface $X$, both $H^0$ and $H^4$ are $\sigma$-invariant of rank $1$ and $H^1 = H^3 = 0$, so the topological Lefschetz fixed-point formula reads
$$
\chi(R) = \sum_i (-1)^i \operatorname{tr}\qty(\sigma^* \mid H^i(X, \bZ)) = 2 + \operatorname{tr}\qty(\sigma^* \mid H^2(X, \bZ))
.
$$
Since $\chi(R) = 2$, we obtain $\operatorname{tr}(\sigma^* \mid H^2(X, \bZ)) = 0$.
As $H^2(X, \bZ)$ has rank $22$ and $\sigma^*$ is an involution, the invariant lattice has rank $\tfrac{1}{2}(22 + 0) = 11$ and the coinvariant lattice rank $\tfrac{1}{2}(22 - 0) = 11$, so that $11 + 11 = 22$; cf.
\cref{prop:involution_eigenspaces}. Hence $S_\Co$, of rank $11$, is a finite-index sublattice of $H^2(X, \bZ)^\sigma$.

**The Nikulin invariants and equality.** The lattice $S_\Co \cong \gens{2}\oplus\gens{-2}^{10}$ has
$$
\abs{\det S_\Co} = 2\cdot 2^{10} = 2^{11},
\qquad
A_{S_\Co} \cong (\bZ/2\bZ)^{11},
\qquad
q_{S_\Co} \cong \gens{\tfrac{1}{2}}\oplus\gens{-\tfrac{1}{2}}^{10}
,
$$
so $S_\Co$ is $2$-elementary of rank $r = 11$ and length $a = 11$.
Because $q_{S_\Co}$ takes the value $\tfrac{1}{2}\notin\bZ$, one has $\delta = 1$, giving $(r, a, \delta) = (11, 11, 1)$.
For a nonsymplectic involution whose fixed locus is a single rational curve, the fixed-locus formula assigns the invariant lattice these same invariants $(r, a, \delta) = (11, 11, 1)$ [@CDL25 Def. 5.4.3, Eqn. 5.3.1], so $\abs{\det H^2(X, \bZ)^\sigma} = 2^{11}$.
Since $S_\Co \subseteq H^2(X, \bZ)^\sigma$ have equal rank $11$ and equal absolute determinant $2^{11}$, the index $[H^2(X, \bZ)^\sigma : S_\Co]$ is $1$: the two coincide, and by \cref{prop:invariant_coinvariant_primitive} the invariant lattice -- hence $S_\Co$ -- is primitive in $H^2(X, \bZ)$.
That the invariants $(11, 11, 1)_1$ determine the isometry class $\gens{2}\oplus\gens{-2}^{10}\cong\gens{-2}\oplus E_{10}(2)$ is Nikulin's classification of indefinite even $2$-elementary lattices [@Nik80]. This derivation makes explicit the invariants stated by citation in \cref{rmk:k3-cover-invariants}.
:::

::: {.remark ref="rmk:k3-cover-twist"}

Following [@CD12], we note that this computation is a special case of a general construction.
Let $S$ be any basic rational surface and write $S$ as the blowup of $\PP^2$ at $N$ points $p_1,\cdots, p_N$ with $N\geq 9$.
It is a fact that $\Pic(S) \cong \latI_{1, N}$, since one can construct a **geometric basis** in the following way: let $e_0$ be the class of the total transform of a hyperplane class in $\PP^2$ and for $1\leq i\leq N$, let $e_i$ be the class of the total transform of the exceptional divisor over $p_i$.
Then $\Pic(S) = \gens{e_0,e_1,\cdots, e_N}$ and $\rho(X) = N+1$; one verifies that $e_0^2 = 1$, and for $i\geq 1$, that $e_i^2 = -1$.
Moreover $e_ie_j = 0$ for $i\neq j$, making this an orthogonal basis with respect to the intersection pairing, yielding $\latI_{1, N}$.
In the case of Coble surfaces, the effect of taking the K3 double cover is to twist this lattice by 2, yielding $\Pic(X) = \latI_{1, N}(2)$, generated by preimages of the $e_i$.
We remark that
$$
K_S = -3e_0 + e_1 + \cdots + e_N
.
$$
:::
