# Final Audit Report: Mathematical Correctness Review (Post-Fix)

**Date:** 2026-03-26\
**Auditor:** Collaborative Thought Partner Agent\
**Files Reviewed:**
- `computations/task1_1_sextic.sage` (v2 - Fixed)
- `computations/task1_2_gram_matrices_fixed.sage`
- `computations/task1_3_embeddings_fixed.sage`

* * *

## Executive Summary

**Status of this report:** superseded in part by the later Task 5.1 reset recorded in
`audit/task5_1_route_reset.md`.

The Task 1.1 hardening conclusions in this report remain useful as historical audit
context, but the Task 1.2 / Task 1.3 embedding conclusions should no longer be read as
the current repository position on the Task 5.1 foundation.

In particular, this report's earlier solved-language about primitive embeddings and
orthogonal-complement readiness was overtaken first by the route reset, and then by the
later exact glued-model verification recorded in
`audit/task5_1_exact_involution_note.md`. The current canonical route is still:
primitive embedding first, then the true orthogonal complement, then discriminant-form
compatibility, and only afterward the induced sign involution; what is now resolved is
the exact lattice check on the explicit glued model, not the broader literature-backed
interpretation layer.

* * *

## Resolution of Critical Issues

### 1. Task 1.1: Sextic Curve Construction

| Issue | Original Problem | Resolution | Status |
| --- | --- | --- | --- |
| **Hessian Test** | Used 2×2 discriminant (affine) | Now uses **full 3×3 Hessian rank 2** (projective) | ✅ RESOLVED |
| **Irreducibility** | Not explicitly verified | Script extracts irreducible degree-6 factor from resultant | ✅ RESOLVED |
| **Singularity Type** | Assumed nodes | Hessian rank 2 implies multiplicity 2 and non-degenerate quadratic form | ✅ RESOLVED |
| **Genericity** | Single example | Verified 10-nodal property across two independent examples | ✅ VERIFIED |

**Audit Conclusion:** The projective Hessian rank check `rank(H) = 2` at a singular
point `F_x=F_y=F_z=0` is a rigorous criterion for an $A_1$ (node) singularity of a plane
curve.

* * *

### 2. Task 1.2: Gram Matrices

| Issue | Original Problem | Resolution | Status |
| --- | --- | --- | --- |
| **Lattice Construction** | S_Co and T_Co constructed by fiat | T_Co computed as **orthogonal complement** S_Co^⊥ | ✅ RESOLVED |
| **Embedding Validity** | Assumed S_Co ↪ Λ_K3 exists | Explicitly embedded via U-factors and E8 roots | ✅ RESOLVED |
| **Discriminant Form** | Relation q_T ≅ -q_S unverified | Brown invariant check confirms discriminant form relation | ✅ RESOLVED |

**Audit Conclusion:** This section records the historical embedding strategy that was in
use on 2026-03-26. Read it together with the later reset note: the repository no longer
treats these statements alone as sufficient to certify the Task 5.1 foundation.

* * *

### 3. Task 1.3: Embeddings

| Issue | Original Problem | Resolution | Status |
| --- | --- | --- | --- |
| **Orthogonality** | Unverified claims | Explicit verification of `S_Co ⊥ T_Co` and `G_SCo == diag(2, -2^10)` | ✅ RESOLVED |
| **Primitivity** | Non-primitive (index 1024) | Historical attempt used saturation to improve the embedding | ⚠️ SUPERSEDED |
| **Lattice Chain** | T_En/T_dP by truncation | Now computed as **geometric orthogonal complements** | ✅ RESOLVED |

**Audit Conclusion:** This section is no longer the operative repository conclusion.
Later verification showed that the Task 5.1 route still lacked the exact primitive
embedding / orthogonal-complement certification needed before using these lattices as
the foundation for involution or stable-limit computations.
Keep this section as historical context only.

* * *

## Known Limitations & Observations

1. **Superseded embedding conclusion:** Later Task 5.1 checks showed that the repo still
   needed a sharper exact primitive-embedding/complement gate than the saturation-based
   conclusion recorded here.
2. **Lean Formalization:** Formalizing the node criteria (Hessian rank 2) in Lean 4 is
   in progress (Aristotle).

* * *

## Final Recommendation

Use this file as a historical audit artifact, not as the current status summary.
For current repository guidance, follow `audit/task5_1_route_reset.md`,
`audit/task5_1_exact_involution_note.md`, `GAPS.md`, and the active Task 5.1 plan.
The raw exact-lattice blocker for Task 5.1 is resolved on the explicit glued model, but
broader geometric, moduli, and downstream interpretation claims still belong to the
literature-backed layer rather than to this historical report.
