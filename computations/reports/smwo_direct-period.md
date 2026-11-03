# A20 direct period theorem for the one-node Coble construction: image and monodromy

Evidence register for the original A20 obligations `@prob:B24` and `@prob:B25`
(`writing/coble/heegner-report/coble-heegner-research-report.md` :1981-1989), from UltraMath run
`smw0o7jbf` (accepted solutions: **m2/d6, m1/d3, m3/d2, m4/d5, m5/d1, m6/d7, m7/d4**; **m8/d8
rejected** with three recorded gaps; referee records `REFEREE-verdict-m{1,..,8}.md` in the swarm's
directory hold the audit trail; nothing in the repository was modified by the run).

**B24 (verbatim).** "The marked direct Coble moduli stack is an explicit arrangement complement
`D_Co^o`, with the ample/nef chamber and exceptional root correctly encoded."
**B25 (verbatim).** "The deck group of the marking cover and the geometric monodromy group equal the
labeled centralizer group `Gamma^dir_{Co,2}`."
The five groups are kept fixed throughout: `G1 = Gamma^geom` (orbifold monodromy image of the
connected direct stack), `G2 = Gamma^dir_{Co,2}` (image of `Z_{O(L_K3)}(I_Co, I_dP)_{H,alpha,c}` in
`O^+(T_Co)`, @def:direct-group), `G3 = Gamma^Hdg_{Co,2}` (Enriques-Heegner stabilizer image), `G4 =
Gamma^cong` (the congruence preimage, strictly bigger than the stable `O^+(T_Co)*`), and `G5 =
Gamma_L` (the auxiliary label-stabiliser image of report item 3). No quotient is replaced by
notation anywhere below.

## Pass log

- **First publication** (`9f98f8f6`): Theorems A-E with the residual (T-mixed); accepted solution
  m2/d6 only.
- **Pass 1** (`aa9efac86b`): six further solutions adjudicated; Theorem D strengthened to the image
  equality `im(p) = O/Gamma_L`; Theorem C's blanket rigidity basis replaced once; Theorem E demoted
  to its proved content; (T-mixed) rewritten with the half-class census.
- **Pass 2 (this pass, one coherent proof correction removing the named obligations).**
  (i) `chi(Fix)` conventions reconciled publicly: the formula is
  `chi(Fix iota) = 2 + tr(iota*|H^2) = 2 rk S_iota - 20` (so `-14` for `iota_dP`, `2` for
  `iota_Co`); the pass-1 text wrote `2 rk S_dP - 22 = -16`, which is the trace line
  `tr(iota*|H^2) = 2 rk - 22`, not `chi` — corrected everywhere in the file; cross-check 3 stands
  (same formula).
  (ii) The quotient lattice identification and its index (Q2), the alpha-descent and transversality
  (Q3), and the one-node reconstruction (Q4-Q6) are *proved* in Section QC, with the double-cover
  adjunction and the Lefschetz/Nikulin numerics named per step, instead of asserted.
  (iii) Section L publishes in full: the positivity lemma, the complete (F1)-(F5) census, Lemma 4
  (one contracted curve), Lemma 4b (the frame inequality, repaired from its circular written form
  with the dependency on nefness of `H` removed), and Lemma 5 (the pencils). Every hypothesis is
  named per lemma; every geometric step is present.
  (iv) The image equality is scoped to what is now publicly established: the pointwise exclusion of
  Theorem A, the corpus's item-3 open-image content, and `im(p) = O/Gamma_L` at the tier of its
  premise ledger — with the (T-mixed) census machine-corroborated by bounded exact enumeration
  with self-stability asserted across two box sizes (`BAD_S = 121`, `BAD_T = 496`, exploratory
  tier; an earlier hand-sketch claiming a counting-forced pairing is retracted there as a
  miscount) replacing any overclaim. No group equality is asserted anywhere.
