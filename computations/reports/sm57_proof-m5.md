# A21: the chamber clause — corrected account, and an unconditional obstruction

Member m5, swarm `smvz57fr3`, direction d2. Second submission, after the referee's correction.
**Withdrawn:** the first submission's Theorem A ("A21 with the chamber on the Picard-rank-$3$
stratum") — its stratum is empty, because every one-node member has
$\operatorname{Pic}\supseteq S_{\mathrm{Co}}$ of rank $11$ (§1.3). Nothing below uses it.
**Kept, as the referee confirmed:** the uniform ample class $H-t\alpha$ (§2) and the
period-independence of the effective $(-2)$-classes (§3).
**New:** an obstruction that needs no genericity premise and no "very general member"
(§§5–7): two explicit, computer-verified one-node members whose tuples cannot be conjugate in
either of the two readings of the fourth bullet under which that bullet has content (§4).

Throughout, the repo is `/workspace/nucleus/work/projects/p-9fcb4ed7f4b64e008de2ee29a7197bf4/repo`,
cited by `file:line`, and was not modified. Repo statement labels are written in backticks.

## 0. Verdict

1. **A21 is false as stated** (Theorem 7.1). The two tuples of §6 both arise from the direct
   projective construction, both satisfy the five authored bullets, their labels, $H$ and
   $\alpha$ *are* conjugate, and no isometry of $L_{K3}$ preserving the labels, $H$ and $\alpha$
   can carry one chamber onto the other. The clause that fails is the fourth; the invariant that
   decides it is the number of $(-2)$-classes of $H$-degree $1$ (§5), which is $0$ for one member
   and $\ge 2$ for the other, and which equals the number of rulings of the two fibrations whose
   fibre is reducible away from the two forced ones.
2. The failure is not about a missing generic member: the invariant is decided on each member by
   a finite computation (the two ruling discriminants, §6). It *is* about the semantics of the
   fourth bullet (§4): under the reading "the chamber sees only the labels' own lattice
   $N=\langle e,f,\alpha\rangle$" A21 holds (m6, `.ultramath/smvz57fr3/m6/a21-chamber-obstruction.md`
   §4.6); under the two readings in which the bullet constrains the member's actual cone — the
   Kähler cone, or the chamber of the member's own effective roots (`rmk:chamber-not-transported`,
   `...the-heegner-line-and-the-coble-arithmetic-group.md:657`) — it fails.
