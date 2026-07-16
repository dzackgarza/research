import Mathlib

namespace FinitePairNumbering

variable {X Y : Type*} [Fintype X] [Fintype Y]

/-- The row-major number of a pair, with the `Y` coordinate varying fastest. -/
def number (eX : X ≃ Fin (Fintype.card X))
    (eY : Y ≃ Fin (Fintype.card Y)) (p : X × Y) :
    Fin (Fintype.card X * Fintype.card Y) :=
  ⟨(eY p.2).val + Fintype.card Y * (eX p.1).val,
    calc
      (eY p.2).val + Fintype.card Y * (eX p.1).val + 1 =
          (eX p.1).val * Fintype.card Y + (eY p.2).val + 1 := by ac_rfl
      _ ≤ (eX p.1).val * Fintype.card Y + Fintype.card Y :=
        Nat.add_le_add_left (eY p.2).isLt _
      _ = ((eX p.1).val + 1) * Fintype.card Y := Eq.symm (Nat.succ_mul _ _)
      _ ≤ Fintype.card X * Fintype.card Y :=
        Nat.mul_le_mul_right _ (eX p.1).isLt⟩

/-- Explicit decoding by quotient and remainder modulo `card Y`. -/
def unnumber [Nonempty Y]
    (eX : X ≃ Fin (Fintype.card X))
    (eY : Y ≃ Fin (Fintype.card Y))
    (k : Fin (Fintype.card X * Fintype.card Y)) : X × Y :=
  (eX.symm ⟨k.val / Fintype.card Y, by
      have hy : 0 < Fintype.card Y := Fintype.card_pos
      exact (Nat.div_lt_iff_lt_mul hy).2 k.isLt⟩,
   eY.symm ⟨k.val % Fintype.card Y, Nat.mod_lt _ Fintype.card_pos⟩)

/-- Decoding the number of a pair recovers that pair. -/
theorem unnumber_number [Nonempty Y]
    (eX : X ≃ Fin (Fintype.card X))
    (eY : Y ≃ Fin (Fintype.card Y)) (p : X × Y) :
    unnumber eX eY (number eX eY p) = p := by
  refine Prod.ext ?_ ?_ <;> simp [unnumber, number, Nat.mod_eq_of_lt]
  convert eX.symm_apply_apply p.1
  rw [Nat.add_mul_div_left _ _ Fintype.card_pos]
  simp

/-- Numbering a decoded index recovers that index. -/
theorem number_unnumber [Nonempty Y]
    (eX : X ≃ Fin (Fintype.card X))
    (eY : Y ≃ Fin (Fintype.card Y))
    (k : Fin (Fintype.card X * Fintype.card Y)) :
    number eX eY (unnumber eX eY k) = k := by
  unfold number unnumber
  simp [Nat.mod_add_div]

/-- The requested bijection, whose inverse is explicit quotient/remainder decoding. -/
def numberEquiv [Nonempty Y]
    (eX : X ≃ Fin (Fintype.card X))
    (eY : Y ≃ Fin (Fintype.card Y)) :
    X × Y ≃ Fin (Fintype.card X * Fintype.card Y) where
  toFun := number eX eY
  invFun := unnumber eX eY
  left_inv := unnumber_number eX eY
  right_inv := number_unnumber eX eY

@[simp]
theorem numberEquiv_apply [Nonempty Y]
    (eX : X ≃ Fin (Fintype.card X))
    (eY : Y ≃ Fin (Fintype.card Y)) (p : X × Y) :
    numberEquiv eX eY p = number eX eY p := rfl

@[simp]
theorem numberEquiv_symm_apply [Nonempty Y]
    (eX : X ≃ Fin (Fintype.card X))
    (eY : Y ≃ Fin (Fintype.card Y))
    (k : Fin (Fintype.card X * Fintype.card Y)) :
    (numberEquiv eX eY).symm k = unnumber eX eY k := rfl

end FinitePairNumbering
