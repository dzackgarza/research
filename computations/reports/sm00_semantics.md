# The three cones and the fourth bullet: corrected semantics, with proofs

Member m7, swarm `smw0b9kmo`. Deliverable for defect 1 (three-cone semantics) and for the
semantics check of the fourth bullet's quantifier. The repository is
`/workspace/nucleus/work/projects/p-9fcb4ed7f4b64e008de2ee29a7197bf4/repo`, read and not modified;
citations are `path:line` at evidence state `83403bc8` unless another commit is named. The authored
text is cited at `a145cea4a5`. Every numbered statement below is either **proved here** (proof in
place), **cited at a level I checked** (the check is named), or **marked open**.

Nothing here uses an integral eigensplitting of $H^2(X,\mathbb{Z})$, the type of $S_\mathrm{Co}$, a
gluing index, or the twist identification. The label-own reading appears only as the named
alternative R6 of §5.3.

---

## 0. The sentences this section replaces

**(Q1) authored bullet.** `writing/coble/heegner-report/coble-heegner-research-report.md`, commit
`a145cea4a5` line 626 (identical at `83403bc8:626`):

> $\mathfrak c$ is the chosen positive/nef chamber in which $\alpha$ is effective and $H$ is nef and
> big;

**(Q2) authored conclusion.** same file `a145cea4a5:631` (identical at `83403bc8:636`):

> Any two tuples $\mathfrak L_{\mathrm{Co},2}$ arising from the direct projective construction are
> conjugate by an element of $O(L_{K3})$ preserving the labels, the degree-$4$ class, the effective
> root, and the chosen chamber.

**(Q3) corpus's reading of (Q1).** `83403bc8:630` "$\mathfrak c$ is a chamber in $H$'s cone", and
`83403bc8:651` "the labels pin a chamber of the arrangement cut by a member's own effective roots,
and the transported chamber coincides with the target's chamber exactly when no extra effective root
cuts it".

**(T1) tracked three-cone parenthetical to be corrected,** `computations/reports/sm57_obstruction-m8.md`
§1.2 (A), in its own words: "$K_{X_b}\subset\operatorname{Pic}(X_b)\otimes\mathbb R$ is the interior of
the nef cone, a cone in a $\rho$-dimensional space; the component above is a chamber of the chamber
arrangement of the positive cone of the full $H^2(X_b,\mathbb R)$, of signature $(3,19)$ … The Kähler
cone is contained in a unique such chamber … and its intersection with $\operatorname{Pic}(X_b)\otimes
\mathbb R$ is exactly $K_{X_b}$, the $x\cdot\delta>0$ description restricted to algebraic $x$."

**(T2) tracked verdict sentence to be corrected,** `83403bc8:661`: "Under either interpretation of the
cone that 'chosen' picks out (Kähler cone in $\operatorname{Pic}\otimes\mathbb R$, or the component of
the positive cone of $H^2(X,\mathbb R)$ containing it), no label-preserving isometry can match the two
chambers."

Five things are wrong or imprecise in (T1)–(T2), and §1–§4 fix them: (i) the Kähler cone is not a cone
in $\operatorname{Pic}\otimes\mathbb R$ and is not $\rho$-dimensional (Lemma 1.3); (ii) $\{x^2>0\}$ in
signature $(3,19)$ is connected, so there is no "the positive cone of $H^2(X,\mathbb R)$" and no
"component containing it" (Lemma 1.5); (iii) the intersection of the Kähler chamber with
$\operatorname{Pic}\otimes\mathbb R$ is the **ample** cone, not the Kähler cone (Lemma 1.3(b), Theorem 2);
(iv) in the $H^{1,1}$ reading the chamber **is** a product, so the tracked worry that it is not is
misplaced, while in the full-$H^2$ reading it is not a product and the tracked assertion about its
trace is still right but for a different reason (Theorem 4, Theorem 5); (v) the conclusion of (T2) is
correct, but the reason it is correct is uniform across **all** the readings, and is not "the chamber
is not a product": it is that the chamber's own intrinsic structure recovers the member's Picard
lattice, so the chamber clause is a Picard-comparison condition (Theorem 6, Corollary 7).

---

## 1. The three objects, with their exact spaces, dimensions and signatures

### 1.1 Conventions

$X$ is a smooth projective K3 surface over $\mathbb C$. Then

* $L := H^2(X,\mathbb Z)$ is the K3 lattice, even unimodular of signature $(3,19)$, rank $22$
  (Hodge index theorem; $b_2=22$);
* $V := H^2(X,\mathbb R) = L\otimes\mathbb R$, signature $(3,19)$;
* $W := H^{1,1}(X,\mathbb R) = H^{1,1}(X)\cap V$, real dimension $h^{1,1}=20$, and the intersection
  form restricts to a form of signature $(1,19)$ on $W$ (Hodge index theorem);
* $\mathrm{Pic}(X) = H^{1,1}(X)\cap L$ (Lefschetz $(1,1)$, $X$ projective), $\rho := \operatorname{rk}
  \operatorname{Pic}(X)\ge 1$, and $\mathrm{NS}_\mathbb R := \operatorname{Pic}(X)\otimes\mathbb R
  \subset W$ has real dimension $\rho$;
* $N := \mathrm{NS}_\mathbb R^{\perp}\cap W$. Since $X$ is projective, the form is non-degenerate on
  $\mathrm{NS}_\mathbb R$ (signature $(1,\rho-1)$), and $N$ is negative definite of dimension
  $20-\rho$; the form is non-degenerate on $W$, so
  $$W = \mathrm{NS}_\mathbb R \perp N \qquad\text{(orthogonal direct sum)} .$$
  Let $p\colon W\twoheadrightarrow \mathrm{NS}_\mathbb R$ be the orthogonal projection with kernel $N$.

**Definition 1.1.** (a) $\mathcal P = \mathcal P(X) \subset W$ — the *positive cone*: the component of
$\{x\in W : x^2>0\}$ containing the classes of Kähler forms. (b) $\mathcal K = \mathcal K(X)\subset W$ —
the *Kähler cone*: classes of Kähler forms. (c) $\operatorname{Nef} := \overline{\mathcal K}\subset W$ —
the (analytic) nef cone. (d) $\operatorname{Amp} = \operatorname{Amp}(X) := \mathcal K\cap \mathrm{NS}_\mathbb R
\subset \mathrm{NS}_\mathbb R$ — the ample cone. (e) $\Delta(X) := \{\delta\in\operatorname{Pic}(X):
\delta^2=-2\}$; $\Delta^+\subset\Delta(X)$ the *effective* ones. (f) A *wall* is $\delta^{\perp}\cap \mathcal P$
for $\delta\in\Delta(X)\setminus\{0\}$; a *chamber* of $\mathcal P$ is a connected component of
$\mathcal P \setminus \bigcup_{\delta}\delta^{\perp}$. The wall sets of $\delta$ and $-\delta$ coincide,
so the arrangement does not depend on the sign choice.

### 1.2 Lemma 1 (the position of each cone)

1. $\mathcal K\subset W$ is an open convex cone of real dimension $20$; $\mathcal K\not\subset
   \mathrm{NS}_\mathbb R$ unless $\rho=20$.
2. $\operatorname{Amp} = \mathcal K\cap \mathrm{NS}_\mathbb R$ is an open convex cone in
   $\mathrm{NS}_\mathbb R$ of real dimension $\rho$. In particular $\operatorname{Amp}\neq\mathcal K$
   whenever $\rho<20$, and "$K_{X_b}\subset \operatorname{Pic}(X_b)\otimes\mathbb R$" of (T1) is false.
3. $\mathcal K = \operatorname{int}\operatorname{Nef}$.

*Proof.* (1) A Kähler form is a real $2$-form of type $(1,1)$, so its class lies in $W$; the set of such
classes is open (openness of the Kähler cone, standard) and convex (a positive sum of Kähler forms is a
Kähler form) and has nonempty interior in $W$, hence spans $W$, so its dimension is $\dim_\mathbb R
W=20$. Since $\dim\mathrm{NS}_\mathbb R=\rho$, $\mathcal K$ is not contained in $\mathrm{NS}_\mathbb R$
when $\rho<20$; $\rho\le h^{1,1}=20$ always.

(2) By Lefschetz $(1,1)$ and Kodaira's embedding theorem, an integral class in $\mathcal K$ is ample;
a real class in $\operatorname{NS}_\mathbb R$ is a finite real combination of integral classes, so
$\mathcal K\cap\mathrm{NS}_\mathbb R$ consists of real combinations of classes of ample line bundles, and
conversely every such combination is a positive combination of Kähler classes, hence Kähler. That is:
$\operatorname{Amp}=\mathcal K\cap\mathrm{NS}_\mathbb R$ — this is the standard identification of the
ample cone inside $H^{1,1}(X,\mathbb R)$, and it can equally be derived from Kleiman's criterion
(Lazarsfeld, *Positivity in Algebraic Geometry I*, Theorem 1.4.9: $\operatorname{Amp}=\operatorname{int}
\operatorname{Nef}$ in $\mathrm{NS}_\mathbb R$) together with $\mathcal K\cap\mathrm{NS}_\mathbb R
\subseteq \operatorname{Nef}$ and the strict positivity $\alpha\cdot C>0$ on every curve $C$ for
$\alpha\in\mathcal K$; both facts I have checked in the cited form. Openness is openness of $\mathcal K$
intersected with the subspace; $\dim=\rho$ because the ample cone is nonempty and open in
$\mathrm{NS}_\mathbb R$ (Kleiman).

