# The operator-preserving labelled extension of A21: full proof, exact sources, verification artifacts

Evidence register entry for swarm `smw0gfl0i` (accepted solutions m2/d7, m3/d5, m4/d3; audits
m5/d6, m6/d8). Repository evidence state `main@dd8edefe6a`. Tier discipline: **only** maintained
semantic runs, corpus theorems, session-verified primary literature, and elementary proved lemmas
enter this proof. Bespoke exact-arithmetic member scripts (`m2/verify2.py`, `m5/certificate.py`,
`m6/verify_pieces.py`, `m6/verify_gluing.py`, `m6/saturate.py`) are **exploratory** and validate
nothing here; where their numbers are used, a maintained or proved source is named instead.

## 0. Statement and scope

**Theorem (the lattice obligation of @prob:coble-rigidity, i.e. report item 8(d)(1)).**
Let $(J_{\mathrm{Co}},J_{\mathrm{dP}})=(w_\alpha I_{\mathrm{enr}},w_\alpha I_{\mathrm{dP}})$ be the
reflected pair on $L=U^3\oplus E_8(-1)^{\oplus 2}$ ($\alpha=e_0-e_1$, $w_\alpha$ the maintained
reflection), with its labelled classes $H=\Delta(e)+\Delta(f)$, $\alpha=e_0-e_1$; and let $b$ be
any member of the (irreducible, one-nodal, $\tau$-invariant) one-node locus of the direct
projective construction, with its pair $(I_{\mathrm{Co},b},I_{\mathrm{dP},b})$ and labels
$H_b=\pi^*\mathcal O_Y(1,1)$, $\alpha_b=[D_b]$. Then there is $g\in O(L_{K3})$ with

$$gJ_{\mathrm{Co}}g^{-1}=I_{\mathrm{Co},b},\qquad gJ_{\mathrm{dP}}g^{-1}=I_{\mathrm{dP},b},\qquad
g(H)=H_b,\qquad g(\alpha)=\alpha_b,$$

after identifying both sides with $L_{K3}$ through their markings. The conclusion holds **uniformly
for every such $b$**: every input used is either a lattice-level maintained computation on the model
side or a theorem whose hypotheses are stated and matched for arbitrary $b$ in §5; no
transport/connectedness shortcut is invoked anywhere.

This is a **lattice statement**. It does not establish: a Hodge isometry or a chamber statement
(m4's accepted dichotomy governs those: under the corpus's adopted R5 reading the chamber needs the
period/Torelli input); the corpus's authored *second slot*, which stays textually undefined; the
(O1)/(O2) questions of `sm00_arithmetic-core.md` (they live in a non-2-elementary decomposition
this proof never touches, §6); or any slot being "original".

## 1. Exact source statements (verbatim, with hypotheses; all used forms checked this session)

**N1. Nikulin's surjectivity (THEOREM 3.6.3).** In-repo primary text
`references/literature/lattice-research/nikulin1979integral.md` :1595:

> „Let $S$ be an even, indefinite 2-elementary lattice. Then the homomorphism
> $O(S)\longrightarrow O(q_S)$ is surjective."

with its printed proof: if $a<t_++t_-$ or $\delta_S=0$, from Theorem 1.14.2; if
$a=t_++t_->2$, then $q_S$ has an orthogonal summand $u_+^{(2)}(2)$ or $v_+^{(2)}(2)$, and
Theorem 1.14.2 again; if $a=t_++t_-=2$ then $S\cong\langle2\rangle\oplus\langle-2\rangle$ and
$O(q_S)$ is trivial. Independent confirmation: the sentence „By [Nik79] for an indefinite
2-elementary lattice $H$, such as $S$ and $T$, the homomorphism $O(H)\to O(A_H,q_H)$ is
surjective" in V. Alexeev, arXiv:2209.09110 §2 (fetched this session); the Alexeev–Nikulin
appendix (MSJ Memoirs 15, §A.1) restates it with boundary $a\ge3$, $\operatorname{rk}\ge3$; and
the corpus carries it as `@thm:two-elementary-surjectivity`,
`writing/lattice-theory/classification/two-elementary-lattices.md`:71. This resolves the standing
„Check the numbering" TODO of `docs/theory/glue-stabilizers.md`.

