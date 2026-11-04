# The positive half of A21 (label rigidity) — audited afresh and re-proved

Author: m8, direction d4 of swarm `smw0b9kmo`.
Repo read (read-only) at evidence state `main@83403bc8`, at
`/workspace/nucleus/work/projects/p-9fcb4ed7f4b64e008de2ee29a7197bf4/repo`; citable paths below are
relative to that root. Nothing in the repo was modified. This document does **not** touch the chamber
clause of A21 (defects 1–3 of the task, directions d1/d2/d3); it isolates and proves the *rigidity
spine* on which the reported outcome shape rests, and records the two places where the tracked
argument does not carry and what replaces it.

Everything below is a statement about the **direct projective construction** of
`writing/coble/heegner-report/coble-heegner-research-report.md` (A21 answer, items 1–3, and
`writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md`,
`prop:local-operators`, `prop:del-pezzo-type-on-the-resolution`, `prop:tuple-of-the-construction`,
`prop:one-node-family`). Notation is the corpus's.

---

## §0. What is proved here, in one place

Fix $Y=\PP^1\times\PP^1$ with $\tau([x_0:x_1],[y_0:y_1])=([-x_0:x_1],[-y_0:y_1])$, let
$p\in Y$ be a $\tau$-fixed point, and for $b$ in the one-node locus $B^{(p)}$ (Def. 3.1) let
$\widehat X_b$ be the minimal resolution of $X^\sharp_b=\{z^2=f_b\}$, with
$H_b=\pi^*\OO_Y(1,1)$, $\alpha_b=[D_b]$ the exceptional $(-2)$-class, and
$I_{\Co,b},I_{\dP,b}$ the lifts of $\iota_\Co,\iota_{\dP}$.

* **Theorem A (labels conjugate; §4).** For any two one-node members $b_0,b_1$ (nodes at possibly
  different $\tau$-fixed points) there is $\gamma\in\Orth(L_{K3})$ with
  $\gamma I_{\Co,b_0}\gamma^{-1}=I_{\Co,b_1}$, $\gamma I_{\dP,b_0}\gamma^{-1}=I_{\dP,b_1}$,
  $\gamma H_{b_0}=H_{b_1}$, $\gamma\alpha_{b_0}=\alpha_{b_1}$. — Proved from: non-emptiness (§3.2,
  independently re-verified here), Zariski-openness and hence connectedness of $B^{(p)}$ (§3.3),
  the smooth proper equivariant family with flat $H,\alpha,I$ (§3.4), Gauss–Manin transport.
* **Theorem B (Picard $\ge 11$; §5).** $\rk\Pic(\widehat X_b)\ge 11$ for **every** one-node member,
  because $S_{\Co,b}=H^2(\widehat X_b,\Z)^{I_\Co=1}\subseteq\Pic(\widehat X_b)$ and
  $\rk S_{\Co,b}=11$. — Proved from: non-symplecticity of $I_\Co$ + Lefschetz. No type of $S_\Co$,
  no integral eigensplitting, no saturation is used.
* **Theorem C (period map rank 9; §6).** The period map of the one-node family
  $p\colon B^{(p)}\to D(T_\Co)/\Gamma$ (Def. 6.1) has fibres equal to the $\Aut(Y)^\tau$-orbits,
  which are $2$-dimensional; hence $\rank dp=11-2=9=\dim D(T_\Co)$ at every member with finite
  orbit stabiliser. — Proved from: the explicitly ample flat class $2H-\alpha$ (Lemma 2.2, proved
  here, previously asserted), strong Torelli, the Segre recovery of $(Y,B)$, a dimension count.
* **Theorem D (very general member; §7).** For $b$ outside a meagre subset of $B^{(p)}$,
  $\Pic(\widehat X_b)=S_{\Co,b}$. — Proved from Theorem C by Baire plus a lattice-projection lemma.

**Two corrections to the tracked argument, with what replaces them.**

1. *$2H-\alpha$ ampleness was asserted, not proved.* The A21 answer, item 3, says "$2H-\alpha$ is
   ample and flat on the family", and the same class carries the whole strong-Torelli step. It is
   true, and Lemma 2.2 below proves it, with the stronger statement that $H_b-t\alpha_b$ is ample for
   every $0<t<1$ on **every** one-node member (no genericity). The proof is Nakai–Moishezon on the
   blow-up model $\widehat X_b\cong$ double cover of $\Bl_pY$.
2. *The rank step "injective holomorphic $\Rightarrow$ open $\Rightarrow$ immersive" is not a valid
   inference scheme as used.* $\bar p\colon M\to D(T_\Co)/\Gamma$ is **not** injective: two members
   related by the ruling-swap $\sigma\in\Aut(Y)^\tau$ (which fixes $p$ but lies outside
   $\Gamma_B=\Aut^0(Y)^\tau$) are isomorphic with the same period and are different points of $M$.
   What is true, and enough, is that the fibres are *exactly* the $\Aut(Y)^\tau$-orbits, hence
   $2$-dimensional, hence the rank is $11-2=9$ by the fibre-dimension theorem. §6 proves it in that
   form. The corpus's Thm 3.3 conclusion survives; its stated route does not.