- **Pass 3 (this pass, the m8 resubmission's verdict folded in).** Three sharpenings.
  (i) By m8's second submission's Theorem 2.1 (verified): for a mixed class `x = (s+t)/2`,
  its wall in `D(T_Co)` equals the wall of its `t`-part (`s` is automatically orthogonal to every
  point of the domain), and it is a *pure-`T_Co` Heegner divisor* (norm `t^2 in {-4, -6}`), so the
  image's excluded set is always a union of ordinary `T_Co`-Heegner divisors — a sharpening, not a
  closure (whether a `(-4)`-piece is charged is exactly the pairing question below).
  (ii) The `(F4)`-family is restructured without the earlier circular reliance on the irreducibility
  of `alpha`: the class-level equivalence is proved (an `(F4)`-class effective with `A`-positive
  sign exists at a realization iff `alpha` is reducible as a class, `alpha = x + D`, each of
  square `-2` with `x.D = 1`), and the tuple's exceptional bullet — `alpha` is by definition the
  class of a smooth irreducible effective `(-2)`-curve — then does the final work: `(F4)`-carrying
  realizations are alpha-reducible, hence outside the tuple's scope. The exceptional bullet is kept
  explicit in Theorem D's definition of `O`.
  (iii) The (T-mixed) pairing question is now asked for all three families with the pairing table
  machine-corroborated by bounded exact enumeration (self-stability asserted across two box sizes;
  exploratory tier): (F2) domain 1 class, partner space 496 at norm `-4`; (F3) domain 120
  classes, partner space 496; (F4) domain 1 class, partner space 528 at norm `-6`. Existence of an
  avoiding glue is *not* certified by the comparison `121 <= 528` alone — it is left open, to be
  exhibited through the maintained discriminant-form constructor when available.`


- **Pass 4 (this pass, the five acceptance gaps of pass 2/3 removed).**
  (i) The dependency cycle `Lemma 4 uses E` / `L.3 uses Lemma 4` is restructured: Theorem SPLIT
  (the IRR/TAC dichotomy) is proved *first and independently* — it uses only RR, adjunction,
  Lemma L.1 and Lemma L.2, and never the curve `E` or Lemma 4 — and Lemma 4 afterwards invokes it
  for the (F4) case only. Each conclusion has its own independent argument before it is used.
  (ii) The `delta` criterion of Q1 is stated at its defining form (`delta = 1` iff the
  discriminant form `q: A_L -> Q/2Z` has a non-integral value), with the correct witness
  (`alpha/2` carries `q = -1/2 notin Z`) and the misclaimed `(e+f)/2` witness (`q = 1 in Z`,
  integral) removed.
  (iii) The census evidence is graded honestly: the `E8`-class split `120/136` is standard
  `O^+(8,2)` arithmetic; the enumeration outputs are machine-corroborated at the exploratory tier
  with self-stability asserted across two box sizes; and the existence of a glue avoiding every
  pairing is *not* asserted from the cardinality comparison alone — it is left open, to be
  exhibited through the maintained discriminant-form constructor when available.
  (iv) Q2's intermediate "`d in {1, 2}`" from `2 S_dP subset image` is replaced by the true
  `d in {1, 2, 4, 8}`, with the determinant comparison doing the whole closing work alone.
  (v) Q4's irreducibility argument is reconciled: the node's structural local term (two transverse
  smooth branches, Q3) lands either as term `2` in `(B_1.B_2)_q` with the remaining
  `B_1.B_2 >= 2` spent at other points, or entirely inside one component with the whole
  `B_1.B_2 >= 4` spent at other points — either branch yielding a second singularity, not a
  confused single-step claim.


- **Pass 5 (this pass, the remaining five acceptance gaps of pass 4).**
  (i) Q4's local term is the correct local calculation: the node is a double point (multiplicity
  `2` as a point of the curve) with two smooth transverse branches; two smooth plane branches with
  distinct tangents meet with local intersection number `1` (`dim k[[u,v]]/(u,v)`), not `2`; the
  earlier text had used the point's multiplicity in place of the `(B_1.B_2)_q` term. The
  cross-component and internal splits then use `1` resp. `0` correctly, and the residual
  `B_1.B_2` budget is spent at other intersection points, each a second singularity.
  (ii) Lemma 4's (F4) bullet separates `R = 0` from `R != 0` before any inequality is drawn (the
  latter gives `A.R >= 1`, whence `1 >= mu + 1` is the contradiction; then `R = 0` gives
  `mu = 1`, `A.D_j = 1` and the residual's single-curve conclusion by the same integral
  counting), and the residual's `D^2 = -2`, `x.D = 1` follow by explicit pairing, not a leftover
  iteration clause.
  (iii) Theorem SPLIT's numerology now covers *all* component squares and multiplicities by
  `A`-counting (integrality of `A.C >= 1` forces `alpha` to have at most two components counting
  multiplicity, killing `alpha = m C` for `m = 2` and every three-component case), and the
  positive-square and isotropic sub-cases are eliminated by square-adjunction and the integral
  `H.C_k = -1/2` obstruction — no irreducible-curve bound is ever applied to a grouped reducible
  divisor (the residual's single-curve status comes from the integral `A`-count, not from an
  irreducibility assumption).
  (iv) The exact standing of `O` against the original A20 claim is stated (Theorem D (relations)):
  `O` with the exceptional bullet is the original tuple's own scope (the bullet is authored), the
  pass-2 A-ample-only locus `O~` possibly contains the TAC strata, `im(p) = O/Gamma_L` is the
  established original claim, and `im(p) = O~/Gamma_L` is established ONCE `(X2)`-alone
  (no (F4)-wall carries a correct-sign A-ample realization); the earlier merged form attaching the
  no-(F2),(F3)-pairing condition to the `O~`-equality is corrected, since that equality only sees
  TAC strata (any other behavior lands outside `O~` as well); and B24 VERBATIM
  (`im(p) = D_Co^o/Gamma_L`) iff the pinned glue carries no (F2),(F3),(F4) pairing at all.
  (v) None of these is labelled closed by publication alone: the tacnode strata are named open
  (as a separate construction question outside the one-node scope), and the remaining (T-mixed)
  pairing question, `(D1)/(D2)`, and chamber determination stand open as before.


- **Pass 6 (this pass, the run `smw0uqe8g`'s first accepted direction folded in).** (CH) decided
  (m4, accepted): `Gamma^dir_{Co,2} = Gamma_L` at the authored chamber's reading, with the
  accumulation hedge of the corpus's chamber-pinning lemma collapsed (uniform
  `dist >= 1/sqrt 2` of every non-alpha effective wall from `H_b`); Theorem E's residual is then
  exactly `(D1)` plus `(RI)` — themselves named, and the `T_Co`-surjectivity removed from `(D2)`s
  path. Readings (b)/(c) stand as faithful counter-readings; no group equality by notation; the
  cross-member transport fork stays open as it stood.

## Theorems, at their registered scopes

**Lemma 1.** `I_dP = -1` on `T_Co`. (Joint character ranks of `<I_Co, I_dP>` are `(3, 8, 0, 11)`
with `rk S_dP = 3`, so the `(-,+)`-eigenspace vanishes and `T_Co` is the `(-,-)`-eigenspace.) Also
the class positioning used everywhere: `A = 2H - alpha in S_Co = T_Co^perp`, so `A perp delta` for
every `delta in T_Co`.

**Theorem A (the arrangement is excluded pointwise, not just generically; three independent proofs
accepted).** No member of the direct one-node construction carries an algebraic class of
`square >= -2` in `NS(X_b) cap (T_Co tensor Q)`. Accepted mechanisms: (i) RR supplies one
sign-effective class; `A` is ample on every member (corpus Lemma 2.2 of
`sm00_positive-half-A21.md`) and `A perp T_Co`, contradiction (m6 Theorem 2 + Remark 2.4, covering
rational classes, strongest form); (ii) RR + `I_dP`-inversion (m2/m1 Theorem 5.0a: the geometric
`iota_dP` inverts the class by Lemma 1, so both signs would be effective); (iii) the fibre lemma
(m5 Lemma 1 / m8 Theorem A: an `H`-null effective class is a union of `H`-trivial curves, the only
one is the exceptional curve of the node resolution). **Consequence.** Every marked period of a
member lies in
`D_Co^o := D(T_Co) \ cup_{delta in T_Co, delta^2 = -2} delta^perp`, pointwise and for every subgroup
`Gamma <= O(T_Co)` (m6 Corollary 2.1: group-independent). Three scope notes:
- The **side-effect** claim is kept at its correct direction only: at a member, ampleness of `A` is
  proved directly (Nakai on the blown-up model); Theorem A is then the *trivial* direction of the
  ampleness-versus-arrangement interaction. The converse — "no `A`-null algebraic root implies `A`
  ample" — is conditional: it holds for pure classes (`S_Co` has no `A`-null root at all, m4's
  Lemma C1) and fails exactly through the mixed glue classes of (T-mixed); see Theorem D.
- The arrangement itself is computed exactly (m6 Lemma 1.2): `delta^perp cap D(T)` is nonempty iff
  `delta^2 < 0`.
- The excluded set is exactly the norm-`(-2)` arrangement at the `(-2)`-level: the corpus's special
  member `F'` carries `[C1 - C2] in T_Co` of square `-6` (verified against
  `sm57_verify_special_member.log`; m6's audit C3), so the image *meets* the `(-6)`-Heegner locus.

**Theorem B (the second slot is realized geometrically at the chamber hypothesis).** At every marked
Coble period `q` at which `2H-alpha` is a Kahler class — the chamber datum `c` and nothing else —
both `I_Co` and `I_dP` are Hodge isometries of the marked structure fixing `2H-alpha`, hence are
induced by commuting automorphisms of `X_q` (effectivity via the fixed-Kahler-class condition;
global Torelli as in Peters SS1.8, equivalent to BHPV VIII.11.1). Inputs with anchors verified
verbatim: realization of `S_Co`-polarized K3s by PSS surjectivity (`huybrechts_k3_lectures.md`
:9480); the automorphism part of global Torelli (:10227-:10240, Corollary 2.3); openness of
ampleness in families (:5167, Proposition 5.6).

## Section L: the published fundamental lemmas

Standing setting for Sections L and QC: `sigma in O`, where

`O := {sigma in D(T_Co) : exists a marked pair (X, psi) at sigma with psi(S_Co) subset NS(X) and
psi(A) ample and psi(alpha) irreducible-effective}`,

`(X, psi)` such a witnessing marked pair — note the last clause is the tuple's *exceptional
bullet*: the authored datum carries `alpha` as the class of a smooth irreducible effective
`(-2)`-curve, so a realization at which `alpha` is reducible-effective is simply out of the
tuple's scope (and is the tacnode-shaped stratum of Theorem SPLIT's (TAC) alternative, named there) —
`(I_Co, I_dP, H = e + f, alpha, A = 2H - alpha)` the
transported classes on `X` (`e, f` the `U(2)` ruling frame, `e^2 = f^2 = 0`, `e.f = 2`,
`alpha^2 = -2`, `H^2 = 4`, `H.alpha = 0`, `A^2 = 14`, `A.alpha = 2`). The gluing is the full-graph
glue of the index-`2^11` overlattice: every `x in L_K3` writes `2x = s + t` with `s in S_Co`,
`t in T_Co`. Riemann-Roch on a K3, adjunction (`C^2 = 2 p_a - 2 >= -2` for an irreducible curve),
and Hodge index are used at textbook tier and are named where used.

**Lemma L.1 (positivity).** Every nonzero `t in NS(X) cap (T_Co tensor Q)` has `t^2 < 0`. *Proof.*
`t perp sigma` with `sigma` a positive definite real `2`-plane in signature `(2,9)`, so `t` lies in
the negative definite orthogonal complement. `square`

**Lemma L.2 (the (F1)-(F5) census, complete).** Let `x in NS(X)` with `x^2 = -2`, `x.H = 0`, and
write `2x = s + t` with `s in S_Co`, `t in T_Co`. If `t != 0`, then, with
`s = a(e-f) + w + c alpha`, `w in E8(2)`, `w^2 = -4m`, `m >= 0`, exactly the following five families
occur:

| family | `s` | `s^2` | `t^2` | `A.x` | content |
|---|---|---|---|---|---|
| (F1) | `0` | `0` | `-8` | `0` | the glue forces `x = t/2 in T_Co`: a pure `T`-root |
| (F2) | `pm(e-f)` | `-4` | `-4` | `0` | mixed glue class |
| (F3) | `w`, `w^2 = -4` | `-4` | `-4` | `0` | mixed glue class |
| (F4) | `pm alpha` | `-2` | `-6` | `pm 1` | mixed glue class |
| (F5) | `w pm alpha` or `(e-f) pm alpha` | `-6` | `-2` | `pm 1` | `t` already a pure `T`-root |

*Proof.* `s^2 = -4a^2 - 4m - 2c^2` and `t^2 = -8 - s^2`. By Lemma L.1 `t^2 <= -2` (the standing
assumption is `t != 0`), and `t^2` is even. If `s^2 <= -10` then `t^2 >= 2`, impossible, and
`s^2 = -8` would force `t^2 = 0`, i.e. `t = 0`, against the same assumption; so
`s^2 in {0, -2, -4, -6}`, and the four even choices enumerate exactly the five families. (F1)
additionally: the glue containing `([0], [t/2])` forces `[t/2] = 0`, i.e. `x = t/2 in T_Co` — a
pure `T`-root, not a mixed one. `square`

