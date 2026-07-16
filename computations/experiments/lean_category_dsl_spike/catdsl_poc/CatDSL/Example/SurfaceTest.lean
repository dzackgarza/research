import CatDSL.Syntax
import CatDSL.Example.F2Semantic

/-!
# The surface syntax, exercised

`Syntax.lean` compiling proves nothing; these commands must actually run.

Per the review's ordering, the semantics were proved first in
`F2Semantic.lean` with no DSL syntax at all.  This file only checks that the
surface *names* those already-working constructions — so a failure here is a
failure of the elaborator, and cannot be confused with a failure of the
mathematics.
-/

namespace CatDSL.SurfaceTest

open CatDSL CatDSL.Categories CatDSL.DSL

/-! ## `prefer F` — registry state via the surface -/

prefer CatDSL.Categories.Lattice.toFreeFinModule
prefer CatDSL.Categories.FreeFinModule.toFiniteSet
prefer CatDSL.Categories.FreeFinModule.toModule
prefer CatDSL.Categories.Module.forget
prefer CatDSL.Categories.FiniteSet.toCountable
prefer CatDSL.Categories.FiniteSet.forget
prefer CatDSL.Categories.CountableSet.forget

/-! ## `let X := t ∈ 𝒞` — a paper-like declaration -/

let L := CatDSL.Example.L ∈ CatDSL.Categories.Lattices CatDSL.Categories.𝔽₂

/-! ## `#home` and `#via` — the graph queries -/

#home L

#via L ∈ CatDSL.Categories.FreeFinModules CatDSL.Categories.𝔽₂
#via L ∈ CatDSL.Categories.FiniteSets
#via L ∈ CatDSL.Categories.CountableSets
#via L ∈ CatDSL.Categories.Sets

/--
The surface `let` really produced an ordinary Lean declaration of type
`Object 𝒞`, definitionally the object it names.  That is the whole claim of
the declaration layer: no second table, no metadata — the generated type
carries the category.
-/
theorem surface_L_is_semantic_L : L = CatDSL.Example.L := rfl

end CatDSL.SurfaceTest
