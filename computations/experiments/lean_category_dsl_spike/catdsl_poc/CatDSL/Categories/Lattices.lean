import CatDSL.Categories.Modules
import CatDSL.ForMathlib.LinearAlgebra.Dual

/-!
# Lattices: the category of elements of the forms presheaf

`Lat(R)` is built compositionally from standard machinery — no bespoke
category and no upstream gap:

* symmetric bilinear forms are a presheaf on `ModuleCat R` (pullback);
* pairs `(M, b)` with form-preserving maps are (the opposite of) Mathlib's
  **category of elements** of that presheaf;
* nondegeneracy and finite-generated-freeness are an `ObjectProperty` cut;
* unimodularity is a further property cut, with `ObjectProperty.ι` as the
  inclusion;
* the forget-the-form functor is the elements projection `π`, whose
  conservativity Mathlib already proves (`(π F).ReflectsIsomorphisms`).
-/

namespace CatDSL.Categories

open CategoryTheory CatDSL

/-- The symmetric-bilinear-forms presheaf: contravariant on modules via
pullback `b ↦ b(f·, f·)`. -/
def SymForms (R : Type) [CommRing R] : (ModuleCat R)ᵒᵖ ⥤ Type where
  obj M := { b : LinearMap.BilinForm R M.unop // ∀ x y, b x y = b y x }
  map {M N} f b :=
    ⟨LinearMap.compl₁₂ b.1 f.unop.hom f.unop.hom,
     fun x y => b.2 (f.unop.hom x) (f.unop.hom y)⟩
  map_id M := by
    funext b
    exact Subtype.ext (LinearMap.ext fun x => LinearMap.ext fun y => rfl)
  map_comp f g := by
    funext b
    exact Subtype.ext (LinearMap.ext fun x => LinearMap.ext fun y => rfl)

/--
`Lat(R)`: nondegenerate symmetric bilinear forms on finitely generated free
modules, with isometries.  Objects of the elements category of `SymForms`
are pairs `(M, b)`; a morphism `(op M, b) ⟶ (op N, c)` there is a linear
map `g : N → M` with `b(g·, g·) = c`, i.e. an isometry `(N, c) → (M, b)` —
so `Lat` is the opposite, cut to the nondegenerate f.g. free objects.
`b : M →ₗ M^∨` in curried form IS the bilinear form, so nondegeneracy is
injectivity of the form itself.
-/
abbrev Lat (R : Type) [CommRing R] :=
  ObjectProperty.FullSubcategory
    (fun X : ((SymForms R).Elements)ᵒᵖ =>
      Function.Injective X.unop.2.1 ∧
      Module.Free R X.unop.1.unop ∧ Module.Finite R X.unop.1.unop)

/-- Forget the form: the elements projection, transported to `Lat`.
Conservativity is Mathlib's `(π F).ReflectsIsomorphisms` — an invertible
isometry's inverse is an isometry, already proved upstream. -/
def Lat.toModule (R : Type) [CommRing R] : Lat R ⥤ ModuleCat R :=
  ObjectProperty.ι _ ⋙ (CategoryOfElements.π (SymForms R)).op ⋙
    (opOpEquivalence (ModuleCat R)).functor

/-- The underlying module is f.g. free by the property cut: `toModule`
lifts through `FGFree`. -/
def Lat.toFGFree (R : Type) [CommRing R] : Lat R ⥤ FGFree R :=
  ObjectProperty.lift _ (Lat.toModule R) fun X => ⟨X.property.2.1, X.property.2.2⟩

/-- Unimodular lattices: the further property cut where the form is
perfect (bijective), i.e. the discriminant group is trivial. -/
abbrev Unimod (R : Type) [CommRing R] :=
  ObjectProperty.FullSubcategory
    (fun L : Lat R => Function.Bijective L.obj.unop.2.1)

/-- The inclusion of unimodular lattices: Mathlib's `ObjectProperty.ι`. -/
def Unimod.ι (R : Type) [CommRing R] : Unimod R ⥤ Lat R :=
  ObjectProperty.ι _

/-!
## The standard lattice (worked example, general rank)

`(Rⁿ, identity Gram)`: the form is `Basis.toDual` of the standard basis —
built entirely from identified pieces; example-local, not vocabulary.
-/

/-- The identity-Gram symmetric form on `Fin n → R`. -/
noncomputable def standardForm (R : Type) [CommRing R] (n : ℕ) :
    (SymForms R).obj (Opposite.op (ModuleCat.of R (Fin n → R))) :=
  ⟨(Pi.basisFun R (Fin n)).toDual,
   fun x y => Module.Basis.toDual_comm _ x y⟩

/-- The standard lattice `(Rⁿ, id)` as an object of `Lat R`. -/
noncomputable def standardLat (R : Type) [CommRing R] (n : ℕ) : Lat R :=
  ⟨Opposite.op ⟨Opposite.op (ModuleCat.of R (Fin n → R)), standardForm R n⟩,
   (Pi.basisFun R (Fin n)).toDual_injective,
   inferInstance, inferInstance⟩

/-- The standard lattice is unimodular: for a basis, `toDual` is bijective
(injective with full range) — a real membership proof. -/
noncomputable def standardUnimod (R : Type) [CommRing R] (n : ℕ) : Unimod R :=
  ⟨standardLat R n,
   ⟨(Pi.basisFun R (Fin n)).toDual_injective,
    LinearMap.range_eq_top.mp (Pi.basisFun R (Fin n)).toDual_range⟩⟩

end CatDSL.Categories
