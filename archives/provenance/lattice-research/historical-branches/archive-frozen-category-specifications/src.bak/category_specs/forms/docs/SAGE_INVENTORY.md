# Forms Sage Inventory

The forms subtree owns the formed-module interpretation recorded in these canonical inventories:

- `modules/docs/SAGE_INVENTORY.md` for `FreeQuadraticModule`, `TorsionQuadraticModule`, `TorsionQuadraticForm`, and module constructor routing.
- `lattices/docs/SAGE_INVENTORY.md` for bilinear, quadratic, torsion, and integral lattice method surfaces.
- `tensor_algebra_components/docs/SAGE_INVENTORY.md` for tensor component representations of scalar-valued bilinear forms.

Relevant Sage surfaces:

| Sage surface | Forms-subtree evidence |
| --- | --- |
| `FreeQuadraticModule_generic` | Free finite-rank module with a bilinear/quadratic form; supplies Gram and inner-product matrix methods. |
| `FreeQuadraticModule_integer_symmetric` | Integral nondegenerate symmetric bilinear module over `ZZ`; supplies lattice algorithms and discriminant-group construction. |
| `TorsionQuadraticModule` | Finite torsion module with bilinear and quadratic products; supplies torsion Gram matrices and finite quadratic form invariants. |
| `TorsionQuadraticForm(q)` | Sage constructor for a torsion quadratic module from a rational symmetric matrix. |
| `TensorFreeModule` dual components | Tensor representation of forms as `(0,1)`, `(0,2)`, and related tensor types. |

This file is an ownership inventory pointing to the source-backed Sage inventories above.
