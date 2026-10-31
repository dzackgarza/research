---
unit: reference
status: source-backed
tags:
  - coble
  - classification
  - automorphisms
  - halphen
---

# Structure and classification facts for Coble surfaces

::: {.provenance title="Provenance"}
Archived Coble-surface, Coble-moduli, and introductory reading notes dated 2023-03 to 2024-05. These are the author's notes on Dolgachev-Zhang 1999, Dolgachev's 1988 monograph, Dolgachev-Kondo 2013, and Cossec-Dolgachev-Liedtke.
:::

Everything here is literature, not new work.
It is recorded because the project's own `content_pandoc/sections/Coble_Surfaces/` carries the definition, the terminal/minimal distinction and the basic-rational property, but none of the items below.
Each was checked absent from `content_pandoc` and `knowledge` before being written down.

## Negative curves

::: {.proposition title="Norms of smooth rational negative curves"}

Let $S$ be a Coble surface with anti-bicanonical divisor $D$.
Every smooth rational negative curve $E \iscontainedin S$ satisfies
$$
E^2 \in \theset{-1,\, -2,\, -4},
$$
and if $E^2 = -4$ then $E$ is a component of $D$.
:::

::: {.proof}

Cited: [@DZ99, §2] for the trichotomy of the norm.
The proof block records why the trichotomy is three values and not more, since that is what the rest of the page uses.

Adjunction on the smooth rational curve $E$ gives $E^2 = -2 - E\cdot K_S$, so the possible values of $E^2$ are read off the intersection numbers of $E$ with $-K_S$.
A Coble surface has $|-2K_S| = \{D\}$ with $D$ nonempty and $D$ a sum of $(-4)$-curves, so $-K_S = \tfrac12 D$ is not integral but $2(-K_S)=D$ is effective.
For $E$ not a component of $D$ the intersection $E\cdot D$ is a nonnegative even integer, $E\cdot K_S = -\tfrac12 E\cdot D$, and $E^2 = -2+\tfrac12 E\cdot D$; the values $E\cdot D = 0, 2$ give $E^2 = -2, -1$, and $E\cdot D\geq4$ would give $E^2\geq0$, contradicting negativity.
For $E$ a component of $D$ one has $D = E + D'$ with $D'$ effective and not containing $E$, and $E^2 = -4$ is the value forced by the classification of the components of $D$.
:::

