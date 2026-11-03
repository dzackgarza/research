# O-S — saturation: **decided, $\det S_{\mathrm{dP}}=8$**, by a route independent of the section argument

Member m8, direction d7, swarm `smw0dbvr6`. Repository
`/workspace/nucleus/work/projects/p-9fcb4ed7f4b64e008de2ee29a7197bf4/repo` (read-only),
evidence state `main@141058a8`. Citations by block id of

* **(A)** `writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md`
  (the statement to decide is `rmk:a21-scope`, "Where the type of $S_{\mathrm{dP}}$ will be decided"),
* **(R)** `computations/reports/sm00_arithmetic-core.md`,
* **(P)** `computations/reports/sdp_discriminant_referee.py` and its log (maintained provider, pin
  `c546077d`).

## 0. Outcome

For every member $b$ of the one-node direct-projective construction (branch curve with exactly one
node, at the $\tau$-fixed point $p$, otherwise smooth with nondegenerate quadratic part),
$$S_{\mathrm{dP},b}\;=\;H^2(\widehat X_b,\mathbb Z)^{I_{\mathrm{dP}}=+1}\;=\;\Lambda
\;=\;\pi_b^*\mathrm{Pic}(\widehat Y)\perp\mathbb Z[D_b]\;\cong\;U(2)\perp\langle-2\rangle,\qquad
\det S_{\mathrm{dP},b}=8,\quad [S_{\mathrm{dP},b}:\Lambda]=1 .$$
The index-$2$ candidate $U\perp\langle-2\rangle$ ($\det2$) of (A) `rmk:a21-scope` does **not** occur.
Three independent proofs are recorded: §2 (**new here**: Nikulin's classification of 2-elementary K3
surfaces applied to the fixed curve of $I_{\mathrm{dP}}$), §3 (my own non-existence proof for the
half-classes $\tfrac12e_b,\tfrac12f_b$ via Riemann–Roch and the verticality lemma, independent of any
ampleness input), and §4 (member m5's section/ampleness argument
`.ultramath/smw0dbvr6/m5/O-S-saturation.md`, which I have read line by line and which is correct).
Consequently the obligation (O-S) carries **no remaining sharp question**: the determinant is $8$.
What remains open in the neighbourhood is *not* this lattice question but the A21 chamber clause
((A) `prob:effective-cone-agreement`), which §6 records as untouched.

No integral eigensplitting of $H^2$, no chamber or translation-invariance detector, and no bespoke
"checker" is used; the only computational input is the provider log of §1.

---

## 1. The lattice, its rank, and the two candidates

**1.1** $Y=\mathbb P^1\times\mathbb P^1$, rulings $h_1,h_2$ ($h_i^2=0$, $h_1\cdot h_2=1$),
$\tau(x,y)=(-x,-y)$, $\widehat Y=\operatorname{Bl}_pY$ with exceptional curve $e$, and
$\pi_b\colon\widehat X_b\to\widehat Y$ the finite degree-$2$ cover branched along
$\widetilde B=-2K_{\widehat Y}$ (the proper transform of the branch curve), which is smooth
((A) `lem:face-at-H`(1); (A) `prop:one-node-family`). $I_{\mathrm{dP}}$ is the deck transformation.
Put $e_b=\pi_b^*h_1$, $f_b=\pi_b^*h_2$, $D_b=\alpha_b=\pi_b^*e$; then $e_b^2=f_b^2=0$,
$e_b\cdot f_b=2$, $D_b^2=-2$, $D_b\perp\pi_b^*\mathrm{Pic}(\widehat Y)$, so
$$\Lambda=\langle e_b,f_b,D_b\rangle\cong U(2)\perp\langle-2\rangle,\qquad
\det\Lambda=-4\cdot(-2)=8,\qquad A_\Lambda\cong(\mathbb Z/2)^3,$$
and $\Lambda\subseteq S_{\mathrm{dP},b}$ since all three classes are $I_{\mathrm{dP}}$-invariant.

**1.2 Rank.** $\operatorname{Fix}(I_{\mathrm{dP}})=\widetilde B$, a smooth curve of genus $8$; by
Lefschetz $\operatorname{tr}(I_{\mathrm{dP}})=\chi(\widetilde B)-2=-14-2=-16=2r-22$, so $r=3$
((A) `prop:tuple-of-the-construction`(5), whose form $r=(\chi+20)/2$ gives the same). Hence $\Lambda$
and $S_{\mathrm{dP}}$ have equal rank, the
index is finite and a power of $2$, and only $[S:\Lambda]\in\{1,2\}$ keeps
$\det S=8/[S:\Lambda]^2$ an integer: the two candidates are $\det8$ ($\Lambda$) and $\det2$
($U\perp\langle-2\rangle$).

