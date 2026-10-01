---
title: Overlattices and the genus
summary: Integral overlattices of a lattice, counted through the discriminant form, and the genus symbol.
order: 5
---

Let $L$ be an [integral](lattices.html#integral) lattice that is [nondegenerate](lattices.html#degenerate), with [discriminant group](discriminant-forms.html#discriminant-group) $A_L = L^*/L$ and discriminant form $b_{A_L}$.

## Integral overlattices {#overlattices}

An *integral overlattice* of $L$ is an integral lattice $M$ with $L \subseteq M \subseteq L^*$.
$M \mapsto M/L$ is a bijection from the integral overlattices to the subgroups $H$ of $A_L$ with $b_{A_L}(H, H) = 0$.
A record states their number, with $M = L$ counted.
It counts subgroups, not their orbits under the isometries of $L$.
An even $L$ can have odd lattices among the $M$.

A record states the number when $A_L$ has few enough subgroups for the build to list them; a record without it is not decided.

## Genus symbol {#genus-symbol}

The genus symbol of $L$ is `I` when $L$ is odd and `II` when $L$ is even, with the signature, such as `II_{1,9}`. When the determinant is not $1$ or $-1$, the local symbol at each prime that divides twice the determinant follows in parentheses, in the notation that SageMath prints.
