---
title: Reduction modulo p and zeta functions
summary: The primes of bad reduction of the quadric Q(x) = n, the character of the discriminant, the points over finite fields, and the zeta functions.
order: 11
---

Let $L$ be an [integral](lattices.html#integral) lattice of rank $r$ that is [nondegenerate](lattices.html#degenerate), with Gram tensor $G$ in the chosen basis.
Let $Q(x) = b(x, x) = x^{t} G x$, and for an integer $n$ let $X_n$ be the closed subscheme $Q(x) = n$ of the affine space $\mathbb{A}^r_{\mathbb{Z}}$.
$X_0$ is the cone of isotropic vectors.

## Primes of bad reduction {#bad-reduction}

::: {.definition}
The *primes of bad reduction* of $L$ are the primes $\Sigma_L = \{p : p \mid 2 \det L\}$.
:::

For an odd prime $p$, $Q$ modulo $p$ is a nondegenerate quadratic form over $\mathbb{F}_p$ exactly when $p \nmid \det L$.
Modulo 2, $Q(x) = \sum_i b(e_i, e_i) x_i^2$ is the square of a linear form, so $2 \in \Sigma_L$ for every $L$.
For $n \neq 0$ and $p \notin \Sigma_L$ with $p \nmid n$, the gradient $2 G x$ of $Q$ is zero modulo $p$ only at $x = 0$, which is not on $X_n$; so $X_n$ is smooth over $\mathbb{Z}[1/(2 n \det L)]$.
The record states $\Sigma_L$ as `integral.bad_reduction_primes`.

## The character of the discriminant {#character}

::: {.definition}
Let $r = 2m$ be even and $D = (-1)^m \det L$.
The record states as `integral.quadratic_character` the discriminant $d$ of the field $\mathbb{Q}(\sqrt{D})$, and $1$ when $D$ is a square.
For $p \notin \Sigma_L$, $\chi_D(p)$ is the Kronecker symbol $(d / p)$, which is the Legendre symbol $(D / p)$.
:::

Every nondegenerate quadratic space over a finite field $\mathbb{F}_q$ of odd characteristic is isomorphic to exactly one of $mH \oplus c x^2$ in dimension $2m + 1$, and $mH$ or $(m - 1)H \oplus N$ in dimension $2m$, where $H$ is the hyperbolic plane and $N$ is the norm form of $\mathbb{F}_{q^2}$ (Casselman, *Quadratic forms over finite fields*, 2018, Theorem 1.6, [PDF](https://personal.math.ubc.ca/~cass/research/pdf/FiniteFields.pdf)). The determinant of $H$ is $-1$ and that of $N$ is $-1$ times a nonsquare, up to squares.
So $Q$ modulo $p$ is $mH$ exactly when $\chi_D(p) = 1$.
Over $\mathbb{F}_{p^k}$ the same holds with $\chi_D(p)^k$, because an element of $\mathbb{F}_p^{\times}$ is a square in $\mathbb{F}_{p^k}$ exactly when it is a square in $\mathbb{F}_p$ or $k$ is even.

## Points over finite fields {#points}

Let $p \notin \Sigma_L$, $q = p^k$ and $\chi = \chi_D(p)^k$.
Casselman (§3, cases 4 and 5) counts the points of $mH$ and $(m - 1)H \oplus N$, which gives for $r = 2m$:

|  | $n = 0$ | $n \neq 0$, $p \nmid n$ |
| --- | --- | --- |
| $\lvert X_n(\mathbb{F}_q) \rvert$ | $q^{2m - 1} + \chi\, q^{m} - \chi\, q^{m - 1}$ | $q^{2m - 1} - \chi\, q^{m - 1}$ |

For $r = 2m + 1$, $Q \cong mH \oplus c x^2$ with $c = (-1)^m \det L$ up to squares.
A point of $mH \oplus c z^2$ with value $n$ is a $z$ and a point of $mH$ with value $n - c z^2$.
The value $0$ is taken $1 + \left(\frac{nc}{q}\right)$ times by $c z^2 - n$, and $mH$ takes the value $0$ at $q^{2m - 1} + q^m - q^{m - 1}$ points and each other value at $q^{2m - 1} - q^{m - 1}$ points, so for $p \nmid n$:

$$\lvert X_n(\mathbb{F}_q) \rvert = q \left(q^{2m - 1} - q^{m - 1}\right) + \left(1 + \left(\tfrac{nc}{q}\right)\right) q^m = q^{2m} + \left(\tfrac{D_n}{p}\right)^k q^m, \qquad D_n = (-1)^m n \det L.$$

Also $\lvert X_0(\mathbb{F}_q) \rvert = q^{2m}$.
Casselman's case 6 prints $\operatorname{sgn}(-x/c)$ in place of $\left(\frac{xc}{q}\right)$; the count above gives the sign.

For $G$ the identity matrix, $\det L = 1$ and the counts for $n = 1$ are those of Ireland and Rosen, *A Classical Introduction to Modern Number Theory*, 2nd edition, Springer, Proposition 8.6.1.

## Zeta functions {#zeta}

::: {.definition}
For a finite set $\Sigma$ of primes that contains $\Sigma_L$, the partial zeta function of $X_n$ is $\zeta^\Sigma(X_n, s) = \prod_{p \notin \Sigma} Z_p(X_n, p^{-s})$, with $Z_p(X_n, T) = \exp\left(\sum_{k \geq 1} \lvert X_n(\mathbb{F}_{p^k}) \rvert\, T^k / k\right)$.
Also $\zeta^\Sigma(s) = \prod_{p \notin \Sigma} (1 - p^{-s})^{-1}$ and $L^\Sigma(s, \chi) = \prod_{p \notin \Sigma} (1 - \chi(p) p^{-s})^{-1}$.
:::

A count $\sum_j \pm a_j^k$ gives $Z_p = \prod_j (1 - a_j T)^{\mp 1}$, because $\sum_k a^k T^k / k = -\log(1 - aT)$.
So the counts of the [points](#points) give, with $\Sigma = \Sigma_L$ for $n = 0$ and $\Sigma = \Sigma_L \cup \{p : p \mid n\}$ for $n \neq 0$:

|  | $\zeta^\Sigma(X_0, s)$ | $\zeta^\Sigma(X_n, s)$, $n \neq 0$ |
| --- | --- | --- |
| $r = 2m$ | $\dfrac{\zeta^\Sigma(s - 2m + 1)\, L^\Sigma(s - m, \chi_D)}{L^\Sigma(s - m + 1, \chi_D)}$ | $\dfrac{\zeta^\Sigma(s - 2m + 1)}{L^\Sigma(s - m + 1, \chi_D)}$ |
| $r = 2m + 1$ | $\zeta^\Sigma(s - 2m)$ | $\zeta^\Sigma(s - 2m)\, L^\Sigma(s - m, \chi_{D_n})$ |

When $D$ is a square, $\chi_D$ is trivial and $L^\Sigma(s, \chi_D) = \zeta^\Sigma(s)$.
For example, $E_8$ has $r = 8$ and $\det = 1$, so $\zeta^\Sigma(X_n, s) = \zeta^\Sigma(s - 7) / \zeta^\Sigma(s - 3)$ with $\Sigma = \{2\} \cup \{p : p \mid n\}$.
$A_2$ has $r = 2$ and $\det = 3$, so $D = -3$ and $\zeta^\Sigma(X_0, s) = \zeta^\Sigma(s - 1)\, L^\Sigma(s - 1, \chi_{-3}) / L^\Sigma(s, \chi_{-3})$ with $\Sigma = \{2, 3\}$.

The page of a lattice states these functions for its $r$, $\det L$ and $\chi_D$.
