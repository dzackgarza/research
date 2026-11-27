# Forms Mapping

`FormedModules(R)` is the forms-subtree owner for modules equipped with forms.
It is the named spelling of `Modules(R, dispatch=False).WithForms()`.

## Ownership

| Surface | Owner | Notes |
| --- | --- | --- |
| `Modules(R).WithForms()` | `forms.subcategories.with_forms._WithForms` | Modules keeps the Sage-compatible route; forms owns the class and method surface. |
| `Modules(R).WithForms().Bilinear()` | `forms.subcategories.bilinear._BilinearModules` | Owns bilinear evaluation and generic bilinear predicates. |
| `Modules(R).WithForms().Quadratic()` | `forms.subcategories.quadratic._QuadraticModules` | Owns quadratic evaluation. |
| Symmetric, alternating, nondegenerate, definite, indefinite, integral, rational bilinear axioms | `forms.subcategories.*` | These are formed-module properties, not lattice-only properties. |
| Free bilinear modules | `forms.subcategories.free_bilinear._FreeBilinearModules` | First tier where Gram matrices, determinant, and discriminant are universally meaningful. |
| Finite-rank free formed-module chain used by `Lattices(R)` | `forms.chain` | Lattices imports this chain and adds only the named `Lattice` endpoint. |
| Finite torsion quadratic modules | `forms.subcategories.torsion_quadratic_modules._TorsionQuadraticModules` | Modules keeps `TorsionQuadraticModules()` as a compatibility constructor route. |
| `Lattices(R)` | `lattices.chain._Lattices` | Lattice-specific endpoint and lattice construction categories remain in `lattices`. |

## Compatibility Routes

The module and lattice import paths remain valid:

- `category_specs.modules.subcategories.with_forms._WithForms`
- `category_specs.modules.subcategories.bilinear._BilinearModules`
- `category_specs.modules.subcategories.quadratic._QuadraticModules`
- `category_specs.modules.subcategories.torsion_quadratic_modules._TorsionQuadraticModules`
- `category_specs.lattices.subcategories.symmetric._SymmetricBilinearModules`
- analogous lattice paths for alternating, nondegenerate, definite, indefinite,
  integral, rational, and free bilinear categories.

Those files are shims. New specs should import or document formed-module ownership
through `forms`.

## Boundary With Tensor Components

`TensorAlgebraComponents(R)` owns tensor component modules and tensor elements.
A scalar-valued bilinear form may be constructed there as a `(0,2)` tensor. The object
becomes a formed module only when attached as form data to a module category in this
subtree.

## Boundary With Lattices

Lattices are integral, nondegenerate, symmetric, finite-rank free bilinear modules with
the additional named `Lattice` axiom. Formed-module methods such as `b`, `gram_matrix`,
`dual_lattice`, and `orthogonal_group` remain owned by forms. The quotient class map
`L^* -> L^*/L` belongs to `Lattices(R).DualObjects().ElementMethods` because it is
nontrivial on dual-lattice elements and zero on ordinary elements of `L`.
Lattice-specific specializations such as `OverIntegers`, `Even`, `Unimodular`, and
lattice construction categories remain owned by `lattices`.
