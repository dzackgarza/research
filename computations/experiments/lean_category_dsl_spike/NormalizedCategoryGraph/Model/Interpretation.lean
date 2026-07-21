/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Core.Expr
import NormalizedCategoryGraph.Model.Atomic

/-!
# Interpretation — evaluate known atoms in an atomic model

Maps stable `CategoryId`s that the atomic model owns to their `ObjCat`
interpretations. Full Spec-driven expression evaluation walks the registry
and uses these atoms as leaves.
-/

namespace NormalizedCategoryGraph

open Normalized

universe uObj uHom

/-- Interpret foundation / algebra / module / exceptional atoms of `M`. -/
noncomputable def evalAtom (M : AtomicModel.{uObj, uHom}) (id : CategoryId) :
    Option (ObjCat.{uObj, uHom}) :=
  if id == CategoryId.sets then some (Sets M)
  else if id == CategoryId.magmas then some (Magmas M)
  else if id == CategoryId.semigroups then some (Semigroups M)
  else if id == CategoryId.monoids then some (Monoids M)
  else if id == CategoryId.groups then some (Groups M)
  else if id == CategoryId.rings then some (Rings M)
  else if id == CategoryId.commutativeRings then some (CommutativeRings M)
  else if id == CategoryId.modulesR then some (Modules M)
  else if id == CategoryId.magmasWithTwoOperations then
    some M.exceptional.MagmasWithTwoOperations
  else if id == CategoryId.crystals then some M.exceptional.Crystals
  else none

/-- Evaluate a category expression whose leaves are atomic-model atoms. -/
noncomputable def evalCategory (M : AtomicModel.{uObj, uHom}) :
    CategoryExpr → Option (ObjCat.{uObj, uHom})
  | .atom id => evalAtom M id
  | .opaque id => evalAtom M id
  | .reference id => evalAtom M id
  | .classifierTotal _ => none
  | .refine base _ _ => evalCategory M base
  | .familyApp _ _ => none
  | .constructor _ _ => none

end NormalizedCategoryGraph
