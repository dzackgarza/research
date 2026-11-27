# AGENTS.md — tensor_algebra_components

GOAL: record tensor-algebra component modules and tensor elements as a small category
subtree.

This subtree owns the category whose objects are the graded pieces
`T_R(M)[p,q]` for finite-rank free modules `M`, and whose elements are tensors in
those parents. The parent categories are `Modules(R).TensorProducts()` and
`Modules(R).Free().FiniteRank()`.

Tasks:
- Keep Sage inventory and mapping in this subtree before adding new spec surface.
- Do not model all tensor calculus here. Add only the methods needed to identify
  tensor component modules, tensor elements, and their tensor type.
- Do not make `TensorAlgebraComponents` a Sage axiom. It is a named subtree with
  `Modules(R).TensorProducts()` and `Modules(R).Free().FiniteRank()` as parent
  categories.
- Constructor methods may accept interop component shapes such as nested lists and
  lists of matrices, but they return tensor elements. The component module is
  recoverable as `tensor.parent()`.
- Interop component shapes are interpreted through the base module's preferred
  generating set. Do not expose a separate `basis` argument on tensor constructors,
  and never forward basis/table/list/matrix shapes into algebra constructors.
- Use standard Sage tensor type order throughout: `(p,q)` means `p` contravariant and
  `q` covariant slots. `tensor_type()` is the only public tuple-valued type method;
  do not add aliases such as `tensor_bidegree()` or reinterpret rank.
- `DualObjects()` stays in this subtree: `T_R(M)[p,q]^* = T_R(M)[q,p]`, so the
  dual object's tensor type is the reversed tensor type. Do not introduce separate
  `dualized_*` or `form_domain_*` surfaces to remember the original component.
- `from_matrix` is the scalar-valued bilinear-form constructor and returns a `(0,2)`
  tensor. `from_module_element_matrix` is the multiplication-table constructor and
  returns a `(1,2)` tensor for `M \otimes_R M -> M`.
