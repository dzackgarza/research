/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Realization.Mathlib.Exceptional
import NormalizedCategoryGraph.Realization.Mathlib.Modules

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

/-- Normalized Magmas from the Mathlib model. -/
example : Normalized.Magmas atomicModel = Magmas := rfl

/-- Normalized Rings is the two-operation product host. -/
example : Normalized.Rings atomicModel = MagmasWithTwoOperations := rfl

end NormalizedCategoryGraph.Realization.Mathlib
