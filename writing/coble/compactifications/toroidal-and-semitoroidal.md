# Toroidal and semitoroidal compactifications

::: {.Remark}
### Orientation

This section collects the general definitions of the compactification types used throughout the monograph -- toroidal, semitoroidal, KSBA, and Looijenga compactifications, together with generalized Coxeter semifans and recognizable divisors.
The material here is background and vocabulary: it fixes the constructions in their natural generality.
The Coble-specific application of these constructions -- the KSBA stable pair, the restricted ramification semifan, and the comparison between the two compactifications -- is developed in the Stable Limits section; see in particular \longref{conj:restricted_ramification_semifan} and \longref{conj:ksba_semitoroidal_comparison}.
:::

## Toroidal compactifications

::: {.Definition #def:toroidal-compactification}

A **toroidal compactification** $\torcpt{\FG}$ refines the singular cusps of the Baily--Borel compactification by choosing an admissible rational polyhedral fan $\torfan_I$ for each cusp $I$.

Locally, the boundary is modeled on toric varieties $X_{\torfan_I}$.
This resolves the singularities of $\bbcpt{\FG}$, providing a proper algebraic variety with a divisorial boundary (often snc).

The choice of fans makes the construction non-canonical.
However, it often allows the extension of period maps and universal families over boundary strata.
There is a proper $\Gamma$-equivariant morphism $\torcpt{\FG} \to \bbcpt{\FG}$.
:::

## Semitoroidal compactifications

::: {.Definition #def:semitoroidal-compactification}

Introduced by Looijenga [@Loo02], a **semitoroidal compactification** $\semitorcpt{\FG}$ replaces the strict fans of toroidal compactifications with $\Gamma$-admissible **semifans** $\mathcal{F}_I$.

A semifan relaxes the conditions of a fan by not requiring local finiteness or full support.
This allows "partial" toroidalization at selected cusps while leaving others untouched or less refined.

Semitoroidal compactifications sit in a tower of proper birational morphisms:
$$
\torcpt{\FG} \too
\semitorcpt{\FG} \too
\bbcpt{\FG}
.
$$
They are critical for modeling KSBA boundaries where fans may be infinitely generated or accumulate.
:::

::: {.Theorem #thm:tower-semitoroidal}

Any normal compactification admitting a tower
$$
\torcpt{\FG} \too
\semitorcpt{\FG} \too
\bbcpt{\FG}
$$
as in \longref{def:semitoroidal-compactification} is isomorphic to a semitoroidal compactification [@AE23, Thm. 1].
:::

::: {.Remark}
### Polarized Coble trace restriction

The polarized Coble compactification program does not build a new semifan from scratch; it uses a Coble-specific restriction of the Enriques ramification semifan.
Concretely, one takes the **trace** of the Enriques ramification semifan on a Coble hyperplane, together with an admissibility condition selecting which restricted walls survive.
This is the semitoroidal side of the Coble comparison problem, recorded here as \longref{conj:restricted_ramification_semifan}; the trace identity is not yet proved, and is kept explicitly conjectural.
:::

## Generalized Coxeter semifans

::: {.Definition #def:generalized-coxeter-semifan}

The main geometric application of folded Coxeter--Vinberg diagrams is the construction of semitoroidal compactifications of moduli spaces $\FG$ via **generalized Coxeter semifans**.

For a $0$-cusp with Coxeter diagram $G(\Gamma_\eta)$, partition the simple roots into $\Phi = \Phi^{\relevant} \sqcup \Phi^{\irrelevant}$ [@AT17]:

- **Irrelevant roots** ($\Phi^{\irrelevant}$): correspond to strata that are contracted in the KSBA stable model over $\eta$.

- **Relevant roots** ($\Phi^{\relevant}$): the active walls where combinatorial types of stable models change.

The **generalized Coxeter semifan** $\mathcal{F}_{\mathrm{gen}}$ is obtained by omitting the walls defined by irrelevant roots [@AT17, Def. 4.16]. Its maximal cones are unions of Weyl chambers $g\big(\Union_{h \in W^{\irrelevant}} h(\mathfrak{C})\big)$.
:::

::: {.Remark}
### Toroidal versus strictly semitoroidal

Unlike classical toroidal compactifications, where all walls of the Weyl chamber are preserved, semitoroidal compactifications allow certain irrelevant roots to be removed.
The distinction between toroidal and strictly semitoroidal behavior depends on the order of the irrelevant root subgroup $W^{\irrelevant}$:

- **Toroidal**: $|W^{\irrelevant}| < \infty$ (finite irrelevant subgroups).

- **Strictly semitoroidal**: $|W^{\irrelevant}| = \infty$ (infinite irrelevant subgroups, so the semifan is not locally finite).
:::

::: {.Remark}
### Polarized Coble trace picture

For the polarized Coble program, the generalized Coxeter semifan of the Enriques cusp is restricted to a Coble hyperplane: one asks for the trace of the Enriques ramification semifan on that hyperplane, together with an admissibility condition determining which restricted walls survive.
Under the proposed restriction, a Coble wall is irrelevant precisely when every Enriques wall restricting to it is already irrelevant; see \longref{conj:restricted_ramification_semifan}.
:::

## KSBA compactifications

::: {.Definition #def:ksba-compactification}

The **KSBA compactification** generalizes the Deligne--Mumford compactification of curves to higher dimensions.
It compactifies moduli of varieties of log general type by considering **stable slc pairs** $(X, D)$ [@KS88; @Ale96].

A pair $(X, D = \Sum b_j D_j)$ is **KSBA-stable** if:

1. $X$ is a projective demi-normal variety;

2. $0 < b_j \le 1$;

3. the pair $(X, D)$ has **semi log canonical (slc)** singularities;

4. $K_X + D$ is ample and $\QQ$-Cartier.

For K-trivial varieties (like K3 or Enriques surfaces), one uses pairs $(X, \varepsilon R)$ for $0 < \varepsilon \ll 1$ and a polarizing divisor $R$.
The KSBA moduli space $\overline{F}_\Gamma$ provides a modular, proper, algebraic compactification where boundary divisors correspond to geometric stable degenerations [@AET23; @AEGS25].
:::

::: {.Remark}
### Polarized Coble application

The Coble-specific stable-pair package extracted from this framework -- the descended ramification divisor on the stable quotient surface, together with its KSBA obligations ($\QQ$-Cartierness, ampleness, and slc control) -- is developed in the Stable Limits section rather than restated here.
The resulting comparison target between the KSBA and semitoroidal compactifications remains an open program rather than a settled theorem; see \longref{conj:ksba_semitoroidal_comparison}.
:::

## Looijenga compactifications

::: {.Definition #def:looijenga-compactification}

Let $\cH$ be a $\Gamma$-invariant arrangement of hyperplane sections of the period
domain $D$.
The **Looijenga compactification** $\overline{\Gamma\backslash D}^{\,\cH}$ is the
compactification of the arrangement complement $\Gamma\backslash(D - \cH)$
determined by $\cH$ [@Loo02].
It is a semitoroidal compactification in the sense of
\longref{def:semitoroidal-compactification}, so it sits in the same tower over the
Baily--Borel compactification; the semifan it defines at a $0$-cusp is read off
the traces of the hyperplanes of $\cH$ on the boundary of that cusp.
When $\cH$ is empty the construction returns the Baily--Borel compactification.
:::

::: {.Remark}
### Three semifans, independently determined

Three semifans are in play for a single period domain, and they are produced by
three unrelated inputs:

- the **Coxeter semifan** of a $0$-cusp, cut out by the walls of a fundamental
  chamber of the reflection group of the cusp lattice
  (\longref{def:generalized-coxeter-semifan});

- the **KSBA semifan**, determined by which degenerations of stable pairs occur
  (\longref{def:ksba-compactification}), and in the cases treated here a
  coarsening of the Coxeter semifan obtained by deleting irrelevant walls;

- the **Looijenga semifan** of an arrangement $\cH$, determined by the arithmetic
  of $\cH$ alone.

The identification of a GIT compactification with a Looijenga compactification
therefore carries no information about the KSBA semifan: the two are computed from
different data, and knowing one does not constrain the other.
Where the three sit relative to one another in the refinement order is a question
in its own right, recorded among the open problems.
:::

## Recognizable divisors

::: {.Definition #def:recognizable-divisor}

A polarizing divisor $R$ on the generic surface in $F_S$ is **recognizable** if, for any quasipolarized Kulikov degeneration $\mathcal{X} \to \Delta$, the divisor $R$ extends unambiguously to a flat limit $R_0 \subset \mathcal{X}_0$, unique up to $\operatorname{Aut}^0(\tilde{\mathcal{X}}_0)$ in any other smoothing.
:::

::: {.Theorem #thm:recognizable-semitoroidal}

If $R$ is recognizable, then the normalization of the KSBA compactification $\overline{F}^R$ is isomorphic to a semitoroidal compactification $\overline{F_S}^{\mathcal{F}_R}$, defined by a specific semifan $\mathcal{F}_R$ [@AE23].
:::

::: {.Example #ex:recognizable-divisors}

Two basic examples of recognizable divisors:

1. The **rational curve divisor** $R_{\rcop} = \Sum R_i$ (the sum of all smooth rational curves in $|L|$).

2. The **ramification divisor** $R_\iota$ of a nonsymplectic involution.
:::
