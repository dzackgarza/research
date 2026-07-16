import CatDSL.Categories.Lattices

/-!
# The 𝔽₂ vertical slice, in ordinary Lean

This is the semantic core of `Example/F2Lattice.lean` with no DSL syntax:
the same objects, the same preferred path, the same claims — written as
plain Lean so that a failure here is a failure of the *mathematics or the
architecture*, not of an elaborator.

The point being tested is the architecture's central claim:

    UnimodularLat(𝔽₂) → Lat(𝔽₂) → FreeFinMod(𝔽₂) → FiniteSet → CountableSet

carries `L` to a countable set **with no lattice-specific code** — the
enumeration and the cardinality are inherited from the general standard
free-module presentation (`finFunctionFinEquiv`, little-endian).
The example enters at the unimodular full subcategory: its membership is a
proved fact (`standard_isUnimodular`), and the first step of the path is
the inclusion functor forgetting that witness.

Everything below is `rfl` or `decide`. Nothing is assumed.
-/

namespace CatDSL.Example

open CatDSL CatDSL.Categories

/-- `Lu ∈ UnimodularLat(𝔽₂)` — the standard lattice with its proved
unimodularity witness. -/
noncomputable def Lu : UnimodularLatticeObj 𝔽₂ :=
  LatticeObj.standardUnimodular 𝔽₂

/-- Step 0 of the preferred path: the inclusion of the unimodular full
subcategory forgets the witness.  `L := (𝔽₂², id) ∈ Lat(𝔽₂)`. -/
noncomputable def L : LatticeObj 𝔽₂ := (Unimodular.toLattice 𝔽₂).obj Lu

/-- Step 1 of the preferred path: `π_R` forgets the form. -/
noncomputable def Lmod : FreeFinModuleObj 𝔽₂ :=
  (Lattice.toFreeFinModule 𝔽₂).obj L

/-- Step 2: the `FiniteSet`-realization of the free module. -/
noncomputable def Lfin : FiniteSetObj :=
  (FreeFinModule.toFiniteSet 𝔽₂).obj Lmod

/-- Step 3: every finite set is countable, via its chosen enumeration. -/
noncomputable def Lcount : CountableSetObj :=
  (FiniteSet.toCountable).obj Lfin

/-!
## Cardinality

`|L| = |𝔽₂²| = |𝔽₂|² = 2² = 4`, computed through the path, not asserted.
-/

/-- Acceptance criterion 12: the generated cardinality is 4. -/
theorem card_L : cardinality Lfin = 4 := by rfl

/-- `|L| = |𝔽₂|²`: the cardinality factors through the product, as claimed. -/
theorem card_L_eq_sq : cardinality Lfin = 𝔽₂.finiteSet.card ^ 2 := by rfl

/-!
## Numbering

The mixed-radix numbering is inherited from the general standard
presentation (`finFunctionFinEquiv`); no lattice, module, or ring code
computes it.  Little-endian: `number ![a, b] = a + 2b`.
-/

/-- Acceptance criterion 11: the generated numbering is `a + 2b`. -/
theorem number_table :
    Lcount.number ![0, 0] = 0 ∧
    Lcount.number ![1, 0] = 1 ∧
    Lcount.number ![0, 1] = 2 ∧
    Lcount.number ![1, 1] = 3 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> decide

/-- `nth` inverts `number`, and is undefined past the end. -/
theorem nth_table :
    Lcount.nth 0 = some ![0, 0] ∧
    Lcount.nth 1 = some ![1, 0] ∧
    Lcount.nth 2 = some ![0, 1] ∧
    Lcount.nth 3 = some ![1, 1] ∧
    Lcount.nth 4 = none := by
  -- The inverse of the general enumeration is not `rfl`-transparent
  -- (`Equiv.ofRightInverseOfCardLE`), so each entry is obtained from the
  -- generic inverse law at the decidably-computed forward value.
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · have h := Lcount.nth_number ![0, 0]
    rwa [show Lcount.number ![0, 0] = 0 from by decide] at h
  · have h := Lcount.nth_number ![1, 0]
    rwa [show Lcount.number ![1, 0] = 1 from by decide] at h
  · have h := Lcount.nth_number ![0, 1]
    rwa [show Lcount.number ![0, 1] = 2 from by decide] at h
  · have h := Lcount.nth_number ![1, 1]
    rwa [show Lcount.number ![1, 1] = 3 from by decide] at h
  · rfl

/-- Criterion 7: the countability implementation is real, not a proposition. -/
theorem nth_number_L (x : Lcount.set) : Lcount.nth (Lcount.number x) = some x :=
  Lcount.nth_number x

/-- `R.cardinality := F(R).cardinality` — a ring's cardinality is obtained
ONLY through the forgetful functor; no ring-level spelling exists.  This is
the architecture's central equation, kernel-checked. -/
example : cardinality (FiniteRing.toFiniteSet.obj 𝔽₂) = 2 := rfl

end CatDSL.Example
