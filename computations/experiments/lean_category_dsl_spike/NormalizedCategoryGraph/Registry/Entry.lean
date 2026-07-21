/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Core.Expr

/-!
# Registry entries

Declaration names are stored as Lean `Name` values.  JSON serialization is a
presentation concern; registration and environment lookup retain the checked
identity.
-/

namespace NormalizedCategoryGraph

/-- Named category registry row. -/
structure NamedCategoryEntry where
  id : CategoryId
  canonicalName : String
  declaration : Lean.Name
  expression : CategoryExpr
  origin : CategoryOrigin
  visibility : Visibility
  deriving Repr, Inhabited

/-- The sort of an explicitly bound category-family parameter. -/
inductive CategoryFamilyParameterKind
  | ringObject
  deriving DecidableEq, Repr, Inhabited

/-- Declared variance of a category family.  This does not assert a registered action on morphisms. -/
inductive CategoryFamilyVariance
  | restrictionOfScalarsContravariant
  deriving DecidableEq, Repr, Inhabited

/-- A bound parameter of a category family. -/
structure CategoryFamilyParameter where
  name : String
  kind : CategoryFamilyParameterKind
  deriving Repr, Inhabited

/--
A parameterized category family, distinct from any selected category node.

`fibreDeclaration` names the Lean declaration that accepts the bound parameter
and returns the corresponding category.  The registry records transport
orientation separately: a family value does not assert covariance.
-/
structure CategoryFamilyEntry where
  id : CategoryFamilyId
  canonicalName : String
  declaration : Lean.Name
  parameter : CategoryFamilyParameter
  fibreDeclaration : Lean.Name
  variance : CategoryFamilyVariance
  deriving Repr, Inhabited

/-- Classifier registry row. -/
structure ClassifierEntry where
  id : ClassifierId
  canonicalName : String
  declaration : Lean.Name
  hostId : CategoryId
  visibility : Visibility
  deriving Repr, Inhabited

/-- Spelling alias — does not create a semantic node. -/
structure AliasEntry where
  id : AliasId
  spelling : String
  aliasOf : CategoryId
  declaration : Lean.Name
  deriving Repr, Inhabited

/-- Opaque category with typed structural ports. -/
structure StructuralPortEntry where
  id : OpaquePortId
  source : CategoryId
  target : CategoryId
  role : PortId
  declaration : Lean.Name
  provenance : String
  deriving Repr, Inhabited

structure OpaqueCategoryEntry where
  id : CategoryId
  declaration : Lean.Name
  ports : Array StructuralPortEntry
  reason : String
  visibility : Visibility
  deriving Repr, Inhabited

/-- Alternative presentation equivalence (not an alias). -/
structure PresentationEquivalenceEntry where
  source : CategoryId
  target : CategoryId
  declaration : Lean.Name
  deriving Repr, Inhabited

/-- Aggregate registry snapshot for export (specimen / compiled). -/
structure RegistrySnapshot where
  schemaVersion : String
  categories : Array NamedCategoryEntry
  categoryFamilies : Array CategoryFamilyEntry
  classifiers : Array ClassifierEntry
  aliases : Array AliasEntry
  opaqueCategories : Array OpaqueCategoryEntry
  equivalences : Array PresentationEquivalenceEntry
  deriving Repr, Inhabited

end NormalizedCategoryGraph