**Theorem SPLIT (the class of alpha: the dichotomy; the independent argument).** At a marked
pair with `alpha` effective and `A` ample — and `alpha` IS effective at every such pair, since
`chi(O(alpha)) = 1` and `A.alpha = 2 > 0` kills the false sign — exactly one of two configurations
holds:
(IRR) `alpha` is a *single* smooth rational curve `E`, with `h^0(alpha) = 1`;
(TAC) `alpha = C_1 + C_2` with the `C_i` smooth rational, `C_i^2 = -2`, `C_1.C_2 = 1`, and each
`A.C_i = 1`; moreover each `[C_i]` is an (F4)-class of Lemma L.2's census.
*Hypotheses in force:* RR; adjunction (`C^2 = 2 p_a - 2 >= -2` for an irreducible curve); Lemma L.1
(negativity of the algebraic part of `T_Co`); Lemma L.2 (the census); integrality of intersection
pairings. **Nothing else — in particular no use of Lemma 4, of the curve `E`, or of any later
lemma.**
*Proof.* Every irreducible effective curve on a K3 has `C^2 >= -2` (adjunction), and ampleness of
`A` gives `A.C >= 1` (an integral, positive pairing with an effective curve) for every component.
Write `alpha = sum_i m_i C_i`, `m_i >= 1`, distinct irreducible components. Then
`2 = A.alpha = sum_i m_i (A.C_i)` with each term a positive integer, so `alpha` has at most two
components counting multiplicity.
- *One component with multiplicity.* `alpha = m C`: `alpha^2 = m^2 C^2 = -2`, with `m in {1, 2}`
  (`m >= 2` gives `4 C^2 = -2`, not an integer square): so `m = 1`: (IRR). Then
  `h^0(alpha) = 1` from `0 -> O -> O(alpha) -> O_E(alpha) -> 0` with `O_E(alpha) = O_{P^1}(-2)`.
- *Two distinct components.* `alpha = C_1 + C_2` (each of multiplicity `1`, by the `A`-counting
  just made), `A.C_1 = A.C_2 = 1`.
  Squares, enumerated (all cases, including the positive-square ones):
  (b1) `C_1^2 = C_2^2 = 0`: `alpha^2 = 2 C_1.C_2 = -2`, so `C_1.C_2 = -1`: impossible for distinct
  irreducible curves.
  (b2a) `C_1^2 >= 0` and `C_2^2 >= 0`: `alpha^2 = C_1^2 + C_2^2 + 2 C_1.C_2 >= 0` — against
  `alpha^2 = -2`.
  (b2b) `C_1^2 > 0`, `C_2^2 = -2`: `alpha^2 = C_1^2 - 2 + 2 (C_1.C_2) = -2` forces
  `C_1.C_2 = -C_1^2/2 <= -1` (the form is even, so `C_1^2` is a positive even integer and the
  right side is a negative integer): impossible for distinct irreducible curves — explicitly the
  positive-square-single-negative case, excluded.
  (b3) `C_1^2 = 0`, `C_2^2 = -2`: `alpha^2 = -2 + 2 (C_1.C_2) = -2` forces `C_1.C_2 = 0`, and then
  `alpha.C_2 = C_1.C_2 + C_2^2 = -2`, whence
  `A.C_2 = 2 H.C_2 - alpha.C_2 = 2 H.C_2 + 2 = 1`, so `H.C_2 = -1/2`: not an integer — impossible.
  (b4) `C_1^2 = C_2^2 = -2`: `alpha^2 = -4 + 2 (C_1.C_2) = -2` forces `C_1.C_2 = 1`: (TAC), and
  then `alpha.C_i = C_i^2 + C_1.C_2 = -1`, so `2 H.C_i = A.C_i + alpha.C_i = 0`: each `[C_i]` is
  an `H`-null `(-2)`-class. Lemma L.2's census places it: not pure (the pure census gives only
  `pm alpha`, and `[C_1] = [C_2] = alpha` would not decompose), not (F1) (a pure `T`-root), not
  (F2)/(F3) (their `A` is `0`, not `1`), and not (F5) (its `t` is a pure `T`-root, RR-effective
  with `A.t = 0`, contradicting ampleness): hence (F4).
  For three-or-more components the `A`-counting above already excludes them (`sum m_i A.C_i >= 3`
  if there are at least three positive-integer terms). `square`
*Reading.* The tuple's exceptional bullet is exactly (IRR): by the authored datum `alpha` is the
class of a smooth irreducible effective `(-2)`-curve. A realization at the (TAC) alternative (the
named tacnode alternative) is out of the authored tuple's scope. Nothing in this theorem uses any
conclusion about the `H`-null `(-2)`-classes, so it can and will be cited independently of the
next lemma.


