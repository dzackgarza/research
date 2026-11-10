# Surfaces: K3, Enriques, and rational

All surfaces are over $\CC$.

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

::: {.notation title="Sign of $E_8$ in the K3 lattice"}

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
:::

## Enriques surfaces

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

Let $Z$ be an Enriques surface.
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

::: {.proposition #prop:enriques-cover-eigenlattices title="Eigenlattices of an Enriques involution"}

Let $X\to Z$ be the $K3$ cover of an Enriques surface, with Enriques involution $\iota$.
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
\Omega_\ten\definedas\theset{[x]\in\PP(\ten\tensor\CC) \mid x\cdot x = 0,\ x\cdot\bar x > 0}
$$
be the type IV period domain of $\ten$, with its two connected components.
Let $\Gamma^K_{\En} = \Orth(\ten)$, and let $\widetilde\Delta\subset\Omega_\ten$ be the union of the hyperplane sections $\alpha^\perp$ over the vectors $\alpha\in\ten$ with $\alpha^2 = -2$; these vectors form one $\Gamma^K_{\En}$-orbit.
Then the points of $(\Omega_\ten\setminus\widetilde\Delta)/\Gamma^K_{\En}$ are in bijection with the isomorphism classes of Enriques surfaces [@AEGS25, Defs. 2.5–2.7].
The group $\Gamma^K_{\En}$ contains an isometry that exchanges the two components of $\Omega_\ten$, so this quotient is also $(\bD(\ten)\setminus\widetilde\Delta)/\Gamma^K_{\En}$ in the notation of @def:type-iv-period-domain (@lem:period-quotient-full-domain).
:::

## $ADE$ and $BC$ surfaces

::: {.notation title="Sign convention for root lattices"}

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
   The normalization of $\overline{F}^{\,\operatorname{ram}}$ is the toroidal compactification for the $\Gamma$-orbit of one chamber, which is the union of $4$ Coxeter chambers.

2. **Rational curve divisor compactification** $\overline{F}^{\,\mathrm{rc}}$.
   The polarizing divisor is $R = s + m\Sum_{i=1}^{24} f_i$, where $f_i$ are the $24$ singular fibers counted with multiplicity, and any $m\geq 1$ gives the same result.
   The normalization of $\overline{F}^{\,\mathrm{rc}}$ is the toroidal compactification for the $\Gamma$-orbit of a subdivision of the Coxeter chamber into $9$ sub-chambers.

Here $\Gamma = O^+(\latII_{1,17})$.
The Baily--Borel boundary of $F_{\mathrm{ell}}$ consists of a unique $0$-cusp and two $1$-cusps [@ABE22, Sec. 2C].
For the two $1$-cusps, with primitive isotropic planes $J\subset\latII_{2,18}$, the lattices $J^\perp/J$ are $E_8^{2}$ and $D_{16}^{+} = \latII_{0,16}$ [@ABE22, Sec. 7I, proof of Thm. 7.58].
:::
