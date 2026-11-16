# KSBA stable limits {#sec-ksba}


## How a stable limit is obtained

::: {.construction #cons:degree-two-k3-affine-sphere title="The degree-two K3 affine sphere"}

For the degree-two K3 moduli space $F_2$, let $K$ be a fundamental chamber of the Coxeter fan in $N=U\oplus E_8(-1)^2\oplus A_1(-1)$. A class $\lambda\in K$ determines a nef class $L$ on the rational surface $T$ used in [@AET23, §§5–6]. First take $\lambda$ in the open chamber, with all length parameters positive. Start with the moment polygon of a toric model of $(T,L)$. It has eighteen sides, indexed $0,\ldots,17$. Perform Symington surgeries of positive sizes $b_{18},b_{19},b_{20}$ on sides $0,6,12$. The resulting integral affine disc $P(\lambda)$ has three interior $I_1$ singularities [@AET23, Construction 6.1].

The construction uses twenty-four nonnegative root pairings $a_i=\lambda\cdot r_i$, indexed $0,\ldots,23$. In the normalization of [@AET23, §6A], their associated length parameters $b_i$ satisfy $a_i=b_i$ for even $0\leq i<18$ and $a_i=2b_i$ for the other indices. The roots span the rank-$19$ cusp lattice, so these numbers satisfy linear relations; arbitrary twenty-four positive parameters do not define a closed polygon. In particular, if $u_0,\ldots,u_{17}$ are the oriented primitive tangent vectors of its sides and $\ell_i$ their affine lengths, closure requires $\sum_{i=0}^{17}\ell_i u_i=0$. The first eighteen parameters control the equator. The three surgery sizes $b_{18},b_{19},b_{20}$ measure the distances of the interior singularities from sides $0,6,12$; $b_{21},b_{22},b_{23}$ measure the distances of those same singularities to the opposite sides $9,15,3$. Doubling copies the three singularities into the other hemisphere. Thus the six latter parameters describe three singularities from both sides of the same disc, subject to the rank-$19$ relations, rather than six independent surgery sizes [@AET23, Construction 6.1 and Remark 6.4].

::: {#fig-k3-coxeter-19-1-1 .figure}
\begin{tikzpicture}[scale=0.56]
\pic {object=coxeter/vinberg-19-1-1};
\end{tikzpicture}

The Coxeter diagram of the cusp lattice $U\oplus E_8(-1)^2\oplus A_1(-1)$; the full diagram also contains the four parabolic types that label the degree-two K3 $1$-cusps [@AET23, §5A, Fig. 1 and §3B].
:::

The reflection group $W(N)$ acts on the positive cone, and the chamber $K$ is a fundamental domain. Its diagram has an $S_3$ symmetry; more precisely $\operatorname O^+(N)=S_3\ltimes W(N)$ [@AET23, §4, Lemma 4.4]. Thus the four parabolic labels above are types modulo this symmetry, while individual parabolic subdiagrams can occur more than once in the full diagram.

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

For Enriques degenerations the quotient complexes are $\RP^2$ and a disc in Type III, and a segment in Type II (@prop:enriques-quotient-dual-complex). The degree-two Enriques stable-limit components are read from the folded Coxeter diagrams (@prop:fen2-stable-limit-strata). The marked Coble-root compatibility is @qst:coble_cusp_admissibility.

For a K3 quotient $\pi\colon X\to Y$ by a nonsymplectic involution, the exceptional curves on $Y$ (irreducible curves of negative self-intersection) have square $-4$, $-2$, or $-1$. A $(-4)$-curve is the image of a pointwise fixed $(-2)$-curve on $X$ and lies in the branch divisor. A $(-2)$-curve lifts to two disjoint $(-2)$-curves exchanged by the involution and misses the branch divisor. A $(-1)$-curve has two possible lifts: one invariant curve meeting the ramification divisor twice, or two exchanged curves meeting once [@AE22, Lemma 4.2]. This distinction matters when a wall of the K3 nef cone descends to a wall of a quotient stable model.

The degree-two K3 model also gives concrete boundary questions for the Enriques and Coble loci. At each Enriques cusp, which folded Coxeter walls survive the quotient by the Enriques involution? Can the K3 integral affine sphere be quotiented to an integral affine $\RP^2$ while keeping the divisor that determines its stable pair? For the Coble locus, how do the commuting Enriques and covering involutions act on the affine complex, and how does the intersection of their ramification data mark the Coble root? Which collisions of affine singularities and equator edges change the stable surface, and which are changes of Kulikov model by flops? The folded Coxeter strata below answer the component question for degree-two Enriques surfaces; the root and contraction questions remain part of @qst:coble_cusp_admissibility and @conj:restricted_ramification_semifan. A triangulated affine complex alone does not determine a unique smoothing or stable contraction, by @def:d-semistability and [@AET23, §§6–7].

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

::: {.proposition #prop:ksba-period-extension-conditional title="Period extension under the compactification comparison"}

If @conj:ksba_semitoroidal_comparison holds, then the period map of the polarized Coble locus extends from the normalization of its KSBA compactification to the Baily--Borel compactification of its period quotient.
:::

::: {.proof}

Under the conjectured identification, the normalized KSBA space is semitoroidal. Compose this identification with the semitoroidal morphism to the Baily--Borel compactification in @cor:toroidal-to-baily-borel. On the interior, the composite is the original period map.
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
