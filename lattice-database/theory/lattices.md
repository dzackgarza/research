---
title: Lattices
summary: Lattices, the basis and the Gram tensor of a record, orthogonal sums, twists, and the invariants that every record states.
order: 2
---

## Lattices {#lattices}

A *lattice* here is a free $\mathbb{Z}$-module $L$ of finite rank $n$ with a symmetric bilinear form $b \colon L \times L \to \mathbb{Q}$.
The form can be definite, indefinite or degenerate, and its values need not be integers.
An *isometry* $\varphi \colon L \to M$ is an isomorphism of modules with $b_M(\varphi x, \varphi y) = b_L(x, y)$ for all $x, y \in L$.
$O(L)$ is the group of the isometries $L \to L$.

## Gram tensor {#gram-tensor}

Each record fixes a basis $e_1, \dots, e_n$ of $L$, the *basis of the record*. The *Gram tensor* is the form $b$, a symmetric $(0, 2)$-tensor, and the record states its components $b(e_i, e_j)$: row $i$ lists $b(e_i, e_1), \dots, b(e_i, e_n)$.
A page writes a vector of $L$ by its coordinates in the basis of the record.
[Named lattices](named-lattices.html) gives the basis of each named lattice.

## Orthogonal sums {#orthogonal-sums}

$L = M_1 \oplus M_2$ is an *orthogonal sum* when $L$ is the direct sum of the submodules $M_1$ and $M_2$ and $b(x, y) = 0$ for $x \in M_1$, $y \in M_2$.
The basis of an orthogonal sum is the union of the bases of the summands, in the order written.
$L^k$ is the orthogonal sum of $k$ copies of $L$.

The page of a lattice states the orthogonal decomposition that the basis of its record gives.
It is the finest partition of $e_1, \dots, e_n$ into parts with $b(e_i, e_j) = 0$ for $e_i$, $e_j$ in different parts, and $L$ is the orthogonal sum of the sublattices that the parts generate.

## Twists {#twists}

For $k \in \mathbb{Q}^\times$, the *twist* $L(k)$ is the module $L$ with the form $k b$.

## Determinant and signature {#signature}

The *determinant* of $L$ is $\det(b(e_i, e_j))$.
It is the same for every basis of $L$: a change of basis by $P \in \mathrm{GL}_n(\mathbb{Z})$ multiplies it by $\det(P)^2 = 1$.

The *signature* $(n_+, n_-)$ gives the numbers of $v$ with $b(v, v) > 0$ and with $b(v, v) < 0$ in a $b$-orthogonal basis of $L \otimes \mathbb{Q}$.
They do not depend on the basis (Sylvester's law of inertia).

## Definiteness {#definiteness}

$L$ is *positive definite* or *negative definite* when $b(x, x)$ has one sign on the nonzero $x$, and *indefinite* when $b(x, x)$ takes both signs.
It is *positive semidefinite* or *negative semidefinite* when $b(x, x)$ has one sign and the determinant is zero, and *zero* when $b = 0$.
[Definite lattices](definite-lattices.html) and [indefinite lattices](indefinite-lattices.html) give the invariants that a record states under each hypothesis.

## Degenerate lattices {#degenerate}

The *correlation* of $L$ is the map $L \to \operatorname{Hom}(L, \mathbb{Q})$, $x \mapsto b(x, -)$.
Its kernel is the *radical* of $b$, of rank $n - n_+ - n_-$.
$L$ is *degenerate* when the radical is not zero, which is when the determinant is $0$.
The discriminant group and the genus symbol are defined for nondegenerate lattices only.

## Integral lattices {#integral}

$L$ is *integral* when $b(x, y) \in \mathbb{Z}$ for all $x, y \in L$, which is when every $b(e_i, e_j)$ is an integer.
An integral lattice is *even* when $b(x, x)$ is even for every $x \in L$, and *odd* otherwise; this is its *parity*. [Dual lattices and discriminant groups](discriminant-forms.html) gives the invariants of an integral lattice that is nondegenerate.
