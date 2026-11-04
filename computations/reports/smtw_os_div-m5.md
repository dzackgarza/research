# O-S — Saturation of $\Lambda$ in $S_{\mathrm{dP}}$: **decided, $\det=8$** (corrected version)

**Claim (Theorem O-S).** For every member $b$ of the one-node locus $B_p$ of the direct-projective
construction (`writing/coble/heegner-report/coble-heegner-research-report.md` §sec-cover-quotient;
`writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md`
@prop:one-node-connected), and by the symmetry of the construction for the three other $\tau$-fixed choices
of node,
$$S_{\mathrm{dP},b}\;=\;H^2(\widehat X_b,\mathbb Z)^{I_{\mathrm{dP}}=+1}\;=\;\Lambda \;=\;\pi_b^*H^2(\widehat Y,\mathbb Z)
\;\cong\;U(2)\perp\langle-2\rangle,\qquad \det=8,\quad [S_{\mathrm{dP},b}:\Lambda]=1 .$$
The alternative of `rmk:a21-scope` — the index-$2$ overlattice $U\perp\langle-2\rangle$ of determinant $2$ — **does
not occur**. The deciding statement is a **divisibility** statement about the two flat ruling classes, and it is
settled by two explicit certified members, one for each ruling.

**What changed from the first submission, and why.** My first proof rested on a universal lemma "no algebraic class
$w$ has $w\cdot F=1$ for $F\in\{e_b,f_b\}$", via a Riemann–Roch/section argument whose last step claimed that a double
cover with nonempty branch divisor is irreducible. **That lemma is false and that step is wrong:** when the
restriction of the branch section to the ruling $D$ is a *perfect square*, the cover splits into two sections meeting
at the tangency points. The corpus already contains the counterexample: on the certified member $b_\star$ the ruling
$\{x=1\}$ is bitangent and the cover splits as $C_++C_-=\widehat\pi^\ast_{b_\star}\{x=1\}$ with
$C_\pm\cong\mathbb P^1$, $C_\pm^2=-2$, $C_\pm\cdot f_{b_\star}=1$ (`computations/reports/sm57_proof-m5.md` §6,
lines 216–227). So algebraic classes of odd degree against a ruling class **do** exist, and the whole
Riemann–Roch/section instrument is the wrong tool: nothing about sections is needed. What decides the index is
whether the ruling class is $2$-divisible in $H^2$, and that is refuted by exhibiting one class of odd pairing —
and the corpus's witness does exactly that for $f_b$, while a **new witness in this document does it for $e_b$**.
The corpus's own recorded route ("splitting needs $D\cdot\widetilde B=0$, and among $D=ah_1+h_2+ce$ only $h_2-h_1$ has
square $\ge-2$ and it is not effective, so this route is closed") is also incomplete for the same reason: sections
arise from *square* restrictions, not only from $D\cdot\widetilde B=0$, and no square bound is relevant.

Nothing below uses an integral eigensplitting of $H^2$, a chamber/translation detector, or any chamber claim.

---

## 1. The invariant lattice of the resolved cover

$Y=\mathbb P^1\times\mathbb P^1$, affine coordinates $(x,y)$, $p=(0,0)$, $\tau=(-1,-1)$ (the corpus's normalisation,
`sm57_proof-m5.md` line 39). Let $f\in H^0(\mathcal O_Y(4,4))^\tau$ have an ordinary node at $p$ and be smooth
elsewhere (the locus $B_p$), $\widehat Y=\Bl_pY$, and $\pi_b:\widehat X_b\to\widehat Y$ the K3 double cover branched
along the proper transform $\widetilde B\in|-2K_{\widehat Y}|$. Put
$$e_b=\pi_b^*h_1,\quad f_b=\pi_b^*h_2,\quad \alpha_b=[D_b]=\pi_b^*e,\quad H_b=e_b+f_b=\pi_b^*\mathcal O(1,1),$$
$$\Lambda:=\pi_b^*H^2(\widehat Y,\mathbb Z)=\langle e_b,f_b,\alpha_b\rangle .$$
With $M:=H^2(\widehat Y,\mathbb Z)=\langle h_1,h_2,e\rangle$, $\det M=+1$ (unimodular), odd, signature $(1,2)$:
$e_b^2=2h_1^2=0$, $f_b^2=0$, $e_b\cdot f_b=2$, $\alpha_b^2=2e^2=-2$, $\alpha_b\cdot e_b=\alpha_b\cdot f_b=0$, so
$\Lambda\cong M(2)=U(2)\perp\langle-2\rangle$, $\det\Lambda=2^3\det M=8$, signature $(1,2)$, $A_\Lambda=(\mathbb Z/2)^3$.

