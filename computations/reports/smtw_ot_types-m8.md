# O-T — twist identification: the piecewise type data are **proved**, the pair **fails**

Member m8, direction d7, swarm `smw0dbvr6`. Repository
`/workspace/nucleus/work/projects/p-9fcb4ed7f4b64e008de2ee29a7197bf4/repo` (read-only),
evidence state `main@141058a8`. Citations by block id of

* **(A)** `writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md`,
* **(H)** `writing/coble/heegner-report/coble-heegner-research-report.md`,
* **(R)** `computations/reports/sm00_arithmetic-core.md` (where the type of $S_{\mathrm{Co}}$ is
  carried as the *hypothesis* `H1`).

## 0. Outcome, in two sentences

1. **The matching piecewise data asked for in (A) `prob:twist-identification` are now theorems,
   not hypotheses.** For every member $b$ of the direct-projective construction with one node at a
   $\tau$-fixed point,
   $$S_{\mathrm{Co},b}\cong U(2)\perp E_8(-2)\perp\langle-2\rangle\;=\;S_{\mathrm{Co}}^{\text{twist}}
   \qquad(\text{rank }11,\ \det 2048,\ a=11,\ \delta=1),$$
   $$T_{\mathrm{Co},b}=S_{\mathrm{Co},b}^{\perp}\cong \langle2\rangle\perp U(2)\perp E_8(-2)\;=\;
   T_{\mathrm{Co}}^{\text{twist}}\qquad(\text{rank }11,\ \det -2048,\ a=11,\ \delta=1),$$
   so corpus hypothesis `H1` of (R) is a theorem (§3), and the Coble slot of the construction is
   *isometric* to the twist's Coble slot, including the sign of the determinant and $\delta$.
2. **Nevertheless the pair $(I_{\mathrm{Co},b},I_{\mathrm{dP},b})$ is *not* $O(L_{K3})$-conjugate to
   the twist pair $(I_{\mathrm{Co}}^{\text{twist}},I_{\mathrm{En}})$**, and the separating invariant
   is *not* in the Coble slot but in the second factor and in the joint $({\mathbb Z}/2)^2$
   decomposition: with the correspondence $I_{\mathrm{Co},b}\leftrightarrow I_{\mathrm{Co}}^{\text{twist}}$,
   $I_{\mathrm{dP},b}\leftrightarrow I_{\mathrm{En}}$ the multiplicity tables are $(3,8,0,11)$ versus
   $(10,1,0,11)$, and the sharpest integral witness is the product's anti-invariant lattice, of rank
   $8$ against $1$. §4 re-derives
   the construction's table from the corpus's own fixed-point counts and §5 verifies the twist's.
   This confirms, by an independent route, the negative answer recorded by member m2
   (`.ultramath/smw0dbvr6/m2/O-T-twist-identification.md`); what is new here is item 1 and the
   isolation of the failure.

Nothing below uses an integral eigensplitting of $H^2(X,\mathbb Z)$, a chamber detector, or a
translation-invariance claim. All use of $H^2\otimes\mathbb Q$ is via *ranks of kernels of integral
endomorphisms*, and all integrality statements are about lattices.

---

## 1. The two sides, and what "the twist pair" is

