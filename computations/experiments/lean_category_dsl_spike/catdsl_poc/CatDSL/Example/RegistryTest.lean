import CatDSL.Registry
import CatDSL.Example.F2Semantic

/-!
# Executing the registry

`Registry.lean` compiling proves nothing about whether it *works*.  Every
result so far composed the preferred functors by hand; this file makes the
resolver discover, instantiate, compose, and apply them.

The final test is the one that matters: the path the registry finds must
produce the same finite set that `F2Semantic.Lfin` builds manually.  That
connects the metaprogram to the already-proved semantics.
-/

namespace CatDSL.RegistryTest

open Lean Elab Command Meta
open CatDSL CatDSL.Registry CatDSL.Categories

/-! ## Register the 𝔽₂ preferred-functor graph -/

run_cmd do
  for e in [``CatDSL.Categories.Unimodular.toLattice,
            ``CatDSL.Categories.Lattice.toFreeFinModule,
            ``CatDSL.Categories.FreeFinModule.toFiniteSet,
            ``CatDSL.Categories.FreeFinModule.toModule,
            ``CatDSL.Categories.Module.forget,
            ``CatDSL.Categories.FiniteSet.toCountable,
            ``CatDSL.Categories.FiniteSet.forget,
            ``CatDSL.Categories.CountableSet.forget,
            ``CatDSL.Categories.Ring.forget,
            ``CatDSL.Categories.FiniteRing.toRing,
            ``CatDSL.Categories.FiniteRing.toFiniteSet] do
    liftTermElabM <| Registry.checkPreferredFunctor e
    liftCoreM <| Registry.addPreferredFunctor e

-- The edges really landed in the extension.
run_cmd do
  let names := Registry.preferredFunctorNames (← getEnv)
  unless names.size = 11 do
    throwError "expected 11 registered edges, got {names.size}: {names}"
  logInfo m!"registry holds {names.size} edges"

/-! ## checkPreferredFunctor rejects a non-functor -/

run_cmd do
  -- `𝔽₂` is an object, not a functor: registering it must fail.
  let ok ← try
      liftTermElabM <| Registry.checkPreferredFunctor ``CatDSL.Categories.𝔽₂
      pure true
    catch _ => pure false
  if ok then
    throwError "checkPreferredFunctor accepted 𝔽₂, which is not a functor"
  logInfo "non-functor correctly rejected"

/-! ## Path resolution -/

-- The whole point: starting from `Lat(𝔽₂)`, the resolver must reach
-- `FiniteSets` on its own -- discovering the edges, inferring `R := 𝔽₂` for the
-- parameterized families, and composing.
run_cmd liftTermElabM do
  let src ← Term.elabTerm (← `(CatDSL.Categories.Lattices CatDSL.Categories.𝔽₂)) none
  let tgt ← Term.elabTerm (← `(CatDSL.Categories.FiniteSets)) none
  let src ← instantiateMVars src
  let tgt ← instantiateMVars tgt
  let path ← Registry.resolvePath src tgt
  logInfo m!"Lat(𝔽₂) ⇝ FiniteSets via {Registry.pathNames path}"
  unless path.steps.size = 2 do
    throwError "expected a 2-step path, got {path.steps.size}"

-- The composite reaches `CountableSets` too, in three steps.
run_cmd liftTermElabM do
  let src ← Term.elabTerm (← `(CatDSL.Categories.Lattices CatDSL.Categories.𝔽₂)) none
  let tgt ← Term.elabTerm (← `(CatDSL.Categories.CountableSets)) none
  let path ← Registry.resolvePath (← instantiateMVars src) (← instantiateMVars tgt)
  logInfo m!"Lat(𝔽₂) ⇝ CountableSets via {Registry.pathNames path}"

-- From the unimodular full subcategory, the resolver must discover the
-- inclusion as the first step: UnimodularLat(𝔽₂) ⇝ FiniteSets in 3 steps.
run_cmd liftTermElabM do
  let src ← Term.elabTerm
    (← `(CatDSL.Categories.UnimodularLattices CatDSL.Categories.𝔽₂)) none
  let tgt ← Term.elabTerm (← `(CatDSL.Categories.FiniteSets)) none
  let path ← Registry.resolvePath (← instantiateMVars src) (← instantiateMVars tgt)
  logInfo m!"UnimodularLat(𝔽₂) ⇝ FiniteSets via {Registry.pathNames path}"
  unless path.steps.size = 3 do
    throwError "expected a 3-step path through the inclusion, got {path.steps.size}"

