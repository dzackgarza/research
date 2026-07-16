import CatDSL.Manifest.Tethers

/-!
# Pinning the tether state

The untethered list is COMPUTED from the environment (`untetheredIn`), never
self-reported.  This test pins it: a new notion with no checked Lean anchor
reds here until it is either tethered (`tether … ~ … via …`) or consciously
acknowledged below with its **mathematical identification** — what the
declaration IS in standard language, and what witness identifies it.  There
is no "plumbing" classification: everything is mathematics, translated;
entries differ only in whether their identification witness exists yet.

The positive assertions come first: a dead extension would pass any
"correctly absent" check.
-/

namespace CatDSL.TetherTest

open Lean Elab Command
open CatDSL.Manifest

-- Positive count first: the tether registry is alive.
run_cmd do
  let ts := tethers (← getEnv)
  unless ts.size = 20 do
    throwError "expected 20 tethers, got {ts.size}: {ts.map (·.localDecl)}"
  let kinds := ts.map (·.kind)
  unless kinds.count .exact = 5 && kinds.count .divergent = 2
      && kinds.count .structural = 13 do
    throwError "tether kinds drifted: {ts.map fun t => (t.localDecl, t.kind)}"
  logInfo m!"tether registry alive: {ts.size} tethers, kinds as pinned"

/-! ## Mathematical identifications of the not-yet-tethered (shared) -/

private def standardFunctor : String :=
  "a standard functor — forgetful, full-subcategory inclusion, or a \
   restriction square of these; identification witness (commuting square / \
   FullSubcategory.map) pending"

private def bundleOfCat : String :=
  "the category bundled as an object of Cat via Cat.of; the category itself \
   is the object type + instance (see the convention note in Sets.lean) and \
   is identified there"

private def routedSpelling : String :=
  "object-level spelling of an already-identified concept, reached through \
   the realization functor (X.op := F(X).op); not a new notion"

private def encodePresentation : String :=
  "Encodable.encode / Encodable.decode of the enumeration presentation \
   (identity witnessed by CountableSetObj.encodable / FiniteSetObj.finEnum)"

private def binaryProduct : String :=
  "the binary product construction; identification target: a limit-cone \
   witness that it IS the categorical product, pending"

private def fgFreeModules : String :=
  "the category of finitely generated free R-modules — full subcategory of \
   ModuleCat on Module.Free ∧ Module.Finite; equivalence witness pending \
   (supporting lemma: basis = Basis.ofEquivFun coordinates)"

private def finCommRings : String :=
  "the category of finite commutative rings — full subcategory of \
   CommRingCat on Finite; equivalence witness pending"

private def latticeCategory : String :=
  "the isometry category of nondegenerate symmetric bilinear f.g. free \
   modules — Mathlib has no home (ZLattice is the embedded-discrete-subgroup \
   ontology; QuadraticModuleCat is quadratic, not symmetric bilinear — over \
   ℤ exactly even vs odd); ForMathlib/upstream target; supporting lemmas: \
   bilinForm, bilinForm_isSymm"

private def supportingLemma : String :=
  "supporting lemma for a pending identification; its statement names the \
   Mathlib target"

private def workedExample : String :=
  "worked example — the identity-Gram form on the standard free \
   presentation, built entirely from identified pieces (standard, \
   Pi.basisFun.toDual)"

private def ofConstructor : String :=
  "object constructor corresponding to ModuleCat.of under the equivalence \
   ModuleObj.equivModuleCat"

/--
The acknowledged not-yet-tethered set: every entry carries its mathematical
identification.
-/
def acknowledgedUntethered : Array (Name × String) := #[
  (`CatDSL.Categories.CountableSet.forget, standardFunctor),
  (`CatDSL.Categories.CountableSets, bundleOfCat),
  (`CatDSL.Categories.FiniteRing.toFiniteSet, standardFunctor),
  (`CatDSL.Categories.FiniteRing.toRing, standardFunctor),
  (`CatDSL.Categories.FiniteRingObj, finCommRings),
  (`CatDSL.Categories.FiniteRingObj.enumerate, routedSpelling),
  (`CatDSL.Categories.FiniteRingObj.prod, binaryProduct),
  (`CatDSL.Categories.FiniteRingObj.set, routedSpelling),
  (`CatDSL.Categories.FiniteRingObj.toFiniteSet, routedSpelling),
  (`CatDSL.Categories.FiniteRingObj.toRing, routedSpelling),
  (`CatDSL.Categories.FiniteRings, bundleOfCat),
  (`CatDSL.Categories.FiniteSet.forget, standardFunctor),
  (`CatDSL.Categories.FiniteSet.toCountable, standardFunctor),
  (`CatDSL.Categories.FiniteSetObj.nth, encodePresentation),
  (`CatDSL.Categories.FiniteSetObj.number, encodePresentation),
  (`CatDSL.Categories.FiniteSetObj.prod, binaryProduct),
  (`CatDSL.Categories.FiniteSetObj.toCountable, routedSpelling),
  (`CatDSL.Categories.FiniteSets, bundleOfCat),
  (`CatDSL.Categories.FreeFinModule.toFiniteSet, standardFunctor),
  (`CatDSL.Categories.FreeFinModule.toModule, standardFunctor),
  (`CatDSL.Categories.FreeFinModuleObj, fgFreeModules),
  (`CatDSL.Categories.FreeFinModuleObj.basis, supportingLemma),
  (`CatDSL.Categories.FreeFinModules, bundleOfCat),
  (`CatDSL.Categories.LatticeHom, latticeCategory),
  (`CatDSL.Categories.LatticeObj, latticeCategory),
  (`CatDSL.Categories.LatticeObj.IsUnimodular, latticeCategory),
  (`CatDSL.Categories.LatticeObj.bilinForm, supportingLemma),
  (`CatDSL.Categories.LatticeObj.standard, workedExample),
  (`CatDSL.Categories.LatticeObj.standardUnimodular, workedExample),
  (`CatDSL.Categories.Lattices, bundleOfCat),
  (`CatDSL.Categories.Mod, bundleOfCat),
  (`CatDSL.Categories.ModuleObj.of, ofConstructor),
  (`CatDSL.Categories.Modules, bundleOfCat),
  (`CatDSL.Categories.Rings, bundleOfCat),
  (`CatDSL.Categories.Sets, bundleOfCat),
  (`CatDSL.Categories.UnimodularLatticeObj, latticeCategory),
  (`CatDSL.Categories.UnimodularLattices, bundleOfCat)]

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
       new untethered (tether or identify): {extra}\n\
       no longer untethered (remove from the acknowledged list): {gone}"
  logInfo m!"untethered set pinned: {actual.size} notions, each with its \
             mathematical identification"

end CatDSL.TetherTest
