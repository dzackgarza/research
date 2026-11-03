# The member/period input (M1) and the chamber bridge of A21: full proof dossier

Corpus evidence-state `main@556455ee` (this document supersedes prose of `smwg_operator-extension.md`
§7.1, which said the twist side "currently has no member/period": that sentence described the original
*text*; this dossier is the mathematics of the same point). Convergent verification: UltraMath run
`smw0kq02h`, accepted solutions m8 (period-blindness), m1 (root-sign blindness + the d5 theorems),
m4 (AEGS closure + realization via Torelli), m6 (parity/Heegner mechanism), m2 (node adjunction),
m7 (deformation smoothness); referee scope corrections are folded in and marked where they bind.
**Review corrections applied after the first publication of this dossier:** (§2) the ampleness
criterion decomposed into (C1) component and (C2) no-null-root, with the locus re-derived as the
construction-bearing component of the wall complement — absence of an orthogonal root alone no
longer stands as an ampleness proof; (S1) the implication chain set out with no unconditional
arrow from `(Hdg)` and the wall-reflection counterexample pinned; (S4) `nu(b0) = 0` explicitly no
longer implies a Picard rank for the certified member (kept open until a Picard computation
supplies one); (§6.1) `Gamma_L`-orbit membership no longer said to *decide* the original chamber
question (sufficiency only); (E2(i)) the product involution's `+1` character separated from the
two `−1` ones.
Tier discipline as in `smwg_operator-extension.md`: every numbered theorem here is proved from the
premises of its own ledger row; member scripts (`twist_wall_check.py`, `twist_lattice_checks.py`,
`m6_parity_probe.sage`, `coble_twist_base_pair.py`, `verify_period_locus.py`, `m8_eigenspaces.py`)
are **exploratory** and validate nothing; the original chamber quantifier — *some* label-carrying
isometry carries the chamber, not every — is preserved verbatim throughout, as is the certified
pair's scope (Theorem 9 of `sm00_chamber-negative-half.md` in readings R2–R5, and Theorem A2 of
`.ultramath/smw0gfl0i/m4/chamber-prioritized.md`).

## 0. The results, in dependency order

* **Existence (Q1, Theorems E1-E3).** The authored single involution `I_Co := w_alpha o I_En`
  (@cons:reflection-twist, report :535) has a genuine realization: the decorated moduli of marked
  K3s with a nonsymplectic involution of its type is **smooth of complex dimension 9** with
  vanishing obstruction space, nonempty (every one-node member lies in it), and equal to the
  amplitude condition's open locus of §2. The corpus's reflected *pair* is realized by commuting
  geometric automorphisms on the same locus; its factorization is never geometric there; the
  authored companion `I_En` fails the construction's joint multiplicities; the second slot costs a
  chamber condition.
* **Determination (M1 proper, Theorem D2).** This existence result is a **moduli, not a member**:
  the original data select no period, and the chamber clause has no truth value on the original
  data — *proved* as non-determination inside the same realization space, which carries both
  verdicts (the certified pair `b0, b_star` supplies them).
* **Bridge (Q2, Theorem B + Separations S1-S4).** `(Hdg) + (M2) + (M3) ⇒ (Chm) ⇒ (Lat)` is the
  sufficient chain with its exact hypotheses; necessity of the Hodge/orbit condition is not proved
  and cannot hold in general (generic-pairs phenomenon, S2); `(Lat)` is strictly weakest (S3);
  one unconditional lattice-level exclusion survives (S4).
* **Adjunction (Theorem E3).** The reflection's whole algebraic content is the adjunction of one
  root: rootless base pair (AEGS, `(2,8,0,12)`) to rooted pair (one-node, `(3,8,0,11)`). This is
  an algebraic mechanism on eigenlattices and is **not** a geometric degeneration construction.

## 1. Sources, in verified form

* **S1 (maintained, pin `c546077d`).** `coble_reflected_pair(-run).txt`;
  `coble_joint_flag_premises(-run).txt` (both reflected involutions fix `H` and `alpha`; integral
  `(++)`-membership coordinates `[0,1,1]`, `[1,0,0]`; types by `is_isometric_to`);
  `coble_aegs_involutions(-run).txt`; `sm00_census_hdegree.py` (13/13, re-run recorded in
  `.ultramath/smw0gfl0i/m4/census-rerun-run.txt`).