**Lemma 4 (one contracted curve).** At `sigma in O` with the full tuple (`A` ample *and* `alpha`
irreducible-effective — the exceptional bullet, i.e. Theorem SPLIT's (IRR) branch as picked by the
authored datum): `{x in NS(X) : x^2 = -2, x.H = 0} = {pm alpha}`; writing `E` for the effective
representative of `alpha` (Theorem SPLIT's (IRR) branch), `E` alone is contracted by `varphi_H`.
*Hypotheses in force:* `A` ample (definition of `O`); RR; Lemma L.1; Lemma L.2; Theorem SPLIT (for
the (F4) case only).
*Proof.* Let `x` be such a class; RR gives one of `pm x` effective. If `x` is pure (`t = 0`), the
glue graph has only zero over zero, so `x = s/2 in S_Co`; write `x = ae + bf + w + c alpha`:
`x.H = 2(a + b) = 0` gives `b = -a`, and `x^2 = -4a^2 + w^2 - 2c^2 = -2` gives
`2a^2 + 2w-part + c^2 = 1` with the `E8(2)` part nonpositive, hence `a = 0`, `w = 0`, `c = pm 1`:
`x = pm alpha`. Otherwise Lemma L.2 puts `x` in one of the five families:
- (F1): `x` is a pure `T`-root; `pm x` effective with `A.x = 0` contradicts `A` ample.
- (F2): `A.x = 2(a+b) + c = 0` (`a+b = 0`, `c = 0`): `pm x` effective contradicts ampleness.
- (F3): identically `A.x = 0`: contradiction.
- (F4): `A.x = pm 1` and `alpha.x = mp 1`. RR supplies an effective sign. If the effective `x`
  has `A.x = -1`, ampleness fails outright, so `sigma notin O`. If the effective `x` has
  `A.x = 1`: write `alpha = sum_j D_j` into effective irreducible curves; since `alpha.x = -1`,
  some component `D_j` satisfies `D_j.x < 0`, hence `D_j subset supp(x)`, i.e.
  `x = mu D_j + R` with `mu >= 1` and `R` an *effective* divisor. Separate the two cases before
  bounding:
  *If `R != 0`:* then `A.R >= 1` (ampleness, integral positive pairing), and every component has
  `A >= 1`, so `1 = A.x = mu * A.D_j + A.R >= mu + 1`, forcing `mu <= 0`: impossible.
  *Hence `R = 0`:* then `x = mu D_j` and `1 = A.x = mu * A.D_j >= mu`, so `mu = 1`,
  `A.D_j = 1`, and `x = D_j` is a single component of `alpha`; the residual
  `D_rest := alpha - x` is effective with `A.D_rest = A.alpha - A.x = 1`, and by the same
  ampleness-counting it cannot decompose (two components would each carry `A >= 1`, totalling
  `>= 2`), so `D_rest` is a single effective curve `D`, with
  `x.D = alpha.x - x^2 = -1 + 2 = 1` and `D^2 = alpha^2 - x^2 - 2 x.D = -2`: the outcome is
  exactly the (TAC) alternative of Theorem SPLIT. On the (IRR) branch the exceptional bullet
  excludes that alternative, so no (F4)-class is algebraic at the counted `sigma`. (This is the
  only place Theorem SPLIT enters; it needs no fact about irreducibility of `alpha` that Theorem
  SPLIT does not itself produce.)
- (F5): its `t` is a pure `T`-root algebraic at `sigma` (since `x` and `s` are), of norm `-2`:
  `pm t` effective, `A.t = 0`, contradiction.
Hence `x = pm alpha`. `square`

**Lemma 4b (the frame inequality, repaired; dependencies explicated).** At `sigma in O`, for every
effective `delta in NS(X)` with `delta^2 = -2`: `e.delta >= 0` and `f.delta >= 0`.
*Hypotheses in force:* `A` ample (definition of `O`); RR; Lemma L.1 (negativity of the algebraic
part of `T_Co`); primitivity of `e` and `f` in `L_K3`. *No other lemma is used; in particular the
nefness of `H` is not an input anywhere.*
*Proof.* Write `2 delta = s + t`, `s = ae + bf + w + c alpha` with `w^2 = -4m`, `m >= 0`, so
`e.delta = b`, `f.delta = a`, `H.delta = a + b`, `A.delta = 2(a+b) + c >= 1` (delta effective, `A`
ample), and `t^2 = -8 - 4ab + 4m + 2c^2`. We show `b >= 0`; `a >= 0` symmetrically. Suppose
`b <= -1`.
*Case 1: `t != 0`.* Then `t^2 <= -2` (Lemma L.1), i.e. `4ab >= 4m + 2c^2 - 6`.
 - If `a + b <= -1`: with `x := -a`, `y := -b >= 1` (and `x <= -a` unsigned only in subcase 1b):
   1a (`a >= 0`): `ab <= 0`. From `a + b <= -1` (i.e. `a <= y - 1`) and `A.delta >= 1`,
   `c >= 1 + 2|a + b| = 1 + 2(y - a)`, so `4m + 2c^2 - 6 >= 2(1 + 2(y-a))^2 - 6 >= 2*9 - 6 = 12`,
   forcing `4ab >= 12`: but `ab <= 0`. Impossible.
   1b (`a <= 0`): `t^2 <= -2` gives `2c^2 <= 4xy - 4m + 6 <= 4xy + 6`; `A.delta >= 1` gives
   `c >= 1 + 2(x + y)`, so `2(1 + 2(x+y))^2 <= 4xy + 6`, i.e.
   `4(x+y)^2 + 4(x+y) <= 2xy + 2`. For `x, y >= 1` one has `(x+y)^2 >= 4xy`, so the left side is
   `>= 16xy + 8 > 2xy + 2`: impossible.
 - If `a + b = 0` (`a = -b >= 1`): `A.delta >= 1` gives `c >= 1`; `t^2 <= -2` gives
   `4a^2 + 4m + 2c^2 <= 6`, i.e. `a = 1`, `m = 0`, `c = pm 1`. These are the (F5)-classes, with
   `t^2 = -2`: `t` is a pure `T`-root algebraic at `sigma` (since `delta` and `s` are algebraic),
   one of `pm t` is effective, and `A.t = 0` contradicts ampleness — ruling out this sub-case at
   `sigma in O` itself.
 - If `a + b = n >= 1`: with `b = -y <= -1`, `a = n + y >= 1`, so `ab = -y(n+y)` and
   `t^2 = -8 + 4y(n+y) + 4m + 2c^2 >= -8 + 4(n+1) + 2c^2 >= 4n - 4 >= 0`; since also `t^2 <= -2`,
   impossible unless `y(n+y) = 2` and `m = c = 0` and `t^2 = 0`: but `t != 0` by hypothesis.
*Case 2: `t = 0`.* Then the glue forces `delta in S_Co` (the coset `[s/2]` pairs with `[0]`), so
write `delta = a'e + b'f + w' + c' alpha` (integrally): `delta^2 = 4 a' b' - 4 m' - 2 c'^2 = -2`,
i.e. `2 a' b' - 2 m' - c'^2 = -1`, so `c'` is odd and `a' b' - m' = (c'^2 - 1)/2 >= 0`, hence
`a' b' >= 0`. Also `A.delta = 4(a' + b') + 2 c' >= 1`, LHS even, so `>= 2`.
 - If `b' <= -1`: write `k := a' + b'`. `A.delta >= 2` gives `2k + c' >= 1`, with `c'` odd.
   If `k <= -1`, then `c' >= 1 + 2|k|`, so
   `a'b' = (c'^2 - 1)/2 + m' >= (c'^2 - 1)/2 >= 2|k|^2 + 2|k|`; but by AM-GM
   `a'b' <= (k/2)^2 = |k|^2/4` — and `|k|^2/4 >= 2|k|^2 + 2|k|` is impossible (`|k| >= 1`):
   contradiction. Hence `k >= 0`; but then `a'b' >= 0` with `b' <= -1` forces `a' <= 0`, whence
   `k = a' + b' <= -1`, contradicting `k >= 0`. So `b' >= 0`, and symmetrically `a' >= 0`.
So `b >= 0` (and `b' >= 0` in the pure case); by symmetry `a >= 0`. `square`
*Remark.* The m7 write-up cited "H is nef" at precisely the point where the case analysis
branches; `H = e + f` is nef only after Lemma 5, which is proved from the present lemma: that
citation was circular. The present derivation uses only ampleness of `A`, RR, Lemma L.1 and
primitivity. It is the referee record's repair, published in full.

**Lemma 5 (the ruling pencils).** At `sigma in O`, `e` and `f` are nef; being primitive and
isotropic, they are base-point-free elliptic pencils by Saint-Donat (`huybrechts_k3_lectures.md`
:1027, Prop. 3.10). *Proof.* Lemma 4b gives `e.delta >= 0` and `f.delta >= 0` for every effective
root `delta` of `X`. For rational `eps > 0` put `e_eps := e + eps A`; then
`e_eps^2 = 8 eps + 14 eps^2 > 0`, `e_eps . A > 0`, and `e_eps . delta >= eps A.delta > 0` for every
effective root, so `e_eps` is ample by Nakai-Moishezon for K3 (:737: ampleness checked on smooth
rational curves). Hence `e = lim_{eps -> 0+} e_eps` lies in the closure of the ample cone: `e` is
nef. Same for `f`. `square`

## Section QC: the quotient's reconstruction, with every quotient-side input proved

**Q0 (setting and one arithmetic reconciliation).** `(X, psi)` at `sigma in O` as in Section L;
Theorem B makes the two involutions automorphisms `iota_Co, iota_dP`. *Conventions, reconciled*:
with `S_iota := H^2(X,Z)^iota`, `tr(iota*|H^2) = 2 rk S_iota - 22`, and the Lefschetz formula
`chi(Fix iota) = 2 + tr = 2 rk S_iota - 20`. So `chi(Fix iota_Co) = 2*11 - 20 = 2` and
`chi(Fix iota_dP) = 2*3 - 20 = -14`. (Pass 1 wrote `2 rk - 22 = -16` in the second line — the
trace value, not `chi`; the branch genus in Q1 uses the correct `-14`, as does cross-check 3.)

**Q1 (the quotient is smooth rational with computed numerics).** `Fix(iota_dP)` is smooth (fixed
locus of an involution of a smooth surface is smooth) and, by Nikulin's classification for the
2-elementary non-symplectic involution with `(r, a, delta) = (3, 3, 1)`. The `delta` is certified
by its defining criterion and not by the rejected witness: for an even `2`-elementary lattice the
discriminant form is `q: A_L -> Q/2Z`, and `delta = 0` iff `q` is integral-valued (every value in
`Z subset Q/2Z`); `delta = 1` iff some class has a non-integral value. Here `A_{S_dP}` contains
`alpha/2` (the generator of the `<-2>` summand) with `q(alpha/2) = -1/2 mod 2Z`, not integral, so
`delta = 1`. (The vector `(e+f)/2`, offered in the previous text, has
`q((e+f)/2) = 1 in Z subset Q/2Z`, hence is integral-valued and cannot be a witness; that citation
was wrong.) With it, `Fix(iota_dP)` is a single curve `C_8` of genus
`g = (22 - r - a)/2 = 8` with no other fixed components and no isolated points; consistently
`chi(C_8) = 2 - 2*8 = -14` (Q0). `Y° := X/iota_dP` is smooth (the fixed locus is a smooth divisor;
local model `(t, u) mapsto (t^2, u)`), `rho: X -> Y°` is finite of degree `2` branched along the
smooth curve `B° := rho(C_8)`, and `rho|_{C_8} : C_8 -> B°` is an isomorphism (a finite map of
degree `1` between smooth curves). The canonical bundle formula `0 = K_X = rho^*(K_{Y°} + B°/2)`
gives `B° ~ -2K_{Y°}`. `q(Y°) = 0` since `H^1(Y°,O) subset H^1(X,O)^{iota_dP} = 0`; `p_g(Y°) =
h^0(K_{Y°}) = h^0(-B°/2) = 0` since `B°` is nonzero effective (and then `p_2 = h^0(2K) = 0` by
`2K = -B°`); so `Y°` is rational by Castelnuovo (`q = p_2 = 0`). Transfer (`pi^* pi_* = 1 +
iota^*`) gives `b_2(Y°) = rk H^2(X)^{iota_dP} = 3` over `Q`, hence integrally as well by the
free-ness of `H^2(Y°,Z)` (simple connectivity). Euler comparison for the double cover:
`e(X) = 2 e(Y°) - e(B°)`, so `e(Y°) = (24 - 14)/2 = 5`, and Noether `K^2 + e = 12` gives
`K_{Y°}^2 = 7`; `B°^2 = 4K^2 = 28`; `p_a(B°) = 1 + (B°^2 + K.B°)/2 = 1 + (28 - 14)/2 = 8`.

**Q2 (the quotient lattice identification, proved, with index one).**
`pi^* : H^2(Y°,Z) -> S_dP := H^2(X,Z)^{iota_dP}` is an isomorphism of abelian groups (index
one), and the restricted form on `S_dP` is double the form on `H^2(Y°,Z)`: hence
`S_dP = pi^* Pic(Y°)` as lattices. *Proof.* `Y°` is simply connected
(rational surfaces are), so `H^2(Y°,Z)` is free abelian, unimodular (`det = pm 1`), rank `3`. The
pullback form computes `(pi^*a, pi^*b) = 2 (a,b)`, hence as a sublattice of `S_dP` the image
`pi^*H^2(Y°)` has determinant `pm 8 = 2^3 * pm 1`. Transfer (`pi^* pi_* = 1 + iota^*`) sends any invariant `x` to
`2x = pi^* pi_* x in pi^* H^2`, hence `2 S_dP subset pi^* H^2 subset S_dP`, i.e. the quotient
`S_dP / pi^* H^2` is an elementary abelian `2`-group of order `d in {1, 2, 4, 8}` (it is a
quotient of `S_dP/2 S_dP = (Z/2)^3`; the text's earlier intermediate "`d in {1, 2}`" was not
justified by the transfer alone and is removed). The separate determinant comparison then closes
it and is the load-bearing step: `det S_dP = det(U(2) perp <-2>) = 8` (the corpus's
invariant-lattice input, transported by the marking), for a finite-index sublattice
`det(pi^*H^2) = d^2 * det S_dP = 8 d^2` up to sign, while `det(pi^*H^2) = 2^3 det H^2(Y°,Z)
= 2^3 * pm 1 = pm 8` was computed above: so `d^2 = 1`, whence `d = 1`. Finally
`Pic(Y°) = H^2(Y°,Z)` (since `q = p_g = 0`, `NS = H^2`): as a lattice it is free unimodular of
signature `(1,2)`, **odd** by `K^2 = 7` (Wu class), hence `Pic(Y°) is congruent to U perp <-1>`
(the unique odd unimodular lattice of signature `(1,2)`; `U perp <-1>` and `<1> perp <-1>^2` are
isometric), with the form on `S_dP = pi^*Pic` the doubled one as claimed. `square`

**Q3 (alpha descends to an irreducible (-1)-curve; intersections transverse — proved).** Let
`alpha = [E]` with `E` the curve of Theorem SPLIT's (IRR) branch. Then: `iota_dP(E) = E` setwise (since
`iota_dP(alpha) = alpha` as classes and `h^0(alpha) = 1` gives `|alpha| = {E}`); `E` is not a
component of `Fix(iota_dP)` (which is the single genus-`8` curve `C_8` of Q1, while `E` is
rational); hence `iota_dP|E: E -> E` is a *nontrivial* involution of `P^1`, with exactly two fixed
points, necessarily lying on `C_8`. Consequently `e' := pi(E)` satisfies: `pi|E: E -> e'` is the
`Z/2`-quotient `P^1 -> P^1` branched at exactly those two points; `e'` is a smooth rational curve;
`pi^* e' = E` as divisors (`E` is `iota`-stable, disjoint from the ramification divisor's generic
points, the cover of `e'` is the curve `E` generically of degree `2`, reduced); hence
`2 e'^2 = (pi^* e')^2 = E^2 = -2`, i.e. `e'^2 = -1`: **`e'` is an irreducible smooth `-1`-curve on
`Y°`.** *Transversality*: at each point of `e' cap B°` choose local coordinates `(u, v)` centered
there with `iota_dP(u, v) = (u, -v)` and `Fix = {v = 0}` (the fixed locus is a smooth curve, so the
`(+1)`-eigendirection spans its tangent and the `(-1)`-eigendirection is a transverse one); `E`
passes through the point and is `iota`-stable without being the fixed curve, so its tangent is the
`(-1)`-eigendirection: `E = {u = 0}` locally. The quotient `Y°` has local coordinates `(u, w :=
v^2)`; `e'` maps to `{u = 0}` and `B°` (the image of `Fix`) maps to `{w = 0}`: smooth curves
meeting transversally at `(0,0)` with local intersection number `1`. Hence **`e'.B° = 2` as two
distinct simple points.**