**What is not claimed here.** No statement about the chamber clause; no integral eigensplitting
$H^2=\bigoplus$ eigenspaces; no isometry type of $S_\Co$ or $S_\dP$ for a member; no saturation of
$U(2)\perp\Z D$ in $S_\dP$; no identification of the construction's involution pair with the
reflection twist (`prob:twist-identification`); no surjectivity of the period map ("projective
coverage"); no claim that the one-node locus is *all* of the hyperplane $\{f(p)=0\}$ minus a divisor
(only that it is a non-empty Zariski-open subset of it).

---

## §1. The construction and the labelled tuple (definitions, exactly)

Let $\cL=\OO_Y(2,2)$, so $\cL^2=\OO_Y(4,4)=-2K_Y$. For $f\in H^0(\cL^2)^\tau$ put

$$X^\sharp_f=\Spec_{\OO_Y}\bigl(\OO_Y\oplus\cL^{-1}\bigr),\qquad z^2=f,$$

the double cover $\pi_f\colon X^\sharp_f\to Y$ branched along $B_f=\{f=0\}$; it satisfies
$\omega_{X^\sharp_f}\cong\OO$ because $K_Y+\cL=0$, and $\pi_{f*}\OO_{X^\sharp_f}=\OO_Y\oplus K_Y$
(so that the double cover is the canonical one; also $R^1\pi_{f*}\OO=0$).

The two involutions are $\iota_\dP(x,y,z)=(x,y,-z)$ (deck transformation) and
$\iota_\Co(x,y,z)=(-x,-y,-z)$; both satisfy $\pi\circ\iota=\iota'\circ\pi$ with $\iota'=\id_Y,\tau$
respectively. They commute and $\iota_\Co\iota_\dP(x,y,z)=(-x,-y,z)$
(`prop:local-operators` parts 1–2; a substitution).

**Lemma 1.1** (the two characters; `prop:local-operators` part 2 re-derived). Let
$\omega=dx\wedge dy/(2z)$ be the holomorphic $2$-form on $X^\sharp_f$ away from $B_f$. Then
$\iota_\dP^*\omega=-\omega$, $\iota_\Co^*\omega=-\omega$ and
$(\iota_\Co\iota_\dP)^*\omega=+\omega$. In particular $I_\Co,I_\dP$ are non-symplectic and their
product is symplectic.

*Proof.* $\iota_\dP^*(dx\wedge dy)=dx\wedge dy$ and $\iota_\dP^*(2z)=-2z$; for $\iota_\Co$ both
factors change sign, so again $-1$; the product fixes $z$ and preserves $dx\wedge dy$. $\square$

**Definition 1.2** (the tuple of a member; `sec-labeled-lattice-data`). For a one-node member $b$
with node at $p$, the associated tuple is
$$\mathfrak L_b=(L_{K3},I_{\Co,b},I_{\dP,b},H_b,\alpha_b,\mathfrak c_b),\quad
L_{K3}=H^2(\widehat X_b,\Z),\ H_b=\pi^*\OO_Y(1,1),\ \alpha_b=[D_b],$$
where $\widehat X_b\to X^\sharp_b$ is the minimal resolution and $D_b$ its exceptional curve. The
chamber $\mathfrak c_b$ is the subject of the other directions and is not used below.

**Lemma 1.3** (basic numerical facts; `prop:tuple-of-the-construction` parts 1–3). For a one-node
member: $H_b^2=4$; $H_b\cdot\alpha_b=0$; $\alpha_b^2=-2$; $\alpha_b$ is the class of the effective
curve $D_b$ and is $I_\Co$-invariant; $H_b$ is fixed by both involutions, nef and big, not ample.

*Proof.* $(\pi^*\OO(1,1))^2=\deg\pi\cdot(\OO(1,1))^2=2\cdot2=4$. $\tau^*\OO(1,1)=\OO(1,1)$ since
$\tau$ acts by $[-1]$ on each factor, so $I_\Co^*H_b=H_b$; $I_\dP^*H_b=H_b$ is the deck statement.
$H_b\cdot D_b=\OO(1,1)\cdot\pi_*D_b=0$ because $D_b$ lies over the node. $D_b\cong\PP^1$ with
$D_b^2=-2$ by Lemma 2.1(3) below (or, equivalently, as the exceptional curve of a resolution of an
$A_1$ point). Nef: $H_b\cdot C=\OO(1,1)\cdot\pi_*C\ge0$; big: $H_b^2>0$ with $H_b$ nef on a surface;
not ample: $H_b\cdot D_b=0$. $\square$

---

## §2. The blow-up model and the two ample classes

This section contains the one genuinely new proof of the positive half.

### 2.1 The model

**Lemma 2.1** (resolution = double cover of the blown-up base). Let $f\in H^0(\OO_Y(4,4))^\tau$ have
an ordinary node at the $\tau$-fixed point $p$ and no other singularity, let $\widehat Y=\Bl_pY$ with
exceptional curve $e$, and let $\tilde B\subset\widehat Y$ be the proper transform of $B=\{f=0\}$.
Then:

1. $\tilde B\in|-2K_{\widehat Y}|$, is smooth, and meets $e$ transversally in the two points over the
   node;
2. the double cover $\hat\pi\colon \widehat X'=\Spec(\OO_{\widehat Y}\oplus\cL'^{-1})\to\widehat Y$
   with $\cL'\in\Pic\widehat Y$ a square root of $\OO(\tilde B)$ is a smooth surface with trivial
   canonical class, i.e. a K3 surface;
3. $\widehat X'\cong\widehat X$, the minimal resolution of $X^\sharp_f$; under this isomorphism
   the exceptional curve of the resolution is $D=\hat\pi^*e$, and $e\mapsto D$ is an isomorphism
   $e\cong D\cong\PP^1$ with $D^2=2\,e^2=-2$;
4. $H=\pi^*\OO(1,1)=\hat\pi^*A$ with $A=\beta^*\OO(1,1)$ ($\beta\colon\widehat Y\to Y$), and
   $\alpha=[D]=\hat\pi^*[e]$.

*Proof.* (1) $B\in|\OO(4,4)|$, $\beta^*B=\tilde B+2e$, so
$\tilde B\sim\beta^*\OO(4,4)-2e=\OO(-2,-2)+2e=-2(K_{\widehat Y})$ where
$K_{\widehat Y}=\beta^*K_Y+e=\OO(-2,-2)+e$. Smoothness of $\tilde B$ and transversality at $e$ are
the normalization of the node: the two branches of $B$ at $p$ have distinct tangents, and blowing up
separates them. (2) A double cover branched along a smooth divisor is smooth; and
$K_{\widehat X'}=\hat\pi^*(K_{\widehat Y}+\tfrac12\tilde B)=\hat\pi^*(K_{\widehat Y}-K_{\widehat Y})=0$.
$\widehat X'$ is a K3 surface: it is simply connected (double cover of the simply connected surface
$\widehat Y$ branched along the ample smooth divisor $\tilde B$), $q=0$ and $p_g=h^0(K)=1$, so
Noether gives $\chi(\OO)=2=(2+b_2)/12$, i.e. $b_2=22$.
(3) Over $\widehat Y\setminus e\cong Y\setminus\{p\}$ the cover restricts to the double cover of
$Y\setminus\{p\}$ branched along $B\setminus\{p\}$, i.e. to $X^\sharp_f\setminus\{\text{node}\}$;
over $e$ it is the double cover of $e\cong\PP^1$ branched at the two points $\tilde B\cap e$, hence a
$\PP^1$, and the total space is smooth there by (2). So $\widehat X'\to X^\sharp_f$ is birational and
is an isomorphism off $D$, contracts $D$ to the node, and is smooth; both $\widehat X'$ and the minimal
resolution are smooth minimal surfaces birational to $X^\sharp_f$, hence isomorphic (uniqueness of
minimal models in dimension 2). $D\to e$ is $2:1$, so $D^2=\deg(D/e)\,e^2=2\cdot(-1)=-2$. (4) is
immediate from $\pi=\beta\circ\hat\pi$. $\square$

*Local check supporting (2)–(3) on the explicit member.* In the chart $x=X,\ y=XY',\ z=XZ'$ of the
blow-up at $p$ the equation $z^2=f$ becomes $Z'^2=q(1,Y')+O(X)$, where $q=x^2+xy+2y^2$ is the
quadratic part; the exceptional curve is the conic $Z'^2=q(1,Y')$, which is smooth because
$\disc q=-7\ne0$. This is `§3.2`'s explicit member.