* **S2 (in-repo primary copies, anchors checked this session).**
  `references/literature/lattice-research/nikulin1979integral.md` (3.6.2 classification :1577 and
  3.6.3 surjectivity :1595, verbatim with proofs, as used in `smwg_operator-extension.md`);
  `references/literature/lattice-research/aegs_2023.md` (main diagram :63; three involutions on the
  surface and on `L` :128; `[Nam85, 2.13]`-uniqueness of the root and
  `Delta = alpha^perp subset D(T_En)/Gamma_En` discriminant divisor :182);
  `references/literature/lattice-research/huybrechts_k3_lectures.md` (effective-Torelli and Weyl
  chamber content, cited at topic/chapter level; its `Amp(X)` is one chamber of the positive
  cone, and a Hodge isometry preserving a Kähler class is effective).
* **S3 (standard references, cited at corpus level).** BHPV VIII.3.11 (Hodge isometry carrying one
  Kähler class into the cone is effective) and VIII.11.1 (isomorphism part), exactly as used in
  `sm00_positive-half-A21.md` Remark 6.7 with the same ample class `2H − alpha`; Nikulin [Ni1]
  Thm. 4.7 for the symplectic-involution uniqueness (via van Geemen–Sarti §§1.1-1.3,
  arXiv:math/0602015, fetched and quoted in `smwg_operator-extension.md` §1 N4).
* **S4 (corpus theorems, used at their stated scope).** `smwg_operator-extension.md` Theorems A, B
  (labelled extension [EXT], uniformly for every irreducible one-nodal `b`);
  `prop:det-saturation-del-pezzo`; `smtw_ot_types-m8.md` Theorem 3.1;
  `sm00_positive-half-A21.md` Lemma 1.3 (numerical facts), Lemma 2.1(3) (`D = pihat^*e`,
  `D^2 = -2`, `alpha = pihat^*[e]`), Lemma 2.2 (`H_b − t alpha_b` ample for `0 < t < 1`,
  `2H_b − alpha_b` integral and ample), Theorem D (generic `Pic = S_Co`);
  `prop:one-node-family` (nonempty locus); `prop:coble-eigenspaces`;
  `prop:chamber-conditional` (the transport-vs-target chamber criterion);
  `prop:tuple-of-the-construction`; Theorem 9 and its readings (`sm00_chamber-negative-half.md`);
  Theorems A2/B of the chamber framing (accepted).
