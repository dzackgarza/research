# O-S decided: Λ is saturated in S_dP, so det S_dP = 8 (index 1)

Member m6, direction d2 of swarm `smw0dbvr6`. Repository read **read-only** at evidence state
`main@141058a8`, `/workspace/nucleus/work/projects/p-9fcb4ed7f4b64e008de2ee29a7197bf4/repo`;
citations are relative to that root. Nothing in the repository was modified.

**Verdict.** For every one-node member of the direct-projective construction,

$$S_{\mathrm{dP},b}=H^2(\widehat X_b,\mathbb Z)^{I_{\mathrm{dP}}=1}
=\Lambda_b:=\pi^*H^2(\widehat Y,\mathbb Z)=\langle e_b,f_b,[D_b]\rangle\cong U(2)\perp\langle-2\rangle,$$

so $[S_{\mathrm{dP},b}:\Lambda_b]=1$ and $\det S_{\mathrm{dP},b}=8$: the determinant-$2$ alternative
$U\perp\langle-2\rangle$ **does not occur**. The same argument settles the $k=0$ question left open in
`@rmk:a21-open` ($S_{\mathrm{dP}}\cong U(2)$, not $U$). No integral eigensplitting of
$H^2(\widehat X_b,\mathbb Z)$ is used, and no chamber or translation-invariance detector appears.

