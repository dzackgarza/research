# A21, arithmetic core: the degree-4 class and the effective root carry no freedom

Member m1, direction d8. Question posed: *is the pair (degree-4 class, effective root) of the
authored tuple determined up to $O(L_{K3})$, or does the numerical data leave several orbits?*
Answer proved here: the pair is **pinned inside the invariant lattice** (Theorems 2 and 3), the
invariant lattice $U(2)$ cannot host it (Theorem 4), and the orthogonal complement of the pair has
a gluing-independent invariant $|\det| = 8$, $A_K \cong \mathbb Z/2 \times \mathbb Z/4$,
$q_K \cong -q_N$ (Theorems 5.3 and 5.4, verified for ten gluings). What remains is exactly one arithmetic
question, named in §6 with its two missing hypotheses. Nothing in this file asserts an integral
eigensplitting of $H^2(X,\mathbb Z)$; the only uses of the rational splitting are index
computations (§5), which are not splittings.

Notation. All lattices are integral, even where stated. $U(2)$ is the lattice with Gram matrix
$\begin{pmatrix}0&2\\2&0\end{pmatrix}$ on a basis $h_1,h_2$ ($h_i^2=0$, $h_1h_2=2$);
$E_8(-2)$ is $-2\cdot$(E8 Cartan), negative definite, all squares in $4\mathbb Z$;
$\langle -2\rangle = \mathbb Z d$ with $d^2=-2$; $L = L_{K3} = U^3 \perp E_8(-1)^2$, even,
unimodular, signature $(3,19)$. For a lattice $M$, $A_M = M^*/M$ with its discriminant form
$q_M \colon A_M \to \mathbb Q/2\mathbb Z$, $q_M(x) = x^2 \bmod 2\mathbb Z$, polar form
$b_M(x,y) = 2x\!\cdot\!y \bmod 2\mathbb Z$; $N^\perp$ denotes the orthogonal complement in the
ambient lattice.

## 1. Inputs, and which of them are hypotheses

* **H1 (type of the invariant lattice).** $S_\Co := L^{I_\Co = 1} \cong U(2)\perp E_8(-2)\perp\langle -2\rangle$,
  i.e. the even $2$-elementary lattice $I_{1,10}(2)$: rank $11$, determinant $2048$, signature
  $(1,10)$, $A_{S_\Co}\cong(\mathbb Z/2)^{11}$. *Source*: report
  `writing/coble/heegner-report/coble-heegner-research-report.md`, `@prop:coble-eigenspaces`
  (the reflection-twist computation $I_\Co = w_\alpha I_{\mathrm{En}}$ in the model with
  $S_{\mathrm{En}} = U(2)\perp E_8(-2)$, $T_{\mathrm{En}} = U\perp U(2)\perp E_8(-2)$, root
  $\alpha = e-f$ of the first $U$). **This is the type of the twist model. That the
  construction's own involution has this type is `@prob:twist-identification`, recorded as open in
  the report; so H1 is a hypothesis about the tuple, not a theorem about the construction.**
  Two independent findings of this swarm bear on it and must be read with it: (i) for the
  construction's own sublattice $\Lambda = \pi^*\mathrm{Pic}(Y)\perp\mathbb Z D$, primitivity in
  $S_{\mathrm{dP}}$ is *equivalent* to $\det S_{\mathrm{dP}} = 8$, the alternative being the even
  lattice $U\perp\langle-2\rangle$ of determinant $2$ (d7, finding f2(B)); (ii) the inference
  "$S_{\mathrm{dP}}\subseteq S_\Co$ because the rulings are $I_\Co$-invariant" is not valid — it
  yields only $U(2) = \pi^*\mathrm{Pic}(Y)$ in both (d4/m8, finding f4(2)). So H1 is exactly the
  saturation statement, and it is *not* established.
