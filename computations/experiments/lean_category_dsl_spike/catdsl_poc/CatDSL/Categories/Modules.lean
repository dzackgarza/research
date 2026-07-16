import CatDSL.Categories.Rings

/-!
# Modules and finite free modules

Object types + Mathlib `Category` instances, bundled with `Cat.of`; functors
between object types, never between bundles (see `Categories/Rings.lean`).
-/

namespace CatDSL.Categories

open CategoryTheory CatDSL

/-- A small module over a fixed small ring. -/
structure ModuleObj (R : RingObj) where
  set : Type
  addCommGroup : AddCommGroup set
  module : Module R.set set

attribute [instance] ModuleObj.addCommGroup ModuleObj.module

instance (R : RingObj) : CoeSort (ModuleObj R) Type where
  coe M := M.set

/--
Bridge `Module R.set M.set` for a finite ring `R`.

`ModuleObj.module` is stated over the structure's own parameter, so for
`M : ModuleObj R.toRing` it yields `Module R.toRing.set M.set`.  That is
definitionally `Module R.set M.set`, but instance search will not discover
it: the two differ by unfolding `toRing` and projecting, which is not
something resolution does while matching an instance head.  Stating it is
cheaper and clearer than making every downstream type mention
`R.toRing.set`.
-/
instance moduleOverFiniteRing (R : FiniteRingObj) (M : ModuleObj R.toRing) :
    Module R.set M.set :=
  M.module

namespace ModuleObj

def of (R : RingObj) (M : Type)
    [AddCommGroup M] [Module R.set M] : ModuleObj R where
  set := M
  addCommGroup := inferInstance
  module := inferInstance

end ModuleObj

instance (R : RingObj) : Category (ModuleObj R) where
  Hom M N := M.set →ₗ[R.set] N.set
  id _ := LinearMap.id
  comp f g := g.comp f

abbrev Modules (R : RingObj) : LargeCat := Cat.of (ModuleObj R)

/--
Tether witness: our category of `R`-modules IS Mathlib's `ModuleCat R.set`,
as an equivalence of categories — the #217 consolidation claim
kernel-checked before any structure retirement.
-/
def ModuleObj.equivModuleCat (R : RingObj) :
    ModuleObj R ≌ ModuleCat R.set where
  functor :=
    { obj := fun M => ModuleCat.of R.set M.set
      map := fun {M N} (f : M.set →ₗ[R.set] N.set) => ModuleCat.ofHom f }
  inverse :=
    { obj := fun X =>
        { set := X.carrier
          addCommGroup := inferInstance
          module := inferInstance }
      map := fun f => f.hom }
  unitIso := NatIso.ofComponents fun M => Iso.refl _
  counitIso := NatIso.ofComponents fun X => Iso.refl _

/-- Surface category family `Mod(R)`. -/
abbrev Mod (R : FiniteRingObj) : LargeCat :=
  Modules R.toRing

/-- The `Set`-realization of a module. -/
def Module.forget (R : FiniteRingObj) : ModuleObj R.toRing ⥤ SetObj where
  obj M := ⟨M.set⟩
  map {M N} (f : M.set →ₗ[R.set] N.set) := ⇑f

/-- Tether witness: `Module.forget` IS Mathlib's forgetful functor on
`ModuleCat`, transported across the equivalence (see
`Ring.forget_eq_forget`). -/
def Module.forget_eq_forget (R : FiniteRingObj) :
    (ModuleObj.equivModuleCat R.toRing).functor ⋙ CategoryTheory.forget (ModuleCat R.set) ≅
      Module.forget R ⋙ SetObj.equivTypes.functor :=
  NatIso.ofComponents fun M => Iso.refl _

/--
A finite free module with chosen coordinates and a chosen concrete finite
realization of its underlying set.

The chosen finite realization is the implementation data that lets the
preferred functor land in `FiniteSets`, not merely in `Sets`.
-/
structure FreeFinModuleObj (R : FiniteRingObj) where
  module : ModuleObj R.toRing
  rank : Nat
  coordinates :
    module.set ≃ₗ[R.set] (Fin rank → R.set)
  finiteSet : FiniteSetObj
  finiteSetEquiv : module.set ≃ finiteSet.set
  cardinality_eq : finiteSet.card = R.finiteSet.card ^ rank