Conventions. $L=H^2(\widehat X_b,\mathbb Z)\cong L_{K3}$, even and unimodular;
$U(2)=(\mathbb Z^2,\left(\begin{smallmatrix}0&2\\2&0\end{smallmatrix}\right))$;
$\langle-2\rangle=\mathbb Z d$, $d^2=-2$; $A_M=M^\#/M$ with $q_M(x)=x^2\bmod2\mathbb Z$; $E_8(-2)$ is
the form $2\cdot$(negative definite $E_8$), $\det=2^8$ (the corpus's $E_8(2)$).

---

## §0 What is *not* proved here and not used

Not proved, not used: any integral eigensplitting $L=S\oplus T$; any statement about
$S_{\mathrm{Co},b}$; any statement about $k\ge2$; anything about chambers or effective cones. Of
$S_{\mathrm{dP},b}$ only its **rank** and its **evenness** are used, both with proofs in the corpus
that I did not redo.

## §1 Inputs, exactly as the corpus states them

$Y=\mathbb P^1\times\mathbb P^1$, $\tau([x_0:x_1],[y_0:y_1])=([-x_0:x_1],[-y_0:y_1])$, $p\in Y$ a
$\tau$-fixed point, $B=\{f=0\}\subset|\mathcal O_Y(4,4)|^\tau$ with exactly one ordinary node, at $p$,
and otherwise smooth with nondegenerate quadratic part at $p$; $X^\sharp=\{z^2=f\}$,
$\widehat X_b\to X^\sharp$ the resolution of the node, $D_b$ the exceptional $(-2)$-curve,
$\pi:\widehat X_b\to\widehat Y=\mathrm{Bl}_pY$ the induced double cover branched along the proper
transform $\widetilde B$ of $B$, $H_b=\pi^*\mathcal O_Y(1,1)$
(`@prop:one-node-family`, `@prop:local-operators`, `@prop:del-pezzo-type-on-the-resolution` in
`writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md`).

**I1 (rank).** $\mathrm{Fix}(\widehat\iota_{\mathrm{dP}})=\widetilde B$, the normalisation of $B$, of
geometric genus $8$; hence $\chi(\mathrm{Fix})=2k-16=-14$ and, by Lefschetz
$\rk S_{\mathrm{dP}}=\tfrac12(22+\chi(\mathrm{Fix})-2)$,
$$\rk S_{\mathrm{dP},b}=k+2=3\qquad(k=1),\qquad \rk S_{\mathrm{dP}}=2\qquad(k=0).$$
Only ranks enter; this is `@prop:del-pezzo-type-on-the-resolution` part 3 with
`@prop:tuple-of-the-construction` part 5, not redone here.

**I2 (the flat lattice).** $\Lambda_b=\langle e_b,f_b,[D_b]\rangle\subseteq S_{\mathrm{dP},b}$, with
$e_b=\pi^*h_1$, $f_b=\pi^*h_2$ ($h_i$ the ruling classes) and $[D_b]=\pi^*e$ for $e\subset\widehat Y$
the exceptional curve (`@rmk:a21-open`, third paragraph). By the projection formula
$(e_b)^2=(f_b)^2=0$, $e_b\cdot f_b=2(h_1\cdot h_2)=2$, $[D_b]^2=2e^2=-2$, $[D_b]\perp e_b,f_b$. So
$\Lambda_b\cong U(2)\perp\langle-2\rangle$ and $\det\Lambda_b=8$.

**I3 (even and primitive).** $S_{\mathrm{dP},b}$ is even (a sublattice of the even lattice $L$) and
primitive in $L$ ($2y\in S\Rightarrow y=\tfrac12(2y+\iota_{\mathrm{dP}}(2y))\in S$).

**I4 (index bound).** $\Lambda_b\subseteq S_{\mathrm{dP},b}$ with equal rank $3$, so
$i:=[S_{\mathrm{dP},b}:\Lambda_b]<\infty$ and $\det S_{\mathrm{dP},b}=\pm8/i^2$; since
$\det S_{\mathrm{dP},b}\in\mathbb Z$, $i^2\mid8$ and $i\in\{1,2\}$. These are exactly the corpus's two
candidates $\det\in\{8,2\}$.

## §2 Lemma 1 (the half classes of Λ are the two ruling classes)

**Lemma 1.** Let $S$ be a lattice with $\Lambda_b\subseteq S\subseteq\Lambda_b\otimes\mathbb Q$,
$\rk S=3$, $[S:\Lambda_b]=2$, and $S$ integral and even. Then $e_b/2\in S$ or $f_b/2\in S$; in
particular $e_b\in2L$ or $f_b\in2L$.

*Proof.* $[S:\Lambda]=2$ gives $2S\subseteq\Lambda$. Pick $z\in S\setminus\Lambda$ and write
$2z=ae_b+bf_b+c[D_b]$, $a,b,c\in\mathbb Z$. By I2,
$$z^2=\tfrac14\bigl(4ab-2c^2\bigr)=ab-\tfrac{c^2}2 .$$
$S$ integral gives $c$ even; $S$ even gives $z^2\in2\mathbb Z$, which with $c$ even forces $ab$ even.
Three cases. (i) $a$ odd, $b$ even: $2z\equiv e_b\pmod{2\Lambda}$, so $z-\tfrac12e_b\in\Lambda$ and
$e_b/2=z-(z-\tfrac12e_b)\in S$. (ii) $b$ odd, $a$ even: symmetrically $f_b/2\in S$. (iii) $a,b$ both
even: $2z\in2\Lambda$ forces $z\in\Lambda$ (as $S$ is torsion-free), contradicting $z\notin\Lambda$.
Any case with $c$ odd is excluded by $z^2\notin\mathbb Z$. $\square$

*Remark (provider agreement).* This is the same enumeration the maintained provider performs:
`computations/reports/sdp_discriminant_referee.py` with log `…-run.txt` (pin `c546077d`) prints
`integral-valued nonzero half-classes (a,b,c,q): [(0,1,0,0),(1,0,0,0)]`, and
`computations/reports/sm00_lattice_saturation.py` derives the same two classes with the index-$2$
overlattices equal to $U\perp\langle-2\rangle$, $\det2$. My `scripts/os_ot_lattices.sage` reproduces
the full $q$-table.

*Sharpness.* Lemma 1 is **false** for $k\ge2$: for $\Lambda_2=U(2)\perp\langle-2\rangle^{\perp2}$ the
half class $(e_b+f_b+[D_1]+[D_2])/2$ has square $1-1=0$ and is admissible (script §3). Hence the
theorem below is stated for $k\le1$; the one-node locus *is* $k=1$, so nothing is lost for A21.

## §3 Lemma 2 (the ruling classes are primitive in H²)

**Lemma 2.** $e_b$ and $f_b$ are primitive in $L=H^2(\widehat X_b,\mathbb Z)$.

*Proof for $e_b$* (the other is identical with the rulings exchanged). Suppose $e_b=2\eta$,
$\eta\in L$. As $e_b$ is of type $(1,1)$ so is $\eta$, hence $\eta\in\mathrm{NS}(\widehat X_b)$, and
$\eta^2=0$, $\eta\cdot e_b=0$, $\eta\cdot f_b=1$, $\eta\cdot H_b=1$, $\eta\cdot[D_b]=0$.

*Effectivity.* $f_b$ is nef ($\pi^*$ of the nef class $h_2$ under a finite map), so an effective
divisor has non-negative $f_b$-degree; as $(-\eta)\cdot f_b=-1<0$, $h^0(-\eta)=h^2(\eta)=0$. With
$K_{\widehat X}=0$ and $\chi(\mathcal O)=2$ one has $\chi(\mathcal O(\eta))=\eta^2/2+2=2$, so
$h^0(\eta)=2+h^1(\eta)\ge2$ and $|\eta|\ne\varnothing$.

*Verticality.* Let $E\in|\eta|$, $E=\sum_ia_iC_i$ with $a_i\ge1$ and $C_i$ distinct irreducible. Then
$E\cdot e_b=\eta\cdot e_b=0$ with $a_i(C_i\cdot e_b)\ge0$ (as $e_b$ is nef), so $C_i\cdot e_b=0$ for
all $i$. Since $|e_b|=\pi^*|\mathcal O_Y(1,0)|$ is base-point free (a base-point-free system pulled
back along a finite morphism), it defines a morphism $\varphi_1\colon\widehat X_b\to\mathbb P^1$ with
fibres of class $e_b$, and $C_i\cdot e_b=\deg(\varphi_1|_{C_i})=0$ means $\varphi_1(C_i)$ is a point:
every $C_i$ lies in a fibre $F_v=\varphi_1^{-1}(v)$.

*Fibre decomposition.* Write $E=\sum_vE_v$, $E_v$ the part supported in $F_v$. Distinct fibres are
disjoint, so $0=E^2=\sum_vE_v^2$. On the span $V_v=\bigoplus_i\mathbb Z[C_i(F_v)]$ of the components of
a fibre the intersection form is negative semidefinite: the components are orthogonal to the fibre
class $e_b$, which is nef of square $0$, so $V_v\subseteq e_b^\perp$ and the Hodge index theorem makes
$e_b^\perp/\mathbb Re_b$ negative definite. Hence $E_v^2\le0$ for every $v$, so all $E_v^2=0$, i.e.
$[E_v]$ lies in the radical of the form on $V_v$: $[E_v]=q_v[F_v]$ with $q_v\in\mathbb Q_{\ge0}$ (the
sign from $E_v\ge0$ and $[F_v]$ nef), and $q_v>0$ iff $E_v\ne0$.

*Multiplicities.* Evaluating on $f_b$, using $[F_v]=e_b$ and $e_b\cdot f_b=2$,
$$1=\eta\cdot f_b=E\cdot f_b=\sum_vq_v\,(e_b\cdot f_b)=2\sum_vq_v .$$
So exactly one $q_v$ equals $\tfrac12$ and all others are $0$: $E\subset F:=F_v$ and
$[E]=\tfrac12[F]$ **inside** $V:=\bigoplus_i\mathbb Z[C_i(F)]$, where $F=\sum_im_iC_i$ is the fibre
written with multiplicities.

*$[F]$ is primitive in $V$.* (i) $V\to H^2$ is injective: if $\sum n_i[C_i]=0$ in $H^2$, then pairing with
each component gives $\sum_i n_i(C_i\cdot C_j)=0$ for all $j$; the Gram matrix of a fibre's
components has rank $r-1$ with kernel spanned by $(m_i)$ (Kodaira's list, i.e. the affine Cartan
matrices), so $(n_i)=\lambda(m_i)$, and $0=\lambda[F]$ forces $\lambda=0$. (ii) $\gcd(m_i)=1$: if $g=\gcd(m_i)>1$ then $F=g\cdot D$ with $D=\sum(m_i/g)C_i$
effective of square $D^2=F^2/g^2=0$, so $D$ is again a fibre of $\varphi_1$ and $F$ is a *multiple*
fibre; but every fibre of $\varphi_1$ is reduced, being $\pi^{-1}(L)$ for a ruling line $L$, i.e. the
spectrum over $L$ of $\mathcal O_L\oplus(\mathcal O(-2,-2)\otimes\mathcal O_L)$ with $z^2=f|_L$, a
separable quadratic algebra over $k(L)$ in characteristic $0$. Hence $[F]=\sum m_i[C_i]$ has coprime
coordinates in the $\mathbb Z$-basis $\{[C_i]\}$ of $V$: it is primitive in $V$.

*Contradiction.* $[E]\in V$ and $2[E]=[F]$ exhibit $[F]\in2V$, against primitivity. So $e_b$ is
primitive. $\square$

*Remark (a route that fails, recorded so that nobody repeats it).* One is tempted to prove Lemma 2 from
"every irreducible curve has even $H_b\cdot C$". That is **false** for special members: if a ruling
line $L$ meets $\widetilde B$ in $2E$ for a divisor $E$ (the double cover $\pi^{-1}(L)\to L$ splits),
then the two sheets $C,C'$ of $\pi^{-1}(L)$ have $C\cdot H_b=\mathcal O(1,1)\cdot L=1$. The fibre
argument above avoids this because it uses primitivity of the fibre class *in its own component
lattice*, which holds for every member.

## §4 Theorem A (the saturation) and corollaries

**Theorem A.** For every one-node member, $S_{\mathrm{dP},b}=\Lambda_b$, $\det S_{\mathrm{dP},b}=8$,
$[S_{\mathrm{dP},b}:\Lambda_b]=1$. For every $k=0$ member (smooth branch curve, no resolution needed),
$S_{\mathrm{dP}}=\pi^*H^2(Y,\mathbb Z)=U(2)$.

*Proof.* By I4 the index is $1$ or $2$. If it is $2$, Lemma 1 gives $e_b/2\in S\subseteq L$ or
$f_b/2\in S\subseteq L$, contradicting Lemma 2. So $i=1$. The $k=0$ case is the same with
$\Lambda_0=U(2)$: the half classes of $U(2)$ are again only $e_b/2,f_b/2$ (script §2), so index $2$
would again make a ruling class $2$-divisible in $L$; and $\rk S_{\mathrm{dP}}=2$ there by I1. $\square$

*Remark (independent confirmation inside the swarm).* Direction d3 of this swarm reached the same
value $\det S_{\mathrm{dP}}=8$ by a different route: from $f_b/2\in S_{\mathrm{dP}}$ one gets an
integral $(1,1)$ class $x=f_b/2$ with $x^2=0$, $x\cdot f_b=0$, $x\cdot e_b=1$, and then
$h^0(x)>0$ leads to a contradiction by evaluating on $e_b$, while $h^0(x)=0$ contradicts
$\chi(\mathcal O(x))=2$. That argument needs the same fibre-primitivity step (their "$E_v=q_v[F_v]$,
$q_v\in\mathbb Z$", which is (ii) of my Lemma 2's third paragraph); with it, their route and mine are
both complete and agree.

**Corollary A1 (type).** $S_{\mathrm{dP},b}\cong U(2)\perp\langle-2\rangle$ is even $2$-elementary
with invariants $(r,a,\delta)=(3,3,1)$: rank $3$, $\det 8=2^3$, signature $(1,2)$,
$A_S\cong(\mathbb Z/2)^3$ generated by $e_b/2,f_b/2,[D_b]/2$, where $q(e_b/2)=q(f_b/2)=0$,
$b(e_b/2,f_b/2)=1$ and $q([D_b]/2)=-\tfrac12$, so $\delta=1$. Consequently $T_{\mathrm{dP},b}=S^\perp_L$
has rank $19$, signature $(2,17)$, $\det\mp8$, $A_T\cong(\mathbb Z/2)^3$ with $q_T\cong-q_S$, and
$[L:S_{\mathrm{dP}}\oplus T_{\mathrm{dP}}]=2^3=8$.

**Corollary A2 (what O-S was for).** The invariant lattice of the construction's del Pezzo involution is
*exactly* $U(2)\perp\langle-2\rangle$ — not $U(2)$ (the $k=0$/AEGS-marking slot) and not
$U\perp\langle-2\rangle$ (the determinant-$2$ alternative). By `@rmk:a21-open`'s parity paragraph the
determinant alone cannot decide this; Lemma 2 is what decides it. Consequence for the twist
identification: `ot-twist-identification.md` §5, where the del Pezzo half of O-T is proved
unconditionally.

## §5 What Theorem A does **not** settle

1. **$k\ge2$:** Lemma 1 fails there (the extra half class), so the argument does not run; the question
   becomes a finite half-class enumeration plus the same primitivity lemma.
2. **$S_{\mathrm{Co},b}$:** untouched here; see `ot-twist-identification.md` §6 for the reformulation
   and the six possible determinants.
3. **Chambers:** nothing is asserted or used about effective or nef cones.
4. **No integral eigensplitting:** $L=S\oplus T$ is never written; $\Lambda\subseteq S$ is a
   containment of sublattices and $S\subseteq L$ is primitive by I3, which is all that is used.

## §6 Checks (what was run, and what it shows)

`scripts/os_ot_lattices.sage`, exact arithmetic, transcript in `scripts/run.log`:

| check | output |
|---|---|
| $\Lambda=U(2)\perp\langle-2\rangle$ | $\det 8$, Smith $[2,2,2]$, $\lvert A\rvert=8$ |
| half classes, $k=1$ | only $e_b/2,f_b/2$ admissible ($q=0$); $[D_b]/2$ has $q=-\tfrac12$; mixed classes $q=\pm\tfrac12,\pm1$ |
| index-$2$ overlattice | basis $e_b/2,f_b,[D_b]$, Gram $\mathrm{diag}(0,1,0)/(1,0,0)/(-2)$, $\det2$, $=U\perp\langle-2\rangle$ |
| $k=0$ | only $e_b/2,f_b/2$ admissible; overlattice $=U$, $\det-1$ |
| $k=2$ | a third admissible class $(1,1,1,1)$, $q=0$ |
| $S(J_{\mathrm{dP}})$ of the twist | $\det 8$, $(r,a,\delta)=(3,3,1)$ |
| $S$-twist, $T$-twist | $\det\pm2048=2^{11}$, ranks $11,11$ |

These are checks of the arithmetic above, not certificates; the same arithmetic is also done by hand in
the text. The provider-level version is the repository's `sdp_discriminant_referee-run.txt`
(pin `c546077d`), whose $k=1$ output my script reproduces.

## §7 Files

* `os-lambda-saturation.md` — this document.
* `ot-twist-identification.md` — companion, O-T.
* `scripts/os_ot_lattices.sage`, `scripts/run.log` — reproducible exact-arithmetic checks.

## §8 Status of every claim, named

* **Proved here:** Theorem A (index $1$, $\det8$, for $k=1$ and $k=0$), Lemma 1, Lemma 2, Corollaries
  A1–A2, plus the failure remark for $k\ge2$.
* **Cited from the corpus with its own proofs:** the Lefschetz rank (I1) and the containment/pairing
  data (I2) — `@prop:del-pezzo-type-on-the-resolution`, `@prop:tuple-of-the-construction`,
  `@rmk:a21-open` in `writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md`.
* **Cited from the provider:** the half-class enumeration — `computations/reports/sdp_discriminant_referee.py`
  and `computations/reports/sm00_lattice_saturation.py` with their logs.
* **Open:** $k\ge2$ saturation; the type of $S_{\mathrm{Co},b}$; the chamber clause of A21 (not touched).