* **H2 (degree-4 class).** $H = \pi^*\mathcal O(1,1) = h_1 + h_2$ lies in the $U(2)$ summand of
  $S_\Co$; $H^2 = 4$. (This is the construction's own class, and `pinned` in
  `computations/reports/sm57_lean-report.md` §2 recovers it from $H^2=4$ and $H\cdot\alpha=0$
  inside $\Lambda = U(2)\perp\langle -2\rangle$.)
* **H3 (root).** $\alpha^2 = -2$, $H\cdot\alpha = 0$, $\alpha \in S_\Co$ (bullet 3 of the
  authored list: $\alpha$ is fixed by $I_\Co$). We do *not* assume that $\alpha$ is the
  $\langle-2\rangle$ generator; Theorem 3 derives it.
* **H4 (complement).** $T_\Co := (S_\Co)^\perp_L \cong \langle 2\rangle \perp U(2)\perp E_8(-2)$,
  rank $11$, determinant $-2048$, signature $(2,9)$, and $[S_\Co \oplus T_\Co : L] = 2^{11}$.
  Source: same proposition; it is the statement that $S_\Co,T_\Co$ are *primitive* orthogonal
  complements glued maximally. Audited here, see §7.

## 2. Theorem (degree-4 pinning; the corpus's statement, reproved)

**Theorem 2.** Let $x = a h_1 + b h_2 + cd \in \Lambda := U(2)\perp\langle-2\rangle \subset S_\Co$
with $x^2 = 4$ and $x\cdot\alpha = 0$ for $\alpha = \pm d$. Then $x = \pm(h_1+h_2)$.

*Proof.* $x\cdot d = -2c$, so $c = 0$. Then $x^2 = (ah_1+bh_2)^2 = 2ab\,(h_1\cdot h_2) = 4ab$
(using $h_1^2=h_2^2=0$, $h_1h_2=2$), so $ab = 1$ over $\mathbb Z$, hence $a = b = \pm1$. $\square$

## 3. Theorem (root pinning; new)

**Theorem 3.** In $S_\Co = U(2)\perp E_8(-2)\perp\langle -2\rangle$ with $H = h_1+h_2$,
$$\{\beta \in S_\Co \;:\; \beta^2 = -2,\ \beta\cdot H = 0\} = \{d,\,-d\}.$$
Consequently, under H1–H3 the effective root of the tuple is *not* a choice: it is the
$\langle-2\rangle$ generator up to sign, it lies in $S_{\mathrm{dP}} = U(2)\perp\langle-2\rangle$,
and bullet 3 carries no freedom beyond the sign, which nef/big effectivity fixes.

*Proof.* Write $\beta = a h_1 + b h_2 + e + cd$ with $a,b,c\in\mathbb Z$, $e \in E_8(-2)$. First,
$\beta\cdot H = (ah_1+bh_2)\cdot(h_1+h_2) = 2(a+b)$ because $E_8(-2)\perp H$ and $d \perp H$; so
$b = -a$. Second, $\beta^2 = (ah_1+bh_2)^2 + e^2 - 2c^2 = 4ab + e^2 - 2c^2 = -4a^2 + e^2 - 2c^2$.
Third, $E_8(-2)$ is negative definite and even: $e^2 \in 4\mathbb Z$ and $e^2 \le 0$ (the E8 Cartan
matrix has even diagonal, so $q_{E8}(x) = x^{\mathsf T}C x \in 2\mathbb Z$ for all $x$, and
$e^2 = -2q_{E8}(e) \in 4\mathbb Z$; definiteness gives $e^2 \le 0$). So
$$-4a^2 - 2c^2 + e^2 = -2 \iff 2a^2 + 2\tfrac{e^2}{4} + c^2 = 1,$$
where $\tfrac{e^2}{4} \in \mathbb Z$, $\tfrac{e^2}{4}\le 0$. All three summands are $\ge 0$
integers, so $2a^2 \le 1$, $c^2\le 1$, $\tfrac{e^2}{4} \le 0$; from $2a^2 + 2k + c^2 = 1$ with
$k \ge 0$: $a = 0$, $k = 0$, $c = \pm 1$; then $e^2 = 0$, and by definiteness $e = 0$. Hence
$\beta = \pm d$. $\square$

