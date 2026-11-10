# KSBA stable limits {#sec-ksba}


## How a stable limit is obtained

::: {.proposition #prop:fen2-limits-are-k3-quotients title="Enriques stable limits are quotients of K3 stable limits"}

Let $(Z, \eps R_Z)$, $0 < \eps \ll 1$, be the pair of a degree-$2$ numerically polarized Enriques surface $Z \in \fentwo$.
Every KSBA stable limit of such pairs is the quotient of a KSBA stable limit of K3 pairs $(X, \eps R)$, $X \in \fttz$, by an Enriques involution [@AEGS25, §7.3].
:::

::: {.proposition #prop:fen2-stable-limit-strata title="Boundary strata of $\ksbacpt{\fentwo}$ from folded Coxeter diagrams"}

For $k = 1, \dots, 5$ let $G_k$ be the folded Coxeter diagram of the $0$-cusp $k$ of $\fentwo$.

1. The semifan $\semifan{F}_k$ of the $0$-cusp $k$ is the generalized Coxeter semifan (@def:generalized-coxeter-semifan) of $G_k$, with irrelevant roots the foldings of the irrelevant roots of the K3 diagrams [@AEGS25, Def. 5.4 and Lemma 5.5].

2. The faces of the Coxeter fan of $G_k$ are of two types: Type II rays, in bijection with the maximal parabolic subdiagrams of $G_k$, and Type III cones, in bijection with the elliptic subdiagrams of $G_k$ [@AEGS25, §5.1].

3. For a Type III stable limit $Z = X/\ien$ at the $0$-cusp $k$, the largest irreducible components of $X$ and of $Z$ are described by the maximal connected elliptic subdiagrams of the Coxeter diagram at that cusp. Every other irreducible component corresponds to a subdiagram of one of these that is preserved by the folding symmetry, and the components are glued according to the Coxeter diagram [@AEGS25, §7.3].

4. The irreducible components of a Type II stable limit are described by the relevant connected components of the maximal parabolic subdiagrams of $G_k$ [@AEGS25, §7.4].
:::

## A worked integral affine structure

::: {.example #ex:type-ii-ias-41 title="The Type II ray at the $1$-cusp $41$"}

Take the monodromy invariant with barycentric coordinates
$$
\ell = (0^6, 1, 0^7, 1, 0^5, 2, 2)
$$
at $0$-cusp $4$.
The resulting integral affine sphere agrees with the one built at $0$-cusp $1$ from $(0, 0, 1, 0^7, 1, 0^9, 2, 2)$, which is what it means for this ray to be shared: it is the Type II ray corresponding to the $1$-cusp labelled $41$, and it occurs as a limit of $\ias$ at either of the two $0$-cusps it joins [@AEGS25 Ex. 4.16].

Being Type II, the dual complex $\Gamma(\mcx_0)$ is a segment rather than a sphere, here of length one, and the central fiber is
$$
\mcx_0 = \wV_1 \union_E \wV_2 ,
$$
two copies of the same $\wD_8$ involution pair glued along the elliptic curves $E \in \abs{-K_{\wV_1}}$ with a twist by $2$-torsion.

The Enriques involution flips the segment $\Gamma(\mcx_0)$, so the Enriques equator is not a subcomplex of $\Gamma(\mcx_0)$ [@AEGS25, Ex. 4.16].
:::

## The polarized Coble locus

::: {.proposition #prop:gamma-co-2-line-stabilizer title="$\Gamma_{\Co, 2}$ is the stabilizer of the Heegner line"}

Let $\delta \in \ten$ be the $(-2)$ vector of @lem:coble-heegner-vector, so that $\delta^{\perp \ten} = T_\Co$, and let $\Gamma_{\Co, 2} = \Stab_{\Orth(\ten)}(T_\Co)$ as in @sec-moduli-construction.
Then
$$
\Gamma_{\Co, 2} \;=\; \Stab_{\Orth(\ten)}(\ZZ\delta)
\;\containing\; \Stab_{\Orth(\ten)}(\delta) ,
$$
and the inclusion has index $2$.
:::

::: {.proof}

Write $\ten = U \oplus U(2) \oplus E_8(2)$ with $U = \ZZ u \oplus \ZZ w$ as in @lem:coble-heegner-vector, so $\delta = u - w$ and $T_\Co = \ZZ\zeta \oplus U(2) \oplus E_8(2)$ with $\zeta = u + w$.
A vector $x = au + bw + y$ with $y \in U(2) \oplus E_8(2)$ is orthogonal to $T_\Co$ exactly when $x \cdot \zeta = a + b = 0$ and $y$ is orthogonal to $U(2) \oplus E_8(2)$.
That lattice is nondegenerate, so $y = 0$ and $x = a\delta$.
Hence $T_\Co^{\perp \ten} = \ZZ\delta$.

An isometry $g$ of $\ten$ with $g(\ZZ\delta) = \ZZ\delta$ preserves $\delta^{\perp \ten} = T_\Co$.
Conversely, if $g$ preserves $T_\Co$, then it preserves $T_\Co^{\perp \ten} = \ZZ\delta$.
So $\Stab_{\Orth(\ten)}(T_\Co) = \Stab_{\Orth(\ten)}(\ZZ\delta)$.

For $g$ in this group, $g(\delta) \in \ZZ\delta$ and $g(\delta)^2 = -2$, so $g(\delta) = \epsilon(g)\,\delta$ with $\epsilon(g) \in \theset{\pm 1}$.
The map $\epsilon$ is a homomorphism with kernel $\Stab_{\Orth(\ten)}(\delta)$.
It is surjective, since $-\id_{\ten}$ preserves $\ZZ\delta$ and $\epsilon(-\id_{\ten}) = -1$.
So the index is $2$.
:::

::: {.corollary #cor:coble-root-orbit-unique title="The $(-2)$ vectors of $\ten$ form one $\gent$-orbit"}

Let $\delta \in \ten$ be the $(-2)$ vector of @lem:coble-heegner-vector.

1. Every $(-2)$ vector of $\ten$ lies in the $\gent$-orbit of $\delta$.

2. The image in $\fentwo = \bD(\ten)/\gent$ of the union of the hyperplane sections $\bD(\alpha^{\perp})$ over all $(-2)$ vectors $\alpha \in \ten$ equals the image of $\bD(\delta^{\perp})$, and the map $\bD(\delta^{\perp}) \to \fentwo$ factors through $\bD(\delta^{\perp})/\Stab_{\gent}(\ZZ\delta)$.
:::

::: {.proof}

(1) Let $\alpha \in \ten$ have $\alpha^2 = -2$.
By @thm:coble-heegner-line-unique there is $g \in \gent$ with $g(\ZZ\delta) = \ZZ\alpha$, so $g(\delta) = \pm\alpha$.
The isometry $-\id$ of $\lkt$ preserves $\ten$ and $\tdp$, so it lies in $\gent = \Orth(\ten) \intersect \Orth(\tdp)$ (@sec-moduli-construction), and it acts on $\ten$ as $-\id_{\ten}$.
Replacing $g$ by $-g$ when $g(\delta) = -\alpha$ gives an element of $\gent$ that sends $\delta$ to $\alpha$.

(2) By (1), for each $\alpha$ there is $g \in \gent$ with $g(\bD(\delta^{\perp})) = \bD(\alpha^{\perp})$, so the two hyperplane sections have the same image in the quotient by $\gent$.
An element of $\Stab_{\gent}(\ZZ\delta)$ preserves $\delta^{\perp}$ and hence $\bD(\delta^{\perp})$, and it identifies points of $\bD(\delta^{\perp})$ that already have the same image in $\fentwo$.
So the map factors through the quotient by $\Stab_{\gent}(\ZZ\delta)$.
:::

## The KSBA stable pair

::: {.theorem #thm:fen2-ksba-pair title="The degree-$2$ Enriques stable pair"}

Let $Z$ be an Enriques surface with ADE singularities and $[\mcl_Z] \in \Pic Z/\ZZ_2$ an ample numerical polarization of degree $2$, and put $M = \mcl_Z^{\tensor 2}$.
The linear system $\abs{M}$ is basepoint free and defines a double cover $\rho \colon Z \to W$ of a quartic del Pezzo surface with $4A_1$ or $A_3 + 2A_1$ singularities.
The ramification divisor $R_Z \in \abs{M}$ of $\rho$ is ample, and the pair $(Z, \eps R_Z)$ is log canonical for $0 < \eps \ll 1$.
Hence $\fentwo$ has a compactification $\ksbacpt{\fentwo}$ in the KSBA moduli space of pairs $(Z, \eps R_Z)$ with semi log canonical singularities, $K_Z \equiv 0$ and $R_Z$ an ample $\QQ$-Cartier divisor [@AEGS25, §1].
:::

::: {.question #qst:coble-stable-pair title="Is the descended Coble pair KSBA stable?"}

Let $\bar S$ be the stable quotient surface and $R_{\bar S}$ the descended ramification divisor, and consider the pair
$$
(\bar S, \eps R_{\bar S}), \qquad 0 < \eps \ll 1 .
$$
Is $R_{\bar S}$ $\QQ$-Cartier and ample, and is $(\bar S, \eps R_{\bar S})$ slc?
For ampleness, one route descends the ample ramification divisor from the K3 cover: $K_{\bar S} + \eps R_{\bar S}$ pulls back to $\eps R_X$, with $R_X$ coming from the $(2,2)$-divisor on $Y = \PP^1 \times \PP^1$.
For the slc condition, one route runs through the du Val singularities on the K3 cover and a finite quotient that is quasi-étale in codimension one.
:::

::: {.proposition #prop:coble-quarter-singularity title="The node fixed by the involution descends to a $\frac{1}{4}(1,1)$ point"}

Let $Y = \PP^1 \times \PP^1$ with $\tau(x,y) = (-x,-y)$, let $B = (f = 0)$ be a $\tau$-invariant curve of bidegree $(4,4)$, and let $X^\sharp = \theset{z^2 = f(x,y)}$ be the double cover of $Y$ branched along $B$ [@Hor77, p. 54].
Suppose that $B$ passes through exactly one $\tau$-fixed point $p$, that the quadratic term of $f$ at $p$ is nondegenerate, and that $B$ is smooth away from $p$.
Let $\iota_{\Co}(x,y,z) = (-x,-y,-z)$; this is the formula of the Enriques involution $\ien$ of @sec-aegs-projective.

1. The curve $B$ has an ordinary node at $p$, and $X^\sharp$ has an $A_1$ singularity over $p$ that $\iota_{\Co}$ fixes.

2. The quotient $\bar S = X^\sharp/\iota_{\Co}$ has a cyclic quotient singularity of type $\frac{1}{4}(1,1)$ at the image of this $A_1$ point.

3. Let $r \colon \wX \to X^\sharp$ be the minimal resolution, with exceptional curve $E$, let $\psi \colon \wX \to \wV$ be the quotient by the lift of $\iota_{\Co}$, and let $C = \psi(E)$. Then $C^2 = -4$ and $\abs{-2K_{\wV}} = \theset{C}$. The morphism $\mu \colon \wV \to \bar S$ induced by $r$ contracts $C$ to the $\frac{1}{4}(1,1)$ point and is an isomorphism over its complement.
:::

::: {.proof}

(1) The curve $B$ has an ordinary node at $p$ by @lem:node-condition.
By the proof of @prop:local-quarter, $X^\sharp$ is analytically $\theset{xy - z^2 = 0}$ over $p$, which is an $A_1$ singularity.
This point is $(p, 0)$, because $f(p) = 0$, and $\iota_{\Co}(p, 0) = (\tau(p), 0) = (p, 0)$.

(2) This is @prop:local-quarter.

(3) $C^2 = -4$ is computed in @sec-anti-bicanonical, and $\abs{-2K_{\wV}} = \theset{C}$ is @prop:antibicanonical-system.
Let $q \colon X^\sharp \to \bar S$ be the quotient map.
The resolution $r$ commutes with the two involutions, so it induces $\mu$ with $\mu \circ \psi = q \circ r$.
Hence $\mu(C) = q(r(E))$, which is the image of the $A_1$ point, and by (2) this is the $\frac{1}{4}(1,1)$ point.
The curve $E$ is $\iota_{\Co}$-invariant, so $\psi^{-1}(C) = E$.
Over the complement of the $A_1$ point, $r$ restricts to an equivariant isomorphism $\wX \setminus E \to X^\sharp \setminus r(E)$.
So $\mu$ restricts to an isomorphism $\wV \setminus C \to \bar S \setminus \mu(C)$.
:::

## The restricted ramification semifan

::: {.conjecture #conj:restricted_ramification_semifan}

The semitoroidal model of the polarized Coble locus is obtained by restricting the Enriques ramification semifan of the degree-$2$ compactification problem to the hyperplane cut out by the Coble root, and keeping exactly those walls whose relative interiors meet the Coble positive cone.
Under this restriction, a Coble wall is irrelevant precisely when every Enriques wall restricting to it is already irrelevant.
:::

## Comparison with the KSBA compactification

::: {.conjecture #conj:ksba_semitoroidal_comparison}

After normalization, the KSBA compactification of the polarized Coble locus agrees with the semitoroidal compactification induced by the restricted ramification semifan.
:::

::: {.conjecture #conj:no_moduli_loss}

The stable quotient determines its marked Coble root: the $\frac{1}{4}(1,1)$ singularity of @prop:coble-quarter-singularity -- equivalently, the contracted anti-bicanonical $(-4)$-curve on the resolution -- recovers it, so that degenerations differing only by their marked root are not identified.
Without this injectivity the restricted semifan would be too fine for the actual KSBA boundary, and the KSBA--semitoroidal comparison conjecture (@conj:ksba_semitoroidal_comparison) would fail.
:::

## Boundary cusp data

::: {.proposition #prop:coble-isotropic-even-in-ten title="Isotropic vectors of $T_\Co$ have even divisibility in $\ten$"}

Let $\eta \colon T_\Co \injects \ten$ be the primitive embedding of @lem:primitive_embedding_eta.
For every isotropic $e \in T_\Co$, every value $\eta(e) \cdot x$ with $x \in \ten$ is even.
Hence, for $e$ primitive and nonzero, $\div_{\ten}(\eta(e))$ is even, and the line $\ZZ\eta(e)$ lies in the $0$-cusp $(10,8,0)_1$ of $F^K_{\En}$.
:::

::: {.proof}

By @cor:eta-is-heegner-complement, $\eta(T_\Co) = \ZZ\zeta \oplus U(2) \oplus E_8(2)$ inside $\ten = U \oplus U(2) \oplus E_8(2)$, with $U = \ZZ u \oplus \ZZ w$ and $\zeta = u + w$.
Write $\eta(e) = a\zeta + y$ with $a \in \ZZ$ and $y \in U(2) \oplus E_8(2) = E_{10}(2)$.
The lattice $E_{10}$ is even, so $y^2 \in 4\ZZ$.
From $0 = \eta(e)^2 = 2a^2 + y^2$ it follows that $a^2$ is even, so $a$ is even.
Now $\eta(e) \cdot u = \eta(e) \cdot w = a$, and $\eta(e) \cdot z = y \cdot z \in 2\ZZ$ for $z \in E_{10}(2)$.
These vectors span $\ten$, so every value $\eta(e) \cdot x$ is even.

For $e$ primitive and nonzero, $\eta(e)$ is primitive and isotropic in $\ten$, and its divisibility is even.
The two $0$-cusps of $F^K_{\En}$ are distinguished by the divisibility $1$ or $2$ of a primitive isotropic vector [@AEGS25, §3.2].
By @thm:cusp_correspondence the vector $\eta(v_1)$ has divisibility $2$ and boundary lattice $(10,8,0)_1$.
So the divisibility-two $0$-cusp is $(10,8,0)_1$, and $\ZZ\eta(e)$ lies in it.
:::

::: {.question #qst:coble_cusp_admissibility}

Model a $0$-cusp marked with a Coble root as an orbit of pairs $(I, r)$, with $I$ a primitive isotropic line and $r$ a Coble root compatible with $I$, and a marked $1$-cusp as an orbit of pairs $(J, r)$ with $J$ a primitive isotropic plane; $(I, r)$ is incident to $(J, r)$ when $I \subset J$.
Admissibility requires at least that $r$ lifts to a $(-2)$ vector of $\ten$, and by @cor:coble-root-orbit-unique every such vector lies in the $\gent$-orbit of the Coble root.
What is the precise admissibility test for Coble roots at a cusp, formulated against the folded K3-to-Enriques Coxeter data, and is it preserved along each incidence $I \subset J$?
Sterk cusps $3$ and $5$ are the delicate cases where additional reflection data may intervene.
:::