(3) $\mathcal K\subseteq \mathcal K$ open gives $\mathcal K\subseteq\operatorname{int}\operatorname{Nef}
=\operatorname{int}\overline{\mathcal K}$. For the converse use convexity: for a convex set $C$ in a
finite-dimensional real vector space, $\operatorname{int}\overline C=\operatorname{int} C$. (Proof:
let $x\in\operatorname{int}\overline C$ and $y\in\operatorname{int} C$; choose $\varepsilon>0$ with
$x':=x+\varepsilon(x-y)\in\overline C$; then $x=\frac{1}{1+\varepsilon}x'+\frac{\varepsilon}{1+\varepsilon}y$
is a convex combination in which one summand is interior, so $x\in\operatorname{int} C$.) $\square$

**Consequence 1.2.** The three objects of the problem statement are now separated: the Kähler cone is a
$20$-dimensional cone in $W$; the ample cone is a $\rho$-dimensional cone in $\mathrm{NS}_\mathbb R$; the
chamber is a $20$-dimensional cone in $\mathcal P\subset W$ (and in §2 we identify exactly how the last
two are related). None of the three is the other, and the two-dimensional gap $N$ is where the tracked
text lost track of the spaces.

### 1.3 Theorem 2 (the Kähler chamber; the only citation this section needs)

Let $X$ be a K3 surface with a Kähler class. Then

$$\mathcal K(X) \;=\; \bigl\{\,x\in\mathcal P(X) \;:\; (x,\delta)>0 \ \ \forall\,\delta\in\Delta^+(X)\,\bigr\},$$

that is, the Kähler cone is exactly the chamber of the arrangement of effective $(-2)$-classes whose
closure contains a Kähler class.

*Status.* This is **BHPV** (*Compact Complex Surfaces*, 2nd ed.), **Corollary VIII.3.9**. I did not read
BHPV itself; I checked the statement as quoted verbatim, with the numbering, in D. Huybrechts,
*Moduli of K3 surfaces and irreducible symplectic manifolds* (Handbook of Moduli), §2.1: "The chamber
$C_S^+=\{x\in C_S \mid (x,\delta)>0\ \text{for all effective }\delta\in\Delta\}$ is equal to the Kähler
cone of $S$ according to [6, Corollary VIII.3.9]", where $[6]$ is BHPV. §2.1 of the same paper also
supplies, at the same checkable level, the positive cone $C_S\subset\{x\in H^{1,1}(S,\mathbb R):
(x,x)>0\}$, the signature $(1,19)$, the description of the chambers as the components of
$C_S\setminus\bigcup_\delta H_\delta$ with $H_\delta$ the hyperplane orthogonal to $\delta$, and the
transitivity of the reflection group's action on chambers. A secondary and independent check on
Theorem 2 as used here: it is used **only** to know that the chamber containing a Kähler class has
closure cut out by the effective roots with signs, i.e. $\overline{\mathcal K}=\{x\in\overline{\mathcal P}:
(x,\delta)\ge 0\ \forall\delta\in\Delta^+\}$; the proofs below never use more than this, and every place
where a weaker input suffices is flagged.

**Corollary 2.1.** The chamber containing a Kähler class is unique and equals $\mathcal K$; its closure is
$\overline{\mathcal K}=\{x\in\overline{\mathcal P}:(x,\delta)\ge0\ \text{for all }\delta\in\Delta^+\}$,
a closed convex cone, and $\mathcal K$ is its interior (Lemma 1(3)).

### 1.4 Lemma 3 (no "positive cone of $H^2(X,\mathbb R)$")

Let $q$ be a real quadratic form of signature $(p,r)$ on a real vector space $V$.

1. If $p\ge 2$ then $\{v\in V:q(v)>0\}$ is connected. Hence in signature $(3,19)$ — in particular for
   $V=H^2(X,\mathbb R)$ — the positivity locus is connected and "the positive cone of $H^2(X,\mathbb R)$"
   is not a two-sheeted object that could select a chamber by itself.
2. If $(p,r)=(1,n)$ then $\{v:q(v)>0\}$ has exactly two components, exchanged by $v\mapsto -v$, and each
   is convex.

*Proof.* (1) Take an orthogonal decomposition $V=V_+\perp V_-$ with $q|_{V_+}$ positive definite of
dimension $p$ and $q|_{V_-}$ negative definite. Write $v=v_++v_-$; $q(v)>0$ gives $\lvert v_+\rvert>\lvert
v_-\rvert\ge0$, so $v_+\neq0$. The path $t\mapsto v_+ + (1-t)v_-$, $t\in[0,1]$, stays in $\{q>0\}$
because $\lvert v_+\rvert^2-(1-t)^2\lvert v_-\rvert^2\ge \lvert v_+\rvert^2-\lvert v_-\rvert^2>0$. Then
$\mathrm{SO}(V_+)$ is connected for $p\ge2$, so $v_+$ can be moved to any other positive vector inside
$V_+\subset\{q>0\}$. Hence every point of $\{q>0\}$ is connected to a fixed one.

(2) For signature $(1,n)$, $\{q>0\}$ has the two components ("sheets") determined by the sign of
$(v,v_0)$ for any fixed $v_0$ with $q(v_0)>0$, and each is convex by the reverse Cauchy–Schwarz
inequality $(x,y)\ge\sqrt{q(x)q(y)}>0$ for $x,y$ in one sheet. $\square$

### 1.5 Remark 4 (what the two readings of "the chamber" can be)

Lemma 3 removes one of the two readings in (T1)/(T2): since $\{x\in V: x^2>0\}$ is connected in
signature $(3,19)$, a chamber of the full-$H^2$ arrangement is a component of
$\{x\in V:x^2>0\}\setminus\bigcup_\delta\delta^\perp$ and **is selected by the Kähler class and not by
positivity**. Positivity at the level of $V$ does not cut anything out; positivity at the level of $W$
does (Lemma 3(2)), and that is where $\mathcal P$ lives. So the two legitimate ambients are

* **(W) $W=H^{1,1}(X,\mathbb R)$, signature $(1,19)$, chamber in $\mathcal P$** — the space in which
  Theorem 2 is stated; and
* **(V) $V=H^2(X,\mathbb R)$, signature $(3,19)$, chamber = component of the positivity locus minus the
  walls that contains the Kähler cone** — the reading (T1) literally proposes.

§2 treats (W) completely; §3 treats (V) and shows that it adds nothing but a two-dimensional
translation-invariant thickening, and that the tracked assertion (T1) about its trace is nevertheless
true, while the reason given for it is not.

---

## 2. Reading (W): trace, product structure, and the counterexample the problem asks for

Keep the notation of §1.1. For $\delta\in\Delta(X)$ we have $\delta\in\mathrm{NS}_\mathbb R$, hence
$N\subseteq\delta^{\perp}$, hence

$$\delta^{\perp}\cap W = p^{-1}\bigl(\delta^{\perp}\cap \mathrm{NS}_\mathbb R\bigr).\tag{2.1}$$

So the whole wall arrangement in $W$ is the $p$-pullback of the arrangement in $\mathrm{NS}_\mathbb R$
cut by the same classes. This is the exact sense in which "every non-algebraic direction escapes every
wall": a direction $x\in W$ lies on the wall of $\delta$ if and only if its algebraic shadow $p(x)$ does;
in particular the whole subspace $N$ lies on **every** wall (so the slogan needs its one-line
correction: it is $p(x)$, not $x$, that the walls see, and $N$ is on all of them).

### 2.1 Theorem 5 (trace = product)

Let $X$ be a projective K3 and $c\subset\mathcal P$ a chamber of the arrangement (2.1).

1. $p(c)$ is contained in exactly one chamber $c_{\mathrm{alg}}$ of the arrangement in
   $\mathcal P_{\mathrm{alg}}:=\mathcal P\cap\mathrm{NS}_\mathbb R\subset\mathrm{NS}_\mathbb R$ cut by the
   hyperplanes $\delta^{\perp}\cap\mathrm{NS}_\mathbb R$, $\delta\in\Delta(X)$.
2. $c = p^{-1}(c_{\mathrm{alg}})\cap\mathcal P$, and in fact $p^{-1}(c_{\mathrm{alg}})\subseteq\mathcal P$,
   so
   $$c \;=\; c_{\mathrm{alg}}\times N \;=\; \bigl(c\cap \mathrm{NS}_\mathbb R\bigr)\times N
   \qquad\text{(literally a product in } W=\mathrm{NS}_\mathbb R\perp N\text{)}.$$
3. $c\mapsto c\cap\mathrm{NS}_\mathbb R$ is a bijection from the set of chambers in $\mathcal P$ onto the
   set of chambers in $\mathcal P_{\mathrm{alg}}$, with inverse $C\mapsto p^{-1}(C)$.

*Proof.* (2) First, $p^{-1}(\mathcal P_{\mathrm{alg}})\subseteq\mathcal P$: if $u\in\mathcal P_{\mathrm{alg}}$
and $n\in N$ then $(u+n)^2=u^2+n^2>0$ because $u^2>0$ and $n^2\le0$, and the segment $t\mapsto u+(1-t)n$
stays in $\{x^2>0\}$; so $u+n$ lies in the same component of $\{x^2>0\}\cap W$ as $u$, namely
$\mathcal P$. Hence for any $C\subseteq\mathcal P_{\mathrm{alg}}$, the set $p^{-1}(C)$ is already
contained in $\mathcal P$.

