import CatDSL.Manifest.Tether
import CatDSL.Categories.Lattices

/-!
# The tether registrations

One `tether` per anchored notion; the kind (exact / divergent / structural)
is computed from the witness, never declared.  Everything NOT registered
here surfaces in `untetheredIn` / `#tether_report` — that computed
complement, pinned by `Example/TetherTest.lean`, is the honest list of
notions with no checked Lean anchor.
-/

namespace CatDSL.Manifest

tether CatDSL.Categories.SetObj ~ CategoryTheory.types
  via CatDSL.Categories.SetObj.equivTypes

tether CatDSL.Categories.RingObj ~ CommRingCat
  via CatDSL.Categories.RingObj.equivCommRingCat

tether CatDSL.Categories.ModuleObj ~ ModuleCat
  via CatDSL.Categories.ModuleObj.equivModuleCat

tether CatDSL.Categories.SetObj.cardinality ~ Cardinal.mk
  via CatDSL.Categories.SetObj.cardinality_eq_mk

tether CatDSL.Categories.ModuleHom.index ~ AddSubgroup.index
  via CatDSL.Categories.ModuleHom.index_eq_addSubgroupIndex

tether CatDSL.Categories.CountableSetObj ~ Encodable
  via CatDSL.Categories.CountableSetObj.encodable

tether CatDSL.Categories.FiniteSetObj ~ FinEnum
  via CatDSL.Categories.FiniteSetObj.finEnum

tether CatDSL.Categories.integers ~ Int
  via CatDSL.Categories.integers.equivInt

tether CatDSL.Categories.two ~ ZMod
  via CatDSL.Categories.two.equivZMod

tether CatDSL.Categories.𝔽₂ ~ ZMod
  via CatDSL.Categories.𝔽₂.equivZMod

tether CatDSL.Categories.cardinality ~ FinEnum.card
  via CatDSL.Categories.cardinality_eq_finEnumCard

tether CatDSL.Categories.Isometries ~ CategoryTheory.Iso
  via CatDSL.Categories.Isometries.eq_iso

tether CatDSL.Categories.isometryGroup ~ CategoryTheory.Aut
  via CatDSL.Categories.isometryGroup.eq_aut

tether CatDSL.Categories.Lattice.toFreeFinModule
  ~ CategoryTheory.Functor.ReflectsIsomorphisms
  via CatDSL.Categories.Lattice.toFreeFinModule_reflectsIsomorphisms

tether CatDSL.Categories.CountableSetObj ~ Countable
  via CatDSL.Categories.CountableSetObj.equivCountableSets

tether CatDSL.Categories.FiniteSetObj ~ Finite
  via CatDSL.Categories.FiniteSetObj.equivFiniteSets

tether CatDSL.Categories.FreeFinModuleObj.standard ~ Pi.basisFun
  via CatDSL.Categories.FreeFinModuleObj.standard_basis

tether CatDSL.Categories.Ring.forget ~ CategoryTheory.forget
  via CatDSL.Categories.Ring.forget_eq_forget

tether CatDSL.Categories.Module.forget ~ CategoryTheory.forget
  via CatDSL.Categories.Module.forget_eq_forget

tether CatDSL.Categories.Unimodular.toLattice ~ CategoryTheory.ObjectProperty.ι
  via CatDSL.Categories.Unimodular.toLattice_eq_ι

end CatDSL.Manifest
