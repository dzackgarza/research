import CatDSL.Manifest.Tethers

/-!
# Pinning the tether state

The untethered list is COMPUTED from the environment (`untetheredIn`), never
self-reported.  This test pins it: a new notion with no checked Lean anchor
reds here until it is either tethered (`tether … ~ … via …`) or consciously
acknowledged below **with a documented reason** — an entry without a reason
does not typecheck.  Shrinking this list is the alignment-catalogue work
(#251); silent growth is the drift this mechanism exists to catch.

The positive assertions come first: a dead extension would pass any
"correctly absent" check.
-/

namespace CatDSL.TetherTest

open Lean Elab Command
open CatDSL.Manifest

-- Positive count first: the tether registry is alive.
run_cmd do
  let ts := tethers (← getEnv)
  unless ts.size = 15 do
    throwError "expected 15 tethers, got {ts.size}: {ts.map (·.localDecl)}"
  let kinds := ts.map (·.kind)
  unless kinds.count .exact = 4 && kinds.count .divergent = 1
      && kinds.count .structural = 10 do
    throwError "tether kinds drifted: {ts.map fun t => (t.localDecl, t.kind)}"
  logInfo m!"tether registry alive: {ts.size} tethers, kinds as pinned"

/-! ## Acknowledged reasons (shared) -/

private def bundleAbbrev : String :=
  "Cat.of bundle or surface alias naming an instance-carrying object type; \
   the notion is the object type, which is tethered or acknowledged \
   separately"

private def realizationEdge : String :=
  "realization functor (preferred-graph edge); its mathematical \
   characterization is CONSERVATIVITY (Functor.ReflectsIsomorphisms — see \
   the tethered Lattice.toFreeFinModule exemplar), not forgetfulness; \
   per-edge conservativity witnesses queued"

private def presentationData : String :=
  "presentation data, accessor, or concrete example on project objects; \
   internal by design, no external concept to anchor"

private def pendingUpstream : String :=
  "the surrounding CATEGORY has no Mathlib home (for lattices: ZLattice is \
   the embedded-discrete-subgroup ontology and QuadraticModuleCat is \
   quadratic, not symmetric bilinear — over ℤ exactly even vs odd); the \
   INGREDIENTS are tethered (LatticeObj.bilinForm ~ LinearMap.BilinForm); \
   see the ForMathlib policy"

/--
The acknowledged untethered set, each entry carrying its documented,
auditable reason.
-/
def acknowledgedUntethered : Array (Name × String) := #[
  (`CatDSL.Categories.CountableSet.forget, realizationEdge),
  (`CatDSL.Categories.CountableSets, bundleAbbrev),
  (`CatDSL.Categories.FiniteRing.toFiniteSet, realizationEdge),
  (`CatDSL.Categories.FiniteRing.toRing, realizationEdge),
  (`CatDSL.Categories.FiniteRingObj, pendingUpstream),
  (`CatDSL.Categories.FiniteRingObj.enumerate, presentationData),
  (`CatDSL.Categories.FiniteRingObj.prod, presentationData),
  (`CatDSL.Categories.FiniteRingObj.set, presentationData),
  (`CatDSL.Categories.FiniteRingObj.size, presentationData),
  (`CatDSL.Categories.FiniteRingObj.toFiniteSet, presentationData),
  (`CatDSL.Categories.FiniteRingObj.toRing, presentationData),
  (`CatDSL.Categories.FiniteRings, bundleAbbrev),
  (`CatDSL.Categories.FiniteSet.forget, realizationEdge),
  (`CatDSL.Categories.FiniteSet.toCountable, realizationEdge),
  (`CatDSL.Categories.FiniteSetObj.nth, presentationData),
  (`CatDSL.Categories.FiniteSetObj.number, presentationData),
  (`CatDSL.Categories.FiniteSetObj.prod, presentationData),
  (`CatDSL.Categories.FiniteSetObj.toCountable, presentationData),
  (`CatDSL.Categories.FiniteSets, bundleAbbrev),
  (`CatDSL.Categories.FreeFinModule.toFiniteSet, realizationEdge),
  (`CatDSL.Categories.FreeFinModule.toModule, realizationEdge),
  (`CatDSL.Categories.FreeFinModuleObj, pendingUpstream),
  (`CatDSL.Categories.FreeFinModuleObj.rankTwo, presentationData),
  (`CatDSL.Categories.FreeFinModules, bundleAbbrev),
  (`CatDSL.Categories.LatticeHom, pendingUpstream),
  (`CatDSL.Categories.LatticeObj.IsUnimodular, pendingUpstream),
  (`CatDSL.Categories.LatticeObj.standard, presentationData),
  (`CatDSL.Categories.LatticeObj.standardUnimodular, presentationData),
  (`CatDSL.Categories.Lattices, bundleAbbrev),
  (`CatDSL.Categories.Mod, bundleAbbrev),
  (`CatDSL.Categories.Module.forget, realizationEdge),
  (`CatDSL.Categories.ModuleObj.of, presentationData),
  (`CatDSL.Categories.Modules, bundleAbbrev),
  (`CatDSL.Categories.Ring.forget, realizationEdge),
  (`CatDSL.Categories.Rings, bundleAbbrev),
  (`CatDSL.Categories.Sets, bundleAbbrev),
  (`CatDSL.Categories.Unimodular.toLattice, realizationEdge),
  (`CatDSL.Categories.UnimodularLatticeObj, pendingUpstream),
  (`CatDSL.Categories.UnimodularLattices, bundleAbbrev)]


run_cmd liftTermElabM do
  let actual ← untetheredIn #[`CatDSL.Categories]
  let expected :=
    (acknowledgedUntethered.map (·.1)).qsort fun a b =>
      a.toString < b.toString
  unless actual = expected do
    let extra := actual.filter (!expected.contains ·)
    let gone := expected.filter (!actual.contains ·)
    throwError
      "untethered set drifted.\n\
       new untethered (tether them or acknowledge WITH a reason): {extra}\n\
       no longer untethered (remove from the acknowledged list): {gone}"
  logInfo m!"untethered set pinned: {actual.size} acknowledged notions, \
             each with a documented reason"

end CatDSL.TetherTest