### 2.2 Two ample classes

**Lemma 2.2** (ample classes). With notation as in 2.1: for every $0<t<1$ and for $t=\tfrac12$
in particular, the $\Q$-class
$$A_t=A-t\,e\qquad\text{is ample on }\widehat Y,\qquad\text{so}\qquad
\hat\pi^*A_t=H_b-t\,\alpha_b\ \text{is ample on }\widehat X_b .$$
In particular $2H_b-\alpha_b=\hat\pi^*(2A-e)$ and $2A-e$ are integral and ample.

*Proof.* $\widehat Y$ is smooth projective. Let $C\subset\widehat Y$ be an irreducible curve. If
$C=e$ then $A_t\cdot e=-t\,e^2=t>0$. Otherwise $C=C'$ is the proper transform of an irreducible
curve $C_0\subset Y$ of bidegree $(a,b)\ne(0,0)$ with multiplicity $m=m_p(C_0)\ge0$ at $p$; then
$A\cdot C'=a+b$ and $e\cdot C'=m$, so
$$A_t\cdot C'=a+b-tm,\qquad m\le\min(a,b)\le\tfrac{a+b}{2},$$
so if $m\ge1$ then $A_t\cdot C'\ge\bigl(1-\tfrac t2\bigr)(a+b)\ge\tfrac{a+b}{2}>0$ (for $t<1$), and
if $m=0$ then $A_t\cdot C'=a+b\ge1$. Hence
$A_t\cdot C>0$ for every irreducible $C$. Further
$A_t^2=(A-te)^2=A^2-2t\,A\cdot e+t^2e^2=2-t^2>0$ (using $A^2=\OO(1,1)^2=2$, $A\cdot e=0$,
$e^2=-1$). Nakai–Moishezon gives ampleness of the $\Q$-divisor $A_t$ on the smooth projective surface
$\widehat Y$. Ampleness is preserved by pullback along a finite morphism, and $\hat\pi$ is finite, so
$\hat\pi^*A_t$ is ample on $\widehat X_b$. For $t=\tfrac12$ multiply by $2$: $2A-e$ and
$2H_b-\alpha_b$ are integral ample classes. $\square$

**Remark 2.3** (what this buys, and what it does not). (i) $H_b$ is nef and big but not ample
(Lemma 1.3), and Lemma 2.2 exhibits an explicit **interior** point $H_b-\tfrac12\alpha_b$ of
$\Amp(\widehat X_b)$ with $H_b$ in its closure; so $\alpha_b$ is the unique effective root with
$\alpha_b\cdot H_b=0$, i.e. $H_b$ lies on exactly one wall of the $(-2)$-arrangement, the wall
$\alpha_b^\perp$. (The last implication: if $\delta$ is effective with $\delta\cdot H_b=0$ then
$0<(\underbrace{H_b-t\alpha_b}_{\text{ample}})\cdot\delta=-t\,\alpha_b\cdot\delta$, so
$\alpha_b\cdot\delta<0$, which for effective $\delta$ forces $D_b$ to be a component of $\delta$; then
$0=\delta\cdot H_b$ forces every component of $\delta$ to be contracted by $\pi$, i.e. $\delta$ a
multiple of $\alpha_b$, and $\delta^2=-2$ gives $\delta=\alpha_b$.) This is
`lem:face-at-H`/Fact 2.2 of the corpus; it is quoted here only because the argument now rests on a
proved ample class. (ii) It does **not** settle the chamber clause: $H_b-\tfrac12\alpha_b$ being an
interior point of $\Amp(\widehat X_b)$ says nothing about the chamber of the arrangement cut by a
*neighbouring* member's effective roots — that is the separate condition the corpus isolates at line
651 and the other directions decide.
(iii) The class is flat in the family: $H_b$ and $\alpha_b$ are restrictions of the relative classes
$c_1(\cH)$ and $[\cD]$ of `prop:one-node-family`, so $2H_b-\alpha_b$ is a flat section of
$R^2\hat\pi_*\Z$ over $B^{(p)}$ (see §3.4).

---

## §3. The parameter space and the family over it

### 3.1 Definitions

**Definition 3.1.** Let $V=H^0(\OO_Y(4,4))^\tau$ and $H_p=\{f\in V:f(p)=0\}$, and
$$B^{(p)}=\Bigl\{f\in H_p:\ \det\Hess_p f\ne0\ \text{and}\ \operatorname{Sing}B_f=\{p\}\Bigr\}.$$
This is the corpus's one-node locus with the node at $p$ (`prop:one-node-family`).

**Lemma 3.2** (bookkeeping; re-derived, agrees with `lem:dim`/`lem:tau` of the tracked audit).
$\dim V=13$, so $|V|=\PP^{12}$; $H_p$ is a hyperplane, $|H_p|=\PP^{11}$; for $f\in V$ the vanishing
order of $f$ at a $\tau$-fixed point is even (odd-degree terms are killed), so on $H_p$ the point $p$
is automatically singular, and "ordinary node at $p$" is exactly $\det\Hess_pf\ne0$.

*Proof.* The monomial basis $x_0^{4-i}x_1^iy_0^{4-j}y_1^j$ is acted on by $\tau^*$ through
$(-1)^{i+j}$, so $\dim V=\#\{(i,j):i+j\text{ even}\}=3\cdot3+2\cdot2=13$. Evaluation at
$p=([1:0],[1:0])$ is the coefficient of $x_0^4y_0^4$, a non-zero $\tau$-invariant functional, so
$H_p$ is a hyperplane. The parity statement is the substitution $(u,v)\mapsto(-u,-v)$ in local
coordinates, and $\det\Hess_p\ne0$ makes the lowest-order part at $p$ a non-degenerate quadratic
form, i.e. an $A_1$ point. $\square$

The dimension count used in §6 is $\dim B^{(p)}=11$ (Zariski-open in $\PP^{11}$).

### 3.2 Non-emptiness, re-verified here rather than inherited

**Proposition 3.3** ($B^{(p)}\ne\varnothing$). The explicit invariant form
$$f=29x^4y^4+23x^4y^2+19x^4+17x^3y^3+13x^3y+11x^2y^4+7x^2y^2+x^2+5xy^3+xy+3y^4+2y^2$$
(affine chart $x_0=y_0=1$; `sec-explicit-curve`) lies in $B^{(p)}$.

*Verification* (mine, not the repo's; script and log in `.ultramath/smw0b9kmo/m8/verify_one_node.py`,
`verify_one_node.log`). Homogenise $f$ to the bidegree-$(4,4)$ form
$F=\sum c_{ab}x_0^{4-a}x_1^ay_0^{4-b}y_1^b$ and compute, in the four standard charts, a Gröbner basis
of $(F,\partial_uF,\partial_vF)$ over $\Q$:

