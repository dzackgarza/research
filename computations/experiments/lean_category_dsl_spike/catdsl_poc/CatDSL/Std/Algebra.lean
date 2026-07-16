import CatDSL.Std.Sets

/-!
# Rings, modules, finite free modules, lattices

Each layer is an object type + a Mathlib `Category` instance, bundled into a
first-class category object with `Cat.of`.

**Functors are declared between the object types** (`RingObj ⥤ SetObj`), not
between the bundled objects (`Rings ⥤ Sets`).  Routing them through the
bundles would resolve `Cat.str Rings` rather than the `Category RingObj`
instance -- a diamond -- and leaves `⇑f` unable to find its coercion.  The
bundles exist for the category graph; the functors are stated where the
elaborator sees through them.  This is also what Mathlib does.
-/

namespace CatDSL.Std

open CategoryTheory CatDSL

/-- A small commutative ring. -/
structure RingObj where
  set : Type
  commRing : CommRing set

attribute [instance] RingObj.commRing

instance : CoeSort RingObj Type where
  coe R := R.set

instance : Category RingObj where
  Hom R S := R.set →+* S.set
  id R := RingHom.id R.set
  comp f g := g.comp f

abbrev Rings : LargeCat := Cat.of RingObj

/-- The `Set`-realization of a ring. -/
def Ring.forget : RingObj ⥤ SetObj where
  obj R := ⟨R.set⟩
  -- The binder's explicit type forces `R ⟶ S =?= R.set →+* S.set` at default
  -- transparency; `⇑f` then has a `RingHom` to coerce.
  map {R S} (f : R.set →+* S.set) := ⇑f

/--
A commutative ring structure on an object already owned by `FiniteSets`.
The finite set is not reconstructed or duplicated by the ring layer.
-/
structure FiniteRingObj where
  finiteSet : FiniteSetObj
  commRing : CommRing finiteSet.set

attribute [instance] FiniteRingObj.commRing

namespace FiniteRingObj

/--
`abbrev`, not `def`: instance search only unfolds reducible definitions, so
`CommRing R.set` would not be found from the `CommRing R.finiteSet.set`
instance despite the two being definitionally equal.
-/
abbrev set (R : FiniteRingObj) : Type :=
  R.finiteSet.set

instance : CoeSort FiniteRingObj Type where
  coe R := R.set

abbrev size (R : FiniteRingObj) : Nat :=
  R.finiteSet.size

abbrev enumerate (R : FiniteRingObj) :
    R.set ≃ Fin R.size :=
  R.finiteSet.enumerate

abbrev toRing (R : FiniteRingObj) : RingObj where
  set := R.set
  commRing := R.commRing

abbrev toFiniteSet (R : FiniteRingObj) : FiniteSetObj :=
  R.finiteSet

def prod (R S : FiniteRingObj) : FiniteRingObj where
  finiteSet := FiniteSetObj.prod R.finiteSet S.finiteSet
  commRing := by
    -- `FiniteSetObj.prod` is a `def`, so the goal's `.set` will not reduce
    -- for instance search; `show` reduces it at default transparency.
    show CommRing (R.set × S.set)
    infer_instance

end FiniteRingObj

instance : Category FiniteRingObj where
  Hom R S := R.set →+* S.set
  id R := RingHom.id R.set
  comp f g := g.comp f

abbrev FiniteRings : LargeCat := Cat.of FiniteRingObj

def FiniteRing.toRing : FiniteRingObj ⥤ RingObj where
  obj := FiniteRingObj.toRing
  map f := f

/-- The `FiniteSet`-realization of a finite ring. -/
def FiniteRing.toFiniteSet : FiniteRingObj ⥤ FiniteSetObj where
  obj := FiniteRingObj.toFiniteSet
  map {R S} (f : R.set →+* S.set) := ⇑f

/-- The concrete two-element set `{0,1}`, owned by `FiniteSets`. -/
abbrev two : FiniteSetObj where
  set := ZMod 2
  size := 2
  enumerate := Equiv.refl (Fin 2)

/--
Paper-like notation for `two`.

`𝟚` is U+1D7DA, a mathematical double-struck *digit*.  Lean's identifier
lexer accepts double-struck *letters* (`𝔽` is fine) but rejects digits, so
`def 𝟚` cannot be written.  Notation may use any token, so the surface
spelling lives here over a declaration whose name Lean can lex.
-/
notation "𝟚" => two

/-- The field `𝔽₂`: the commutative-ring structure on `𝟚`. -/
def 𝔽₂ : FiniteRingObj where
  finiteSet := 𝟚
  commRing := inferInstance

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

/--
A **unimodular** `R`-lattice: a finite free `R`-module with a *perfect*
symmetric bilinear form.

