---
title: "Degree-2 Coble Surfaces and the Coble Heegner Divisor"
subtitle: "A mathematical research report on the established framework, precise constructions, open comparison problems, and proof strategies"
author: "Working research report"
date: "2026-07-23"
lang: en
toc: true
toc-depth: 4
number-sections: true
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

## Introduction and logical status {#sec-introduction}

### Purpose {#sec-purpose}

This report fixes a common mathematical language for the study of the degree-2 Coble locus associated with the $(-2)$-Heegner arrangement in the period space of numerically degree-$2$ polarized Enriques surfaces.
It has four purposes.

1. It records the definitions, constructions, lattice identifications, local calculations, and numerical formulas that have been isolated with a level of precision suitable for further research.

2. It distinguishes those statements that follow from standard results or direct calculations from those that remain comparison theorems, lifting problems, or compactification problems.

3. It formulates two principal approaches to the compactification problem: the **Heegner-restriction approach** and the **autonomous Coble approach**.

4. It gives a theorem-by-theorem research program for completing either approach and later identifying the two constructions.

The intended reader is assumed to know the theory of K3 and Enriques surfaces, integral lattices, type-IV period domains, Baily--Borel and toroidal compactifications, Kulikov models, KSBA stable pairs, Nikulin's theory of $2$-elementary involutions, and the compactification framework developed by Alexeev and Engel.
Standard terminology is cited rather than reproved; see @sec-terminology and the bibliography.

The report is not a proof of the final Coble compactification theorem.
It is a mathematical specification of the objects and the exact statements that a proof must establish.
This distinction is essential because several plausible computations discussed below are computations of finite quadratic spaces or hyperplane slices, not yet computations of arithmetic cusps or Vinberg chambers.

### Convention on logical status {#sec-status-convention}

The following convention is used throughout.

- A statement labeled **Theorem**, **Proposition**, **Lemma**, or **Corollary** is either a standard cited result, a result of AEGS, or a direct calculation whose hypotheses are stated explicitly.

- A statement labeled **Required theorem**, **Required lemma**, or **Problem** is not presently established in the Coble setting.
  It records an exact unit of work needed by one of the proposed strategies.

- A **Candidate construction** is a mathematically defined construction whose relation to the desired moduli problem has not yet been proved.

- A **Computational record** is a reproducible finite or symbolic calculation.
  It is not promoted to an arithmetic or geometric theorem unless the relevant lifting or realization statement is separately proved.

- A **Warning** records an invalid inference or a conflation of two distinct objects.

### Central compactification problem {#sec-central-problem}

Let $T_{\mathrm{En}} \cong U\oplus U(2)\oplus E_8(2)$ be the Enriques anti-invariant lattice in the AEGS degree-$2$ construction, and let $\alpha\in T_{\mathrm{En}}$ be a primitive vector with $\alpha^2=-2$.
The hyperplane $\bD(T_{\mathrm{En}})\intersect\alpha^\perp$ is the period domain of the Coble Heegner locus.
The final problem is to identify the normalization of the KSBA closure of that locus as an explicit semitoroidal compactification, including the arithmetic group, all Baily--Borel cusps, the cusp reflection chambers, the integral-affine and dlt models, the relevant semifans, and the toroidal versus strictly semitoroidal locus.

The ambient AEGS theorem supplies the model for the required level of specificity: the compactification is meaningful only after the lattices, groups, divisors, cusp data, Coxeter data, and stable-pair contractions have all been identified.
Those data are part of the theorem, not optional consequences.

### Principal distinction between the two strategies {#sec-two-strategies}

There are two conceptually different ways to organize the proof.

1. **Heegner-restriction strategy.** Begin with the AEGS Enriques moduli problem and regard the Coble locus as the normalization of a fixed $(-2)$-Heegner component.
   The principal new work is to justify passage to arithmetic quotients, normalize the boundary restriction, solve the cusp lifting problem, identify the restricted semifans, and prove that the resulting KSBA family loses no moduli.

2. **Autonomous Coble strategy.** Define a direct moduli problem of K3 covers with a Coble involution, a commuting del Pezzo involution, a degree-$4$ class, and a distinguished exceptional root.
   Reproduce direct analogues of the AEGS period, cusp, Vinberg, integral-affine, dlt, recognizable-divisor, and semitoroidal theorems.
   Only after this independent theory is complete does one prove that it agrees with the Enriques Heegner construction.

The second strategy avoids using the Enriques compactification as a black box, but it creates a separate comparison theorem at the end.

The second strategy asks for a *commuting del Pezzo involution* on the Coble covers, and that is a geometric requirement: an involution of the surface. What the lattice records is weaker, and the two must not be conflated. On the covers of [@DK13, section 3] the distinguished root $\alpha$ is the class of the ramification curve and is effective; the lattice candidate carried by the two isotropic summands of the polarization is orthogonal to $\alpha$ and carries it to $-\alpha$, so that candidate is not the action of an automorphism in the marking of the construction (@cor:no-del-pezzo-involution-coble-cover). That is a statement about one lattice candidate. It does not show that no commuting del Pezzo involution exists, and no source exhibits one; the geometric requirement stands as stated.
The first strategy uses more existing geometry, but it requires careful normalization and monodromy arguments that cannot be replaced by the phrase “restrict the semifan.”

## Terminology, notation, and standard background {#sec-terminology}

### General conventions {#sec-general-conventions}

The ground field is $\bC$.
All lattices are free abelian groups of finite rank equipped with a nondegenerate symmetric bilinear form.
The K3 lattice is $L_{K3}=II_{3,19}\cong U^3\oplus E_8^2$, where $E_8$ is negative definite.
If $M$ is a lattice, then $M(n)$ denotes the same abelian group with its bilinear form multiplied by $n$.
The orthogonal group preserving a chosen component of the positive cone is denoted $O^+(M)$.

For an even lattice $M$, its discriminant group and discriminant quadratic form are $A_M=M^*/M$ and $q_M:A_M\too \bQ/2\bZ$.

A primitive embedding is an embedding whose cokernel is torsion free.
The classification and gluing theory of even $2$-elementary lattices are used in the sense of Nikulin [@Nik80].

### Surface singularities and covers {#sec-surface-terminology}

A **rational double point** or **ADE singularity** is a Du Val surface singularity.
An **$A_1$-singularity** is analytically $\{xy-z^2=0\}\subset\bA^3$.

The cyclic quotient singularity

\[
\frac{1}{4}(1,1)
  =\bA^2_{u,v}/\mu_4,
\qquad
\zeta\cdot(u,v)=(\zeta u,\zeta v),
\]

has quotient group of order $4$ and canonical index $2$.
Its canonical index-one cover is the $A_1$-singularity $\bA^2/\{\pm1\}$, not the smooth plane.
The smooth plane is the canonical degree-$4$ quasi-\'etale cover.

A normal surface is $R_1$ and $S_2$.
In particular, the $\frac{1}{4}(1,1)$-singularity is normal.
Nonnormal surfaces can nevertheless occur at the KSBA boundary through conductor self-gluings; this phenomenon is logically separate from the local quotient singularity.

The terms **index-one cover**, **reflexive power**, **deminormal**, **semi-log-canonical**, and **divisorially log terminal** are used in the standard MMP sense [@KM98; @Kol23; @Stacks].
In particular, an slc pair is tested by requiring the normalized pair with conductor to be log canonical, not klt.

### K3, Enriques, and Coble terminology {#sec-surface-classes}

A K3 surface is a smooth projective surface $X$ with $K_X\sim0$ and $H^1(X,\mathcal O_X)=0$.
An Enriques surface is a smooth projective surface $Z$ with $2K_Z\sim0$, $K_Z\not\sim0$, and $q(Z)=0$; see [@CD89; @CDL25].

The word **Coble surface** is used in two closely related senses in the literature.
To remove ambiguity, this report uses the following notation.

