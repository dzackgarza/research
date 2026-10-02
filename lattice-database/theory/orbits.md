---
title: Orbits of primitive vectors
summary: The series $F_{L,\Gamma}(z, w)$ of the numbers of $\Gamma$-orbits of primitive vectors of each norm, for eight subgroups $\Gamma$ of $O(L)$.
order: 10
---

Let $L$ be an [integral](lattices.html#integral) lattice that is [nondegenerate](lattices.html#degenerate), with [discriminant group](discriminant-forms.html#discriminant-group) $A_L$.

## Eight subgroups of the orthogonal group {#groups}

::: {.definition}
$SO(L)$ is the kernel of $\det\colon O(L) \to \{\pm 1\}$.
The *stable orthogonal group* $\widetilde{O}(L)$ is the kernel of $O(L) \to O(A_L)$ ([GHS 2013](https://arxiv.org/abs/1012.4155), (6)). $O^+(L)$ is the kernel of the real spinor norm $\operatorname{sn}_\mathbb{R}\colon O(L \otimes \mathbb{R}) \to \mathbb{R}^*/(\mathbb{R}^*)^2 = \{\pm 1\}$, restricted to $O(L)$.
For a subgroup $\Gamma$ of $O(L)$, $\Gamma^+ = \Gamma \cap O^+(L)$, $S\Gamma = \Gamma \cap SO(L)$ and $\widetilde{\Gamma} = \Gamma \cap \widetilde{O}(L)$; so $\widetilde{O}^+(L) = \widetilde{O}(L) \cap O^+(L)$ ([GHS 2013](https://arxiv.org/abs/1012.4155), (7)).
:::

A record names the eight groups $O$, $SO$, $O^+$, $SO^+$, $\widetilde{O}$, $S\widetilde{O}$, $\widetilde{O}^+$ and $S\widetilde{O}^+$ with the keys `O`, `SO`, `O+`, `SO+`, `Otilde`, `SOtilde`, `Otilde+` and `SOtilde+`.

## Cokernel of the discriminant action {#mm-cokernel}

Let $L$ be nondegenerate, even and indefinite, with $\operatorname{rank}L>3$, and let $\rho_L\colon O(L)\to O(A_L,q_L)$ be its discriminant action. Define $MM(L):=\operatorname{coker}\rho_L$. The [Miranda–Morrison exact sequence](https://webdoc.sub.gwdg.de/ebook/serien/e/mpi_mathematik/2013/63.pdf), stated in Akyol–Degtyarev, Theorem 3.8, is
$$O(L)\xrightarrow{\rho_L}O(A_L,q_L)\longrightarrow E(L)\longrightarrow\mathfrak g(L)\longrightarrow 1,$$
where $E(L)$ is the Miranda–Morrison group and $\mathfrak g(L)$ is the genus group. Hence $MM(L)\cong\ker(E(L)\to\mathfrak g(L))$ is an $\mathbb F_2$-vector space. Its isomorphism class as a torsion $\mathbb Z$-module is determined by $d=\dim_{\mathbb F_2}MM(L)$: it is $(\mathbb Z/2\mathbb Z)^d$. Define *MM-triviality* by $d=0$; this is equivalent to surjectivity of $\rho_L$. Theorem 3.12 gives a local formula for the cokernel. The full group $E(L)$ equals $MM(L)$ only when $\mathfrak g(L)=1$.

For a lattice outside these hypotheses, surjectivity of $\rho_L$ remains a well-defined predicate. A torsion-module-valued cokernel requires a separate result that its image is normal and that the quotient is abelian.

The reflection in $w \in L \otimes \mathbb{R}$ with $b(w, w) \neq 0$ is $\sigma_w(x) = x - \frac{2 b(x, w)}{b(w, w)} w$.
Every element of $O(L \otimes \mathbb{R})$ is a product $\sigma_{w_1} \cdots \sigma_{w_m}$ of reflections, and $$\operatorname{sn}_\mathbb{R}(\sigma_{w_1} \cdots \sigma_{w_m}) = \prod_{i=1}^m \left(-\frac{b(w_i, w_i)}{2}\right) \in \mathbb{R}^*/(\mathbb{R}^*)^2$$ ([Dawes 2022](https://arxiv.org/abs/2205.10601), (4)).

::: {.proposition}
On a positive definite lattice, $O^+(L) = SO(L)$.
On a negative definite lattice, $O^+(L) = O(L)$.
:::

::: {.proof}
A product of $m$ reflections has determinant $(-1)^m$.
When $b$ is positive definite, each factor $-b(w_i, w_i)/2$ is negative, so the spinor norm is $(-1)^m$ too.
When $b$ is negative definite, each factor is positive, so the spinor norm is $1$.
:::

So on a definite lattice the eight groups are at most four.
When $A_L = 0$, $\widetilde{O}(L) = O(L)$, and the eight groups are at most four again.

## The series of orbits {#primitive-orbits}

::: {.definition}
For a subgroup $\Gamma$ of $O(L)$ and an integer $n$, $c_\Gamma(n)$ is the number of $\Gamma$-orbits on the primitive vectors $v \in L$ with $b(v, v) = n$, when it is finite.
The *series of orbits of primitive vectors* is $$F_{L,\Gamma}(z, w) = c_\Gamma(0) + \sum_{n \geq 1} c_\Gamma(n) z^n + \sum_{n \geq 1} c_\Gamma(-n) w^n \in \mathbb{Z}[[z, w]].$$
:::

So $F_{L,\Gamma}(0, 0)$ is the number of $\Gamma$-orbits of primitive isotropic vectors, the coefficient of $z^n$ is the number of $\Gamma$-orbits of primitive vectors of norm $n$, and the coefficient of $w^n$ is that of norm $-n$.
A record states the coefficients that are known, through $z^4$ and $w^4$ at first, and a coefficient that is not known is null.

Each coefficient obeys these relations, which `latticedb check` verifies:

- $c_\Gamma(n) = 0$ exactly when no primitive vector has norm $n$, for every $\Gamma$.
  That is so for odd $n$ when $L$ is even, and for $n = 0$ and for $n$ of the sign opposite to $b$ when $L$ is definite.

- When $n$ has no square factor $k^2 > 1$, every vector of norm $n$ is primitive, since $b(kv, kv) = k^2 b(v, v)$.
  Then $c_\Gamma(n) = 0$ exactly when the [theta series](definite-lattices.html#theta-series) has no vector of norm $n$.

- For $H \subseteq \Gamma$, each $\Gamma$-orbit is a union of $H$-orbits, so $c_H(n) \geq c_\Gamma(n)$.

- Two keys that name one group, by the proposition above, have the same coefficients.

## Computation {#computation}

::: {.proposition}
Let $\varphi\colon G \to Q$ be a surjective homomorphism with kernel $H$, and let $G$ act on a set $X$.
Then $x \mapsto G \cdot (x, 1)$ induces a bijection from the $H$-orbits on $X$ to the $G$-orbits on $X \times Q$, where $g \cdot (x, q) = (g x, \varphi(g) q)$.
:::

::: {.proof}
$g \cdot (x, 1) = (y, 1)$ exactly when $y = g x$ and $g \in H$.
Every $G$-orbit meets $X \times \{1\}$: for $g$ with $\varphi(g) = q$, $g^{-1} \cdot (x, q) = (g^{-1} x, 1)$.
:::

For a definite lattice, `latticedb certify` computes $c_\Gamma(n)$ for $1 \leq |n| \leq 4$.
The function `qfauto` of PARI/GP gives generators of $O(L)$, and `qfminim` gives the vectors of norm at most 4, of which it keeps the primitive ones.
For $SO$, $\widetilde{O}$ and $S\widetilde{O}$, $Q$ is the image of $O(L)$ under $\det$, under $O(L) \to O(A_L)$, or under both, and the orbits are those of the proposition.
$O^+$ and its subgroups are then given by the [proposition on definite lattices](#groups).

For an indefinite lattice the sets are infinite.
Dawes gives algorithms for the orbits of vectors under subgroups of $O(L)$ ([Dawes 2022](https://arxiv.org/abs/2205.10601), Algorithms 2.1 to 2.3). When $L$ is even and contains two orthogonal hyperbolic planes, the coefficients come from $A_L$ and its finite quadratic form $q_L\colon A_L \to \mathbb{Q}/2\mathbb{Z}$.

The *divisor* $\operatorname{div}(v)$ of $v \in L$ is the positive generator of the ideal $b(v, L) \subseteq \mathbb{Z}$.
Then $v^* = v / \operatorname{div}(v)$ is in $L^\vee$, and its image in $A_L$ has order $\operatorname{div}(v)$ when $v$ is primitive ([GHS 2009](https://arxiv.org/abs/0810.1614), Section 3.3).

::: {.theorem data-name="Eichler"}
Let $L = U \oplus U_1 \oplus L_0$ be an even lattice, with $U = \mathbb{Z}e \oplus \mathbb{Z}f$ and $U_1$ hyperbolic planes, and let $L_1 = U_1 \oplus L_0$.
If $u, v \in L$ are primitive, $b(u, u) = b(v, v)$ and $u^* \equiv v^* \bmod L$, then $\tau(u) = v$ for some $\tau$ in the group $E_U(L_1)$ generated by the Eichler transvections $t(e, a)$ and $t(f, a)$ with $a \in L_1$ ([GHS 2009](https://arxiv.org/abs/0810.1614), Proposition 3.3(i), with the hypothesis of Section 1 that $L$ is even).
$E_U(L_1)$ is a subgroup of $S\widetilde{O}^+(L)$ ([GHS 2009](https://arxiv.org/abs/0810.1614), (10)).
:::

The theorem needs $L$ even.
In the odd lattice $U^2 \oplus \langle 1 \rangle$ with $b(x, x) = 1$, the vectors $x$ and $e + x$ are primitive of norm 1, and $A_L = 0$.
But $x$ is characteristic, $b(x, y) \equiv b(y, y) \bmod 2$ for every $y$, and $e + x$ is not, since $b(e + x, f) = 1$ and $b(f, f) = 0$.
An isometry keeps this property, so no element of $O(L)$ sends $x$ to $e + x$.

::: {.proposition}
Let $L = U \oplus U_1 \oplus L_0$ be even, and for an integer $n$ let $S_n$ be the set of $\alpha \in A_L$ of some order $d$ with $q_L(\alpha) = n / d^2$ in $\mathbb{Q}/2\mathbb{Z}$.
Then $v \mapsto v^* + L$ is a surjection from the primitive vectors of norm $n$ onto $S_n$, and its fibres are the $\widetilde{\Gamma}$-orbits for each $\widetilde{\Gamma}$ with $E_U(L_1) \subseteq \widetilde{\Gamma} \subseteq \widetilde{O}(L)$.
So $c_\Gamma(n) = |S_n|$ for $\Gamma = \widetilde{O}, S\widetilde{O}, \widetilde{O}^+, S\widetilde{O}^+$.
For $\Gamma = O, SO, O^+, SO^+$, $c_\Gamma(n)$ is the number of $O(q_L)$-orbits on $S_n$.
:::

::: {.proof}
For $v$ primitive of norm $n$ and $d = \operatorname{div}(v)$, $v^* + L$ has order $d$ and $q_L(v^* + L) = n / d^2$, so it is in $S_n$.
Let $\alpha \in S_n$ have order $d$.
Since $A_L = A_{L_0}$, $\alpha = x + L$ for some $x \in L_0^\vee$ with $d x \in L_0$, and $d^2 b(x, x) \equiv n \bmod 2 d^2$.
So $m = (n - d^2 b(x, x)) / 2d^2$ is an integer, and $v = d(e + m f + x)$ is in $L$ with $b(v, v) = n$.
$b(v, f) = d$ and $b(v, L) \subseteq d \mathbb{Z}$, so $\operatorname{div}(v) = d$ and $v^* + L = \alpha$.
If $v = k w$ with $w \in L$, then $\frac{d}{k} x \in L_0$, so $d$ divides $d / k$ and $k = 1$: $v$ is primitive.
Each $\widetilde{\Gamma}$ fixes $v^* + L$, and by the theorem $E_U(L_1)$ is transitive on each fibre; so the fibres are the $\widetilde{\Gamma}$-orbits.

For $SO^+ \subseteq \Gamma$, the map is $\Gamma$-equivariant and each fibre is one $S\widetilde{O}^+$-orbit, so the $\Gamma$-orbits correspond to the orbits on $S_n$ of the image of $\Gamma$ in $O(q_L)$.
The reflections $\sigma_{e+f}$ and $\sigma_{e-f}$ are in $O(L)$, since $b(e \pm f, e \pm f) = \pm 2$, and act trivially on $A_L = A_{U_1 \oplus L_0}$, so they are in $\widetilde{O}(L)$.
Their determinants are $-1$ and $-1$, and their real spinor norms $-b(w, w)/2$ are $-1$ and $1$; so they map onto $O(L) / SO^+(L) \subseteq \{\pm 1\}^2$, and $O(L) = \widetilde{O}(L) \cdot SO^+(L)$.
Thus $O$, $SO$, $O^+$ and $SO^+$ have one image in $O(q_L)$.
$L$ is even and indefinite, and $\operatorname{rank} L = 4 + \operatorname{rank} L_0 \geq l(A_L) + 4$, where $l$ is the minimal number of generators; so $O(L) \to O(q_L)$ is surjective ([Nikulin 1980](https://doi.org/10.1070/IM1980v014n01ABEH001060), Theorem 1.14.2).
:::

`latticedb certify` computes $c_\Gamma(n)$ for $1 \leq |n| \leq 4$ and $n = 0$ by this proposition, for an even lattice whose hyperbolic index, stored or bounded from below by the embeddings of $U^k$ in its morphism files, is at least 2. The class `TorsionQuadraticModule` of SageMath gives $A_L$, $q_L$ and generators of $O(q_L)$, and the orbits on $S_n$ are found by breadth-first search.
For an odd lattice the coefficients are stated with a `reference` that proves them.

::: {.example}
Let $L = U^2 \oplus L'$ be even and unimodular.
Then $A_L = 0$ and $S_n = \{0\}$ for each even $n$, so $c_\Gamma(n) = 1$ for each of the eight groups: the vector $e + \frac{n}{2} f$ in the first $U$ is primitive of norm $n$.
For the K3 lattice $U^3 \oplus E_8(-1)^2$ this is [GHS 2013](https://arxiv.org/abs/1012.4155), Example 7.6.
:::

GHS 2009: V. Gritsenko, K. Hulek and G. K. Sankaran, *Abelianisation of orthogonal groups and the fundamental group of modular varieties*, arXiv:0810.1614. GHS 2013: V. Gritsenko, K. Hulek and G. K. Sankaran, *Moduli of K3 surfaces and irreducible symplectic manifolds*, arXiv:1012.4155. Dawes 2022: M. Dawes, *Orbits in lattices*, arXiv:2205.10601.
