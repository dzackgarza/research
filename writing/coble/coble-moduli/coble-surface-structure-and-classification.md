---
title: Structure and classification facts for Coble surfaces
unit: reference
status: source-backed
tags:
  - coble
  - classification
  - automorphisms
  - halphen
---

# Structure and classification facts for Coble surfaces

**Provenance.** `/home/dzack/gitclones/diss/100-corpus/100-data/dzg-research/coble-research/canonical/my_coble_notes/`, files `Coble Surfaces.md`, `moduli of Cobles.md` (Obsidian reading notes dated 2023-03 to 2024-05) and `000_Introduction.md`. These are the author's notes on Dolgachev-Zhang 1999, Dolgachev's 1988 monograph, Dolgachev-Kondo 2013, and Cossec-Dolgachev-Liedtke.

Everything here is literature, not new work.
It is recorded because the project's own `content_pandoc/sections/Coble_Surfaces/` carries the definition, the terminal/minimal distinction and the basic-rational property, but none of the items below.
Each was checked absent from `content_pandoc` and `knowledge` before being written down.

## Negative curves

::: {.Proposition}
### Norms of smooth rational negative curves

Let $S$ be a Coble surface with anti-bicanonical divisor $D$.
Every smooth rational negative curve $E \containedin S$ satisfies
$$
E^2 \in \{-1,\, -2,\, -4\},
$$
and if $E^2 = -4$ then $E$ is a component of $D$.
:::

This is the fact that makes the $(-4)$-curves intrinsic: they cannot occur away from the boundary.
It is the surface-level counterpart of the $-2$ / $-4$ norm dichotomy that governs the Coxeter diagrams in [[root-vectors-and-folded-sterk-diagrams]].

## Automorphisms

::: {.Theorem}
### Coble's theorem, lattice form

Write $M_S \da K_S^{\perp\, \Pic(S)}$.
Then $\Aut(S)$ is isomorphic to a finite-index subgroup $H \leq \Orth(M_S)$, and
$$
\Orth(M_S)/\{\pm1\} \cong W(E_{10}).
$$
For general $C$, $H \cong W(E_{10})(2)$, the level 2 congruence subgroup.
:::

The project's introduction records $\Aut(S)\cong W(E_{10})$ for general $C$; the refinement to the level 2 congruence subgroup, and the quotient statement for $\Orth(M_S)$, are the sharper forms.

::: {.Remark}
### Finiteness of negative curves modulo automorphisms

Let $A_1(S)^{\mathrm{sm,rat},<0}$ denote the smooth rational curves of negative self-intersection.
Then $A_1(S)^{\mathrm{sm,rat},<0}/\Aut(S)$ is **finite**: up to automorphism a Coble surface carries only finitely many smooth rational negative curves.
Classifying all surfaces with this property is an open question recorded in the source.
:::

## The Coble-Mukai lattice

::: {.Definition}
### Coble-Mukai lattice

With $B_1,\ldots,B_n$ the boundary components, set
$$
L \da \gens{\NS(S),\ \tfrac12 B_1 + \cdots + \tfrac12 B_n}_\ZZ,
\qquad
\mathrm{CM}(S) \da \gens{B_1,\ldots,B_n}_\ZZ^{\perp L}.
$$
$\mathrm{CM}(S)$ serves as the replacement for $\NS(S)$ in the Coble setting.
:::

This object appears nowhere in the project, which works throughout with $S_{\Co}$ and $T_{\Co}$ inside $\lkt$.
Whether $\mathrm{CM}(S)$ relates to $S_{\Co}$, and whether it is the more natural home for the $\Gamma_{\Co}$ action, is not addressed in the source and looks worth settling.

## The Dolgachev-Zhang classification

::: {.Definition}
### Elliptic and rational types

A Coble surface is of **elliptic type** when there is $S \birational Y$ with $|-K_Y|$ a singleton and the mobile part of $|-2K_Y|$ generically a smooth elliptic curve.
Elliptic type splits further:

- **Halphen type**: blowups of singular points, and their infinitely near points, on a non-multiple fibre of a minimal rational elliptic surface with one multiple fibre of multiplicity 2.

- **Jacobian type**: blowdowns of disjoint sections, and possibly components of one fibre, of a non-minimal rational elliptic surface with a section.

It is of **rational type** when the mobile part of $|-2K_Y|$ consists of divisors $D$ with $p_a(D) = 0$, $D$ not necessarily irreducible.
These are blowups of minimal rational surfaces.
:::

::: {.Theorem}
### K3 type criterion, Dolgachev-Zhang Thm. 6.5