**Hypothesis check for the only lattice N1 is applied to.** $D=\langle2\rangle\perp
U(2)\perp E_8(-2)$: *even* (each summand even); *indefinite*, signature $(2,9)$; *2-elementary*,
$A_D\cong(\mathbb Z/2)^{11}$ ($|A_D|=|det D|=2048=2^{11}$); $a=11>2$. Twist side: maintained
(`coble_reflected_pair-run.txt`: rank 11, det $-2048$, sig $(2,9)$, even, `is_isometric_to` True
against this type). Construction side: type established by m8's Theorem 3.1 (`smtw_ot_types-m8.md`
§3) — the corpus's Nikulin fixed-locus classification application with the exception table handled.

**N2. Nikulin's classification (THEOREM 3.6.2, same note :1577).** The genus of an even
2-elementary lattice is determined by $(\delta;t_+,t_-,a)$; if $t_+>0$ and $t_->0$ the class is
determined. Used *only* through the corpus's established type theorems (m8's Theorem 3.1 for
$S_{\mathrm{Co},b}$, $T_{\mathrm{Co},b}$; `@prop:det-saturation-del-pezzo` for
$S_{\mathrm{dP},b}=\Lambda$), exactly as those theorems invoke it.

**N3. Gluing correspondence (corpus-level statements, used as proved corpus theorems).**
`@thm:nikulin-gluing` (`writing/lattice-theory/embeddings-and-overlattices.md`:125): even
overlattices of an even lattice $S$ correspond bijectively to isotropic quadratic subobjects of
$A_{S,q}$; if the ambient is unimodular the subgroup is the graph of an anti-isometry between the
two complementary discriminant forms. `@cor:lifting-unimodular`
(`writing/lattice-theory/automorphism-lifting-through-a-gluing.md`:152): a piecewise isometry
$\varphi_S\perp\varphi_T$ extends to the overlattice iff
$\bar\varphi_T\circ\gamma=\gamma\circ\bar\varphi_S$.

**N4. The symplectic-involution input (the coinvariant type).** Nikulin [Ni1], Theorem 4.7: any
abelian group acting symplectically on a K3 surface has a unique up-to-isometry action on
$H^2(X,\mathbb Z)$ — quoted in van Geemen–Sarti, *Nikulin involutions on K3 surfaces*, Math. Z.
255 (2007) 731–753, §1.1 (arXiv:math/0602015, fetched this session). Morrison's realization, same
paper §1.2:

> „there exist K3 surfaces with a Nikulin involution which acts in the following way ... $(u,x,y)\mapsto(u,y,x)$ ... Thus for any K3 surface $X$ with a Nikulin involution $\iota$ there is an isomorphism $H^2(X,\mathbb Z)\cong U^3\oplus E_8(-1)\oplus E_8(-1)$ such that $\iota^*$ acts as above."

and §1.3, verbatim conclusions:

> „The invariant sublattice is $H^2(X,\mathbb Z)^\iota\cong\{(u,x,x)\}\cong U^3\oplus E_8(-2)$. The anti-invariant lattice is the lattice perpendicular to the invariant sublattice: $(H^2(X,\mathbb Z)^\iota)^\perp\cong\{(0,x,-x)\}\cong E_8(-2)$."

so the invariants of the action are $(s,t,r)=(6,0,8)$. The only geometric hypothesis is that
$\iota$ is a symplectic involution of a K3 surface — i.e. $\iota^*$ fixes $H^{2,0}$.

