import CatDSL.Categories.Rings

/-!
# Modules and the finitely generated free subcategory

The category of `R`-modules IS Mathlib's `ModuleCat R`; nothing local is
declared for it.  Finitely generated free modules are the full
subcategory on the property `Module.Free ∧ Module.Finite` — chosen bases
and enumerations are evaluation-seam witnesses, never object structure.
-/

namespace CatDSL.Categories

open CategoryTheory CatDSL

/-- The category of finitely generated free `R`-modules: the full
subcategory of `ModuleCat R` on `Module.Free ∧ Module.Finite`. -/
abbrev FGFree (R : Type) [CommRing R] :=
  ObjectProperty.FullSubcategory
    (fun M : ModuleCat R => Module.Free R M ∧ Module.Finite R M)

/-- The inclusion into modules. -/
def FGFree.ι (R : Type) [CommRing R] : FGFree R ⥤ ModuleCat R :=
  ObjectProperty.ι _

/-- A finitely generated module over a finite ring has a finite carrier:
a surjection from `Fin n → R`. -/
theorem Module.Finite.finite_carrier (R : Type) [CommRing R] [Finite R]
    (M : Type) [AddCommGroup M] [Module R M] [Module.Finite R M] :
    Finite M := by
  obtain ⟨n, f, hf⟩ := Module.Finite.exists_fin' R M
  exact Finite.of_surjective f hf

/--
The restriction of the forgetful functor to the finite fragment over a
finite base ring: finitely generated over finite scalars means finite
carrier, so `forget` lifts through the `Finite` property.
-/
def FGFree.toFinSet (R : Type) [CommRing R] [Finite R] :
    FGFree R ⥤ FinSet :=
  ObjectProperty.lift _
    (ObjectProperty.ι _ ⋙ CategoryTheory.forget (ModuleCat R))
    fun M =>
      haveI : Module.Finite R M.obj := M.property.2
      Module.Finite.finite_carrier R M.obj

/-!
## Morphism-sited operations

Operations whose input is a morphism are typed on the morphism.
-/

namespace ModuleHom

/--
The **index** `[N : f(M)]` of a module morphism: the cardinality of its
cokernel.  Home: morphisms of `ModuleCat R` (abelian, so every morphism has
a cokernel — the same definition cannot be written on `Grp`, where images
need not be normal).  Mathlib owns the concept as `AddSubgroup.index`
(`Nat.card` of the quotient, 0-for-infinite); this is that invariant on
`range f`, stated convention-free in cardinals, with the ℕ shadow equal to
Mathlib's by `rfl` (`index_eq_addSubgroupIndex`).
-/
noncomputable def index {R : Type} [CommRing R] {M N : ModuleCat R}
    (f : M ⟶ N) : Cardinal :=
  Cardinal.mk (N ⧸ LinearMap.range f.hom)

/-- The ℕ shadow of `index` is Mathlib's `AddSubgroup.index` of the image,
definitionally. -/
theorem index_eq_addSubgroupIndex {R : Type} [CommRing R] {M N : ModuleCat R}
    (f : M ⟶ N) :
    (index f).toNat = ((LinearMap.range f.hom).toAddSubgroup).index :=
  rfl

/-- The identity has index 1: its cokernel is trivial. -/
theorem index_id {R : Type} [CommRing R] (N : ModuleCat R) :
    index (𝟙 N) = 1 := by
  unfold index
  rw [show LinearMap.range (𝟙 N : N ⟶ N).hom = ⊤ from LinearMap.range_id]
  exact Cardinal.mk_eq_one _

end ModuleHom

end CatDSL.Categories
