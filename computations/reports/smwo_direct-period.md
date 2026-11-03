# A20 direct period theorem for the one-node Coble construction: image and monodromy

Evidence register for the original A20 obligations `@prob:B24` and `@prob:B25`
(`writing/coble/heegner-report/coble-heegner-research-report.md` :1981-1989), from UltraMath run
`smw0o7jbf` (accepted solution m2/d6; `REFEREE-verdict-m2.md` in the swarm's directory has the full
audit trail; nothing in the repository was modified). Caveats recorded by the referee follow each
theorem and are part of its statement. The original B24/B25 statements are quoted at their
capitalizations; other A20/A21 obligations are left as they stand.
The corpus's other theorems (the labelled operator extension [EXT] at lattice level, the conditional
Hodge bridge, the certified pair) are used at their stated scope and are never reopened here.

**B24 (verbatim).** "The marked direct Coble moduli stack is an explicit arrangement complement
`D_Co^o`, with the ample/nef chamber and exceptional root correctly encoded."
**B25 (verbatim).** "The deck group of the marking cover and the geometric monodromy group equal the
labeled centralizer group `Gamma^dir_{Co,2}`."
The five groups are kept fixed throughout: `G1 = Gamma^geom` (orbifold monodromy image of the
connected direct stack), `G2 = Gamma^dir_{Co,2}` (image of `Z_{O(L)}(I_Co, I_dP)_{H,alpha,c}` in
`O^+(T_Co)`, @def:direct-group), `G3 = Gamma^Hdg_{Co,2}` (Enriques-Heegner stabilizer image), `G4 =
Gamma^cong` (the congruence preimage, strictly bigger than the stable `O^+(T_Co)*`), and `G5 =
Gamma_L` (the auxiliary label-stabiliser image of report item 3). Identification of any pair not
proved here is left open; no quotient is replaced by notation.

## Theorems, at their registered scopes

**Lemma 1.** `I_dP = -1` on `T_Co`. (Construction's joint characters `(3,8,0,11)` at :673 with
`rk S_dP = 3`, so the `(−+) = 0` piece vanishes and `T_Co = (−−)`.)

**Theorem A (the arrangement is excluded pointwise, not just generically).** No member of the direct
one-node construction (the one-node refinement of `@def:direct-cover-datum`: irreducible τ-invariant
`(4,4)` branch, one ordinary node at a τ-fixed point, else smooth) carries an algebraic `(−2)`-class
of `T_Co`. Proof: Riemann–Roch supplies one of `±delta` effective for `delta² = -2`; the
construction's own geometric `iota_dP` inverts the class (Lemma 1), and automorphisms preserve
effectiveness; then an ample class pairs strictly positively with both, a contradiction. Only
pointedness of the ample cone is used; the chamber is unused. **Consequence.** Every marked period of
a member lies in
`D_Co^o := D(T_Co) \ cup_{delta ∈ T_Co, delta² = -2} delta^perp`,
an explicit arrangement complement of the Coble period domain, and this is *pointwise*, strictly
stronger than the corpus's very-general `Pic = S_Co` statement. **Side-effect statement.** The same
argument re-grounds, with the precise reason the corpus left un-stated, why `2H−alpha ∈ S_Co ⟂ T_Co`
is ample on members: a member's would-be `T_Co`-curve, orthogonal to `2H−alpha`, cannot exist.

