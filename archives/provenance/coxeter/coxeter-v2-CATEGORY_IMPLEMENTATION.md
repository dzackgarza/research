<!--
Origin: gitclones/Coxeter-v2/docs/authority/CATEGORY_IMPLEMENTATION.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a PROVENANCE RECORD: a corpus map or superseded design plan, kept
so the routing decisions of the migration stay legible. It is not a
statement about the current repository.
-->

# Category Implementation Authority Document

This document defines the implementation patterns and translation rules for migrating legacy source code to the new Category-based architecture. It consolidates literal extractions from the legacy `src` archives and the `BilinearModule` design documents.

## 1. Gram Matrix & Quadratic Forms

The legacy implementation of `GramMatrix` in `coxeter_matrices.py` provides the foundational logic for the new `BilinearModule` parent.

- **Legacy Node**: Diagonal entries are negative ($G_{ii} < 0$), encoding indefinite forms.
- **Translation Rule**: This convention is preserved. The `BilinearModules` category must enforce this via validation in the `ParentMethods.gram_matrix()` implementation.
- **Exact Arithmetic**: All matrix operations (determinant, signature, inverse) must utilize SageMath's exact arithmetic types (`ZZ`, `QQ`, `AlgebraicNumberField`).

## 2. Lattice to Bilinear Module Mapping

The transition from the legacy `Lattice` class to the new `BilinearModule` structure follows these mapping rules:

| Legacy Component (`lattices/lattice.py`) | New Category Implementation |
| :--- | :--- |
| `FreeQuadraticModule_integer_symmetric` | `BilinearModule` (Parent wrapper) |
| `signature()` | `ParentMethods.signature()` (via Sage's `eigenvalues`) |
| `dual_lattice()` | `ParentMethods.dual()` |
| `sublattice()` | `ParentMethods.submodule()` (standard Sage) |
| `LatticeElement` | `BilinearModules.ElementMethods` (methods injected into existing elements) |

### Key Categorical Logic
- **Bilinear Pairing**: The legacy `v1 * v2` (which bypassed dot product to use the Gram matrix) is now implemented in `BilinearModules.ElementMethods.__mul__`.
- **Injection instead of Inheritance**: Instead of elements inheriting from a custom `LatticeElement` class, they are standard Sage module elements that gain `*` and `inner_product()` behavior when their parent is and remains in the `BilinearModules` category.

## 3. Hyperbolic Root Lattice Specialization

Specialized logic for hyperbolic systems from `hyperbolic/hyperbolic_root_lattice.py` is migrated to the `IndefiniteBilinearModules` and `HyperbolicBilinearModules` subcategories.

- **Maximal Parabolic Enumeration**:
    - **Legacy Logic**: Enumerate subsets of vertices and check if the induced submatrix is negative semidefinite with rank $n-1$.
    - **Optimization Node**: Use eigenvalue monotonicity (interlacing) to prune the search tree (from `alternative-approaches.md`).
- **Finite Covolume Check**:
    - **Rule**: Finite volume iff all maximal parabolics are of affine type (negative semidefinite).
    - **Implementation**: `IndefiniteBilinearModules.ParentMethods.is_finite_volume()`.

## 4. Construction Patterns

The unified factory `BilinearModule()` replaces specific constructors for `GramMatrix`, `Lattice`, and `HyperbolicRootLattice`.

- **Automatic Category Discovery**:
    1. Check signature: (0, n, 0) $\rightarrow$ `NegativeDefinite`.
    2. Check signature: (0, n-1, 1) $\rightarrow$ `Parabolic`.
    3. Check signature: (1, n-1, 0) $\rightarrow$ `Hyperbolic`.
    4. Default $\rightarrow$ `BilinearModule`.

### Coxeter Matrix to Gram Matrix
The `from_coxeter_matrix` logic (legacy `coxeter_matrices.py:L177`) is strictly preserved:
- For simple roots, $G_{ii} = -2$.
- $G_{ij} = -2 \cos(\pi/M_{ij})$.
- **Hyperbolic Extension**: Indefinite edges ($M_{ij} = \infty$) require explicit embedding data or default to $G_{ij} \leq -2$.

## 5. Hyperbolic Utility Methods

Specialized geometric utilities are injected into the `HyperbolicBilinearModules` category:

- **Light Cone Search**: `light_cone_vectors(max_height)` (from `hyperbolic_root_lattice.py:L289`). Use coordinates product search to find $v$ such that $v * v = 0$.
- **Reflection Walls**: `reflection_walls()` (from `hyperbolic_root_lattice.py:L326`). Return the simple roots $\{\alpha_i\}$ as normal vectors to the reflection hyperplanes.

## 5. Summary of Transferred Invariants

- **Negative Diagonal Convention**: $G_{ii} = -2$ for roots.
- **Traceability**: All algorithms derived from `hyperbolic_root_lattice.py` must retain 1:1 parity with the legacy mathematical logic, specifically the `is_compact()` (cusp-count based) and `is_finite_volume()` criteria.
- **Formatting**: Preserve the `_repr_` style: `"Hyperbolic root lattice of rank n"` becomes `"Bilinear module of rank n over R"`.