**1.3 The half-class census.** Of the seven non-zero classes of $A_\Lambda$, parametrised by
$\bar a\,\tfrac{e_b}2+\bar b\,\tfrac{f_b}2+\bar c\,\tfrac{D_b}2$:
* $\tfrac12e_b,\ \tfrac12f_b$ are integral with square $0$;
* $\tfrac12(e_b+f_b)$ has square $\tfrac14(e_b+f_b)^2=1$, **odd**, so it is not in the even lattice
  $L$ (this is the class that would generate the third overlattice of $\Lambda\otimes\mathbb Q$);
* every class involving $\tfrac12D_b$ has square $\equiv-\tfrac12$, not integral.
This is the provider's output at pin `c546077d` ((P): "integral-valued nonzero half-classes
$(a,b,c,q)$: $[(0,1,0,0),(1,0,0,0)]$; generated overlattice det would be 2"), and it is three lines of
integer arithmetic. So, with unimodularity of $L$ and primitivity of $e_b,f_b$,
$$[S_{\mathrm{dP},b}:\Lambda]=2\quad\Longleftrightarrow\quad
\tfrac12e_b\in L\ \text{ or }\ \tfrac12f_b\in L .$$
(Equivalently: some integral class pairs oddly with $e_b$, since every element of $\Lambda$ pairs
evenly with $e_b$ — the question isolated in (A) `rmk:a21-scope`.)

---

## 2. First proof: the classification of non-symplectic involutions (**new**)

The tool is Nikulin's classification of 2-elementary K3 surfaces: for a non-symplectic involution
$\iota$ of a K3 with invariant lattice $L^+$ of rank $r$, discriminant group $(\mathbb Z/2)^a$ and
parity $\delta$, the fixed locus is empty iff $(r,a,\delta)=(10,10,0)$, the disjoint union of two
elliptic curves iff $(r,a,\delta)=(10,8,0)$, and otherwise a curve of genus $g$ together with $k$
rational curves, where
$$g=\frac{22-r-a}{2},\qquad k=\frac{r-a}{2};$$
furthermore $(r,a,\delta)$ together with the signature determines the isometry class of $L^+$
(Rudakov–Shafarevich), and $\delta=0$ iff the class of the fixed locus is divisible by $2$ in
$H^2(X,\mathbb Z)$. Source: V. V. Nikulin, *Factor groups of groups of automorphisms of hyperbolic
forms…*, 1979, §4, Theorem 4.2.2, and *Discrete reflection groups in Lobachevsky spaces and algebraic
surfaces*, §4; the statement with exactly these formulas, the $\delta$-criteria and the table is
reproduced in M. Artebani, S. Boissière, A. Sarti, *The Berglund–Hübsch–Chiodo–Ruan mirror symmetry
for K3 surfaces*, §4.1 and Theorem 4.1 (read at
`sarti.pages.math.cnrs.fr/home/ArtebaniBoissiereSarti_1dec2013.pdf`).

> **Theorem (O-S, classification proof).** $S_{\mathrm{dP},b}\cong U(2)\perp\langle-2\rangle=\Lambda$
> and $\det S_{\mathrm{dP},b}=8$.

*Proof.* $I_{\mathrm{dP}}$ is non-symplectic ((A) `prop:local-operators`(2)), so $L^+$ is
2-elementary and the classification applies. Its fixed locus is $\widetilde B$, a **single smooth
curve of genus $8$** — neither empty nor two elliptic curves, and "a curve of genus $g=8$ together
with $k=0$ rational curves". Inverting the two formulas,
$$r=11-g+k=3,\qquad a=11-g-k=3 .$$
The value $r=3$ reproduces the corpus's Lefschetz count $r=k_{\text{nodes}}+2$ at
$k_{\text{nodes}}=1$ — a check, not an input. So $A_{S_{\mathrm{dP}}}\cong(\mathbb Z/2)^3$,
$|\det S_{\mathrm{dP}}|=2^3=8$, signature $(1,2)$, and $\delta=1$: indeed $\widetilde B^{\,2}=2g-2=14$,
so were $\widetilde B=2\gamma$ with $\gamma\in L$ we would get $\gamma^2=\tfrac{14}4\notin\mathbb Z$,
against evenness of $L$; hence the fixed class is not divisible by $2$ and $\delta=1$ (this also
follows from $a=3$ odd). An even 2-elementary lattice is determined by
$(r,a,\delta,\text{signature})$, and $U(2)\perp\langle-2\rangle$ has $(3,3,1)$ and signature
$(1,2)$. Therefore $S_{\mathrm{dP},b}\cong U(2)\perp\langle-2\rangle$; as $|\det|=8$ and
$\Lambda\subseteq S_{\mathrm{dP},b}$ with $\det\Lambda=8$, the index is $1$. $\square$