* **S5 (standard deformation theory / Hodge theory, proved in place where stated).**
  Decorated deformation smoothness (Theorem E1's Lemma D1-D2); Riemann–Roch for line bundles on a
  K3; the `Aut(X) -> O(H^2(X,Z))` injectivity; Local Torelli; the characterization of the ample
  cone by `{x : x^2 > 0, x·C > 0}` for effective curves `C`.

## 2. The realization locus, with its exact hypotheses and topology

Put `A := 2H − alpha` (`A² = 14`, `A.H = 8`, `A.alpha = 2`).

**The ampleness criterion used everywhere below (named, not smuggled).** For a projective K3
surface `X`, the ample cone is

`Amp(X) = { x in C_X^+ : x·delta > 0 for every effective (−2)-class delta of X }`,

where `C_X^+` is the component of `{x ∈ NS_R(X) : x² > 0}` (signature (1,·)) containing Kähler
classes (Huybrechts, Lectures on K3 Surfaces, §2 of the chapters on the Torelli/cone side, in-repo
`references/literature/lattice-research/huybrechts_k3_lectures.md` at topic level; BHPV Ch. VIII at
corpus level). Hence ampleness of the fixed integral class `A` is the conjunction of:

* **(C1) the chamber/component condition:** `A ∈ C_X^+` — equivalently `A·kappa > 0` for some
  (hence every) Kähler class kappa. It fails exactly when `A` sits in the wrong component of the
  positive cone, never at a wall;
* **(C2) the no-null-effective-root condition:** `A·delta ≠ 0` for every effective `(−2)`-class
  `delta` — equivalently, no effective `(−2)`-class is orthogonal to `A`. With `(C1)` the signs then
  come out `> 0` automatically inside a chamber.

For a marked pair `(X, psi)` with `psi(H^{2,0}(X)) ⊆ T_Co ⊗ C` (i.e. `sigma in D(T_Co)`) every
class of `S_Co`, hence `A`, is algebraic on `X` (pairwise orthogonal to `sigma`). The realization
locus of this dossier is **defined as**

`U := { sigma in D(T_Co) : A in Amp(X_sigma) }`
     = (the connected component, in the analytic topology, of
        `D(T_Co) \ cup_{delta}` (`delta^perp ∩ D(T_Co)`), over `(−2)`-classes `delta` with
        `A·delta = 0`,
        that contains the construction members).

**Lemma (properties of `U`).**

1. *The failure set is a wall union.* If `A·delta = 0` with `delta² = -2` algebraic at `sigma`,
   then one of `±delta` is effective (Riemann–Roch) and pairs `0` with `A`, violating (C2): the
   failure set is therefore **contained in** the countable, locally finite union of closed analytic
   hyperplane sections `delta^perp ∩ D(T_Co)` with `A·delta = 0`. Deleting it leaves an
   **analytic-open** subset.
2. *Every point of `U` satisfies (C1) and (C2).* (C2) holds by the deletion just made (within a
   region bounded by walls, algebraicity of each `(−2)`-class is constant, so the sign of
   `A·delta` for effective `delta` is constant). (C1) holds on the named component: at the
   construction members `A` is ample by Lemma 2.2 of `sm00_positive-half-A21.md`, and the sign of
   `A·kappa` against a Kähler class is continuous along the connected locus.
3. *`U` is nonempty and 9-dimensional*: it contains `sigma_b` for every one-node member `b`
   (Lemma 2.2), hence a nonempty open subset of the image of the construction's period map; its
   dimension is `11 − 2 = 9`.
4. *The two chapters, kept straight.* (i) ampleness of `A` is a property of **the marked member**
   (its null-root arrangement and positive component), never of a bare point; (ii) nevertheless
   `sigma` decides *which `(−2)`-classes are algebraic* and hence where the walls are, so the
   membership of the locus above is decidable at period level through (C1)+(C2). These are the only
   two chapters of the condition; **absence of an algebraic `(−2)`-class orthogonal to `A` is not,
   by itself, a proof of ampleness** — (C1) is the other half, and it is earned on the connected
   component containing the construction members, not asserted everywhere in `D(T_Co)`.
5. *Elevation warning, kept separate:* `Pic(X_sigma) = psi^{-1}(S_Co)` holds on `D(T_Co)` minus a
   countable union of Noether–Lefschetz divisors. That set is dense and Baire-general; it is
   **not** Zariski-open, and no argument in this dossier uses an open-set form of it (cf. also S4,
   which is a pointwise parity argument, not a locus argument).

## 3. Part 1 — existence (Q1), in three theorems

**Theorem E1 (the authored single operator: smooth, nonempty, 9-dimensional realization space).**
Let `U_d` be the set of marked K3 surfaces `(X, psi)` carrying the authored involution (of type
`S_Co = U(2) ⊕ E8(2) ⊕ ⟨-2⟩` invariant, `T_Co` coinvariant) with `A` ample. Then `U_d` is a
nonempty open subset of a **smooth 9-dimensional** decorated moduli space: (i) pairs `(X, iota)`
deform with tangent space `H^1(X, T_X)^iota` and obstruction space `H^2(X, T_X)^iota`; for a K3,
`T_X ≅ Omega^1` and `H^2(X, T_X) = H^{2,1} = 0` (S5), so the functor is smooth; (ii) for a
nonsymplectic involution the canonical `T_X -> Omega^1` contraction by the 2-form picks up a sign
(`iota^* omega = -omega`), giving `dim H^1(T_X)^iota = rank T_Co - 2 = 11 - 2 = 9`; (iii) nonempty
by item 2 of §2. So `D(T_Co)` is the period domain of the *authored operator alone*, and the
twist datum's realizations form a free-parameter, unobstructed 9-dimensional family. (A check on
fixed loci accompanies this: the author-recorded rank formula `rk S = 2 + k` belongs to the
*resolved* model with the branch normalization of geometric genus `9 − k`; at `k = 1` that is
genus 8 and `χ(Fix) = -14` — not a smooth genus-9 value. It is used nowhere below.)
*(m7's Lemmas 1-2, Theorem 1.)*

**Theorem E2 (the pair realization and its exclusions).**
(i) On any member of `U` (§2), the reflected operators `J_Co = w_alpha I_En` and
`J_dP = w_alpha I_dP` are Hodge isometries — _each acts as `-1` on `T_Co ⊗ C`_ — and they fix `A`
(they fix `H` and `alpha`); their product `I_nik = J_Co J_dP` acts as `+1` on `T_Co ⊗ C` (hence
fixes the period `sigma`), so its character on `H^{2,0}` is `(−1,−1,+1)`, and the product is the
symplectic involution of Nikulin type (its coinvariant is the `(+-)`-piece `E8(-2)`; uniqueness
[Ni1] Thm. 4.7 via S3). Every class they fix includes the integral ample class `A`, so by
effective Torelli (S3) **all three are induced by commuting automorphisms**, all five authored
bullets then hold, and their realization is the whole locus `U`.
(ii) *The factorization is never geometric anywhere the fourth bullet holds:* on a member with `A`
ample and `alpha` effective, `w_alpha`, `I_En`, `I_dP` each send `A` to
`2H + alpha`, and `(2H + alpha)·alpha = -2 < 0`; an automorphism preserves the effective cone, so
none of the three is induced. In particular `w_alpha` is a wall reflection (a flop), never an
automorphism — whence the AEGS-route closure: on a very general AEGS cover, `w_alpha I_En` is not even
a Hodge isometry — and at its algebraic locus `Delta = alpha^perp` it is a wall crossing, not a
symmetry (S2's AEGS anchors :63, :128, :182).
(iii) *The authored companion is excluded arithmetically:* the joint character multiplicities of
`(I_Co, I_En)` are `(10,1,0,11)` while the construction tuples have `(3,8,0,11)` ([EXT] and
maintained run); a conjugacy preserves joint multiplicities, so `(I_Co, I_En)` is conjugate to no
construction tuple. Among the AEGS operators, only `J_dP = w_alpha I_dP` satisfies the tuple's
requirements (commuting, nonsymplectic, geometric on `U`, symplectic product, matching
multiplicities) at once. This excludes the base companion and admits the reflected one — it
manufactures nothing and hides no rank-match step.
(iv) *The second slot costs a chamber condition, not a period one:* `J_dP` is a Hodge isometry for
every period in `D(T_Co)` (since `T_Co ⊂ T_dP`), so it adds no period constraint. But it acts as
`−1` on `E8(-2) ⊂ S_Co ⊂ Pic`, and realization is `J_dP(K_X) = K_X`: not automatic. Witness that
it is not automatic: for a `J_dP`-invariant chamber `c` and a `(−2)`-class
`delta = e + f + v + alpha` (`v in E8(-2)`, `v² = -4`, so `delta² = -2`) one has
`J_dP(delta) = delta - 2v ≠ ±delta`, and `J_dP(w_delta(c)) = w_{J_dP delta}(c) ≠ w_delta(c)` —
a different chamber. Whenever such a class is algebraic and effective, the second slot's
realization is genuinely a chamber condition. *(m7's Theorem 2, m6's Proposition 2.4.)*

**Theorem E3 (the node-class adjunction — an algebraic mechanism, not a geometric construction).**
The un-reflected pair `(I_enr, I_dP)` has invariant lattices `U(2) ⊥ E8(-2)` (rank 10),
`U(2)` (rank 2), joint pieces `(2,8,0,12)`, with `alpha in V_{--}`; the reflected pair has
`S_Co = ⟨alpha⟩ ⊥ L^{I_enr}` (index 1), `S_dP-type = ⟨alpha⟩ ⊥ L^{I_dP}` (index 1), joint pieces
`(3,8,0,11)`, with `alpha in V_{++}` (maintained register arithmetic: ranks, determinants, the
index-2 overlattice relation of the two `V_{--}`'s). So the reflection adjoins exactly one root,
moving `alpha` from the period-hosting piece to the common invariant piece where it is
automatically algebraic, and it precisely interpolates the **arithmetic** of the rootless regime
(`k = 0`: ranks `10, 2 = 0+10, 0+2`; AEGS, fix-free) with the rooted one (`k = 1`: ranks
`11, 3 = 1+10, 1+2`; one-node, Coble). **Scope (bound firmly):** this is an identification of
eigenlattice data under the operation "reflect in a root". No geometric degeneration of an AEGS
member to a one-node member is constructed or claimed here; whether and how such a degeneration
exists is a separate question, untouched.
*(m2's Theorem 1, Corollaries 1.1-1.2.)*

## 4. Part 2 — determination (M1 proper), in two theorems

**Theorem D1 (root-sign blindness: the sign of `alpha` is not lattice data).** In the common
invariant piece, `alpha in S_Co = T_Co^perp`, so `w_alpha|_{T_Co} = id`, `w_alpha` is a Hodge
isometry of every tuple realizing the datum (its period lies in `T_Co ⊗ C`), fixes `H`, reverses
`alpha`, and commutes with both `J_Co`, `J_dP` — because `g w_delta g^{-1} = w_{g delta} = w_{±delta}
= w_delta` when both operators send `alpha` to `-alpha` (for `I_En`, `I_dP` equally:
`I_dP(alpha) = -alpha`, since it is `-1` on the whole first `U` block; this corrects an
"`-I_dP` fixes `alpha`" parenthesis seen in review — the commutation conclusion is
unchanged). Hence the labelled data `(L, J_Co, J_dP, H, alpha)` and `(L, J_Co, J_dP, H, -alpha)`
are `O(L)`-conjugate by `w_alpha` itself, and **no** `O(L)`-invariant computation — eigenlattice,
gluing, discriminant, placement — can see the sign of `alpha`. Consequently effectivity and the
chamber are not lattice data, independently of any member. *(m1's Theorem 1.)*

**Theorem D2 (proved non-determination, inside the realization space itself).**
The authored comparison clause (a chamber statement on the twist side against a construction
tuple) has no truth value on the original data, proved in two complementing steps:
(i) *the data determine an `O(L)`-class and a smooth, connected, open 9-dimensional realization
family* (Theorem E1, §2), containing **both** models: the realization at the certified one-node
member `b0` (the clause against the construction tuple `b0` then holds degenerately, by the
identity — no rank claim about `b0` is used or needed), and at the certified `b_star` (the clause
against the construction tuple `b0` then fails: Theorem 9, and `nu(b0) = 0 ≠ 4 = nu(b_star)`);
(ii) *the two verdicts are not defects of algebraicity*: both realizations satisfy all five
authored bullets (item 2 of §2, Theorem E1's nonemptiness).
So the clause is **not a proposition** on the original data — *proved* non-determination, a
theorem about a positive-dimensional moduli, exactly distinguished from:
  *text absence* (the authored text defines one operator and no second slot: true, and immaterial
  to (i)-(ii)); *computational/API absence* (the constructor gap of the old pin and, marked
  current, the validated `6ad7a5ea` pin's `isometry_to` with typed inverse/composition — neither
  is invoked by any step here);
  *a missing member* (existence is part 1, in full).
*(m8's Theorem 2, m4's Corollary 4, m6's Proposition N, m7's Theorem 4, m2's §5(b).)*

## 5. Part 3 — the chamber bridge (Q2), sufficient and separated

**Theorem B (the positive comparison, hypotheses named once).** The five authored bullets read in
`R5`; `A = 2H − alpha` ample on both members (**M2**, proved for every one-node member, S4);
some label-carrying `gamma in O(L_K3)` with `gamma I_Co gamma^{-1} = I_Co,b`,
`gamma I_dP gamma^{-1} = I_dP,b`, `gamma(H) = H_b`, `gamma(alpha) = alpha_b` exists ([EXT]) and is
a **Hodge** isometry, equivalently `[sigma_2] = [sigma_1]` in `D(T_Co)/Gamma_L` (period-orbit
membership, **M3'**). Then effective Torelli (**M3**, S3) produces an isomorphism of tuples with
containing induced cohomology action, carrying the Kähler, nef, and effective cones, and every
chamber of every effective-root arrangement; α-effective and `H` nef and big automatically, and
`(Chm)` in **every** reading, in particular `R5`. *(The corpus's `(Hdg) + (M2) + (M3) ⇒ (Chm)`,
restated with exact quantifiers; the ampleness and Torelli hypotheses are load-bearing, and
`Aut(X) ↪ O(H²(X,Z))`-injectivity is needed only for exact operator equivariance, Remark 4.1 of
the framing.)*

**Separation S1 (levels, and exactly which implications hold).** Three levels: `(Lat)` (some
label-carrying isometry exists; **weakest**), `(Chm)` (some label-carrying isometry carries the
chamber; implies `(Lat)`), `(Orb)` (some label-carrying isometry carries `(sigma, chamber)`
together, equivalently is induced by an isomorphism of tuples; implies `(Chm)` by definition).

*The sufficient route:* `(Hdg) ∧ (M2) ∧ (M3) ⇒ (Orb)` — a Hodge isometry `gamma` of label type
that also carries the integral ample class `A` (`(M2)`, and `gamma(A) = A` because `gamma` fixes
`H, alpha`) is induced by an isomorphism of tuples via effective Torelli `(M3)`.

*No unconditional arrow from `(Hdg)` to anything.* `(Hdg)` alone does not imply `(Orb)` or
`(Chm)`, and `(M2)` is exactly why: Hodge isometries may move chambers — concretely, the wall
reflection `w_alpha` is a Hodge isometry for every period with `alpha` algebraic (it fixes the
period then) and it moves the adjacent chamber across `alpha^perp`, by Theorem 2 of
`.ultramath/smw0gfl0i/m4/chamber-prioritized.md`'s companion results and D1/E2(ii) below. Only
with `(M2)` forcing the ample class does a Hodge isometry land on the chamber.

*Strictness, each verified at its stated scope:* `(Lat) ⫋ (Chm)` by Theorem 9 of
`sm00_chamber-negative-half.md` (and by Corollary 3.4 of the framing, `(Lat) ∧ ¬(Hdg)` exhibited);
`(Chm)` does not imply `(Hdg)` by Separation S2's generic-pairs mechanism; `(Hdg)` alone does not
imply `(Chm)` by the wall-reflection fact just named; no strictness claim on `(Orb)` beyond its
per-definition implication is made.

**Separation S2 (necessity is not available — neither as theorem nor as generality).**
The original clause's *necessity* is not proved, and in general is false in the only sense the
corpus can presently test: by `prop:chamber-conditional` (S4) the label-transported chamber
coincides with the target's exactly when no extra effective root cuts it; for two **very
general** one-node members — whose existence with `Pic = S_Co` is Theorem D of
`sm00_positive-half-A21.md`, and whose `nu = 0` follows by parity (S4) — the effective-root data
are lattice-constant, so a label-carrying *non-Hodge* isometry transports the chamber between
members whose periods nevertheless differ in the connected 9-dimensional family: `(Chm)` holds
while `(Hdg)` fails for some such pairs. Therefore: `(Hdg)` is the proved sufficient bridge;
whether `(Chm)` can imply `(Hdg)` in some restricted sense is *unproved*; and any statement of
necessity for the orbit condition is in general false by the mechanism just displayed. No verdict
or theorem here asserts necessity of orbit membership, or decidability of the orbit question.
(Any in-dialogue phrase suggesting it — "the clause is exactly orbit-membership", "precisely when
Hodge" — stands corrected to the one-sided implication plus this paragraph.)

**Separation S3 (the certified pair's exact scope, preserved verbatim).**
`(b0, b_star)`: no `gamma in O(L_K3)` with `gamma H_0 = H_star`, `gamma alpha_0 = alpha_star`,
`gamma(c_0) = c_star`, in any of readings R2–R5 (Theorem 9 of `sm00_chamber-negative-half.md`, and
Theorem A2: no isometry with `gamma H = ±H` matches the effective cones, `nu(b0) = 0`,
`nu(b_star) = 4`, coset-free, maintained census). Consequences now proved *by contraposition
through the sufficient route, not by a necessity claim*: `(Chm)` fails there, hence `(Orb)` fails
there, hence `(Hdg)` fails there — `b_star`'s period is not in the label-stabiliser orbit of
`b0`'s (`m1`'s `smw0kq02h/d5` argument: `(Hdg)` would have given `(Chm)` by Theorem B, contradicting
Theorem 9). Nothing universal is claimed: for a general pair of one-node members the chamber
question lives at the period level and is open exactly there.

**Separation S4 (one unconditional lattice-level exclusion, with its exact scope).** Parity:
`H · S_Co = 2Z` (`H.(ae + bf + v + c alpha) = 2(a+b)`). Hence:
(i) a member with `Pic = S_Co` has `nu = 0` (no `H`-degree-1 `(-2)`-classes exist there);
(ii) `nu > 0` forces `Pic ⊋ S_Co` and `rho >= 12` (`S_Co` is primitive, and
`smwg_chamber-bridge`'s m6 arguments: the `H`-degree-1 classes glue into half-classes
`(e ± w)/2`, `w in E8(-2)`, algebraic only at that member — where the Picard action on them is a
permutation of the effective cone, attributed to the member's own automorphism, not to any
`Pic = S_Co`-fixedness criterion).
(iii) Therefore a member with `Pic = S_Co` and a member with `nu > 0` are never tuple-isomorphic,
at **every** period and **unconditionally** — the exclusion needs no period input.

*What `nu(b0) = 0` does not prove.* The certified member `b0` satisfies `nu(b0) = 0` (maintained
census), and the corpus proves very general members have `Pic = S_Co` (Theorem D of
`sm00_positive-half-A21.md`). But `nu` is a curve count, not a Picard-rank statement: `b0`'s rank
is not decided by `nu = 0`, and no step in this dossier may assert `rho(b0) = 11` until an
independent Picard computation on that member supplies one. The rank-separated reading of the
obstruction is therefore exactly (iii): `nu`-level facts never imply rank-level facts about the
certified member; the certified failure itself is preserved verbatim in S3. (The label-free
dimension/span variant of (iii) — an open chamber spans `NS_R(X)`, so a chamber-carrying map must
be rank-preserving — is valid **for a rank-11-witnessed pair** (e.g. any very-general member
against `b_star`) by (i)-(ii), and is explicitly **not** applied to the certified member `b0`
absent that rank evidence.)

## 6. Part 4 — what the surviving original comparison therefore is

1. **Construction vs construction (one-node members).** `[EXT]` holds for every pair (proved,
   uniform, lattice level). The chamber clause, in the corpus's adopted `R5` reading, is
   *sufficiently* carried by `(Hdg)` + `M2` + `M3` — which lands the two members on isomorphism by
   label-carrying marking — and **fails at the certified pair** `(b0, b_star)`. Whether any
   period-orbit membership is *necessary* for the original label-carrying chamber isometry is
   **not** decided by these theorems: the current document supplies sufficiency only, and the
   clause *also has true instances* between generic members at lattice level without Hodge input
   (`prop:chamber-conditional`). No statement here attaches decision-of-the-original-clause to the
   `Gamma_L`-orbit.
2. **Twist vs construction, as authored.** Part 1 (existence, in full) + Part 2 (proved
   non-determination): the original data select none of these realizations,
   and its clause is not well-posed — a theorem now, not a gap. The first slot is genuinely
   realized (E1/E2); the second slot is not authored, is not excluded from the roots alone
   (the reflected slot is admitted by Theorem E2(iii) and is not thereby *identified* with
   anything authored), and its realization costs the chamber condition of E2(iv).
3. **Everything else, untouched.** The lattice scope of `smwg_operator-extension.md` stands
   unchanged; no `R1` is used anywhere in this dossier (under `R1` the authored clause closes by
   the labels' own arrangement, and nothing above disputes it); `k >= 2`, `(O1)/(O2)` of the
   non-2-elementary decomposition, `R4` recovery, and the four downstream dep-audit citation
   sites remain open at their recorded places.

## 7. Premise ledger

# | premise | used in | status
|---|------|------|
| P1 | `L = U^3 + E8(-1)^2`, piece types/ranks `(3,8,0,11)`, `H²=4`, `alpha²=-2`, `H.alpha=0`, both fix `H, alpha`; `(++)` coordinates | §2-§5 | **maintained** (`coble_reflected_pair-run.txt`, `coble_joint_flag_premises-run.txt`), S1 |
| P2 | `S_Co/T_Co` types, ranks, signatures, `(r,a,delta)`; `T_Co = alpha^⊥_{T_En}` | all | corpus theorem + authored (`smtw_ot_types-m8.md` Thm 3.1; `@prop:coble-eigenspaces`) |
| P3 | AEGS three involutions surface/lattice; `alpha` unique mod `Gamma_En`; `Delta = alpha^perp` as discriminant divisor | E2(ii) | **in-repo primary** (`aegs_2023.md` :63, :128, :182), anchors checked |
| P4 | `H_b` nef and big (not ample), `alpha_b = [D_b]` effective, `D^2 = -2`, `alpha = pihat^*[e]` | §2, E1-E2, D2 | proved, `sm00_positive-half-A21.md` Lemmas 1.3, 2.1(3) |
| P5 | `2H_b − alpha_b` integral and ample, with `H_b − t alpha_b` ample for `0 < t < 1` | M2 everywhere | proved, Lemma 2.2 there |
| P6 | effective Torelli VIII.3.11 + VIII.11.1; `Aut ↪ O(H²)` | M3, M4 | cited, BHPV at corpus level (Remark 6.7 of the same file) |
| P7 | deformed-pair smoothness + `dim H^1(T_X)^iota = rank T_Co - 2` (sign bookkeeping) | E1 | **proved here** from `H^{2,1} = 0`, `T_X ≅ Omega^1` (S5) |
| P8 | labelled extension `[EXT]`, uniformly in `b` | D1, D2, B, Part 4 | published, `smwg_operator-extension.md` Theorems A, B |
| P9 | `b0/b_star` failure: Theorem 9 in R2-R5; Theorem A2 coset-free | D2, S3 | published/corpus theorems, maintained census 13/13 |
| P10 | `H · S_Co = 2Z`; `Pic = S_Co` at a very general member (Theorem D of the positive half) | S4 | proved (parity); Theorem D cited |
| P11 | symplectic product's coinvariant `E8(-2)`; [Ni1] Thm 4.7 uniqueness | E2(i) | session-verified via van Geemen–Sarti, S3 |
| P12 | period domain dimension `11 - 2 = 9`; construction's period image contains a nonempty Zariski-open piece | §2, E1, D2 | established (report item 3; framing §5) |
| P13 | I_En / I_dP negate `alpha`; `w_alpha` fixes `T_Co`; reflected operators fix `H, alpha, A` | E2, D1 | maintained check + one-line computations, S1/this dossier |
| P14 | `2H + alpha` has `(2H+alpha)·alpha = -2` while `alpha` is effective on `U` | E2(ii) | Lemma arithmetic on `U` (`A.alpha = 2`, RR); proved here/in m7 |
| P15 | `prop:chamber-conditional` (no-extra-root criterion for transported-vs-target chambers) | S2 | corpus proposition (the Heegner file, §"one-node comparison") |
| P16 | no second authored slot; item 8(b) | D2, Part 4 | authored-text fact (`docs/a21-tuple-hypotheses.md`) |

No premise is used outside its stated scope. The exploratory member scripts listed in the header are
registered in their member directories and are *not* among P1-P16.

## 8. Reviewer's checklist (hostile points, and where each stands)

* *Is `U` really open, and with which hypotheses? The §2 lemma items 1-5: ampleness decomposed into
  the component condition (C1) and the no-null-root condition (C2), the failure set contained in
  the wall union, the locus the construction-bearing connected component of the wall complement.
  Nothing in the dossier claims "absence of orthogonal roots alone proves ampleness": (C1) is
  earned at the named component and no implication is run without both chapters named.
* *Does existence overclaim E1/E2?* Every existence claim carries its hypothesis (`A` ample on the
  member for the pair; the authored single operator by smoothness+nonemptiness for E1); the
  factorization exclusion E2(ii) carries its own hypothesis explicitly.
* *Is the adjunction sold as geometry?* E3 restatement bound: eigenlattice arithmetic only;
  no degeneration constructed.
* *Is the bridge sold as necessity?* S2 states the only defensible scope, with the
  chamber-conditional mechanism displayed; no necessity or decidability claim stands anywhere.
* *Is the certified pair's scope inflated?* S3 quotes Theorem 9 + A2 verbatim; consequences are
  contrapositive through the sufficient route.
* *Is `Pic = S_Co` treated as open?* §2 item 5 and S4: Baire-general only, and S4 additionally
  records that `nu(b0) = 0` proves no rank for the certified member (kept open), with the
  rank-separated exclusion exact at `(i)–(iii)` and the dimension/span variant reserved for
  rank-witnessed pairs.
* *Tier discipline:* every "maintained" tag points to the published run logs; every exploratory
  member script is named in the header and excluded from P1-P16.

*Run state at publication:* `smw0kq02h` continues with m3 (fixed-locus route) and m5
(Enriques-side route) active; their reports, when they arrive, will be checked against this
dossier's scope, and any supported additions published likewise.
