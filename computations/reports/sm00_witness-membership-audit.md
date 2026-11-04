# Witness membership in the direct-projective one-node family: audit, corrections, certificates

Member m3, swarm `smw0b9kmo`, direction d6.  Evidence state: main@`83403bc8` of
`/workspace/nucleus/work/projects/p-9fcb4ed7f4b64e008de2ee29a7197bf4/repo` (read-only here, cited by
path).  Authored statement: `writing/coble/heegner-report/coble-heegner-research-report.md` at
`a145cea4a5` lines 601--638.  Tracked evidence audited: `computations/reports/sm57_proof-m5.md`,
`sm57_chamber-obstruction-m6.md`, `sm57_obstruction-m8.md`, with the scripts and logs they cite.

Files of this directory that carry the computation:

* `audit_witnesses.py` -- exact-arithmetic (sympy, rational) audit, written from scratch for this
  report, no code copied from the tracked scripts;
* `audit-witnesses-run.txt` -- its complete output (127 lines, exit status 0; six members, the sixth
  being the codim-2 tangency stratum of the Remark in §5), the certificates quoted below.

The question this direction answers: *are the named members genuinely members of the same
direct-projective one-node family, with the same labels, the same degree-4 class and the same root, so
that the chamber obstruction compares two tuples that the authored statement actually quantifies
over?*  Answer: yes for all of them, with four corrections to the tracked text, none of which removes
the obstruction, and one of which (Theorem A below) is a missing hypothesis in two tracked lemmas.

---

## 0. Verdict

1. **Membership: all pass.**  The five members audited -- m5's `b_0`, m5's `b_*`, m6's member `B`,
   m8's `F'`, and the corpus's own explicit member of `sec-explicit-curve` -- each satisfy, by exact
   rational certificate: `f` is a `tau`-invariant section of `O(4,4)` (monomials `x^i y^j`, `i+j`
   even, `0<=i,j<=4`), `f(p) = a_00 = 0`, `a_11^2 - 4 a_20 a_02 != 0`, and the singular locus of
   `B = {f=0}` is exactly `{p}` in all four affine charts of `P^1 x P^1`.  This is the corpus's own
   membership predicate (`lem:node-condition`, `sec-invariant-system`) and nothing weaker.
2. **Same labels.**  Each of them has no node at the three remaining `tau`-fixed points, which is what
   makes `Fix(iota_Co)` a single smooth rational curve, `chi(Fix) = 2`, and hence
   `rk S_Co = (2+20)/2 = 11` (Lefschetz, `prop:tuple-of-the-construction`).  So the label data of all
   five have the same shape; they are one family, not five families (Theorem B).
3. **Four corrections to the tracked text** (details and proofs below):
   * **(C1)** m6 `Thm 2.3` displays `... - x^3y^3 ...`; the coefficient list printed in the same
     theorem and the tracked log `sm57_verify_members.log` both have `a_33 = -4`, i.e.
     `-4x^3y^3`.  With the displayed polynomial the claimed bitangency `f_B(+-1,y) = (y^2-1)^2` is
     false; with `a_33 = -4` it is true.  Displayed polynomial: typo.
   * **(C2)** m5 `sec-6` says `b_*` is *the same member, found independently,* as m6's member `B`.
     It is not.  The two affine coefficient vectors are not proportional (ratio list
     `-13/6, -5/4, 28, -13/4, -3/2, 2, -1, 4, -5/4, 2, 7/3, -2`) and their bitangent rulings differ
     (`f_*(1,y) = (y-1)^2(y-3)^2` against `f_B(1,y) = (y-1)^2(y+1)^2`).  Both are valid witnesses; the
     identity claim is false and must not be used as one certificate for two members.
   * **(C3)** m5 `Lemma 5.1`'s last sentence ("In case 1 the fibre over the ruling through `p` is
     `I_2` with component `H`-degrees 0 and 2") and m6 `Lemma 1.2` ("hence
     `f(0,y) = y^2(a_02 + a_04 y^2)`, which has a double root at `y=0`") both silently assume
     `a_02 != 0` (resp. `a_20 != 0`) -- a hypothesis that is **not** part of the corpus's node
     condition.  On the complementary divisor the node's ruling fibre degenerates from `I_2` to
     Kodaira type `IV` (three `P^1`s through one common point, `H`-degrees 0,1,1), producing two extra
     `(-2)`-classes of `H`-degree 1.  m8's `F'` has `a_02 = 0` and is on that divisor; m5's `b_0`,
     `b_*` and m6's `B` do not, so the obstruction's own case analysis is valid for the pair it
     compares.  Theorem A gives the dichotomy with proof.
   * **(C4)** m6 `Lemma 3.1` states the label transport for "any two one-node members", but its family
     is the double cover family over the *fixed* base `Y' = Bl_p Y`, which only contains members whose
     node is *the fixed point* `p`.  The one-node locus has four quadrants, one per `tau`-fixed point,
     and m8's `F'` sits in another quadrant from all the others (its node is
     `([0:1],[0:1])`, the antipode of the corpus's `p`).  The statement is repaired, not refuted:
     Theorem B (ii) supplies the cross-quadrant isometry from the automorphism of `Y` preserving
     `(tau,h_1,h_2)`.  The statement of Lemma 3.1 is true (Theorem B); what is wrong is that its *proof*
establishes it only inside one quadrant, so as written the lemma does not cover `F'`.
4. **The `H`-degree-1 census is exact, not a bound** (§5): `nu = 0` for the corpus's member and for
   `b_0`; `nu = 4` for `b_*` and for `B`; `nu = 2` for `F'`.  m5's `nu(b_*) >= 2` and m8's degree-1
   classes are thereby sharpened and reconciled.

