---
title: Overlattices and the genus symbol
summary: Integral overlattices of a lattice, counted through the discriminant form, and the genus symbol.
order: 5
---

Let $L$ be an [integral](lattices.html#integral) lattice that is [nondegenerate](lattices.html#degenerate), with [discriminant group](discriminant-forms.html#discriminant-group) $A_L \cong L^*/L$ and discriminant form $b_{A_L}$.

## Integral overlattices {#overlattices}

::: {.definition}
An *integral overlattice* of $L$ is an integral lattice $M$ with $L \subseteq M \subseteq L^*$.
:::

::: {.proposition}
$M \mapsto M/L$ is a bijection from the integral overlattices to the subgroups $H$ of $A_L$ with $b_{A_L}(H, H) = 0$.
:::

::: {.example}
An even $L$ can have odd overlattices: for $L = \langle 4 \rangle = \mathbb{Z}v$, $M = \mathbb{Z}\tfrac{v}{2} \cong \langle 1 \rangle$.
:::

The page states the number of integral overlattices, with $M = L$ counted.
Each subgroup $H$ counts once, so overlattices that are isometric to each other count separately.
The number is stated when $A_L$ has at most 100000 subgroups; otherwise it is [not decided](records.html#not-decided).

## Genus symbol {#genus-symbol}

::: {.definition}
The genus symbol of $L$ is $\mathrm{I}$ when $L$ is odd and $\mathrm{II}$ when $L$ is even, with the signature as subscript, such as $\mathrm{II}_{1,9}$.
When the determinant is not $1$ or $-1$, the local symbol at each prime that divides twice the determinant follows in parentheses, in the notation that SageMath prints.
:::