**Rank.** $H^2(\widehat X_b,\mathbb Q)^{+}=\pi_b^*H^2(\widehat Y,\mathbb Q)$ (for a double cover $\pi^*$ is injective
and $\pi_*\pi^*=2$, and the invariant part of $H^2$ of a double cover of a smooth surface has the rational dimension
$b_2$ of the base, here $3$), so $\operatorname{rk}S_{\mathrm{dP},b}=3$ — matching the Lefschetz count
$\operatorname{rk}S=\frac12(20+\chi(\mathrm{Fix}))=\frac12(20-14)$ for the fixed locus $R\cup D_b$ of
$\widehat\iota_{\mathrm{dP}}$ (`prop:tuple-of-the-construction`, part 5). Hence $\Lambda\subseteq S_{\mathrm{dP},b}$
has equal ranks, and since $S_{\mathrm{dP},b}$ is even (it lies in the even lattice $H^2(\widehat X_b,\mathbb Z)$),
$$[S_{\mathrm{dP},b}:\Lambda]^2=\frac{\det\Lambda}{\det S_{\mathrm{dP},b}}=\frac{8}{\det S_{\mathrm{dP},b}}
\quad\Longrightarrow\quad [S_{\mathrm{dP},b}:\Lambda]\in\{1,2\},$$
i.e. $\det S_{\mathrm{dP},b}\in\{8,2\}$ and nothing else. **Only two candidates exist.**

## 2. The criterion (provider-certified census)

`computations/reports/sdp_discriminant_referee.py` + `sdp_discriminant_referee-run.txt`, maintained provider pin
`c546077d`:

```
det M: 8
integral-valued nonzero half-classes (a,b,c,q): [(0, 1, 0, 0), (1, 0, 0, 0)]
  generated overlattice det would be 2
  generated overlattice det would be 2
```

Of the seven nonzero classes of $A_\Lambda$ (written $a\frac{e_b}2+b\frac{f_b}2+c\frac{\alpha_b}2$), exactly
$\overline{e_b/2}$ and $\overline{f_b/2}$ are integral with even square, and each generates an even overlattice of
type $U\perp\langle-2\rangle$, determinant $2$. Every class involving $\frac{\alpha_b}2$ is non-integral
($(\frac{\alpha_b}2)^2=-\frac12$), and $\frac{e_b+f_b}2$ is integral with odd square $1$. Therefore

> **Criterion.** $[S_{\mathrm{dP},b}:\Lambda]=2\iff \tfrac12 e_b\in H^2(\widehat X_b,\mathbb Z)$ or
> $\tfrac12 f_b\in H^2(\widehat X_b,\mathbb Z)$; equivalently $\iff$ $e_b$ or $f_b$ has even pairing with every
> integral class; equivalently $\iff$ $S_{\mathrm{dP},b}$ contains an $I_{\mathrm{dP}}$-invariant integral class of
> odd pairing against a ruling class.
>
> Indeed an index-$2$ overlattice is $\Lambda+\mathbb Z w$ with $2w\in\Lambda$; such a $w$ is automatically
> $I_{\mathrm{dP}}$-invariant ($2(Iw-w)=0$ and $H^2$ is torsion-free), lies in $S_{\mathrm{dP},b}$, and satisfies
> $w\cdot f_b$ or $w\cdot e_b$ odd (the two census classes are $\overline{e_b/2}$ and $\overline{f_b/2}$); conversely
> an invariant $w$ with $w\cdot e_b$ or $w\cdot f_b$ odd is not in $\Lambda$ (elements of $\Lambda=\pi^*M$ satisfy
> $\pi^*c\cdot\pi^*h_i=2(c\cdot h_i)\in2\mathbb Z$) and forces index $2$.

