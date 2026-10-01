---
title: Lattices
summary: Lattices, the chosen basis and the Gram tensor, orthogonal sums, twists, and the invariants of every lattice.
order: 2
---

## Lattices {#lattices}

::: {.definition}
A *lattice* is a free $\mathbb{Z}$-module $L$ of finite rank $n$ with a symmetric bilinear form $b \colon L \times L \to \mathbb{Q}$.
An *isometry* $\varphi \colon L \to M$ is an isomorphism of modules with $b_M(\varphi x, \varphi y) = b_L(x, y)$ for all $x, y \in L$.
$O(L)$ is the group of the isometries $L \to L$.
:::

## Gram tensor {#gram-tensor}

::: {.definition}
Each lattice of the catalogue comes with a *chosen basis* $e_1, \dots, e_n$ of $L$; the [named lattices](named-lattices.html) state theirs.
The *Gram tensor* is the form $b$, a symmetric $(0, 2)$-tensor, and the catalogue stores its components $b(e_i, e_j)$ in the chosen basis: row $i$ lists $b(e_i, e_1), \dots, b(e_i, e_n)$.
:::

A vector of $L$ is written by its coordinates in the chosen basis.

## Orthogonal sums {#orthogonal-sums}

::: {.definition}
$L = M_1 \oplus M_2$ is an *orthogonal sum* when $L$ is the direct sum of the submodules $M_1$ and $M_2$ and $b(x, y) = 0$ for $x \in M_1$, $y \in M_2$.
The basis of an orthogonal sum is the union of the bases of the summands, in the order written.
$L^k$ is the orthogonal sum of $k$ copies of $L$.
:::

The page of a lattice states the orthogonal decomposition that the chosen basis gives.
It is the finest partition of $e_1, \dots, e_n$ into parts with $b(e_i, e_j) = 0$ for $e_i$, $e_j$ in different parts, and $L$ is the orthogonal sum of the sublattices that the parts generate.

## Twists {#twists}

::: {.definition}
For $k \in \mathbb{Q}^\times$, the *twist* $L(k)$ is the module $L$ with the form $k b$.
:::

## Determinant and signature {#signature}

::: {.definition}
The *determinant* of $L$ is $\det(b(e_i, e_j))$.
:::

::: {.proposition}
The determinant is the same for every basis of $L$.
:::

::: {.proof}
A change of basis by $P \in \mathrm{GL}_n(\mathbb{Z})$ multiplies it by $\det(P)^2 = 1$.
:::

::: {.definition}
Let $v_1, \dots, v_n$ be a $b$-orthogonal basis of $L \otimes_{\mathbb{Z}} \mathbb{Q}$.
The *signature* of $L$ is $(n_+, n_-)$, where $n_+$ is the number of $i$ with $b(v_i, v_i) > 0$ and $n_-$ the number of $i$ with $b(v_i, v_i) < 0$.
:::

::: {.theorem data-name="Sylvester's law of inertia"}
The signature does not depend on the orthogonal basis.
:::

## Definiteness {#definiteness}

::: {.definition}
$L$ is *positive definite* when $b(x, x) > 0$ for every nonzero $x \in L$, *negative definite* when $b(x, x) < 0$ for every nonzero $x \in L$, and *indefinite* when $b(x, x) > 0$ and $b(y, y) < 0$ for some $x, y \in L$.
It is *positive semidefinite* when $b(x, x) \geq 0$ for all $x$, $b \neq 0$ and the determinant is zero, *negative semidefinite* when the same holds with $\leq$, and *zero* when $b = 0$.
:::

## Degenerate lattices {#degenerate}

::: {.definition}
The *correlation* of $L$ is the map $L \to \operatorname{Hom}_{\mathbb{Z}}(L, \mathbb{Q})$, $x \mapsto b(x, -)$.
Its kernel is the *radical* of $b$.
$L$ is *degenerate* when the radical is not zero.
:::

::: {.proposition}
The radical has rank $n - n_+ - n_-$, and $L$ is degenerate exactly when its determinant is $0$.
:::

## Integral lattices {#integral}

::: {.definition}
$L$ is *integral* when $b(x, y) \in \mathbb{Z}$ for all $x, y \in L$, which is when every $b(e_i, e_j)$ is an integer.
An integral lattice is *even* when $b(x, x)$ is even for every $x \in L$, and *odd* otherwise.
The *parity* of $L$ is even or odd accordingly.
:::