instance (R : FiniteRingObj) : CoeSort (FreeFinModuleObj R) Type where
  coe M := M.module.set

namespace FreeFinModuleObj

/--
The standard presentation of the free module of rank `n`: the function
module `Fin n → R` with identity coordinates, enumerated by Mathlib's
`finFunctionFinEquiv` (little-endian mixed radix) through the base ring's
enumeration.

This is the GENERAL definition; examples instantiate it (`n = 2` for the
standard lattice).  Special cases are recovered, never named — there is no
`rankTwo`.
-/
def standard (R : FiniteRingObj) (n : Nat) : FreeFinModuleObj R where
  module := ModuleObj.of R.toRing (Fin n → R.set)
  rank := n
  coordinates := LinearEquiv.refl R.set (Fin n → R.set)
  finiteSet :=
    { set := Fin n → R.set
      card := R.finiteSet.card ^ n
      enumerate :=
        (Equiv.arrowCongr (Equiv.refl (Fin n)) R.finiteSet.enumerate).trans
          finFunctionFinEquiv }
  finiteSetEquiv := Equiv.refl _
  cardinality_eq := rfl

/--
Tether witness: the `coordinates` field IS a Mathlib basis — a finitely
generated free module of rank `rank` with chosen coordinates is exactly a
module with a `Module.Basis (Fin rank)` (`Basis.ofEquivFun`).
-/
noncomputable def basis {R : FiniteRingObj} (M : FreeFinModuleObj R) :
    Module.Basis (Fin M.rank) R.set M.module.set :=
  Module.Basis.ofEquivFun M.coordinates

/-- Tether witness: the standard presentation's basis is Mathlib's standard
basis, definitionally, at every rank (`Pi.basisFun` is itself
`Basis.ofEquivFun (LinearEquiv.refl _ _)`). -/
theorem standard_basis (R : FiniteRingObj) (n : Nat) :
    (standard R n).basis = Pi.basisFun R.set (Fin n) :=
  rfl

end FreeFinModuleObj

instance (R : FiniteRingObj) : Category (FreeFinModuleObj R) where
  Hom M N := M.module.set →ₗ[R.set] N.module.set
  id _ := LinearMap.id
  comp f g := g.comp f

abbrev FreeFinModules (R : FiniteRingObj) : LargeCat := Cat.of (FreeFinModuleObj R)

/-- The `Mod(R)`-realization of a finite free module. -/
def FreeFinModule.toModule (R : FiniteRingObj) :
    FreeFinModuleObj R ⥤ ModuleObj R.toRing where
  obj M := M.module
  map f := f

/-- The `FiniteSet`-realization of a finite free module. -/
def FreeFinModule.toFiniteSet (R : FiniteRingObj) :
    FreeFinModuleObj R ⥤ FiniteSetObj where
  obj M := M.finiteSet
  -- explicit binder type so `f` is a LinearMap that can be applied
  map {M N} (f : M.module.set →ₗ[R.set] N.module.set) :=
    fun x => N.finiteSetEquiv (f (M.finiteSetEquiv.symm x))
  map_id M := by
    funext x
    exact M.finiteSetEquiv.apply_symm_apply x
  map_comp {M N P} f g := by
    funext x
    -- `≫` is `LinearMap.comp` on the left and function composition on the
    -- right; unfold both, then N's equiv cancels in the middle.
    simp only [CategoryStruct.comp, LinearMap.coe_comp, Function.comp_apply,
               Equiv.symm_apply_apply]

/-!
## Morphism-sited operations

Operations whose input is a morphism are typed on the morphism — they cannot
be spelled without constructing it (the ratified method-placement doctrine).
-/

namespace ModuleHom

/--
The **index** `[N : f(M)]` of a module morphism `f : M ⟶ N`: the cardinality
of its cokernel `N ⧸ range f`.

*Home.*  Morphisms of `Mod(R)`.  The operation is meaningful here with no
extra hypothesis because `Mod(R)` is abelian — every morphism has a cokernel.
Contrast groups: the image of a group homomorphism need not be normal, the
coset object exists only as a set, and no such operation can be declared on
`Grp`'s morphisms with this definition.

