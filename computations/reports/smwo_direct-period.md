# A20 direct period theorem for the one-node Coble construction: image and monodromy

Evidence register for the original A20 obligations `@prob:B24` and `@prob:B25`
(`writing/coble/heegner-report/coble-heegner-research-report.md` :1981-1989), from UltraMath run
`smw0o7jbf` (accepted solutions: **m2/d6, m1/d3, m3/d2, m4/d5, m5/d1, m6/d7, m7/d4**; **m8/d8
rejected** with three recorded gaps; referee records `REFEREE-verdict-m{1,..,8}.md` in the swarm's
directory hold the full audit trail; nothing in the repository was modified by the run).

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
- **Pass 1 (this pass).** Six further swarm solutions adjudicated (five accepted, one rejected).
  Three named defects of the first publication corrected: (i) Theorem C's blanket appeal to
  "rigidity of smooth rational surfaces" replaced by the arithmetic chain (unique degree-7
  del Pezzo + the degree-8 classification + the irreducibility exhaustion), per the operator note;
  (ii) (T-mixed) rewritten from its defective `L_K3 = (S_Co + T_Co)` form to the overlattice
  formulation with the complete half-class census, and sharpened to a discriminant-form question
  about the pinned glue; (iii) Theorem A's side-effect statement and cross-check 2 reworded to the
  correct directionality (ampleness excludes pure roots trivially; the converse is conditional on
  exactly those mixed classes). Theorem E is demoted per the referee verdicts: `deck = G1` is
  proved at the covering content, `G2 = Gamma^dir` is **not** asserted, and the two missing
  statements are named. Theorem D is strengthened to the full equality `im(p) = O/Gamma_L`.
  One further correction adjudicated: m8's claimed contradiction against corpus item 3 was
  rejected (fixed-norm walls are locally finite, never dense), so the corpus's standing inputs
  :659-:661 stand as published.

## Theorems, at their registered scopes

**Lemma 1.** `I_dP = -1` on `T_Co`. (Joint character ranks of `<I_Co, I_dP>` are `(3, 8, 0, 11)`
with `rk S_dP = 3`, so the `(-,+)`-eigenspace vanishes and `T_Co` is the `(-,-)`-eigenspace.)

