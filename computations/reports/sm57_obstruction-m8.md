# A21: the chamber clause fails — an explicit obstruction (revised)

**Status.** This document proves that the *original full statement* A21 (all five bullets
plus the chamber) is **false**, by exhibiting two one-node members of the direct projective
construction whose labelled tuples are not conjugate by any isometry of $L_{K3}$ preserving
the labels, the degree-$4$ class, the effective root *and* the chamber.

Revision note (second submission). Two premises of the first version are now discharged
rather than assumed:

* **the chamber semantics** are pinned to the authored text, §1.2 (quotation of the
  authored bullet at commit `a145cea4a5` and of the corpus's own reading of it at
  `cb48774f88`), and the chamber is shown to be *canonically determined* by $(H,\alpha)$
  through the explicit ample class $H-t\alpha$ of Lemma 1.4 — so nothing has to be assumed
  about competing readings, and the clause is not vacuous because the *arrangement* it is a
  chamber of is still member-dependent;
* **Lemma 4.4** (existence of a one-node member with $\Pic=S_\Co$) is now *proved*, not
  hypothesised: Theorem 3.3 shows the period map of the one-node family has maximal rank
  $9$ at every member, by global Torelli plus invariance of domain; the corpus's open
  "projective coverage" problem is *not* used (§4.4).

Nothing else uses a disputed input. In particular no integral eigensplitting, no type of
$S_\Co$, no gluing index and no twist identification is used.

---

## 1. The statement, and the semantics of the fourth bullet

### 1.1 The datum

The authored text (`writing/coble/heegner-report/coble-heegner-research-report.md`, commit
`a145cea4a5`, lines 601–638) attaches to a member $b$ of the direct projective construction
the tuple
$$\mathfrak L_b=\bigl(L_{K3},\;I_{\Co,b},\;I_{\mathrm{dP},b},\;H_b,\;\alpha_b,\;\mathfrak c_b\bigr),
\qquad L_{K3}=H^2(X_b,\Z),$$
where $X_b\to X^\sharp_b=\{z^2=f_b\}\subset \mathrm{Tot}(\OO_Y(2,2))\to Y=\PP^1\times\PP^1$
is the minimal resolution of the unique $A_1$ point (over the $\tau$-fixed point $p$),
$\iota_{\mathrm{dP}}(x,y,z)=(x,y,-z)$, $\iota_\Co(x,y,z)=(-x,-y,-z)$,
$H_b=\pi^*\OO_Y(1,1)$ and $\alpha_b=[D_b]$ is the exceptional $(-2)$-class. A21 is:

> Any two tuples $\mathfrak L_b$ arising from the construction are conjugate by an element
> of $O(L_{K3})$ preserving the labels, the degree-$4$ class, the effective root, and the
> chosen chamber (line 637).

Notation: $S_{\Co,b}=L_{K3}^{I_{\Co,b}=1}$, $S_{\mathrm{dP},b}=L_{K3}^{I_{\mathrm{dP},b}=1}$,
with $\rk S_{\Co,b}=11$ and $\rk S_{\mathrm{dP},b}=3$ for a one-node member (Lefschetz count
with the rational eigensplitting only; `prop:tuple-of-the-construction`).

### 1.2 The fourth bullet, pinned to the authored text

The bullet is verbatim (commit `a145cea4a5`, line 626):

> $\mathfrak c$ is the chosen positive/nef chamber in which $\alpha$ is effective and $H$
> is nef and big;

and the corpus's own reading of it, in the same file (commit `cb48774f88`, lines 630 and
651), is:

> "$\mathfrak c$ is a chamber in $H$'s cone" (line 630),
> "the labels pin a chamber of **the arrangement cut by a member's own effective roots**,
> and the transported chamber coincides with the target's chamber exactly when **no extra
> effective root cuts it**" (line 651).

Three consequences, and they are what the proof uses.

**(A) The walls are the member's own effective roots.** The chamber is a connected
component of $C_{X_b}\setminus\bigcup_{\delta\in\Delta_b}\delta^\perp$, where
$C_{X_b}$ is a component of $\{x\in H^2(X_b,\R):x^2>0\}$ and
$\Delta_b=\{\delta\in\Pic(X_b):\delta^2=-2,\ \delta\text{ effective}\}$. (Referee's
correction, not the author's words: BHPV VIII.3 does *not* identify that component with the
Kaehler cone. $K_{X_b}\subset\Pic(X_b)\otimes\R$ is the interior of the nef cone, a cone
in a $\rho$-dimensional space; the component above is a chamber of the chamber arrangement
of the positive cone of the full $H^2(X_b,\R)$, of signature $(3,19)$, and the two are
different cones in different spaces unless $\rho = 22$. The Kaehler cone is contained in a
unique such chamber, and by (C) below that chamber is also characterised as the one
containing $\omega_b$; Reading A2 below is the chamber in $H^2(X_b,\R)$, and its
intersection with $\Pic(X_b)\otimes\R$ is exactly $K_{X_b}$, the $x\cdot\delta>0$
description restricted to algebraic $x$.) The arrangement is member-dependent — that is the
whole content of the clause, and line 651 says so explicitly. **Reading A2** below is this
literal reading; **Reading A1** is the same chamber regarded inside
$\Pic(X_b)\otimes\R$. Both are proved below.