| chart | variables | Gröbner basis |
|---|---|---|
| $x_0=1,y_0=1$ | $x_1,y_1$ | $(x_1,\,y_1)$ |
| $x_0=1,y_1=1$ | $x_1,y_0$ | $(1)$ |
| $x_1=1,y_0=1$ | $x_0,y_1$ | $(1)$ |
| $x_1=1,y_1=1$ | $x_0,y_0$ | $(1)$ |

So $\operatorname{Sing}B_f=\{p\}$ exactly. The monomials present have total degrees $2,4,6,8$ (all
even), so $f\in V$; $f(p)=0$; the quadratic part at $p$ is $x^2+xy+2y^2$ with discriminant
$1-8=-7\ne0$. Hence $f\in B^{(p)}$. $\square$

This reproduces, independently and by a different implementation, the claim the repo records as its
verification contract at `sec-explicit-curve`.

### 3.3 Openness and connectedness

**Lemma 3.4.** $B^{(p)}$ is a non-empty Zariski-open subset of $H_p\cong\PP^{11}$, hence connected
and path-connected; $\dim B^{(p)}=11$.

*Proof.* $\{\det\Hess_p=0\}$ is a proper closed algebraic subset of $H_p$ (the Hessian entries are
linear functionals in $f$). Let
$W_0=\{(f,q)\in H_p\times(Y\setminus\{p\}):f(q)=0,\ d_qf=0\}$, Zariski closed in
$H_p\times(Y\setminus\{p\})$, and let $\bar\Sigma\subseteq H_p$ be the image of its closure in
$H_p\times Y$; $\bar\Sigma$ is closed because $H_p\times Y$ is proper over $H_p$. Then
$$B^{(p)}=H_p\setminus\bigl(\{\det\Hess_p=0\}\cup\bar\Sigma\bigr).$$
*Proof of the two inclusions.* (i) $B^{(p)}$ misses $\{\det\Hess_p=0\}$ by definition, and it misses
$\bar\Sigma$: if $f_0\in B^{(p)}$ and $f_k\in W_0$'s image (so $B_{f_k}$ is singular at some
$q_k\ne p$) with $f_k\to f_0$, then $\det\Hess_pf_k\ne0$ for $k$ large with inverses bounded, so by
the quantitative inverse-function theorem applied to $\nabla f_k$ (this is the tracked `lem:open` of
`sm57_audit-one-node-m2.md`: $|\nabla f_k(u,v)|\ge|A_k(u,v)|-C'|(u,v)|^2>0$ on a punctured ball of
radius $r$ around $p$, uniformly in $k$) the points $q_k$ stay at distance $\ge r>0$ from $p$; a
subsequence then converges to $q\ne p$ with $f_0(q)=d_qf_0=0$, contradicting
$\operatorname{Sing}B_{f_0}=\{p\}$. This is the one step of the lemma that is not formal; it is
exactly m2's escape-to-$p$ argument, and the only new content here is that $\bar\Sigma$ is closed and
that this makes $B^{(p)}$ the complement of a closed set. (ii) Conversely, if $\det\Hess_pf\ne0$ and
$f\notin\bar\Sigma$, then a singular point of $B_f$ other than $p$ would make $f$ a point of $W_0$'s
image, so $\operatorname{Sing}B_f=\{p\}$ and $f\in B^{(p)}$.
So $B^{(p)}$ is the complement of a closed algebraic subset, proper by Proposition 3.3: a non-empty
Zariski-open and dense subset of the irreducible variety $H_p$. A non-empty Zariski-open subset of an
irreducible complex variety is connected (its complement has empty interior and real codimension
$\ge2$), and a connected complex manifold is path-connected. $\square$

*Remark 3.5* (relation to the tracked proofs). The corpus proves connectivity of the one-node locus
by a generic-pencil/Bertini argument (`prop:one-node-connected`), and the tracked audit
`sm57_audit-one-node-m2.md` repairs two gaps in it (`lem:open`: openness in $H_p$ needs an
escape-to-$p$ argument, which the non-degeneracy of $\Hess_p$ supplies; `lem:irred`: pencils have no
fixed component). That argument is correct. It is also **unnecessary** for label conjugacy once the
locus is fixed at $p$: openness in $\PP^{11}$ plus non-emptiness already gives connectedness. The
distinction matters for exactly one point of the ledger: no part of the rigidity theorem needs the
pencil argument or Bertini, hence none of the disputed inputs m6 flagged as bypassing
`prop:one-node-connected`.

### 3.4 The family

**Lemma 3.6** (smooth proper equivariant family; `prop:one-node-family`, with the blow-up constructed
in a smooth ambient). Let $\cY=Y\times B^{(p)}$, $\cL=\OO_Y(2,2)$, and
$\cX^\sharp=\Spec_{\cY}(\OO_\cY\oplus\cL^{-1})$ with algebra structure $z^2=f_b$. Let
$\widehat{\cX}\to\cX^\sharp$ be the blow-up of the section $\sigma(B^{(p)})$ (taken inside the smooth
total space of the $\PP^1\times\PP^1$-bundle $\PP(\cL\oplus\OO)_\cY$, so the blow-up is defined). Then

1. $\widehat\cX\to B^{(p)}$ is smooth and proper with K3 fibres;
2. $\iota_\Co,\iota_\dP$ act fibrewise, commute, fix $\sigma$, hence lift to $\widehat\cX$;
3. $\cH=\pi^*\OO_Y(1,1)$ and the exceptional divisor $\cD$ of the blow-up are flat over $B^{(p)}$,
   with $\cH_b=H_b$, $\cD_b=D_b$, $\cD_b^2=-2$, $\cH_b\cdot\cD_b=0$;
4. hence $c_1(\cH)$ and $[\cD]$ are flat sections of $R^2\widehat\pi_*\Z$ for the Gauss–Manin
   connection.

*Proof.* (1) In local coordinates at $\sigma(b)$ the equation is $z^2=q_b(u,v)+O(3)$ with $q_b$
non-degenerate for all $b\in B^{(p)}$; in the chart $u\ne0$ with $v=uv_1$, $z=uz_1$ the proper
transform is $z_1^2=q_b(1,v_1)+O(u)$, a smooth equation (the gradient has a non-vanishing
$\partial_{z_1}$-entry), and likewise in the chart $v\ne0$; over the open set $u,v\ne0$ the family is
smooth because $\det\Hess_p\ne0$ is an open condition and the fibres have no other singularity by
definition of $B^{(p)}$. Properness: $\widehat\cX$ is a blow-up of a projective morphism's total
space, and $\cX^\sharp\to B^{(p)}$ is finite hence proper and projective. (2) Both involutions fix
the section $\sigma$ pointwise (they fix $p$ and $z\mapsto-z$ fixes $z=0$), and an automorphism
fixing the centre of a blow-up lifts. (3) $\cH$ is pulled back from $Y\times B^{(p)}$; $\cD$ is a
$\PP^1$-bundle over the section, hence flat with $\PP^1$ fibres; the fibre computations are Lemma
2.1(3)–(4). (4) Classes of a flat family of divisors are flat sections of $R^2\widehat\pi_*\Z$. $\square$

