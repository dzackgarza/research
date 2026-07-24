/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Categories.Algebra.Rings
import NormalizedCategoryGraph.Core.Ids

/-!
# Standard names and spelling aliases

Aliases do not create semantic nodes. `CRings` is recorded as `aliasOf`
`cat.commutative_rings`.
-/

namespace NormalizedCategoryGraph.Names

open NormalizedCategoryGraph

abbrev CommutativeRings := Categories.Algebra.Rings.CommutativeRings

/-- Spelling alias — registry id `alias.crings`. -/
abbrev CRings := CategoryId.commutativeRings

example : AliasId.crings.raw = "alias.crings" := by rfl

end NormalizedCategoryGraph.Names
