## Shortcut: Orbits of isotropic vectors/planes for Λ = Π_{1,9} ≃ U ⊕ E₈

**Source:** Alexeev-Liu-Schütt 2025 (arXiv:2510.17678), Lemma 5.4 and proof.

**Key result:** ∂F^BB_Λ ≅ P¹_j — one 0-cusp and one 1-cusp.

**Proof technique (shortcut for orbit computation):**

- **0-cusps ↔ O(Λ^⊥)-orbits of primitive isotropic vectors.**
  Any primitive isotropic e ∈ Λ^⊥ lies in a copy of U, which splits off: Λ^⊥ = U ⊕ U^⊥.
  U^⊥ is even unimodular of signature (1,9) → unique such lattice → U^⊥ ≅ U ⊕ E₈.
  Any two such decompositions differ by an isometry of U^⊥; any two isotropic vectors in U differ by an isometry of U.
  **Conclusion: unique O(Λ^⊥)-orbit of primitive isotropic vectors → one 0-cusp.**

- **1-cusps ↔ O(Λ^⊥)-orbits of primitive isotropic planes.**
  Same argument: J ⊂ U², Λ^⊥ = U² ⊕ (U²)^⊥, and (U²)^⊥ is even unimodular of signature (0,8) → unique such lattice E₈.
  **Conclusion: unique O(Λ^⊥)-orbit of primitive isotropic planes → one 1-cusp ≅ A¹_j.**

**The shortcut:** Uniqueness of even unimodular lattices of given signature collapses the orbit count immediately — no explicit coset enumeration needed. The isometry type of v^⊥/v (or J^⊥/J) is forced by the classification of unimodular lattices.

**Combinatorial/divisor model note:** The 1-cusp is the j-line A¹_j, parametrized by the j-invariant of the elliptic curve E in a Type II Kulikov degeneration; the 0-cusp is j = ∞ (Type III, rational nodal). Understanding the boundary combinatorially means understanding these Kulikov fiber types and their dual graphs — this is the bridge to divisor models.

**To investigate:** Can this unimodularity argument be systematized for other lattices Λ where Λ^⊥ is not unimodular? (cf. Dawes 2021/2016 for the non-unimodular case requiring explicit orbit algorithms.)
