import Mathlib

/-!
# The rim of Alexeev--Engel--Thompson's Coxeter diagram is an affine `A₁₇`, and it is null

Source: V. Alexeev, P. Engel, A. Thompson, *Stable pair compactification of moduli of K3
surfaces of degree 2*, arXiv:1903.09742v3 (= bibliography key `AET23`), Figure 1 on p. 22
and Lemma 4.5: mod `S₃` there are four maximal parabolic subdiagrams of the Coxeter diagram
`G_cox` of `N = H ⊕ E₈² ⊕ A₁`, the first of them `Ã₁₇`.

The nodes of `G_cox` are the 24 roots `r_i`, `i = 0, …, 23`, and the figure prints them in
the triangular lattice

    12
    13  11
    14  20  10
    15  22  21   9
    16            8
    17  18  23  19   7
     0   1   2   3   4   5   6

with inner products `(r_i, r_j) ∈ {0, 1, 2, 6}` according to whether the edge is absent,
single, double or dashed.  Reading the first of the four small figures next to it: the black
nodes are exactly the eighteen on the rim of the triangle, in the cyclic order

    12, 13, 14, 15, 16, 17, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,

and the six interior nodes `20, 22, 21, 23, 19, 18` are white.  All eighteen rim edges are
single edges, so the restriction of the form to the rim is the affine Cartan matrix
`Ã₁₇`: `-2` on the diagonal and `1` between cyclically adjacent nodes.

What is proved here is the arithmetic of that reading: the marks of `Ã₁₇` are all `1`, the
mark vector lies in the kernel of the rim Gram matrix, and its square is zero.  So a null ray
of `N` is spanned by the sum of the eighteen rim roots, which is what the `Ã₁₇` cusp's plane
is a cone over.  Primitivity of that sum in `N`, and the identification of its isotropic
reduction with the label `A₁₇`, are *not* proved here; they are the library computation that
remains pending.
-/

namespace Coble

/-- The Gram matrix of the rim of `G_cox`: the affine `A₁₇` Cartan matrix, in the cyclic
order `12, 13, 14, 15, 16, 17, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11` of the rim. -/
def rimGRAM : Matrix (Fin 18) (Fin 18) ℤ :=
  Matrix.of fun i j =>
    if i = j then -2
    else if (i.val + 1) % 18 = j.val ∨ (j.val + 1) % 18 = i.val then 1
    else 0

/-- The affine marks of `Ã₁₇`: all of them are `1`. -/
def rimMarks : Fin 18 → ℤ := fun _ => 1

/-- The mark vector is in the kernel of the rim Gram matrix: the null root. -/
theorem rim_mulVec_marks : rimGRAM.mulVec rimMarks = 0 := by
  decide

/-- The null root is isotropic. -/
theorem rim_marks_isotropic : rimMarks ⬝ᵥ rimGRAM.mulVec rimMarks = 0 := by
  rw [rim_mulVec_marks]
  simp

/-- The null root is not zero, and its coefficients are the marks. -/
theorem rim_marks_ne_zero : rimMarks ≠ 0 := by
  intro h
  have := congrFun h 0
  simp [rimMarks] at this

#print axioms Coble.rim_mulVec_marks
#print axioms Coble.rim_marks_isotropic

end Coble
