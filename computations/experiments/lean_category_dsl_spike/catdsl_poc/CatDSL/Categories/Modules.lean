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

/-- Surface category family `Mod(R)`. -/
abbrev Mod (R : FiniteRingObj) : LargeCat :=
  Modules R.toRing

/-- The `Set`-realization of a module. -/
def Module.forget (R : FiniteRingObj) : ModuleObj R.toRing ⥤ SetObj where
  obj M := ⟨M.set⟩
  map {M N} (f : M.set →ₗ[R.set] N.set) := ⇑f

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
  cardinality_eq : finiteSet.size = R.size ^ rank

instance (R : FiniteRingObj) : CoeSort (FreeFinModuleObj R) Type where
  coe M := M.module.set

namespace FreeFinModuleObj

/-- The explicit equivalence `(Fin 2 → α) ≃ α × α`. -/
def finTwoFunctionEquiv (α : Type) : (Fin 2 → α) ≃ α × α where
  toFun := fun f => (f 0, f 1)
  invFun := fun p i => Fin.cases p.1 (fun _ => p.2) i
  left_inv := by
    intro f
    funext i
    fin_cases i <;> rfl
  right_inv := by
    intro p
    cases p
    rfl

/--
The standard rank-two free module.  Its finite set is the product of two
copies of the finite set of `R`, so all enumeration and cardinality code is
inherited from finite-set products.
-/
def rankTwo (R : FiniteRingObj) : FreeFinModuleObj R where
  module := ModuleObj.of R.toRing (Fin 2 → R.set)
  rank := 2
  coordinates := LinearEquiv.refl R.set (Fin 2 → R.set)
  finiteSet := FiniteSetObj.prod R.toFiniteSet R.toFiniteSet
  finiteSetEquiv := finTwoFunctionEquiv R.set
  cardinality_eq := by
    show R.size * R.size = R.size ^ 2
    ring

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

end CatDSL.Categories
