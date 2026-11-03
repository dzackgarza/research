# O-T: which twist pair, and how far the identification goes

Member m6, direction d2 of swarm `smw0dbvr6`. Repository read **read-only** at evidence state
`main@141058a8`; citations relative to the repository root. Nothing was modified. Companion:
`os-lambda-saturation.md` (O-S), which is used in §5 and proved there.

**Verdict, in four sentences.**
(1) `@prob:twist-identification` does not say which twist-side involution is paired with
$I_{\mathrm{dP}}$; `@cons:reflection-twist` defines only $I_\Co=w_\alpha I_{\mathrm{En}}$.
(2) For each of the three literal readings of "the twist pair" the statement is **false**, and the
separating invariant is the rank of the invariant lattice (Theorem B) — the conclusion the swarm
reached independently in direction d3.
(3) The reflection twist applied to the **pair**,
$(J_\Co,J_{\mathrm{dP}}):=(w_\alpha I_{\mathrm{En}},w_\alpha I_{\mathrm{dP}})$, has eigenlattices of
ranks $(11,3)$, joint invariant lattice $\Lambda=U(2)\perp\langle-2\rangle$ and symplectic product of
rank $14$: the same four numbers as the construction's pair (Theorem C; the del Pezzo slot of the
twist is a lattice that the corpus does not compute anywhere).
(4) In that reading the identification is equivalent to exactly one statement about the construction's
Coble slot ($H1$ below) plus placement data; the placement data are proved unconditionally (Theorem D)
and so is the del Pezzo half (Theorem E, via O-S). $H1$ stays open and is reformulated in §6 as a
saturation statement for the quotient $\widehat X_b/I_\Co$, with six possible determinants.

---

## §1 The two sides, as the corpus states them

**Twist side** (`writing/coble/heegner-report/coble-heegner-research-report.md`,
`@cons:reflection-twist`, `@prop:coble-eigenspaces`). $L_{K3}\supset S_{\mathrm{En}}\oplus T_{\mathrm{En}}$
of index $2^{10}$, $S_{\mathrm{En}}=U(2)\oplus E_8(-2)$ (rank $10$),
$T_{\mathrm{En}}=U\oplus U(2)\oplus E_8(-2)$ (rank $12$); $I_{\mathrm{En}}=\pm1$ on them;
$\alpha=e-f\in U\subset T_{\mathrm{En}}$, $\alpha^2=-2$, $w_\alpha$ the reflection,
$I_\Co:=w_\alpha I_{\mathrm{En}}$, and
$$S(I_\Co)=S_{\mathrm{En}}\oplus\mathbb Z\alpha\cong U(2)\oplus E_8(-2)\oplus\langle-2\rangle
\quad(\text{rank }11,\ \det 2048,\ (r,a,\delta)=(11,11,1)),$$
$$T(I_\Co)=\alpha^\perp_{T_{\mathrm{En}}}\cong\langle2\rangle\oplus U(2)\oplus E_8(-2)
\quad(\text{rank }11,\ \det-2048).$$
The AEGS package on the same marking (`coble-heegner-research-report.md`, "The AEGS lattice package";
cited there from `@AEGS25, def:involutions`): the del Pezzo involution
$I_{\mathrm{dP}}(v,u,u',e,e')=(-v,u',u,-e,-e')$ on $U^3\oplus E_8^2$ with
$$S_{\mathrm{dP}}\cong\Delta(U)=U(2)\ (\text{rank }2),\qquad
T_{\mathrm{dP}}\cong U\oplus\Delta^-(U)\oplus E_8^2\ (\text{rank }20),$$
a degree-$4$ class $H\in S_{\mathrm{dP}}\subset S_{\mathrm{En}}$, and
$T_{\mathrm{En}}\hookrightarrow T_{\mathrm{dP}}\hookrightarrow L_{K3}$ (`@thm:aegs-rigidity`).

