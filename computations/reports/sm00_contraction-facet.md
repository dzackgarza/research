# Defect 2, corrected: the contraction–facet chain on the one-node K3 members

Member `m4`, swarm `smw0b9kmo`, direction `d3`.  The repo is
`/workspace/nucleus/work/projects/p-9fcb4ed7f4b64e008de2ee29a7197bf4/repo`, cited by
`path:line`, not modified.  Charter evidence state `main@83403bc8`; the tracked files read
here (`computations/reports/sm57_proof-m5.md`, `computations/reports/sm57_obstruction-m8.md`,
`writing/coble/heegner-report/coble-heegner-research-report.md`) are at `HEAD = cd72f71ec3`,
which differs from `83403bc8` only in the two passages named in its commit message (the
$T_{En}$ root paragraph and the node-fibre line), neither of which occurs in the chain
corrected here (§8).

---

## 0. Verdict

The tracked chain — `sm57_proof-m5.md`, *Referee addendum B*, the paragraph beginning
"Let $\delta$ be an effective class of square $-2$ whose corresponding curve is the only
contracted curve of a contraction $\sigma\colon\widehat X\to X'$ of ADE type" and ending
"…no label-preserving isometry — not merely the transport one — carries one chamber onto the
other" — is **correctable, and is corrected below**.  Three things are wrong or missing in it,
and one worry raised in the incorporation review is *not* a problem but a different problem
sits next to it.

1. **The contraction with a projective target and an integral ample divisor is a theorem.**
   Not Grauert plus an algebraization step: *Artin's contractibility criterion* for curves on
   projective surfaces gives, in one stroke, the morphism, the normality **and the
   projectivity** of the target.  The hypotheses are three lines to check here
   (§2, Theorem B).  Consequently the analytic (Grauert) contraction of the same curve is
   projective, by uniqueness of contractions (§3, B4 and B6) — the "is the contraction projective?"
   question of the review closes affirmatively, and no analytic input is needed.

2. **"$y\cdot\delta'\ge 1$ for every effective $\delta'$ implies a wall-free neighbourhood"
   is true here, but the reason matters and the review was right that it is not formal.**
   The review's objection — infinitely many strict half-spaces can intersect in a set with
   empty interior — is *correct as stated for arbitrary normals*, and I give the exact
   counterexample (Remark A3).  What saves the K3 case is that all wall normals are
   $(-2)$-classes: their length is *fixed* ($|\delta|^2=-2$), and every root of bounded
   $y$-degree is one of *finitely many* (Lemma A1).  Together these give an explicit
   $\varepsilon>0$ with $x\cdot\delta>0$ for all $x$ in the ball of radius $\varepsilon$
   about $y$ and all effective roots $\delta$ except $\pm C_+$ (Corollary A2).  So the
   tracked sentence is repairable rather than merely open; but it must cite Lemma A1, not
   Cauchy–Schwarz, and the naive estimate $|v\cdot\delta|\le|v|\,|\delta|$ is *false* in
   indefinite signature — that is exactly where a careless version of the tracked sentence
   would break.

3. **"No other wall near $y$, hence a facet" needs one more input, and it is not the same
   input in the two readings of the fourth bullet.**  The arrangement is not the nef cone.
   In Reading C (chamber of the arrangement in the positive cone of $H^2$) the conclusion is
   *definitional* once the ball of (2) is in hand, and uses no cone theorem at all.  In
   Reading K (nef cone inside $\operatorname{Pic}_{\mathbb R}$ or $H^{1,1}_{\mathbb R}$)
   the conclusion needs the K3 cone theorem, i.e. **BHPV, Corollary VIII.3.9**
   (stated and sourced in §4).  Both are supplied; the tracked text conflates them.

4. **Space and dimension bookkeeping is wrong in the tracked addendum.**  It says the face
   has "full hyperplane dimension $21$ in the stated cone", "$\operatorname{Pic}^\perp$ has
   signature $(2,19-\rho)$" and speaks of "a facet of the nef cone in $\operatorname{Pic}\otimes\mathbb R$".
   The correct numbers, with the space each belongs to, are in the table of §5.3:
   facets are $21$-dimensional in $H^2_{\mathbb R}$ (dim $22$), $19$-dimensional in
   $H^{1,1}_{\mathbb R}$ (dim $20$), and $(\rho-1)$-dimensional in $\operatorname{Pic}_{\mathbb R}$
   (dim $\rho$); and $\operatorname{Pic}^\perp$ has signature $(2,20-\rho)$, not $(2,19-\rho)$.
   "Dimension $21$" and "$\operatorname{Pic}\otimes\mathbb R$" cannot be combined.

