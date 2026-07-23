---
title: "Degree-2 Coble Surfaces and the Coble Heegner Divisor"
subtitle: "A mathematical research report on the established framework, precise constructions, open comparison problems, and proof strategies"
author: "Working research report"
date: "2026-07-23"
lang: en
toc: true
toc-depth: 4
number-sections: true
bibliography: coble_references.bib
link-citations: true
citeproc: true
crossrefYaml: pandoc-crossref.yaml
header-includes:
  - |
    \usepackage{amsmath,amssymb,amsthm,mathtools}
    \usepackage{tikz-cd}
    \usepackage{booktabs,longtable}
    \newtheorem{theorem}{Theorem}[section]
    \newtheorem{proposition}[theorem]{Proposition}
    \newtheorem{lemma}[theorem]{Lemma}
    \newtheorem{corollary}[theorem]{Corollary}
    \theoremstyle{definition}
    \newtheorem{definition}[theorem]{Definition}
    \newtheorem{construction}[theorem]{Construction}
    \newtheorem{problem}[theorem]{Problem}
    \theoremstyle{remark}
    \newtheorem{remark}[theorem]{Remark}
    \newtheorem{warning}[theorem]{Warning}
---

# Introduction and logical status {#sec:introduction}

## Purpose {#sec:purpose}

This report fixes a common mathematical language for the study of the degree-2 Coble locus associated with the $(-2)$-Heegner arrangement in the period space of numerically degree-$2$ polarized Enriques surfaces.
It has four purposes.

1. It records the definitions, constructions, lattice identifications, local calculations, and numerical formulas that have been isolated with a level of precision suitable for further research.
2. It distinguishes those statements that follow from standard results or direct calculations from those that remain comparison theorems, lifting problems, or compactification problems.
3. It formulates two principal approaches to the compactification problem: the **Heegner-restriction approach** and the **autonomous Coble approach**.
4. It gives a theorem-by-theorem research program for completing either approach and later identifying the two constructions.

The intended reader is assumed to know the theory of K3 and Enriques surfaces, integral lattices, type-IV period domains, Baily--Borel and toroidal compactifications, Kulikov models, KSBA stable pairs, Nikulin's theory of $2$-elementary involutions, and the compactification framework developed by Alexeev and Engel.
Standard terminology is cited rather than reproved; see @sec:terminology and the bibliography.

The report is not a proof of the final Coble compactification theorem.
It is a mathematical specification of the objects and the exact statements that a proof must establish.
This distinction is essential because several plausible computations discussed below are computations of finite quadratic spaces or hyperplane slices, not yet computations of arithmetic cusps or Vinberg chambers.

## Convention on logical status {#sec:status-convention}

The following convention is used throughout.

- A statement labeled **Theorem**, **Proposition**, **Lemma**, or **Corollary** is either a standard cited result, a result of AEGS, or a direct calculation whose hypotheses are stated explicitly.
- A statement labeled **Required theorem**, **Required lemma**, or **Problem** is not presently established in the Coble setting.
  It records an exact unit of work needed by one of the proposed strategies.
- A **Candidate construction** is a mathematically defined construction whose relation to the desired moduli problem has not yet been proved.
- A **Computational record** is a reproducible finite or symbolic calculation.
  It is not promoted to an arithmetic or geometric theorem unless the relevant lifting or realization statement is separately proved.
- A **Warning** records a point at which an earlier line of reasoning made an invalid inference or conflated two distinct objects.

Thus the report uses formal mathematical language without disguising the logical status of unfinished comparison statements.

## Central compactification problem {#sec:central-problem}

Let

\[
T_{\mathrm{En}}
  \cong U\oplus U(2)\oplus E_8(2)
\]

be the Enriques anti-invariant lattice in the AEGS degree-$2$ construction, and let $\alpha\in T_{\mathrm{En}}$ be a primitive vector with $\alpha^2=-2$.
The hyperplane

\[
\mathbb D(T_{\mathrm{En}})\cap\alpha^\perp
\]

is the period domain of the Coble Heegner locus.
The final problem is to identify the normalization of the KSBA closure of that locus as an explicit semitoroidal compactification, including the arithmetic group, all Baily--Borel cusps, the cusp reflection chambers, the integral-affine and dlt models, the relevant semifans, and the toroidal versus strictly semitoroidal locus.

The ambient AEGS theorem supplies the model for the required level of specificity: the compactification is meaningful only after the lattices, groups, divisors, cusp data, Coxeter data, and stable-pair contractions have all been identified.
The research prompt explicitly treats those data as part of the theorem rather than optional consequences.

## Principal distinction between the two strategies {#sec:two-strategies}

There are two conceptually different ways to organize the proof.

1. **Heegner-restriction strategy.**  Begin with the AEGS Enriques moduli problem and regard the Coble locus as the normalization of a fixed $(-2)$-Heegner component.
   The principal new work is to justify passage to arithmetic quotients, normalize the boundary restriction, solve the cusp lifting problem, identify the restricted semifans, and prove that the resulting KSBA family loses no moduli.
2. **Autonomous Coble strategy.**  Define a direct moduli problem of K3 covers with a Coble involution, a commuting del Pezzo involution, a degree-$4$ class, and a distinguished exceptional root.
   Reproduce direct analogues of the AEGS period, cusp, Vinberg, integral-affine, dlt, recognizable-divisor, and semitoroidal theorems.
   Only after this independent theory is complete does one prove that it agrees with the Enriques Heegner construction.

The second strategy avoids using the Enriques compactification as a black box, but it creates a separate comparison theorem at the end.
The first strategy uses more existing geometry, but it requires careful normalization and monodromy arguments that cannot be replaced by the phrase “restrict the semifan.”

# Terminology, notation, and standard background {#sec:terminology}

## General conventions {#sec:general-conventions}

The ground field is $\mathbb C$.
All lattices are free abelian groups of finite rank equipped with a nondegenerate symmetric bilinear form.
The K3 lattice is

\[
L_{K3}=II_{3,19}\cong U^3\oplus E_8^2,
\]

where $E_8$ is negative definite.
If $M$ is a lattice, then $M(n)$ denotes the same abelian group with its bilinear form multiplied by $n$.
The orthogonal group preserving a chosen component of the positive cone is denoted $O^+(M)$.

For an even lattice $M$, its discriminant group and discriminant quadratic form are

\[
A_M=M^*/M,
\qquad
q_M:A_M\longrightarrow \mathbb Q/2\mathbb Z.
\]

A primitive embedding is an embedding whose cokernel is torsion free.
The classification and gluing theory of even $2$-elementary lattices are used in the sense of Nikulin [@Nik79].

## Surface singularities and covers {#sec:surface-terminology}

A **rational double point** or **ADE singularity** is a Du Val surface singularity.
An **$A_1$-singularity** is analytically

\[
\{xy-z^2=0\}\subset\mathbb A^3.
\]

The cyclic quotient singularity

\[
\frac{1}{4}(1,1)
  =\mathbb A^2_{u,v}/\mu_4,
\qquad
\zeta\cdot(u,v)=(\zeta u,\zeta v),
\]

has quotient group of order $4$ and canonical index $2$.
Its canonical index-one cover is the $A_1$-singularity $\mathbb A^2/\{\pm1\}$, not the smooth plane.
The smooth plane is the canonical degree-$4$ quasi-\'etale cover.

A normal surface is $R_1$ and $S_2$.
In particular, the $\frac{1}{4}(1,1)$-singularity is normal.
Nonnormal surfaces can nevertheless occur at the KSBA boundary through conductor self-gluings; this phenomenon is logically separate from the local quotient singularity.

The terms **index-one cover**, **reflexive power**, **deminormal**, **semi-log-canonical**, and **divisorially log terminal** are used in the standard MMP sense [@KM98; @Kol23; @Stacks].  In particular, an slc pair is tested by requiring the normalized pair with conductor to be log canonical, not klt.

## K3, Enriques, and Coble terminology {#sec:surface-classes}

A K3 surface is a smooth projective surface $X$ with $K_X\sim0$ and $H^1(X,\mathcal O_X)=0$.
An Enriques surface is a smooth projective surface $Z$ with $2K_Z\sim0$, $K_Z\not\sim0$, and $q(Z)=0$; see [@CD89; @CDL24].

The word **Coble surface** is used in two closely related senses in the literature.
To remove ambiguity, this report uses the following notation.

