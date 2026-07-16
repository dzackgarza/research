import CatDSL.Manifest.Tethers

/-!
# Pinning the tether state

The untethered list is COMPUTED from the environment (`untetheredIn`), never
self-reported.  This test pins it: a new notion with no checked Lean anchor
reds here until it is either tethered (`tether … ~ … via …`) or consciously
added below.  Shrinking this list is the alignment-catalogue work (#251);
silent growth is the drift this mechanism exists to catch.

The positive assertions come first: a dead extension would pass any
"correctly absent" check.
-/

namespace CatDSL.TetherTest

open Lean Elab Command
open CatDSL.Manifest

-- Positive count first: the tether registry is alive.
run_cmd do
  let ts := tethers (← getEnv)
  unless ts.size = 4 do
    throwError "expected 4 tethers, got {ts.size}: {ts.map (·.localDecl)}"
  let kinds := ts.map (·.kind)
  unless kinds.count .exact = 1 && kinds.count .divergent = 1
      && kinds.count .structural = 2 do
    throwError "tether kinds drifted: {ts.map fun t => (t.localDecl, t.kind)}"
  logInfo m!"tether registry alive: {ts.size} tethers, kinds as pinned"

/--
The acknowledged untethered set: every notion here has NO checked tie to a
Lean/Mathlib declaration yet.  Bundles, realization functors, and accessors
are project glue awaiting their catalogue adjudication; `LatticeObj` and
friends are pending upstream theory; `RingObj`/`ModuleObj` are the
#217-ratified consolidation queue.
-/
def acknowledgedUntethered : Array Name := #[
  `CatDSL.Categories.CountableSet.forget,
  `CatDSL.Categories.CountableSets,
  `CatDSL.Categories.FiniteRing.toFiniteSet,
  `CatDSL.Categories.FiniteRing.toRing,
  `CatDSL.Categories.FiniteRingObj,
  `CatDSL.Categories.FiniteRingObj.enumerate,
  `CatDSL.Categories.FiniteRingObj.prod,
  `CatDSL.Categories.FiniteRingObj.set,
  `CatDSL.Categories.FiniteRingObj.size,
  `CatDSL.Categories.FiniteRingObj.toFiniteSet,
  `CatDSL.Categories.FiniteRingObj.toRing,
  `CatDSL.Categories.FiniteRings,
  `CatDSL.Categories.FiniteSet.forget,
  `CatDSL.Categories.FiniteSet.toCountable,
  `CatDSL.Categories.FiniteSetObj.nth,
  `CatDSL.Categories.FiniteSetObj.number,
  `CatDSL.Categories.FiniteSetObj.prod,
  `CatDSL.Categories.FiniteSetObj.toCountable,
  `CatDSL.Categories.FiniteSets,
  `CatDSL.Categories.FreeFinModule.toFiniteSet,
  `CatDSL.Categories.FreeFinModule.toModule,
  `CatDSL.Categories.FreeFinModuleObj,
  `CatDSL.Categories.FreeFinModuleObj.rankTwo,
  `CatDSL.Categories.FreeFinModules,
  `CatDSL.Categories.Isometries,
  `CatDSL.Categories.Lattice.toFreeFinModule,
  `CatDSL.Categories.LatticeHom,
  `CatDSL.Categories.LatticeObj,
  `CatDSL.Categories.LatticeObj.IsUnimodular,
  `CatDSL.Categories.LatticeObj.standard,
  `CatDSL.Categories.LatticeObj.standardUnimodular,
  `CatDSL.Categories.Lattices,
  `CatDSL.Categories.Mod,
  `CatDSL.Categories.Module.forget,
  `CatDSL.Categories.ModuleObj,
  `CatDSL.Categories.ModuleObj.of,
  `CatDSL.Categories.Modules,
  `CatDSL.Categories.Ring.forget,
  `CatDSL.Categories.RingObj,
  `CatDSL.Categories.Rings,
  `CatDSL.Categories.SetObj,
  `CatDSL.Categories.Sets,
  `CatDSL.Categories.Unimodular.toLattice,
  `CatDSL.Categories.UnimodularLatticeObj,
  `CatDSL.Categories.UnimodularLattices,
  `CatDSL.Categories.cardinality,
  `CatDSL.Categories.integers,
  `CatDSL.Categories.isometryGroup,
  `CatDSL.Categories.two,
  `CatDSL.Categories.𝔽₂]

run_cmd liftTermElabM do
  let actual ← untetheredIn #[`CatDSL.Categories]
  let expected :=
    acknowledgedUntethered.qsort fun a b => a.toString < b.toString
  unless actual = expected do
    let extra := actual.filter (!expected.contains ·)
    let gone := expected.filter (!actual.contains ·)
    throwError
      "untethered set drifted.\n\
       new untethered (tether them or acknowledge): {extra}\n\
       no longer untethered (remove from the acknowledged list): {gone}"
  logInfo m!"untethered set pinned: {actual.size} acknowledged notions"

end CatDSL.TetherTest
