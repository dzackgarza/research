---
title: Definite lattices
summary: Invariants of definite lattices, and the sign convention for negative definite forms.
order: 6
---

Let $L$ be a [definite](lattices.html#definiteness) lattice.

## Sign convention {#sign}

For $L$ negative definite, the invariants below are those of the twist $L(-1)$.

## Minimum and kissing number {#minimum}

The *minimum* of $L$ is the least value of $b(x, x)$ over the nonzero $x \in L$.
The *kissing number* is the number of $x$ with $b(x, x)$ equal to the minimum; it is finite because the form is definite.

## Theta series {#theta-series}

The *theta series* of $L$ is $\sum_{x \in L} q^{b(x, x)}$.
The coefficient of $q^k$ is the number of $x \in L$ with $b(x, x) = k$.
The page states it when $L$ is [integral](lattices.html#integral).

## Isometry group {#isometry-group}

$O(L)$ is finite because the form is definite.
$-1 \in O(L)$, so the order of $O(L)$ is even for $L \neq 0$.
The order is [declared](records.html#declared); the notes cite its source.

## Vectors of norm 2 {#norm-two}

$\Phi_{\{2\}}(L) = \{r \in L : b(r, r) = 2\}$ is a set of [roots](roots.html#roots).
By [Witt's theorem](roots.html#definite), $\mathbb{Z}\Phi_{\{2\}}(L)$ is an orthogonal sum of lattices $A_n$, $D_n$, $E_6$, $E_7$ and $E_8$, and the page of an integral lattice states its type.
The full set of roots $\Phi(L)$ is a [root system](roots.html#definite), with components and simple roots.