::: {#def-singular-coble .definition}
**Definition (singular Coble quotient).**  A *singular Coble quotient* is a
normal rational surface $V^\sharp$ obtained as the quotient of a K3 surface
$X^\sharp$ with one $A_1$-singularity by a nonsymplectic involution that fixes
the singular point and is otherwise free in codimension one.  The quotient
has one singularity of type $\frac{1}{4}(1,1)$.
:::

::: {#def-resolved-coble .definition}
**Definition (resolved Coble surface).**  The *resolved Coble surface*
$\widetilde V$ is the minimal resolution of $V^\sharp$.  It is a smooth
rational surface satisfying

\[
|-K_{\widetilde V}|=\varnothing,
\qquad
|-2K_{\widetilde V}|\ne\varnothing
\]

on the classical one-node locus.
:::

The resolved surface is the object traditionally called a classical Coble surface.
The singular quotient is the natural $K$-trivial object for the small-coefficient KSBA problem.

## Polarizations {#sec:polarization-terminology}

A **quasipolarization** is a nef and big line bundle.
A polarization is ample.
This distinction is essential in the Coble setting: the natural class on $\widetilde V$ is orthogonal to the anti-bicanonical $(-4)$-curve and is therefore not ample.
It becomes ample after contracting the complete null locus.

## Period domains and Heegner divisors {#sec:period-terminology}

For a lattice $T$ of signature $(2,n)$, a connected type-IV domain is

\[
\mathbb D(T)
 =\left\{
 [\omega]\in\mathbb P(T\otimes\mathbb C)
 : (\omega,\omega)=0,
   (\omega,\overline\omega)>0
 \right\}^{+}.
\]

If $\Gamma\subset O^+(T)$ is arithmetic, the quotient $\Gamma\backslash\mathbb D(T)$ is a quasi-projective orthogonal modular variety.
For a negative vector $r\in T$, the image of $\mathbb D(T)\cap r^\perp$ is a **Heegner divisor** or arrangement divisor.
See [@BB66; @Loo03] for the compactification theory and [@Nik79; @Nam85] for the relevant Enriques lattice geometry.

A primitive isotropic line in $T$ determines a zero-dimensional Baily--Borel boundary component, called a **$0$-cusp**.  A primitive isotropic plane determines a one-dimensional boundary component, called a **$1$-cusp**. The arithmetic orbit, not merely the rational isotropic subspace, is part of the cusp datum.

## Reflection theory {#sec:reflection-terminology}

Let $M$ be hyperbolic.
For a negative vector $r\in M$, the reflection is

\[
w_r(x)=x-\frac{2(x,r)}{r^2}r.
\]

The vector $r$ is a **root** if $w_r\in O(M)$; equivalently,

\[
2\operatorname{div}(r)\in r^2\mathbb Z.
\]

A **Coxeter chamber** is a fundamental chamber for a reflection group acting on the positive cone.
Its codimension-one walls are perpendicular to simple roots.
A maximal parabolic subdiagram determines an isotropic ray and hence a Type II direction.
An elliptic subdiagram determines a Type III cone.
The terminology and algorithms are those of Vinberg [@Vin72; @Vin75].

## Degenerations and integral-affine structures {#sec:degeneration-terminology}

A **Kulikov model** is a semistable $K$-trivial model of a degeneration of K3 surfaces [@Kul77; @PP81].  Type II degenerations have dual complex a segment; Type III degenerations have dual complex a $2$-sphere.
Type III dual complexes carry canonical integral-affine structures with singularities [@Eng18; @EF21; @GHK15a].

A **divisor model** is a Kulikov or dlt model carrying a nef extension of the distinguished divisor.
Its integral-affine polarization is a weighted balanced graph on the dual complex [@ABE22; @AE22].  A **visible curve** is a curve class represented by a path joining affine singularities with parallel monodromy.
Collapsing such a path can merge two $I_1$ affine singularities into an $I_2$ singularity.

## KSBA and semitoroidal compactifications {#sec:compactification-terminology}

A KSBA stable pair $(X,B)$ is a projective deminormal pair such that $(X,B)$ is slc and $K_X+B$ is ample and $\mathbb Q$-Cartier [@Kol23].  For small-coefficient polarized Calabi--Yau pairs, boundedness and independence of sufficiently small $\epsilon$ are used in the form of [@KX20; @Bir23].

A toroidal compactification is defined by compatible rational polyhedral fans at the rational boundary components.
A semitoroidal compactification is defined by compatible semifans; cones may have infinitely many rational generators [@Loo03; @AE23].  A generalized Coxeter semifan is obtained from a Coxeter fan by removing the walls generated entirely by roots that are invisible to the stable-pair combinatorics [@AET23; @AEGS25].

# The ambient AEGS framework {#sec:aegs-framework}

## The projective Klein-four diagram {#sec:aegs-projective}

Let

\[
Y=\mathbb P^1\times\mathbb P^1,
\qquad
\tau(x,y)=(-x,-y)
\]

on the dense torus.
Let

\[
B\in|-2K_Y|=|\mathcal O_Y(4,4)|
\]

be $\tau$-invariant, with at worst ADE singularities, and assume that $B$ avoids the four fixed points of $\tau$.
The double cover

\[
\pi:X\longrightarrow Y
\]

branched along $B$ is a K3 surface with at worst ADE singularities.
Writing $X$ as

\[
z^2+f(x,y)=0,
\]

one has three commuting involutions

\[
\iota_{\mathrm{dP}}(x,y,z)=(x,y,-z),
\]

\[
\iota_{\mathrm{En}}(x,y,z)=(-x,-y,-z),
\]

\[
\iota_{\mathrm{Nik}}(x,y,z)=(-x,-y,z)
  =\iota_{\mathrm{dP}}\iota_{\mathrm{En}}.
\]

The first two are nonsymplectic and the product is symplectic.
The quotient $Z=X/\iota_{\mathrm{En}}$ is generically Enriques, while $X/\iota_{\mathrm{Nik}}$ is a K3 surface with eight $A_1$ singularities.
The ramification divisor used in the AEGS stable-pair problem is the ramification of the **del Pezzo involution**, not the fixed locus of the Enriques involution.

## The AEGS lattice package {#sec:aegs-lattices}

The involutions act on

\[
L_{K3}=U^3\oplus E_8^2
\]

with eigenspaces

\[
S_{\mathrm{dP}}\cong U(2),
\qquad
T_{\mathrm{dP}}\cong U\oplus U(2)\oplus E_8^2,
\]

\[
S_{\mathrm{En}}\cong U(2)\oplus E_8(2),
\qquad
T_{\mathrm{En}}\cong U\oplus U(2)\oplus E_8(2).
\]

The degree-$4$ K3 polarization is a vector $H\in S_{\mathrm{dP}}\subset S_{\mathrm{En}}$ with $H^2=4$.

::: {#thm-aegs-rigidity .theorem}
**Theorem (AEGS embedding rigidity).**  The primitive embedding chain

\[
T_{\mathrm{En}}\hookrightarrow T_{\mathrm{dP}}
  \hookrightarrow L_{K3}
\]

is unique up to $O(L_{K3})$.
:::

This theorem is the model for the stronger labeled rigidity statement needed for the Coble problem.
It prevents later constructions from depending on a hidden coordinate choice.

## AEGS arithmetic groups and period maps {#sec:aegs-groups}

AEGS define

\[
\Gamma_{\mathrm{En},2}
 =\operatorname{im}\left(
   \{g\in O(L_{K3}):gI_{\mathrm{En}}=I_{\mathrm{En}}g,
                         \ g(H)=H\}
   \longrightarrow O(T_{\mathrm{En}})
  \right).
\]

They prove that this is the stabilizer of the Enriques period subdomain inside the del Pezzo arithmetic quotient.
Consequently the period-domain inclusion gives a finite generically injective map

\[
\mathcal F_{\mathrm{En},2}
  \longrightarrow
\mathcal F_{(2,2,0)}.
\]

The group definition is geometric: it is taken from the common K3 lattice, the involution, and the polarization.
This is the standard that any direct Coble group must meet.

## The AEGS compactification theorem {#sec:aegs-main-theorem}

AEGS define stable pairs $(Z,\epsilon R_Z)$, where $R_Z$ is the divisorial ramification of the descended del Pezzo involution.
Their main theorem identifies the normalization of the KSBA closure with a semitoroidal compactification described by five explicit semifans.
The proof has the following indispensable stages.

1. classify the Baily--Borel cusps;
2. compute the reflective cusp lattices;
3. prove a root-folding theorem with a converse;
4. prove that chamber intersection gives a fundamental chamber;
5. lift the cusp involutions through the discriminant gluing to the full period lattice;
6. realize monodromy by integral-affine divisor models;
7. extend the involution algebraically;
8. take dlt quotients and the relative Proj;
9. identify the generalized Coxeter semifans; and
10. prove that the classifying map is finite and that no further coarsening occurs.

This architecture will be used repeatedly below as a list of theorem types, not as a black-box proof of the Coble case.

# Direct Coble geometry from invariant $(4,4)$ curves {#sec:projective-coble}

## The invariant linear system {#sec:invariant-system}

The vector space

\[
H^0\bigl(Y,\mathcal O_Y(4,4)\bigr)^\tau
\]

has basis the monomials whose two affine exponents have even sum.
It has dimension $13$, so its projectivization is $\mathbb P^{12}$.

Fix a $\tau$-fixed point $p\in Y$.
Choose local coordinates $(x,y)$ centered at $p$.
An invariant local equation has the form

\[
f(x,y)
 =a_{00}+a_{20}x^2+a_{11}xy+a_{02}y^2
  +\text{terms of degree at least }4.
\]

There are no linear terms.

::: {#lem-node-condition .lemma}
**Lemma (node condition).**  The curve $B=(f=0)$ has an ordinary node at $p$
if and only if

\[
a_{00}=0,
\qquad
 a_{11}^2-4a_{20}a_{02}\ne0.
\]
:::

**Proof sketch.**  The first condition says that $p\in B$.
Invariance kills the linear part.
The second condition says that the quadratic tangent cone is nondegenerate.
This is the analytic criterion for an ordinary plane node.

A general member satisfying these conditions is smooth away from $p$.
This is an open condition, and it is enough to exhibit one member having no other singularities.
A symbolic example is recorded in @sec:computational-record.

## Toric interpretation {#sec:coble-toric-model}

Let $Q$ be the square polytope of $\mathcal O_Y(4,4)$.
The quotient $W=Y/\tau$ is the toric surface defined by the same rational polygon but with cocharacter lattice

\[
\mathbb Z^2_{\mathrm{ev}}
 =\{(a,b)\in\mathbb Z^2:a+b\in2\mathbb Z\}.
\]

The invariant monomials are precisely the lattice points of $Q$ in this even sublattice.
If $P$ is the pyramid over $Q$ with apex corresponding to $z^2$, the K3 hypersurface is defined in the toric threefold $V_P$.
The quotient by the sign involution uses the lattice

\[
\mathbb Z^3_{\mathrm{ev}}
 =\{(a,b,c)\in\mathbb Z^3:a+b+c\in2\mathbb Z\}.
\]

Passing through a chosen torus-fixed point is the vanishing of the coefficient of the corresponding vertex monomial.
The nondegeneracy of the quadratic part is the local node condition of the preceding lemma.

## The nodal K3 cover and the Coble quotient {#sec:cover-quotient}

Let

\[
X^\sharp=\{z^2=f(x,y)\}\longrightarrow Y.
\]

Then $X^\sharp$ has an $A_1$-singularity over $p$.
The involutions

\[
\iota_{\mathrm{dP}}(x,y,z)=(x,y,-z),
\qquad
\iota_{\mathrm{Co}}(x,y,z)=(-x,-y,-z)
\]

commute.
The first is the del Pezzo deck involution.
The second fixes the $A_1$-point.

::: {#prop-local-quarter .proposition}
**Proposition (local Coble quotient).**  The quotient
$X^\sharp/\iota_{\mathrm{Co}}$ has a singularity of type
$\frac{1}{4}(1,1)$ at the image of the node.
:::

**Proof.**  Write

\[
X^\sharp_{\mathrm{an}}
 \cong \{xy-z^2=0\}
 \cong \mathbb A^2_{u,v}/\{\pm1\}
\]

using $x=u^2$, $y=v^2$, and $z=uv$.
The involution on the node lifts to $(u,v)\mapsto(iu,iv)$.
The composite quotient is therefore $\mathbb A^2/\mu_4$ with scalar weights $(1,1)$.

## Equivariant smoothing {#sec:equivariant-smoothing}

Vary the constant coefficient $a_{00}$ in a one-parameter family.
For $a_{00}\ne0$, the branch curve avoids the fixed point $p$, the K3 cover is smooth near the corresponding fiber, and the involution $\iota_{\mathrm{Co}}$ has no point over $p$.
If the branch curve avoids all four $\tau$-fixed points, then the same fixed-point calculation shows that $\iota_{\mathrm{Co}}$ is fixed-point free.
Its quotient is an Enriques surface.

::: {#prop-explicit-smoothing .proposition}
**Proposition (explicit Coble-to-Enriques smoothing).**  The invariant
$(4,4)$ family obtained by varying $a_{00}$ gives an explicit equivariant
smoothing of the singular Coble quotient to Enriques quotients.
:::

This proposition proves existence of one smoothing mechanism.
It does not imply that every abstract smoothing of the K3 cover carries an extension of the node-fixing involution.

## Dimension and coverage {#sec:projective-coverage}

The projective invariant linear system has dimension $12$.
Imposing $a_{00}=0$ gives a hyperplane, and the connected centralizer of $\tau$ in $\operatorname{Aut}(Y)$ has dimension $2$.
Thus the expected moduli dimension is

\[
12-1-2=9.
\]

The finite symmetry group permutes the four fixed points.

::: {#prob-projective-coverage .problem}
**Required theorem (projective coverage and intrinsic reconstruction).**  The
quotient of the open nodal invariant $(4,4)$ locus by the full centralizer of
$\tau$ is the complete direct moduli stack of generic degree-$2$ Coble data.
Equivalently, the projective diagram can be reconstructed intrinsically from
the Coble pair, and the resulting period map has image the full relevant
period-domain component.
:::

A dimension count and one explicit family do not prove this theorem.
A proof must establish irreducibility at the level of the actual arithmetic group and recover the K3 cover, the two involutions, and the degree-$4$ class from the Coble datum.

# The Coble lattice package {#sec:coble-lattices}

## The orthogonal complement lattice {#sec:orthogonal-complement}

Write

\[
T_{\mathrm{En}}
 \cong U\oplus E(2),
\qquad
E=U\oplus E_8.
\]

Choose a standard basis $e,f$ of the first copy of $U$, and define

\[
\alpha=e-f,
\qquad
\eta=e+f.
\]

Then

\[
\alpha^2=-2,
\qquad
\eta^2=2,
\qquad
(\alpha,\eta)=0.
\]

The notation $\eta$ is deliberately used here: the letter $H$ is reserved for the degree-$4$ K3 polarization in the AEGS construction.

::: {#prop-coble-transcendental .proposition}
**Proposition (Coble anti-invariant lattice).**  The orthogonal complement of
$\alpha$ in $T_{\mathrm{En}}$ is

\[
T_{\mathrm{Co}}
 :=\alpha^\perp_{T_{\mathrm{En}}}
 \cong \langle2\rangle\oplus U(2)\oplus E_8(2).
\]

It has signature $(2,9)$, rank $11$, discriminant group
$(\mathbb Z/2)^{11}$, and $2$-elementary invariant $\delta=1$.  Equivalently,

\[
T_{\mathrm{Co}}\cong I_{2,9}(2).
\]
:::

**Proof.**  The first copy of $U$ decomposes over the sublattice $\mathbb Z\alpha\oplus\mathbb Z\eta$, and the orthogonal complement of $\alpha$ there is $\mathbb Z\eta\cong\langle2\rangle$.
The remaining summand is $E(2)=U(2)\oplus E_8(2)$.
The stated invariants follow directly.

## The invariant lattice and the reflection twist {#sec:reflection-twist}

Let $I_{\mathrm{En}}$ be the Enriques involution on the K3 lattice, acting as $+1$ on $S_{\mathrm{En}}$ and as $-1$ on $T_{\mathrm{En}}$.
Let $w_\alpha$ be the reflection in the root $\alpha$.

::: {#construction-reflection-twist .construction}
**Construction (reflection twist).**  Define

\[
I_{\mathrm{Co}}:=w_\alpha I_{\mathrm{En}}.
\]
:::

Since $I_{\mathrm{En}}(\alpha)=-\alpha$, the two factors commute.

::: {#prop-coble-eigenspaces .proposition}
**Proposition (eigenspaces of the reflection twist).**  One has

\[
L_{K3}^{I_{\mathrm{Co}}=1}
  =S_{\mathrm{En}}\oplus\mathbb Z\alpha
  \cong U(2)\oplus E_8(2)\oplus\langle-2\rangle,
\]

and

\[
L_{K3}^{I_{\mathrm{Co}}=-1}
  =\alpha^\perp_{T_{\mathrm{En}}}
  =T_{\mathrm{Co}}.
\]

Thus the invariant lattice is

\[
S_{\mathrm{Co}}
 \cong U(2)\oplus E_8(2)\oplus\langle-2\rangle
 \cong I_{1,10}(2).
\]
:::

**Proof.**  The reflection fixes $\alpha^\perp$ and sends $\alpha$ to $-\alpha$.
The formula follows by separating $S_{\mathrm{En}}$, $\mathbb Z\alpha$, and $\alpha^\perp_{T_{\mathrm{En}}}$.

The abstract eigenspace computation agrees with the lattice type appearing in the period theory of classical Coble surfaces [@DK13].  It does not, by itself, prove that every family of direct Coble data realizes the same labeled embedding in $L_{K3}$.

## The local geometric meaning of the root {#sec:root-geometry}

Let

\[
\widetilde X\longrightarrow X^\sharp
\]

be the minimal resolution of the $A_1$-point, and let $E\subset\widetilde X$ be the exceptional $(-2)$-curve.
In the explicit local model, the lift of $\iota_{\mathrm{Co}}$ fixes $E$ pointwise, while the lift of $\iota_{\mathrm{dP}}$ acts nontrivially on $E$ with two fixed points.
The cohomology class $[E]$ is the geometric realization of $\alpha$ after a choice of marking.

The involution $I_{\mathrm{Co}}$ is therefore the expected cohomological involution on the resolved cover.
Turning this expectation into a global statement in families requires a simultaneous resolution and a rigidity theorem; see @sec:labeled-lattice-data.

## Labeled lattice data {#sec:labeled-lattice-data}

The abstract isomorphism type of $T_{\mathrm{Co}}$ does not determine the geometric moduli problem.
The relevant datum is a labeled tuple

\[
\mathfrak L_{\mathrm{Co},2}
 =\bigl(
 L_{K3},
 I_{\mathrm{Co}},
 I_{\mathrm{dP}},
 H,
 \alpha,
 \mathscr C
 \bigr),
\]

where

- $I_{\mathrm{Co}}$ and $I_{\mathrm{dP}}$ are commuting nonsymplectic involutions;
- $H^2=4$ is fixed by both involutions;
- $\alpha^2=-2$, $H\cdot\alpha=0$, and $\alpha$ is fixed by $I_{\mathrm{Co}}$;
- $\mathscr C$ is the chosen positive/nef chamber in which $\alpha$ is effective and $H$ is nef and big;
- the product $I_{\mathrm{Co}}I_{\mathrm{dP}}$ has the required symplectic character.

::: {#prob-coble-rigidity .problem}
**Required theorem (labeled Coble rigidity).**  Any two tuples
$\mathfrak L_{\mathrm{Co},2}$ arising from the direct projective construction
are conjugate by an element of $O(L_{K3})$ preserving the labels, the degree-$4$ class, the effective root, and the chosen chamber.
:::

This is stronger than uniqueness of a primitive embedding of $S_{\mathrm{Co}}$ into $L_{K3}$.
It is the Coble analogue of the AEGS embedding-rigidity lemma and is needed before any direct period quotient can be declared coordinate independent.

## The embedded comparison chain {#sec:embedded-chain}

The Heegner strategy uses the chain

\[
T_{\mathrm{Co}}
  =\alpha^\perp_{T_{\mathrm{En}}}
  \hookrightarrow T_{\mathrm{En}}
  \hookrightarrow T_{\mathrm{dP}}
  \hookrightarrow L_{K3}.
\]

The autonomous strategy begins with the leftmost lattice as the anti-invariant lattice of $I_{\mathrm{Co}}$ and must later construct and identify the two larger lattices.
The comparison theorem must show that the two chains are conjugate as **labeled embedded chains**, not merely termwise isometric.

# The resolved surface, the quasipolarization, and the stable divisor {#sec:surface-divisors}

## The resolved quotient diagram {#sec:resolved-diagram}

Let

\[
\psi:\widetilde X\longrightarrow\widetilde V
\]

be the quotient of the resolved K3 cover by $\iota_{\mathrm{Co}}$.
Let $E\subset\widetilde X$ be the fixed exceptional curve and let

\[
C:=\psi(E)\subset\widetilde V.
\]

Then

\[
\psi^*C=2E.
\]

Let

\[
H=\pi^*\mathcal O_Y(1,1)
\]

on $\widetilde X$.
The class $H$ satisfies

\[
H^2=4,
\qquad
H\cdot E=0.
\]

With the natural descent linearization, there is a class $L\in\operatorname{Pic}(\widetilde V)$ such that

\[
\psi^*L=H.
\]

::: {#prop-quasipolarization .proposition}
**Proposition (degree-$2$ quasipolarization).**  The class $L$ satisfies

\[
L^2=2,
\qquad
L\cdot C=0.
\]

Hence $L$ is not ample on $\widetilde V$.  On a general one-node member it is
nef and big and its only null curve is $C$.  After contracting the full
$L$-null configuration, its descent is ample.
:::

The final sentence must be interpreted with care on intersections with other Heegner divisors: additional curves can become $L$-trivial.

## The anti-bicanonical curve {#sec:anti-bicanonical}

Riemann--Hurwitz for the double cover $\psi$ gives

\[
K_{\widetilde X}
 =\psi^*\left(K_{\widetilde V}+\frac12C\right).
\]

Since $K_{\widetilde X}\sim0$ and $\widetilde V$ is rational,

\[
C\sim-2K_{\widetilde V}.
\]

Moreover,

\[
2C^2=(2E)^2=-8,
\qquad
C^2=-4.
\]

::: {#prop-antibicanonical-system .proposition}
**Proposition (anti-bicanonical system on the one-node locus).**  For the
resolved one-node Coble surface,

\[
|-K_{\widetilde V}|=\varnothing,
\qquad
|-2K_{\widetilde V}|=\{C\}.
\]
:::

**Proof.**  If $D\in|-2K_{\widetilde V}|$, then $\psi^*D\in|2E|$.
Since $E^2=-2$, every effective divisor linearly equivalent to $2E$ contains $E$; iterating gives $|2E|=\{2E\}$.
Thus $D=C$.
If $D\in|-K_{\widetilde V}|$, then $\psi^*D\in|E|=\{E\}$.
The pullback of a divisor from the quotient has even multiplicity along a branch component, so this is impossible.

If the invariant branch curve has ordinary nodes at $k$ distinct fixed points, the same argument gives

\[
|-2K_{\widetilde V}|
 =\{C_1+\cdots+C_k\},
\]

where the $C_i$ are disjoint rational $(-4)$-curves.
Thus $n=1$ on the generic Heegner divisor but not on its higher-codimension multiple-node loci.

## The del Pezzo ramification divisor {#sec:ramification-divisor}

Let $\widetilde R\subset\widetilde X$ be the strict transform of the fixed curve of $\iota_{\mathrm{dP}}$.
At the node, the total ramification divisor contains the exceptional curve with multiplicity one, and

\[
\widetilde R+E\sim2H.
\]

Let $R_{\widetilde V}$ be the quotient divisor on $\widetilde V$.
Then

\[
\psi^*R_{\widetilde V}=\widetilde R.
\]

::: {#prop-ramification-numerics .proposition}
**Proposition (ramification class and numerical invariants).**  One has

\[
R_{\widetilde V}\sim2L+K_{\widetilde V},
\]

and

\[
R_{\widetilde V}^2=7,
\qquad
R_{\widetilde V}\cdot C=2,
\qquad
K_{\widetilde V}\cdot R_{\widetilde V}=-1,
\qquad
p_a(R_{\widetilde V})=4.
\]
:::

**Proof sketch.**  Pulling back $2L+K_{\widetilde V}$ gives $2H-E=\widetilde R$.
Moreover,

\[
\widetilde R^2=(2H-E)^2=14,
\]

so $R_{\widetilde V}^2=7$.
The remaining formulas follow from $C=-2K_{\widetilde V}$, $R_{\widetilde V}\cdot C=2$, and adjunction.

The divisor $R_{\widetilde V}$ is not the anti-bicanonical curve $C$.
It is the divisor relevant to the KSBA polarization.

## Contraction to the singular Coble surface {#sec:canonical-contraction}

Let

\[
\mu:\widetilde V\longrightarrow V^\sharp
\]

contract $C$.
The discrepancy formula is

\[
K_{\widetilde V}
 =\mu^*K_{V^\sharp}-\frac12C.
\]

Consequently

\[
K_{V^\sharp}\sim_{\mathbb Q}0.
\]

Let $R^\sharp=\mu_*R_{\widetilde V}$.
Then

\[
\mu^*R^\sharp
 =R_{\widetilde V}+\frac12C
 =2L.
\]

It follows that

\[
(R^\sharp)^2=8.
\]

Locally, $R^\sharp$ is the image of the union of the coordinate axes $(uv=0)$ in the quotient singularity $\frac{1}{4}(1,1)$.
Its local class is $2$ in $\operatorname{Cl}(\frac{1}{4}(1,1))\cong\mathbb Z/4$, so it is $\mathbb Q$-Cartier of index $2$.

::: {#def-open-stable-coble-pair .definition}
**Definition (open stable Coble pair).**  An open degree-$2$ stable Coble pair
is

\[
(V^\sharp,\epsilon R^\sharp),
\qquad
0<\epsilon\ll1,
\]

where $V^\sharp$ is the singular canonical contraction and $R^\sharp$ is the
divisorial ramification of the descended del Pezzo involution.
:::

The log-crepant pullback is

\[
\mu^*(K_{V^\sharp}+\epsilon R^\sharp)
 =K_{\widetilde V}
  +\frac{1+\epsilon}{2}C
  +\epsilon R_{\widetilde V}.
\]

For a general member, $C+R_{\widetilde V}$ is simple normal crossing and the coefficients are less than one when $0<\epsilon<1$.
Thus the resolved pair is klt, and so is the singular pair.
If the descent of $L$ is ample, then $K_{V^\sharp}+\epsilon R^\sharp$ is ample.

::: {#warning-index-one-cover .warning}
**Warning (index-one cover).**  The canonical index-one cover of the local
surface singularity $\frac{1}{4}(1,1)$ is the $A_1$ singularity.  Pulling back
further to $\mathbb A^2$ is useful for local log calculations, but it is not
the index-one cover.
:::

# Direct moduli functors, arithmetic groups, and period spaces {#sec:moduli-groups}

## The resolved-cover moduli problem {#sec:cover-moduli}

The autonomous strategy should begin with a stack of labeled K3-cover data.
The following definition is a mathematical specification; representability and equivalence with the singular pair moduli are required theorems.

::: {#def-direct-cover-datum .definition}
**Definition (direct resolved Coble cover datum).**  Over a scheme $S$, a
direct resolved degree-$2$ Coble cover datum consists of

\[
(\widetilde{\mathcal X}/S,
 \mathcal E,
 \iota_{\mathrm{Co}},
 \iota_{\mathrm{dP}},
 \mathcal H,
 \mathscr C)
\]

with the following properties.

1. $\widetilde{\mathcal X}/S$ is a family of K3 surfaces, or a family with the
   controlled ADE singularities allowed by the period problem.
2. $\mathcal E$ is a relative Cartier divisor whose geometric fibers are
   smooth $(-2)$-curves.
3. $\iota_{\mathrm{Co}}$ is a nonsymplectic involution whose divisorial fixed
   locus is $\mathcal E$.
4. $\iota_{\mathrm{dP}}$ is a commuting nonsymplectic involution whose
   divisorial fixed locus is the ramification divisor $\mathcal R$.
5. $\mathcal H$ is a relatively nef and big line bundle with
   $\mathcal H_s^2=4$ and $\mathcal H_s\cdot\mathcal E_s=0$.
6. $\mathscr C$ specifies the positive/nef chamber in which $\mathcal E$ is
   effective and $\mathcal H$ gives the desired contraction.
7. Fiberwise contraction of $\mathcal E$ gives an $A_1$-surface on which the
   Coble involution descends and fixes the node.
:::

The chamber and the effective root are part of the data because an abstract lattice marking does not determine which root is represented by the exceptional curve or which degree-$4$ class gives the projective model.

## The singular-pair moduli problem {#sec:singular-moduli}

::: {#def-direct-singular-datum .definition}
**Definition (direct singular Coble datum).**  Over $S$, a direct singular
Coble datum consists of

\[
(\mathcal V^\sharp/S,
 \mathcal L^\sharp,
 \tau_{\mathrm{dP}},
 \mathcal R^\sharp)
\]

such that each geometric fiber has the following properties.

1. $V^\sharp$ is a normal rational surface with one
   $\frac{1}{4}(1,1)$ singularity.
2. $K_{V^\sharp}\sim_{\mathbb Q}0$.
3. $L^\sharp$ is an ample degree-$2$ class.
4. $\tau_{\mathrm{dP}}$ is an involution whose divisorial fixed locus is
   $R^\sharp$.
5. $R^\sharp$ is ample, $\mathbb Q$-Cartier, and $(R^\sharp)^2=8$.
6. The canonical index-one cover is a K3 surface with one $A_1$ singularity.
:::

::: {#prob-cover-singular-equivalence .problem}
**Required theorem (equivalence of the two open moduli problems).**  After
accounting for the Weyl ambiguity of the exceptional root, contraction,
canonical cover, and quotient define inverse equivalences between the direct
resolved-cover stack and the direct singular-pair stack.  The equivalence is
compatible with base change and automorphisms.
:::

This theorem is the direct replacement for silently identifying a Heegner period point with a geometric Coble pair.

## Four arithmetic groups that must not be conflated {#sec:four-groups}

Fix an embedded root $\alpha\in T_{\mathrm{En}}$ and put $T_{\mathrm{Co}}=\alpha^\perp$.
There are at least four natural groups.

::: {#def-unpolarized-direct-group .definition}
**Definition (direct unpolarized Coble group).**  Dropping the degree-$4$
polarization and the del Pezzo involution from the labeled datum gives the
candidate direct unpolarized group

\[
\Gamma_{\mathrm{Co}}^{\mathrm{dir}}
 :=\operatorname{im}\left(
 Z_{O(L_{K3})}(I_{\mathrm{Co}})_{\alpha,\mathscr C}
 \longrightarrow O^+(T_{\mathrm{Co}})
 \right).
\]

The corresponding geometric monodromy group is defined from the direct
unpolarized Coble moduli stack.  The expected equality
$\Gamma_{\mathrm{Co}}^{\mathrm{dir}}=O^+(T_{\mathrm{Co}})$ is compatible
with the full stabilizer lemma below, but it remains a geometric monodromy
statement until the direct period theorem is proved.
:::

::: {#def-hodge-group .definition}
**Definition (Hodge-theoretic Heegner group).**

\[
\Gamma_{\mathrm{Co},2}^{\mathrm{Hdg}}
 :=\operatorname{im}\left(
   \operatorname{Stab}_{\Gamma_{\mathrm{En},2}}(\mathbb Z\alpha)
   \longrightarrow O^+(T_{\mathrm{Co}})
  \right).
\]
:::

This group is the natural group of a fixed normalized Heegner component once the Enriques construction has been fixed.

::: {#def-direct-group .definition}
**Definition (direct labeled centralizer group).**

\[
\Gamma_{\mathrm{Co},2}^{\mathrm{dir}}
 :=\operatorname{im}\left(
 Z_{O(L_{K3})}(I_{\mathrm{Co}},I_{\mathrm{dP}})_{H,\alpha,\mathscr C}
 \longrightarrow O^+(T_{\mathrm{Co}})
 \right).
\]
:::

This is the arithmetic group naturally attached to the autonomous lattice datum, provided the labeled rigidity theorem holds.

::: {#def-geometric-monodromy .definition}
**Definition (geometric monodromy group).**
$\Gamma_{\mathrm{Co},2}^{\mathrm{geom}}$ is the image of the orbifold
monodromy representation of the connected direct moduli stack of polarized
Coble data on the local system $T_{\mathrm{Co}}$.
:::

Finally, the degree-$2$ marking gives an orthogonal decomposition

\[
A_{T_{\mathrm{En}}}
 \cong A_{U(2)}\perp A_{E_8(2)},
\]

and hence the finite subgroup

\[
P:=O(q_{U(2)})\times O(q_{E_8(2)}).
\]

Using the characteristic class $\eta/2$ to identify the remaining finite quadratic space with the Enriques discriminant space, discriminant gluing suggests the congruence subgroup

\[
\Gamma_{\mathrm{Co},2}^{\mathrm{cong}}
 :=\rho_{T_{\mathrm{Co}}}^{-1}(P).
\]

::: {#prob-group-identification .problem}
**Required theorem (arithmetic and monodromy identification).**  Prove

\[
\Gamma_{\mathrm{Co},2}^{\mathrm{geom}}
 =\Gamma_{\mathrm{Co},2}^{\mathrm{dir}}
 =\Gamma_{\mathrm{Co},2}^{\mathrm{Hdg}}
 =\Gamma_{\mathrm{Co},2}^{\mathrm{cong}}.
\]

Each equality requires a separate argument: global Torelli and parallel
transport for the first, labeled embedding comparison for the second, and
discriminant-form gluing for the third.
:::

Defining one of these groups to be “the group for which the desired semifan works” is circular.

## A lattice-theoretic stabilizer sequence {#sec:stabilizer-sequence}

There is a useful pure lattice calculation.
Let

\[
L_0=\mathbb Z\alpha\oplus T_{\mathrm{Co}}.
\]

The lattice $T_{\mathrm{En}}$ is an index-$2$ overlattice of $L_0$, obtained by adjoining $(\alpha+\eta)/2$.
The gluing subgroup in $A_{\mathbb Z\alpha}\oplus A_{T_{\mathrm{Co}}}$ is generated by

\[
\left(\frac\alpha2,\frac\eta2\right).
\]

The class $\eta/2$ is the characteristic element of the discriminant form of $T_{\mathrm{Co}}\cong I_{2,9}(2)$ and is fixed by every isometry.

::: {#lem-full-stabilizer .lemma}
**Lemma (full orthogonal stabilizer).**  Restriction gives an exact sequence

\[
1\longrightarrow\langle w_\alpha\rangle
\longrightarrow
\operatorname{Stab}_{O^+(T_{\mathrm{En}})}(\mathbb Z\alpha)
\longrightarrow
O^+(T_{\mathrm{Co}})
\longrightarrow1.
\]
:::

**Proof sketch.**  Every isometry of $T_{\mathrm{Co}}$ fixes the characteristic class $\eta/2$, hence preserves the gluing subgroup and extends to the index-$2$ overlattice.
The two extensions differ by the root reflection $w_\alpha$.

This lemma is a lattice statement.
It does not identify the degree-$2$ monodromy group and does not solve the integral isotropic-subspace lifting problem.

## Period domains {#sec:coble-period-domains}

Define

\[
\mathbb D_{\mathrm{Co}}:=\mathbb D(T_{\mathrm{Co}}).
\]

The unpolarized Hodge quotient is naturally

\[
\mathcal F_{\mathrm{Co}}^{\mathrm{Hdg}}
 :=O^+(T_{\mathrm{Co}})\backslash\mathbb D_{\mathrm{Co}}.
\]

The direct and polarized quotients are, provisionally,

\[
\mathcal F_{\mathrm{Co},2}^{\mathrm{dir}}
 :=\Gamma_{\mathrm{Co},2}^{\mathrm{dir}}
   \backslash\mathbb D_{\mathrm{Co}},
\]

and

\[
\mathcal F_{\mathrm{Co},2}^{\mathrm{Hdg}}
 :=\Gamma_{\mathrm{Co},2}^{\mathrm{Hdg}}
   \backslash\mathbb D_{\mathrm{Co}}.
\]

The period theorem for classical Coble surfaces identifies an open subset of an orthogonal modular variety of this lattice type [@DK13].  The direct polarized period theorem and the equality of the two polarized quotients are required results, not consequences of the abstract lattice isomorphism.

## The required diagram of period quotients {#sec:period-diagram}

At the level of fixed embedded period domains, one has inclusions

\[
\mathbb D(T_{\mathrm{Co}})
 \subset\mathbb D(T_{\mathrm{En}})
 \subset\mathbb D(T_{\mathrm{dP}}).
\]

The desired quotient diagram is

\[
\begin{tikzcd}[column sep=large,row sep=large]
\mathcal F_{\mathrm{Co},2}
  \arrow[r]
  \arrow[d]
& \mathcal F_{\mathrm{En},2}
  \arrow[r]
  \arrow[d]
& \mathcal F_{(2,2,0)}
  \arrow[r]
& \mathcal F_4\\
\mathcal F_{\mathrm{Co}}
  \arrow[r]
& \mathcal F_{\mathrm{En}}.
\end{tikzcd}
\]

A diagram of rational domains is not automatically a diagram of arithmetic quotients.
To construct each arrow, one must prove that the relevant group acts through a compatible subgroup of a common $O(L_{K3})$, and one must identify the image group.
The direct arrow to $\mathcal F_{(2,2,0)}$ must later be shown to factor through the Enriques Heegner component.

::: {#prob-period-diagram .problem}
**Required theorem (commuting period diagram).**  The direct and Heegner
arithmetic groups are compatible with the common labeled embedding chain; all
arrows in the displayed diagram are well defined on quotients; and the direct
Coble construction factors through the normalized $(-2)$-Heegner divisor in
$\mathcal F_{\mathrm{En},2}$.
:::

# Baily--Borel boundary and integral cusp problems {#sec:cusps}

## Standard cusp data {#sec:standard-cusps}

Let $T$ have signature $(2,n)$ and let $\Gamma\subset O^+(T)$ be arithmetic.
A $0$-cusp is a $\Gamma$-orbit of primitive isotropic lines $\mathbb Ze\subset T$.
Its hyperbolic cusp lattice is

\[
\overline{T}_e:=e^\perp/\mathbb Ze.
\]

A $1$-cusp is a $\Gamma$-orbit of primitive isotropic planes $J\subset T$.
Its negative-definite quotient is

\[
K_J:=J^\perp/J.
\]

For a fixed line $e$, the stabilizer has an exact sequence

\[
1\longrightarrow U_e
\longrightarrow \operatorname{Stab}_\Gamma(e)
\longrightarrow \Gamma_e
\longrightarrow1,
\]

where $U_e$ is the unipotent radical and $\Gamma_e$ acts on $\overline{T}_e$.
The arithmetic group $\Gamma_e$, not the full orthogonal group of $\overline{T}_e$, is the group relevant to the cusp reflection problem.

## The unpolarized Coble boundary {#sec:unpolarized-cusps}

Since scaling a form does not change its integral orthogonal group,

\[
O(T_{\mathrm{Co}})=O(I_{2,9}).
\]

Standard transitivity results for indefinite odd unimodular forms imply the following [@Wall62; @DK13].

::: {#thm-unpolarized-cusps .theorem}
**Theorem (unpolarized Coble cusps).**  The quotient
$O^+(T_{\mathrm{Co}})\backslash\mathbb D_{\mathrm{Co}}$ has one orbit of
primitive isotropic lines and one orbit of primitive isotropic planes.  For
representatives $e$ and $J$,

\[
e^\perp/e\cong I_{1,8}(2),
\qquad
J^\perp/J\cong I_{0,7}(2).
\]
:::

This theorem concerns the full orthogonal group.
It does not determine the cusps for the polarized subgroup.

## Reduction to the discriminant form {#sec:finite-shadow}

For a $2$-elementary lattice, a primitive isotropic vector of divisibility $2$ determines a nonzero isotropic class in the discriminant group.
Thus reduction modulo the lattice gives maps

\[
\left\{
\Gamma_{\mathrm{Co},2}\text{-orbits of primitive isotropic lines}
\right\}
\longrightarrow
\left\{
\rho(\Gamma_{\mathrm{Co},2})\text{-orbits of singular classes in }A_T
\right\},
\]

and analogous maps for isotropic planes and incident flags.

::: {#warning-finite-shadow .warning}
**Warning (finite shadow versus integral cusp).**  These maps need not be
bijective.  The integral parabolic stabilizer can have a proper image in the
finite stabilizer of the reduced flag.  Consequently, an orbit calculation in
$O(A_{T_{\mathrm{Co}}})$ does not classify Baily--Borel cusps without a
separate integral lifting theorem.
:::

The standard ways to solve this problem are:

1. integral normal forms and explicit Eichler transvections;
2. computation of the images of integral line and plane stabilizers followed by finite double-coset calculations; or
3. a certified integral orbit algorithm, for example of the type developed in [@Dawes22].

## Computational record in the finite quadratic space {#sec:finite-orbits}

A finite calculation was carried out in a $10$-dimensional plus-type quadratic space over $\mathbb F_2$ for the subgroup associated with the proposed degree-$2$ congruence condition.
It produced four orbits of nonzero singular vectors and five orbits of totally singular planes.
The labels below are internal finite labels; they are not cusp labels.

| Finite vector type | Orbit size |
| :--- | ---: |
| $A$ | $135$ |
| $B$ | $2$ |
| $C$ | $270$ |
| $D$ | $120$ |

: Finite singular-vector orbits. {#tbl:finite-vector-orbits}

| Finite plane type | Orbit size |
| :--- | ---: |
| $AAA$ | $1575$ |
| $ABC$ | $270$ |
| $ACC$ | $9450$ |
| $ADD$ | $3780$ |
| $CCD$ | $8640$ |

: Finite totally singular plane orbits. {#tbl:finite-plane-orbits}

A later enhanced calculation decorated a finite plane by one of eight ``stars'' in the natural $S_8$-set attached to its $6$-dimensional quotient.
For a prescribed $S_7$ subgroup it produced seven enhanced plane orbits and thirteen enhanced flag orbits.
This remains a computational record only: the required identification of that $S_7$ with the image of the integral plane stabilizer has not been proved.

::: {#prob-cusp-lifting .problem}
**Required theorem (integral cusp lifting).**  Determine the exact images of
the integral isotropic-line and isotropic-plane stabilizers in the finite
orthogonal group and use them to classify

\[
\Gamma_{\mathrm{Co},2}\backslash
\{\text{primitive isotropic lines}\},
\]

\[
\Gamma_{\mathrm{Co},2}\backslash
\{\text{primitive isotropic planes}\},
\]

and the incident flags.  Give explicit integral representatives and
stabilizers.
:::

## Necessary restrictions on maps to Enriques cusps {#sec:possible-cusp-images}

Suppose the comparison map to the Enriques period quotient has been constructed.
Let $e$ be a Coble isotropic line.
The root $\alpha$ lies in $e^\perp$ and gives a $(-2)$ class in the Enriques cusp lattice.
Therefore an Enriques $0$-cusp whose hyperbolic lattice has all norms divisible by $4$ cannot contain a Coble branch.
In the AEGS numbering, this excludes cusp $1$ and leaves only cusps $2,3,4,5$ as possible images.

Similarly, if $J$ is a Coble isotropic plane, the class of $\alpha$ gives a $(-2)$ vector in $J^\perp/J$.
Hence a Type II Enriques cusp whose negative quotient is $E_8(2)$ cannot contain a Coble branch.
Reading the border types in AEGS Figure 4, the double-rectangle cusps

\[
12,\ 13,\ 14,\ 15,\ 245
\]

map to the segment-flipping $E_8(2)$ cusp and are excluded.
The only possible Enriques $1$-cusp images are therefore

\[
34,\ 35,\ 45,\ 55.
\]

::: {#remark-cusp-images .remark}
**Remark.**  This is a necessary-condition argument, not an integral orbit
classification.  It does not determine how many Coble cusps lie above any of
the four possible image cusps.
:::

An earlier finite-orbit calibration that assigned a Coble branch to cusp $245$ is therefore not compatible with the embedded root criterion and must not be used.

# Reflection theory and Coxeter data {#sec:coxeter}

## The unpolarized cusp chamber {#sec:unpolarized-coxeter}

Write

\[
I_{1,8}(2)
 =\mathbb ZH_0\oplus\bigoplus_{i=1}^8\mathbb ZE_i,
\qquad
H_0^2=2,
\qquad
E_i^2=-2.
\]

Define

\[
r_0=H_0-E_1-E_2-E_3,
\]

\[
r_i=E_i-E_{i+1}\quad(1\le i\le7),
\qquad
r_8=E_8.
\]

Then

\[
r_0^2=\cdots=r_7^2=-4,
\qquad
r_8^2=-2.
\]

::: {#thm-unpolarized-coxeter .theorem}
**Theorem (unpolarized Coble Coxeter chamber).**  A fundamental chamber for
the reflection group of $I_{1,8}(2)$ is defined, for

\[
x=aH_0-\sum_{i=1}^8b_iE_i,
\]

by

\[
b_1\ge b_2\ge\cdots\ge b_8\ge0,
\qquad
 a\ge b_1+b_2+b_3.
\]

The simple roots are $r_0,\ldots,r_8$.  The diagram is the chain

\[
r_1-r_2-r_3-r_4-r_5-r_6-r_7\Rightarrow r_8
\]

with $r_0$ attached to $r_3$ by a single edge.
:::

**Proof sketch.**  Signed permutations of the $E_i$ reduce to the ordered region, and the Cremona reflection in $r_0$ reduces the final inequality.
This is the standard Vinberg chamber for $I_{1,8}$, with the form scaled by $2$.

The unique maximal parabolic subdiagram is obtained by deleting $r_1$ and has type $\widetilde B_7$.
The rank-$8$ elliptic subdiagrams are listed in @tbl:unpolarized-elliptic.

| Deleted node | Elliptic type |
| :--- | :--- |
| $r_0$ | $B_8$ |
| $r_2$ | $A_1+B_7$ |
| $r_3$ | $A_1+A_2+B_5$ |
| $r_4$ | $A_4+B_4$ |
| $r_5$ | $D_5+B_3$ |
| $r_6$ | $E_6+B_2$ |
| $r_7$ | $E_7+A_1$ |
| $r_8$ | $E_8$ |

: Rank-$8$ elliptic subdiagrams of the unpolarized chamber. {#tbl:unpolarized-elliptic}

## Orthogonal wall links {#sec:orthogonal-link}

Let $a$ be a $(-2)$ root in a hyperbolic lattice $M$, and let $b$ be another negative wall normal.
The normal inside $a^\perp$ to the intersection $b^\perp\cap a^\perp$ is the primitive vector proportional to the orthogonal projection of $b$ to $a^\perp$.

::: {#construction-wall-link .construction}
**Construction (orthogonal wall link).**  Define

\[
b_{\operatorname{link}}
 :=\operatorname{prim}\bigl(2b+(b,a)a\bigr).
\]
:::

The formula is integral and defines the correct hyperplane in $a^\perp$.
It is a linear-algebra statement.
It does not imply that $b_{\operatorname{link}}$ is a root of the orthogonal lattice.

::: {#warning-wall-root .warning}
**Warning (restricted wall versus reflection wall).**  A hyperplane obtained
by slicing an ambient Coxeter chamber can fail to be the mirror of an integral
reflection in the sublattice.  Conversely, the orthogonal sublattice can have
reflective roots whose mirrors are invisible in the ambient root system.
:::

A Coble analogue of the AEGS root-folding theorem must prove both directions: that every relevant restricted wall is a Coble root wall and that every Coble root wall meeting the chamber is obtained in the prescribed way.

## Candidate reflection twist at a cusp {#sec:cusp-reflection-twist}

At the full K3-lattice level one has the reflection twist $I_{\mathrm{Co}}=w_\alpha I_{\mathrm{En}}$.
If a primitive isotropic line $e$ is orthogonal to $\alpha$, the involutions induce actions on the cusp quotient $e^\perp/e$.
This suggests the cusp-level candidate

\[
J_{\mathrm{Co}}=w_{\bar\alpha}J_{\mathrm{En}},
\]

where $\bar\alpha$ is the image of $\alpha$ in the cusp lattice.

This formula is not yet a direct folding theorem.
One must prove that the cusp action lifts through the full discriminant gluing and corresponds to the geometric involution, just as AEGS separately prove their lifting lemma.

## Corrected ambient square Gram data {#sec:gram-correction}

In the square ambient K3 cusp diagram, the two black roots $\alpha_{20}$ and $\alpha_{21}$ both have square $-4$.
The edge joining them is thick.
Therefore

\[
(\alpha_{20},\alpha_{21})=4.
\]

The previously used value $2$ gives a Gram matrix of rank $20$, incompatible with the rank-$18$ cusp lattice.
The value $4$ gives the correct rank $18$.

## Candidate wall-slice diagrams {#sec:wall-slices}

Correcting the Gram entry above, one can intersect selected Enriques chambers with selected white-root hyperplanes.
This produces four explicit hyperplane arrangements, denoted

\[
G_{\mathrm{slice}}^2,
\quad
G_{\mathrm{slice}}^3,
\quad
G_{\mathrm{slice}}^4,
\quad
G_{\mathrm{slice}}^5.
\]

The chosen roots in the previously used labeling were $\alpha_{10}$, $\alpha_0$, $\alpha_6$, and $\alpha_{16}$, respectively.
Each displayed sliced wall is a genuine root in the orthogonal lattice in the cases checked symbolically.
No proof was given that the displayed walls form a complete simple system.

The raw numbers of maximal parabolic faces in the four sliced arrangements were

\[
1,\quad3,\quad3,\quad9.
\]

These counts are diagnostic data only.
They disagree with some finite-shadow orbit counts, which indicates that chamber completeness, arithmetic diagram automorphisms, and the calibration of finite orbits must all be resolved before boundary strata are enumerated.

::: {#prob-coxeter-completeness .problem}
**Required theorem (Coble Vinberg and root completeness).**  For every
polarized Coble $0$-cusp:

1. determine the arithmetic cusp lattice and the image of its stabilizer;
2. run Vinberg's algorithm or prove a two-sided root-link theorem;
3. prove that the resulting simple roots define a fundamental chamber;
4. compute the chamber automorphism group and reflection index; and
5. enumerate all maximal parabolic and elliptic subdiagrams modulo the full
   arithmetic group.
:::

A list of vectors or a finite Gram-matrix computation is not a Coxeter theorem without these steps.

# Integral-affine structures, dlt quotients, and stable models {#sec:integral-affine}

## The AEGS dictionary {#sec:aegs-dictionary}

AEGS relate five forms of degeneration data:

\[
\text{period and monodromy}
\longleftrightarrow
\text{Coxeter chamber}
\longleftrightarrow
\text{integral-affine dual complex}
\longleftrightarrow
\text{dlt quotient}
\longleftrightarrow
\text{KSBA stable pair}.
\]

For a primitive isotropic line $e$, a Type III monodromy invariant is a vector

\[
\lambda\in\overline{T}_e\otimes\mathbb R
\]

in the closure of a positive chamber.
If $\{r_i\}$ is a simple-root system, the root coordinates are

\[
\ell_i=(\lambda,r_i)\ge0.
\]

They become edge lengths, internal blowup parameters, and nodal-surgery sizes in a moment or Symington polygon.
A zero coordinate places the monodromy on a wall.
If the wall corresponds to a visible curve, the zero can collapse a path joining two focus-focus singularities.

The direct Coble theory should preserve this dictionary but must add the data of the fixed exceptional root and its quotient branch curve.

## The Coble integral-affine package {#sec:coble-affine-package}

::: {#def-coble-affine-package .definition}
**Definition (candidate polarized Coble integral-affine package).**  A Coble
integral-affine package is a tuple

\[
\bigl(B(\lambda),R_{\mathrm{IA}},E_{\mathrm{IA}},
      \iota_{\mathrm{Co,IA}},\iota_{\mathrm{dP,IA}}\bigr)
\]

where

1. $B(\lambda)$ is the integral-affine dual sphere or Type II segment of a
   K3 divisor model;
2. $R_{\mathrm{IA}}$ is the weighted balanced graph recording the del Pezzo
   ramification divisor;
3. $E_{\mathrm{IA}}$ records the visible class, collapsed path, or marked
   affine stratum associated with the exceptional root $\alpha$;
4. the two affine involutions commute and preserve the full polarized package;
5. the quotient data predicts the branch curve $C$ and the divisor
   $R_{\widetilde V}$ on a Coble dlt model.
:::

The notation $E_{\mathrm{IA}}$ is schematic.
Depending on the cusp, the exceptional root can be represented by a visible path, a collapsed edge, an $I_2$ affine singularity, or equivalent marked data in the triangulation.
A direct theory must specify the correct object cusp by cusp.

## Heegner-wall specialization of an ambient model {#sec:heegner-affine-specialization}

Suppose a degeneration lies in the $\alpha$-Heegner locus and approaches a Type III cusp represented by $e$.
After a suitable marking and base change, one expects

\[
(\alpha,e)=0,
\qquad
(\alpha,\lambda)=0.
\]

If $\alpha$ is represented by a visible path in the chosen integral-affine model, the second equation says that the path has zero affine length.
The corresponding pair of parallel $I_1$ singularities coalesces to an $I_2$ singularity.
This is the same local operation used by AEGS for crossed nodes, but in the Coble problem it records the persistent $A_1$ singularity of the K3 cover.

::: {#remark-affine-local .remark}
**Remark.**  The local collision picture is reliable once the relevant root
has been identified in the genuine cusp lattice.  It cannot be used to prove
that a candidate wall slice is the full Coxeter chamber.
:::

## Required realization theorem {#sec:affine-realization}

::: {#prob-affine-realization .problem}
**Required theorem (direct integral-affine realization).**  For every
sufficiently divisible monodromy invariant in every direct Coble cusp
chamber, construct a K3 divisor model

\[
(\mathcal X,\mathcal R,\mathcal E)\longrightarrow(C,0)
\]

whose dual complex is the prescribed Coble integral-affine package.  Conversely,
show that every direct Coble degeneration admits such a model after finite
base change and allowed dlt modification.
:::

The proof must include polygon closure, parity and divisibility conditions, triangulation, component periods, gluing parameters, and the realization of the exceptional class as a Cartier divisor or contractible ADE configuration.

## Required algebraic extension theorem {#sec:algebraic-extension}

An affine symmetry is not automatically an algebraic involution.
AEGS use limiting-period conditions and invariant component/gluing parameters to extend their involution over a general divisor model.
The Coble version must also retain the exceptional root.

::: {#prob-algebraic-extension .problem}
**Required theorem (algebraic extension of the Coble package).**  A general
divisor model with direct Coble monodromy admits commuting regular involutions

\[
\iota_{\mathrm{Co}},\qquad\iota_{\mathrm{dP}}
\]

such that

\[
\iota_{\mathrm{Co}}(\mathcal E)=\mathcal E,
\qquad
\iota_{\mathrm{Co}}(\mathcal R)=\mathcal R.
\]

The cohomological action is the prescribed labeled lattice action, the
involutions commute on the total space, and equivariant simultaneous
resolution and contraction are compatible with the family.
:::

A proof must not infer regularity solely from the action on the dual complex.
For special degenerations the initial action can be birational and may require contraction of ADE configurations before it becomes regular.

## The direct dlt Coble model {#sec:coble-dlt}

Assume the algebraic extension theorem.
Form the quotient

\[
\widetilde{\mathcal V}:=\mathcal X/\iota_{\mathrm{Co}}.
\]

Let $\mathcal C$ be the divisorial branch locus descending from $\mathcal E$, and let $\mathcal R_{\widetilde V}$ be the quotient of the del Pezzo ramification divisor.
The natural crepant pair is

\[
\left(
\widetilde{\mathcal V},
\frac{1+\epsilon}{2}\mathcal C
 +\epsilon\mathcal R_{\widetilde V}
\right).
\]

::: {#prob-dlt-quotient .problem}
**Required theorem (direct dlt quotient).**  After the prescribed dlt
modification, the above pair is dlt over the base; its fibers are slc; the
boundary contains no prohibited log canonical center; and

\[
K_{\widetilde{\mathcal V}}
 +\frac{1+\epsilon}{2}\mathcal C
 +\epsilon\mathcal R_{\widetilde V}
\]

is relatively big and nef.
:::

The local analysis differs from the Enriques case because the Coble involution has a divisorial fixed locus on the resolved K3 model.
One must analyze fixed components, fixed double curves, triple points, and the interaction between $\mathcal C$ and the conductor.

## Relative Proj and the stable model {#sec:relative-proj}

The dlt model is not the KSBA stable model.
The stable model is the relative log canonical model

\[
\operatorname{Proj}_C
\bigoplus_{m\ge0}
H^0\!\left(
\widetilde{\mathcal V},
 m\left(
 K_{\widetilde{\mathcal V}}
 +\frac{1+\epsilon}{2}\mathcal C
 +\epsilon\mathcal R_{\widetilde V}
 \right)
\right).
\]

After contracting $\mathcal C$ to the singular Coble family, this is expected to agree with the relative Proj for a sufficiently divisible multiple of $\mathcal R^\sharp$.

::: {#prob-stable-proj .problem}
**Required theorem (stable contraction).**  Determine exactly which curves,
components, and conductor strata are contracted by the above relative Proj,
and prove that the resulting family is the KSBA stable family of pairs
$(V^\sharp,\epsilon R^\sharp)$.
:::

## Component classification problem {#sec:component-classification}

The direct Coble quotient can produce surface components with branch boundary $C$, conductor boundary $D$, and ramification divisor $R$.
The appropriate normalized component datum is

\[
\left(
V,
D+\frac{1+\epsilon}{2}C+\epsilon R
\right).
\]

::: {#prob-component-classification .problem}
**Required theorem (Coble component classification).**  Classify all finite
Type III and affine Type II component pairs arising in direct Coble stable
limits.  Give explicit equations or toric models, involutions, quotient
singularities, branch allocation, decorations, and stable contractions; prove
that every component occurs in the list and every listed type occurs.
:::

This is the Coble analogue of the AEGS ABCDE surface classification.
It cannot be obtained merely by replacing the Enriques involution in the existing tables: the resolved Coble involution has a fixed curve.

## Status of adaptations of AEGS examples {#sec:example-status}

Several candidate recipes were identified:

- start with the AEGS cusp-$3$ integral-affine model and impose one additional Coble-root equation;
- start with the cusp-$5$ model, where several crossed-root coordinates already vanish, and impose an independent Coble-root condition;
- start with the non-simple cusp-$2$ model and impose the appropriate white-root wall while retaining the fact that the bottom fixed edge has no ramification support.

These are recipes, not completed examples.
A complete example must specify the integral root, the visible path, the compatible triangulation, the component periods and gluings, the two algebraic involutions, all quotient singularities, and the final $R^\sharp$-trivial contraction.

# Fans, semifans, and semitoroidal compactifications {#sec:semifans}

## Coxeter fans and generalized Coxeter semifans {#sec:generalized-coxeter}

Let $M$ be a hyperbolic cusp lattice, $W$ a reflection group, and $C$ a fundamental chamber.
The Coxeter fan consists of the $W$-translates of $C$ in the rational closure of the positive cone.
If the chamber has finite volume, this is a rational polyhedral fan.

Suppose the simple roots are partitioned into relevant and irrelevant roots.
Let $W_{\mathrm{irr}}$ be generated by the irrelevant reflections.
The generalized chamber is

\[
C_{\mathrm{gen}}
 =\bigcup_{w\in W_{\mathrm{irr}}}wC.
\]

Its $W$-translates form the generalized Coxeter semifan.
Geometrically, a root is relevant only if crossing its wall changes the stable pair after the relative Proj.

::: {#warning-relevance .warning}
**Warning (relevance is geometric).**  In the autonomous Coble theory, a root
cannot be declared relevant merely because it lies on the boundary of an
ambient Enriques or K3 diagram.  Relevance must be characterized by the
Coble package $(R_{\mathrm{IA}},E_{\mathrm{IA}})$ and the resulting stable
contraction.
:::

## Direct Coble semifans {#sec:direct-semifans}

Assume that the direct cusp groups and Coxeter chambers have been computed.
For each direct Coble $0$-cusp, define a root to be relevant if a general crossing of its wall changes at least one of the following stable data:

1. the support or degree distribution of $R^\sharp$;
2. the branch curve or exceptional-root contraction;
3. the normalization components or conductor gluing;
4. the number of surviving double curves or components; or
5. the isomorphism class of the relative Proj.

::: {#prob-direct-semifan .problem}
**Required theorem (direct Coble semifan).**  The maximal regions of
combinatorial constancy of direct Coble stable pairs are exactly the cones of
the generalized Coxeter semifan obtained from the verified direct Coble
Coxeter diagram and the intrinsic relevance marking.
:::

The theorem must determine cusp by cusp whether the irrelevant reflection group is finite, whether the semifan is an actual fan, and whether any Type II parabolic component consists entirely of irrelevant roots.

## Normalized closure of a subtorus {#sec:subtorus-lemma}

The Heegner-restriction strategy uses the following standard toric fact.

::: {#lem-subtorus-normalization .lemma}
**Lemma (normalization of a subtorus closure).**  Let $N\subset M$ be a
saturated sublattice of cocharacter lattices, let $T_N\subset T_M$ be the
corresponding subtorus, and let $X_\Sigma$ be a toric variety for a fan
$\Sigma\subset M_\mathbb R$.  The normalization of the closure of $T_N$ in
$X_\Sigma$ is the toric variety associated with the induced fan

\[
\Sigma|_{N_\mathbb R}
 =\{\sigma\cap N_\mathbb R:\sigma\in\Sigma\},
\]

with the induced lattices saturated.
:::

This lemma is local and toric.
It does not by itself identify the normalized closure of a Heegner divisor in a semitoroidal arithmetic quotient.

## Why semitoroidal restriction is not formal {#sec:restriction-not-formal}

To apply the subtorus lemma to the Coble Heegner locus, one must prove all of the following.

1. The local Heegner branch is the asserted saturated subtorus rather than a translated subtorus or a union of branches.
2. The integral unipotent-center lattice for the Coble cusp is the expected sublattice of the Enriques cusp lattice.
3. The arithmetic cusp stabilizer acts compatibly on the induced fan.
4. The induced local constructions agree along every $1$-cusp.
5. Normalization commutes with the prescribed semitoroidal contractions.
6. The ambient contraction does not identify distinct normalized Coble branches.
7. No additional coarsening occurs after passing to Coble stable pairs.

::: {#prob-restricted-semifan .problem}
**Required theorem (semitoroidal restriction).**  After passage to a common
toroidal refinement, the normalization of the Heegner closure is obtained by
saturated intersection with the Coble cusp subspaces, and the induced
semitoroidal contractions coincide with combinatorial constancy for the
Coble stable-pair family.
:::

Without this theorem, “intersect the AEGS semifans” is a candidate construction rather than a compactification theorem.

# The KSBA moduli space and the two target theorems {#sec:ksba-targets}

## The open KSBA moduli functor {#sec:open-ksba}

Let $\mathfrak M_{\mathrm{Co},2}^{\circ}$ denote the direct open moduli stack of singular Coble data for which the pair

\[
(V^\sharp,\epsilon R^\sharp)
\]

is klt and $K_{V^\sharp}+\epsilon R^\sharp$ is ample.
Define

\[
\overline{\mathfrak M}_{\mathrm{Co},2}^{\mathrm{KSBA}}
\]

to be its closure in the appropriate KSBA stack with fixed coefficient and volume.

The divisor $R^\sharp$ must be defined universally as the divisorial fixed locus of the descended del Pezzo involution.
Choosing a divisor separately on each fiber does not define a moduli problem.

## Autonomous target theorem {#sec:autonomous-target}

::: {#conj-autonomous-theorem .problem}
**Target theorem A (autonomous Coble compactification).**  The direct open
period map identifies

\[
\mathfrak M_{\mathrm{Co},2}^{\circ}
\simeq
\Gamma_{\mathrm{Co},2}^{\mathrm{dir}}
\backslash\mathbb D_{\mathrm{Co}}^{\circ},
\]

for an explicit hyperplane complement.  The normalization of
$\overline{\mathfrak M}_{\mathrm{Co},2}^{\mathrm{KSBA}}$ is the
semitoroidal compactification defined by the explicit direct Coble semifans.
All cusps, Coxeter diagrams, Type II and Type III strata, and fan-versus-semifan loci are explicitly determined.
:::

This theorem is logically independent of the Enriques Heegner comparison.
It requires direct analogues of the entire AEGS proof architecture.

## Heegner comparison target {#sec:heegner-target}

Let $\Delta_\alpha$ be the $(-2)$-Heegner divisor in the degree-$2$ Enriques period quotient, defined using a fixed embedded root.

::: {#conj-comparison-theorem .problem}
**Target theorem B (comparison with the Enriques Heegner divisor).**  The
direct Coble period quotient is canonically isomorphic to the normalization of
$\Delta_\alpha$.  Under this isomorphism:

1. the direct and Heegner arithmetic groups agree;
2. the period maps to $\mathcal F_{\mathrm{En}}$,
   $\mathcal F_{\mathrm{En},2}$, $\mathcal F_{(2,2,0)}$, and
   $\mathcal F_4$ commute;
3. the direct projective construction agrees with the Heegner specialization;
4. the direct cusps and Coxeter diagrams map to the corresponding Enriques
   and K3 data;
5. the direct stable divisor agrees with the restriction of the ambient
   ramification divisor; and
6. the direct semitoroidal compactification is the normalization of the KSBA
   closure of the Heegner divisor inside the AEGS compactification.
:::

Target theorem B is the theorem requested by the original problem.
Target theorem A is a substantial independent theorem and an intermediate strategy, but it becomes a proof of the Heegner statement only after Target theorem B is established.

# Proof strategies and research programs {#sec:strategies}

This section records the proof strategies that emerged, the precise theorem chains each requires, and the points at which earlier attempts failed.
It is not an attempt to advance any of the proofs.

## Strategy A: normalize the Heegner closure inside the AEGS compactification {#sec:strategy-heegner}

### Outline {#sec:strategy-heegner-outline}

Fix a root $\alpha\in T_{\mathrm{En}}$ and let $\Delta_\alpha$ be the corresponding degree-$2$ Heegner component.
Let

\[
\nu_{\mathrm{En}}:
\mathcal F_{\mathrm{En},2}^{\Sigma_{\mathrm{En}}}
\longrightarrow
\overline{\mathcal F}_{\mathrm{En},2}^{\mathrm{KSBA}}
\]

be the AEGS normalization map.
Take the normalization $H_\alpha$ of the closure of $\Delta_\alpha$ in the source.
The strategy is to identify $H_\alpha$ with the normalization of the Coble KSBA closure and compute its local semitoroidal structure.

### Required chain of results {#sec:strategy-heegner-chain}

The strategy requires the following sequence.

::: {#req-A1 .problem}
**A1. Root-orbit and embedded-component lemma.**  The relevant roots form one
orbit under the actual degree-$2$ Enriques group, or the chosen component is
otherwise specified intrinsically.  The stabilizer image on
$T_{\mathrm{Co}}$ is computed.
:::

::: {#req-A2 .problem}
**A2. Root-marked universal-family lemma.**  Over the stack-theoretic
normalization of the Heegner component, there is a universal family in which
the fixed $A_1$ point, its simultaneous resolution after the required Weyl
cover, the exceptional root, and the ambient ramification divisor are
compatible with base change.
:::

::: {#req-A3 .problem}
**A3. Coble-pair identification lemma.**  The restriction of the AEGS stable
pair to the generic Heegner point is precisely
$(V^\sharp,\epsilon R^\sharp)$ of @sec:canonical-contraction, with the same
universal divisor.
:::

::: {#req-A4 .problem}
**A4. Generic reconstruction lemma.**  A general stable Coble pair recovers
its canonical K3 cover, the distinguished $A_1$ point, the degree-$4$ class,
the del Pezzo involution, and the Heegner period point.  Consequently the
restricted finite map is generically injective.
:::

::: {#req-A5 .problem}
**A5. Arithmetic cusp-lifting theorem.**  The Coble cusp orbits, stabilizers,
and maps to Enriques cusps are computed integrally.
:::

::: {#req-A6 .problem}
**A6. Local toroidal normalization theorem.**  In every cusp chart, the
normalized Heegner closure is the saturated toric subvariety associated with
the actual Coble unipotent-center lattice and the induced arithmetic action.
:::

::: {#req-A7 .problem}
**A7. Semitoroidal compatibility theorem.**  The local normalized toric
closures glue along the Type II boundary and are compatible with the AEGS
semitoroidal contractions.
:::

::: {#req-A8 .problem}
**A8. No-further-coarsening theorem.**  Every wall retained by the induced
Coble semifan changes the Coble stable pair; equivalently, the classifying map
from the normalized Heegner closure to the Coble KSBA closure is finite and
has no positive-dimensional fibers.
:::

With A1--A8, the conclusion follows by normality and finite birationality.

### What worked {#sec:strategy-heegner-worked}

The following ingredients are useful and survive scrutiny.

- The root complement $T_{\mathrm{Co}}$ and reflection twist are explicit.
- The open local Coble quotient and stable divisor are explicit.
- The parent AEGS normalization is already finite.
- The normalization of a saturated subtorus closure in an ordinary toric chart is understood.
- Parent charts that are honest fans remain rational polyhedral after intersection with a rational subspace.

### What failed {#sec:strategy-heegner-failed}

The earlier restriction argument failed at the following points.

1. It treated the stabilizer-image group as automatically equal to geometric monodromy.
2. It inferred a quotient map from an inclusion of rational domains without proving group compatibility.
3. It used generic index-one-cover reconstruction without proving recovery of the degree-$4$ projective model and the labeled lattice tuple.
4. It replaced the integral cusp problem by an $O(A)$ computation.
5. It called hyperplane slices Coxeter diagrams without a root-completeness theorem.
6. It assumed that normalization of a toric subtorus closure automatically survives arithmetic quotienting and semitoroidal contraction.

These failures do not discredit Strategy A.  They identify the exact new lemmas it needs.

## Strategy B: autonomous Coble theory in the style of AEGS {#sec:strategy-autonomous}

### Outline {#sec:strategy-autonomous-outline}

This strategy never defines the direct Coble objects as a locus in Enriques moduli.
It begins with the direct cover datum of [Definition (direct resolved Coble cover datum)](#def-direct-cover-datum), computes its period theory, and reproduces Coble analogues of the AEGS constructions.
Only after the autonomous compactification theorem is proved does one compare it with the Heegner divisor.

### Section 2 analogue: open moduli and periods {#sec:strategy-B-section2}

The following results are required in order.

::: {#req-B21 .problem}
**B2.1. Direct projective-model theorem.**  The nodal invariant $(4,4)$
construction defines the complete generic direct Coble family and its
universal divisors.
:::

::: {#req-B22 .problem}
**B2.2. Intrinsic reconstruction theorem.**  The singular Coble pair recovers
the quartic del Pezzo quotient, the two double-cover algebras, the nodal K3
cover, both involutions, and the degree-$4$ class.
:::

::: {#req-B23 .problem}
**B2.3. Labeled lattice classification theorem.**  Compute the simultaneous
eigenspaces of the Klein-four action, their primitive closures and
discriminant forms, and prove the labeled rigidity theorem of
@sec:labeled-lattice-data.
:::

::: {#req-B24 .problem}
**B2.4. Direct global Torelli theorem.**  The marked direct Coble moduli stack
is an explicit arrangement complement
$\mathbb D_{\mathrm{Co}}^\circ$, with the ample/nef chamber and exceptional
root correctly encoded.
:::

::: {#req-B25 .problem}
**B2.5. Direct monodromy theorem.**  The deck group of the marking cover and
the geometric monodromy group equal the labeled centralizer group
$\Gamma_{\mathrm{Co},2}^{\mathrm{dir}}$.
:::

::: {#req-B26 .problem}
**B2.6. Direct stable-pair theorem.**  The universal divisor
$R^\sharp$ is flat, uniformly $\mathbb Q$-Cartier and ample, and the pairs
$(V^\sharp,\epsilon R^\sharp)$ define a separated bounded KSBA moduli
problem for $0<\epsilon\ll1$.
:::

### Section 3 analogue: cusps and reflection chambers {#sec:strategy-B-section3}

::: {#req-B31 .problem}
**B3.1. Integral Baily--Borel classification.**  Classify all primitive
isotropic lines, planes, and flags under
$\Gamma_{\mathrm{Co},2}^{\mathrm{dir}}$, with explicit representatives and
stabilizers.
:::

::: {#req-B32 .problem}
**B3.2. Vinberg theorem at each $0$-cusp.**  Run Vinberg's algorithm for each
actual cusp lattice and arithmetic reflection group.  Prove termination,
completeness of the simple roots, and compute the chamber automorphism group.
:::

::: {#req-B33 .problem}
**B3.3. Full-lattice lift theorem.**  Lift every cusp-lattice involution or
reflection-twist description through the discriminant gluing to the labeled
K3 lattice datum.
:::

::: {#req-B34 .problem}
**B3.4. Parabolic and elliptic exhaustion theorem.**  Enumerate all maximal
parabolic and relevant elliptic subdiagrams modulo the arithmetic chamber
automorphism group and verify agreement with the independently computed
isotropic-plane orbits.
:::

### Section 4 analogue: integral-affine and dlt models {#sec:strategy-B-section4}

::: {#req-B41 .problem}
**B4.1. Mirror and polygon theorem.**  Construct, for every direct Coble
cusp, the mirror anticanonical pair, moment polygons, Symington surgeries, and
root-coordinate formulas.
:::

::: {#req-B42 .problem}
**B4.2. Integral-affine realization theorem.**  Realize every sufficiently
divisible chamber point by a divisor model carrying the full Coble affine
package.
:::

::: {#req-B43 .problem}
**B4.3. Affine-symmetry characterization theorem.**  Characterize the direct
Coble period locus exactly by the presence of the prescribed affine
involutions and exceptional-root data.
:::

::: {#req-B44 .problem}
**B4.4. Algebraic involution theorem.**  Promote the affine symmetries to
commuting regular involutions on general divisor models and control the
birational-to-regular modification for special models.
:::

::: {#req-B45 .problem}
**B4.5. dlt quotient and relative-Proj theorem.**  Prove the dlt and slc
properties, canonical bundle formula, positivity, and exact stable
contractions.
:::

### Sections 5--7 analogues: semifans and boundary classification {#sec:strategy-B-section5}

::: {#req-B51 .problem}
**B5.1. Coble recognizability theorem.**  Prove that the direct divisor
package is recognizable from limiting Hodge and combinatorial data in the
sense required by the Alexeev--Engel compactification theory.
:::

::: {#req-B52 .problem}
**B5.2. Geometric relevance theorem.**  Determine exactly which direct
Coxeter walls change the stable pair and hence which roots are relevant.
:::

::: {#req-B53 .problem}
**B5.3. Generalized Coxeter semifan theorem.**  Prove that the direct regions
of combinatorial constancy are the generalized Coxeter semifans of the
verified direct chambers.
:::

::: {#req-B54 .problem}
**B5.4. Direct KSBA normalization theorem.**  Construct the classifying map,
prove properness, finiteness, generic injectivity, and absence of further
coarsening.
:::

::: {#req-B61 .problem}
**B6.1. Coble component classification.**  Classify all finite and affine
component pairs, including equations, quotient involutions, branch curves,
ramification divisors, and contractions.
:::

::: {#req-B71 .problem}
**B7.1. Complete boundary theorem.**  List every Type II and Type III stable
Coble surface and prove compatibility with the Baily--Borel and semitoroidal
incidence diagrams.
:::

### Advantages and principal difficulties {#sec:strategy-B-assessment}

The autonomous strategy has three advantages.

1. The arithmetic group is defined geometrically rather than inherited.
2. Relevance and the stable divisor are intrinsic to Coble pairs.
3. The final comparison with Enriques moduli becomes a discrete rigidity theorem rather than part of every local construction.

Its principal difficulties are equally clear: direct monodromy, complete Vinberg calculations, algebraic realization of the fixed exceptional curve in degenerations, and a Coble-specific recognizable-divisor theorem.

## Strategy C: direct K3-to-Coble folding or reflection twisting {#sec:strategy-folding}

### Candidate mechanism {#sec:strategy-C-mechanism}

The identity

\[
I_{\mathrm{Co}}=w_\alpha I_{\mathrm{En}}
\]

suggests that the Coble theory can be obtained from the ambient K3 involution space by a direct reflection-twisted folding, rather than by first folding to Enriques and then slicing by $\alpha^\perp$.

At a cusp, the candidate operation is

\[
J_{\mathrm{Co}}=w_{\bar\alpha}J_{\mathrm{En}}.
\]

### Required chain {#sec:strategy-C-chain}

::: {#req-C1 .problem}
**C1. Classification of admissible ambient actions.**  Classify involutions
of the two reflective K3 cusp lattices whose fixed lattices have the Coble
cusp types and whose full-lattice lifts preserve the labeled direct Coble
data.
:::

::: {#req-C2 .problem}
**C2. Direct root-folding theorem.**  Classify all ambient root orbits under
the direct Coble involution and prove that every negative folded vector is a
Coble root and every Coble root arises in this way.
:::

::: {#req-C3 .problem}
**C3. Chamber-intersection theorem.**  Prove that intersection of an ambient
K3 chamber with the direct Coble fixed subspace is a fundamental chamber for
the direct Coble reflection group.
:::

::: {#req-C4 .problem}
**C4. Full-lattice and geometric realization theorem.**  Lift the cusp action
to $L_{K3}$ and identify it with the geometric pair of involutions on divisor
models.
:::

::: {#req-C5 .problem}
**C5. Comparison with the wall-link construction.**  Prove that the direct
folded chamber agrees with the orthogonal link of the corresponding Enriques
root wall after the comparison of labeled embeddings.
:::

### Failure mode in the earlier attempt {#sec:strategy-C-failure}

The previous argument verified only the orthogonal-projection formula for selected walls.
It did not prove the root converse, chamber completeness, or full-lattice lifting.
Thus it produced wall-slice diagrams rather than Coxeter diagrams.
Strategy C remains viable only if C1--C5 are proved.

## Strategy D: computation-first arithmetic and Vinberg analysis {#sec:strategy-computational}

### Legitimate uses {#sec:strategy-D-legitimate}

Computation is well suited to the following tasks.

- verifying lattice signatures, discriminant groups, and primitive closures;
- computing centralizers of explicit lattice involutions;
- enumerating finite discriminant-form orbits once the integral stabilizer images are known;
- running Vinberg's algorithm in explicit cusp lattices;
- certifying parabolic and elliptic subdiagram exhaustion;
- checking integral-affine polygon closure and involution symmetry;
- computing local invariant rings, divisor classes, and intersection numbers.

### Invalid substitutions {#sec:strategy-D-invalid}

Computation does not replace the following parametric statements.

- A finite $O(A)$ orbit computation does not identify integral cusps.
- A Gram matrix does not certify that a root list is a complete simple system.
- A finite list of monodromy vectors does not prove an integral-affine realization theorem.
- A family of explicit curves does not prove coverage of the moduli space.
- A local quotient calculation does not identify the universal KSBA divisor.

Each script must therefore state a verification contract: the exact finite or symbolic assertion it certifies and the theorem it does not prove.

## Strategy E: hybrid direct-open and inherited-boundary approach {#sec:strategy-hybrid}

A potentially efficient hybrid is to prove the direct open period and monodromy theorem first, then use the AEGS ambient stable family only to construct boundary models.
The comparison with the Heegner divisor is made at the open level before the boundary is analyzed.

The required chain is:

1. direct projective coverage and labeled rigidity;
2. equality of direct monodromy with the Heegner stabilizer group;
3. open-period factorization through $\mathcal F_{\mathrm{En},2}$;
4. restriction of the AEGS family to the now identified direct period space;
5. integral cusp and Vinberg calculations for the direct group;
6. normalized toroidal restriction and semitoroidal compatibility;
7. generic reconstruction/no-further-coarsening.

This strategy reduces duplication of integral-affine existence theorems but still requires all arithmetic and comparison steps.
It is not equivalent to simply declaring the Coble compactification to be a closed subspace of the AEGS compactification.

# Common errors, caveats, and dependency-sensitive warnings {#sec:footguns}

The following warnings are stated in self-contained form and cross-reference the constructions they affect.

## Surface-theoretic warnings {#sec:surface-footguns}

::: {#warn-coble-enriques .warning}
**Warning (Coble is not Enriques).**  The smooth resolution
$\widetilde V$ is rational and has non-torsion canonical class.  The singular
surface $V^\sharp$ is $\mathbb Q$-Calabi--Yau only after contracting the
anti-bicanonical $(-4)$-curve.  Arguments using $K_Z$ torsion on an Enriques
surface cannot be transferred to $\widetilde V$.
:::

::: {#warn-singularity-index .warning}
**Warning (order versus canonical index).**  The notation
$\frac{1}{4}(1,1)$ records a quotient group of order $4$.  The Cartier index of
the canonical class is $2$.
:::

::: {#warn-normality .warning}
**Warning (normality versus boundary nonnormality).**  The generic
$\frac{1}{4}(1,1)$ Coble quotient is normal.  Irreducible nonnormal stable
surfaces can occur only through conductor self-identifications or other
boundary phenomena.
:::

::: {#warn-anticanonical-ramification .warning}
**Warning (anti-bicanonical curve versus stable divisor).**  The divisor
$C\in|-2K_{\widetilde V}|$ is the branch curve of the Coble cover on the
resolution.  The stable divisor is $R^\sharp$, the descended del Pezzo
ramification divisor.  The two are related by the crepant formula in
@sec:canonical-contraction but are not equal.
:::

::: {#warn-quasi-ample .warning}
**Warning (quasipolarization versus polarization).**  The natural degree-$2$
class on $\widetilde V$ is orthogonal to $C$ and is not ample.  It becomes
ample only after contracting the complete null locus.  Any moduli group that
purports to remember an ample class on $\widetilde V$ is using the wrong
object.
:::

::: {#warn-special-null .warning}
**Warning (special Heegner intersections).**  On the generic one-node locus,
$C$ is the only null curve.  On higher Heegner intersections additional
curves may be null and must also be contracted before the singular degree-$2$
polarization becomes ample.
:::

::: {#warn-two-heegner .warning}
**Warning (Coble versus unigonal Heegner divisors).**  The Coble locus is the
$(-2)$-Heegner arrangement associated with a fixed node and a
$\frac{1}{4}(1,1)$ quotient.  The unigonal locus is a distinct $(-4)$-Heegner
divisor whose projective model uses $\mathbb P(1,1,2)$.  The two constructions
must not be interchanged.
:::

::: {#warn-ramification-source .warning}
**Warning (which involution defines the stable divisor).**  In AEGS and in
the proposed Coble theory, the stable divisor is the divisorial fixed locus of
the del Pezzo involution.  The Enriques involution is fixed-point free on the
generic Enriques K3 cover, and the Coble involution fixes the exceptional
curve only on the resolution.  Neither of these is the source of
$R^\sharp$.
:::

::: {#warn-quarter-not-ade .warning}
**Warning (the Coble singularity is not ADE).**  The singularity
$\frac{1}{4}(1,1)$ is a non-Gorenstein cyclic quotient singularity.  ADE
arguments apply only after passing to the canonical $A_1$ cover or to the
resolution, and the boundary coefficients must be tracked through that
passage.
:::

## Group and period warnings {#sec:group-footguns}

::: {#warn-group-fiat .warning}
**Warning (group by fiat).**  The Hodge stabilizer image,
centralizer image, congruence inverse image, and geometric monodromy group are
distinct definitions; see @sec:four-groups.  Equality must be proved.  Choosing
one definition because it makes the desired compactification statement true
is circular.
:::

::: {#warn-isometry-rigidity .warning}
**Warning (abstract isometry is not labeled rigidity).**  An isomorphism
$T_{\mathrm{Co}}\cong I_{2,9}(2)$ does not determine the embedding into
$L_{K3}$, the degree-$4$ class, the exceptional root, the second involution,
or the chamber.  Strategy B requires the labeled rigidity theorem of
@sec:labeled-lattice-data.
:::

::: {#warn-domain-quotient .warning}
**Warning (domain inclusion versus quotient morphism).**  An inclusion of
type-IV domains does not by itself descend to arithmetic quotients.  The
groups must arise from compatible subgroups of a common orthogonal group.
This issue controls the diagram in @sec:period-diagram.
:::

::: {#warn-direct-factorization .warning}
**Warning (direct construction versus Heegner theorem).**  A direct Coble
period quotient inside the K3 involution space is a separate theorem until
its group, labeled embedding, and universal family are shown to factor
through the Enriques Heegner construction.  Strategy B must be followed by
Target theorem B.
:::

::: {#warn-cover-smoothing .warning}
**Warning (smoothing the cover versus smoothing the quotient).**  An arbitrary
smoothing of the nodal K3 cover need not carry the node-fixing involution.
The explicit invariant $(4,4)$ family of @sec:equivariant-smoothing does give
an equivariant smoothing; no general conclusion should be drawn without a
family-level extension theorem.
:::

## Cusp and Coxeter warnings {#sec:cusp-footguns}

::: {#warn-orbit-groups .warning}
**Warning (four orbit problems).**  Orbits under
$O(T_{\mathrm{Co}})$, $O^+(T_{\mathrm{Co}})$,
$\Gamma_{\mathrm{Co},2}$, and $O(A_{T_{\mathrm{Co}}})$ can all differ.  A
claim about one group cannot be transferred to another without an exact
sequence, a stabilizer-image calculation, or an integral transitivity theorem.
:::

::: {#warn-cusp-map .warning}
**Warning (cusp maps require embedded representatives).**  A permutation of
cusp labels is not a proof of a Baily--Borel map.  One must exhibit an
isotropic line or plane inside the common embedded lattice chain and compute
its divisibility and arithmetic orbit in both groups.
:::

::: {#warn-rectangles .warning}
**Warning (AEGS Figure 4 border types).**  The double-rectangle Enriques
$1$-cusps are $12,13,14,15,245$; the single-rectangle cusps are
$34,35,45,55$.  The former map to the segment-flipping quotient lattice
$E_8(2)$ and cannot contain a $(-2)$ Coble root in the negative quotient.
Earlier assignments that treated $245$ as a Coble image are incompatible with
this lattice obstruction.
:::

::: {#warn-wall-slice .warning}
**Warning (wall slice is not Coxeter diagram).**  The construction in
@sec:orthogonal-link gives an arrangement of restricted hyperplanes.  It
becomes a Coxeter chamber only after root integrality, simplicity,
completeness, and arithmetic-index statements are proved.
:::

::: {#warn-parabolic-exhaustion .warning}
**Warning (parabolic inspection is not exhaustion).**  Type II rays are
arithmetic orbits of maximal parabolic subdiagrams of the complete chamber.
Listing visually apparent affine subdiagrams is insufficient unless a
Vinberg computation or classification proves that no others occur.
:::

::: {#warn-gram .warning}
**Warning (square-diagram Gram entry).**  The black nodes
$\alpha_{20}$ and $\alpha_{21}$ are joined by a thick edge and have inner
product $4$, not $2$.  Any computation based on the latter value has the wrong
rank.
:::

::: {#warn-correct-ambient .warning}
**Warning (the correct reflective ambient space).**  The reflective cusp
diagrams used by AEGS belong to the hyperelliptic degree-$4$ K3 involution
space $\mathcal F_{(2,2,0)}$, not to the full quartic K3 moduli space
$\mathcal F_4$.  Any direct folding strategy must explain its relation to
$\mathcal F_{(2,2,0)}$ before using the ambient diagrams.
:::

## Integral-affine and stable-pair warnings {#sec:affine-footguns}

::: {#warn-affine-algebraic .warning}
**Warning (affine symmetry versus algebraic involution).**  An involution of a
dual complex predicts but does not prove an involution of the degeneration.
One must impose the correct limiting-period condition and choose invariant
component and gluing moduli; see @sec:algebraic-extension.
:::

::: {#warn-crossed-node .warning}
**Warning (crossed node).**  A crossed Coxeter node is not merely a diagram
symmetry.  It includes a root reflection, forces the corresponding root
coordinate to vanish, and is realized by an $I_1$--$I_1$ collision to an
$I_2$ affine singularity.
:::

::: {#warn-fixed-edge .warning}
**Warning (fixed affine edge need not support ramification).**  In the
non-simple AEGS cusp, a fixed bottom edge has no support in the ramification
polarization.  Coble relevance must likewise be read from the divisor package,
not from fixed loci alone.
:::

::: {#warn-dlt-stable .warning}
**Warning (dlt model versus stable model).**  The quotient dlt model can
contain $R^\sharp$-trivial curves, components, and conductor strata.  The KSBA
model is obtained only after the relative Proj of @sec:relative-proj.
:::

::: {#warn-restrict-semifan .warning}
**Warning (restriction versus compactification of the restriction).**  The
intersection of an ambient semifan with a Heegner subspace is not automatically
the semitoroidal normalization of the Heegner closure.  The arithmetic,
normalization, gluing, and no-further-coarsening statements of
@sec:restriction-not-formal are indispensable.
:::

# Dependency graph for further work {#sec:dependency-graph}

The following diagram records the logical order of the autonomous strategy.
An arrow means that the lower statement uses the upper statement.

\[
\begin{tikzcd}[row sep=large,column sep=large]
\text{projective coverage}
 \arrow[d]
& \text{labeled lattice rigidity}
 \arrow[d]
\\
\text{direct period theorem}
 \arrow[r]
& \text{geometric monodromy group}
 \arrow[d]
\\
\text{integral cusp classification}
 \arrow[d]
& \text{full-lattice cusp lifts}
 \arrow[dl]
\\
\text{Vinberg chambers and parabolics}
 \arrow[d]
\\
\text{integral-affine realization}
 \arrow[d]
\\
\text{algebraic involutions and dlt quotients}
 \arrow[d]
\\
\text{component classification and relative Proj}
 \arrow[d]
\\
\text{geometric relevance and direct semifans}
 \arrow[d]
\\
\text{direct KSBA normalization theorem}.
\end{tikzcd}
\]

The later comparison with the Heegner divisor requires, in addition,

\[
\begin{tikzcd}[row sep=large,column sep=large]
\text{embedded-chain comparison}
 \arrow[d]
& \text{group equality}
 \arrow[d]
\\
\text{commuting open-period diagram}
 \arrow[d]
& \text{universal divisor comparison}
 \arrow[dl]
\\
\text{cusp and Coxeter comparison}
 \arrow[d]
\\
\text{semifan comparison}
 \arrow[d]
\\
\text{identification of KSBA closures}.
\end{tikzcd}
\]

The arithmetic cusp classification precedes the Coxeter theorem because the lattice and group acting at a cusp must be known before a chamber is computed.
The stable-model analysis precedes the relevance marking because relevance is defined by the relative Proj.
Any proof order that reverses either dependency risks classifying the wrong objects.

# Consolidated status ledger {#sec:status-ledger}

The following table summarizes the present mathematical status.

| Item | Status | Controlling section |
| :--- | :--- | :--- |
| Local invariant $(4,4)$ node construction | established | @sec:invariant-system |
| Local $\frac{1}{4}(1,1)$ quotient | established | @sec:cover-quotient |
| Explicit equivariant smoothing | established for the projective family | @sec:equivariant-smoothing |
| Coverage of the complete Coble locus | required theorem | @sec:projective-coverage |
| $T_{\mathrm{Co}}\cong\langle2\rangle\oplus U(2)\oplus E_8(2)$ | established | @sec:orthogonal-complement |
| $S_{\mathrm{Co}}$ and reflection twist | established as lattice calculations | @sec:reflection-twist |
| Labeled embedding uniqueness | required theorem | @sec:labeled-lattice-data |
| Degree-$2$ class is quasipolarized on $\widetilde V$ | established | @sec:resolved-diagram |
| $\lvert-2K_{\widetilde V}\rvert=\{C\}$ generically | established | @sec:anti-bicanonical |
| Stable divisor $R^\sharp$ and numerical formulas | established on the projective one-node locus | @sec:ramification-divisor |
| Open KSBA pair $(V^\sharp,\epsilon R^\sharp)$ | established fiberwise on the general locus | @sec:canonical-contraction |
| Direct moduli equivalence in families | required theorem | @sec:singular-moduli |
| Equality of four arithmetic groups | required theorem | @sec:four-groups |
| Full orthogonal stabilizer exact sequence | established lattice lemma | @sec:stabilizer-sequence |
| Unpolarized cusp count | established with standard lattice input | @sec:unpolarized-cusps |
| Polarized cusp count | not established | @sec:finite-shadow |
| Finite $O(A)$ orbit tables | established computation | @sec:finite-orbits |
| Unpolarized Coxeter chamber | established | @sec:unpolarized-coxeter |
| Polarized wall-slice arrangements | established computations | @sec:wall-slices |
| Polarized Coble Coxeter diagrams | not established | @sec:coxeter |
| Integral-affine Coble package | defined; realization open | @sec:coble-affine-package |
| Direct dlt and stable-model theorem | open | @sec:coble-dlt |
| Exact Coble semifans | open | @sec:direct-semifans |
| Normalization of the Heegner KSBA closure | target theorem | @sec:heegner-target |

: Consolidated status of the Coble compactification project. {#tbl:status-ledger}

# Computational record and verification contracts {#sec:computational-record}

This section records calculations that may be reused after the corresponding parametric theorems are proved.

## Explicit invariant branch curve {#sec:explicit-curve}

On the affine chart $x_0=y_0=1$, one checked the invariant polynomial

\[
\begin{aligned}
f(x,y)={}&29x^4y^4+23x^4y^2+19x^4
 +17x^3y^3+13x^3y\\
&+11x^2y^4+7x^2y^2+x^2
 +5xy^3+xy+3y^4+2y^2.
\end{aligned}
\]

Its quadratic part is

\[
x^2+xy+2y^2,
\]

with discriminant $-7$.
Gr\"obner-basis calculations on the four standard affine charts give one singular point, at $(0,0)$ on the displayed chart, and no singularities on the other charts.

**Verification contract.**  This calculation proves nonemptiness of the open one-node invariant family.
It does not prove that the family is the complete Coble moduli space.

## Lattice calculations {#sec:computational-lattices}

Symbolic Gram-matrix computations verify:

- the signature and determinant of the displayed $T_{\mathrm{Co}}$ and $S_{\mathrm{Co}}$ decompositions;
- the eigenspaces of the reflection twist on an explicit model;
- the rank correction for the ambient square diagram when $(\alpha_{20},\alpha_{21})$ is changed from $2$ to $4$.

**Verification contract.**  These computations certify explicit lattice models.
They do not prove labeled embedding uniqueness or geometric monodromy.

## Finite cusp computations {#sec:computational-cusps}

The finite-orbit data of @sec:finite-orbits and the enhanced star calculation are reproducible.
They are inputs to, not substitutes for, the integral cusp-lifting theorem.

**Verification contract.**  The scripts compute orbits under explicitly specified finite matrix groups.
They do not identify those groups with the images of integral parabolic stabilizers.

## Wall-slice computations {#sec:computational-slices}

The corrected ambient Gram matrix reproduces the selected wall-link roots and the four candidate arrangements.
The scripts test root integrality for the displayed vectors and enumerate parabolic and elliptic subgraphs of the candidate graphs.

**Verification contract.**  The scripts verify the finite graph calculations for the input root list.
They do not prove that the list is a complete Vinberg simple system or that graph automorphisms equal arithmetic chamber automorphisms.

# Appendix: corrected candidate wall-slice arrangements {#sec:appendix-wall-slices}

This appendix records the finite arrangements obtained by slicing selected AEGS Enriques chambers by selected white-root hyperplanes.
The data are retained because they are useful starting points for a direct Vinberg calculation.
They are not asserted to be complete Coxeter diagrams.

White vertices below have square $-2$ and black vertices have square $-4$.
A double arrow denotes the non-simply-laced Coxeter edge between roots of unequal length; $==$ denotes a thick edge; and $\cdots$ denotes a dotted edge.

## Slice over the triangular ambient cusp {#sec:slice-2}

The arrangement $G_{\mathrm{slice}}^2$ has nine vertices.
The vertices $c_0,\ldots,c_7$ are black and $c_8$ is white.
Its edges are

\[
c_0-c_3,
\qquad
c_1-c_2-c_3-c_4-c_5-c_6-c_7\Rightarrow c_8.
\]

This arrangement agrees with the standard unpolarized chamber after a relabelling, but its identification with a polarized cusp requires the integral cusp theorem.

## First square-cusp slice {#sec:slice-3}

The white vertices are $c_0,c_7,c_8$ and the black vertices are $c_1,\ldots,c_6,c_9,c_{10}$.
The nonzero edges are

\[
c_0\Rightarrow c_1,
\qquad
c_0==c_8,
\]

\[
c_1-c_2-c_3-c_4-c_5-c_6\Rightarrow c_7,
\]

\[
c_3-c_9,
\qquad
c_7\Rightarrow c_{10},
\qquad
c_8\cdots c_{10}.
\]

## Second square-cusp slice {#sec:slice-4}

The white vertices are $c_5,c_7$ and all other displayed vertices are black.
The edges are

\[
c_0-c_1-c_2-c_3-c_4\Rightarrow c_5,
\]

\[
c_0-c_6\Rightarrow c_7,
\qquad
c_0-c_8,
\qquad
c_4-c_9.
\]

## Third square-cusp slice {#sec:slice-5}

The white vertices are $c_0,c_8,c_9,c_{10},c_{11}$ and the black vertices are $c_1,\ldots,c_7,c_{12}$.
The edges are

\[
c_0\Rightarrow c_1,
\qquad
c_0\Rightarrow c_7,
\qquad
c_0==c_{11},
\]

\[
c_1-c_2-c_3-c_4-c_5-c_6-c_7,
\]

\[
c_2\Rightarrow c_8,
\qquad
c_4\Rightarrow c_9,
\qquad
c_6\Rightarrow c_{10},
\]

\[
c_8\Rightarrow c_{12},
\qquad
c_{10}\Rightarrow c_{12},
\qquad
c_9==c_{11},
\qquad
c_{11}\cdots c_{12}.
\]

## Discarded cusp calibration {#sec:discarded-cusp-calibration}

One later finite calculation decorated each totally singular plane by one of eight stars and assigned the resulting seven finite orbits the labels

\[
245,\quad34,\quad45,\quad
35^{(2)},\quad35^{(6)},\quad
55^{(2)},\quad55^{(6)}.
\]

This calibration is not retained.
The integral parabolic image used to define the star action was not proved, and the label $245$ is incompatible with the necessary $(-2)$-class condition in @sec:possible-cusp-images.
The finite enhanced orbit calculation can still be reused after the actual integral stabilizer image is known, but the displayed labels have no current arithmetic meaning.

# Appendix: adversarial consistency audit {#sec:adversarial-audit}

The report was checked against the principal failure modes identified in the research discussions.
The purpose of this appendix is not to add new mathematics, but to make explicit where each ambiguity is resolved or retained as an open theorem.

| Audit question | Resolution in this report |
| :--- | :--- |
| Are the ambient Enriques and del Pezzo lattices stated with all summands? | Yes; see @sec:aegs-lattices. |
| Is the Coble surface distinguished from its smooth rational resolution? | Yes; see Definitions in @sec:surface-classes. |
| Is $\frac{1}{4}(1,1)$ treated as a normal non-Gorenstein quotient with canonical index $2$? | Yes; see @sec:surface-terminology and @warn-singularity-index. |
| Is the canonical index-one cover correctly identified as $A_1$? | Yes; see @warning-index-one-cover. |
| Is the stable divisor distinguished from the anti-bicanonical curve? | Yes; see @sec:ramification-divisor and @warn-anticanonical-ramification. |
| Is the degree-$2$ class identified as a quasipolarization before contraction? | Yes; see @sec:resolved-diagram. |
| Are the Hodge stabilizer, direct centralizer, congruence group, and geometric monodromy separated? | Yes; see @sec:four-groups. |
| Is equality of these groups stated as a theorem already proved? | No; it is Required theorem @prob-group-identification. |
| Is abstract lattice isometry distinguished from labeled embedding rigidity? | Yes; see @sec:labeled-lattice-data and @warn-isometry-rigidity. |
| Are period-domain inclusions distinguished from maps of arithmetic quotients? | Yes; see @sec:period-diagram and @warn-domain-quotient. |
| Is the direct K3 construction required to factor through the Enriques construction? | Yes; this is Target theorem B in @sec:heegner-target. |
| Is an $O(A)$ orbit computation used as an integral cusp theorem? | No; see @sec:finite-shadow and @warn-finite-shadow. |
| Are the possible Enriques Type II cusp images read with the correct single/double rectangle convention? | Yes; see @sec:possible-cusp-images and @warn-rectangles. |
| Are wall slices called Coxeter diagrams? | No; see @sec:wall-slices and @warn-wall-slice. |
| Is the corrected thick edge $\alpha_{20}$--$\alpha_{21}$ recorded? | Yes; see @sec:gram-correction. |
| Are maximal parabolic lists required to be exhaustive? | Yes; see @prob-coxeter-completeness and @warn-parabolic-exhaustion. |
| Is an affine involution treated as automatically algebraic? | No; see @sec:algebraic-extension. |
| Is the dlt quotient identified with the stable model before relative Proj? | No; see @sec:relative-proj and @warn-dlt-stable. |
| Is restriction of an ambient semifan treated as formal? | No; see @sec:restriction-not-formal. |
| Is the autonomous direct strategy presented as already proving the Heegner theorem? | No; the two target theorems are separated in @sec:ksba-targets. |
| Are computational scripts assigned explicit mathematical limits? | Yes; see @sec:computational-record. |

: Adversarial consistency audit. {#tbl:adversarial-audit}

Two residual points are intentionally left as research problems rather than silently resolved.

1. The exact descent category of the degree-$2$ class on the singular Coble model---Cartier line bundle, reflexive sheaf, or numerical class in special families---must be fixed as part of the direct moduli theorem.
   The generic projective model supports the stated numerical and ampleness properties.
2. The family-theoretic construction of the canonical cover and simultaneous resolution is not used as a formal black box.
   It is isolated in the cover--singular equivalence theorem and in the root-marked universal-family lemma of Strategy A.

# Source map {#sec:source-map}

The following references indicate where the standard theories used in this report may be consulted.

- AEGS [@AEGS25] is the controlling model for the projective diagram, unique embedding chain, cusp folding, integral-affine quotient models, generalized Coxeter semifans, and the finite/no-further-coarsening step.
- Nikulin [@Nik79] is the primary source for even $2$-elementary lattices, discriminant forms, and primitive embeddings.
- Namikawa [@Nam85] and Sterk [@Sterk91] control the Enriques period and cusp theory used in the Heegner strategy.
- Dolgachev--Kond\=o [@DK13] treat orthogonal modular descriptions of classical Coble surfaces.
- Vinberg [@Vin72; @Vin75] supplies the reflection-group algorithms and Coxeter theory.
- Alexeev--Engel and related work [@AE22; @AE23; @AEH21; @AET23; @ABE22] supplies recognizable divisors, integral-affine models, and semitoroidal normalizations of K3 moduli.
- Koll\'ar, Koll\'ar--Mori, Koll\'ar--Xu, and Birkar [@KM98; @Kol23; @KX20; @Bir23] supply the MMP and KSBA framework.
- Kulikov, Persson--Pinkham, Friedman--Scattone, Gross--Hacking--Keel, Engel, and Engel--Friedman [@Kul77; @PP81; @FS86; @GHK15a; @GHK15b; @Eng18; @EF21] supply the degeneration and integral-affine background.
- The Stacks Project [@Stacks] is a general reference for relative spectra, finite morphisms, normalization, descent, and family-theoretic language.

# Conclusion {#sec:conclusion}

The Coble compactification problem now has a precise mathematical ontology.
The open geometry is governed by invariant nodal $(4,4)$ curves, a nodal K3 cover with two commuting involutions, the lattice

\[
T_{\mathrm{Co}}
 \cong \langle2\rangle\oplus U(2)\oplus E_8(2),
\]

and the singular stable pair

\[
(V^\sharp,\epsilon R^\sharp).
\]

On the resolution, the degree-$2$ class is a quasipolarization, $|-2K|$ consists generically of one rational $(-4)$-curve, and the crepant dlt boundary is

\[
\frac{1+\epsilon}{2}C+\epsilon R_{\widetilde V}.
\]

The principal unresolved issues are not the local quotient calculation or the basic lattice type.
They are the labeled embedding rigidity, equality with geometric monodromy, integral cusp lifting, complete Vinberg chambers, algebraic realization of the Coble affine package, intrinsic relevance of walls, and the comparison between the autonomous compactification and the normalized Enriques Heegner closure.

The autonomous strategy organizes these issues into direct Coble analogues of the AEGS theorem chain.
The Heegner strategy organizes them into arithmetic normalization, universal-family, and no-further-coarsening statements.
A complete proof may combine the two, but it must eventually identify their lattices, groups, divisors, cusp structures, semifans, and KSBA families as the same mathematical objects.

# References {.unnumbered}

::: {#refs}
:::