Let $X$ be a Coble surface with $M^2 = 0$.

- If $X$ is of Halphen type, obtained from a minimal Halphen surface $Y_m$ of index 2 by one blowup of a singular point on its non-multiple fibre $F$, then $X$ is of K3 type **if and only if** $F$ has type $I_n$, $\II$, $\III$ or $\IV$.

- If $X$ is of Jacobian type, obtained from a minimal Jacobian rational elliptic surface by blowing up a singular point of one fibre $F$ and at least one singular point, with infinitely near points, on another fibre $F_1$, then $X$ is of K3 type **if and only if** each of $F$ and $F_1$ has type $I_n$, $\II$, $\III$ or $\IV$.
:::

::: {.Lemma}
### Dolgachev-Zhang Lem. 6.2

For a Coble surface $X$ the following are equivalent:

1. $|-2K_X|$ contains a reduced divisor;

2. there is a double cover $\tilde X \to X$ with $\tilde X$ a K3 surface having at worst ordinary double points.
:::

::: {.Remark}
### Why this matters for the Halphen program

The project's `Degenerations/Halphen_Surfaces.md` records the Coble-to-Halphen blowdown and conjectures a correspondence of moduli spaces along the $g=0$ line of Nikulin's triangle; see [[halphen-index-2-moduli-program]]. The elliptic/rational dichotomy and Theorem 6.5 are the classification that the conjecture must respect: they say exactly which Halphen and Jacobian configurations produce K3-type Cobles, and so which fibres of the conjectured correspondence are nonempty.
The Jacobian branch has no counterpart anywhere in the project.
:::

## Rational log Enriques surfaces of index 2

::: {.Definition}
### Rational log Enriques surface of index 2

A normal rational surface $\bar X$ with at worst quotient singularities such that $\OO(-2K_{\bar X}) \cong \OO_{\bar X}$.
:::

::: {.Theorem}
### Terminal Cobles are resolutions of these

A terminal Coble surface is the minimal resolution of a **maximum** rational log Enriques surface of index 2. Conversely, the minimal resolution $X$ of a rational log Enriques surface $\bar X$ of index 2 is a Coble surface with $h^0(-2K_X) = 1$, whose unique member $D \in |-2K_X|$ is reduced and each of whose connected components is either a single $(-4)$-curve or a linear chain with a prescribed dual graph.
:::

The dual graph is a hand-drawn figure in the source and did not survive.
If this characterization is used, that graph must be recovered from Dolgachev-Zhang.

## Dolgachev-Kondo geometry of the degree 2 polarization

The project's `Stable_Limits/Geometric.md` records the map $\phi_{ij}$ onto a quartic del Pezzo surface and the key fact that it is **never finite** in the Coble case.
The following incidence data accompanying it is absent.

::: {.Remark}
### The branch geometry

Take $h = [F_1 + F_2] \in \Pic(S)$ of degree 2, so $|h|$ defines $\phi_{|h|}: S \to \PP^4$ with image $D$ a 4-nodal quartic del Pezzo surface.
Let $\sigma$ be the deck transformation.
Then:

- $\Fix(\sigma) = \bar W$ is a smooth genus 4 curve together with 3 isolated points;

- $\phi_h(C) = \{q\}$ is a **singular point** of $D$, where $C \in |-2K_S|$ is the Coble curve;

- $\bar W \intersect C = \{p_1, p_2\}$;

- $W \da \phi_h(\bar W)$ has $p_a(W) = 5$ and a double point at $q$.

A Coble surface arises as a degeneration of an Enriques surface exactly when the branch curve $W$ passes through a singular point of $D$.
:::

::: {.Remark}
### The rationality correspondence in its explicit form

Dolgachev-Kondo prove $\fco$ rational by comparison with $\cM_{\mathrm{cusp}} = U/\PGL_3$, the moduli of cuspidal plane quintics.
They show $\cM_{\mathrm{cusp}} \birational \cM_{\En}$, which is 10-dimensional, and that a distinguished codimension one locus $\cM'_{\mathrm{cusp}} \cong \cM_{\Co}$.
The locus is explicit: for $C$ a plane quintic with cusp $p$ and $L$ the tangent line to $C$ at $p$, it is the case where $L$ is **also** tangent to $C$ at a smooth point $q \in C$.

The project states only that $\fco$ is rational "by relating it to a codimension one subvariety of a moduli space of certain $A_2$-singular quintics".
The tangency condition above is what cuts out that subvariety.
:::

Related: [[coble-families-research-program]], [[halphen-index-2-moduli-program]], [[cusp-correspondence-morphism-chain]].
