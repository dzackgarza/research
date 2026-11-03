# A21: machine-checked arithmetic, two corrections, and the exact residual obstruction

Member m4 (swarm smvz57fr3), direction d7: formal verification of the arithmetic core of the
labelled tuple. This document is a **partial** answer, reported as partial: it does not settle
A21. It (i) verifies by machine the finite integral statements the tuple's definitions and the
repository's integral twist computation use, (ii) corrects two of those statements, and (iii)
locates the residual gap of A21 exactly, as one named theorem with a stated hypothesis.

All commits below are of `/workspace/nucleus/work/projects/p-9fcb4ed7f4b64e008de2ee29a7197bf4/repo`
checked out at `cb48774f88`. Files in this directory: `A21Arithmetic.lean` (Lean 4.33.1 +
Mathlib, compiles with no `sorry`), `verify_lattices.py` (exact integer arithmetic),
`verification_log.txt` (the run of both), `matrices_gen.txt` (generated Gram matrices).

---

## 1. The statement, and its exact decomposition

A21 is `@prob:coble-rigidity` in `writing/coble/heegner-report/coble-heegner-research-report.md`
(sec. "Labeled lattice data"): any two tuples
𝔏_{Co,2} = (L_{K3}, I_Co, I_dP, H, α, 𝔠) arising from the direct projective construction are
conjugate by an element of O(L_{K3}) preserving the labels, the degree-4 class, the effective
root and the chosen chamber. The five bullets defining the tuple are quoted verbatim, with the
before/after table of the authored text, in `docs/a21-tuple-hypotheses.md`.

The repository's own decomposition of the four clauses, which I adopt after checking its
statements (not its proofs):

* **Labels, degree-4 class, root** — `@thm:a21-labels`
  (`writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md`,
  lines 578–586): for any two one-node members there is γ ∈ O(L_{K3}) with
  γ S_Co = S'_Co, γ S_dP = S'_dP, γ H = H', γ α = α'. **Hypotheses**: `@prop:one-node-family`
  (line 544: a smooth proper equivariant family with relative polarization and exceptional
  divisor), `@prop:one-node-connected` (line 562: path-connectedness of the one-node locus),
  `@thm:one-node-transport` (line 609: Gauss–Manin transport carries H, α and the two
  involutions). I did **not** verify these three; the swarm's direction d3 audits the second.
* **Chamber** — this is not implied by the above. `@prop:chamber-conditional` (line 662)
  states: with 𝔠_b the chamber of the tuple at b and γ the isometry of `@thm:one-node-transport`,
  γ𝔠_b = 𝔠_b′ **iff** no effective class δ of square −2 on the second member outside γΔ_b cuts
  γ𝔠_b. So the chamber clause is exactly `@prob:effective-cone-agreement` (line 589).
* **Identification of the tuple's type with the reflection twist** — `@prob:twist-identification`
  (line 597). This is *not* needed for A21, which quantifies only over tuples of the
  construction; it is needed for comparisons with the twist model, and my §3(a) below is about
  exactly that.

**Consequence.** A21 ⟺ `@thm:a21-labels` ∧ `@prob:effective-cone-agreement`, and the second
conjunct is a genuine additional hypothesis about effective cones (equivalently, by
`@prop:chamber-conditional`, about periods), not a consequence of the local system. This is the
specific missing theorem of the obstruction: **the chamber clause of A21 is
`@prob:effective-cone-agreement`, unproved**, and a refutation of A21 would consist of one pair
of one-node members b, b′ together with one effective class δ of square −2 on X̂_{b′} with
δ ∉ γΔ_b that cuts γ𝔠_b. I did not produce such a pair; §4 says what a witness has to satisfy.

## 2. Machine-verified arithmetic (new in this direction)

Conventions: `U(2) = [[0,2],[2,0]]`, `E8(−m) = −m·(E8 Cartan matrix)`, form x·y = xᵀGy.
`S_dP = U(2) ⊥ ⟨−2⟩`, `S_En = U(2) ⊥ E8(−2)`, `T_En = U ⊥ U(2) ⊥ E8(−2)`,
`S_Co = S_En ⊥ ⟨−2⟩`, `T_Co = ⟨2⟩ ⊥ U(2) ⊥ E8(−2)`, `L_K3 = U³ ⊥ E8(−1)²`.

