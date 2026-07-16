# Moduli

:::{.remark}

For each $1\leq n \leq 10$, there is a moduli space of Coble surfaces with $n$
boundary components.
As noted, we will primarily be interested in the $n=1$ case.
In this case, we have two distinct constructions of a moduli space of such Coble
surfaces.
Coble surfaces appear as degenerations of Enriques surfaces, and in fact they
form a boundary divisor $\cH_{-2}$ in the 10-dimensional moduli space $F_{\En}$
of Enriques surfaces.
Thus they form a 9-dimensional moduli space.
These are realized by allowing the K3 cover of an Enriques surface to acquire an
$A_1$ singularity fixed by the Enriques involution; the resulting quotient has a
quartic singularity whose resolution is an irreducible smooth rational curve $C$
satisfying $C^2 = -4$, and by [@Nue15 p. 8] is thus a Coble surface $S$.
:::

:::
: {.remark}

Separately, one can construct a Hodge-theoretic period domain directly using
lattice theory [@DM19].
Write $\abs{-2K_S} = \ts{C}$ where $C = C_1 + \cdots + C_n$
has $n$ irreducible components.
By adjunction and the genus formula, $C_i\cong \PP^1$ and $C_i^2 = -4$, so
$K_S^2 = -n$.
Let $\Sigma$ be a sufficiently general Coble point set in $\PP^2$.
There are 10 irreducible families of K3s obtained as the double cover of $S$
branched over $C$, where the fixed locus of the deck transformation is comprised
of $n$ smooth rational curves.
Generally the rank of $\Pic(X)$ is $r=10+n$ and $\ell = 12-n$, and
$K_S^2 = 9 - \abs{\Sigma}$.

```include

```

The case of interest to us is $n=1$, and thus the lattice
$M = (11, 11, 1) = A_1 \oplus E_{10}(2)$ and its complement $N$ in the K3
lattice will be used to construct a period domain quotiented by an appropriate
arithmetic subgroup, producing the coarse moduli space of interest.
::::

::: {.remark}

As described in [@DZ99], the double cover $\pi: X\to S$ realizes $X$ as a
degeneration of a K3 cover of an Enriques surface, which thus describes a family
of K3s equipped with a nonsymplectic involution as studied in
[@AE22] and a corresponding family of Enriques surfaces as studied
in [@AEGS23].
It seems that these degenerations correspond to the (weakly projective)
**flowerpot** degenerations of [@Ols04], and I conjecture that the corresponding
Kulikov models correspond to integral-affine discs (as opposed to spheres or
real projective spaces).
:::