**1.1 The construction** ((A) `prop:one-node-family`, `prop:local-operators`,
`prop:del-pezzo-type-on-the-resolution`, `prop:tuple-of-the-construction`; proofs re-read).
Let $Y=\mathbb P^1\times\mathbb P^1$, $\tau(x,y)=(-x,-y)$, $\mathcal L=\mathcal O_Y(2,2)$,
$f\in H^0(\mathcal L^2)^\tau$ with exactly one node, at a $\tau$-fixed point $p$, and otherwise
smooth with nondegenerate quadratic part. Put
$$X^\sharp=\{z^2=f\}\to Y,\qquad \beta\colon \widehat X_b\to X^\sharp\ \text{the resolution of the node},\qquad
\pi_b\colon\widehat X_b\to\widehat Y=\operatorname{Bl}_pY .$$
$\widehat X_b$ is a K3, $\pi_b$ is a finite degree-$2$ cover branched along the smooth proper
transform $\widetilde B\in|-2K_{\widehat Y}|$ of $B=\{f=0\}$ ((A) `lem:face-at-H`(1)), and
$$I_{\mathrm{dP}}\colon z\mapsto -z\ (\text{the deck transformation}),\qquad
I_{\mathrm{Co}}\colon (z,x,y)\mapsto(-z,-x,-y),\qquad
\rho:=I_{\mathrm{Co}}I_{\mathrm{dP}}\colon (z,x,y)\mapsto(z,-x,-y).$$
$I_{\mathrm{Co}}$ and $I_{\mathrm{dP}}$ are nonsymplectic, $\rho$ is symplectic
((A) `prop:local-operators`(2)). The labels are $H=\pi_b^*\mathcal O_Y(1,1)$ ($H^2=4$) and
$\alpha=[D_b]=\pi_b^*e$ (the exceptional $(-2)$-curve), and
$$\Lambda:=\langle e_b,f_b,D_b\rangle,\quad e_b=\pi_b^*h_1,\ f_b=\pi_b^*h_2,\quad
\Lambda\cong U(2)\perp\langle-2\rangle,\ \det\Lambda=8 .$$
Fixed loci ((A) `prop:local-operators`, `prop:del-pezzo-type-on-the-resolution`):
$$\operatorname{Fix}(I_{\mathrm{dP}})=\widetilde B\ \text{(smooth, genus }8),\qquad
\operatorname{Fix}(I_{\mathrm{Co}})=D_b\cong\mathbb P^1,\qquad
\operatorname{Fix}(\rho)=\text{8 points}.$$

**1.2 The twist.** (H) `cons:reflection-twist` defines *one* involution
$I_{\mathrm{Co}}:=w_\alpha I_{\mathrm{En}}$ on $L_{K3}$, with $\alpha=e-f$ a root of the first
$U\subset T_{\mathrm{En}}$; (H) `prop:coble-eigenspaces` computes its eigenlattices integrally.
The corpus's `cons:reflection-twist` names no second involution, so "the twist pair" of
(A) `prob:twist-identification` can only be $(I_{\mathrm{Co}}^{\text{twist}},I_{\mathrm{En}})$ — the
twist's own involution paired with the Enriques involution it is built from. That is the reading
used here; §6 records what an alternative partner would have to satisfy and why no alternative can
rescue the identification.

---

## 2. The invariants used

**2.1 Multiplicities.** For two commuting involutions $i_1,i_2$ of a rank-$22$ lattice $L$, put
$n(\varepsilon,\delta')=\operatorname{rk}_\mathbb Q\{x\in L\otimes\mathbb Q: i_1x=\varepsilon x,\
i_2x=\delta' x\}$. The function $n$ is an $O(L)$-conjugacy invariant of the pair (the joint
eigenspaces are kernels of integral endomorphisms), and it is computed from traces by
$$4n(+,+)=22+\operatorname{tr}i_1+\operatorname{tr}i_2+\operatorname{tr}(i_1i_2),\quad
4n(+,-)=22+\operatorname{tr}i_1-\operatorname{tr}i_2-\operatorname{tr}(i_1i_2),$$
$$4n(-,+)=22-\operatorname{tr}i_1+\operatorname{tr}i_2-\operatorname{tr}(i_1i_2),\quad
4n(-,-)=22-\operatorname{tr}i_1-\operatorname{tr}i_2+\operatorname{tr}(i_1i_2).$$
**2.2 Traces.** For an involution $g$ of a K3 with $\operatorname{Fix}(g)$ a disjoint union of
points and smooth curves, $\operatorname{tr}(g|H^2)=\chi(\operatorname{Fix} g)-2$ (Lefschetz;
$H^1=H^3=0$). For an integral lattice involution $g$,
$\operatorname{tr}g=2\operatorname{rk}L^{g=+1}-22$.

---

## 3. The two types, proved: `H1` is a theorem

