import CatDSL.Std.Algebra

/-!
# The 𝔽₂ vertical slice, in ordinary Lean

This is the semantic core of `Example/F2Lattice.lean` with no DSL syntax:
the same objects, the same preferred path, the same claims — written as
plain Lean so that a failure here is a failure of the *mathematics or the
architecture*, not of an elaborator.

The point being tested is the architecture's central claim:

    Lat(𝔽₂) → FreeFinMod(𝔽₂) → FiniteSet → CountableSet

carries `L` to a countable set **with no lattice-specific code** — the
enumeration and the cardinality are inherited from the finite-set product.

Everything below is `rfl` or `decide`. Nothing is assumed.
-/

namespace CatDSL.Example

open CatDSL CatDSL.Std

/-- `L := (𝔽₂², id) ∈ Lat(𝔽₂)` — the rank-two standard lattice over `𝔽₂`. -/
noncomputable def L : LatticeObj 𝔽₂ := LatticeObj.standard 𝔽₂

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
theorem card_L_eq_sq : cardinality Lfin = 𝔽₂.size ^ 2 := by rfl

/-!
## Numbering

The mixed-radix numbering is inherited from `FiniteSetObj.prod`; no lattice,
module, or ring code computes it.  `number (a,b) = 2a + b`.
-/

/-- Acceptance criterion 11: the generated numbering is `2a + b`. -/
theorem number_table :
    Lcount.number (0, 0) = 0 ∧
    Lcount.number (0, 1) = 1 ∧
    Lcount.number (1, 0) = 2 ∧
    Lcount.number (1, 1) = 3 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> decide

/-- `nth` inverts `number`, and is undefined past the end. -/
theorem nth_table :
    Lcount.nth 0 = some (0, 0) ∧
    Lcount.nth 1 = some (0, 1) ∧
    Lcount.nth 2 = some (1, 0) ∧
    Lcount.nth 3 = some (1, 1) ∧
    Lcount.nth 4 = none := by
  -- `decide` would need `DecidableEq Lcount.set`, which does not resolve:
  -- the type only reduces to `ZMod 2 × ZMod 2` at default transparency.
  refine ⟨?_, ?_, ?_, ?_, ?_⟩ <;> rfl

/-- Criterion 7: the countability implementation is real, not a proposition. -/
theorem nth_number_L (x : Lcount.set) : Lcount.nth (Lcount.number x) = some x :=
  Lcount.nth_number x

end CatDSL.Example
