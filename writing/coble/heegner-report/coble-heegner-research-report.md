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

## Introduction {#sec-introduction}

### Central compactification problem {#sec-central-problem}

Let $T_{\mathrm{En}} \cong U\oplus U(2)\oplus E_8(2)$ be the Enriques anti-invariant lattice in the AEGS degree-$2$ construction, and let $\alpha\in T_{\mathrm{En}}$ be a primitive vector with $\alpha^2=-2$.
The hyperplane $\bD(T_{\mathrm{En}})\intersect\alpha^\perp$ is the period domain of the Coble Heegner locus.
The final problem is to identify the normalization of the KSBA closure of that locus as an explicit semitoroidal compactification, including the arithmetic group, all Baily--Borel cusps, the cusp reflection chambers, the integral-affine and dlt models, the relevant semifans, and the toroidal versus strictly semitoroidal locus.

### Principal distinction between the two strategies {#sec-two-strategies}

There are two conceptually different ways to organize the proof.

1. **Heegner-restriction strategy.** Begin with the AEGS Enriques moduli problem and regard the Coble locus as the normalization of a fixed $(-2)$-Heegner component.
   The principal new work is to justify passage to arithmetic quotients, normalize the boundary restriction, solve the cusp lifting problem, identify the restricted semifans, and prove that the resulting KSBA family loses no moduli.

2. **Autonomous Coble strategy.** Define a direct moduli problem of K3 covers with a Coble involution, a commuting del Pezzo involution, a degree-$4$ class, and a distinguished exceptional root.
   Reproduce direct analogues of the AEGS period, cusp, Vinberg, integral-affine, dlt, recognizable-divisor, and semitoroidal theorems.
   Only after this independent theory is complete does one prove that it agrees with the Enriques Heegner construction.

The second strategy avoids using the Enriques compactification as a black box, but it creates a separate comparison theorem at the end.

The del Pezzo involution of the second strategy is an involution of the surface.
On the covers of the direct projective construction it exists and commutes with the Coble involution (@prop:tuple-of-the-construction).
On the covers of [@DK13, section 3], the isometry of $H^2(X,\ZZ)$ defined by the two isotropic summands of the polarization is not the action of an automorphism in the marking of the construction (@cor:no-del-pezzo-involution-coble-cover).

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
In the Coble setting, the natural class on $\wV$ is orthogonal to the anti-bicanonical $(-4)$-curve and is therefore not ample.
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

## The AEGS framework {#sec-aegs-framework}

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

Uniqueness up to $O(L_{K3})$ means that every embedding of $T_{\mathrm{En}}$ into $L_{K3}$ extending the chosen one differs by an isometry of $L_{K3}$, so no construction built from the chain can depend on a choice of primitive complement.
:::

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

