---
title: Dual lattices and discriminant groups
summary: The dual lattice, the discriminant group and its form, unimodular and 2-elementary lattices, and Nikulin's invariants.
order: 4
---

Let $L$ be an [integral](lattices.html#integral) lattice that is [nondegenerate](lattices.html#degenerate).

## Dual lattice {#dual-lattice}

The *dual lattice* $L^*$ is $\{x \in L \otimes \mathbb{Q} : b(x, y) \in \mathbb{Z} \text{ for all } y \in L\}$ with the form $b$.
It contains $L$, and [named lattices](named-lattices.html#dual-lattices) gives the basis of its record.

## Discriminant group {#discriminant-group}

The *discriminant group* of $L$ is the cokernel of the correlation $L \to \operatorname{Hom}(L, \mathbb{Z})$, $x \mapsto b(x, -)$.
It is the finite group $A_L = L^*/L$, of order $|\det L|$.
A record states it by its invariant factors $d_1 \mid d_2 \mid \dots$, each greater than 1; the empty list is the trivial group.

The *discriminant form* is $b_{A_L}(x + L, y + L) = b(x, y) + \mathbb{Z}$, with values in $\mathbb{Q}/\mathbb{Z}$.

## Unimodular lattices {#unimodular}

$L$ is *unimodular* when the correlation $L \to \operatorname{Hom}(L, \mathbb{Z})$ is an isomorphism, which is when $A_L = 0$ and the determinant is $1$ or $-1$.

## 2-elementary lattices {#two-elementary}

$L$ is *2-elementary* when $A_L$ is $(\mathbb{Z}/2)^a$ with $a \geq 1$.
An even 2-elementary lattice has invariants $(r, a, \delta)$: $r$ is the rank, the discriminant group is $(\mathbb{Z}/2)^a$, and $\delta = 0$ exactly when $b(x, x)$ is an integer for every $x$ in the dual lattice.

An indefinite even 2-elementary lattice is determined by its signature and $(r, a, \delta)$: V. V. Nikulin, "Integral symmetric bilinear forms and some of their applications", Math.
USSR-Izv.
14 (1980), 103-167, DOI [10.1070/IM1980v014n01ABEH001060](https://doi.org/10.1070/IM1980v014n01ABEH001060).