::: {.definition #def:singular-coble title="singular Coble quotient"}
A *singular Coble quotient* is a normal rational surface $V^\sharp$ obtained as the quotient of a K3 surface $X^\sharp$ with one $A_1$-singularity by a nonsymplectic involution that fixes the singular point and is otherwise free in codimension one.
The quotient has one singularity of type $\frac{1}{4}(1,1)$.
:::

::: {.definition #def:resolved-coble title="resolved Coble surface"}
The *resolved Coble surface* $\wV$ is the minimal resolution of $V^\sharp$.
It is a smooth rational surface satisfying

\[
|-K_{\wV}|=\varnothing,
\qquad
|-2K_{\wV}|\ne\varnothing
\]

on the classical one-node locus.
:::

The resolved surface is the object traditionally called a classical Coble surface.
The singular quotient is the natural $K$-trivial object for the small-coefficient KSBA problem.

### Polarizations {#sec-polarization-terminology}

A **quasipolarization** is a nef and big line bundle.
A polarization is ample.
This distinction is essential in the Coble setting: the natural class on $\wV$ is orthogonal to the anti-bicanonical $(-4)$-curve and is therefore not ample.
It becomes ample after contracting the complete null locus.

### Period domains and Heegner divisors {#sec-period-terminology}

For a lattice $T$ of signature $(2,n)$, a connected type-IV domain is

\[
\bD(T)
 =\left\{
 [\omega]\in\bP(T\otimes_\ZZ\bC)
 : (\omega,\omega)=0,
   (\omega,\overline\omega)>0
 \right\}^{+}.
\]

If $\Gamma\subset O^+(T)$ is arithmetic, the quotient $\Gamma\backslash\bD(T)$ is a quasi-projective orthogonal modular variety.
For a negative vector $r\in T$, the image of $\bD(T)\intersect r^\perp$ is a **Heegner divisor** or arrangement divisor.
See [@BB66; @Loo03] for the compactification theory and [@Nik80; @Nam85] for the relevant Enriques lattice geometry.

A primitive isotropic line in $T$ determines a zero-dimensional Baily--Borel boundary component, called a **$0$-cusp**. A primitive isotropic plane determines a one-dimensional boundary component, called a **$1$-cusp**. The arithmetic orbit, not merely the rational isotropic subspace, is part of the cusp datum.

### Reflection theory {#sec-reflection-terminology}

Let $M$ be hyperbolic.
For a negative vector $r\in M$, the reflection is

\[
w_r(x)=x-\frac{2(x,r)}{r^2}r.
\]

The vector $r$ is a **root** if $w_r\in O(M)$; equivalently, $2\div(r)\in r^2\bZ$.

A **Coxeter chamber** is a fundamental chamber for a reflection group acting on the positive cone.
Its codimension-one walls are perpendicular to simple roots.
A maximal parabolic subdiagram determines an isotropic ray and hence a Type II direction.
An elliptic subdiagram determines a Type III cone.
The terminology and algorithms are those of Vinberg [@Vin72; @Vin75].

### Degenerations and integral-affine structures {#sec-degeneration-terminology}

A **Kulikov model** is a semistable $K$-trivial model of a degeneration of K3 surfaces [@Kul77; @PP81].
Type II degenerations have dual complex a segment; Type III degenerations have dual complex a $2$-sphere.
Type III dual complexes carry canonical integral-affine structures with singularities [@Eng18; @EF21; @GHK15a].

A **divisor model** is a Kulikov or dlt model carrying a nef extension of the distinguished divisor.
Its integral-affine polarization is a weighted balanced graph on the dual complex [@ABE22; @AE22].
A **visible curve** is a curve class represented by a path joining affine singularities with parallel monodromy.
Collapsing such a path can merge two $I_1$ affine singularities into an $I_2$ singularity.

### KSBA and semitoroidal compactifications {#sec-compactification-terminology}

A KSBA stable pair $(X,B)$ is a projective deminormal pair such that $(X,B)$ is slc and $K_X+B$ is ample and $\bQ$-Cartier [@Kol23].
For small-coefficient polarized Calabi--Yau pairs, boundedness and independence of sufficiently small $\epsilon$ are used in the form of [@KX20; @Bir23].

A toroidal compactification is defined by compatible rational polyhedral fans at the rational boundary components.
A semitoroidal compactification is defined by compatible semifans; cones may have infinitely many rational generators [@Loo03; @AE23].
A generalized Coxeter semifan is obtained from a Coxeter fan by removing the walls generated entirely by roots that do not occur in the stable-pair combinatorics [@AET23; @AEGS25].

## The ambient AEGS framework {#sec-aegs-framework}

### The projective Klein-four diagram {#sec-aegs-projective}

Let $Y=\bP^1\cross\bP^1$ and $\tau(x,y)=(-x,-y)$ on the dense torus.
Let $B\in|-2K_Y|=|\mathcal O_Y(4,4)|$ be $\tau$-invariant, with at worst ADE singularities, and assume that $B$ avoids the four fixed points of $\tau$.
The double cover $\pi:X\too Y$ branched along $B$ is a K3 surface with at worst ADE singularities.
Writing $X$ as $z^2+f(x,y)=0$, one has three commuting involutions

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

### The AEGS lattice package {#sec-aegs-lattices}

The involutions act on $L_{K3}=U^3\oplus E_8^2$ with eigenspaces

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

::: {.theorem #thm:aegs-rigidity title="AEGS embedding rigidity"}
The primitive embedding chain

\[
T_{\mathrm{En}}\embeds T_{\mathrm{dP}}
  \embeds L_{K3}
\]

is unique up to $O(L_{K3})$.
:::

::: {.proof}

This is [@AEGS25, §3].

Uniqueness up to $O(L_{K3})$ means that every embedding of $T_{\mathrm{En}}$ into $L_{K3}$ extending the chosen one differs by an isometry of the ambient lattice, so no construction built from the chain can depend on a choice of primitive complement.
That is the sense in which the statement is a model for the labeled rigidity the Coble problem needs: the label is the extra structure -- in this case the involution and the polarization -- and the question is whether it too is unique up to the stabilizer rather than only up to the full orthogonal group.
:::

This theorem is the model for the stronger labeled rigidity statement needed for the Coble problem.
It prevents later constructions from depending on a hidden coordinate choice.

### AEGS arithmetic groups and period maps {#sec-aegs-groups}

AEGS define

\[
\Gamma_{\mathrm{En},2}
 =\im\left(
   \{g\in O(L_{K3}):gI_{\mathrm{En}}=I_{\mathrm{En}}g,
                         \ g(H)=H\}
   \too O(T_{\mathrm{En}})
  \right).
\]

They prove that this is the stabilizer of the Enriques period subdomain inside the del Pezzo arithmetic quotient.
Consequently the period-domain inclusion gives a finite generically injective map $\mcf_{\mathrm{En},2} \too \mcf_{(2,2,0)}$.

The group definition is geometric: it is taken from the common K3 lattice, the involution, and the polarization.
This is the standard that any direct Coble group must meet.

### The AEGS compactification theorem {#sec-aegs-main-theorem}

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

## Direct Coble geometry from invariant $(4,4)$ curves {#sec-projective-coble}

### The invariant linear system {#sec-invariant-system}

The vector space $H^0\bigl(Y,\mathcal O_Y(4,4)\bigr)^\tau$ has basis the monomials whose two affine exponents have even sum.
It has dimension $13$, so its projectivization is $\bP^{12}$.

Fix a $\tau$-fixed point $p\in Y$.
Choose local coordinates $(x,y)$ centered at $p$.
An invariant local equation has the form

\[
f(x,y)
 =a_{00}+a_{20}x^2+a_{11}xy+a_{02}y^2
  +\text{terms of degree at least }4.
\]

There are no linear terms.

::: {.lemma #lem:node-condition title="node condition"}
The curve $B=(f=0)$ has an ordinary node at $p$ if and only if $a_{00}=0$ and $a_{11}^2-4a_{20}a_{02}\ne0$.
:::

::: {.proof}
The first condition says that $p\in B$.
Invariance kills the linear part.
The second condition says that the quadratic tangent cone is nondegenerate.
This is the analytic criterion for an ordinary plane node.

A general member satisfying these conditions is smooth away from $p$.
This is an open condition, and it is enough to exhibit one member having no other singularities.
A symbolic example is recorded in @sec-computational-record.
:::

### Toric interpretation {#sec-coble-toric-model}

Let $Q$ be the square polytope of $\mathcal O_Y(4,4)$.
The quotient $W=Y/\tau$ is the toric surface defined by the same rational polygon but with cocharacter lattice $\bZ^2_{\mathrm{ev}} =\{(a,b)\in\bZ^2:a+b\in2\bZ\}$.

The invariant monomials are precisely the lattice points of $Q$ in this even sublattice.
If $P$ is the pyramid over $Q$ with apex corresponding to $z^2$, the K3 hypersurface is defined in the toric threefold $V_P$.
The quotient by the sign involution uses the lattice

\[
\bZ^3_{\mathrm{ev}}
 =\{(a,b,c)\in\bZ^3:a+b+c\in2\bZ\}.
\]

Passing through a chosen torus-fixed point is the vanishing of the coefficient of the corresponding vertex monomial.
The nondegeneracy of the quadratic part is the local node condition of the preceding lemma.

### The nodal K3 cover and the Coble quotient {#sec-cover-quotient}

Let $X^\sharp=\{z^2=f(x,y)\}\too Y$.

Then $X^\sharp$ has an $A_1$-singularity over $p$.
The involutions

\[
\iota_{\mathrm{dP}}(x,y,z)=(x,y,-z),
\qquad
\iota_{\Co}(x,y,z)=(-x,-y,-z)
\]

commute.
The first is the del Pezzo deck involution.
The second fixes the $A_1$-point.

::: {.proposition #prop:local-quarter title="local Coble quotient"}
The quotient $X^\sharp/\iota_{\Co}$ has a singularity of type $\frac{1}{4}(1,1)$ at the image of the node.
:::

::: {.proof}

The node of the branch curve lifts to an $A_1$ singularity of the double cover, so
$$
X^\sharp_{\mathrm{an}}\cong\{xy-z^2=0\}\subseteq\bC^3
$$
at the preimage of the node.
The map $\bA^2_{u,v}\to\{xy-z^2=0\}$, $(u,v)\mapsto(u^2,v^2,uv)$, is surjective with fibres the orbits of $(u,v)\mapsto(-u,-v)$, so $\{xy-z^2=0\}\cong\bA^2_{u,v}/\{\pm1\}$.

The involution $\iota_{\Co}$ does not act here as the deck transformation $\iota_{\mathrm{dP}} = (x,y,-z)$ of the double cover, whose fixed locus through the node is the pair of branches $\{uv = 0\}$ of the branch curve, but as $(x,y,z)\mapsto(-x,-y,-z)$, which preserves $\{xy = z^2\}$ because $(-x)(-y) = (-z)^2$.
On $\bA^2_{u,v}$ this is $(u,v)\mapsto(iu,iv)$: the unique lift, since $z=uv$ must change sign while $x=u^2$ and $y=v^2$ are fixed, and $iu$ and $iv$ retain the correct squares.

Composing the two quotients gives $\bA^2/\mu_4$ acting by $(u,v)\mapsto(\zeta u,\zeta v)$ for $\zeta^4=1$, which is the cyclic quotient singularity $\frac14(1,1)$ of @def:coxeter-vinberg-diagram's notation for quotient weights.
So the quotient has a $\frac14(1,1)$ point at the image of the node, and that is the only singular point arising from the node because the action is free away from the origin of $\bA^2$.
:::

### Equivariant smoothing {#sec-equivariant-smoothing}

Vary the constant coefficient $a_{00}$ in a one-parameter family.
For $a_{00}\ne0$, the branch curve avoids the fixed point $p$, the K3 cover is smooth near the corresponding fiber, and the involution $\iota_{\Co}$ has no point over $p$.
If the branch curve avoids all four $\tau$-fixed points, then the same fixed-point calculation shows that $\iota_{\Co}$ is fixed-point free.
Its quotient is an Enriques surface.

::: {.proposition #prop:explicit-smoothing title="explicit Coble-to-Enriques smoothing"}
The invariant $(4,4)$ family obtained by varying $a_{00}$ gives an explicit equivariant smoothing of the singular Coble quotient to Enriques quotients.
:::

::: {.proof}

By @prop:local-quarter the singular quotient is $\bA^2/\mu_4$ of type $\frac14(1,1)$ at the image of the node, and the smoothing is the family obtained by restoring the constant term killed there.
For $a_{00}\ne0$ the branch curve misses the four $\tau$-fixed points, so the K3 cover is smooth over the corresponding fibre and the involution $\iota_{\Co}$ acts on it without fixed points; a fixed-point-free involution on a K3 surface is Enriques by definition, so the quotient is Enriques and the fibre is smooth.
Varying $a_{00}$ through $0$ gives a one-parameter family whose general fibre is that quotient and whose special fibre is the singular one, which is a smoothing, and the involution acts on the whole family, which is the equivariance.

The proposition asserts existence of one mechanism and nothing more: it does not claim that every abstract smoothing of the K3 cover extends the node-fixing involution, and that gap is genuine rather than an omission -- an abstract smoothing need not be equivariant, and a non-equivariant one would not quotient to a family of Enriques surfaces at all.
:::

This proposition proves existence of one smoothing mechanism.
It does not imply that every abstract smoothing of the K3 cover carries an extension of the node-fixing involution.

### Dimension and coverage {#sec-projective-coverage}

The projective invariant linear system has dimension $12$.
Imposing $a_{00}=0$ gives a hyperplane, and the connected centralizer of $\tau$ in $\Aut(Y)$ has dimension $2$.
Thus the expected moduli dimension is $12-1-2=9$.

The finite symmetry group permutes the four fixed points.

::: {.problem #prob:projective-coverage title="Required theorem (projective coverage and intrinsic reconstruction)"}
The quotient of the open nodal invariant $(4,4)$ locus by the full centralizer of $\tau$ is the complete direct moduli stack of generic degree-$2$ Coble data.
Equivalently, the projective diagram can be reconstructed intrinsically from the Coble pair, and the resulting period map has image the full relevant period-domain component.
:::

A dimension count and one explicit family do not prove this theorem.
A proof must establish irreducibility at the level of the actual arithmetic group and recover the K3 cover, the two involutions, and the degree-$4$ class from the Coble datum.

## The Coble lattice package {#sec-coble-lattices}

### The orthogonal complement lattice {#sec-orthogonal-complement}

Write $T_{\mathrm{En}} \cong U\oplus E(2)$ and $E=U\oplus E_8$.

Choose a standard basis $e,f$ of the first copy of $U$, and define $\alpha=e-f$ and $\eta=e+f$.

Then $\alpha^2=-2$, $\eta^2=2$, and $(\alpha,\eta)=0$.

The notation $\eta$ is deliberately used here: the letter $H$ is reserved for the degree-$4$ K3 polarization in the AEGS construction.

::: {.proposition #prop:coble-transcendental title="Coble anti-invariant lattice"}
The orthogonal complement of $\alpha$ in $T_{\mathrm{En}}$ is

\[
T_{\Co}
 :=\alpha^\perp_{T_{\mathrm{En}}}
 \cong \langle2\rangle\oplus U(2)\oplus E_8(2).
\]

It has signature $(2,9)$, rank $11$, discriminant group $(\bZ/2)^{11}$, and $2$-elementary invariant $\delta=1$.
Equivalently, $T_{\Co}\cong I_{2,9}(2)$.
:::

::: {.proof}

*The complement inside the first copy of $U$.*
Write the first summand $U=\bZ e\oplus\bZ f$ with $e^2=f^2=0$ and $e\cdot f=1$, and put $\alpha=e-f$, $\eta=e+f$.
Then
$$
\alpha^2=-2,\qquad \eta^2=2,\qquad \alpha\cdot\eta=(e-f)\cdot(e+f)=e^2-f^2+e\cdot f-f\cdot e=0,
$$
and $e=\tfrac12(\eta+\alpha)$, $f=\tfrac12(\eta-\alpha)$, so $\bZ\alpha\oplus\bZ\eta$ is the sublattice of $U$ of index $2$ with Gram matrix $\operatorname{diag}(-2,2)$.
An element $x=ae+bf$ satisfies $x\cdot\alpha=(ae+bf)\cdot(e-f)=-a+b$, so $x\in\alpha^{\perp}$ exactly when $a=b$, that is $\alpha^{\perp}\cap U=\bZ\eta=\langle2\rangle$.
Since $U=(\bZ\alpha\oplus\bZ\eta)\otimes$ nothing else in the summand, and $E(2)$ is orthogonal to $U$, the complement is
$$
T_{\Co}=\alpha^{\perp}_{T_{\mathrm{En}}}=\bZ\eta\oplus E(2)\cong\langle2\rangle\oplus U(2)\oplus E_8(2).
$$

*Rank and signature.*
$\langle2\rangle$ contributes $(1,0)$, $U(2)$ contributes $(1,1)$ because the isotropic basis $e,f$ of $U$ survives the twist, and $E_8(2)$ is negative definite of rank $8$; by @def:signature signatures add over an orthogonal sum of nondegenerate summands, so $\signature(T_{\Co})=(2,1+8)=(2,9)$ and the rank is $1+2+8=11$.

*Discriminant group.*
Each summand has determinant a power of $2$, so $T_{\Co}$ is integral and its discriminant is a $2$-group; by @prop:discriminant-orthogonal-sum the discriminant of an orthogonal sum is the orthogonal sum of the discriminants, and here
$$
\abs{A_{\langle2\rangle}}=2,\qquad \abs{A_{U(2)}}=4=2^2,\qquad \abs{A_{E_8(2)}}=2^8,
$$
the first because $\langle2\rangle$ is rank one with Gram $(2)$, the second because $\det U(2)=(-2)^2=4$, the third because $\det E_8=1$ makes $\det E_8(2)=2^8$.
So $\abs{A_{T_{\Co}}}=2^{1+2+8}=2^{11}$, and since $2T_{\Co}^{\#}\subseteq T_{\Co}$ the group is $(\bZ/2)^{11}$.

*The invariant $\delta$.*
By @def:two-elementary-isotropic-types and the criterion of @thm:two-elementary-classification, $\delta(T_{\Co})=0$ exactly when the quadratic form $q_L$ takes values in $\bZ/2\bZ\subseteq\bQ/2\bZ$.
For the $\langle2\rangle$ summand with generator $\eta$ of square $2$, the dual vector is $\eta/2$ and
$$
q(\eta/2)=\tfrac{1}{4}\,\eta^2=\tfrac12.
$$
For $\delta$ (@def:two-elementary-isotropic-types) one has $\delta(T_{\Co}) = 0$ exactly when the image of $q$ lies in $\bZ/2\bZ\subseteq\bQ/2\bZ$, and in that quotient the canonical $\bZ/2\bZ$ is $\set{[0], [1]}$. The $\langle2\rangle$ summand gives $q(\eta/2) = [\tfrac12]$, and $[\tfrac12]\ne[0]$ and $[\tfrac12]\ne[1]$ in $\bQ/2\bZ$, so it alone gives $\delta = 1$. The $U(2)$ summand gives $q\bigl((e+f)/2\bigr) = \tfrac14(e+f)^2 = 1$, i.e. the class $[1]$, which lies in $\bZ/2\bZ$ and so does not change the verdict. Hence $\delta(T_{\Co})=1$.

Finally $T_{\Co}$ is even: every vector of $\langle2\rangle\perp U(2)\perp E_8(2)$ has even square, $\eta^2 = 2$ being even in $\bZ$. An even $2$-elementary lattice of rank $11$ with $A=(\bZ/2)^{11}$ and $\delta=1$ is unique (@def:two-elementary-isotropic-types), and this one is $I_{2,9}(2)$ in the notation of @sec-unimodular-lattice-classification.
:::

### The invariant lattice and the reflection twist {#sec-reflection-twist}

Let $I_{\mathrm{En}}$ be the Enriques involution on the K3 lattice, acting as $+1$ on $S_{\mathrm{En}}$ and as $-1$ on $T_{\mathrm{En}}$.
Let $w_\alpha$ be the reflection in the root $\alpha$.

::: {.construction #cons:reflection-twist title="reflection twist"}
Define

\[
I_{\Co}:=w_\alpha I_{\mathrm{En}}.
\]
:::

Since $I_{\mathrm{En}}(\alpha)=-\alpha$, the two factors commute.

::: {.proposition #prop:coble-eigenspaces title="eigenspaces of the reflection twist"}
One has

\[
L_{K3}^{I_{\Co}=1}
  =S_{\mathrm{En}}\oplus\bZ\alpha
  \cong U(2)\oplus E_8(2)\oplus\langle-2\rangle,
\]

and

\[
L_{K3}^{I_{\Co}=-1}
  =\alpha^\perp_{T_{\mathrm{En}}}
  =T_{\Co}.
\]

Thus the invariant lattice is

\[
S_{\Co}
 \cong U(2)\oplus E_8(2)\oplus\langle-2\rangle
 \cong I_{1,10}(2).
\]
:::

::: {.proof}

*The eigenspaces over* $\bQ$. The involution $I_{\mathrm{En}}$ acts as $+1$ on $S_{\mathrm{En}}$ and as $-1$ on $T_{\mathrm{En}}$, and $w_\alpha$ fixes $\alpha^\perp$ and sends $\alpha\mapsto-\alpha$, so over $\bQ$ the composite $I_\Co = w_\alpha I_{\mathrm{En}}$ acts as $+1$ on $S_{\mathrm{En}}\oplus\bZ\alpha$ and as $-1$ on $\alpha^{\perp T_{\mathrm{En}}} = T_\Co$. Three points of integrality have to be checked, and are not assumptions.

*The gluing, and the extension of the factors.* $S_\En\oplus T_\En\subseteq\lkt$ has index $2^{10}$ with the full graph gluing of its two discriminant forms; $I_\En$ acts trivially on $A_{S_\En}\oplus A_{T_\En}$ because the forms are $2$-elementary and $-\id$ is the identity there, so the gluing subgroup is preserved and $I_\En$ extends to an integral isometry of $\lkt$. And $w_\alpha(x) = x+(x\cdot\alpha)\alpha$ is integral on $\lkt$ because $x\cdot\alpha\in\bZ$ for $x\in\lkt$. Hence $I_\Co = w_\alpha I_\En\in\Orth(\lkt)$.

*The invariant lattice.* Write $y\in\lkt^{I_\Co}$ as $y = y_S+y_T$ over $\bQ$ with $y_S\in S_\En^\#$ and $y_T\in T_\En^\#$, possible because $S_\En$ is primitive. Then
$$I_\Co y = y_S - w_\alpha(y_T) = y_S - y_T - (y_T\cdot\alpha)\,\alpha,$$
so $y = I_\Co y$ forces $2y_T = -(y_T\cdot\alpha)\alpha$. Writing $y_T = q\alpha + r$ with $r$ in the $\alpha$-orthogonal part of $T_\En^\#$ gives $2r = 0$ and hence $r = 0$, so $y_T = q\alpha$; and testing $q\alpha\in T_\En^\#$ against the generator $e$ of the summand $U$ of $T_\En$ gives $q\,(\alpha\cdot e) = -q\in\bZ$, so $q\in\bZ$. Therefore
$$L_{K3}^{I_\Co = 1} = S_\En\oplus\bZ\alpha,$$
and the $(-1)$-eigenspace is $T_\Co$ by the same computation with the sign reversed.

*The type.* The summands $S_\En\cong U(2)\oplus E_8(2)$ and $\bZ\alpha\cong\langle-2\rangle$ are orthogonal, so the invariant lattice is $U(2)\oplus E_8(2)\oplus\langle-2\rangle$, of signature $(1,\ 1+8+1) = (1,10)$ (summing to the rank $11$), determinant $(-2)\det S_\En = 2048$ and discriminant group $(\bZ/2)^{11}$: the even $2$-elementary lattice $I_{1,10}(2)$. The invariant lattice and $T_\Co$ are mutually orthogonal complements in $\lkt$ of ranks $11+11 = 22$, and $S_\Co\oplus T_\Co$ has index $2^{11}$ there.

*The root is a choice, and what is computed is not uniqueness.* The twist above uses the displayed root $\alpha=e-f$ of $T_\En$, a choice made by the construction itself, not a computation about the lattice: $T_\En = U\oplus U(2)\oplus E_8(2)$ has many further vectors of square $-2$ — for example $\beta = (e+f)+v$ with $v^2 = -4$ in the $E_8(2)$ summand, $240$ of which exist (`computations/reports/ten_roots_twist.py`) — so not every such vector lies in $U$, because of the compensation between summands the example exhibits: $2ab = 2$ in $U$ balances $v^2 = -4$. The swap $e\leftrightarrow f$ and the sign act on the chosen root, and @cons:reflection-twist is lattice data on that chosen root. Whether the twist pair built from another root is conjugate to this one by an isometry of $\lkt$ is open; and the identification of the construction's own involutions with this twist is the same open problem as at @rmk:a21-open. The type of @prop:coble-transcendental and the eigenspace computation above depend only on the chosen root.

That the abstract type agrees with the period theory of [@DK13] is a check on the computation; it does not show that every family of direct Coble data realizes the same labeled embedding in $L_{K3}$, which is the labeled rigidity question of @sec-surface-divisors.


:::

### The local geometric meaning of the root {#sec-root-geometry}

Let $\wX\too X^\sharp$ be the minimal resolution of the $A_1$-point, and let $E\subset\wX$ be the exceptional $(-2)$-curve.
In the explicit local model, the lift of $\iota_{\Co}$ fixes $E$ pointwise, while the lift of $\iota_{\mathrm{dP}}$ acts nontrivially on $E$ with two fixed points.
The cohomology class $[E]$ is the geometric realization of $\alpha$ after a choice of marking.

The involution $I_{\Co}$ is therefore the expected cohomological involution on the resolved cover.
Turning this expectation into a global statement in families requires a simultaneous resolution and a rigidity theorem; see @sec-labeled-lattice-data.

### Labeled lattice data {#sec-labeled-lattice-data}

The abstract isomorphism type of $T_{\Co}$ does not determine the geometric moduli problem.
The relevant datum is a labeled tuple

\[
\mathfrak L_{\Co,2}
 =\bigl(
 L_{K3},
 I_{\Co},
 I_{\mathrm{dP}},
 H,
 \alpha,
 \mcc
 \bigr),
\]

where

- $I_{\Co}$ and $I_{\mathrm{dP}}$ are commuting nonsymplectic involutions;

- $H^2=4$ is fixed by both involutions;

- $\alpha^2=-2$, $H\cdot\alpha=0$, and $\alpha$ is fixed by $I_{\Co}$;

- $\mcc$ is the chosen positive/nef chamber in which $\alpha$ is effective and $H$ is nef and big;

- the product $I_{\Co}I_{\mathrm{dP}}$ has the required symplectic character.

**The geometric reading and a weaker lattice reading.** The five conditions are geometric: $I_{\Co}$ and $I_{\mathrm{dP}}$ are involutions of the K3 cover, $H$ and $\alpha$ are classes on it, and $\mcc$ is a chamber in $H$'s cone. Nothing in them is a statement about a lattice alone. A *weaker* reading asks only for lattice data: an involution of $L_{K3}$ with invariant lattice $\sdp = U(2)$, containing $H$, commuting with $I_{\mathrm{dP}}$'s counterpart $I_{\Co}$. The results below belong to that weaker reading: @prop:del-pezzo-placement says which placements of $\sdp$ the weaker conditions leave open, and @cor:no-del-pezzo-involution-coble-cover excludes one of them as the action of an automorphism in the marking of the construction. Neither is a statement about the tuple, and neither closes it.

**No condition relates $I_{\mathrm{dP}}$ to $\alpha$.** Of the five bullets, three mention $I_{\mathrm{dP}}$ (the first, second and fifth) and two mention $\alpha$ (the third and fourth); none mentions both, so no condition relates $I_{\mathrm{dP}}$ to $\alpha$. The condition on $\alpha$ is that $I_{\Co}$ fix it, and the chamber condition is on the class $H$.

**On the fourth and fifth bullets.** The fourth is a definition of the chosen chamber, not an assertion that $H$ is nef and big on any particular surface: $H$ is nef and big in $\mcc$ exactly when the downstairs class $h_\Co$ is nef, bigness of $H$ then being automatic from $H^2=4>0$ (@prop:nef-big-finite-cover), and no cited source proves that $h_\Co$ is nef. The fifth is a consequence rather than independent data once the first bullet's commutation is granted: for commuting involutions the product is an involution, and it acts on the one-dimensional $H^{2,0}$ by $(-1)(-1) = +1$ (@prop:product-of-involutions).

::: {.problem #prob:coble-rigidity title="Required theorem (labeled Coble rigidity)"}
Any two tuples $\mathfrak L_{\Co,2}$ arising from the direct projective construction are conjugate by an element of $O(L_{K3})$ preserving the labels, the degree-$4$ class, the effective root, and the chosen chamber.
:::

This is stronger than uniqueness of a primitive embedding of $S_{\Co}$ into $L_{K3}$.
It is the Coble analogue of the AEGS embedding-rigidity lemma and is needed before any direct period quotient can be declared coordinate independent.

**What the construction's involutions give.** The construction's own involutions are local and explicit: on $X^\sharp = \set{z^2 = f(x,y)}$ at the $\tau$-fixed point, $\iota_{\mathrm{dP}}(x,y,z) = (x,y,-z)$ and $\iota_\Co(x,y,z) = (-x,-y,-z)$. They commute; with $\omega = \frac{dx\wedge dy}{2z}$ one has $\iota_{\mathrm{dP}}^*\omega = -\omega$ and $\iota_\Co^*\omega = -\omega$ while the product scales $\omega$ by $+1$, so both are nonsymplectic and the product is symplectic, as the bullets require. $\mathrm{Fix}(\iota_{\mathrm{dP}})$ is the branch curve, nodal at $p$; $\mathrm{Fix}(\iota_\Co)$ is carried by the singular $\tau$-fixed points, since $\iota_\Co(x,y,z) = (x,y,z)$ forces $x = y = z = 0$ and $f(0,0) = 0$, and $f$ being $\tau$-invariant vanishes there to even order — so $\iota_\Co$ has no isolated fixed point, which its nonsymplecticity demands (@prop:local-operators).

On the resolution, $\widehat\iota_\Co$ acts trivially on the exceptional $\PP^2$ and fixes the exceptional curve $D_g$ pointwise, while $\widehat\iota_{\mathrm{dP}}$ acts by $[X:Y:Z]\mapsto[X:Y:-Z]$ and fixes on $D_g$ exactly the two points $[1:\pm i:0]$, which are also the two points where the proper transform of the branch curve meets it. So $\mathrm{Fix}(\widehat\iota_{\mathrm{dP}})$ is the normalization of the branch curve, of Euler characteristic $2k-16$ for $k$ nodes, and Lefschetz gives invariant rank $2+k$ (@prop:del-pezzo-type-on-the-resolution). The invariant lattice contains $\pi^*\Pic(\PP^1\times\PP^1)\perp\ZZ D_1\perp\cdots\perp\ZZ D_k = U(2)\perp\langle-2\rangle^{\oplus k}$; equality is a saturation question and is not settled here.

Two consequences follow. First, the del Pezzo type $U(2)$ occurs only for $k = 0$, where $\mathrm{Fix}(I_\Co)$ is empty and the quotient is Enriques rather than Coble: every Coble member has $k\ge1$ and invariant rank at least $3$. Second, the root $\alpha$ is one of the exceptional curves $D_g$ — effective, of square $-2$, $I_\Co$-invariant, of degree $0$ against $H$ — and it is preserved by $\widehat\iota_{\mathrm{dP}}$, so the slot *fixes* the root instead of reversing it and the effectivity argument that forbids a reversal has nothing to forbid (@rmk:a21-open).

**The tuple is not empty.** All five bullets hold on it: $H = \pi^*\OO_{\PP^1\times\PP^1}(1,1)$ is fixed by both involutions and is nef and big with $H^2 = 4$ because $\OO(1,1)$ is very ample, $H\cdot D_g = 0$ and $\alpha = [D_g]$ is the class of an effective curve, the two involutions are nonsymplectic with symplectic product, and the invariant ranks are $k+2$ and $k+10$ by Lefschetz (@prop:tuple-of-the-construction). So what is open here is the rigidity statement of @prob:coble-rigidity, not the existence of a tuple; an empty labelled set is not an available answer, and the effectivity argument that closes the $U(2)$ slots has no purchase on this one.

**The one-node comparison: the labels are conjugate; the chamber is a separate condition.** The one-nodal invariant locus is a nonempty Zariski-open of the hyperplane $\{f(p)=0\}$ in the invariant system — the explicit polynomial of @sec-explicit-curve makes it nonempty, and the openness is the point — so it is connected (@prop:one-node-connected). The construction is a smooth proper equivariant family over it carrying the relative polarization $\pi^*\OO(1,1)$ and the exceptional divisor, and parallel transport along a path is an isometry of $H^2$ carrying the two invariant lattices, $H$ and $\alpha$ of one member to those of the other. So for any two one-node members there is $\gamma\in\Orth(\lkt)$ conjugating the involutions, the degree-$4$ class and the effective root (@thm:a21-labels). That is three of the four clauses of @prob:coble-rigidity, for every pair on the locus. The chamber clause is separate: the root is the only effective class of square $-2$ orthogonal to $H$ (@lem:face-at-H), so the labels pin a chamber of the arrangement cut by a member's own effective roots, and the transported chamber coincides with the target's chamber exactly when no extra effective root cuts it (@prop:chamber-conditional) — a condition on the effective cones, hence on the period, and not a statement about the local system. So what remains of @prob:coble-rigidity on the one-node locus is exactly that condition: agreement of the effective roots across the locus.

**The node count, separately.** Away from the one-node locus the invariant rank of $I_{\mathrm{dP}}$ is $k+2$, and a conjugation preserving the labels preserves it, so a one-node and a two-node member are not conjugate (@prop:node-count-invariant). The one-node question does not use this statement.

What that leaves. The negative statements proved in the Coble chapter — @prop:no-rank-one-automorphism and @prop:rank-two-slot-boundary — are about a slot whose invariant lattice is $U(2)$ and whose fixed lattice in $S_\Co$ is $\ZZ H$ or all of $S_\Co$. They do not describe the tuple of this construction, whose invariant rank is $2+k\ge3$ and which meets $S_\Co$ in rank $2+k=\rk S_{\mathrm{dP}}$, the two lattices both containing $\pi^*\Pic(\PP^1\times\PP^1)\perp\bigoplus\ZZ D_g$.

**Labeled rigidity on the one-node locus.** The computations cited below are in `computations/reports/` and `formalization/coble-enriques/A21Arithmetic.lean`.
1. *The one-node locus is a nonempty open, path-connected subset of the hyperplane $\{f(p)=0\}$ in the invariant system*: nonempty by the polynomial of @sec-explicit-curve, open because escape-to-$p$ is excluded by a uniform inverse-function theorem on the Hessian (@lem:node-condition nondegeneracy preserved on the family), connected because for two members $f_0,f_1$ the pencil $\ell = \langle f_0,f_1\rangle$ is a pencil without fixed component (a member $f = gh$ of $B$ would satisfy $C_g \cap C_h = \{p\}$, against the even positive global intersection number $(a,b)\cdot(4-a,4-b)$ — local multiplicity $1$ at $p$ — so no factor share exists, after which Bertini for pencils on a smooth surface applies), the bad members of $\ell$ are closed and finitely many, and the locus is path-connected (@prop:one-node-connected). So the labels of any two members are conjugate (@thm:a21-labels): $S_\Co$, $S_{\mathrm{dP}}$, $H$, $\alpha$.
2. *Every one-node member has* $\rk \Pic \ge 11$: the nonsymplectic $I_\Co$ has anti-invariant $H^{2,0}\oplus H^{0,2}$, so $S_\Co\subseteq H^{1,1}(\widetilde X_b)\cap H^2(\widetilde X_b,\ZZ) = \Pic(\widetilde X_b)$, of rank $11$ (@sec-labeled-lattice-data). What the rulings give is instead: the flat lattice $\Lambda = \langle e_b, f_b, [D_b]\rangle$ lies in $S_{\mathrm{dP}}$, since its classes are invariant under the deck involution (classes of the ruling fibrations' fibres) and the exceptional curve's class, and it lies in $S_\Co$ as well, since $\tau$ preserves each ruling fibration fibrewise. $\Lambda\cong U(2)\perp\langle-2\rangle$, det $8$; $\rk S_{\mathrm{dP}} = 3 = \rk\Lambda$ (Lefschetz, ranks only), so the index is $1$ or $2$ — det candidates $\set{8,2}$ — and the saturation of $\Lambda$ in $S_{\mathrm{dP}}$ is *open*. Whether $S_{\mathrm{dP}}\subseteq S_\Co$ as sublattices is likewise open: ruling-class invariance gives $\Lambda\subseteq S_\Co$, not the invariant lattice's.
3. *The image of the period map has dimension $9$, and its differential has generic rank $9$.* The one-node family is algebraic (it is the universal family over the one-node locus $B$, a nonempty Zariski-open subset of the hyperplane $|\{f(p)=0\}|\cong\PP^{11}$, with the relative polarization and the node section, by @prop:one-node-family), so its period map $p\colon B \to D(T_\Co)/\Gamma$ exists as a holomorphic map into the period domain's quotient by the arithmetic group (an orbifold of complex dimension $9$, which for dimensional statements may be lifted locally to $D(T_\Co)$), and it is algebraic on $B$ by Borel's extension theorem [@Bor72]: a holomorphic map from a smooth quasi-projective variety, which $B$ is, to the quotient of a hermitian symmetric domain by an arithmetic group, that lifts locally to the domain — which the period map does with the local system trivialised — is algebraic. Its fibres are exactly the $\Aut(Y)^\tau$-orbits of members. Because the four labels are flat in the family, monodromy lands in their stabiliser in $\Orth(L_{K3})$; its image in $\Orth(T_\Co)$ is the *label-stabiliser group* (image of $Z_{\Orth(L_{K3})}(I_\Co,I_{\mathrm{dP}})_{H,\alpha}$ in $\Orth(T_\Co)$), and the marked periods descend well-definedly to $D(T_\Co)$ modulo that subgroup; equality there means *some* element of the label-stabiliser group carries one period to the other, and that element fixes the labels, in particular the flat ample class $2H-\alpha$, ample on every member by the same Nakai--Moishezon argument used in the positive half, so strong Torelli (BHPV VIII.11.1) gives isomorphic $H$-polarized pairs, and $\varphi_H$'s Segre recovery of $(Y,B)$ ($h^0(H) = 4$, $\pi_*\OO_X = \OO_Y\oplus K_Y$) gives the same member; an automorphism of $Y$ preserving $(Y,B)$ conversely gives equal periods mod that subgroup. The label-stabiliser group is not identified with the direct labeled centralizer group $\Gamma_{\Co,2}^{\mathrm{dir}}$ of @def:direct-group, which centralises the datum with the chamber $\mcc$ as well, or with the geometric monodromy of @def:geometric-monodromy; that identification is @prob:group-identification, which is open. This item uses the label-stabiliser group alone. On the dense open subset of $B$ where the $\Aut^0(Y)^\tau$-stabiliser is **finite** (its complement is one proper closed subset: for the action of the algebraic torus $\Aut^0(Y)^\tau$ on $B$ the function $b\mapsto\dim\stab(b)$ is upper semi-continuous by the source-semicontinuity of fibre dimensions, EGA IV(13.1.3), so $\{b:\dim\stab(b)\ge1\}$ is closed; it is proper because the member of @sec-explicit-curve has finite stabiliser; and *finite* means dimension $0$, an orbit of dimension $2-0 = 2$), each fibre is a $2$-dimensional orbit (with the ruling swap accounting for the $\mathbb Z/2$ component of the stabiliser). By the generic fibre-dimension and generic-rank theorems (Stacks tag 02FZ and its standard corollaries; EGA IV(13.1)), the image of $p$ has dimension $\dim B - 2 = 11 - 2 = 9$ at its generic point: since the target has dimension $9$, the image contains a nonempty Zariski-open subset of $D(T_\Co)/\Gamma$, and the differential of $p$ has generic rank $9$ at a dense set of members. The pointwise inequality "dimension of a fibre at $b$ ≥ $11 - \rank_b(dp)$" fails in general (the map $(u,v)\mapsto(u^2,uv)$ at the origin is a counterexample) and is not used: the Baire/Noether–Lefschetz step that follows uses only that the image of $p$ is Zariski-dense (contains a Zariski-open subset of the target), with each Noether–Lefschetz locus of a nonzero $\delta\in T_\Co$ the zero locus of a manifestly nonzero linear holomorphic function on the target's period domain, whose pullback to $B$ is then proper analytic. Consequently $\Pic = S_\Co$ for a very general member (proper analytic NL loci over that generic image; Baire).
4. *The chamber clause of @prob:coble-rigidity is false* when the fourth bullet is read as a chamber of the arrangement cut by the member's own effective roots. The statement is pair-specific:
(a) *The census pair $b_0, b_\star$.* For two members $b_0,b_\star$ (membership computed in `computations/reports/sm00_audit-witnesses-run.txt`), $\nu(b) = \#\{\delta:\delta^2=-2,\ \delta\cdot H_b = 1\}$ has the values $0$ and $4$ (`sm00_chamber-negative-half.md` with its scripts and logs). In each reading where the chamber's span is its own ambient space — the nef reading (span $= \mathrm{NS}_\bR$), the ample reading (span $= \mathrm{NS}_\bR$), the Kähler reading ($c = \mathcal K$ open in $H^{1,1}(X,\bR)$ of signature $(1,19)$, whence span $= W$ and $\operatorname{Pic} = W\cap L$), and the positivity reading — equality of chambers forces an isomorphism of the Picard lattices *by the span argument alone*; no Pic-recovery hypothesis enters. In the positive-region reading of the fourth bullet — chambers in the positive region $\{x^2>0\}$ of $H^2(X,\bR)$ (where $\{x^2=1\}$ is not hyperbolic space and the Kähler cone is not a subspace-version of the chamber at all) — the ambient-free facet construction (`sm00_chamber-negative-half.md`: the facet of $\overline{\mathfrak c_{b_\star}}$ at $C_+$, with a Grauert-free wall-free ball computed from an integral class, and the census argument) applies directly: the facet-normal $|H\cdot|$-census differs exactly, $0$ against $\ge 2$ at degree $1$, so no label-preserving isometry carries one chamber to the other. The Kähler cone itself is $\mathcal K_X = \operatorname{int}\operatorname{Nef}(X) \subset H^{1,1}(X,\bR)$, whose trace in $\operatorname{Pic}(X)\otimes\bR$ is the **ample** cone — never a Kähler cone in $\operatorname{Pic}\otimes\bR$.
(b) *The Pic-baseline pair (a very general member against $F'$).* By step 3 a member $b$ with $\Pic(X_b) = S_{\Co,b}$ exists; the member $F'$ (computed in `computations/reports/sm57_verify_special_member.py`) has an anti-invariant extremal $(-2)$-curve class $[C_1]$. Under every reading in which the span argument at (a) applies, chamber equality would force $\gamma(\operatorname{Pic}(X_b)) = \operatorname{Pic}(X_{F'})$, while label preservation gives $\gamma(S_{\Co,b}) = S_{\Co,F'}$; but $\operatorname{Pic}(X_b) = S_{\Co,b}$, so $\gamma(\operatorname{Pic}(X_b)) = \gamma(S_{\Co,b}) = S_{\Co,F'} \subsetneq \operatorname{Pic}(X_{F'})$, since $[C_1]\in\operatorname{Pic}(X_{F'})\setminus S_{\Co,F'}$: impossible. This argument is stated only for the readings in which the span argument applies; the census pair of (a) covers the positive-region reading. The failure is therefore dense on the locus beyond a single pair: the NL strata are dense under the open period image of step 3.
The universal statement that chamber equality forces an identification of the Picard lattices in the full $H^2$ reading is open; this item does not use it.
5. *Alternative semantics:* under the label-own reading of the fourth bullet — walls only from the labels' own lattice — the clause closes by @lem:face-at-H, and the chamber clause holds: the only wall through $H$ is $\alpha^\perp$, two chambers have $H$ in their closure, one is $\alpha$-positive. The two readings give opposite answers, so the statement of @prob:coble-rigidity has to fix the reading.
6. *The arithmetic of the tuple.* The determinants, the evenness of each lattice (from the diagonal Gram entries), the $H$-degree condition inside $U(2)\perp\langle-2\rangle$ and the twist root are computed in `formalization/coble-enriques/A21Arithmetic.lean` and `computations/reports/sm57_matrices_gen.txt`. The gluing indices $2^{10}$ and $2^{11}$ follow from the determinants and primitivity.
7. *Open points.* The twist identification (item 8) is open: the literal slot is refuted there under one reading (8(a)), the second involution is unresolved (8(b)), and lattice-level conjugacy of the reflected pair is proved (8(d)(1)). The saturation of $\Lambda$ in $S_{\mathrm{dP}}$ is proved by @prop:det-saturation-del-pezzo for $k = 1$, with one ordinary node at a $\tau$-fixed point and the branch curve irreducible; the same argument gives $U(2)$ for $k = 0$. For $k\ge2$ the saturation is open: the half-class criterion changes shape (`computations/reports/smtw_os_fibre-m6.md`). The open points are: the reading of the fourth bullet (item 5); the identification of Picard lattices from chamber equality (item 4); the second involution (item 8(b)); and the $k\ge2$ saturation, which the one-node question does not need.

8. *The twist identification (@prob:twist-identification).* @cons:reflection-twist defines one involution, $I_\Co:=w_\alpha I_{\mathrm{En}}$; it does not define a second involution of a pair, and the geometric $I_{\mathrm{dP}}$ part of the labeled construction (its action on the exceptional curve, @sec-root-geometry) requires a global rigidity theorem that is open. Four statements follow.
(a) *Conditional obstructions.* If "the twist pair" is taken to be $\langle I_\Co^{\mathrm{tw}}, I_{\mathrm{En}}\rangle$, conjugacy fails by a conjugacy invariant of pairs: the joint $(\mathbb Z/2\times\mathbb Z/2)$ character multiplicities are $(10,1,0,11)$ model-side against $(3,8,0,11)$ construction-side, and the product's anti-invariant lattice has rank $1$ against $8$ (computed in `computations/reports/smtw_ot_neg-m2.md`). This conclusion depends on that reading; it does not supply the missing second involution.
(b) *The second involution.* @cons:reflection-twist and its cited sources supply no second involution completing $I_\Co$ to a pair congruent to the construction's pair. That datum is open; the rank computation of (a) does not determine it.
(c) *The reflected-pair candidate is a separate, lattice-consistent fact.* The twist applied to both AEGS involutions, $(J_\Co,J_{\mathrm{dP}})=(w_\alpha I_{\mathrm{En}},w_\alpha I_{\mathrm{dP}})$, has eigenspace ranks $(11,3)$, joint invariant lattice $\Lambda=U(2)\perp\langle-2\rangle$ and symplectic product of rank $14$ — the four numbers of the construction's pair — and all single-lattice types match: $S_{\mathrm{dP},b}=\Lambda$ is proved in @prop:det-saturation-del-pezzo, whose only computational input is the census of the two even half-classes, computed in `computations/reports/sdp_discriminant_referee-run.txt`; and $S_{\mathrm{Co},b}$ has the twist's type $U(2)\perp E_8(-2)\perp\langle-2\rangle$ ($a=11$, $\delta=1$) by Nikulin's classification for the fixed locus $D_b$ (Theorem 3.1 of `computations/reports/smtw_ot_types-m8.md`). Abstract type does not decide the labelled embedding and gluing; (d)(1) treats them. This item does not close @prob:twist-identification.  The auxiliary binary that @rmk:a21-open records as open at $k=0$ is decided by the same primitivity argument: $S_{\mathrm{dP}}\cong U(2)$ at $k=0$, not the unimodular overlattice $U$.
(d) *Nikulin's primitive embeddings, and what the labelled statement needs in addition.* By [@Nik80, Prop. 1.15.1], the primitive embeddings of an even lattice $S$ into an even lattice with invariants $(m_{(+)},m_{(-)},q)$ are determined by data $(H_S,H_q,\gamma;K,\gamma_K)$: subgroups $H_S\subseteq A_S$ and $H_q\subseteq A_q$, an isomorphism $\gamma\colon q_S|_{H_S}\to q|_{H_q}$ of the restricted forms, an even lattice $K$ (the orthogonal complement of $S$), and an isomorphism of forms $\gamma_K$; the proposition also states when two such data give isomorphic embeddings, in terms of $O(q)$ and $\operatorname{Isom}(K,K')$. So the *lattice blocks* of this comparison can be handled block by block at discriminant-form level. For the blocks in question: the types $U(2)\perp E_8(-2)\perp\langle-2\rangle$ and $\langle2\rangle\perp U(2)\perp E_8(-2)$ are common to both sides (computed in `computations/reports/smtw_ot_types-m8.md` and `coble_aegs_involutions-run.txt`); the discriminant forms of the $T_\Co$ family are anti-isometric (computed in `coble_gluing_discriminants.py`); and each piece of the joint-eigenspace decomposition of the reflected pair is isometric to the corresponding piece of the construction's pair (computed in `coble_reflected_pair-run.txt`). *What the block-wise machinery does not establish.* A conjugacy of **operators** of the comparison — a statement about two *involutions of $L_{K3}$*, their invariant lattices, and the placed classes $(H,\alpha)$ — is stronger than every identified primitive embedding of one lattice block into the same ambient unimodular lattice, and the double-coset enumeration of block embeddings does not give it: it asks that *one* isometry of $L_{K3}$ carry not only each eigenlattice but also the pair of commuting involutions defined by the sign-changes across those eigenlattices, and the placed classes, neither of which is part of any block-embedding problem. The equality of types, joint decompositions and gluing anti-isometries of the eigenlattice blocks on the two sides is the piecewise basis of that step. In particular: (1) the extension of a piecewise isometry to an integral isometry conjugating the pair $(w_\alpha I_{\mathrm{En}}, w_\alpha I_{\mathrm{dP}})$ with the construction's pair $(I_{\Co,b}, I_{\mathrm{dP},b})$, at the operator level and carrying the placed classes $(H,\alpha)$, holds at lattice level for every irreducible one-nodal member $b$ (proof in `computations/reports/smwg_operator-extension.md`). The gluing of the joint pieces is a full graph, and one lift from Nikulin's surjectivity theorem for even indefinite $2$-elementary lattices [@Nik80, Theorem 3.6.3], applied to the rank-$11$ block only, matches any two gluings, so the double coset collapses. The construction side's $(+-)$-piece is $E_8(-2)$ because it is the coinvariant lattice of the product involution, which is symplectic, whose action on $H^2$ of a K3 is unique up to isometry (Nikulin [Ni1] Thm. 4.7 via van Geemen–Sarti §§1.1–1.3); this excludes the $\langle-2\rangle^{\oplus 8}$ alternative for the complement. The corner classes come from the construction ($H_b = \pi^*\OO_Y(1,1) = e_b+f_b$ of the $U(2)$ ruling frame, $\alpha_b = [D_b]$, index one from @prop:det-saturation-del-pezzo), the marked orbit of such corner pairs is transitive, and the integral isometry of the rank-$3$ piece is realized through the flag by the graph-compatibility equation $\bar\psi\gamma = \gamma(\bar\varphi\oplus\mathrm{id})$. The conclusion is $g\in\Orth(\lkt)$ conjugating the pairs with $g(H)=H_b$, $g(\alpha)=\alpha_b$, for every $b$ directly, with no transport step. It is a lattice statement, not a Hodge-isometry or chamber statement. An unlabelled discriminant surjectivity alone does not give it; the marked orbit and stabilizer and the gluing compatibility supply the rest. (2) @cons:reflection-twist defines no second involution, and (1) does not define one. (3) Any conclusion about the tuple's chamber (item 4) is independent of the gluing argument of (1): lattice-level conjugacy does not imply the chamber clause, $(Lat)\nRightarrow(Chm)$; under the positive-region reading the chamber conclusion awaits the period and Torelli input of item 4. The open part of the twist identification is the second involution of (b); (1) holds at lattice level; (2) and (3) are not answered in this section.
### The embedded comparison chain {#sec-embedded-chain}

The Heegner strategy uses the chain

\[
T_{\Co}
  =\alpha^\perp_{T_{\mathrm{En}}}
  \embeds T_{\mathrm{En}}
  \embeds T_{\mathrm{dP}}
  \embeds L_{K3}.
\]

The autonomous strategy begins with the leftmost lattice as the anti-invariant lattice of $I_{\Co}$ and must later construct and identify the two larger lattices.
The comparison theorem must show that the two chains are conjugate as **labeled embedded chains**, not merely termwise isometric.

## The resolved surface, the quasipolarization, and the stable divisor {#sec-surface-divisors}

### The resolved quotient diagram {#sec-resolved-diagram}

Let $\psi:\wX\too\wV$ be the quotient of the resolved K3 cover by $\iota_{\Co}$.
Let $E\subset\wX$ be the fixed exceptional curve and let $C:=\psi(E)\subset\wV$.

Then $\psi^*C=2E$.

Let $H=\pi^*\mathcal O_Y(1,1)$ on $\wX$.
The class $H$ satisfies $H^2=4$ and $H\cdot E=0$.

With the natural descent linearization, there is a class $L\in\Pic(\wV)$ such that $\psi^*L=H$.

::: {.proposition #prop:quasipolarization title="degree-$2$ quasipolarization"}
The class $L$ satisfies $L^2=2$ and $L\cdot C=0$.

Hence $L$ is not ample on $\wV$.
On a general one-node member it is nef and big and its only null curve is $C$.
After contracting the full $L$-null configuration, its descent is ample.
:::

::: {.proof}

Against the fixed curve: $\psi^*L=H$ and $\psi^*C=2E$, so $2\,L\cdot C=\psi^*L\cdot\psi^*C=H\cdot(2E)=2\,H\cdot E=0$, whence $L\cdot C=0$; and $H^2 = (\psi^*L)^2 = \deg\psi\cdot L^2 = 2\,L^2$ (pullback by a finite morphism of degree $\deg\psi$ scales squares by $\deg\psi$, and here $H^2 = 4$), so $L^2 = H^2/\deg\psi = 2$, using that $\psi$ has degree $2$, being the quotient by the involution $\iota_{\Co}$.

Not ample: an ample class meets every curve positively, and $L\cdot C=0$ with $C$ a curve.

Nef and big on a general one-node member: nef means $L\cdot D\geq0$ for every curve $D$, which holds because $L$ is pulled back from a polarization by the construction of $H=\pi^*\OO_Y(1,1)$ and $H^2=4>0$ makes it big.
That $C$ is the only null curve is the content of the one-node computation and is where the hypothesis "general" is spent: the null curves of $L$ are the curves contracted by the linear system, and on the general member those are exactly the fibres over the node.

Ampleness after contraction: a nef and big class whose null curves are all contracted is ample on the contraction, by the Nakai--Moishezon criterion applied to the pullback.
:::

The final sentence must be interpreted with care on intersections with other Heegner divisors: additional curves can become $L$-trivial.

### The anti-bicanonical curve {#sec-anti-bicanonical}

Riemann--Hurwitz for the double cover $\psi$ gives

\[
K_{\wX}
 =\psi^*\left(K_{\wV}+\frac12C\right).
\]

Since $K_{\wX}\sim0$ and $\wV$ is rational, $C\sim-2K_{\wV}$.

Moreover, $2C^2=(2E)^2=-8$ and $C^2=-4$.

::: {.proposition #prop:antibicanonical-system title="anti-bicanonical system on the one-node locus"}
For the resolved one-node Coble surface,

\[
|-K_{\wV}|=\varnothing,
\qquad
|-2K_{\wV}|=\{C\}.
\]
:::

::: {.proof}
If $D\in|-2K_{\wV}|$, then $\psi^*D\in|2E|$.
Since $E^2=-2$, every effective divisor linearly equivalent to $2E$ contains $E$; iterating gives $|2E|=\{2E\}$.
Thus $D=C$.
If $D\in|-K_{\wV}|$, then $\psi^*D\in|E|=\{E\}$.
The pullback of a divisor from the quotient has even multiplicity along a branch component, so this is impossible.

If the invariant branch curve has ordinary nodes at $k$ distinct fixed points, the same argument gives $|-2K_{\wV}| =\{C_1+\cdots+C_k\}$, where the $C_i$ are disjoint rational $(-4)$-curves.
Thus $n=1$ on the generic Heegner divisor but not on its higher-codimension multiple-node loci.
:::

### The del Pezzo ramification divisor {#sec-ramification-divisor}

Let $\wR\subset\wX$ be the strict transform of the fixed curve of $\iota_{\mathrm{dP}}$.
At the node, the total ramification divisor contains the exceptional curve with multiplicity one, and $\wR+E\sim2H$.

Let $R_{\wV}$ be the quotient divisor on $\wV$.
Then $\psi^*R_{\wV}=\wR$.

::: {.proposition #prop:ramification-numerics title="ramification class and numerical invariants"}
One has

\[
R_{\wV}\sim2L+K_{\wV},
\]

and

\[
R_{\wV}^2=7,
\qquad
R_{\wV}\cdot C=2,
\qquad
K_{\wV}\cdot R_{\wV}=-1,
\qquad
p_a(R_{\wV})=4.
\]
:::

::: {.proof}
Pulling back $2L+K_{\wV}$ gives $2H-E=\wR$, and $R_{\wV}=\psi_*\wR$ is the divisor on $\wV$ whose pullback is that class.

For the self-intersection, $H=\pi^*\OO_Y(1,1)$ and $H\cdot E=0$ because $E$ is the exceptional curve of the minimal resolution of the $A_1$ point, hence contracts to a point of $Y$, so $\pi_*E=0$ and $H\cdot E=\OO_Y(1,1)\cdot\pi_*E=0$.
So
$$
\wR^2=(2H-E)^2=4H^2-4\,H\cdot E+E^2=4\cdot4-0+E^2 .
$$
And $E^2=-2$ because $E$ is the exceptional curve of a minimal resolution of a node, so the calculation is $\wR^2=16-0-2=14$.
Then $R_{\wV}^2=\wR^2/\deg\psi=14/2=7$, because $\psi$ is $2$-to-$1$ and self-intersections of divisors pulled back along a finite map of degree $d$ scale by $d$.

For the remaining numbers: $C=\psi(E)$ has pullback $2E$, so $C^2=(2E)^2/2=4\cdot(-2)/2=-4$, consistent with $C=-2K_{\wV}$; and $R_{\wV}\cdot C=\wR\cdot\psi^*C/2=\wR\cdot2E/2=(2H-E)\cdot E=-E^2=2$.
Adjunction on $C\cong\PP^1$ then gives $K_{\wV}\cdot C=-2-C^2=-2+4=2$, consistent with $C=-2K_{\wV}$; and since $C=-2K_{\wV}$ the canonical class against $R_{\wV}$ is
$$
K_{\wV}\cdot R_{\wV}=-\tfrac12\,C\cdot R_{\wV}=-\tfrac12\cdot2=-1 .
$$
Adjunction for $R_{\wV}$ gives
$$
2p_a(R_{\wV})-2=R_{\wV}^2+K_{\wV}\cdot R_{\wV}=7-1=6,
\qquad\text{so } p_a(R_{\wV})=4,
$$
an integer, as the consistency check requires.

The divisor $R_{\wV}$ is not the anti-bicanonical curve $C$.
It is the divisor relevant to the KSBA polarization.
:::

### Contraction to the singular Coble surface {#sec-canonical-contraction}

Let $\mu:\wV\too V^\sharp$ contract $C$.
The discrepancy formula is

\[
K_{\wV}
 =\mu^*K_{V^\sharp}-\frac12C.
\]

Consequently $K_{V^\sharp}\sim_{\bQ}0$.

Let $R^\sharp=\mu_*R_{\wV}$.
Then

\[
\mu^*R^\sharp
 =R_{\wV}+\frac12C
 =2L.
\]

It follows that $(R^\sharp)^2=8$.

Locally, $R^\sharp$ is the image of the union of the coordinate axes $(uv=0)$ in the quotient singularity $\frac{1}{4}(1,1)$.
Its local class is $2$ in $\operatorname{Cl}(\frac{1}{4}(1,1))\cong\bZ/4$, so it is $\bQ$-Cartier of index $2$.

::: {.definition #def:open-stable-coble-pair title="open stable Coble pair"}
An open degree-$2$ stable Coble pair is

\[
(V^\sharp,\epsilon R^\sharp),
\qquad
0<\epsilon\ll1,
\]

where $V^\sharp$ is the singular canonical contraction and $R^\sharp$ is the divisorial ramification of the descended del Pezzo involution.
:::

The log-crepant pullback is

\[
\mu^*(K_{V^\sharp}+\epsilon R^\sharp)
 =K_{\wV}
  +\frac{1+\epsilon}{2}C
  +\epsilon R_{\wV}.
\]

For a general member, $C+R_{\wV}$ is simple normal crossing and the coefficients are less than one when $0<\epsilon<1$.
Thus the resolved pair is klt, and so is the singular pair.
If the descent of $L$ is ample, then $K_{V^\sharp}+\epsilon R^\sharp$ is ample.

::: {.warning #warn:index-one-cover title="index-one cover"}
The canonical index-one cover of the local surface singularity $\frac{1}{4}(1,1)$ is the $A_1$ singularity.
Pulling back further to $\bA^2$ is useful for local log calculations, but it is not the index-one cover.
:::

## Direct moduli functors, arithmetic groups, and period spaces {#sec-moduli-groups}

### The resolved-cover moduli problem {#sec-cover-moduli}

The autonomous strategy should begin with a stack of labeled K3-cover data.
The following definition is a mathematical specification; representability and equivalence with the singular pair moduli are required theorems.

::: {.definition #def:direct-cover-datum title="direct resolved Coble cover datum"}
Over a scheme $S$, a direct resolved degree-$2$ Coble cover datum consists of

\[
(\widetilde{\mcx}/S,
 \mce,
 \iota_{\Co},
 \iota_{\mathrm{dP}},
 \mch,
 \mcc)
\]

with the following properties.

1. $\widetilde{\mcx}/S$ is a family of K3 surfaces, or a family with the controlled ADE singularities allowed by the period problem.

2. $\mce$ is a relative Cartier divisor whose geometric fibers are smooth $(-2)$-curves.

3. $\iota_{\Co}$ is a nonsymplectic involution whose divisorial fixed locus is $\mce$.

4. $\iota_{\mathrm{dP}}$ is a commuting nonsymplectic involution whose divisorial fixed locus is the ramification divisor $\mcr$; this is a requirement on the tuples of the moduli problem, and the representative that the polarization $U(2)$ supplies on a classical Coble cover is not an automorphism but a lattice isometry (@cor:no-del-pezzo-involution-coble-cover), so the requirement is part of what the problem imposes and not a property read off those covers.

5. $\mch$ is a relatively nef and big line bundle with $\mch_s^2=4$ and $\mch_s\cdot\mce_s=0$.

6. $\mcc$ specifies the positive/nef chamber in which $\mce$ is effective and $\mch$ gives the desired contraction.

7. Fiberwise contraction of $\mce$ gives an $A_1$-surface on which the Coble involution descends and fixes the node.
:::

The chamber and the effective root are part of the data because an abstract lattice marking does not determine which root is represented by the exceptional curve or which degree-$4$ class gives the projective model.

### The singular-pair moduli problem {#sec-singular-moduli}

::: {.definition #def:direct-singular-datum title="direct singular Coble datum"}
Over $S$, a direct singular Coble datum consists of

\[
(\mcv^\sharp/S,
 \mcl^\sharp,
 \tau_{\mathrm{dP}},
 \mcr^\sharp)
\]

such that each geometric fiber has the following properties.

1. $V^\sharp$ is a normal rational surface with one $\frac{1}{4}(1,1)$ singularity.

2. $K_{V^\sharp}\sim_{\bQ}0$.

3. $L^\sharp$ is an ample degree-$2$ class.

4. $\tau_{\mathrm{dP}}$ is an involution whose divisorial fixed locus is $R^\sharp$.

5. $R^\sharp$ is ample, $\bQ$-Cartier, and $(R^\sharp)^2=8$.

6. The canonical index-one cover is a K3 surface with one $A_1$ singularity.
:::

::: {.problem #prob:cover-singular-equivalence title="Required theorem (equivalence of the two open moduli problems)"}
After accounting for the Weyl ambiguity of the exceptional root, contraction, canonical cover, and quotient define inverse equivalences between the direct resolved-cover stack and the direct singular-pair stack.
The equivalence is compatible with base change and automorphisms.
:::

### Four arithmetic groups that must not be conflated {#sec-four-groups}

Fix an embedded root $\alpha\in T_{\mathrm{En}}$ and put $T_{\Co}=\alpha^\perp$.
There are at least four natural groups.

::: {.definition #def:unpolarized-direct-group title="direct unpolarized Coble group"}
Dropping the degree-$4$ polarization and the del Pezzo involution from the labeled datum gives the candidate direct unpolarized group

\[
\Gamma_{\Co}^{\mathrm{dir}}
 :=\im\left(
 Z_{O(L_{K3})}(I_{\Co})_{\alpha,\mcc}
 \too O^+(T_{\Co})
 \right).
\]

The corresponding geometric monodromy group is defined from the direct unpolarized Coble moduli stack.
The expected equality $\Gamma_{\Co}^{\mathrm{dir}}=O^+(T_{\Co})$ is compatible with the full stabilizer lemma below, but it remains a geometric monodromy statement until the direct period theorem is proved.
:::

::: {.definition #def:hodge-group title="Hodge-theoretic Heegner group"}

\[
\Gamma_{\Co,2}^{\mathrm{Hdg}}
 :=\im\left(
   \Stab_{\Gamma_{\mathrm{En},2}}(\bZ\alpha)
   \too O^+(T_{\Co})
  \right).
\]
:::

This group is the natural group of a fixed normalized Heegner component once the Enriques construction has been fixed.

::: {.definition #def:direct-group title="direct labeled centralizer group"}

\[
\Gamma_{\Co,2}^{\mathrm{dir}}
 :=\im\left(
 Z_{O(L_{K3})}(I_{\Co},I_{\mathrm{dP}})_{H,\alpha,\mcc}
 \too O^+(T_{\Co})
 \right).
\]
:::

This is the arithmetic group naturally attached to the autonomous lattice datum, provided the labeled rigidity theorem holds.

::: {.definition #def:geometric-monodromy title="geometric monodromy group"}
$\Gamma_{\Co,2}^{\mathrm{geom}}$ is the image of the orbifold monodromy representation of the connected direct moduli stack of polarized Coble data on the local system $T_{\Co}$.
:::

Finally, the degree-$2$ marking gives an orthogonal decomposition $A_{T_{\mathrm{En}}} \cong A_{U(2)}\perp A_{E_8(2)}$, and hence the finite subgroup $P:=O(q_{U(2)})\cross O(q_{E_8(2)})$.

Using the characteristic class $\eta/2$ to identify the remaining finite quadratic space with the Enriques discriminant space, discriminant gluing suggests the congruence subgroup

\[
\Gamma_{\Co,2}^{\mathrm{cong}}
 :=\rho_{T_{\Co}}^{-1}(P).
\]

::: {.problem #prob:group-identification title="Required theorem (arithmetic and monodromy identification)"}
Prove

\[
\Gamma_{\Co,2}^{\mathrm{geom}}
 =\Gamma_{\Co,2}^{\mathrm{dir}}
 =\Gamma_{\Co,2}^{\mathrm{Hdg}}
 =\Gamma_{\Co,2}^{\mathrm{cong}}.
\]

Each equality requires a separate argument: global Torelli and parallel transport for the first, labeled embedding comparison for the second, and discriminant-form gluing for the third.
:::

**Consequence for the direct group.** The labelled tuple of @prob:coble-rigidity is open for the direct-projective construction (@rmk:a21-open), and what is settled there is that the lifted del Pezzo involution has invariant rank $2+k\ge3$ rather than $U(2)$ (@prop:del-pezzo-type-on-the-resolution). So the pair $(I_\Co,I_{\mathrm{dP}})$ whose centralizer defines $\Gamma^{\mathrm{dir}}_{\Co,2}$ is a pair of lattice involutions and of a local model rather than of two automorphisms of one Coble cover; the definition itself stands, being taken in $\Orth(L_{K3})$, and what a comparison with $\Gamma^{\mathrm{geom}}_{\Co,2}$ needs is precisely the missing geometric realisation. The comparisons with $\Gamma^{\mathrm{Hdg}}_{\Co,2}$ and with the congruence group are lattice statements about $\Orth(L_{K3})$ and are untouched by that.

Defining one of these groups to be “the group for which the desired semifan works” is circular.

::: {.remark title="What the four-group problem reduces to"}

Two of the four are explicitly built over the stable group $\Gamma_\Co = \Orth^+(T_\Co)^*$ and differ from it by a finite subgroup of $\Orth(A_{T_\Co}, q_{T_\Co})$.
$\Gamma^{\mathrm{Hdg}}_{\Co,2}$ is the group of @prop:gamma-co-in-heegner-group, the root $\alpha$ fixed above being the vector $\delta$ of @lem:coble-heegner-vector and $\Gamma_{\mathrm{En},2}$ being $\gent$: it contains $\Gamma_\Co$ as the kernel of its action on $A_{T_\Co}$, and its quotient has order exactly $\abs{W(E_8)}$ (@prop:gamma-cong-eq-heegner(2)); it is the group $P$ below if and only if the gluing $\gamma$ is block-compatible in the sense of that proposition.
$\Gamma^{\mathrm{cong}}_{\Co,2}$ is by definition the full preimage of a subgroup $P$ under $\rho_{T_\Co}$ — the $P$ defined above, made a subgroup of $\Orth(A_{T_\Co},q_{T_\Co})$ by the identity on $\ZZ\tfrac12\zeta$ — so its kernel is $\ker\rho_{T_\Co}$.
$P$ is nontrivial — it contains the swap of the two isotropic classes of $A_{U(2)}$ — and that swap is realised by an integral isometry of $T_\Co$, the reflection $s_{e'-f'}$ in a vector of square $-4$, which lies in $\Orth^+(T_\Co)$ and fixes the class $\eta/2$ (`computations/reports/coble_congruence_witness.py`, and @sec-gamma-co-comparison).
So the congruence group strictly contains the stable group, and so do the Heegner group, by @prop:gamma-co-heegner-strict, and the $\theta$-group, by @prop:theta-co-index, both with index exactly $\abs{W(E_8)} = 696\,729\,600$. Moreover, under block-compatibility of the gluing, $\Gamma^{\mathrm{Hdg}}_{\Co,2} = \Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)$: the two quotients are then both $P$, computed in @prop:gamma-cong-eq-heegner, which reduces the comparison of the Heegner group with the congruence group to that one statement about the gluing. The indices are unconditional: $[\Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co):\Gamma_\Co] = \abs{W(E_8)}$ and $[\Gamma^{\mathrm{cong}}_{\Co,2}:\Gamma_\Co] = 2\abs{W(E_8)} = 1\,393\,459\,200$. Of the four groups of @prob:group-identification what remains open is the comparison with the direct and geometric entries (@prob:coble-rigidity, @prob:B24, @prob:B25), and for the $\theta$-group the block-compatibility of $\gamma_\Co$.
The four-group identification therefore cannot be an identification with $\Gamma_\Co$: what it asserts is that four overgroups of $\Gamma_\Co$ coincide, which is a statement about subgroups of one finite quadratic space and nothing more.

The other two are not of that kind.
$\Gamma^{\mathrm{dir}}_{\Co,2}$ is the image of a centralizer in $\Orth(L_{K3})$ of the labeled Coble datum, and comparing it with $\Gamma^{\mathrm{Hdg}}_{\Co,2}$ needs an isometry of $L_{K3}$ carrying the Coble-labeled primitive embedding to the Enriques-labeled one and $\tilde h_\Co$ to $h$; that is @prob:coble-rigidity, which is exactly what @warn:isometry-rigidity warns cannot be replaced by an abstract lattice isometry.
$\Gamma^{\mathrm{geom}}_{\Co,2}$ is a monodromy group of a moduli stack, and no lattice computation reaches it: it needs the direct global Torelli and direct monodromy theorems, @prob:B24 and @prob:B25.
:::

### A lattice-theoretic stabilizer sequence {#sec-stabilizer-sequence}

There is a useful pure lattice calculation.
Let $L_0=\bZ\alpha\oplus T_{\Co}$.

The lattice $T_{\mathrm{En}}$ is an index-$2$ overlattice of $L_0$, obtained by adjoining $(\alpha+\eta)/2$.
The gluing subgroup in $A_{\bZ\alpha}\oplus A_{T_{\Co}}$ is generated by

\[
\left(\frac\alpha2,\frac\eta2\right).
\]

The class $\eta/2$ is the characteristic element of the discriminant form of $T_{\Co}\cong I_{2,9}(2)$ and is fixed by every isometry.

::: {.lemma #lem:full-stabilizer title="full orthogonal stabilizer"}
Restriction gives an exact sequence

\[
1\too\langle w_\alpha\rangle
\too
\Stab_{O^+(T_{\mathrm{En}})}(\bZ\alpha)
\too
O^+(T_{\Co})
\too1.
\]
:::

::: {.proof}

The exact sequence is the one relating the two orthogonal groups through the index-$2$ overlattice: $T_{\En}$ contains $T_{\Co}=\alpha^{\perp}_{T_{\En}}$ as a sublattice of index $2$, so restriction of an isometry of $T_{\En}$ preserving $\bZ\alpha$ gives one of $T_{\Co}$.

*Surjectivity.*
An isometry $g\in O^+(T_{\Co})$ preserves the discriminant form $q_{T_{\Co}}$, since $A_{T_{\Co}}$ is computed from $T_{\Co}$ alone.
To extend it must also fix the gluing class $[\eta/2]$, and it does: by @prop:coble-discriminant-group the discriminant representation of $\Orth(T_{\Co})$ factors through the isomorphism $\Orth(A_{T_{\Co}}, q_{T_{\Co}})\iso\Orth(A^0, q_{T_{\Co}}|_{A^0})$, where $A^0$ is the index-$2$ subgroup carrying the classes of integral $q$-value, and injectivity of that restriction together with the orthogonality of the decomposition $A_{T_{\Co}} = \ZZ\overline{h}\perp A^0$ forces the image of $\overline{h} = [\eta/2]$ to be $\overline{h}$ itself.
The $q$-value does not single the class out: the classes of $q$-value $\tfrac12$ modulo $\ZZ$ are exactly the coset $\overline{h} + A^0$, of order $2^{10}$, so fixing $\overline{h}$ is a genuine condition and not a formality — only the restriction isomorphism above shows that it holds for every isometry.
So $g$ preserves the gluing subgroup $H$ of @thm:nikulin-gluing determined by the primitive vector $\eta$, and hence extends to the overlattice: by the gluing criterion, isometries of the two summands preserving $H$ glue to an isometry of the overlattice.
The two choices of sign of the action on the line $\ZZ\alpha$ are the two extensions, and both lie in $O^+(T_{\En})$ because $\alpha$ is negative and the positive plane is untouched.

*The kernel.*
The kernel of the restriction is the subgroup of $\Stab_{O^+(T_{\En})}(\bZ\alpha)$ acting trivially on $\alpha^{\perp}$.
Such an isometry preserves $\alpha$ (the stabilizer condition) and the whole of $T_{\Co}$, and acts trivially there; it therefore acts by a scalar on the rank-one complement $\bZ\alpha$, and being an isometry with $\alpha^2=-2$ the only scalars are $\pm1$.
The scalar $+1$ is the identity, and the scalar $-1$ is the reflection $w_\alpha$ in the root $\alpha$.
So the kernel is $\langle w_\alpha\rangle$, of order $2$.

This lemma is a lattice statement.
It does not identify the degree-$2$ monodromy group and does not solve the integral isotropic-subspace lifting problem.
:::

### Period domains {#sec-coble-period-domains}

Define $\bD_{\Co}:=\bD(T_{\Co})$.

The unpolarized Hodge quotient is naturally

\[
\mcf_{\Co}^{\mathrm{Hdg}}
 :=O^+(T_{\Co})\backslash\bD_{\Co}.
\]

The direct and polarized quotients are, provisionally,

\[
\mcf_{\Co,2}^{\mathrm{dir}}
 :=\Gamma_{\Co,2}^{\mathrm{dir}}
   \backslash\bD_{\Co},
\]

and

\[
\mcf_{\Co,2}^{\mathrm{Hdg}}
 :=\Gamma_{\Co,2}^{\mathrm{Hdg}}
   \backslash\bD_{\Co}.
\]

The period theorem for classical Coble surfaces identifies an open subset of an orthogonal modular variety of this lattice type [@DK13].
The direct polarized period theorem and the equality of the two polarized quotients are required results, not consequences of the abstract lattice isomorphism.

### The required diagram of period quotients {#sec-period-diagram}

At the level of fixed embedded period domains, one has inclusions

\[
\bD(T_{\Co})
 \subset\bD(T_{\mathrm{En}})
 \subset\bD(T_{\mathrm{dP}}).
\]

The desired quotient diagram is

\[
\begin{tikzcd}[column sep=large,row sep=large]
\mcf_{\Co,2}
  \arrow[r]
  \arrow[d]
& \mcf_{\mathrm{En},2}
  \arrow[r]
  \arrow[d]
& \mcf_{(2,2,0)}
  \arrow[r]
& \mcf_4\\
\mcf_{\Co}
  \arrow[r]
& \mcf_{\mathrm{En}}.
\end{tikzcd}
\]

A diagram of rational domains is not automatically a diagram of arithmetic quotients.
To construct each arrow, one must prove that the relevant group acts through a compatible subgroup of a common $O(L_{K3})$, and one must identify the image group.
The direct arrow to $\mcf_{(2,2,0)}$ must later be shown to factor through the Enriques Heegner component.

::: {.problem #prob:period-diagram title="Required theorem (commuting period diagram)"}
The direct and Heegner arithmetic groups are compatible with the common labeled embedding chain; all arrows in the displayed diagram are well defined on quotients; and the direct Coble construction factors through the normalized $(-2)$-Heegner divisor in $\mcf_{\mathrm{En},2}$.
:::

## Baily--Borel boundary and integral cusp problems {#sec-cusps}

### Standard cusp data {#sec-standard-cusps}

Let $T$ have signature $(2,n)$ and let $\Gamma\subset O^+(T)$ be arithmetic.
A $0$-cusp is a $\Gamma$-orbit of primitive isotropic lines $\bZ e\subset T$.
Its hyperbolic cusp lattice is $\oT_e:=e^\perp/\bZ e$.

A $1$-cusp is a $\Gamma$-orbit of primitive isotropic planes $J\subset T$.
Its negative-definite quotient is $K_J:=J^\perp/J$.

For a fixed line $e$, the stabilizer has an exact sequence

\[
1\too U_e
\too \Stab_\Gamma(e)
\too \Gamma_e
\too1,
\]

where $U_e$ is the unipotent radical and $\Gamma_e$ acts on $\oT_e$.
The arithmetic group $\Gamma_e$, not the full orthogonal group of $\oT_e$, is the group relevant to the cusp reflection problem.

### The unpolarized Coble boundary {#sec-unpolarized-cusps}

Since scaling a form does not change its integral orthogonal group, $O(T_{\Co})=O(I_{2,9})$.

Standard transitivity results for indefinite odd unimodular forms imply the following [@Wal62; @DK13].

::: {.proof}

The cited transitivity is Wall's description of the orthogonal group of an indefinite odd unimodular lattice [@Wal62], applied to $I_{2,9}$ as in [@DK13].

The reduction: $T_{\Co}$ is not unimodular, but it is $I_{2,9}(2)$ by @prop:coble-transcendental, and scaling a form by a unit does not change its orthogonal group, so $O(T_{\Co})=O(I_{2,9}(2))=O(I_{2,9})$ as groups acting on the same lattice.
That is the step that puts the unpolarized Coble question inside Wall's classification of orbits in an odd unimodular lattice, rather than leaving it as a question about a non-unimodular form of type $(2,9)$.
:::

::: {.theorem #thm:unpolarized-cusps title="unpolarized Coble cusps"}
The quotient $O^+(T_{\Co})\backslash\bD_{\Co}$ has one orbit of primitive isotropic lines and one orbit of primitive isotropic planes.
For representatives $e$ and $J$,

\[
e^\perp/e\cong I_{1,8}(2),
\qquad
J^\perp/J\cong I_{0,7}(2).
\]
:::

::: {.proof}

*Lines.* Transitivity on primitive isotropic lines of $I_{2,9}$ follows from James' integral Witt theorem
[@Jam68, Theorem, p. 303] applied directly to the odd unimodular lattice: an isometry between primitive
sublattices extends when $r-|s|\geq2(r(J)+1)$, which for rank-one $J$ reads $11-7=4\geq4$, provided it
preserves characteristic status --- and here the clause is vacuous, since a characteristic vector of
$I_{p,q}$ has odd coordinates and square $\equiv p-q\equiv-7\equiv1\pmod 8$, never $0$. So no isotropic
line is characteristic and any two are isometric. This is the argument of
@prop:odd-unimodular-rank-one-transitivity, and it is a full-$O$ statement, as Wall's [@Wal62] is; the
component-preserving refinement is not part of either.

Wall's own theorem is the general statement behind the line case, and it is a theorem about *vectors*.
It determines the transitivity class of a vector of an odd unimodular lattice under its orthogonal group by
the four invariants norm, divisor, index and type (ordinary or characteristic), under the restriction
$r(L)-\abs{\fs(L)}\geq4$ [@Wal62]. For a primitive isotropic vector of $I_{2,9}$ the invariants are
$(0,\ 1,\ 1,\ \text{ordinary})$: norm $0$, divisor $1$ and index $1$ because the lattice is unimodular,
and ordinary by the congruence above. So there is exactly one class, which is the line half of the
statement; James' extension theorem is the special case of this that gives the isometry explicitly.

*Planes.* Transitivity on primitive isotropic planes is proved in this book, at
@thm:plane-transitivity-tco: it follows from the split unimodular model $B=\latI_{2,9}=\latI_{1,1}\perp
\latI_{1,8}$, in which planes through a line are the isotropic lines of the quotient, every isometry of the
quotient lifts as $\id\perp\varphi$ with the component character computed from
@def:period-component-character, and lines are transitive there. Neither [@Wal62] nor [@DK13] supplies either half of that.
Dolgachev--Kondo [@DK13] is about rationality of moduli spaces; it introduces $O(L)$, $O(A_L)$ and $O(L)^*$ in its §2 and the period domains in §3, and it contains no orbit statement for vectors or planes.
Wall [@Wal62] is described in the secondary literature as a classification of vectors by norm, divisor, index and type under $r-\abs{\fs}\geq4$, which the James argument agrees with. And $r-\abs{\fs}=4$ does not reach the rank-two case of James' inequality,
which would need $2(2+1)=6$.

The $\Gamma_{\Co}$-analogue of either half is not proved here, and the two halves stand differently. On lines the refinement is strict: $\Gamma_\Co$ has at least $527$ orbits where
$\Orth^+(T_\Co)$ has one, one for each nonzero isotropic class of $A_{T_\Co}$
(@prop:coble-stable-cusp-lower-bound). On planes even the number of orbits is open, and it is not implied
by strictness on lines. Nor does properness of a subgroup by itself make its orbits strictly finer: the
discriminant kernel is strictly larger than $\Gamma_\Co$ and has exactly the same orbits on lines and on
vectors (@prop:discriminant-kernel-orbits), so the question is decided orbit by orbit through the
stabilizers, as @lem:character-kernel-orbits states.

Both are statements about $O(T_{\Co})=O(I_{2,9})$, by the observation above; the exceptional case $I_{2,2}$,
where a characteristic isotropic vector does exist and line transitivity fails, shows why the congruence in
the line argument is doing real work (computations/reports/james_characteristic_counterexample.py).

*The component.* What the two halves above give is transitivity under $\Orth$, and the theorem asserts it
for $\Orth^+$. The step is the same in the two and happens at a primitive isotropic
line: split $B=P'\perp M'$ at the target line $l'$ by @cor:hyperbolic-splitting, and put
$\sigma'=\id_{P'}\perp(-\id_{M'})$, which fixes $l'$ pointwise and has
$\chi_{\mathrm{per},B}(\sigma')=(+1)\cdot\chi_{\mathrm{per},M'}(-\id_{M'})=-1$ by the product formula
@thm:plane-transitivity-tco derives from @def:period-component-character, so a transiting isometry that
lands in the wrong component is corrected by multiplying it by $\sigma'$ on the left. The Lorentzian
shortcut does not transfer: $-g$ has the same action on lines as $g$, but for signature $(2,9)$ the centre
$-\id$ is *inside* $\Orth^+$, its determinant on the positive plane being $(-1)^2=+1$, so it cannot move
anything between components. With lines transitive under $\Orth^+(B)$, primitive isotropic *vectors* are too:
a transiting $g$ sends $v$ to $\pm v'$, and $-\id\in\Orth^+$ supplies the sign.

For a primitive isotropic $e$ in a lattice $L$ of signature $(2,9)$, the quotient $e^\perp/e$ is a lattice of signature $(1,8)$ and inherits the discriminant form of $L$ up to the factor $1/p^2$ that $\div$-scaling forces; for $T_{\Co}=I_{2,9}(2)$ and $\div(e)=2$ it is $I_{1,8}(2)$, and for a primitive isotropic plane $J$ the quotient $J^\perp/J$ has signature $(0,7)$ and is $I_{0,7}(2)$.
So the two boundary strata are single orbits and the lattices attached to them are as displayed.

The statement is about $O^+(T_{\Co})$ acting on $\bD_{\Co}$, and the arithmetic subgroup $\Gamma_{\Co,2}$ is strictly smaller, so the orbits for the polarized problem are a refinement of these and are not determined here.
:::

This theorem concerns the full orthogonal group.
It does not determine the cusps for the polarized subgroup.

### Reduction to the discriminant form {#sec-finite-shadow}

For a $2$-elementary lattice, a primitive isotropic vector of divisibility $2$ determines a nonzero isotropic class in the discriminant group.
Thus reduction modulo the lattice gives maps

\[
\left\{
\Gamma_{\Co,2}\text{-orbits of primitive isotropic lines}
\right\}
\too
\left\{
\rho(\Gamma_{\Co,2})\text{-orbits of singular classes in }A_T
\right\},
\]

and analogous maps for isotropic planes and incident flags.

::: {.warning #warn:finite-shadow title="finite shadow versus integral cusp"}
These maps need not be bijective.
The integral parabolic stabilizer can have a proper image in the finite stabilizer of the reduced flag.
Consequently, an orbit calculation in $O(A_{T_{\Co}})$ does not classify Baily--Borel cusps without a separate integral lifting theorem.
:::

The standard ways to solve this problem are:

1. integral normal forms and explicit Eichler transvections;

2. computation of the images of integral line and plane stabilizers followed by finite double-coset calculations; or

3. a certified integral orbit algorithm, for example of the type developed in [@Dawes22].

### Computational record in the finite quadratic space {#sec-finite-orbits}

In the $10$-dimensional plus-type quadratic space over $\bF_2$, the subgroup associated with the proposed degree-$2$ congruence condition has four orbits of nonzero singular vectors and five orbits of totally singular planes.
The labels below are internal finite labels; they are not cusp labels.

| Finite vector type | Orbit size |
| :--- | ---: |
| $A$ | $135$ |
| $B$ | $2$ |
| $C$ | $270$ |
| $D$ | $120$ |

: Finite singular-vector orbits. {#tbl-finite-vector-orbits}

| Finite plane type | Orbit size |
| :--- | ---: |
| $AAA$ | $1575$ |
| $ABC$ | $270$ |
| $ACC$ | $9450$ |
| $ADD$ | $3780$ |
| $CCD$ | $8640$ |

: Finite totally singular plane orbits. {#tbl-finite-plane-orbits}

A finer calculation decorates a finite plane by one of eight ``stars'' in the natural $S_8$-set attached to its $6$-dimensional quotient.
For a prescribed $S_7$ subgroup there are seven enhanced plane orbits and thirteen enhanced flag orbits.
The identification of that $S_7$ with the image of the integral plane stabilizer is not proved.

::: {.problem #prob:cusp-lifting title="Required theorem (integral cusp lifting)"}
Determine the exact images of the integral isotropic-line and isotropic-plane stabilizers in the finite orthogonal group and use them to classify

\[
\Gamma_{\Co,2}\backslash
\{\text{primitive isotropic lines}\},
\]

\[
\Gamma_{\Co,2}\backslash
\{\text{primitive isotropic planes}\},
\]

and the incident flags.
Give explicit integral representatives and stabilizers.
:::

**The line case.** By §@sec-cusp-lifting: $\Orth(B)$ is transitive on primitive isotropic vectors ([@Wal62], Theorem 1.2, an isotropic vector being non-characteristic since a characteristic one has $w^2\equiv\sigma(B)\equiv1 \pmod 8$), every nonzero isotropic class is $[v/2]$ for a primitive isotropic $v$ and the zero class is not, and $\rho(\Stab_{\Orth(B)}(v)) = \Stab_{\Orth(q)}([v/2])$ with the Eichler transvections accounting for the kernel of order $2^8$. Hence the $\Gamma_\Co$-orbits of primitive isotropic lines are the $527$ nonzero isotropic classes, and for $\Gamma = \rho^{-1}(G_\Co)$ they are the four orbits $135, 2, 270, 120$. The plane case is the same two steps with the index for $\Stab(P)$, which is not computed here. The finite half: the group whose orbits are the reported $135, 2, 270, 120$ is $G_\Co = \rho_{S_\En}(\Stab_{\Orth(S_\En)}(h))$, the image of the degree-$2$ parabolic stabilizer, of order $\abs{W(E_8)}$, and the orbit partition $[1,2,120,135,270]$ of the $528$ isotropic classes is computed in `computations/reports/coble_gco_orbit-decomposition.py`. The integral half is open and is stated in §@sec-cusp-lifting: the map $\Gamma_\Co\cdot v\mapsto[v/2]$ is well defined because $\Gamma_\Co$ acts trivially on $A_{T_\Co}$, it is **not** injective, its fibres are the $\Gamma_\Co$-orbits inside a single class, and what is missing is transitivity of the congruence subgroup $\ker\rho_{T_\Co}$ on a class — available for $\Orth(B)$ by Eichler's criterion ([@Eic74]), not for $\ker\rho$.

### Necessary restrictions on maps to Enriques cusps {#sec-possible-cusp-images}

Suppose the comparison map to the Enriques period quotient has been constructed.
Let $e$ be a Coble isotropic line.
The root $\alpha$ lies in $e^\perp$ and gives a $(-2)$ class in the Enriques cusp lattice.
Therefore an Enriques $0$-cusp whose hyperbolic lattice has all norms divisible by $4$ cannot contain a Coble branch.
In the AEGS numbering, this excludes cusp $1$ and leaves only cusps $2,3,4,5$ as possible images.

Similarly, if $J$ is a Coble isotropic plane, the class of $\alpha$ gives a $(-2)$ vector in $J^\perp/J$.
Hence a Type II Enriques cusp whose negative quotient is $E_8(2)$ cannot contain a Coble branch.
Reading the border types in AEGS Figure 4, the double-rectangle cusps $12,\ 13,\ 14,\ 15,\ 245$ map to the segment-flipping $E_8(2)$ cusp and are excluded.
The only possible Enriques $1$-cusp images are therefore $34,\ 35,\ 45,\ 55$.

::: {.remark #rmk:cusp-images}
This is a necessary-condition argument, not an integral orbit classification.
It does not determine how many Coble cusps lie above any of the four possible image cusps.
:::

## Reflection theory and Coxeter data {#sec-coxeter}

### The unpolarized cusp chamber {#sec-unpolarized-coxeter}

Write

\[
I_{1,8}(2)
 =\bZ H_0\oplus\bigoplus_{i=1}^8\bZ E_i,
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

::: {.theorem #thm:unpolarized-coxeter title="unpolarized Coble Coxeter chamber"}
A fundamental chamber for the reflection group of $I_{1,8}(2)$ is defined, for

\[
x=aH_0-\Sum_{i=1}^8b_iE_i,
\]

by

\[
b_1\ge b_2\ge\cdots\ge b_8\ge0,
\qquad
 a\ge b_1+b_2+b_3.
\]

The simple roots are $r_0,\ldots,r_8$.
The diagram is the chain

\[
r_1-r_2-r_3-r_4-r_5-r_6-r_7\dto r_8
\]

with $r_0$ attached to $r_3$ by a single edge.
:::

::: {.proof}
Signed permutations of the $E_i$ reduce to the ordered region, and the Cremona reflection in $r_0$ reduces the final inequality.
This is the standard Vinberg chamber for $I_{1,8}$, with the form scaled by $2$.

The unique maximal parabolic subdiagram is obtained by deleting $r_1$ and has type $\widetilde B_7$.
The rank-$8$ elliptic subdiagrams are listed in @tbl-unpolarized-elliptic.

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

: Rank-$8$ elliptic subdiagrams of the unpolarized chamber. {#tbl-unpolarized-elliptic}
:::

### Orthogonal wall links {#sec-orthogonal-link}

Let $a$ be a $(-2)$ root in a hyperbolic lattice $M$, and let $b$ be another negative wall normal.
The normal inside $a^\perp$ to the intersection $b^\perp\intersect a^\perp$ is the primitive vector proportional to the orthogonal projection of $b$ to $a^\perp$.

::: {.construction #cons:wall-link title="orthogonal wall link"}
Define

\[
b_{\operatorname{link}}
 :=\operatorname{prim}\bigl(2b+(b,a)a\bigr).
\]
:::

The formula is integral and defines the correct hyperplane in $a^\perp$.
It is a linear-algebra statement.
It does not imply that $b_{\operatorname{link}}$ is a root of the orthogonal lattice.

::: {.warning #warn:wall-root title="restricted wall versus reflection wall"}
A hyperplane obtained by slicing an ambient Coxeter chamber can fail to be the mirror of an integral reflection in the sublattice.
Conversely, the orthogonal sublattice can have reflective roots whose mirrors are invisible in the ambient root system.
:::

A Coble analogue of the AEGS root-folding theorem must prove both directions: that every relevant restricted wall is a Coble root wall and that every Coble root wall meeting the chamber is obtained in the prescribed way.

### Candidate reflection twist at a cusp {#sec-cusp-reflection-twist}

At the full K3-lattice level one has the reflection twist $I_{\Co}=w_\alpha I_{\mathrm{En}}$.
If a primitive isotropic line $e$ is orthogonal to $\alpha$, the involutions induce actions on the cusp quotient $e^\perp/e$.
This suggests the cusp-level candidate $J_{\Co}=w_{\bar\alpha}J_{\mathrm{En}}$, where $\bar\alpha$ is the image of $\alpha$ in the cusp lattice.

This formula is not yet a direct folding theorem.
One must prove that the cusp action lifts through the full discriminant gluing and corresponds to the geometric involution, just as AEGS separately prove their lifting lemma.

### Corrected ambient square Gram data {#sec-gram-correction}

In the square ambient K3 cusp diagram, the two black roots $\alpha_{20}$ and $\alpha_{21}$ both have square $-4$.
The edge joining them is thick.
Therefore $(\alpha_{20},\alpha_{21})=4$.

The value $2$ gives a Gram matrix of rank $20$, incompatible with the rank-$18$ cusp lattice.
The value $4$ gives the correct rank $18$.

### Candidate wall-slice diagrams {#sec-wall-slices}

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

The chosen roots are $\alpha_{10}$, $\alpha_0$, $\alpha_6$, and $\alpha_{16}$, respectively.
Each displayed sliced wall is a genuine root in the orthogonal lattice in the cases checked symbolically.
That the displayed walls form a complete simple system is not proved.

The raw numbers of maximal parabolic faces in the four sliced arrangements are $1$, $3$, $3$, $9$.

These counts are diagnostic data only.
They disagree with some finite-shadow orbit counts, which indicates that chamber completeness, arithmetic diagram automorphisms, and the calibration of finite orbits must all be resolved before boundary strata are enumerated.

::: {.problem #prob:coxeter-completeness title="Required theorem (Coble Vinberg and root completeness)"}
For every polarized Coble $0$-cusp:

1. determine the arithmetic cusp lattice and the image of its stabilizer;

2. run Vinberg's algorithm or prove a two-sided root-link theorem;

3. prove that the resulting simple roots define a fundamental chamber;

4. compute the chamber automorphism group and reflection index; and

5. enumerate all maximal parabolic and elliptic subdiagrams modulo the full arithmetic group.
:::

A list of vectors or a finite Gram-matrix computation is not a Coxeter theorem without these steps.

The five items are stated for the cusp lattices, and they are the right site for them: item 2 is Vinberg's algorithm, which is a statement about a lattice of signature $(1,n)$, and the transcendental lattice $T_\Co$ of signature $(2,9)$ is not one.
For $T_\Co$ itself the corresponding question is the reflective-lattice one, and its first half holds: by @prop:gamma-co-reflective-set the reflections lying in the stable group $\Gamma_\Co$ are exactly those in the short roots, no long root qualifying.
What remains open for $T_\Co$, and is not one of the five items above, is the index of the group generated by that reflective set in $\Gamma_\Co$.

## Integral-affine structures, dlt quotients, and stable models {#sec-integral-affine}

### The AEGS dictionary {#sec-aegs-dictionary}

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

For a primitive isotropic line $e$, a Type III monodromy invariant is a vector $\lambda\in\oT_e\tensor_\ZZ\bR$ in the closure of a positive chamber.
If $\{r_i\}$ is a simple-root system, the root coordinates are $\ell_i=(\lambda,r_i)\ge0$.

They become edge lengths, internal blowup parameters, and nodal-surgery sizes in a moment or Symington polygon.
A zero coordinate places the monodromy on a wall.
If the wall corresponds to a visible curve, the zero can collapse a path joining two focus-focus singularities.

The direct Coble theory should preserve this dictionary but must add the data of the fixed exceptional root and its quotient branch curve.

### The Coble integral-affine package {#sec-coble-affine-package}

::: {.definition #def:coble-affine-package title="candidate polarized Coble integral-affine package"}
A Coble integral-affine package is a tuple

\[
\bigl(B(\lambda),R_{\IA},E_{\IA},
      \iota_{\Co,IA},\iota_{\mathrm{dP,IA}}\bigr)
\]

where

1. $B(\lambda)$ is the integral-affine dual sphere or Type II segment of a K3 divisor model;

2. $R_{\IA}$ is the weighted balanced graph recording the del Pezzo ramification divisor;

3. $E_{\IA}$ records the visible class, collapsed path, or marked affine stratum associated with the exceptional root $\alpha$;

4. the two affine involutions commute and preserve the full polarized package;

5. the quotient data predicts the branch curve $C$ and the divisor $R_{\wV}$ on a Coble dlt model.
:::

The notation $E_{\IA}$ is schematic.
Depending on the cusp, the exceptional root can be represented by a visible path, a collapsed edge, an $I_2$ affine singularity, or equivalent marked data in the triangulation.
A direct theory must specify the correct object cusp by cusp.

### Heegner-wall specialization of an ambient model {#sec-heegner-affine-specialization}

Suppose a degeneration lies in the $\alpha$-Heegner locus and approaches a Type III cusp represented by $e$.
After a suitable marking and base change, one expects $(\alpha,e)=0$ and $(\alpha,\lambda)=0$.

If $\alpha$ is represented by a visible path in the chosen integral-affine model, the second equation says that the path has zero affine length.
The corresponding pair of parallel $I_1$ singularities coalesces to an $I_2$ singularity.
This is the same local operation used by AEGS for crossed nodes, but in the Coble problem it records the persistent $A_1$ singularity of the K3 cover.

::: {.remark #rmk:affine-local}
The local collision picture is reliable once the relevant root has been identified in the genuine cusp lattice.
It cannot be used to prove that a candidate wall slice is the full Coxeter chamber.
:::

### Required realization theorem {#sec-affine-realization}

::: {.problem #prob:affine-realization title="Required theorem (direct integral-affine realization)"}
For every sufficiently divisible monodromy invariant in every direct Coble cusp chamber, construct a K3 divisor model $(\mcx,\mcr,\mce)\too(C,0)$ whose dual complex is the prescribed Coble integral-affine package.
Conversely, show that every direct Coble degeneration admits such a model after finite base change and allowed dlt modification.
:::

The proof must include polygon closure, parity and divisibility conditions, triangulation, component periods, gluing parameters, and the realization of the exceptional class as a Cartier divisor or contractible ADE configuration.

## Required algebraic extension theorem {#sec-algebraic-extension}

An affine symmetry is not automatically an algebraic involution.
AEGS use limiting-period conditions and invariant component/gluing parameters to extend their involution over a general divisor model.
The Coble version must also retain the exceptional root.

::: {.problem #prob:algebraic-extension title="Required theorem (algebraic extension of the Coble package)"}
A general divisor model with direct Coble monodromy admits commuting regular involutions $\iota_{\Co}$ and $\iota_{\mathrm{dP}}$ such that

\[
\iota_{\Co}(\mce)=\mce,
\qquad
\iota_{\Co}(\mcr)=\mcr.
\]

The cohomological action is the prescribed labeled lattice action, the involutions commute on the total space, and equivariant simultaneous resolution and contraction are compatible with the family.
:::

A proof must not infer regularity solely from the action on the dual complex.
For special degenerations the initial action can be birational and may require contraction of ADE configurations before it becomes regular.

## The direct dlt Coble model {#sec-coble-dlt}

Assume the algebraic extension theorem.
Form the quotient $\widetilde{\mcv}:=\mcx/\iota_{\Co}$.

Let $\mcc$ be the divisorial branch locus descending from $\mce$, and let $\mcr_{\wV}$ be the quotient of the del Pezzo ramification divisor.
The natural crepant pair is

\[
\left(
\widetilde{\mcv},
\frac{1+\epsilon}{2}\mcc
 +\epsilon\mcr_{\wV}
\right).
\]

::: {.problem #prob:dlt-quotient title="Required theorem (direct dlt quotient)"}
After the prescribed dlt modification, the above pair is dlt over the base; its fibers are slc; the boundary contains no prohibited log canonical center; and

\[
K_{\widetilde{\mcv}}
 +\frac{1+\epsilon}{2}\mcc
 +\epsilon\mcr_{\wV}
\]

is relatively big and nef.
:::

The local analysis differs from the Enriques case because the Coble involution has a divisorial fixed locus on the resolved K3 model.
One must analyze fixed components, fixed double curves, triple points, and the interaction between $\mcc$ and the conductor.

## Relative Proj and the stable model {#sec-relative-proj}

The dlt model is not the KSBA stable model.
The stable model is the relative log canonical model

\[
\Proj_C
\bigoplus_{m\ge0}
H^0\!\left(
\widetilde{\mcv},
 m\left(
 K_{\widetilde{\mcv}}
 +\frac{1+\epsilon}{2}\mcc
 +\epsilon\mcr_{\wV}
 \right)
\right).
\]

After contracting $\mcc$ to the singular Coble family, this is expected to agree with the relative Proj for a sufficiently divisible multiple of $\mcr^\sharp$.

::: {.problem #prob:stable-proj title="Required theorem (stable contraction)"}
Determine exactly which curves, components, and conductor strata are contracted by the above relative Proj, and prove that the resulting family is the KSBA stable family of pairs $(V^\sharp,\epsilon R^\sharp)$.
:::

## Component classification problem {#sec-component-classification}

The direct Coble quotient can produce surface components with branch boundary $C$, conductor boundary $D$, and ramification divisor $R$.
The appropriate normalized component datum is

\[
\left(
V,
D+\frac{1+\epsilon}{2}C+\epsilon R
\right).
\]

::: {.problem #prob:component-classification title="Required theorem (Coble component classification)"}
Classify all finite Type III and affine Type II component pairs arising in direct Coble stable limits.
Give explicit equations or toric models, involutions, quotient singularities, branch allocation, decorations, and stable contractions; prove that every component occurs in the list and every listed type occurs.
:::

This is the Coble analogue of the AEGS ABCDE surface classification.
It cannot be obtained merely by replacing the Enriques involution in the existing tables: the resolved Coble involution has a fixed curve.

## Status of adaptations of AEGS examples {#sec-example-status}

Several candidate recipes were identified:

- start with the AEGS cusp-$3$ integral-affine model and impose one additional Coble-root equation;

- start with the cusp-$5$ model, where several crossed-root coordinates already vanish, and impose an independent Coble-root condition;

- start with the non-simple cusp-$2$ model and impose the appropriate white-root wall while retaining the fact that the bottom fixed edge has no ramification support.

These are recipes, not completed examples.
A complete example must specify the integral root, the visible path, the compatible triangulation, the component periods and gluings, the two algebraic involutions, all quotient singularities, and the final $R^\sharp$-trivial contraction.

## Fans, semifans, and semitoroidal compactifications {#sec-semifans}

### Coxeter fans and generalized Coxeter semifans {#sec-generalized-coxeter}

Let $M$ be a hyperbolic cusp lattice, $W$ a reflection group, and $C$ a fundamental chamber.
The Coxeter fan consists of the $W$-translates of $C$ in the rational closure of the positive cone.
If the chamber has finite volume, this is a rational polyhedral fan.

Suppose the simple roots are partitioned into relevant and irrelevant roots.
Let $W_{\mathrm{irr}}$ be generated by the irrelevant reflections.
The generalized chamber is

\[
C_{\mathrm{gen}}
 =\Union_{w\in W_{\mathrm{irr}}}wC.
\]

Its $W$-translates form the generalized Coxeter semifan.
Geometrically, a root is relevant only if crossing its wall changes the stable pair after the relative Proj.

::: {.warning #warn:relevance title="relevance is geometric"}
In the autonomous Coble theory, a root cannot be declared relevant merely because it lies on the boundary of an ambient Enriques or K3 diagram.
Relevance must be characterized by the Coble package $(R_{\IA},E_{\IA})$ and the resulting stable contraction.
:::

### Direct Coble semifans {#sec-direct-semifans}

Assume that the direct cusp groups and Coxeter chambers have been computed.
For each direct Coble $0$-cusp, define a root to be relevant if a general crossing of its wall changes at least one of the following stable data:

1. the support or degree distribution of $R^\sharp$;

2. the branch curve or exceptional-root contraction;

3. the normalization components or conductor gluing;

4. the number of surviving double curves or components; or

5. the isomorphism class of the relative Proj.

::: {.problem #prob:direct-semifan title="Required theorem (direct Coble semifan)"}
The maximal regions of combinatorial constancy of direct Coble stable pairs are exactly the cones of the generalized Coxeter semifan obtained from the direct Coble Coxeter diagram of @prob:coxeter-completeness and the intrinsic relevance marking.
:::

The theorem must determine cusp by cusp whether the irrelevant reflection group is finite, whether the semifan is an actual fan, and whether any Type II parabolic component consists entirely of irrelevant roots.

### Normalized closure of a subtorus {#sec-subtorus-lemma}

The Heegner-restriction strategy uses the following standard toric fact.

::: {.lemma #lem:subtorus-normalization title="normalization of a subtorus closure"}
Let $N\subset M$ be a saturated sublattice of cocharacter lattices, let $T_N\subset T_M$ be the corresponding subtorus, and let $X_\torfan$ be a toric variety for a fan $\torfan\subset M_\bR$.
The normalization of the closure of $T_N$ in $X_\torfan$ is the toric variety associated with the induced fan $\torfan|_{N_\bR} =\{\sigma\intersect N_\bR:\sigma\in\torfan\}$, with the induced lattices saturated.
:::

::: {.proof}

This is standard in toric geometry; the saturation hypothesis enters in the last step.

The $T_M$-orbits of $X_\torfan$ correspond to the cones of $\torfan$, and the closure of $T_N$ meets exactly those orbits whose cone meets $N_\bR$ in a full-dimensional subset — that is, the closure is the union of the $T_N$-orbits indexed by the intersections $\sigma\cap N_\bR$.
Each such intersection is a cone in $N_\bR$ because $\sigma$ is a cone and $N_\bR\subseteq M_\bR$ is a linear subspace, and the intersections are closed under taking faces, so they form the fan $\torfan|_{N_\bR}$.
The toric variety of that fan is normal by construction, and it is the closure up to normalization; the two agree because $N$ is saturated in $M$, which is what makes $M/N$ torsion-free so that the intersections above are the faces of a genuine fan with saturated cones rather than only a rational polyhedral subdivision.
:::

This lemma is local and toric.
It does not by itself identify the normalized closure of a Heegner divisor in a semitoroidal arithmetic quotient.

### Why semitoroidal restriction is not formal {#sec-restriction-not-formal}

To apply the subtorus lemma to the Coble Heegner locus, one must prove all of the following.

1. The local Heegner branch is the asserted saturated subtorus rather than a translated subtorus or a union of branches.

2. The integral unipotent-center lattice for the Coble cusp is the expected sublattice of the Enriques cusp lattice.

3. The arithmetic cusp stabilizer acts compatibly on the induced fan.

4. The induced local constructions agree along every $1$-cusp.

5. Normalization commutes with the prescribed semitoroidal contractions.

6. The ambient contraction does not identify distinct normalized Coble branches.

7. No additional coarsening occurs after passing to Coble stable pairs.

::: {.problem #prob:restricted-semifan title="Required theorem (semitoroidal restriction)"}
After passage to a common toroidal refinement, the normalization of the Heegner closure is obtained by saturated intersection with the Coble cusp subspaces, and the induced semitoroidal contractions coincide with combinatorial constancy for the Coble stable-pair family.
:::

Without this theorem, “intersect the AEGS semifans” is a candidate construction rather than a compactification theorem.

## The KSBA moduli space and the two target theorems {#sec-ksba-targets}

### The open KSBA moduli functor {#sec-open-ksba}

Let $\mathfrak M_{\Co,2}^{\circ}$ denote the direct open moduli stack of singular Coble data for which the pair $(V^\sharp,\epsilon R^\sharp)$ is klt and $K_{V^\sharp}+\epsilon R^\sharp$ is ample.
Define $\overline{\mathfrak M}_{\Co,2}\uksba$ to be its closure in the appropriate KSBA stack with fixed coefficient and volume.

The divisor $R^\sharp$ must be defined universally as the divisorial fixed locus of the descended del Pezzo involution.
Choosing a divisor separately on each fiber does not define a moduli problem.

### Autonomous target theorem {#sec-autonomous-target}

::: {.problem #prob:autonomous-theorem title="Target theorem A (autonomous Coble compactification)"}
The direct open period map identifies

\[
\mathfrak M_{\Co,2}^{\circ}
\homotopic
\Gamma_{\Co,2}^{\mathrm{dir}}
\backslash\bD_{\Co}^{\circ},
\]

for an explicit hyperplane complement.
The normalization of $\overline{\mathfrak M}_{\Co,2}\uksba$ is the semitoroidal compactification defined by the explicit direct Coble semifans.
All cusps, Coxeter diagrams, Type II and Type III strata, and fan-versus-semifan loci are explicitly determined.
:::

This theorem is logically independent of the Enriques Heegner comparison.
It requires direct analogues of the entire AEGS proof architecture.

### Heegner comparison target {#sec-heegner-target}

Let $\discriminant_\alpha$ be the $(-2)$-Heegner divisor in the degree-$2$ Enriques period quotient, defined using a fixed embedded root.

::: {.problem #prob:comparison-theorem title="Target theorem B (comparison with the Enriques Heegner divisor)"}
The direct Coble period quotient is canonically isomorphic to the normalization of $\discriminant_\alpha$.
Under this isomorphism:

1. the direct and Heegner arithmetic groups agree;

2. the period maps to $\mcf_{\mathrm{En}}$, $\mcf_{\mathrm{En},2}$, $\mcf_{(2,2,0)}$, and $\mcf_4$ commute;

3. the direct projective construction agrees with the Heegner specialization;

4. the direct cusps and Coxeter diagrams map to the corresponding Enriques and K3 data;

5. the direct stable divisor agrees with the restriction of the ambient ramification divisor; and

6. the direct semitoroidal compactification is the normalization of the KSBA closure of the Heegner divisor inside the AEGS compactification.
:::

Target theorem B is the comparison theorem of @sec-central-problem.
Target theorem A is a substantial independent theorem and an intermediate strategy, but it becomes a proof of the Heegner statement only after Target theorem B is established.

## Proof strategies and research programs {#sec-strategies}

This section states five proof strategies, the theorem chain each requires, and the inferences each must avoid.

### Strategy A: normalize the Heegner closure inside the AEGS compactification {#sec-strategy-heegner}

#### Outline {#sec-strategy-heegner-outline}

Fix a root $\alpha\in T_{\mathrm{En}}$ and let $\discriminant_\alpha$ be the corresponding degree-$2$ Heegner component.
Let

\[
\nu_{\mathrm{En}}:
\mcf_{\mathrm{En},2}^{\torfan_{\mathrm{En}}}
\too
\overline{\mcf}_{\mathrm{En},2}\uksba
\]

be the AEGS normalization map.
Take the normalization $H_\alpha$ of the closure of $\discriminant_\alpha$ in the source.
The strategy is to identify $H_\alpha$ with the normalization of the Coble KSBA closure and compute its local semitoroidal structure.

#### Required chain of results {#sec-strategy-heegner-chain}

The strategy requires the following sequence.

::: {.problem #prob:A1 title="A1. Root-orbit and embedded-component lemma"}
The relevant roots form one orbit under the actual degree-$2$ Enriques group, or the chosen component is otherwise specified intrinsically.
The stabilizer image on $T_{\Co}$ is computed.
:::

::: {.problem #prob:A2 title="A2. Root-marked universal-family lemma"}
Over the stack-theoretic normalization of the Heegner component, there is a universal family in which the fixed $A_1$ point, its simultaneous resolution after the required Weyl cover, the exceptional root, and the ambient ramification divisor are compatible with base change.
:::

::: {.problem #prob:A3 title="A3. Coble-pair identification lemma"}
The restriction of the AEGS stable pair to the generic Heegner point is precisely $(V^\sharp,\epsilon R^\sharp)$ of @sec-canonical-contraction, with the same universal divisor.
:::

::: {.problem #prob:A4 title="A4. Generic reconstruction lemma"}
A general stable Coble pair recovers its canonical K3 cover, the distinguished $A_1$ point, the degree-$4$ class, the del Pezzo lattice isometry, and the Heegner period point; the del Pezzo slot is recovered as a lattice isometry, at least for the representative carried by the two isotropic summands, which no automorphism realizes (@cor:no-del-pezzo-involution-coble-cover); whether another admissible choice is geometric is open.
Consequently the restricted finite map is generically injective.
:::

::: {.problem #prob:A5 title="A5. Arithmetic cusp-lifting theorem"}
The Coble cusp orbits, stabilizers, and maps to Enriques cusps are computed integrally.
:::

::: {.problem #prob:A6 title="A6. Local toroidal normalization theorem"}
In every cusp chart, the normalized Heegner closure is the saturated toric subvariety associated with the actual Coble unipotent-center lattice and the induced arithmetic action.
:::

::: {.problem #prob:A7 title="A7. Semitoroidal compatibility theorem"}
The local normalized toric closures glue along the Type II boundary and are compatible with the AEGS semitoroidal contractions.
:::

::: {.problem #prob:A8 title="A8. No-further-coarsening theorem"}
Every wall retained by the induced Coble semifan changes the Coble stable pair; equivalently, the classifying map from the normalized Heegner closure to the Coble KSBA closure is finite and has no positive-dimensional fibers.
:::

With A1--A8, the conclusion follows by normality and finite birationality.

#### Available ingredients {#sec-strategy-heegner-worked}

The following ingredients are available.

- The root complement $T_{\Co}$ and reflection twist are explicit.

- The open local Coble quotient and stable divisor are explicit.

- The parent AEGS normalization is already finite.

- The normalization of a saturated subtorus closure in an ordinary toric chart is understood.

- Parent charts that are honest fans remain rational polyhedral after intersection with a rational subspace.

#### Invalid inferences {#sec-strategy-heegner-failed}

A restriction argument must not make the following inferences.

1. The stabilizer-image group equals geometric monodromy.

2. An inclusion of rational domains gives a quotient map, without a proof of group compatibility.

3. Generic index-one-cover reconstruction recovers the degree-$4$ projective model and the labeled lattice tuple, without a proof.

4. An $O(A)$ computation solves the integral cusp problem.

5. Hyperplane slices are Coxeter diagrams, without a root-completeness theorem.

6. Normalization of a toric subtorus closure survives arithmetic quotienting and semitoroidal contraction.

Each of these steps requires a proof; the chain A1--A8 states the required lemmas.

### Strategy B: autonomous Coble theory in the style of AEGS {#sec-strategy-autonomous}

#### Autonomous outline {#sec-strategy-autonomous-outline}

This strategy never defines the direct Coble objects as a locus in Enriques moduli.
It begins with the direct cover datum of Definition (direct resolved Coble cover datum) (@def:direct-cover-datum), computes its period theory, and reproduces Coble analogues of the AEGS constructions.
Only after the autonomous compactification theorem is proved does one compare it with the Heegner divisor.

#### Open moduli and periods {#sec-strategy-B-section2}

The following results are required in order.

::: {.problem #prob:B21 title="B2.1. Direct projective-model theorem"}
The nodal invariant $(4,4)$ construction defines the complete generic direct Coble family and its universal divisors.
:::

::: {.problem #prob:B22 title="B2.2. Intrinsic reconstruction theorem"}
The singular Coble pair recovers the quartic del Pezzo quotient, the two double-cover algebras, the nodal K3 cover, both involutions, and the degree-$4$ class.
:::

::: {.problem #prob:B23 title="B2.3. Labeled lattice classification theorem"}
Compute the simultaneous eigenspaces of the Klein-four action, their primitive closures and discriminant forms, and prove the labeled rigidity theorem of @sec-labeled-lattice-data.
:::

::: {.problem #prob:B24 title="B2.4. Direct global Torelli theorem"}
The marked direct Coble moduli stack is an explicit arrangement complement $\bD_{\Co}^\circ$, with the ample/nef chamber and exceptional root correctly encoded.
:::

::: {.problem #prob:B25 title="B2.5. Direct monodromy theorem"}
The deck group of the marking cover and the geometric monodromy group equal the labeled centralizer group $\Gamma_{\Co,2}^{\mathrm{dir}}$.
:::

::: {.problem #prob:B26 title="B2.6. Direct stable-pair theorem"}
The universal divisor $R^\sharp$ is flat, uniformly $\bQ$-Cartier and ample, and the pairs $(V^\sharp,\epsilon R^\sharp)$ define a separated bounded KSBA moduli problem for $0<\epsilon\ll1$.
:::

#### Cusps and reflection chambers {#sec-strategy-B-section3}

::: {.problem #prob:B31 title="B3.1. Integral Baily--Borel classification"}
Classify all primitive isotropic lines, planes, and flags under $\Gamma_{\Co,2}^{\mathrm{dir}}$, with explicit representatives and stabilizers.
:::

::: {.problem #prob:B32 title="B3.2. Vinberg theorem at each $0$-cusp"}
Run Vinberg's algorithm for each actual cusp lattice and arithmetic reflection group.
Prove termination, completeness of the simple roots, and compute the chamber automorphism group.
:::

::: {.problem #prob:B33 title="B3.3. Full-lattice lift theorem"}
Lift every cusp-lattice involution or reflection-twist description through the discriminant gluing to the labeled K3 lattice datum.
:::

::: {.problem #prob:B34 title="B3.4. Parabolic and elliptic exhaustion theorem"}
Enumerate all maximal parabolic and relevant elliptic subdiagrams modulo the arithmetic chamber automorphism group and verify agreement with the independently computed isotropic-plane orbits.
:::

#### Integral-affine and dlt models {#sec-strategy-B-section4}

::: {.problem #prob:B41 title="B4.1. Mirror and polygon theorem"}
Construct, for every direct Coble cusp, the mirror anticanonical pair, moment polygons, Symington surgeries, and root-coordinate formulas.
:::

::: {.problem #prob:B42 title="B4.2. Integral-affine realization theorem"}
Realize every sufficiently divisible chamber point by a divisor model carrying the full Coble affine package.
:::

::: {.problem #prob:B43 title="B4.3. Affine-symmetry characterization theorem"}
Characterize the direct Coble period locus exactly by the presence of the prescribed affine involutions and exceptional-root data.
:::

::: {.problem #prob:B44 title="B4.4. Algebraic involution theorem"}
Promote the affine symmetries to commuting regular involutions on general divisor models and control the birational-to-regular modification for special models.
:::

::: {.problem #prob:B45 title="B4.5. dlt quotient and relative-Proj theorem"}
Prove the dlt and slc properties, canonical bundle formula, positivity, and exact stable contractions.
:::

#### Sections 5--7 analogues: semifans and boundary classification {#sec-strategy-B-section5}

::: {.problem #prob:B51 title="B5.1. Coble recognizability theorem"}
Prove that the direct divisor package is recognizable from limiting Hodge and combinatorial data in the sense required by the Alexeev--Engel compactification theory.
:::

::: {.problem #prob:B52 title="B5.2. Geometric relevance theorem"}
Determine exactly which direct Coxeter walls change the stable pair and hence which roots are relevant.
:::

::: {.problem #prob:B53 title="B5.3. Generalized Coxeter semifan theorem"}
Prove that the direct regions of combinatorial constancy are the generalized Coxeter semifans of the direct chambers of @prob:B32.
:::

::: {.problem #prob:B54 title="B5.4. Direct KSBA normalization theorem"}
Construct the classifying map, prove properness, finiteness, generic injectivity, and absence of further coarsening.
:::

::: {.problem #prob:B61 title="B6.1. Coble component classification"}
Classify all finite and affine component pairs, including equations, quotient involutions, branch curves, ramification divisors, and contractions.
:::

::: {.problem #prob:B71 title="B7.1. Complete boundary theorem"}
List every Type II and Type III stable Coble surface and prove compatibility with the Baily--Borel and semitoroidal incidence diagrams.
:::

#### Advantages and principal difficulties {#sec-strategy-B-assessment}

The autonomous strategy has three advantages.

1. The arithmetic group is defined geometrically rather than inherited.

2. Relevance and the stable divisor are intrinsic to Coble pairs.

3. The final comparison with Enriques moduli becomes a discrete rigidity theorem rather than part of every local construction.

Its principal difficulties are equally clear: direct monodromy, complete Vinberg calculations, algebraic realization of the fixed exceptional curve in degenerations, and a Coble-specific recognizable-divisor theorem.

### Strategy C: direct K3-to-Coble folding or reflection twisting {#sec-strategy-folding}

#### Candidate mechanism {#sec-strategy-C-mechanism}

The identity $I_{\Co}=w_\alpha I_{\mathrm{En}}$ suggests that the Coble theory can be obtained from the ambient K3 involution space by a direct reflection-twisted folding, rather than by first folding to Enriques and then slicing by $\alpha^\perp$.

At a cusp, the candidate operation is $J_{\Co}=w_{\bar\alpha}J_{\mathrm{En}}$.

#### Required chain {#sec-strategy-C-chain}

::: {.problem #prob:C1 title="C1. Classification of admissible ambient actions"}
Classify involutions of the two reflective K3 cusp lattices whose fixed lattices have the Coble cusp types and whose full-lattice lifts preserve the labeled direct Coble data.
:::

::: {.problem #prob:C2 title="C2. Direct root-folding theorem"}
Classify all ambient root orbits under the direct Coble involution and prove that every negative folded vector is a Coble root and every Coble root arises in this way.
:::

::: {.problem #prob:C3 title="C3. Chamber-intersection theorem"}
Prove that intersection of an ambient K3 chamber with the direct Coble fixed subspace is a fundamental chamber for the direct Coble reflection group.
:::

::: {.problem #prob:C4 title="C4. Full-lattice and geometric realization theorem"}
Lift the cusp action to $L_{K3}$ and identify it with the geometric pair of involutions on divisor models.
:::

::: {.problem #prob:C5 title="C5. Comparison with the wall-link construction"}
Prove that the direct folded chamber agrees with the orthogonal link of the corresponding Enriques root wall after the comparison of labeled embeddings.
:::

#### Projection formula versus Coxeter diagram {#sec-strategy-C-failure}

The orthogonal-projection formula for selected walls does not prove the root converse, chamber completeness, or full-lattice lifting.
It gives wall-slice diagrams, not Coxeter diagrams.
Strategy C succeeds only if C1--C5 are proved.

### Strategy D: computation-first arithmetic and Vinberg analysis {#sec-strategy-computational}

#### Legitimate uses {#sec-strategy-D-legitimate}

Computation is well suited to the following tasks.

- verifying lattice signatures, discriminant groups, and primitive closures;

- computing centralizers of explicit lattice involutions;

- enumerating finite discriminant-form orbits once the integral stabilizer images are known;

- running Vinberg's algorithm in explicit cusp lattices;

- enumerating the parabolic and elliptic subdiagrams of an explicit diagram exhaustively;

- checking integral-affine polygon closure and involution symmetry;

- computing local invariant rings, divisor classes, and intersection numbers.

#### Invalid substitutions {#sec-strategy-D-invalid}

Computation does not replace the following parametric statements.

- A finite $O(A)$ orbit computation does not identify integral cusps.

- A Gram matrix does not prove that a root list is a complete simple system.

- A finite list of monodromy vectors does not prove an integral-affine realization theorem.

- A family of explicit curves does not prove coverage of the moduli space.

- A local quotient calculation does not identify the universal KSBA divisor.

### Strategy E: hybrid direct-open and inherited-boundary approach {#sec-strategy-hybrid}

A potentially efficient hybrid is to prove the direct open period and monodromy theorem first, then use the AEGS ambient stable family only to construct boundary models.
The comparison with the Heegner divisor is made at the open level before the boundary is analyzed.

The required chain is:

1. direct projective coverage and labeled rigidity;

2. equality of direct monodromy with the Heegner stabilizer group;

3. open-period factorization through $\mcf_{\mathrm{En},2}$;

4. restriction of the AEGS family to the direct period space identified in steps 1--3;

5. integral cusp and Vinberg calculations for the direct group;

6. normalized toroidal restriction and semitoroidal compatibility;

7. generic reconstruction/no-further-coarsening.

This strategy reduces duplication of integral-affine existence theorems but still requires all arithmetic and comparison steps.
It is not equivalent to simply declaring the Coble compactification to be a closed subspace of the AEGS compactification.

## Common errors, caveats, and dependency-sensitive warnings {#sec-footguns}

### Surface-theoretic warnings {#sec-surface-footguns}

::: {.warning #warn:coble-enriques title="Coble is not Enriques"}
The smooth resolution $\wV$ is rational and has non-torsion canonical class.
The singular surface $V^\sharp$ is $\bQ$-Calabi--Yau only after contracting the anti-bicanonical $(-4)$-curve.
Arguments using $K_Z$ torsion on an Enriques surface cannot be transferred to $\wV$.
:::

::: {.warning #warn:singularity-index title="order versus canonical index"}
The notation $\frac{1}{4}(1,1)$ records a quotient group of order $4$.
The Cartier index of the canonical class is $2$.
:::

::: {.warning #warn:normality title="normality versus boundary nonnormality"}
The generic $\frac{1}{4}(1,1)$ Coble quotient is normal.
Irreducible nonnormal stable surfaces can occur only through conductor self-identifications or other boundary phenomena.
:::

::: {.warning #warn:anticanonical-ramification title="anti-bicanonical curve versus stable divisor"}
The divisor $C\in|-2K_{\wV}|$ is the branch curve of the Coble cover on the resolution.
The stable divisor is $R^\sharp$, the descended del Pezzo ramification divisor.
The two are related by the crepant formula in @sec-canonical-contraction but are not equal.
:::

::: {.warning #warn:quasi-ample title="quasipolarization versus polarization"}
The natural degree-$2$ class on $\wV$ is orthogonal to $C$ and is not ample.
It becomes ample only after contracting the complete null locus.
Any moduli group that purports to remember an ample class on $\wV$ is using the wrong object.
:::

::: {.warning #warn:special-null title="special Heegner intersections"}
On the generic one-node locus, $C$ is the only null curve.
On higher Heegner intersections additional curves may be null and must also be contracted before the singular degree-$2$ polarization becomes ample.
:::

::: {.warning #warn:two-heegner title="Coble versus unigonal Heegner divisors"}
The Coble locus is the $(-2)$-Heegner arrangement associated with a fixed node and a $\frac{1}{4}(1,1)$ quotient.
The unigonal locus is a distinct $(-4)$-Heegner divisor whose projective model uses $\bP(1,1,2)$.
The two constructions must not be interchanged.
:::

::: {.warning #warn:ramification-source title="which involution defines the stable divisor"}
In AEGS and in the proposed Coble theory, the stable divisor is the divisorial fixed locus of the del Pezzo involution.
The Enriques involution is fixed-point free on the generic Enriques K3 cover, and the Coble involution fixes the exceptional curve only on the resolution.
Neither of these is the source of $R^\sharp$.
:::

::: {.warning #warn:quarter-not-ade title="the Coble singularity is not ADE"}
The singularity $\frac{1}{4}(1,1)$ is a non-Gorenstein cyclic quotient singularity.
ADE arguments apply only after passing to the canonical $A_1$ cover or to the resolution, and the boundary coefficients must be tracked through that passage.
:::

### Group and period warnings {#sec-group-footguns}

::: {.warning #warn:group-fiat title="group by fiat"}
The Hodge stabilizer image, centralizer image, congruence inverse image, and geometric monodromy group are distinct definitions; see @sec-four-groups.
Equality must be proved.
Choosing one definition because it makes the desired compactification statement true is circular.
:::

::: {.warning #warn:isometry-rigidity title="abstract isometry is not labeled rigidity"}
An isomorphism $T_{\Co}\cong I_{2,9}(2)$ does not determine the embedding into $L_{K3}$, the degree-$4$ class, the exceptional root, the second involution, or the chamber.
Strategy B requires the labeled rigidity theorem of @sec-labeled-lattice-data.
:::

::: {.warning #warn:domain-quotient title="domain inclusion versus quotient morphism"}
An inclusion of type-IV domains does not by itself descend to arithmetic quotients.
The groups must arise from compatible subgroups of a common orthogonal group.
This issue controls the diagram in @sec-period-diagram.
:::

::: {.warning #warn:direct-factorization title="direct construction versus Heegner theorem"}
A direct Coble period quotient inside the K3 involution space is a separate theorem until its group, labeled embedding, and universal family are shown to factor through the Enriques Heegner construction.
Strategy B must be followed by Target theorem B.
:::

::: {.warning #warn:cover-smoothing title="smoothing the cover versus smoothing the quotient"}
An arbitrary smoothing of the nodal K3 cover need not carry the node-fixing involution.
The explicit invariant $(4,4)$ family of @sec-equivariant-smoothing does give an equivariant smoothing; no general conclusion should be drawn without a family-level extension theorem.
:::

### Cusp and Coxeter warnings {#sec-cusp-footguns}

::: {.warning #warn:orbit-groups title="four orbit problems"}
Orbits under $O(T_{\Co})$, $O^+(T_{\Co})$, $\Gamma_{\Co,2}$, and $O(A_{T_{\Co}})$ can all differ.
A claim about one group cannot be transferred to another without an exact sequence, a stabilizer-image calculation, or an integral transitivity theorem.
:::

::: {.warning #warn:cusp-map title="cusp maps require embedded representatives"}
A permutation of cusp labels is not a proof of a Baily--Borel map.
One must exhibit an isotropic line or plane inside the common embedded lattice chain and compute its divisibility and arithmetic orbit in both groups.
:::

::: {.warning #warn:rectangles title="AEGS Figure 4 border types"}
The double-rectangle Enriques $1$-cusps are $12,13,14,15,245$; the single-rectangle cusps are $34,35,45,55$.
The former map to the segment-flipping quotient lattice $E_8(2)$ and cannot contain a $(-2)$ Coble root in the negative quotient.
:::

::: {.warning #warn:wall-slice title="wall slice is not Coxeter diagram"}
The construction in @sec-orthogonal-link gives an arrangement of restricted hyperplanes.
It becomes a Coxeter chamber only after root integrality, simplicity, completeness, and arithmetic-index statements are proved.
:::

::: {.warning #warn:parabolic-exhaustion title="parabolic inspection is not exhaustion"}
Type II rays are arithmetic orbits of maximal parabolic subdiagrams of the complete chamber.
Listing visually apparent affine subdiagrams is insufficient unless a Vinberg computation or classification proves that no others occur.
:::

::: {.warning #warn:gram title="square-diagram Gram entry"}
The black nodes $\alpha_{20}$ and $\alpha_{21}$ are joined by a thick edge and have inner product $4$, not $2$.
Any computation based on the latter value has the wrong rank.
:::

::: {.warning #warn:correct-ambient title="the correct reflective ambient space"}
The reflective cusp diagrams used by AEGS belong to the hyperelliptic degree-$4$ K3 involution space $\mcf_{(2,2,0)}$, not to the full quartic K3 moduli space $\mcf_4$.
Any direct folding strategy must explain its relation to $\mcf_{(2,2,0)}$ before using the ambient diagrams.
:::

### Integral-affine and stable-pair warnings {#sec-affine-footguns}

::: {.warning #warn:affine-algebraic title="affine symmetry versus algebraic involution"}
An involution of a dual complex predicts but does not prove an involution of the degeneration.
One must impose the correct limiting-period condition and choose invariant component and gluing moduli; see @sec-algebraic-extension.
:::

::: {.warning #warn:crossed-node title="crossed node"}
A crossed Coxeter node is not merely a diagram symmetry.
It includes a root reflection, forces the corresponding root coordinate to vanish, and is realized by an $I_1$--$I_1$ collision to an $I_2$ affine singularity.
:::

::: {.warning #warn:fixed-edge title="fixed affine edge need not support ramification"}
In the non-simple AEGS cusp, a fixed bottom edge has no support in the ramification polarization.
Coble relevance must likewise be read from the divisor package, not from fixed loci alone.
:::

::: {.warning #warn:dlt-stable title="dlt model versus stable model"}
The quotient dlt model can contain $R^\sharp$-trivial curves, components, and conductor strata.
The KSBA model is obtained only after the relative Proj of @sec-relative-proj.
:::

::: {.warning #warn:restrict-semifan title="restriction versus compactification of the restriction"}
The intersection of an ambient semifan with a Heegner subspace is not automatically the semitoroidal normalization of the Heegner closure.
The arithmetic, normalization, gluing, and no-further-coarsening statements of @sec-restriction-not-formal are indispensable.
:::

## Dependency graph for further work {#sec-dependency-graph}

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

## Consolidated status ledger {#sec-status-ledger}

The following table summarizes the present mathematical status.

| Item | Status | Controlling section |
| :--- | :--- | :--- |
| Local invariant $(4,4)$ node construction | established | @sec-invariant-system |
| Local $\frac{1}{4}(1,1)$ quotient | established | @sec-cover-quotient |
| Explicit equivariant smoothing | established for the projective family | @sec-equivariant-smoothing |
| Coverage of the complete Coble locus | required theorem | @sec-projective-coverage |
| $T_{\Co}\cong\langle2\rangle\oplus U(2)\oplus E_8(2)$ | established | @sec-orthogonal-complement |
| $S_{\Co}$ and reflection twist | established as lattice calculations | @sec-reflection-twist |
| Labeled embedding uniqueness | required theorem | @sec-labeled-lattice-data |
| Degree-$2$ class is quasipolarized on $\wV$ | established | @sec-resolved-diagram |
| $\lvert-2K_{\widetilde V}\rvert=\{C\}$ generically | established | @sec-anti-bicanonical |
| Stable divisor $R^\sharp$ and numerical formulas | established on the projective one-node locus | @sec-ramification-divisor |
| Open KSBA pair $(V^\sharp,\epsilon R^\sharp)$ | established fiberwise on the general locus | @sec-canonical-contraction |
| Direct moduli equivalence in families | required theorem | @sec-singular-moduli |
| Equality of four arithmetic groups | required theorem | @sec-four-groups |
| Full orthogonal stabilizer exact sequence | established lattice lemma | @sec-stabilizer-sequence |
| Unpolarized cusp count | established with standard lattice input | @sec-unpolarized-cusps |
| Polarized cusp count | not established | @sec-finite-shadow |
| Finite $O(A)$ orbit tables | established computation | @sec-finite-orbits |
| Unpolarized Coxeter chamber | established | @sec-unpolarized-coxeter |
| Polarized wall-slice arrangements | established computations | @sec-wall-slices |
| Polarized Coble Coxeter diagrams | not established | @sec-coxeter |
| Integral-affine Coble package | defined; realization open | @sec-coble-affine-package |
| Direct dlt and stable-model theorem | open | @sec-coble-dlt |
| Exact Coble semifans | open | @sec-direct-semifans |
| Normalization of the Heegner KSBA closure | target theorem | @sec-heegner-target |

: Consolidated status of the Coble compactification project. {#tbl-status-ledger}

## Computations {#sec-computational-record}

This section states calculations that apply once the corresponding parametric theorems are proved.

### Explicit invariant branch curve {#sec-explicit-curve}

On the affine chart $x_0=y_0=1$, consider the invariant polynomial

\[
\begin{aligned}
f(x,y)={}&29x^4y^4+23x^4y^2+19x^4
 +17x^3y^3+13x^3y\\
&+11x^2y^4+7x^2y^2+x^2
 +5xy^3+xy+3y^4+2y^2.
\end{aligned}
\]

Its quadratic part is $x^2+xy+2y^2$, with discriminant $-7$.
Gr\"obner-basis calculations on the four standard affine charts give one singular point, at $(0,0)$ on the displayed chart, and no singularities on the other charts.

::: {.remark title="What the calculation proves"}
This calculation proves nonemptiness of the open one-node invariant family.
It does not prove that the family is the complete Coble moduli space.
:::

### Lattice calculations {#sec-computational-lattices}

Symbolic Gram-matrix computations give:

- the signature and determinant of the displayed $T_{\Co}$ and $S_{\Co}$ decompositions;

- the eigenspaces of the reflection twist on an explicit model;

- the rank of the ambient square-diagram Gram matrix for $(\alpha_{20},\alpha_{21})=2$ and for $(\alpha_{20},\alpha_{21})=4$ (@sec-gram-correction).

::: {.remark title="What the calculation proves"}
These computations prove the listed facts for explicit lattice models.
They do not prove labeled embedding uniqueness or geometric monodromy.
:::

### Finite cusp computations {#sec-computational-cusps}

The finite-orbit data of @sec-finite-orbits and the enhanced star calculation are inputs to, not substitutes for, the integral cusp-lifting theorem.

::: {.remark title="What the calculation proves"}
The scripts compute orbits under explicitly specified finite matrix groups.
They do not identify those groups with the images of integral parabolic stabilizers.
:::

### Wall-slice computations {#sec-computational-slices}

The ambient Gram matrix of @sec-gram-correction gives the selected wall-link roots and the four candidate arrangements.
The scripts test root integrality for the displayed vectors and enumerate parabolic and elliptic subgraphs of the candidate graphs.

::: {.remark title="What the calculation proves"}
The scripts carry out the finite graph calculations for the input root list.
They do not prove that the list is a complete Vinberg simple system or that graph automorphisms equal arithmetic chamber automorphisms.
:::

## Appendix: candidate wall-slice arrangements {#sec-appendix-wall-slices}

This appendix gives the finite arrangements obtained by slicing selected AEGS Enriques chambers by selected white-root hyperplanes, with the Gram entry of @sec-gram-correction.
They are starting points for a direct Vinberg calculation.
They are not proved to be complete Coxeter diagrams.

White vertices below have square $-2$ and black vertices have square $-4$.
A double arrow denotes the non-simply-laced Coxeter edge between roots of unequal length; $==$ denotes a thick edge; and $\cdots$ denotes a dotted edge.

### Slice over the triangular ambient cusp {#sec-slice-2}

The arrangement $G_{\mathrm{slice}}^2$ has nine vertices.
The vertices $c_0,\ldots,c_7$ are black and $c_8$ is white.
Its edges are

\[
c_0-c_3,
\qquad
c_1-c_2-c_3-c_4-c_5-c_6-c_7\dto c_8.
\]

This arrangement agrees with the standard unpolarized chamber after a relabelling, but its identification with a polarized cusp requires the integral cusp theorem.

### First square-cusp slice {#sec-slice-3}

The white vertices are $c_0,c_7,c_8$ and the black vertices are $c_1,\ldots,c_6,c_9,c_{10}$.
The nonzero edges are

\[
c_0\dto c_1,
\qquad
c_0==c_8,
\]

\[
c_1-c_2-c_3-c_4-c_5-c_6\dto c_7,
\]

\[
c_3-c_9,
\qquad
c_7\dto c_{10},
\qquad
c_8\cdots c_{10}.
\]

### Second square-cusp slice {#sec-slice-4}

The white vertices are $c_5,c_7$ and all other displayed vertices are black.
The edges are

\[
c_0-c_1-c_2-c_3-c_4\dto c_5,
\]

\[
c_0-c_6\dto c_7,
\qquad
c_0-c_8,
\qquad
c_4-c_9.
\]

### Third square-cusp slice {#sec-slice-5}

The white vertices are $c_0,c_8,c_9,c_{10},c_{11}$ and the black vertices are $c_1,\ldots,c_7,c_{12}$.
The edges are

\[
c_0\dto c_1,
\qquad
c_0\dto c_7,
\qquad
c_0==c_{11},
\]

\[
c_1-c_2-c_3-c_4-c_5-c_6-c_7,
\]

\[
c_2\dto c_8,
\qquad
c_4\dto c_9,
\qquad
c_6\dto c_{10},
\]

\[
c_8\dto c_{12},
\qquad
c_{10}\dto c_{12},
\qquad
c_9==c_{11},
\qquad
c_{11}\cdots c_{12}.
\]

### Star-decorated plane orbits {#sec-discarded-cusp-calibration}

Decorate each totally singular plane by one of eight stars.
The resulting seven finite orbits can be matched with the labels

\[
245,\quad34,\quad45,\quad
35^{(2)},\quad35^{(6)},\quad
55^{(2)},\quad55^{(6)}.
\]

This matching is not a cusp assignment.
It assumes that the star action is the image of the integral parabolic stabilizer, which is not proved, and the label $245$ is incompatible with the necessary $(-2)$-class condition in @sec-possible-cusp-images.
The finite enhanced orbit calculation applies once the integral stabilizer image is known; until then the labels have no arithmetic meaning.

## Residual open points {#sec-residual-open-points}

1. The descent category of the degree-$2$ class on the singular Coble model---Cartier line bundle, reflexive sheaf, or numerical class in special families---is open and must be fixed as part of the direct moduli theorem.
   The generic projective model supports the stated numerical and ampleness properties.

2. The family-theoretic construction of the canonical cover and simultaneous resolution is not assumed.
   It is isolated in the cover--singular equivalence theorem (@prob:cover-singular-equivalence) and in the root-marked universal-family lemma of Strategy A (@prob:A2).

## Source map {#sec-source-map}

The following references indicate where the standard theories used in this report may be consulted.

- AEGS [@AEGS25] is the controlling model for the projective diagram, unique embedding chain, cusp folding, integral-affine quotient models, generalized Coxeter semifans, and the finite/no-further-coarsening step.

- Nikulin [@Nik80] is the primary source for even $2$-elementary lattices, discriminant forms, and primitive embeddings.

- Namikawa [@Nam85] and Sterk [@Ste91] control the Enriques period and cusp theory used in the Heegner strategy.

- Dolgachev--Kond\=o [@DK13] treat orthogonal modular descriptions of classical Coble surfaces.

- Vinberg [@Vin72; @Vin75] supplies the reflection-group algorithms and Coxeter theory.

- Alexeev--Engel and related work [@AE22; @AE23; @AEH21; @AET23; @ABE22] supplies recognizable divisors, integral-affine models, and semitoroidal normalizations of K3 moduli.

- Koll\'ar, Koll\'ar--Mori, Koll\'ar--Xu, and Birkar [@KM98; @Kol23; @KX20; @Bir23] supply the MMP and KSBA framework.

- Kulikov, Persson--Pinkham, Friedman--Scattone, Gross--Hacking--Keel, Engel, and Engel--Friedman [@Kul77; @PP81; @FS86; @GHK15a; @GHK15b; @Eng18; @EF21] supply the degeneration and integral-affine background.

- The Stacks Project [@Stacks] is a general reference for relative spectra, finite morphisms, normalization, descent, and family-theoretic language.

## Conclusion {#sec-conclusion}

The open geometry of the Coble compactification problem is governed by invariant nodal $(4,4)$ curves, a nodal K3 cover with two commuting involutions, the lattice $T_{\mathrm{Co}} \cong \langle2\rangle\oplus U(2)\oplus E_8(2)$, and the singular stable pair $(V^\sharp,\epsilon R^\sharp)$.

On the resolution, the degree-$2$ class is a quasipolarization, $|-2K|$ consists generically of one rational $(-4)$-curve, and the crepant dlt boundary is

\[
\frac{1+\epsilon}{2}C+\epsilon R_{\wV}.
\]

The principal unresolved issues are not the local quotient calculation or the basic lattice type.
They are the labeled embedding rigidity, equality with geometric monodromy, integral cusp lifting, complete Vinberg chambers, algebraic realization of the Coble affine package, intrinsic relevance of walls, and the comparison between the autonomous compactification and the normalized Enriques Heegner closure.

The autonomous strategy organizes these issues into direct Coble analogues of the AEGS theorem chain.
The Heegner strategy organizes them into arithmetic normalization, universal-family, and no-further-coarsening statements.
A complete proof may combine the two, but it must eventually identify their lattices, groups, divisors, cusp structures, semifans, and KSBA families as the same mathematical objects.

## References {.unnumbered}

::: {#refs}
:::
