# Anticanonical pairs, charge, and MMP singularities

::: {.remark title="Orientation"}

The components of a Type III degeneration are anticanonical pairs, and the combinatorics of such degenerations is controlled by a single additive invariant, the *charge*. We collect the definitions here, together with the singularity classes of the minimal model program that govern which limits are admissible in KSBA moduli.
:::

## Anticanonical pairs and their charge

::: {.definition ref="def:anticanonical-pair"}

An **anticanonical pair** $(V, D)$ consists of a smooth projective rational surface $V$ together with a reduced effective snc divisor $D$ such that
$$
K_V + D \sim_{\QQ} 0
.
$$
Anticanonical pairs are also known as **log Calabi--Yau surfaces**.
:::

::: {.definition ref="def:charge"}

The **charge** of an anticanonical pair $(V, D)$, with $D = \sum_j D_j$ its decomposition into irreducible components, measures the deviation of $(V, D)$ from being toric.
It is defined by
$$
Q(V, D) \da 12 - \sum_j \left( D_j^2 + 3 \right)
.
$$
For a toric surface $V$ with $D = \partial V$ its toric boundary, the charge vanishes:
$$
Q(V, \partial V) = 0
.
$$
:::

::: {.proposition ref="prop:charge-under-blowup" title="Charge under blowup"}

The charge behaves as follows under blowups of an anticanonical pair:

- **Corner blowups**, at nodes of $D$ (points where two components of $D$ meet), preserve the charge.

- **Interior blowups**, at smooth points of $D$ (points lying on a single component of $D$), increase the charge by $1$.

\todo{cite: reference for the charge formula and its blowup behaviour (Friedman/Engel--Friedman on anticanonical pairs); the migrated note gives no citation.}
:::

::: {.theorem ref="thm:friedman-morrison-charge" title="Friedman--Morrison charge theorem"}

Let $\cX \to (C, 0)$ be a Type III Kulikov degeneration of $K3$ surfaces with central fiber
$$
\cX_0 = \bigcup_{i=1}^n V_i
,
$$
and for each component set
$$
D_i \da V_i \intersect \overline{\left( \cX_0 \setminus V_i \right)}
,
$$
so that each $(V_i, D_i)$ is an anticanonical pair.
Then the sum of the charges of all components is exactly $24$:
$$
\sum_{i=1}^n Q(V_i, D_i) = 24
.
$$
This imposes severe constraints on the possible combinatorial types of degenerations.

\todo{cite: Friedman--Morrison charge theorem; the migrated note names the result but supplies no citation key.}
:::

## Singularities in the minimal model program

::: {.definition ref="def:discrepancy"}

Let $(X, D)$ be a normal pair with $K_X + D$ $\QQ$-Cartier, and let $f\colon Y \to X$ be a log resolution.
The **discrepancy** $a(E, X, D)$ of a divisor $E$ over $X$ is defined by
$$
K_Y + D_Y = f^*(K_X + D) + \sum_E a(E, X, D)\, E
.
$$
:::

::: {.definition ref="def:mmp-singularities"}

With discrepancies as in \cref{def:discrepancy}, the pair $(X, D)$ has the following classes of singularities, according to the values taken by $a(E, X, D)$ over all divisors $E$ over $X$:

- **Terminal**: $a(E, X, D) > 0$.

- **Canonical**: $a(E, X, D) \geq 0$.

- **Kawamata log terminal (klt)**: $a(E, X, D) > -1$.

- **Log canonical (lc)**: $a(E, X, D) \geq -1$.
  This is the maximal class in which the minimal model program works.

The definitions of these singularity classes follow [@KM98].
:::

::: {.definition ref="def:demi-normal-slc"}

For non-normal varieties one has the following notions.

- A variety $X$ is **demi-normal** if it is reduced, satisfies Serre's condition $S_2$, and has at worst normal crossings in codimension $1$.

- A pair $(X, D)$ is **semi-log canonical (slc)** if $X$ is demi-normal and the normalization, taken with the conductor divisor, $(X^\nu, D^\nu)$ is log canonical.

Being slc is the condition required for limits in KSBA moduli spaces.
:::

\todo{The migrated note lists "dlt" among its aliases but its body gives no definition of dlt (divisorial log terminal); definition omitted here rather than invented.}