Let $L=H^2(\widehat X_b,\mathbb Z)$. The tool is Nikulin's classification of 2-elementary K3
surfaces, in the form quoted and used in the literature: for a non-symplectic involution $\iota$ of
a K3 with invariant lattice $L^+$ of rank $r$, discriminant group $(\mathbb Z/2)^a$ and parity
$\delta$ ($\delta=0$ iff $x^2\in\mathbb Z$ for all $x\in(L^+)^\vee$), the fixed locus is

* empty iff $(r,a,\delta)=(10,10,0)$;
* two elliptic curves iff $(r,a,\delta)=(10,8,0)$;
* otherwise a curve of genus $g$ together with $k$ rational curves, where
  $$g=\tfrac{22-r-a}{2},\qquad k=\tfrac{r-a}{2};$$

equivalently $r=11-g+k$ and $a=11-g-k$; and $(r,a,\delta)$ together with the signature determines
the isometry class of $L^+$. (V. V. Nikulin, *Factor groups of groups of automorphisms of
hyperbolic forms…*, 1979, §4, Theorem 4.2.2, and *Discrete reflection groups in Lobachevsky spaces
and algebraic surfaces*, §4; the statement with these formulas and the $\delta$-criterion is
reproduced in M. Artebani, S. Boissière, A. Sarti, *The Berglund–Hübsch–Chiodo–Ruan mirror symmetry
for K3 surfaces*, §4.1 and Theorem 4.1, which I read at
`sarti.pages.math.cnrs.fr/home/ArtebaniBoissiereSarti_1dec2013.pdf`.)

**3.1 Theorem (type of $S_{\mathrm{Co},b}$; `H1` of (R)).**
$S_{\mathrm{Co},b}:=L^{I_{\mathrm{Co}}=+1}\cong U(2)\perp E_8(-2)\perp\langle-2\rangle$:
rank $11$, signature $(1,10)$, $\det 2048$, $A_{S_{\mathrm{Co}}}\cong(\mathbb Z/2)^{11}$,
$\delta=1$. In particular $|A_{S_{\mathrm{Co}}}|=2^{11}$ and
$[S_{\mathrm{Co}}\oplus T_{\mathrm{Co}}:L]=2^{11}$ — the numbers (H) `prop:coble-eigenspaces`
computes for the twist, now for the construction.

*Proof.* $I_{\mathrm{Co}}$ is non-symplectic ((A) `prop:local-operators`(2)), so $S_{\mathrm{Co}}$ is
2-elementary and the classification applies.
*(i) Fixed locus.* $\operatorname{Fix}(I_{\mathrm{Co}})=D_b$ is a single smooth rational curve
((A) `prop:local-operators`(4) with `prop:del-pezzo-type-on-the-resolution`(1)) and there are no
isolated fixed points. This is neither the empty case nor the two-elliptic-curve case, and it is
"a curve of genus $g=0$ together with $k=0$ rational curves".
*(ii) $(r,a)$.* The formulas invert: $r=11-g+k=11$ and $a=11-g-k=11$. The value $r=11$ reproduces
the corpus's independent Lefschetz count $r=k+10$ ((A) `prop:tuple-of-the-construction`(5)) at
$k=1$; that agreement is a check, not an input.
*(iii) $\delta$.* By the divisibility criterion, $\delta=0$ iff the class of the fixed locus is
divisible by $2$ in $L$. Here the fixed class is $\alpha=[D_b]$, $\alpha^2=-2$; if $\alpha=2\gamma$
with $\gamma\in L$ then $\gamma^2=-1/2\notin\mathbb Z$, since $L$ is even. So $\alpha\notin2L$ and
$\delta=1$. (Same conclusion by lattice arithmetic: $a=11$ is odd, and $\delta=0$ forces $a$ even
because the discriminant form of a $2$-elementary lattice with $\delta=0$ is a sum of hyperbolic
planes.)
*(iv) Isometry type.* An even 2-elementary lattice is determined by
$(r,a,\delta,\text{signature})$ (Rudakov–Shafarevich; quoted in the source above), the signature
being $(1,r-1)=(1,10)$ for a non-symplectic involution. The lattice
$U(2)\perp E_8(-2)\perp\langle-2\rangle$ has rank $11$, signature $(1,10)$,
$|A|=2\cdot2^2\cdot 2^8=2^{11}$, $\delta=1$ (its $\langle-2\rangle$ summand gives
$q(\alpha/2)=-1/2\notin\mathbb Z/2\mathbb Z$). Hence $S_{\mathrm{Co},b}$ is isometric to it.
$\square$

