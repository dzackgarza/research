---
title: Named lattices
summary: The notation for the named lattices of the catalogue, and the basis that a record of each one uses.
order: 3
---

The basis of an [orthogonal sum](lattices.html#orthogonal-sums) is the union of the bases of the summands, in the order written, and $L(k)$ is the [twist](lattices.html#twists) of $L$ by $k$.

## Diagonal lattices {#diagonal}

$\langle a \rangle$ is the lattice of rank 1 with basis $e_1$ and $b(e_1, e_1) = a$.
$\mathrm{I}_{p,q}$ is the orthogonal sum of $p$ copies of $\langle 1 \rangle$ and $q$ copies of $\langle -1 \rangle$.
$\mathrm{I}_{n,0}$ is the module $\mathbb{Z}^n$ with the Euclidean form: its basis $e_1, \dots, e_n$ has $b(e_i, e_j) = \delta_{ij}$.

## The hyperbolic plane {#hyperbolic-plane}

$U$ is the lattice with basis $e, f$ and $b(e, e) = b(f, f) = 0$, $b(e, f) = 1$.

## Root lattices {#root-lattices}

$X_n$, for $X$ one of $A$, $D$, $E$, is the root lattice of that type: $e_1, \dots, e_n$ is a basis of simple roots, numbered as SageMath's `CartanMatrix` numbers them, and $b(e_i, e_j)$ is the entry $(i, j)$ of the Cartan matrix.
$\widetilde{X}_n$ is the root lattice of the affine root system of that type: the basis is a basis of simple roots, numbered as SageMath's `CartanMatrix` numbers them, and $b(e_i, e_j)$ is the entry $(i, j)$ of the affine Cartan matrix.
[Roots](roots.html) defines the roots of a lattice.

$D_n^+$ is the lattice in $\mathbb{Q}^n$, with the standard form, that $D_n = \{x \in \mathbb{Z}^n : x_1 + \dots + x_n \text{ even}\}$ and the vector $(\tfrac{1}{2}, \dots, \tfrac{1}{2})$ generate.

## Dual lattices {#dual-lattices}

$L^*$ is the [dual lattice](discriminant-forms.html#dual-lattice) of $L$.
The record of $L^*$, for $L$ a record, has the basis $e_1^*, \dots, e_n^*$ with $b(e_i^*, e_j) = \delta_{ij}$, dual to the basis of the record of $L$.
