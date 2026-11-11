# K3 covers

::: {.proposition #prop:nikulin-fixed-locus title="Fixed locus of an involution acting as $-1$ on the transcendental lattice"}

Let $X$ be a complex algebraic K3 surface and let $\sigma$ be an involution of $X$ that acts as $-\id$ on the transcendental lattice $T(X)$.
Then $M\definedas\Pic(X)^{\sigma^*}$ is a $2$-elementary lattice that contains an ample divisor class [@CDL25, Lemma 5.3.3].
Let $(r,a,\delta)$ be its invariants, with $a$ as in @def:p-elementary.
The fixed locus of $\sigma$ is
$$
X^{\sigma}=\left\{\begin{array}{ll}
\emptyset & \text { if }(r, a, \delta)=\EnriquesInvariants, \\
C_{1}^{(1)}+C_{2}^{(1)} & \text { if }(r, a, \delta)=(10,8,0), \\
C^{(g)}+\Sum_{i=1}^{k} R_{i} & \text { otherwise, }
\end{array}\right.
$$
where $C^{(g)}$ is a curve of genus $g \geq 0$, the $R_{i}$ are disjoint $(-2)$-curves, and
$$
g=\frac{1}{2}(22-r-a), \qquad k=\frac{1}{2}(r-a)
$$
[@CDL25, (5.3.1)].

:::

::: {.proposition #prop:coble-k3-cover title="The K3 cover of a terminal Coble surface"}

Let $S$ be a terminal Coble surface of K3 type over $\CC$, with $\abs{-2K_S} = \theset{C}$ and $C = C_1+\cdots+C_n$, where $C_1,\dots,C_n$ are disjoint $(-4)$-curves.
Let $\mcl \definedas \OO_S(-K_S)$, let $s\in H^0(S, \mcl^{\tensor_{\OO_S} 2})$ have $Z(s) = C$, and let $f\colon X\to S$ be the double cover defined by $(\mcl, s)$.
Let $\sigma$ be the covering involution of $f$.

1. $X$ is a K3 surface, and the ramification divisor of $f$ is the disjoint union of $n$ smooth rational curves [@DK25, Prop. 9.1.1 and its proof].
2. $e(S) = 12+n$ and $\rho(S) = 10+n$ [@DK25, §9.1].
3. The preimages $\bar C_i$ of the curves $C_i$ are disjoint $(-2)$-curves on $X$ [@CDL25, §5.4, p. 552].
4. $S$ is the blowup of $\PP^2$ at $N\geq 10$ points, possibly infinitely near, and $K_S^2 = 9-N = -n$ [@CDL25, §5.4, (5.4.1)].
5. The sublattice $M\definedas\Pic(X)_0$ of $\Pic(X)$ spanned by $f^*\Pic(S)\cong\latI_{1,N}(2)$ and the classes of the $\bar C_i$ is $2$-elementary, it contains $f^*\Pic(S)$ with finite index, and $a(M) = a(\latI_{1,N}(2)) - 2(n-1) = 21-N = 12-n$ [@CDL25, §5.4, p. 552].
6. For a general such $S$, the ramification divisor of $f$ is as in @prop:nikulin-fixed-locus with $g = 0$ and $k = n-1$, and $\Pic(X)$ is a $2$-elementary lattice of rank $10+n$ with $a(\Pic(X)) = 12-n$ [@CDL25, §5.4, p. 552].

:::

::: {.corollary #cor:coble-k3-cover-lattice-chain title="The lattices of the K3 cover of a Coble surface"}

In the setting of @prop:coble-k3-cover,
$$
f^*\Pic(S) \;\cong\; \latI_{1, N}(2) \;\iscontainedin\; M \;=\; \Pic(X)_0 \;\iscontainedin\; \Pic(X),
$$
the lattices $f^*\Pic(S)$ and $M$ have rank $10+n$, and $\rank\Pic(X)\geq 10+n$.
The first inclusion is an equality if and only if $n=1$.
For a general $S$ the second inclusion is an equality.

:::

::: {.proof}

By @prop:blowup-geometric-basis (3), $f^*$ is injective with image $f^*\Pic(S)\cong\latI_{1,N}(2)$.
By @prop:coble-k3-cover (2), $\rank\Pic(S) = \rho(S) = 10+n$, so $\rank f^*\Pic(S) = 10+n$.
By @prop:coble-k3-cover (5), $f^*\Pic(S)$ has finite index in $M$, so $\rank M = 10+n$.
Since $\latI_{1,N}$ is unimodular, @prop:scaled-discriminant-ses gives $A_{\latI_{1,N}(2)}\cong(\bZ/2)^{N+1}$, so $\abs{\det f^*\Pic(S)} = 2^{N+1}$.
By @prop:coble-k3-cover (5), $M$ is $2$-elementary with $a(M) = 21-N$, so $\abs{\det M} = 2^{21-N}$.
The square of the index $[M : f^*\Pic(S)]$ is the quotient of these determinants, $2^{N+1}/2^{21-N} = 2^{2N-20} = 2^{2(n-1)}$, where $N = 9+n$ by @prop:coble-k3-cover (4).
So $[M : f^*\Pic(S)] = 2^{n-1}$, which is $1$ if and only if $n = 1$.
Since $M\iscontainedin\Pic(X)$, $\rank\Pic(X)\geq 10+n$.
For a general $S$, $\Pic(X)$ has rank $10+n$ and $a(\Pic(X)) = 12-n = a(M)$ by @prop:coble-k3-cover (5) and (6).
Both lattices are $2$-elementary, so $\abs{\det\Pic(X)} = 2^{12-n} = \abs{\det M}$, and the index $[\Pic(X):M]$, whose square is $\abs{\det M}/\abs{\det\Pic(X)}$, is $1$.

:::

::: {.proposition #prop:double-cover-is-k3 title="The branched double cover is a K3 surface"}

Let $S$ be a smooth rational surface, let $\mcl\definedas\OO_S(-K_S)$, and let $s\in H^0(S, \mcl^{\tensor_{\OO_S} 2})$ have smooth divisor $B\in\abs{-2K_S}$.
Let
$$
\pi\colon X \definedas \Spec_S\bigl(\OO_S\oplus\inverseof{\mcl}\bigr)\to S
$$
be the double cover determined by $s$, branched along $B$.
Then $X$ is a K3 surface, and for divisors $D, D'$ on $S$,
$$
\pi^{*}D\cdot\pi^{*}D' = 2\,(D\cdot D')
.
$$
:::

::: {.proof}

The canonical bundle formula for a cyclic double cover branched along $B\in\abs{\mcl^{\tensor_{\OO_S} 2}}$ gives
$$
K_X = \pi^{*}(K_S + \mcl) = \pi^{*}(K_S - K_S) = 0
,
$$
so $\omega_X\cong\OO_X$.
Pushing forward, $\pi_*\OO_X = \OO_S\oplus\inverseof{\mcl} = \OO_S\oplus\OO_S(K_S)$, and $\pi$ is finite, so
$$
H^i(X, \OO_X) = H^i(S, \OO_S)\oplus H^i(S, K_S)
\qquad\text{for all } i
.
$$
Since $S$ is rational, $h^1(\OO_S) = 0$, and Serre duality on the surface $S$ gives $h^1(K_S) = h^1(\OO_S) = 0$; hence $h^1(\OO_X) = 0$.
Again by Serre duality $\chi(K_S) = \chi(\OO_S) = 1$, so
$$
\chi(\OO_X) = \chi(\OO_S) + \chi(K_S) = 2
,
$$
and combining $\chi(\OO_X) = 1 - h^1(\OO_X) + h^2(\OO_X)$ with $h^1(\OO_X) = 0$ gives $p_g(X) = h^2(\OO_X) = 1$.
A smooth projective surface with $\omega_X\cong\OO_X$ and $h^1(\OO_X) = 0$ is a K3 surface, which is the first claim.

For the intersection numbers, $\pi$ is finite of degree $2$, so $\pi_*\pi^{*} = 2$ on divisor classes, and the projection formula gives
$$
\pi^{*}D\cdot\pi^{*}D' = D\cdot\pi_*\pi^{*}D' = D\cdot 2D' = 2(D\cdot D')
.
$$
:::

::: {.proposition #prop:coble-invariant-lattice}

Let $f: X\to S$ be the K3 double cover of a terminal Coble surface of K3 type with $n = 1$, and let $\sigma$ be the covering involution.
Write $\Pic(S) = \generators{H, E_1, \ldots, E_{10}} \cong \latI_{1, 10}$, where $H$ is the pullback of a line and the $E_i$ are the exceptional curves of $S = \Bl_{p_1, \ldots, p_{10}} \PP^2$, so that $H^2 = 1$, $E_i^2 = -1$, and $H\cdot E_i = E_i\cdot E_j = 0$ for $i\neq j$.
Then $f^*: \Pic(S)\to \Pic(X)$ is injective, its image
$$
S_\Co \definedas f^*\Pic(S) = \generators{f^*H, f^*E_1, \ldots, f^*E_{10}}
$$
is the invariant lattice $H^2(X, \bZ)^\sigma$, and
$$
S_\Co \cong \generators{2}\oplus\generators{-2}^{10} = \latI_{1, 10}(2) = (11, 11, 1)_1
.
$$
:::

::: {.proof}

If $f^*D = 0$ then $2D = f_* f^* D = 0$, and $\Pic(S)\cong\latI_{1, 10}$ is torsion-free, so $D = 0$; thus $f^*$ is injective.
As $f$ has degree $2$, one has $f_* f^* = 2$, and the projection formula gives, for all $D, D'\in\Pic(S)$,
$$
\qty{f^*D \cdot f^*D'} = D \cdot f_* f^* D' = D\cdot 2D' = 2\qty(D\cdot D')
.
$$
Applied to the orthogonal basis $H, E_1, \ldots, E_{10}$, this shows that $f^*H, f^*E_1, \ldots, f^*E_{10}$ have Gram matrix $\diag(2, -2, \ldots, -2)$, so that $S_\Co \cong \generators{2}\oplus\generators{-2}^{10} = \latI_{1, 10}(2)$, of signature $(1, 10)$.

The lattice $S_\Co$ is $\sigma$-invariant, so $S_\Co\iscontainedin H^2(X, \bZ)^\sigma$.
The fixed locus $\Fix(\sigma) = R$ is a single smooth rational curve (the case $n = 1$), so $\chi(R) = 2$.
On the K3 surface $X$, both $H^0$ and $H^4$ are $\sigma$-invariant of rank $1$ and $H^1 = H^3 = 0$, so the topological Lefschetz fixed-point formula reads
$$
\chi(R) = \Sum_i (-1)^i \trace\qty(\sigma^* \mid H^i(X, \bZ)) = 2 + \trace\qty(\sigma^* \mid H^2(X, \bZ))
.
$$
Since $\chi(R) = 2$, we obtain $\trace(\sigma^* \mid H^2(X, \bZ)) = 0$.
As $H^2(X, \bZ)$ has rank $22$ and $\sigma^*$ is an involution, the invariant lattice has rank $\tfrac{1}{2}(22 + 0) = 11$ and the coinvariant lattice rank $\tfrac{1}{2}(22 - 0) = 11$, so that $11 + 11 = 22$; cf. @prop:involution_eigenspaces. Hence $S_\Co$, of rank $11$, is a finite-index sublattice of $H^2(X, \bZ)^\sigma$.

The lattice $S_\Co \cong \generators{2}\oplus\generators{-2}^{10}$ has
$$
\abs{\det S_\Co} = 2\cdot 2^{10} = 2^{11},
\qquad
A_{S_\Co} \cong (\bZ/2\bZ)^{11},
\qquad
q_{S_\Co} \cong \generators{\tfrac{1}{2}}\oplus\generators{-\tfrac{1}{2}}^{10}
,
$$
so $S_\Co$ is $2$-elementary of rank $r = 11$ and length $a = 11$.
Because $q_{S_\Co}$ takes the value $\tfrac{1}{2}\notin\bZ$, one has $\delta = 1$, giving $(r, a, \delta) = (11, 11, 1)$.

The involution $\sigma$ acts as $-\id$ on $T(X)$, and $H^2(X, \bZ)^\sigma = \Pic(X)^{\sigma^*}$.
The lattice $\NS(X) = H^{1,1}(X)\intersect H^2(X, \bZ)\cong\Pic(X)$ is primitive in $H^2(X, \bZ)$, and $T(X) = \NS(X)^{\perp}$ [@Huy16, Ch. 3, Def. 2.5 and Lemma 3.1].
The sublattice $S_\Co = f^*\Pic(S)$ lies in $\Pic(X)$, and it has finite index in $H^2(X, \bZ)^\sigma$, so $H^2(X, \bQ)^\sigma = S_\Co\tensor\bQ\iscontainedin\NS(X)\tensor\bQ$.
Primitivity of $\NS(X)$ gives $H^2(X, \bZ)^\sigma\iscontainedin H^2(X, \bZ)\intersect(\NS(X)\tensor\bQ) = \NS(X)$, hence $H^2(X, \bZ)^\sigma = \Pic(X)^{\sigma^*}$.
It also gives $T(X) = \NS(X)^\perp\iscontainedin(H^2(X, \bZ)^\sigma)^\perp$, which is the coinvariant lattice of @def:invariant_coinvariant_lattices.
By @prop:involution_eigenspaces, $\sigma^*$ acts as $-1$ on the rational span of the coinvariant lattice, so $\sigma^*$ acts as $-\id$ on $T(X)$.

So @prop:nikulin-fixed-locus applies to $\sigma$ and to $M = \Pic(X)^{\sigma^*} = H^2(X, \bZ)^\sigma$.
The fixed locus $R$ is nonempty and is not a union of two elliptic curves, so it has the form $C^{(g)}+\Sum_{i=1}^k R_i$.
A single smooth rational curve gives $g = 0$ and $k = 0$, so $22-r-a = 0$ and $r-a = 0$, that is $r = a = 11$.
As $M$ is $2$-elementary with $a = 11$, $\abs{\det H^2(X, \bZ)^\sigma} = 2^{11}$.
Since $S_\Co \iscontainedin H^2(X, \bZ)^\sigma$ have equal rank $11$ and equal absolute determinant $2^{11}$, the index $[H^2(X, \bZ)^\sigma : S_\Co]$ is $1$: the two coincide, and by @thm:invariants-coinvariants-integral the invariant lattice -- hence $S_\Co$ -- is primitive in $H^2(X, \bZ)$.
That the invariants $(11, 11, 1)_1$ determine the isometry class $\generators{2}\oplus\generators{-2}^{10}\cong\generators{-2}\oplus E_{10}(2)$ is Nikulin's classification of indefinite even $2$-elementary lattices [@Nik80].
:::

::: {.proposition #prop:blowup-geometric-basis title="Geometric basis of a blowup of the plane"}

Let
$$
S = S_N \xrightarrow{\pi_N} S_{N-1} \too \cdots \xrightarrow{\pi_1} S_0 = \PP^2
$$
be a sequence of blowups, where $\pi_i$ is the blowup of a point $p_i\in S_{i-1}$ with exceptional curve $E_i\iscontainedin S_i$.
Let $e_0\in\Pic(S)$ be the pullback of the class of a line in $\PP^2$, and for $1\leq i\leq N$ let $e_i\in\Pic(S)$ be the pullback of the class of $E_i$.

1. The classes $e_0, e_1, \ldots, e_N$ form a basis of $\Pic(S)$ with $e_0^2 = 1$, $e_i^2 = -1$ for $i\geq 1$, and $e_i\cdot e_j = 0$ for $i\neq j$. So $\Pic(S)\cong\latI_{1,N}$, and $\rho(S) = N+1$.
2. $K_S = -3e_0 + e_1 + \cdots + e_N$.
3. If $S$ is a terminal Coble surface of K3 type and $f\colon X\to S$ is the double cover of @prop:coble-k3-cover, then $f^*$ is injective and $f^*\Pic(S)\cong\latI_{1,N}(2)$, with basis $f^*e_0,\dots,f^*e_N$.

A choice of such a basis is a marking of $S$, and it defines an isomorphism of lattices $\Pic(S)\to\latI_{1,N}$ [@CDL25, §5.4, p. 552].

:::

::: {.proof}

For $N = 0$, $\Pic(\PP^2)\cong\bZ$ with generator the class $h$ of a line, $h^2 = 1$ [@Har10a, V Ex. 1.4.2], and $K_{\PP^2} = -3h$ [@Har10a, V Ex. 1.4.4].
For $N\geq 1$, @prop:blowup-geometric-basis holds for $S_{N-1}$ by induction, with basis $e_0', \ldots, e_{N-1}'$.
By [@Har10a, V.3.2], $\Pic(S_N)\cong\Pic(S_{N-1})\oplus\bZ\,E_N$ by $\pi_N^*$ and $1\mapsto E_N$, with $(\pi_N^*D)\cdot(\pi_N^*D') = D\cdot D'$, $(\pi_N^*D)\cdot E_N = 0$ and $E_N^2 = -1$.
So $e_i = \pi_N^* e_i'$ for $i < N$ and $e_N = [E_N]$ form a basis of $\Pic(S_N)$ with the stated intersection numbers, which is (1).
By [@Har10a, V.3.3], $K_{S_N} = \pi_N^*K_{S_{N-1}} + E_N = -3e_0 + e_1 + \cdots + e_{N-1} + e_N$, which is (2).

For (3), the divisor $C\in\abs{-2K_S}$ is the disjoint union of the smooth curves $C_i$, so it is smooth, and $S$ is a smooth rational surface.
So @prop:double-cover-is-k3 applies to $f$ and gives $f^*D\cdot f^*D' = 2(D\cdot D')$ for all $D, D'\in\Pic(S)$.
If $f^*D = 0$ then $2D = f_*f^*D = 0$, and $\Pic(S)$ is torsion-free by (1), so $D = 0$.
Thus $f^*$ is injective, and by (1) the Gram matrix of $f^*e_0, \ldots, f^*e_N$ is $\diag(2, -2, \ldots, -2)$, which is the Gram matrix of $\latI_{1,N}(2)$.

:::