**3.2 Corollary (type of $T_{\mathrm{Co},b}$).** For a 2-elementary invariant lattice $S$ of a
non-symplectic involution, $T=S^{\perp}$ is 2-elementary with the same $a$ and $\delta$ (Nikulin's
duality for the invariant/anti-invariant pair; also (H) `prop:coble-eigenspaces`, where the same
computation is made for the twist). So $T_{\mathrm{Co},b}$ has rank $11$, signature $(2,9)$, $a=11$,
$\delta=1$, and is therefore the even 2-elementary lattice
$\langle2\rangle\perp U(2)\perp E_8(-2)$ with $\det-2048$ — the twist's $T_{\mathrm{Co}}$ (the
correction recorded in `.ultramath/smvz57fr3/m4/report.md` §3(b): it is *even*, and the label
$I_{2,9}(2)$ is to be read with the signature).
$\square$

**3.3 Corollary ($S_{\mathrm{Co}}=\Lambda\perp E_8(-2)$; and $k=0$).**
(a) Since $\Lambda\subseteq S_{\mathrm{Co}}$ ((A) `rmk:a21-open`) and $|A_{S_{\mathrm{Co}}}|=2^{11}
=|\det\Lambda|\cdot|\det E_8(-2)|$, no half-class survives; in the sharp form: the $(+,-)$-eigenspace
of $\rho$ is a primitive rank-$8$ sublattice of $T_\rho$ with the same $\mathbb Q$-span, hence equals
$T_\rho$, which is therefore an even negative definite 2-elementary lattice of rank $8$ with
$a=8$, i.e. $E_8(-2)$; and $\Lambda\perp T_\rho\subseteq S_{\mathrm{Co}}$ with equal ranks and equal
discriminant order, so
$$S_{\mathrm{Co},b}=\Lambda\perp E_8(-2)\;=\;S_{\mathrm{dP},b}\perp E_8(-2).$$
(b) At $k=0$ (smooth branch curve) $\operatorname{Fix}(I_{\mathrm{Co}})=\varnothing$ — the
Enriques case — so $(r,a,\delta)=(10,10,0)$ and $S_{\mathrm{Co}}\cong U(2)\perp E_8(-2)$, not $U$:
this decides the binary which (A) `rmk:a21-open` records as open at $k=0$.
$\square$

The two facts of §3 are the whole content of "the matching piecewise data" of
(A) `prob:twist-identification` on the Coble side.

---

## 4. The construction's multiplicity table (re-derived)

By §2.2 and the fixed loci of §1.1, with $k=1$:
$$\operatorname{tr}(I_{\mathrm{Co}})=\chi(D_b)-2=2-2=0,\qquad
\operatorname{tr}(I_{\mathrm{dP}})=\chi(\widetilde B)-2=(2-2\cdot8)-2=-16,\qquad
\operatorname{tr}(\rho)=\chi(8\text{ points})-2=8-2=6 .$$
Then, with $i_1=I_{\mathrm{Co}}$, $i_2=I_{\mathrm{dP}}$,
$$n(+,+)=\tfrac{22+0-16+6}{4}=3,\quad n(+,-)=\tfrac{22+0+16-6}{4}=8,\quad
n(-,+)=\tfrac{22-0-16-6}{4}=0,\quad n(-,-)=\tfrac{22-0+16+6}{4}=11 .$$
Checks, none of which uses an eigensplitting: $n(+,+)=\operatorname{rk}(S_{\mathrm{Co}}\cap S_{\mathrm{dP}})
=3$ (the corpus computes this rank geometrically, (A) `rmk:a21-open`); $n(+,+)+n(+,-)=11
=\operatorname{rk}S_{\mathrm{Co}}$; $n(+,+)+n(-,+)=3=\operatorname{rk}S_{\mathrm{dP}}$;
$n(+,+)+n(-,-)=14=\operatorname{rk}S_\rho=\tfrac12(\chi(\operatorname{Fix}\rho)+20)$;
$n(+,-)+n(-,+)=8=\operatorname{rk}T_\rho$. In particular $n(-,+)=0$ reproves
$S_{\mathrm{dP}}\subseteq S_{\mathrm{Co}}$ without the primitivity argument of (A) `rmk:a21-open`.