---

## §4. Theorem A: the three label clauses hold for every pair

**Theorem 4.1** (labels conjugate). Let $b_0,b_1$ be one-node members of the direct projective
construction, with nodes at $\tau$-fixed points $p_0,p_1$ (possibly distinct). Then there is
$\gamma\in\Orth(L_{K3})$ such that
$$\gamma\,I_{\Co,b_0}\,\gamma^{-1}=I_{\Co,b_1},\qquad
\gamma\,I_{\dP,b_0}\,\gamma^{-1}=I_{\dP,b_1},\qquad
\gamma H_{b_0}=H_{b_1},\qquad \gamma\alpha_{b_0}=\alpha_{b_1}.$$

*Proof.* **Step 1 (reduce to a common node).** Let $g\in\Aut(Y)$ with $g\tau g^{-1}=\tau$ and
$g(p_0)=p_1$: in the coordinates of §1 take $g=(\psi,\id)$ with $\psi([x_0:x_1])=([x_1:x_0])$,
i.e. $x\mapsto1/x$; then $\psi\tau_1\psi^{-1}=\tau_1$ in $\PG_2$ because an involution of $\PP^1$ is
determined by its two fixed points and $\psi$ permutes $\{0,\infty\}$, and $\psi(0)=\infty$. Since
$g$ preserves $\OO(1,1)$, $\tau$, and the systems $H_p$ (as $g^*f(p_1)=f(p_0)$), it maps $B^{(p_0)}$
isomorphically onto $B^{(p_1)}$ and the construction at $b_0$ to the construction at $g(b_0)$, hence
induces an isometry $\gamma_g\in\Orth(L_{K3})$ carrying the whole tuple of $b_0$ to that of $g(b_0)$.
It remains to treat $p_0=p_1=p$.

**Step 2 (transport inside one fibre-type).** Fix $p$, let $\pi\colon\widehat\cX\to B^{(p)}$ be the
family of Lemma 3.6, and let $b_0,b_1\in B^{(p)}$. By Lemma 3.4 the base is path-connected, so choose
a path $\delta\colon[0,1]\to B^{(p)}$ from $b_0$ to $b_1$. $\widehat\cX\to B^{(p)}$ is a smooth proper
family of K3 surfaces, so its restriction to $[0,1]$ is a smooth proper family of compact complex
surfaces; by Ehresmann's theorem it is a $C^\infty$ fibre bundle, and parallel transport in the local
system $R^2\pi_*\Z$ gives a $\Z$-linear isometry of lattices
$$T\colon H^2(\widehat X_{b_0},\Z)\xrightarrow{\ \sim\ }H^2(\widehat X_{b_1},\Z),\qquad
T(x\cdot y)=T(x)\cdot T(y),$$
the intersection form being flat. Since $c_1(\cH)$ and $[\cD]$ are flat sections (Lemma 3.6(4)),
$$T(H_{b_0})=H_{b_1},\qquad T(\alpha_{b_0})=\alpha_{b_1},$$
and since $\iota_\Co,\iota_\dP$ act on the total space $\widehat\cX$ fibrewise (Lemma 3.6(2)),
transport intertwines them: $T\circ I_{\Co,b_0}^*=I_{\Co,b_1}^*\circ T$ and likewise for $\dP$.
Choosing markings $\varphi_i\colon H^2(\widehat X_{b_i},\Z)\to L_{K3}$ and putting
$\gamma=\varphi_1\circ T\circ\varphi_0^{-1}\in\Orth(L_{K3})$ gives all four identities. $\square$

*Remark 4.1.1* (what transport does and does not give). $T$ is an isometry of lattices, not a Hodge
isometry: parallel transport for the Gauss–Manin connection does not preserve the Hodge
decomposition ($\nabla$ satisfies Griffiths transversality $\nabla F^p\subset F^{p-1}\otimes\Omega^1$
and nothing stronger), and the *period* of $b_1$ is not the transport of the period of $b_0$. The
label clause of A21 is a statement about $(L_{K3},I_\Co,I_\dP,H,\alpha)$ as a lattice-with-labels
only, so this is exactly what is needed; no Hodge-theoretic assertion enters Theorem 4.1. The
Hodge-theoretic input is confined to §6, where it enters through the period equality and strong
Torelli.

**Corollary 4.2.** The first three clauses of `prob:coble-rigidity` hold for every pair of one-node
members: the invariant lattices, $H$ and the effective root are conjugate. In particular
$\gamma S_{\Co,b_0}\gamma^{-1}=S_{\Co,b_1}$ and $\gamma S_{\dP,b_0}\gamma^{-1}=S_{\dP,b_1}$.

*Remark 4.3.* The theorem is silent about the chamber, and that silence is structural: transport
gives $\gamma\alpha_{b_0}=\alpha_{b_1}$ but says nothing about the effective cone of $b_1$ beyond
$\alpha_{b_1}$ (Remark 2.3(ii)). The chamber clause is not a fifth consequence of the same argument;
it is a genuinely separate condition, which is what the corpus at line 651 states and what the other
directions decide.

*Remark 4.4* (what the argument does *not* need). No base change for a simultaneous resolution is
needed: the family is not smoothed — every fibre has its node at $p$, the singular locus is the
section $\sigma$, and blowing up inside the smooth ambient of Lemma 3.6 resolves the family
simultaneously. This is exactly where a naive "the total space is singular, so use Brieskorn–Tjurina
with a double cover of the base" would overcomplicate; the double cover would be harmless but is
superfluous here, and avoiding it keeps the base path-connected with the same path.

---

## §5. Theorem B: Picard rank $\ge 11$ for every one-node member

**Fact 5.1** (the invariant lattice of a non-symplectic involution is algebraic). If $\iota$ is a
non-symplectic involution of a K3 surface $X$ and $\omega$ spans $H^{2,0}$, then
$H^2(X,\Z)^{\iota=1}\subseteq\Pic(X)$.

*Proof.* $\iota^*\omega=-\omega$; for $x\in H^2(X,\Z)$ with $\iota^*x=x$ one gets
$\langle x,\omega\rangle=\langle\iota^*x,\iota^*\omega\rangle=-\langle x,\omega\rangle$, so
$\langle x,\omega\rangle=0$, i.e. $x\in H^{1,1}(X)$; and
$\Pic(X)=H^{1,1}(X)\cap H^2(X,\Z)$. $\square$