Two consequences worth recording: the answer is *member-independent* (it uses only the number of
nodes at $\tau$-fixed points and the genus of the normalization of the branch curve), and the
index-$2$ candidate is excluded by $a=3$, not by a square-norm bound.

**2.1 The $k=0$ case.** For a smooth branch curve, $\operatorname{Fix}(I_{\mathrm{dP}})$ is a smooth
curve of genus $9$, so $(r,a)=(2,2)$, and $a=2$ forces $\delta=0$; the unique such lattice of
signature $(1,1)$ is $U(2)$. This decides the binary which (A) `rmk:a21-open` records as open at
$k=0$ ("the invariant lattice is $U(2)$ or $U$"): it is $U(2)$.

**2.2 Two nodes at $\tau$-fixed points.** $\operatorname{Fix}(I_{\mathrm{dP}})$ has genus $7$, so
$(r,a)=(4,4)$ and $\det S_{\mathrm{dP}}=\pm16$; if $\delta=1$ (as (A) `rmk:a21-open` expects) then
$S_{\mathrm{dP}}\cong U(2)\perp\langle-2\rangle^{\oplus2}$. (I do not decide $\delta$ here; nothing
in the one-node obligation depends on it.)

---

## 3. Second proof: no half of a ruling class is integral (**new**, and ampleness-free)

> **Lemma 3.1.** Let $F\in\{e_b,f_b\}$. Then $\tfrac12F\notin H^2(\widehat X_b,\mathbb Z)$.

*Proof.* Suppose $\gamma\in L$ with $2\gamma=F$.
(i) $\gamma$ is a rational $(1,1)$-class (as $F$ is), so $\gamma\in\operatorname{Pic}(\widehat X_b)$;
and $\gamma^2=0$, $\gamma\cdot F=0$.
(ii) Riemann–Roch on a K3 gives $\chi(\mathcal O(\gamma))=2+\tfrac12\gamma^2=2$, and Serre duality
gives $h^2(\gamma)=h^0(-\gamma)$, $h^1(\gamma)=h^1(-\gamma)$; hence
$h^0(\gamma)+h^0(-\gamma)=2+2h^1(\gamma)\ge2$, so $\gamma$ or $-\gamma$ is effective.
(iii) Let $D\ge0$, $[D]=\pm\gamma$. Since $D\cdot F=0$ and $F$ is nef (it is the class of the
connected fibres of $\varphi_{|F|}\colon\widehat X_b\to\mathbb P^1$, the pullback of a ruling pencil
by (A) `lem:face-at-H`(1)), every irreducible component $C$ of $D$ satisfies $0\le C\cdot F\le D\cdot F=0$,
so $C\cdot F=0$, so $\varphi(C)$ is a point: every component is vertical.
(iv) Write $D=\sum_t D_t$ with $D_t$ supported on the fibre over $t$, finitely many $t$. Distinct
fibres are disjoint, so $0=D^2=\sum_t D_t^2$; each $D_t^2\le0$, because the components of a
connected fibre of a fibration by curves are smooth rational (here: double covers of ruling lines,
and for the line through $p$ the two components described below) with each $C^2=-2$ by adjunction on
a K3, and the intersection matrix of a connected reduced fibre is negative semidefinite with
$1$-dimensional radical spanned by the fibre class; hence every $D_t^2=0$ and $D_t\in\mathbb Q\cdot F$.
(v) Each fibre of $|F|$ is **reduced**: it is $\pi_b^{-1}$ of a ruling line, a double cover branched
at $F\cdot\widetilde B=4$ points (for the line through $p$: the proper transform of that line gives a
two-point branched cover, plus $D_b$ meeting it in $2$ points, and both components have multiplicity
$1$). With all multiplicities $1$, the fibre is $E_t=\sum_j C_j$ and the relation space of
$\{C_j\}$ is $\mathbb Z\cdot(1,\dots,1)$; so $D_t=c_tF$ with $c_t\in\mathbb Z_{\ge0}$, and $D_t\ne0$
gives $c_t\ge1$.
(vi) Then $[D]=\sum_t c_tF=(\sum_t c_t)F$, and comparing with $[D]=\pm\tfrac12F$ gives
$\sum_tc_t=\pm\tfrac12$ with all $c_t\ge1$ — absurd. $\square$

> **Corollary 3.2.** $[S_{\mathrm{dP},b}:\Lambda]=1$ for every such member.