This is the question `rmk:a21-scope` records, in the correct (divisibility) form.

## 3. Neither ruling class is $2$-divisible: two witnesses

Both witnesses must lie in the *same* connected family, and they do: both are members of $B_p$ (node at
$p=(0,0)$, smooth elsewhere, $\tau$-invariant), which is path-connected by @prop:one-node-connected.

*Robustness.* The argument uses connectivity only to transport a divisibility fact from a witness to the member of
interest; it needs the two points to lie in one path-component of $B_p$, which @prop:one-node-connected supplies
(the pencil argument: for $f_0,f_1\in B_p$ the pencil $\langle f_0,f_1\rangle\subset H$ meets the bad conditions —
shared base point, degenerate quadratic part at $p$, singularity off the base locus — in a finite set, and a punctured
$\mathbb P^1$ is connected). If that connectedness is not granted, the theorem holds verbatim for every member of the
path-component of $b_\dagger$ and of $b_\star$; nothing else in the argument uses it.

**Flatness.** Over $B_p$ the base $\widehat Y$ is fixed and $e_b=\pi_b^*h_1$, $f_b=\pi_b^*h_2$ are pullbacks of fixed
classes: flat sections of $R^2\widehat\pi_*\mathbb Z$. Membership in $2H^2$ is preserved by isometries, so
"$e_b$ is $2$-divisible" and "$f_b$ is $2$-divisible" are **constant on $B_p$**. One class of odd pairing at one
member therefore settles it for every member.

**(W1) $f_b$ is not $2$-divisible: already in the corpus.** On the certified member $b_\star$
($f_\star=8x^4y^4+7x^4y^2+6x^4+5x^3y^3+4x^3y+3x^2y^4+2x^2y^2+3x^2-13xy^3-28xy-10y^4+13y^2$) the ruling
$\{x=1\}$ is bitangent ($f_\star(1,y)=(y-1)^2(y-3)^2$) and the cover splits:
$C_++C_-=\widehat\pi^\ast_{b_\star}\{x=1\}$, $C_\pm\cong\mathbb P^1$, $C_\pm^2=-2$,
$$C_\pm\cdot f_{b_\star}=h_2\cdot[\{x=1\}]=1\quad(\text{odd}).$$
Source: `computations/reports/sm57_proof-m5.md` §6, lines 216–227, with the chart and Gröbner verifications in
`computations/reports/sm57_verify_witness.py`, `sm57_verify_charts.py`. Hence
$\frac12 f_{b_\star}\notin H^2(\widehat X_{b_\star},\mathbb Z)$, hence $\frac12f_b\notin H^2$ for every
$b\in B_p$ by flatness and connectedness.

**(W2) $e_b$ is not $2$-divisible: new witness of this document.** Consider the member $b_\dagger$ with
$$f_\dagger=3x^4y^4+4x^4y^2-10x^4-x^3y^3+x^3y-12x^2y^4+12x^2y^2+6x^2-2xy^3+2xy-3y^4 .$$
Verified by the ordinary script `witness_bdag.py` (output `witness_bdag-run.txt`, in the style of the corpus's own
member checks — a record, not a certificate):

1. $f_\dagger$ is $\tau$-invariant (every monomial has even total degree);
2. $f_\dagger(0,0)=0$ with quadratic part $6x^2+2xy$, discriminant $4\ne0$: an ordinary node at $p$;
3. the singular locus of $B_\dagger$ is exactly the node: Gröbner bases of $\langle g,g_u,g_v\rangle$ are
   $\langle x,y\rangle$ in the chart $x_0y_0\ne0$ and $\langle1\rangle$ in each of the other three charts of
   $\mathbb P^1\times\mathbb P^1$ — so $b_\dagger\in B_p$;