**Construction side** (`writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md`,
`@prop:tuple-of-the-construction`, `@rmk:a21-open`): for a one-node member $b$,
$$\rk S_{\Co,b}=k+10=11,\qquad \rk S_{\mathrm{dP},b}=k+2=3,\qquad \rk S_{\rho,b}=14\ (k=1),$$
$\Lambda_b=\langle e_b,f_b,[D_b]\rangle\subseteq S_{\Co,b}\cap S_{\mathrm{dP},b}$, and
$\rk(S_{\Co,b}\cap S_{\mathrm{dP},b})=3=\rk S_{\mathrm{dP},b}$, so $S_{\mathrm{dP},b}\subseteq S_{\Co,b}$.

## §2 Theorem C (the reflection-twisted pair and its eigenlattices)

Put $J_\Co:=w_\alpha I_{\mathrm{En}}=I_\Co$ (the corpus's twist) and
$J_{\mathrm{dP}}:=w_\alpha I_{\mathrm{dP}}$. Since $I_{\mathrm{dP}}(\alpha)=-\alpha$ — because
$\alpha\in U\subset T_{\mathrm{En}}\subset T_{\mathrm{dP}}$ and $I_{\mathrm{dP}}=-\mathrm{id}$ on
$T_{\mathrm{dP}}$ — $w_\alpha$ commutes with $I_{\mathrm{En}}$ and with $I_{\mathrm{dP}}$, so $J_\Co$
and $J_{\mathrm{dP}}$ are commuting involutions of $L_{K3}$.

**Theorem C.**
1. $L_{K3}^{J_{\mathrm{dP}}=+1}=S_{\mathrm{dP}}\oplus\mathbb Z\alpha\cong U(2)\perp\langle-2\rangle$:
   rank $3$, $\det8$, signature $(1,2)$, even $2$-elementary with $(r,a,\delta)=(3,3,1)$.
2. $L_{K3}^{J_{\mathrm{dP}}=-1}=\alpha^\perp_{T_{\mathrm{dP}}}$: rank $19$, signature $(2,17)$,
   $\det\pm8$, $A\cong(\mathbb Z/2)^3$, discriminant form $-q_\Lambda$.
3. $L_{K3}^{J_\Co=+1}=S_{\mathrm{En}}\oplus\mathbb Z\alpha$ (rank $11$, $\det2048$) and
   $L_{K3}^{J_\Co=-1}=T(I_\Co)$ (rank $11$), as in `@prop:coble-eigenspaces`.
4. Joint invariants: $S(J_\Co)\cap S(J_{\mathrm{dP}})=S_{\mathrm{dP}}\oplus\mathbb Z\alpha
   =\Lambda=U(2)\perp\langle-2\rangle$, rank $3$.
5. $J_\Co J_{\mathrm{dP}}=I_{\mathrm{En}}I_{\mathrm{dP}}=I_{\mathrm{Nik}}$, and
   $S(I_{\mathrm{Nik}})=S_{\mathrm{dP}}\oplus T_{\mathrm{En}}$: rank $14$, signature $(3,11)$ — exactly
   the rank and signature of a symplectic involution.

*Proof.* (1) *Over $\mathbb Q$.* $I_{\mathrm{dP}}=+1$ and $w_\alpha=+1$ on $S_{\mathrm{dP}}$ (as
$\alpha\perp S_{\mathrm{dP}}\subseteq S_{\mathrm{En}}\perp T_{\mathrm{En}}$), so $J_{\mathrm{dP}}=+1$
there; for $y\in T_{\mathrm{dP}}$, $J_{\mathrm{dP}}y=-y-(y\cdot\alpha)\alpha$, whose $+1$-part is
$\mathbb Q\alpha$ and whose $-1$-part is $\alpha^\perp_{T_{\mathrm{dP}}}$. So over $\mathbb Q$ the
eigenspaces of $J_{\mathrm{dP}}$ are $S_{\mathrm{dP}}\oplus\mathbb Q\alpha$ (rank $2+1=3$) and
$\alpha^\perp_{T_{\mathrm{dP}}}$ (rank $20-1=19$).
*Integrality* (the analogue of the argument in `@prop:coble-eigenspaces`, redone rather than quoted):
let $y\in L$ and write $y=y_S+y_T$ with $y_S\in S_{\mathrm{dP}}^\#$, $y_T\in T_{\mathrm{dP}}^\#$,
possible because $S_{\mathrm{dP}}$ is primitive and $L\subseteq S_{\mathrm{dP}}^\#\oplus T_{\mathrm{dP}}^\#$.
Then $J_{\mathrm{dP}}y=y_S-y_T-(y_T\cdot\alpha)\alpha$, so $J_{\mathrm{dP}}y=y$ forces
$2y_T=-(y_T\cdot\alpha)\alpha$. Writing $y_T=q\alpha+r$ with $r\perp\alpha$ gives $2r=0$, and
$T_{\mathrm{dP}}^\#$ is torsion-free, so $r=0$ and $y_T=q\alpha$. Now
$e\in U\subset T_{\mathrm{En}}\subset T_{\mathrm{dP}}$ has $e\cdot\alpha=e\cdot(e-f)=-1$, so
$q\alpha\in T_{\mathrm{dP}}^\#$ forces $q\in\mathbb Z$. Hence
$y_S=y-q\alpha\in L\cap(S_{\mathrm{dP}}\otimes\mathbb Q)=S_{\mathrm{dP}}$ by primitivity, and
$L^{J_{\mathrm{dP}}=+1}=S_{\mathrm{dP}}\oplus\mathbb Z\alpha$ with
$\det=(-4)(-2)=8$ and signature $(1,1)+(0,1)=(1,2)$. The $(-1)$-eigenspace is
$\alpha^\perp_{T_{\mathrm{dP}}}$ by the same computation with the sign reversed; since $L$ is
unimodular its discriminant form is $-q_\Lambda$.
(2) immediate from (1). (3) is `@prop:coble-eigenspaces`.
(4) $\subseteq$ is clear. For $\supseteq$, let $s+q\alpha=s'+q'\alpha$ with $s\in S_{\mathrm{En}}$,
$s'\in S_{\mathrm{dP}}$; then $s-s'=(q'-q)\alpha\in S_{\mathrm{En}}\cap\mathbb Q\alpha=0$ because
$S_{\mathrm{En}}\perp T_{\mathrm{En}}\ni\alpha$, so $s=s'\in S_{\mathrm{En}}\cap S_{\mathrm{dP}}=S_{\mathrm{dP}}$
and $q=q'$.
(5) $J_\Co J_{\mathrm{dP}}=w_\alpha I_{\mathrm{En}}w_\alpha I_{\mathrm{dP}}=I_{\mathrm{En}}I_{\mathrm{dP}}$
as $w_\alpha^2=1$ and all factors commute. Over $\mathbb Q$: on $S_{\mathrm{En}}$,
$I_{\mathrm{Nik}}v=I_{\mathrm{dP}}v$, so the $+1$-part is $S_{\mathrm{En}}\cap S_{\mathrm{dP}}=S_{\mathrm{dP}}$;
on $T_{\mathrm{En}}$, $I_{\mathrm{Nik}}v=-I_{\mathrm{dP}}v$, so the $+1$-part is
$T_{\mathrm{En}}\cap T_{\mathrm{dP}}=T_{\mathrm{En}}$. Hence $S(I_{\mathrm{Nik}})=S_{\mathrm{dP}}\oplus T_{\mathrm{En}}$,
rank $2+12=14$, signature $(1,1)+(2,10)=(3,11)$. $\square$

*Remark.* Statement (1) is new: the corpus computes the eigenspaces of the twist $I_\Co$ only, and the
AEGS package records $S_{\mathrm{dP}}=U(2)$ for the marking. The reflection twist of the del Pezzo
involution raises the invariant rank from $2$ to $3$ and the invariant lattice from $U(2)$ to
$\Lambda=U(2)\perp\langle-2\rangle$, which is exactly the flat lattice of the one-node construction.

## §3 Theorem B (the literal readings are separated by an invariant)

**Theorem B.** Let $\mathfrak T$ be any pair of distinct commuting involutions from the twist datum
$\{I_{\mathrm{En}},w_\alpha,J_\Co,I_{\mathrm{dP}}^{\mathrm{AEGS}}\}$. Then $\mathfrak T$ is not
$\mathrm O(L_{K3})$-conjugate to the construction's pair $(I_{\Co,b},I_{\mathrm{dP},b})$ for any
one-node member $b$; nor is any single involution of that datum conjugate to $I_{\mathrm{dP},b}$.

*Proof.* Conjugate isometries have isometric $+1$-eigenspaces, in particular equal ranks. The ranks in
the twist datum are $\rk S(I_{\mathrm{En}})=10$, $\rk S(w_\alpha)=21$, $\rk S(J_\Co)=11$,
$\rk S(I_{\mathrm{dP}}^{\mathrm{AEGS}})=2$, so a pair from it has rank multiset one of
$\{10,21\},\{11,10\},\{11,21\},\{11,2\},\{10,2\},\{21,2\}$, while the construction's pair has multiset
$\{11,3\}$ by I1/§1. No $3$ occurs on the twist side. $\square$

This is the swarm's direction-d3 conclusion (finding f1: joint $(Z/2)^2$ multiplicities
$(11,3,14)$ against the twist's $(11,10,21)$), restated as a rank statement; it also identifies the one
twist-side element that *does* have rank $3$, namely $J_{\mathrm{dP}}$.

## §4 Theorem D (the labels $H$ and $\alpha$ are pinned inside $\Lambda$, unconditionally)

**Theorem D.** Let $x\in\Lambda_b$ with $x^2=4$ and $x\cdot\alpha_b=0$. Then $x=\pm H_b$, where
$H_b=e_b+f_b$. Let $\beta\in\Lambda_b$ with $\beta^2=-2$ and $\beta\cdot H_b=0$. Then
$\beta=\pm\alpha_b$, where $\alpha_b=[D_b]$. No hypothesis on $S_{\Co,b}$ is used.

*Proof.* Write $x=ae_b+bf_b+c[D_b]$. From $0=x\cdot[D_b]=-2c$ get $c=0$, and from $4=x^2=4ab$ get
$ab=1$, so $x=\pm(e_b+f_b)$. For $\beta$: $\beta\cdot H_b=2(a+b)=0$ gives $b=-a$, and
$-2=\beta^2=-4a^2-2c^2$ gives $2a^2+c^2=1$, so $a=0$ and $c=\pm1$. $\square$

So the marked lattices $(\Lambda;H,\alpha)$ agree on the two sides with $H\mapsto\pm H$ and
$\alpha\mapsto\pm\alpha$: on the twist side $H\in S_{\mathrm{dP}}\subset\Lambda$ has $H^2=4$ and
$\alpha\perp S_{\mathrm{dP}}$ generates the $\langle-2\rangle$ summand (Theorem C(1)), and on the
construction side Theorem D gives the same. The sign is fixed by effectivity: $H_b$ is nef and big and
$\alpha_b$ is the class of an effective curve (`@prop:tuple-of-the-construction`, parts 2–3).

## §5 Theorem E (the del Pezzo half holds unconditionally)

**Theorem E.** For every one-node member, $S_{\mathrm{dP},b}\cong U(2)\perp\langle-2\rangle$; this
lattice is isometric to $S(J_{\mathrm{dP}})$ of Theorem C(1), compatibly with
$(H,\alpha)\mapsto(\pm H,\pm\alpha)$.

*Proof.* `os-lambda-saturation.md` Theorem A gives $S_{\mathrm{dP},b}=\Lambda_b$ and Corollary A1 gives
the type $(3,3,1)$; Theorem C(1) gives the same type for the twist's del Pezzo slot, and Theorem D
matches the two marked classes. $\square$

This is where O-S decides part of O-T: had the determinant been $2$, $S_{\mathrm{dP},b}$ would be
$U\perp\langle-2\rangle$ with $A\cong\mathbb Z/2\not\cong(\mathbb Z/2)^3$, and *no* isometry to $\Lambda$
— hence no conjugacy of the pairs — would exist. The swarm's O-S result therefore **is** the del Pezzo
half of O-T, and it also shows that the del Pezzo slot of the construction is not the AEGS slot
$U(2)$ but its reflection twist.

## §6 What remains: exactly one statement, $H1$

On the Coble slot the corpus does not describe the lattice (`@rmk:a21-open`: "neither invariant lattice
is described exactly, at any $k$"). The statement needed is

> **$H1$.** For a one-node member, $S_{\Co,b}\cong U(2)\oplus E_8(-2)\oplus\langle-2\rangle$,
> equivalently: even $2$-elementary of type $(r,a,\delta)=(11,11,1)$, i.e. $\det=\pm2048$.

This is the corpus's $H1$ (`computations/reports/sm00_arithmetic-core.md` §1).

**Conditional Theorem F.** Assume $H1$. Then $(I_{\Co,b},I_{\mathrm{dP},b})$ is
$\mathrm O(L_{K3})$-conjugate to $(J_\Co,J_{\mathrm{dP}})$ with $H_b\mapsto\pm H$ and
$\alpha_b\mapsto\pm\alpha$; hence `@prob:twist-identification` holds in that reading. Ingredients, and this is where the statement stops being
self-contained. Theorem C (types, joint lattice), Theorem E (del Pezzo slot) and Theorem D (labels) are
proved. Two further inputs are needed and are **not** proved here:
(i) the primitive-embedding classification of Nikulin for $S_{\Co,b}$ together with the surjectivity
$\mathrm O(S_{\Co,b})\to\mathrm O(A_{S_{\Co,b}})$ that the corpus records as owner-verified
(`@thm:two-elementary-surjectivity`, cited there; for $T_\Co$ it is a cited theorem whose provider check
failed at one pin and is reproduced at a later one — `writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md`,
around line 338);
(ii) **(U)** every primitive embedding $\Lambda\hookrightarrow S_\Co\cong U(2)\oplus E_8(-2)\oplus\langle-2\rangle$
whose image contains the marked pair $(H,\alpha)$ ($H^2=4$, $\alpha^2=-2$, $H\cdot\alpha=0$, $\alpha$
primitive) is carried to the standard one $U(2)\oplus\langle-2\rangle\subset U(2)\oplus E_8(-2)\oplus\langle-2\rangle$
by an isometry of $S_\Co$; equivalently the complement is forced to be $E_8(-2)$, the unique even
$2$-elementary lattice of type $(8,8,1)$. (U) is a finite $2$-adic computation of the same kind as the
corpus's (O1)/(O2) (`computations/reports/sm00_arithmetic-core.md` §6) and is not carried out here; with
$H1$ alone, and without (U), the pair could in principle fail to be conjugate even though its two
pieces are isometric.

**Reformulation of $H1$ (the exact remaining sharp question).** Let $Q:=\widehat X_b/I_\Co$, so
$\pi':\widehat X_b\to Q$ is a double cover branched along the image $\overline D$ of the fixed curve
$D_b$. Then $Q$ is smooth (a fixed curve makes the action $\mathrm{diag}(1,-1)$ transversally, and $I_\Co$
has no isolated fixed point, `@prop:local-operators` part 4) and rational (the standard fact for a
non-symplectic involution with nonempty fixed locus; its numerical invariants are consistent with it),
with $\chi(Q)=\tfrac12(\chi(\widehat X_b)+\chi(\mathrm{Fix}))=\tfrac12(24+2)=13$, hence $b_1(Q)=0$,
$b_2(Q)=11$, $K_Q^2=-1$ (Noether), $\overline D\in|-2K_Q|$, $\overline D\cong\mathbb P^1$, $\overline D^2=-4$; and
$$H^2(Q,\mathbb Z)\cong I_{1,10}=\langle1\rangle\oplus\langle-1\rangle^{10},\qquad
\pi'^*H^2(Q,\mathbb Z)\cong 2I_{1,10}\cong U(2)\oplus E_8(-2)\oplus\langle-2\rangle,$$
the isometry holding because both sides are even, of rank $11$, $\det2048$, $A\cong(\mathbb Z/2)^{11}$,
$\delta=1$, signature $(1,10)$, and an even $2$-elementary lattice is determined by
$(r,a,\delta)$ and signature (corpus `@thm:two-elementary-classification`). Moreover
$[D_b]=\pi'^*(-K_Q)$ and $\pi'^*\overline D=2[D_b]$, so the fixed curve is *not* an extra class. Since
$\rk S_{\Co,b}=\rk\pi'^*H^2(Q,\mathbb Z)=11$,

> **$H1$ $\iff$ $\pi'^*H^2(Q,\mathbb Z)$ is saturated in $H^2(\widehat X_b,\mathbb Z)$; then
> $\det S_{\Co,b}=2048/m^2$ with $m=[S_{\Co,b}:\pi'^*H^2(Q,\mathbb Z)]$, so
> $\det S_{\Co,b}\in\{2048,512,128,32,8,2\}$.**

This is the exact analogue of O-S with the roles of $I_{\mathrm{dP}}$ and $I_\Co$ exchanged, but with
$b_2=11$ instead of $3$: there the half-class problem had three variables and exactly two admissible
classes, whereas here the half classes of $2I_{1,10}$ form a group of $\mathbb F_2$-rank $11$ (against
$3$ for $\Lambda$), so I record the sharp question rather than guess. What would settle it: the analogue of Lemma 2 of
`os-lambda-saturation.md`, i.e. an integrality obstruction excluding the half classes
$\pi'^*\lambda/2$ with $\lambda\in I_{1,10}$, $\lambda^2\in4\mathbb Z$,
$\lambda\notin2I_{1,10}$ — or a geometric argument producing one.

## §7 Honest accounting

* **Proved here:** Theorem C (eigenlattices of the reflection-twisted pair, including the new
  $S(J_{\mathrm{dP}})=\Lambda$), Theorem B (literal readings false; separating invariant = the
  invariant-lattice rank), Theorem D (labels pinned), Theorem E (del Pezzo half, using O-S).
* **Cited:** the corpus's eigenspace computation for $I_\Co$; the AEGS package for $I_{\mathrm{dP}}$;
  the ranks $k+10,k+2,14$; the surjectivity theorems used in Theorem F.
* **Open:** $H1$ (§6) and with it the Coble slot of the conjugacy; and the two further inputs of
  Theorem F, namely the cited surjectivity and statement **(U)**.
* **Not used anywhere:** any integral eigensplitting of $H^2(\widehat X_b,\mathbb Z)$; any chamber,
  nef-cone or translation-invariance detector; any change of the labels $H$, $\alpha$, $\iota_\Co$,
  $\iota_{\mathrm{dP}}$.

## §8 Files

* `ot-twist-identification.md` — this document.
* `os-lambda-saturation.md` — companion, containing Theorem A used in §5.
* `scripts/os_ot_lattices.sage`, `scripts/run.log` — exact-arithmetic checks of every determinant,
  discriminant group, half-class list and rank used above.
