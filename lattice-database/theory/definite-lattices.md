---
title: Definite lattices
summary: Invariants of definite lattices, and the sign convention for negative definite forms.
order: 6
---

Let $L$ be a [definite](lattices.html#definiteness) lattice.

## Sign convention {#sign}

For $L$ negative definite, the invariants below are those of the twist $L(-1)$.

## Minimum and kissing number {#minimum}

::: {.definition}
The *minimum* of $L$ is the least value of $b(x, x)$ over the nonzero $x \in L$.
The *kissing number* is the number of $x$ with $b(x, x)$ equal to the minimum.
:::

The kissing number is finite because the form is definite.

## Theta series {#theta-series}

::: {.definition}
The *theta series* of $L$ is $\sum_{x \in L} q^{b(x, x)}$.
The coefficient of $q^k$ is the number of $x \in L$ with $b(x, x) = k$.
:::

The page states the theta series when $L$ is [integral](lattices.html#integral).

## Isometry group {#isometry-group}

::: {.proposition}
$O(L)$ is finite, and its order is even for $L \neq 0$.
:::

::: {.proof}
Because the form is definite, the set $V_c = \{x \in L : |b(x, x)| \leq c\}$ is finite for each $c$, and for $c$ large it contains a basis of $L$.
$O(L)$ permutes $V_c$, and an isometry is determined by its values on that basis, so $O(L)$ is finite.
$-1 \in O(L)$ has order 2 for $L \neq 0$.
:::

The order is computed with `qfauto` of PARI/GP.

## Vectors of norm 2 {#norm-two}

$\Phi_{\{2\}}(L) = \{r \in L : b(r, r) = 2\}$ is a set of [roots](roots.html#roots).
By [Witt's theorem](roots.html#definite), $\mathbb{Z}\Phi_{\{2\}}(L)$ is an orthogonal sum of lattices $A_n$, $D_n$, $E_6$, $E_7$ and $E_8$, and the [database](../database.html) states its type for each integral lattice.
The full set of roots $\Phi(L)$ is a [root system](roots.html#definite), with components and simple roots.
