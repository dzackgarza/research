import Mathlib

/-!
# ForMathlib: dual-basis lemmas

**Layer contract.**  Everything under `CatDSL/ForMathlib/` is upstream-destined
general theory: statements Mathlib should own but does not yet.  Files here

  * import **Mathlib only** — never any other `CatDSL` module (mechanically
    enforced by `just layering-check`);
  * mirror Mathlib's directory layout and live in Mathlib-natural namespaces;
  * name their upstream target in the declaration docstring.

Graduation: contribute the declaration upstream, delete it here, and re-alias
the one manifest row that referenced it.
-/

namespace Module.Basis

/--
The form induced by a basis is symmetric.

Expanding `y` in the basis gives `b.toDual x y = Σⱼ (repr y j) * (repr x j)`,
which is symmetric in `x` and `y` by `mul_comm`.  In the basis, this is the
form with identity Gram matrix.

Upstream target: `Mathlib.LinearAlgebra.Dual` (beside `Module.Basis.toDual`).
-/
theorem toDual_comm {ι K N : Type*} [CommRing K] [AddCommGroup N] [Module K N]
    [DecidableEq ι] [Fintype ι] (b : Module.Basis ι K N) (x y : N) :
    b.toDual x y = b.toDual y x := by
  conv_lhs => rw [← b.sum_repr y]
  conv_rhs => rw [← b.sum_repr x]
  simp only [map_sum, map_smul, Module.Basis.toDual_apply_left, smul_eq_mul]
  exact Finset.sum_congr rfl fun i _ => mul_comm _ _

end Module.Basis