**Theorem B (the second slot is realized geometrically at the chamber hypothesis).** At every marked
Coble period `q` at which `2H−alpha` is a Kähler class — the chamber datum `c` and nothing else —
both `I_Co` and `I_dP` are Hodge isometries of the marked structure that fix `2H−alpha`, and are
therefore induced by commuting automorphisms `iota_Co`, `iota_dP` of `X_q` (effectivity via the
fixed-Kähler-class condition and the chamber arrangement of the positive cone; global Torelli as in
Peters, *Torelli theorems for Kähler K3 surfaces* §1.8, equivalent to the corpus's BHPV VIII
statements). This is exactly the "missing geometric realisation" the corpus names at :1015 and
consistent with the published realization theorem of `smwg_chamber-bridge.md` (E2). *Propagate-level
caveat:* its input (R), the abstract lattice-polarized realization of `q`, is quoted at statement
level (PSS/Todorov framework, as the corpus's item 3 itself uses), not re-verified in this run.

**Theorem C (model rigidity — the retained geometric hypotheses of the construction cost nothing).**
With the two involutions realized, the resolved quotient `Y° = X/iota_dP` is a smooth rational
surface with `b₂ = 3`, `K² = 7` (Noether), `B° = Fix(iota_dP)` smooth of genus 8 with
`e(Fix) = 2·rk S_dP − 20 = −14` and the corpus's corrected fixed-locus census (geometric genus
`9 − k = 8`, two points on the conic, node = one blow-up downstairs, no isolated extra points), with
`B° ∼ −2K_{Y°}`; the discrete model `(Y°, B°, τ°, h)` is locally constant in the period (rigidity of
smooth rational surfaces), so on each connected component of the chamber-locus it is identically
`(Bl_p(P1xP1), (4,4)-proper-transform, τ, O(1,1))`; and contracting the `(−1)`-class recovers the
construction's one-node member exactly: `Y ≅ P1×P1`, branch `B ∈ |O(4,4)|` irreducible with exactly
one ordinary node at a `τ`-fixed point, smooth elsewhere, `H = π*O(1,1)`, product symplectic form.
So irreducibility, the single node, its τ-fixedness, product type and `H = π*O(1,1)` are all
automatic at every such period.

**Theorem D (the image, at the original quantifiers).** On the component of `D(T_Co)` containing the
periods of members, with `D_Co^{oc} := {q in D_Co^o : 2H−alpha is a Kähler class on X_q}` and
`p` the period map of the marked one-node direct construction into `D_Co = D(T_Co)/Γ_L`,

> `im(p) = D_Co^{oc} / Γ_L`.

The three markers of B24 are identified: the **arrangement** is `{delta^perp : delta ∈ T_Co,
delta² = -2}` (excluded pointwise by Theorem A); the **chamber** is the single labelled inequality
"`2H−alpha ∈ K_{X_q}`" (not a period condition, since the effective sign of each `S_Co`-class is a
function of the component, not of `q`); and the **exceptional root** `alpha` is the `⟨-2⟩`
generator of `S_Co`, effective on every member, with `2H−alpha` the degree-14 chamber class. With
`2H−alpha ∈ K`, `alpha` effective with `alpha² = -2`, `H·alpha = 0`. Fibres are the
`Aut(Y)^τ`-orbits; both domain and image have complex dimension 9.

**Theorem (residual, the exact remaining geometric obstruction).** The only possible further
excluded loci are the walls inside `D_Co^o` cut by *mixed* `(−2)`-classes `delta = s + t`
(`s ∈ S_Co`, `0 ≠ t ∈ T_Co`) with `(2H−alpha)·delta = 0`. Two of the three cases are proved removed
here: the `s = 0` case (Theorem A), and the `t = 0` case by the hand-checkable divisibility result
**`(2H−alpha)^⊥ ∩ S_Co` contains no `(−2)`-class** (with `s = ae+bf+c α+w`,
`(2H−alpha)·s = 4a+4b+2c`, so `c = −2a−2b` and `s² = 4ab − 8(a+b)² + w² ≡ 0 (mod 4)`), which is the
lattice content of "the exceptional root correctly encoded". The remaining named theorem —

> **(T-mixed).** Let `S_Co ⊂ L_K3` be `U(2) ⊕ E_8(-2) ⊕ ⟨-2⟩` with its primitive index-`2^11`
> gluing `L_K3 = (S_Co ⊕ T_Co)` at glue order `2^11`; let `H = e+f`, `alpha` the `⟨-2⟩` generator.
> Then (a) the set of `delta ∈ L_K3` with `delta² = -2`, `delta ∉ S_Co ∪ T_Co`, and
> `(2H−alpha)·delta = 0` and (b) which of those classes are effective at some `q ∈ D_Co^o`,

is open and is exactly what decides between the two branches of Theorem D's image statement:
if no such effective class exists anywhere, the image is **exactly** the arrangement complement
(B24 verbatim); if it exists on a nonempty locus, the image is the arrangement complement minus that
further closed hyperplane section.
(T-mixed) is a lattice-and-gluing computation plus the effective-cone argument — the mixed-stratum
analogue of `@prop:det-saturation-del-pezzo`'s for the pure piece.

**Theorem E (B25 at the quotient-group content).** `M̃ ≅ D_Co^{oc}` (as analytic spaces,
`Γ^dir`-equivariantly) by injectivity then surjectivity of the marked period map (segre recovery of
`(Y,B)` from `|H|` with the transport fixing the ample class; Theorem B for the effectivity clause),
the mark-cover is connected and has deck group `G2 = Γ^dir_{Co,2}` acting on periods by
`theta ↦ theta ∘ g^{-1}`, and the associated-bundle local system has monodromy image equal to the
same group, so

