/-
Copyright (c) 2026 Dzack Garza. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
module

public import LeanCategories.LatticeResearch.Divisibility

/-!
# The lattice-research subtree

Statements from the Coble--Enriques lattice work whose form is arithmetic enough to
check: divisibility of a vector, its behaviour under twisting the form, and the
counterexamples that decide which hypotheses the statements of the prose actually
need.

This subtree is separate from `LeanCategories.Lattices`, which follows Mathlib's
lattice categories, because the objects here are integral lattices over `ℤ` in the
sense of the book, not order-theoretic lattices.
-/

@[expose] public section
