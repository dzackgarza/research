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

/-- Component realization, before named atom declarations are attached. -/
noncomputable def atomicModelComponents : AtomicModel.{u + 1, u} where
  foundations := foundationAtoms
  algebra := algebraAtoms
  modules := moduleAtoms
  exceptional := exceptionalAtoms

/-- Named atoms of the Mathlib realization. -/
noncomputable def namedCategory (id : CategoryId) : Option (ObjCat.{u + 1, u}) :=
  if id == CategoryId.sets then some (Normalized.Sets atomicModelComponents)
  else if id == CategoryId.magmas then some (Normalized.Magmas atomicModelComponents)
  else if id == CategoryId.semigroups then some (Normalized.Semigroups atomicModelComponents)
  else if id == CategoryId.monoids then some (Normalized.Monoids atomicModelComponents)
  else if id == CategoryId.groups then some (Normalized.Groups atomicModelComponents)
  else if id == CategoryId.rings then some (Normalized.Rings atomicModelComponents)
  else if id == CategoryId.commutativeRings then
    some (Normalized.CommutativeRings atomicModelComponents)
  else if id == CategoryId.divisionRings then some (Normalized.DivisionRings atomicModelComponents)
  else if id == CategoryId.additiveMagmas then
    some (Normalized.AdditiveMagmas atomicModelComponents)
  else if id == CategoryId.magmasWithTwoOperations then
    some (Normalized.MagmasWithTwoOperations atomicModelComponents)
  else if id == CategoryId.crystals then some atomicModelComponents.exceptional.Crystals
  else none

/-- The Mathlib realization of the atomic model. -/
noncomputable def atomicModel : AtomicModel.{u + 1, u} :=
  { atomicModelComponents with namedCategory }

@[simp] theorem evalAtom_sets :
    evalAtom atomicModel CategoryId.sets = some (Normalized.Sets atomicModel) := rfl

/-- Concrete binding used to evaluate the specimen family expression over `ℤ`. -/
def specimenRingBinding (id : RingParameterId) : Option RingCat.{0} :=
  if id == RingParameterId.r then some (RingCat.of ℤ) else none

example :
    (evalCategory atomicModel.{0} specimenRingBinding (.empty atomicModel)
      (.familyApp CategoryFamilyId.modules #[.ringVariable RingParameterId.r])).isSome = true := by
  simp [evalCategory, forgetfulToModules,
    Normalized.moduleParameter, specimenRingBinding]

example :
    (evalCategory atomicModel.{0} specimenRingBinding (.empty atomicModel)
      (.familyApp CategoryFamilyId.modules #[.opposite (.ringVariable RingParameterId.r)])).isSome =
      true := by
  change (some (Normalized.Modules atomicModel (oppositeRing (RingCat.of ℤ)))).isSome = true
  rfl

example :
    (evalCategory atomicModel.{0} specimenRingBinding (.empty atomicModel)
      (.familyApp CategoryFamilyId.modules #[])).isNone = true := by
  simp [evalCategory, forgetfulToModules]

example :
    (evalCategory atomicModel.{0} specimenRingBinding (.empty atomicModel)
      (.familyApp CategoryFamilyId.modules
        #[.ringVariable RingParameterId.r, .ringVariable RingParameterId.r])).isNone = true := by
  simp [evalCategory, forgetfulToModules]

/-- Normalized Magmas from the Mathlib model. -/
example : Normalized.Magmas atomicModel = Magmas := rfl

/-- The two-operation host is the categorical pullback. -/
example : Normalized.MagmasWithTwoOperations atomicModel = MagmasWithTwoOperations := rfl

end NormalizedCategoryGraph.Realization.Mathlib