**N5. Invariant/coinvariant 2-elementarity.** Same primary note :1565 (§3.6): for a polarized
integral involution, $L^\varphi$ is even and $(L^\varphi)^*/L^\varphi\cong(\mathbb Z/2)^\alpha$;
the corpus's `@prop:coinvariant_involution_2elementary`
(`writing/lattice-theory/invariant-and-coinvariant-lattices.md`:269) states invariant *and
coinvariant* 2-elementarity for an involution of an even unimodular lattice, whose hypotheses hold
trivially for $L_{K3}$.

## 2. The objects and the retained inputs

Model side (maintained, `coble_reflected_pair-run.txt`, all via provider semantic calls at pin
`c546077d`): the joint pieces of $(J_{\mathrm{Co}},J_{\mathrm{dP}})$ have ranks $(3,8,0,11)$,
dets $8,256,1,-2048$, signatures $(1,2),(0,8),(0,0),(2,9)$, and are `is_isometric_to`
$\Lambda:=U(2)\perp\langle-2\rangle$, $E_8(-2)$, $0$, $T:=\langle2\rangle\perp U(2)\perp E_8(-2)$
respectively; $J_{\mathrm{Co}},J_{\mathrm{dP}}$ are commuting integral involutions; $H^2=4$,
$\alpha^2=-2$, $H\cdot\alpha=0$; the maintained check
`computations/reports/coble_joint_flag_premises-run.txt` (provider semantic calls at the same pin)
additionally verifies: both involutions fix $H$ and $\alpha$;
$H/2,\alpha/2,(H\pm\alpha)/2\notin L$; in the maintained basis of $V_{++}$ (Gram
$\langle-2\rangle\perp U(2)$) $H=b_2+b_3$ and $\alpha=b_1$ (a *corner basis*, §4.2); the gluing
index $[L:\bigoplus V_{ss'}]=2048=|A_{V_{--}}|=|A_{V_{++}\perp V_{+-}}|$. All of this is the
published maintained check `computations/reports/coble_joint_flag_premises.py` + `-run.txt`
(provider semantic calls at the pin, reproducing the original swarm log line-for-line except one
corrected print note on the definite piece). (The three
`  in piece? False` lines of the older log are a basis-equality artifact, not membership tests;
membership is integral, coordinates `["0","1","1"]`, `["1","0","0"]`.)

Notation: $A=V_{++}$ (rank 3), $B=V_{+-}$ (rank 8), $E=V_{-+}=0$, $D=V_{--}$ (rank 11). The two
involutions are the sign-changes across the pieces: $\sigma=+1$ on $A\perp B$, $-1$ on $D$;
$\tau=+1$ on $A$, $-1$ on $B\perp D$.

## 3. Pair-level conjugacy (Theorem A)

**Lemma L1 (flag structure).** Each joint piece $V_{ss'}=L\cap(\text{rational eigenspace})$ is
primitive in $L$ (saturated kernel); the pieces are pairwise orthogonal; $\bigoplus V_{ss'}$ spans
$L\otimes\mathbb Q$, so has finite index; each piece is an invariant or coinvariant lattice of one
of $\sigma,\tau,\iota=\sigma\tau$ — against the sign table of §2 the identifications are
$$A=V_{++}=L^\tau\ \text{(invariant of }\tau\text{)},\qquad
B=V_{+-}=L^-_\iota\ \text{(coinvariant of the product }\sigma\tau\text{)},\qquad
D=V_{--}=L^-_\sigma\ \text{(coinvariant of }\sigma\text{)},$$
since $V_-(\tau)=B\perp D$ (its index-$256$ saturation is the $T_{J_{\mathrm{dP}}}$-lattice, not a
piece) and $V_-(\sigma)=E\perp D=D=V_+(\sigma)^\perp=:T_\sigma$ — hence each piece is even and
2-elementary by N5. (This corrects the identification "$D=L^-_\tau$" printed in m3's and m2's
documents; their 2-elementarity conclusions are unaffected, since all three corrected
identifications are still (co)invariant lattices of involutions on the unimodular $L$.) The index satisfies
$[L:A\perp B\perp D]^2=\prod|\det V_{ss'}|=2^{22}$, so $[L:M]=2^{11}$ for
$M:=A\perp B\perp D$.

**Lemma L2 (the gluing is a full graph).** The gluing $G=L/M\subset A_M$, isotropic of order
$2^{11}$, projects *isomorphically* onto $A_D$ (order $2^{11}$): an element of the kernel would be
a class in $A_{A\perp B}$ represented by an $L$-element in the rational span of $A\perp B$, but
$A\perp B\subseteq S_\sigma$ and
$\det(A)\cdot|\det B|=8\cdot 256=2048=|det S_\sigma|$ — established on both sides (model:
maintained; construction: types theorem) — so $A\perp B=S_\sigma$ with index $1$, and
$S_\sigma$ is saturated, hence the projection is injective, and by equal orders bijective. Dually
$G$ projects isomorphically onto $A_{A\perp B}$. By N3, $G=\mathrm{graph}(\gamma)$ for an
anti-isometry $\gamma\colon A_{A\perp B}\to A_D(-1)$: $q(\gamma v)=-q(v)$ for all
$v\in A_{A\perp B}$.

**Theorem A.** Let $(\sigma,\tau)$, $(\sigma',\tau')$ be commuting involution pairs of an even
unimodular $L$ with $V_{-+}=V'_{-+}=0$, matching joint ranks $(3,8,0,11)$, and matching piece
types $\Lambda,E_8(-2),T$, and $|det S_\sigma|=|det S_{\sigma'}|$. Then they are $O(L)$-conjugate.

*Proof.* Choose piece isometries $\psi_A\colon A\to A'$, $\psi_B\colon B\to B'$ (types match),
and any $\psi_D\colon D\to D'$. After transporting by
$\Psi_0=\psi_A\perp\psi_B\perp\psi_D\colon M\to M'$, the two gluings are two graphs
$\gamma,\gamma'\colon A_{A'\perp B'}\to A_{D'}(-1)$. Then
$\theta:=\gamma'\circ\gamma^{-1}\in O(A_{D'},q_{D'})$ — both are anti-isometries, so $\theta$
preserves $q_{D'}$. $D'$ is even, indefinite (sig $(2,9)$), 2-elementary ($a=11$), so **N1 applies
hypothesis-by-hypothesis** (§1): there is $h\in O(D')$ with $\bar h=\theta$ on $A_{D'}$. Then
$\Psi_1:=(\psi_A\perp\psi_B,\ h\circ\psi_D)\colon M\to M'$ satisfies
$\bar\Psi_1(G)=G'$ (for graph elements $(v,\gamma v)$: maps to
$(v,\theta\gamma v)=(v,\gamma'v)$ after A,B-coding), hence by N3 extends to an isometry
$g\colon L=M[G]\to L=M'[G']$; it carries the $(\pm1)$-eigenlattices of the first pair to those of
the second ($A\perp B\to A'\perp B'$ and $D\to D'$ for $\sigma$; $A\to A'$ and $B\perp D\to
B'\perp D'$ for $\tau$), so $g\sigma g^{-1}=\sigma'$, $g\tau g^{-1}=\tau'$. $\blacksquare$

*Remark (the definite piece — corrected).* No surjectivity statement enters the proof through
$B=E_8(-2)$ at all: the lifting is performed on $D$ only, and $B$ enters Lemma L2's graph property
solely as a passive factor. For the record, outside the logical chain — and correcting m3's
Remark 4.6, whose "trivial image" claim is false — the actual discriminant action is computed by the
proper reflection normalization as follows. With $B^*=\tfrac12B$,
$A_B\cong E_8/2E_8\cong(\mathbb Z/2)^8$ carries the plus-type form
$q(\bar x)\equiv \tfrac{q_{E_8}(x)}{2}\pmod 2$ (the sign is invisible mod $2$). For a $(-4)$-root
$\delta$ of $B$ (so $-2/(\delta\cdot\delta)=\tfrac12$),
$$s_\delta(\bar x)=\bar x+(\xi\cdot\delta)\,[\delta/2]\qquad(\xi\in B^*),$$
well-defined because $B$ is even, so $\xi\cdot\delta\in\mathbb Z$ for $\xi\in B^*$; it is the nonzero
transvection in the non-isotropic vector $[\delta/2]$ — not a scalar multiple of $\bar\delta$, the
error in the discarded claim (the normalization pitfall: for $(-4)$-roots the correction is
$\tfrac{\xi\cdot\delta}{2}\delta$, which is integral-$B$-valued only when $\xi\cdot\delta$ is even).
The full image is the classical mod-$2$ Weyl reduction
$W(E_8)\twoheadrightarrow O_8^+(\mathbb F_2)$ with kernel $\{\pm1\}$ ($-1$ acts trivially on the
$2$-torsion discriminant), consistently with $|W(E_8)|=696\,729\,600=2\cdot348\,364\,800
=2\,|O_8^+(2)|$. So $O(E_8(-2))\to O(q_B)$ is in fact also surjective, by direct reflection
computation rather than by N1 — a remark, used nowhere.

## 4. The $(+-)$-type on the construction side, and uniformity

**Theorem ($(\star)$).** On the construction side, $V'_{+-}\cong E_8(-2)$ for every $b$.

*Proof.* The product $\iota_b=I_{\mathrm{Co},b}\cdot I_{\mathrm{dP},b}$ is a **symplectic**
involution of the K3 surface $X_b$ — this is the authored fifth bullet, i.e. a structural property
of every construction tuple (`prop:tuple-of-the-construction`; uniform in $b$, since it is the two
covering involutions' product by construction, fixing the holomorphic 2-form pointwise: the
nonsymplectic pair compensates). Its rank: $V_-(\iota_b)=V'_{+-}\oplus V'_{-+}=V'_{+-}$ since
$V'_{-+}=0$ (established multiplicity). By **N4**, the action of a symplectic involution on
$H^2(X,\mathbb Z)$ is unique up to isometry and its coinvariant lattice is $E_8(-2)$ — directly
$(H^2(X_b)^\iota)^\perp\cong\{(0,x,-x)\}\cong E_8(-2)$ as sublattices of $U^3\oplus E_8(-1)^2$.
Hence $V'_{+-}\cong E_8(-2)$. $\blacksquare$

*Consistency observation (not a premise).* N4 also fixes the *invariant* lattice
$U^3\oplus E_8(-2)$ (rank 14, sig $(3,11)$, $|\det|=256$). The model-side saturated invariant
lattice $\operatorname{sat}(A\perp D)$ of the product $\iota=J_{\mathrm{Co}}J_{\mathrm{dP}}$
($=I_{\mathrm{enr}}I_{\mathrm{dP}}$ since $w_\alpha$ commutes with both) has
$\det=2^{14}/(2^3)^2=2^8=256$ — the gluing of $A_{V_{++}}\oplus A_{V_{--}}$ of order $2^3$ —
consistent; the atlas of the $(s,t,r)=(6,0,8)$ invariants gives rank $14=6+8$, matching.

*Exploratory corroboration only (validationly inert)*: m6's `saturate.py` independently reaches the
same type from the corpus's recorded $S_{\mathrm{Co}}$-coordinates (integer kernel of the three
orthogonality relations, det 256, exhaustive absence of $(-2)$-vectors, an exhibited
$-2\,\mathrm{Cartan}(E_8)$ basis). It is exact arithmetic but bespoke; it is not cited as validation
anywhere in this proof. The established route to $(\star)$ is N4 alone.

## 5. Uniformity of the $b$-side hypotheses

For arbitrary $b$ in the locus the proof uses, each time with its hypotheses:

1. `prop:tuple-of-the-construction` items: $\pi^*\operatorname{Pic}(Y)\perp\mathbb Z
   D_1\perp\cdots\perp\mathbb ZD_k\subseteq S_{\mathrm{dP},b}$ with pullback Gram $U(2)$, each
   $D_g$ a $(-2)$-class, mutual orthogonality; $\operatorname{rk}S_{\mathrm{dP},b}=k+2$ by the
   Lefschetz/fixed-locus count. For one-node $b$ (ordinary node at a $\tau$-fixed point, smooth
   elsewhere, irreducible branch): rank $3$.
2. `@prop:det-saturation-del-pezzo` at its stated one-node hypotheses ($k=1$, ordinary node at a
   $\tau$-fixed point, branch curve irreducible): $S_{\mathrm{dP},b}=\pi^*\operatorname{Pic}(Y)
   \perp\mathbb Z[D_b]$ with **index 1** — the ruling-frame lattice is saturated.
3. m8's Theorem 3.1 (`smtw_ot_types-m8.md` §3, hypotheses: the fixed-locus data of
   $I_{\mathrm{Co},b}$, uniform over the locus): $S_{\mathrm{Co},b}\cong U(2)\oplus
   E_8(-2)\oplus\langle-2\rangle$ (det $2048$, $(r,a,\delta)=(11,11,1)$) and
   $T_{\mathrm{Co},b}\cong\langle2\rangle\perp U(2)\perp E_8(-2)$.
4. The joint multiplicities $(3,8,0,11)$ for one-node $b$ (established); in particular
   $V'_{++}=S_{\mathrm{Co},b}\cap S_{\mathrm{dP},b}=S_{\mathrm{dP},b}$ (rank equality plus
   primitivity of the intersection), $V'_{--}=T_{\mathrm{Co},b}$, $V'_{-+}=0$.
5. $(\star)$ of §4 (uniform, N4).
6. The authored bullets as construction data: $H_b=\pi^*\mathcal O_Y(1,1)$ fixed by both,
   $\alpha_b=[D_b]$ fixed by $I_{\mathrm{Co},b}$; product symplectic.

Item `(iii)` of Theorem A (matching single-involution determinants) is then
$|\det S_{\mathrm{Co},b}|=2048=|\det S_{J_{\mathrm{Co}}}|$ and
$|\det S_{\mathrm{dP},b}|=8=|\det S_{J_{\mathrm{dP}}}|$ — maintained on the model side, theorem
on the $b$-side. All hypotheses of Theorem A hold **for every $b$** by these uniform inputs;
no step uses one member to infer another.

## 6. The labelled level (Theorem B): derived $H,\alpha$ identification, marked orbit, gluing compatibility

**Derived identification from the original construction.** By §5.1–5.2, in
$S_{\mathrm{dP},b}=\pi^*\operatorname{Pic}(Y)\perp\mathbb Z[D_b]$ put
$e_b:=\pi^*\mathcal O_Y(1,0)$, $f_b:=\pi^*\mathcal O_Y(0,1)$: then
$e_b^2=f_b^2=2\cdot0=0$, $e_b\cdot f_b=2\cdot(1\cdot1)=2$ (the form doubles under the double
cover), so $\langle e_b,f_b\rangle\cong U(2)$, and
$H_b=\pi^*\mathcal O_Y(1,1)=e_b+f_b$ — the *corner* diagonal; $\alpha_b=[D_b]$ with
$D_b^2=-2$, orthogonal to $\pi^*\operatorname{Pic}(Y)$. Under the index-1 saturation (§5.2),
$(e_b,f_b,\alpha_b)$ is an index-one basis of $V'_{++}\cong U(2)\perp\langle-2\rangle$ with Gram
$U(2)\perp\langle-2\rangle$ and $H_b=e_b+f_b$, $\alpha_b$ the $\langle-2\rangle$-generator.
The model side has the corner basis $H=b_2+b_3$, $\alpha=b_1$ (§2). Hence the *marked triples*
$(V_{++},H,\alpha)\cong(V'_{++},H_b,\alpha_b)$, by the manifest isometry matching corner bases —
Gram matrices agree. (m3's *corner pair* formulation; equivalent to m2's $Q=\langle-4\rangle$
computation: the orthogonal complement of $\langle H,\alpha\rangle$ in the piece is
$\mathbb Z(e_b-f_b)$ of square $-4$, with gluing $(H\pm\omega)/2\in V'_{++}$.)

**Lemma (marked orbit).** Any two corner pairs in $V\cong U(2)\perp\langle-2\rangle$ are one
$O(V)$-orbit: match the corner bases; the linear map is an isometry since the Gram matrices are
identical. $\blacksquare$

**Lemma (flag stabilizer: the marked isometry of the $(++)$-piece is realized by $O(L)$ through
the gluing).** In the situation of Theorem A's conclusion, with gluing graph $\gamma\colon
A_{S_\sigma}\to A_{T_\sigma}(-1)$ ($S_\sigma=A\perp B$): for every $\varphi\in O(A)$ there is
$h_L\in O(L)$ *fixing the pair* (commuting with both $\sigma,\tau$) and acting on $A$ as
$\varphi$.

*Proof (the required gluing compatibility, carried out).* Let
$\alpha_A:=(\bar\varphi\oplus\mathrm{id}_{A_B})\in O(q_{S_\sigma})$ — it preserves $q$
factorwise, hence is a $q_{S_\sigma}$-isometry. Set
$$\theta:=\gamma\circ\alpha_A\circ\gamma^{-1}\colon A_{T_\sigma}\to A_{T_\sigma};$$
then $q_{T_\sigma}(\theta u)=-q_{S_\sigma}(\alpha_A\gamma^{-1}u)=-q_{S_\sigma}(
\gamma^{-1}u)=q_{T_\sigma}(u)$, so $\theta\in O(q_{T_\sigma})$. $T_\sigma=D$ meets N1's
hypotheses (§1), so there is $\psi\in O(D)$ with $\bar\psi=\theta$. The triple
$(\varphi,\mathrm{id}_B,\psi)$ is an isometry of $M=A\perp B\perp D$ and preserves the graph by
construction: for $v\in A_{S_\sigma}$,
$$\bar\psi\,\gamma(v)=\theta\gamma(v)=\gamma(\alpha_A v)=\gamma((\bar\varphi\oplus\mathrm{id})v),$$
i.e. precisely N3's compatibility equation
$\bar\varphi_T\circ\gamma=\gamma\circ\bar\varphi_S$ with
$\varphi_S=\varphi\perp\mathrm{id}_B$, $\varphi_T=\psi$. Hence the triple extends to
$h_L\in O(L)$; it fixes each joint piece ($B$ pointwise, $A$ as $\varphi$, $D$ as $\psi$), so it
commutes with both sign-change involutions. $\blacksquare$

**Theorem B (labelled extension).** With Theorem A's $g_0$ and the derived marked identification:
$g_0(H),g_0(\alpha)$ is a corner pair in $V'_{++}$ (corner bases map to corner bases); by the
marked-orbit lemma there is $\varphi\in O(V'_{++})$ with $\varphi(g_0H)=H_b$,
$\varphi(g_0\alpha)=\alpha_b$; by the flag-stabilizer lemma there is $h_L\in O(L)$ fixing the
second pair with $h_L|_{V'_{++}}=\varphi$. Then $g:=h_L\circ g_0$ conjugates the pairs and carries
$H\mapsto H_b$, $\alpha\mapsto\alpha_b$. $\blacksquare$

*This is the step an unlabelled discriminant surjectivity does not give:* the labelled statement
needs (i) the retained $H,\alpha$ identification derived from the construction (done above, not
assumed), (ii) the marked-orbit lemma, and (iii) the realization of an *integral* $(++)$-piece
isometry through the flag by a *discriminant* lift on the $T_\sigma$-side that satisfies the graph
compatibility equation — (ii)+(iii) proved above with N1 applied to $D$ only.

## 7. What this does not settle (kept separate)

1. **The chamber clause** of A21 (all of R1–R5): untouched here. m4's accepted report is the
   standing state: under R5 ($=$ the corpus's adopted reading) no $O(L)$-level result implies the
   chamber ($(Lat)\nRightarrow(Chm)$, certified separation $\nu(b_0)=0$, $\nu(b_\star)=4$);
   what suffices is the period statement (Hdg) via $2H-\alpha$ ample + effective Torelli, and the
   twist side currently has no member/period (entangled with 8(d)(b)).
2. **The authored second slot of the twist** (@cons:reflection-twist): textually undefined;
   no slot is called original. Lattice-level remark only (m2's Lemma 1): with $V_{-+}=0$ the
   *second* operator is structurally pinned by its invariant piece inside $S_\sigma$; this does
   not identify the corpus's undefined text.
3. **(O1)/(O2) of `sm00_arithmetic-core.md`** concern the non-2-elementary decomposition
   $L\supset\langle H,\alpha\rangle\perp K$ (discriminants $\mathbb Z/4\times\mathbb Z/2$): no
   surjectivity theorem applies there, the double coset is genuinely nontrivial, and nothing here
   answers or needs them.
4. **R4 recovery** (whether $\gamma(\mathfrak c)=\gamma\mathfrak c'$ in general forces
   $\gamma\operatorname{Pic}=\operatorname{Pic}'$): open, unaffected.
5. $k\ge2$ saturation, the downstream m7-depaudit citation sites: unchanged, still queued.

## 8. Hostile-reader checklist

- N1's applicability: only to $D$/$T_\sigma$, checked hypothesis-by-hypothesis in §1 (even,
  indefinite $(2,9)$, 2-elementary $a=11>2$). The in-repo verbatim statement is at
  `references/literature/lattice-research/nikulin1979integral.md`:1595; its context (§3.6) and
  proof are on the page.
- N1 is *discriminant*-surjectivity; the marked extension uses it inside the proved
  flag-stabilizer lemma (§6), not alone.
- The graph property $(\gamma$ onto$A)$ rests on Lemma L2's index-1 equality
  $\det(A)|\det B|=|\det S_\sigma|$ on **both** sides — maintained model-side, theorem b-side.
- $(\star)$'s geometric premise is exactly „$\iota_b$ symplectic on a K3" (authored bullet,
  uniform), and N4's conclusion is cited with its own hypotheses (Ni1 4.7 + the explicit
  realization, vGS §§1.1–1.3).
- The $H,\alpha$ frame is derived from the construction items + index-1 saturation (§6), in
  identical coordinates on both sides; the marked orbit and the compatibility equation are proved,
  not cited.
- All-$b$ uniformity: §5 lists every input with its hypotheses; each is uniform over the stated
  locus; no transport step appears anywhere.
- Exploratory scripts: `verify2` (m2), `certificate` (m5), `verify_pieces/gluing`, `saturate` (m6)
  are exploratory; the proof uses none of their outputs as validation. The maintained-tier artifact
  is `computations/reports/coble_joint_flag_premises.py` + `-run.txt` (provider semantic calls at
  the pin; the transplanted, deduplicated form of the m3 check, with the one print line that had
  repeated the false discriminant-image claim corrected, and every computed value unchanged).
- Swarm state: accepted — m2 (d7), m3 (d5), m4 (d3); audits m5, m6 retained as proofs with their
  scripts demoted; d2 (explicit witness), d4 (group-action classification), d1 (gluing
  enumeration), d8 (mod-2 shadow) continue as of writing.
