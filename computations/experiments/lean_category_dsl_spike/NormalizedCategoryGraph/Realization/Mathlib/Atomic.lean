/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Realization.Mathlib.Exceptional
import NormalizedCategoryGraph.Realization.Mathlib.Modules
import NormalizedCategoryGraph.Model.Interpretation

/-!
# Full Mathlib `AtomicModel`

Assembles foundation, algebra, module, and exceptional atoms into one model.
-/

namespace NormalizedCategoryGraph.Realization.Mathlib

open NormalizedCategoryGraph

universe u

set_option linter.checkUnivs false

/-- The Mathlib realization of the atomic model. -/
noncomputable def atomicModel : AtomicModel.{u + 1, u} where
  foundations := foundationAtoms
  algebra := algebraAtoms
  modules := moduleAtoms
  exceptional := exceptionalAtoms

/-- Concrete binding used to evaluate the specimen family expression over `ℤ`. -/
def specimenRingBinding (id : RingParameterId) : Option RingCat.{0} :=
  if id == RingParameterId.r then some (RingCat.of ℤ) else none

example :
    (evalCategory atomicModel.{0} specimenRingBinding
      (.familyApp CategoryFamilyId.modules #[.ringVariable RingParameterId.r])).isSome = true := by
  simp [evalCategory, forgetfulToModules, Normalized.moduleParameter, specimenRingBinding]

example :
    (evalCategory atomicModel.{0} specimenRingBinding
      (.familyApp CategoryFamilyId.modules #[.opposite (.ringVariable RingParameterId.r)])).isSome =
      true := by
  change (some (Normalized.Modules atomicModel (oppositeRing (RingCat.of ℤ)))).isSome = true
  rfl

example :
    (evalCategory atomicModel.{0} specimenRingBinding
      (.familyApp CategoryFamilyId.modules #[])).isNone = true := by
  simp [evalCategory, forgetfulToModules]

example :
    (evalCategory atomicModel.{0} specimenRingBinding
      (.familyApp CategoryFamilyId.modules
        #[.ringVariable RingParameterId.r, .ringVariable RingParameterId.r])).isNone = true := by
  simp [evalCategory, forgetfulToModules]

/-- Normalized Magmas from the Mathlib model. -/
example : Normalized.Magmas atomicModel = Magmas := rfl

/-- The two-operation host is the categorical pullback. -/
example : Normalized.MagmasWithTwoOperations atomicModel = MagmasWithTwoOperations := rfl

end NormalizedCategoryGraph.Realization.Mathlib