**Theorem A (the arrangement is excluded pointwise, not just generically; three independent
proofs accepted).** No member of the direct one-node construction carries an algebraic class of
`square >= -2` in `NS(X_b) cap (T_Co tensor Q)`. Proofs accepted: (i) Riemann-Roch supplies one
sign-effective class; `A = 2H - alpha` is ample on every member and `A perp T_Co` (m6 Theorem 2 +
Remark 2.4, strongest form, covering rational classes); (ii) RR + `I_dP`-inversion (m2/m1 Theorem
5.0a: the geometric `iota_dP` inverts the class by Lemma 1, so both signs would be effective,
meeting an ample class with opposite sign); (iii) the fibre lemma (m5 Lemma 1, m8 Theorem A first
form: an `H`-null effective class is a union of `H`-trivial curves, the only one is the exceptional
curve `alpha`, and `alpha not in T_Co`). **Consequence.** Every marked period of a member lies in
`D_Co^o := D(T_Co) \ cup_{delta in T_Co, delta^2 = -2} delta^perp`, an explicit arrangement
complement of the Coble period domain, pointwise and for every subgroup `Gamma <= O(T_Co)` (m6
Corollary 2.1: the exclusion is group-independent — but note it strikes the *pure* `T_Co` roots
only, cf. (T-mixed) below). Three notes on its scope.
- The **side-effect** claim of the first publication is reworded to its correct direction: at a
  member, ampleness of `A` is proved directly (Nakai on the blown-up model, corpus Lemma 2.2), and
  Theorem A is then the *trivial* direction of the ampleness-versus-arrangement interaction
  (`A` ample, `A perp delta`, RR, so no effective pure-root class exists). The converse —
  "no `A`-null algebraic root implies `A` ample" — is *conditional*: it holds for pure classes
  (`S_Co` has no `A`-null root at all, m4's Lemma C1; a pure `T_Co` root is killed pointwise) and
  fails exactly through the mixed glue classes `(F2),(F3)` of (T-mixed), whose status is open.
- The arrangement itself, computed exactly (m6 Lemma 1.2): `delta^perp cap D(T)` is nonempty iff
  `delta^2 < 0`, so the only walls of norm `-2` are the root classes; norm-`0` and positive classes
  cut nothing.
- The excluded set is *exactly* the norm-`(-2)` arrangement, at the `(-2)` level: m6's Corollary 2.2
  exhibits the corpus's special member `F'` with the anti-invariant class `[C1 - C2] in T_Co` of
  square `-6` (verified against `sm57_verify_special_member.log`), so the image *meets* the
  `(-6)`-Heegner locus — no larger stratum is excluded by the construction's data.

**Theorem B (the second slot is realized geometrically at the chamber hypothesis).** At every marked
Coble period `q` at which `2H-alpha` is a Kahler class — the chamber datum `c` and nothing else —
both `I_Co` and `I_dP` are Hodge isometries of the marked structure that fix `2H-alpha`, and are
therefore induced by commuting automorphisms `iota_Co, iota_dP` of `X_q` (effectivity via the
fixed-Kahler-class condition and the chamber arrangement of the positive cone; global Torelli as in
Peters §1.8, equivalent to BHPV VIII). The earlier publication's flagged input `(R)` is replaced by
the m1-anchored theorem: PSS surjectivity for `N = S_Co` lattice-polarized realizations is verified
verbatim at `huybrechts_k3_lectures.md` :9480; the automorphism part of global Torelli is verified
at :10227-:10240 (Corollary 2.3); openness of ampleness is :5167 (Proposition 5.6); see also the
cover step below.

**Theorem C (the quotient reconstruction is arithmetic, not "rigid").** Under the hypotheses of
Theorem B the resolved quotient `Y° = X/iota_dP` and its descendant `Y` satisfy, step by step:

1. `Y°` is smooth rational, `b_2 = 3`, `K^2 = 7` (`chi(Fix iota_dP) = 2 rk S_dP - 22 = -16`, so the
   branch curve `B°` has `chi = -14`, hence `(B°)^2 = 28 = 4K^2`); `B° in |-2K_{Y°}|` is smooth of
   genus `8`. `e' = pi(alpha)` is a `(-1)`-curve with `e'.B° = 2` (transverse), and
   `S_dP = pi^*H^2(Y°)` gives the form `U perp <-1>` on `Pic(Y°)`.
2. Contracting `e'` yields `Y` rational with `b_2 = 2`, `K^2 = 8`, `Pic(Y) = U`, and a nef class
   `h'` of square `2` (`h'^2 = H^2/2`). The alternatives are disposed of by arithmetic, not
   rigidity: the non-minimal (odd Picard) case forces `a^2 - b^2 = 2`, which has no integral
   solution (a difference of two squares is `0, ±1 mod 4`); the `F_2` case admits `h' = C_0 + 2f`
   arithmetically and is excluded by ampleness of `A` itself
   (`A.delta <= 0` against its effective class; m6 Lemma 5.3); the remaining minimal case is
   `F_0 = P1 x P1` with `h' = O(1,1)` up to automorphism. So `Y° is Bl_q(P1 x P1) = Bl_{p1,p2}(P²)`
   — the *unique* isomorphism type of a del Pezzo surface of degree `7` (Demazure, *Surfaces de Del
   Pezzo II - Eclater n points dans P²*, Seminaire sur les singularites des surfaces 1976-1977,
   exposé 4, LNM 777 (1980), Théorème 1 on the classification; degree-7 case; in degree 8 the two
   types `P1 x P1` and `Bl_{pt} P²` are further distinguished by the arithmetic above). No
   constancy/rigidity argument for smooth rational surfaces is used anywhere.
3. `B = beta_*(B°) in |-2K_Y| = O(4,4)`: `p_a(B) = 1 + (B^2 + B.K)/2 = 9`, `chi(B°) = -14`, hence
   `g(B~) = 8` and the number of double points is `delta = 1`. Writing `B = sum_i B_i` of
   bidegrees `(a_i, b_i)` with `sum a_i = sum b_i = 4`: `sum a_ib_i = 15 + sum delta_i <=
   (sum a_i)(sum b_i) = 16`, equality forcing a single component and `sum delta_i = 1` — so `B` is
   irreducible with exactly one ordinary double point, an `A_1` node since its resolution is one
   `(-2)`-curve (m1 Step 6; m7 §3.2(6) independently: `B_1.B_2 = 4a + 4b - 2ab >= 4` against a node
   contributing `2`).
4. `iota_Co` descends to an involution `tau` of `Y` preserving both rulings (it fixes `e, f`),
   preserving `B`, and fixing the node `q` (it preserves the `A_1` point over it); its fixed locus is
   finite (else the symplectic product `iota_Co iota_dP` would fix a curve), hence `tau` is of
   product type with exactly four fixed points — the standard model up to `Aut(Y)`.

So irreducibility, the single node, its `tau`-fixedness, product type, and `H = pi^*O(1,1)` are all
*recovered* from the chamber hypotheses plus arithmetic, at every period where Theorem B applies.

**Theorem D (the image, at the original quantifiers; strengthened to the full equality).** Let

`O := {sigma in D(T_Co) : exists a marked pair (X, psi) at sigma with psi(S_Co) subset NS(X) and
psi(2H-alpha) ample}`.

Then, in the component of `D(T_Co)` containing the periods of members, with `p` the marked period
map of the direct one-node construction into `D_Co = D(T_Co)/Gamma_L`,

> `im(p) = O / Gamma_L`

exactly (m7, as repaired in `REFEREE-verdict-m7.md`; m6's Theorem 5 independently at the same
statement with its supplies recorded; m1's Theorem 4.2 on the generic stratum by a third
mechanism). No dominance-to-surjectivity inference enters: the lower inclusion is a member-by-member
reconstruction `( redundantly: the two pencils give the quadric cover, the crepancy gives
bidegree (4,4), the single contracted curve gives the single node, the intersection bound
`B_1.B_2 >= 4` gives irreducibility, and the fixed-locus analysis gives `tau`).

The three markers of B24, at their now-proved content:

- **The arrangement** `{delta^perp : delta in T_Co, delta^2 = -2} = NL_2(T_Co)` is excluded
  pointwise (Theorem A). The *complete* wall list of `O` is this arrangement **plus the mixed glue
  walls `(F2),(F3)` of (T-mixed), if the pinned glue carries them** (m7 §4, m3's Corollary A1; the
  `(F4),(F5)` candidates are killed unconditionally, and `(F1)` collapses to a pure root; see
  (T-mixed) below). Hence `O = D(T_Co) \ [NL_2 U (F2),(F3)- glued walls]`, and the verbatim
  arrangement complement `D_Co^o = D \ NL_2` stands iff that residual census is empty.
- **The chamber** is the single labelled condition "`2H-alpha` ample": `A` lies on the Kahler side
  of the positive cone on the whole component (m5 Theorem 4: the sign of `A.omega` is a locally
  constant, label-invariant function of the period, and it is `+` at members); `S_Co` carries no
  `A`-null root (m4 Lemma C1), so `A` lies in the interior of a genuine chamber of the
  `S_Co`-arrangement; and the frame inequality `e.delta >= 0, f.delta >= 0` for every effective
  root holds at *every* `sigma in O` (m7 Lemma 4b, as repaired in the referee record from its
  circular written form), so no separate chamber wall needs to be excluded.
- **The exceptional root** `alpha` is a *function* of the labelled data, not a label: the unique
  `(-2)`-class of `S_Co` with `H.alpha = 0` and `A.alpha > 0` (m4 Lemma C1(b)); `alpha` effective as
  soon as `A` ample (RR: `chi(alpha) = 1` and `A.alpha = 2 > 0`); the only effective `H`-null
  `(-2)`-class at any `sigma in O` (m7 Lemma 4), so the one-node/irreducibility/`tau`-fixedness
  clauses of the retained construction are automatic on `O`.

Settled density point (adjudicated, against m8's rejected claim): `O` is analytically open
(relative ampleness, :5167) and contains the corpus's nonempty Zariski-open subset of
`D_Co^o/Gamma_L` (corpus item 3); and `D_Co^o/Gamma_L` is itself Zariski-open in `D/Gamma_L`
(the wall image is one Heegner divisor — finitely many orbits of roots of fixed norm, standard
finiteness of norm-orbits in indefinite 2-elementary lattices — hence algebraic by Baily-Borel on
the arithmetic quotient). Item 3's standing statement therefore stands, with the m6-Remark-4.0
reading (the Zariski-open it claims lies inside the arrangement complement where the image lives).

**Theorem (residual, rewritten: (T-mixed) as a discriminant-form question).** With
`S_Co = U(2) perp E8(-2) perp <-2>` and `T_Co = <2> perp U(2) perp E8(-2)`, `L_K3 supset S_Co
perp T_Co` of index `2^11` with the full-graph glue `A_{S_Co} =~ A_{T_Co}(-1)`, every mixed class is
`x = (s+t)/2`, `s in S_Co`, `t in T_Co`, `t != 0`, `x^2 = -2` iff `s^2 + t^2 = -8`. The complete
census (m7 Lemma 3, matching m3's Corollary A1 independently):

| family | `s` | `s^2` | `t^2` | `A.x` | status |
|---|---|---|---|---|---|
| (F1) | `0` | `0` | `-8` | `0` | collapses: `x = t/2 in T` forced by the glue, i.e. a pure root |
| (F2) | `e - f` | `-4` | `-4` | `0` | **live** |
| (F3) | `w in E8(2)`, `w^2 = -4` | `-4` | `-4` | `0` | **live** |
| (F4) | `±alpha` | `-2` | `-6` | `±1` | killed: effective representative would meet `E` negatively |
| (F5) | `w ± alpha` / `(e-f) ± alpha` | `-6` | `-2` | `±1` | killed: its `t` is already a pure root |

So the residual to B24-verbatim is exactly:

> **(T-mixed).** Does the pinned Coble glue (the specific full-graph anti-isometry of the labelled
> construction, itself recorded as an open datum at report :661 item 7) contain a class of type
> (F2) or (F3) — equivalently, does its glue map pair the class of `(e-f)/2`, or of `w/2` for a
> `(-4)`-root `w`, to a `T_Co`-discriminant class having a representative of norm `-4`?

If the answer is *no*, B24 holds verbatim with `D_Co^o = D(T_Co) \ NL_2`, because then `O =
D_Co^o`; if *yes*, the image is the complement of those Heegner divisors (of `T_Co`, norms `-4`),
with the same chamber and root content. The brick probe
`computations/reports/coble_mixed_gluing_probe.py` (+`-run.txt`) builds `L = U^3 + E8(-1)^2`
blockwise, embeds `S_Co` and `T_Co` as the maintained `L.glue_map`-verifiable diagonal/anti-diagonal
pair (both embeddings `is_isometric_to` the corpus's models by the maintained predicate, glue order
`2^11`), and exhibits in *that* glue two `x` with `x^2 = -2`, `H.x = 0`, `A.x = 0` and both
projections nonzero (`x = e_a - f_a`, `x = e_b - f_b`): so the "no" branch is not automatic —
whether it holds is genuinely a property of the pinned Coble glue, exactly as the (T-mixed)
statement says. The probe is exploratory with respect to B24 (the brick glue is not claimed to be
the Coble glue); its arithmetic is exact and its constructions maintained.

**Theorem E (B25, at its proved content; demoted from the first publication's naming).**

1. **Deck = monodromy image.** The marking cover of the direct one-node stack is the cover
   trivialising the labelled local system `R^2 f_* Z`; it is attached to the monodromy kernel, hence
   normal with deck group equal to the monodromy image `G1` on `T_Co` (m1 Theorem 6.2; m4's
   normalizer-quotient statement for the general possibly-non-Galois phrasing is consistent — the
   labelled-trivialising cover is normal by construction). The mark-cover of periods
   `O -> O/Gamma_L` has deck `Gamma_L/(Gamma_L cap {±1})` (m7 §5(a)).
2. **Inclusions proved.** `G1 subseteq Gamma_L = G5` (flatness of the four labels in the family;
   m4's Proposition D2, m7 §5(b)), and `G1 subseteq Gamma^dir_{Co,2} = G2` when the marking datum
   carries the chamber (the monodromy preserves `A = 2H-alpha` and the ample cone; m7 §5).
3. **Computed generators.** `G1` contains `W_node = <w_delta, (w_s, w_e)>`: the
   Picard-Lefschetz reflections with `delta in T_Co`, `delta^2 = -2`, of the
   second-`tau`-fixed-point wall `Z_q`, and the nodal-pair transformations with
   `s = delta + delta' in S_Co`, `e = delta - delta' in T_Co`, `s^2 = e^2 = -4` (m5 Theorem 3 and
   §6.1; verified symbolically). Note these monodromies live at *boundary* degenerations — never at
   members — which is precisely compatible with Theorem A (the wrong claim that they cannot exist is
   m8's rejected Gap 3). Separately, the node degeneration's own vanishing class is `±alpha`, and
   `w_alpha|_{T_Co} = id`: `alpha` contributes nothing to `G1` (m3 §6.2, m7 §5, consistent).
4. **The two missing statements (named, replacing the first publication's group naming).**
   (D1) *monodromy-maximality*: the family's discriminant meets every `Gamma^dir`-orbit of walls
   (so `G1` reaches the whole reflection subgroup; dynamical, not a period statement);
   (D2) *generation*: `Gamma^dir_{Co,2}` is generated by those wall reflections together with the
   discriminant-automorphism image of `O(T_Co)` (a 2-elementary overlattice statement of exactly
   the kind `coble_labeled_embedding-run.txt` §3.3-3.4 records as owner-undecided for `T_Co`).
   Until both hold, `G1 = G2` is open; `Gamma^dir = Gamma_L` is separately open (it would need the
   chamber datum determined by `(H, alpha)`, via `@lem:face-at-H` and `@prop:chamber-conditional`,
   and is *not* decided here or in the run); `G3, G4` are untouched; `@prob:group-identification`
   stands unchanged with no equality by notation.

## Premise ledger (inputs and their tiers)

| # | input | tier |
|---|---|---|
| 1 | `@def:direct-cover-datum` with the one-node refinement; involutions and labelled classes | corpus definitions (:853-932) |
| 2 | Explicit member with no other singularity, from `@sec-explicit-curve` (:2425-2445) plus its own verification contract | corpus |
| 3 | Lattice labels (`S_Co, T_Co, S_dP = Lambda`, ranks `(3,8,0,11)`, index `2^11`, full-graph glue); `formalization/coble-enriques/A21Arithmetic.lean` at its file's own scope | corpus theorems + machine verification at its scope |
| 4 | `D(T_Co)` dimension 9; `Gamma_L`; Zariski-open image of the family's period map; fibres; Borel extension (J. Differential Geom. 6 (1972) 543-560, hypotheses as cited at :661) | corpus item 3; m6's Remark 4.0 reading of the Zariski-open clause |
| 5 | Global Torelli and its effectivity criterion; automorphism part (Huyb. Cor. 2.3, :10227-:10240); polarized pairs (Huyb. Thm 3.4, :3536-:3548); Peters §1.8; BHPV VIII | primary statement-level, anchors verified verbatim |
| 6 | Riemann-Roch for `(-2)`-classes; Lefschetz for nonsymplectic involutions; quotient smoothness at fixed curves; Nikulin's fixed-locus classification for the one-node `(r,a,delta) = (11,11,1)` involution; del Pezzo classification at degrees 7-8 (Demazure, LNM 777, exposé 4, Théorème 1); Saint-Donat bpf pencils (:1027); Nakai on rational curves (:737) | standard / primary statement-level, anchors verified verbatim |
| 7 | Surjectivity of the lattice-polarized period map (PSS/Todorov; Huyb. :9480 verified verbatim) | primary statement-level, anchor verified verbatim |
| 8 | `2H-alpha` ample on every member; `E^2 = -2`, `H.E = 0` | corpus lemmas 1.3, 2.2 of `sm00_positive-half-A21.md` |
| 9 | Swarm-accepted intermediate theorems (m2's Lemma and exclusion; m1's cover step; m7's census and frame repair; m5's monodromy generators and sign constancy; m6's arrangement computation and audit) | referee-accepted with records (`REFEREE-verdict-m*.md`) |
| 10 | `L = U^3 + E8(-1)^2` ambient; maintained `primitive_sublattice_from`, `orthogonal_complement`, `is_isometric_to`, `glue_map`; glue order `2^11`; mixed witnesses `x = e_a - f_a`, `x = e_b - f_b` | maintained construction (`coble_mixed_gluing_probe.py`); exploratory with respect to B24 |

Computation used is hand-carried exact arithmetic small enough to check line by line (the
`A^2 = 14`, `A.alpha = 2`, `(2H-alpha)^perp cap S_Co` emptiness of roots, the census table, the
genus/chi bookkeeping, `a^2 - b^2 = 2`'s insolubility, the `Sigma a_i b_i <= 16` bound); the
corpus's machine-verified tiers are cited, not re-run; the brick probe's witnesses are printed and
hand-checkable in the probe's run file.

## Falsifiable cross-checks carried by the theorems

1. **No `T_Co`-curve of square >= -2 on a member** (Theorem A): the register
   `computations/reports/sm57_README.md`'s `F'` extra classes must be read against this; the
   consistent reading is the one m6's audit C3 supplies: `[C1+C2]` invariant of square `-2`,
   `[C1-C2]` anti-invariant of square `-6`, the latter in `T_Co` exactly as the (R2)-clause admits.
2. **Ampleness-versus-arrangement at the wall** (Theorem A's note): the image is contained in the
   arrangement complement because members are ample (trivial direction); the *converse* — a period
   off the walls being a member — is Theorem D's content and passes through the O-locus and its
   census, never through "ample on every member" read backwards.
3. **Fixed-locus bookkeeping** (Theorem C1's footnote): `e(Fix) = 2(2+k) - 20`, the two conic
   points, and the one blow-up per node make `rk S_dP = 2+k` consistent with `e(Fix)`; consistency
   was falsely reported elsewhere in aid of the same proposition.
4. **Density**: the `(-2)`-walls are locally finite (Hodge-form bound), so the corpus's
   open-image statement is consistent with the pointwise exclusion; a density claim for a
   fixed-norm arrangement is the rejected form (m8's Gap 1), and the form over *all* norms is true
   but irrelevant here.

## What remains open next (named, not cosmetic)

* `(T-mixed)` — the discriminant-form question of the residual theorem, deciding between the two
  branches of B24; attackable by computing the pinned glue's action on the classes of
  `(e-f)/2` and `w/2`, exactly as in the probe's maintained machinery, and it is *the* next
  arithmetic move of this project.
* `(D1)` and `(D2)` of Theorem E — the monodromy-maximality and generation content of B25's
  remaining equality; the computed `W_node <= G1` and the wall structures are on record.
* `Gamma^dir = Gamma_L` — the chamber-datum identification, via `@lem:face-at-H` and
  `@prop:chamber-conditional`; a separate theorem, unsettled.
* `@prob:group-identification` among the four — untouched except `G1`'s proved content.
* Construction-vs-construction chamber comparisons at rank `>= 12` with unmatched extra classes —
  the A21-side S5' leftover, beyond this dossier's scope.
* The R4 recovery question, the (O1)/(O2) non-2-elementary decomposition, the `k >= 2` saturation,
  and the four downstream dep-audit citation sites of `computations/reports/sm57_depaudit-ledger.tsv`
  (three unsatisfiable as worded, det 1024 vs 2048) — untouched.
