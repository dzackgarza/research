# O-S: the saturation of the flat lattice. Answer: $S_{\mathrm{dP}} = \Lambda$, $\det = 8$, index $1$

Swarm `smw0dbvr6`, member m4, direction d6 (certification layer).
Corpus read-only at `main@141058a8` of
`/workspace/nucleus/work/projects/p-9fcb4ed7f4b64e008de2ee29a7197bf4/repo`.
Certificate script and log: `results/certify_lattices.py`, `results/certify.log`.

## 0. What is being decided

`writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md`,
`prop:del-pezzo-type-on-the-resolution` (4) and `prop:tuple-of-the-construction` (5)
give, on the resolved K3 $\widehat X_b$ of a one-node member ($k=1$):

* $S_{\mathrm{dP}} = H^2(\widehat X_b,\mathbb Z)^{\iota_{\mathrm{dP}}=+1}$ has rank $k+2 = 3$;
* $S_{\mathrm{dP}} \supseteq \Lambda := \pi^*\mathrm{Pic}(Y) \perp \mathbb Z D_b
  = \langle e_b, f_b, E\rangle$ with Gram $U(2)\perp\langle-2\rangle$, $\det\Lambda = -8$;
* the note there is explicit that "equality of lattices is a saturation question, not a
  rank count, and is not settled here".

So $[S_{\mathrm{dP}}:\Lambda] \in \{1,2\}$. **Result of this document: the index is $1$.**
Equivalently: $\Lambda$ is already saturated in $H^2(\widehat X_b,\mathbb Z)$; there is no
$\iota_{\mathrm{dP}}$-invariant class of odd pairing with $e_b$ or $f_b$, and no
$\iota_{\mathrm{dP}}$-invariant section of the fibration $|e_b|$.

The route is different from the gluing/fibre-census route (d1) and from the
nefness/$h^0$ route (d3): it is a **saturation lemma in an even unimodular ambient
lattice**, needing no effectivity, no Hodge theory and no member-specific data beyond
primitivity of $e_b, f_b$. It agrees with d3's independent conclusion.

## 1. The geometric inputs (the corpus's, cited; nothing else is assumed)

Let $X = \widehat X_b$ be the resolved one-node member: a smooth K3, so
$L := H^2(X,\mathbb Z)$ is an **even unimodular** lattice of signature $(3,19)$.
Let $Y = \mathbb P^1\times\mathbb P^1$ with ruling classes $h_1, h_2$
($h_1^2 = h_2^2 = 0$, $h_1\cdot h_2 = 1$), $\pi\colon X \to Y$ the double cover
branched along the branch curve (nodal at the $\tau$-fixed point $p$; $\pi$ is the
composition of the resolution with the cover of `prop:one-node-family`). Put

$$e_b := \pi^*h_1,\qquad f_b := \pi^*h_2,\qquad E := [D_b],$$

$D_b$ the exceptional $(-2)$-curve over the node.

**(G1)** $e_b^2 = f_b^2 = 0$, $e_b\cdot f_b = 2$: projection formula
$(\pi^*F)\cdot(\pi^*G) = \deg\pi\,(F\cdot G) = 2(F\cdot G)$
(`prop:del-pezzo-type-on-the-resolution`, proof of (4)).

**(G2)** $E^2 = -2$, and $E \perp e_b, f_b$: $D_b$ is the exceptional curve of the
resolution and $\pi_*D_b = 0$, so $E\cdot\pi^*(\text{anything}) = 0$
(`prop:tuple-of-the-construction` (2)).

**(G3)** $e_b$ and $f_b$ are primitive in $L$: $\pi^*$ is injective
($\pi_*\pi^* = 2\,\mathrm{id}$) and $h_1, h_2$ are primitive in
$H^2(Y,\mathbb Z)$.

**(G4)** $L$ is even and unimodular: $X$ is a K3 surface.

For (G2) note also $H\cdot E = 0$ with $H = \pi^*\mathcal O(1,1) = e_b+f_b$ ample
(pullback of a very ample class under a finite morphism), which is the corpus's
`prop:tuple-of-the-construction` (1) and (3).

## 2. Lemma 1 (primitivity of the two ruling classes)

> **Lemma 1.** In the situation of §1, $e_b \notin 2L$ and $f_b \notin 2L$.

