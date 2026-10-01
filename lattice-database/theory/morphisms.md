---
title: Morphisms of lattices
summary: Morphisms of lattices and their block matrices.
order: 9
---

## Morphisms {#morphisms}

::: {.definition}
A *morphism* $\varphi \colon S \to T$ of [lattices](lattices.html#lattices) is a $\mathbb{Z}$-linear map with $b_T(\varphi x, \varphi y) = b_S(x, y)$ for all $x, y \in S$.
:::

::: {.proposition}
When $S$ is nondegenerate, a morphism $\varphi \colon S \to T$ is injective; it is then an *isometric embedding*.
:::

::: {.proof}
$\varphi x = 0$ gives $b_S(x, y) = b_T(0, \varphi y) = 0$ for all $y$, so $x$ is in the radical of $S$, which is zero.
:::

## Matrices {#matrices}

::: {.definition}
The matrix $M$ of $\varphi$ is in the [chosen bases](lattices.html#gram-tensor) of $S$ and $T$, with the orthogonal summands in the order in which the name of the lattice writes them.
It has $\operatorname{rank} T$ rows and $\operatorname{rank} S$ columns: column $j$ lists the coordinates of $\varphi(e_j)$ in the chosen basis of $T$.
:::

$M^{\top} G_T M = G_S$ for the matrices $G_S = (b_S(e_i, e_j))$ and $G_T = (b_T(e_i, e_j))$, so $\varphi$ preserves the forms.
A SageMath morphism `phi` gives `phi.matrix().transpose()`, because SageMath lists the images in rows.

## Block matrices {#blocks}

Lines between the rows and between the columns subdivide the matrix into blocks, as `M.subdivisions()` of SageMath states them: a line $k$ lies between rows $k$ and $k + 1$, or between columns $k$ and $k + 1$.
The basis vectors of $T$ between two consecutive row lines span an [orthogonal summand](lattices.html#orthogonal-sums) of $T$, and the basis vectors of $S$ between two consecutive column lines span an orthogonal summand of $S$.