The end result is **Theorem C** (§4): for every effective $(-2)$-class $\delta$ on a smooth
projective K3 over $\mathbb C$ **that is represented by a smooth rational curve** — in
particular for the $C_+$ of the witnesses — the hyperplane $\delta^\perp$ supports a facet of
the closure of the chamber containing the Kähler cone, in each of the three spaces, and the
facet's normal is $\pm\delta$.  (For a *reducible* effective $(-2)$-class the same method gives
only the face cut by the whole configuration, of codimension equal to the number of its
components; that case is not needed here and is not claimed.)  In particular the facet that `sm57_proof-m5.md` §7 (Reading C) uses for
$b_\star$ is unconditional, and needs *no* knowledge of the member's Picard lattice — so the
finite-root-bound route offered by the charter ("reduce to an explicit finite verification if
you can bound the effective roots of the witness") is not merely unnecessary, it is
**unavailable**: $\operatorname{Pic}(\widehat X_{b})$ is unknown beyond $\rho\ge 11$, so
$\Delta_b$ cannot be enumerated (§7.3).

---

## 1. Setting and standing hypotheses

$(H_1)$ $X$ is a smooth projective K3 surface over $\mathbb C$.  Hence $K_X=0$,
$H^2(X,\mathbb Z)=L_{K3}=3U\oplus 2E_8(-1)$, signature $(3,19)$, $b_2=22$,
$h^{2,0}=1$, $\dim_{\mathbb R}H^{1,1}_{\mathbb R}=20$, and the Hodge index theorem gives the
intersection form on $\operatorname{Pic}(X)$ signature $(1,\rho-1)$ with $\rho=\rho(X)\le 20$.

$(H_2)$ $C=C_+\subset X$ is a smooth rational curve with $C^2=-2$; $[C]\in\operatorname{Pic}(X)$.

Notation.  $\Delta_b=\{\delta\in\operatorname{Pic}(X):\delta^2=-2,\ \delta \text{ effective}\}$
(the corpus' set; the subscript is m5's and is kept).  $P\subset H^2_{\mathbb R}(X)$ is the
component of $\{x:x^2>0\}$ containing the Kähler classes, $\overline P$ its closure;
$P_{1,1}=P\cap H^{1,1}_{\mathbb R}$ and $P_{\mathrm{Pic}}=P\cap\operatorname{Pic}_{\mathbb R}$
are the corresponding positive cones (signature $(1,19)$ resp. $(1,\rho-1)$).  For $H$ nef and big, $K_X$ is the Kähler cone and $\operatorname{Nef}(X)=\overline{K_X}$.

Three readings of the fourth bullet are in use in the corpus and are kept distinct (m5 §4,
m8 §1.2): **Reading K** $c=\operatorname{Nef}(X)=$ closure of $K_X$, a cone in
$\operatorname{Pic}_{\mathbb R}$; **Reading C** $c=$ the chamber of
$P\setminus\bigcup_{\delta\in\Delta_b}\delta^\perp$ containing the Kähler classes (m8's
Reading A2), a cone in $H^2_{\mathbb R}$; **Reading A1** the same chamber regarded inside
$\operatorname{Pic}_{\mathbb R}$ (or $H^{1,1}_{\mathbb R}$).  This document proves the facet
statement in all three, with the input each one needs made explicit.  Which reading the
authored bullet at `writing/coble/heegner-report/coble-heegner-research-report.md:601-638`
("the chosen positive/nef chamber in which $\alpha$ is effective and $H$ is nef and big")
*means* is defect 1's business, not mine; §5.4 records only what the facet theorem changes
about it.

---

## 2. Lemma A: root finiteness, and the wall-free ball

**Lemma A1 (root finiteness).**  Let $(\Lambda,\cdot)$ be a free $\mathbb Z$-module with a
nondegenerate symmetric form of signature $(1,\rho-1)$, $\rho\ge 1$, and let
$y\in\Lambda_{\mathbb R}$ with $y^2>0$.  For every $K\in\mathbb R$ the set
$$\{\delta\in\Lambda:\ \delta^2=-2,\ 0<y\cdot\delta\le K\}$$
is finite.

*Proof.*  $E:=y^\perp$ is a negative definite real inner product space of dimension $\rho-1$,
and $p(v):=v-\frac{y\cdot v}{y^2}y$ is the orthogonal projection onto $E$.  Then
$\bar\Lambda:=p(\Lambda)$ is a lattice in $E$ (the image of the lattice $\Lambda$ under the
quotient map $V\to V/\mathbb Ry\cong E$, $V=\Lambda_{\mathbb R}$; if $\Lambda\cap\mathbb Ry\ne0$
the projection has a kernel, which is harmless: $p(\delta)=p(\delta')$ and $y\cdot\delta=y\cdot\delta'$
force $\delta=\delta'$).  For $\delta$ in the displayed set,
$$\delta^2=p(\delta)^2+\frac{(y\cdot\delta)^2}{y^2}\quad\Longrightarrow\quad
p(\delta)^2=-2-\frac{(y\cdot\delta)^2}{y^2}\in\Bigl[-2-\frac{K^2}{y^2},\,-2\Bigr].$$
On the negative definite space $E$ the set $\{v\in\bar\Lambda:\ -2-K^2/y^2\le v^2<0\}$ is
bounded, hence finite by discreteness.  For fixed $v=p(\delta)$ the equation $\delta^2=-2$
determines $(y\cdot\delta)^2$, and $y\cdot\delta>0$ picks the sign, so
$\delta=v+\frac{y\cdot\delta}{y^2}y$ is determined.  $\square$

**Corollary A2 (the wall-free ball, quantitative form).**  Fix a Euclidean norm $|\cdot|$ on
$\Lambda_{\mathbb R}$, and let $y\in\Lambda_{\mathbb R}$, $y^2>0$, satisfy
$y\cdot\delta\ge 1$ for all $\delta\in\Delta$, where $\Delta\subseteq\{\delta\in\Lambda:\delta^2=-2\}$
is any set of roots.  Then there is $\varepsilon>0$, depending on $y$ and the norm only, such
that
$$|x-y|<\varepsilon\ \text{and}\ \delta\in\Delta
\quad\Longrightarrow\quad x\cdot\delta>0 .$$
In particular the open ball of radius $\varepsilon$ about $y$ meets no wall $\delta^\perp$,
$\delta\in\Delta$, other than those with $y\cdot\delta=0$.

*Proof.*  Write $\delta=ay+p(\delta)$ with $a=(y\cdot\delta)/y^2$.  Since the form is negative
definite on $E$, the Euclidean norm and $\sqrt{|q|}$ are comparable on $E$: there is $c_1>0$
with $|p(\delta)|\le c_1\sqrt{-p(\delta)^2}$.  By Lemma A1's computation,
$|p(\delta)|\le c_1\sqrt{2+(y\cdot\delta)^2/y^2}\le c_1(\sqrt2+y\cdot\delta/\sqrt{y^2})$, so
with $C:=2\max\{|y|/y^2,\ c_1\sqrt2,\ c_1/\sqrt{y^2}\}$,
$$|\delta|\le |a|\,|y|+|p(\delta)|\le C\,(1+y\cdot\delta).$$
Then for $|x-y|<\varepsilon$,
$x\cdot\delta\ \ge\ y\cdot\delta-\varepsilon|\delta|\ \ge\
y\cdot\delta-\varepsilon C(1+y\cdot\delta)\ \ge\ \tfrac34 y\cdot\delta-\tfrac14\ \ge\ \tfrac12$,
the last step because $y\cdot\delta\ge1$, once $\varepsilon C\le1/4$, i.e.
$\varepsilon:=1/(4C)$.  $\square$

**Remark A3 (the review's objection is correct for unbounded normals — the two examples).**

(i) *Pairing bound does not bound a neighbourhood.*  In $\mathbb R^2$ with classes
$\delta_k:=(-k,1)$, $k\ge1$, the point $y:=(0,1)$ satisfies $y\cdot\delta_k=1\ge1$ for every
$k$, while
$$\bigcap_{k\ge1}\{x:x\cdot\delta_k\ge0\}=\{(0,x_2):x_2\ge0\},$$
a ray, of empty interior.  So "$y\cdot\delta_k\ge1$ for all $k$" does **not** imply that a
ball about $y$ lies in the intersection of the half-spaces.  What fails is that
$|\delta_k|\to\infty$: the normals are not of bounded length, which is hypothesis (L) below.
In the K3 case (L) holds *exactly*: every wall normal is a root, and all roots satisfy
$|\delta|^2=-2$.  Lemma A1 + Corollary A2 is the replacement for the missing "local
finiteness of the arrangement".  Note also that the estimate used in a careless proof,
$|v\cdot\delta|\le|v|\,|\delta|$, is Cauchy–Schwarz and is **false** for an indefinite form;
Corollary A2 avoids it by using $y^2>0$ and the comparability of norms on $y^\perp$.

(ii) *A facet of an intersection of half-spaces need not lie in one of the walls.*
$\{x_1\ge0\}\cap\bigcap_{k\ge1}\{x_1+x_2/k\ge0\}=\{x_1\ge0,\ x_1+x_2\ge0\}$ is a convex cone
whose facet $\mathbb R_{\ge0}(0,1)$ is contained in no wall $x_1+x_2/k=0$.  Hence "the facet
normals are roots" is a genuine lemma, proved below (Lemma D), and is not a consequence of
"walls are the only constraints".

**Remark A4 (the three inputs of the facet chain, named).**
(L) *bounded normal length*: every wall normal is a $(-2)$-class, so $|\delta|^2=-2$;
(V) *a point of positive square with a uniform pairing bound*: $y^2>0$, $y\cdot\delta\ge1$ for
$\delta\in\Delta\setminus\{\pm C\}$, $y\cdot C=0$ — supplied by Theorem B;
(D) *the wall set is the constraint set*: either by definition of the chamber (Reading C), or
by the K3 cone theorem (Reading K, §4.2).
(L) and (V) give Corollary A2; (D) converts the ball into the facet.

---

## 3. Theorem B: the contraction, its projectivity, and the ample class

**Theorem B.**  Let $X$, $C=C_+$ satisfy $(H_1)$–$(H_2)$.  Then:
1. there is a morphism $\pi\colon X\to X'$ onto a **normal projective** surface $X'$,
   $\pi(C)$ a point, $\pi$ an isomorphism $X\setminus C\to X'\setminus\{\pi(C)\}$, and the
   pair $(X',\pi)$ is unique up to unique isomorphism;
2. for every ample line bundle $H'$ on $X'$ the class $y:=\pi^*H'\in\operatorname{Pic}(X)$
   satisfies $y^2>0$, $y\cdot C=0$, $y\cdot D\ge0$ for every curve $D$, and
   $$y\cdot\delta\ \ge\ 1\qquad\text{for every effective }\delta\in\operatorname{Pic}(X)
   \text{ with }\ \pi_*\delta\ne0 .$$

*Proof.*  **1. Existence, normality, projectivity.**  We use Artin's contractibility
criterion in the following form.

> **Artin (1962), Theorem 2.3.**  *Let $S$ be a normal projective surface and $C\subset S$ a
> connected curve such that $S$ is nonsingular along $C$, with irreducible components
> $C_i$.  Then $C$ is contractible — there is a morphism $\pi\colon S\to S'$ onto a **normal
> projective** surface $S'$ with $\pi(C)$ a point and $\pi$ an isomorphism over
> $S'\setminus\pi(C)$ — if and only if (i) the matrix $(C_i\cdot C_j)$ is negative definite
> and (ii) every effective cycle $Z>0$ supported on $C$ has $p_a(Z)\le0$.*
> (M. Artin, *Some numerical criteria for contractability of curves on algebraic surfaces*,
> Amer. J. Math. **84** (1962), 485–496, Theorem 2.3, p. 491.)

Hypotheses for $S=X$, $C=C_+$: $X$ is smooth projective, hence normal and projective
$(H_1)$; $C$ is irreducible, hence connected, and $X$ is smooth along it; (i) is the
$1\times1$ matrix $(-2)$, negative definite by $(H_2)$; (ii) effective cycles supported on
$C$ are $Z=mC$, $m\ge1$, and by adjunction on a surface with $K_X=0$,
$$p_a(mC)=1+\frac{(mC)^2+mC\cdot K_X}{2}=1+\frac{-2m^2}{2}=1-m^2\le0 .$$
So the criterion applies and gives $\pi\colon X\to X'$ with $X'$ normal projective.  This
disposes of the review's question (a) in the affirmative: **the contraction of a single
$(-2)$-curve on a smooth projective K3 is projective**, and the ample divisor $A'$ the chain
needs exists because $X'$ is projective (take $H'$ very ample, integral).

**2. The pullback class.**  $\pi$ is birational (it is an isomorphism over a dense open set),
so $(\pi^*H')^2=H'^2>0$ and $y^2>0$.  For a curve $D\subset X$: $y\cdot D=H'\cdot\pi_*D\ge0$
(the pushforward of an effective cycle is an effective cycle, and an ample class is
nonnegative on effective cycles), and $y\cdot C=H'\cdot\pi_*C=0$.

**3. The pairing bound.**  Let $\delta$ be effective with $\pi_*\delta\ne0$.  Then
$\pi_*\delta=\sum n_i\Gamma_i$ with $n_i\ge1$ and $\Gamma_i\subset X'$ irreducible curves, so
$$y\cdot\delta=H'\cdot\pi_*\delta=\sum_i n_i\,(H'\cdot\Gamma_i)\ \ge\ \sum_i n_i\ \ge\ 1,$$
using $H'$ ample *and integral*: $H'\cdot\Gamma_i$ is a positive integer.  $\square$

**B4 (uniqueness of the contraction).**  If $\pi_i\colon X\to Y_i$, $i=1,2$, both
contract $C$ and are isomorphisms outside $C$, then both have connected fibres, so
$\pi_{i*}\mathcal O_X=\mathcal O_{Y_i}$ (Zariski's connectedness theorem / Stein
factorization), and $Y_1\cong Y_2$ canonically.

**B6 (answer to the review's question (a), literally).**  *Yes, the analytic contraction of a
single $(-2)$-curve on a projective K3 is always projective.*  Grauert's theorem
(H. Grauert, *Über Modifikationen und exzeptionelle analytische Mengen*, Math. Ann. **146**
(1962), 331–368, §5–6: a connected compact analytic subset of a complex surface with negative
definite intersection matrix is contractible to a point, the contraction being an isomorphism
outside it) applies to $C$, and by B4 its target is canonically
isomorphic to the projective surface $X'$ of Theorem B1.  So no algebraization theorem is
needed for this step at all; the *projective* contraction is the same contraction.  (A third,
independent route to $X'$: the base point free theorem, Kollár–Mori, *Birational Geometry of
Algebraic Varieties*, Theorem 3.3, applied to the pair $(X,0)$ — klt since $X$ is smooth —
and the divisor $D:=2A+(A\cdot C)\,C$ for an ample $A$: $D$ is Cartier, integral,
$D\cdot C=0$, $D\cdot E>0$ for every other curve $E$, $D^2=4A^2+2(A\cdot C)^2>0$; so $D$ is
nef and big and $D-K_X=D$ is nef and big, and $|mD|$ is base point free for $m\gg0$, the
associated morphism contracting exactly the curves $D^\perp$ — i.e. exactly $C$.  This is a
cross-check, not used.)

**Remark B5 (the identity behind "$y=\sigma^*A'$").**  For any ample $A$ on $X$ one has
$$y=A+\frac{A\cdot C}{2}\,C\qquad\text{in }\operatorname{Pic}(X)_{\mathbb Q},$$
indeed $y\cdot C=A\cdot C+\frac{A\cdot C}{2}C^2=0$, and $y^2=A^2+\frac{(A\cdot C)^2}{2}>0$;
the right-hand side is $\pi^*$ of the class $\pi_*(A+\frac{A\cdot C}{2}C)$, which is where the
ample class on $X'$ comes from.  `verify_defect2.py` checks the arithmetic on the explicit
lattice of `sm57_proof-m5.md` §1.1 for $A=H-t\alpha$, $t=1/2,3/4$: $y\cdot C=0$ and
$y^2=4$ resp. $27/8>0$.

---

## 4. Theorem C: $\delta^\perp$ supports a facet, in each of the three spaces

**Theorem C.**  Assume $(H_1)$, $(H_2)$, let $\Delta=\Delta_b$, and let $\pi\colon X\to X'$,
$y=\pi^*H'$ be as in Theorem B.  Let $c$ be the chamber of
$P\setminus\bigcup_{\delta\in\Delta}\delta^\perp$ containing the Kähler cone, $\overline c$
its closure, $\overline P$ the closure of $P$.  Then:

* **(C1) Reading C (full space $H^2_{\mathbb R}$).**  $c=\{x\in P:x\cdot\delta>0\ \forall\delta\in\Delta\}$,
  $\overline c=\{x\in\overline P:x\cdot\delta\ge0\ \forall\delta\in\Delta\}$,
  $y\in\overline c$, and
  $F:=\overline c\cap C^\perp$ *is a facet of the closed convex cone $\overline c$*, of
  dimension $21=\dim H^2_{\mathbb R}-1$, supported by $C^\perp$; moreover $y$ lies in its
  relative interior.  No cone theorem is used; only Theorem B and Corollary A2.
* **(C2) Reading K (nef cone, $\operatorname{Pic}_{\mathbb R}$).**  With
  $\operatorname{Nef}(X)=\overline K_X$, the set $\operatorname{Nef}(X)\cap C^\perp$ is a facet
  of the nef cone of dimension $\rho-1$.  Two proofs are given: one through
  **BHPV, Corollary VIII.3.9**, one through the class group of the contraction (Lemma C3), so
  the statement does not depend on either input alone.
* **(C3) Reading A1 ($\operatorname{Pic}_{\mathbb R}$ as the ambient space).**
  $c\cap\operatorname{Pic}_{\mathbb R}=\{x\in P_{\mathrm{Pic}}:x\cdot\delta>0\ \forall\delta\in\Delta\}$
  is a chamber of the restricted arrangement and $C^\perp\cap\operatorname{Pic}_{\mathbb R}$ is
  a facet of its closure, of dimension $\rho-1$; same for $H^{1,1}_{\mathbb R}$ with dimension
  $19$.

*Proof of (C1).*
(i) *The chamber.*  Let $c':=\{x\in P:x\cdot\delta>0\ \forall\delta\in\Delta\}$.  Every Kähler
class belongs to $c'$ (a Kähler class is positive on every effective class); $c'$ is convex,
hence connected; $c'\subseteq P$ is open in $P$; so $c'$ is exactly one connected component of
$P\setminus\bigcup_\delta\delta^\perp$, and it is the one containing $K_X$.
(ii) *The closure.*  $\subseteq$ is clear.  For $\supseteq$: let $x\in\overline P$,
$x\cdot\delta\ge0$ for all $\delta$, and $h\in c'$; then $x+\varepsilon h\in P$ (the sum of
two vectors in the closure of the same component of $\{v^2>0\}$ with one of positive square has
positive square), $(x+\varepsilon h)\cdot\delta>0$ for all $\delta$, so $x+\varepsilon h\in c'$
and $x+\varepsilon h\to x$.
(iii) *$y\in\overline c$.*  $y^2=H'^2>0$, and $y=\lim_{\varepsilon\to0}(y+\varepsilon A)$ for any ample
$A$, where $y+\varepsilon A$ is ample for $0<\varepsilon\ll1$ by Nakai–Moishezon:
$(y+\varepsilon A)\cdot D>0$ for every curve $D$ ($D\ne C$: $y\cdot D\ge0$ and $A\cdot D>0$;
$D=C$: $A\cdot C>0$) and $(y+\varepsilon A)^2>0$.  So $y$ lies in the closure of the Kähler
classes, i.e. in $\overline P$; and $y\in P$ because $y^2>0$ and
$P=\overline P\cap\{x^2>0\}$.  Finally $y\cdot\delta\ge0$ for $\delta\in\Delta$ by Theorem B2.
(iv) *The facet.*  Corollary A2 applied to $\Lambda=\operatorname{Pic}(X)$, $\Delta=\Delta_b$
(note $y\cdot\delta\ge1$ for $\delta\ne\pm C$ by Theorem B2, and $y\cdot C=0$) gives
$\varepsilon>0$ with $x\cdot\delta>0$ for all $\delta\in\Delta\setminus\{\pm C\}$ and all
$x\in H^2_{\mathbb R}$ with $|x-y|<\varepsilon$.  Then
$$U:=\{x\in C^\perp:\ |x-y|<\varepsilon,\ x^2>0\}$$
is open in the affine space $C^\perp$ of dimension $21$, contains $y$, and is contained in
$\overline c$: indeed $x\cdot C=0$, $x\cdot\delta>0$ for the other $\delta$'s and $x^2>0$ with
$x\in P$ (same component as $y$).  So $y$ is a relative interior point of
$\overline c\cap C^\perp$, whose linear span is therefore all of $C^\perp$: $F$ is a face of
codimension one, i.e. a facet, with supporting hyperplane $C^\perp$.  $\square$

*Proof of (C3).*  Identical, with $\Lambda=\operatorname{Pic}(X)$ and the ambient space
$C^\perp\cap\operatorname{Pic}_{\mathbb R}$ (dimension $\rho-1$) resp.
$C^\perp\cap H^{1,1}_{\mathbb R}$ (dimension $19$); the set $U\cap\operatorname{Pic}_{\mathbb R}$
is open in $C^\perp\cap\operatorname{Pic}_{\mathbb R}$ because $x^2>0$ is open there.  The
closure formula (ii) is unchanged.  $\square$

*Proof of (C2), first route (uses the K3 cone theorem).*  The input is

> **BHPV, Corollary VIII.3.9.**  Let $S$ be a K3 surface, $C_S\subset\{x\in H^{1,1}(S,\mathbb R):
> x^2>0\}$ the component containing the Kähler classes, and $\Delta$ the set of classes of
> effective divisors of square $-2$.  Then
> $C_S^+=\{x\in C_S:(x,\delta)>0\ \text{for all }\delta\in\Delta\}$ **is the Kähler cone of
> $S$**.  (Barth–Hulek–Peters–Van de Ven, *Compact Complex Surfaces*, 2nd ed., Corollary
> VIII.3.9 — see also the statement and attribution in Hulek–Sankaran, *Moduli of K3 surfaces
> and irreducible symplectic manifolds*, Handbook of Moduli vol. II, §2.1, eq. (2.2).)

By that corollary and (ii) above (applied inside $H^{1,1}_{\mathbb R}$),
$\operatorname{Nef}(X)=\overline K_X=\{x\in\overline P_{1,1}:x\cdot\delta\ge0\ \forall
\delta\in\Delta\}$.  Hence $U\cap\operatorname{Pic}_{\mathbb R}\subseteq
\operatorname{Nef}(X)\cap C^\perp$, and $U\cap\operatorname{Pic}_{\mathbb R}$ is open in
$C^\perp\cap\operatorname{Pic}_{\mathbb R}$, which has dimension $\rho-1$: a facet.  $\square$

*Proof of (C2), second route (no cone theorem).*

**Lemma C3 (class group of the contraction).**  In the situation of Theorem B,
$$\operatorname{Pic}(X)_{\mathbb R}=\bigl(C^\perp\cap\operatorname{Pic}(X)_{\mathbb R}\bigr)
\oplus\mathbb R\,[C],\qquad \pi^*\operatorname{Cl}(X')_{\mathbb R}
=C^\perp\cap\operatorname{Pic}(X)_{\mathbb R},\qquad
\dim \pi^*\operatorname{Cl}(X')_{\mathbb R}=\rho-1 .$$

*Proof.*  $X'$ has only the Du Val (=quotient) singular point $\pi(C)$, so every Weil divisor
on $X'$ is $\mathbb Q$-Cartier.  Let $D\in\operatorname{Pic}(X)_{\mathbb Q}$ with $D\cdot C=0$,
and let $E:=\pi_*D\in\operatorname{Cl}(X')$ be its cycle-theoretic image (a Weil divisor, hence
$\mathbb Q$-Cartier); let $\pi^*E\in\operatorname{Pic}(X)_{\mathbb Q}$ be the $\mathbb Q$-Cartier
pullback.  Then $\pi^*E$ and $D$ agree on $X\setminus C$, so $\pi^*E=D+kC$ for some $k\in\mathbb Q$;
and the projection formula for the $\mathbb Q$-Cartier class $E$ gives
$\pi^*E\cdot C=E\cdot\pi_*C=0$.  Hence $0=\pi^*E\cdot C=D\cdot C+k\,C^2=-2k$, so $k=0$ and
$D=\pi^*E$.  Conversely $\pi^*E\cdot C=E\cdot\pi_*C=0$ for every $E$.  So
$\pi^*\operatorname{Cl}(X')_{\mathbb Q}=C^\perp\cap\operatorname{Pic}(X)_{\mathbb Q}$; tensoring
with $\mathbb R$ and using $C\notin C^\perp$ (as $C^2=-2$) gives the direct sum and
$\dim=\rho-1$.  $\square$

Now let $M\in\operatorname{Cl}(X')_{\mathbb R}$ and $\lambda>0$.  Since $X'$ is projective, the
ample cone is open in $N^1(X')_{\mathbb R}=\operatorname{Cl}(X')_{\mathbb R}$ (Kleiman's
criterion), so $H'+\lambda M$ is ample for $0<\lambda\ll1$; then
$y_\lambda:=\pi^*(H'+\lambda M)\in\operatorname{Pic}(X)_{\mathbb R}$ is nef (pullback of a nef
class under a morphism), lies in $C^\perp$, and $y_\lambda\to y$ as $\lambda\to0$.  Varying $M$
and $\lambda$, the $y_\lambda$ span $\pi^*\operatorname{Cl}(X')_{\mathbb R}\oplus\mathbb R y
=C^\perp\cap\operatorname{Pic}(X)_{\mathbb R}$ (Lemma C3), so the face
$\operatorname{Nef}(X)\cap C^\perp$ has linear span $C^\perp\cap\operatorname{Pic}_{\mathbb R}$
and is a facet of dimension $\rho-1$.  $\square$

**Remark C4 (defect 1, item (ii), as a byproduct — complementary to whoever owns defect 1).**
From (C1)(i) and BHPV VIII.3.9, $c\cap H^{1,1}_{\mathbb R}=K_X$ exactly (the two descriptions
of the same chamber coincide), hence
$$c\cap\operatorname{Pic}(X)_{\mathbb R}=K_X\cap\operatorname{Pic}(X)_{\mathbb R}
=\operatorname{Amp}(X),$$
the last equality being Kleiman/Nakai–Moishezon on the projective surface $X$ (an algebraic
class positive on every curve is ample).  So the tracked assertion "the intersection with
$\operatorname{Pic}\otimes\mathbb R$ is exactly the Kähler cone" is correct **when read as
$c\cap\operatorname{Pic}_{\mathbb R}=\operatorname{Amp}(X)$**, and requires BHPV VIII.3.9;
whereas the *chamber of the full-$H^2$ arrangement is not a product* — it is the full
preimage of its $H^{1,1}$-part under the linear projection $H^2_{\mathbb R}\to
H^{1,1}_{\mathbb R}$: the sign conditions $x\cdot\delta\neq0$ involve only the $H^{1,1}$
component of $x$, while $x^2$ couples the components, so
$c=\{x\in P:\ x_{1,1}\in c\cap H^{1,1}_{\mathbb R}\}$ and chamber invariants *are* read on the
algebraic part.  (The transcendental part enters $x^2$, which is why $c$ is not literally a
product $c_{1,1}\times(\text{something})$; it is a pullback along a projection.)

---

## 5. Lemma D: facet normals are roots — and the space table

**Lemma D.**  Assume $(H_1)$, $(H_2)$, and let $V$ be one of $H^2_{\mathbb R}$,
$H^{1,1}_{\mathbb R}$, $\operatorname{Pic}(X)_{\mathbb R}$, with $P_V$ the positive cone and
$c_V$ the chamber containing the Kähler cone.  Let $F$ be a facet of $\overline{c_V}$.  Then
$F\subseteq\delta^\perp$ for some $\delta\in\Delta$, $\operatorname{span}F=\delta^\perp$, and
every normal of $F$ is $\pm\delta$ for that $\delta$ (unique up to sign).

*Proof.*  (i) $F\not\subseteq\partial\overline P_V$.  If $F\subseteq\{x:x^2=0\}$, then for
$x,x'\in F$ also $\frac{x+x'}2\in F$, so
$0=(\frac{x+x'}2)^2=\frac14(x^2+2x\cdot x'+x'^2)=\frac12 x\cdot x'$, i.e. the form vanishes on
$\operatorname{span}F$: a totally isotropic subspace.  In signature $(3,19)$ totally isotropic
subspaces have dimension $\le3$, in $(1,19)$ and $(1,\rho-1)$ dimension $\le1$; but
$\dim F=21$ resp. $19$ resp. $\rho-1$ (Theorem C).  (The argument needs $\dim F\ge2$, i.e.
$\rho\ge3$ in the $\operatorname{Pic}_{\mathbb R}$ case.  For $\rho=2$, where a facet is a ray
and a lightlike boundary ray is not excluded by this count, the lemma is *not* proved here; no
witness is in that range, all having $\rho\ge11$.)
(ii) $F\cap\partial\overline P_V$ is a face of $F$; by (i) $F\not\subseteq\partial\overline P_V$,
so $\operatorname{ri}F\cap\partial\overline P_V=\emptyset$ and $\operatorname{ri}F\cap
P_V\neq\emptyset$.
(iii) Let $x\in\operatorname{ri}F\cap P_V$.  Then $x\in F\subseteq\partial\overline{c_V}$.  If
$x\cdot\delta\ne0$ for every $\delta\in\Delta$, then $x$ lies in $P_V\setminus\bigcup_\delta
\delta^\perp$, a disjoint union of chambers; let $c'$ be the chamber containing $x$.  By the
closure formula (C1)(ii), $\overline{c_V}=\{z\in\overline P_V:z\cdot\delta\ge0\ \forall\delta
\in\Delta\}$ and $c'$ is defined by $z\cdot\delta_0<0$ for some $\delta_0$; hence
$c'\cap\overline{c_V}=\emptyset$, contradicting $x\in c'\cap\overline{c_V}$.  So $x\cdot\delta=0$
for some $\delta\in\Delta$.
(iv) $E:=\{z\in\overline{c_V}:z\cdot\delta=0\}$ is a face of $\overline{c_V}$ containing $x$;
since $x\in\operatorname{ri}F$ and $F$ is a face, $F\subseteq E$, i.e. $F\subseteq\delta^\perp$;
$F$ is a facet, so $\operatorname{span}F=\delta^\perp$.  If $u$ is a normal of $F$ then
$u^\perp=\delta^\perp$, so $u=\lambda\delta$; if $u$ is a root too, $\lambda^2=(\lambda\delta)^2/
\delta^2=1$.  $\square$

**5.3 The space table.**  (All dimensions exact; $\rho=\rho(X)\le20$.)

| ambient space $V$ | $\dim V$ | signature | chamber | facet dimension | input needed to identify the chamber with geometry |
|---|---|---|---|---|---|
| $H^2_{\mathbb R}(X)$ | $22$ | $(3,19)$ | Reading C / m8's A2: $c\subset P$ | $21$ | none (definitional); its $H^{1,1}$-part *is* $K_X$ by BHPV VIII.3.9 |
| $H^{1,1}_{\mathbb R}(X)$ | $20$ | $(1,19)$ | $c\cap H^{1,1}_{\mathbb R}$ | $19$ | BHPV VIII.3.9 ($K_X$) |
| $\operatorname{Pic}(X)_{\mathbb R}$ | $\rho$ | $(1,\rho-1)$ | Reading A1: $c\cap\operatorname{Pic}_{\mathbb R}$; Reading K: $\operatorname{Nef}$ | $\rho-1$ | BHPV VIII.3.9, or Lemma C3 + Kleiman |
| $\operatorname{Pic}^\perp\subset H^2_{\mathbb R}$ | $22-\rho$ | $(2,\,20-\rho)$ | — (no walls meet it transversally: its elements pair $0$ with every algebraic class) | — | — |

Two corrections against the tracked addendum B: $\operatorname{Pic}^\perp$ has signature
$(2,20-\rho)$ and not $(2,19-\rho)$ (subtract the signature $(1,\rho-1)$ of
$\operatorname{Pic}_{\mathbb R}$ from $(3,19)$); and the expression "a facet of the nef cone in
$\operatorname{Pic}\otimes\mathbb R$ of dimension $\rho-1$" and the later "full hyperplane
dimension $21$" are statements about *different spaces* and cannot both apply to one face.  In
Reading C no transcendental perturbation is needed at all: $U$ of (C1)(iv) is already a
$21$-dimensional ball inside the facet, since the walls only see the algebraic directions.  The
tracked addendum's device "$y+z$ with $z\in\operatorname{Pic}^\perp$" is correct but redundant;
its real use is in the *other* direction (it shows $c$ is a pullback along
$H^2_{\mathbb R}\to H^{1,1}_{\mathbb R}$, Remark C4).

**5.4 What the facet theorem changes about the fourth bullet's quantifier.**  The authored text
was read at the named commit (`git show a145cea4a5:writing/coble/heegner-report/coble-heegner-research-report.md`,
lines 601–638): the tuple is $(L_{K3},I_{\mathrm{Co}},I_{\mathrm{dP}},H,\alpha,\mathfrak c)$ with
the bullets $\alpha^2=-2$, $H\cdot\alpha=0$, $\alpha$ fixed by $I_{\mathrm{Co}}$, and
"$\mathfrak c$ is the chosen positive/nef chamber in which $\alpha$ is effective and $H$ is nef
and big".  Since $H\cdot\alpha=0$, $H$ lies on the wall $\alpha^\perp$ and in no open chamber;
read with $\mathfrak c$ open, "$H$ is nef and big in $\mathfrak c$" is unsatisfiable.  Three
readings survive, and the facet theorem says exactly what each needs:
(a) *chamber with the condition on its closure*: $\mathfrak c$ is a chamber of the effective-root
arrangement and $H\in\overline{\mathfrak c}$.  This is consistent and non-vacuous: with
$\alpha=[D_b]$ the exceptional $(-2)$-curve, Theorem C (applied to $C=D_b$) gives that
$\alpha^\perp$ supports a *facet* of $\overline{\mathfrak c}$, so $\alpha$ has one sign on
$\mathfrak c$ (it is effective there) while $H\in\overline{\mathfrak c}\cap\alpha^\perp$ is
nef ($H\in\operatorname{Nef}=\overline{K_X}$) and big ($H^2=4>0$, nef with positive square).
(b) *Mori/nef chamber of the member*: $\mathfrak c=\operatorname{Nef}(X)$; then $H\in\mathfrak c$
literally and is nef and big, and "$\alpha$ effective in $\mathfrak c$" means $\alpha\cdot x>0$
for Kähler $x$; the root-arrangement information is lost.  (c) *the labels' own lattice* (the
reading m5/m6 call L): vacuous about the member's cone.  "Preserving the chosen chamber" means,
in (a), preserving the chamber (equivalently the closure, equivalently the census of facet
normals, whence Lemma D makes it a root census), in (b) preserving $\operatorname{Nef}(X)$, in
(c) nothing beyond $(H,\alpha)$.  Which of (a)/(b) the authored text intends is defect 1's
deliverable; what is settled here is that (a) is satisfiable at $H$, that in (a) no ambiguity of
choice remains (m8's $\omega=H-\tfrac12\alpha$ is an interior point of the chamber, so the
chamber is pinned by $(H,\alpha)$), and that the chamber-invariant used by the obstruction is
exactly its facet-normal census.

---

## 6. Line-by-line audit of the tracked chain (addendum B of `sm57_proof-m5.md`)

| tracked sentence | verdict |
|---|---|
| "on a K3 surface a smooth rational curve with negative self-intersection is contractible, Grauert" | true (Grauert 1962), but the projective contraction is directly Artin 1962 Thm 2.3, which also gives **projectivity of the target** — the sentence leaves that open (review gap (a)) |
| "Take an integral ample class $A'$ on $X'$ and put $y=\sigma^*A'$" | now justified: $X'$ is projective by Theorem B1, so $A'$ exists |
| "$y$ is nef, $y\cdot\delta=0$, and for every effective class $\delta'$ with $\sigma_*\delta'\ne0$ one has $y\cdot\delta'=A'\cdot\sigma_*\delta'\ge1$, since $A'$ is integral ample" | correct, and proved in Theorem B3 (integrality is what gives $\ge1$, not just $>0$); note $\pi_*\delta'\ne0$ fails only for $\delta'\in\mathbb Z_{\ge1}C$, where $\delta'^2=-2$ forces $\delta'=C$ |
| "the only curves contracted by $\sigma$ are the ones in the ADE configuration — here the single $C_+$" | correct but *not needed*: Artin's criterion applied to the analytic set $C_+$ alone produces a contraction whose only contracted set is $C_+$; the claim that the ADE configuration is a single curve is therefore a consequence, not a hypothesis |
| "Hence in a neighbourhood of $y$ no wall other than $\delta^\perp$ exists" | **true, but the proof in the text is missing and the naive proof is wrong.** Correct version: Lemma A1 + Corollary A2, with the explicit $\varepsilon=1/(4C)$; Cauchy–Schwarz in the indefinite form gives nothing, and with unbounded root norms the assertion is false (Remark A3(i)) |
| "the face $\overline{K_b}\cap\delta^\perp$ contains an open ball of $\delta^\perp$ in $\operatorname{Pic}\otimes\mathbb R$, of dimension $\rho-1$" | true in content (Theorem C2/C3), but it needs the identification $\operatorname{Nef}=\{x\in\overline P:x\cdot\delta\ge0\ \forall\delta\}$ — BHPV VIII.3.9 — or Lemma C3 + Kleiman; the text supplies neither, so "no other wall near $y$, hence a facet" is a gap as written |
| "For the chamber as a cone of the full $H^2(\widehat X,\mathbb R)$ (Reading C) … with $(y+z)^2=y^2+z^2>0$ for all but a thin set of small $z$, the face … has full hyperplane dimension $21$" | conclusion true (Theorem C1); the $z$-device is a valid *alternative* route, but the sentence mixes spaces (a $21$-dimensional hyperplane is in $H^2_{\mathbb R}$, not in $\operatorname{Pic}\otimes\mathbb R$) and its signature count is off by one (see 5.3); the ball needed for the facet is already there without $z$ |
| "the walls that support facets of $\overline{\mathfrak c_b}$ are exactly the $\delta^\perp$ for effective $(-2)$-classes $\delta$ whose contraction is valid, and any facet's normal is $\pm\delta$ unique up to sign" | the second half is Lemma D (proved); for the first half, "whose contraction is valid" is vacuous for a *smooth rational* $(-2)$-curve (Artin's criterion always applies, Theorem B), and is a genuine restriction for a reducible effective $(-2)$-class $\delta=C_1+\dots+C_k$: contracting the whole configuration makes $y$ orthogonal to every $C_i$, so the method yields the face of codimension $k$, not the facet $\delta^\perp$. The corpus needs only the irreducible case |
| "On $b_0$, any facet normal is $\pm\delta$ for an effective $\delta$ of square $-2$, and $\operatorname{Pic}(\widehat X_{b_0})$ has no such $\delta$ of $|H\cdot|=1$ — by A, since every ruling away from the node's is irreducible" | Lemma D supplies the normal-is-a-root step; the second step, $\nu(b_0)=0$, is m5's own finite computation: its discriminant half is re-verified in §7.2, and it is *sufficient* for $\nu(b_0)=0$ (the sharper wording "irreducible nodal cubic" is stronger than what the discriminant gives and is not needed) |

---

## 7. Application to the explicit witnesses

**7.1 The bitangent witness $b_\star$ (m5 §6).**  $Y=\mathbb P^1\times\mathbb P^1$,
$p=(0,0)$, $\tau=(-1,-1)$, $B_\star=\{f_\star=0\}$ with $f_\star$ as printed in
`sm57_proof-m5.md` §6.  Independently re-computed (`verify_defect2.py`, exact arithmetic,
log in `verify_defect2.log`):

* $f_\star$ involves only monomials $x^iy^j$ with $i+j$ even (so $B_\star$ is $\tau$-invariant);
  $f_\star(p)=0$ with quadratic part $3x^2-28xy+13y^2$, of discriminant
  $28^2-4\cdot3\cdot13=628\ne0$: an ordinary node at $p$;
* $f_\star(1,y)=(y-1)^2(y-3)^2$: the ruling $D=\{x=1\}$, whose class is $h_1$, is bitangent to
  $B_\star$ at $(1,1)$ and $(1,3)$ and meets it in no other point (total intersection $4$);
* hence the double cover $\pi\colon\widehat X_{b_\star}\to Y$ pulls $\{x=1\}$ back to two
  components, $\pi^*D=C_++C_-$, each mapping isomorphically to $D\cong\mathbb P^1$ (the branch
  divisor on $D$ is $2[(1,1)]+2[(1,3)]$, even, so the local equations split), with
  $$C_\pm^2=D^2-\tfrac12 D\cdot\widetilde B=0-\tfrac124=-2,\qquad
  0=(\pi^*D)^2=C_+^2+C_-^2+2C_+\cdot C_-\ \Rightarrow\ C_+\cdot C_-=2,$$
  $$C_\pm\cdot H=(h_1+h_2)\cdot h_1=1,\qquad C_\pm\cdot\alpha=\pi_*C_\pm\cdot e=h_1\cdot e=0,$$
  and $C_\pm\cdot e_b=h_1\cdot h_1=0$, $C_\pm\cdot f_b=h_1\cdot h_2=1$ in the notation of
  `sm57_proof-m5.md` §1.1.  In particular $\nu(b_\star)\ge2$ (both $C_\pm$ are effective of
  square $-2$ and $H$-degree $1$).  The same computation at $x=-1$ (using $\tau$-invariance,
  $f_\star(-1,y)=f_\star(1,-y)=(y+1)^2(y+3)^2$) gives two more such classes, so
  $\nu(b_\star)\ge4$; only $\ge2$ is used.
* Consequence: $C_+$ is a smooth rational curve of square $-2$ on the smooth projective K3
  $\widehat X_{b_\star}$, so Theorem B and Theorem C apply with $C=C_+$.  Hence
  $C_+^\perp$ supports a facet of $\overline{\mathfrak c_{b_\star}}$ in each of the three
  spaces, its normal is exactly $\pm C_+$, and $|H\cdot C_+|=1$.  That is precisely the facet
  statement `sm57_proof-m5.md` §7 (Reading C) uses, now unconditional and with no knowledge of
  $\operatorname{Pic}(\widehat X_{b_\star})$ required.

**7.2 Audit of the $b_0$ side ($\nu(b_0)=0$).**  This is a premise of the obstruction, not of
the facet chain, but it uses the same indexing, so it is re-checked.  For
$g_c(y):=f_0(c,y)$ the fibre of the ruling map
$\widehat X_{b_0}\to\mathbb P^1_{(x)}$ over $x=c$ is the double cover $\{z^2=g_c(y)\}$; away
from the node's ruling ($c\ne0$) the resolution is an isomorphism there, and
$\{z^2=g_c\}$ is reducible **iff $g_c$ is a square up to a nonzero scalar** (a reducible double
cover of $\mathbb P^1$ has two components of degree $1$, each a graph $z=\pm h$).  A square has
vanishing discriminant, and if $g_c=h^2$ with $h$ of degree $2$ with distinct roots, the
discriminant of $g_c$ vanishes to order $\ge2$ in $c$.  Re-computed:
$$\operatorname{disc}_y f_0=x^2\,q(x),\qquad \deg q=22,\quad q\ \text{squarefree (verified)},\quad
f_0(0,y)=-y^2(y^2+5),$$
and symmetrically $\operatorname{disc}_x f_0=-y^2 r(y)$ with $\deg r=22$.  Hence for $c\ne0$
no fibre is a square, and all ruling fibres away from $x=0$ are irreducible.  The fibre over
$x=0$ *is* reducible, by the two-branch phenomenon of the node: $z^2=-y^2(y^2+5)$ has two
smooth branches at $(0,0)$ since $-5$ is a square up to sign, and the resolution separates them
into the exceptional curve $D_{b_0}$ ($H$-degree $0$) and the proper transform ($H$-degree
$2$).  So $\nu(b_0)=0$ by m5's Lemma 5.1.  Two scoping remarks: (a) the tracked wording "the
other $22$ singular fibres are irreducible nodal cubics" asserts more than the discriminant
computation gives — what it gives, and what $\nu(b_0)=0$ needs, is irreducibility of those
fibres, which follows from squarefreeness of $q$; (b) the reducibility criterion above is the
one used, and it is deliberately stated for the *unresolved* cover away from the node's ruling.

*Cross-check against the other directions.*  m3's node-ruling dichotomy
(`.ultramath/smw0b9kmo/m3`, finding f7) shows that "the node's ruling fibre is $I_2$ with
$H$-degrees $0$ and $2$" is a theorem only when $a_{02}\ne0$: for $a_{02}=0$ that fibre is
Kodaira type IV — three $\mathbb P^1$'s through one common point, pairwise transverse, of
$H$-degrees $1,1,0$ — and then $\nu\ge2$ already arises from the node's own ruling.  Both
members the obstruction compares have $a_{02}\ne0$: $b_0$ has quadratic part
$2x^2+7xy-5y^2$, so $a_{02}=-5$, and $b_\star$ has $3x^2-28xy+13y^2$, so $a_{02}=13$.  Hence
the case analysis used above is valid for the pair, and m5's Lemma 5.1 ("a curve of
$H$-degree $1$ forces a reducible fibre over a ruling *other* than the ruling through $p$") is
a theorem on the divisor $a_{02}\ne0$ — where the compared pair lies — but not on all of the
one-node locus; Corollary 5.2's invariant should carry that hypothesis or the type IV case.
m3's exact census (finding f5: $\nu=0$ for the corpus' member and for $b_0$, $\nu=4$ for
$b_\star$ and for m6's $B$, $\nu=2$ for m8's $F'$) agrees with $\S7.1$'s bound $\nu(b_\star)\ge4$
and supplies the exact value left open in `sm57_proof-m5.md` §10(i).

**7.3 All four witnesses, not only $b_\star$.**  If $b$ is any one-node member and
$\delta\in\operatorname{Pic}(\widehat X_b)$ has $\delta^2=-2$, $H_b\cdot\delta=1$, then $\delta$
is (m5 Lemma 5.1, m5 finding f8) the class of a component of a reducible ruling fibre, hence
represented by a *smooth rational* curve $C$ with $C^2=-2$; Theorem C then applies verbatim and
gives a facet of $\overline{\mathfrak c_b}$ with normal $\pm\delta$ and $|H\cdot\delta|=1$.  So the
facet chain is unconditional for every witness of the charter (m5's $b_\star$, m8's $F'$,
m6's three-split member and the tangent members), not merely for the bitangent one; what changes
from member to member is only the *number* of such classes (the census $\nu$), which is m5's,
m3's and m2's object, not an input of the facet theorem.

**7.4 The finite-root-bound route is unavailable, not merely unnecessary.**  The charter offers:
reduce the facet claim on the explicit witnesses to a finite verification by bounding the
witness' effective roots.  A bound on $\Delta_b$ needs $\operatorname{Pic}(\widehat X_b)$, which
the tracked evidence does not have: only $\rho\ge11$ (m5 Lemma 1.3) and the explicit sublattice
$\langle e_b,f_b,\alpha_b\rangle$ (rank $3$, plus $C_\pm$ for $b_\star$) are known.  Roots of
unbounded $y$-degree exist as soon as the lattice has rank $\ge3$ (if $|y\cdot\delta|$ were
bounded on the root set, Lemma A1 applied to $\delta$ and to $-\delta$ would make that set
finite, which it is not in an indefinite lattice of rank $\ge3$), so a finite check needs the
lattice, not just a bound on $y\cdot\delta$.  The route is not needed: Theorem C is
lattice-free.

---

## 8. Hypothesis ledger

| premise | status |
|---|---|
| $X$ smooth projective K3, $K_X=0$, signature $(3,19)$, $h^{2,0}=1$, $\rho\le20$ | $(H_1)$; standard |
| $C=C_+\cong\mathbb P^1$, $C^2=-2$ | $(H_2)$; for $b_\star$ verified in §7.1 |
| **Artin's contractibility criterion**, Thm 2.3 of Amer. J. Math. 84 (1962) 485–496 | cited; hypotheses (i) negative definite, (ii) $p_a(mC)\le0$ checked in Theorem B. Statement verified against two independent secondary quotations (arXiv:2110.05447, Thm 1.3 with attribution to Artin Thm 2.3 p. 491; a MathOverflow answer stating the same theorem) — the original paper was not opened |
| **Grauert's contraction theorem**, Math. Ann. 146 (1962) 331–368 §5–6 | cited only in the *uniqueness/projectivity* remark B6; not needed for the chain |
| **Kollár–Mori, Base Point Free Theorem, Thm 3.3** | cited only as a cross-check in B6; hypotheses (smooth $\Rightarrow$ klt, $D$ nef and big, $D-K_X=D$) checked there. Numbering verified against secondary lecture notes |
| **BHPV, Corollary VIII.3.9** (Kähler cone $=$ chamber cut by nodal classes) | cited in (C2) first route, Lemma D's input (iii), Corollary C4. Statement and numbering verified against two independent secondary sources (Hulek–Sankaran, *Moduli of K3 surfaces and irreducible symplectic manifolds*, §2.1 eq. (2.2), which cites exactly "[BHPV, Corollary VIII.3.9]"; and a second survey citing the same numbering) — the book itself was not opened |
| "quotient singularities are $\mathbb Q$-factorial" (Lemma C3) | standard; used only in the *second* route to (C2) |
| Kleiman's criterion (ample cone open in $N^1_{\mathbb R}$ of a projective variety) | standard; used in (C2) second route |
| NAKAI–MOISHEZON on a smooth projective surface | standard; used to produce the ample classes $y+\varepsilon A$ and to identify $\operatorname{Amp}=$ interior of the nef cone |
| Lemma A1, Corollary A2, Lemma D, Theorem B, Theorem C | proved here |
| $\nu(b_0)=0$ | m5 Lemma 5.1 + §7.2 (discriminant re-verified); discarded input: "nodal cubic" shape |
| NOT used | integral eigensplittings of $H^2$; any knowledge of $\operatorname{Pic}(\widehat X_b)$ beyond $\rho\ge11$; the very-general-member/period-map input (`prob:projective-coverage`, m8 Thm 3.3); Grauert or Artin *algebraization* of formal moduli; the disputed connectedness of the one-node locus |

---

## 9. What is *not* established here (exact boundary)

1. **The reading question of the fourth bullet** is not settled here; §5.3 says which space
   each facet statement lives in and what each reading costs, but "which reading the authored
   text at `a145cea4a5` intends" is defect 1's deliverable.  What is now settled is that
   *under every reading* the wall $C_+^\perp$ supports a facet, with normal $\pm C_+$ and
   $|H$-degree$|=1$ — the input m5's §7 census uses.
2. **The census comparison itself** (m5 §7: "no effective root of $b_0$ has $|H\cdot|=1$, while
   $b_\star$ has $C_+$, hence no label-preserving isometry matches the chambers") is m5's
   argument; I verified its two premises lie in the right shape (Lemma D on the $b_0$ side, §7.1
   on the $b_\star$ side, §7.2 for $\nu(b_0)=0$) but did not re-derive the isometry-theoretic
   conclusion.
3. **The generic-member fibre frame** (charter defect 3, "single fibre, degree cases $0/2/1$")
   is untouched here: §7 computes fibres of the two *explicit* members only.  Theorem B/C do
   not need that frame.
4. **Citation depth.**  Artin Thm 2.3, BHPV Cor. VIII.3.9 and Kollár–Mori Thm 3.3 are cited at
   the level of their statements and numbering as verified in the secondary literature named
   in §8; the originals were not opened in this VM.  A thesis-level audit should open them; in
   the meantime the second route to (C2) removes the dependence on BHPV from the nef-cone
   statement, and (C1) removes it from the full-space statement, so only the $H^{1,1}$ reading
   (which the corpus does not use for the obstruction) depends on BHPV alone.
5. **$\rho=2$ edge case** of Lemma D is explicitly left open (dimension count insufficient); no witness is in that range ($\rho\ge11$), and nothing here uses it.

---

## 10. Files

* `proof.md` — this document.
* `verify_defect2.py` — exact-arithmetic verification of §7.1, §7.2 and of Remark B5.
* `verify_defect2.log` — its output.

---

## 11. Replacement text for addendum B (paste-ready, all hypotheses named)

> **B (corrected).  Why $\delta^\perp$ supports a facet, and why $b_0$ has no facet of degree $1$.**
> Let $\widehat X$ be a smooth projective K3, $C\subset\widehat X$ a smooth rational curve with
> $C^2=-2$, $\delta=[C]$.
>
> *Step 1 (contraction, projectivity, ample class).*  By **Artin's contractibility criterion**
> (M. Artin, Amer. J. Math. 84 (1962), Theorem 2.3, p. 491) — a connected curve $C$ on a normal
> projective surface, nonsingular along $C$, is contractible to a point of a **normal projective**
> surface iff its intersection matrix is negative definite and every effective cycle $Z>0$
> supported on $C$ has $p_a(Z)\le0$ — applied to the single curve $C$: the matrix is $(-2)$ and
> $p_a(mC)=1+\tfrac12(mC)^2=1-m^2\le0$.  So there is $\sigma\colon\widehat X\to X'$ with $X'$
> normal projective, $\sigma(C)$ a point, $\sigma$ an isomorphism outside $C$.  (The analytic
> Grauert contraction of $C$ is the *same* map, by uniqueness of contractions; in particular it is
> projective.)
> *Step 2 (the class $y$).*  Let $A'$ be an integral ample class on $X'$ and $y=\sigma^*A'$.  Then
> $y^2=A'^2>0$, $y\cdot C=0$, $y\cdot D\ge0$ for every curve $D$, and
> $y\cdot\delta'=A'\cdot\sigma_*\delta'\ge1$ for every effective $\delta'$ with
> $\sigma_*\delta'\ne0$; and $\sigma_*\delta'=0$ forces $\delta'=mC$, and then
> $\delta'^2=-2m^2=-2$ gives $m=1$.
> *Step 3 (the wall-free ball — the lemma the earlier text assumed).*  Let $\Lambda$ be a lattice
> of signature $(1,\rho-1)$, $y\in\Lambda_{\mathbb R}$, $y^2>0$, and $\Delta$ a set of roots with
> $y\cdot\delta\ge1$ for all $\delta\in\Delta$.  Then there is $\varepsilon>0$ such that
> $|x-y|<\varepsilon$ implies $x\cdot\delta>0$ for all $\delta\in\Delta$.  Explicitly: write
> $\delta=\frac{y\cdot\delta}{y^2}y+p(\delta)$ with $p(\delta)\in y^\perp$; then
> $p(\delta)^2=-2-\frac{(y\cdot\delta)^2}{y^2}$, and comparability of the Euclidean norm with
> $\sqrt{|q|}$ on the negative definite space $y^\perp$ gives
> $|\delta|\le C_0(1+y\cdot\delta)$; hence for $\varepsilon\le1/(4C_0)$
> $x\cdot\delta\ge y\cdot\delta-\varepsilon|\delta|\ge\frac34y\cdot\delta-\frac14\ge\frac12$.
> (This is where the argument is *not* Cauchy–Schwarz — that inequality is false in indefinite
> signature — and where bounded root length $|\delta|^2=-2$ is essential: with unbounded normal
> length the assertion is false.)
> *Step 4 (facet).*  Let $\mathfrak c$ be the chamber of
> $C_{\widehat X}\setminus\bigcup_{\delta\in\Delta_b}\delta^\perp$ containing the Kähler classes.
> Then $\overline{\mathfrak c}=\{x\in\overline{C_{\widehat X}}:x\cdot\delta\ge0\ \forall\delta
> \in\Delta_b\}$ and $y\in\overline{\mathfrak c}$; the ball of Step 3 intersected with
> $C^\perp\cap\{x^2>0\}$ is open in $C^\perp$ (dimension $21$) and lies in $\overline{\mathfrak c}$.
> So $C^\perp$ supports a facet of $\overline{\mathfrak c}$ of dimension $21$ with normal $\pm C$.
> For the nef-cone reading $\mathfrak c=\operatorname{Nef}$, the same ball lies in
> $\operatorname{Nef}$ by **BHPV, Corollary VIII.3.9** (the Kähler cone is the chamber
> $\{x\in C_X:x\cdot\delta>0\ \forall\delta\in\Delta_b\}$), giving a facet of dimension $\rho-1$;
> without BHPV, the classes $\sigma^*(A'+\lambda M)$ ($M\in\operatorname{Cl}(X')_{\mathbb R}$,
> $0<\lambda\ll1$) are nef, lie in $C^\perp$ and span $C^\perp\cap\operatorname{Pic}_{\mathbb R}$,
> since $\sigma^*\operatorname{Cl}(X')_{\mathbb R}=C^\perp\cap\operatorname{Pic}_{\mathbb R}$ has
> rank $\rho-1$ (a class orthogonal to $C$ descends: $\pi^*\pi_*D=D+kC$ with
> $0=D\cdot C=-2k$).
> *Step 5 (facet normals are roots).*  Every facet of $\overline{\mathfrak c}$ is contained in some
> $\delta^\perp$, $\delta\in\Delta_b$: its relative interior is not contained in the light cone (a
> totally isotropic subspace has dimension $\le3<21$ in signature $(3,19)$, $\le1<19$ in
> $(1,19)$), so it contains $x\in C_{\widehat X}$; then $x\cdot\delta=0$ for some
> $\delta\in\Delta_b$ (otherwise $x$ would lie in another chamber, disjoint from
> $\overline{\mathfrak c}$), and the face exposed by $\delta$ contains the facet.  The normal is
> $\pm\delta$, determined by the facet up to sign.
> *Step 6 (the census).*  For $b_\star$, $C_+$ is a smooth rational $(-2)$-curve (verified:
> $f_\star(1,y)=(y-1)^2(y-3)^2$ makes the ruling $\{x=1\}$ split into $C_++C_-$, $C_\pm\cong
> \mathbb P^1$, $C_\pm^2=-2$), so $C_+^\perp$ supports a facet whose normal has $|H\cdot C_+|=1$.
> For $b_0$, every facet normal is $\pm\delta$ with $\delta\in\Delta_{b_0}$ and $\nu(b_0)=0$
> (discriminant computation: no ruling away from the node's is reducible), so no normal has
> $|H\cdot|=1$.  An isometry taking one chamber to the other takes facets to facets, normals to
> normals, and preserves $|H\cdot|$: contradiction.