---

## 1. The membership predicate, exactly

`Y = P^1 x P^1` with rulings `h_1,h_2` (`h_i^2 = 0`, `h_1.h_2 = 1`); in affine coordinates
`(x,y) = (x_1/x_0, y_1/y_0)` around a `tau`-fixed point `p`, `tau(x,y) = (-x,-y)`.  The invariants
of the `tau`-action on `H^0(O(4,4))` are the monomials `x^i y^j` with `i+j` even, `0<=i,j<=4` (13 of
them, `sec-invariant-system`); the section is

    f = sum_{i+j even} a_ij x^i y^j,   so   f = a_00 + a_20 x^2 + a_11 x y + a_02 y^2 + (degree >= 4)
    (no linear terms, by tau-invariance),  and   X^sharp_b = {z^2 = f} -> Y.

**Definition (member).**  `b` is a *one-node member of the direct-projective construction* iff
`a_00 = 0`, `a_11^2 - 4a_20 a_02 != 0` (ordinary node at `p`, `lem:node-condition`) and `B_b = {f=0}` is
smooth away from `p`.  The tuple attached to `b` is `(L_K3, I_dP, I_Co, H, alpha, c)` with
`iota_dP(x,y,z) = (x,y,-z)`, `iota_Co(x,y,z) = (-x,-y,-z)`, `H = pi^*O(1,1)`,
`alpha = [D_b] = pi^*(e)` on the resolution, `e` the exceptional curve of `Y' = Bl_p Y`.