**(B) Not the "label-own" reading.** A reading in which the walls are only those roots lying
in a lattice spanned by the labels (e.g. $N=\langle L_1,L_2,D\rangle$ of rank $3$) is *not*
the authored text: line 651 says "a member's own effective roots", not "the labels' roots",
and under such a reading the bullet's clause "in which $\alpha$ is effective" is vacuous,
the sign of $\alpha$ being constant on a chamber of that coarser arrangement by
construction. §9.2 records this, and §3–5 show the clause fails under the authored reading.

**(C) The chamber is canonically pinned by $(H,\alpha)$ — no ambiguity and no
local-finiteness hypothesis.** The first version of this document pinned $\mathfrak c_b$
among the chambers adjacent to the wall $\alpha^\perp$ at $H$, which needs local finiteness
of the $(-2)$-arrangement near $H$ (true and standard, BHPV VIII.3, but an extra citation).
That is unnecessary: the labels supply an explicit *interior* point of the chamber.

> **Lemma 1.4 (explicit ample class; from m2, direction d3, re-proved here).**
> Let $\widehat Y=\Bl_pY$ with exceptional curve $e$ and rulings $h_1,h_2$. For
> $0<t<1$ the class $A_t=h_1+h_2-t\,e$ is ample on $\widehat Y$, and
> $\pi^*A_t=H_b-t\,\alpha_b$ is ample on $X_b$ for **every** one-node member $b$.
>
> *Proof.* $\pi\colon X_b\to\widehat Y$ is finite, and the pullback of an ample class along a
> finite morphism is ample. On the surface $\widehat Y$, every irreducible curve is $e$ or
> the strict transform $C'$ of an irreducible curve $C$ of bidegree $(a,b)$ with multiplicity
> $m=m_p(C)$ at $p$. Now $A_t\cdot e=t>0$; $A_t\cdot C'=(a+b)-tm\ge0$, with equality only if
> $a+b=m$, impossible when $m\ge1$ because $a+b\ge2m$; and for curves not through $p$ the
> value is $a+b>0$. Finally $A_t^2=2-t^2>0$. Nakai–Moishezon gives ampleness. $\square$

