/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import Mathlib.CategoryTheory.Category.Cat

/-!
# Universe tower vs mathematical Cat

Lean universe levels are implementation provenance. Manifest IDs must not contain them.

`ObjCat` uses object universe `max uObj uHom` so Mathlib's `CategoricalPullback`
(whose type lives in `Type (max uObj uHom)`) packs back into `Cat` without a
universe bump mismatch.
-/

namespace NormalizedCategoryGraph

universe uObj uHom uMetaObj uMetaHom

-- Twin levels are intentional for Cat packing; they only appear jointly.
set_option linter.checkUnivs false

/-- The universe of ordinary categories (Sets, Magmas, Rings, …). -/
abbrev ObjCat := CategoryTheory.Cat.{uHom, max uObj uHom}

/-- The universe one stratum above: categories of categories. -/
abbrev MetaCat := CategoryTheory.Cat.{uMetaHom, max uMetaObj uMetaHom}

end NormalizedCategoryGraph
