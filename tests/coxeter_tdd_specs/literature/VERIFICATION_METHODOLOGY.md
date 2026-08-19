<!--
Origin: gitclones/Coxeter-v2/docs/authority/COMPUTATIONAL_RIGOR.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

The verification methodology of the Coxeter-v2 tree, landed beside
PROJECT_CONVENTIONS.md because it states the standards this test corpus is
written to: form linearity, the Cartan relation, reflection preservation,
exact arithmetic over AA, and the determinant fallacy.

Two qualifications on the content below, neither of which it states:

1. Section 1's Cartan relation A = -G holds for the SIMPLY-LACED types only.
   For B, C, F and G the Cartan matrix is not symmetric, so it is not the
   Gram matrix of the simple roots; the Gram matrix is the symmetrization
   d_i * a_ij. Both test cases it names (A2, E8) are simply-laced, so both
   are correct as written.
2. Section 2's Lanner golden reference — maximal parabolic counts against
   Lanner's list for n <= 10 — is not in this corpus. It is a named gap, not
   an available fixture.
-->

# Computational Rigor Authority Document

This document defines the standards for mathematical correctness and verification in the Coxeter project. It codifies the invariants and testing strategies required to ensure 1:1 parity with the legacy implementation and theoretical foundations.

## 1. Testing Invariants

### Bilinear Form Linearity
Every BILINEAR form must satisfy the linearity condition:
- **Identity**: $B(v+w, u) = B(v, u) + B(w, u)$
- **Mandatory Test**: A automated linearity check must be performed for all base constructors.

### Cartan Property Verification
For root lattices of finite type, the relationship $A = -G$ must be verified:
- **Test Case A2**: Verify that $-G$ yields the standard $A_2$ Cartan matrix $\begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$.
- **Test Case E8**: Verify the Cartan structure for the $E_8$ lattice constructor.

### Reflection Preservation
The primary gate for root lattice correctness is the preservation of the form under simple reflections $s_i$:
- **Invariant**: $\langle s_i(v), s_i(w) \rangle = \langle v, w \rangle$
- **Verification**: This must be tested for all hyperbolic and parabolic realizations.

## 2. Verification Strategies

### Cross-Validation
- **Independent Methods**: Compare signatures calculated via eigenvalues in `AA` against characteristic polynomial decomposition in `QQ`.
- **Golden References**: Compare maximal parabolic counts against Lannér's list for small dimensions ($n \leq 10$).

### Determinant Fallacy
- **WARNING**: Do NOT use determinant signs alone to classify parabolicity or hyperbolic signatures. 
- **Rigor**: Use explicit signature calculation ($(p, q, r)$) and rank verification to distinguish between parabolic (nullity 1) and indefinite cases.

### Exact Arithmetic
- **Mandate**: All verification suites must run over the Algebraic Real Field (`AA`) or specific number field extensions.
- **Fail Pattern**: Epsilon-based comparisons are strictly prohibited in the authority gate.

## 3. Test Data Specification

### Sage-First Construction
All test data must be constructed using SageMath native objects (e.g., `CoxeterGroup`, `CartanMatrix`) to ensure the input to the `BilinearModule` factory is a valid geometric object.
