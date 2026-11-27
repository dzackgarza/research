# Tensor Algebra Components Sage Inventory

Primary source:

- Sage docs: <https://doc.sagemath.org/html/en/reference/tensor_free_modules/sage/tensor/modules/free_module_tensor.html>

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
| `M.tensor_module(k,l)` | Constructs or returns the `TensorFreeModule` parent `T^(k,l)(M)`. |
| `t.parent()` | Recovers the tensor component module. Sage examples show `t.parent() is M.tensor_module(k,l)`. |
| `t.base_module()` and `t.parent().base_module()` | Recover `M`. |
| `t.tensor_type()` and `t.parent().tensor_type()` | Recover `(k,l)`. |
| `t.tensor_rank()` | Returns the Sage total order `k + l`, not the `tensor_type()` tuple. |

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

Project-specific constructor shapes built from this inventory:

| Project shape | Tensor type | Meaning |
| --- | --- | --- |
| Matrix over the base ring | `(0,2)` | Scalar-valued bilinear form `M \otimes_R M -> R`. |
| `Sequence[Sequence[RModuleElement]]` | `(1,2)` | Multiplication-style bilinear map `M \otimes_R M -> M`, represented as a structure tensor in `M \otimes_R M^* \otimes_R M^*`. |
