/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
module

public import CasCatalogue.Leaf
public import CasLeaves.Foundation.FiniteSets
public import CasLeaves.Foundation.Cardinality
public meta import CasCatalogue.Leaf
public meta import CasLeaves.Foundation.FiniteSets
public meta import CasLeaves.Foundation.Cardinality

@[expose] public section

/-!
# The forgetful functor of finite sets, on presented finite sets

A realization hosted outside `lean-cas-dsl`: the registered forgetful functor
`forget[clf.sets.finite] : FiniteSets ⥤ Sets` (`lean-categories`), acting on finite sets presented
by `n` (`rz.finite_sets.presented`) as `n ↦ Fin n` presented as a set (`rz.sets.presented`). Its
square commutes strictly: both sides are `Fin n`. It adds no mathematics; with it, everything sets
have (cardinality, finiteness, …) is computable on presented finite sets.
-/

open CategoryTheory
open CasCatalogue CasCatalogue.Foundation.Actions CasCatalogue.Foundation.FiniteSets

namespace ResearchLeaves.FiniteSets

/-- `n ↦ Fin n`, realizing the forgetful functor of finite sets. -/
noncomputable def forgetAction : RealizedAction (LeanCategories.Foundation.Mathlib.finite.{0}.forget.toFunctor)
    finiteDenotation setDenotation :=
  RealizedAction.induced _ (fun n => SetHandle.finite n) (fun _ => rfl)

end ResearchLeaves.FiniteSets

namespace ResearchLeaves

register_leaf
  { backend := "lean"
    contributions := [
  .action
  { id := ⟨"act.research.finite_sets.forget"⟩
    edge := .classifierForget ⟨"clf.sets.finite"⟩
    realization := `ResearchLeaves.FiniteSets.forgetAction }] }

end ResearchLeaves