*Value.*  A `Cardinal`; finite exactly when the image has finite colength
(for `ℤ`-lattices: full rank).  The Sage realization spells the value in the
extended scalars `ℤ ∪ {∞}` (`domain_algebra.py`, morphism-sited geometry
per #100).

*Name adjudication (manifest finding).*  The Sage spike carries TWO distinct
operations named `index`: this one, morphism-sited (`domain_algebra.py:868`),
and `Lattice.index(element)` — reverse enumeration lookup, the inverse of
`__getitem__` (`domain_algebra.py:358`), whose honest concept is
`CountableSetObj.number` (= Mathlib's `Encodable.encode`) and whose home is
numbering-equipped countable sets.  The alignment manifest must give the two
distinct concept identities; `list.index` idiom notwithstanding, they share
nothing but the string.

*Mathlib alignment.*  Mathlib owns this concept as `AddSubgroup.index` /
`Subgroup.index` (`Nat.card (G ⧸ H)`, sited on the subobject, ℕ-valued with
the 0-for-infinite convention).  This declaration is that invariant applied
to `range f` — the subobject a morphism carries — stated convention-free in
cardinals; `index_toNat` connects the two value conventions by `rfl`.  The
home is not chosen: it is read off Mathlib's own signature, transported from
the subobject to the morphism that presents it.  At abelian-category
generality the universal invariant is the cokernel *object*; every numeric
"index" is a decategorification (Nat.card for groups, length for modules,
covolume ratio for ℤ-lattices in ℝⁿ), which is why Mathlib names only the
concrete shadows.

Convention divergence: value is a `Cardinal` here vs Mathlib's ℕ with the
0-for-infinite collapse (`AddSubgroup.index`).  Deliberate: the cardinal
statement is convention-free and the ℕ shadow is recovered by `index_toNat`
(`rfl`).  Adjudication: keep local; the collapse choice belongs to each
concrete context, and conflating "infinite" with "0" at the concept level
would repeat the unimodular-`Lat(R)` mistake in miniature.
-/
noncomputable def index {R : RingObj} {M N : ModuleObj R} (f : M ⟶ N) :
    Cardinal :=
  Cardinal.mk (N.set ⧸ LinearMap.range (f : M.set →ₗ[R.set] N.set))

/-- The ℕ-valued shadow of `index` is Mathlib's convention (`Nat.card` of
the cokernel, 0 if infinite) — definitionally. -/
theorem index_toNat {R : RingObj} {M N : ModuleObj R} (f : M ⟶ N) :
    (index f).toNat
      = Nat.card (N.set ⧸ LinearMap.range (f : M.set →ₗ[R.set] N.set)) :=
  rfl

/-- Tether witness: the ℕ shadow of `index` is exactly Mathlib's
`AddSubgroup.index` of the image — the wrapping (`toNat`) is the recorded
convention divergence. -/
theorem index_eq_addSubgroupIndex {R : RingObj} {M N : ModuleObj R}
    (f : M ⟶ N) :
    (index f).toNat
      = ((LinearMap.range (f : M.set →ₗ[R.set] N.set)).toAddSubgroup).index :=
  rfl

/-- The identity has index 1: its cokernel is `N ⧸ ⊤`, which is trivial. -/
theorem index_id {R : RingObj} (N : ModuleObj R) :
    index (𝟙 N) = 1 := by
  unfold index
  rw [show LinearMap.range ((𝟙 N : N ⟶ N) : N.set →ₗ[R.set] N.set) = ⊤ from
        LinearMap.range_id]
  exact Cardinal.mk_eq_one _

/--
The zero morphism has index `|N|`: its cokernel is all of `N`.  This is the
exact point where the two operations that collide on the name `index` touch:
the morphism index of `0 : M ⟶ N` equals the cardinality that enumeration
indexes.
-/
theorem index_zero {R : RingObj} (M N : ModuleObj R) :
    index ((0 : M.set →ₗ[R.set] N.set) : M ⟶ N) = Cardinal.mk N.set := by
  unfold index
  rw [LinearMap.range_zero]
  exact Cardinal.mk_congr (Submodule.quotEquivOfEqBot ⊥ rfl).toEquiv

end ModuleHom

end CatDSL.Categories
