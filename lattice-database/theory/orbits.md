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

For an indefinite lattice the sets are infinite, and the coefficients come from theorems.
Dawes gives algorithms for the orbits of vectors under subgroups of $O(L)$ ([Dawes 2022](https://arxiv.org/abs/2205.10601), Algorithms 2.1 to 2.3).

::: {.theorem data-name="Eichler"}
Let $L$ be a lattice that contains two orthogonal hyperbolic planes.
Then the $S\widetilde{O}(L)$-orbit of a primitive vector $l \in L$ is determined by $b(l, l)$ and by the image of $l / \operatorname{div}(l)$ in $A_L$ ([GHS 2013](https://arxiv.org/abs/1012.4155), Lemma 7.5).
:::

::: {.example}
Let $L = U^2 \oplus L'$ be even and unimodular.
Then $A_L = 0$, so $c_{S\widetilde{O}}(n)$ is 1 for each even $n$: the vector $e + \frac{n}{2} f$ in the first $U$, with $b(e, e) = b(f, f) = 0$ and $b(e, f) = 1$, is primitive of norm $n$.
Each of $O$, $SO$ and $\widetilde{O}$ contains $S\widetilde{O}$, so it has one orbit too.
For the K3 lattice $U^3 \oplus E_8(-1)^2$ this is [GHS 2013](https://arxiv.org/abs/1012.4155), Example 7.6.
:::

GHS 2013: V. Gritsenko, K. Hulek and G. K. Sankaran, *Moduli of K3 surfaces and irreducible symplectic manifolds*, arXiv:1012.4155. Dawes 2022: M. Dawes, *Orbits in lattices*, arXiv:2205.10601.
