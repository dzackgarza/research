/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Core.Expr

/-!
# Registry entries

Declaration names are stored as strings (stable export identity). Lean `Name`
values are recovered at registration time by the command elaborator.
-/

namespace NormalizedCategoryGraph

/-- Named category registry row. -/
structure NamedCategoryEntry where
  id : CategoryId
  canonicalName : String
  declaration : String
  expression : CategoryExpr
  origin : CategoryOrigin
  visibility : Visibility
  deriving Repr, Inhabited

/-- Classifier registry row. -/
structure ClassifierEntry where
  id : ClassifierId
  canonicalName : String
  declaration : String
  hostId : CategoryId
  visibility : Visibility
  deriving Repr, Inhabited

/-- Spelling alias — does not create a semantic node. -/
structure AliasEntry where
  id : AliasId
  spelling : String
  aliasOf : CategoryId
  declaration : String
  deriving Repr, Inhabited

/-- Opaque category with typed structural ports. -/
structure StructuralPortEntry where
  id : OpaquePortId
  source : CategoryId
  target : CategoryId
  role : PortId
  declaration : String
  provenance : String
  deriving Repr, Inhabited

structure OpaqueCategoryEntry where
  id : CategoryId
  declaration : String
  ports : Array StructuralPortEntry
  reason : String
  visibility : Visibility
  deriving Repr, Inhabited

/-- Alternative presentation equivalence (not an alias). -/
structure PresentationEquivalenceEntry where
  source : CategoryId
  target : CategoryId
  declaration : String
  deriving Repr, Inhabited

/-- Aggregate registry snapshot for export (specimen / compiled). -/
structure RegistrySnapshot where
  schemaVersion : String
  categories : Array NamedCategoryEntry
  classifiers : Array ClassifierEntry
  aliases : Array AliasEntry
  opaqueCategories : Array OpaqueCategoryEntry
  equivalences : Array PresentationEquivalenceEntry
  deriving Repr, Inhabited

end NormalizedCategoryGraph