**Remark 3.1 (what this does and does not contradict).** The report
(`@prop:coble-eigenspaces`, paragraph "The root is a choice, and what is computed is not
uniqueness") warns that $T_{\mathrm{En}} = U\perp U(2)\perp E_8(-2)$ has many vectors of square
$-2$, e.g. $\beta = (e+f)+v$ with $v^2 = -4$ in $E_8(-2)$, so the *twist* is a choice of root of
$T_{\mathrm{En}}$. That is a statement about roots of the anti-invariant lattice, and it is
correct. Theorem 3 is the dual statement: once the invariant lattice and the degree-4 class are
fixed, $H^\perp_{S_\Co}$ is negative definite of rank $10$ and contains exactly one antipodal pair
of $(-2)$-vectors. So the freedom in the *twist construction* and the freedom in the *authored
bullet 3* are not the same freedom; the authored bullet has none.

**Remark 3.2 (the geometric counterpart, and the scope of Theorem 3).** Theorem 3 is a statement
about the *twist type* H1. Its geometric counterpart is proved for every one-node member without
any type hypothesis: $H = L_1+L_2$ with $L_i = \pi^*(\text{ruling})$ nef, so an irreducible curve
$C$ with $H\cdot C = 0$ has $L_1\cdot C = L_2\cdot C = 0$, hence $\pi(C)$ is a point and $C$ is one
of the exceptional curves $D_g$; for $k = 1$ the only effective $(-2)$-classes orthogonal to $H$
are $\pm\alpha$ (d7/m5, finding f2(A), proved from the construction). So the *effective* root is
unique unconditionally, and Theorem 3 adds that under H1 the *lattice-level* set of $(-2)$-vectors
orthogonal to $H$ is no bigger. If H1 fails, only the geometric statement survives, and the
lattice-level pinning of Theorem 3 must be re-examined against the actual type of $S_\Co$.

**Remark 3.3.** Theorem 3 also shows bullet 3 is not implied by bullet 2 alone: $H^2 = 4$ alone
does not pin $H$ (e.g. $h_1 + 2h_2 + r$ with $r \in E_8(-2)$ a root has square
$8 - 4 = 4$). Pinning of $H$ needs $H \in \Lambda$, which is H2, i.e. the construction's own
identification $H = \pi^*\mathcal O(1,1)$.

## 4. Theorem (the "weaker abstract reading" cannot host bullet 3)

**Theorem 4.** There is no embedding of $\langle 4\rangle \perp \langle -2\rangle$ into $U(2)$;
equivalently, there are no $x,y \in U(2)$ with $x^2 = 4$, $y^2 = -2$, $x\cdot y = 0$.

*Proof.* $U(2)$ has rank $2$ and determinant $-4$. A rank-$2$ sublattice $N \subseteq U(2)$ of
index $k \ge 1$ has determinant $\det N = \det U(2)\cdot k^2 = -4k^2$. The Gram matrix of
$(x,y)$ is $\begin{pmatrix}4&0\\0&-2\end{pmatrix}$ with determinant $-8$, and $-8 = -4k^2$ has no
integer solution. $\square$

**Consequence (audit).** The paragraph "The geometric reading, and a weaker abstract reading kept
separate" of the report considers the weaker reading "an involution of $L_{K3}$ with invariant
lattice $S = U(2)$, containing $H$". Theorem 4 says this weaker reading is *strictly* weaker:
it cannot be upgraded to include bullet 3. Any argument that uses $S_\Co = U(2)$ *and* $\alpha$ is
using an inconsistent hypothesis set; the report's `@prop:del-pezzo-placement` (which takes
$S_\Co = U(2)$ and $H \in U(2)$) is therefore a statement about a hypothesis set that no authored
tuple satisfies. This does not refute `@prop:del-pezzo-placement` — it delimits it.

