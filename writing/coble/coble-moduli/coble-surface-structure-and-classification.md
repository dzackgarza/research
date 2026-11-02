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
The trichotomy has three values; the argument is:

Adjunction on the smooth rational curve $E$ gives $E^2 = -2 - E\cdot K_S$, so the possible values of $E^2$ are read off the intersection numbers of $E$ with $-K_S$.
A Coble surface has $|-2K_S| = \{D\}$ with $D$ nonempty and $D$ a sum of $(-4)$-curves, $\tfrac12D$ being a *divisor* representative of $-K_S$ that is not integral: the class $-K_S$ is integral as a class, and by the definition [@DK13, §3] gives it is ineffective, $|-K_S| = \emptyset$, while $2(-K_S) = [D]$ is effective.
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

Cited: [@DO88] for the description of $\Aut(S)$ through the action on $M_S$, and [@CDL25, Ch. 5] for the level 2 structure.

The two groups are read as follows.
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
L \definedas \generators{\NS(S),\ \tfrac12 B_1,\ \ldots,\ \tfrac12 B_n}_\ZZ
\iscontainedin \NS(S)_\QQ,
\qquad
\CM(S) \definedas \generators{B_1,\ldots,B_n}_\ZZ^{\perp L}.
$$
The half-classes are adjoined one at a time, so $L$ is an integral overlattice of $\NS(S)$ exactly when every $B_i$ is $2$-divisible, that is when $B_i \cdot D$ is even for every $D\in\NS(S)$; we assume this in what follows, and it is where the Coble boundary configuration earns the name.
$\CM(S)$ serves as the replacement for $\NS(S)$ in the Coble setting.
:::

Three computations about the defining data, since they decide what $\CM(S)$ can be.

The index. One has $2\cdot\tfrac12 B_i = B_i \in \NS(S)$, and $\sum_i \tfrac12 B_i = \tfrac12(-2K_S) = -K_S\in\NS(S)$ because $|-2K_S|=\{D\}$ gives $D=-2K_S$; so $L/\NS(S)$ is an $\mathbb{F}_2$-vector space spanned by the $n$ classes of the $\tfrac12 B_i$ subject to the single relation $\sum_i[\tfrac12 B_i] = 0$, hence of dimension at most $n-1$, and of dimension exactly $n-1$ when the classes are independent:
$$
[L : \NS(S)] = 2^{\,n-1}.
$$
In particular $L = \NS(S)$ exactly when $n = 1$: then $\tfrac12 B_1 = -K_S$ is already integral, and the half-class adjoined carries nothing.

The rank and signature. Since $L \iscontainedin \NS(S)_\QQ$ the two have the same rank $11$ and the same signature $(1,10)$.
The $B_i$ are mutually orthogonal of square $-4$, so $\generators{B_1,\dots,B_n}_\ZZ$ is negative definite of rank $n$ and primitive in $L$; a primitive negative definite sublattice has orthogonal complement of
$$
\rank \CM(S) = 11 - n,
\qquad
\text{signature } \CM(S) = (1,\,10-n).
$$
At $n=1$ this is rank $10$ of signature $(1,9)$, the Enriques lattice $E_{10}$, and indeed $\CM(S) = K_S^{\perp \NS(S)}$ there, isometric to $S_\Co$.

The embedding. $\CM(S)\hookrightarrow L$ is primitive, being an orthogonal direct summand, while $\CM(S)\hookrightarrow\NS(S)$ is not primitive once $n\geq 2$, since $L$ is strictly larger.
So a relation between $\CM(S)$ and $S_\Co$ compares complements of different configurations inside the same K3 lattice, and the lattice to compare with $\Pic(X)$ of the K3 cover is $L$, not $\NS(S)$.

::: {.question #qst:coble-mukai-naturality title="Is the Coble--Mukai lattice the natural home for the group action?"}

Is $\CM(S)$ rather than $S_{\Co}$ the natural home for the action of $\Gamma_{\Co}$, and how are the two related?

Neither the source nor this book answers this.
The prerequisites are settled above: $\CM(S)$ has rank $11-n$ and signature $(1,10-n)$, the boundary configuration is primitive in $L$ but not in $\NS(S)$ for $n\geq 2$, and $\CM(S)\hookrightarrow L$ is primitive while $\CM(S)\hookrightarrow\NS(S)$ is not.
What remains open is whether the group acting on $\CM(S)$ is the stable orthogonal group of $L$ or the subgroup induced from $\NS(S)$.
What the rank and signature do not determine is the discriminant form of $\CM(S)$ along the boundary, and that is where the group action lives.

What can be said is why the question is not idle.
$S_{\Co}\cong\generators{-2}\oplus E_{10}(2)$ is $2$-elementary, so $A_{S_{\Co}}=(\bZ/2)^{11}$ and the discriminant representation of @thm:two-elementary-surjectivity is surjective; the two mod-$2$ invariants $(r,a,\delta)$ that classify a $2$-elementary lattice are then the only handles on $\Orth(S_{\Co})$, and in the inert case $n_1=n_2=10$ they are the ones that take equal values.
A complement of the boundary configuration inside $\NS(S)$ is not $2$-elementary in general -- the $B_i$ have square $-4$, so odd primes enter the discriminant of the boundary lattice and hence, by @prop:scaled-discriminant-ses, into the gluing between $\CM(S)$ and its complement.
If $\Gamma_{\Co}$ acts on $\CM(S)$ compatibly with that gluing, the odd part of the discriminant group is an invariant the $2$-elementary data of $S_{\Co}$ cannot see, and it would be visible exactly where those data stop separating cases.
Whether that is what happens is open.
:::

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
The mechanism: $|-2K_X|$ nonempty is the datum of a $\bZ/2$-cover, branched over a divisor in that class, and the condition that a member be reduced is what keeps the branch divisor smooth enough for the cover to have only ordinary double points.
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