Lean (`A21Arithmetic.lean`, all proved, no `sorry`, `native_decide` only for closed integer
computations):

| theorem | statement | how |
|---|---|---|
| `det_cartanE8`, `det_E8m2`, `det_E8m1` | det E8 = 1, det E8(−2) = 256, det E8(−1) = 1 | `native_decide`; `det_smul` for the scalings |
| `det_U2m`, `det_U1m`, `det_G_dP` | det U(2) = −4, det U = −1, det S_dP = 8 | `native_decide` |
| `det_G_S_En`, `det_G_S_Co`, `det_G_T_Co`, `det_G_T_En`, `det_G_LK3` | −1024, 2048, −2048, 1024, −1 | `det_fromBlocks_zero₁₂` + the summand determinants |
| `G_LK3_unimodular`, `G_LK3_even` | \|det L_K3\| = 1; all diagonal entries of the Gram matrix even | `decide` |
| `even_G_S_En`, `even_G_S_Co`, `even_G_T_Co`, `G_T_En_fin_even`, `even_G_T_Co` | every Gram diagonal entry of S_En, S_Co, T_Co, T_En is even; for an integral lattice this is equivalent to evenness (`x·x = Σᵢxᵢ²Gᵢᵢ + 2Σᵢ<ⱼxᵢxⱼGᵢⱼ`) | `native_decide` |
| `pinned` | in S_dP = U(2)⊥⟨−2⟩, x² = 4 and x·α = 0 force x = ±(h₁+h₂) | coordinate algebra + `Int.mul_eq_one_iff_eq_one_or_neg_one` |
| `betaRoot_sq`, `betaRoot_not_U` | β = (e+f) + r₁ has β² = −2 and β ∉ U | `native_decide` |
| `twist_root_pinned` | if (b−a)a = −2, (b−a)b = 2 and (b−a)βᵢ = 0 for i ≥ 2 — the coordinate form of (α·β)β = −2α with a = β₀, b = β₁ — then β = ±α | coordinate algebra (`nlinarith`, `omega`) |
| `summand_det_unit`, `S_dP_no_unit_det` | a summand in an orthogonal splitting of a unimodular lattice has det ±1; det S_dP = 8 | `Int.mul_eq_one_iff_eq_one_or_neg_one` |

Exact Python (`verify_lattices.py`, `verification_log.txt`):

* determinants (signed): S_dP 8, S_En −1024, T_En 1024, S_Co 2048, T_Co −2048, L_K3 −1;
* every one of these lattices is 2-elementary, and its discriminant group is computed as the
  mod-2 kernel of the Gram matrix: orders 8, 1024, 1024, 2048, 2048 — i.e. (ℤ/2)^3, ^10, ^10,
  ^11, ^11 as the repository states;
* δ: 0 for U(2) and E8(−2), hence 0 for S_En and T_En; 1 for ⟨2⟩ (q(η/2) = 1/2), ⟨−2⟩
  (q(e/2) = 3/2) and hence 1 for S_dP, S_Co, T_Co;
* signatures: S_dP (1,2), S_En (1,9), T_En (2,10), S_Co (1,10), T_Co (2,9), L_K3 (3,19);
* gluing indices, from the determinants (valid because L_K3 is unimodular and the pairs are
  stated to be primitive orthogonal complements): [S_En ⊕ T_En : L_K3] = 2^10 and
  [S_Co ⊕ T_Co : L_K3] = 2^11 — both match `@prop:coble-eigenspaces`;
* the "full graph gluing" is realisable: an explicit linear bijection A_S → A_T with
  q_T(φa) = −q_S(a) exists for both pairs (backtracking search over the 1024 resp. 2048
  elements). With evenness and the signature this makes the glued lattice an even unimodular
  lattice of signature (3,19), i.e. L_K3 by Milnor's uniqueness theorem (citation in §6).

Consequences that matter for the argument, not just for the numbers:

1. **The degree-4 class is pinned by the root, inside the sublattice the construction gives.**
   H = π*O(1,1) and α = [D] both lie in Λ := π*Pic(ℙ¹×ℙ¹) ⊥ ℤD ≅ U(2) ⊥ ⟨−2⟩, which the
   repository proves is *contained* in S_dP (`@prop:del-pezzo-type-on-the-resolution`); the
   saturation Λ = S_dP is open (`@rmk:a21-open`) and is not used here. Inside Λ, `pinned` says
   x² = 4 and x·α = 0 force x = ±(h₁+h₂) = ±H, and nef/big fixes the sign. So on every member
   the degree-4 class is determined by the root (and by π*O(1,1)); if Λ = S_dP then this pins H
   in the whole invariant lattice. Bullet 2 therefore carries no freedom beyond bullet 3 and the
   construction's own H.
2. **No integral eigensplitting may be used.** det Λ = 8 ≠ ±1 (`S_dP_no_unit_det` together with
   `summand_det_unit`) is a machine-checked proof that Λ is never an orthogonal direct summand of
   the unimodular L_K3: the rational splitting H²(X,ℚ) = S ⊕ T does not descend, and for a
   primitive S the index satisfies [S ⊕ S^⊥ : L_K3]² = |det S|·|det S^⊥| ≥ 8 > 1. Nothing in this
   document uses such a splitting.
3. The repository's numbers det S_Co = 2048, [S_Co ⊕ T_Co : L_K3] = 2^11, |A_{S_En}| = 2^10,
   [S_En ⊕ T_En : L_K3] = 2^10 are all confirmed.

## 3. Two corrections to the repository's integral twist computation (`@prop:coble-eigenspaces`)

**(a) Root uniqueness in T_En is false as stated.** The report argues: "every vector of the
second or third summand has square divisible by 4, so a vector of square −2 lies in U; there
2ab = −2 … leaves {±(e−f)}". The second and third summands do have squares divisible by 4, but
that does not confine a square-(−2) vector to U: with η = e+f (η² = 2) and r₁ the first
E8(−2) simple root (r₁² = −4), β = η + r₁ has β² = −2 (`betaRoot_sq`) and β's E8-coordinate is 1
(`betaRoot_not_U`). Machine-checked witness: β = (1,1,0,0,1,0,0,0,0,0,0,0).

What is true, and all the twist needs, is that the *authored bullet* pins the root:
for a root β of T_En the twisted involution w_β∘I_En fixes α iff (α·β)β = −2α, and that forces
β = ±α (`twist_root_pinned`). So the reflection twist of `@cons:reflection-twist` has a unique
root direction compatible with bullet 3, and `@prob:twist-identification` is *not* obstructed by
root ambiguity: what remains open there is the integral eigenspace/type identification (that the
construction's I_Co has invariant lattice U(2)⊕E8(−2)⊕⟨−2⟩ with α the (+1)-direction, and that
the containment π*Pic(Y) ⊥ ⊕ℤD_g ⊆ S_dP is saturated — `@rmk:a21-open`), not an enumeration of
roots.

**(b) T_Co is even, not odd.** `@prop:coble-eigenspaces` says "T_Co is odd, since η² = 2 is odd",
and identifies T_Co with the odd 2-elementary lattice I_{2,9}(2). But 2 is even, so ⟨2⟩ is an
even lattice and T_Co = ⟨2⟩ ⊥ U(2) ⊥ E8(−2) is even: every Gram diagonal entry of T_Co is even
(Lean `even_G_T_Co`, Python the same check), and for an integral lattice even diagonal entries are
equivalent to evenness. Its verified invariants are rank 11, signature (2,9),
det −2048, discriminant group (ℤ/2)^11, δ = 1, **even**; S_Co has rank 11, signature (1,10),
a = 11, δ = 1, even. Note that S_Co and T_Co have the same (rank, a, δ) = (11,11,1) and differ
in signature and in nothing else here: (r, a, δ) alone does not separate them, so the
classification input must be (rank, signature, a, δ, parity). The gluing numbers are unaffected
(loc. cit.); only the type label `I_{2,9}(2)` is wrong, and should read: the even 2-elementary
lattice with signature (2,9), a = 11, δ = 1.

## 4. What a witness for the failure of A21 has to satisfy

