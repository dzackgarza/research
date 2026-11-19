# Surfaces: K3, Enriques, and rational

All surfaces are over $\CC$.

## Kodaira dimension and minimal surfaces

For a smooth projective surface $S$, put $P_m(S)=h^0(S,mK_S)$.
Its Kodaira dimension is the largest dimension of the image of a
pluricanonical rational map $\varphi_{|mK_S|}$, or $-\infty$ if all
$P_m$ vanish [@Bea96, Definition VII.1]. Equivalently it measures the
growth of the nonzero plurigenera. The growth must be taken along
sufficiently divisible degrees: on an Enriques surface $P_m$ is zero
for odd $m$ and one for even $m$.

The minimal smooth projective surfaces fall into the following classes
[@Bea96, Chapters III, VII–X].

| Kodaira dimension | Minimal models |
| --- | --- |
| $-\infty$ | $\PP^2$ and minimal ruled surfaces $\PP_C(E)$, excluding $\mathbb F_1$ |
| $0$ | Abelian, K3, Enriques, and bielliptic surfaces |
| $1$ | Properly elliptic surfaces |
| $2$ | Surfaces of general type |

Here a ruled surface is birational to $C\times\PP^1$; the rational
case has $C\cong\PP^1$. Among ruled surfaces, $\mathbb F_1$ is not
minimal. A smooth projective surface is ruled if and only if $P_{12}=0$;
in particular, $p_g=0$ and $q\geq2$ imply ruledness
[@Bea96, Chapters V–VI]. Classification by Kodaira dimension separates
birational types; it does not determine an individual surface or its
moduli. For curves the corresponding distinction is genus: $\mathcal M_g$
has dimension $3g-3$ for $g\geq2$, whereas the coarse spaces
$\mathcal M_0$ and $\mathcal M_1$ have dimensions zero and one.

For compact complex surfaces the classification is broader. There are
nonprojective complex tori and K3 surfaces, non-Kähler Kodaira surfaces
of Kodaira dimension zero, and class VII surfaces of Kodaira dimension
$-\infty$ [@BHPV04, Chapter VI]. These analytic surfaces are distinct
from the smooth projective surfaces considered in the rest of this chapter.

Kodaira dimension one does not prevent endomorphisms of degree greater
than one. If $E$ is an elliptic curve and $C$ has genus at least two,
then $E\times C$ has Kodaira dimension one and
$[n]\times\operatorname{id}_C$ has degree $n^2$ for $n>1$.

