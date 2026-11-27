GOAL: record the algebra-specific method surface as ABC specs on subcategories
of `Algebras(R)`.

This subtree exists so that algebra-specific structure is defined here instead
of being redeclared inside ring-specific categories like matrix algebras.

Tasks:
    - Define `Algebras(R)` as the category of `R`-algebras in the local spec.
    - Keep algebra-specific parent methods here: `subalgebra`, `center`,
      `radical`, `derivations_basis`, `hochschild_complex`, and related
      structure maps.
    - Ensure ring constructions that are naturally `R`-algebras refine into
      this subtree rather than defining their algebra surface ad hoc.
    - Let specialized ring/algebra categories inherit from this subtree plus
      their ring/module surfaces instead of redeclaring inherited methods.
