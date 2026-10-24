# Handoff: research issue #606

[Issue #606](https://github.com/dzackgarza/research/issues/606) owns the full set-layer requirement and acceptance. Continue it on `main`, one mathematical owner at a time. The root `HANDOFF.md` retains a separate geometry and cohomology task and its outstanding specimens.

## Next formal unit

Work in `lean-categories` at `LeanCategories/ForMathlib/OrdinalNaturalSum.lean`. The published `main` tip at this handoff is `ef3bded2611a97799b6462ebcf2a7aa7b228c669`. `naturalProduct` is defined for ordinals by the least `c` satisfying, for every `a' < a` and `b' < b`,

`(a' ⊗ b) ⊕ (a ⊗ b') < c ⊕ (a' ⊗ b')`.

Here `⊕` is the separately defined Hessenberg natural sum. The file proves that the admissible set is nonempty, its infimum satisfies the constraint, and product is commutative with zero on either side. The next proofs are natural-sum associativity, then the natural-product unit, monotonicity with its exact positivity hypotheses, distributivity, and associativity. Establish the commutative semiring and ordered laws before claiming that structure. Register the typed product object construction at its formal owner; register its comparison-arrow action when monotonicity supplies the arrow. Retain distinct names for ordinary ordinal sum/product/power and Hessenberg natural sum/product. The n-ary forms used by research still need their formal route. A direct equivalence with the Cantor-normal-form algorithm has not been proved here and is not a prerequisite invented by this handoff.

The recursive definitions are adapted from Violeta Hernández Palacios' Apache-2.0 [natural ordinal operations](https://github.com/Vilin97/lean-pool/blob/main/LeanPool/MisereGames/Mathlib/NatOrdinal.lean) and [natural-product formulation](https://github.com/Vilin97/lean-pool/blob/main/LeanPool/ConwayRefinement/CombinatorialGames/NatOrdinal/Basic.lean). Inspect the pinned source and preserve attribution when extending the adaptation. The research Python Cantor-normal-form implementation is a consumer, not a mathematical authority.

## Remaining #606 route

1. At `lean-categories`, reconcile the other set constructions against the complete issue scope. In particular, `LeanCategories/Catalogue/Semantics/Limits/Registration.lean` currently registers binary set product/coproduct and pullback; arbitrary filtered diagrams still need their limit and colimit presentations, cones or cocones, legs, mediators, and exact hypotheses. Preserve the distinctions among finite, countable, enumerated, partial-order, linear-order, discrete-cardinal, ordered-cardinal, and ordinal categories and their selected structural maps.
2. At `lean-cas-dsl`, present and execute the formal declarations through the kernel's typed catalogue route, keeping leaf registrations opaque and acceptance independent of their claims. Inspect its current branch and dirty source before editing: this host's checkout was at `dbaa47c1` and ten commits behind `origin/main`, with an existing edit to `CasCatalogue/Language.lean` and an untracked `TODO.md` at handoff. Those paths were not changed for #606.
3. Migrate research's public set consumers through the catalogue-derived language, with the same defining data, maps, categories and result types. Remove the set-layer `OwnedCategory` provider path only after its consumers have moved; #384 retains removal of shared transitional machinery. Keep #606 open until its complete acceptance is met. Required research execution and independent acceptance remain under #496/#498 and the current `DEV-58` phase.

The focused Lean build of `LeanCategories.ForMathlib.OrdinalNaturalSum` passed at `ef3bded2`. No full suite or research preamble execution was run. Recheck branch tips, dirty files, issue dependencies and the verification phase before resuming.