**Lemma 5.2** (rank). For a one-node member, $\rk S_{\Co,b}=11$ and $\rk S_{\dP,b}=3$.

*Proof.* For a non-symplectic involution, Lefschetz gives
$\chi(\mathrm{Fix}\,\iota)=2+\operatorname{tr}(\iota^*|H^2)$, and with the eigenspace ranks
$\operatorname{tr}=2\rk S_\iota-22$ (rational eigenspaces only). For $I_\Co$ the fixed locus is the
exceptional curve $D_b\cong\PP^1$, so $\chi=2$ and $\rk S_\Co=\tfrac12(2+20)=11$. For $I_\dP$ the
fixed locus is the normalization of $B_f$, of geometric genus $8$, so $\chi=2-16=-14$ and
$\rk S_\dP=\tfrac12(-14+20)=3$. Sources: `prop:local-operators` part 4 and
`prop:del-pezzo-type-on-the-resolution` parts 1–3. Only ranks are used, no integral
eigensplitting. $\square$

**Theorem 5.3.** For every one-node member $\rk\Pic(\widehat X_b)\ge11$, with
$S_{\Co,b}\subseteq\Pic(\widehat X_b)$ of rank $11$.

*Proof.* $S_{\Co,b}=H^2(\widehat X_b,\Z)^{I_\Co=1}$ (the fixed lattice; over $\Q$ the eigenspaces are
the $\pm1$ eigenspaces and the fixed lattice of the integral involution is exactly the $+1$-part),
which is contained in $\Pic$ by Fact 5.1 and has rank $11$ by Lemma 5.2. $\square$

*Remark 5.4* (a false inference in the tracked text, and why it is harmless). The A21 answer, item 2,
adds "and $S_{\dP}\subseteq S_\Co$ because the pullbacks of the rulings are $I_\Co$-invariant". The
stated reason only shows $\pi^*\Pic(Y)=U(2)\subseteq S_\Co$ (indeed $\subseteq S_\Co\cap S_\dP$); it
does not give $S_\dP\subseteq S_\Co$. The latter would follow from
$S_\dP=U(2)\perp\Z D_b$ together with $D_b\in S_\Co$, but the corpus's own
`prop:del-pezzo-type-on-the-resolution` states exactly that this equality "is a saturation question,
not a rank count, and is not settled here". So $S_\dP\subseteq S_\Co$ is *not available*, and it is
*not needed*: Theorem 5.3 uses only $S_\Co\subseteq\Pic$. (A class of $S_\dP$ can a priori be
anti-invariant for $I_\Co$; nothing here decides it.)

---

## §6. Theorem C: the period map has rank $9$

### 6.1 The statement

**Definition 6.1** (the period map). Let $S_\Co=S_{\Co,b}$, $T_\Co=S_\Co^{\perp}\subset L_{K3}$ (a
primitive sublattice of rank $11$, signature $(2,9)$ by Lemma 5.2 and the signature $(3,19)$ of
$L_{K3}$), and
$$D(T_\Co)=\{[\omega]\in\PP(T_\Co\otimes\C):\ \omega\cdot\omega=0,\ \omega\cdot\bar\omega>0\},$$
which is a $9$-dimensional complex manifold (an open subset of the quadric $\omega^2=0$ in
$\PP^{10}$). Because $S_{\Co,b}\subseteq\Pic(\widehat X_b)$ (Theorem 5.3), $H^{2,0}(\widehat
X_b)\subset T_\Co\otimes\C$, so $b\mapsto[\omega_b]$ defines a map
$$p\colon B^{(p)}\longrightarrow D(T_\Co)/\Gamma,$$
$\Gamma$ the image in $\Orth(T_\Co)$ of the subgroup
$\Orth(L_{K3})^{(I_{\Co},I_{\dP},H,\alpha)}$ of isometries preserving the four labels.

*The Torelli citations, checked.* Two statements of BHPV are used, and only these:
(BHPV = Barth–Hulek–Peters–Van de Ven, *Compact Complex Surfaces*, 2nd ed.)
* **Prop. VIII.3.11** (effectivity criterion): a Hodge isometry
  $\Phi\colon H^2(S,\Z)\to H^2(S',\Z)$ is *effective* — maps the Kähler cone of $S$ into that of
  $S'$ — iff it maps *one* Kähler class of $S$ into the Kähler cone of $S'$. For projective surfaces
  the Kähler cone is the ample cone.
* **Thm. VIII.11.1** (strong Torelli): an effective Hodge isometry is induced by a *unique*
  isomorphism $S'\to S$. (The polarized form for an ample class $h$ is Cor. VIII.3.12; it is *not*
  applied here, because the degree-$4$ class $H_b$ is nef and big but not ample — this is exactly
  why an ample class has to be produced, and Lemma 2.2 produces $2H_b-\alpha_b$.)

**Theorem 6.2.** Let $b\in B^{(p)}$ and assume the stabiliser of $b$ in
$\Aut(Y)^\tau/\Aut^0(Y)^\tau$ is trivial (in particular $b$ is not fixed by the ruling swap $\sigma$
of Lemma 6.4). Then
$$\rank(dp)_b=9=\dim D(T_\Co)=\dim B^{(p)}-\dim\Aut^0(Y)^\tau .$$
In particular the image of $p$ contains a non-empty open subset of $D(T_\Co)/\Gamma$, and $p$ has
maximal rank.

The proof is 6.2–6.5.

### 6.2 Fibres are exactly the automorphism orbits

**Proposition 6.3.** If $b_0,b_1\in B^{(p)}$ have $p(b_0)=p(b_1)$, then $b_1=g(b_0)$ for some
$g\in\Aut(Y)^\tau$.

*Proof.* Equality of periods in $D(T_\Co)/\Gamma$ means: after trivialising the local system on a
chart containing $b_0,b_1$, there is $\gamma\in\Orth(L_{K3})$ preserving $I_\Co,I_\dP,H,\alpha$, with
$\gamma(\omega_{b_0})=\omega_{b_1}$. Since $\gamma$ acts on $T_\Co$ and preserves $S_\Co$ (as it
preserves $I_\Co$), and $S_\Co,S_\Co^\perp$ span $L_{K3}\otimes\Q$, $\gamma$ is a Hodge isometry of
$L_{K3}$ for the two Hodge structures. It is effective: $\gamma(2H-\alpha)=2H-\alpha$, and
$2H-\alpha$ is an ample (hence Kähler) class on both surfaces by Lemma 2.2, so BHPV Prop. VIII.3.11
applies. By the strong Torelli theorem (BHPV Thm. VIII.11.1; Piatetskii-Shapiro–Shafarevich) there is
a unique isomorphism $f\colon\widehat X_{b_0}\to\widehat X_{b_1}$ with $f^*=\gamma$ (in the
trivialisation). Then
$f^*H_{b_1}=H_{b_0}$, $f^*\alpha_{b_1}=\alpha_{b_0}$,
$f^*I_{\Co,b_1}=I_{\Co,b_0}$, $f^*I_{\dP,b_1}=I_{\dP,b_0}$.