---

## 5. The twist's multiplicity table

With $i_1=I_{\mathrm{Co}}^{\text{twist}}=w_\alpha I_{\mathrm{En}}$, $i_2=I_{\mathrm{En}}$, where
$w_\alpha$ is the reflection in the root $\alpha=e-f$ and $S_{\mathrm{En}}\perp\alpha$
((H) `prop:coble-eigenspaces`): for $x\in S_{\mathrm{En}}$, $w_\alpha x=x$ because
$\alpha\perp S_{\mathrm{En}}$, so $S_{\mathrm{En}}\subseteq L_{+,+}$ and, both being kernels,
$L_{+,+}=S_{\mathrm{En}}$, $n(+,+)=10$. Next $\alpha\in S_{\mathrm{Co}}$ (as
$I_{\mathrm{Co}}w_\alpha=\mathrm{id}$ on $\alpha$) and $\alpha\in T_{\mathrm{En}}$ (as
$I_{\mathrm{En}}\alpha=-\alpha$), so $L_{+,-}=S_{\mathrm{Co}}\cap T_{\mathrm{En}}=\mathbb Z\alpha$ and
$n(+,-)=1$; and $L_{-,+}=T_{\mathrm{Co}}\cap S_{\mathrm{En}}=0$, since $S_{\mathrm{En}}\subset S_{\mathrm{Co}}$
and $S_{\mathrm{Co}}\cap T_{\mathrm{Co}}=0$ over $\mathbb Q$. Finally $T_{\mathrm{Co}}\subseteq T_{\mathrm{En}}$
(resp. $T_{\mathrm{Co}}=\alpha^{\perp}_{T_{\mathrm{En}}}$), so $L_{-,-}=T_{\mathrm{Co}}$ and
$n(-,-)=11$. Sum $10+1+0+11=22$ ✓.
Trace check: $\operatorname{tr}I_{\mathrm{Co}}^{\text{twist}}=0$ ($\operatorname{rk}S_{\mathrm{Co}}=\operatorname{rk}T_{\mathrm{Co}}=11$),
$\operatorname{tr}I_{\mathrm{En}}=-2$, $\operatorname{tr}w_\alpha=20=22-2$, and the formulas of §2.1 return
$(10,1,0,11)$.
In the reversed ordering $(i_1,i_2)=(I_{\mathrm{En}},I_{\mathrm{Co}}^{\text{twist}})$ the same four
spaces give $(10,0,1,11)$; the multiset is $\{10,1,0,11\}$ in either case, and
$\operatorname{rk}S_{\mathrm{Co}}^{\text{twist}}=10+1=11$, $\operatorname{rk}S_{\mathrm{En}}=10$,
$\operatorname{rk}T_{w_\alpha}=0+1=1$.

---

## 6. The separation, and where the failure is *not*

**6.1 Theorem (no pair conjugacy).** There is no $\varphi\in O(L_{K3})$ with
$\varphi I_{\mathrm{Co},b}\varphi^{-1}=I_{\mathrm{Co}}^{\text{twist}}$ and
$\varphi I_{\mathrm{dP},b}\varphi^{-1}=I_{\mathrm{En}}$; nor with the two labels interchanged.

