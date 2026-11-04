# Ordinal Hessenberg natural product: delivered interface + successor bound, and the exact obstruction

Status record for research issue #606's next formal unit at the `lean-categories`
owner (`LeanCategories/ForMathlib/OrdinalNaturalSum.lean`), per the handoff absorbed
into #606. Everything below was checked in this VM; nothing is claimed that was not
built.

## Provenance

- Source: `dzackgarza/lean-categories`, pristine `main` at
  `fc6d3d6961223c75290c93da540c87f17a926cc7` ("Formalize lattice divisibility and
  stable-group line separation"), the tip the #606 handoff names as its starting
  point (the handoff's `ef3bded2` is a later tip; the checkout here was `fc6d3d6`).
- Toolchain: Lean 4.33.0, Mathlib as pinned by that checkout.
- Command: `lake build LeanCategories.ForMathlib.OrdinalNaturalSum` — **green,
  909 jobs, no `sorry` in the file** (before and after the change).

## Delivered (patch: `leancategories-ordinal-natural-product.patch`)

The patch applies cleanly to pristine `fc6d3d6` (`git apply --check` verified) and adds
four declarations, all sorry-free:

1. `naturalProduct_le_of_constraint`. Any ordinal satisfying the defining constraint of
   the natural product at `(a, b)` bounds `a ⊗ b` above. Before this, every law that had
   to compare the product with a candidate ordinal had to inline the defining `sInf`.
2. `naturalProduct_isLeast`. `a ⊗ b` satisfies the constraint and is below every ordinal
   that does.
3. `naturalProduct_eq_iff`. `c = a ⊗ b` exactly when `c` satisfies the constraint and is
   minimal among ordinals that do — the usable form of the `sInf` definition.
4. `naturalProduct_succ_le`. **`a ⊗ (b + 1) ≤ (a ⊗ b) ⊕ a`**, by induction on `a` using
   (1). This is the first half of distributivity over a one-step extension: multiplying
   by a successor costs at most one extra `a`-summand. It is the first inequality of
   this kind in the file; unit, zero, monotonicity, strict monotonicity and cancellation
   were already present.

Why (4) is the substantive step: the two cases (`b' < b`, `b' = b`) each require
re-associating a four-term Hessenberg sum around the constraint supplied by
`naturalProduct_constraint`, and the `b' = b` case has to compare the shared `a ⊗ b`
summand and then spend `a' < a` inside a nested natural sum. Both reductions are now
machine-checked rather than sketched.

## Second delivery (this pass): the mirrored bound and the unit-factor case

The #606 handoff orders the next proofs as "natural-sum associativity, then the
natural-product unit, monotonicity with its exact positivity hypotheses, distributivity,
and associativity". Checked against the file at `fc6d3d6`: associativity of the natural
sum, the product's unit (`naturalProduct_one`, `naturalProduct_one_left`), monotonicity
(`naturalProduct_mono_left/right/mono`), strict monotonicity
(`naturalProduct_lt_left/right`, `naturalProduct_lt_iff_left/right`) and cancellation are
**already there**. The only items of that list still outstanding are distributivity and
associativity — the two the obstruction below governs.

Added in this pass, both sorry-free and in the same patch:

5. `naturalProduct_succ_le_left`. **`(a + 1) ⊗ b ≤ (a ⊗ b) ⊕ b`** — the same one-step
   bound with the successor in the *first* argument, which `naturalProduct_comm` gives
   from (4) in two rewrites. The distributivity argument needs the bound in that
   orientation.
6. `naturalProduct_one_succ`. **`1 ⊗ (b + 1) = (1 ⊗ b) ⊕ 1`** — at the unit factor the
   two sides of the missing successor law coincide (`simp` with `naturalProduct_one_left`
   and `naturalSum_one`). It is the `a = 1` base case of the induction that would close
   the general equality, and the only case of that equality proved here.

## `#606` route item 1: the set-diagram presentations are already registered

The handoff says "arbitrary filtered diagrams still need their limit and colimit
presentations, cones or cocones, legs, mediators, and exact hypotheses". Checked by
building, at `fc6d3d6`, that claim is **stale**:

- `lake build LeanCategories.Catalogue.Semantics.Limits.Registration` — green, 2707
  jobs. That file already carries `setsDiagramLimit` / `setsDiagramColimit` for arbitrary
  small shapes (`{J : Type v} [Category.{w} J]`, no finite or enumerable index set),
  their projections/injections, the universal mediators with `_fac` and `_uniq`,
  `hom_ext`, the endofunctors on `J ⥤ Type`, the filtered-colimit comparison
  `setsFilteredColimit_eq_iff` under `IsFilteredOrEmpty`, and the registrations
  `lim.sets.diagram` / `colim.sets.diagram` with their four morphism entries.
- `lake build` of `Foundation.Cardinality`, `Foundation.PowerSets`, `Foundation.Ordinals`,
  `Foundation.FiniteOrders`, `Foundation.FiniteSubsets` — green, 2786 jobs.
- No `sorry` term and no `axiom` declaration anywhere under `LeanCategories/` (grep for
  the bare token, and for `axiom` at line start).

So the remaining formal inputs for the set layer are exactly the four open upstream
issues that #606 is blocked by, not missing work at the limits file:
`lean-categories#95` (finite-subset direct-image functor), `#96` (selected
enumeration/ranking data), `#97` (well-ordered sets and order types), `#98` (partial and
total order categories). All four are still open, which is why #606 stays open.

## The exact obstruction (not proved, and why)

The reverse inequality

    naturalSum (naturalProduct a b) a ≤ naturalProduct a (Order.succ b)

— equivalently the other half of distributivity — does **not** follow from the available
machinery. The `≤` direction above is a `naturalProduct_le_of_constraint` application
(show the candidate is in the defining set). The `≥` direction is a `le_csInf`
application: it needs `(a ⊗ b) ⊕ a ≤ c` for **every** `c` satisfying the constraint at
`(a, succ b)`. The constraint at `b' = 0` gives only

    ∀ a' < a, (a' ⊗ succ b) < c,

and no `sup` over `a' < a` of these recovers `(a ⊗ b) ⊕ a`:

- for a successor `a = a₀ + 1` the supremum `⨆_{a' < a} ((a' ⊗ b) ⊕ a')` collapses to the
  single `a' = a₀` term and is *strictly smaller* than the target — checked concretely at
  `a = b = 1`, where the target is `2` and every `a' < 1` term is `0`;
- for a limit `a` the supremum is the right shape but still needs continuity of
  `b ↦ a ⊗ b`-style interchange, which the file does not have.

So the gap is exactly one of: (i) a continuity/sup-interchange lemma for the natural
product in each argument, or (ii) the Cantor-normal-form description of the natural
product (in which associativity and distributivity are immediate). The file's attribution
note explicitly declines to prove the CNF comparison and the handoff does not require it;
either route is new work, not a re-derivation of what is already there.

**Therefore: associativity of the natural product, distributivity in general, and the
commutative-semiring and ordered laws are all still open.** No structure instance was
added — and note that packaging Hessenberg operations as a second `CommMonoid (Ordinal)`
instance would collide with the existing instance on `Ordinal` for ordinary
multiplication, so any eventual structure claim needs a bundled type or a distinctly
named law set. That is a design decision reserved to the formal owner.

## Blockers (bounded, exact)

1. **`lean-categories` push.** The connected GitHub channel covers `dzackgarza/research`
   only; `git push` in the local `lean-categories` clone fails with
   `could not read Username for 'https://github.com'`. The change is delivered as the
   patch file in this directory instead. The shared clone at
   `$HOME/gitclones/lean-categories` was left at its original tip `fc6d3d6` and clean, so
   other agents see exactly what they left; the patch is the only record of the change.
2. **Research issue write.** `gh` has no token in this VM, so #606 cannot be closed or
   commented. Closure of #606 also requires far more than this unit (its acceptance is
   the whole set layer, not this file).

## Reproduce

    cd <lean-categories checkout>            # at fc6d3d6, clean
    git apply computations/reports/leancategories-ordinal-natural-product.patch
    lake build LeanCategories.ForMathlib.OrdinalNaturalSum          # 909 jobs, green
    lake build LeanCategories.Catalogue.Semantics.Limits.Registration   # 2707 jobs, green
    lake build LeanCategories.Catalogue.Semantics.Foundation.Cardinality \
      LeanCategories.Catalogue.Semantics.Foundation.PowerSets \
      LeanCategories.Catalogue.Semantics.Foundation.Ordinals \
      LeanCategories.Catalogue.Semantics.Foundation.FiniteOrders \
      LeanCategories.Catalogue.Semantics.Foundation.FiniteSubsets        # 2786 jobs, green