So put $\omega_b:=H_b-\tfrac12\alpha_b=\pi^*A_{1/2}$, ample on every member, and define
$$\mathfrak c_b:=\text{ the chamber of }C_{X_b}\setminus\bigcup_{\delta\in\Delta_b}\delta^\perp
\text{ containing }\omega_b .$$
There is no choice in this: $\omega_b\cdot\delta>0$ for every nonzero effective $\delta$, so
$\omega_b$ lies on no wall and is interior to exactly one chamber. It agrees with the
authored bullet: $H_b$ is nef and big and lies in $\overline{\mathfrak c_b}$, and
$\omega_b\cdot\alpha_b=2>0$ with the sign of $\alpha$ constant on $\mathfrak c_b$, so
$\alpha$ is effective there. And it transports: for any $\gamma$ with $\gamma H_b=H_{b'}$
and $\gamma\alpha_b=\alpha_{b'}$ one has $\gamma\omega_b=\omega_{b'}$, so
$\gamma\mathfrak c_b$ is *a* chamber containing $\omega_{b'}$. **The clause
$\gamma\mathfrak c_b=\mathfrak c_{b'}$ is nevertheless not automatic**: $\gamma\mathfrak c_b$
is a chamber of the arrangement cut by $\gamma(\Pic(X_b))$-walls, while $\mathfrak c_{b'}$ is
a chamber of the arrangement cut by $\Delta_{b'}$; they coincide exactly when no extra
effective root of $b'$ cuts $\gamma\mathfrak c_b$ — verbatim line 651. That is the condition
§3–5 decide.

---

## 2. Three elementary facts

**Fact 2.1 (the invariant lattice is algebraic).** Let $\iota$ be a *non-symplectic*
involution of a K3 surface $X$. Then $H^2(X,\Z)^{\iota=+1}\subseteq\Pic(X)$.

*Proof.* $\iota^*\omega=-\omega$, so $H^{2,0}\oplus H^{0,2}\subset(H^2\otimes\C)^{-1}$;
hence $(H^2)^+\otimes\C\subseteq H^{1,1}(X)$, and intersecting with $H^2(X,\Z)$ gives
$H^2(X,\Z)^+\subseteq H^{1,1}\cap H^2(X,\Z)=\Pic(X)$ — inclusion, not equality; the
strict-containment case is exactly the special member of §4 below. $\square$

Hence $\Pic(X_b)\supseteq S_{\Co,b}$ for every member, and $S_{\Co,b}$ is primitive in
$L_{K3}$ (it is the kernel of $\iota^*-1$).

**Fact 2.2 (the only root orthogonal to $H$; coincides with the corpus's `lem:face-at-H`).**
For every one-node member and every
$\delta\in\Pic(X_b)$ with $\delta^2=-2$, $\delta\cdot H_b=0$, one has $\delta=\pm\alpha_b$.

*Proof.* On a K3, $\chi(\OO(\delta))=\delta^2/2+2=1$ and $h^2(\delta)=h^0(-\delta)$ by Serre
duality, so $h^0(\delta)+h^0(-\delta)=1+h^1(\delta)\ge1$: one of $\pm\delta$ is effective.
Let $\delta=\sum a_i[C_i]$ be effective, $a_i>0$. Then
$0=\delta\cdot H_b=\sum a_i(C_i\cdot H_b)$ with $C_i\cdot H_b=\OO_Y(1,1)\cdot\pi_*[C_i]\ge0$
by the projection formula and ampleness of $\OO_Y(1,1)$; so every $C_i\cdot H_b=0$ and
$\pi(C_i)$ is a point. Curves contracted by $\pi$ are exactly the exceptional curves of
$\widehat X_b\to X^\sharp_b$ (the double cover $X_b^\sharp\to Y$ is finite), i.e. $D_b$.
Hence $\delta=m\alpha_b$ and $-2=-2m^2$ gives $m=1$. $\square$

**Fact 2.3 (Euler characteristics of the fixed loci).** For a nonsymplectic involution $\iota$
of a K3 with fixed locus $F$ one has $\chi(F)=2+\operatorname{tr}(\iota^*|H^2)
=2+(2\rk S_\iota-22)$, using only ranks of rational eigenspaces. For a one-node member this
gives $\rk S_{\mathrm{dP}}=3$ (fixed locus the normalization of $B$, genus $8$) and
$\rk S_\Co=11$ (fixed locus $D_b\cong\PP^1$, $\chi=2$). Source:
`prop:tuple-of-the-construction`, `prop:del-pezzo-type-on-the-resolution`.

---

## 3. Chamber criteria, and the rank of the period map

**Theorem 3.1 (Reading A1: the chamber determines the Picard lattice).** Let $b,b'$ be
one-node members and $\gamma\in O(L_{K3})$ with $\gamma I_{\Co,b}\gamma^{-1}=I_{\Co,b'}$,
$\gamma H_b=H_{b'}$, $\gamma\alpha_b=\alpha_{b'}$. Then
$$\gamma\mathfrak c_b=\mathfrak c_{b'}\quad\Longleftrightarrow\quad
\gamma\bigl(\Pic(X_b)\otimes\R\bigr)=\Pic(X_{b'})\otimes\R .$$

*Proof.* ($\Rightarrow$) $\mathfrak c_b=K_{X_b}$ is open in $\Pic(X_b)\otimes\R$, so
$\operatorname{span}_\R\mathfrak c_b=\Pic(X_b)\otimes\R$, and an isometry carries spans to
spans. ($\Leftarrow$) Then $\gamma$ carries the wall arrangement
$\{\delta^\perp:\delta\in\Pic(X_b),\delta^2=-2\}$ onto that of $b'$, so
$\gamma\mathfrak c_b$ is a chamber of the $b'$-arrangement; it contains
$\gamma\omega_b=\omega_{b'}$, and so does $\mathfrak c_{b'}$; a chamber containing a given
interior point is unique. $\square$

**Theorem 3.2 (Reading A2: the wall set).** For a one-node member $b$ put
$$W(\mathfrak c_b)=\{\delta\in L_{K3}:\delta^2=-2,\ \delta^\perp\text{ supports a facet of }
\overline{\mathfrak c_b}\}\qquad(\mathfrak c_b\subset C_{X_b}\subset H^2(X_b,\R)).$$
Then

1. $W(\mathfrak c_b)$ is determined by the cone $\mathfrak c_b$, hence
   $W(\gamma\mathfrak c_b)=\gamma W(\mathfrak c_b)$ for every isometry $\gamma$;
2. $W(\mathfrak c_b)\subseteq\Pic(X_b)$; indeed $W(\mathfrak c_b)\subseteq\{\pm\delta:
   \delta\in\Delta_b\}$.

*Proof.* (1) is the definition. (2) $\overline{\mathfrak c_b}$ is cut out in
$\overline C_{X_b}$ by the inequalities $x\cdot\delta\ge0$, $\delta\in\Delta_b$, so each
facet — a $21$-dimensional piece of a hyperplane — lies in some $\delta_0^\perp$ with
$\delta_0\in\Delta_b$; if $\delta^\perp=\delta_0^\perp$ then, the intersection form being
non-degenerate, $\delta=\lambda\delta_0$, and $\delta^2=\delta_0^2=-2$ gives $\lambda=\pm1$.
$\square$

*Remark.* In Theorem 3.1 the "unique chamber through a point" step is elementary, Lemma 1.4
supplying an interior point; no local finiteness of the root arrangement is used anywhere.
Local finiteness of the $(-2)$-arrangement in the positive cone (BHPV VIII.3) gives the same
conclusion for the variant pinning the chamber by adjacency to $H$, and is cited here only
as a check on the un-pinned variant.

### 3.3 The period map of the one-node family has maximal rank

This is the statement whose absence left the first version conditional. It is proved here by
Torelli and invariance of domain rather than by an infinitesimal computation; the statement
established is exactly "the differential of the period map has maximal rank".

Let $B\subseteq\PP^{11}$ be the one-node locus (non-empty, Zariski open in the hyperplane
$\{f(p)=0\}$ of the invariant system $\PP^{12}$; `prop:one-node-connected`), let
$\mathcal X\to B$ be the family of `prop:one-node-family`, and let
$\Gamma_B=\Aut^0(Y)^\tau$ be the $2$-dimensional torus of scalings of the two rulings,
acting on $B$.

**Theorem 3.3.** Let $b_0\in B$ have trivial stabiliser in the finite group
$\Aut(Y)^\tau/\Gamma_B$, let $U\ni b_0$ be a small ball over which the local system
$R^2\pi_*\Z$ is trivialised, and let $p\colon U\to D(T_\Co)$ be the resulting period map
into the period domain $D(T_\Co)\subset\PP(T_\Co\otimes\C)$ of the anti-invariant lattice
$T_\Co=S_{\Co,b}^{\perp}$ (signature $(2,9)$, hence $\dim D(T_\Co)=9$). Then

1. two members in one $\Gamma_B$-orbit are isomorphic (the automorphism of $Y$ identifies
   their double covers), so the period of $b$ depends only on the image of $b$ in
   $B/\Aut(Y)^\tau$; equivalently $dp$ vanishes on the $2$-dimensional tangent space of the
   $\Gamma_B$-orbit at $b_0$;
2. $\operatorname{rank}dp=9=\dim U-2$ at $b_0$; that is, $dp$ has maximal rank. In
   particular the image of $p$ contains an open subset of $D(T_\Co)$.

*Proof.* (a) *The period determines the member up to $\Aut(Y)^\tau$.* The trivialisation
identifies $H^2(X_b,\Z)$ with $L_{K3}$ for all $b\in U$, and $c_1(\mathcal H)$,
$c_1(\mathcal D)$ are flat, so $H_b$ and $\alpha_b$ correspond to fixed classes
$H,\alpha\in L_{K3}$; by Lemma 1.4 the class $L:=2H-\alpha\in S_\Co$ is ample on every
member, so it corresponds to a fixed *ample* class. If $p(b_1)=p(b_2)$ for
$b_1,b_2\in U$, the identity of $L_{K3}$ is a Hodge isometry of the two marked surfaces
carrying the ample class $L$ to the ample class $L$; by the Torelli theorem for K3 surfaces
(Piatetski-Shapiro–Shafarevich) there is an isomorphism $X_{b_1}\cong X_{b_2}$ inducing it,
hence an isomorphism of $H$-polarised surfaces, since $H$ corresponds to the same class.
Now recover the construction from $(X,H)$: $h^0(H)=h^0(\OO_Y(1,1))+h^0(\OO_Y(1,1)\otimes
K_Y)=4+0=4$ (using $\pi_*\OO_X=\OO_Y\oplus K_Y$), so $\varphi_H\colon X\to\PP^3$ is defined
by all sections, and these are exactly the pullbacks of $H^0(\OO_Y(1,1))$; hence
$\varphi_H$ factors through the Segre embedding $Y\hookrightarrow\PP^3$, its image is the
quadric $Q\cong\PP^1\times\PP^1$, and $X\to Q$ is the branched double cover with branch
divisor $B$. So $(X,H)$ determines $(Y,B)$, i.e. $b_1$ and $b_2$ differ by an element of
$\Aut(Y)^\tau$.
(b) *Conclusion.* So the period determines the member up to $\Aut(Y)^\tau$, i.e. the period
map factors through the $9$-dimensional moduli $M=B/\Aut(Y)^\tau$ of members (for $U$ small
and $b_0$ of trivial stabiliser, the quotient is a complex manifold) and the induced map
$$\bar p\colon M\longrightarrow D(T_\Co)/\Gamma\qquad(\Gamma=\text{the isometry group of }T_\Co,\ \text{the marking ambiguity})$$
is *injective*: two members with proportional periods are isomorphic as $H$-polarised
surfaces by (a), hence equal in $M$. Both sides have dimension $9$. An injective holomorphic
map between equidimensional complex spaces is open — invariance of domain, applied after
passing to a finite local cover of the orbifold $D(T_\Co)/\Gamma$ — hence it is immersive,
and a holomorphic map with positive-dimensional fibres would not be injective. Therefore
$\operatorname{rank}dp=9=\dim U-2$, the kernel being exactly the tangent space of the
$\Aut(Y)^\tau$-orbit. $\square$

*Remark 3.4.* This is the rank statement a Kodaira–Spencer computation would give, obtained
globally. What is used: *injectivity* of member $\mapsto(X,H)$ (the elementary half of the
corpus's projective-coverage problem); the *surjectivity* half ("every Coble pair arises from
a projective $(4,4)$ curve") is **not** used and remains open. The dimension count is
$\dim D(T_\Co)=\rk T_\Co-2=9$ from Fact 2.3, against $\dim B-2=11-2=9$.

---

## 4. The witness pair

### 4.1 The special member $b'$

$Y=\PP^1\times\PP^1$ with coordinates $([x_0:x_1],[y_0:y_1])$ and
$\tau([x_0:x_1],[y_0:y_1])=([-x_0:x_1],[-y_0:y_1])$; the $\tau$-invariant forms of bidegree
$(4,4)$ are the monomials with $a+b$ even. Put
$$F'=x_0^4y_0^4+x_1^4y_0^4+x_0x_1^3y_0^3y_1+x_0^2x_1^2y_0^2y_1^2+x_0^3x_1y_0y_1^3
+x_0x_1^3y_0y_1^3+x_0^4y_1^4+x_0^2x_1^2y_1^4,\qquad B'=\{F'=0\}.$$

Verified in `verify_special_member.log` (Sage 10.8, exact rational Gröbner bases):

1. $F'$ is $\tau$-invariant of bidegree $(4,4)$;
2. the singular locus of $B'$ is exactly $\{p\}$: in the chart $x_1=y_1=1$ the ideal
   $(F',\partial_xF',\partial_yF')$ has Gröbner basis $(x,y)$, and in the other three charts
   it is $(1)$;
3. at $p$ the linear part vanishes and the quadratic part is $x^2+xy$, discriminant $1$: an
   ordinary node;
4. $B'$ misses the other three $\tau$-fixed points;
5. **the key degeneracy:** the restriction of $F'$ to the $\tau$-fixed ruling
   $\ell=\{x_0=0\}\ni p$ is $x_1^4y_0^4$, i.e. the branch divisor on $\ell\cong\PP^1$ is
   $4[y_0=0]$, a **square**.

So $b'$ is a one-node member. Over $\ell$ the cover is $z^2=x_1^4y_0^4$, i.e.
$z=\pm x_1^2y_0^2$: it **splits**, giving two smooth rational curves $C_1,C_2\to\ell$
(isomorphisms onto $\ell$) meeting over $y_0=0$, that is, at the $A_1$ point. In the
resolution chart $(x,z)=(XY,ZY)$ one computes (`verify_special_member.log`, items [7]–[8])
$$D_{b'}=\{Y=0\},\qquad C_1=\{X=0,\;Z=Y\},\qquad C_2=\{X=0,\;Z=-Y\},$$
the strict transform smooth, the three curves pairwise transverse at single points, and the
total transform of the ruling divisor equal to $C_1+C_2+D_{b'}$. By adjunction on the K3
($K=0$) each component is a smooth rational curve of square $-2$; consistently
$(C_1+C_2+D)^2=-6+2\cdot3=0=\pi^*(\OO(1,0))^2$ and $(C_1+C_2+D)\cdot D=1+1-2=0$.

**Lemma 4.2.** $[C_1]\notin S_{\Co,b'}$; indeed $\iota_\Co^*[C_1]=[C_2]\ne[C_1]$.

*Proof.* $\iota_\Co$ preserves $\ell$ and acts on the fibre as $(y,z)\mapsto(-y,-z)$, so it
exchanges the branches $z=\pm y^2$. Distinct irreducible curves on a smooth surface meet
non-negatively, so $[C_1]=[C_2]$ would give $[C_1]^2=[C_1]\cdot[C_2]=1$, against
$[C_1]^2=-2$. $\square$

Moreover $[C_1]\cdot H_{b'}=1$, while every class of $S_{\Co,b'}$ has even $H$-degree: on
$S_\Co$ one has $H=u+v$ with $u=\pi^*h_1$, $v=\pi^*h_2$, $u\cdot v=2$, and $\alpha\cdot H=0$,
so $\delta\cdot H\in2\Z$ for $\delta\in S_\Co$. This parity is the second invariant used
below.

### 4.3 The general member $b$

**Lemma 4.4 (existence of a member with $\Pic=S_\Co$).** For a very general one-node member,
$\Pic(X_b)=S_{\Co,b}$.

*Proof.* By Fact 2.1, $\Pic(X_b)\supseteq S_{\Co,b}$ for every $b$. Fix
$\delta\in L_{K3}\setminus S_\Co$ and write $\delta=\delta_S+\delta_T$ with
$\delta_T\ne0$ in $T_\Co\otimes\Q$. The Noether–Lefschetz locus
$Z_\delta=\{b\in B:\delta\text{ is algebraic on }X_b\}$ is the zero locus of the holomorphic
function $b\mapsto(\omega_b,\delta_T)$ (after trivialising the local system over a chart; the
zero locus does not depend on the trivialisation). By Theorem 3.3 the image of the period map
is open in $D(T_\Co)$, and $\omega\mapsto(\omega,\delta_T)$ is not identically zero on
$D(T_\Co)$, since $\delta_T\ne0$ gives a non-zero linear form and $D(T_\Co)$ is a
non-degenerate quadric hypersurface, not contained in any hyperplane section. Hence
$Z_\delta$ is a proper closed analytic subset of $B$, of empty interior. There are countably
many $\delta$, and $B$ — a non-empty Zariski open of a projective space — is a Baire space;
so $\bigcup_{\delta}Z_\delta\ne B$, and any $b$ outside the union has no algebraic class
outside $S_{\Co,b}$, that is, $\Pic(X_b)=S_{\Co,b}$. $\square$

---

## 5. The obstruction

**Theorem 5.1.** Let $b$ be a one-node member with $\Pic(X_b)=S_{\Co,b}$ (Lemma 4.4) and let
$b'$ be the member of §4.1. Then, with the chamber as in §1.2 (either reading A1 or A2),
there is **no** $\gamma\in O(L_{K3})$ with
$$\gamma I_{\Co,b}\gamma^{-1}=I_{\Co,b'},\quad
\gamma I_{\mathrm{dP},b}\gamma^{-1}=I_{\mathrm{dP},b'},\quad
\gamma H_b=H_{b'},\quad \gamma\alpha_b=\alpha_{b'},\quad
\gamma\mathfrak c_b=\mathfrak c_{b'}.$$
Hence A21 is false.

*Proof for Reading A1.* Suppose $\gamma$ exists. Since $S_{\Co,b}=\ker(I_{\Co,b}-1)$ and
$S_{\Co,b'}=\ker(I_{\Co,b'}-1)$,
$$\gamma(S_{\Co,b})=S_{\Co,b'}. \tag{5.1}$$
By Theorem 3.1, $\gamma\mathfrak c_b=\mathfrak c_{b'}$ forces
$\gamma(\Pic(X_b)\otimes\R)=\Pic(X_{b'})\otimes\R$; both lattices are primitive and
$\Pic(X_b)=S_{\Co,b}$, so
$$\Pic(X_{b'})=\bigl(\Pic(X_{b'})\otimes\R\bigr)\cap L_{K3}
=\gamma(\Pic(X_b)\otimes\R)\cap L_{K3}=\gamma(S_{\Co,b})=S_{\Co,b'},$$
using primitivity of $\Pic$ and of $S_{\Co,b'}$. But $[C_1]\in\Pic(X_{b'})$ and
$[C_1]\notin S_{\Co,b'}$ (Lemma 4.2). Contradiction.

*Proof for Reading A2.* Suppose $\gamma$ exists. By Theorem 3.2(1) and
$\gamma\mathfrak c_b=\mathfrak c_{b'}$,
$$\gamma\bigl(W(\mathfrak c_b)\bigr)=W(\mathfrak c_{b'}). \tag{5.2}$$
By Theorem 3.2(2), $W(\mathfrak c_b)\subseteq\Pic(X_b)=S_{\Co,b}$, so by (5.1)
$\gamma(W(\mathfrak c_b))\subseteq S_{\Co,b'}$, hence $W(\mathfrak c_{b'})\subseteq
S_{\Co,b'}$. But $[C_1]\in W(\mathfrak c_{b'})$: $[C_1]$ is an effective class of square
$-2$ and it is extremal in $\overline{NE}(X_{b'})$, because
$-2=[C_1]^2=\sum_i a_i\,[C_1]\cdot[C_i]$ with $a_i>0$, $[C_i]\ne[C_1]$, is impossible —
every term on the right is $\ge0$. An extremal ray of $\overline{NE}$ supports a facet of its
dual, the nef cone $=\overline{\mathfrak c_{b'}}$. And $[C_1]\notin S_{\Co,b'}$ by Lemma
4.2. Contradiction. $\square$

*Variant of the A2 proof, using the parity invariant.* For the member $b$ of Lemma 4.4, all
classes of $W(\mathfrak c_b)\subseteq S_{\Co,b}$ have even $H$-degree, while
$[C_1]\in W(\mathfrak c_{b'})$ has $[C_1]\cdot H=1$. Since an isometry fixing $H$ preserves
$H$-degrees, (5.2) is contradicted. This variant needs only
$\Pic(X_b)\subseteq\{\delta:\delta\cdot H\in2\Z\}$ instead of equality.

**Corollary 5.2 (no repair by labels).** The failure occurs already for the smaller label set
$\{I_\Co,H,\alpha\}$; the $I_{\mathrm{dP}}$ clause is not used. The labels clause of A21
(`thm:a21-labels`) remains true: transport gives an isometry preserving
$S_\Co,S_{\mathrm{dP}},H,\alpha$, so the two tuples are conjugate *as labelled tuples without
the chamber* and not conjugate *with* it.

**Corollary 5.3 (the failure is not an isolated accident).** For **any** pair of one-node
members with $\Pic(X_b)=S_{\Co,b}$ and $\Pic(X_{b'})\ne S_{\Co,b'}$ the same conclusion
holds. The set $\{\Pic\ne S_\Co\}$ is the union of the NL loci $Z_\delta$,
$\delta\in L_{K3}\setminus S_\Co$, a countable union of proper closed analytic subsets that
is dense in $B$, and its complement is dense as well. So the set of pairs of tuples for
which A21's chamber clause fails is dense in $B\times B$.

**Corollary 5.4 (where a correct statement lives).** By Theorem 3.1 the correct chamber
statement — decidable, and true on every stratum — is: *for $b,b'$ with
$\Pic(X_b)=S_{\Co,b}$ and $\Pic(X_{b'})=S_{\Co,b'}$ any two tuples are conjugate by a
label-preserving $\gamma$, and then $\gamma\mathfrak c_b=\mathfrak c_{b'}$ automatically.*
A21 asserts this for all pairs; §4–5 show it fails exactly on the Noether–Lefschetz strata.

---

## 6. What this says about the corpus's two open "required theorems"

1. `prob:effective-cone-agreement` ("no effective class of square $-2$ of the second member
   outside the transported set cuts the transported chamber") is **false**, with the explicit
   witness of §4: the class $[C_1]$, of odd $H$-degree, is an effective root of $b'$ outside
   $S_{\Co,b'}$ and it cuts, its wall being a facet of the Kähler cone because it is
   extremal. Hence `prop:chamber-conditional` does not apply, and the sentence of
   `rmk:a21-resolution` that the remaining content is "precisely that agreement" is
   sharpened: the agreement fails.
2. `prob:twist-identification` is untouched: no integral eigensplitting, no type of
   $S_\Co$, no gluing index appears anywhere above.

---

## 7. Provenance of every premise

| Premise | Where it comes from |
|---|---|
| A21 verbatim; the fourth bullet; the tuple | `coble-heegner-research-report.md`, commit `a145cea4a5`, lines 601–638 (bullet at 626, problem at 637) |
| The chamber's reading: "a chamber in $H$'s cone", "the arrangement cut by a member's own effective roots", "no extra effective root cuts it" | same file, commit `cb48774f88`, lines 630 and 651 |
| The tuple exists; $\rk S_{\mathrm{dP}}=k+2=3$, $\rk S_\Co=k+10=11$ (rational eigensplitting, ranks only) | `the-heegner-line-and-the-coble-arithmetic-group.md`, `prop:tuple-of-the-construction`; $\mathrm{Fix}$ descriptions from `prop:local-operators`, `prop:del-pezzo-type-on-the-resolution` |
| $B$ non-empty, open, path-connected; the family smooth and proper with flat $c_1(\mathcal H)$, $[\mathcal D]$ | ibid. `prop:one-node-connected`, `prop:one-node-family` (audited in §8) |
| Labels are conjugate for every pair | ibid. `thm:a21-labels`, `thm:one-node-transport` |
| $\omega_t=H-t\alpha=\pi^*A_t$ ample for $0<t<1$ on every member | m2, direction d3, finding f9 (`uniform-ample-class-and-chamber.md`); re-proved here as Lemma 1.4 |
| Kähler cone $=$ chamber of the positive cone cut by the effective $(-2)$-classes | BHPV, *Complex Algebraic Surfaces*, VIII.3 |
| Every $\delta\in\Pic$ of square $-2$ has $\pm\delta$ effective | proved here, Fact 2.2 (Riemann–Roch + Serre duality) |
| Nonsymplectic involution $\Rightarrow$ $(+1)$-eigenspace $\subseteq\Pic$ | proved here, Fact 2.1 |
| Torelli for K3 surfaces (a Hodge isometry carrying an ample class to an ample class is induced by an isomorphism) | Piatetski-Shapiro–Shafarevich; standard |
| Invariance of domain | Brouwer; standard |
| $h^0(H)=4$, and $(X,H)$ determines $(Y,B)$ | proved here, Theorem 3.3(a) |
| The period map has maximal rank $9$ | proved here, Theorem 3.3 |
| Existence of a member with $\Pic=S_\Co$ | proved here, Lemma 4.4 (from Theorem 3.3 + Baire) |
| The explicit member $B'$: node, smoothness elsewhere, splitting, the three curves | **computation here**: `verify_special_member.py`, log `verify_special_member.log` |

---

## 8. Audit of the disputed geometric inputs used here

**8.1 Connectedness of the one-node locus: sound.** For $f_0,f_1\in B$, the pencil through
them: members singular at a base point $q\ne p$ form at most one point per base point (a
linear condition) and the base locus is finite; degeneracy of the quadratic part at $p$ is a
single determinant condition; a singularity away from the base locus is a closed condition on
the pencil, proper by Bertini. So $\PP^1\cap B$ is $\PP^1$ minus finitely many points, hence
path-connected. (m2's independent audit supplies the needed uniformity of the inverse function
theorem at $p$ and the irreducibility of a one-nodal invariant $(4,4)$ curve.)

**8.2 The relative family and the resolution: sound.** $\mathcal X^\sharp=\{z^2=F_b\}\to B$
is flat, its singular locus is the section over $p$ of transverse $A_1$ type, and blowing it
up is smooth with a $\PP^1$-bundle exceptional divisor; the chart computation is in the log,
item [7], and works with the coefficients as parameters. `thm:one-node-transport` needs
nothing else.

---

## 9. Other readings of the fourth bullet

### 9.1 The "all $(-2)$-classes of $L_{K3}$" reading

If $\mathfrak c_b$ were a chamber of the *fixed* arrangement of all $(-2)$-classes of
$L_{K3}$ (the arithmetic chamber decomposition of the period domain), it would no longer be
cut by the member's own roots, Theorems 3.1 and 3.2 would give nothing, and the clause would
become: *the label-preserving group is transitive on the relevant chambers of that fixed
arrangement.* This document does not decide that statement. Under that reading the clause
"$\alpha$ is effective in $\mathfrak c$" is also no longer a condition on $\mathfrak c$,
since effectivity is a property of the surface — so it is not the authored reading.

### 9.2 The "label-own" reading

If the walls were restricted to the roots of a lattice spanned by the labels (say
$N=\langle L_1,L_2,D\rangle$), the chamber would be a function of the labels alone, hence
transported automatically, and the chamber clause a tautology. That is not the authored
reading: line 651 says the chamber is one "of the arrangement cut by a member's own effective
roots", and the authored clause "$\alpha$ is effective in $\mathfrak c$" has content only
when the arrangement contains walls other than $\alpha^\perp$. §3–5 show the clause fails
under the authored reading.

---

## 10. Summary

The chamber of a tuple is determined by $(H,\alpha)$ through the explicit ample class
$H-\tfrac12\alpha$ (Lemma 1.4), and it is cut by the member's own effective roots — the
authored semantics, quoted in §1.2. Under that semantics the chamber records the member's
Picard data: its span is $\Pic\otimes\R$ (Theorem 3.1), and the effective roots supporting
facets of its closure lie in $\Pic$ and are carried to the other member's set by any isometry
(Theorem 3.2). The period map of the one-node family has maximal rank $9$ (Theorem 3.3), so
some one-node member has $\Pic=S_\Co$ of rank $11$ (Lemma 4.4). The explicit member $B'$ of
§4.1 has an extra effective root $[C_1]$ of odd $H$-degree, exchanged with $[C_2]$ by
$\iota_\Co$, hence outside $S_\Co$ and extremal. No label-preserving isometry can match the
two members' Picard data, so none preserves the chamber: **A21 is false**, and it fails
densely (Corollary 5.3). What is true is its restriction to pairs with equal Picard lattice
(Corollary 5.4), together with the labels clause.