`form` is `b̃ : M → M^∨`, `x ↦ b(x,-)`.  Note what requiring it to be a
`LinearEquiv` actually says:

  * `b̃` injective            = `b` is **nondegenerate**
  * `b̃` an isomorphism       = `b` is **perfect**, i.e. `M` is **unimodular**

These coincide for finite-dimensional `M` over a field -- which is why the
`𝔽₂` example is unaffected -- but not over a general commutative ring.  The
cokernel of `b̃ : L ↪ L^∨` is precisely the *discriminant group* `L^∨/L`,
which is trivial exactly when `L` is unimodular.

So this structure is NOT "lattices"; it is the unimodular ones, and it
defines the discriminant form out of existence.  A general lattice layer
would weaken `form` to a `LinearMap` with a separate nondegeneracy field and
recover the unimodular case as the specialisation where `b̃` is an iso.  That
is deliberately not done here: the PoC only needs `𝔽₂`, where the notions
agree, and doing it properly is a real design task, not a rename.

-/
structure LatticeObj (R : FiniteRingObj) where
  module : FreeFinModuleObj R
  form :
    module.module.set ≃ₗ[R.set] Module.Dual R.set module.module.set
  symmetric : ∀ x y, form x y = form y x

instance (R : FiniteRingObj) : CoeSort (LatticeObj R) Type where
  coe L := L.module.module.set

/-- Morphisms of lattices are isometries: they preserve the form. -/
structure LatticeHom {R : FiniteRingObj} (L M : LatticeObj R) where
  hom :
    L.module.module.set →ₗ[R.set] M.module.module.set
  isometry :
    ∀ x y, M.form (hom x) (hom y) = L.form x y

namespace LatticeHom

@[ext]
theorem ext {R : FiniteRingObj} {L M : LatticeObj R}
    {f g : LatticeHom L M}
    (h : f.hom = g.hom) :
    f = g := by
  cases f
  cases g
  cases h
  rfl

end LatticeHom

instance (R : FiniteRingObj) : Category (LatticeObj R) where
  Hom L M := LatticeHom L M
  id L := { hom := LinearMap.id, isometry := by intro x y; rfl }
  comp {L M N} f g :=
    { hom := g.hom.comp f.hom
      isometry := by
        intro x y
        simp only [LinearMap.comp_apply]
        rw [g.isometry, f.isometry] }
  id_comp _ := by apply LatticeHom.ext; rfl
  comp_id _ := by apply LatticeHom.ext; rfl
  assoc _ _ _ := by apply LatticeHom.ext; rfl

abbrev Lattices (R : FiniteRingObj) : LargeCat := Cat.of (LatticeObj R)

namespace LatticeObj

/--
The form induced by a basis is symmetric.

Expanding `y` in the basis gives `b.toDual x y = Σⱼ (repr y j) * (repr x j)`,
which is symmetric in `x` and `y` by `mul_comm`.  In the basis, this is the
form with identity Gram matrix.
-/
theorem toDual_comm {ι K N : Type*} [CommRing K] [AddCommGroup N] [Module K N]
    [DecidableEq ι] [Fintype ι] (b : Module.Basis ι K N) (x y : N) :
    b.toDual x y = b.toDual y x := by
  conv_lhs => rw [← b.sum_repr y]
  conv_rhs => rw [← b.sum_repr x]
  simp only [map_sum, map_smul, Module.Basis.toDual_apply_left, smul_eq_mul]
  exact Finset.sum_congr rfl fun i _ => mul_comm _ _

/--
The standard lattice on `R²`: the form with identity Gram matrix.

This is what `(R², id)` denotes in DSL source -- `id` is the *form*, not an
automorphism.  For the standard basis, `toDualEquiv` is precisely the
identity-Gram form `b(x,y) = Σᵢ xᵢ yᵢ`.

`noncomputable` because `toDualEquiv` is built with `LinearEquiv.ofBijective`
and so rests on `Classical.choice`.  That costs nothing here, and is quietly
a demonstration of the architecture's own point: `π_R` forgets the form, so
`|L|` reduces through `L.module` and never touches `form` at all.
-/
noncomputable def standard (R : FiniteRingObj) : LatticeObj R where
  module := FreeFinModuleObj.rankTwo R
  form := (Pi.basisFun R.set (Fin 2)).toDualEquiv
  symmetric := fun x y => toDual_comm _ x y

end LatticeObj

/-- The `FreeFinMod(R)`-realization of a lattice: `(L,b) ↦ L`. -/
def Lattice.toFreeFinModule (R : FiniteRingObj) :
    LatticeObj R ⥤ FreeFinModuleObj R where
  obj L := L.module
  map f := f.hom

end CatDSL.Std