Now let $c$ be a chamber. $p(c)$ is connected (as $c$ is) and avoids every hyperplane $\delta^\perp\cap
\mathrm{NS}_\mathbb R$ by (2.1); since $p(c)\subseteq\mathcal P_{\mathrm{alg}}$ as just shown, $p(c)$ lies
in a single chamber $c_{\mathrm{alg}}$ of $\mathcal P_{\mathrm{alg}}$. Then
$p^{-1}(c_{\mathrm{alg}})=\{(u,n):u\in c_{\mathrm{alg}},n\in N\}$ is convex, hence connected, avoids every
wall by (2.1), is contained in $\mathcal P$, and contains $c$; since a chamber is a maximal connected
subset of $\mathcal P\setminus\bigcup_\delta\delta^\perp$, $p^{-1}(c_{\mathrm{alg}})=c$. This is the
displayed formula, and (1), (3) follow: injectivity from the formula $c=p^{-1}(c\cap\mathrm{NS}_\mathbb R)$,
surjectivity because for a chamber $C$ of $\mathcal P_{\mathrm{alg}}$ the set $p^{-1}(C)$ is convex,
contained in $\mathcal P$, avoids all walls, and its trace is $C$. $\square$

**Corollary 5.1 (answer to the question "are chamber invariants read on $\operatorname{Pic}_\mathbb R$ at
all?").** Yes, and exactly: the chamber is *equal* to the product of its trace with $N$. Hence (i) no
chamber invariant is lost by passing to the trace, and no chamber carries information beyond a chamber of
the algebraic arrangement; (ii) **the track of (T1) that "the chamber is not a product" is false in the
only reading in which Theorem 2 lives** — it is *literally* a product, with the $N$-factor being the
Hodge-theoretic direction, on which no wall depends; (iii) the faithfulness of the trace is *not* the
same as the corpus's step "span of a chamber $=\operatorname{Pic}\otimes\mathbb R$", see Theorem 6.

### 2.2 Corollary 5.2 (the two traces that matter, and the counterexample)

1. $\mathcal K\cap\mathrm{NS}_\mathbb R=\operatorname{Amp}$ (Lemma 1.2), so the trace of the *Kähler*
   chamber is the ample cone, **not** the Kähler cone. The tracked phrase "$K_{X_b}$ … restricted to
   algebraic $x$" is therefore the ample cone and must be written $\operatorname{Amp}(X_b)$.
2. For any $\delta\in\Delta(X)\setminus\{0\}$ let $s_\delta(x)=x+(x,\delta)\delta$ be the reflection, an
   integral isometry of $L$ preserving $W$ (because $\delta\in H^{1,1}$) and $\mathrm{NS}_\mathbb R$. Then
   $c:=\mathcal P\cap s_\delta(\mathcal K)$ is a chamber, $c=s_\delta(\mathcal K)$, and
   $$c\cap\mathrm{NS}_\mathbb R=s_\delta(\operatorname{Amp}),\qquad
   s_\delta(\operatorname{Amp})\cap\operatorname{Amp}=\emptyset .$$
   Indeed, replacing $\delta$ by $-\delta$ does not change $s_\delta$ (as $s_{-\delta}=s_\delta$), so we may
   suppose $\delta$ effective; then $(x,\delta)>0$ for every $x\in\operatorname{Amp}$, while
   $(s_\delta x,\delta)=-(x,\delta)<0$, so $s_\delta(\operatorname{Amp})$ lies in the open half-space
   $\{(y,\delta)<0\}$ and is disjoint from $\operatorname{Amp}$. So at least one chamber's trace is the
   ample cone of *another* K3 (the one with period $s_\delta$ applied) and is disjoint from this member's
   ample cone.
3. Consequently the assertion "for every chamber $c$ of the arrangement, $c\cap\operatorname{Pic}\otimes
   \mathbb R=\mathcal K_X$", in the only reading in which it can be true, must be replaced by
   $$\operatorname{trace}(\text{Kähler chamber})=\operatorname{Amp}(X),\qquad
   \operatorname{trace}(w\mathcal K)=w(\operatorname{Amp}(X))\ \ (w\in W(X)),$$
   and it is *false* for $w\neq$ a Kähler-cone-preserving isometry.

*Proof.* The only cases needing proof are (2) and (3). $\delta^\perp$ is a wall, and $s_\delta$ fixes
$\delta^\perp$ pointwise and permutes $\Delta(X)$ (integral isometry), hence maps walls to walls and
chambers to chambers; so $s_\delta(\mathcal K)$ is a chamber. It preserves $\mathrm{NS}_\mathbb R$ and
$N$, so $s_\delta(\mathcal K)\cap\mathrm{NS}_\mathbb R=s_\delta(\operatorname{Amp})$. The computation
$(s_\delta x,\delta)=- (x,\delta)$ shows $s_\delta(\operatorname{Amp})$ lies in the open half-space
$\{y:(y,\delta)<0\}$ while $\operatorname{Amp}$ lies in $\{y:(y,\delta)>0\}$ for $\delta$ effective;
$\operatorname{Amp}$'s positivity against effective classes is $\alpha\cdot C>0$ for $\alpha$ ample and
$C\neq0$ effective. (3) is then (1) plus part (2), the general chamber being $w(\mathcal K)$ for
$w$ in the group generated by the reflections — this last phrase is *not* used anywhere below; the
statement is only that the trace of $\mathcal K$ is $\operatorname{Amp}$ and that other chambers have
other traces, for which one example suffices. $\square$

**How to read 5.2 against the corpus.** The corpus says (in `sm57_obstruction-m8.md` §1.2(C), and
repeatedly on the board) that the chamber is *canonically determined by $(H,\alpha)$* because
$\omega_b=H_b-\tfrac12\alpha_b$ is ample on every member. That is true and I re-prove it in §5.2 (Lemma 9). The
two statements are compatible: $\omega_b$ pins *which* chamber, and Theorem 5 says what a chamber
contains once pinned. What 5.2 adds is the correction of the object: the pinned chamber's *trace* is
$\operatorname{Amp}(X_b)$, an object that varies with the member; the chamber itself is the product of
that trace with $N_b$.

---

## 3. Reading (V): the full-$H^2$ chamber, and why it is equivalent

Now let $V=H^2(X,\mathbb R)$, kept as a quadratic space of signature $(3,19)$, and let
$W=H^{1,1}(X,\mathbb R)$, $N_V:=$ the real part of $H^{2,0}\oplus H^{0,2}$. Then $N_V$ is positive
definite of dimension $2$, $V=W\perp N_V$, and every wall $\delta^{\perp}\subset V$ contains $N_V$
(because $\delta\in W$), so
$$\delta^\perp\cap V = p_W^{-1}\bigl(\delta^\perp\cap W\bigr),\qquad
p_W\colon V\twoheadrightarrow W\ \text{orthogonal projection}. \tag{3.1}$$

### 3.1 Theorem 6 (the $V$-chamber)

Let $c_x$ be the chamber of $\{v\in V:v^2>0\}\setminus\bigcup_{\delta\in\Delta(X)}
\delta^{\perp}$ containing a Kähler class $k$.

1. **Not a product.** $c_x=p_W^{-1}(\mathrm{Cell})\cap\{v:v^2>0\}$, where $\mathrm{Cell}\subset W$ is the
   component of $W\setminus\bigcup_\delta\delta^\perp$ containing $k$; this set is not a product of its
   trace with anything, because the condition $v^2>0$ couples the $W$- and $N_V$-coordinates.
2. **Its trace is still the ample cone:** $c_x\cap\mathrm{NS}_\mathbb R=\operatorname{Amp}(X)$.
3. **It adds no wall data:** the set $c_x$ is invariant under translation by $N_V$ (i.e. $x\in c_x$ and
   $n\in N_V$ imply $x+n\in c_x$), and $N_V$ is *the* maximal linear subspace $L_0$ with $c_x+L_0=c_x$.
   Consequently a lattice isometry $\gamma\in O(L)$ with $\gamma(c_x)=\gamma(c_{x'})$ satisfies
   $\gamma(N_{V})=\gamma(N_{V}')$ and hence $\gamma(W)=\gamma(W')$ and $\gamma\operatorname{Pic}(X)=
   \gamma\operatorname{Pic}(X')$.
4. **Correction of (T1).** In this reading the tracked sentence "its intersection with
   $\operatorname{Pic}(X_b)\otimes\mathbb R$ is exactly $K_{X_b}$" is right only after replacing
   $K_{X_b}$ by $\operatorname{Amp}(X_b)$; and the tracked description of $c_x$ as "the component of the
   positive cone of $H^2(X_b,\mathbb R)$ of signature $(3,19)$ containing $\mathcal K$" is not a
   description at all, because that positivity locus is connected (Lemma 3(1)) and every chamber of the
   arrangement in $V$ lies in it: the chamber is selected by $k$, not by positivity.

*Proof.* (1) By (3.1) the walls see only $p_W(v)$; the sign pattern of $(p_W(v),\delta)$, $\delta\in\Delta(X)$,
is locally constant on $\{v^2>0\}\setminus\bigcup\delta^\perp$, so each such chamber is
$\{v: v^2>0,\ p_W(v)\in \mathrm{Cell}\}$ for one cell $\mathrm{Cell}$ of $W\setminus\bigcup\delta^\perp$.
Because $k$ has $p_W(k)=k\in\mathrm{Cell}$ and $k^2>0$, the chamber of $k$ is the displayed set.
It is not a product: if $v\in c_x$ and $n\in N_V$ with $n\neq0$, then $v+n$ need not satisfy
$(v+n)^2>0$ when $v^2\le n^2$, so $c_x$ is not $C\times N_V$ for any $C$; equivalently the fibres of
$p_W|_{c_x}$ are the sets $\{n: n^2>-p_W(v)^2\}$, which are balls-complements for $p_W(v)^2\le0$.

(2) For $u\in\mathrm{NS}_\mathbb R\subset W$, $p_W(u)=u$; and $u\in c_x$ iff $u\in\mathrm{Cell}$ and
$u^2>0$. Now $\mathrm{Cell}$ is the component of $W\setminus\bigcup_\delta\delta^\perp$ containing $k$;
since the sign pattern of $(u,\delta)$ is constant on $\mathrm{Cell}$ and equals that of $k$ (positive
on $\Delta^+$, negative on $-\Delta^+$), $\mathrm{Cell}\cap\mathrm{NS}_\mathbb R$ consists exactly of the
$u$ with $(u,\delta)>0$ for all $\delta\in\Delta^+$, i.e. (Theorem 2) of $\operatorname{Amp}(X)$.

(3) Translation invariance is immediate from (3.1) and $(v+n)^2=v^2+n^2+2(v,n)=v^2+n^2>0$ for $v\in c_x$,
$n\in N_V$. If $c_x+L_0=c_x$ then for $v\in c_x$ and $y\in L_0$ we need all $v+ty\in c_x$, in particular
$p_W(v)+tp_W(y)$ stays in the cone $\mathrm{Cell}$, which is an open convex cone containing no affine
line, so $p_W(y)=0$, i.e. $y\in N_V$; hence $L_0=N_V$. Then $\gamma(N_V)=N_V'$ from
$\gamma(c_x)=c_{x'}$, and $W=N_V^{\perp}$, so $\gamma W=W'$; and
$\gamma\operatorname{Pic}(X)=\gamma(W\cap L)=W'\cap L=\operatorname{Pic}(X')$. $\square$

**Summary of §2–§3.** The trace of the chamber on $\operatorname{Pic}\otimes\mathbb R$ is
$\operatorname{Amp}(X)$ in *both* readings, and in both readings the chamber is determined by the pair
(arrangement of the member's own roots, the pinned Kähler class) together with the Hodge-theoretic
direction ($N$ respectively $N_V$), which carries no wall data. So the tracked debate between the two
ambients is immaterial: the readings agree on every invariant used below, and both make the tracked
"not a product" claim either false (W) or irrelevant (V).

---

## 4. What "preserving the chamber" forces: the uniform theorem

This is the correct replacement for the corpus's step "span of a chamber $=\operatorname{Pic}\otimes
\mathbb R$" (`sm57_obstruction-m8.md` Theorem 3.1 proof; `sm57_proof-m5.md` Corollary 5.2), which is
valid in one reading only.

### 4.1 Theorem 7 (Picard forcing)

Let $X,X'$ be projective K3 surfaces, $\gamma\in O(L_{K3})$ an isometry of the abstract K3 lattice let
$\gamma\colon H^2(X,\mathbb Z)\to H^2(X',\mathbb Z)$ (no Hodge condition is assumed), and let
$c\subseteq W$, $c'\subseteq W'$ be, respectively, one of the five objects

| reading | object $c$ | space | intrinsic detector of $\gamma\operatorname{NS}_\mathbb R=\operatorname{NS}'_\mathbb R$ |
|---|---|---|---|
| R1 | $\operatorname{Nef}(X)$ (closed) | $\mathrm{NS}_\mathbb R\subset W$ | $\operatorname{span}_{\mathbb R}c=\mathrm{NS}_\mathbb R$ ($\dim\rho$) |
| R2 | $\operatorname{Amp}(X)$ | $\mathrm{NS}_\mathbb R$ | $\operatorname{span}_{\mathbb R}c=\mathrm{NS}_\mathbb R$ |
| R3 | $\mathcal K(X)$ | $W$ ($\dim20$) | $\operatorname{span}_{\mathbb R}c=W$, then $\operatorname{NS}_\mathbb R=W\cap L$ |
| R4 | the $V$-chamber $c_x$ of Theorem 6 | $V$ ($\dim22$) | maximal translation-invariance subspace $=N_V$, then $W=N_V^\perp$, then $\operatorname{NS}_\mathbb R=W\cap L$ |
| R5 | $\mathcal P(X)$ (positive cone) | $W$ | $\operatorname{span}_{\mathbb R}c=W$, then $\operatorname{NS}_\mathbb R=W\cap L$ |
| R6 | the chamber cut by the label lattice only | $N\otimes\mathbb R$-ambient | *not* recovering $\operatorname{NS}_\mathbb R$; $c$ is a function of $(H,\alpha)$ (named alternative, §4.3) |

Suppose $\gamma(c)=c'$. Then $\gamma(\operatorname{NS}_\mathbb R)=\operatorname{NS}'_\mathbb R$ and hence
$\gamma\operatorname{Pic}(X)=\operatorname{Pic}(X')$; moreover in readings R3, R4, R5 also
$\gamma W=W'$, so $\gamma$ matches the $(1,1)$-parts of the two Hodge structures at the level of real
subspaces. Consequently, for any $h\in\operatorname{Pic}(X)$, the counting set
$\{\delta\in\operatorname{Pic}(X):\delta^2=-2,\ (\delta,h)=1\}$ is carried bijectively onto
$\{\delta'\in\operatorname{Pic}(X'):\delta'^2=-2,\ (\delta',\gamma h)=1\}$, since $\gamma$ preserves the
lattice, the form and $h$.

*Proof.* The five detectors are exactly the assertions proved in Lemma 1 and Theorems 2, 5 and 6:
$\operatorname{span}\operatorname{Nef}=\operatorname{span}\operatorname{Amp}=\mathrm{NS}_\mathbb R$
(Nef contains the open ample cone, Lemma 1.2); $\operatorname{span}\mathcal K=W$ (Lemma 1.1);
$\operatorname{span}\mathcal P=W$ (Lemma 1.1 and Lemma 3(2): $\mathcal P$ is open in $W$); and the
$V$-chamber's maximal translation-invariance subspace is $N_V$ (Theorem 6(3)). An isometry carries spans
to spans and translation-invariant subspaces to translation-invariant subspaces, so
$\gamma\mathrm{NS}_\mathbb R=\mathrm{NS}'_\mathbb R$ (R1, R2), $\gamma W=W'$ (R3, R4, R5), and in all
cases $\gamma\operatorname{Pic}(X)=\gamma(W\cap L)=W'\cap L=\operatorname{Pic}(X')$ — the last step uses
only that $\gamma$ is an isometry of the integral lattice $L_{K3}$ and that
$\operatorname{Pic}=H^{1,1}\cap L$. The counting identity is then the bijection $\delta\mapsto\gamma\delta$,
which preserves squares and the values of the pairing with $h$ and $\gamma h$. $\square$

**Remark 7.0 (effectivity, and why no proof here needs it).** The counting set above is defined over all
of $\operatorname{Pic}$, not over the effective classes; this is deliberate, because it is then invariant
under a bare lattice isometry with $\gamma h=h'$ and needs no effectivity. In the hands of §6 the set is
*computed* inside a single member, where Riemann–Roch and the nefness of $H_b$ decide effective signs
(Lemma 10(3)); no cross-member effectivity statement is used. If one does want it: a Hodge isometry
$\gamma$ with $\gamma W=W'$ is effective (carries $\overline{\mathcal K}$ into $\overline{\mathcal K}'$)
iff it carries one Kähler class to a Kähler class — BHPV Proposition VIII.3.11 as quoted in Huybrechts
§2.1.

**Corollary 7.1.** In readings R1–R5 the chamber clause of (Q2) implies $\gamma\operatorname{Pic}(X_b)
=\operatorname{Pic}(X_{b'})$, hence identifies $\operatorname{Pic}$, $\Delta$ and all invariants of the
tuple that are functions of $(\operatorname{Pic},H,\alpha)$ — in particular the number
$\nu(b)=\#\{\delta\in\operatorname{Pic}(X_b):\delta^2=-2,\ \delta\cdot H_b=1\}$. In reading R6 the same
clause is implied *by* the labels and carries no such information.

**Corollary 7.2 (the corpus's Theorem 3.1, corrected).** "$\gamma c_b=c_{b'}\iff \gamma
(\operatorname{Pic}(X_b)\otimes\mathbb R)=\operatorname{Pic}(X_{b'})\otimes\mathbb R$" is correct with
the forward implication as in Corollary 7.1, but the backward implication needs the hypothesis "no
effective root of $b'$ outside the transported set cuts $c_{b'}$" — verbatim the corpus's own condition
at `83403bc8:651`. Reason: if $\gamma\Delta_b\subsetneq\Delta_{b'}$ then the $b'$-arrangement is finer,
$\gamma c_b$ is a chamber of the coarser arrangement only, and $c_{b'}\subseteq\gamma c_b$ with equality
exactly when no extra root cuts. The proof in `sm57_obstruction-m8.md` Theorem 3.1 ($\Leftarrow$) omits
this hypothesis; the corpus's own line 651 states it, so the omission is in the proof, not in the
conclusion as used.

**Nothing in Theorem 7 is a Hodge condition.** Parallel transport in the one-node family gives a *lattice*
isometry with $\gamma H_b=H_{b'}$, $\gamma\alpha_b=\alpha_{b'}$, $\gamma S_{\mathrm{Co},b}
=S_{\mathrm{Co},b'}$ — it does **not** give a Hodge isometry, because the Hodge filtration is a varying
subbundle of the flat bundle, not a flat one. This is not a defect of any tracked document (I checked: the
only "Hodge isometry" in the tracked reports is in `sm57_obstruction-m8.md` Theorem 3.3, where *equal
periods* under a trivialisation give one, which is a different and correct statement). It matters because
it shows exactly where the chamber clause bites: it is the clause that upgrades a bare lattice isometry to
a $(1,1)$-matching isometry (R3–R5) or a Picard-matching one (R1–R2), and nothing else in the tuple of
(Q2) does that. See §6.3 for the numerical witness (the $\nu$ jump), which is possible precisely because
transport is not a Hodge isometry.

### 4.2 The three corpus argument steps, checked against each reading

The problem names three steps of the corpus's chamber reasoning. Here is their status in each reading.

**(a) "span of a chamber $=\operatorname{Pic}\otimes\mathbb R$"** — as used in the proof of
`sm57_obstruction-m8.md` Theorem 3.1 ($\Rightarrow$) and in `sm57_proof-m5.md` Corollary 5.2.

* R1, R2: **valid**, because $\operatorname{Nef}$ contains the open ample cone, so
  $\operatorname{span}\operatorname{Nef}=\operatorname{span}\operatorname{Amp}=\mathrm{NS}_\mathbb R$.
* R3, R5: **invalid as stated**: $\operatorname{span}\mathcal K=\operatorname{span}\mathcal P=W$, of
  dimension $20$, not $\rho$. Correct replacement, and the one Theorem 7 uses: from
  $\gamma\operatorname{span}c=\operatorname{span}c'$ deduce $\gamma W=W'$, and then
  $\gamma\operatorname{Pic}=\gamma(W\cap L)=W'\cap L=\operatorname{Pic}'$ — the second step is pure
  integrality of $\gamma$, and it is where the "$\otimes\mathbb R$" of the corpus's formula hides the
  lattice.
* R4: **invalid** ($\operatorname{span}c_x=V$, dimension $22$). Correct replacement: maximal
  translation-invariance subspace $=N_V$, then $W=N_V^\perp$, then integrality.
* R6: valid but vacuous (the span is the label lattice's real span, which is preserved by definition of
  the reading).

**(b) "wall set $W(c)=\{\delta\in L:\delta^2=-2,\ \delta^\perp\text{ supports a facet of }
\overline c\}$"** — `sm57_obstruction-m8.md` Theorem 3.2.

* The *definition* is intrinsic to $c$ in every reading, with one nuance in R4: there $c_x$ is not a cone
  (it is not closed under positive scaling), so "facet" must be read as "codimension-one supporting
  hyperplane of the closed convex set $\overline{c_x}$"; it is still an intrinsic notion.
* The substantive claim $W(c)\subseteq\{\pm\delta:\delta\in\Delta(X)\}$ — that facet normals are root
  classes — is **valid in every reading**, by the following argument, which I supply because the tracked
  reports assert it: in R1–R3, $\partial\overline{\mathcal K}\subseteq\bigcup_{\delta\in\Delta^+}
  (\delta^\perp\cap\overline{\mathcal K})$ by Theorem 2 and Lemma 1(3), and $\partial\overline{\mathcal K}$
  is a complete metric space; a facet $F$ is closed, hence $F=\bigcup_{\delta}(F\cap\delta^\perp)$ is a
  countable union of closed subsets, so by Baire one of them has nonempty relative interior in $F$; that
  subset is a face of $F$, and a face with nonempty relative interior equals $F$; so $F\subseteq
  \delta^\perp$ for some $\delta$, and since the supporting hyperplane of a facet is unique up to scale and
  $\delta$ is a normal, the normal is $\pm\delta$ (the normalisation $\delta^2=-2$ being immaterial: the
  class is $\pm\delta$ because both are primitive). In R4 apply $p_W$ and use the same statement in $W$,
  using (3.1). So the step survives, and it does not need local finiteness of the arrangement — only
  countability of $\Delta(X)$.
* In R6 the wall set is the label lattice's, by definition.

**(c) the facet fingerprint** (the multiset of $\lvert H\cdot\delta\rvert$ over facet normals; the route
`sm57_proof-m5.md` §7 takes for Reading C).

* Intrinsic to $c$ in every reading, hence carried to the fingerprint of $\gamma c$ by any isometry, and
  computed from $(c_b,H_b)$ *alone* — no access to $\gamma$ is needed. This makes it **coset-robust**: it
  rules out every $\gamma$ in the coset of label-preserving isometries at once, which is what the
  quantifier of (Q2) requires. (By contrast, `sm57_chamber-obstruction-m6.md` Theorem 4.4 tests $h=1$ only
  and says so.)
* It is *reading-independent*: the facet normals are the same classes in R1–R5 by (b), so the fingerprint
  does not distinguish the readings.
* Its one prerequisite is that the face where a given root vanishes be a genuine facet (codimension one),
  which the fingerprint comparison needs in order that a root with $\lvert H\cdot\delta\rvert=1$ appear in
  the fingerprint of $b_\star$'s chamber. That premise is *not needed* on the route of Theorem 7 +
  Corollary 10.1, which is the route I recommend; so the facet-dimension question, flagged in the
  incorporation review, can be dropped from the critical path.



---

## 5. The fourth bullet: exact quantifiers, six readings, and the verdict

### 5.1 The position of $H$: the clause "in which $H$ is nef and big" is a boundary condition

**Lemma 8.** On every member of the construction, with $H_b=\pi^*\mathcal O_Y(1,1)$, $\alpha_b=[D_b]$
the exceptional $(-2)$-curve, $\alpha_b$ effective:

1. $H_b^2=4>0$, $H_b\cdot\alpha_b=0$, and $H_b$ is nef and big;
2. $H_b\notin\operatorname{Amp}(X_b)$ and $H_b\notin\mathcal K(X_b)$; indeed $H_b\in\partial\mathcal K(X_b)$
   and $H_b\in\alpha_b^\perp$, which is a wall;
3. $H_b$ is *never* interior to any chamber of the root arrangement;
4. $H_b$ lies in the closure of exactly those chambers $c$ with $H_b\in\overline c$; among the chambers
   adjacent to the wall $\alpha_b^\perp$ these are at least the Kähler chamber $\mathcal K(X_b)$ and its
   reflection $s_{\alpha_b}(\mathcal K(X_b))$, and the second of these is $\alpha$-negative.

*Proof.* (1) $H_b$ is the pullback of an ample class under a finite morphism, hence nef and big, and
$H_b^2=\deg(\pi)\cdot(\mathcal O(1,1))^2 = 2\cdot 2 = 4$; $H_b\cdot D_b=\mathcal O(1,1)\cdot\pi_*[D_b]
=\mathcal O(1,1)\cdot 0=0$ because $D_b$ is contracted to the point $p$ and the cycle-theoretic
pushforward of a curve contracted to a point vanishes in $H_2$. (2) An ample class pairs strictly
positively with every effective curve class; $H_b\cdot\alpha_b=0$ with $\alpha_b\neq0$ effective, so
$H_b\notin\operatorname{Amp}$ and (Lemma 1.2(b)) $H_b\notin\mathcal K=\operatorname{int}\operatorname{Nef}$;
it is in $\partial\mathcal K\cap\alpha_b^\perp$. (3) Every interior point of every chamber of
$\mathcal P$ avoids all walls (chambers are by definition components of the complement of the walls), and
$H_b$ is on one. (4) $H_b\in\overline{\mathcal K}$ and $s_{\alpha_b}H_b=H_b$ (as $H_b\perp\alpha_b$), so
$H_b\in s_{\alpha_b}\overline{\mathcal K}=\overline{s_{\alpha_b}\mathcal K}$; and
$(x,\alpha_b)<0$ for $x\in s_{\alpha_b}\mathcal K$ by the computation of Corollary 5.2(2). $\square$

So the authored phrasing "the chamber in which $H$ is nef and big" cannot mean $H\in c$ for an open
chamber $c$; it means $H\in\overline c$ together with bigness, which is a condition on the closure
(and, as Lemma 8(4) shows, does not by itself pin $c$ among the two chambers adjacent to the wall
$\alpha^\perp$). The next lemma is what pins it.

### 5.2 Lemma 9 (the chamber is forced, not chosen; re-proof of the corpus's Lemma 1.4)

Let $\widehat Y=\operatorname{Bl}_p Y$, $e$ the exceptional curve, $h_1,h_2$ the ruling classes, and
$A_t=h_1+h_2-te$, $0<t<1$. Then

1. $A_t$ is ample on $\widehat Y$, $A_t^2=2-t^2>0$;
2. $\pi_b\colon X_b\to\widehat Y$ is finite of degree $2$, so $\omega_b:=H_b-\tfrac12\alpha_b
   =\pi_b^*A_{1/2}$ is ample on every one-node member;
3. $\omega_b\cdot\delta>0$ for every nonzero effective $\delta\in\operatorname{Pic}(X_b)$; consequently
   $\omega_b$ lies in the interior of exactly one chamber of $\mathcal P(X_b)$, and for any isometry
   $\gamma$ with $\gamma H_b=H_{b'}$, $\gamma\alpha_b=\alpha_{b'}$ one has $\gamma\omega_b=\omega_{b'}$.

*Proof.* (1) $A_t\cdot e=t>0$; for an irreducible $C\subset\widehat Y$ that is the proper transform of an
irreducible $C_Y\subset Y$ of bidegree $(a,b)$ with multiplicity $m$ at $p$, $A_t\cdot C=a+b-tm$; and
$m\le\min(a,b)\le\frac{a+b}{2}$, with $a+b\ge2m>0$, so $a+b-tm>(1-t)m>0$; for $C$ the proper transform of
a ruling not through $p$, $m=0$ and $a+b>0$; for $C=e$, $t>0$. $A_t^2=2-t^2>0$. Kleiman's criterion
(Lazarsfeld, Positivity I, Theorem 1.4.9: ample $\iff$ interior of nef $\iff$ strict positive on every
irreducible curve) gives ampleness. (2) $\pi_b$ is finite of degree $2$ (the double cover of the blow-up
branched along the strict transform $\widetilde B_b\in|-2K_{\widehat Y}|$), and the pullback of an ample
class under a finite morphism is ample. (3) $\omega_b$ is ample, and an ample class pairs strictly
positively with every nonzero effective class; interior of exactly one chamber because it is on no wall.
The last sentence: $\gamma(H_b-\tfrac12\alpha_b)=H_{b'}-\tfrac12\alpha_{b'}$. $\square$

**Consequence 9.1.** The chamber is *canonically determined* by $(H_b,\alpha_b)$ as the chamber
containing $\omega_b$; it is not an extra choice. Hence (i) the tuple of (Q2) is a function of
$(L,I_\mathrm{Co},I_\mathrm{dP},H,\alpha)$ and a Hodge-theoretic ambient, and (ii) if "chosen" is read as
a *free* choice among chambers with $H$ in the closure, then the canonical tuple is one of the admissible
choices, so "any two tuples are conjugate" (Q2) is refuted a fortiori by a refutation of the canonical
case. Reading the phrase "$\alpha$ is effective in $\mathfrak c$" as a *sign condition* (the sign of
$(x,\alpha)$ is positive on $c$) pins the chamber among the two chambers adjacent to $\alpha^\perp$, but
by Lemma 9(3) it is already pinned: no weaker or stronger pinning is needed.

### 5.3 The six readings, and the truth value of the chamber clause under each

Throughout: $X=X_b$, $X'=X_{b'}$ are one-node members (or any two members with equal $H^2$), $\gamma\in
O(L_{K3})$, and "the clause" abbreviates the chamber clause of (Q2), i.e. $\gamma\mathfrak c_b
=\mathfrak c_{b'}$.

* **R1 — nef reading** ($\mathfrak c=\operatorname{Nef}(X)$, the Mori/nef chamber, closed):
  space $\mathrm{NS}_\mathbb R$. "$H$ nef and big in $\mathfrak c$" holds literally ($H\in\operatorname{Nef}$,
  Lemma 8(1)); "$\alpha$ effective in $\mathfrak c$" cannot hold as membership ($\alpha\cdot\alpha=-2<0$),
  so it must be read as a property of the class. Clause $\Longrightarrow\gamma\operatorname{NS}_\mathbb R=
  \operatorname{NS}'_\mathbb R$ (Theorem 7) $\Longrightarrow$ Corollary 7.1. **Clause false for
  $(b_0,b_\star)$** (Corollary 10.1).
* **R2 — ample reading** ($\mathfrak c=\operatorname{Amp}(X)=\mathcal K\cap\mathrm{NS}_\mathbb R$, the
  trace of the Kähler chamber): space $\mathrm{NS}_\mathbb R$. "$H$ nef and big in $\mathfrak c$" holds in
  the closure (Lemma 8(2)); $(\alpha,x)>0$ for every $x\in\operatorname{Amp}$; the sign reading is
  satisfied and pins $\mathfrak c$ (Lemma 8(4)). Clause $\Longrightarrow$ as in R1. **Clause false.**
* **R3 — Kähler reading** ($\mathfrak c=\mathcal K(X)$, the chamber of Theorem 2 in $W$; this is the
  corpus's "arrangement cut by a member's own effective roots", `83403bc8:651`): space $W$, dimension
  $20$. Clause $\Longrightarrow\gamma W=W'$, $\gamma\operatorname{Pic}=\operatorname{Pic}'$
  (Theorem 7) $\Longrightarrow$ Corollary 7.1. **Clause false.**
* **R4 — full-$H^2$ reading** (the literal "positive/nef chamber" of (T1)): space $V$, dimension $22$,
  chamber as in Theorem 6. Clause $\Longrightarrow\gamma N_V=N_{V'}$, $\gamma W=W'$,
  $\gamma\operatorname{Pic}=\operatorname{Pic}'$ (Theorem 6(3)). **Clause false.**
* **R5 — positivity reading** ($\mathfrak c=\mathcal P(X)$, the positive cone): space $W$. "$H$ nef and
  big in $\mathfrak c$" holds in the closure; "$\alpha$ effective in $\mathfrak c$" fails as membership
  ($\alpha^2=-2<0$), so it must be read as a property of the class. Clause $\Longrightarrow\gamma W=W'$,
  i.e. "$\gamma$ matches the Hodge structure at the level of $(1,1)$", $\Longrightarrow
  \gamma\operatorname{Pic}=\operatorname{Pic}'$. **Clause false.**
* **R6 — label-own reading** (named alternative, *not* the authored text): $\mathfrak c$ is the chamber of
  the arrangement cut only by the roots lying in the lattice spanned by the labels, e.g.
  $N=\langle e_b,f_b,\alpha_b\rangle$ of rank $3$. Then $\mathfrak c$ is a function of $(H,\alpha)$ up to a
  label-preserving isometry, so the clause is implied by the labels. **Clause true.** This is the only
  reading among the six under which the clause survives; it survives because it says nothing about the
  member's own cone (as the corpus says at `83403bc8:661`).

**Verdict (the semantics check the problem asks for).** (1) The authored words "positive/nef chamber"
admit both a positivity reading (R5) and a nef/Mori reading (R1–R2); "in which $\alpha$ is effective and
$H$ is nef and big" is a boundary condition for $H$ and a sign condition for $\alpha$ (Lemma 8); and
"chosen" is either canonical (Lemma 9, in which case the author's "chosen" is a misnomer for
"determined") or free (in which case (Q2) is a fortiori false, Consequence 9.1(ii)). (2) Under every
reading in which $\mathfrak c$ is a cone determined by the member — R1, R2, R3, R4, R5 — the clause is
equivalent to a Picard/Hodge comparison and **fails** for the explicit pair $(b_0,b_\star)$ of §6.2. So
the failure recorded by the previous run is not an artefact of one semantics: it is uniform, and it is
uniform for one reason (Theorem 7), not for the reason stated at `83403bc8:661`. (3) Under R6 the clause
is true and A21 is a theorem, exactly as the corpus records; R6 must be kept as a named alternative and
must not be used as a substitute for the authored reading, because the authored text says "a member's own
effective roots" — the corpus's own gloss at `83403bc8:651`.

**Which reading is the corpus's adopted text?** `83403bc8:651` and `:661` say "the arrangement cut by a
member's own effective roots", i.e. **R3** with R2 as its trace and R1 as its closure. The tracked
reports' "Reading C" (`sm57_proof-m5.md` §4) is R3; their "Reading K" is R1/R2; their "Reading L" is R6;
`sm57_obstruction-m8.md` §1.2(A)'s literal A2 is R4. With §2–§3 these are not four different mathematical
situations but two ambient spaces with the same trace, and Theorem 7 handles them uniformly.

---

## 6. Independent re-verification of the numerical premise $\nu(b_0)=0$, $\nu(b_\star)=4$

Corollary 7.1 makes the failure of the clause for a pair follow from $\nu(b_0)\neq\nu(b_\star)$. Since
that is now load-bearing for the semantics verdict, I re-derived it without using the tracked scripts,
and I record the two computations (§6.2) and the criteria (§6.1) here.

### 6.1 Lemma 10 (which fibres of the two elliptic fibrations can contribute)

Let $b$ be a one-node member, $\pi_b\colon X_b\to\widehat Y\to Y=\mathbb P^1_x\times\mathbb P^1_y$,
$e_b=\pi_b^*h_1$, $f_b=\pi_b^*h_2$, $H_b=e_b+f_b$. Let $R\subset Y$ be a ruling not passing through $p$,
and $F=\pi_b^{-1}(R)$ the corresponding fibre.

1. $F$ is a fibre of an elliptic fibration, $F^2=0$, $F\cdot H_b=2$; $F$ is reduced (no multiple
   fibres), and $F$ is reducible if and only if the branch divisor $B_b$ meets $R$ with even
   multiplicity at each of its points. If $F$ is reducible then $F=C_++C_-$ with $C_\pm\simeq\mathbb P^1$,
   $C_\pm^2=-2$, $C_+\cdot C_-=2$, $H_b\cdot C_\pm=1$.
2. The fibre over the ruling through $p$ (i.e. over $x=0$ or $y=0$) is $D_b\cup C$ with $D_b$ the
   exceptional curve, $H_b\cdot D_b=0$, $H_b\cdot C=2$, $C\simeq\mathbb P^1$, $C^2=D_b^2=-2$,
   $C\cdot D_b=2$; it is the only reducible fibre forced by the construction.
3. If $\delta\in\operatorname{Pic}(X_b)$ satisfies $\delta^2=-2$ and $\delta\cdot H_b=1$ then $\delta$ is
   effective, and $\delta$ is a sub-divisor of a reducible fibre of one of the two fibrations, and that
   fibre has a component (or a sub-divisor) of $H_b$-degree $1$. Hence
   $$\nu(b)>0\iff \text{some ruling }R\not\ni p\text{ of }B_b\text{ has a split fibre}.$$

*Proof.* (1) For $R$ a ruling not through $p$, $\pi_b^{-1}(\sigma^{-1}R)=\{z^2=f_b|_R\}$ is the double
cover of $R\simeq\mathbb P^1$ branched at the divisor $B_b|_R$, of degree $4$; it splits iff
$B_b|_R\in 2\operatorname{Div}(R)$, i.e. iff all multiplicities are even (the scheme
$\operatorname{Spec}(\mathcal O_R\oplus\mathcal O_R(-L))$ is reduced and disconnected exactly in that
case; the local computation at a double point, $z^2=t^2\cdot u$ with $u$ a unit, gives
$(z-t\sqrt u)(z+t\sqrt u)=0$, two smooth branches). If reducible, the two components meet at the points of
$B_b\cap R$ with intersection multiplicity $1$ each — there are exactly $2$ such points when the
multiplicities are $(2,2)$, and the relation $C_+^2+C_+C_-=C_+\cdot F=0$ with $C_+C_-=2$ gives $C_\pm^2=-2$,
consistent with the adjunction formula for a smooth rational curve on a K3. $H_b\cdot C_\pm=1$ because
$\pi_{b*}[C_\pm]=[R]$ and $H_b\cdot F=2$. Reducedness: the fibre is a curve in the smooth surface $X_b$
defined by the vanishing of the function $x-c$ (respectively $y-c$), whose local equations
$z^2-t^2u$ have smooth branches; no fibre is a multiple. (2) For the ruling through $p$, the strict
transform in $\widehat Y$ meets the exceptional curve $e$ in one point and misses the two points of
$\widetilde B_b\cap e$ (for a one-node member the node of $B_b$ at $p$ has two distinct tangent
directions, neither of them the two coordinate directions when the quadratic part is nondegenerate and
not a product of coordinate forms — verified for the two members used: the quadratic parts are
$2x^2+7xy-5y^2$ and $3x^2-28xy+13y^2$, neither divisible by $x$ or $y$); so $\widetilde B_b$ meets the
strict transform in $2$ points and the preimage of the strict transform is an irreducible rational curve
$C$, while $\pi_b^{-1}(e)=D_b\simeq\mathbb P^1$ with $D_b\cdot C=2\cdot(e\cdot R_{\mathrm{str}})=2$;
$H_b\cdot D_b=0$ and $H_b\cdot C=2$ as in the proof of Lemma 8. (3) Riemann–Roch gives
$\chi(\mathcal O(\delta))=1$ and $h^0(\delta)+h^0(-\delta)\ge1$, so $\pm\delta$ is effective; since $H_b$
is nef and $\delta\cdot H_b=1>0$, $\delta$ is the effective one. Put $k=\delta\cdot e_b\ge0$,
$m=\delta\cdot f_b\ge0$; then $k+m=\delta\cdot H_b=1$, so $(k,m)\in\{(1,0),(0,1)\}$. If $k=0$ then
$\delta$ is contracted by the $x$-fibration, hence lies in a fibre $F$; since $\delta\cdot H_b=1<2=F\cdot H_b$,
$\delta\neq F$ and $F$ is reducible with $\delta$ of degree $1$; symmetrically for $m=0$ with the
$y$-fibration. Together with (1) and (2): the only fibres with a degree-$1$ sub-divisor are the split
ones over rulings away from $p$. $\square$

### 6.2 The two computations (mine; log beside this file)

For $b_0$ and $b_\star$ the polynomials are those of `sm57_proof-m5.md` §6; I recomputed everything from
them. Everything below is reproduced by `verify_semantics.py` in this directory, whose output is
`verify_semantics-run.txt`; the intermediate scripts `nucheck.py`, `i2check.py`, `disc.py` reproduce the
same numbers and are kept beside it.

* **Lattice arithmetic** (the Gram matrix of `sm57_proof-m5.md` §1.1, $G=\begin{pmatrix}0&2&0\\2&0&0\\
  0&0&-2\end{pmatrix}$ in the basis $e_b,f_b,\alpha_b$): $H_b^2=4$, $H_b\cdot\alpha_b=0$,
  $(e_b-\alpha_b)^2=(f_b-\alpha_b)^2=-2$, $(e_b-\alpha_b)\cdot H_b=(f_b-\alpha_b)\cdot H_b=2$,
  $\omega_b^2=\tfrac72$, $\omega_b\cdot H_b=4$, $\omega_b\cdot\alpha_b=2$; and
  $\omega_b\cdot\delta>0$ for all $15$ effective $(-2)$-classes of $\langle e_b,f_b,\alpha_b\rangle$ with
  coefficients of absolute value $\le3$ (the proof of Lemma 9(3) gives it for all).
  *Audit note:* `sm57_proof-m5.md` Remark 2.3 says $L_{1/2}$ has "square $7/4$"; on $X_b$ the square is
  $\deg\pi\cdot A_{1/2}^2=2\cdot\frac74=\frac72$, and $7/4$ is $A_{1/2}^2$ on $\widehat Y$. No argument
  uses the number, but the tracked value is on the wrong surface.
* **Node direction.** $f_b(p)=0$ with nondegenerate quadratic parts $2x^2+7xy-5y^2$ (discriminant $89$)
  and $3x^2-28xy+13y^2$ (discriminant $628$); the values on the two coordinate directions are
  $(-5,2)$ and $(13,3)$, both nonzero, so no branch of the node at $p$ is tangent to either ruling — the
  hypothesis used in Lemma 10(2).

* **Split-fibre criterion made effective.** For the fibration with fibre variable $y$ and base variable
  $x$, write $f=\sum_{i=0}^4a_i(x)y^i$; the fibre over $x=c$ is a perfect square (i.e. split, by Lemma 10(1))
  iff $f(c,\cdot)$ is, and that is the pair of polynomial conditions
  $$E_1=a_0a_3^2-a_4a_1^2,\qquad E_2=4a_4a_3a_2-a_3^3-8a_4^2a_1$$
  vanishing at $c$ (with the cases $a_4(c)=0$ or $a_3(c)=0$ handled separately; both are checked
  explicitly and contribute no split fibre here).
* **$b_0$:** $\operatorname{disc}_y f_0=x^2\cdot q_{22}(x)$ with $q_{22}$ squarefree of degree $22$, and
  $\operatorname{disc}_x f_0=y^2\cdot r_{22}(y)$ squarefree of degree $22$; $\gcd(E_1,E_2)=x$ in the
  $x$-fibration and $=y$ in the $y$-fibration, and $x=0$ (resp. $y=0$) is spurious because $a_3(0)=0$ and
  $f_0(0,y)=-y^2(y^2+5)$ is not a square. So the only reducible fibres are the two forced ones, whose
  components have degrees $0$ and $2$ (Lemma 10(2)), and **$\nu(b_0)=0$**.
* **$b_\star$:** $\operatorname{disc}_y f_\star=(x-1)^2x^2(x+1)^2\cdot s_{18}(x)$ with $s_{18}$ squarefree
  (degree $18$), and $\operatorname{disc}_x f_\star=y^2\cdot t_{22}(y)$ squarefree;
  $\gcd(E_1,E_2)=x(x-1)(x+1)$ in the $x$-fibration and $=y$ in the $y$-fibration. Moreover
  $f_\star(1,y)=(y-1)^2(y-3)^2$ and $f_\star(-1,y)=(y+1)^2(y+3)^2$, so the rulings $x=\pm1$ are tangent to
  $B_\star$ at two points each and split (formulae of Lemma 10(1): $C_\pm\simeq\mathbb P^1$,
  $C_\pm^2=-2$, $C_\pm\cdot H_\star=1$). The $18$ remaining singular fibres have simple discriminant roots
  and are irreducible nodal. Hence **$\nu(b_\star)=4$** (the two components of each of the two split
  fibres; a multiple $2C$ of a component has square $-8$ and does not contribute).
  This sharpens the tracked "$\nu\ge2$" to an equality, and confirms the tracked "$=0$".

### 6.3 Why the two values can differ without contradicting deformation theory

They can, because **parallel transport in the family is not a Hodge isometry** (§4.1): the abstract set
$\{\delta\in L:\delta^2=-2,\ (\delta,H)=1\}$ is the same for the two members (the lattice and $H$ are
transported), but which of its elements are *algebraic* is decided by the period. Precisely,
$\nu(b)=\#\{\delta\in L:\delta^2=-2,\ (\delta,H)=1,\ \delta\in H^{1,1}(X_b)\}$, so $\nu$ jumps on
Noether–Lefschetz loci — it is the Noether–Lefschetz condition of the classes $\delta$ with
$(\delta,H)=1$. This is *consistent* with `thm:a21-labels` and with every tracked statement; and it is why
the chamber clause, which by Corollary 7.1 forces $\gamma\operatorname{Pic}(X_b)=\operatorname{Pic}(X_{b'})$,
cannot be satisfied. No tracked document claims otherwise (checked, §4.1).

### 6.4 Corollary 10.1 (the failure, uniformly in all five readings)

Let $b_0,b_\star$ be the two members of §6.2, with $\nu(b_0)=0$ and $\nu(b_\star)=4$. Then there is no
$\gamma\in O(L_{K3})$ with $\gamma H_{b_0}=H_{b_\star}$, $\gamma\alpha_{b_0}=\alpha_{b_\star}$ and
$\gamma\mathfrak c_{b_0}=\mathfrak c_{b_\star}$ in any of the readings R1, R2, R3, R4, R5. Consequently the
chamber clause of (Q2) is false for the pair $(b_0,b_\star)$ in each of those five readings; and if
"chosen" is read as a free choice (Consequence 9.1), (Q2) is false as well.

*Proof.* Suppose $\gamma\mathfrak c_{b_0}=\mathfrak c_{b_\star}$. By Theorem 7,
$\gamma\operatorname{Pic}(X_{b_0})=\operatorname{Pic}(X_{b_\star})$, and $\gamma$ preserves squares and
the pairing with $\gamma H_{b_0}=H_{b_\star}$, so it bijects the counting set of Corollary 7.1, giving
$\nu(b_0)=\nu(b_\star)$, i.e. $0=4$ — contradiction. $\square$

This proves the failure without the facet-fingerprint argument of `sm57_proof-m5.md` §7 (Reading C), and
therefore without the facet-dimension premise flagged in the incorporation review: Theorem 7's R3 case
needs only the span of the Kähler cone, not the facet structure of its closure. That argument is still
correct as an independent route, and its facet-normal step is provable (each facet of
$\overline{\mathcal K}$ lies in some $\delta^\perp$ with $\delta\in\Delta^+$: the boundary of
$\overline{\mathcal K}$ is covered by the countably many traces $\overline{\mathcal K}\cap\delta^\perp$ by
Lemma 8/Theorem 2, and Baire applied to the complete convex facet gives one $\delta^\perp$ containing it);
but it is no longer needed.

---

## 7. What this section establishes, and the exact open points

### 7.1 Status table

| item | status |
|---|---|
| Kähler cone in $H^{1,1}(X,\mathbb R)$, dim $20$, signature $(1,19)$ | proved, Lemma 1 |
| $\operatorname{Amp}=\mathcal K\cap\operatorname{Pic}\otimes\mathbb R$, dim $\rho$ | proved, Lemma 1 |
| $\mathcal K=\operatorname{int}\operatorname{Nef}$ | proved, Lemma 1 |
| $\mathcal K$ is a chamber of the effective-root arrangement | cited: BHPV Cor. VIII.3.9 as quoted verbatim in Huybrechts (Handbook of Moduli) §2.1 |
| $\{x^2>0\}$ connected in signature $(3,19)$ | proved, Lemma 3 |
| chamber = trace $\times\ N$; trace is a bijection (W reading) | proved, Theorem 5 |
| trace of the Kähler chamber $=\operatorname{Amp}$, not $\mathcal K$; other traces $=s_\delta(\operatorname{Amp})\neq\operatorname{Amp}$ | proved, Corollary 5.2 |
| $V$-chamber not a product, trace still $\operatorname{Amp}$, translation direction $N_V$ | proved, Theorem 6 |
| chamber equality $\Longrightarrow$ Picard identification, in all five readings | proved, Theorem 7 |
| chamber is canonically pinned by $(H,\alpha)$ via $\omega=H-\tfrac12\alpha$ ample | proved, Lemma 9 |
| $H$ is on a wall, never interior; "nef and big in $c$" is a boundary condition | proved, Lemma 8 |
| $\nu(b_0)=0$, $\nu(b_\star)=4$ | proved here from the polynomials, §6.1–6.2, logs beside this file |
| clause false in R1–R5, true in R6 | proved, Corollary 10.1 + §5.3 |

### 7.2 Named open points, and what they are not

1. **An authoring question, not a mathematical one.** Whether the authored "positive/nef chamber" is
   meant as R3 (the member's own effective roots, the corpus's gloss) or as R6 (label-own) is not decidable
   from `a145cea4a5:626`; this section proves that the *mathematical* content of the clause differs in the
   two readings (false in R3, R4, R5, R1, R2; true in R6), so the authoring choice is a real one. It is
   recorded here as the exact boundary, not resolved.
2. **Two citation levels I did not verify myself.** (i) BHPV Corollary VIII.3.9 is cited as quoted in
   Huybrechts §2.1; I did not read BHPV. (ii) Kleiman's criterion is cited at the level of Lazarsfeld,
   Positivity I, Theorem 1.4.9 (and the standard statement "ample $=$ interior of nef"). Everything else
   in this section is proved here.
3. **Not done, and named so that nobody repeats it.** This section does not touch defect 2 (the
   contraction/facet chain of `sm57_proof-m5.md` addendum B) or defect 3 (the node/infinity/general-fibre
   audit), except that §6.1 re-proves the forced fibre's degree split $(0,2)$ used by both; and it does not
   re-verify m8's Theorem 3.3 (rank of the period map) or the Barcy–Baire step "$\operatorname{Pic}=S_\mathrm{Co}$
   for a very general member", which it only quotes as the corpus's.

---

## Referee reclamation (third cycle): the two steps the incorporation review flagged, resolved

### R1. The chamber is not literally a product; the trace bijection survives with its actual shape

The document's Theorem 5(2) asserted that with $p\colon W\to\mathrm{NS}_\mathbb R$ the projection and
$c$ a chamber in $\mathcal P$, "in fact $p^{-1}(c_{\mathrm{alg}})\subseteq\mathcal P$, so literally
$c = c_{\mathrm{alg}}\times N$". That argument fails: for $u\in c_{\mathrm{alg}}$ and
$n\in N$ one has $(u+n)^2 = u^2+n^2$, and $n^2 \le 0$ does not bound $n^2$ below, so $(u+n)^2<0$
for $n$ large — $u+n$ can leave the positive cone. The corrected shape is
$$c \ =\\ \bigl\{\,(u,n)\in\mathrm{NS}_\mathbb R\perp N:\ u\in c_{\mathrm{alg}},\ u^2+n^2>0\,\bigr\},$$
i.e. an open ball fibre over each point of the trace. With that formula, the document's *bijection*
between chambers of $\mathcal P$ and chambers of $\mathcal P_{\mathrm{alg}}$ still holds (each fibre is
connected, the trace map is surjective with its truncation, and maximality follows by projecting any
extension path). The root-walls depend only on the trace, as advertised; the positive-square condition
is supplied by that formula, not by the walls.

### R2. In the full $V = H^2(X,\mathbb R)$ of signature $(3,19)$ the "translation-invariance subspace = $N_V$" detector is unsupported; the R4 forcing row is sustained by the census, not by that detector

In signature $(3,19)$ the domain $D = \{x^2>0\}$ is connected and $N_V = \mathrm{NS}^{\perp V}$ has
signature $(2, 20-\rho)$, which contains *negative-square* directions, and $x + t n$ exits $D$ across the
quadric $\{x^2 = 0\}$ (not across a root wall) for any $n$ with $n^2 < 0$ and $t$ large. Hence the
document's claimed chamber "maximal translation-invariance subspace" is not $N_V$ as stated: negative-norm
directions of $N_V$ are not globally translation-invariant. The forcing conclusion
"$\gamma(c) = c'$ forces $\gamma\mathrm{Pic} = \gamma\mathrm{Pic}'$" for the $V$-chamber (R4)
nevertheless stands, by the accepted census argument of `sm00_chamber-negative-half.md` (Lemma 8(iii)
there: facet normals are $\pm$ effective roots, facet census is isometry-invariant, and the degree-$1$
census differs across the certified pair), whose ambient space is already the full $V$ — its facet
construction is ambient-signature-free. The remaining R4 content of this document (the trace chamber,
and the clause-false-in-R1–R5/truth-in-R6 table) is unchanged.

*Verification note on the ambient-signature assumption used elsewhere.* The hyperbolic-distance formula
$\sinh d([x],[\delta^\perp]) = |x\cdot\delta|/\sqrt{x^2(-\delta^2)}$ with $\delta^2 = -2$ is used in the
accepted negative-half document on **integral** $y$ of square $24 > 0$: it is signature-independent
(a totally geodesic $(1,1)$ reduction), and the ball of radius $\operatorname{arcsinh}(1/\sqrt{48})$.
Applying that formula to *non-integral* centres or beyond the fixed $y$ would re-open the flagged step;
its current use in the corpus is exactly integral-centre $y$, and it is what settles the wall-free ball.