::: {.example #ex:clebsch-cubic title="The Clebsch cubic"}
The equations
$$
\sum_{i=0}^4 x_i=0,\qquad \sum_{i=0}^4 x_i^3=0
$$
define a smooth cubic surface in a hyperplane $\PP^3\subset\PP^4$.
At a putative singular point all $x_i^2$ would be equal. Five numbers
each equal to $a$ or $-a$ cannot sum to zero unless $a=0$, which gives
no projective point. Like every smooth cubic surface over $\CC$, it has
twenty-seven lines [@Bea96, Chapter IV]: in the plane blowup model these
are the six exceptional curves, the fifteen transforms of lines through
pairs of the six points, and the six transforms of conics through five
points. Smoothness is essential to this line count.
:::

## $K3$ surfaces

::: {.definition #def:k3-surface title="K3 surface"}

A **$K3$ surface** is a smooth, projective, geometrically integral surface $X$ over $k = \CC$ such that its canonical bundle is trivial,
$$
\omega_X \cong \OO_X
\qquad\text{(equivalently } K_X\sim 0\text{)},
$$
and its irregularity vanishes,
$$
q(X) \definedas h^{0,1}(X) = h^1(X, \OO_X) = 0
.
$$
:::

Terminology for Calabi–Yau varieties varies. In the convention used
here, *weak Calabi–Yau* means smooth and projective with
$\omega_X\simeq\mathcal O_X$; the *strong* condition also asks for
$H^i(X,\mathcal O_X)=0$ for $0<i<\dim X$ and trivial fundamental
group. In dimension two, an abelian surface meets the weak condition,
whereas a K3 surface meets the strong one.

::: {.proposition #prop:k3-lattice title="The K3 lattice"}

Let $X$ be a $K3$ surface.
With its cup-product pairing, $H^2(X;\ZZ)$ is isometric to the **$K3$ lattice**
$$
\lkt = U^3 \oplus E_8^{2} = \latII_{3, 19}
,
$$
the orthogonal direct sum of three hyperbolic planes and two copies of the negative-definite $E_8$ lattice of @def:lattice-En.
It is even, unimodular, of signature $(3, 19)$ [@Huy16, Prop. 1.3.5].
:::

::: {#not:k3-lattice-e8-sign .notation title="Sign of $E_8$ in the K3 lattice"}

If $E_8$ denotes the positive-definite root lattice, the K3 lattice is written $U^3\oplus E_8(-1)^2$.
:::

::: {.definition #def:marked-k3-surface title="Marked K3 surface"}

A **marked $K3$ surface** is a pair $(X, \varphi)$ of a $K3$ surface $X$ and an isometry
$$
\varphi\colon H^2(X; \ZZ) \iso \lkt
$$
[@Huy16, Sec. 6.3.3].
:::

::: {.proposition #prop:k3-hodge-diamond title="Hodge diamond of a K3 surface"}

The Hodge numbers of a $K3$ surface are
$$
h^{0,0} = h^{2,2} = 1,
\qquad
h^{1,1} = 20,
\qquad
h^{2,0} = h^{0,2} = 1,
$$
and all other Hodge numbers vanish [@Huy16, Sec. 1.2, (2.7)].
So the Hodge diamond is
$$
\begin{matrix}
 &  & 1 &  & \\
 & 0 &  & 0 & \\
1 &  & 20 &  & 1 \\
 & 0 &  & 0 & \\
 &  & 1 &  &
\end{matrix}
$$
and the second Betti number is $b_2(X)=1+20+1=22$.
In particular $\chi(\OO_X)=1-0+1=2$ and
$e(X)=1+22+1=24$. Noether's formula gives
$c_2(X)=12\chi(\OO_X)-K_X^2=24$.
The intersection form has signature $3-19=-16$.
:::

The nowhere-vanishing holomorphic two-form on a K3 surface is
symplectic and contracts vector fields to one-forms, giving
$T_X\simeq\Omega_X^1$. Since $h^{1,0}(X)=0$, it follows that
$H^0(X,T_X)=0$: there are no holomorphic infinitesimal
automorphisms. A complex K3 surface is simply connected
[@Huy16, §§1.1–1.3]. There is also a direct algebraic obstruction to
a nontrivial connected finite étale cover $\pi:Y\to X$: its canonical
bundle is trivial, while étale Riemann–Roch gives
$\chi(\mathcal O_Y)=\deg(\pi)\chi(\mathcal O_X)=2\deg(\pi)$.
But $Y$ is connected and proper, so Serre duality gives
$\chi(\mathcal O_Y)=2-h^1(\mathcal O_Y)\leq2$; hence
$\deg(\pi)=1$. Thus the étale fundamental group is trivial.

::: {.example #ex:k3-projective-models title="Projective models of K3 surfaces"}

Adjunction gives $K_X\sim0$ for a smooth quartic $X\subset\PP^3$,
a smooth intersection of a quadric and a cubic in $\PP^4$, and a
smooth intersection of three quadrics in $\PP^5$: in each case the
sum of the defining degrees equals the dimension of the ambient
projective space plus one. The standard cohomology sequence for a
complete intersection gives $H^1(X,\OO_X)=0$, so each is a K3 surface
[@Huy16, §1.2]. Their hyperplane classes have squares $4$, $6$ and
$8$, respectively.
A quartic equation in four variables has
$h^0(\PP^3,\OO(4))=\binom{7}{4}=35$ coefficients. Projectivizing and
dividing by the $15$-dimensional group $\PGL_4$ gives the expected
$34-15=19$ moduli dimensions for smooth quartics. This count agrees
with the degree-$4$ polarized K3 period domain, but describes the
quartic model locus rather than every degree-$4$ polarized model.

If $B\subset\PP^2$ is a smooth sextic, its double cover $X\to\PP^2$
is also K3. Indeed $\pi_*\OO_X=\OO_{\PP^2}\oplus\OO_{\PP^2}(-3)$,
so $H^1(\OO_X)=0$, and the double-cover canonical formula
@prop:double-cover-canonical-bundle gives
$K_X=\pi^*(K_{\PP^2}+\OO_{\PP^2}(3))\sim0$.
The minimal resolution of the quotient of an abelian surface by
$a\mapsto-a$ is a Kummer K3 surface [@Huy16, §1.2].

For a quartic $X\subset\PP^3$ containing a line $R$, let $H$ be its
hyperplane class and $E=H-R$. The plane sections through $R$ give a
genus-one pencil $|E|$: $H^2=4$, $R^2=-2$, $H\cdot R=1$, hence
$E^2=0$ and $H\cdot E=3$. The classes
$L_k=H+(k-1)E$ then have
$L_k^2=6k-2$. They are primitive since
$L_k\cdot E=3$ and $L_k\cdot R=3k-2$ are coprime. This supplies
explicit K3 polarizations of genera
$3k$ for $k\geq1$; it is a family of degrees, while nonemptiness of
the polarized K3 moduli space holds for every positive degree
$2d$ [@Huy16, Chs. 2, 6].
The same construction gives unbounded primitive polarization degrees
over a finite field: over $\mathbb F_{17}$, the smooth Fermat quartic
contains the line $x_0=\zeta x_1,\ x_2=\zeta x_3$ for an element
$\zeta$ of order eight. Its classes $L_k$ are defined over
$\mathbb F_{17}$ and have squares $6k-2$. Thus a fixed finite base
field does not impose a bound on polarization degree.

For an ample line bundle $L$ on a K3 surface, Riemann--Roch and
Kodaira vanishing give
$$
h^0(X,L)=\chi(X,L)=2+\frac{L^2}{2}.
$$
Thus $|L|$, when basepoint-free, maps to
$\PP^{\,1+L^2/2}$. In degree $4$ the map can be hyperelliptic,
of degree two onto a quadric, or birational onto a quartic surface;
the degree alone does not choose the model
[@Huy16, §2.1; @Sai74].
:::

::: {.proposition #prop:k3-elliptic-isotropic title="Isotropic classes and genus-one fibrations"}
A projective K3 surface $X$ admits a genus-one fibration
$X\to\PP^1$ if and only if $\NS(X)$ contains a nonzero class $v$
with $v^2=0$. In the forward direction the fibre gives such a class.
Conversely, Riemann--Roch makes one of $v,-v$ effective. Reflections
in effective $(-2)$-classes move an effective primitive isotropic class
to the nef cone; its complete linear system is a basepoint-free
genus-one pencil [@Huy16, Ch. 11].
The statement concerns a genus-one fibration. A section, which makes
it Jacobian, is additional data.
:::

### Linear systems, curves, and positivity

For a line bundle $L$ on a projective variety $X$, the base scheme of
$|L|$ is cut out by the image of the evaluation map
$H^0(X,L)\otimes\mathcal O_X\to L$. Its support is the intersection of
the zero sets of all sections. Sections define a rational map
$X\dashrightarrow\mathbb P(H^0(X,L)^\vee)$ wherever they do not vanish
simultaneously. When $|L|$ is basepoint-free, its evaluation map
defines a morphism on all of $X$. A rational map may also extend after
removing a fixed divisor, so regularity of the rational map alone is
not a basepoint-freeness test. A basepoint-free *multiple* of $L$
means that $L$ is semiample [@Huy16, §2.3].
For a smooth complex projective variety in a projective embedding,
Bertini's theorem makes a general hyperplane section smooth; for a
basepoint-free linear system the general member is smooth under the
usual separability hypotheses [@Huy16, §2.3].

For a reduced, irreducible projective curve $C$, let
$\nu:\widetilde C\to C$ be its normalization. Its geometric genus is
$g(\widetilde C)$, whereas $p_a(C)=1-\chi(\mathcal O_C)$. The normalization
sequence gives
$$
p_a(C)-g(\widetilde C)
=h^0(C,\nu_*\mathcal O_{\widetilde C}/\mathcal O_C)
=\sum_{p\in C_{\mathrm{sing}}}\delta_p.
$$
On a K3 surface, adjunction gives $p_a(C)=1+C^2/2$. Hence an
*irreducible* curve has $C^2\geq-2$, and an irreducible curve of square
$-2$ is smooth and rational. This does not say that every curve on a
K3 is smooth. If $C$ is smooth of genus $g\geq1$, the restriction
sequence and $K_X=0$ give $h^0(X,\mathcal O_X(C))=g+1$
[@Huy16, §§2.1–2.2].

An unpointed stable curve of genus at least two is a connected,
complete nodal curve with finite automorphism group. Its nodes have
completed local ring $\mathbb C[[x,y]]/(xy)$. A smooth proper genus-one
curve over a base scheme becomes an elliptic curve when supplied with
a section; the section is its group identity. This distinction also
applies to the generic fibers of genus-one fibrations on surfaces.

A line bundle is nef when its intersection with every integral curve
is nonnegative. On a smooth projective surface, a nef line bundle is
big exactly when its square is positive. The ample cone is the
interior of the nef cone; on a K3 it is the component of the positive
cone cut out by positive intersection with every smooth rational
$(-2)$-curve. Thus a nef and big class may lie on a wall and need not
be ample. Even on a K3, $|L|$ itself need not be basepoint-free for a
nef and big $L$; the fixed-part alternatives are described by
Saint-Donat [@Sai74; @Huy16, §2.3]. Kleiman's criterion concerns
strict positivity on the *closed cone of curves*, rather than merely
nonnegative intersection with each curve.
The cone of effective curves $\mathrm{NE}(X)\subset N_1(X)_{\mathbb R}$
is generated by classes of integral curves with nonnegative real
coefficients. Its closure $\overline{\mathrm{NE}}(X)$ is the closed
Mori cone; the nef cone in $N^1(X)_{\mathbb R}$ is its dual under
intersection. This separates a cone generated by actual curves from
its possible limit rays.

In characteristic zero, Kawamata–Viehweg vanishing on a smooth
projective surface gives $H^i(X,K_X+L)=0$ for $i>0$ when $L$ is nef
and big. This statement fails in general in positive characteristic.
For K3 surfaces, the corresponding $H^1(X,L)=0$ for nef and big $L$
holds in every characteristic by the surface argument in
[@Huy16, §3.1]; it does not follow just from the existence of a lift.
The numerical bound $\rho(X)\leq22$ also holds in positive
characteristic: for a prime $\ell$ different from the characteristic,
the Kummer sequence injects $\mathrm{NS}(X)\otimes\mathbb Q_\ell$
into $H^2_{\mathrm{\acute et}}(X,\mathbb Q_\ell(1))$, whose dimension is
$22$ [@Huy16, §§1.3, 3.2]. In contrast, over $\mathbb C$ the Hodge
bound is $\rho(X)\leq h^{1,1}(X)=20$.

## Enriques surfaces

::: {.proposition #prop:nonsymplectic-k3-projective title="Nonsymplectic finite-order automorphisms force projectivity"}
Let $X$ be a compact complex K3 surface and $g$ a finite-order
automorphism whose action on $H^{2,0}(X)$ is nontrivial. Then $X$ is
projective.
:::

::: {.proof}
Average a Kähler class over $\langle g\rangle$. The invariant real
subspace of $H^2(X,\RR)$ is of type $(1,1)$, since the invariant
subspaces of $H^{2,0}$ and $H^{0,2}$ vanish. The invariant subspace is
defined over $\QQ$, so it contains a rational class arbitrarily close
to the averaged Kähler class. Openness of the Kähler cone makes that
rational class Kähler. An integral multiple is the first Chern class
of a positive line bundle by the Lefschetz $(1,1)$ theorem, and the
Kodaira embedding theorem makes $X$ projective [@BHPV04, Chapters IV, VIII].
:::

::: {.definition #def:enriques-surface title="Enriques surface"}

An **Enriques surface** is a non-rational algebraic surface $Z$ of Kodaira dimension $\kappa(Z) = 0$ for which
$$
h^1(\OO_Z) = h^2(\OO_Z) = 0
$$
and the canonical class $K_Z$ is a nontrivial $2$-torsion element of $\Pic(Z)$.

Equivalently, $Z=X/\langle\iota\rangle$ for a $K3$ surface $X$ and a fixed-point-free involution $\iota$, called an **Enriques involution**.
:::

::: {.proposition #prop:enriques-minimal title="Enriques surfaces are minimal"}

An Enriques surface contains no smooth rational curve of square $-1$.
:::

::: {.proof}

Let $Z$ be an Enriques surface and let $E\subset Z$ be a smooth rational curve with $E^2 = -1$.
By adjunction, $K_Z\cdot E = 2g(E) - 2 - E^2 = -2 + 1 = -1$.
By @def:enriques-surface, $2K_Z\sim 0$, so $2(K_Z\cdot E) = 0$ and $K_Z\cdot E = 0$.
This is a contradiction.
:::

::: {.proposition #prop:enriques-universal-cover title="The K3 cover of an Enriques surface"}

Let $Z$ be an Enriques surface.
Then $\pi_1(Z)\cong\ZZ/2\ZZ$, and the universal covering $X\to Z$ is a $K3$ surface [@BHPV04, Lemma VIII.15.1(ii)].
Its deck group is $\langle\iota\rangle\cong\ZZ/2\ZZ$, where $\iota$ is the Enriques involution of @def:enriques-surface.
:::

::: {.proposition #prop:enriques-cohomology title="Hodge numbers and cohomology of an Enriques surface"}

Let $Z$ be an Enriques surface (@def:enriques-surface).
Then
$$
h^{1,0}(Z) = h^{0,1}(Z) = h^{2,0}(Z) = h^{0,2}(Z) = 0,
\qquad
h^{1,1}(Z) = 10
$$
[@BHPV04, Lemma VIII.15.1(i)], and $h^{0,0}(Z)=h^{2,2}(Z)=1$.
The first Chern class is an isomorphism
$$
c_1\colon\Pic(Z) \iso H^2(Z; \ZZ) \cong \ZZ^{10}\oplus \ZZ/2\ZZ
$$
[@BHPV04, Prop. VIII.15.2].
The intersection form on the torsion-free quotient of $H^2(Z;\ZZ)$ is isometric to the Enriques lattice $E_{10}=U\oplus E_8\iso\latII_{1,9}$, of signature $(1,9)$, of @def:enriques-lattice [@BHPV04, Lemma VIII.15.1(iii)].
:::

::: {.remark #rmk:enriques-even-lattice-not-spin title="An even free intersection lattice does not make an Enriques surface spin"}
The free lattice $H^2(Z,\ZZ)/\mathrm{tors}\cong U\oplus E_8$ is
even, but $Z$ is not spin. For a complex surface,
$w_2(TZ)$ is the reduction of $c_1(TZ)=-c_1(K_Z)$ modulo $2$.
The canonical class is the nonzero element of the $\ZZ/2$ summand of
$H^2(Z,\ZZ)$ in @prop:enriques-cohomology, and its reduction remains
nonzero. Thus $w_2(TZ)\neq0$.
The signature is $1-9=-8$, so Rokhlin's divisibility-by-$16$
theorem for closed smooth **spin** four-manifolds does not apply.
:::

::: {.proposition #prop:enriques-cover-eigenlattices title="Eigenlattices of an Enriques involution"}

Let $X\to Z$ be the $K3$ cover of an Enriques surface (@def:enriques-surface), with Enriques involution $\iota$.
Then there is an isometry $\varphi\colon H^2(X;\ZZ)\iso\lkt$ with $\varphi\circ\iota^* = \Ien\circ\varphi$, for $\Ien$ as in @def:lattice-involutions-k3.
The invariant sublattice of $H^2(X;\ZZ)$ under $\iota^*$ is isometric to $\sen = E_{10}(2)=U(2)\oplus E_8(2)$.
Its orthogonal complement is isometric to $\ten = U\oplus U(2)\oplus E_8(2)$, of signature $(2,10)$.
:::

::: {.proof}

Write $\lkt = E_8\oplus E_8\oplus U\oplus U\oplus U$ and let $\rho(x, y, z_1, z_2, z_3) = (y, x, -z_1, z_3, z_2)$.
There is an isometry $\varphi\colon H^2(X;\ZZ)\iso\lkt$ with $\varphi\circ\iota^* = \rho\circ\varphi$ [@BHPV04, Lemma VIII.19.1].
After the summands are put in the order $U\oplus U\oplus U\oplus E_8\oplus E_8$, the involution $\rho$ is $\Ien$ of @def:lattice-involutions-k3.
So $\varphi$ maps the invariant and coinvariant sublattices of $\iota^*$ isometrically to $\sen$ and $\ten$, whose isometry classes and signatures are given in @prop:k3-cover-eigenlattices.
:::

::: {.proposition #prop:enriques-period-domain title="The Enriques period domain"}

Let
$$
\Omega_{\ten}\definedas\theset{[x]\in\PP(\ten\tensor\CC) \mid x\cdot x = 0,\ x\cdot\bar x > 0}
$$
be the type IV period domain of $\ten$, with its two connected components.
Let $\Gamma^K_{\En} = \Orth(\ten)$, and let $\widetilde\Delta\subset\Omega_{\ten}$ be the union of the hyperplane sections $\alpha^\perp$ over the vectors $\alpha\in\ten$ with $\alpha^2 = -2$; these vectors form one $\Gamma^K_{\En}$-orbit.
Then the points of $(\Omega_{\ten}\setminus\widetilde\Delta)/\Gamma^K_{\En}$ are in bijection with the isomorphism classes of Enriques surfaces (@def:enriques-surface) [@AEGS25, Defs. 2.5–2.7].
The group $\Gamma^K_{\En}$ contains an isometry that exchanges the two components of $\Omega_{\ten}$, so this quotient is also $(\bD(\ten)\setminus\widetilde\Delta)/\Gamma^K_{\En}$ in the notation of @def:type-iv-period-domain (@lem:period-quotient-full-domain).
:::

## $ADE$ and $BC$ surfaces

::: {#not:surface-root-lattice-sign .notation title="Sign convention for root lattices"}

The root lattices $A_n$, $D_n$ and $E_n$ here are negative definite, with roots of square $-2$; see @def:root-lattice and @def:lattice-En.
:::

::: {.definition #def:ade-surface title="ADE surface"}

An **$ADE$ surface** is a normal surface $(Y, C)$ with reduced boundary $C$ given by one of the explicit constructions of [@AT17, Sec. 3, Def. 3.1].

1. The $ADE$ surfaces of pure shape are toric. They are defined by the polytopes of [@AT17, Sec. 3A, Def. 3.5, Table 1].
2. The $ADE$ surfaces of primed shape are obtained from surfaces of pure shape by priming (@def:priming; [@AT17, Sec. 3C, Def. 3.15]).

Each $ADE$ surface is a log del Pezzo surface of index $2$: the pair $(Y, C)$ is log canonical, and the divisor $-2(K_Y + C)$ is Cartier and ample [@AT17, Def. 3.1].
The $ADE$ surfaces are of type III in the sense of [@AT17, Lem. 2.5], so the pair $(Y, C)$ is not klt [@AT17, Def. 3.1, Lem. 2.5].
The construction associates to each $ADE$ surface a shape: a decorated $ADE$ Dynkin diagram, and the $ADE$ root lattice obtained by deleting the decorations [@AT17, Sec. 3].
:::

::: {.definition #def:priming title="Priming"}

Let $(Y, C)$ be an $ADE$ surface, let $P_1, \dots, P_k$ be distinct points of $C$ that are nonsingular on $Y$ and on $C$, and choose ideals $I_i \simeq (y, x^2)$ supported at $P_i$ and transverse to $C$.
Let $Y'\to Y$ be the weighted blowup at $\prod_i I_i$, let $C'$ be the strict transform of $C$, and let $L_0 = -2(K_{Y'} + C')$.
Assume that $L_0$ is big, nef and semiample.
The **priming** of $(Y, C)$ is the pair obtained by composing the blowup with the contraction given by $\abs{N L_0}$ for $N\gg 0$, with boundary the strict transform of $C$ [@AT17, Def. 3.13].
:::

::: {.definition #def:folding-bc title="Folding"}

A **folding** passes from a simply-laced $ADE$ diagram to a non-simply-laced $BC$ diagram by taking the quotient by a diagram automorphism $\tau$ [@AT17; @AET23].
:::

## The base surface $\PP^1\times\PP^1$

::: {.definition #def:p1xp1 title="The base surface"}

Let $Y = \PP^1\times\PP^1$ over $\CC$.
The Picard group $\Pic(Y)\cong\ZZ^2$ is freely generated by the pullbacks of hyperplanes $\ell_1, \ell_2$ from the two factors.
The intersection numbers are
$$
\ell_1^2 = \ell_2^2 = 0,
\qquad
\ell_1\cdot\ell_2 = 1
,
$$
yielding the lattice isometry
$$
(\Pic(Y), \cdot) \iso
\left( \ZZ^2,\ \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \right)
= U
.
$$
The canonical divisor is $K_Y = -2\ell_1 - 2\ell_2$, of self-intersection
$$
K_Y^2 = (-2\ell_1 - 2\ell_2)^2 = 8\,(\ell_1\cdot\ell_2) = 8
,
$$
so that $Y$ is a del Pezzo surface of degree $8$.
:::

## The toric surface $W$

::: {.proposition #prop:toric-surface-w title="The toric surface $W$"}

Let $Y = \PP^1\times\PP^1$ and let $\tau\colon (x, y)\mapsto(-x, -y)$ be the coordinate involution, which has $4$ fixed points.
The quotient $W = Y/\tau$ is a quartic del Pezzo surface with four $A_1$ singularities.
Both $Y$ and $W$ are toric, for the same polytope
$$
Q_{4, 4} \definedas [0, 4]^2
,
$$
with the lattices
$$
M_Y = \ZZ^2,
\qquad
M_W = \ZZ^2_{\mathrm{ev}}
\definedas \theset{ (i, j)\in\ZZ^2 \mid i + j\in 2\ZZ }
$$
[@AEGS25, Sec. 2.1].
:::

## Moduli of elliptic $K3$ surfaces

::: {.definition #def:moduli-elliptic-k3 title="The moduli space $F_{\mathrm{ell}}$"}

The moduli space $F_{\mathrm{ell}}$ is the moduli space of $K3$ surfaces polarized by the hyperbolic plane $U = \latII_{1,1}$, with a choice of vectors $s, f\in U$ such that $s^2 = -2$, $f^2 = 0$ and $s\cdot f = 1$.
For a suitable marking these are elliptic surfaces $X\to\PP^1$ with section $s$ and fiber $f$ [@ABE22, Sec. 1].
:::

::: {.proposition #prop:elliptic-period-lattice title="The period lattice of $F_{\mathrm{ell}}$"}

Let $U_1\iscontainedin\lkt$ be a hyperbolic summand. Then
$$
T_{\mathrm{ell}} \definedas U_1^{\perp\,\lkt} \cong U^2\oplus E_8^{2} = \latII_{2,18}
,
$$
of signature $(2, 18)$.
:::

::: {.proof}

Write $\lkt = U_1\oplus U\oplus U\oplus E_8\oplus E_8$ as in @prop:k3-lattice.
The summands are mutually orthogonal and $U_1$ is unimodular, so $U_1^{\perp\,\lkt} = U\oplus U\oplus E_8\oplus E_8$.
Its signature is $(3,19) - (1,1) = (2,18)$, and it is even and unimodular, so it is $\latII_{2,18}$.
:::

::: {.theorem #thm:abe-elliptic-compactifications title="Two stable pair compactifications of $F_{\mathrm{ell}}$"}

The following hold [@ABE22, Sec. 1, Thms. 1.1 and 1.2].

1. **Ramification divisor compactification** $\overline{F}^{\,\operatorname{ram}}$.
   The polarizing divisor is the ramification divisor $R\in\abs{3(s + 2f)}$ of the double cover $X\to\PP(1, 1, 4)$.
   The normalization of $\overline{F}^{\,\operatorname{ram}}$ is the toroidal compactification (@def:toroidal-compactification) for the $\Gamma$-orbit of one chamber, which is the union of $4$ Coxeter chambers.

2. **Rational curve divisor compactification** $\overline{F}^{\,\mathrm{rc}}$.
   The polarizing divisor is $R = s + m\Sum_{i=1}^{24} f_i$, where $f_i$ are the $24$ singular fibers counted with multiplicity, and any $m\geq 1$ gives the same result.
   The normalization of $\overline{F}^{\,\mathrm{rc}}$ is the toroidal compactification for the $\Gamma$-orbit of a subdivision of the Coxeter chamber into $9$ sub-chambers.

Here $\Gamma = O^+(\latII_{1,17})$.
The Baily--Borel boundary of $F_{\mathrm{ell}}$ consists of a unique $0$-cusp and two $1$-cusps [@ABE22, Sec. 2C].
For the two $1$-cusps, with primitive isotropic planes $J\subset\latII_{2,18}$, the lattices $J^\perp/J$ are $E_8^{2}$ and $D_{16}^{+} = \latII_{0,16}$ [@ABE22, Sec. 7I, proof of Thm. 7.58].
:::
