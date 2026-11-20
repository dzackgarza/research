# KSBA stable limits {#sec-ksba}


## How a stable limit is obtained

::: {.construction #cons:degree-two-k3-affine-sphere title="The degree-two K3 affine sphere" defines="integral affine disc $P(\lambda)$; $B(\lambda)$; integral affine ramification divisor $R_{\mathrm{IA}}$; $a_i$; $b_i$"}

For the degree-two K3 moduli space $F_2$, let $K$ be a fundamental chamber of the Coxeter fan in $N=U\oplus E_8(-1)^2\oplus A_1(-1)$. A class $\lambda\in K$ determines a nef class $L$ on the rational surface $T$ used in [@AET23, §§5–6]. First take $\lambda$ in the open chamber, with all length parameters positive. Start with the moment polygon of a toric model of $(T,L)$. It has eighteen sides, indexed $0,\ldots,17$. Perform Symington surgeries of positive sizes $b_{18},b_{19},b_{20}$ on sides $0,6,12$. The resulting integral affine disc $P(\lambda)$ has three interior $I_1$ singularities [@AET23, Construction 6.1].

The construction uses twenty-four nonnegative root pairings $a_i=\lambda\cdot r_i$, indexed $0,\ldots,23$. In the normalization of [@AET23, §6A], their associated length parameters $b_i$ satisfy $a_i=b_i$ for even $0\leq i<18$ and $a_i=2b_i$ for the other indices. The roots span the rank-$19$ cusp lattice, so these numbers satisfy linear relations; arbitrary twenty-four positive parameters do not define a closed polygon. In particular, if $u_0,\ldots,u_{17}$ are the oriented primitive tangent vectors of its sides and $\ell_i$ their affine lengths, closure requires $\sum_{i=0}^{17}\ell_i u_i=0$. The first eighteen parameters control the equator. The three surgery sizes $b_{18},b_{19},b_{20}$ measure the distances of the interior singularities from sides $0,6,12$; $b_{21},b_{22},b_{23}$ measure the distances of those same singularities to the opposite sides $9,15,3$. Doubling copies the three singularities into the other hemisphere. Thus the six latter parameters describe three singularities from both sides of the same disc, subject to the rank-$19$ relations, rather than six independent surgery sizes [@AET23, Construction 6.1 and Remark 6.4].

::: {#fig-k3-coxeter-19-1-1 .figure}
\begin{tikzpicture}[scale=0.56]
\pic {object=coxeter/vinberg-19-1-1};
\end{tikzpicture}

The Coxeter--Vinberg diagram (@def:coxeter-vinberg-diagram) of the cusp lattice $U\oplus E_8(-1)^2\oplus A_1(-1)$; the full diagram also contains the four parabolic types that label the degree-two K3 $1$-cusps [@AET23, §5A, Fig. 1 and §3B].
:::

The reflection group $W(N)$ acts on the positive cone (@not:reflection-groups-sign-convention), and the chamber $K$ is a fundamental domain. Its diagram has an $S_3$ symmetry; more precisely $\operatorname O^+(N)=S_3\ltimes W(N)$ [@AET23, §4, Lemma 4.4]. Thus the four parabolic labels above are types modulo this symmetry, while individual parabolic subdiagrams can occur more than once in the full diagram.

![The toric fan with eighteen rays used to form the starting polygon.](/rendered/toric18.jpg){#fig-k3-toric-eighteen}

![The starting eighteen-sided polygon.](/rendered/toric18polytope.jpg){#fig-k3-eighteen-gon}

![The polygon after three interior surgeries on sides $0,6,12$.](/rendered/toric18polytope2.jpg){#fig-k3-surgery-polygon}

Glue $P(\lambda)$ to an oppositely oriented copy along the boundary. The gluing has an $I_1$ singularity at each of the eighteen corners. Thus
$$
B(\lambda)=P(\lambda)\cup_{\partial P(\lambda)}P(\lambda)^{\mathrm{op}}
$$
is an integral affine sphere with twenty-four $I_1$ singularities when all length coordinates are positive. The involution exchanges its hemispheres. Its integral affine ramification divisor $R_{\mathrm{IA}}$ lies on the equator, with weight $2$ on even indexed sides and weight $1$ on odd indexed sides [@AET23, Construction 6.1 and Def. 6.2]. A triangulation by unit lattice triangles, invariant under the involution and containing the equator, prescribes anticanonical components and their double-curve incidences through @prop:kulikov-ias-gluing [@AE22, §8.4].

![The doubled disc with its equator and the hemispherical singularities.](/rendered/IASPuPop.jpg){#fig-k3-doubled-disc}

![A schematic unit triangulation of one hemisphere.](/rendered/IAScompletetriang.jpg){#fig-k3-hemisphere-triangulation}

![The paired triangulations on the integral affine sphere.](/rendered/IASdoubletriang.jpg){#fig-k3-doubled-triangulation}
:::

When length coordinates reach zero, the singularities of $B(\lambda)$ can collide: a vertex of larger charge then corresponds to an anticanonical component with several interior blowups. On isotropic boundary rays the sphere can collapse to an interval. The Coxeter fan divides the positive cone by the combinatorial type of $(B(\lambda),R_{\mathrm{IA}})$ [@AET23, Intro. and §§6A–6B]. This construction supplies the combinatorial type of a Kulikov central fiber. Its stable pair is obtained by the subsequent contraction in [@AET23, §7].

The involution determines the ramification divisor in the generic equatorial components, but the flat limit $R_0$ need not equal the scheme-theoretic fixed locus $\operatorname{Fix}(\iota_0)$ on a nongeneric Kulikov central fiber. It is the Cartier divisor obtained by pulling back the fixed divisors from the stable equatorial models. Even when the involution extends only birationally across the total family, [@AET23, Remark 6.22, Lemma 6.34, and Theorem 6.35] proves that this $R_0$ is the flat limit of the ramification divisors. This is the precise recognizability statement used to identify the ramification semifan.

For $\lambda$ in the open Coxeter chamber, the degree-two K3 stable limit is the maximal degeneration made from eighteen copies of $(\PP^2,L+C)$, with a line $L$ and a conic $C$ on each. Successive gluings identify lines with lines and conics with conics, while the fixed lines form a Cartier ramification divisor [@AET23, Example 7.4]. On boundary rays, four Type II possibilities correspond to the $\widetilde A_{17}$, $\widetilde D_{10}\widetilde E_7$, $\widetilde E_8^2\widetilde A_1$, and $\widetilde D_{16}\widetilde A_1$ parabolic subdiagrams [@AET23, §3B and Thm. 7.5]. These are stable-pair types; a choice of Kulikov model can still change by flops before contraction.

For the $2$-elementary lattices $T=(10+k,10-k,\delta)$ with $1\leq k\leq9$, the equatorial cycle of the Coxeter diagram has $2k$ white vertices, alternating single and double circles. Each edge of the cycle gives a component $(\PP^2,D_1+D_2)$ with $D_1$ a line and $D_2$ a conic. An odd single-circle vertex gives the line side; an even double-circle vertex gives the conic side. If $\alpha_i$ is its root and $\lambda$ an integral class in the open chamber, the pairing $\ell_i=\lambda\cdot\alpha_i$ is the length of the corresponding equatorial chain. The odd-indexed chains are of toric involution type E1, with fixed locus a fiber and two points; the even-indexed chains are of type E2, with two fixed fibers. The remaining pairings locate the non-toric surfaces in the hemispheres, which contain $12-k$ exchanged pairs of single-blowup anticanonical components. The chosen invariant triangulation fixes the remaining toric components and their incidence data [@AE22, §8, Lemma on equatorial toric pairs and "Models for $T=(10+k,10-k,\delta)$"].

The unique limit asserted by separatedness of the stable-pair moduli problem is the stable pair after contraction, not a unique normal-crossings central fiber or smoothing family. The same integral affine triangulation permits different gluing data, and Kulikov models of a given punctured degeneration may differ by flops [@AE22, §6.2; @AET23, §§6–7]. The recognizable divisor controls the stable contraction across these choices.

For Enriques degenerations the quotient complexes are $\RP^2$ and a disc in Type III, and a segment in Type II (@prop:enriques-quotient-dual-complex). The degree-two Enriques stable-limit components are read from the folded Coxeter diagrams (@prop:fen2-stable-limit-strata). The arithmetic test for marked Coble roots is @thm:coble-cusp-admissibility.

For a K3 quotient $\pi\colon X\to Y$ by a nonsymplectic involution, the exceptional curves on $Y$ (irreducible curves of negative self-intersection) have square $-4$, $-2$, or $-1$. A $(-4)$-curve is the image of a pointwise fixed $(-2)$-curve on $X$ and lies in the branch divisor. A $(-2)$-curve lifts to two disjoint $(-2)$-curves exchanged by the involution and misses the branch divisor. A $(-1)$-curve has two possible lifts: one invariant curve meeting the ramification divisor twice, or two exchanged curves meeting once [@AE22, Lemma 4.2]. This distinction matters when a wall of the K3 nef cone descends to a wall of a quotient stable model.

The degree-two K3 model also gives concrete boundary questions for the Enriques and Coble loci. At each Enriques cusp, which folded Coxeter walls survive the quotient by the Enriques involution? Can the K3 integral affine sphere be quotiented to an integral affine $\RP^2$ while keeping the divisor that determines its stable pair? For the Coble locus, how do the commuting Enriques and covering involutions act on the affine complex, and how does the intersection of their ramification data mark the Coble root? Which collisions of affine singularities and equator edges change the stable surface, and which are changes of Kulikov model by flops? The folded Coxeter strata below answer the component question for degree-two Enriques surfaces, and @thm:coble-cusp-admissibility supplies the arithmetic marking test. The geometric contraction question remains part of @conj:restricted_ramification_semifan. A triangulated affine complex alone does not determine a unique smoothing or stable contraction, by @def:d-semistability and [@AET23, §§6–7].

::: {.proposition #prop:fen2-limits-are-k3-quotients title="Enriques stable limits are quotients of K3 stable limits"}

Let $(Z, \eps R_Z)$, $0 < \eps \ll 1$, be the pair of a degree-$2$ numerically polarized Enriques surface (@def:enriques-surface) $Z \in \fentwo$.
Every KSBA stable limit of such pairs is the quotient of a KSBA stable limit of K3 pairs $(X, \eps R)$, $X \in \fttz$, by an Enriques involution [@AEGS25, §7.3].
:::

::: {.proposition #prop:fen2-stable-limit-strata title="Boundary strata of $\ksbacpt{\fentwo}$ from folded Coxeter--Vinberg diagrams"}

For $k = 1, \dots, 5$ let $G_k$ be the folded Coxeter--Vinberg diagram (@def:coxeter-vinberg-diagram) of the $0$-cusp $k$ of $\fentwo$.

1. The semifan $\semifan{F}_k$ of the $0$-cusp $k$ is the generalized Coxeter semifan (@def:generalized-coxeter-semifan) of $G_k$, with irrelevant roots the foldings of the irrelevant roots of the K3 diagrams [@AEGS25, Def. 5.4 and Lemma 5.5, printed p. 611].

2. The faces of the Coxeter fan of $G_k$ are of two types: Type II rays, in bijection with the maximal parabolic subdiagrams of $G_k$, and Type III cones, in bijection with the elliptic subdiagrams of $G_k$ [@AEGS25, §5.1].

3. For a Type III stable limit $Z = X/\ien$ at the $0$-cusp $k$, the largest irreducible components of $X$ and of $Z$ are described by the maximal connected elliptic subdiagrams of the Coxeter--Vinberg diagram at that cusp. Every other irreducible component corresponds to a subdiagram of one of these that is preserved by the folding symmetry, and the components are glued according to the Coxeter--Vinberg diagram [@AEGS25, §7.3].

4. The irreducible components of a Type II stable limit are described by the relevant connected components of the maximal parabolic subdiagrams of $G_k$ [@AEGS25, §7.4].
:::

## Three Type III quotient models

Write $B_k(\ell)$ for a folding-symmetric polarized integral affine sphere
at the $k$-th Enriques $0$-cusp. In the following examples
$\widetilde V_i$ is a component of the K3 Kulikov central fiber,
$V_i$ its component in the Enriques dlt quotient, and $\overline V_i$
the component after stable contraction [@AEGS25, §4.4].

::: {.example #ex:ias-cusp-three-stable-limit title="The diagonal cusp-three model"}
At cusp $3$ take
$$
\ell=(2,0^{15},2,4,6,4,0,4)\in(\ZZ_{\geq0})^{22}.
$$
The moment polygon has successive edge vectors
$(3,-3),(2,2),(-3,3),(-2,-2)$; their sum is zero. Symington
surgeries of sizes $(1,2,3,2)$ on those edges give $P(\ell)$, and
$B_3(\ell)=P(\ell)\cup P(\ell)^{\mathrm{op}}$. Its five singularities
and the two involution equators are shown in @fig-sterk3-ias.
The del Pezzo equator has weight $2$ and gives $R_{\IA}$
[@AEGS25, Ex. 4.13].

![The cusp-three integral affine sphere, Kulikov central fiber, and Enriques dlt quotient [@AEGS25, Fig. 13].](/rendered/fig_ias_sterk3_models.png){#fig-ias-stk3-three-models}

The dlt quotient has eight components. In cyclic order along the
Enriques equator they are
$$
V_1,V_2,V_4,V_6,V_8,V_7,V_5,V_3.
$$
Each double curve along this cycle contains two $A_1$ points of the
adjacent quotient components.
The pairs $(\widetilde V_6,\widetilde D_6)$ and
$(\widetilde V_7,\widetilde D_7)$ are twofold corner blowups of
$\FF_6$; $(\widetilde V_1,\widetilde D_1)$ is the four-corner blowup
of the anticanonical square in $\PP^1\times\PP^1$.
The pairs $(\widetilde V_4,\widetilde D_4)$ and
$(\widetilde V_5,\widetilde D_5)$ are $\FF_2$.
The pair $(\widetilde V_8,\widetilde D_8)$ resolves an $A_{15}$
surface: it is the sixteenfold internal blowup of $\FF_8$ at
involution-symmetric points of a section of square $8$.

The pairs $(\widetilde V_2,\widetilde D_2)$ and
$(\widetilde V_3,\widetilde D_3)$ are internal blowups of opposite
sides of an anticanonical square in $\PP^1\times\PP^1$. For the
Enriques involution $(x,y)\mapsto(x^{-1},-y)$ to lift, the two
blowup points $p,q$ must be exchanged, so $y(p)=-y(q)$. This is
the anti-invariant period condition at the crossed node of cusp $3$.

The quotient ramification divisor is supported on
$V_1\cup_{D_{18}}V_8$, with $R\cdot D_{18}=1$,
$R_1^2=0$ and $R_8^2=8$; its K3 preimage on
$\widetilde V_8$ has square $16$.
Stable contraction sends $V_2,\ldots,V_7$ to points and contracts
$V_1$ along a ruling. The stable surface has one irreducible
component, with normalization $\overline V_8$ and anticanonical
boundary $\overline D_8\cong\PP^1$ self-glued by an involution
fixing $0$ and $\infty$ [@AEGS25, Ex. 4.13].
:::

::: {.example #ex:ias-cusp-five-stable-limit title="The cusp-five model"}
At cusp $5$ take
$$
\ell=(0,0,2,0^7,1,0^3,1,0,0,0,2,0,2,6)
\in(\ZZ_{\geq0})^{22}.
$$
The polygon has successive vectors $(2,0),(-1,1),(-1,0),(0,-1)$,
whose sum is zero. A surgery of size $1$ on the $(-1,1)$ edge
gives $P(\ell)$ and hence $B_5(\ell)$. All four components of the
Kulikov central fiber are preserved by the Enriques involution.

![The cusp-five integral affine sphere, Kulikov central fiber, and Enriques dlt quotient [@AEGS25, Fig. 14].](/rendered/fig_ias_sterk5_models.png){#fig-ias-stk5-three-models}

The pairs $(\widetilde V_3,\widetilde D_3)$ and
$(\widetilde V_4,\widetilde D_4)$ are corner blowups of $D_4$
involution pairs; $(\widetilde V_2,\widetilde D_2)$ is a corner
blowup of a $D_8$ pair. The pair
$(\widetilde V_1,\widetilde D_1)$ is an internal blowup of
opposite fibers of an anticanonical square in $\FF_2$, with
the blowup points exchanged by the involution.
The K3 ramification squares are
$$
\widetilde R_1^2=0,\qquad \widetilde R_2^2=8,\qquad
\widetilde R_3^2=\widetilde R_4^2=4.
$$
In the stable Enriques limit only $V_1$ is contracted, along
a ruling. The surviving $V_3,V_4$ have type
$D_4:2={}_2'B_2^-$ and $V_2$ has type
$D_8:2={}_2'B_4^-$ [@AEGS25, Ex. 4.14 and §6].
:::

::: {.example #ex:ias-cusp-two-stable-limit title="The non-simple cusp-two model"}
At cusp $2$ take
$$
\ell=(0,1,0^7,2,0^7,1,0)\in(\ZZ_{\geq0})^{19}.
$$
The successive vectors $(0,1),(-2,0),(0,-1)$ are closed by a
horizontal base of vector $(2,0)$; no positive-size Symington
surgery is needed. The central horizontal segment is fixed by
the del Pezzo affine involution but is outside the support of
$R_{\IA}$, as required by the non-simple mirror
[@AEGS25, §4.2 and Ex. 4.15].

![The cusp-two integral affine sphere, Kulikov central fiber, and Enriques dlt quotient [@AEGS25, Fig. 15].](/rendered/fig_ias_sterk2_models.png){#fig-ias-stk2-three-models}

The K3 preimages of $V_2$ and $V_3$ each have two components
exchanged by the Enriques involution, so their periods have no
involution constraint. The pair $(V_2,D_2)$ is
$(\FF_1,\widehat L+C)$, where $\widehat L$ is the strict transform
of a line in $\PP^2$ and $C$ is a conic. Up to two corner blowups,
$(V_3,D_3)$ is the $D_8$ pair of @ex:ias-cusp-five-stable-limit.
The other two quotient pairs are images of the Enriques equator
and are toric involution quotients for
$(x,y)\mapsto(x^{-1},-y)$.

Only $V_3$ survives the stable contraction. Its normalization has
double locus $\overline D_3\cong\PP^1\cup\PP^1$, a banana curve;
each component is self-glued by an involution fixing its two nodes.
The surviving ramification divisor has square $\overline R_3^2=8$
[@AEGS25, Ex. 4.15].
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
The quotient central fiber $\mcz_0$ is nonnormal. Its normalization is
$(\wV_1,E)$, and the conductor curve $E$ is self-glued by translation
by the nonzero $2$-torsion point. In this example the dlt quotient is
already the stable model: $\overline{\mcz}_0=\mcz_0$
[@AEGS25, Ex. 4.16].
:::

## The polarized Coble locus

::: {.proposition #prop:gamma-co-2-line-stabilizer title="$\Gamma^{\mathrm{stab}}_{\Co, 2}$, the lattice stabilizer of the Heegner line"}

Let $\delta \in \ten$ be the $(-2)$ vector of @lem:coble-heegner-vector, so that $\delta^{\perp \ten} = T_\Co$, and let $\Gamma^{\mathrm{stab}}_{\Co, 2} \definedas \Stab_{\Orth(\ten)}(T_\Co)$ as in @sec-moduli-construction.
Then
$$
\Gamma^{\mathrm{stab}}_{\Co, 2} \;=\; \Stab_{\Orth(\ten)}(\ZZ\delta)
\;\containing\; \Stab_{\Orth(\ten)}(\delta) ,
$$
and the inclusion has index $2$.
The group $\Gamma_{\Co,2}$ itself is not this stabilizer: it is the monodromy group of the family of @def:coble-family-degree-two (@def:gamma-co-groups(5)), and what relates the two is the inclusion $\Gamma_{\Co,2}\leq R_{\gent}$ of @lem:d2-degree-two-base(3), not an identity.
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

Let $Z$ be an Enriques surface (@def:enriques-surface) with ADE singularities and $[\mcl_Z] \in \Pic Z/\ZZ_2$ an ample numerical polarization (@def:numerical-polarization) of degree $2$, and put $M = \mcl_Z^{\tensor 2}$.
The linear system $\abs{M}$ is basepoint free and defines a double cover $\rho \colon Z \to W$ of a quartic del Pezzo surface with $4A_1$ or $A_3 + 2A_1$ singularities.
The ramification divisor $R_Z \in \abs{M}$ of $\rho$ is ample, and the pair $(Z, \eps R_Z)$ is log canonical for $0 < \eps \ll 1$.
Hence $\fentwo$ has a compactification $\ksbacpt{\fentwo}$ in the KSBA moduli space of pairs $(Z, \eps R_Z)$ with semi log canonical singularities, $K_Z \equiv 0$ and $R_Z$ an ample $\QQ$-Cartier divisor [@AEGS25, Def. 2.10].
:::

::: {.definition #def:coble-descended-ramification title="The descended ramification divisor $R_{\bar S}$ of a stable limit" defines="descended ramification divisor; $R_{\bar S}$"}

Let $(\bar S, \eps R_{\bar S})$, $0 < \eps \ll 1$, be a KSBA stable limit of the pairs $(Z, \eps R_Z)$ of @thm:fen2-ksba-pair, and let $\rho \colon \bar S \to W$ be the morphism to the quotient by the descended del Pezzo involution, so that $\bar S$ is the quotient of a K3 stable limit by the Enriques involution (@prop:fen2-limits-are-k3-quotients).
Then $R_{\bar S}$ is the divisorial part of the ramification divisor of $\rho$ that is not contained in the double locus of $\bar S$ [@AEGS25, §2.4, printed p. 588].
For the dlt models of @prop:fen2-stable-limit-strata(3), $R_{\bar S} = \tfrac{1}{2}\rho^*(B_W)$ is a reduced divisor and equals the image of the invariant ramification divisor of the K3 cover [@AEGS25, Prop. 6.1(2), printed p. 616].
On a Type III stable limit the boundary of the Coxeter diagram of the cusp represents $R_{\bar S}$: a cycle at cusps $1$ and $5$, and a chain at cusps $2$, $3$ and $4$ [@AEGS25, §7.3, printed p. 622].
:::

::: {.question #qst:coble-stable-pair title="Is the descended Coble pair KSBA stable?"}

Let $\bar S$ be the stable quotient surface and $R_{\bar S}$ the divisor of @def:coble-descended-ramification, and consider the pair
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
Let $\iota_{\Co}(x,y,z) = (-x,-y,-z)$; this is the formula of the Enriques involution $\ien$ (@def:enriques-surface) of @sec-aegs-projective.

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

The semitoroidal model of the polarized Coble locus is obtained by restricting the Enriques ramification semifan of the degree-$2$ compactification problem to the hyperplane cut out by the Coble root, and keeping exactly those walls whose relative interiors meet the Coble positive cone (@not:reflection-groups-sign-convention).
Under this restriction, a Coble wall is irrelevant precisely when every Enriques wall restricting to it is already irrelevant.
:::

## Comparison with the KSBA compactification

::: {.conjecture #conj:ksba_semitoroidal_comparison}

After normalization, the KSBA compactification (@def:ksba-compactification) of the polarized Coble locus agrees with the semitoroidal compactification (@def:semitoroidal-compactification) induced by the restricted ramification semifan.
Degenerations at a marked cusp whose marked roots lie in different $\Gamma_{\Co,2}$-orbits are then not identified in the KSBA boundary.
That marked-root statement is @conj:no_moduli_loss, and as a statement it is the boundary Torelli statement that an isomorphism of stable pairs over the cusp induces an element of $\Gamma_{\Co,2}$ carrying one marked root to the other, with the converse.
It is one of the four inputs this identification records (A7, research#650), so the identification cannot be used to establish it.
:::

::: {.proposition #prop:ksba-period-extension-conditional title="Period extension under the compactification comparison"}

If @conj:ksba_semitoroidal_comparison holds, then the period map of the polarized Coble locus extends from the normalization of its KSBA compactification (@def:ksba-compactification) to the Baily--Borel compactification of its period quotient.
:::

::: {.proof}

Under the conjectured identification, the normalized KSBA space is semitoroidal. Compose this identification with the semitoroidal morphism to the Baily--Borel compactification in @cor:toroidal-to-baily-borel. On the interior, the composite is the original period map.
:::


::: {.proposition #prop:marking-line-no-coble-lift title="The marking-line root of a marked cusp lies in no $\Gamma_{\Co,2}$-orbit"}

At each marked cusp $[I]$ among Sterk's cusps $3$, $4$ and $5$, with representative $\eta_I \in T_\Co = \delta^{\perp\ten}$ and boundary lattice $K_I = \eta_I^{\perp\ten}/\ZZ\eta_I$, the marking-line root $[\pm\delta] \in K_I$ has $\delta$-pairing $-\delta^2 = 2 \neq 0$.
Every lift $\pm\delta + k\eta_I$ with $k \in \ZZ$ pairs with $\delta$ as $\pm\delta^2 = \mp 2 \neq 0$, so no lift lies in $T_\Co = \delta^{\perp\ten}$, and the marking-line root lies in no $\Gamma_{\Co,2}$-orbit.
:::

::: {.proof}
At the marked cusps the representative is orthogonal to the Coble root, $\eta_I \cdot \delta = 0$ (`computations/reports/coble_cusp-admissibility-run.txt`), and every lift therefore pairs with $\delta$ as $\pm\delta^2 + k(\eta_I \cdot \delta) = \mp 2 + 0 \neq 0$.
A vector of $T_\Co = \delta^{\perp\ten}$ pairs trivially with $\delta$, so no lift lies in $T_\Co$, and $R_{\gent}$ is a subgroup of $\Orth(T_\Co)$ by @prop:gamma-co-images(3): the marking-line root is outside the domain of the group.
The white nodes certify which root is the marking line: at cusps $3$ and $4$ it is Sterk's label $8$, at cusp $5$ his label $11$, each certified ``is $\pm\delta$: True'', and the root vectors carry $U$-coordinates $(-1, 1)$, of $\delta$-pairing $2$, while the remaining admissible roots carry $U$-coordinates $(1, 1)$, of $\delta$-pairing $0$ (`computations/reports/coble_cusp-admissibility-run.txt`, `computations/reports/coble_enriques-white-root-facets-run.txt`).
:::

::: {.theorem #thm:face-irrelevant-marking title="Every admissible $T_\Co$-root at a marked cusp cuts the same cone of the restricted semifan"}

Let $[I]$ be a marked $0$-cusp among Sterk's cusps $3$, $4$ and $5$, with boundary lattice $K_I = \eta_I^{\perp\ten}/\ZZ\eta_I$, fundamental chamber $\mathfrak{C}_I$ of the reflection group of $K_I$, and restricted Enriques semifan $\semifan{F}_I$ whose irrelevant roots are the foldings of the irrelevant roots of the K3 diagram (@prop:fen2-stable-limit-strata(1)).
For a simple root $r$ of $K_I$, that is a vertex of the Coxeter diagram $G_I$ of the cusp, let $\mathfrak{f}(r)$ be the cone of $\semifan{F}_I$ whose relative interior contains the relative interior of $r^{\perp}\intersect\mathfrak{C}_I$; it is unique, and one exists, because the relative interiors of the cones of $\semifan{F}_I$ partition its support. Of the two objects the question offers this is the smallest cone, and not the restricted fan: the fan $r^{\perp}\intersect\semifan{F}_I$ lies in a hyperplane that depends on $r$, so two of them are compared only after an identification is chosen, whereas $\mathfrak{f}(r)$ is a cone of the one semifan $\semifan{F}_I$ and is comparable without one. The restricted fan is not computed here.

1. If $r$ is relevant then $\mathfrak{f}(r)$ is the wall $r^{\perp}\intersect\overline{\mathfrak{C}_I}$, of codimension one in $\mathfrak{C}_I$. If $r$ is irrelevant then $\mathfrak{f}(r)$ is the maximal cone $\mathfrak{C}_I^{\mathrm{gen}} = \bigcup_{h\in W^{\mathrm{irr}}_I} h(\mathfrak{C}_I)$ of $\semifan{F}_I$, and that value does not depend on which irrelevant root $r$ is.

2. Every admissible $T_\Co$-root is irrelevant: at cusp $3$ Sterk's label $12$, at cusp $4$ his label $10$, at cusp $5$ his labels $12$, $13$ and $14$.

3. At cusp $5$ the three admissible $T_\Co$-roots lie in pairwise distinct classes of $K_5$ (`computations/reports/coble_coble-root-orbits-run.txt`), and
$$\mathfrak{f}(r_{12}) = \mathfrak{f}(r_{13}) = \mathfrak{f}(r_{14}) = \mathfrak{C}_5^{\mathrm{gen}} .$$

So a face of the restricted semifan cannot separate the three marked roots at cusp $5$: they cut one and the same cone. What a face could separate is a pair of roots of different $\Gamma_{\Co,2}$-orbits, and at the marked cusps every admissible $T_\Co$-root is irrelevant, so it is no face that separates them.
:::

::: {.proof}

**(1).** By @def:generalized-coxeter-semifan the maximal cones of $\semifan{F}_I$ are $\mathfrak{C}_I^{\mathrm{gen}}$ and its $W$-images, and by [@AEGS25, §5.2, printed p. 610] the semifan is the coarsening of the Coxeter fan obtained by removing the faces $\bigcap_j \alpha_j^{\perp} \intersect C$ in which all $\alpha_j$ are irrelevant roots. A point $x$ in the relative interior of $r^{\perp}\intersect\mathfrak{C}_I$ lies in the relative interior of the facet $r^{\perp}\intersect\overline{\mathfrak{C}_I}$ of the chamber; that facet is the face $\bigcap_j \alpha_j^{\perp} \intersect C$ of the definition for the single root $r$, so it is removed exactly when $r$ is irrelevant. If $r$ is relevant the facet is not removed, it is a cone of $\semifan{F}_I$, and $\mathfrak{f}(r)$ is it. If $r$ is irrelevant the facet is removed: its two sides are the interiors of $\mathfrak{C}_I$ and of $s_r(\mathfrak{C}_I)$, and $s_r \in W^{\mathrm{irr}}_I$, so both chambers lie in the single maximal cone $\mathfrak{C}_I^{\mathrm{gen}}$, in whose relative interior $x$ then lies. The value depends on $\mathfrak{C}_I$ and on the set of irrelevant roots only, not on $r$; and if the face cut by $r^{\perp}$ is read instead as the unordered pair of maximal cones on its two sides, every irrelevant root gives the pair $(\mathfrak{C}_I^{\mathrm{gen}}, \mathfrak{C}_I^{\mathrm{gen}})$, again the same for all of them.
At cusps $3$ and $5$ the group $W^{\mathrm{irr}}_I$ is infinite, so $\mathfrak{C}_I^{\mathrm{gen}}$ is not finitely generated and $\semifan{F}_I$ is not a fan [@AEGS25, Lemma 5.6, printed p. 611]; the maximal cones are still the unions of chambers and their $W$-images [@AEGS25, §5.2, printed p. 610], which is all that the argument uses.

**(2).** Each printed root of Sterk's diagram is a folding of the K3 roots of [@AEGS25, Fig. 5, printed p. 592], and by [@AEGS25, Def. 5.4, printed p. 611] a folded root is irrelevant exactly when the roots it folds are outside the boundary $0$--$15$ of the square, respectively $2$--$18$ of the triangle [@AEGS25, §5.2, printed p. 610]. `computations/reports/coble_irrelevant-marking-face-run.txt` prints the constituents of every folded root, asserts each against the library's own expression, and reads off: cusp $3$, label $12$ is the folding of the printed nodes $21$, $17$, $17$, and labels $10$ and $11$ of $16$, $18$ and $21$, $19$, $19$; cusp $4$, label $10$ is the folding of $16$, $19$ and label $11$ of $17$, $18$; cusp $5$, label $11$ is the folding of $16$ and labels $7$, $9$, $12$, $13$, $14$ of $20$, $21$, $17$, $18$, $19$. Every constituent lies in $16$--$21$, so each of the listed roots is irrelevant. At cusp $5$ the printed order and the library's vertex order differ, and the record enumerates all eight permutations of the library order that carry one labelled Gram matrix to the other, and obtains the same set of printed labels under each; at cusps $3$ and $4$ the two orders agree.
That no admissible root at cusp $5$ is relevant is consistent with the count of [@AEGS25, Lemma 5.8, printed p. 611]: the semitoroidal compactification has $3 + 0$ divisors at cusp $5$, so no Type III cone survives the coarsening there, and the wall of a relevant root is one.

**(3).** For two of the three root vectors $r_a$, $r_b$ the record computes the rank over $\QQ$ of the pair $(\eta_5, r_a - r_b)$ and obtains $2$ in all three cases. A difference in $\eta_5^{\perp\ten}$ that is not a rational multiple of $\eta_5$ is not a class difference in $K_5$, so the three classes are distinct. With (2) each of the three is irrelevant, so (1) gives the common value $\mathfrak{C}_5^{\mathrm{gen}}$; the fold data of `computations/reports/coble_irrelevant-marking-face-run.txt` print that value, and the same one at cusps $3$ and $4$, where the single admissible root leaves no pair to compare.
Distinct classes are not distinct $\Gamma_{\Co,2}$-orbits, and the difference decides the question: let $r$ be a root of $K_I$ orthogonal to $\delta$ and $s_r$ the reflection in it. Then $s_r$ is an isometry of $\ten$, since a root of a $2$-elementary lattice satisfies $2\div(r) \in (r\cdot r)\ZZ$ [@AEGS25, §3.4]; it preserves $\ZZ\delta$, so it lies in the lattice stabilizer $\Gamma^{\mathrm{stab}}_{\Co,2} = \Stab_{\Orth(\ten)}(\ZZ\delta)$, which contains $\Stab_{\Orth(\ten)}(\delta)$ with index $2$ and is *not* the monodromy group (@prop:gamma-co-2-line-stabilizer); its restriction to $T_\Co$ lies in $R_{\gent}$ (@prop:gamma-co-images(3)); and it fixes $\eta_I$, so it acts on $K_I$ and carries the class of $r$ to the class of $-r$. Those are different classes, because $2r \in \ZZ\eta_I$ would make the non-isotropic $r$ a rational multiple of the isotropic $\eta_I$. The computation of classes therefore does not decide the $R_{\gent}$-orbits of the three classes at cusp $5$, nor a fortiori the $\Gamma_{\Co,2}$-orbits, which refine them; and it is those orbits, not the faces, that @thm:no-moduli-loss turns on.
The boundary lattice's own invariants do not decide them either: the complements $r^\perp_{K_5}$ of the three classes are all the even lattice of rank $9$, determinant $512 = 2^9$, signature $(1,8)$ and coparity $\delta = 1$, hence isometric, since an indefinite even $2$-elementary lattice is determined by its signature and the triple $(r, a, \delta)$ [@AEGS25, §2.3] (`computations/reports/coble_cusp5-complement-isometry-run.txt`: all three print `rank 9, det 512, signature (1, 8), Smith [2^9], even True, coparity delta 1`). So no invariant of $K_5$ separates the three classes, and what decides the pair $(12,13)$ is the group. The reflection route is closed outright: the square-$(-2)$ printed roots at cusp $5$ are pairwise orthogonal, and neither a sum nor a difference of two of them is a root, so a reflection in any of them fixes the other two classes up to sign and no product of such reflections carries one class to another (`computations/reports/coble_cusp5-class-orbits-run.txt`, section (0)); under the eleven roots that fix both $\delta$ and $\eta_5$ each orbit still passes $20\,001$ classes without closing and none contains another; the one cusp symmetry that fixes the Coble root's label and exchanges the labels of $13$ and $14$ **lifts**: its linear action fixes $\delta$ itself, and since $T_\En = S \perp S^\perp$ with $S$ the rank-$10$ span of the roots and $S^\perp$ of determinant $-4$, the map equal to that action on $S$ and to the identity on $S^\perp$ is an integral isometry of $T_\En$ fixing $\delta$ (`computations/reports/coble_759-lift-1314-run.txt`: $M^\top G M = G$, $M\delta = \delta$, $M r_i = r_{\sigma(i)}$, $\det M = -1$); the map fixes $\delta$, which by itself places its restriction only in the image of the full stabilizer $\Stab_{\Orth(\ten)}(\delta)$, not in $R_{\gent}$: $R_{\gent}$ is the image of $\Stab_{\gent}(\delta)$ (@prop:gamma-co-images(3)) and $\gent=\rho^{-1}(M)$ is the summand-preserving subgroup (@prop:sterk-group-identification(2)), and the record tests no preservation of the two summands of $A_{\ten}$ for this matrix. So the lift gives an $O(\ten)$-relation. The $R_{\gent}$-relation is decided on the correct criterion elsewhere: `computations/reports/coble_760-gent-membership-run.txt` tests the diagram symmetry itself --- integral, form-preserving, fixing $\delta$ and $\eta_5$, swapping the printed labels $13$ and $14$ --- and finds it in $\gent$, so its restriction lies in $\Stab_{\gent}(\delta)$ and hence in $R_{\gent}$ (@rmk:coble-root-orbits-cusp-five).

Every invariant of the remaining pair agrees, so no invariant decides it: the complement of the saturated pair $\langle\delta,r\rangle$ is the same lattice of rank $10$ and determinant $1024$ for the two roots, the invariant lattices $(r^\perp\cap\delta^\perp\cap\eta_5^\perp)/\ZZ\eta_5$ agree in rank, determinant, Smith invariants, signature, parity and discriminant form, the gluing classes and the gluing norms agree, and the local symbol at $2$ is the same block (`computations/reports/coble_760-pair-complement-run.txt`, `computations/reports/coble_759-invariant-lattices-1213-run.txt`, `computations/reports/coble_759-gluing-class-1213-run.txt`, `computations/reports/coble_759-local-symbol-1213-run.txt`). The pair is decided by the group instead, in one coset computation.

Let $\psi$ be any isometry of $T_\Co$ carrying $r_{12}$ to $r_{13}$; one exists, the restriction to $T_\Co$ of the $12\leftrightarrow13$ transposition of `computations/reports/coble_760-witness-12-13-run.txt`, which fixes $\delta$ and does not lie in $\gent$. Then
$$
\theset{u\in\Gamma_{\Co,2}\mid u(r_{12})=r_{13}}\subseteq\theset{\psi s\mid s\in\Stab_{\Orth(T_\Co)}(r_{12}),\ \bar\rho(\psi)\bar\rho(s)\in P},
$$
because $u(r_{12})=r_{13}$ exactly when $\psi^{-1}u$ fixes $r_{12}$, and $u=\psi s\in\Gamma_{\Co,2}$ forces $\bar\rho(u)=\bar\rho(\psi)\bar\rho(s)\in P$, that is $\bar\rho(s)\in\bar\rho(\psi)^{-1}P$ (@thm:coble-monodromy-versus-enriques(4), the containment $\Gamma_{\Co,2}\subseteq R_{\gent}=\bar\rho^{-1}(P)$ of @prop:gamma-co-images(3)); the converse is the open reverse inclusion @qst:coble-monodromy-equality and is not used, the displayed set being a superset of the one on the left. Since $P$ is the stabilizer of the point $A_{U(2)}$ of $A_{T_\Co}$, the condition on $s$ is that the orbit of $A_{U(2)}$ under $\bar\rho(\Stab_{\Orth(T_\Co)}(r_{12}))$ contain $\bar\rho(\psi)^{-1}(A_{U(2)})$: one subspace orbit in a finite module of $2048$ classes, enumerated exhaustively.
The record prints the answer with its controls (`computations/reports/coble_759-gamma-co-2-orbit-1213-run.txt`). The membership test in $R_{\gent}$, run through two independent class maps which agree on every element tested, accepts the identity, $-\id$, the eleven reflections in the printed roots orthogonal to $\delta$ and the $13\leftrightarrow14$ symmetry, and rejects the $12\leftrightarrow13$ transposition. The orbit of $A_{U(2)}$ under $\bar\rho(\Stab_{\Orth(T_\Co)}(r_{12}))$ has $18\,360$ subspaces and does not contain the target, while the same computation on the pair $(13,14)$, whose answer is known, reaches its target and returns an integral element of $R_{\gent}$ carrying $r_{13}$ to $r_{14}$, so the miss is not an artefact of the search. Hence, modulo the contract named in the next paragraph, no element of $\Gamma_{\Co,2}$ carries $r_{12}$ to $r_{13}$ either, $\Gamma_{\Co,2}$ being contained in $R_{\gent}$ (@thm:coble-monodromy-versus-enriques(4)), and the three admissible roots at cusp $5$ are exactly two $R_{\gent}$-orbits, $\{13,14\}$ and $\{12\}$, the orbits of $\Gamma_{\Co,2}$ refining them (@thm:coble-monodromy-versus-enriques(4)).

Two qualifications belong with that. The enumeration is exhaustive over the subgroup generated by the family the provider returns for $\Stab_{\Orth(T_\Co)}(r_{12})$, the call `vector_stabilizer_generators` (`src/sage_extensions/categories/lattice_morphisms.py:4875`, `sage_extensions` at `6b8f7d2`), whose documented contract is to generate that stabilizer and whose indefinite branch the same file labels untrusted engine output (`:4914`--`:4917`): a pointed marking is a coslice, and the library's own constructions, added for the primitive isotropic line (`src/sage_extensions/categories/lattices.py:2955`) and the primitive isotropic plane (`:2934`), are not entered for one --- the coslice is declined at `:2859`--`:2865` and the port answers at `:2870` --- so the completeness of the family is the provider's claim and not the library's, and the library has nothing that decides it, equality of the subgroup the family generates with the stabilizer answering `False` even between two families of one and the same stabilizer, both sides having countably many elements (`computations/reports/coble_760-vector-stabilizer-certification-run.txt`); a library-owned family for a pointed marking is the operation this step waits on, owned by the provider as sage-extensions#603 (open), and `computations/reports/coble_759-vector-stabilizer-absence-run.txt` prints its absence at the pinned provider commit. The same defect sits one level up, and changing route does not remove it: for an indefinite lattice the generators of $\Orth(T_\Co)$ itself are the port's, "all answers are untrusted engine output" (`src/sage_extensions/categories/lattice_morphisms.py:4739`--`:4742`), and a family read off a Schreier construction over them is complete only relative to a family the caller states generates the ambient group (`src/sage_extensions/categories/group/groups.py:6419`, `:6430`), so carrying the computation on the family of $R_{\gent} = \bar\rho^{-1}(P)$ --- the discriminant-point stabilizer that sage-extensions#459 repaired, which contains $\Gamma_{\Co,2}$ (@thm:coble-monodromy-versus-enriques(4)) and so makes the enumeration a superset --- moves the dependence to that statement and does not remove it. The orbit came out the same, $18\,360$ subspaces, when the family was enlarged from $40$ to $44$ stabilizer generators by the four generators of $\Stab_{\Orth(T_\Co)}(r_{13})$ that also fix $r_{12}$, so the independent route to elements of the stabilizer adds nothing to the orbit; the number of generators is a datum of the run, the provider's family for a stabilizer not being the same between runs (compare `computations/reports/coble_760-transporter-in-gent-run.txt`, which names fifty-one in one run and sixty in another). And the pair is decided in both readings of it. The reading used above and for $13$ and $14$ is transport of the root vectors. The weaker reading compares the two roots as classes of $K_5$ by elements of $\Gamma_{\Co,2}$ that also preserve the cusp line, which allows a shift of $r_{12}$ by a multiple of $\eta_5$, and the shift is removable. The reflection $s_m$ in the root $r_{13}+m\eta_5$ is an isometry of $T_\Co$ fixing $\delta$ and $\eta_5$ and acting trivially on $A_{T_\Co}$, since a reflection in a vector of the lattice moves every dual vector by a multiple of that vector, so $s_m\in\ker\bar\rho\subseteq R_{\gent}$ (@prop:gamma-co-images(3)); whether $s_m$ lies in the smaller $\Gamma_{\Co,2}$ is the reverse inclusion @qst:coble-monodromy-equality and is not asserted either way; on the plane $\langle r_{13},\eta_5\rangle$, where $r_{13}^2=-2$ and $\eta_5$ is isotropic and orthogonal to $r_{13}$, one has $s_m(\alpha r_{13}+\beta\eta_5) = -\alpha r_{13}+(\beta-2m\alpha)\eta_5$, so $\sigma=s_1s_0$ fixes $\eta_5$ and carries $r_{13}+k\eta_5$ to $r_{13}+(k+2)\eta_5$. Hence an element of $R_{\gent}$ that keeps the cusp line and carries $r_{12}$ to $\pm r_{13}+k\eta_5$ composes with a power of $\sigma$ to one carrying $r_{12}$ to $\pm r_{13}$ when $k$ is even, which the previous paragraph excludes, and to $\pm(r_{13}\pm\eta_5)$ when $k$ is odd; and both odd targets are themselves outside the orbit of $r_{12}$, by the same coset computation run on them (`computations/reports/coble_759-class-reading-1213-run.txt`: the shear is verified integral, form-preserving, in $R_{\gent}$ and adding $2$ to the coefficient, and the two searches exhaust the same $18\,360$ subspaces without reaching either target, while the vector reading reproduces its miss on the same family of stabilizer generators). So the classes of $12$ and $13$ in $K_5$ lie in different orbits of the image of $\Gamma_{\Co,2}$ in $\Orth(K_5)$, and the searches that bounded this reading (`computations/reports/coble_760-orbit-witness-run.txt`, `computations/reports/coble_760-transporter-pruned-search-run.txt`) are superseded by the reduction.
:::

## The dictionary from the contracted curve to the boundary lattice

::: {.definition #def:coble-marking-dictionary title="The marked root of a degeneration at a marked cusp" defines="$K_I$; vanishing class; $\nu_\xi$; marked root; $\kappa_{[I]}(\xi)$"}

Let $[I]$ be a marked $0$-cusp, $\eta_I$ a representative of its isotropic line, and $K_I = \eta_I^{\perp\ten}/\ZZ\eta_I$; let $\delta$ be the Heegner vector of @lem:coble-heegner-vector, so that $\delta^{\perp\ten} = T_\Co$.
Let $\xi$ be a degeneration at $[I]$ whose general member is a smooth degree-two Enriques pair, whose K3 cover is $X$, whose KSBA limit is $(\bar S,\eps R_{\bar S})$, and which meets the Coble locus transversally at the parameter $0$, where the K3 cover acquires its ordinary double point.
Let $\nu_\xi$ be the **vanishing class** of that double point: the class, up to sign, of the cycle that vanishes at the parameter, that is, the class of the local system $R^2$ of the family that is algebraic at $0$.
The **marked root** of $\xi$ is
$$
\kappa_{[I]}(\xi) \definedas [\,\nu_\xi\,] \;\in\; K_I ,
$$
the image in the boundary lattice of the vanishing class of the node.
:::

::: {.proposition #prop:coble-marking-class-is-heegner title="The vanishing class of the node is the Heegner vector"}

Let $(\bar S,\eps R_{\bar S})$ be a KSBA stable limit at a marked $0$-cusp $[I]$, let $C\subset\wV$ and $E\subset\wX$ be the curves of @prop:coble-quarter-singularity(3), and let $\xi$ be a degeneration to it as in @def:coble-marking-dictionary.

1. The curves are functions of the limit: $|-2K_{\wV}| = \theset{C}$ is a single curve, $E = \psi^{-1}(C)$ is a single curve, and $E$ is the exceptional curve of the resolution of the unique node of the K3 cover, the node that the involution fixes.
2. The vanishing class is primitive of square $-2$ and satisfies $\iota^*\nu_\xi = -\nu_\xi$; hence $\nu_\xi\in T_\En$.
3. $\nu_\xi$ is orthogonal to $T_\Co$, and therefore $\nu_\xi = \pm\delta$; hence $\kappa_{[I]}(\xi) = [\pm\delta]$, which is a class of $K_I$, and it does not depend on the degeneration, the smoothing, the Kulikov model, or the marking of the Coble lattice, that is, on $\Gamma_{\Co,2}$. It does depend on a marking taken one level up: the markings modulo $\gent$ carry $\delta$ to the whole $\gent$-orbit of $\delta$, and by @thm:coble-cusp-admissibility(1) the classes so obtained are exactly the admissible roots of the cusp, so at cusp $5$ the four classes $11$, $12$, $13$, $14$ (@thm:coble-cusp-admissibility(2)). @rmk:coble-marking-conventions names the two conventions and what each one leaves of @conj:no_moduli_loss.
:::

::: {.proof}

**(1).** @prop:coble-quarter-singularity(1) and (3): the branch curve has exactly one node, at the $\tau$-fixed point, $X^\sharp$ has one $A_1$ singularity fixed by $\iota_\Co$, and the resolution contracts exactly $C$; @prop:coble-from-nodal-enriques-cover identifies the quotient of the nodal K3 cover with the Coble surface and $C$ with the proper transform of the sextic, the single curve of $\abs{-2K_{\wV}}$. The curve $E$ is the exceptional curve of that node, unique because the node is.

**(2).** The resolution of the node is smooth at $E$ and $E$ is a smooth rational curve with $E\cdot K = 0$ on a K3 surface, so $2g-2 = E^2+E\cdot K$ gives $\nu_\xi^2 = -2$; a $(-2)$-class is primitive.
For the sign of the involution: in the model of @prop:coble-quarter-singularity, $X^\sharp = \theset{z^2 = f(x,y)}$ and $\iota_\Co(x,y,z) = (-x,-y,-z)$, so on a smoothing $\theset{z^2 = f+\eps}$ of the node a fixed point of $\iota_\Co$ would need $x = y = z = 0$ and $\eps = 0$. So $\iota_\Co$ acts on the vanishing cycle, a $2$-sphere, without fixed points; an involution of $S^2$ with no fixed point is the antipodal map, of degree $-1$ on $H^2$, so $\iota^*\nu_\xi = -\nu_\xi$.
The anti-invariant lattice of the K3 cover of a degree-two Enriques surface is the orthogonal complement of $\pi^*H^2(Y)\cong S_\En = U(2)\oplus E_8(2)$ in $L = H^2(X_t)$; it is even and $2$-elementary of signature $(2,10)$, with $a = 10$ because $\det\pi^*H^2(Y) = 2^{10}$ and coparity $0$ because its discriminant form is the negative of that of $\pi^*H^2(Y)$ (@thm:nikulin-gluing), and an indefinite even $2$-elementary lattice is determined by those invariants [@AEGS25, §2.3, printed p. 586]; $T_\En = U\oplus U(2)\oplus E_8(2) = (12,10,0)_2$ is that lattice [@AEGS25, Lemma 2.4 and Definitions 2.5--2.7, printed pp. 586--587]. So $\nu_\xi\in T_\En$.

**(3).** At the parameter the class $\nu_\xi$ is that of the curve $E$, hence algebraic; and $T_\Co$ is the period lattice of the resolved K3 cover, namely $N = \generators{2}\oplus U(2)\oplus E_8(2)$ [@DK13, (3.6) and Prop. 3.2, printed p. 513], which is $\delta^{\perp\ten}$ [@lem:coble-heegner-vector]. Hence $\nu_\xi\perp\delta^{\perp\ten}$.
Since $\delta^2 = -2\ne0$, one has $\ten\otimes\QQ = \QQ\delta\perp(\delta^{\perp\ten}\otimes\QQ)$, so $\nu_\xi = a\delta$ with $a\in\QQ$; $\delta$ primitive and $\nu_\xi\in\ten$ give $a\in\ZZ$, and $\nu_\xi^2 = -2a^2 = -2$ gives $a = \pm1$, that is $\nu_\xi = \pm\delta$.
At a marked cusp $\delta\perp\eta_I$ (@thm:coble-cusp-admissibility(2)), so $[\pm\delta]\in K_I$ is defined; and nothing in (2) and (3) refers to the member, to the smoothing family, to a Kulikov model or to the marking.

**(The hyperplane of [@AEGS25].)** The two statements above do not use the vector $\alpha$ of [@AEGS25], and they identify it: $\Delta = \alpha^{\perp}$ parameterizes the quotients of nodal K3 surfaces by an involution fixing a node [@AEGS25, printed p. 587], and a member has that node only if the vanishing class is algebraic at it, so $\Delta\subseteq\nu_\xi^{\perp}$; both are hyperplanes in the same period domain, so $\alpha^{\perp} = \nu_\xi^{\perp}$ and, both vectors primitive of square $-2$, $\alpha = \pm\nu_\xi = \pm\delta$.
:::

::: {.remark #rmk:coble-marking-dictionary-scope title="What the dictionary gives, and what it does not"}

Two readings, and it settles one of them.

**The contracted-curve reading is settled.** By @prop:coble-marking-class-is-heegner the class of the contracted anti-bicanonical curve at a marked cusp is $\pm\delta$ at every degeneration and every marking: it is one class, and a statement phrased as "two degenerations at $[I]$ whose marked roots are inequivalent are not identified in the KSBA boundary" has no instance when "marked root" means that class.
This is not the argument withdrawn in @warn:no-moduli-loss-vacuity: that one compared the three $T_\Co$-roots at cusp $5$ through two isometries of $\ten$ and turned on $\gent$-membership, while this one never mentions those roots.

**The $T_\Co$-root reading is not touched by it, and it is what @conj:no_moduli_loss carries.** A $T_\Co$-root is a class of $K_I$ with a lift $w\in T_\Co$ of square $-2$ (@thm:coble-cusp-admissibility(1), @thm:face-irrelevant-marking(2)); the contracted curve's class is $[\pm\delta]$ and $\delta\notin T_\Co = \delta^{\perp\ten}$, so the two sets of classes are disjoint and no identity between a $T_\Co$-root and the curve's class can be proved or refuted by the dictionary. At cusp $5$ the curve's class is Sterk's label $11$, which @prop:marking-line-no-coble-lift certifies to be $[\pm\delta]$, and the three $T_\Co$-roots are his labels $12$, $13$ and $14$; at cusps $3$ and $4$ the curve's class is label $8$ and the $T_\Co$-root is label $12$, respectively $10$ (@thm:coble-cusp-admissibility(2), @thm:face-irrelevant-marking(2)).
So a $T_\Co$-root is a class attached to the degeneration and its marking and not to the contracted curve, and the two-orbit computation of @rmk:coble-root-orbits-cusp-five decides the $T_\Co$-root question, which is @conj:no_moduli_loss's and research#760's, not the contracted-curve question, which is @prop:coble-marking-class-is-heegner's and is closed.
:::

::: {.remark #rmk:coble-marking-conventions title="Two marking conventions, and where the marked-root statement has content"}

The two readings of the preceding remark are two conventions for what a marking is, and each one leaves a different statement.

**The Coble convention.** A marking identifies the transcendental lattice of the resolved K3 cover with $T_\Co = \delta^{\perp\ten}$, and markings are considered modulo $R_{\gent}$: this is the group of @def:gamma-co-groups(4), and it is not the monodromy group $\Gamma_{\Co,2}$ of @def:gamma-co-groups(5). There the marked root is the single class $[\pm\delta]$ (@prop:coble-marking-class-is-heegner(3)), so the hypothesis of the marked-root statement is not met and the statement holds.

**The Enriques convention.** The marking is taken on the ambient Enriques lattice, so markings are considered modulo $\gent$; the marked root is then $[h\delta]$ for the marking $h$, and by @thm:coble-cusp-admissibility(1) the values at a marked cusp are exactly its admissible roots. On this convention the marked root is data of the marking, so the separation statement is a statement about the forgetful map from markings to stable pairs and not about curves on $\bar S$.

**Where the content is.** On the Coble convention the statement is a corollary of @prop:coble-marking-class-is-heegner and is settled. On the Enriques convention the (semi)toroidal compactification of $\bD(T_\Co)/\Gamma_{\Co,2}$ has, by construction, the $\Gamma_{\Co,2}$-orbits of its boundary data as its boundary points, so inequivalent marked roots give distinct points of *that* compactification with nothing to prove; what such a statement can carry is then the transport to the KSBA boundary, which is the identification of @conj:ksba_semitoroidal_comparison, A7 of research#650, whose own question is when a semitoroidal compactification restricted to a Heegner divisor is semitoroidal.
So the KSBA-boundary form of the marked-root statement is not a statement that research#759 proves on the second convention: what this page carries of it is the definition of the root (@def:coble-marking-dictionary), the proof that it is $[\pm\delta]$ in the Coble convention (@prop:coble-marking-class-is-heegner), the form of what the comparison would transport (this remark), and the decision of the orbit question at cusp $5$ modulo the stabilizer family (research#759 item 1, sage-extensions#603).

:::

::: {.lemma #lem:coble-root-separation-transport title="Root separation transports along an identification that preserves the marked side"}

Let $\Gamma\definedas\Gamma_{\Co,2}$, $F\definedas\bD(T_\Co)/\Gamma$ (@def:gamma-co-groups(5)), and let $\semitorcpt{F}$ be a semitoroidal compactification of $F$ (@def:semitoroidal-compactification).
Let $\pi$ send a marked degeneration at a marked cusp to its boundary point in $\semitorcpt{F}$, and let $\pi^{K}$ send it to its point of the KSBA boundary.
Suppose:

1. $\pi$ is well defined, and two marked degenerations have the same image in $\semitorcpt{F}$ exactly when their markings differ by an element of $\Gamma$;
2. the marked root of a marked degeneration is a function of the marking modulo $\Gamma$ (@def:coble-marking-dictionary);
3. after normalization of $\ksbacpt{\fco}$ there is an isomorphism $\varphi\colon\ksbacpt{\fco}\to\semitorcpt{F}$ with $\varphi\circ\pi^{K} = \pi$.

Then two marked degenerations at a marked cusp whose marked roots lie in different $\Gamma$-orbits are not identified in the KSBA boundary.
:::

::: {.proof}

By (2) the marked root is constant on the fibres of $\pi$, so marked roots in different $\Gamma$-orbits put the two degenerations in different fibres of $\pi$; by (1) their images in $\semitorcpt{F}$ differ; by (3), an isomorphism commuting with the forgetful maps, their images in $\ksbacpt{\fco}$ differ.
:::

::: {.remark #rmk:coble-transport-hypotheses title="Which hypotheses of the transport hold, and which one is A7"}

Hypothesis (1) is the construction of the semitoroidal compactification, which glues the boundary components modulo $\Gamma$ (@def:semitoroidal-compactification, after [@Loo02, Def. 6.1] and [@AE23, Def. 5.11]); the group there is the group of the moduli problem, $\Gamma_{\Co,2}$, and the degree-two numerical polarization is part of the datum, as it is for $F_{\En,2} = \bD(T_\En)/\Gamma_{\En,2}$ in [@AEGS25, Def. 2.7, printed p. 587].
Hypothesis (2) is @prop:coble-marking-class-is-heegner(3) together with @def:coble-marking-dictionary; it is hypothesis (2) alone that @rmk:coble-marking-conventions separates from the Coble convention.
Hypothesis (3) is not available on $F_\Co$: it is A7, @conj:ksba_semitoroidal_comparison, research#650. It is also strictly stronger than the identification of the two spaces, because an isomorphism $\varphi$ of the underlying varieties does not by itself make the two forgetful maps agree; in the one case where the agreement is known it comes not from the identification but from a construction on the marked level, the family over the compactified moduli stack in the proof of [@AEGS25, Thm. 5.9, printed p. 612].
So the transport is a lemma whose only missing hypothesis is (3), and (3) cannot be recovered from the identification of the two compactifications as spaces.
:::

::: {.remark #rmk:coble-transport-failure title="The group of hypothesis (1) is not cosmetic: the same sentence fails for the unpolarized quotient"}

Replace $\Gamma_{\Co,2}$ by $\Orth^+(T_\Co)$ throughout, that is, compactify the unpolarized quotient instead. Hypotheses (1) and (2) hold for that group as well, and the conclusion fails at cusp $5$: the roots $12$ and $13$ are $\Gamma_{\Co,2}$-inequivalent on the decision of research#759's item 1, modulo the stabilizer family owned by sage-extensions#603, while the transposition of the two square-$(-2)$ generators of the saturation of $\generators{\delta,r_{12},r_{13}}$, extended by the identity on its complement, is an integral form-preserving isometry of $\ten$ fixing $\delta$, hence preserves $\delta^{\perp\ten} = T_\Co$ and restricts to an isometry of $T_\Co$ carrying the class of $12$ to that of $13$ (@rmk:coble-root-orbits-cusp-five, `computations/reports/coble_760-witness-12-13-run.txt`). So the two roots are one $\Orth^+(T_\Co)$-orbit and the unpolarized compactification does not separate their degenerations; at the level of cusps the collapse is total, since $\Orth^+(T_\Co)\backslash\bD_\Co$ has a single orbit of primitive isotropic lines (@thm:unpolarized-cusps), so the unpolarized boundary does not distinguish even the four marked cusps of $F_\Co$.
What fails in this reading is therefore not (3) but hypothesis (1) read with a group other than the one the KSBA moduli problem carries. The sentence is true for the polarized compactification exactly because $\Gamma_{\Co,2}$ is that group, and false for the unpolarized one.
:::

::: {.conjecture #conj:no_moduli_loss title="The stable Coble quotient determines its marked Coble root"}

The stable quotient is $\bD(T_\Co)/\Gamma_{\Co,2}$ (@def:gamma-co-groups(5)).
Let $[I]$ be a marked cusp with boundary lattice $K_I = \eta_I^{\perp\ten}/\ZZ\eta_I$, and let a degeneration at $[I]$ carry a marking and a $T_\Co$-root $r\in K_I$: a class with a lift $w\in T_\Co$ of square $-2$ (@thm:coble-cusp-admissibility(1), @thm:face-irrelevant-marking(2)).
The class of the contracted anti-bicanonical curve is not one of these: it is $[\pm\delta]$ at every degeneration and every marking (@prop:coble-marking-class-is-heegner), so the present statement is about the $T_\Co$-roots.
Two degenerations at $[I]$ whose $T_\Co$-roots lie in different $\Gamma_{\Co,2}$-orbits are not identified in the KSBA boundary.

**Which half is proved.** On the stable quotient the claim is @thm:no-moduli-loss, proved there modulo the stabilizer family its proof names.
On the KSBA boundary it is a statement about stable pairs: the boundary of the moduli problem is the moduli of stable pairs, so two degenerations at $[I]$ are identified there exactly when their stable limits are isomorphic, and the claim is the contrapositive of the first half of the boundary Torelli statement of research#760, that an isomorphism of stable pairs over $[I]$ induces an element of $\Gamma_{\Co,2}$ carrying one root to the other; the second half of that statement is the converse.
@def:coble-marking-dictionary does not decide it and does not need to: by @prop:coble-marking-class-is-heegner the contracted curve's class is $\pm\delta\notin T_\Co$, so no $T_\Co$-root is the class of a curve of $\bar S$ at the cusp, and what a $T_\Co$-root classifies is the degeneration together with its marking (@rmk:coble-marking-dictionary-scope).
Its hypothesis is met at cusp $5$ on one decision and not unconditionally: $13$ and $14$ lie in one $R_{\gent}$-orbit, by an explicit integral isometry (@rmk:coble-root-orbits-cusp-five), which establishes nothing about their $\Gamma_{\Co,2}$-orbits (@thm:coble-monodromy-versus-enriques(3), (4)), while $12$ and $13$ lie in different $R_{\gent}$-orbits, hence in different $\Gamma_{\Co,2}$-orbits since $\Gamma_{\Co,2}\subseteq R_{\gent}$, and that half is research#759's item 1, whose computation on this page is exhaustive only over the subgroup generated by the family `vector_stabilizer_generators` returns, and is decided there modulo that family (sage-extensions#603, `computations/reports/coble_759-vector-stabilizer-absence-run.txt`). So the statement is not vacuous; its instance at cusp $5$ is conditional on that family.
Open is the identification step, and a comparison of two stable pairs needs a limit-pair operation that the library does not have (`computations/reports/coble_759-limit-pair-call-probe-run.txt`); a counterexample would be a pair of degenerations at one marked cusp, with $T_\Co$-roots in different $\Gamma_{\Co,2}$-orbits, whose stable limits are isomorphic.

:::

::: {.theorem #thm:no-moduli-loss title="The stable quotient determines the marked root of a marked cusp up to $\Gamma_{\Co,2}$"}

The stable quotient is $\bD(T_\Co)/\Gamma_{\Co,2}$ (@def:gamma-co-groups(5)). Let $[I]$ be a marked cusp, with boundary lattice $K_I = \eta_I^{\perp\ten}/\ZZ\eta_I$, and let a degeneration at $[I]$ carry a marking. Its marked root is the $T_\Co$-root that the marking assigns, as in @conj:no_moduli_loss; the class of its contracted anti-bicanonical curve is not that root but the single class $[\pm\delta]$ (@prop:coble-marking-class-is-heegner). Two degenerations at $[I]$ whose marked roots lie in different $\Gamma_{\Co,2}$-orbits are distinct points of the stable quotient.

**Not vacuous, and not decided by a face.** In that quotient the statement determines its marked Coble root at every marked cusp at which there is a pair: at cusp $2$ there is no $T_\Co$-root, the unique admissible class being the marking line (@prop:marking-line-no-coble-lift, @thm:face-irrelevant-marking(2)), at cusps $3$ and $4$ there is one $T_\Co$-root each, so nothing is separated there, while at cusp $5$ the three $T_\Co$-roots have classes in two $R_{\gent}$-orbits, $\{13,14\}$ and $\{12\}$ (@thm:face-irrelevant-marking(3), @rmk:coble-root-orbits-cusp-five), so a pair is separated. The form of the statement that names the KSBA boundary rather than the stable quotient --- that such degenerations are not identified there --- is @conj:no_moduli_loss, and the present theorem is its quotient-side half; the other half is the boundary Torelli statement of research#760, and @conj:no_moduli_loss identifies the two.

**What the face does and does not give.** An earlier form of this statement asked a face of the restricted semifan to carry the marking, and no face can: by @thm:face-irrelevant-marking every admissible $T_\Co$-root at every marked cusp is irrelevant, so all of them cut one maximal cone, and at cusp $5$ the three roots $12$, $13$ and $14$ cut it together.
So the hypothesis is met at cusp $5$ (@thm:face-irrelevant-marking(3), `computations/reports/coble_759-gamma-co-2-orbit-1213-run.txt`): $12$ and $13$ are inequivalent already under $R_{\gent}$, and $\Gamma_{\Co,2}\subseteq R_{\gent}$ (@thm:coble-monodromy-versus-enriques(4)), so they are inequivalent under $\Gamma_{\Co,2}$, which is what the statement asks; the form of the statement that names the KSBA boundary asserts of that pair that the two degenerations are not identified there. That is the step this page does not have: it is the identification below, and no face supplies it, all three roots cutting one maximal cone. An earlier version of this page drew the opposite conclusion from the same pair --- that an inequivalence of the two roots by itself makes the conjecture false --- and that is withdrawn with the vacuity reading: inequivalence is a statement about $\Gamma_{\Co,2}$-orbits, identification in the boundary is a statement about stable pairs, and the passage between them is exactly what is missing. Distinct classes in $K_5$ do not decide the orbits (`computations/reports/coble_coble-root-orbits-run.txt`, @thm:face-irrelevant-marking(3)). Nor does an isometry of $\ten$ that fixes $\delta$ and $\eta_5$ but lies outside $\gent$: the transposition of the two square-$(-2)$ generators of the saturation of $\generators{\delta, r_{12}, r_{13}}$ is integral, of determinant $-1$ and form-preserving, and carries the class of $12$ to that of $13$, but it carries classes out of both summands of $A_{\ten}$, so it is not in $\gent$ (`computations/reports/coble_760-gent-membership-run.txt`).
The recovery asserted here is therefore a statement about the contracted curve alone: the divisor it would be read off is @def:coble-descended-ramification, defined from [@AEGS25, §2.4, printed p. 588] and [@AEGS25, Prop. 6.1(2), printed p. 616].
Its referent is @prop:coble-marking-class-is-heegner: reading a class of $K_I$ off the contracted curve needs the class of the exceptional curve of the fixed node, and that class is $\pm\delta$, so the marking is a definition that is made and not a citation that is missing (@def:coble-marking-dictionary). What `computations/reports/coble_760-cusp-marking-search-run.txt` records stays true as recorded and is narrower: no source pairs a *simple root of the chamber* with a curve of the Coble surface, the word "Coble" not occurring at all in Alexeev--Nikulin and "simple root" not occurring in Dolgachev--Kondo (@warn:coble-marking). Nor does the library supply the operation. The two it would take are absent in different degrees, and the probe prints each expression that fails (`computations/reports/coble_759-limit-pair-call-probe-run.txt`): the restricted semifan as cones is absent from an object that exists, the folded Coxeter diagram of `src/sage_extensions/categories/coxeter_diagrams.py:374`, on which `Coble.rank_ten_diagram().semifan()` and `.cones()` raise `AttributeError`, so it is an operation to add; and the limit pair is absent from the package altogether, no name in its $318$ python files referring to a semifan, a KSBA compactification, a stable pair or a marked root, `Coble.rank_ten_diagram().stable_pairs()` and `.marked_root()` raising `AttributeError`, while a cusp record retains only representatives, parabolics, stabilizers and transporters (`src/sage_extensions/categories/lattices.py:9864`), so it is an object to build. Until one of the two exists, the $T_\Co$-root reading of "the two degenerations are not identified in the KSBA boundary" is a sentence without a computation behind it, in either direction; the reading through @def:coble-marking-dictionary does not need them, since its root is a single class.

The identity of the marking is not in question, and the two objects above are not rival candidates for it: what is missing is the passage between them. The marking is a class of the boundary lattice — $\delta$ itself marks the cusp (@thm:coble-cusp-admissibility(2)), the marking line in $K_I$ is its class $[\pm\delta]$ (@prop:marking-line-no-coble-lift), and the admissible $T_\Co$-roots are the classes of $K_I$ that lift to $T_\Co$ (@thm:face-irrelevant-marking(2), (3)) — while the face $f(r)$ is derived from a root together with the coarsening of the Coxeter fan. Whether that face carries the marking is a separate question, and @thm:face-irrelevant-marking answers it in the negative: at cusp $5$ the inequivalent roots $12$ and $13$ cut one cone (`computations/reports/coble_759-gamma-co-2-orbit-1213-run.txt`, @thm:face-irrelevant-marking(3)). What is missing is the other half of the dictionary, the one from a curve of $\bar S$ to its class in $K_I$, and behind it the limit-pair operation that would let two degenerations be compared at all. Nor can the two issues between them discharge the statement: @conj:ksba_semitoroidal_comparison records this statement among its own four inputs, so it cannot be used to prove it. What is independent of both is the dictionary from a curve of $\bar S$ to its class in $K_I$, and it is the one input that neither the sources nor the library supplies. One consequence of @prop:coble-quarter-singularity(3) belongs with this and narrows the statement: $\abs{-2K_{\wV}} = \theset{C}$ there is a single curve, so the class in $K_I$ is a function of the marked surface and not a choice among its curves, and a pair of degenerations differing only by their marked root is a pair of level structures on one and the same degeneration. The statement then asks where the moduli problem sits: at the monodromy group $\Gamma_{\Co,2}$, which is the group $\bD(T_\Co)/\Gamma_{\Co,2}$ quotients by and which lies in the arithmetic group $R_{\gent} = \bar\rho^{-1}(P)$ of finite index in $\Orth(T_\Co)$ (@prop:gamma-co-images(3), @thm:coble-monodromy-versus-enriques(4)), two markings whose root classes are inequivalent remain distinct; at $\Orth(T_\Co)$ they do not. So the residual question is a single one about the level structure of the Coble moduli functor, and it is not answered here.
Nor do the cusp's own symmetries supply one: of the eight symmetries of the labelled cusp-$5$ Gram exactly one swaps the labels of $12$ and $13$, and it moves the Coble root's label $11$ (`computations/reports/coble_760-cusp-symmetry-run.txt`).
Nor does the statement follow from an isomorphism of stable pairs without one of the two routes: that needs a cited statement that a stable pair over a cusp determines its lattice data, and the two statements the source the acceptance names offers do something else. [@AEGS25, Thm. 1.1, at p. 2 of the version read, arXiv:2312.03638v2; the bibliography records the Nagoya pagination 581--624] identifies the normalization of the KSBA compactification of $\fentwo$ with a semitoroidal compactification for five explicit semifans, one per $0$-cusp, dominated by the toroidal one for the corresponding Coxeter fans: that identifies two compactifications of one period space, and the Coble root $\delta$ is not a datum of that space. And the determination that paper proves runs from the monodromy invariant $\lambda$, valued in the fundamental chamber of a folded Coxeter diagram, through the elliptic subdiagram of that diagram, to the *combinatorial type* of the stable limit, a union of ADE surfaces glued along double curves ([@AEGS25, §4], attributing that determination to [@AE23, Cor. 8.13]; §7 of the same paper describes those limits). A combinatorial type is coarser than a marked root: by @thm:face-irrelevant-marking all three admissible roots at cusp $5$ cut one cone, so they share the type and it cannot separate them. Neither statement gives (a) or (b), and the probe of that source records why (`computations/reports/coble_759-marking-dictionary-probe-run.txt`: the word "Coble" occurs in it twice, both times as an example of a degeneration, and no Coble root, marked root or boundary lattice occurs at all).
The pair the page carried as a counterexample before -- roots $11$ and $12$ at cusp $5$ -- is withdrawn on a different ground: root $11$ is the marking line $[\pm\delta]$, which has no lift in $T_\Co$ by @prop:marking-line-no-coble-lift, so that pair was never comparable; the comparable pair is $12$ and $13$ at cusp $5$, and it is a pair of inequivalent roots (@thm:face-irrelevant-marking(3)).

The group that the determination is modulo is $R_{\gent}$, the image of $\Stab_{\gent}(\delta)$ in $\Orth(\delta^{\perp})$ (@prop:gamma-co-images, @prop:gamma-co-2-line-stabilizer): the stabilizer of the root line $\ZZ\delta$ in $\gent$.
It is not the monodromy group $\Gamma_{\Co}$ of @def:gamma-co-groups, which equals the stable subgroup $\widetilde{\Orth}^+(T_{\Co})$ on the labelled base (@thm:gamma-co-is-stable).
The marking-line root is not among the $T_\Co$-roots by @prop:marking-line-no-coble-lift, and at cusp $2$ the unique admissible root is the marking line itself, so no $T_\Co$-root exists there.
Cusps $3$ and $4$ carry one $T_\Co$-root each and so no pair, which leaves cusp $5$, whose three roots are pairwise distinct classes of $K_5$ (@thm:face-irrelevant-marking(3)) and exactly two $R_{\gent}$-orbits, $\{13,14\}$ and $\{12\}$, whose $\Gamma_{\Co,2}$-orbits are refinements (@rmk:coble-root-orbits-cusp-five).
:::

::: {.proof}

$\Gamma_{\Co,2}$ acts on $T_\Co$ (@def:gamma-co-groups(5)), hence on the isotropic vectors of $T_\Co$, on the lattices $K_I$ of their quotients, and on the pairs consisting of a period point together with a class. Two marked degenerations at $[I]$ are one point of $\bD(T_\Co)/\Gamma_{\Co,2}$ exactly when some $\gamma \in \Gamma_{\Co,2}$ carries one to the other, and that $\gamma$ carries the class of the contracted curve of the one to that of the other; so $r_1$ and $r_2$ then lie in one $\Gamma_{\Co,2}$-orbit.
It remains to say which admissible roots lie in different orbits. At cusp $5$ the three have classes forming the two $R_{\gent}$-orbits $\{13,14\}$ and $\{12\}$: the explicit element $u=\psi s$ of $R_{\gent}$ carries $r_{13}$ to $r_{14}$, and no element of $\Gamma_{\Co,2}$ carries $r_{12}$ to $r_{13}$ (@rmk:coble-root-orbits-cusp-five, `computations/reports/coble_759-gamma-co-2-orbit-1213-run.txt`, `computations/reports/coble_760-gent-membership-run.txt`), so $12$ is separated from both. At cusps $3$ and $4$ there is one admissible root each, and at cusp $2$ only the marking line, which is not a $T_\Co$-root (@prop:marking-line-no-coble-lift, @thm:face-irrelevant-marking(2)), so no pair arises at those cusps.
:::

::: {.remark #rmk:coble-root-orbits-cusp-five title="The three admissible roots at cusp $5$ are exactly two $R_{\gent}$-orbits, $\{13,14\}$ and $\{12\}$"}

The three admissible $T_\Co$-roots at cusp $5$ have pairwise distinct classes in $K_5$, so they are three distinct roots; the question is how many markings they are, and the answer is two.
Each root of $K_5$ that is the class of a $(-4)$- or $(-2)$-vector of $T_\Co$ orthogonal to $\eta_5$ --- Sterk's printed labels $1$--$8$ and $12$--$14$ --- lifts to a vector $w$ of $\ten$ with $2\div(w)\in(w\cdot w)\ZZ$, so $s_w$ is an integral isometry [@AEGS25, §3.4]; its restriction to $T_\Co$ lies in $R_{\gent}$, and the reason splits by the square of $w$. For $w^2=-2$ --- the labels $12$--$14$ --- the reflection moves a dual vector by the integral multiple $2(x^*,w)/(w,w) = -(x^*,w)$, so $s_w$ acts trivially on $A_{\ten}$ and lies in $\ker\rho_{T_\En}\subseteq\gent$ (@prop:sterk-group-identification(2)). For $w^2=-4$ --- the labels $1$--$8$ --- that coefficient is a half-integer in general, so $s_w$ is not discriminant-trivial and its membership in $\gent$ is not an integrality computation; it is the summand test of `computations/reports/coble_760-gent-membership-run.txt`, which passes for all fourteen reflections. In both cases it fixes $\delta$, hence lies in $\Stab_{\gent}(\delta)$ and its restriction to $T_\Co$ lies in $R_{\gent}$ (@prop:gamma-co-images(3)); and it fixes $\eta_5$, so it acts on $K_5$.
Being an isometry of $\ten$ is not enough to lie in $R_{\gent}$, which is the image of $\Stab_{\gent}(\delta)$, and $\gent$ is strictly smaller than $O(\ten)$: by [@AEGS25, Def. 2.6] it is the image of the centralizer of the Enriques involution in $O(L)$, and by [@Ste91, Prop. 2.7] that image is exactly the set of isometries whose induced map on the discriminant module respects its decomposition in two summands, here $A_{U(2)}\oplus A_{E_8(-2)}$ of orders $4$ and $256$ (@prop:gamma-co-images). A record tests that condition directly --- in the dual-basis coordinates where the discriminant module is $\ZZ^{12}/G\ZZ^{12}$ the induced map is $a\mapsto g^{\mathsf T}a$ --- and calibrates the test on the elements this page already places in $R_{\gent}$: the identity, $-\id$, and all eleven reflections in printed roots orthogonal to $\delta$ pass it (`computations/reports/coble_760-gent-membership-run.txt`).
Of the two candidates one passes and one does not.
The unique symmetry of the labelled cusp-$5$ Gram that fixes the Coble root's label $11$ and exchanges labels $13$ and $14$ lifts to an integral isometry of $\ten$ fixing $\delta$ and $\eta_5$ and exchanging the two roots (`computations/reports/coble_760-witness-13-14-run.txt`, `computations/reports/coble_759-lift-1314-run.txt`); the record `computations/reports/coble_760-gent-membership-run.txt` tests this witness for membership in $\gent$ --- the condition is the preservation of the two summands of $A_{\ten}$ (@prop:sterk-group-identification(2)), calibrated on the identity, on $-\id$ and on the eleven reflections --- and finds it there, so its restriction lies in $\Stab_{\gent}(\delta)$ and the roots $13$ and $14$ are $R_{\gent}$-equivalent (@prop:gamma-co-images(3)). The same record returns an explicit integral element carrying $r_{13}$ to $r_{14}$, accepted by both class maps (`computations/reports/coble_759-gamma-co-2-orbit-1213-run.txt`). That says nothing about their $\Gamma_{\Co,2}$-orbits, which refine these (@thm:coble-monodromy-versus-enriques(3), (4)).
For the pair $12$, $13$ no symmetry of the printed diagram suffices: the transposition that would serve does not preserve the labelled Gram, and the span of $\delta$, $r_{12}$, $r_{13}$ is not a direct summand of $\ten$, its saturation having index $2$. The transposition of the two square-$(-2)$ generators of that span, extended by the identity on the rank-$9$ complement, is integral, of determinant $-1$ and form-preserving, and it exchanges the two lifts; but it carries the classes $[d_4]$, $[d_6]$, $[d_7]$ and $[d_{11}]$ out of their summands, so it lies outside $\gent$ (`computations/reports/coble_760-witness-12-13-run.txt`, `computations/reports/coble_760-gent-membership-run.txt`).
That the witness lies outside $\gent$ does not make the pair $\gent$-inequivalent, and the pair is not: multiplying it by a word in the generators of $\Stab_{\Orth(\ten)}(r_{12})$ that the provider returns gives an element of $\gent$ carrying $r_{12}$ to $r_{13}$ (`computations/reports/coble_760-transporter-in-gent-run.txt`).
The condition that $R_{\gent}$ imposes on top of that is decided, negatively: $R_{\gent}$ is the image of $\Stab_{\gent}(\delta)$, and no element of it carries $r_{12}$ to $r_{13}$ at all (`computations/reports/coble_759-gamma-co-2-orbit-1213-run.txt`), by the coset reduction of @thm:face-irrelevant-marking(3) --- the coset $\Stab_{\Orth(T_\Co)}(r_{12})\cdot\psi$ meets $R_{\gent}$ exactly when one subspace orbit of $A_{T_\Co}$ contains one point, the orbit that arises has $18\,360$ subspaces and does not, and the same computation on $(13,14)$ reaches its target and returns an element of $R_{\gent}$. That computation is exhaustive over the subgroup generated by the family `vector_stabilizer_generators` returns; the certified family is sage-extensions#603, absent at the pinned provider commit (`computations/reports/coble_759-vector-stabilizer-absence-run.txt`), which names sage-extensions#603 (open) as its owner.
The library's orbit call for these classes, `IsotropicVectorReductionImage.root_class_orbits` (sage-extensions#370, closed), has been run at cusp $5$: it returns three singleton orbits (`computations/reports/coble_760-cusp5-root-orbits-run.txt`).
A singleton is not a proof of inequivalence there, and the family it acts with is demonstrably incomplete: the $13\leftrightarrow14$ isometry above fixes $\delta$ and $\eta_5$ and lies in $\gent$, so its reduction lies in the group acting on $K_5$ and joins the two classes the call separates.
The weaker class reading gives the same answer, and by a reduction rather than by a longer search. There an element of $R_{\gent}$ that preserves the line $\ZZ\eta_5$ carries $r_{12}$ to $\pm r_{13}+k\eta_5$ instead of to $\pm r_{13}$, and the shift is removable: the reflections in the roots $r_{13}+m\eta_5$ lie in $R_{\gent}$, and their product $s_1s_0$ fixes $\eta_5$ and adds $2$ to the coefficient, so an even $k$ would give a transporter of the vector reading, which does not exist, and an odd $k$ leaves the two targets $\pm(r_{13}\pm\eta_5)$, which are themselves outside the orbit of $r_{12}$ (`computations/reports/coble_759-class-reading-1213-run.txt`). So the classes of $12$ and $13$ in $K_5$ lie in different orbits of the image of $R_{\gent}$ in $\Orth(K_5)$, and hence of the image of $\Gamma_{\Co,2}$, which is contained in it (@thm:coble-monodromy-versus-enriques(4)).
What the earlier search did is therefore superseded and not wrong: composing the transporter with words of length up to $16$ in the $52$ generators of $\Stab_{\Orth(T_\Co)}(r_{12})$ left $51\,830$ candidates that keep the line and carry the class, and none of them lies in $R_{\gent}$ (`computations/reports/coble_760-transporter-pruned-search-run.txt`); that is a bound rather than a decision, the stabilizer having infinite index, and the saturation of its survivor counts is not exhaustion, a word satisfying both conditions having prefixes that need not.
So at cusp $5$ the roots $13$ and $14$ form one $R_{\gent}$-orbit and the root $12$ forms another, although it is $\gent$-equivalent to them; the orbits of $\Gamma_{\Co,2}$ refine this partition (@thm:coble-monodromy-versus-enriques(4)), and what is proved of them is that $12$ and $13$ are separated, the positive half $— that $13$ and $14$ are one $\Gamma_{\Co,2}$-orbit — being unproved and equivalent to @qst:coble-monodromy-equality at this pair; cusps $3$ and $4$ carry one admissible root each, and cusp $2$ only the marking line (@prop:marking-line-no-coble-lift), so no pair exists there at all.
:::

::: {.warning #warn:no-moduli-loss-vacuity title="The withdrawn vacuity argument, and what became of it"}

An earlier version of this page carried, until `bdb78a77ce`, a theorem `thm:no-moduli-loss-vacuous` stating that the three admissible roots at cusp $5$ are pairwise $\Gamma_{\Co,2}$-equivalent and that @thm:no-moduli-loss therefore holds vacuously.
That argument is withdrawn.
It rested on two integral isometries of $\ten$ fixing $\delta$ and $\eta_5$, and being an isometry of $\ten$ is not the same as lying in $\gent$: $R_{\gent}$ is the image of $\Stab_{\gent}(\delta)$, and $\gent$ is the summand-preserving subgroup of $O(\ten)$ ([@AEGS25, Def. 2.6], [@Ste91, Prop. 2.7]), which the proof of @prop:gamma-co-images on this page states.
Of the two witnesses only the $13\leftrightarrow14$ one preserves the two summands of $A_{\ten}$; the $12\leftrightarrow13$ one does not, so it proves an $O(\ten)$-orbit and neither an $R_{\gent}$-orbit nor a $\Gamma_{\Co,2}$-orbit (`computations/reports/coble_760-gent-membership-run.txt`).
The pair $(12,13)$ is decided in the other direction: no element of $\Gamma_{\Co,2}$ carries $r_{12}$ to $r_{13}$ (@thm:face-irrelevant-marking(3), `computations/reports/coble_759-gamma-co-2-orbit-1213-run.txt`), so the three roots are two $R_{\gent}$-orbits, and $12$ and $13$ are separated under $\Gamma_{\Co,2}$ as well (@rmk:coble-root-orbits-cusp-five). The premise the withdrawn argument needed is therefore not merely unproved but false, and the hypothesis of @thm:no-moduli-loss is met at cusp $5$.
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
   The marked cusps are exactly Sterk's cusps $2,3,4,5$; his representatives $\eta_2,\dots,\eta_5$ are orthogonal to $\delta$, so $\delta$ itself is a lift at each of the four, and among his printed simple systems (@def:weyl-chamber) the admissible roots are exactly the white nodes: cusp $2$: his root $10$; cusp $3$: his roots $8$ and $12$; cusp $4$: his roots $8$ and $10$; cusp $5$: his roots $11$--$14$.
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