Now recover the base. $h^0(H_b)=h^0(\OO_Y(1,1)\otimes\pi_*\OO_{\widehat X_b})=h^0(\OO(1,1))+
h^0(\OO(1,1)\otimes K_Y)=4+0=4$, and these sections are exactly the pullbacks of
$H^0(\OO(1,1))$, so $\varphi_{H_b}\colon\widehat X_b\to\PP^3$ factors as the Segre embedding
composed with $\pi_b$ and has image the quadric $Y\subset\PP^3$; and $\widehat X_b\to Y$ is the
branched double cover with branch divisor $B_{f_b}$. Since $f$ carries $|H_{b_1}|$ to $|H_{b_0}|$
linearly, it descends to $g\in\Aut(Y)$ with $g(\Segre(Y))=\Segre(Y)$, $g^*\OO(1,1)=\OO(1,1)$ and
$g(B_{f_{b_1}})=B_{f_{b_0}}$; and $f^*I_{\Co,b_1}=I_{\Co,b_0}$ gives $g\tau g^{-1}=\tau$. Hence
$g\in\Aut(Y)^\tau$ and $b_1=g(b_0)$ (the branch divisor determines the member). Conversely, if
$b_1=g(b_0)$ with $g\in\Aut(Y)^\tau$, then $g$ induces an isomorphism of the two constructions
carrying $I_\Co,I_\dP,H,\alpha$ each to itself, so the two marked periods agree modulo $\Gamma$; hence
$p(b_0)=p(b_1)$. So the fibres of $p$ are exactly the $\Aut(Y)^\tau$-orbits on $B^{(p)}$. $\square$

### 6.3 The orbits are $2$-dimensional

**Lemma 6.4** (the stabiliser of $p$). $\Aut(Y)=(\PG_2\times\PG_2)\rtimes\Z/2$ and
$\Aut(Y)^\tau=\{(g_1,g_2):g_i\tau_ig_i^{-1}=\tau_i\}\rtimes\Z/2$. For a fixed $\tau$-fixed point
$p$, the subgroup of $\Aut(Y)^\tau$ preserving $p$ is $N(T_1)\times N(T_2)$-elements fixing $p$, i.e.
$$G_p=\{g\in\Aut(Y)^\tau: g(p)=p\}=(T_1\times T_2)\rtimes\langle\sigma\rangle,$$
where $T_i\cong\C^\times$ is the diagonal torus and $\sigma$ is the ruling swap; its identity
component is $\Gamma_B=T_1\times T_2$, of dimension $2$, and its component group is $\Z/2$.

*Proof.* $\tau_i$ is the split involution of $\PP^1$ with fixed points $\{0,\infty\}$, so
$\{g_i:g_i\tau_ig_i^{-1}=\tau_i\}=N(T_i)=T_i\rtimes\Z/2$, where the non-trivial coset is the
anti-diagonal element interchanging $0$ and $\infty$; and $g_i$ fixes $0$ iff $g_i\in T_i$. Hence the
elements of $\Aut(Y)^\tau$ fixing $p=([1:0],[1:0])$ are exactly the pairs from $T_1\times T_2$,
together with those also composed with the ruling swap $\sigma$, which fixes $p$. $\square$

**Lemma 6.5.** For $b\in B^{(p)}$ with trivial stabiliser in $G_p/\Gamma_B$, the orbit
$\Aut(Y)^\tau\cdot b$ meets $B^{(p)}$ in a complex manifold of dimension exactly $2$.

*Proof.* By Lemma 6.4, $G_p\cdot b=(T_1\times T_2)\cdot b\cup\sigma((T_1\times T_2)\cdot b)$, and
each piece is the image of the orbit map of a $2$-dimensional torus. The orbit of $b$ under
$T_1\times T_2$ has dimension $2$ because the stabiliser in the torus is a closed algebraic subgroup,
positive-dimensional exactly when a 1-parameter subgroup fixes $f_b$; for $b$ with trivial stabiliser
in $G_p/\Gamma_B$ the stabiliser is finite, so the orbit has dimension $2$. (Points of $B^{(p)}$
outside the countable union of the loci "a given 1-parameter subgroup fixes $f$" — a proper closed
condition for each subgroup — have finite stabiliser; the union is meagre, so such $b$ are dense.)
$\square$

### 6.4 Rank

*Proof of Theorem 6.2.* By Proposition 6.3 the fibres of $p$ are the intersections
$\Aut(Y)^\tau\cdot b\cap B^{(p)}$, of dimension $2$ at $b$ by Lemma 6.5. For a holomorphic map of
complex manifolds, $\dim_b p^{-1}(p(b))\ge\dim B^{(p)}-\rank_b(dp)$; since every fibre has dimension
exactly $2$, $\rank_b(dp)\le 11-2=9$. If $\rank_b(dp)<9$ then
$\dim_b p^{-1}(p(b))>\dim B^{(p)}-\rank_b(dp)>2$, contradiction. Hence $\rank_b(dp)=9$. Both sides are
$9$-dimensional, so $p$ is a submersion at $b$ and its image is open. $\square$

*Remark 6.6* (why not "injective, hence immersve"). The map $\bar p\colon B^{(p)}/\Gamma_B\to
D(T_\Co)/\Gamma$ is *not* injective: if $\sigma(b)\ne b$ then $b$ and $\sigma(b)$ are different
points of $B^{(p)}/\Gamma_B$ with the same period (Proposition 6.3 applies with $g=\sigma$). The
tracked Thm 3.3(b) asserts injectivity of $\bar p$ and deduces immersivity from injectivity by
invariance of domain; neither the assertion nor the inference is correct as stated (an injective
holomorphic map between equidimensional manifolds is biholomorphic onto its image by Osgood's
theorem, but the map here is not injective). The fibre-dimension argument above replaces both steps
and yields the same conclusion: rank $9$ at every member with finite stabiliser.

*Remark 6.7* (what is used). Strong Torelli in the effective form: a Hodge isometry carrying an ample
class to an ample class is induced by an isomorphism. Applied to $2H-\alpha$, whose ampleness is
Lemma 2.2. This is the single place where the tracked text relies on an unproved ampleness assertion;
with Lemma 2.2 the step is closed.

---

## §7. Theorem D: the very general member has $\Pic=S_\Co$

**Lemma 7.1** (projection lemma). If $\Pic(\widehat X_b)\supsetneq S_{\Co,b}$, then there is
$0\ne\delta\in T_\Co$ with $\delta\in\Pic(\widehat X_b)$.

