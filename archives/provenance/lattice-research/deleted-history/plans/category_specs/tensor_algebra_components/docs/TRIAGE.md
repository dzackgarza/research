# Tensor Algebra Components Triage

## Current Scope

This subtree is intentionally minimal.

Included now:

- Category owner for component modules `T_R(M)[p,q]`.
- Central `Tensor` type as any element of any such component module.
- Constructor stubs that return tensor elements from Sage-backed construction and
  coordinate interop shapes.
- Named constructors for scalar matrices as `(0,2)` tensors and module-element
  matrices as `(1,2)` tensors.
- Inventory and mapping grounded in Sage's tensor-free-module docs.

Deferred:

- Exhaustive tensor calculus method mapping.
- Symmetry and antisymmetry subtrees.
- Full component-storage API.
- Tensor contraction, trace, display, and index-notation surfaces.
- A detailed migration guide for all old component container inputs.