## 5. The complement of the pair: a gluing-independent invariant

Let $N := \langle H,\alpha\rangle \subseteq S_\Co$ and $K := N^\perp_L$. Let
$B := N^\perp_{S_\Co} = \langle h_1-h_2\rangle \perp E_8(-2)$ (rank $9$, $\det B = -4\cdot 256 = -1024$).

**Lemma 5.1.** $H$ and $\alpha$ are primitive in $L$, and $N$ is primitive in $L$; $N \cong \langle4\rangle\perp\langle-2\rangle$, $\det N = -8$.

*Proof.* If $v = m w \in L$ with $m \ge 2$ and $w \in L$, then $|v^2| = m^2|w^2| \ge 4\cdot 2 = 8$
because $w^2$ is a nonzero element of $2\mathbb Z$ (L is even, w ≠ 0). So no vector of $L$ with
$v^2 = 4$ or $v^2 = -2$ is divisible by $m\ge2$: $H$ and $\alpha$ are primitive. For primitivity of $N$: $(H\pm\alpha)^2 =
4 - 2 = 2$ and $2/4 \notin 2\mathbb Z$, so $(H\pm\alpha)/2 \notin L$. $\square$

**Lemma 5.2.** $A^0 := \{x \in A_{S_\Co} : \varphi_H(x) = \varphi_\alpha(x) = 0\}$ has order $2^9$, where
$$\varphi_H \colon A_{S_\Co}\to \mathbb Z/2\mathbb Z,\qquad \varphi_H(x) := \tilde x\cdot H \bmod 2\mathbb Z,$$
and $\tilde x \in S_\Co^* = \tfrac12 S_\Co$ is any lift of $x$.

*Proof.* Well-definedness: $2\tilde x \in S_\Co$ gives $2(\tilde x\cdot H) = (2\tilde x)\cdot H \in H\cdot S_\Co = 2\mathbb Z$,
so $\tilde x\cdot H \in \mathbb Z$; and replacing $\tilde x$ by $\tilde x + s$, $s\in S_\Co$, changes
$\tilde x\cdot H$ by $s\cdot H \in 2\mathbb Z$. So $\varphi_H$ is a well-defined homomorphism (and
likewise $\varphi_\alpha$). Both are nonzero: $\varphi_H(h_1/2) = \tfrac12(h_1\cdot(h_1+h_2)) = 1$,
$\varphi_\alpha(h_1/2) = 0$, $\varphi_\alpha(d/2) = -1\equiv 1$. They are distinct, hence independent
in the dual of the $\mathbb F_2$-space $A_{S_\Co}\cong(\mathbb Z/2)^{11}$, and the joint kernel has
order $2^{11-2} = 2^9$. $\square$

**Lemma 5.2′ (what $A^0$ counts).** With H1–H4, $K/(B\oplus T_\Co)\cong A^0$.

*Proof.* $L/(S_\Co\oplus T_\Co) \cong A_{S_\Co}$; write the coset of a glue vector $u = (w/2, v/2)$
as $x$, $w \in S_\Co$. Then $u\cdot H = \tfrac12(w\cdot H) = \varphi_H(x)$ *as an element of
$\mathbb Z/2$*, and vectors of the same coset differ by elements of $S_\Co\oplus T_\Co$, changing
$u\cdot H$ by $2\mathbb Z$. So the coset meets $K$ iff $\varphi_H(x) = \varphi_\alpha(x) = 0$, and
then $K\cap(\text{coset})$ is a coset of $(S_\Co\oplus T_\Co)\cap K = B\oplus T_\Co$. Hence
$K/(B\oplus T_\Co)\cong A^0$. $\square$

**Theorem 5.3 (index count).** With H1–H4: $[S_\Co : N\oplus B] = 2$,
$[K : B\oplus T_\Co] = 2^9$, $[L : N\oplus K] = 8$, and hence
$$|\det K| = \frac{[L:N\oplus K]^2\,|\det L|}{|\det N|} = \frac{64}{8} = 8 .$$