-- And the discovered inclusion-extended path applied to `Lu` is
-- definitionally the same finite set the semantics builds from `L`.
run_cmd liftTermElabM do
  let src ← instantiateMVars
    (← Term.elabTerm (← `(CatDSL.Categories.UnimodularLattices CatDSL.Categories.𝔽₂)) none)
  let tgt ← instantiateMVars (← Term.elabTerm (← `(CatDSL.Categories.FiniteSets)) none)
  let path ← Registry.resolvePath src tgt
  let Lu ← instantiateMVars (← Term.elabTerm (← `(CatDSL.Example.Lu)) none)
  let resolved ← Registry.applyPath path Lu
  let manual ← instantiateMVars (← Term.elabTerm (← `(CatDSL.Example.Lfin)) none)
  unless ← Meta.isDefEq resolved manual do
    throwError
      "unimodular-resolved realization differs from the manual one:\n\
       resolved: {resolved}\nmanual:   {manual}"
  logInfo m!"unimodular registry path ≡ hand-built Lfin"

-- Reflexivity: a category resolves to itself in zero steps.
run_cmd liftTermElabM do
  let c ← Term.elabTerm (← `(CatDSL.Categories.FiniteSets)) none
  let path ← Registry.resolvePath (← instantiateMVars c) (← instantiateMVars c)
  unless path.steps.size = 0 do
    throwError "self-path should be empty, got {path.steps.size}"

-- An unreachable target must fail, not silently succeed.
run_cmd liftTermElabM do
  let src ← Term.elabTerm (← `(CatDSL.Categories.Sets)) none
  let tgt ← Term.elabTerm (← `(CatDSL.Categories.Lattices CatDSL.Categories.𝔽₂)) none
  let ok ← try
      let _ ← Registry.resolvePath (← instantiateMVars src) (← instantiateMVars tgt)
      pure true
    catch _ => pure false
  if ok then
    throwError "resolver claimed Sets ⇝ Lat(𝔽₂), which has no preferred path"
  logInfo "unreachable target correctly rejected"

/-!
## Closing the loop

Everything above shows the registry finds a path.  This shows the path it
finds is the *same* one `F2Semantic` built by hand -- otherwise the two are
independent results that merely agree by inspection.

`applyPath` composes the discovered functors and applies them to `L`; the
result must be definitionally the manually-composed `Lfin`.
-/

run_cmd liftTermElabM do
  let src ← instantiateMVars (← Term.elabTerm (← `(CatDSL.Categories.Lattices CatDSL.Categories.𝔽₂)) none)
  let tgt ← instantiateMVars (← Term.elabTerm (← `(CatDSL.Categories.FiniteSets)) none)
  let path ← Registry.resolvePath src tgt
  -- apply the discovered composite to L
  let L ← instantiateMVars (← Term.elabTerm (← `(CatDSL.Example.L)) none)
  let resolved ← Registry.applyPath path L
  -- and to what F2Semantic built by hand
  let manual ← instantiateMVars (← Term.elabTerm (← `(CatDSL.Example.Lfin)) none)
  unless ← Meta.isDefEq resolved manual do
    throwError
      "registry-resolved realization differs from the manual one:\n\
       resolved: {resolved}\nmanual:   {manual}"
  logInfo m!"registry path ≡ hand-built Lfin"

/-!
## Multiple paths, and why membership resolution is not operation dispatch

`Lat(𝔽₂) ⇝ Sets` has two preferred routes:

    Lat → FreeFinMod → Mod → Set                       (3 steps)
    Lat → FreeFinMod → FiniteSet → CountableSet → Set  (4 steps)

Membership is existential, so either witnesses `L ∈ Set` and BFS is entitled
to return the shorter one.  But only the *longer* route passes through the
finite presentation that `number`, `nth`, and `cardinality` are read from.

So `resolvePath` cannot be the dispatcher for `|L|`: the shortest path to
`Set` reaches no implementation of cardinality at all.  Membership resolution
and operation-implementation resolution are different searches over the same
graph.  This test records which route is taken, so the distinction is a fact
rather than an argument.
-/

run_cmd liftTermElabM do
  let src ← instantiateMVars (← Term.elabTerm (← `(CatDSL.Categories.Lattices CatDSL.Categories.𝔽₂)) none)
  let tgt ← instantiateMVars (← Term.elabTerm (← `(CatDSL.Categories.Sets)) none)
  let path ← Registry.resolvePath src tgt
  logInfo m!"Lat(𝔽₂) ⇝ Sets selected ({path.steps.size} steps): {Registry.pathNames path}"

end CatDSL.RegistryTest
