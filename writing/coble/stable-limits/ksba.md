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

::: {.theorem #thm:no_moduli_loss title="The stable quotient determines its marked Coble root"}

Let $\mathcal{C}\iscontainedin\fentwo$ be the Coble locus, the image of the Heegner divisor $\bD(T_\Co) = \bD(\ten)\intersect\delta^{\perp}$, and let $\overline{\mathcal{C}}$ be its closure in the semitoroidal compactification $\overline F^{\En,2}$, whose normalization is the KSBA compactification $\ksbacpt{\fentwo}$ by @thm:fen2-ksba-pair and [@AEGS25, Thm. 5.9, printed p. 31].
Write $\Gamma_{\Co} = \Stab_{\gent}(\ZZ\delta)$ for the stabilizer of the root line, so that the normalization of $\mathcal{C}$ is $\bD(T_\Co)/\Gamma_{\Co}$ (@cor:coble-root-orbit-unique).

1. **The marked root.** For a primitive isotropic line $I = \ZZ e$ of $\ten$ with $\delta\in I^{\perp\ten}$, i.e. for a line representing a marked $0$-cusp of @thm:coble-cusp-admissibility(2), the **marked root** of a boundary point of $\overline{\mathcal{C}}$ over the cusp $[I]$ is the image $\bar\delta = \delta\bmod I\in K_I = e^{\perp\ten}/\ZZ e$, a root of square $-2$.
The same definition applies at a primitive totally isotropic plane $J$ with $\delta\in J^{\perp\ten}$, with $\bar\delta = \delta\bmod J\in K_J$.

2. **The determination.** The map that sends a KSBA stable pair $(\bar S, \eps R_{\bar S})$ in the closure of $\mathcal{C}$ to its marked root $\bar\delta$ is well defined: the root is determined, up to the action of the group $\gent$ of the Enriques quotient, by the isomorphism class of the pair, and two degenerations of the Coble locus whose marked roots are inequivalent under $\gent$ give nonisomorphic stable pairs.
Equivalently, the boundary components of the normalization of $\overline{\mathcal{C}}$ over a marked cusp $[I]$ are indexed by the $\gent$-orbits of admissible roots of $K_I$, so that a degeneration of the Coble locus determines its marked root through the pair alone, and degenerations that differ only in their marked root are not identified in the KSBA boundary.

3. **The mechanism.** The $\frac{1}{4}(1,1)$ singularity of @prop:coble-quarter-singularity(2) -- equivalently, the contracted anti-bicanonical $(-4)$-curve of @prop:coble-quarter-singularity(3) and @prop:antibicanonical-system -- is the geometric carrier of the marked root: two degenerations of the Coble locus that differ only in their marked root are not identified in the KSBA boundary.
Without this injectivity the restricted semifan of @conj:restricted_ramification_semifan would be too fine for the actual KSBA boundary, and the KSBA--semitoroidal comparison conjecture (@conj:ksba_semitoroidal_comparison) would fail.

:::

::: {.proof}

**The two readings.** As written, the conjecture admits a stronger reading in which the determination is required at the level of cusp orbits: that the map from $\Gamma_{\Co}$-orbits of primitive isotropic lines of $T_\Co$ to $\gent$-orbits of marked lines of $\ten$ be injective, so that two cusps of the Coble locus could never contribute to the same cusp of $\fentwo$.
That reading is false: the stable quotient $\bD(T_\Co)/\widetilde\Orth^+(T_\Co)$ has $527$ $0$-cusps (@thm:cusp-lifting) while $\fentwo$ has five, of which four carry markings (@thm:coble-cusp-admissibility(2)), so the orbit map cannot be injective.
The comparison @conj:ksba_semitoroidal_comparison does not need it: the semitoroidal model of the polarized Coble locus is $\bD(T_\Co)/\Gamma_{\Co}$ with the restricted semifan, and what it needs is that the fibers of the map to the KSBA boundary carry no two markings of the same cusp -- the reading proved here.

**The marked root is a datum of the pair.** Let $(\bar S, \eps R_{\bar S})$ be a KSBA stable pair in the closure of $\mathcal{C}$, reached along a degeneration whose period points lie in $\bD(T_\Co)$ with marked root $\delta$.
The degeneration determines a cusp $[I]$ and a face $\sigma$ of the Enriques semifan $\mathcal{F}_I$ that lies in the hyperplane $\bar\delta^{\perp}\intersect C_I$ cut by the marked root, and $\sigma$ is the boundary datum of the stable pair in $\overline F^{\En,2}$.
By @prop:coble-quarter-singularity(2) the stable quotient $\bar S = X^\sharp/\iota_{\Co}$ carries a $\frac{1}{4}(1,1)$ cyclic quotient singularity at the image of the $A_1$ point of $X^\sharp$, and by @prop:coble-quarter-singularity(3) the morphism $\mu\colon\wV\to\bar S$ contracts the anti-bicanonical curve $C$ with $C^2 = -4$ and $\abs{-2K_{\wV}} = \theset{C}$ to that point and is an isomorphism over its complement.
So the $\frac{1}{4}(1,1)$ singularity, with the position of the contracted curve, is a well defined datum of the pair $(\bar S, \eps R_{\bar S})$: it is the image of exactly one $A_1$ point of the cover, namely the node fixed by $\iota_{\Co}$, because $\mu$ is an isomorphism over the complement of the point.

**The singularity recovers the root.** The node of $X^\sharp$ is the unique $A_1$ point fixed by the Enriques involution, and the period condition that cuts the Heegner divisor is $\omega\perp\delta$ for the marked root $\delta\in\ten$; the discriminant divisor $\Delta=\alpha^{\perp}\subset\bD(\ten)/\Orth(\ten)$ that it cuts parametrizes quotients of nodal K3 surfaces by an involution fixing a node, and these are rational Coble surfaces with a $\frac{1}{4}(1,1)$ singularity [@AEGS25, §2.3, printed p. 587].
Transporting $\delta$ to the boundary lattice at the cusp gives the marked root $\bar\delta = \delta\bmod I\in K_I$, and @thm:coble-cusp-admissibility(1) certifies that $\bar\delta$ is an admissible root, that the reflection in every lift of it lies in $\gent$, and that the pair $(I, \bar\delta)$ is $\gent$-equivalent to one marked by $\delta$ itself.
Conversely, every admissible root $r$ of $K_I$ has a lift in $I^{\perp\ten}$ that lies in the $\gent$-orbit of $\delta$, so the $\gent$-orbit of the marked root is uniquely attached to the cusp by the admissibility test.
Therefore the node -- recoverable from the pair as the unique preimage of the $\frac{1}{4}(1,1)$ point -- determines the $\gent$-orbit of the marked root, and conversely two degenerations of the Coble locus with inequivalent marked roots have different nodes, hence nonisomorphic stable pairs.

**No identification.** Two degenerations of the Coble locus that differ only in their marked root have different nodes, since the marked root is the period-theoretic avatar of the node: the hyperplanes $\bar\delta_1^{\perp}$ and $\bar\delta_2^{\perp}$ cut different faces of $\mathcal{F}_I$ whenever $\bar\delta_1$ and $\bar\delta_2$ are inequivalent, for the admissibility test of @thm:coble-cusp-admissibility(1) is the certificate.
The contracted anti-bicanonical curves then lie over different points of the respective stable quotients, so the pairs are not identified in the KSBA boundary.
This is the injectivity that the restricted semifan needs: without it, the restriction of $\mathcal{F}_I$ to the hyperplane of an admissible root would coarsen or refine a face belonging to another root, and the KSBA--semitoroidal comparison would fail.
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

::: {.theorem #thm:coble-cusp-admissibility title="The admissibility test for Coble roots at a cusp"}

Let $\delta\in\ten$ be the $(-2)$ vector of @lem:coble-heegner-vector, so that $\delta^{\perp\ten} = T_\Co$.
For a primitive isotropic line $I = \ZZ e$ and a primitive totally isotropic plane $J$ of $\ten$, write $K_I = e^{\perp\ten}/\ZZ e$ and $K_J = J^{\perp\ten}/J$ for the boundary lattices of @prop:sterk-cusp-quotients.
A **marked $0$-cusp** is a $\gent$-orbit of a pair $(I, r)$ with $r$ a root of $K_I$; a **marked $1$-cusp** is a $\gent$-orbit of a pair $(J, r)$ with $r$ a root of $K_J$; $(I, r)$ is **incident** to $(J, r)$ when $I \subset J$ and the two roots have a common lift $\alpha\in J^{\perp\ten}$, whose images in $K_I$ and $K_J$ are the two roots.
Call the pair **admissible** when some lift of $r$ in $I^{\perp\ten}$, respectively $J^{\perp\ten}$, lies in the $\gent$-orbit of the Coble root $\delta$.

1. **The test.** $(I, r)$, respectively $(J, r)$, is admissible if and only if $r^2 = -2$.
   Then every lift is a $(-2)$ vector of $\ten$ orthogonal to $I$, respectively $J$, the reflection in every lift lies in $\gent$, and the pair is $\gent$-equivalent to one marked by $\delta$ itself.
2. **The $0$-cusps.** A $0$-cusp carries a marking if and only if its boundary lattice contains a class of square $-2$.
   The marked cusps are exactly Sterk's cusps $2,3,4,5$; his representatives $\eta_2,\dots,\eta_5$ are orthogonal to $\delta$, so $\delta$ itself is a lift at each of the four, and among his printed simple systems the admissible roots are exactly the white nodes: cusp $2$: his root $10$; cusp $3$: his roots $8$ and $12$; cusp $4$: his roots $8$ and $10$; cusp $5$: his roots $11$--$14$.
   His roots $10$, $8$, $8$ and $11$ are $\pm\delta$.
3. **The $1$-cusps.** A $1$-cusp carries a marking if and only if $J^{\perp\ten}$ contains a $(-2)$ vector of $\ten$, if and only if some $\gent$-translate of the plane lies in $T_\Co$.
   The four $1$-cusps whose closures contain cusp $1$ --- those of types $\{1,2\}$, $\{1,3\}$, $\{1,4\}$, $\{1,5\}$ in the type notation of [@Ste91, §4.3.15, printed p. 26] --- carry none; the remaining five, of types $\{2,4,5\}$, $\{3,4\}$, $\{3,5\}$, $\{4,5\}$ and $\{5,5\}$, each carry markings, and each has exactly $16$ classes of square $-2$ in its boundary lattice.
4. **Preservation along incidences.** If $(I, r)$ is incident to $(J, r)$, then $(I, r)$ is admissible exactly when $(J, r)$ is.
   An admissible pair at a $0$-cusp extends to an admissible pair at an incident $1$-cusp if and only if that $1$-cusp carries a marking, so the extension fails exactly along the four incidences from a marked cusp $x\in\{2,3,4,5\}$ to the $1$-cusp of type $\{1,x\}$.
   In particular the test is **not** preserved along the incidence at Sterk's cusp $3$ to the $1$-cusp $\{1,3\}$, and along the incidence at cusp $5$ to the $1$-cusp $\{1,5\}$.
:::

::: {.proof}

**(1).** Let $I = \ZZ e$ and let $\alpha\in e^{\perp\ten}$ be a lift of $r$.
Every lift is $\alpha + ke$ with $k\in\ZZ$, and $(\alpha + ke)^2 = \alpha^2$ because $\alpha\perp e$ and $e^2 = 0$; so the square of every lift equals $r^2$, and the same argument applies at a plane $J$, whose radical $J$ pairs trivially with $J^{\perp\ten}$.
If $r^2 = -2$, then $\alpha$ is a $(-2)$ vector of $\ten$, and by @cor:coble-root-orbit-unique(1) there is $g\in\gent$ with $g(\delta) = \alpha$, so some lift of $r$ lies in the $\gent$-orbit of $\delta$.
Conversely, if a lift equals $g(\delta)$, then $r^2 = \delta^2 = -2$.
For the reflection: a $(-2)$ vector $\alpha$ of $\ten$ has $s_\alpha(x) = x + (x, \alpha)\alpha$ for every $x$ of the dual lattice $\ten^*$, and $(x,\alpha)\in\ZZ$, so $s_\alpha$ maps every class of $A_{\ten} = \ten^*/\ten$ to itself; hence $s_\alpha$ lies in the discriminant kernel, which is contained in $\gent$ by @prop:sterk-group-identification(2).
This holds for every lift of $r$, each of which is again a $(-2)$ vector by the first paragraph; in contrast to the $(-4)$ roots, no discriminant condition on a lift intervenes (@lem:sterk-reflection-lift-criterion(3)).
Finally, if $g(\delta) = \alpha\perp e$, then $g^{-1}$ carries the pair $(I, r)$ to the pair $(\ZZ g^{-1}(e), \bar\delta)$, where $\bar\delta$ is the image of $\delta$ in $g^{-1}(e)^{\perp\ten}/\ZZ g^{-1}(e)$ and $g^{-1}(e)$ is an isotropic vector of $T_\Co$.

**(2).** A $0$-cusp $[I]$ carries a marking exactly when some root $r$ of $K_I$ has $r^2 = -2$: such an $r$ is admissible by (1), and an admissible $r$ has that square.
For cusp $1$, @prop:sterk-cusp-quotients gives $K_{\eta_1} \cong U(2)\oplus E_8(2)$, in which every square is a multiple of $4$: a vector $ae'+bf'$ of the $U(2)$ summand has square $4ab$, and the $E_8(2)$ summand is twice an even lattice.
So cusp $1$ carries no marking.
For cusps $2$--$5$ the pairing $\delta\cdot\eta_j$ decides.
Write $\ten$ in the basis $e, f, e', f', \alpha_1,\dots,\alpha_8$ of @prop:sterk-cusp-quotients, so that $u = e$, $w = f$, $\delta = u - w$, and $\bar\alpha_i$ is the dual basis of the $E_8(2)$ summand.
Each of $\eta_2 = e'$, $\eta_3 = e'+f'+\bar\alpha_8$ and $\eta_4 = 2e'+f'+\bar\alpha_1$ lies in the $U(2)\oplus E_8(2)$ summand, on which $\delta$ vanishes, and $\eta_5 = 2e+2f+\bar\alpha_1$ has $U$-part $2u+2w$ with $\delta\cdot(2u+2w) = -2+2 = 0$ and $E_8(2)$-part on which $\delta$ vanishes.
So $\delta\perp\eta_j$ for $j = 2,\dots,5$, the image of $\delta$ in $K_{\eta_j}$ is a root of square $-2$, and $\delta$ itself marks the cusp; cusp $1$ is excluded by the lattice type just given, so the marked cusps are exactly $2,3,4,5$ [@Ste91, Prop. 4.2.3, printed p. 16].
The inventory of the admissible printed roots, with the identifications of the white nodes with $\pm\delta$, is the first half of `computations/reports/coble_cusp-admissibility-run.txt`, which also verifies that the reflection in every lift $r + k\eta_j$, $-6\leq k\leq 6$, of every white node lies in $\gent$.

**(3).** The first equivalence repeats the argument of (2) at a plane: a marking exists exactly when some root of $K_J$ has square $-2$, and the classes of square $-2$ of $K_J$ are exactly the images of the $(-2)$ vectors of $\ten$ in $J^{\perp\ten}$, because every lift of such a class lies in $J^{\perp\ten}$ with the same square.
For the second equivalence, if $[J]$ carries a marking with lift $\alpha = g(\delta)$, then $\delta\perp g(J)$, so the translate $g(J)$ lies in $\delta^{\perp\ten} = T_\Co$; conversely a translate contained in $T_\Co$ is orthogonal to $\delta$, and $\delta$ is a $(-2)$ vector.
For the exclusion of the four types containing $1$: if some translate $g(J)$ lies in $T_\Co$, then every primitive isotropic line of $g(J)$ lies in $T_\Co$ and has even divisibility in $\ten$ by @prop:coble-isotropic-even-in-ten, so no line of the plane represents cusp $1$, and the type of the plane in the notation of [@Ste91, §4.3.15, printed p. 26] avoids $1$.
The four $1$-cusps whose closures contain cusp $1$ are exactly the four of Sterk's first kind, built from two inequivalent isotropic vectors [@Ste91, §4.3.16, printed p. 27], and they are of types $\{1,2\}$, $\{1,3\}$, $\{1,4\}$, $\{1,5\}$: cusp $1$ is incident with four $1$-cusps [@AEGS25, Lemma 5.2, printed p. 610], all of the first kind, since none of the five remaining types listed at [@Ste91, §4.3.17, printed p. 28] contains $1$, and the four first-kind types are then forced by the incidence counts $4,2,3,4,5$.
The verdicts, the counts of $16$ classes of square $-2$, and explicit $(-2)$ vectors in $J^{\perp\ten}$ witnessing them, are the second half of `computations/reports/coble_cusp-admissibility-run.txt`: the maximal parabolic subdiagrams of Sterk's five printed diagrams, with their radicals saturated to planes, realize exactly the nine $1$-cusps of the diagram of [@Ste91, §4.4, Fig. 14, printed p. 28], with the incidences that figure shows, and the count of square-$(-2)$ classes is the same for every representative of a given type.
At each of the five second-kind types the transcript exhibits a printed parabolic subdiagram whose radical is orthogonal to $\delta$, so that the plane of Sterk's representative and that radical lies in $T_\Co$ and is marked by $\delta$ itself.

**(4).** If $(I, r)$ is incident to $(J, r)$ with common lift $\alpha$, then $(I, r)$ is admissible exactly when $r^2 = -2$ exactly when $(J, r)$ is, by (1).
For the extension statement, let $[I]$ be a marked $0$-cusp, so that after applying an element of $\gent$ the line is spanned by an isotropic vector $e$ of $T_\Co$ and the marking is by $\delta$; let $[J]$ be incident to $[I]$.
If some representative $J'$ of $[J]$ lies in $T_\Co$ and contains a vector of the class of $[I]$, then $I' \subset J' \subset T_\Co$ with $\delta\perp J'$, and the pair $(I', \bar\delta)$ is incident to the admissible pair $(J', \bar\delta)$.
Such a $J'$ exists exactly when $[J]$ carries a marking, by (3), and the class of $[I]$ occurs among the lines of $J'$ because the type of $J'$ is the type of $[J]$.
Conversely, if an admissible pair at $[I]$ is incident to a pair at $[J]$, then that pair is admissible by the first sentence, so $[J]$ carries a marking.
The four failures are read off the cusp diagram: each marked cusp $x\in\{2,3,4,5\}$ is incident with exactly one $1$-cusp of a type containing $1$ [@Ste91, §4.4, Fig. 14, printed p. 28], that $1$-cusp is unmarked by (3), and every other incidence from $x$ ends at a marked $1$-cusp.
:::

::: {.remark #rmk:cusp-admissibility-reflection title="Why no reflection data intervenes at cusps $3$ and $5$"}

The question asked whether additional reflection data intervenes at Sterk's cusps $3$ and $5$, where the folding involutions of [@AEGS25, Lemma 3.10, printed p. 594] are composed with lattice reflections.
For the admissible roots it does not: by @thm:coble-cusp-admissibility(1) the reflection in every lift of a square-$(-2)$ root lies in $\gent$ unconditionally, the discriminant image of a $(-2)$ reflection being trivial, so the lift-dependence that @lem:sterk-reflection-lift-criterion(3) records for the printed $(-4)$ roots at cusps $2$, $3$ and $4$ cannot arise for the marking.
What fails at cusps $3$ and $5$ --- as at cusps $2$ and $4$ --- is the cusp-level extension along the incidence to the $1$-cusp of type $\{1,3\}$, respectively $\{1,5\}$, which carries no marking at all.
The transcript `computations/reports/coble_cusp-admissibility-run.txt` also records, for every printed parabolic subdiagram, which white nodes descend along it; that datum is a datum of Sterk's frame rather than of the $\gent$-class, since it says only that the printed root is orthogonal to the printed radical.
:::