::: {.proposition #prop:coble-and-unigonal-heegner-divisors title="The Coble divisor and the unigonal divisor"}
Let $\Gamma^K_{\mathrm{En}}=O(T_{\mathrm{En}})$, so that $\mcf_{(10,10,0)}=\bD(T_{\mathrm{En}})/\Gamma^K_{\mathrm{En}}$.

1. Up to $\Gamma^K_{\mathrm{En}}$ there is a unique $(-2)$-vector $\alpha\in T_{\mathrm{En}}$. The discriminant divisor $\Delta=\alpha^\perp\subset\bD(T_{\mathrm{En}})/\Gamma^K_{\mathrm{En}}$ parameterizes quotients of nodal K3 surfaces by an involution that fixes a node. These quotients are rational Coble surfaces with a $\frac{1}{4}(1,1)$ singularity.

2. There are two $\Gamma^K_{\mathrm{En}}$-orbits of $(-4)$-vectors $\beta\in T_{\mathrm{En}}$. The divisor of the vector with $\beta^\perp\cong\langle4\rangle\oplus U\oplus E_8(2)$ parameterizes nodal Enriques surfaces. The divisor of the other orbit parameterizes the unigonal Enriques surfaces, which are double covers of $\bP(1,1,2)$.

3. On the unigonal Heegner divisor of $\mcf_{\mathrm{En},2}$, the projective diagram of @sec-aegs-projective is replaced by the diagram with $(Y,L)=(\bP(1,1,2),\mathcal O(4))$, a singular quadric.

Items 1 and 2 are [@AEGS25, §2.3]. Item 3 is [@AEGS25, §2.2].
:::

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
:::

### Dimension and coverage {#sec-projective-coverage}

The projective invariant linear system has dimension $12$.
Imposing $a_{00}=0$ gives a hyperplane, and the connected centralizer of $\tau$ in $\Aut(Y)$ has dimension $2$.
Thus the expected moduli dimension is $12-1-2=9$.

The finite symmetry group permutes the four fixed points.

::: {.problem #prob:projective-coverage title="Required theorem (projective coverage and intrinsic reconstruction)"}
The quotient of the open nodal invariant $(4,4)$ locus by the full centralizer of $\tau$ is the complete direct moduli stack of generic degree-$2$ Coble data.
Equivalently, the projective diagram can be reconstructed intrinsically from the Coble pair, and the resulting period map has image the full relevant period-domain component.
:::

## The Coble lattice package {#sec-coble-lattices}

### The orthogonal complement lattice {#sec-orthogonal-complement}

Write $T_{\mathrm{En}} \cong U\oplus E(2)$ and $E=U\oplus E_8$.

Choose a standard basis $e,f$ of the first copy of $U$, and define $\alpha=e-f$ and $\eta=e+f$.

Then $\alpha^2=-2$, $\eta^2=2$, and $(\alpha,\eta)=0$.

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

*The eigenspaces over* $\bQ$. The involution $I_{\mathrm{En}}$ acts as $+1$ on $S_{\mathrm{En}}$ and as $-1$ on $T_{\mathrm{En}}$, and $w_\alpha$ fixes $\alpha^\perp$ and sends $\alpha\mapsto-\alpha$, so over $\bQ$ the composite $I_\Co = w_\alpha I_{\mathrm{En}}$ acts as $+1$ on $S_{\mathrm{En}}\oplus\bZ\alpha$ and as $-1$ on $\alpha^{\perp T_{\mathrm{En}}} = T_\Co$.

*The gluing, and the extension of the factors.* $S_\En\oplus T_\En\subseteq\lkt$ has index $2^{10}$ with the full graph gluing of its two discriminant forms; $I_\En$ acts trivially on $A_{S_\En}\oplus A_{T_\En}$ because the forms are $2$-elementary and $-\id$ is the identity there, so the gluing subgroup is preserved and $I_\En$ extends to an integral isometry of $\lkt$. And $w_\alpha(x) = x+(x\cdot\alpha)\alpha$ is integral on $\lkt$ because $x\cdot\alpha\in\bZ$ for $x\in\lkt$. Hence $I_\Co = w_\alpha I_\En\in\Orth(\lkt)$.

*The invariant lattice.* Write $y\in\lkt^{I_\Co}$ as $y = y_S+y_T$ over $\bQ$ with $y_S\in S_\En^\#$ and $y_T\in T_\En^\#$, possible because $S_\En$ is primitive. Then
$$I_\Co y = y_S - w_\alpha(y_T) = y_S - y_T - (y_T\cdot\alpha)\,\alpha,$$
so $y = I_\Co y$ forces $2y_T = -(y_T\cdot\alpha)\alpha$. Writing $y_T = q\alpha + r$ with $r$ in the $\alpha$-orthogonal part of $T_\En^\#$ gives $2r = 0$ and hence $r = 0$, so $y_T = q\alpha$; and testing $q\alpha\in T_\En^\#$ against the generator $e$ of the summand $U$ of $T_\En$ gives $q\,(\alpha\cdot e) = -q\in\bZ$, so $q\in\bZ$. Therefore
$$L_{K3}^{I_\Co = 1} = S_\En\oplus\bZ\alpha,$$
and the $(-1)$-eigenspace is $T_\Co$ by the same computation with the sign reversed.

*The type.* The summands $S_\En\cong U(2)\oplus E_8(2)$ and $\bZ\alpha\cong\langle-2\rangle$ are orthogonal, so the invariant lattice is $U(2)\oplus E_8(2)\oplus\langle-2\rangle$, of signature $(1,\ 1+8+1) = (1,10)$ (summing to the rank $11$), determinant $(-2)\det S_\En = 2048$ and discriminant group $(\bZ/2)^{11}$: the even $2$-elementary lattice $I_{1,10}(2)$. The invariant lattice and $T_\Co$ are mutually orthogonal complements in $\lkt$ of ranks $11+11 = 22$, and $S_\Co\oplus T_\Co$ has index $2^{11}$ there.

:::

::: {.example #ex:roots-of-t-en-outside-u title="roots of $T_\En$ outside $U$"}
Let $e,f$ be the isotropic basis of the summand $U$ of $T_\En = U\oplus U(2)\oplus E_8(2)$, with $e\cdot f = 1$, so that $\alpha = e-f$.
Since $E_8$ is negative definite, the vectors of square $-4$ in $E_8(2)$ are the $240$ roots of $E_8$.
For each such $v$ the vector $\beta = (e+f)+v$ has $\beta^2 = 2-4 = -2$, and $\beta\notin U$.
So $T_\En$ has vectors of square $-2$ outside $U$, and @cons:reflection-twist depends on the choice of $\alpha$.
:::

::: {.question #qst:twist-root-conjugacy title="conjugacy of reflection twists"}
Let $\beta\in T_\En$ be a vector of square $-2$.
Is the pair $(I_\En, w_\beta I_\En)$ conjugate to the pair $(I_\En, w_\alpha I_\En)$ by an isometry of $\lkt$?
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

::: {.problem #prob:coble-rigidity title="Required theorem (labeled Coble rigidity)"}
Any two tuples $\mathfrak L_{\Co,2}$ arising from the direct projective construction are conjugate by an element of $O(L_{K3})$ preserving the labels, the degree-$4$ class, the effective root, and the chosen chamber.
:::

This is stronger than uniqueness of a primitive embedding of $S_{\Co}$ into $L_{K3}$.
It is the Coble analogue of the AEGS embedding-rigidity lemma and is needed before any direct period quotient can be declared coordinate independent.

The tuple of the direct projective construction is @prop:tuple-of-the-construction.
On the one-node locus its labels are conjugate (@thm:a21-labels), and its chamber clause is @qst:chamber-clause-one-node.

::: {.lemma #lem:one-node-picard-rank title="the invariant lattices of a one-node member"}
Let $b$ be a one-node member of @prop:one-node-family.
Then
$$S_{\mathrm{dP},b}\subseteq S_{\Co,b}\subseteq\Pic(\widehat X_b),\qquad \rk S_{\mathrm{dP},b} = 3,\qquad \rk S_{\Co,b} = 11,$$
and in particular $\rk\Pic(\widehat X_b)\ge11$.
Moreover $S_{\Co,b}$ is an even $2$-elementary lattice of signature $(1,10)$ with invariants $(r,a,\delta) = (11,11,1)$, so $S_{\Co,b}\cong\latI_{1,10}(2)\cong S_\Co$.
:::

::: {.proof}
The ranks are part (5) of @prop:tuple-of-the-construction with $k=1$.
By part (4) of the same proposition $I_{\Co,b}$ is nonsymplectic, so it acts by $-1$ on $H^{2,0}(\widehat X_b)$ and on $H^{0,2}(\widehat X_b)$.
An $I_{\Co,b}$-invariant integral class is therefore orthogonal to $H^{2,0}\oplus H^{0,2}$, hence of type $(1,1)$, hence in $\Pic(\widehat X_b)$ by the Lefschetz $(1,1)$ theorem.
This gives $S_{\Co,b}\subseteq\Pic(\widehat X_b)$.

By @prop:det-saturation-del-pezzo, $S_{\mathrm{dP},b} = \langle e_b,f_b,[D_b]\rangle$, where $e_b$ and $f_b$ are the pullbacks of the two ruling classes of $Y=\PP^1\times\PP^1$.
The involution $\iota_\Co$ covers $\tau$, and $\tau$ acts by $[-1]$ on each factor, so $\tau$ fixes each ruling class and $I_{\Co,b}$ fixes $e_b$ and $f_b$.
The class $[D_b]=\alpha_b$ is fixed by $I_{\Co,b}$ by part (2) of @prop:tuple-of-the-construction.
Hence $S_{\mathrm{dP},b}\subseteq S_{\Co,b}$.

*The isometry class.*
$T(\widehat X_b) = \Pic(\widehat X_b)^\perp$ lies in $S_{\Co,b}^\perp$, on which $I_{\Co,b}$ acts by $-1$, and $\Pic(\widehat X_b)^{I_{\Co,b}} = S_{\Co,b}$ because $S_{\Co,b}\subseteq\Pic(\widehat X_b)$.
So @prop:nikulin-fixed-locus applies to $\widehat\iota_{\Co,b}$ with $M = S_{\Co,b}$: this lattice is $2$-elementary, and $r = 11$.
Its signature is $(1,10)$, because it contains $H_b$ with $H_b^2 = 4$ and lies in $\Pic(\widehat X_b)$, which is hyperbolic by the Hodge index theorem.
The fixed locus of $\widehat\iota_{\Co,b}$ is the single $(-2)$-curve $D_b$ (proof of part (5) of @prop:tuple-of-the-construction, with $k = 1$).
Since $r = 11$, the invariants are neither $(10,10,0)$ nor $(10,8,0)$, so @prop:nikulin-fixed-locus writes the fixed locus as $C^{(g)}+\Sum_{i=1}^{k'}R_i$; a single smooth rational curve forces $g = 0$ and $k' = 0$, that is $22-r-a = 0$ and $r = a$, so $a = 11$.
The coparity is $\delta = 1$, because $\delta = 0$ requires $p-q\equiv0\pmod4$ and here $p-q = -9$ (@thm:two-elementary-classification).
The lattice $\latI_{1,10}(2) = S_\Co$ is even and $2$-elementary with the same signature and invariants $(11,11,1)$ (@prop:coble-invariant-lattice), and both lattices are indefinite, so @thm:two-elementary-classification gives $S_{\Co,b}\cong S_\Co$.
:::

::: {.proposition #prop:one-node-period-image title="the period map of the one-node family"}
Let $B$ be the one-node locus of @prop:one-node-family.
Let $\Gamma_{\mathrm{lab}}\subseteq\Orth(T_\Co)$ be the image of the stabilizer in $\Orth(\lkt)$ of the labels $(S_\Co,S_{\mathrm{dP}},H,\alpha)$, and let
$$\mathcal P\colon B\too\Gamma_{\mathrm{lab}}\backslash\bD(T_\Co)$$
be the period map of the family.
Let $G$ be the stabilizer of the point $p$ of @prop:one-node-family in the centralizer of $\tau$ in $\Aut(Y)$.
Then:

1. the fibres of $\mathcal P$ are the $G$-orbits in $B$;
2. the image of $\mathcal P$ contains a nonempty Zariski-open subset of a component of $\Gamma_{\mathrm{lab}}\backslash\bD(T_\Co)$, and the differential of $\mathcal P$ has rank $9$ on a dense open subset of $B$;
3. $\Pic(\widehat X_b) = S_{\Co,b}$ for a very general $b\in B$.
:::

::: {.proof}
*The map.* By part (4) of @prop:tuple-of-the-construction, $I_{\Co,b}$ is nonsymplectic, so $H^{2,0}(\widehat X_b)\subseteq T_{\Co,b}\otimes\bC$.
By @cor:construction-monodromy the monodromy of the family preserves the labels, so a marking that carries the labels of $\widehat X_b$ to $(S_\Co,S_{\mathrm{dP}},H,\alpha)$ is defined up to the stabilizer of the labels, and the period of $\widehat X_b$ is a point of $\bD(T_\Co)$ defined up to $\Gamma_{\mathrm{lab}}$.
The family is smooth and proper over the smooth quasi-projective variety $B$, so $\mathcal P$ is holomorphic and lifts locally to $\bD(T_\Co)$.
The group $\Gamma_{\mathrm{lab}}$ is arithmetic, being the image of the stabilizer of lattice data, so $\Gamma_{\mathrm{lab}}\backslash\bD(T_\Co)$ is quasi-projective.
After passage to a neat subgroup of finite index and the corresponding finite étale cover of $B$, Borel's extension theorem [@Bor72] makes $\mathcal P$ algebraic.

*The fibres.* Let $b,b'\in B$ with $\mathcal P(b) = \mathcal P(b')$.
Then there is a Hodge isometry $g\colon H^2(\widehat X_b,\bZ)\to H^2(\widehat X_{b'},\bZ)$ that carries the labels of $b$ to the labels of $b'$.
Each involution acts by $+1$ on its invariant lattice and by $-1$ on the orthogonal complement, so $g$ intertwines the involutions of $b$ and $b'$.
Let $\sigma\colon\widehat Y=\Bl_{p_0}Y\to Y$ be the blow-up and $e$ its exceptional curve.
By part (1) of @lem:face-at-H, $\alpha_b = \widehat\pi_b^*e$, and $H_b = \widehat\pi_b^*\sigma^*\OO_Y(1,1)$, so
$$2H_b-\alpha_b = \widehat\pi_b^*\bigl(\sigma^*\OO_Y(2,2)-e\bigr) = \widehat\pi_b^*(-K_{\widehat Y}).$$
The surface $\widehat Y$ is a del Pezzo surface of degree $7$, so $-K_{\widehat Y}$ is ample, and $\widehat\pi_b$ is finite, so $2H_b-\alpha_b$ is ample.
The isometry $g$ carries $2H_b-\alpha_b$ to the ample class $2H_{b'}-\alpha_{b'}$, so by the strong Torelli theorem [@BHPV04, Ch. VIII, Thm. 11.1] $g = \varphi^*$ for an isomorphism $\varphi\colon\widehat X_{b'}\to\widehat X_b$.
The action of the automorphism group of a K3 surface on its second cohomology is faithful, so $\varphi$ conjugates $\widehat\iota_{\mathrm{dP},b'}$ to $\widehat\iota_{\mathrm{dP},b}$ and $\widehat\iota_{\Co,b'}$ to $\widehat\iota_{\Co,b}$.
So $\varphi$ descends to an automorphism of $\widehat X_b/\widehat\iota_{\mathrm{dP},b} = \widehat Y$ that commutes with $\tau$, carries the branch curve of $b'$ to the branch curve of $b$, and preserves $e$ because $g(\alpha_b)=\alpha_{b'}$.
It therefore descends to an element of $G$ that carries $b'$ to $b$.
Conversely, an element of $G$ that carries $b'$ to $b$ lifts to an isomorphism $\widehat X_{b'}\to\widehat X_b$ that commutes with both involutions and preserves $H$ and $\alpha$, so $\mathcal P(b) = \mathcal P(b')$.
This proves (1).

*The image.* The identity component of the centralizer of $\tau$ in $\Aut(Y)$ is the product of the diagonal tori of the two factors $\mathrm{PGL}_2$, which fixes each $\tau$-fixed point.
So $\dim G = 2$, and by (1) every fibre of $\mathcal P$ has dimension at most $2$.
By @prop:one-node-connected, $B$ is a nonempty open subset of a projective space of dimension $11$, so the closure of the image of $\mathcal P$ has dimension at least $11-2 = 9$.
The target has dimension $\rk T_\Co-2 = 9$, so the closure of the image is a component of the target.
By Chevalley's theorem the image is constructible, so it contains a nonempty Zariski-open subset of that component.
By generic smoothness in characteristic $0$, the differential of $\mathcal P$ has rank $9$ on a dense open subset of $B$.
This proves (2).

*The very general member.* Let $v\in T_\Co$ be nonzero.
The set $\bD(T_\Co)\cap v^\perp$ has dimension $8$, so by (2) the set of $b\in B$ whose period is orthogonal to a $\Gamma_{\mathrm{lab}}$-translate of $v$ is a proper closed analytic subset of the irreducible variety $B$.
There are countably many $v$, so a very general $b$ lies in none of these subsets, and for such $b$ no nonzero class of $T_{\Co,b}$ is orthogonal to $H^{2,0}(\widehat X_b)$, that is, $T_{\Co,b}\cap\Pic(\widehat X_b) = 0$.
Let $x\in\Pic(\widehat X_b)$.
The automorphism $\widehat\iota_{\Co,b}$ preserves $\Pic(\widehat X_b)$, so $x-I_{\Co,b}x$ lies in $T_{\Co,b}\cap\Pic(\widehat X_b) = 0$, and $x\in S_{\Co,b}$.
With @lem:one-node-picard-rank this gives $\Pic(\widehat X_b) = S_{\Co,b}$.
This proves (3).
:::

::: {.question #qst:chamber-clause-one-node title="the chamber clause on the one-node locus"}
Are there one-node members $b,b'$ such that no isometry of $\lkt$ that carries the labels of $b$ to the labels of $b'$ carries the chamber of the tuple at $b$ to the chamber of the tuple at $b'$?
:::

::: {.question #qst:del-pezzo-saturation-higher-k title="the del Pezzo invariant lattice for several nodes"}
Let the branch curve have $k\ge2$ ordinary nodes at $\tau$-fixed points and be otherwise smooth.
Is $S_{\mathrm{dP}} = \pi^*\Pic(Y)\perp\ZZ D_1\perp\cdots\perp\ZZ D_k$?
:::

::: {.proposition #prop:twist-pair-not-construction-pair title="the pair $\{I_\En,I_\Co\}$ is not the pair of a one-node member"}
Let $b$ be a one-node member.
No isometry of $\lkt$ conjugates the set $\{I_\En,I_\Co\}$ of @cons:reflection-twist to the set $\{I_{\Co,b},I_{\mathrm{dP},b}\}$.
:::

::: {.proof}
For commuting involutions $A,A'$ of $\lkt$ and signs $\epsilon,\epsilon'\in\{\pm1\}$, let $r_{\epsilon\epsilon'}(A,A')$ be the rank of the subspace of $\lkt\otimes\bQ$ on which $A$ acts by $\epsilon$ and $A'$ acts by $\epsilon'$.
A conjugation preserves these four ranks, and exchanging $A$ and $A'$ exchanges $r_{+-}$ and $r_{-+}$.
So the multiset of the four ranks is an invariant of the set $\{A,A'\}$ under conjugation.

The involutions $I_\Co$ and $I_\En$ commute, because $I_\En(\alpha) = -\alpha$.
By @prop:coble-eigenspaces, over $\bQ$ the involution $I_\Co$ acts by $+1$ on $S_\En\oplus\bZ\alpha$ and by $-1$ on $T_\Co$, and $I_\En$ acts by $+1$ on $S_\En$ and by $-1$ on $\bZ\alpha\oplus T_\Co\subseteq T_\En$.
So
$$\bigl(r_{++},r_{+-},r_{-+},r_{--}\bigr)(I_\Co,I_\En) = (10,1,0,11).$$

For the member $b$, @lem:one-node-picard-rank gives $\rk S_{\mathrm{dP},b} = 3$, $\rk S_{\Co,b} = 11$ and $S_{\mathrm{dP},b}\subseteq S_{\Co,b}$.
So $r_{++} = \rk S_{\mathrm{dP},b} = 3$, $r_{+-} = 11-3 = 8$, $r_{-+} = 0$ because the $(+1)$-eigenspace of $I_{\mathrm{dP},b}$ lies in that of $I_{\Co,b}$, and $r_{--} = 22-11 = 11$:
$$\bigl(r_{++},r_{+-},r_{-+},r_{--}\bigr)(I_{\Co,b},I_{\mathrm{dP},b}) = (3,8,0,11).$$
The multisets $\{10,1,0,11\}$ and $\{3,8,0,11\}$ differ.
:::

::: {.question #qst:reflected-pair-conjugacy title="the reflected pair"}
Let $I_{\mathrm{dP}}$ be the del Pezzo involution of [@AEGS25], and suppose that $w_\alpha I_{\mathrm{dP}}$ is an involution that commutes with $w_\alpha I_\En$.
For a one-node member $b$, is there $g\in\Orth(\lkt)$ with
$$g\,(w_\alpha I_\En)\,g^{-1} = I_{\Co,b},\qquad g\,(w_\alpha I_{\mathrm{dP}})\,g^{-1} = I_{\mathrm{dP},b},\qquad g(H) = H_b,\qquad g(\alpha) = \alpha_b?$$
:::

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
\qquad\text{so } p_a(R_{\wV})=4.
$$

The divisor $R_{\wV}$ is not the anti-bicanonical curve $C$.
It is the divisor relevant to the KSBA polarization.
:::

::: {.corollary #cor:resolved-coble-canonical-not-torsion title="The canonical class of $\wV$ is not torsion"}
The canonical class $K_{\wV}$ is not a torsion class in $\Pic(\wV)$.
:::

::: {.proof}
By @prop:ramification-numerics, $K_{\wV}\cdot R_{\wV}=-1$.
A torsion class is numerically trivial, so its intersection number with every divisor is $0$.
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
The group $\Gamma_\Co$ of @def:gamma-co-groups is conjecturally $\widetilde\Orth^+(T_\Co)$ (@conj:gamma-co-stable); no relation between $\Gamma_{\Co}^{\mathrm{dir}}$ and $\Gamma_\Co$ is established.
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

With $\alpha$ the vector $\delta$ of @lem:coble-heegner-vector, $\Gamma^{\mathrm{Hdg}}_{\Co,2}$ is the group $\Gamma^{\mathrm{Hdg}}_\Co$ of @prop:gamma-co-in-heegner-group.
The images of $\Gamma^{\mathrm{Hdg}}_{\Co,2}$ and $\Gamma^{\mathrm{cong}}_{\Co,2}\intersect\Orth^+(T_\Co)$ in $\Orth(q_{T_\Co})$, their indices over $\widetilde\Orth^+(T_\Co)$, and the condition under which the two groups coincide are @prop:gamma-cong-eq-heegner.

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
The classes of $q$-value $\tfrac12$ modulo $\ZZ$ form the coset $\overline{h} + A^0$, of order $2^{10}$, so the value of $q$ alone does not determine $\overline{h}$.
So $g$ preserves the gluing subgroup $H$ of @thm:nikulin-gluing determined by the primitive vector $\eta$, and hence extends to the overlattice: by the gluing criterion, isometries of the two summands preserving $H$ glue to an isometry of the overlattice.
The two choices of sign of the action on the line $\ZZ\alpha$ are the two extensions, and both lie in $O^+(T_{\En})$ because $\alpha$ is negative and the positive plane is untouched.

*The kernel.*
The kernel of the restriction is the subgroup of $\Stab_{O^+(T_{\En})}(\bZ\alpha)$ acting trivially on $\alpha^{\perp}$.
Such an isometry preserves $\alpha$ (the stabilizer condition) and the whole of $T_{\Co}$, and acts trivially there; it therefore acts by a scalar on the rank-one complement $\bZ\alpha$, and being an isometry with $\alpha^2=-2$ the only scalars are $\pm1$.
The scalar $+1$ is the identity, and the scalar $-1$ is the reflection $w_\alpha$ in the root $\alpha$.
So the kernel is $\langle w_\alpha\rangle$, of order $2$.
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
By @prop:tco-as-twist, $T_\Co=I_{2,9}(2)$, so $O^+(T_\Co)=O^+(I_{2,9})$ and the two lattices have the same
primitive isotropic lines and planes. Transitivity on lines is @lem:I29-plus-line-transitivity, and on
planes it is @thm:plane-transitivity-tco. The quotients are given by @cor:tco-isotropic-splitting.
:::

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

### Orbits in the finite quadratic space {#sec-finite-orbits}

::: {.example #ex:gco-finite-orbits title="Orbits of $G_\Co$ on singular vectors and totally singular planes"}
By @lem:gco-orbit-transfer, the isotropic classes of $A_{T_\Co}$ are those of the summand $A_{S_\En} = A_{U(2)}\perp A_{E_8(2)}$, and by @thm:coble-heegner-finite-orbits the group $G_\Co$ acts there as $P = \Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$.
Write a class as $(a,y)$ with $a\in A_{U(2)} = \{0,[u_0/2],[w_0/2],[h/2]\}$ and $y\in E_8/2E_8$, and identify the values $0,\tfrac12$ of the bilinear form with $\bF_2$.
The form $q_{U(2)}$ takes the values $0,0,1$ on $[u_0/2],[w_0/2],[h/2]$, and two distinct nonzero classes of $A_{U(2)}$ pair to $1$.
The form $q_{E_8(2)}$ is a nondegenerate plus-type form on the $8$-dimensional space $E_8/2E_8$, with $135$ nonzero singular vectors and $120$ nonsingular vectors.

*Vectors.* By part (2) of @thm:coble-heegner-finite-orbits, the nonzero isotropic classes fall into four $P$-orbits:

- type $A$: $(0,s)$ with $s$ nonzero singular, $135$ classes;
- type $B$: $([u_0/2],0)$ and $([w_0/2],0)$, $2$ classes;
- type $C$: $([u_0/2],s)$ and $([w_0/2],s)$ with $s$ nonzero singular, $270$ classes;
- type $D$: $([h/2],t)$ with $t$ nonsingular, $120$ classes.

*Planes.* The type of an order-$4$ isotropic subgroup lists the types of its three nonzero classes.
Two classes of type $B$ pair to $1$, and so do a class of type $B$ and a class of type $C$ or $D$ with a different $U(2)$-coordinate.
A sum of two classes of type $C$ with the same $U(2)$-coordinate has type $A$, and with different $U(2)$-coordinates has type $D$; a sum of two classes of type $D$ has type $A$.
So the possible types are $AAA$, $ABC$, $ACC$, $ADD$ and $CCD$.
For a nonzero singular $s\in E_8/2E_8$, the space $s^\perp/\bF_2s$ is a nondegenerate plus-type space of dimension $6$, with $36$ singular and $28$ nonsingular vectors; so $s^\perp$ contains $72$ singular and $56$ nonsingular vectors, and $136-72 = 64$ nonzero singular vectors $t$ have $b(s,t) = 1$.
The counts are:

- $AAA$: totally singular planes of $E_8/2E_8$; there are $135\cdot70$ ordered pairs $(s,t)$ of distinct nonzero orthogonal singular vectors, and each plane has $6$ ordered bases, so there are $1575$;
- $ABC$: $\{([u_0/2],0),(0,s),([u_0/2],s)\}$ and its image under $u_0\leftrightarrow w_0$, so $2\cdot135 = 270$;
- $ACC$: $\{(0,s),(a,t),(a,s+t)\}$ with $a\in\{[u_0/2],[w_0/2]\}$ and $\langle s,t\rangle$ totally singular, determined by $a$, the plane $\langle s,t\rangle$ and the element $s$ of it, so $2\cdot1575\cdot3 = 9450$;
- $ADD$: $\{(0,s),([h/2],t),([h/2],s+t)\}$ with $s$ nonzero singular and $t\in s^\perp$ nonsingular, so $135\cdot56/2 = 3780$;
- $CCD$: $\{([u_0/2],s),([w_0/2],t),([h/2],s+t)\}$ with $s,t$ singular and $b(s,t) = 1$, so $135\cdot64 = 8640$.

The sum is $23\,715$, the number of order-$4$ isotropic subgroups of @prop:coble-planecusp-finite.
Within each type, Witt's extension theorem for $q_{E_8(2)}$, together with the swap $u_0\leftrightarrow w_0$ in $\Orth(q_{U(2)})$, makes $P$ transitive, so each type is one orbit.
The sizes are @tbl-finite-vector-orbits and @tbl-finite-plane-orbits.
:::

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

::: {.definition #def:plane-star title="Stars of an order-$4$ isotropic subgroup"}
Let $J$ be an order-$4$ isotropic subgroup and let $V = J^{\perp}/J$, the perpendicular taken in $A_{S_\En}$.
A **star** of $J$ is a set of seven nonsingular vectors of $V$ that are pairwise non-orthogonal.
:::

::: {.lemma #lem:plane-stars title="Stars and the plane orbits over $J$"}
Let $J$ be an order-$4$ isotropic subgroup and $F = \Stab_{\Orth(q)}(J)$.

1. $J$ has eight stars, and $F$ permutes them transitively.
2. For a primitive isotropic plane $P$ with $J(P) = J$, the group $\rho(\Stab_{\Orth(B)}(P))$ is the stabilizer in $F$ of exactly one star $s(P)$, and $s(gP) = \rho(g)\,s(P)$ for $g\in\Orth(B)$.
3. The map $P\mapsto s(P)$ induces a bijection from the eight $\ker\rho$-orbits of primitive isotropic planes over $J$ onto the eight stars of $J$.
:::

::: {.proof}
In the coordinates of @thm:coble-plane-stabilizer-image(4), $V$ is the six-dimensional plus-type space $V_6$ of even-weight classes $\sum c_i\bar d_i$, and $\beta(x,y)$ is the parity of the number of common coordinates.
The nonsingular vectors of $V_6$ are the $21$ classes of weight $2$ and the $7$ classes of weight $6$.
The weight-$6$ classes form a star $s_0$; for each $i$, the six classes $\bar d_i+\bar d_j$ with $j\neq i$ and the weight-$6$ class without $\bar d_i$ form a star $s_i$; these are the eight stars.
The stabilizer $F = \Stab_{\Orth(q)}(J)$ acts on them through its Levi quotient $\Orth^+(6,2)\cong S_8$.
The image $S = \rho(\Stab_{\Orth(B)}(P))$ of the standard plane acts on $V_6$ through the coordinate permutations $S_7$, because its unipotent radical acts trivially on $J^{\perp}/J$; so $S$ fixes $s_0$ and permutes $s_1,\dots,s_7$ transitively.
The group $F$ is transitive on the stars: otherwise $S_8$ fixes $s_0$ and acts transitively on the other seven, but every homomorphism $S_8\to S_7$ has image of order at most $2$.
Since $[F:S] = 8$, the group $S$ is the stabilizer of $s_0$.
So each primitive isotropic plane $P$ determines one star $s(P)$ of $J(P)$, the star fixed by $\rho(\Stab_{\Orth(B)}(P))$, and $s(gP) = \rho(g)\,s(P)$.
Over each $J$, the map $P\mapsto s(P)$ is a bijection from the eight $\ker\rho$-orbits of planes (@thm:coble-plane-stabilizer-image(5)) onto the eight stars: if $s(gP) = s(P)$ with $\rho(g)\in F$, then $\rho(g) = \rho(h)$ for some $h\in\Stab_{\Orth(B)}(P)$, and $gP = (gh^{-1})P$ with $gh^{-1}\in\ker\rho$.
:::

::: {.theorem #thm:cusp-lifting title="Integral cusp lifting"}
Let $\Gamma$ be a group with $\ker\rho_{T_\Co}\subseteq\Gamma\subseteq\Orth(T_\Co)$, and let $H = \rho_{T_\Co}(\Gamma)$.

1. The map $\Gamma v\mapsto[v/2]$ is a bijection from the $\Gamma$-orbits of primitive isotropic vectors of $T_\Co$, which are also its orbits of primitive isotropic lines, onto the $H$-orbits of nonzero isotropic classes of $A_{T_\Co}$.
2. The map $\Gamma P\mapsto H\cdot(J(P),s(P))$ is a bijection from the $\Gamma$-orbits of primitive isotropic planes onto the $H$-orbits of pairs $(J,s)$ of an order-$4$ isotropic subgroup $J$ and a star $s$ of $J$.
3. The map $\Gamma(L\subset P)\mapsto H\cdot(J(P),s(P),[v_L/2])$, with $v_L$ a primitive vector of $L$, is a bijection from the $\Gamma$-orbits of flags of a primitive isotropic line in a primitive isotropic plane onto the $H$-orbits of triples $(J,s,c)$ with $c$ a nonzero element of $J$.
4. Parts 1–3 hold with $\Gamma\intersect\Orth^+(T_\Co)$ in place of $\Gamma$.

For $\widetilde\Orth^+(T_\Co) = \ker\rho_{T_\Co}\intersect\Orth^+(T_\Co)$ the three counts are $527$, $8\cdot 23\,715 = 189\,720$ and $3\cdot 189\,720 = 569\,160$.
For $\rho_{T_\Co}^{-1}(G_\Co)$ they are $4$, $7$ and $13$.
:::

::: {.proof}
Since $\ker\rho\subseteq\Gamma$, each part reduces to the $\ker\rho$-orbits over a fixed finite datum.
Part 1: every nonzero isotropic class is $[v/2]$ for a primitive isotropic $v$, the zero class is not, and $\rho(\Stab_{\Orth(B)}(v)) = \Stab_{\Orth(q)}([v/2])$ (@lem:isotropic-classes-lift, @lem:cusp-vector-stabilizer-image(1)), so each fibre is one $\ker\rho$-orbit; since $-\id\in\ker\rho$, vector orbits are line orbits.
Part 2 is @lem:plane-stars(3).
Part 3: two flags with the same triple lie on planes in one $\ker\rho$-orbit by part 2, and with the plane fixed, the line action of $\Stab_{\widetilde\Orth^+(T_\Co)}(P)$ in the proof of @prop:coble-arithmetic-flag-incidence carries one line of class $c$ to the other.
Part 4: the spinor witnesses of @lem:cusp-vector-stabilizer-image(2) and @thm:coble-plane-stabilizer-image(5) lie in $\ker\rho$, lie outside $\Orth^+(T_\Co)$, and stabilize the vector and the plane, and so do their conjugates; so no orbit splits.
For $\widetilde\Orth^+(T_\Co)$ the group $H$ is trivial.
For $\rho^{-1}(G_\Co)$ the counts are the orbit numbers of @tbl-finite-vector-orbits and of $G_\Co$ on pairs $(J,s)$, of sizes $2160, 3150, 7560, 9450, 22680, 69120, 75600$, and on triples $(J,s,c)$.
:::

### Necessary restrictions on maps to Enriques cusps {#sec-possible-cusp-images}

::: {.proposition #prop:possible-cusp-images title="Enriques cusps that can contain Coble cusps"}
Let $e$ be a primitive isotropic line and $J$ a primitive isotropic plane of $T_\Co = \alpha^{\perp}_{T_\En}$, viewed in $T_\En$.

1. The lattice $e^{\perp T_\En}/e$ has a vector of square $-2$. So in the AEGS numbering the Enriques $0$-cusp of $e$ is not cusp $1$, and it is one of $2,3,4,5$.
2. The lattice $J^{\perp T_\En}/J$ has a vector of square $-2$. So the Enriques $1$-cusp of $J$ is not one of the double-rectangle cusps $12,\ 13,\ 14,\ 15,\ 245$, and it is one of $34,\ 35,\ 45,\ 55$.
:::

::: {.proof}
The sublattice $T_\Co$ is primitive in $T_\En$, being an orthogonal complement, so $e$ and $J$ are primitive and isotropic in $T_\En$. Since $e, J\subset\alpha^{\perp}$, the root $\alpha$ lies in $e^{\perp T_\En}$ and in $J^{\perp T_\En}$. Adding an isotropic vector orthogonal to $\alpha$ does not change $\alpha^2$, so the class of $\alpha$ in each quotient has square $-2$.
The hyperbolic lattice of the Enriques $0$-cusp $1$ has all norms divisible by $4$, so it has no vector of square $-2$.
The double-rectangle cusps $12,\ 13,\ 14,\ 15,\ 245$ lie over the segment-flipping $1$-cusp, whose negative quotient is $E_8(2)$ [@AEGS25, Fig. 4], and $E_8(2)$ has all norms divisible by $4$.
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
It does not imply that $b_{\operatorname{link}}$ is a root of the orthogonal lattice.

### Candidate reflection twist at a cusp {#sec-cusp-reflection-twist}

At the full K3-lattice level one has the reflection twist $I_{\Co}=w_\alpha I_{\mathrm{En}}$.
If a primitive isotropic line $e$ is orthogonal to $\alpha$, the involutions induce actions on the cusp quotient $e^\perp/e$.
This suggests the cusp-level candidate $J_{\Co}=w_{\bar\alpha}J_{\mathrm{En}}$, where $\bar\alpha$ is the image of $\alpha$ in the cusp lattice.

This formula is not yet a direct folding theorem.
One must prove that the cusp action lifts through the full discriminant gluing and corresponds to the geometric involution, just as AEGS separately prove their lifting lemma.

### Gram data of the square K3 cusp diagram {#sec-gram-correction}

In the square K3 cusp diagram of AEGS, the two black roots $\alpha_{20}$ and $\alpha_{21}$ both have square $-4$.
The edge joining them is thick.
Therefore $(\alpha_{20},\alpha_{21})=4$.

The value $2$ gives a Gram matrix of rank $20$, incompatible with the rank-$18$ cusp lattice.
The value $4$ gives the correct rank $18$.

### Candidate wall-slice diagrams {#sec-wall-slices}

With the Gram entry of @sec-gram-correction, intersect selected Enriques chambers with selected white-root hyperplanes.
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
Whether the displayed walls form a complete simple system is @prob:coxeter-completeness.

::: {.problem #prob:coxeter-completeness title="Required theorem (Coble Vinberg and root completeness)"}
For every polarized Coble $0$-cusp:

1. determine the arithmetic cusp lattice and the image of its stabilizer;

2. run Vinberg's algorithm or prove a two-sided root-link theorem;

3. prove that the resulting simple roots define a fundamental chamber;

4. compute the chamber automorphism group and reflection index; and

5. enumerate all maximal parabolic and elliptic subdiagrams modulo the full arithmetic group.
:::

The reflections of $T_\Co$ that lie in $\widetilde\Orth^+(T_\Co)$ are given by @prop:gamma-co-reflective-set, and the index in $\widetilde\Orth^+(T_\Co)$ of the group they generate is @qst:gamma-co-generators.

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

### Heegner-wall specialization of an AEGS integral-affine model {#sec-heegner-affine-specialization}

Suppose a degeneration lies in the $\alpha$-Heegner locus and approaches a Type III cusp represented by $e$.
After a suitable marking and base change, one expects $(\alpha,e)=0$ and $(\alpha,\lambda)=0$.

If $\alpha$ is represented by a visible path in the chosen integral-affine model, the second equation says that the path has zero affine length.
The corresponding pair of parallel $I_1$ singularities coalesces to an $I_2$ singularity.
This is the same local operation used by AEGS for crossed nodes, but in the Coble problem it records the persistent $A_1$ singularity of the K3 cover.

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

After contracting $\mcc$ to the singular Coble family, its agreement with the relative Proj for a sufficiently divisible multiple of $\mcr^\sharp$ is @prob:stable-proj.

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

## Adapting AEGS examples {#sec-example-status}

::: {.proposition #prop:aegs-nonsimple-mirror-bottom-edge title="The non-simple mirror cusp $(18,0,0)_1$"}
The $0$-cusp $(18,0,0)_1$ of $\mcf_{(2,2,0)}$ corresponds to a non-simple mirror of $\mcf_{(2,2,0)}$.
At this cusp the integral-affine polarization $R_{\IA}\subset B(\ell)$ has no support on the bottom edge of the Symington polytope $P(\ell)$, and the ramification divisor $R_0$ is empty on the corresponding components of the central fiber $X_0$ [@AEGS25, §4.2].
:::

Three recipes adapt AEGS examples:

- start with the AEGS cusp-$3$ integral-affine model and impose one additional Coble-root equation;

- start with the cusp-$5$ model, where several crossed-root coordinates already vanish, and impose an independent Coble-root condition;

- start with the non-simple cusp-$2$ model and impose the appropriate white-root wall while retaining @prop:aegs-nonsimple-mirror-bottom-edge.

An example must specify the integral root, the visible path, the compatible triangulation, the component periods and gluings, the two algebraic involutions, all quotient singularities, and the final $R^\sharp$-trivial contraction.

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

At the one $0$-cusp of $F^{\mathrm{un}}_\Co$ the Coxeter part is a theorem: the chamber is that of @thm:coble-cusp-chamber and the Coxeter semifan of it is a fan with one Type II ray, @thm:coble-coxeter-semifan. What that theorem records as missing is the marking: the divisor of the Coble stable pair is not defined on the pages, so the generalized semifan is not formed there.

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

### Semitoroidal normalization after the semifan theorem {#sec-semitoroidal-after-restriction}

@thm:semifan-restriction is a statement about cone complexes and markings, not about the normalization of a Heegner closure. Its hypotheses are the conditions that must be checked to identify a restricted generalized Coxeter semifan; the assertions about branch saturation, arithmetic compatibility, normalization, and nonidentification of Coble branches are not consequences of it. For the Coble case, @thm:coble-restricted-semifan proves the cone and marking statements, leaving the following independent geometric problem.

::: {.problem #prob:restricted-semifan title="Required theorem (semitoroidal restriction)"}
After passage to a common toroidal refinement, prove that the normalization of the Heegner closure is obtained by saturated intersection with the Coble cusp subspaces, and that the induced semitoroidal contractions coincide with combinatorial constancy for the Coble stable-pair family.
:::

Without this theorem, the semifan identification does not by itself identify the normalized semitoroidal compactification.

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

5. the direct stable divisor agrees with the restriction of the AEGS ramification divisor $R_Z$; and

6. the direct semitoroidal compactification is the normalization of the KSBA closure of the Heegner divisor inside the AEGS compactification.
:::

Target theorem B is the comparison theorem of @sec-central-problem.
Target theorem A is a substantial independent theorem and an intermediate strategy, but it becomes a proof of the Heegner statement only after Target theorem B is established.

## Proof strategies and research programs {#sec-strategies}

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
Over the stack-theoretic normalization of the Heegner component, there is a universal family in which the fixed $A_1$ point, its simultaneous resolution after the required Weyl cover, the exceptional root, and the ramification divisor of the del Pezzo involution are compatible with base change.
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

The identity $I_{\Co}=w_\alpha I_{\mathrm{En}}$ suggests that the Coble theory can be obtained from the K3 involution space $\mcf_{(2,2,0)}$ by a direct reflection-twisted folding, rather than by first folding to Enriques and then slicing by $\alpha^\perp$.

At a cusp, the candidate operation is $J_{\Co}=w_{\bar\alpha}J_{\mathrm{En}}$.

#### Required chain {#sec-strategy-C-chain}

::: {.problem #prob:C1 title="C1. Classification of admissible involutions of the K3 cusp lattices"}
Classify involutions of the two reflective K3 cusp lattices whose fixed lattices have the Coble cusp types and whose full-lattice lifts preserve the labeled direct Coble data.
:::

::: {.problem #prob:C2 title="C2. Direct root-folding theorem"}
Classify all orbits of roots of the two reflective K3 cusp lattices under the direct Coble involution and prove that every negative folded vector is a Coble root and every Coble root arises in this way.
:::

::: {.problem #prob:C3 title="C3. Chamber-intersection theorem"}
Prove that the intersection of a Coxeter chamber of a reflective K3 cusp lattice with the direct Coble fixed subspace is a fundamental chamber for the direct Coble reflection group.
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

A potentially efficient hybrid is to prove the direct open period and monodromy theorem first, then use the AEGS stable family only to construct boundary models.
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

## Restriction of a generalized Coxeter semifan {#sec-semifan-restriction}

::: {.theorem #thm:semifan-restriction title="Restriction of a generalized Coxeter semifan to a $(-2)$-Heegner sublattice"}
Let $T$ be an even lattice, $e\in T$ primitive isotropic, $\bar T=e^\perp/\ZZ e$, and $\delta\in T$ primitive with $\delta^2=-2$ and $\delta\cdot e=0$. Put
$$
H=\bar\delta^\perp,\qquad
\bar S=(\delta^\perp\cap e^\perp)/\ZZ e=H\cap\bar T,
$$
a primitive corank-one sublattice of $\bar T$. Let $W$ be a reflection group on $\bar T$, let $C$ be a chamber for $W$ cut out by a diagram $G$, and let $\Fgen(I\sqcup J)$ be its generalized Coxeter semifan in the sense of [@AEGS25], §5.2, printed p. 610. Write $C_\delta=C\cap H_\RR$ and let $W_\delta$ be generated by the integral reflections of $\bar S$ whose mirrors bound $C_\delta$ in the interior of its positive cone.

**Case A: $\bar\delta$ is not a mirror of $W$.** Assume

- (A1) every wall of $C$ meeting the interior of the positive cone of $\bar S$ is the mirror of an integral root of $\bar S$;
- (A2) the induced angles between those restricted walls are $\pi/m$ with $m\in\ZZ_{\ge2}$, or the walls do not meet;
- (A3) no two roots of $G$ with different relevance have the same restricted wall.

**Case B: $\bar\delta$ is a mirror of $W$.** Assume

- (B1) that mirror is relevant;
- (B2) every finite nonzero angle between $\bar\delta$ and another wall of $C$ is $\pi/(2k)$ for some $k\in\ZZ_{\ge1}$;
- (B3) every restricted wall bounding $C_\delta$ in the interior of its positive cone is the mirror of an integral root of $\bar S$;
- (B4) every pair of restricted walls that meets in that interior has induced angle $\pi/m$ with $m\in\ZZ_{\ge2}$ or is parallel;
- (B5) no two roots of $G$ with different relevance have the same restricted wall.

In either case, the following two conclusions hold:

1. every wall of $C_\delta$ in the interior of the positive cone of $\bar S$ is $\alpha^\perp\cap H_\RR$ for a root $\alpha$ of $G$;
2. $C_\delta$ is a fundamental chamber for $W_\delta$ on the positive cone of $\bar S$.

In Case B, moreover:

3. $\Fgen(I\sqcup J)\cap H_\RR$ is the generalized Coxeter semifan of $C_\delta$, with the relevance inherited from $I\sqcup J$; and
4. its Type II rays and Type III cones are the maximal parabolic and elliptic faces of $C_\delta$, respectively, in the sense of [@AEGS25], Definition 5.1, printed p. 609, and its Type II coarsening is governed by the irrelevant components in [@AEGS25], Lemma 5.7, printed p. 611.
:::

::: {.proof}
For every $\alpha$ not proportional to $\bar\delta$, $\alpha^\perp\cap H_\RR$ is the hyperplane in $H_\RR$ cut by the orthogonal projection of $\alpha$ to $H_\QQ$. This proves (1), since a wall must meet the interior of the positive cone to contribute a bounding hyperplane of $C_\delta$.

In Case A, (A1) makes each of these hyperplanes the mirror of an integral reflection of $\bar S$, and (A2) is Vinberg's cell criterion: a convex polyhedron whose dihedral angles are submultiples of $\pi$ is a fundamental chamber for the group generated by the reflections in its walls ([@Vin67], §1, printed p. 430, conditions $(\beta)$ and $(\beta')$). Since $C_\delta$ is the intersection of the corresponding half-spaces, this proves (2). No global identification of the restricted arrangement with the $W_\delta$-chambers is asserted in Case A: such an identification is proved below only in Case B, where every generator of $W_\delta$ is induced by an element of the stabilizer of $H_\RR$ in $W$.

It remains to prove (2) and (3) in Case B. Put $K=\Stab_W(H_\RR)$ and let $\alpha\neq\pm\bar\delta$ be a wall of $C$. Suppose first that $\alpha\perp\bar\delta$. Then $s_\alpha\in K$ restricts to reflection of $H_\RR$ in $\alpha^\perp\cap H_\RR$. If $\alpha$ is not orthogonal to $\bar\delta$ but the two hyperplanes meet in the positive cone, write their angle as $\pi/(2k)$ by (B2). On $P=\RR\bar\delta+\RR\alpha$, the product $s_{\bar\delta}s_\alpha$ is rotation through $\pi/k$. Consequently
$$
R_\alpha=(s_{\bar\delta}s_\alpha)^k
$$
is $-\id$ on $P$ and the identity on $P^\perp$. It therefore preserves $H_\RR=\bar\delta^\perp$, belongs to $K$, and restricts to reflection in $\alpha^\perp\cap H_\RR$. Thick and non-intersecting walls do not contribute a wall in the interior of $C_\delta$. Thus every induced wall reflection is induced by an element of $K$.

By (B3) all these reflections are integral on $\bar S$, and by (B4), with the same Vinberg criterion used above, $C_\delta$ is a fundamental chamber for $W_\delta$. This proves (2).

Let $\mathcal H$ be the set of hyperplanes of $H_\RR$ obtained by intersecting it with mirrors of $W$. The two constructions above place every initial wall of $W_\delta$ in $\mathcal H$ and every generating reflection of $W_\delta$ in the restriction of $K$. Since $K$ preserves $\mathcal H$, every $W_\delta$-wall belongs to $\mathcal H$, and every $W_\delta$-image of $C_\delta$ has no hyperplane of $\mathcal H$ through its interior. Indeed, such a hyperplane would pull back to one through the interior of $C_\delta$, hence to a wall of $W$ through the interior of $C$.

Let $D$ be a $W$-chamber whose intersection with $H_\RR$ meets the interior of some $W_\delta$-chamber $D'$. Every wall of $D'$ is a mirror of $W$, so $D$ lies entirely in the closed half-space of each such wall selected by their common interior point. Hence $D\cap H_\RR\subseteq D'$. Since no hyperplane of $\mathcal H$ crosses the interior of $D'$, also $D'\subseteq D\cap H_\RR$. It follows that $D'=D\cap H_\RR$. The Vinberg tiling by $W_\delta$ covers the positive cone of $\bar S$, so every original chamber intersection arises in this way. Therefore the maximal cones of $\Fcox\cap H_\RR$ and of the Coxeter semifan of $W_\delta$ are identical, not merely combinatorially similar. Intersecting with the rational closure preserves this identification of their supports.

Finally (B1) excludes the deleted mirror itself from the irrelevant roots, and (B5) assigns a unique relevance to every remaining restricted wall. Deleting an original face given by a set of irrelevant walls therefore deletes precisely the face with the same walls in $C_\delta$. Intersection commutes with taking these wall faces, so it identifies the generalized coarsenings and proves (3).
:::


::: {.proposition #prop:semifan-restriction-obstruction title="The hypothesis of Case A is not automatic"}
Let $\bar T = U\oplus A_3$ with simple roots $\alpha_1,\alpha_2,\alpha_3$ of the $A_3$ summand, and $\bar\delta = \alpha_2$. Then $\bar S = U\oplus\langle\alpha_1-\alpha_3,\ \alpha_2+2\alpha_3\rangle$ has signature $(1,2)$, and the wall cut by $\alpha_1$ is not reflective in $\bar S$: no multiple of the projection $\alpha_1+\tfrac12\alpha_2$ that lies in $\bar S$ has an integral reflection there. So the reflectivity condition (A1) fails and the restricted cone is not cut out by reflections of $\bar S$.

The example $U\oplus A_2$ with $\bar\delta = \alpha_1$ does **not** obstruct: the projection of $\alpha_2$ is $\tfrac12 v$ with $v = \alpha_1+2\alpha_2$ of square $-6$, the two have the same wall $v^{\perp}$ in $\bar S = U\oplus\ZZ v$, and $v\cdot\bar S = 6\ZZ$ makes $s_v(x) = x+\tfrac13(x\cdot v)v$ integral. That is why (H1) is a condition on walls and not on the vectors themselves.
:::

::: {.proof}
In $\bar T = U\oplus A_3$ the projection of $\alpha_1$ along $\bar\delta = \alpha_2$ is $\alpha_0 = \alpha_1+\tfrac12\alpha_2$: it has $(\alpha_0,\alpha_2) = 0$ and $\alpha_0 - \alpha_1\in\QQ\alpha_2$. Its square is $-2+1-\tfrac12 = -\tfrac32$. The vectors of the line $\QQ\alpha_0\cap\bar S$ are the multiples $m(2\alpha_0) = m(2\alpha_1+\alpha_2)$: since $\bar S$ is generated by $U$, $\alpha_1-\alpha_3$ and $\alpha_2+2\alpha_3$, one checks $2\alpha_0 = 2(\alpha_1-\alpha_3)+(\alpha_2+2\alpha_3)\in\bar S$ is primitive there, and $\alpha_0\notin\bar S$. For $w = m(2\alpha_0)$ the reflection is integral on $\bar S$ only if $w^2 = -6m^2$ divides $2(x,w) = 4m\,(x,\alpha_0)$ for all $x\in\bar S$, and $(x,\alpha_0)$ takes the value $1$ on $x = \alpha_2+2\alpha_3$; so $6m^2\mid 4m$, which has no positive solution. Hence the wall carries no integral reflection of $\bar S$.

For the second paragraph: $v = \alpha_1+2\alpha_2$ has $v^2 = -6$, its orthogonal complement in $\bar S$ is the same hyperplane as $\alpha_0^{\perp}$ because $\alpha_0 = \tfrac12v$, and $v\cdot\bar S\subseteq 6\ZZ$ since $v\cdot U = 0$, $v\cdot v = -6$ and $v\cdot(\alpha_1+2\alpha_2) = -6$; so $x\mapsto x+\tfrac13(x\cdot v)v$ is an integral reflection of $\bar S$ with mirror $v^{\perp}$. Here (A1) holds although $\alpha_0\notin\bar S$.
:::

::: {.proposition #prop:facet-angles-aegs title="The induced facet angles at every white node of the AEGS cusp diagrams"}
Read the nodes of [@AEGS25], Figures 7--8, printed pp. 594--595, using its definition in §3.4, printed p. 591: for simple roots $\alpha_i$,
$$
g_{ij}=\frac{(\alpha_i,\alpha_j)}{\sqrt{\alpha_i^2\alpha_j^2}},
$$
and a single, double, thick, or dotted bond records respectively $g_{ij}=\tfrac12$, $g_{ij}=\tfrac1{\sqrt2}$, $g_{ij}=1$, or $g_{ij}>1$. The same paragraph states that white nodes are $(-2)$-roots and black nodes $(-4)$-roots. The five diagrams have respectively $12,10,12,11,14$ nodes; the white ones are
$$
\begin{array}{c|c|c}
\text{cusp}&\text{figure node}&\text{printed root in the Sterk transcription}\\ \hline
2&10&r_{10}\\
3&5,9&r_8,r_{12}\\
4&7,9&r_{10},r_8\\
5&9,10,11,12&r_{14},r_{12},r_{11},r_{13}.
\end{array}
$$
Cusp $1$ has no white node. The node order at each cusp, the coloured bond lists, the exact integral root representatives, and the resulting integral wall Gram matrices are printed in `computations/reports/coble_enriques-white-root-facets-run.txt`; the coloured graph match to Figures 7--8 is checked entry by entry in `computations/reports/coble_enriques-white-root-facets.py`.

Let $\delta$ be a white node and let $i,j$ range over **every** pair of distinct walls other than $\delta^\perp$, including walls orthogonal to $\delta$. Put $\theta_{ij}=\arccos g_{ij}$ and define $\phi_{ij}$ by
$$
\cos\phi_{ij}
 =\frac{g_{ij}+g_{\delta i}g_{\delta j}}
 {\sqrt{(1-g_{\delta i}^2)(1-g_{\delta j}^2)}}.
$$
The value $1$ denotes a parallel pair and a value $>1$ a pair that does not meet. The complete tables of these values have the following multisets.
$$
\begin{array}{c|c|c|r|r|r|r|r}
\text{cusp}&\delta&\text{remaining walls}&\pi/2&\pi/3&\pi/4&
 \text{parallel}&\text{no intersection}\\ \hline
2&10& 9&28&7&1&0&0\\
3& 5&11&44&6&3&1&1\\
3& 9&11&44&6&3&1&1\\
4& 7&10&36&7&2&0&0\\
4& 9&10&36&7&2&0&0\\
5& 9&13&62&6&7&2&1\\
5&10&13&62&6&7&2&1\\
5&11&13&62&6&7&2&1\\
5&12&13&62&6&7&2&1
\end{array}
$$
Thus every intersecting pair of induced walls has angle $\pi/2$, $\pi/3$, or $\pi/4$. Exactly one of the nine facets is the nine-wall chamber of @thm:coble-cusp-chamber: the facet at node $10$ of cusp $2$. Its bonds are
$$
1-2,\quad 2-3,\quad 1-4,\quad 1-5,\quad 5-6,\quad 6-7,\quad 7-8,\quad 8-9,
$$
with $8-9$ double and all others single.
:::

::: {.proof}
The integral wall Gram matrices in the record are computed from the printed root representatives, and their normalized off-diagonal entries reproduce the coloured bond lists of the printed figures. This verifies the input before any facet is taken. The full pair-by-pair angle tables are in the transcript beside its code.

All nine white nodes have only double incident bonds. If $i,j$ are both orthogonal to $\delta$, then $\phi_{ij}=\theta_{ij}$. If $i$ is joined to $\delta$ by a double bond and $j$ is orthogonal to $\delta$, then $\cos\phi_{ij}=\sqrt2\,g_{ij}$; hence a single, double, or thick bond $i-j$ becomes respectively double, thick, or non-intersecting. If both $i$ and $j$ are double-bonded to $\delta$, then $\cos\phi_{ij}=2g_{ij}+1$; in each printed case $i$ and $j$ are nonadjacent, so the induced bond is single. The remaining pairs are orthogonal. These substitutions give every entry of the table, including the parallel and non-intersecting pairs. In particular, none of the earlier values $\arccos(1/3)$ or $\arccos(1/\sqrt3)$ occurs at a white node, and the deleted angle-sum argument was not a valid test of the spherical link.

At cusp $2$, deletion of the white node $10$ changes the bond $8-9$ from single to double and leaves the displayed nine-wall diagram. The transcript checks this bond list against @thm:coble-cusp-chamber. The other facets have $11$, $10$, or $13$ induced wall restrictions. Even if each listed parallel pair identified two restrictions, the totals would remain at least $10$, $10$, and $11$ respectively, so they cannot produce the nine-wall diagram.
:::

::: {.lemma #lem:cusp-root-lift-independence title="Lift independence of the perpendicular discriminant form at a white cusp root"}
Let $\eta\in T_{\En}$ be primitive isotropic and let $\delta\in\eta^\perp$ satisfy $\gcd((\delta,\eta^\perp))=1$. For every $k\in\ZZ$ there is an integral isometry $u_k$ that fixes $\eta$, acts trivially on $\eta^\perp/\ZZ\eta$, and satisfies $u_k(\delta)=\delta-k\eta$. Consequently the lattices $\delta^\perp$ and $(\delta+k\eta)^\perp$ are isometric and have the same discriminant quadratic form.
:::

::: {.proof}
Choose $a\in\eta^\perp$ with $(a,\delta)=1$. In the version actually read, arXiv:0810.1614v1, §3.1, Lemma 3.1 and formula (4) give precisely the Eichler transvection displayed next, and the integrality assertion following equation (10), printed pp. 8--9 of that version, applies because $\eta$ and $a$ are integral vectors with $a^2$ even. The *J. Algebra* record cited by the bibliography supplies publication data only. Explicitly,
$$
E_{\eta,a}(x)=x+(x,\eta)a-(x,a)\eta-\frac{a^2}{2}(x,\eta)\eta
$$
and it is integral on $T_{\En}$. Direct expansion gives $E_{\eta,a}(\eta)=\eta$ and $E_{\eta,a}(\delta)=\delta-\eta$. Moreover, for $x\in\eta^\perp$,
$$
E_{\eta,a}(x)-x=-(x,a)\eta,
$$
so $E_{\eta,a}$ acts trivially on $\eta^\perp/\ZZ\eta$. Take $u_k=E_{\eta,a}^k$. An isometry $u$ identifies $\delta^\perp$ with $u(\delta)^\perp$, which proves the last assertion.
:::

::: {.proposition #prop:cusp-white-root-complements title="The perpendicular lattices of the nine white cusp-diagram roots"}
For each of the nine white roots in @prop:facet-angles-aegs, and for every lift $\delta$ of that root to $\eta^\perp\subset T_{\En}$, the perpendicular $\delta^\perp$ is isometric to
$$
T_{\Co}=\langle2\rangle\oplus E(2)
 =\langle2\rangle\oplus U(2)\oplus E_8(2),
$$
the lattice of [@DK13], (3.6), printed p. 513. Its discriminant group is $(\ZZ/2\ZZ)^{11}$, and the normal form of its discriminant quadratic form is
$$
\begin{pmatrix}0&1/2\\1/2&0\end{pmatrix}^{\oplus 5}
  \oplus(1/2),
$$
with values in $\QQ/2\ZZ$.
:::

::: {.proof}
The exact representatives of the nine roots satisfy $\delta^2=-2$ and $\gcd((\delta,\eta^\perp))=1$, as the transcript prints next to each candidate. By @lem:cusp-root-lift-independence it therefore suffices to compute on those representatives.

For each representative the record prints a $\ZZ$-basis $B$ of $\delta^\perp$ and the Gram matrix $H_\delta=BGB^{\mathit T}$. Every $H_\delta$ has rank $11$ and determinant $-2048$. The same owner call
`IntegralLattice(H).discriminant_group().normal_form()`
on each $H_\delta$ and on the displayed model $T_{\Co}$ returns identical value modules, invariants, quadratic matrices, and bilinear matrices; the common output is the normal form in the statement. The nine triples (cusp, figure node, printed root) are listed at the end of the transcript, which terminates with `PYEXIT=0`; their matrices and full normal forms appear in the per-candidate sections.

The perpendicular is even because $T_{\En}$ is even, and it has signature $(p,q)=(2,9)$ because $\delta^2<0$. Its discriminant group has order $2^{11}$, and the final $(1/2)$-summand distinguishes the $2$-elementary invariant $\delta=1$. Thus $a=p+q=11$ and its invariants are $(11,11,1)$. The existence hypotheses of @thm:two-elementary-classification hold directly: $p,q\ge1$, $a=p+q$, $p+q+a=22$ is even, and the further listed conditions impose nothing when $\delta=1$, $a\ne0,1,2$. Its uniqueness clause ([@Nik80, Thm. 3.6.2, printed p. 144]), rather than @prop:coble-transcendental, gives $\delta^\perp\cong T_{\Co}$.
:::

::: {.theorem #thm:coble-restricted-semifan title="The restricted Coxeter semifan at cusp 2 is the marked Coble semifan"}
Let $\eta$ be the cusp-$2$ isotropic vector, let $\delta=r_{10}$, let $C_\delta$ be the facet of the AEGS cusp-$2$ chamber computed in @prop:facet-angles-aegs, and put
$$
\bar S=(\delta^\perp\cap\eta^\perp)/\ZZ\eta .
$$
Then $\bar S\cong\langle2\rangle\oplus E_8(2)$ and:

1. $C_\delta$ is a fundamental chamber of the full reflection group $W^{(2,4)}(\bar S)$, generated by all $(-2)$-roots and all $(-4)$-roots of divisibility $2$ in the sense of [@AN06], Theorem 3.1, printed p. 51, and it is the chamber of [@AN06], Table 1, entry $(9,9,1)$, printed p. 52;
2. intersection with $\bar\delta^\perp$ identifies the AEGS semifan $\mathcal F^2$ of [@AEGS25], Definitions 5.3 and 5.4, printed pp. 610--611, with the generalized Coxeter semifan of $C_\delta$ whose irrelevant set is the single interior spur, in the manuscript's current wall labels $\{4\}$; and
3. after reordering the walls as
$$
(v_1,v_2,v_3,v_4,v_5,v_6,v_7,v_8,v_9)
 =(3,2,1,5,6,7,8,9,4),
$$
the irrelevant root is $v_9$ and the restricted irrelevant group is $\langle s_{v_9}\rangle\cong S_2$, while $v_1,\dots,v_8$ are relevant.
:::

::: {.proof}
The exact representatives give $\bar S=\ZZ(e+f)\oplus E_8(2)$ in the basis used for Figure 7. For $i<10$, the projected normals are $w_i=r_i+\tfrac12(r_i,\delta)\delta$, integral vectors of $\bar S$; only $w_9=r_9+\delta$ differs from $r_i$. The record `computations/reports/coble_cusp2-restricted-semifan.py` and its transcript print these coordinates and verify $w_9^2=-2$, $w_i^2=-4$ for $i<9$, and the divisibility required for each reflection to be integral (divisibility $2$ at $w_9$ and at the eight $(-4)$-vectors). The nine hyperplanes are distinct because their Gram matrix is nonsingular.

All hypotheses of Case B of @thm:semifan-restriction hold. The mirror $r_{10}$ is on the boundary of AEGS Figure 7's folded triangle, hence relevant by Definition 5.4. Its only nonorthogonal incidence is the double bond $9-10$, which has the even label $4$. The projected roots are reflective by the preceding paragraph. @prop:facet-angles-aegs gives only $\pi/2,\pi/3,\pi/4$ as intersecting induced angles, with no parallel pair at this candidate. Relevance is collision-free because the nine restricted hyperplanes are distinct. Therefore $C_\delta$ is a fundamental chamber of $W_\delta$, and intersection is the generalized Coxeter semifan with the inherited marking.

Now let $W_\delta$ be generated by these nine projected reflections. Their Gram matrix in the displayed AN order is exactly that of @thm:coble-cusp-chamber, namely a chain $v_1-\cdots-v_8$ with $v_7-v_8$ double and $v_8$ open, and the additional $v_9$ attached to $v_3$. Mapping the nine projected normals to the corresponding normals of the AN chamber preserves all pairings; it therefore induces an isometry between their real spans and identifies the two simplicial chamber cones. In particular, $C_\delta$ and the AN chamber have the same finite hyperbolic volume, the AN chamber being of finite volume by @thm:coble-cusp-chamber's source in [@AN06], Table 1, printed p. 52. Also $W_\delta\subseteq W^{(2,4)}(\bar S)$ by the checked squares and divisibilities. The fundamental-covolumes of the two groups are the volumes of these chambers, so
$$
[W^{(2,4)}(\bar S):W_\delta]
 =\frac{\operatorname{vol}(C_\delta)}
        {\operatorname{vol}(C_{\mathrm{AN}})}=1 .
$$
The groups are equal and $C_\delta$ is a fundamental chamber of the full group, proving (1).

The marking is AEGS Definition 5.4: roots on the folded triangle's boundary are relevant, and Figure 7's interior spur is the only irrelevant root. Lemma 5.5 attaches that marking to $\mathcal F^2$. It descends unchanged by @thm:semifan-restriction, while @thm:semifan-restriction(3) supplies the generalized fan identification. The only irrelevant reflection is integral and of order $2$, so its group is $S_2$, in agreement with AEGS Lemma 5.6, printed p. 611. Current node $4$ is named $v_9$ by the displayed reordering, proving (2) and (3).
:::

::: {.remark title="Why the mirror case has a parity hypothesis"}
In Case B, (B3) is used to make each induced wall reflection integral on $\bar S$, and (B4) is used to make $C_\delta$ a Vinberg chamber. The additional even-incidence condition (B2) serves a different purpose: it supplies the element of $\Stab_W(H_\RR)$ inducing that reflection, hence it makes the $W_\delta$-chambers coincide with the restriction of the original chamber decomposition. Without this compatibility, proving that one facet has Coxeter angles would not prove equality of the two semifans.
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

## Summary of results {#sec-status-ledger}

The table lists each statement, whether it is proved, and the section that proves or states it.

| Statement | Status | Section |
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
| Polarized cusp count: $527$ $0$-cusps and $189\,720$ $1$-cusps | established | @sec-finite-orbits |
| Finite $O(A)$ orbit tables | established computation | @sec-finite-orbits |
| Unpolarized Coxeter chamber | established | @sec-unpolarized-coxeter |
| Polarized wall-slice arrangements | established computations | @sec-wall-slices |
| Polarized Coble Coxeter diagrams | not established | @sec-coxeter |
| Integral-affine Coble package | defined; realization open | @sec-coble-affine-package |
| Direct dlt and stable-model theorem | open | @sec-coble-dlt |
| Exact Coble semifans | open | @sec-direct-semifans |
| Normalization of the Heegner KSBA closure | target theorem | @sec-heegner-target |

: Statements of the report and the sections that prove or state them. {#tbl-status-ledger}

## Computations {#sec-computational-record}

### Explicit invariant branch curve {#sec-explicit-curve}

::: {.example #ex:one-node-branch-curve title="an invariant $(4,4)$ curve with one node"}
On the affine chart $x_0=y_0=1$ of $Y$, let

\[
\begin{aligned}
f(x,y)={}&29x^4y^4+23x^4y^2+19x^4
 +17x^3y^3+13x^3y\\
&+11x^2y^4+7x^2y^2+x^2
 +5xy^3+xy+3y^4+2y^2.
\end{aligned}
\]

Each monomial of $f$ has exponents at most $4$ in each variable and even total degree, so $f$ is a $\tau$-invariant section of $\mathcal O_Y(4,4)$.
The constant term of $f$ is $0$, and its quadratic part $x^2+xy+2y^2$ has discriminant $1-8=-7\ne0$.
So by @lem:node-condition the curve $B=(f=0)$ has an ordinary node at the $\tau$-fixed point $p=(0,0)$.

On the chart $(x,y)$ the ideal $(f,\partial_xf,\partial_yf)$ has reduced lexicographic Gröbner basis $\{x,y\}$.
On each of the other three standard affine charts of $Y=\bP^1\times\bP^1$, the ideal of the dehomogenized equation and its two partial derivatives has Gröbner basis $\{1\}$.
So $p$ is the only singular point of $B$.

Smoothness away from $p$ is a Zariski-open condition on the irreducible linear system of invariant curves through $p$, and $B$ satisfies it.
So a general invariant curve with an ordinary node at $p$ is smooth away from $p$.
:::

## Appendix: candidate wall-slice arrangements {#sec-appendix-wall-slices}

This appendix gives the finite arrangements obtained by slicing selected AEGS Enriques chambers by selected white-root hyperplanes, with the Gram entry of @sec-gram-correction.
Whether each is a complete Coxeter diagram is @prob:coxeter-completeness.

White vertices below have square $-2$ and black vertices have square $-4$.
A double arrow denotes the non-simply-laced Coxeter edge between roots of unequal length; $==$ denotes a thick edge; and $\cdots$ denotes a dotted edge.

### Slice over the triangular AEGS cusp {#sec-slice-2}

The arrangement $G_{\mathrm{slice}}^2$ has nine vertices.
The vertices $c_0,\ldots,c_7$ are black and $c_8$ is white.
Its edges are

\[
c_0-c_3,
\qquad
c_1-c_2-c_3-c_4-c_5-c_6-c_7\dto c_8.
\]

This arrangement agrees with the standard unpolarized chamber after a relabelling.

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

## Residual open points {#sec-residual-open-points}

1. The descent category of the degree-$2$ class on the singular Coble model---Cartier line bundle, reflexive sheaf, or numerical class in special families---is open and must be fixed as part of the direct moduli theorem.
   The generic projective model supports the stated numerical and ampleness properties.

2. The family-theoretic construction of the canonical cover and simultaneous resolution is the cover--singular equivalence theorem (@prob:cover-singular-equivalence) together with the root-marked universal-family lemma of Strategy A (@prob:A2).

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

The open problems are the labeled embedding rigidity, equality with geometric monodromy, complete Vinberg chambers, algebraic realization of the Coble affine package, intrinsic relevance of walls, and the comparison between the autonomous compactification and the normalized Enriques Heegner closure.

The autonomous strategy organizes these issues into direct Coble analogues of the AEGS theorem chain.
The Heegner strategy organizes them into arithmetic normalization, universal-family, and no-further-coarsening statements.
A complete proof may combine the two, but it must eventually identify their lattices, groups, divisors, cusp structures, semifans, and KSBA families as the same mathematical objects.

## References {.unnumbered}

::: {#refs}
:::