**Q4 (the contraction produces the one-node `(4,4)`-curve — computed; no rigidity used).** Let
`beta: Y° -> Y` contract `e'` (Castelnuovo's criterion: a smooth `-1`-curve).
*Y's shape via its Picard lattice*, not via blanket rigidity. `Y` is smooth rational with
`b_2 = 2`, `K_Y^2 = 8`, and `Pic(Y) congruent U` even (Q2: only the `<-1>` summand of
`U perp <-1>` is removed; explicitly, Q2's form reads: the pullback `H = pi^*h` with `h in Pic(Y°)`
orthogonal to `e'` descends to `h' in Pic(Y)` with `h'^2 = h^2 = H^2 / 2 = 2`, and `h'` is nef and
big because `H` is nef and big — `H` nef by Lemma 5: `H = e + f`). The alternatives are closed
arithmetically:
- *`Y` non-minimal.* Then `Y` blows down further to `K^2 = 9 = P^2` and `Pic(Y) = <l, eps>` odd —
  excluded already by parity (`Pic(Y) congruent U` is even); and independently, a nef
  `h' = al + m eps` of square `2` would solve `a^2 - m^2 = 2` with integers, impossible (`0, pm 1
  mod 4`).
- *`Y` minimal, `Y congruent F_e`, `e` even (`Pic congruent U`).* `h' = a C_0 + b f` with
  `C_0^2 = -e`, `f^2 = 0`, `C_0.f = 1`: `h'^2 = -e a^2 + 2ab = 2` with nefness
  `h'.C_0 = -ea + b >= 0`, `h'.f = a >= 0` gives `e in {0, 2}` (at `e >= 4` no nef solution; at
  odd `e` the Picard lattice is odd).
- *`F_2` is excluded by ampleness of `A` itself.* If `Y congruent F_2`, then `h' = C_0 + 2f` meets
  `C_0` in `0`. Let `C_0^~ subset Y°` be the proper transform of `C_0` (a curve) and set
  `delta := pi^* C_0^~`, an effective class of `X`. Then `H.delta = 2 h'.C_0 = 0`, and
  `alpha.delta = (pi^* e').(pi^* C_0^~) = 2 (e'.C_0^~) >= 0`, so
  `A.delta = 2 H.delta - alpha.delta = -2 (e'.C_0^~) <= 0`,
  contradicting `A` ample at `sigma` (if `C_0^~ = e'` then `C_0 = beta_*(e')` is contractible,
  excluded: `C_0^2 = -2` on `F_2` is not a `(-1)`-curve). So `e = 0`.
Hence `Y congruent P^1 x P^1` and `h' = O(1,1)` up to `Aut(Y)`; `Y° congruent Bl_q(Y) for some q`,
which is, by the del Pezzo classification, the *unique* isomorphism type of a del Pezzo surface of
degree `7` (Demazure, *Surfaces de Del Pezzo II - Eclater n points dans P^2*, Seminaire sur les
singularites des surfaces (1976-1977), expose 4, LNM 777 (1980), Theoreme 1; also
`Bl_{p1,p2} P^2`). No constancy or rigidity argument for smooth rational surfaces is used anywhere:
the type arithmetic and the uniqueness citation do the whole work.
*The branch curve.* `B := beta_*(B°)` computes: `-2K_{Y°} = beta*(-2K_Y) - 2 e'` and `B° = -2K_{Y°}`
give `B° + 2 e' in |beta^*(-2K_Y)|`, hence `B = beta_*(B° + 2 e') in |-2K_Y| = |O(4,4)|` (since
`beta_*(e') = 0`); `B^2 = (B° + 2 e')^2 = 28 + 4*2 - 4 = 32` consistently with `O(4,4)^2 = 32`;
`B.K_Y = -16`. Then:
- `B` has exactly one singularity, at `q := beta(e')`, and it is an ordinary node: `beta` is an
  isomorphism off `e'`, so `B` is smooth off `q`; by Q3 `B°` meets `e'` transversally at two
  distinct points, and contracting a smooth `-1`-curve meeting a smooth curve transversally at two
  distinct points produces an ordinary double point (two distinct local tangent directions);
  independently and consistently, `p_a(B) = 1 + (B^2 + B.K_Y)/2 = 9` against the normalisation
  genus `8` gives total delta-invariant exactly `1`.
- `B` is irreducible. The cover `X^# -> Y` has branch divisor reduced (it is smooth, and a
  smooth double cover of a smooth surface cannot have a multiple branch component), so `B` is
  reduced with Q3's single node as its only singularity. Suppose `B = B_1 + B_2` with bidegrees
  `(a, b)`, `(4 - a, 4 - b)`, all `0 <= a, b <= 4`, not both zero in either. Then
  `B_1.B_2 = a(4 - b) + (4 - a)b = 4(a + b) - 2ab >= 4` (minimum at `(1,0)+(3,4)` and mirrors).
  Now the local calculation of the node's own term, stated at its proved structure: the node is a
  double point (multiplicity `2` as a singular point of the curve `B`), with two *smooth transverse
  local branches*; two smooth plane branches with distinct tangents have local intersection number
  `1` at the node (in the local model `{u v = 0}` the branches `{u = 0}` and `{v = 0}` intersect
  with multiplicity `dim_C k[[u,v]]/(u,v) = 1`; Bezout's lower bound `mult_p(f) mult_p(g) = 1`,
  attained for distinct tangents). So the node contributes `{1}` as a local intersection term
  between the two branches — not `2` (the `2` is the *multiplicity of the point for the whole
  curve*, and the earlier text's use of it as the `(B_1.B_2)_q` term confused the two). Now split
  as before:
  (i) the two branches lie in different components: then `(B_1.B_2)_q = 1`, and the remaining
  `B_1.B_2 - 1 >= 3` is spent at other points of `B_1 cap B_2`, each a second singularity of `B`;
  (ii) both branches lie in one component: the node is internal to that component and contributes
  `0` to `(B_1.B_2)_q`, so the whole `B_1.B_2 >= 4` is spent at other intersection points, each a
  second singularity of `B` (if all additional intersections lie at one point, it is a singular
  point of the union distinct from `q`, again a second one). Either way there is a second singular
  point, contradicting "exactly one". (The m1 alternative
  `sum a_i b_i = 15 + sum delta_i <= 16` exhaustion gives the same and is recorded in the ledger.)

**Q5 (tau and the fixed node).** `iota_Co` commutes with `iota_dP`, so it descends to an involution
`tau°` of `Y°`, preserving `e'` (it preserves `alpha`, hence `E`, hence its image curve) and
descending to `tau` of `Y` fixing the node `q` (the node is the image of the `A_1` point over
`E`, which `iota_Co` preserves setwise); `tau` preserves `B` (it preserves `Fix(iota_dP)`, hence
`B°`); `tau` preserves each ruling (it fixes the classes `e, f` pointwise, as `e, f in S_Co`).
`Fix(tau)` contains no curve: for a fixed curve `C`, on `pi^{-1}(C)` the involution `iota_Co`
would either act as the identity — impossible, since `Fix(iota_Co) = E` (Nikulin's classification
at `(r, a, delta) = (11, 11, 1)`: a single rational fixed curve) and `pi(E)` is a single point —
or agree with `iota_dP` there, making the *symplectic* product `iota_Co iota_dP` fix the curve
`pi^{-1}(C)` pointwise, while a symplectic involution of a K3 has finite fixed locus. Hence
`Fix(tau)` is finite; an involution of `P^1 x P^1` preserving `O(1,1)` with finite fixed locus is
of product type with both factors nontrivial, hence conjugate with `q` to
`(x, y) mapsto (-x, -y)` at a `tau`-fixed point (four fixed points).

**Q6 (landing).** After that conjugation, `B in |O_Y(4,4)|^tau` is irreducible with exactly one
ordinary node at a `tau`-fixed point and smooth elsewhere, and the resolved double cover of
`{z^2 = f}` is `X`, carrying the same labelled `H`, `alpha`, `I_Co`, `I_dP`: the member is in the
one-node family `B^(p)`, and `sigma` is its period. `square` (Section QC).

## Theorem C (the quotient is arithmetic, not rigid)

With Theorem B in place, Section QC proves: at every `sigma in O`, the marked K3 carries the
quotient model `(Y° = X/iota_dP, B°, iota_Co-induced tau, h')` with the numerics of Q1, the
quotient lattice identified with index one in Q2, the node curve and transversality in Q3, the
one-node `(4,4)`-curve in Q4, `tau` product with a `tau`-fixed node in Q5 — i.e. **a member of the
retained one-node construction**. The earlier blanket appeal to rigidity of smooth rational
surfaces is removed: the load is carried by the degree-`7` uniqueness of del Pezzo surfaces
(Demazure, cited in Q4), the `a^2 - m^2 = 2` parity obstruction, the `F_2`-exclusion by ampleness,
and the `B_1.B_2 >= 4` irreducibility bound.

## Theorem D (the image, at the original quantifiers)

On the component of `D(T_Co)` containing the periods of members, with `p` the marked period map of
the direct one-node construction into `D(T_Co)/Gamma_L`, and with `O` as in Section L:

> `im(p) = O / Gamma_L`

*Proof.* `im(p) subset O/Gamma_L`: every member carries `A = 2H - alpha` ample (corpus
Lemma 2.2 of `sm00_positive-half-A21.md`) and the labels are flat in the family, so each marked
period of every member lies in `O` at the construction's markings. `O/Gamma_L subset im(p)` is
Section QC applied point-by-point: every `sigma in O` admits its witnessing marked pair (PSS
realization of the `S_Co`-polarized structure at :9480, verified verbatim), Theorem B makes the
involutions geometric at the chamber hypothesis (`A` ample), Section L supplies the census, the
single contracted curve, the frame inequality and the pencils, and Section QC reconstructs the
member whose period is `sigma`. Membership in the image is decided member by member; no
dominance-to-surjectivity inference appears anywhere. `square`

**Theorem D (relations; the exact standing of `O` against the original A20 claim).** Put

`O~ := {sigma : exists a marked pair (X, psi) at sigma with psi(S_Co) subset NS(X), psi(A) ample}`
(the pass-2 locus), and `O := {sigma in O~ for which psi(alpha) is irreducible-effective}`.

- The original A20 problem's own scope is `O`, not `O~`: the tuple's fourth authored bullet
  carries `alpha` as the class of the node's *exceptional curve* — a smooth irreducible
  `(-2)`-curve by the very definition of the nodal resolution — so the original marked-image
  question reads natively on the realization locus with the exceptional bullet fulfilled.
  Defining `O` with the irreducibility clause is thus *restoring* the original hypothesis at the
  realization side, not weakening it.
- The relations are exact: `im(p) subset O` (at every member, `alpha` is by construction the
  node's exceptional curve: irreducible-effective; so members lie even in `O`, a fortiori
  beyond what pass 1 recorded as `O~`); `O subset O~` (by definition); and
  `O~ minus O subseteq {(F4)-walls}`: at a `sigma` of `O~` lying outside the exceptional bullet,
  `alpha` is reducible; Theorem SPLIT puts such a realization at its (TAC) alternative, whose
  components are (F4)-classes, so `sigma` lies on an (F4)-wall; and conversely, on an (F4)-wall
  either the effective-sign pairing kills ampleness outright (so `sigma` is not even in `O~`), or
  the effective (F4)-class with `A`-positive sign decomposes `alpha` as in Lemma 4, again making
  the realization alpha-reducible. So the two sets are disjoint.
- Therefore, with the directions separated as they must be:
  **(Suff-direction, established).** The image theorem at the ORIGINAL quantifiers is
  `im(p) = O/Gamma_L` (proved by Section QC at the original tuple). If the pinned glue is
  (F4)-free, then additionally `O~ = O` at every realization (an (F4) class is what makes
  `alpha` reducible, by Theorem SPLIT's class-membership check and Lemma 4's ampleness-counting),
  so `im(p) = O~/Gamma_L` as well; and if moreover the pinned glue carries no (F2),(F3)-class,
  then `O~ = O = D_Co^o` exactly and B24 holds verbatim. None of this rests on any realization
  beyond those of the original family.
  **(Necessity-direction, with each equality stated at its own domain's criterion — the earlier
  merged form is corrected.)** An (F4)-carrying wall's periods fall into exactly two behaviors at
  any realization: with the `A`-negative sign, ampleness fails at every point of that wall (the
  wall is dead on both sides — it is neither in `O~` nor in the image, but it **is** still inside
  `D_Co^o`, which contains every non-`NL_2` stratum); with the `A`-positive sign and ampleness
  surviving, Lemma 4's mechanism gives `alpha = x + D` reducible — a genuine TAC stratum of
  `O~ minus O`, absent from the image. It follows (i) every *paired* wall of any of the three
  families kills the verbatim equality `im(p) = D_Co^o/Gamma_L`, because its points are in
  `D_Co^o` while never being in `O` (hence never in the image): the ampleness-dead behavior by
  itself already kills it, and the TAC behavior kills it a fortiori. And (ii) the equality
  `im(p) = O~/Gamma_L` is threatened by exactly one behavior: a nonempty TAC stratum, since
  every other behavior (death of ampleness at an (F4)-wall, and the ampleness death of every
  (F2),(F3)-paired wall) puts its points outside `O~` **as well**, so they do not spoil the
  `O~`-equality. Hence, at their own domains:
  > `im(p) = O~/Gamma_L`  iff  **(X2)** no glue-carried (F4)-wall carries a correct-sign
  > `A`-ample realization (no nonempty TAC stratum).
  > B24 VERBATIM: `im(p) = D_Co^o/Gamma_L`, `D_Co^o := D \ NL_2`,  iff
  > **(X-TM)** the pinned glue carries NO (F2),(F3),(F4) pairing at all.
  Here `(X-TM)` — the full (T-mixed)-no — is the discriminant-form question about the pinned
  glue (open; the maintained ambient exists, and the correct Enriques-side anchors for it are
  `T_En = U + U(2) + E8(2)` of rank `12` and det `2^10` with `alpha = e - f` in the first `U`
  and `T_Co = alpha^perp_{T_En} = Z(e+f) + U(2) + E8(2) = <2> + U(2) + E8(2)` of rank `11`,
  report :472-:505, :73; the earlier `rank-10` shorthand in referee communications is wrong and
  is withdrawn). `(X2)` is the named geometric question **(T-strata)** about the existence of
  `alpha`-reducible tacnode-alternative (A2) members with the same labels — attacked via the
  cuspidal discriminant inside the one-node locus's closure in `|H_p|` and the
  effectivity/ampleness-sign analysis there (with ties to m4's `Heeg_one`/`(warn:special-null)`
  reading). Both are left open exactly as stated; the tacnode strata are NOT claimed closed by
  publication, and no group equality is asserted anywhere.

The three markers of B24, at their now-proved content:

- **The arrangement** `{delta^perp : delta in T_Co, delta^2 = -2} = NL_2(T_Co)` is excluded
  pointwise (Theorem A). By the (verified, m8-round2) observation that every mixed class's wall
  equals its `t`-part's wall (`x^perp cap D = t^perp cap D`, since `s in S_Co = T_Co^perp` is
  automatically orthogonal to every point of the domain), every excluded wall of the image is an
  ordinary `T_Co`-Heegner divisor: the complete list is `NL_2` **plus the glued (F2),(F3),(F4)
  walls** (norms `-4, -4, -6`; (F1) collapses to a pure root, subsumed in `NL_2`; (F5) has
  `t^2 = -2`, likewise subsumed). The (F2),(F3)-walls are excluded by ampleness (`A`-null
  Riemann-Roch-effective at the wall), the (F4)-walls by reducibility of `alpha` (the exceptional
  bullet of `O`; the tacnode alternative), the un-glued walls of those norms are *not* excluded
  (their periods may well be in `O` and in the image). Hence
  > `O = D(T_Co) \ [ NL_2(T_Co)  U  {gamma-paired (F2),(F3),(F4) walls} ]`.
- **The chamber** is the single labelled condition "`2H-alpha` ample": `A` lies on the Kahler side
  of the positive cone on the whole component (the sign of `A.omega` is locally constant on the
  labelled moduli, descends because every label-preserving change of marking fixes `A`, and is `+`
  at members — m5's Theorem 4); `S_Co` carries no `A`-null root (m4's Lemma C1, one-line parity),
  so `A` lies in the interior of a genuine chamber of the `S_Co`-arrangement; and the frame
  inequality `e.delta >= 0`, `f.delta >= 0` for every effective root holds at *every* `sigma in O`
  (Lemma 4b), so no separate chamber wall needs to be excluded.
- **The exceptional root** `alpha` is a *function* of the labelled data, not a label: the unique
  `(-2)`-class of `S_Co` with `H.alpha = 0` and `A.alpha > 0` (m4's Lemma C1(b)); effective as soon
  as `A` is ample (Theorem SPLIT), irreducible-effective by the exceptional bullet of `O`'s
  definition, and the only effective `H`-null `(-2)`-class at any `sigma in O` (Lemma 4 with the
  bullet) — which is what places the one node, its `tau`-fixedness and the irreducibility of `B`
  automatically at every period of `O` (Q4-Q5).

Density point (adjudicated, against m8's rejected claim): `O` is analytically open (relative
ampleness, :5167) and contains the corpus's nonempty Zariski-open subset of `D_Co^o/Gamma_L`
(corpus item 3); and `D_Co^o/Gamma_L` is itself Zariski-open in `D/Gamma_L` (finitely many orbits
of roots of fixed norm in an indefinite 2-elementary lattice make the wall image a single Heegner
divisor, algebraic by Baily-Borel on the arithmetic quotient). The corpus's standing statement is
consistent with every exclusion proved, with this reading; a density claim for a fixed-norm
arrangement is the (rejected) false form.

**Theorem (residual (T-mixed), at its verified census and its completed pairing table).** With
`L_K3 supset S_Co perp T_Co` of index `2^11` and the full-graph glue `A_{S_Co} =~ A_{T_Co}(-1)`,
Lemma L.2's census and the wall identification above (`x^perp cap D = t^perp cap D`) show the
excluded walls of the image are the pure `T_Co`-roots plus, at most, the glued (F2),(F3),(F4)
families; and:

- `BAD_S` — the 2-adic classes of `S_Co` containing an `A`-null `s` of norm `-4` — has exactly
  **121** classes: the 120 (F3)-classes (`(a,b) = (0,0)` in the `U`-part, `w` a root class of
  `E8 mod 2`, one per root class) and the single (F2)-class `(U-bits (1,1), w-bar = 0)`. Verified
  in `computations/reports/coble_mixed_census.py` (+`-run.txt`), and matching the deficit
  computation: for `s = a e + b f - 2(a+b) alpha + w` with `s^2 = -4`,
  `ell := norm_{E8}(w)/2 = 1 + a b - 2(a+b)^2 = 1 - 2(a + 3b/4)^2 - (7/8) b^2`, so `ell >= 0`
  forces `b in {0, pm 1}`, and enumerating gives `(a,b) in {(0,0), (-1,1), (1,-1)}` — the latter
  two being the one (F2) class, the first covering all 120 root classes `(F3)`. The machine census
  (box `[-40,40]`) and this bound agree.
- `BAD_T` — the 2-adic classes of `T_Co` containing a norm-`(-4)` `t` — has exactly **496**
  classes (`3 * 120 + 136`), where the `E8`-class split is `120` classes of `q`-value `1` in
  `E8/2E8` (reachable by a root, and exactly those) versus `136` of `q`-value `0` including zero.
- So `|BAD_S| = 121 <= |NOTBAD_T| = 1024 - 496 = 528`: no *counting* argument forces a glue
  pairing of a `BAD_S` class with a `BAD_T` class. That is all the cardinality comparison
  establishes; it does not construct or prove existence of a quadratic-form-compatible glue
  avoiding every pairing. Such an existence claim would have to be exhibited through the
  maintained discriminant-form constructor (`DS.isometry_to(DT.twist(-1))` at the validated pin
  `6ad7a5ea396da6e758ee28f3dea10a35baee0266`; the local image does not implement it), and it is
  **left open**, separately from the pinned-glue question itself. The pairing question is now
  asked for all three families, with each domain and partner space machine-corroborated by bounded
  exact enumeration (self-stability asserted across two box sizes, exploratory tier):
  > **(T-mixed).** Does the pinned Coble glue (recorded as an open datum at report :661 item 7)
  > pair
  > (F2) the one class `[ (e-f)/2 ]`        into the 496-class partner space at norm `-4`, or
  > (F3) one of the 120 root classes `[w/2]` into that same 496-class partner space, or
  > (F4) the class `[alpha/2]`              into the 528-class partner space at norm `-6`?
  
  Consequently, at their own domains: `im(p) = O~/Gamma_L` iff `(X2)`; and B24 VERBATIM
  (`im(p) = D_Co^o/Gamma_L`, `D_Co^o = D \ NL_2`, with the chamber and root content of Theorem D)
  iff the pinned glue carries **no (F2),(F3),(F4) pairing at all** — because any single pairing
  makes some `D_Co^o`-point miss the image ((F2),(F3),(F4)-paired walls all sit inside `D_Co^o`:
  (F2),(F3) by ampleness death and (F4) by either ampleness-death or alpha-reducibility). In every
  case the chamber and root content of Theorem D stands; and the two equality questions are
  separately named, not merged. An earlier hand-sketch asserting a forced pairing was
  retracted above as a miscount; the counts here are machine-corroborated by bounded exact
  enumeration (`BAD_S = 121`, partner spaces `496`, `528`, self-stability asserted across two box
  sizes in the run log; exploratory tier).
- The brick probe (`coble_mixed_gluing_probe.py` +`-run.txt`): the diagonal/anti-diagonal glue of
  `U^3 + E8(-1)^2` carries two mixed wall classes (`x = e_a - f_a`, `x = e_b - f_b`, `x^2 = -2`,
  `H.x = 0`, `A.x = 0`, both projections nonzero — their class pair is exactly the (F2)-type
  `((1,1),0) <-> ((0,(1,1),0)`, itself in `BAD_S x BAD_T`): so both branches are genuinely live.
  It is exploratory with respect to B24 — the brick glue is not claimed to be the Coble glue, and
  the retained geometric glue is the open input. That distinction is preserved.

**Theorem E (B25, at its proved content; group names kept separate).**

1. **Deck = monodromy image.** The marking cover of the direct one-node stack is the cover
   trivialising the labelled local system `R^2 f_* Z`; it is attached to the monodromy kernel,
   hence normal with deck group equal to the monodromy image `G1` on `T_Co` (m1 Theorem 6.2; m4's
   normalizer-quotient form for the general phrasing is consistent — the labelled-trivialising
   cover is normal by construction). The mark-cover of periods `O -> O/Gamma_L` has deck
   `Gamma_L/(Gamma_L cap {pm 1})` (m7 SS5(a)).
2. **Inclusions proved.** `G1 subseteq Gamma_L = G5` (flatness of the four labels in the family;
   m4 Prop. D2, m7 SS5(b)) and `G1 subseteq Gamma^dir_{Co,2} = G2` when the marking datum carries
   the chamber (the monodromy preserves `A = 2H-alpha` and the ample cone; m7 SS5).
3. **Computed generators.** `G1` contains `W_node = <w_delta, (w_s, w_e)>`: the
   Picard-Lefschetz reflections `w_delta`, `delta in T_Co`, `delta^2 = -2`, of the
   second-`tau`-fixed-point wall `Z_q`, and the nodal-pair transformations with
   `s = delta + delta'`, `e = delta - delta'`, `s^2 = e^2 = -4` (m5 Theorem 3 and SS6.1; verified
   symbolically). They live at *boundary* degenerations, never at members — precisely compatible
   with Theorem A. Separately, the node degeneration's own vanishing class is `pm alpha`, with
   `w_alpha|_{T_Co} = id`: `alpha` contributes nothing to `G1` (m3 SS6.2, m7 SS5).
4. **The chamber question (CH) is decided; and the residual is named at its two pieces.**
   (CH) is **decided** (m4 of run `smw0uqe8g`, accepted at `.ultramath/smw0uqe8g/REFEREE-verdict-m4.md`):
   at the corpus's authored chamber semantics — `@def:direct-cover-datum` item 6 (:878: the chamber
   in which the exceptional curve is effective and the contraction good) with
   `@rmk:chamber-not-transported`'s chamber containing the Kahler cone — the chamber is determined
   by `(H, alpha)` at every member, because no effective `(-2)`-wall approaches `H`
   (`dist(H_b, delta^perp) >= 1/sqrt 2` for every effective root `delta != +-alpha_b`, integrality;
   the accumulation hedge of `the-heegner-line:638`/`:659` is obsolete at the member scope), so the
   stabiliser condition `{g c = c}` is automatic for the label stabiliser, and
   > `Gamma^dir_{Co,2} = Gamma_L`
   as a lattice-level statement at the authored chamber's reading. The two faithful counter-readings
   (full-lattice and period-domain chambers) keep their own determination failures (each recorded
   with its witness); and the cross-member *transport* fork of the corpus's fourth bullet is
   untouched by this decision and stays open as it stood.
   The residual content of B25 is then exactly the two named pieces, with nothing else intervening:
   (D1) *monodromy-maximality*: the family's discriminant meets every `Gamma^dir`-orbit of walls;
   (RI) *reflection index*: is `ker rho_{T_Co}` (the `O^+`-stable group with the discriminant
   action's kernel) generated by the `(-2)`-reflections of `T_Co`? — with the observation that every
   wall reflection already lies in the stable group (`rho_T` is trivial on lattice-vector
   reflections because `[delta] = 0` in `A_{T_Co}`), so `(D2)` is equivalent to `(RI)`. Both are
   named open; in particular the `T_Co`-surjectivity of `coble_labeled_embedding-run.txt` SS3.3-3.4
   enters only the four-group comparisons, not `(D2)`. With `(D1) + (RI)`, B25 concludes
   `G1 = G2 = G5`; `G3, G4` are untouched; `@prob:group-identification` stands unchanged with no
   equality by notation.

## Premise ledger (inputs and their tiers)

| # | input | tier |
|---|---|---|
| 1 | `@def:direct-cover-datum` with the one-node refinement; involutions and labelled classes | corpus definitions (:853-932) |
| 2 | Explicit member with no other singularity, `@sec-explicit-curve` plus its verification contract | corpus (:2425-2445) |
| 3 | Lattice labels (`S_Co, T_Co, S_dP = Lambda`, ranks `(3,8,0,11)`, index `2^11`, full-graph glue); `formalization/coble-enriques/A21Arithmetic.lean` at its own scope | corpus theorems + machine verification at its scope |
| 4 | Corpus item 3 (`B` connected, image dimension, Zariski-open content, Borel extension per its stated hypotheses) :659-:663 | corpus |
| 5 | PSS realization (`huybrechts :9480`); global Torelli/automorphism part (`:10227`-`:10240`); ampleness openness (`:5167`); ampleness on rational curves (`:737`); Saint-Donat (`:1027`) | primary statement-level; anchors verified verbatim |
| 6 | Nikulin's fixed-locus classification for 2-elementary involutions at `(r,a,delta) = (3,3,1)` and `(11,11,1)` (computed in place); Noether/Castelnuovo numerics; del Pezzo classification degree `7` (Demazure, LNM 777) | standard/book tier |
| 7 | `2H-alpha` ample on every member; characters/ranks | corpus lemmas 1.3, 2.2 of `sm00_positive-half-A21.md` |
| 8 | Swarm-accepted intermediate theorems (exclusion mechanisms; cover-step ingredients; monodromy generators; sign constancy; m6's arrangement computation and audit) | referee-accepted with records |
| 9 | Verified class censuses: `BAD_S = 121`, `BAD_T = 496`, the `E8`-split `120/136`, the `ell`-bound, the quadratic deficit | exact arithmetic, `coble_mixed_census.py` (+run log), exploratory tier |
| 10 | The brick ambient `U^3 + E8(-1)^2`: maintained embeddings, glue order `2^11`, two mixed wall classes | maintained construction (`coble_mixed_gluing_probe.py`); exploratory with respect to B24 |
| 11 | Every mixed class's wall equals its `t`-part's wall (m8-round2 Theorem 2.1, verified); the pairing table (`496/528`, stability-asserted) | referee-verified; exact arithmetic, `coble_mixed_census2.py` (+run log), exploratory tier |

Computation used is hand-carried exact arithmetic small enough to check line by line; the machine
counts are verified and each is also proved in the text.

## Falsifiable cross-checks carried by the theorems

1. **No `T_Co`-curve of square >= -2 on a member** (Theorem A): reads `sm57_README.md`'s `F'`
   classes consistently (`[C_1+C_2]` invariant `(-2)`, `[C_1-C_2]` anti-invariant `(-6)`), as m6's
   audit C3 supplies.
2. **Ampleness-versus-arrangement at the wall**: members are ample, so they avoid the arrangement
   (trivial direction); off-arrangement periods being members is Theorem D's content via `O`, never
   "ample on every member" read backwards.
3. **Fixed-locus bookkeeping**: `chi(Fix iota_dP) = 2 rk S_dP - 20 = -14`; the branch genus `8`;
   the two conic points and the one blow-up per node make `rk S_dP = 2+k` consistent with
   `e(Fix) = 2(2+k) - 20`.
4. **Density**: the `(-2)`-walls are locally finite (Hodge-form bound), so the corpus's open-image
   statement is consistent with the pointwise exclusion.

## What remains open next (named, not cosmetic)

* `(T-mixed)` — the glue-pairing question above, deciding between the two branches of B24;
  attackable by computing the pinned Coble glue's action on the 121 `BAD_S` classes (the maintained
  machinery for the ambient exists; the pinned glue is the recorded open datum). Reference inputs
  for the pinning route, corrected at their source: `T_En = U + U(2) + E8(2)` of rank `12` and det
  `2^10`, `alpha = e - f` in its first `U`, `T_Co = alpha^perp_{T_En} = Z(e+f) + U(2) + E8(2)` of
  rank `11` and det `-2^11`, `S_En + T_En` of index `2^10` in `L_K3` with the full-graph gluing
  (report :73, :472-:505, :575-:585, :333; an earlier `rank-10` shorthand for `T_En` is withdrawn).
* `(D1)` and `(D2)` of Theorem E — with `(D2)` equivalent to the reflection-index question
  **(RI)** (is `ker rho_{T_Co}` generated by `T_Co`'s `(-2)`-reflections?); `W_node <= G1` is
  computed; the `T_Co`-surjectivity enters only the four-group comparisons, not `(D2)` (m4's D2',
  accepted).
* `Gamma^dir_{Co,2} = Gamma_L` — **decided** at the authored chamber's reading (CH: m4 of
  `smw0uqe8g`, accepted at `.ultramath/smw0uqe8g/REFEREE-verdict-m4.md`): the chamber is determined
  by `(H, alpha)` at every member with the accumulation hedge collapsed; readings (b)/(c) remain
  faithful counter-readings; the cross-member transport fork stays open.
* `@prob:group-identification` among the four — untouched except `G1`'s proved content.
* The A21-side leftovers: rank-`>=12` unmatched-extra-class chamber comparisons, R4 recovery, the
  (O1)/(O2) decomposition, `k >= 2` saturation, and the four dep-audit citation sites of
  `computations/reports/sm57_depaudit-ledger.tsv` (three unsatisfiable as worded).