**Chart invariance.**  Everything above is chart-independent in the only sense needed: the transition
`x -> 1/x` (resp. `y -> 1/y`) between corner charts sends a monomial `x^i y^j` to `x^{4-i} y^{4-j}`
up to a unit, and `(4-i)+(4-j) = 8-(i+j)`, so the invariant system, the vanishing at the corner, and
the node condition (`lem:node-condition` is a local analytic statement) are preserved.  So a member
may be presented in the corner chart in which *its* node is the origin; that is what the certificate
below does, and it is why m8's `F'` -- whose node is `([0:1],[0:1])`, not the corpus's `p` -- is
audited on exactly the same footing as the others.

**Proposition 1.1 (membership gives the tuple).**  Let `b` be a member.  Then on the resolution
`X_b -> X^sharp_b`:
(i) `iota_dP, iota_Co` are commuting involutions of `X_b`; (ii) `iota_dP^* omega = iota_Co^* omega =
-omega` and `(iota_dP iota_Co)^* omega = omega` for `omega = dx ^ dy / (2z)`; (iii)
`H^2 = 4`, `H.alpha = 0`, `alpha^2 = -2`; (iv) `H` and `alpha` are fixed by both involutions; (v)
`Fix(iota_Co) = D_b`, `chi = 2`, so `rk S_Co = 11`.

*Proof.*  (i),(ii) are `prop:local-operators`, and only need `f` in the invariant system (the formulas
are the same for every member).  (iii): `H^2 = 2 O(1,1)^2 = 4`; `alpha = pi^*e`, `e.O(1,1) = 0`;
`alpha^2 = 2 e^2 = -2`.  (iv): both involutions act on the base by `(x,y) -> (+-x, +-y)`, hence
trivially on `h_1, h_2` and on `e`, so `I^*H = H`, `I^*alpha = alpha`.  (v): `iota_Co` fixes `(x,y,z)`
iff `x = 0 = y` (in the corner chart) and `z = 0`, i.e. iff `f` vanishes at the corner; the corner
value is `a_00 = 0`, and the values at the three other `tau`-fixed points are `a_04, a_40, a_44`
(coefficients of `y^4, x^4, x^4y^4`), which the membership certificate shows to be nonzero.  Hence
`Fix(iota_Co)` is the single node, resolved to the single curve `D_b`, fixed pointwise because the
lifted `tau` acts trivially on `P(T_pY)`; `chi = 2`; Lefschetz gives `2 = chi(Fix) = 2 + tr(iota_Co)`
and `rk S_Co = (2+20)/2 = 11`.  `[]`

The point of (v) is that the *rank* is part of the audited data: a member with two nodes at two
`tau`-fixed points would have `rk S_Co = 12` and would not carry the same labels.  So the one-node
hypothesis is load-bearing for the labels, and it is verified, not assumed.

## 1bis. Which of the tuple's data are canonical (so that "the same labels, degree-4 class, root" is a
statement about the construction, not about a chart)

For every member `b`:

* **(a) the two invariant lattices have fixed ranks.**  `S_dP = H^2(X_b,Z)^{I_dP=1}` has rank `3` and
  equals `N = <L_1,L_2,D>`; `S_Co = H^2(X_b,Z)^{I_Co=1}` has rank `11`.  Proof: `Fix(iota_dP)` is the
  normalization of `B`, a smooth curve of genus `8` (`p_a(4,4) = 9` minus the node), so
  `chi = -14 = 2 + tr(iota_dP)` and `rk S_dP = (22-16)/2 = 3`; `L_1,L_2,D` are `iota_dP`-invariant of
  rank `3`, so `N = S_dP`.  For `S_Co` see Proposition 1.1(v).  Both ranks are part of the label data
  (`prop:node-count-invariant` uses the analogous statement for `k` nodes), and both are the same on
  all five audited members.
* **(b) the root is determined by `(H,` effective cone `)`.**  `{delta in Pic(X_b) : delta^2 = -2,
  delta.H = 0} = {+alpha, -alpha}`:  Riemann-Roch gives `chi(O(delta)) = 1`, so one of `+delta` is
  effective; `delta.H = 0` with `H` nef forces `pi_*(delta) = 0`, i.e. `delta` a multiple of the
  exceptional class, and `delta^2 = -2` pins the multiple.  So the authored phrase "the effective root"
  is a well-defined function of the pair `(labels, H)` plus the choice of sign, and the sign is fixed
  by effectivity -- which is exactly the clause of the fourth bullet.
* **(c) the marking is the only freedom.**  `(Y, h_1, h_2, tau, B, e)` determines the member; a
  marking `H^2(X_b,Z) ~= L_K3` is unique up to `O(L_K3)`, so comparing tuples *is* comparing
  `O(L_K3)`-orbits of `(I_dP, I_Co, H, alpha, c)`.  Nothing in (a),(b) depends on the chart: they are
  stated in `H^2(X_b,Z)`.

---


## 2. The certificates

Run `python3 audit_witnesses.py` (sympy, exact `QQ` arithmetic; the output in
`audit-witnesses-run.txt`).  Per member the script checks: the monomial support; `a_00`; the quadratic
part and its discriminant; the four `tau`-fixed values; the singular locus in each of the four affine
charts (Groebner basis of `(g, g_u, g_v)`, `[1]` means empty); the node-ruling tangency flags
`a_02 = 0`, `a_20 = 0`; the factorizations of `f(0,y)`, `f(x,0)`; and the factorizations of
`disc_y f`, `disc_x f` with multiplicities.

| member | source | `(a_20,a_11,a_02)` | disc | `(a_04,a_40,a_44)` | singular locus | node-ruling tangent? |
|---|---|---|---|---|---|---|
| corpus `sec-explicit-curve` | `sm57_verify_members.log`, `report:2407` | (1,1,2) | -7 | (3,19,29) | `{p}` only | no |
| m5 `b_0` | `sm57_member_b0_full.py`, m5 `sec-6` | (2,7,-5) | 89 | (-1,3,5) | `{p}` only | no |
| m5 `b_*` | m5 `sec-6` | (3,-28,13) | 628 | (-10,6,8) | `{p}` only | no |
| m6 `B` | m6 `Thm 2.3` (with `a_33 = -4`) | (-2,-1,-6) | -47 | (8,3,-4) | `{p}` only | no |
| m8 `F'` | m8 `sec 4.1` | (1,1,0) | 1 | (1,1,1) | `{p}` only | **yes, `a_02 = 0`** |

