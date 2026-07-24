# Isometries and arithmetic invariants {#sec-isometry}

## Isometries and automorphism groups {#sec-isometry-groups}

Let $\mathbf{Lat}_R^{\simeq}$ be the core of the category of $R$-lattices.
Its morphisms are isometries.
For lattices $L$ and $M$,
$$
\operatorname{Iso}(L,M)
=\operatorname{Hom}_{\mathbf{Lat}_R^{\simeq}}(L,M),
\qquad
O(L)=\operatorname{Aut}(L).
$$
When nonempty, $\operatorname{Iso}(L,M)$ is an $(O(M),O(L))$-bitorsor: $O(M)$ acts on the left by postcomposition and $O(L)$ acts on the right by precomposition.

::: {#def-discriminant-rep}
## Discriminant representation

An isometry of $L$ induces an isometry of its discriminant form.
Hence the discriminant construction gives a homomorphism
$$
O(L)\longrightarrow O(A_L,q_L)
$$
for an even lattice, and the analogous map for the discriminant bilinear form in the general case.
Its kernel is the stable orthogonal group
$$
\widetilde O(L)=\ker\bigl(O(L)\to O(A_L,q_L)\bigr).
$$
If $L$ is even and indefinite and $\operatorname{rank}(L)\geq\ell(A_L)+2$, where $\ell(A_L)$ is the minimum number of generators of $A_L$, the homomorphism $O(L)\to O(A_L,q_L)$ is surjective [@Nik80].
:::

## Matrix realizations

::: {#prp-matrix-realizations}
If $L$ is free and a basis has been chosen, its Gram matrix $B$ identifies
$$
O(L)=\{g\in\operatorname{GL}_n(R)\mid g^{\mathsf T}Bg=B\}.
$$
Changing the basis conjugates this subgroup.
For a finite module with mixed invariant factors, choose a decomposition $A=\bigoplus_{i=1}^r\mathbb Z/d_i\mathbb Z$.
An endomorphism is a matrix $(a_{ij})$ in which $a_{ij}$ represents a homomorphism $\mathbb Z/d_j\mathbb Z\to\mathbb Z/d_i\mathbb Z$, equivalently $d_j a_{ij}=0$ in $\mathbb Z/d_i\mathbb Z$; the automorphisms are exactly the invertible endomorphisms in this matrix ring.
In the homocyclic case this gives
$$
\operatorname{Aut}\bigl((\mathbb Z/d\mathbb Z)^n\bigr)
\cong\operatorname{GL}_n(\mathbb Z/d\mathbb Z).
$$
:::

## Index

::: {#def-index}
For a subgroup $H\le G$, the *index* $[G:H]$ is the cardinality of the set of left cosets $G/H$.
If $G$ is finite, $[G:H]=|G|/|H|$.
In an abelian category, the analogous cardinality of a cokernel is used only after the relevant monomorphism and finiteness hypotheses have been stated.
:::

## The Miranda--Morrison sequence

::: {#thm-miranda-morrison}
For an even indefinite lattice $L$ of rank at least $3$, the discriminant representation fits into the Miranda--Morrison exact sequence
$$
1\to\widetilde O(L)\to O(L)\to O(A_L,q_L)
\to
\Sigma(L)\big/\big((\Gamma_{\mathbb Q}\cap\Sigma(L))\Sigma^\#(L)\big)
\to0
$$
with the notation and local factors of [@MM09, Thm. V.5.1]. The last group measures the failure of the discriminant representation to be surjective.
It is distinct from $\operatorname{SO}(L)=\ker(\det)$.
:::

::: {#def-genus}
## Genus {#sec-genus-sec}

Two integral lattices lie in the same genus if they are isometric over $\mathbb R$ and over $\mathbb Z_p$ for every prime $p$.
Extension of scalars induces the map
$$
\pi_0(\mathbf{Lat}_{\mathbb Z}^{\simeq})
\longrightarrow
\pi_0\!\left(
\mathbf{Lat}_{\mathbb R}^{\simeq}
\times\prod_p\mathbf{Lat}_{\mathbb Z_p}^{\simeq}
\right).
$$
The genus of $L$ is the fiber of this map over the image of $[L]$.
It is a pointed set containing $[L]$.
Its relation to the components of the homotopy fiber is governed by the exact sequence in @sec-pi0-fiber.
:::
