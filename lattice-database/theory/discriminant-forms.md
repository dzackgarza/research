---
title: Dual lattices and discriminant groups
summary: The dual lattice, the discriminant group and its form, unimodular and 2-elementary lattices, and Nikulin's invariants.
order: 4
---

Let $L$ be an [integral](lattices.html#integral) lattice that is [nondegenerate](lattices.html#degenerate).

## Dual lattice {#dual-lattice}

::: {.definition}
The *dual lattice* $L^*$ is $\{x \in L \otimes_{\mathbb{Z}} \mathbb{Q} : b(x, y) \in \mathbb{Z} \text{ for all } y \in L\}$, with the $\mathbb{Q}$-bilinear extension of $b$.
:::

$L^*$ contains $L$, and its [chosen basis](named-lattices.html#dual-lattices) is dual to that of $L$.

## Discriminant group {#discriminant-group}

::: {.definition}
The *discriminant group* $A_L$ of $L$ is the cokernel of the correlation $L \to \operatorname{Hom}_{\mathbb{Z}}(L, \mathbb{Z})$, $x \mapsto b(x, -)$.
:::

::: {.proposition}
The isomorphism $L^* \to \operatorname{Hom}_{\mathbb{Z}}(L, \mathbb{Z})$, $y \mapsto b(y, -)$, gives $A_L \cong L^*/L$, a finite group of order $|\det L|$.
:::

The page states $A_L$ by its invariant factors $d_1 \mid d_2 \mid \dots$, each greater than 1; the empty list is the trivial group.

::: {.definition}
The *discriminant form* is $b_{A_L}(x + L, y + L) = b(x, y) + \mathbb{Z}$, with values in $\mathbb{Q}/\mathbb{Z}$.
:::

## Unimodular lattices {#unimodular}

::: {.definition}
$L$ is *unimodular* when the correlation $L \to \operatorname{Hom}_{\mathbb{Z}}(L, \mathbb{Z})$ is an isomorphism; equivalently $A_L = 0$, and equivalently $\det L = \pm 1$.
:::

## 2-elementary lattices {#two-elementary}

::: {.definition}
$L$ is *2-elementary* when $A_L \cong (\mathbb{Z}/2)^a$ with $a \geq 1$.
An even 2-elementary lattice has invariants $(r, a, \delta)$: $r$ is the rank, the discriminant group is $(\mathbb{Z}/2)^a$, and $\delta = 0$ exactly when $b(x, x)$ is an integer for every $x$ in the dual lattice.
:::

::: {.theorem data-name="Nikulin"}
An indefinite even 2-elementary lattice is determined by its signature and $(r, a, \delta)$ ([Nikulin 1980](https://doi.org/10.1070/IM1980v014n01ABEH001060): V. V. Nikulin, *Integral symmetric bilinear forms and some of their applications*, Math.
USSR-Izv.
14 (1980), 103–167).
:::