*Proof.* Let $x\in\Pic(\widehat X_b)\setminus S_\Co$ be integral. Since $S_\Co$ is primitive, the
composition $L_{K3}\otimes\Q\to T_\Co\otimes\Q$ is well defined; put $t=x_{\text{proj}}$; then
$x-t\in S_\Co\otimes\Q$ and $t\ne0$. Choose $n\ge1$ with $n\,t\in T_\Co$ and $n(x-t)\in S_\Co$; then
$\delta:=n\,t=nx-n(x-t)\in\Pic(\widehat X_b)\cap T_\Co$ is non-zero and integral. $\square$

**Theorem 7.2.** Let $B^{(p)}$ be as in Definition 3.1 and $p$ as in Definition 6.1. Then
$\bigcup_{\delta\in T_\Co\setminus\{0\}}Z_\delta$ is meagre in $B^{(p)}$, where
$Z_\delta=\{b:\delta\in\Pic(\widehat X_b)\}$, and for every $b$ outside it,
$\Pic(\widehat X_b)=S_{\Co,b}$.

*Proof.* For fixed $\delta\ne0$, $Z_\delta$ is the zero locus of the holomorphic function
$b\mapsto(\omega_b,\delta)$ on a chart in which the local system is trivialised; it is closed
analytic. It is proper: the period map has rank $9$ at the members of Theorem 6.2, so its image is
open in $D(T_\Co)/\Gamma$, and $[\omega]\mapsto(\omega,\delta)$ is not identically zero on $D(T_\Co)$
(a non-zero linear form does not vanish on the non-degenerate quadric $\{\omega^2=0\}$), so the image
meets the complement of $\{(\omega,\delta)=0\}$. Baire's theorem for the locally compact space
$B^{(p)}$ gives $\bigcup_\delta Z_\delta\ne B^{(p)}$. At $b\notin\bigcup_\delta Z_\delta$ there is no
non-zero $\delta\in T_\Co$ in $\Pic(\widehat X_b)$; by Lemma 7.1, $\Pic(\widehat X_b)=S_{\Co,b}$.
$\square$

*Remark 7.3.* This is the "very general member" statement in the outcome shape, now with the
properness of the Noether–Lefschetz loci derived from Theorem 6.2 rather than assumed. Note that
$S_\Co$ here is the member's own invariant lattice; the *abstract type*
$U(2)\oplus E_8(2)\oplus\langle-2\rangle$ is not asserted (see Remark 5.4 and §8).

---

## §8. Ledger: what this gives for A21, and the exact boundary

**What is established.** For the direct projective construction, with no genericity hypothesis on the
pair: all pairs of one-node members have conjugate labels $(I_\Co,I_\dP,H,\alpha)$ (Thm 4.1); every
one-node member has $\rk\Pic\ge11$ (Thm 5.3); the period map of the one-node family has maximal rank
$9$, with $2H-\alpha$ a flat ample class (Lemma 2.2, Thm 6.2); a very general one-node member has
$\Pic=S_\Co$ (Thm 7.2). Consequently, of the four clauses of `prob:coble-rigidity`, the label clause
(which subsumes the invariant lattices, the degree-$4$ class and the effective root) holds for every
pair, and its proof does not use any of: the type of $S_\Co$, an integral eigensplitting, a gluing
index, the twist identification, or the connectedness argument disputed by m6.

**The exact boundary.** (i) The chamber clause is untouched: a label-preserving isometry transports
$\alpha$, not the member's effective cone; whether the transported chamber equals the target's is the
condition of line 651, and it is the object of the other directions. (ii) $S_\dP=U(2)\perp
\langle-2\rangle^{\oplus k}$ (saturation) is not available and not used. (iii) The abstract type of
$S_\Co$ is not proved for a member. (iv) Surjectivity of the period map / "projective coverage" is not
used and remains open; only injectivity-in-the-weak-sense (Prop. 6.3) is used. (v) Nothing here
identifies the construction's involution pair with the reflection twist
(`prob:twist-identification`).

**Failures found in the tracked text, with the repair.**
1. Ampleness of $2H-\alpha$ asserted without proof (A21 answer item 3; `sm57_obstruction-m8.md`
   Thm 3.3(a)): now Lemma 2.2, with the stronger $H_b-t\alpha_b$ ample for $0<t<1$.
2. "$\bar p$ injective $\Rightarrow$ open $\Rightarrow$ immersive" (Thm 3.3(b)): the map is not
   injective (the ruling swap); replaced by the exact fibre computation (Prop. 6.3, Lemmas 6.4–6.5,
   fibre-dimension theorem).
3. "$S_\dP\subseteq S_\Co$" (A21 answer item 2, parenthetical): invalid as inferred; not needed
   (Remark 5.4).
4. Simpler connectivity: no pencil/Bertini input is needed (Lemma 3.4); the corpus's
   `prop:one-node-connected` and its repairs in `sm57_audit-one-node-m2.md` are correct but
   superfluous for the rigidity theorem.

---

## Appendix: verification files

* `.ultramath/smw0b9kmo/m8/verify_one_node.py`, `verify_one_node.log` — symmetric Gröbner
  verification of Proposition 3.3 (singular locus of the explicit invariant branch curve in four
  charts), of $\dim V=13$, of $\tau$-invariance, and of the non-degeneracy of the quadratic part.
* `.ultramath/smw0b9kmo/m8/verify_ample.txt` — the arithmetic of Lemma 2.2: $A^2=2$, $A\cdot e=0$,
  $e^2=-1$, $A_t^2=2-t^2>0$, $(2A-e)^2=7$, $(2H-\alpha)^2=14$, $(2H-\alpha)\cdot\alpha=2$.

**Sources checked for the external theorems.** (i) Strong Torelli in the effective form and the
effectivity criterion: BHPV Prop. VIII.3.11 and Thm VIII.11.1, as cited in
G. K. Sankaran, *Moduli of K3 surfaces and irreducible symplectic manifolds*,
`https://people.bath.ac.uk/masgks/Papers/handbook.pdf`, Prop. 2.5 and Thm 2.6 (both attributed there
to BHPV Prop. VIII.3.11 and Sections VIII.7–VIII.11); and the polarized form Cor. VIII.3.12 / Thm
VIII.11.1 in `https://ar5iv.labs.arxiv.org/html/1501.04049`, Thm 4. (ii) Nakai–Moishezon for
$\Q$-divisors on a smooth projective surface (Lemma 2.2), and the fact that ampleness pulls back
along a finite morphism. (iii) Ehresmann's theorem and the flatness of classes of divisors in a flat
proper family for the transport of Lemma 3.6(4) and Theorem 4.1. No statement of BHPV is used at a
chapter level without its hypotheses checked above: in each case the class to which the theorem is
applied is exhibited (the ample class $2H_b-\alpha_b$ for VIII.3.11/Thm VIII.11.1).
