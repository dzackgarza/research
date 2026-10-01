---
title: Morphisms of lattices
summary: Morphisms of lattices and the block matrices that state them.
order: 9
---

## Morphisms {#morphisms}

A *morphism* $\varphi \colon S \to T$ of [lattices](lattices.html#lattices) is a $\mathbb{Z}$-linear map with $b_T(\varphi x, \varphi y) = b_S(x, y)$ for all $x, y \in S$.

## Matrices {#matrices}

The matrix $M$ of $\varphi$ is in the bases of the records of $S$ and $T$, which list the orthogonal summands in the order of their names.
It has $\operatorname{rank} T$ rows and $\operatorname{rank} S$ columns: column $j$ lists the coordinates of $\varphi(e_j)$ in the basis of the record of $T$.
The build checks that $M^{\top} G_T M = G_S$ for the Gram tensors $G_S$, $G_T$, so the map preserves the forms.
A SageMath morphism `phi` gives `phi.matrix().transpose()`, because SageMath lists the images in rows.

## Block matrices {#blocks}

Lines between the rows and between the columns cut the matrix into blocks, as `M.subdivisions()` of SageMath states them: a line $k$ lies between rows $k$ and $k + 1$.
The build checks that the parts of the rows are [orthogonal summands](lattices.html#orthogonal-sums) of $T$ and that the parts of the columns are orthogonal summands of $S$.
