/-
A21 arithmetic core: machine-checked integer content of Theorems 3 and 4 of
`.ultramath/smw0b9kmo/m1/proof.md`.

Setting: S_Co = U(2) ⟂ E8(-2) ⟂ <-2>, with U(2) basis h1,h2 (h_i^2 = 0, h1·h2 = 2),
d a generator of <-2> (d^2 = -2), H = h1 + h2, and e in E8(-2) with e^2 = -4k, k >= 0
(E8(-2) is negative definite and even, so every square is a nonpositive multiple of 4).

Theorem 3 (root pinning):  beta = a h1 + b h2 + e + c d with beta^2 = -2 and beta·H = 0
forces beta = ± d, i.e. a = 0, k = 0, c = ± 1.
Theorem 4: no pair in U(2) has the Gram data of (H, alpha).
-/
import Mathlib

namespace A21Core

/-- Integer core of Theorem 3 (root pinning).
`beta·H = 0` has already been used to eliminate `b` (`b = -a`), and `beta^2 = -2` has been
put in the form `2a^2 + 2k + c^2 = 1` with `k = -e^2/4 >= 0`; the conclusion is `beta = ± d`. -/
theorem pinned_root (a c k : ℤ) (hk : 0 ≤ k) (h : 2 * a ^ 2 + 2 * k + c ^ 2 = 1) :
    a = 0 ∧ k = 0 ∧ (c = 1 ∨ c = -1) := by
  have ha2 : a ^ 2 = 0 := by nlinarith [sq_nonneg a, sq_nonneg c]
  have ha : a = 0 := by
    have := pow_eq_zero_iff (n := 2) (by norm_num : (2 : ℕ) ≠ 0) |>.mp ha2
    exact this
  subst ha
  have hk0 : k = 0 := by nlinarith [sq_nonneg c]
  subst hk0
  have hc : c ^ 2 = 1 := by nlinarith
  have hfac : (c - 1) * (c + 1) = 0 := by nlinarith
  rcases mul_eq_zero.mp hfac with h1 | h1
  · exact ⟨rfl, rfl, Or.inl (by omega)⟩
  · exact ⟨rfl, rfl, Or.inr (by omega)⟩

/-- Theorem 2 (degree-4 pinning): with `x = a h1 + b h2 + c d`, `x·d = -2c = 0` and
`x^2 = 4ab - 2c^2 = 4` force `c = 0` and `a b = 1`. -/
theorem deg4_pinned (a b c : ℤ) (hd : -2 * c = 0) (hx : 4 * a * b - 2 * c ^ 2 = 4) :
    c = 0 ∧ a * b = 1 := by
  have hc : c = 0 := by omega
  subst hc
  exact ⟨rfl, by linarith⟩

/-- Theorem 4: `U(2)` contains no pair `x, y` with `x^2 = 4`, `y^2 = -2`, `x·y = 0`
(writing `x = a h1 + b h2`, `y = c h1 + d h2`, so that `x^2 = 4ab`, `y^2 = 4cd`). -/
theorem no_deg4_root_in_U2 (a b c d : ℤ) (_hx : 4 * a * b = 4) (hy : 4 * c * d = -2) :
    False := by
  have h : (4 : ℤ) ∣ -2 := ⟨c * d, by linarith⟩
  obtain ⟨k, hk⟩ := h
  omega

/-- The same, in the form used in the text: an index-`m` sublattice of `U(2)` has determinant
`-4 m^2`, and `-8` is not of that form. -/
theorem det_index_sq (m : ℤ) : -8 ≠ -4 * m ^ 2 := by
  intro h
  have hm2 : m ^ 2 = 2 := by linarith
  have hle : m ≤ 1 := by nlinarith [sq_nonneg (m - 2)]
  have hge : -1 ≤ m := by nlinarith [sq_nonneg (m + 2)]
  interval_cases m <;> norm_num at hm2

end A21Core