4. **the $h_2$-ruling $D'=\{y=1\}$ is bitangent**: $f_\dagger(x,1)=-3(x-1)^2(x+1)^2$, and
   $\partial_yf_\dagger(\pm1,1)=-22,-10\ne0$, so $B_\dagger$ is smooth at the two tangency points and meets $D'$
   nowhere else.

$D'$ does not pass through $p$, so $\pi_{b_\dagger}^{-1}(D')\to D'$ is a double cover of $\mathbb P^1$ branched along
the doubled divisor $2[(1)]+2[(-1)]$; it therefore **splits**: $\pi^{-1}(D')=C'_++C'_-$ with $C'_\pm\cong\mathbb P^1$
meeting transversally at the two tangency points. Then
$$(C'_\pm)^2=\tfrac12\bigl((\pi^*D')^2-2C'_+C'_-\bigr)=\tfrac12(0-4)=-2,\qquad
C'_\pm\cdot e_{b_\dagger}=\tfrac12\bigl(\pi^*D'\cdot\pi^*h_1\bigr)=D'\cdot h_1=1\quad(\text{odd}),$$
the last equality by the projection formula (the analogous computation in the corpus is
$C_\pm\cdot f_{b_\star}=h_2\cdot D=1$). Hence $\frac12 e_{b_\dagger}\notin H^2(\widehat X_{b_\dagger},\mathbb Z)$,
and by flatness and connectedness $\frac12 e_b\notin H^2(\widehat X_b,\mathbb Z)$ for every $b\in B_p$.

## 4. Theorem and proof

> **Theorem O-S.** For every $b\in B_p$: $S_{\mathrm{dP},b}=\Lambda=\pi_b^*H^2(\widehat Y,\mathbb Z)
> \cong U(2)\perp\langle-2\rangle$, $\det 8$, index $1$. The $\det 2$ candidate does not occur. The same holds for the
> three other choices of $\tau$-fixed node, by the automorphisms of $Y$ preserving $\tau$ and $\mathcal O(4,4)$.

*Proof.* By §1 the index is $1$ or $2$; by the criterion of §2 it is $2$ only if $\frac12e_b$ or $\frac12f_b$ is
integral; by (W1), (W2) with flatness and connectedness neither is. $\square$

## 5. Consequences

1. **$\operatorname{Pic}=\Lambda$ in rank $3$.** If $\operatorname{rk}\operatorname{Pic}(\widehat X_b)=3$ then
   $S_{\mathrm{dP},b}=\Lambda\subseteq\operatorname{Pic}(\widehat X_b)$ are primitive of equal rank, so
   $\operatorname{Pic}(\widehat X_b)=\Lambda$, determinant $8$.