*Proof.* Suppose $e_b = 2y$ with $y \in L$. Then
$$y^2 = \tfrac14 e_b^2 = 0,\qquad y\cdot f_b = \tfrac12 e_b\cdot f_b = 1,\qquad
y\cdot e_b = \tfrac12 e_b^2 = 0,$$
so $y\ne 0$ and $y$ is primitive. Let $H := e_b + f_b$: $H$ is ample with
$H^2 = 4$ and $H\cdot y = \tfrac12 H\cdot e_b = 1$.

Riemann–Roch on a K3 gives $\chi(y) = 2 + \tfrac12 y^2 = 2$, i.e.
$h^0(y) - h^1(y) + h^0(-y) = 2$. Since $H$ is ample and $H\cdot(-y) = -1 < 0$, $-y$ is
not effective, so $h^0(-y) = 0$ and $h^0(y) \ge 2$: the linear system $|y|$ is nonempty.

Let $Y_0 = \sum_i a_i C_i \in |y|$ (irreducible components, $a_i \ge 1$). As $H$ is
ample, $H\cdot C_i \ge 1$ for every $i$, so
$1 = H\cdot Y_0 = \sum_i a_i (H\cdot C_i)$ forces $Y_0 = C$ to be a single irreducible
curve with multiplicity one. Then $y = [C]$, $C^2 = y^2 = 0$, and an irreducible curve
with non-negative self-intersection is nef (distinct irreducible curves on a surface
meet non-negatively, and $C^2 = 0$). Hence $|y|$ is a base-point-free pencil whose
general member is a smooth genus-$1$ curve, i.e. a genus-$1$ fibration
$\psi\colon X \to \mathbb P^1$ with fibre class $y$ (Stein factorization: the fibres are
connected).

Take a general fibre $C'$ of the $e_b$-fibration $\varphi\colon X\to\mathbb P^1$; it is a
smooth genus-$1$ curve (the double cover of a ruling line branched at the
$4 = B\cdot h_1$ intersection points), and $[C'] = e_b$. Then
$y\cdot C' = y\cdot e_b = 0$ and $|y|$ is base-point-free, so a general member of $|y|$
is disjoint from $C'$; hence $C'$ is contracted by $\psi$ and is contained in a fibre
$F'$ of $\psi$, with $[F'] = y$.

Now $H\cdot C' = H\cdot e_b = 2$, while $H\cdot F' = H\cdot y = 1$; but
$F' = \sum_j m_j C'_j$ with $m_j \ge 1$ and $H\cdot C'_j \ge 0$, so
$H\cdot F' \ge H\cdot C'$ whenever $C'$ is a component of $F'$. Thus $1 \ge 2$ — a
contradiction. Hence $e_b \notin 2L$; the same argument with $e_b$ and $f_b$
interchanged proves $f_b \notin 2L$. $\square$

*Scope.* Lemma 1 uses only that $H$ is ample, that $|e_b|$ is a genus-$1$ fibration with
connected fibres and smooth general fibre, and $e_b\cdot f_b = 2$; it is exactly the kind
of elimination that the problem statement asks for in route (ii), but it is used here
only for primitivity, not for sections.

## 3. Lemma 2 (saturation)

> **Lemma 2.** Let $L$ be an even unimodular lattice and $\Lambda = \langle e,f,E\rangle
> \subseteq L$ with $e, f$ primitive, $e^2 = f^2 = 0$, $e\cdot f = 2$, $E^2 = -2$ and
> $E \perp e, f$. Then every sublattice $S$ with $\Lambda \subseteq S \subseteq L$
> satisfies $S = \Lambda$. In particular $\Lambda \cap 2L = 2\Lambda$.

*Proof.* First, $e,f,E$ are $\mathbb F_2$-independent in $L/2L$. For each of the seven
non-zero residues $w = ae+bf+cE$, $a,b,c\in\{0,1\}$, we show $w \notin 2L$:
if $w = 2y$ then $y \in L$ and $4y^2 = w^2$; now
$$e^2 = 0,\quad f^2 = 0,\quad E^2 = -2,\quad (e+f)^2 = 4,\quad
(e+E)^2 = (f+E)^2 = -2,\quad (e+f+E)^2 = 2 .$$
For $w\in\{E, e+E, f+E\}$ this gives $y^2 = -\tfrac12$ and for $w = e+f+E$
$y^2 = \tfrac12$, all non-integral; for $w = e+f$ it gives $y^2 = 1$, which is odd
while $L$ is even. The two remaining cases $w = e$, $w = f$ are excluded by primitivity
(Lemma 1 / hypothesis). So $\overline e, \overline f, \overline E$ are independent in
$L/2L$.