*Proof.* A conjugacy of pairs carries joint eigenspaces to joint eigenspaces (§2.1), so it preserves
$n$. In the correspondence $I_{\mathrm{Co},b}\leftrightarrow I_{\mathrm{Co}}^{\text{twist}}$,
$I_{\mathrm{dP},b}\leftrightarrow I_{\mathrm{En}}$ the tables are $(3,8,0,11)$ (§4) and $(10,1,0,11)$
(§5); they already differ in the $(+,+)$ entry ($3\ne10$) and in the $(+,-)$ entry ($8\ne1$).
Under the only other correspondence $I_{\mathrm{Co},b}\leftrightarrow I_{\mathrm{En}}$,
$I_{\mathrm{dP},b}\leftrightarrow I_{\mathrm{Co}}^{\text{twist}}$ the construction's table reads
$(3,0,8,11)$ and the twist's $(10,0,1,11)$ — again different in the $(+,+)$ entry and in the $(-,+)$
entry. $\square$
(This is the same separation as member m2's; the numbers are re-derived here from the corpus's own
counts, and both routes agree.)

**6.2 The sharpest witness, and its integral form.** The product is part of the pair's structure, so
$\operatorname{rk}$ of its $(-1)$-eigenspace is an invariant of the pair under either correspondence:
$$22-14=8\quad\text{(construction: }T_\rho=E_8(-2)\text{, by §3.3)}\qquad\text{versus}\qquad
22-21=1\quad\text{(twist: }w_\alpha\text{ is a reflection, }T=\mathbb Z\alpha\cong\langle-2\rangle).$$
Ranks $8\ne1$ separate the lattices, so no isometry of the products' eigenspaces exists either.

**6.3 Not the Coble slot.** By §3 the two Coble slots are *isometric*:
$S_{\mathrm{Co},b}\cong S_{\mathrm{Co}}^{\text{twist}}$ with the same $(r,a,\delta,\text{signature})$
and the same determinant sign, and likewise for the anti-invariant lattices. So the failure of
(A) `prob:twist-identification` is **not** a failure of the piecewise lattice types on the Coble side.
It is located in (i) the second involution — $\operatorname{rk}S_{\mathrm{dP},b}=3$ ($\Lambda$,
(A) `prop:tuple-of-the-construction`) against $\operatorname{rk}S_{\mathrm{En}}=10$ — and (ii) the
joint decomposition, in the form of 6.2. In particular the statement "the construction's del Pezzo
slot is the orthogonal summand $U(2)\perp\langle-2\rangle$ of the twist's Coble slot" is now a
theorem with no index left over: by §3.3, $S_{\mathrm{Co},b}=\Lambda\perp E_8(-2)$ and
$S_{\mathrm{Co}}^{\text{twist}}=U(2)\perp\langle-2\rangle\perp E_8(-2)$.

**6.4 The placement of $H$ and of $\alpha$.** Both labels lie in $\Lambda=S_{\mathrm{dP},b}$, which is
the $(+,+)$-eigenspace of $(I_{\mathrm{Co},b},I_{\mathrm{dP},b})$: $H=\pi_b^*\mathcal O(1,1)$ is a
pullback and $\alpha=[D_b]$ is fixed pointwise by $I_{\mathrm{Co}}$ and preserved by $I_{\mathrm{dP}}$
((A) `rmk:a21-open`). For the twist, $I_{\mathrm{En}}\alpha=-\alpha$ and $w_\alpha\alpha=-\alpha$, so
$I_{\mathrm{Co}}^{\text{twist}}\alpha=+\alpha$: the twist's root spans the $1$-dimensional eigenspace
in which the Coble involution acts by $+1$ and the other by $-1$ (the $(+,-)$-eigenspace in the
ordering $(I_{\mathrm{Co}},I_{\mathrm{En}})$, the $(-,+)$ one in the reversed ordering). The requirement
of (A) `prob:twist-identification` that "$\alpha$ maps to $\pm$ the twist's root" would therefore have
to carry the construction's rank-$3$ $(+,+)$-eigenspace onto a rank-$1$ space, and it would put the
root in different characters on the two sides; the correspondence that matches the root's character
fails already at $n(+,+)=3\ne10$. $H$ alone separates nothing: $H^2=4$ is represented in $S_{\mathrm{En}}$
by $(h_1+h_2)^2=4$.

