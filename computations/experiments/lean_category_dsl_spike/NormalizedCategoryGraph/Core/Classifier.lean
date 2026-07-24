/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import NormalizedCategoryGraph.Core.Universes
import Mathlib.CategoryTheory.Functor.FullyFaithful

/-!
# Classifier

The fundamental object: for an axiom/structure `A` on `C`,

\[
A = (\iota_A : C.A \to C).
\]

Property / structure / stuff are consequences of fullness and faithfulness of
`forget`, not an authored enum. The manifest may report `property` only when a
proof declaration supports it.
-/

namespace NormalizedCategoryGraph

open CategoryTheory

universe uObj uHom

/-- Minimal classifier datum on a host category. -/
structure Classifier (C : ObjCat.{uObj, uHom}) where
  total : ObjCat.{uObj, uHom}
  forget : total ⟶ C

/-- Property classifier: full, faithful, and replete (when repleteness is available).
Manifest `kind := property` requires these proofs — never an unchecked tag. -/
structure PropertyClassifier (C : ObjCat.{uObj, uHom}) extends Classifier C where
  full : forget.toFunctor.Full
  faithful : forget.toFunctor.Faithful

/-- Structure classifier: faithful forgetful (not necessarily full). -/
structure StructureClassifier (C : ObjCat.{uObj, uHom}) extends Classifier C where
  faithful : forget.toFunctor.Faithful

end NormalizedCategoryGraph