Now let $v\in\Lambda$, $v = 2y$ with $y\in L$, and let $w\in\{e,f,E,e+f,\dots\}$ be the
residue of $v$ modulo $2\Lambda$. Then $w = v - 2\lambda = 2(y-\lambda)$ with
$\lambda\in\Lambda\subset L$, so $w\in 2L$; by independence $w = 0$, i.e. $v\in 2\Lambda$.
Hence $\Lambda\cap 2L = 2\Lambda$.

Finally let $\Lambda\subseteq S\subseteq L$. Since $L$ is integral, $S\cdot\Lambda
\subseteq \mathbb Z$, i.e. $S\subseteq\Lambda^\vee$; and
$\Lambda^\vee/\Lambda \cong (\mathbb Z/2)^3$ (certified: §5), so $S/\Lambda$ has
exponent $2$ and $2S\subseteq\Lambda$. For $x\in S$ then
$2x\in\Lambda\cap 2L = 2\Lambda$, say $2x = 2\lambda$ with $\lambda\in\Lambda$; as $L$ is
torsion-free, $x = \lambda\in\Lambda$. Hence $S = \Lambda$. $\square$

*Remark.* Lemma 2 needs no hypothesis on $S$ beyond $\Lambda\subseteq S\subseteq L$: in
particular no rank hypothesis, no evenness of $S$, and no involution. This is why the
question never depends on the member $b$.

## 4. Conclusion (O-S)

Apply Lemma 2 with $L = H^2(\widehat X_b,\mathbb Z)$ (G4), $\Lambda = \langle e_b, f_b,
E\rangle$ with (G1), (G2), $e_b, f_b$ primitive by (G3), and
$S = S_{\mathrm{dP}}$. Then

$$S_{\mathrm{dP}} = \Lambda = U(2)\perp\langle-2\rangle,\qquad
\det S_{\mathrm{dP}} = -8,\qquad [S_{\mathrm{dP}}:\Lambda] = 1 .$$

Consequences, in the language of the problem statement:

1. **$\det$ is decided**: $8$, not $2$; the index-$2$ candidate $U\perp\langle-2\rangle$
   ($\det -2$) does **not** occur.
2. There is **no** $\iota_{\mathrm{dP}}$-invariant class of odd pairing with $e_b$ or
   $f_b$: such a class would be an element of $S_{\mathrm{dP}}$ outside $\Lambda$.
   This is exactly the "genuinely deciding question" of the referee's verdict on d1
   (see §6), and the answer is *negative*.
3. The fibration $|e_b|$ has **no** $\iota_{\mathrm{dP}}$-invariant section (a section
   $s$ would have $s\cdot e_b = 1$), and no invariant odd-degree multisection gives an
   overlattice element.
4. The candidate set $\{8,2\}$ of the corpus's discriminant-side data
   ($\texttt{computations/reports/sdp\_discriminant\_referee.py}$, pin `c546077d`) is
   correct as a statement about $\Lambda^\vee$ (certified in §5: exactly two even
   index-$2$ overlattices, generated by $e/2$ and $f/2$, both $\cong U\perp\langle-2\rangle$),
   but it is not a dichotomy for $S_{\mathrm{dP}}$: an even overlattice of $\Lambda$
   generated by $e_b/2$ or $f_b/2$ cannot sit inside the even unimodular $L$
   (Lemma 2 / Lemma 1). The "index $2$" alternative is empty for every member.

## 5. Exact-arithmetic certificate

`results/certify_lattices.py` (Python 3, `fractions.Fraction` only; no floating point
enters a verdict). Log: `results/certify.log`. It verifies:

| claim | certified value |
|---|---|
| $\Lambda = U(2)\perp\langle-2\rangle$: rank, $\det$, signature, evenness | $3$, $8$, $(1,2)$, even |
| $\Lambda^\vee/\Lambda$: three explicit dual generators, all $7$ non-trivial $\mathbb F_2$-combinations non-integral | $\cong(\mathbb Z/2)^3$, $q$-values $\{0,\tfrac12,1,\tfrac32\}$, $\delta = 1$ |
| the $7$ index-$2$ superlattices of $\Lambda$ in $\Lambda^\vee$: evenness | even exactly for $e/2$ and $f/2$ |
| those two overlattices | both have basis with Gram exactly $U\perp\langle-2\rangle$, $\det 2$ |
| model check in $L_{K_3} = U^3\perp E_8(-1)^2$: $e = u_1+u_3$, $f = f_1+f_3$, $E$ a root of $E_8(-1)$ | $e^2 = f^2 = 0$, $e\cdot f = 2$, $E^2 = -2$; none of the $7$ combinations lies in $2L_{K_3}$ |

The squares used in Lemma 2 are exactly the ones tabulated in Part 2 of the log.
Lemma 1 is not a computation and is not claimed to be one.

## 6. What this does and does not settle

* **Settled**: $[S_{\mathrm{dP}}:\Lambda] = 1$ and $\det S_{\mathrm{dP}} = -8$ for every
  one-node member, hence the answer to (O-S). The four inputs are the corpus's named
  facts (G1)–(G4); Lemma 1 supplies the primitivity that (G3) states, and Lemma 2 is
  new and elementary.
* **Independent agreement, and one rejected route**: d3 (m2) reaches $\det = 8$ by a
  nefness/$h^0$ argument on a would-be class $f_b/2$; d2 (m6) reaches it by a fibre-wise
  primitivity lemma. Lemma 2 subsumes both and needs no effectivity at all. The
  elimination route of d1 (m5) was correctly rejected by the referee at one step: a
  ruling line whose branch divisor restricts to a perfect square splits the double cover
  into two sheets $C_\pm$ with $C_+\cdot H = 1$ (a *certified* anti-invariant class of
  odd pairing against a ruling class), so "no odd class exists" is false as stated.
  **Lemma 2 is immune to that phenomenon**, and this is the point of the route: it never
  asserts anything about effective or irreducible classes, only about divisibility in the
  even unimodular $L$. An anti-invariant odd class $C_+$ is harmless — its pairing with
  $e_b,f_b$ says nothing about $S_{\mathrm{dP}}$, whose elements must satisfy
  $2x\in\Lambda\subset 2L$. (For $f_b$ there is in fact a one-line primitivity proof
  from the corpus's own bitangent witness: if $f_b = 2y$ then $y\cdot C_+ = \tfrac12
  \notin\mathbb Z$; Lemma 1 supplies the same for $e_b$, where no such witness is
  recorded.)
* **Scope of $k$**: the statement here is $k = 1$ (one-node members), where
  $\operatorname{rk}S_{\mathrm{dP}} = 3$ and $\Lambda$ is the rank-$3$ lattice of §2.
  For $k\ge 2$ the flat lattice $U(2)\perp\langle-2\rangle^{\perp k}$ has rank $\ge 4$
  and Lemma 2 does not apply; d2 (m6) observes that the class
  $(e_b+f_b+D_1+D_2)/2$ has integral square $0$ at $k=2$, so there the saturation
  question is genuinely open. (O-S as posed is the $k=1$ question.)
* **Not claimed here**: the type of $T_{\mathrm{dP}} = S_{\mathrm{dP}}^\perp$
  (rank $19$, $2$-elementary, $A_T\cong(\mathbb Z/2)^3$ with $q_T = -q_\Lambda$; its
  refined isometry class is fixed by that data but is not needed), and anything about
  other members' Picard lattices.
* **Erratum (sign only)**: $\det S_{\mathrm{Co}}$-twist is $+2048$, not $-2048$: a
  Gram determinant has the sign $(-1)^{n_-}$, and the signature is $(1,10)$. The
  absolute value $2048$ is what the discriminant group uses. See the O-T document.

## 7. Errata / sharpening for the corpus text

`prop:del-pezzo-type-on-the-resolution` says the invariant type is
$U(2)\perp\langle-2\rangle^{\perp k}$ "up to a finite index". For $k=1$ the finite index
is now proved to be $1$ (this document). The corpus's caution that
"computed ranks of the sublattice do not constrain the type without more" is respected:
no rank count is used in §4 — Lemma 2 is a statement about divisibility in $L$, not
about ranks.