> deck group of the marking cover `=` `G1` `=` `G2` `=` `Γ^dir_{Co,2}`

at the quotient-group content. Any reading of "Galois" stronger than the stack/quotient-group
content (e.g. freeness of the action) is kept unclaimed here. The identification
`Γ^dir = Γ_L` is **left open**: it holds exactly if the chamber datum `c` is determined by `(H,
alpha)`, an input the corpus has at `@lem:face-at-H` and `@prop:chamber-conditional` but which is
not decided here or in the run; `G3` and `G4` are untouched and @prob:group-identification stands
unchanged with no equality by notation.

## Premise ledger (inputs and their tiers)

| # | input | tier |
|---|---|---|
| 1 | `@def:direct-cover-datum` with the one-node refinement; involutions and labelled classes as in §1 of the run's document | corpus definitions (:853-932) |
| 2 | Explicit member with no other singularity, from `@sec-explicit-curve` (:2425-2445) plus its own verification contract | corpus |
| 3 | Lattice labels (`S_Co, T_Co, S_dP = Λ`, ranks `(3,8,0,11)`, index `2^11`); `formalization/coble-enriques/A21Arithmetic.lean` at its file's own scope | corpus theorems + machine verification at its scope |
| 4 | `D(T_Co)` dimension 9; `Γ_L`; Zariski-open image of the family's period map; fibres; Borel extension (J. Differential Geom. 6 (1972) 543-560, hypotheses as cited at :661) | corpus item 3 |
| 5 | Global Torelli and its effectivity criterion (Peters §1.8; BHPV VIII) | primary statement-level |
| 6 | Riemann–Roch for `(−2)`-classes; Lefschetz for nonsymplectic involutions; quotient smoothness at fixed curves; smooth-rational rigidity | standard |
| 7 | Surjectivity of the lattice-polarized period map (PSS/Todorov; the corpus's standing framework) | statement-level (flagged in the verdict) |
| 8 | `2H−alpha` ample on every member; `E² = -2`, `H·E = 0` | corpus lemmas 1.3, 2.2 of `sm00_positive-half-A21.md` |

Computation used is hand-carried exact arithmetic small enough to check line by line
(`(2H−alpha)² = 14`, `(2H−alpha)^⊥ ∩ S_Co` without `(-2)`-classes, `e(Fix) = 2 rk S − 20`,
`K² = 10 − b₂ = 7`, `2g−2 = 2K²`); the corpus's machine-verified tiers are cited, not re-run.

## Falsifiable cross-checks carried by the theorems

1. **No `T_Co`-curve on a member** (Theorem A): the register `computations/reports/sm57_README.md`'s
   `F'` extra classes must be read against this; the consistent reading (as the register itself
   already required) is against the symplectic product's anti-invariance, not the del Pezzo one.
2. **Ampleness-vs-nefness at the wall** (Theorem A's converse side in §6 of the run's document):
   `2H−alpha` is ample on a family member exactly because the member avoids the arrangement; reading
   "ample on every member" from the corpus's :661 never gives an on-arrangement member.
3. **Fixed-locus bookkeeping** (Theorem C1's footnote): `e(Fix) = 2(2+k) − 20`, the two conic
   points, and the one blow-up per node make `rk S_dP = 2+k` consistent with `e(Fix)`; consistency
   was falsely reported elsewhere in aid of the same proposition.

## What remains open next (named, not cosmetic)

* `(T-mixed)` — the exact theorem deciding which of the two image branches stands (above);
  attackable by enumerating the index-`2^11` glued lattice, then the effective-cone clause.
* `Γ^dir = Γ_L` — the chamber-datum identification, via `@lem:face-at-H` and
  `@prop:chamber-conditional`; though it would sharpen Theorem E's group naming to the label
  stabiliser, it is a separate theorem and was not used here.
* `@prob:group-identification` among the four — lattice/Hodge/congruence/monodromy statements,
  untouched except where each group was separately settled.
* The same theorem's mixed-class `s ≠ 0 ≠ t` analysis as a computation: the index-`2^11` gluing
  lattice's explicit basis and the automorphism action on it (the corpus's next arithmetic move;
  not yet in this or the run's register).
