---
title: Named lattices
summary: Notation for the named lattices of the catalogue, and the chosen basis of each one.
order: 3
---

Each name is built from the lattices below by [orthogonal sums](lattices.html#orthogonal-sums) and [twists](lattices.html#twists) $L(k)$.

## Diagonal lattices {#diagonal}

::: {.definition}
$\langle a \rangle$ is the lattice of rank 1 with basis $e_1$ and $b(e_1, e_1) = a$.
$\mathrm{I}_{p,q}$ is the orthogonal sum of $p$ copies of $\langle 1 \rangle$ and $q$ copies of $\langle -1 \rangle$.
$\mathrm{I}_{n,0}$ is also written $\mathbb{Z}^n$: its basis $e_1, \dots, e_n$ has $b(e_i, e_j) = \delta_{ij}$.
:::

## The hyperbolic plane {#hyperbolic-plane}

::: {.definition}
$U$ is the lattice with basis $e, f$ and $b(e, e) = b(f, f) = 0$, $b(e, f) = 1$.
:::

## Root lattices {#root-lattices}

::: {.definition}
$X_n$, for $X_n$ one of $A_n$ ($n \geq 1$), $D_n$ ($n \geq 4$), $E_6$, $E_7$, $E_8$, is the [root lattice](roots.html#roots) of that type: $e_1, \dots, e_n$ is a basis of simple roots, numbered as SageMath's `CartanMatrix` numbers them, and $b(e_i, e_j)$ is the entry $(i, j)$ of the Cartan matrix.
:::

::: {.definition}
$\widetilde{X}_n$ is the lattice of rank $n + 1$ of the affine root system of that type: its basis $e_1, \dots, e_{n+1}$ is a basis of simple roots, numbered as SageMath's `CartanMatrix` numbers them, and $b(e_i, e_j)$ is the entry $(i, j)$ of the affine Cartan matrix.
:::

::: {.definition}
For $n$ even, $D_n^+ := D_n \cup (h + D_n) \subset \mathbb{Q}^n$, where $D_n = \{x \in \mathbb{Z}^n : x_1 + \dots + x_n \text{ even}\}$, $h = (\tfrac{1}{2}, \dots, \tfrac{1}{2})$, and the form is $b(x, y) = \sum_i x_i y_i$.
:::

## Dual lattices {#dual-lattices}

::: {.definition}
$L^*$ is the [dual lattice](discriminant-forms.html#dual-lattice) of $L$.
For $L$ in the catalogue, the chosen basis of $L^*$ is $e_1^*, \dots, e_n^*$ with $b(e_i^*, e_j) = \delta_{ij}$, dual to the chosen basis of $L$.
:::