Discriminant factorizations (from the log; squarefree parts as computed):

| member | `disc_y f` | `disc_x f` |
|---|---|---|
| corpus member | `x^2 P_22(x)` | `y^2 Q_22(y)` |
| m5 `b_0` | `x^2 P_22(x)` | `y^2 Q_22(y)` |
| m5 `b_*` | `x^2 (x-1)^2 (x+1)^2 P_18(x)` | `y^2 Q_22(y)` |
| m6 `B` | `x^2 (x-1)^2 (x+1)^2 P_18(x)` | `y^2 Q_22(y)` |
| m8 `F'` | `x^4 (x^2+1) P_18(x)` | `y^2 Q_22(y)` |

with every displayed factor squarefree and pairwise coprime (the log prints the squarefree part of
each discriminant; its agreement with the listed squarefree part is the certificate).  Read off, with
the `I_1`/`I_2`/`IV` identifications proved in §3-§4:

* each `P_22`, `Q_22` root gives an irreducible nodal fibre (`I_1`, `chi = 1`);
* the corpus member and `b_0`: the only non-reduced ruling fibres are `x = 0` and `y = 0`, both `I_2`;
* `b_*` and `B`: additionally `x = +-1` are bitangent (`f(+-1,y) = (y-1)^2(y-3)^2`, resp.
  `(y^2-1)^2`), giving split fibres with two `P^1` components each;
* `F'`: `x = 0` carries a fourth-order point (`f(0,y) = y^4`, a perfect square), and `x = +-i` give
  `I_1`.

Euler-characteristic bookkeeping, which is what forces the types: for each member and each fibration
the sum of `chi` of the singular fibres must be `24`:

    corpus member, b_0 :  2 + 22 = 24     (both fibrations)
    b_*, B             :  2 + 2 + 2 + 18 = 24   (x),   2 + 22 = 24  (y)
    F'                 :  4 + 2 + 18 = 24       (x),   2 + 22 = 24  (y)