*Proof.* By §1.3 the index could be $2$ only if $\tfrac12e_b$ or $\tfrac12f_b$ were integral; Lemma
3.1 excludes both. $\square$

Remarks. (a) Unlike the section argument of §4 this needs no ampleness of $\widetilde B$; unlike the
classification of §2 it needs no classification theorem. (b) The one non-elementary input is the
standard negative-semidefiniteness of the fibre-component intersection matrix; it can be replaced by
the direct check $C_j^2=-2$ (adjunction), $C_j\cdot C_{j'}\ge0$, $(\sum_jC_j)^2=0$ with connected
support, which makes the matrix an affine Cartan matrix. (c) The same argument applies verbatim to
the smooth-branch ($k=0$) member, and to both rulings.

---

## 4. Third proof: the corpus's own route, completed (member m5's; verified here)

The argument in `.ultramath/smw0dbvr6/m5/O-S-saturation.md` §3, which I checked step by step:
if $w\in\operatorname{Pic}$ had $w\cdot F=1$ ($F\in\{e_b,f_b\}$), then for $n\gg0$ the class
$\mathcal O(w+nF)$ has $h^0\ge1$ by Riemann–Roch ($h^0(-L_n)=0$ since $L_n\cdot F=1$), and its
effective representative has exactly one non-vertical component $C_0$ of degree $1$ over the base,
which is therefore a section $C_0\cong\mathbb P^1$ of $\varphi_{|F|}$; its image
$D=\pi_b(C_0)\subset\widehat Y$ then has $\deg\pi_b|_{C_0}=\deg(p_1|_D)=1$ and
$\pi_b^{-1}(D)\to D$ is a connected double cover branched along $D\cap\widetilde B$; a section being
a component forces $D\cap\widetilde B=\varnothing$, i.e. $D\cdot\widetilde B=0$, contradicting
ampleness of $\widetilde B=-2K_{\widehat Y}$ ($\widehat Y$ is the degree-$7$ del Pezzo surface
$\operatorname{Bl}_p(\mathbb P^1\times\mathbb P^1)$). Hence no algebraic class of odd degree over a
ruling exists, and by §1.3 the index is $1$. This is correct and independent of §2–§3. Its only
geometric inputs are ampleness of $-K_{\widehat Y}$ and the connectedness of a branched double cover;
both hold. (It also explains why (A) `rmk:a21-scope`'s own elimination of linear classes
$D=ah_1+h_2+ce$ of square $\ge-2$ was not yet a proof: a class of odd degree need be neither
effective nor of square $\ge-2$, and "sections do not exist" needs ampleness, not a square bound.)

---

## 5. What this settles elsewhere

1. **The corpus's open binary at $k=0$** is decided: $S_{\mathrm{dP}}\cong U(2)$, not $U$ (§2.1).
2. **$D_b$ is primitive of divisibility $2$** in $L$: $D_b=\pi_b^*e$ with $e$ primitive, and
   $D_b\notin2L$ by $D_b^2=-2$; consistently $(A)$ `lem:face-at-H`(1).
3. **Input to O-T.** $S_{\mathrm{dP},b}=\Lambda$ is used in my `O-T-twist-identification.md` §3.3 and
   §6 only through the identity $S_{\mathrm{Co},b}=\Lambda\perp E_8(-2)$, which is proved there from
   the type of $S_{\mathrm{Co},b}$ and does not need §2–§4 beyond $S_{\mathrm{dP}}\subseteq S_{\mathrm{Co}}$
   (which (A) `rmk:a21-open` and every route here give).

---

## 6. What is *not* claimed, and what remains open near this question

* No statement about chambers, effective cones, the A21 chamber clause
  ((A) `prob:effective-cone-agreement`), or about (A) `rmk:a21-open`'s slot: this document concerns
  only the saturation of $\Lambda$ in $S_{\mathrm{dP}}$.
* No claim about $\operatorname{Pic}(\widehat X_b)$ beyond the trivial sandwich: if a member had
  Picard rank $3$, then $\operatorname{Pic}=S_{\mathrm{dP}}=\Lambda$; by (R) and the corpus's
  preserved facts every member has Picard rank $\ge11$, so that case is vacuous here and is not used.
* No chamber/translation-invariance detector and no integral eigensplitting is used anywhere.
* The **exact remaining sharp question** of (O-S): there is none for the determinant. The nearest
  genuinely open binary is the *type of the Coble slot*, which is not part of (O-S); it is settled in
  my companion document `O-T-twist-identification.md` §3 (it is
  $U(2)\perp E_8(-2)\perp\langle-2\rangle$, i.e. (R)'s hypothesis `H1` is a theorem), and the types of
  the two eigenlattices together give the "matching piecewise data" of (A) `prob:twist-identification`.