2. **$S_{\mathrm{dP}}\subseteq S_{\mathrm{Co}}$** (listed open in the research report's "A21 state of record"): the
   intersection has rank $\operatorname{rk}S_{\mathrm{dP}}=3$ (@prop:tuple-of-the-construction: it contains
   $\pi^*\mathrm{Pic}(Y)\perp\mathbb Z D_g$), and $S_{\mathrm{dP}}/(S_{\mathrm{Co}}\cap S_{\mathrm{dP}})$ embeds in the
   torsion-free $L_{K3}/S_{\mathrm{Co}}$, so it is trivial. This uses only ranks, not Theorem O-S.
3. **The $k=0$ (node-free) case: $U(2)$, not $U$.** The criterion of §2 applies verbatim with $M=H^2(Y)$
   ($\widehat Y=Y$, rank $2$): the candidates are again $e_b/2$ and $f_b/2$ (the third coset, $h_1+h_2$, has odd
   square $2$). One witness suffices here, because the node-free locus *is* stable under the swap of the two factors,
   so "$f_b$ is $2$-divisible" and "$e_b$ is $2$-divisible" are equivalent on it. The witness is the member $b^0$ with
   $$f_0=9x^4y^4-12x^4y^2+9x^4+12x^3y^3-12x^3y-6x^2y^4+8x^2y^2-14x^2+9xy^3-9xy+6y^4-6y^2+6,$$
   verified by `witness_k0_verify.py` / `witness_k0_verify-run.txt`: $\tau$-invariant, $f_0(p)=6\ne0$ (so no node at
   $p$), smooth in all four charts (Gröbner basis $\langle1\rangle$ in each), and $f_0(x,1)=6(x-1)^2(x+1)^2$ with
   $\partial_yf_0(\pm1,1)=58,-26\ne0$: the ruling $\{y=1\}$ is bitangent, the cover splits, and
   $C'_\pm\cdot e_{b^0}=h_1\cdot[\{y=1\}]=1$ is odd. So $\frac12e_b\notin H^2$ on the node-free locus, and by the swap
   symmetry the same holds for $f_b$; hence
   $S_{\mathrm{dP},b}=\pi_b^*H^2(Y)\cong U(2)$ there. The corpus's "at $k=0$ the invariant lattice is $U(2)$ or $U$
   and which of the two is not decided here" (`rmk:a21-open`) is thereby $U(2)$.
   Consistency check: the classification relation $r=a$ for non-symplectic involutions (Nikulin;
   Artebani–Sarti–Taki, arXiv:0903.3481) gives $(r,a)=(2,2)$ for $U(2)$ and $(3,3)$ for $\Lambda$, both matched.
4. **All $k$.** Same argument at any $k$: the only non-$U(2)$ candidates are the ruling halves, excluded by (W1), (W2).

## 6. Why sections are the wrong instrument (record for the corpus)

The corpus's `rmk:a21-scope` argues that an index-$2$ overlattice would be generated by an $I_{\mathrm{dP}}$-invariant
section-type class, and tries to exclude such classes by a square bound on curves
$D=ah_1+h_2+ce\subset\widehat Y$. That argument cannot work, in either direction:

* the index question is about **integral classes**, not about effective curves of bounded square, and
* sections do exist: whenever the restriction of the branch section to a ruling is a perfect square, the double cover
  splits and produces two sections (the corpus's $b_\star$; this document's $b_\dagger$).

What is true, and is what decides the question, is the divisibility statement of §2–§4: the ruling classes are not
$2$-divisible, witnessed by one odd-degree class each. In particular my earlier universal "no odd-degree algebraic
class" lemma is **withdrawn** (it survives only in the version "no integral *effective* $I_{\mathrm{dP}}$-invariant
divisor has odd degree against a ruling class", which does not decide the index because the index-$2$ class need not
be effective); the correct statements are (W1), (W2) and Theorem O-S.

## 7. What is not claimed

* No chamber/effectivity/nefness statement; `@prob:effective-cone-agreement` is untouched.
* Nothing about the type of $S_{\mathrm{Co},b}$ (the companion document `O-T-twist-identification.md` §6 reduces the
  twist identification to that single binary).
* The two witness verifications are ordinary scripts (Gröbner/sympy), recorded as such; the only provider-grade
  certificate used is the discriminant census of §2 at pin `c546077d`.

## 8. Artefacts

| item | path |
|---|---|
| census of $A_\Lambda$ and its even overlattices (provider pin `c546077d`) | `computations/reports/sdp_discriminant_referee.py`, `sdp_discriminant_referee-run.txt` |
| (W1): bitangent member $b_\star$, $C_\pm\cdot f_{b_\star}=1$ | `computations/reports/sm57_proof-m5.md` §6 (lines 216–227), `sm57_verify_witness.py`, `sm57_verify_charts.py` |
| (W2): bitangent member $b_\dagger$, $C'_\pm\cdot e_{b_\dagger}=1$ | `witness_bdag.py`, `witness_bdag-run.txt` (this directory) |
| $k=0$ witness $b^0$ ($U(2)$, not $U$) | `witness_k0.py`, `witness_k0-run.txt`, `witness_k0_verify.py`, `witness_k0_verify-run.txt` |
| connectedness and flatness over $B_p$ | `@prop:one-node-connected`, `@prop:one-node-family`, `@prop:one-node-transport` |
| the statement decided, verbatim | `rmk:a21-scope` (lines 714 ff.), `rmk:a21-open` (lines 684–699) |