so `F'`'s node-ruling fibre must contribute `chi = 4`, not the `chi = 2` of `I_2`.  That is Theorem A.

---

## 3. Theorem A: the node-ruling dichotomy `I_2` / `IV` (the missing hypothesis of m5 Lemma 5.1
and m6 Lemma 1.2)

Set-up: `b` a member in the corner chart at its node, `Y' = Bl_p Y`, `e` the exceptional curve,
`C~ = h_1 - e` the strict transform of the ruling `{x=0}` through the node,
`pi: X_b -> Y'` the double cover branched along `B~`.  Write
`f = a_20 x^2 + a_11 x y + a_02 y^2 + a_04 y^4 + a_22 x^2y^2 + a_13 xy^3 + a_31 x^3y + a_40 x^4
+ a_24 x^2y^4 + a_33 x^3y^3 + a_42 x^4y^2 + a_44 x^4y^4`.  In the blow-up chart
`(x,y) = (XY, Y)` (so `e = {Y=0}`, `C~ = {X=0}`) the strict transform is

    ftilde(X,Y) = a_20 X^2 + a_11 X + a_02
                  + Y^2 ( a_40 X^4 + a_31 X^3 + a_22 X^2 + a_13 X + a_04 )
                  + Y^4 ( a_42 X^4 + a_33 X^3 + a_24 X^2 )
                  + a_44 X^4 Y^6 ,                                    (*)

(the degree 6 and 8 monomials of `f` become `Y^4(...)` and `Y^6(...)`; that is the only place the
parity of the exponents is used).

**Theorem A.**  Let `b` be a member (so `a_00 = 0`, `a_11^2 - 4a_20a_02 != 0`, and
`a_04 a_40 a_44 != 0`: none of the other three `tau`-fixed points lies on `B`, which is the condition
verified for every witness in §2 -- it is what makes `Fix(iota_Co)` the single curve `D`, §1(v)).
Let `F_0 = pi^*h_1` be the fibre of the `x`-ruling fibration over the node's ruling.  Then
`F_0 = (L_1 - D) + D` with `D = pi^*e`, and:
(i) if `a_02 != 0` (the ruling is transverse to `B` at the node): `L_1 - D` is a single smooth
rational curve, so `F_0` is an `I_2` fibre, component `H`-degrees `0` and `2`;
(ii) if `a_02 = 0` (then `a_11 != 0`): `L_1 - D = C_1 + C_2` with `C_i` smooth rational,
`C_1.C_2 = C_i.D = 1`, all three curves passing through one common point and pairwise transverse:
Kodaira type `IV`, `H`-degrees `1,1,0`, `C_i^2 = D^2 = -2`, `chi(F_0) = 4`.

