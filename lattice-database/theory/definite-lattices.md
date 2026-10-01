---
title: Definite lattices
summary: The invariants that a record of a definite lattice states, and the sign convention for negative definite forms.
order: 6
---

Let $L$ be a [definite](lattices.html#definiteness) lattice.

## Sign convention {#sign}

The invariants of a definite record are stated for a positive definite form.
On a negative definite lattice they are the invariants of $-b$.

## Minimum and kissing number {#minimum}

The *minimum* of $L$ is the least value of $b(x, x)$ over the nonzero $x \in L$.
The *kissing number* is the number of $x$ with $b(x, x)$ equal to the minimum; it is finite because the form is definite.

## Theta series {#theta-series}

The *theta series* of $L$ is $\sum_{x \in L} q^{b(x, x)}$.
The coefficient of $q^k$ is the number of $x \in L$ with $b(x, x) = k$.
A record states it when $b$ has integer values.

## Isometry group {#isometry-group}

$O(L)$ is finite because the form is definite.
A record can declare its order; the build checks only that it is even, and the notes give its source.

## Vectors of norm 2 {#norm-two}

$\Phi_{\{2\}}(L) = \{r \in L : b(r, r) = 2\}$ is a set of [roots](roots.html#roots).
By Witt's theorem (Conway and Sloane, *Sphere Packings, Lattices and Groups*, 3rd edition, Chapter 4, §3), $\mathbb{Z}\Phi_{\{2\}}(L)$ is the orthogonal sum of root lattices of types $A_n$, $D_n$, $E_6$, $E_7$ and $E_8$, and a record of an integral lattice states that type.
$\mathbb{Z}\Phi_{\{2\}}(L)$ is not primitive in $L$ in general.
[Roots](roots.html#definite) gives the full root system $\Phi(L)$, its components and their simple roots.