*Proof.* (i) $\det N\cdot\det B = (-8)(-1024) = 8192 = 4\,\det S_\Co$, so $[S_\Co:N\oplus B]^2 = 4$.
(ii) $K\cap(S_\Co\oplus T_\Co) = B\oplus T_\Co$: an element of $S_\Co$ orthogonal to $H,\alpha$ is in
$B$ by definition of $B$, and $T_\Co\perp S_\Co\ni H,\alpha$ gives $T_\Co\subseteq K$. Hence
$K/(B\oplus T_\Co)\hookrightarrow L/(S_\Co\oplus T_\Co)$, and by Lemma 5.2$'$ the image is exactly
$A^0$, of order $2^9$ by Lemma 5.2. (iii)
$[L:N\oplus B\oplus T_\Co] = [L:S_\Co\oplus T_\Co]\cdot[S_\Co:N\oplus B] = 2^{11}\cdot2 = 2^{12}$, so
$[L:N\oplus K] = 2^{12}/2^9 = 8$. (iv) For a primitive sublattice $N\oplus K\subseteq L$ of finite
index, $\det N\cdot\det K = \det L\cdot[L:N\oplus K]^2$; with $|\det L| = 1$ and $\det N = -8$ this
gives $|\det K| = 64/8 = 8$. $\square$

**Theorem 5.4 (machine, ten gluings).** For ten independently found anti-isometries
$\gamma \colon A_{S_\Co}\to A_{T_\Co}(-1)$ — each producing an even unimodular rank-$22$ lattice of
signature $(3,19)$, hence isomorphic to $L_{K3}$ — the complement of $N$ has
$$|\det K| = 8,\qquad A_K\cong \mathbb Z/2\times\mathbb Z/4,\qquad
q_K \cong -q_N = \langle -\tfrac12\rangle \perp \langle -\tfrac14\rangle,$$
with no variation. The quadratic Gram matrices printed by the run are
$q_K = \begin{pmatrix}3/2&1/2\\1/2&7/4\end{pmatrix}$ against
$q_N = \begin{pmatrix}1/2&1/2\\1/2&1/4\end{pmatrix}$ (convention $q(a) = a^{\mathsf T}Ma$); all
$q$-values on the four generators of $\mathbb Z/2\times\mathbb Z/4$ agree between $q_K$ and $-q_N$, and
so do the four $b$-values, so $q_K\cong -q_N$. The same invariant is obtained for three pairs in the standard model
$U^3\perp E_8(-1)^2$ with $H = e_1+f_1+e_2+f_2$ and $\alpha \in \{e_1-f_1,\ e_2-f_2,\ r\}$
($r$ an $E_8(-1)$ root). Certificate: `a21_arithmetic.sage`, log `a21_arithmetic-run.txt`,
comparison `qcompare.py`.

**Reading of Theorem 5.** The pair $(H,\alpha)$ has no arithmetic invariant that distinguishes
members: not its determinant, not its discriminant group, not its discriminant form. Whatever
distinguishes two tuples, it is *not* the local arithmetic of the degree-4 class and the root.

## 6. The exact open point

What Theorem 5 does *not* settle is whether $K$ itself is unique up to isometry. Precisely:

> **(O1)** Does the genus of even lattices of rank $20$, signature $(2,18)$, discriminant form
> $q_K \cong -q_N \cong \langle-\tfrac12\rangle\perp\langle-\tfrac14\rangle$, have class number $1$?
>
> **(O2)** Does $O(K) \to O(q_K)$ act transitively on the set of anti-isometries
> $A_N \to A_K$ modulo $O(N) = \{\pm 1\}$ (the Eichler/spinor condition for the gluing)?