*Proof.*  `pi^*h_1 = pi^*(C~ + e) = pi^*C~ + D`.  The branch divisor of `D -> e` is the zero divisor of
`ftilde(X,0) = a_20X^2 + a_11X + a_02` -- exactly the quadratic part of `f` at `p`, so it has two
distinct roots *by the node condition* `a_11^2 - 4a_20a_02 != 0`; hence `D ~= P^1`.  The branch
divisor of `pi^*C~ -> C~` is the zero divisor of `ftilde(0,Y) = a_02 + a_04 Y^2`, by (*).  If
`a_02 != 0`, that divisor is `{Y = +-sqrt(-a_02/a_04)}`, two distinct points (`a_04 != 0` because `B`
is smooth at the diagonal `tau`-fixed point), so `pi^*C~` is connected and of genus `0` by
Riemann-Hurwitz: one `P^1`, meeting `D` in `pi^*C~.D = 2(C~.e) = 2` points.  If `a_02 = 0`, `ftilde(0,Y) = a_04 Y^2` and the cover of `C~` is
`{w^2 = a_04 Y^2} = {w = +-sqrt(a_04) Y}`, two copies of `C~` meeting in the single point `Y = 0`;
together with `D = {Y = 0, w^2 = X(a_20X+a_11)}`, the three curves meet at `(X,Y,w) = (0,0,0)` and
nowhere else, and the tangent directions there are `(0,1,+-sqrt(a_04))` and `(0,1,0)`: distinct, so
pairwise transverse and every pairwise intersection number is `1`.  Squares: on a K3 `K = 0`, so a
smooth rational curve has square `-2` (adjunction); alternatively
`C_1 + C_2 = L_1 - D` has square `(h_1-e)^2 = -1`, so `2(-2) + 2 C_1.C_2 = 2(-1)` gives
`C_1.C_2 = 1`, and `(C_1+C_2).D = 2(C~.e) = 2` gives `C_i.D = 1`.  Degrees: `C_i` lies in the fibre
of the `x`-fibration, so `C_i.L_1 = 0`, and `pi_* C_i = C~ = h_1 - e` has `h_2`-degree `1`, so
`C_i.H = C_i.L_2 = 1`; `D.H = 0`.  `chi`: one `P^1` is `2`; two `P^1`s meeting twice is `2`; three
`P^1`s pairwise transverse through one point is `6 - 3 + 1 = 4`.  `[]`

