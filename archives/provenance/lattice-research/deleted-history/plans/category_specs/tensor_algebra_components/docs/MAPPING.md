# Tensor Algebra Components Mapping

This file maps the narrow Sage tensor-free-module surface into the project
`tensor_algebra_components` subtree.

| Sage surface | Project surface | Rationale |
| --- | --- | --- |
| `TensorFreeModule` / `M.tensor_module(k,l)` | `TensorAlgebraComponents(R)` object, with parent categories `Modules(R).TensorProducts()` and `Modules(R).Free().FiniteRank()` | The object is the graded piece `T_R(M)[k,l]`, hence a finite-rank free module when `M` is finite-rank free. |
| `FreeModuleTensor` / `M.tensor((k,l), ...)` | `Tensor` element | A tensor is an element of some component module `T_R(M)[k,l]`; its parent recovers that module. |
| `base_module()` | `base_module() -> RModule` on component parents and tensor elements | This is the structural link from `T_R(M)[k,l]` back to `M`. |
| `tensor_type()` | `tensor_type() -> tuple[Integer, Integer]` | This is the unique public tuple-valued tensor type `(k,l)`, with `k` contravariant and `l` covariant slots. Ordinary rank is inherited from the finite-rank free module structure. |
| Sage `tensor_rank()` as total tensor order `k + l` | `sum(tensor_type())` when the total tensor order is needed | The project does not expose a second tensor-type/rank method. The tuple is `tensor_type()`; total order is a derived integer. |
| Module `rank()` / `dimension()` on tensor component parents | inherited from `Modules(R).Free().FiniteRank()` | The tensor component is a finite-rank free module, so ordinary module rank comes from that supercategory. It is not tensor type data. |
| `t[:]`, `t.set_comp(basis)[:]`, indexed component assignment | Named interop constructors on `TensorAlgebraComponents(R).Constructors()` using the base module's preferred generating set | Component arrays are coordinate inputs for constructing tensor elements, not public tensor objects. The old catch-all `from_components(...)` surface is private helper code only; public callers use the named matrix, module-element matrix, multidimensional-list, or list-of-matrices route. Sage's explicit `basis` plumbing is not part of the project constructor surface. |
| Matrix over `R` | `TensorAlgebraComponents(R).Constructors().from_matrix(base_module=M, entries=B)` | A scalar-valued bilinear form `M \otimes_R M -> R` is a covariant `(0,2)` tensor. |
| Matrix of module elements `Sequence[Sequence[RModuleElement]]` | `TensorAlgebraComponents(R).Constructors().from_module_element_matrix(base_module=M, entries=products)` | A multiplication table with entries in `M` is the bilinear map `M \otimes_R M -> M`, hence a structure tensor in `M \otimes_R M^* \otimes_R M^*` of type `(1,2)`. |
| Multiplication tensor structure constants | `Tensor.structure_constants()` | A tensor of type `(1,2)` determines coordinate structure constants in the preferred generating set of its base module. Algebra constructors may read this canonical tensor surface instead of accepting Sage table/list shapes directly. |
| Lists of matrices for component data | `TensorAlgebraComponents(R).Constructors().from_matrices(...)` | This is an admitted interop shape for old table-like data. The return value is a tensor element. |
| Multidimensional lists for component data | `TensorAlgebraComponents(R).Constructors().from_multidimensional_list(...)` | This is an admitted interop shape for coordinate data. The return value is a tensor element. |
| Catch-all component data | no public constructor; private `_from_components(...)` helper only | Shape unions are implementation-local. Public callers use the named constructor matching the data they hold. |

## Dual Objects And Forms

The dual-object surface of this subtree owns integral forms and remains inside the
tensor-component category:

```text
T_R(M)[p,q]^* = T_R(M)[q,p]
```

The same dual component is naturally interpretable as `Hom_R(T_R(M)[p,q], R)`.
`Modules(R).HomCategory().Forms().Integral()` records that evaluation interpretation,
but it does not own the tensor component. If the original component has
`tensor_type() == (p,q)`, the dual component has `tensor_type() == (q,p)`.

The forms subtree owns formed modules: attaching such a tensor as form data to a module
places the result in `FormedModules(R).Bilinear()` or another forms-owned refinement.

| Sage/form surface | Project resurfacing |
| --- | --- |
| `Hom_R(T_R(M)[p,q], R)` as a form parent | `TensorAlgebraComponents(R).DualObjects()` with extra supercategory `Modules(R).HomCategory().Forms().Integral()` |
| Evaluating a form on a tensor | inherited hom/morphism evaluation from `Modules(R).HomCategory().Forms()` |

## Algebra Constructor Use

An algebra multiplication on a finite-rank free module `M` should be validated as a
`Tensor` with `tensor_type() == (1, 2)` and `base_module() is M`. Constructor
interop may accept multiplication tables as `Sequence[Sequence[RModuleElement]]` or
legacy lists of matrices, but those shapes belong here. `Algebras(R).Constructors()`
receives only the tensor element after this subtree has converted the shape into
canonical tensor data. Its only public extraction surface is
`Tensor.structure_constants()`, which recovers the coordinate structure constants
encoded by the tensor.