This is the fact that makes the $(-4)$-curves intrinsic: they cannot occur away from the boundary.
It is the surface-level counterpart of the $-2$ / $-4$ norm dichotomy that governs the Coxeter diagrams in [Explicit root vectors and the folded Sterk diagrams](#sec-root-vectors-and-folded-sterk-diagrams).

## Automorphisms

::: {.theorem title="Coble's theorem, lattice form"}

Write $M_S \definedas K_S^{\perp\, \Pic(S)}$.
Then $\Aut(S)$ is isomorphic to a finite-index subgroup $H \leq \Orth(M_S)$, and
$$
\Orth(M_S)/\theset{\pm1} \cong W(E_{10}).
$$
For general $C$, $H \cong W(E_{10})(2)$, the level 2 congruence subgroup.
:::

::: {.proof}

Cited: [@Dol88] for the description of $\Aut(S)$ through the action on $M_S$, and [@CDL25, Ch. 5] for the level 2 structure.

What the statement adds to the citation is the reading of the two groups, and that is what the page uses.
$\Aut(S)$ acts on $\Pic(S)$ preserving $K_S$ and the intersection form, hence on $M_S = K_S^{\perp\,\Pic(S)}$; that the resulting homomorphism is injective with finite image is the cited part, and the image is the group $H$.
$\Orth(M_S)/\{\pm1\}\cong W(E_{10})$ identifies the *full* orthogonal group with the Coxeter group, so the quotient is by the central $\pm1$ and not by anything else; for general $C$ the finite-index subgroup $H$ is then the level 2 congruence subgroup of that $W(E_{10})$.
The two statements are therefore consistent, and the difference between them is the difference between the full orthogonal group and the image of one particular surface's automorphism group.
:::

The project's introduction records $\Aut(S)\cong W(E_{10})$ for general $C$; the refinement to the level 2 congruence subgroup, and the quotient statement for $\Orth(M_S)$, are the sharper forms.

::: {.remark title="Finiteness of negative curves modulo automorphisms"}

Let $A_1(S)^{\mathrm{sm,rat},<0}$ denote the smooth rational curves of negative self-intersection.
Then $A_1(S)^{\mathrm{sm,rat},<0}/\Aut(S)$ is **finite**: up to automorphism a Coble surface carries only finitely many smooth rational negative curves.
Classifying all surfaces with this property is an open question recorded in the source.
:::

## The Coble-Mukai lattice

::: {.definition title="Coble-Mukai lattice"}

With $B_1,\ldots,B_n$ the boundary components, set
$$
L \definedas \generators{\NS(S),\ \tfrac12 B_1 + \cdots + \tfrac12 B_n}_\ZZ,
\qquad
\CM(S) \definedas \generators{B_1,\ldots,B_n}_\ZZ^{\perp L}.
$$
$\CM(S)$ serves as the replacement for $\NS(S)$ in the Coble setting.
:::

This object appears nowhere in the project, which works throughout with $S_{\Co}$ and $T_{\Co}$ inside $\lkt$.
Whether $\CM(S)$ relates to $S_{\Co}$, and whether it is the more natural home for the $\Gamma_{\Co}$ action, is not addressed in the source and looks worth settling.

## The Dolgachev-Zhang classification

::: {.definition title="Elliptic and rational types"}

A Coble surface is of **elliptic type** when there is $S \birationaliso Y$ with $|-K_Y|$ a singleton and the mobile part of $|-2K_Y|$ generically a smooth elliptic curve.
Elliptic type splits further:

- **Halphen type**: blowups of singular points, and their infinitely near points, on a non-multiple fibre of a minimal rational elliptic surface with one multiple fibre of multiplicity 2.

- **Jacobian type**: blowdowns of disjoint sections, and possibly components of one fibre, of a non-minimal rational elliptic surface with a section.

It is of **rational type** when the mobile part of $|-2K_Y|$ consists of divisors $D$ with $p_a(D) = 0$, $D$ not necessarily irreducible.
These are blowups of minimal rational surfaces.
:::

::: {.theorem title="K3 type criterion, Dolgachev-Zhang Thm. 6.5"}

Let $X$ be a Coble surface with $M^2 = 0$.

- If $X$ is of Halphen type, obtained from a minimal Halphen surface $Y_m$ of index 2 by one blowup of a singular point on its non-multiple fibre $F$, then $X$ is of K3 type **if and only if** $F$ has type $I_n$, $\II$, $\III$ or $\IV$.

- If $X$ is of Jacobian type, obtained from a minimal Jacobian rational elliptic surface by blowing up a singular point of one fibre $F$ and at least one singular point, with infinitely near points, on another fibre $F_1$, then $X$ is of K3 type **if and only if** each of $F$ and $F_1$ has type $I_n$, $\II$, $\III$ or $\IV$.
:::

::: {.proof}

This is [@DZ99, Thm. 6.5], stated here with its hypotheses spelled out because the page's use of it depends on them: $M^2 = 0$ is required, and in each branch the surface must be obtained by exactly the blowups described, at singular points of the stated fibres.

The list $I_n, \II, \III, \IV$ is the list of fibre types whose Kodaira type is not multiple, i.e. the fibre is reduced; a fibre of type $I_n^*$, $\II^*$, $\III^*$ or $\IV^*$ is not, and that is the content of the criterion, not an additional condition.
:::

::: {.lemma title="Dolgachev-Zhang Lem. 6.2"}

For a Coble surface $X$ the following are equivalent:

1. $|-2K_X|$ contains a reduced divisor;

2. there is a double cover $\tilde X \to X$ with $\tilde X$ a K3 surface having at worst ordinary double points.
:::

::: {.proof}

This is [@DZ99, Lem. 6.2].
The mechanism, worth recording because it is used throughout the Coble literature: $|-2K_X|$ nonempty is the datum of a $\bZ/2$-cover, branched over a divisor in that class, and the condition that a member be reduced is what keeps the branch divisor smooth enough for the cover to have only ordinary double points.
Without a reduced member the cover acquires worse singularities along the non-reduced part.
:::

::: {.remark title="Why this matters for the Halphen program"}

The project's [Halphen surfaces](#sec-halphen-surfaces) note records the Coble-to-Halphen blowdown and conjectures a correspondence of moduli spaces along the $g=0$ line of Nikulin's triangle; see [Moduli of index 2 Halphen and rational elliptic surfaces](#sec-halphen-index-2-moduli-program). The elliptic/rational dichotomy and Theorem 6.5 are the classification that the conjecture must respect: they say exactly which Halphen and Jacobian configurations produce K3-type Cobles, and so which fibres of the conjectured correspondence are nonempty.
The Jacobian branch has no counterpart anywhere in the project.
:::

## Rational log Enriques surfaces of index 2

::: {.definition title="Rational log Enriques surface of index 2"}

A normal rational surface $\bar X$ with at worst quotient singularities such that $\OO(-2K_{\bar X}) \cong \OO_{\bar X}$.
:::

::: {.theorem title="Terminal Cobles are resolutions of these"}

A terminal Coble surface is the minimal resolution of a **maximum** rational log Enriques surface of index 2. Conversely, the minimal resolution $X$ of a rational log Enriques surface $\bar X$ of index 2 is a Coble surface with $h^0(-2K_X) = 1$, whose unique member $D \in |-2K_X|$ is reduced and each of whose connected components is either a single $(-4)$-curve or a linear chain with a prescribed dual graph.
:::

::: {.proof}

Cited: [@DZ99, §3] for both directions.

The characterization is a minimal-resolution statement and its content is which surfaces resolve to a terminal Coble.
Resolving a rational log Enriques surface of index 2 replaces the quotient singularities by configurations of rational curves, and terminality of the resolution is exactly the condition that no $(-1)$-curve remains, which is what forces each connected component of the exceptional divisor to be a single $(-4)$-curve or a chain of the stated shape.
The converse direction is the same computation read backwards, together with $h^0(-2K_X)=1$: on a Coble surface $|-2K_X|$ is a single member, so the resolution contributes no further sections.

The dual graph of the chains is a hand-drawn figure in the source and was not transcribed here; it must be recovered from [@DZ99, §3] before the characterization is used.
:::

## Dolgachev-Kondo geometry of the degree 2 polarization

The project's [geometric stable-limits note](#sec-geometric-preliminaries) records the map $\phi_{ij}$ onto a quartic del Pezzo surface and the key fact that it is **never finite** in the Coble case.
The following incidence data accompanying it is absent.

::: {.remark title="The branch geometry"}

Take $h = [F_1 + F_2] \in \Pic(S)$ of degree 2, so $|h|$ defines $\phi_{|h|}: S \to \PP^4$ with image $D$ a 4-nodal quartic del Pezzo surface.
Let $\sigma$ be the deck transformation.
Then:

- $\Fix(\sigma) = \bar W$ is a smooth genus 4 curve together with 3 isolated points;

- $\phi_h(C) = \theset{q}$ is a **singular point** of $D$, where $C \in |-2K_S|$ is the Coble curve;

- $\bar W \intersect C = \theset{p_1, p_2}$;

- $W \definedas \phi_h(\bar W)$ has $p_a(W) = 5$ and a double point at $q$.

A Coble surface arises as a degeneration of an Enriques surface exactly when the branch curve $W$ passes through a singular point of $D$.
:::

::: {.remark title="The rationality correspondence in its explicit form"}

Dolgachev-Kondo prove $\fco$ rational by comparison with $\mcm_{\cusp} = U/\PGL_3$, the moduli of cuspidal plane quintics.
They show $\mcm_{\cusp} \birationaliso \mcm_{\En}$, which is 10-dimensional, and that a distinguished codimension one locus $\mcm'_{\cusp} \cong \mcm_{\Co}$.
The locus is explicit: for $C$ a plane quintic with cusp $p$ and $L$ the tangent line to $C$ at $p$, it is the case where $L$ is **also** tangent to $C$ at a smooth point $q \in C$.

The project states only that $\fco$ is rational "by relating it to a codimension one subvariety of a moduli space of certain $A_2$-singular quintics".
The tangency condition above is what cuts out that subvariety.
:::

Related: [The research program for $F_{\Co,n}$, $2 \leq n \leq 10$](#sec-coble-families-research-program), [Moduli of index 2 Halphen and rational elliptic surfaces](#sec-halphen-index-2-moduli-program), [The Coble cusp correspondence and the morphism chain](#sec-cusp-correspondence-morphism-chain).
