# Tensor Algebra Components Sage Inventory

Primary source:

- Sage docs: <https://doc.sagemath.org/html/en/reference/tensor_free_modules/sage/tensor/modules/free_module_tensor.html>
- Sage docs: <https://doc.sagemath.org/html/en/reference/tensor_free_modules/sage/tensor/modules/tensor_with_indices.html>
- Sage docs: <https://doc.sagemath.org/html/en/reference/tensor_free_modules/sage/tensor/modules/finite_rank_free_module.html>

This inventory is intentionally narrow. It records the Sage facts needed to scaffold
the project `TensorAlgebraComponents` subtree and the central `Tensor` type.

## Sage Objects

| Sage surface | Inventory fact |
| --- | --- |
| `FreeModuleTensor` | Element class for tensors on a finite-rank free module `M` over a commutative ring `R`. |
| `TensorFreeModule` | Parent class for all tensors of a fixed type `(k,l)` on `M`; Sage writes this as `T^(k,l)(M)`. |
| Derived tensor element classes | Sage lists alternating contravariant tensors, finite-rank free-module elements as type `(1,0)` tensors, alternating forms, and automorphisms as specialized tensor classes. |

## Mathematical Definition Recorded By Sage

Sage defines a tensor of type `(k,l)` on `M` as a multilinear map

```text
(M*)^k x M^l -> R
```

where `M* = Hom_R(M, R)`. Thus `k` counts contravariant slots and `l` counts
covariant slots. Sage calls `k + l` the tensor rank. The tuple `(k,l)` is
available through `tensor_type()`.

## Construction And Recovery

| Sage surface | Behavior |
| --- | --- |
| `M.tensor((k,l), name=..., latex_name=..., sym=..., antisym=...)` | Constructs a `FreeModuleTensor` element. |
| `M.tensor_module(k,l, sym=..., antisym=...)` | Constructs or returns the `TensorFreeModule` parent `T^(k,l)(M)`, with optional symmetry metadata on the parent itself. |
| `t.parent()` | Recovers the tensor component module. Sage examples show `t.parent() is M.tensor_module(k,l)`. |
| `t.base_module()` and `t.parent().base_module()` | Recover `M`. |
| `t.tensor_type()` and `t.parent().tensor_type()` | Recover `(k,l)`. |
| `t.tensor_rank()` | Returns the Sage total order `k + l`, not the `tensor_type()` tuple. |
| `sym=` / `antisym=` | Sage stores declared symmetry/antisymmetry data on the constructed tensor or tensor module; `symmetries()` reports it. |

## Component Interop

Sage component assignment is coordinate interop, not the public mathematical object:

| Sage surface | Behavior |
| --- | --- |
| `t.set_comp(basis)[...] = ...` | Assigns components in a chosen basis. |
| `t[:] = ...` | Assigns components in the default basis. |
| `t[basis, ...] = ...` | Index notation shortcut for chosen-basis assignment. |
| `matrix(t.comp(basis))` | For rank-two tensors, views components as a matrix over the base ring. |
| `Components` | Sage storage object for nonzero coordinate components. |

The project constructors preserve useful interop shapes such as nested lists and
lists of matrices, but map them to tensor elements rather than admitting raw
component containers as category objects.

Sage's component storage facts that matter for this subtree:

- `Components` is the storage class behind basis-indexed coordinate data.
- only nonzero components are stored internally;
- basis-specific component dictionaries and `display_comp(...)` are rendering or
  storage interop, not the mathematical tensor object.

Project-specific constructor shapes built from this inventory:

| Project shape | Tensor type | Meaning |
| --- | --- | --- |
| Matrix over the base ring | `(0,2)` | Scalar-valued bilinear form `M \otimes_R M -> R`. |
| `Sequence[Sequence[RModuleElement]]` | `(1,2)` | Multiplication-style bilinear map `M \otimes_R M -> M`, represented as a structure tensor in `M \otimes_R M^* \otimes_R M^*`. |

## Tensor Calculus Surfaces Recorded By Sage

| Sage surface | Inventory fact |
| --- | --- |
| `t.trace(pos1, pos2)` | Contracts one contravariant and one covariant slot of a single tensor; the result is scalar only in tensor type `(1,1)`, otherwise it is a tensor of type `(k-1,l-1)` on the same base module. |
| `t.contract(...)` | Performs contraction between two tensors along an opposite-variance pair of slots; Sage admits defaulted and explicit position spellings. |
| `t.display(...)` | Prints the tensor expansion in a chosen basis, with optional formatting controls and basis change computation. |
| `t.display_comp(...)` | Prints components one per line in a chosen basis. |
| `TensorWithIndices(t, indices)` and `t['...']` | Technical index-notation layer for contractions and symmetrizations; repeated indices encode Einstein contraction and bracket/parenthesis syntax encodes antisymmetrization/symmetrization. |
