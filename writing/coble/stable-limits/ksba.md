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

For Enriques degenerations the quotient complexes are $\RP^2$ and a disc in Type III, and a segment in Type II (@prop:enriques-quotient-dual-complex). The degree-two Enriques stable-limit components are read from the folded Coxeter diagrams (@prop:fen2-stable-limit-strata). The arithmetic test for marked Coble roots is @thm:coble-cusp-admissibility.

For a K3 quotient $\pi\colon X\to Y$ by a nonsymplectic involution, the exceptional curves on $Y$ (irreducible curves of negative self-intersection) have square $-4$, $-2$, or $-1$. A $(-4)$-curve is the image of a pointwise fixed $(-2)$-curve on $X$ and lies in the branch divisor. A $(-2)$-curve lifts to two disjoint $(-2)$-curves exchanged by the involution and misses the branch divisor. A $(-1)$-curve has two possible lifts: one invariant curve meeting the ramification divisor twice, or two exchanged curves meeting once [@AE22, Lemma 4.2]. This distinction matters when a wall of the K3 nef cone descends to a wall of a quotient stable model.

The degree-two K3 model also gives concrete boundary questions for the Enriques and Coble loci. At each Enriques cusp, which folded Coxeter walls survive the quotient by the Enriques involution? Can the K3 integral affine sphere be quotiented to an integral affine $\RP^2$ while keeping the divisor that determines its stable pair? For the Coble locus, how do the commuting Enriques and covering involutions act on the affine complex, and how does the intersection of their ramification data mark the Coble root? Which collisions of affine singularities and equator edges change the stable surface, and which are changes of Kulikov model by flops? The folded Coxeter strata below answer the component question for degree-two Enriques surfaces, and @thm:coble-cusp-admissibility supplies the arithmetic marking test. The geometric contraction question remains part of @conj:restricted_ramification_semifan. A triangulated affine complex alone does not determine a unique smoothing or stable contraction, by @def:d-semistability and [@AET23, §§6–7].