By `@prop:chamber-conditional` (line 662) and `@rmk:chamber-not-transported` (line 651), with
the chamber of the tuple read as the chamber of the positive cone containing the Kähler cone,
C_X a component of {x² > 0} in H²(X,ℝ) and Δ_X the classes of square −2 that are *effective*:

  K_X = {x ∈ C_X : x·δ > 0 for all δ ∈ Δ_X},  𝔠_X = the chamber of C_X∖⋃_{δ∈Δ_X}δ^⊥ containing K_X.

A refutation of A21 is then exactly: two one-node members b, b′ and a class δ on X̂_{b′} with
δ² = −2, δ ∉ γΔ_b, δ·(γ𝔠_b) changing sign on γ𝔠_b. Sufficient: Pic(X̂_{b′}) strictly larger
than γ Pic(X̂_b) together with a new effective (−2)-class. I did **not** produce such a pair, and
I did not verify that the one-node locus contains members with ρ(X̂) > 3; that is direction d2/d3
work, not mine. What I can say precisely: A21 is *not* refuted by anything in the lattice data —
all tuples have the same lattice labels (§2), so any refutation must come from Δ, i.e. from the
period, exactly as `@prob:effective-cone-agreement` says.

## 5. Premise ledger

| claim | source | status |
|---|---|---|
| the five bullets, verbatim | `docs/a21-tuple-hypotheses.md`; report sec. "Labeled lattice data" | authored text |
| A21 = `@prob:coble-rigidity` | report l. 620–640 | authored |
| labels conjugate | `@thm:a21-labels` (l. 578) | theorem, conditional on the two below plus transport |
| one-node family is smooth/proper/equivariant | `@prop:one-node-family` (l. 544) | repo theorem, **not verified here** |
| one-node locus path-connected | `@prop:one-node-connected` (l. 562) | repo theorem, **not verified here** (disputed; d3) |
| transport carries H, α, involutions | `@thm:one-node-transport` (l. 609) | repo theorem, **not verified here** |
| chamber clause | `@prob:effective-cone-agreement` (l. 589) + `@prop:chamber-conditional` (l. 662) | **open** — the missing theorem |
| twist type of I_Co | `@prop:coble-eigenspaces` (report l. 560–600) | integral computation; corrected in §3 |
| dets, disc groups, δ, gluing indices | this document, §2 | machine-verified (Lean + exact Python) |
| H pinned by α; no integral splitting | this document, §2 | machine-verified (Lean) |
| saturation of π*Pic(Y) ⊥ ⊕ℤD_g in S_dP | `@rmk:a21-open` | open |

## 6. Sources

* `writing/coble/heegner-report/coble-heegner-research-report.md` (commit `cb48774f88`):
  sec. "Direct Coble geometry from invariant (4,4) curves" (l. 341–470), sec. "The Coble lattice
  package" (l. 480–660), sec. "Labeled lattice data" (l. 601–656).
* `writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md`:
  `@prop:one-node-family` (544), `@prop:one-node-connected` (562), `@thm:a21-labels` (578),
  `@prob:effective-cone-agreement` (589), `@prob:twist-identification` (597),
  `@thm:one-node-transport` (609), `@lem:face-at-H` (621), `@prop:chamber-pinned` (641),
  `@rmk:chamber-not-transported` (651), `@prop:chamber-conditional` (662), `@rmk:a21-open`.
* `docs/a21-tuple-hypotheses.md`: the authored bullets at `a145cea4a5` and the note that no
  authored bullet relates I_dP to α.
* Uniqueness of even unimodular indefinite lattices (used once, in §2, to conclude that the
  glued lattice is L_K3): Milnor–Husemoller, *Symmetric Bilinear Forms*, or Serre,
  *Cours d'arithmétique*, Ch. V.
* Chamber/positivity description of Kähler cones of K3 surfaces: BHPV, *Compact Complex
  Surfaces*, Thm. 8.1.5 / (2.2), as cited at `@rmk:chamber-not-transported`.

## 7. Limits of this document

Not verified here, and not claimed: the geometry of the fixed loci and the Lefschetz ranks
k+2 and k+10; the family and transport theorems; the connectedness of the one-node locus; the
saturation of the invariant lattices; every statement about chambers and effective cones beyond
quoting the repository's. The Lean file checks the arithmetic of the *summands* and their
orthogonal sums by determinants and evenness; the discriminant-form and gluing checks are exact
Python, not Lean. A21 remains open, with the gap located at `@prob:effective-cone-agreement`.