3. What survives of the positive direction: the chamber clause is a theorem on any subfamily of
   constant Picard lattice (§8, Theorem 8.1), and the corpus' missing input
   (`prob:projective-coverage`; m8's Lemma 4.4) is exactly what would supply the natural such
   stratum, the general member. It is *not* needed for the obstruction.

## 1. Set-up

$Y=\PP^1\times\PP^1$ with affine coordinates $(x,y)$ in which $p=(0,0)$; $\tau=(-1,-1)$;
$f$ runs over the $13$ monomials $x^iy^j$, $0\le i,j\le4$, $i+j$ even, with $f(p)=0$ and a
nondegenerate quadratic part (`sec-invariant-system`, `lem:node-condition`).
$X^\sharp=\{z^2=f\}\to Y$, $\widehat X_b\to X^\sharp$ the minimal resolution, $D_b$ the exceptional
$(-2)$-curve, $H_b=\pi^*\OO_Y(1,1)$, $\alpha_b=[D_b]$, $\iota_{\mathrm{dP}}=(x,y,-z)$,
$\iota_{\mathrm{Co}}=(-x,-y,-z)$ (`prop:local-operators`).

**1.1** (repo `lem:face-at-H` part 1, re-derived in the first submission and kept) With
$\widehat Y=\Bl_pY$, $e$ the exceptional $(-1)$-curve and $h_1,h_2$ the ruling classes
($h_1\cdot h_2=1$, $h_i^2=0$, $e\cdot h_i=0$, $e^2=-1$), there is a commutative diagram
$$\widehat X_b\xrightarrow{\ \widehat\pi_b\ }\widehat Y,\qquad
\widehat\pi_b^{-1}(e)=D_b,\qquad \alpha_b=\widehat\pi_b^*e,\qquad H_b=\widehat\pi_b^*\OO(1,1),$$
$\widehat\pi_b$ finite of degree $2$ branched along $\widetilde B=-2K_{\widehat Y}=4h_1+4h_2-2e$.
Put $e_b:=\widehat\pi_b^*h_1$, $f_b:=\widehat\pi_b^*h_2$; then
$H_b=e_b+f_b$, and in the basis $(e_b,f_b,\alpha_b)$,
$$M_b:=\widehat\pi_b^*\operatorname{Pic}(\widehat Y)=\langle e_b,f_b,\alpha_b\rangle,\qquad
G=\begin{pmatrix}0&2&0\\2&0&0\\0&0&-2\end{pmatrix},\quad\det=8,\ \operatorname{sig}=(1,2).$$
$e_b,f_b,H_b,\alpha_b$ are flat sections of $R^2\widehat\pi_*\ZZ$ over the one-node locus
(`prop:one-node-family` part 4 and the relative rulings).

**1.2 The numerics used below** (verified in `computations/lattice.py`):
$(e_b-\alpha_b)^2=(f_b-\alpha_b)^2=-2$, $(e_b-\alpha_b)\cdot H_b=(f_b-\alpha_b)\cdot H_b=2$,
$H_b^2=4$, $H_b\cdot\alpha_b=0$, $e_b\cdot\alpha_b=f_b\cdot\alpha_b=0$, $e_b\cdot f_b=2$.

**1.3 Lemma (the referee's correction, recorded with proof).** Let $\iota$ be a *nonsymplectic*
involution of a K3 surface $X$. Then $H^2(X,\ZZ)^{\iota}\subseteq\operatorname{Pic}(X)$.
*Proof.* $\iota$ acts on $H^{2,0}(X)$ by $-1$ and on $H^{1,1}(X)$ by $+1$ (it is holomorphic).
For $u\in H^2(X,\ZZ)$ with $\iota u=u$, the Hodge components satisfy $u^{2,0}=u^{0,2}=0$; hence
$u\in H^{1,1}(X)$ and, by Lefschetz $(1,1)$, $u\in\operatorname{Pic}(X)$. $\square$

Consequently, for every one-node member, $\operatorname{Pic}(\widehat X_b)\supseteq S_{\mathrm{Co}}$
and $\rho(\widehat X_b)\ge\operatorname{rk}S_{\mathrm{Co}}=k+10=11$ for $k=1$
(`prop:tuple-of-the-construction` for the ranks, which uses only rational eigensplittings).
**This is why the first submission's rank-$3$ stratum is empty**: I withdraw that theorem, and
with it everything that used $\operatorname{Nef}=\operatorname{cone}(e,f,H-\alpha)$ as an
equality. The inclusion $\operatorname{cone}(e_b,f_b,H_b-\alpha_b)\subseteq\operatorname{Nef}$
(Theorem 2.2, Corollary 2.4) is not affected.

## 2. Salvaged: one ample class, defined by the labels, valid on every member

**Lemma 2.1.** For $0<t<1$, $M_t:=\OO_{\widehat Y}(1,1)-t\,e$ is ample on $\widehat Y$; $M_1$ is
nef; $M_0=\OO(1,1)$ is nef and big.

*Proof.* For an irreducible curve $C\subset\widehat Y$, $C\ne e$, write $C$ as the proper
transform of an irreducible $C_Y\subset Y$ of bidegree $(\alpha',\beta')$ with multiplicity
$m=m_p(C_Y)$ at $p$. Then $C\cdot h_1=\beta'$, $C\cdot h_2=\alpha'$, $C\cdot e=m$; for $C=e$,
$C\cdot h_i=0$, $C\cdot e=-1$. For irreducible $C_Y$ either $C_Y$ is a ruling
($m\le1=\alpha'+\beta'$), or no ruling through $p$ is a component of $C_Y$, and intersecting with
the two rulings through $p$ gives $m\le\alpha'$ and $m\le\beta'$. So $m\le\alpha'+\beta'$ and
$$M_t\cdot C=\alpha'+\beta'-tm\ge(1-t)m\ \ (C\ne e),\qquad M_t\cdot e=t>0,$$
which is $>0$ for $0<t<1$, while $M_t^2=2-t^2>0$. Nakai–Moishezon on $\widehat Y$ gives
ampleness; at $t=1$ the class vanishes on the proper transform $h_1-e$ of the ruling through $p$
and is $\ge0$ elsewhere, so it is nef with $M_1^2=1$. $\square$

**Theorem 2.2.** On every one-node member, $L_t:=H_b-t\,\alpha_b=\widehat\pi_b^*M_t$ is ample for
$0<t<1$, and $L_1=H_b-\alpha_b$ is nef of square $2$; $e_b$ and $f_b$ are nef.
Consequently $C\cdot e_b\ge0$, $C\cdot f_b\ge0$, $C\cdot(H_b-\alpha_b)\ge0$ for every effective
class $C$, and (Nakai–Moishezon, as in the first submission)
$\operatorname{int}\operatorname{cone}(e_b,f_b,H_b-\alpha_b)\subseteq K_b$, the Kähler cone.
*Proof.* $\widehat\pi_b$ is finite and $L_t$ is the pullback of an ample class. $\square$

**Remark 2.3.** $L_{1/2}$ is one and the same label-defined class on every member: an explicit
ample class, of square $7/4$, whose existence does not depend on the period. It is *not* enough
to compare chambers (§8), but it does pin the local picture at $[H_b]$ (only $\alpha_b^\perp$ is
a wall there, §3) on the whole locus.

## 3. Salvaged: the effective $(-2)$-classes are period-independent

**Theorem 3.1.** For every one-node member $b$ (with $H_b$ nef),
$$\Delta_b:=\{\delta\in\operatorname{Pic}(\widehat X_b):\ \delta^2=-2,\ \delta\ \text{effective}\}
=\{\delta\in\operatorname{Pic}(\widehat X_b):\ \delta^2=-2,\ \delta\cdot H_b>0\}\cup\{\alpha_b\}.$$
In particular $\Delta_b$ is determined by $(\operatorname{Pic}(\widehat X_b),H_b,\alpha_b)$.

*Proof.* Riemann–Roch gives $\chi(\OO(\delta))=1$ and $h^0(\delta)+h^0(-\delta)\ge1$, so $\pm\delta$
is effective; nefness of $H_b$ decides which sign, except for $\delta\cdot H_b=0$, where Lemma 3.2
gives $\delta=\pm\alpha_b$. $\square$

**Lemma 3.2.** An effective class $C$ with $C\cdot H_b=0$ is a multiple of $\alpha_b$.
*Proof.* $C\cdot H_b=\OO(1,1)\cdot\widehat\pi_{b*}C$, and $\OO(1,1)$ is the pullback of the ample
$\OO_Y(1,1)$, so it is $\ge0$ on every curve and vanishes only on curves contracted by
$\widehat Y\to Y$, i.e. on $e$; hence $\widehat\pi_b(C)\subseteq e$ and $C\subseteq D_b$, which is
irreducible. $\square$

Two consequences used below: the only $(-2)$-classes orthogonal to $H_b$ are $\pm\alpha_b$; and
the walls of the arrangement of $b$ through $[H_b]$ are exactly $\alpha_b^\perp$ (as in
`lem:face-at-H` part 4, whose proof is the one just given).

## 4. What the fourth bullet can mean, and which reading the obstruction addresses

The authored bullet is: "$\mathfrak c$ the chosen positive/nef chamber in which $\alpha$ is
effective and $H$ is nef and big"
(`writing/coble/heegner-report/coble-heegner-research-report.md:601-638`).
m6's analysis (`.ultramath/smvz57fr3/m6/a21-chamber-obstruction.md` §4.1, §4.5, §4.6) identifies
the readings, and I follow it:

* **Reading L** (m6 §4.6; labels' own lattice). $\mathfrak c$ is the chamber of the arrangement cut
  by the classes of $N=\langle e,f,\alpha\rangle$ only. Then $\mathfrak c$ is a function of
  $(H,\alpha)$ (only $\alpha^\perp$ passes through $[H]$), hence transported by any label isometry,
  and **A21 holds in full**. In this reading the fourth bullet carries no information about the
  member's cone of curves.
* **Reading C** (m6 §4.1 = repo `rmk:chamber-not-transported`; the member's own effective roots).
  $\mathfrak c$ is the component of $\mathcal P\setminus\bigcup_{\delta\in\Delta_b}\delta^\perp$
  containing the Kähler cone. This is the reading under which the bullet is not vacuous, and under
  which `prop:chamber-conditional` is stated.
* **Reading K** (the literal "positive/nef chamber": $\mathfrak c$ is the *nef* cone
  $\operatorname{Nef}(\widehat X_b)$ of the member, equivalently its interior, the Kähler cone —
  the two determine each other). This is the reading under which "$H$ is nef and big in
  $\mathfrak c$" is literally true ($H_b\in\operatorname{Nef}$, on its boundary) and under which
  the chamber is *the* isomorphism-invariant cone of the surface.

The obstruction of §§5–7 is proved in **Reading K and Reading C**. Under Reading L, A21 is a
theorem (m6 §4.6, and §3 gives the one-wall statement it needs), so the failure below is a
statement about the semantics of the fourth bullet and not about the rest of the tuple. This is
the honest form of the answer: *A21 is false, and the clause that fails is the fourth; under the
weakest reading of that clause it is true precisely because the clause then says nothing about
the member.*

## 5. The invariant: a $(-2)$-class of $H$-degree $1$ is an extra reducible ruling fibre

**Lemma 5.1.** Let $b$ be a one-node member, $C\in\operatorname{Pic}(\widehat X_b)$ with
$C^2=-2$ and $H_b\cdot C=1$. Then $C$ is effective (Theorem 3.1), and one of the following holds:
1. $C\cdot e_b=0$ and $C$ is a proper sub-divisor of a reducible fibre of the $h_1$-fibration
   $\widehat X_b\to\PP^1_{(x)}$;
2. $C\cdot e_b=1$, $C\cong\PP^1$, and $C$ is a proper sub-divisor of a reducible fibre of the
   $h_2$-fibration $\widehat X_b\to\PP^1_{(y)}$.
In either case some fibre of one of the two fibrations is reducible. In case 2 the ruling is not the
ruling through $p$; in case 1 the fibre over the ruling through $p$ is $I_2$ with component
$H$-degrees $0$ and $2$, so a curve of $H$-degree $1$ forces a reducible fibre over a ruling other
than the ruling through $p$.

*Proof.* $k:=C\cdot e_b\ge0$ because $e_b$ is nef and $C$ is effective. For any curve $C$,
$H_b\cdot C=k+m$ with $m:=C\cdot f_b\ge0$ (projection formula: $H_b\cdot C=(h_1+h_2)\cdot\widehat\pi_{b*}C$,
and $\widehat\pi_{b*}C$ has $h_1$-degree $k$ and $h_2$-degree $m$), so $k\le 1$.
If $k=0$ then $C\cdot e_b=0$, so every component of $C$ is contracted by $\widehat X_b\to\PP^1_{(x)}$,
i.e. each component lies in a fibre; no component can be a whole fibre (if $F\subseteq C$ then
$H_b\cdot(C-F)=1-2<0$ contradicts nefness of $H_b$ on the effective class $C-F$), so $C$ is a
proper sub-divisor of some reducible fibre.
If $k=1$ then $m=0$; $C\cdot e_b=1$ makes $C\to\PP^1_{(x)}$ birational, so $C\cong\PP^1$ and
$\widehat\pi_b(C)$ has class $mh_1+kh_2=h_2$: a ruling of the second family, not through $p$, over
which $C\cdot f_b=0$ makes $C$ a proper sub-divisor of the (reducible) fibre. The last sentence: the
fibre over the ruling through $p$ is $D_b+(L_1-D_b)$ with $H$-degrees $0$ and $2$ (as
$H_b\cdot D_b=0$ and $H_b\cdot(H_b-f_b)=2$), and it is the fibre over $x=0$. $\square$

**Corollary 5.2 (the invariant).** For a member $b$ define
$$\nu(b):=\#\{\delta\in\operatorname{Pic}(\widehat X_b):\ \delta^2=-2,\ \delta\cdot H_b=1\}.$$
Then $\nu(b)>0$ iff some ruling of $B$ other than the ruling through $p$ has a reducible fibre
(respectively, in the two families), and $\nu$ is an invariant of the tuple: any isometry $\gamma$
with $\gamma H_b=H_{b'}$ and $\gamma(\operatorname{span}\mathfrak c_b)
=\operatorname{span}\mathfrak c_{b'}$ carries $\{\delta:\delta^2=-2,\delta\cdot H_b=1\}$ onto the
corresponding set for $b'$.

*Proof.* Theorem 3.1 and Lemma 5.1 give the first claim. For the second: $\gamma$ preserves the
lattice and the intersection form and sends $H_b$ to $H_{b'}$, so it maps the set in question
bijectively onto the set for $b'$ — provided $\gamma\operatorname{Pic}(\widehat X_b)
=\operatorname{Pic}(\widehat X_{b'})$, which holds whenever $\gamma(\operatorname{span}\mathfrak c_b)
=\operatorname{span}\mathfrak c_{b'}$ (Reading K: $\operatorname{span}K_b=
\operatorname{Pic}(\widehat X_b)_\RR$). For Reading C the corresponding invariant is in §7. $\square$

## 6. The two members, verified

Everything in this section is a finite computation, recorded in `computations/`.

**Member $b_0$ (no $H$-degree-$1$ class).**
$$f_0=5x^4y^4-2x^4y^2+3x^4+x^3y^3-4x^3y+2x^2y^4+x^2y^2+2x^2-3xy^3+7xy-y^4-5y^2 .$$
(`computations/member_b0_full.py`.)
1. $f_0$ is $\tau$-invariant (only $i+j$ even monomials appear) and $f_0(p)=0$ with quadratic part
   $2x^2+7xy-5y^2$, of discriminant $7^2+40=89\ne0$: an ordinary node at $p$;
2. $B_0=\{f_0=0\}$ is smooth away from $p$: in the chart $X_1=Y_1=1$ the Gröbner basis of
   $\langle f_0,\partial_{x}f_0,\partial_yf_0\rangle$ is $\langle x,y\rangle$ (one reduced point,
   the node) and in each of the other three charts of $\PP^1\times\PP^1$ it is $\langle1\rangle$;
3. $\operatorname{disc}_y f_0=x^2\,q(x)$ with $q$ of degree $22$ occurring to multiplicity $1$ in the
   factorisation, and $\operatorname{disc}_x f_0=-y^2\,r(y)$ with $r$ of degree $22$ to multiplicity
   $1$; $\gcd(\operatorname{disc},\operatorname{disc}')=x$, respectively $y$.
   So the only reducible fibre of the $h_1$-fibration is the one over $x=0$ (the ruling through
   $p$, of type $I_2$, components $D_{b_0}$ and $L_1-D_{b_0}$ of $H$-degree $0$ and $2$) and the
   other $22$ singular fibres are irreducible nodal cubics; likewise for the $h_2$-fibration.
   By Lemma 5.1, $\nu(b_0)=0$.

**Member $b_\star$ (two $H$-degree-$1$ classes).**
$$f_\star=8x^4y^4+7x^4y^2+6x^4+5x^3y^3+4x^3y+3x^2y^4+2x^2y^2+3x^2-13xy^3-28xy-10y^4+13y^2 .$$
(`computations/verify_witness.py`, `computations/verify_charts.py`.)
1. $f_\star$ is $\tau$-invariant; $f_\star(p)=0$ with quadratic part $3x^2-28xy+13y^2$,
   discriminant $628\ne0$;
2. smooth away from $p$ in all four charts (same Gröbner computation, output recorded);
3. $f_\star(1,y)=(y-1)^2(y-3)^2$: the ruling $D=\{x=1\}$ (not the one through $p$) is bitangent to
   $B_\star$ at $(1,1)$ and $(1,3)$ and meets it nowhere else. Hence $\widehat\pi_{b_\star}^{-1}(D)$
   splits: $C_++C_-=\widehat\pi_{b_\star}^*D$ with $C_\pm\cong\PP^1$,
   $C_\pm^2=D^2-\tfrac12D\cdot\widetilde B=-2$, $C_+\cdot C_-=2$, and
   $C_\pm\cdot f_{b_\star}=h_2\cdot[D]=1$, $C_\pm\cdot H_{b_\star}=1$.
   By Theorem 3.1 both are effective, so $\nu(b_\star)\ge2$.

(The same member, found independently, is m6's Theorem 2.3 / finding f12; the verification here is
mine, and the referee reproduced it as "a valid one-node member".)

## 7. Theorem B: A21 is false, unconditionally

**Theorem 7.1.** Let $\mathfrak L_0,\mathfrak L_\star$ be the tuples of the direct projective
construction attached to $b_0$ and $b_\star$ (`prop:tuple-of-the-construction`: all five authored
bullets hold). Then:
1. the labels, the degree-$4$ class and the root are conjugate: there is
   $\gamma\in O(L_{K3})$ with $\gamma S_{\mathrm{Co}}=S'_{\mathrm{Co}}$,
   $\gamma S_{\mathrm{dP}}=S'_{\mathrm{dP}}$, $\gamma H=H'$, $\gamma\alpha=\alpha'$
   (m6 Corollary 3.2 — the transport along the connected parameter space of smooth members of the
   family of double covers of the fixed base $\widehat Y$, which does not use the disputed
   connectedness of the one-node locus; equivalently repo `thm:a21-labels`);
2. **no** isometry $\gamma$ of $L_{K3}$ with $\gamma H=H'$, $\gamma\alpha=\alpha'$ that conjugates
   the two involutions carries the chamber of $\mathfrak L_0$ to that of $\mathfrak L_\star$, in
   Reading K or in Reading C.

*Proof of (2), Reading K.* Suppose $\gamma\mathfrak c_0=\mathfrak c_\star$ with
$\mathfrak c=\operatorname{Nef}$. Then $\gamma\operatorname{span}\mathfrak c_0
=\operatorname{span}\mathfrak c_\star$, and $\operatorname{span}\operatorname{Nef}_b
=\operatorname{Pic}(\widehat X_b)_\RR$ (the Kähler cone is open in it), so
$\gamma\operatorname{Pic}(\widehat X_0)=\operatorname{Pic}(\widehat X_\star)$. By Corollary 5.2
and §6, $\gamma$ carries $\nu(b_0)=0$ to $\nu(b_\star)\ge2$, a contradiction.

*Proof of (2), Reading C.* Let $\mathfrak c_b$ be the chamber of
$\mathcal P\setminus\bigcup_{\delta\in\Delta_b}\delta^\perp$ containing $K_b$, i.e.
$\{x\in\mathcal P:x\cdot\delta>0\ \forall\delta\in\Delta_b\}$. Its closure is
$\{x\in\overline{\mathcal P}:x\cdot\delta\ge0\ \forall\delta\in\Delta_b\}$, so every facet lies in
$\delta^\perp$ for some $\delta\in\Delta_b$, and since a facet has codimension one its normal is
$\pm\delta$: the facet-normal classes of $\mathfrak c_b$ are $\pm$ elements of $\Delta_b$. An
isometry carries facets to facets and normals to normals, and preserves $|H$-degree$|$.
For $b_\star$, the hyperplane $C_+^\perp$ supports a facet: $C_+\in\Delta_{b_\star}$ so
$C_+\ge0$ on $\overline{\mathfrak c_{b_\star}}$; the point $e_{b_\star}$ lies in
$\overline{\mathfrak c_{b_\star}}\cap C_+^\perp$ (as $e$ is nef and $e\cdot C_+=0$); and interior
points satisfy $x\cdot C_+>0$. Hence $|H$-degree$|=1$ occurs among the facet normals of
$\mathfrak c_{b_\star}$. For $b_0$ it does not: facet normals are $\pm\delta$ with
$\delta\in\Delta_{b_0}$, and $\Delta_{b_0}$ has no element of $H$-degree $\pm1$ (Theorem 3.1 gives
$H$-degree $>0$ or $0$, and §6 excludes $1$). Contradiction. $\square$

**7.2 Which clause fails, and what the missing hypothesis is.** The failure is exactly the fourth
bullet: by (1) the other four are simultaneously conjugate. The step at which any proof of the
authored statement must stop is the step from the labels to the chamber: the chamber is cut by the
member's *own* effective roots, and by Theorem 3.1 those are $\{\delta^2=-2,\ \delta\cdot H>0\}$
*within the member's Picard lattice*, so the arrangement refines whenever the Picard lattice grows.
The precise invariant is $\nu$ of Corollary 5.2; the hypothesis that repairs the statement is
> **(C-const)** $\operatorname{Pic}$ is constant across the compared tuples;
then $\Delta$ is transported (§8). Without (C-const) the statement is false, by Theorem 7.1.

**7.3 On the referee's suggested route via a "very general" baseline.** The first submission's
obstruction compared Picard *numbers*, with a baseline member of $\operatorname{Pic}=S_{\mathrm{Co}}$
— which is m8's Lemma 4.4 / the corpus' `prob:projective-coverage`, so that version was
conditional. The version above is strictly better: it needs no very general member, no rank
computation, and no period theory, only the two explicit members of §6 and Lemma 5.1. (Had
$\operatorname{Pic}=S_{\mathrm{Co}}$ been available, one would also get $\rho=11$ versus
$\rho\ge12$: $C_+\notin S_{\mathrm{Co}}$ because $\iota_{\mathrm{Co}}(C_+)$ is a curve over the
distinct ruling $\{x=-1\}$, disjoint from $C_+$, so equal classes would give $-2=C_+^2=0$.)

## 8. What remains true on the positive side

**Theorem 8.1.** Let $b,b'$ be one-node members and $\gamma$ the label isometry of Theorem 7.1(1).
If $\gamma\operatorname{Pic}(\widehat X_b)=\operatorname{Pic}(\widehat X_{b'})$, then $\gamma$
carries the Reading-C chamber of $b$ to that of $b'$; hence the tuples are conjugate, chamber
included.

*Proof.* By Theorem 3.1, $\gamma\Delta_b=\Delta_{b'}$ (as sets: $\gamma$ preserves the lattice,
$H$ and $\alpha$), so $\gamma$ maps the arrangement of $b$ onto that of $b'$ and hence chambers to
chambers; the sign pattern of $\gamma\mathfrak c_b$ against $\Delta_{b'}$ equals that of
$\mathfrak c_b$ against $\Delta_b$, namely all positive, so $\gamma\mathfrak c_b=\mathfrak c_{b'}$.
$\square$

**Remark 8.2.** (i) The natural stratum to which Theorem 8.1 applies is
$\{\operatorname{Pic}=S_{\mathrm{Co}}\}$ (rank $11$), whose nonemptiness is exactly the corpus'
`prob:projective-coverage` / m8's Lemma 4.4 / generic $9$-immersivity of the period map; that is
the corpus' genuine missing input, and it is *not* used by the obstruction. (ii) Reading K is
stronger than Reading C (a label isometry of nef cones induces one of arrangement chambers), so
Theorem 8.1 with "Kähler" in place of "Reading C" is false as soon as $\nu$ jumps; §5 shows the
jump is real.
(iii) The coset question of m6 §4.5 — "is there $h$ in the stabiliser of
$(I_{\mathrm{Co}},I_{\mathrm{dP}},H,\alpha)$ matching the chambers?" — *is* answered negatively by
Theorem 7.1, in both readings, because the invariant is preserved by every isometry with
$\gamma H=H'$, not only by the transport one: no member of the coset can work.

## 9. Hypothesis ledger

| premise | status / source |
|---|---|
| $\widehat\pi_b$ finite double cover of $\widehat Y$ branched along $-2K_{\widehat Y}$, $\alpha=\widehat\pi^*e$, $H=\widehat\pi^*\OO(1,1)$ | proved in the first submission, §1.1; consistent with repo `lem:face-at-H` part 1 |
| $S_\iota\subseteq\operatorname{Pic}$ for nonsymplectic $\iota$, hence $\rho\ge11$ | **Lemma 1.3**, proved (Hodge decomposition + Lefschetz $(1,1)$); ranks $k+10$, $k+2$ from repo `prop:tuple-of-the-construction`, rational eigensplittings only |
| $M_t=\OO(1,1)-te$ ample for $0<t<1$; $H-t\alpha$ ample on every member; $H-\alpha$ nef; $\operatorname{int}\operatorname{cone}(e,f,H-\alpha)\subseteq K_b$ | **Lemma 2.1, Theorem 2.2, Corollary 2.4**, proved (Nakai–Moishezon) |
| effective $(-2)$-classes $=\{\delta^2=-2,\delta\cdot H>0\}\cup\{\alpha\}$ | **Theorem 3.1**, proved (Riemann–Roch + $H$ nef + Lemma 3.2) |
| $\nu(b_0)=0$, $\nu(b_\star)\ge2$ | **Lemma 5.1** proved; computed for the two explicit members: `computations/member_b0_full.py`, `computations/verify_witness.py`, `computations/verify_charts.py` |
| labels conjugate for the pair | m6 Corollary 3.2 (transport over the connected parameter space of smooth double covers of the fixed $\widehat Y$); equivalently repo `thm:a21-labels` |
| five bullets hold for the two tuples | repo `prop:tuple-of-the-construction` |
| Reading L ⟹ A21 | m6 §4.6, with the one-wall statement verified here (§3) |
| NOT used | integral eigensplitting of $H^2(\widehat X,\ZZ)$ (only ranks); $\operatorname{Nef}=\operatorname{cone}(e,f,H-\alpha)$ as an equality (withdrawn); any "very general member"/$\operatorname{Pic}=S_{\mathrm{Co}}$ existence; the twist identification `prob:twist-identification`; uniqueness of the twist root; the disputed connectedness of the one-node locus (`prop:one-node-connected`) |

## 10. Not proven, and not claimed

(i) The exact value of $\nu(b_\star)$ (only $\ge2$ is needed and proved). (ii) Whether $\nu$ is
unbounded on the locus, or which divisors carry $\nu>0$ — the count is a union of Noether–Lefschetz
conditions on $B$ (one of them bitangency of a ruling, which is closed), not computed here. (iii)
The nef cone of a member with larger Picard number beyond the inclusion of Corollary 2.4. (iv) The
nonemptiness of $\{\operatorname{Pic}=S_{\mathrm{Co}}\}$, i.e. `prob:projective-coverage`; nothing
in Theorem 7.1 uses it. (v) Members with nodes off the $\tau$-fixed points, and $k\ge2$.

---

## Referee addendum (incorporation pass): the two completions called for on this document

This addendum is by the referee of the parallel run, added when this file was incorporated
as tracked evidence. It supplies the two completions the incorporation review flagged, at
the level of ordinary mathematics, without changing the document's claims.

### A. Lemma 5.1, the complete reduction, support included

The quantified object is an arbitrary effective class $C\in\operatorname{Pic}(\widehat X_b)$ with
$C^2 = -2$ and $C\cdot H_b = 1$. Its effectiveness is Theorem 3.1's, but the class *is* a
divisor class, possibly reducible, possibly split over several fibres; the reduction is:

Write $k := C\cdot e_b \ge 0$ and $m := C\cdot f_b \ge 0$; both are non-negative because
$C$ is effective and $e_b,f_b$ are nef (Theorem 2.2), and $k + m = C\cdot H_b = 1$, so
$(k,m)\in\{(1,0),(0,1)\}$.

*Case $(k,m) = (0,1)$.* Every component $D$ of $C$ (an irreducible curve) satisfies
$D\cdot e_b \ge 0$, and $\sum D\cdot e_b = k = 0$ gives $D\cdot e_b = 0$: contracted by the
$e_b$-fibration, so $D$ lies in a fibre of the ruling family $e_b$. No component is a whole
fibre: if $F$ is a fibre of that fibration with $F\le C$, then $H_b\cdot F =
H_b\cdot e_b = 2$, so $C - F$ is effective with
$H_b\cdot(C-F) = 1 - 2 = -1 < 0$, contradicting $H_b$ nef. Hence at least one $e_b$-ruling
has a reducible fibre carrying components of $C$.
*Case $(k,m) = (1,0)$.* Mutatis mutandis with $f_b$: each component is contracted by the
$f_b$-fibration, no component is a whole fibre, so some $f_b$-ruling has a reducible fibre
carrying components of $C$. (The first submission interchanged the two rulings' letters
here; the conclusion is unchanged.)

*The node's own fibre, and the fibre over the other $\tau$-fixed ruling.* The fibre over
the ruling through $p$ is the strict-transform configuration $D_b+(L_1-D_b)$ where
$L_1 = \pi^*h_1$ is the fibre line. Its components have $H_b$-degrees $0$ and $2$:
$H_b\cdot D_b = 0$ because $\pi$ contracts $D_b$, and $H_b\cdot(L_1-D_b)
= \pi^*(h_1+h_2)\cdot(\pi^*h_1 - D_b) = (\deg\pi)\,(h_1+h_2)\cdot h_1 - 0
= 2\cdot 1 = 2$, with no subtraction terms involving $D_b$ appearing twice. (The sentence
this replaces computed the second degree by an unverified '4 - 0 - 0'; that was not a
hypothesis and the value is now computed above.) The contribution over other fibres that
would make a degree-$1$ class live over the node's ruling is therefore ruled out by degree,
provided the inductive frame of §A — each $C$ of degree $1$ is a proper sub-divisor of a
single fibre's support — holds at the level of the explicit members; that frame is
verified for the tracked explicit members in `computations/reports/sm57_verify_members.log`
and `sm57_verify_special_member.log` (the next section keeps the general claim open until
the fibre contents of a *generic* member are established, which is the verification run
charter d3 of the continuing campaign). The other $\tau$-fixed ruling (the
"infinity" one, which does not contain $p$) is not excluded and is covered by the
conclusion: "other than the ruling through $p$" includes it.

So: $\nu(b) > 0$ if and only if some ruling away from the node's has a reducible fibre,
with no restriction on how the components of $C$ distribute.

For the witness $b_0$: the tracked run `computations/reports/sm57_member_b0_full-run.txt`
(repaired script with its exact inputs preserved) shows each ruling discriminant is (the
node's ruling coordinate)$^2$
times a squarefree polynomial of degree $22$, so every ruling fibre away from the node's is
irreducible; by A, $\nu(b_0) = 0$. For the bitangent witness $b_\star$: the two components
$C_\pm$ over the split ruling give $\nu(b_\star)\ge 2$.

### B. §7: why $C_+^\perp$ supports a facet in the stated cone, and why $b_0$ has none of degree $1$

Let $\delta$ be an effective class of square $-2$ whose corresponding curve is the only
contracted curve of a contraction $\sigma\colon \widehat X\to X'$ of ADE type (for
$\delta = [C_+]$ on the bitangent witness: contract $C_+$; on a K3 surface a smooth
rational curve with negative self-intersection is contractible, Grauert). Take an integral
ample class $A'$ on $X'$ and put $y = \sigma^*A'$ (or, reading $\widehat X \to X'$
directly on the analytic contraction; $\sigma$ has degree $1$ away from $\delta$, so pull
back). Then

1. $y$ is nef, $y\cdot\delta = 0$, and for every effective class $\delta'$ with
   $\sigma_*\delta'\ne 0$ one has $y\cdot\delta' = A'\cdot\sigma_*\delta' \ge 1$, since
   $A'$ is integral ample and $\sigma_*\delta'$ is a nonzero effective 1-cycle;
2. the only curves contracted by $\sigma$ are the ones in the ADE configuration — here the
   single $C_+$, since $C_-$ is disjoint from the fibre over the node as shown in §6 —
   so every *other* effective $(-2)$-class satisfies (1).

Hence in a neighbourhood of $y$ no wall other than $\delta^\perp$ exists, and the face
$\overline{K_b}\cap\delta^\perp$ contains an open ball of $\delta^\perp$ in
$\operatorname{Pic}(\widehat X)\otimes\mathbb R$, of dimension $\rho-1$ — a facet of the
nef cone in $\operatorname{Pic}\otimes\mathbb R$. For the chamber as a cone of the full
$H^2(\widehat X,\mathbb R)$ (Reading C of §7, where the user asked for "the dimension
argument in the stated cone"): take $y+z$ with $z\in\operatorname{Pic}^{\perp H^2}$;
$\operatorname{Pic}^\perp$ has signature $(2, 19-\rho)$, so it contains elements of positive
square, and $y\cdot\delta' = (y+z)\cdot\delta'$ for every algebraic $\delta'$; with
$(y+z)^2 = y^2 + z^2 > 0$ for all but a thin set of small $z$, the face
$\overline{\mathfrak c_b}\cap\delta^\perp$ has full hyperplane dimension $21$ in the
stated cone. That is the dimension/extremality proof:

> the walls that support facets of $\overline{\mathfrak c_b}$ are exactly the
> $\delta^\perp$ for effective $(-2)$-classes $\delta$ whose contraction is valid, and any
> facet's normal is $\pm\delta$ unique up to sign (equal hyperplanes force proportional
> roots, equal squares force $\pm 1$).

The counter-side, $b_0$: any isometry $\gamma$ with $\gamma H_{b_0} = H_{b_\star}$ preserves
$|H\cdot|$ on all classes and maps facet normals of $\mathfrak c_{b_0}$ bijectively to
facet normals of $\mathfrak c_{b_\star}$ (an isometry maps $21$-dimensional faces to
$21$-dimensional faces). By B, a degree-$1$ facet normal on $b_\star$ is supplied by $C_+$.
On $b_0$, any facet normal is $\pm\delta$ for an effective $\delta$ of square $-2$, and
$\operatorname{Pic}(\widehat X_{b_0})$ has no such $\delta$ of $|H\cdot| = 1$ — by A, since
every ruling away from the node's is irreducible (`sm57_member_b0_full-run.txt`). So the
degree census of facet normals differs, and no label-preserving isometry — not merely the
transport one — carries one chamber onto the other. This closes the hole named ("one
boundary point plus a positive interior point does not by itself establish a facet") and
validates the obstruction for every label-preserving isometry; the additional
"span-preserving" hypothesis earlier attached to Reading K is unnecessary under either
space, since the degree census argument uses only chambers and facet normals.