**Corollary A' (m5 Lemma 5.1 and m6 Lemma 1.2, corrected).**  The sentence "in case 1 the fibre over
the ruling through `p` is `I_2` with component `H`-degrees 0 and 2" is a theorem only for members with
`a_20 a_02 != 0`; for `a_02 = 0` the fibre is type `IV` and carries *two* `(-2)`-classes of
`H`-degree one, which are precisely the two extra classes of `F'`.  m5's Lemma 5.1 conclusion ("a
curve of `H`-degree 1 forces a reducible fibre away from the node's ruling") and m5's
`Corollary 5.2`'s *iff* therefore each acquire the hypothesis `a_20 a_02 != 0`.  With it, both proofs
are correct as written; without it, m8's `F'` is a counterexample to the letter of both statements.
Nothing in the obstruction depends on the unqualified form: the pair the obstruction compares,
`(b_0, b_*)`, has `a_02 = 2, 13` and `a_20 = 2, 3`, so `a_20a_02 != 0` and Lemma 5.1 applies to
both.  `[]`

---

## 4. Theorem B: all members are members of *one* family, and the labels transport

**(i) Within a quadrant.**  Fix the `tau`-fixed point `p` and let
`B_p = {f : a_00 = 0, a_11^2-4a_20a_02 != 0, B_f` smooth away from `p`} subset `|O(4,4)|^tau`; it is
the complement of the discriminant-type divisor (the bad quadratic part, and the image of the proper
incidence variety of singular points away from `p`), hence nonempty Zariski open in the hyperplane
`{a_00 = 0} ~= P^11`, hence path-connected -- the complement of a closed complex-analytic subset of
real codimension at least two.  *This replaces the Bertini argument of the corpus's
`prop:one-node-connected` (the input the problem statement flags as disputed) by a dimension count.*
Over `B_p` the double covers of the *fixed* base
`Y' = Bl_pY` branched along the strict transforms form a smooth proper family, `H, alpha, L_1, L_2`
are pullbacks of classes of the fixed surface `Y'`, and `iota_dP, iota_Co` are given by the fixed
formulas on the total space.  Ehresmann plus parallel transport then gives, for any two members in
`B_p`, an isometry of `H^2` carrying `H -> H`, `alpha -> alpha`, `L_i -> L_i`, `I_dP -> I_dP`,
`I_Co -> I_Co`.  (This is m6 `Lemma 3.1`, whose proof I have re-derived and whose hypotheses I have
checked: the only inputs are that the branch class `O(-2K_{Y'})` and the square root
`O(-K_{Y'})` are fixed, that the branch divisor is smooth precisely off the discriminant, and that
the discriminant is a hypersurface, i.e. of real codimension 2.)

**(ii) Across quadrants (the repair of (C4)).**  Let `p' != p` be another `tau`-fixed point.  There
is an automorphism `sigma` of `Y` with `sigma(p') = p`, `sigma tau = tau sigma`, `sigma^* h_i = h_i`
(e.g. `x -> 1/x` on a factor; it commutes with `x -> -x` and preserves each ruling class).  `sigma`
acts on `|O(4,4)|^tau` (as `x^i y^j -> x^{4-i}y^{4-j}`, parity preserved) and maps `B_{p'}` to `B_p`;
the induced map of double covers is an isomorphism of families, and its cohomological shadow is an
isometry `gamma_sigma` with `gamma_sigma H = H`, `gamma_sigma alpha = alpha`,
`gamma_sigma I_dP = I_dP`, `gamma_sigma I_Co = I_Co` (the isomorphism of double covers is canonical up
to right multiplication by the deck involution `iota_dP`, which fixes `H`, `alpha` and both
involutions).  So (i) extends to all pairs of one-node members.

**Corollary B'.**  The five audited members lie in one connected family; after marking, their five
bullets-1,2,3,5 data `(I_Co, I_dP, H, alpha)` are conjugate in `O(L_K3)`.  Nothing about chambers is
asserted in this theorem.

---

## 5. The `H`-degree-1 census, exact

**Lemma 5.1' (completeness).**  Let `b` be a member with `a_20 a_02 != 0`.  If
`C in Pic(X_b)` has `C^2 = -2` and `C.H = 1` then `C` is effective and is a component of a reducible
fibre of one of the two ruling fibrations, away from that node's ruling.

*Proof.*  Effectiveness: Riemann-Roch on a K3 gives `chi(O(C)) = 1`, so `h^0(C) + h^0(-C) >= 1`; the
sign is decided by `C.H = 1 > 0` because `H` is nef.  Write `k = C.L_1 >= 0`, `m = C.L_2 >= 0`
(both nef), so `1 = k + m`; if `k = 0` then `C` is contracted by the `x`-fibration, hence lies in a
fibre, and it cannot be the whole fibre (`H.(fibre) = 2 > 1`); by Theorem A the node's ruling
contributes only degrees `0, 2`, so a degree-1 component comes from a reducible fibre over some other
`x_0`.  If `k = 1` then `m = 0` and `C -> P^1_x` is birational, `pi_*C = h_2`, so `C` is a component
of a fibre of the `y`-fibration over `y_0 != 0`.  `[]`

**Splitting criterion.**  For `x_0 != 0` the fibre `pi^{-1}(h_1)` is smooth and is reducible iff
`f(x_0,.)` is a scalar multiple of a square of a binary quadratic; then it is the union of two smooth
rational curves, each of `H`-degree `1` (each maps isomorphically to the ruling).

**Census.**  From the factorizations of §2 (a repeated root of the discriminant is necessary for a
non-reduced branch divisor, and a split fibre needs the branch divisor to be `2P+2Q` or `4P`, i.e. a
square, which forces the discriminant to vanish at least to order two, and on our members the
multiplicity-`>=2` factors are exactly the listed ones, at which the restriction was evaluated
explicitly):

    corpus member :  nu = 0
    m5 b_0        :  nu = 0
    m5 b_*        :  nu = 4    (x = 1 and x = -1, two components each)
    m6 B          :  nu = 4    (same two rulings)
    m8 F'         :  nu = 2    (the node's own ruling, type IV by Theorem A)

These are equalities, not bounds, and they agree with the Euler-characteristic bookkeeping of §2.  In
particular m5's `nu(b_*) >= 2` is sharpened to `= 4`, and m8's two degree-1 classes are the two
components of the type `IV` fibre.