::: {.proposition #prop:fen2-limits-are-k3-quotients title="Enriques stable limits are quotients of K3 stable limits"}

Let $(Z, \eps R_Z)$, $0 < \eps \ll 1$, be the pair of a degree-$2$ numerically polarized Enriques surface $Z \in \fentwo$.
Every KSBA stable limit of such pairs is the quotient of a KSBA stable limit of K3 pairs $(X, \eps R)$, $X \in \fttz$, by an Enriques involution [@AEGS25, §7.3].
:::

::: {.proposition #prop:fen2-stable-limit-strata title="Boundary strata of $\ksbacpt{\fentwo}$ from folded Coxeter diagrams"}

For $k = 1, \dots, 5$ let $G_k$ be the folded Coxeter diagram of the $0$-cusp $k$ of $\fentwo$.

1. The semifan $\semifan{F}_k$ of the $0$-cusp $k$ is the generalized Coxeter semifan (@def:generalized-coxeter-semifan) of $G_k$, with irrelevant roots the foldings of the irrelevant roots of the K3 diagrams [@AEGS25, Def. 5.4 and Lemma 5.5, printed p. 611].

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

::: {.definition #def:coble-descended-ramification title="The descended ramification divisor $R_{\bar S}$ of a stable limit"}

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


::: {.proposition #prop:marking-line-no-coble-lift title="The marking-line root of a marked cusp lies in no $\Gamma_{\Co,2}$-orbit"}

At each marked cusp $[I]$ among Sterk's cusps $3$, $4$ and $5$, with representative $\eta_I \in T_\Co = \delta^{\perp\ten}$ and boundary lattice $K_I = \eta_I^{\perp\ten}/\ZZ\eta_I$, the marking-line root $[\pm\delta] \in K_I$ has $\delta$-pairing $-\delta^2 = 2 \neq 0$.
Every lift $\pm\delta + k\eta_I$ with $k \in \ZZ$ pairs with $\delta$ as $\pm\delta^2 = \mp 2 \neq 0$, so no lift lies in $T_\Co = \delta^{\perp\ten}$, and the marking-line root lies in no $\Gamma_{\Co,2}$-orbit.
:::

::: {.proof}
At the marked cusps the representative is orthogonal to the Coble root, $\eta_I \cdot \delta = 0$ (`computations/reports/coble_cusp-admissibility-run.txt`), and every lift therefore pairs with $\delta$ as $\pm\delta^2 + k(\eta_I \cdot \delta) = \mp 2 + 0 \neq 0$.
A vector of $T_\Co = \delta^{\perp\ten}$ pairs trivially with $\delta$, so no lift lies in $T_\Co$, and $\Gamma_{\Co,2} = R_{\gent}$ is a subgroup of $\Orth(T_\Co)$ by @prop:gamma-co-images(3): the marking-line root is outside the domain of the group.
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
Distinct classes are not distinct $\Gamma_{\Co,2}$-orbits, and the difference decides the question: let $r$ be a root of $K_I$ orthogonal to $\delta$ and $s_r$ the reflection in it. Then $s_r$ is an isometry of $\ten$, since a root of a $2$-elementary lattice satisfies $2\div(r) \in (r\cdot r)\ZZ$ [@AEGS25, §3.4, printed p. 591]; it preserves $\ZZ\delta$, so it lies in $\Gamma_{\Co,2} = \Stab_{\Orth(\ten)}(\ZZ\delta)$ (@prop:gamma-co-2-line-stabilizer); and it fixes $\eta_I$, so it acts on $K_I$ and carries the class of $r$ to the class of $-r$. Those are different classes, because $2r \in \ZZ\eta_I$ would make the non-isotropic $r$ a rational multiple of the isotropic $\eta_I$. The computation of classes therefore does not decide the $\Gamma_{\Co,2}$-orbits of the three classes at cusp $5$, and it is those orbits, not the faces, that @conj:no_moduli_loss turns on.
The boundary lattice's own invariants do not decide them either: the complements $r^\perp_{K_5}$ of the three classes are all the even lattice of rank $9$, determinant $512 = 2^9$, signature $(1,8)$ and coparity $\delta = 1$, hence isometric, since an indefinite even $2$-elementary lattice is determined by its signature and the triple $(r, a, \delta)$ [@AEGS25, §2.3, printed p. 586] (`computations/reports/coble_cusp5-complement-isometry-run.txt`: all three print `rank 9, det 512, signature (1, 8), Smith [2^9], even True, coparity delta 1`). So no invariant of $K_5$ separates the three classes, and what remains is the orbit computation under the image of $\Gamma_{\Co,2}$ in $\Orth(K_5)$. The reflection route is closed outright: the square-$(-2)$ printed roots at cusp $5$ are pairwise orthogonal, and neither a sum nor a difference of two of them is a root, so a reflection in any of them fixes the other two classes up to sign and no product of such reflections carries one class to another (`computations/reports/coble_cusp5-class-orbits-run.txt`, section (0)); under the eleven roots that fix both $\delta$ and $\eta_5$ each orbit still passes $20\,001$ classes without closing and none contains another; the one cusp symmetry that fixes the Coble root's label and exchanges the labels of $13$ and $14$ **lifts**: its linear action fixes $\delta$ itself, and since $T_\En = S \perp S^\perp$ with $S$ the rank-$10$ span of the roots and $S^\perp$ of determinant $-4$, the map equal to that action on $S$ and to the identity on $S^\perp$ is an integral isometry of $T_\En$ fixing $\delta$ (`computations/reports/coble_759-lift-1314-run.txt`: $M^\top G M = G$, $M\delta = \delta$, $M r_i = r_{\sigma(i)}$, $\det M = -1$); so roots $13$ and $14$ are one $\Gamma_{\Co,2}$-orbit and only the pair $(12,13)$ is left, and that pair is not touched by the same construction: the span of $r_{12}$, $r_{13}$ and $\delta$ is not a direct summand of $T_\En$, its index being $2$ for the class of $r_{13}$ shifted by any multiple of $\eta_5$, and inside the rank-$10$ span of the fourteen roots $\langle r_{12},r_{13}\rangle$ is not a summand either, its index there also being $2$, so the swap meets a gluing obstruction at both ranks and settles nothing (`computations/reports/coble_759-swap-1213-run.txt`), and the transporter that would decide the pair is refused outright: the family $\{r_{12},\delta,\eta_5\}$ onto $\{r_{13},\delta,\eta_5\}$ has nontrivial pointwise orthogonal stabilizer, which the library's spanning hypothesis excludes — "this computation requires the full space or an isotropic hyperplane, whose pointwise orthogonal stabilizer is trivial" (`computations/reports/coble_759-transporter-1213-run.txt`); the invariant lattices of the two roots, $(r^\perp\cap\delta^\perp\cap\eta_5^\perp)/\ZZ\eta_5$, agree in rank, determinant, Smith invariants, signature and parity, and their discriminant forms agree as well, $|A| = 256$ on both with the same multiset of $q$-values, so that comparison separates nothing either (`computations/reports/coble_759-invariant-lattices-1213-run.txt`), and the integral witness later built on that span is not in $\gent$ either, for the same reason (`computations/reports/coble_760-gent-membership-run.txt`);
the orbit operation itself has been run: at cusp $5$ it returns three singleton orbits, one per class (sage-extensions, `results/issue370-the-coble-root-orbits.md`), and by that document's own reading a singleton is not a proof of inequivalence, the acting family not being certified complete; here it is demonstrably incomplete, since it separates $13$ from $14$ and those are equivalent by the isometry above. So the pair $(12,13)$ is undecided in both directions, and what it needs is a certified-complete acting family; and no operation in the library decides these orbits, since the orbit series of $K_5$ does not return within a $600$ s bound and no reduction, normal form or orbit invariant for a stabilizer subgroup is exposed (`computations/reports/coble_760-orbit-decision-probe-run.txt`); the widest search that exists, over words in all fourteen printed roots with $\delta$ and $\eta_5$ tested on the word, finds no transporter of the class of $12$ to that of $13$ or $14$ within depth $10$ over $135\,571$ classes, and that is a bound and not a proof, the group being infinite (`computations/reports/coble_760-orbit-witness-run.txt`).
:::

::: {.conjecture #conj:no_moduli_loss title="The marking of a marked cusp is read off the contracted $(-4)$-curve, not off a face"}

**Open at one pair.** The form of this statement that the issue asks about --- degenerations at a marked cusp whose marked roots are $T_\Co$-roots, inequivalent under $\Gamma_{\Co,2}$, are not identified in the KSBA boundary --- is vacuous at cusps $2$, $3$ and $4$ and open at cusp $5$: the first three carry at most one admissible $T_\Co$-root each (@prop:marking-line-no-coble-lift, @thm:face-irrelevant-marking(2)), and at cusp $5$ the roots $13$ and $14$ are one $\Gamma_{\Co,2}$-orbit while the root $12$ is in their $O(\ten)$-orbit and is not shown to be $\Gamma_{\Co,2}$-equivalent to them (@rmk:coble-root-orbits-cusp-five). If $12$ is inequivalent to $13$ the hypothesis is met at cusp $5$ and the conclusion fails there; if it is equivalent the hypothesis is never met and the conclusion holds vacuously. The paragraphs below record the state of the weaker, curve-based reading of the recovery.

The stable quotient determines its marked Coble root among the $T_\Co$-roots of each marked cusp: the $\frac{1}{4}(1,1)$ singularity of @prop:coble-quarter-singularity -- equivalently, the contracted anti-bicanonical $(-4)$-curve of @prop:antibicanonical-system -- recovers it, so that degenerations at a marked cusp whose marked roots are $T_\Co$-roots, inequivalent under $\Gamma_{\Co,2}$, are not identified in the KSBA boundary.

**What the face does and does not give.** This conjecture asked a face of the restricted semifan to carry the marking, and no face can: by @thm:face-irrelevant-marking every admissible $T_\Co$-root at every marked cusp is irrelevant, so all of them cut one maximal cone, and at cusp $5$ the three roots $12$, $13$ and $14$ cut it together.
Whether the conjecture then fails at cusp $5$ turns on the single pair $(12,13)$: roots $13$ and $14$ are one orbit (@thm:face-irrelevant-marking(3), `computations/reports/coble_759-lift-1314-run.txt`), and the orbit operation returns three singleton orbits at cusp $5$ (sage-extensions, `results/issue370-the-coble-root-orbits.md`), which is not a proof of inequivalence — the acting family is not certified complete, and on this page's data it is demonstrably incomplete, separating $13$ from $14$; if $12$ and $13$ are inequivalent, their two degenerations are identified in the KSBA boundary and no face separates them, and the conjecture is false; if they are one orbit, the hypothesis of the conjecture is never met at cusp $5$. Distinct classes in $K_5$ do not decide this (`computations/reports/coble_coble-root-orbits-run.txt`, @thm:face-irrelevant-marking(3)). Nor does an isometry of $\ten$ that fixes $\delta$ and $\eta_5$ but lies outside $\gent$: the transposition of the two square-$(-2)$ generators of the saturation of $\generators{\delta, r_{12}, r_{13}}$ is integral, of determinant $-1$ and form-preserving, and carries the class of $12$ to that of $13$, but it carries classes out of both summands of $A_{\ten}$, so it is not in $\gent$ and settles nothing (`computations/reports/coble_760-gent-membership-run.txt`).
The recovery asserted here is therefore a statement about the contracted curve alone: the divisor it would be read off is @def:coble-descended-ramification, defined from [@AEGS25, §2.4, printed p. 588] and [@AEGS25, Prop. 6.1(2), printed p. 616].
It has no referent yet, and so cannot be computed: reading a class of $K_I$ off a curve of $\bar S$ needs a dictionary from the roots of the chamber to curves of the Coble surface, and the sources supply none — a search of the two sources the warning names finds no such identification, the word "Coble" not occurring at all in Alexeev--Nikulin and "simple root" not occurring in Dolgachev--Kondo, so the marking is a definition to be made and not a citation to be found (`computations/reports/coble_760-cusp-marking-search-run.txt`, @warn:coble-marking).
Nor do the cusp's own symmetries supply one: of the eight symmetries of the labelled cusp-$5$ Gram exactly one swaps the labels of $12$ and $13$, and it moves the Coble root's label $11$ (`computations/reports/coble_760-cusp-symmetry-run.txt`).
Nor does the statement follow from an isomorphism of stable pairs without one of the two routes: that needs a cited statement that a stable pair over a cusp determines its lattice data, and the nearest statement read does something else — [@AEGS25, Thm. 5.9, printed p. 611] identifies the normalization of $\ksbacpt{\fentwo}$ with the semitoroidal compactification and shows that no moduli are lost in passing from K3 pairs to their Enriques quotients, which is not that determination.
The pair the page carried as a counterexample before -- roots $11$ and $12$ at cusp $5$ -- is withdrawn on a different ground: root $11$ is the marking line $[\pm\delta]$, which has no lift in $T_\Co$ by @prop:marking-line-no-coble-lift, so that pair was never comparable; the comparable pair is $12$ and $13$ at cusp $5$, and whether it is a pair of inequivalent roots is the computation left open here.

The group that the determination is modulo is $\Gamma_{\Co,2} = R_{\gent}$, the image of $\Stab_{\gent}(\delta)$ in $\Orth(\delta^{\perp})$ (@prop:gamma-co-images, @prop:gamma-co-2-line-stabilizer): the stabilizer of the root line $\ZZ\delta$ in $\gent$.
It is not the monodromy group $\Gamma_{\Co}$ of @def:gamma-co-groups, whose equality with the stable subgroup $\widetilde{\Orth}^+(T_{\Co})$ is @conj:gamma-co-stable.
The marking-line root is not among the $T_\Co$-roots by @prop:marking-line-no-coble-lift, and at cusp $2$ the unique admissible root is the marking line itself, so no $T_\Co$-root exists there.
Cusps $3$ and $4$ carry one $T_\Co$-root each and so no pair, which leaves cusp $5$, whose three roots are pairwise distinct classes of $K_5$ (@thm:face-irrelevant-marking(3)) of which $13$ and $14$ are one $\Gamma_{\Co,2}$-orbit and $12$ is undecided (@rmk:coble-root-orbits-cusp-five).
:::

::: {.remark #rmk:coble-root-orbits-cusp-five title="Two of the three admissible roots at cusp $5$ are one $\Gamma_{\Co,2}$-orbit; the third is undecided"}

The three admissible $T_\Co$-roots at cusp $5$ have pairwise distinct classes in $K_5$, so they are three distinct roots; what is undecided is whether they are three markings.
Each root of $K_5$ that is the class of a $(-4)$- or $(-2)$-vector of $T_\Co$ orthogonal to $\eta_5$ --- Sterk's printed labels $1$--$8$ and $12$--$14$ --- lifts to a vector $w$ of $\ten$ with $2\div(w)\in(w\cdot w)\ZZ$, so $s_w$ is an integral isometry [@AEGS25, §3.4, printed p. 591]; it fixes $\delta$, so it lies in $\Gamma_{\Co,2}$ (@prop:gamma-co-2-line-stabilizer); and it fixes $\eta_5$, so it acts on $K_5$.
Being an isometry of $\ten$ is not enough to lie in $\Gamma_{\Co,2} = R_{\gent}$, which is the image of $\Stab_{\gent}(\delta)$, and $\gent$ is strictly smaller than $O(\ten)$: by [@AEGS25, Def. 2.6] it is the image of the centralizer of the Enriques involution in $O(L)$, and by [@Ste91, Prop. 2.7] that image is exactly the set of isometries whose induced map on the discriminant module respects its decomposition in two summands, here $A_{U(2)}\oplus A_{E_8(-2)}$ of orders $4$ and $256$ (@prop:gamma-co-images). A record tests that condition directly --- in the dual-basis coordinates where the discriminant module is $\ZZ^{12}/G\ZZ^{12}$ the induced map is $a\mapsto g^{\mathsf T}a$ --- and calibrates the test on the elements this page already places in $\Gamma_{\Co,2}$: the identity, $-\id$, and all eleven reflections in printed roots orthogonal to $\delta$ pass it (`computations/reports/coble_760-gent-membership-run.txt`).
Of the two candidates one passes and one does not.
The unique symmetry of the labelled cusp-$5$ Gram that fixes the Coble root's label $11$ and exchanges labels $13$ and $14$ lifts to an integral isometry of $\ten$ fixing $\delta$ and $\eta_5$ and preserving both summands, so roots $13$ and $14$ are $\Gamma_{\Co,2}$-equivalent (`computations/reports/coble_760-witness-13-14-run.txt`, `computations/reports/coble_760-gent-membership-run.txt`).
For the pair $12$, $13$ no symmetry of the printed diagram suffices: the transposition that would serve does not preserve the labelled Gram, and the span of $\delta$, $r_{12}$, $r_{13}$ is not a direct summand of $\ten$, its saturation having index $2$. The transposition of the two square-$(-2)$ generators of that span, extended by the identity on the rank-$9$ complement, is integral, of determinant $-1$ and form-preserving, and it exchanges the two lifts; but it carries the classes $[d_4]$, $[d_6]$, $[d_7]$ and $[d_{11}]$ out of their summands, so it lies outside $\gent$ (`computations/reports/coble_760-witness-12-13-run.txt`, `computations/reports/coble_760-gent-membership-run.txt`). It witnesses that $12$ and $13$ lie in one $O(\ten)$-orbit, and nothing more.
So at cusp $5$ the roots $13$ and $14$ form one $\Gamma_{\Co,2}$-orbit, the root $12$ is undecided, and the question the issue asks is open exactly at that pair; cusps $3$ and $4$ carry one admissible root each, and cusp $2$ only the marking line (@prop:marking-line-no-coble-lift), so no pair exists there at all.
:::

::: {.warning #warn:no-moduli-loss-vacuity title="The step that fails: one $\Gamma_{\Co,2}$-orbit at cusp $5$"}

An earlier version of this page carried, until `bdb78a77ce`, a theorem `thm:no-moduli-loss-vacuous` stating that the three admissible roots at cusp $5$ are pairwise $\Gamma_{\Co,2}$-equivalent and that @conj:no_moduli_loss therefore holds vacuously.
That argument is withdrawn.
It rested on two integral isometries of $\ten$ fixing $\delta$ and $\eta_5$, and being an isometry of $\ten$ is not the same as lying in $\gent$: $\Gamma_{\Co,2} = R_{\gent}$ is the image of $\Stab_{\gent}(\delta)$, and $\gent$ is the summand-preserving subgroup of $O(\ten)$ ([@AEGS25, Def. 2.6], [@Ste91, Prop. 2.7]), which the proof of @prop:gamma-co-images on this page states.
Of the two witnesses only the $13\leftrightarrow14$ one preserves the two summands of $A_{\ten}$; the $12\leftrightarrow13$ one does not, so it proves an $O(\ten)$-orbit and not a $\Gamma_{\Co,2}$-orbit (`computations/reports/coble_760-gent-membership-run.txt`).
The pair $(12,13)$ is therefore open in both directions, as @rmk:coble-root-orbits-cusp-five states, and no statement on this page asserts that the hypothesis of @conj:no_moduli_loss is never met.
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