If (O1) and (O2) hold, then any two primitive embeddings of $N \cong \langle4\rangle\perp\langle-2\rangle$
into $L_{K3}$ with the numerical data of §1 and $H,\alpha$ in the positive cone are conjugate by
$O(L_{K3})$, and the "degree-4 class + effective root" clause of A21 is arithmetic — no family and
no Gauss–Manin transport needed for that clause. If (O1) fails, there are two non-conjugate pairs,
and A21's clause holds only because the construction's periods single out one gluing; then the
clause is a period statement, not an arithmetic one. **This is the boundary that the swarm's
answer should state.** H1 is needed for both alternatives; it is the same hypothesis as the
corpus's open `@prob:twist-identification`.

## 7. Audited numbers (independent run)

From `a21_arithmetic-run.txt`: $\det S_\Co = 2048$, rank $11$, signature $(1,10)$,
$A_{S_\Co}\cong(\mathbb Z/2)^{11}$, even; $\det T_\Co = -2048$, rank $11$, signature $(2,9)$,
$A_{T_\Co}\cong(\mathbb Z/2)^{11}$, even; $L$ unimodular, signature $(3,19)$, even;
$(2H-\alpha)^2 = 14 > 0$ and $H\cdot(2H-\alpha) = 8 > 0$, so $H$ and $2H-\alpha$ lie in the same
component of the positive cone; $H^2/4 = 1$ and $(\alpha/2)^2 = -1/2$, so $H,\alpha$ are primitive;
$((H\pm\alpha)/2)^2 = 1/2$, so $N$ is primitive; the integer solutions of $2a^2+2k+c^2 = 1$,
$k\ge 0$, are $(a,c,k) = (0,\pm1,0)$, which is Theorem 3's arithmetic core. That core, Theorem 2,
and Theorem 4 are also machine-checked in Lean (`a21_core.lean`).

## 8. Consequence for the authored problem

Under H1–H4:

1. Bullets 2 and 3 carry **no freedom**: given the construction's $H = \pi^*\mathcal O(1,1)$ and
   the type of the invariant lattice, $\alpha = \pm d$ (Theorem 3), and given $\alpha$, $H$ is
   pinned up to sign by $H^2 = 4$, $H\cdot\alpha = 0$ (Theorem 2).
2. Hence the freedom in a tuple is confined to (a) the placement of the pair of involutions,
   i.e. of $S_\Co, S_{\mathrm{dP}}$ in $L_{K3}$ — the period datum, the corpus's
   `@prob:twist-identification` — and (b) the chamber $\mathfrak c$. Of the four clauses of A21,
   the degree-4 and root clauses are therefore not where the difficulty lies, and Theorem 5 shows
   the arithmetic of the pair presents no obstruction at all.
3. The chamber clause is not covered here. On the swarm's current evidence it is false: the
   $H$-degree-$1$ census $\nu$ takes the value $0$ on the corpus member and $\ge 4$ on a verified
   bitangent witness (d7/m5, finding f8), and $\nu$ is carried by a chamber-preserving isometry
   (the invariance argument is the negative-half direction's). If that invariance is granted, A21
   as authored is false, while its $\{$labels, degree, root$\}$ part is exactly as strong as H1 plus
   the placement statement, i.e. as `@thm:a21-labels` with its family input. Nothing in this file
   supports, and nothing needs, an integral eigensplitting.

## 9. Files

* `proof.md` — this file.
* `a21_arithmetic.sage`, `a21_arithmetic-run.txt` — the certificates of §7, §5.
* `clat.py` — lattice builders, anti-isometry search, gluing, complement computation.
* `qcompare.py`, `qcompare.out` — the discriminant-form comparison $q_K \cong -q_N$.
* `a21_core.lean`, `a21_core-run.txt` — Lean 4.33.1 + Mathlib, compiles with no `sorry` and no
  warnings: `A21Core.pinned_root` (the integer core of Theorem 3), `A21Core.deg4_pinned`
  (Theorem 2), `A21Core.no_deg4_root_in_U2` and `A21Core.det_index_sq` (Theorem 4).