**Remark (the `nu > 0` locus contains a divisor of the one-node locus).**  `a_02 = 0`, resp.
`a_20 = 0`, is one linear condition, so each tangency stratum is a divisor in the one-node locus, and
by Theorem A every member of it has `nu >= 2`; the codimension-two stratum `a_20 = a_02 = 0` is
nonempty too.  The member

    f = x y + x^2 y^2 + x^4 + y^4 + x^4 y^4

has `(a_20,a_11,a_02) = (0,1,0)`, `a_04 = a_40 = a_44 = 1`, singular locus exactly the node in all
four charts, `f(0,y) = y^4`, `f(x,0) = x^4`, and

    disc_y f = x^4 (x^4+1)(256x^16+384x^12+288x^8+113x^4-27),   disc_x f = the same in y,

so `4 + 4 + 16 = 24` and both node-ruling fibres are type `IV`: `nu = 4`.  It is in the certificate
log (`audit-witnesses-run.txt`, last block).  Consequence for the corpus's framing: "`nu = 0`" is a
condition on an open set (in fact on the complement of a divisor), not a generic accident, and the
members with extra `H`-degree-1 roots are dense in the one-node locus -- they are exactly the ones
with the node-ruling tangency, together with the bitangent ones.  Both of the obstruction's compared
members are on the complement of that divisor, which is what makes their comparison the sharp one.

---

## 6. What this certifies and what it does not

Certified here: the membership of all five members in the corpus's own sense, with exact arithmetic
(§2); Proposition 1.1 (the tuple's bullets 1,2,3,5 and `rk S_Co = 11`) from membership alone;
Theorem A and its corollary (the node-ruling dichotomy, and hence the corrected hypotheses of m5
Lemma 5.1 and m6 Lemma 1.2); Theorem B (one family, labelled transport, incl. the cross-quadrant
step); the exact census of §5.

**Not** certified here, and not to be cited as if it were:
* the chamber clause or its failure -- that is m5 `Thm 7.1`, whose *inputs* this audit repairs but
  whose isometry-theoretic step (facet normals, `|H`-degree census, the coset question of m6
  `sec 4.5`) is outside this direction;
* any statement about a very general member (`Pic = S_Co`, m8 `Lemma 4.4`), which is Baire-plus-period
  theory and is not verified by these examples;
* the identification of the construction's involution pair with the reflection twist, listed as
  unmet in `sm57_README.md`;
* any claim that the `I_2` / `IV` dichotomy is exhaustive for all one-node members: Theorem A treats
  the node's `x`-ruling; the `y`-ruling is the same statement with `a_20` for `a_02` (both rulings are
  covered by the two flags in the certificate), and the case `a_20 = a_02 = 0` (both rulings tangent,
  a codimension-2 stratum) is handled by applying the theorem twice -- it gives `nu >= 2` per ruling.
  Neither of the compared witnesses is on that stratum.

---

## 7. Hypothesis ledger

| premise | status |
|---|---|
| invariant system = 13 monomials, `i+j` even; no linear terms | `sec-invariant-system`, `lem:node-condition`; re-checked per member |
| node condition = `a_00 = 0` and `a_11^2-4a_20a_02 != 0` | `lem:node-condition`; satisfied by all five members (certificate) |
| no second node at a `tau`-fixed point (`a_04 a_40 a_44 != 0`) | verified for all five; gives `Fix(iota_Co) = D_b`, `rk S_Co = 11` |
| `H, alpha, L_i` flat, `I_dP, I_Co` defined on the family | Theorem B (i), proof given; the branch class and square root are fixed |
| cross-quadrant comparison | Theorem B (ii); uses the automorphism `x -> 1/x` of `Y` commuting with `tau` |
| `a_20 a_02 != 0` for the node-ruling fibre to be `I_2` | Theorem A: necessary and sufficient; `F'` violates it |
| splitting criterion (square binary quartic) | proved in §5 |
| exactness of `nu` | needs the discriminant multiplicities listed in §2 and the explicit evaluation of `f` on the multiplicity-`>=2` rulings; both in `audit-witnesses-run.txt` |