**6.5 No alternative partner rescues it.** If a pair $(I_{\mathrm{Co}}^{\text{twist}},\;g)$ with
$g$ an involution commuting with $I_{\mathrm{Co}}^{\text{twist}}$ were conjugate to the
construction's pair, then $I_{\mathrm{Co}}^{\text{twist}}g$ would be conjugate to $\rho$, so its
$(-1)$-eigenspace would have rank $8$. But a geometric involution of a K3 never has a $1$-dimensional
anti-invariant lattice: if it is nonsymplectic then
$H^{2,0}\oplus H^{0,2}\subseteq T\otimes\mathbb C$ forces $\operatorname{rk}T\ge2$; if it is
symplectic then $T\subseteq H^{1,1}$, its fixed points are isolated with $dg_p=-\mathrm{id}$, the
holomorphic Lefschetz formula gives $|\operatorname{Fix}|=8$ and the topological one gives
$\operatorname{tr}=6$, i.e. $\operatorname{rk}T=8$. So no partner at all can have product
$w_\alpha$ (whose anti-invariant lattice is the rank-$1$ $\mathbb Z\alpha$); in particular the
corpus's twist pair, built from a reflection, is not the cohomological action of a geometric pair,
and (A) `prob:twist-identification` is false as stated, not merely open. What a *hypothetical*
different partner would need is $\operatorname{tr}(I_{\mathrm{Co}}^{\text{twist}}g)=14-8=6$ together
with $g\alpha=\alpha$; since $I_{\mathrm{Co}}^{\text{twist}}$ and $I_{\mathrm{En}}$ generate the
$2$-elementary symmetry of the pair $(S_{\mathrm{Co}},T_{\mathrm{Co}})$ computed in (H)
`prop:coble-eigenspaces`, no such $g$ is produced anywhere in the corpus, and the question is not
one this document settles.

---

## 7. What is claimed, what is not

* Claimed: §3 (the two types, hence `H1`), §3.3, §4 (the construction's table, re-derived from the
  corpus's fixed loci), §6.1–6.5. These are proofs from (i) the corpus's proven fixed-locus
  statements, (ii) Nikulin's classification in the exact form quoted in §3, (iii) elementary trace
  algebra.
* Not claimed: any statement about chambers, effective cones, or the A21 chamber clause
  ((A) `prob:effective-cone-agreement`) — untouched. No claim that the construction's tuple fails
  A21: the labels clauses of A21 are about tuples of the construction, and §6 speaks only about the
  comparison with the twist model.
* Not claimed: uniqueness of the primitive embedding. §3 gives isometric eigenlattices; the passage
  to $O(L_{K3})$-conjugacy of the *single* involution $I_{\mathrm{Co},b}\sim I_{\mathrm{Co}}^{\text{twist}}$
  needs the uniqueness of the embedding of a 2-elementary lattice with $r=\operatorname{rk}S^{\perp}=11$,
  which is a boundary case of Nikulin's uniqueness theorem and is not verified here. Nothing in §6
  depends on it.
* Dependence on other members: the construction's fixed loci are the corpus's ((A), proofs
  re-read); the joint-multiplicity method and the negative answer agree with member m2's independent
  document; O-S is settled separately (my `O-S-saturation.md`, member m5's and member m2's
  documents), and §6.2 uses $S_{\mathrm{dP}}\cong\Lambda$ only in the form proved there.

## 8. Reproducing the arithmetic

All numbers above are integer arithmetic on ranks and Euler characteristics; each is displayed with
its derivation. The two tables, with the four traces $(i_1,i_2,i_1i_2)$:
$$\text{construction }(0,-16,6):\ \tfrac14(22+0-16+6,\ 22+0+16-6,\ 22-0-16-6,\ 22-0+16+6)=(3,8,0,11),$$
$$\text{twist }(0,-2,20):\ \tfrac14(22+0-2+20,\ 22+0+2-20,\ 22-0-2-20,\ 22-0+2+20)=(10,1,0,11).$$
Each tuple sums to $22$, and the ranks of the three involutions and of the product are recovered from
each other by the identities of §2.1.

