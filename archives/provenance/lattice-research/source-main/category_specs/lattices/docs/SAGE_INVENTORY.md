# SAGE_INVENTORY.md — Lattices Subtree

Indexes every Sage class and method relevant to the lattices hierarchy, with on-disk
paths and line numbers. Consult this before searching Sage source directly.

`SAGE_LIB` below expands to:
`/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage`

---

## Top-level Sage constructor and construction functions

| File | Line | Surface | Signature | Notes |
|------|------|---------|-----------|-------|
| `SAGE_LIB/modules/free_quadratic_module.py` | 86 | `FreeQuadraticModule` | `(base_ring, rank, inner_product_matrix, sparse=False, inner_product_ring=None)` | free quadratic module factory over a commutative ring; coerces `rank` to `int`, canonicalizes `inner_product_matrix` as an immutable `rank x rank` matrix over `base_ring`, caches by `(base_ring, rank, matrix, sparse)`, and selects field, PID, integral-domain, or generic ambient backend from base-ring category; the form matrix need not be symmetric or definite; `inner_product_ring` is a source stub that raises `NotImplementedError` |
| `SAGE_LIB/modules/free_quadratic_module.py` | 190 | `QuadraticSpace` | `(K, dimension, inner_product_matrix, sparse=False)` | field-only wrapper around `FreeQuadraticModule`; `K` must be a field and `sparse` must be a boolean |
| `SAGE_LIB/modules/free_quadratic_module.py` | 223 | `InnerProductSpace` | alias of `QuadraticSpace` | Sage-compatible alias |
| `SAGE_LIB/modules/free_quadratic_module.py` | 232 | `is_FreeQuadraticModule` | `(M)` | deprecated predicate; Sage docs direct callers to `isinstance(..., FreeQuadraticModule_generic)` |
| `SAGE_LIB/modules/free_quadratic_module_integer_symmetric.py` | 73 | `IntegralLattice` | `(data, basis=None)` | integral lattice factory from symmetric matrix, integer Euclidean rank, Cartan/root descriptor, or `U`/`H`; optional basis selects rows in the ambient quadratic space; source checks symmetry, then the returned class checks nondegeneracy and integrality |
| `SAGE_LIB/modules/free_quadratic_module_integer_symmetric.py` | 262 | `IntegralLatticeDirectSum` | `(Lattices, return_embeddings=False)` | orthogonal direct sum of a list of integral lattices; source requires Sage integral-lattice instances, block-diagonalizes ambient forms, block-embeds selected bases, and optionally returns summand embeddings |
| `SAGE_LIB/modules/free_quadratic_module_integer_symmetric.py` | 372 | `IntegralLatticeGluing` | `(Lattices, glue, return_embeddings=False)` | overlattice of a direct sum from rows of discriminant-group glue elements; source checks row length and component membership, lifts each glue component by `lift()*order()/order`, and optionally returns summand embeddings into the glued lattice |
| `SAGE_LIB/modules/free_quadratic_module_integer_symmetric.py` | 1708 | `local_modification` | `(M, G, p, check=True)` | p-adic local-genus modification algorithm: constructs `L = IntegralLattice(G)`, replaces it by its `p`-maximal overlattice, compares p-adic normal forms for `L_max` and `M`, sets `d = p^valuation_p(denominator(G^-1))`, returns `M.sublattice(((M.span(B) & M) + d*M).gens())`, and with `check=True` asserts equality of the p-adic genus symbols of the result and `G` at precision `scale` |

### Package-level public import surfaces

| File | Line | Surface | Notes |
|------|------|---------|-------|
| `SAGE_LIB/modules/all.py` | 16 | `FreeModule`, `VectorSpace`, `span` | public module import route; `FreeModule(..., inner_product_matrix=...)` can dispatch to `FreeQuadraticModule` |
| `SAGE_LIB/modules/all.py` | 18 | `FreeQuadraticModule`, `QuadraticSpace`, `InnerProductSpace` | public import route for free quadratic module constructors |
| `SAGE_LIB/modules/all.py` | 24 | `vector`, `free_module_element`, `zero_vector`, `random_vector` | public module-element helper import route |
| `SAGE_LIB/modules/all.py` | 31 | `linear_transformation` | public vector-space morphism constructor import route |
| `SAGE_LIB/modules/all.py` | 37 | `FilteredVectorSpace`, `MultiFilteredVectorSpace`, `IntegralLattice`, `TorsionQuadraticForm` | public lazy-import route for filtered vector spaces, integral lattices, and torsion quadratic forms |
| `SAGE_LIB/quadratic_forms/genera/all.py` | 8 | `Genus`, `LocalGenusSymbol`, `is_GlobalGenus` | public genus-package import route |
| `SAGE_LIB/geometry/all.py` | 14 | `ToricLattice` | public geometry lazy-import route for toric character lattices |
| `SAGE_LIB/geometry/all.py` | 1-20 | `PolyhedralComplex`, `Cone`, `random_cone`, `cones`, `Fan`, `FaceFan`, `NormalFan`, `Fan2d`, `FanMorphism`, `LatticePolytope`, `NefPartition`, `ReflexivePolytope`, `ReflexivePolytopes`, `lattice_polytope`, `toric_plotter`, `VoronoiDiagram`, `RibbonGraph`, `HyperplaneArrangements`, `OrderedHyperplaneArrangements`, `hyperplane_arrangements`, and wildcard imports from `polyhedron.all` and `hyperbolic_space.all` | public geometry import routes that touch toric/discrete geometry vocabulary but are not algebraic formed-lattice constructors; route as geometry/polyhedral/interop context unless a later geometry spec admits a specific object |

---

## Tier 0 — Generic modules with inner product (free, over commutative ring)

### `FreeQuadraticModule_generic`
**File:** `SAGE_LIB/modules/free_quadratic_module.py:258`  
**Inherits:** `free_module.FreeModule_generic`  
**Role:** Base class for all free quadratic modules; carries an inner product matrix.

| Line | Method | Signature | Notes |
|------|--------|-----------|-------|
| 310 | `__init__` | `(base_ring, rank, degree, inner_product_matrix, sparse=False)` | |
| 369 | `ambient_module` | `(self)` | ambient quadratic module |
| 390 | `determinant` | `(self)` | det of Gram matrix |
| 408 | `discriminant` | `(self)` | `(-1)^r * det(gram_matrix)`, where `r = rank // 2` in Sage's convention |
| 439 | `gram_matrix` | `(self)` | `B·A·B^T` where `A` = inner product matrix, `B` = basis |
| 472 | `inner_product_matrix` | `(self)` | raw inner product matrix |
| 335 | `_dense_module` | `(self)` | internal backend conversion to dense storage |
| 352 | `_sparse_module` | `(self)` | internal backend conversion to sparse storage |
| 526 | `_inner_product_is_dot_product` | `(self)` | internal optimization predicate for dot-product Gram data |
| 550 | `_inner_product_is_diagonal` | `(self)` | internal optimization predicate comparing the inner-product matrix to the diagonal matrix with the same diagonal |

### `FreeQuadraticModule_generic_pid`
**File:** `SAGE_LIB/modules/free_quadratic_module.py:588`  
**Inherits:** `FreeModule_generic_pid`, `FreeQuadraticModule_generic`

| Line | Method | Signature | Notes |
|------|--------|-----------|-------|
| 610 | `span` | `(self, gens, check=True, already_echelonized=False)` | R-span, need not be submodule |
| 637 | `span_of_basis` | `(self, basis, check=True, already_echelonized=False)` | free R-module on basis |
| 680 | `zero_submodule` | `(self)` | zero submodule |

### `FreeQuadraticModule_generic_field`
**File:** `SAGE_LIB/modules/free_quadratic_module.py:696`  
**Inherits:** `FreeModule_generic_field`, `FreeQuadraticModule_generic_pid`

| Line | Method | Notes |
|------|--------|-------|
| 731 | `span` | K-span |
| 771 | `span_of_basis` | K-basis |

### Ambient/submodule variants

These classes are Sage presentation strata for ambient objects, submodules, selected
bases, PID/field specializations, and display/storage behavior.  Most rows are backend
or display surfaces; `ambient_vector_space()` and `change_ring(R)` are mathematical
construction surfaces that still belong above the lattice endpoint.

| Line | Surface | Signature | Notes |
|------|---------|-----------|-------|
| 827 | `FreeQuadraticModule_ambient.__init__` | `(self, base_ring, rank, inner_product_matrix, sparse=False)` | ambient free quadratic module constructor |
| 846 | `FreeQuadraticModule_ambient._repr_` | `(self)` | display surface for degree, rank, and inner-product matrix |
| 880 | `FreeQuadraticModule_ambient._latex_` | `(self)` | LaTeX display of the ambient module |
| 904 | `FreeQuadraticModule_ambient._dense_module` | `(self)` | backend conversion to dense storage |
| 922 | `FreeQuadraticModule_ambient._sparse_module` | `(self)` | backend conversion to sparse storage |
| 952 | `FreeQuadraticModule_ambient_domain.__init__` | `(self, base_ring, rank, inner_product_matrix, sparse=False)` | integral-domain ambient constructor |
| 964 | `FreeQuadraticModule_ambient_domain._repr_` | `(self)` | display surface for ambient domain modules |
| 1013 | `FreeQuadraticModule_ambient_domain.ambient_vector_space` | `(self)` | scalar extension to the fraction-field ambient vector space |
| 1044 | `FreeQuadraticModule_ambient_pid.__init__` | `(self, base_ring, rank, inner_product_matrix, sparse=False)` | PID ambient constructor |
| 1074 | `FreeQuadraticModule_ambient_pid._repr_` | `(self)` | display surface for PID ambient modules |
| 1130 | `FreeQuadraticModule_ambient_field.__init__` | `(self, base_field, dimension, inner_product_matrix, sparse=False)` | field ambient constructor |
| 1169 | `FreeQuadraticModule_ambient_field._repr_` | `(self)` | display surface for field ambient modules |
| 1248 | `FreeQuadraticModule_submodule_with_basis_pid.__init__` | `(self, ambient, basis, inner_product_matrix, check=True, echelonize=True, echelonized_basis=None, already_echelonized=False)` | selected-basis PID submodule constructor |
| 1293 | `FreeQuadraticModule_submodule_with_basis_pid._repr_` | `(self)` | display surface for selected-basis PID submodules |
| 1337 | `FreeQuadraticModule_submodule_with_basis_pid._latex_` | `(self)` | LaTeX display of the row-span basis |
| 1351 | `FreeQuadraticModule_submodule_with_basis_pid.change_ring` | `(self, R)` | base-ring change preserving inner product and user basis when coercion succeeds |
| 1421 | `FreeQuadraticModule_submodule_pid.__init__` | `(self, ambient, gens, inner_product_matrix, check=True, already_echelonized=False)` | PID submodule constructor from generators |
| 1441 | `FreeQuadraticModule_submodule_pid._repr_` | `(self)` | display surface for PID submodules |
| 1519 | `FreeQuadraticModule_submodule_with_basis_field.__init__` | `(self, ambient, basis, inner_product_matrix, check=True, echelonize=True, echelonized_basis=None, already_echelonized=False)` | selected-basis field subspace constructor |
| 1550 | `FreeQuadraticModule_submodule_with_basis_field._repr_` | `(self)` | display surface for selected-basis field subspaces |
| 1641 | `FreeQuadraticModule_submodule_field.__init__` | `(self, ambient, gens, inner_product_matrix, check=True, already_echelonized=False)` | field subspace constructor from generators |
| 1660 | `FreeQuadraticModule_submodule_field._repr_` | `(self)` | display surface for field subspaces |

Exact class-qualified backend aliases:
`FreeQuadraticModule_generic._dense_module`,
`FreeQuadraticModule_generic._sparse_module`,
`FreeQuadraticModule_generic._inner_product_is_dot_product`,
`FreeQuadraticModule_generic._inner_product_is_diagonal`.

---

## Toric character-lattice boundary (Sage geometry)

### Top-level factory and deprecated predicates

| File | Line | Surface | Signature | Notes |
|------|------|---------|-----------|-------|
| `SAGE_LIB/geometry/toric_lattice.py` | 166 | `is_ToricLattice` | `(x)` | deprecated predicate; Sage docs direct callers to `isinstance(..., ToricLattice_generic)` |
| `SAGE_LIB/geometry/toric_lattice.py` | 199 | `is_ToricLatticeQuotient` | `(x)` | deprecated predicate; Sage docs direct callers to `isinstance(..., ToricLattice_quotient)` |
| `SAGE_LIB/geometry/toric_lattice.py` | 238 | `ToricLatticeFactory` | `UniqueFactory` subclass | factory for named rank-`n` toric free `ZZ` lattices |
| `SAGE_LIB/geometry/toric_lattice.py` | 322 | `ToricLatticeFactory.create_key` | `(rank, name=None, dual_name=None, latex_name=None, latex_dual_name=None)` | factory key and naming algorithm; docs warn not to call directly |
| `SAGE_LIB/geometry/toric_lattice.py` | 362 | `ToricLatticeFactory.create_object` | `(version, key)` | factory backend returning `ToricLattice_ambient`; docs warn not to call directly |
| `SAGE_LIB/geometry/toric_lattice.py` | 381 | `ToricLattice` | `(rank, name=None, dual_name=None, latex_name=None, latex_dual_name=None)` | public factory for named toric lattices |
| `SAGE_LIB/geometry/toric_lattice_element.pyx` | 106 | `is_ToricLatticeElement` | `(x)` | deprecated predicate; Sage docs direct callers to `isinstance(..., ToricLatticeElement)` |

### `ToricLattice_generic`

**File:** `SAGE_LIB/geometry/toric_lattice.py:389`
**Inherits:** `FreeModule_generic_pid`
**Role:** Free `ZZ`-module parent with toric parent identity, notation, conversion
barriers, and toric subobject/quotient parent preservation.

| Line | Method | Signature | Notes |
|------|--------|-----------|-------|
| 401 | `__call__` | `(self, *args, **kwds)` | element constructor/coercion; variadic coordinate shortcut and quotient-element lift path |
| 466 | `_coerce_map_from_` | `(self, other)` | coercion barrier for toric lattices with different ambient modules; returns `None` so element conversion is rejected by `__call__` rather than silently depending only on rank |
| 486 | `__contains__` | `(self, point)` | parent membership via attempted coercion |
| 527 | `construction` | `(self)` | returns `None` to prevent arithmetic between different toric lattices through Sage construction functors |
| 544 | `direct_sum` | `(self, other)` | toric direct sum when `other` is a toric lattice, otherwise inherited free-module direct sum |
| 601 | `intersection` | `(self, other)` | intersection sublattice construction |
| 643 | `quotient` | `(self, sub, check=True, positive_point=None, positive_dual_point=None, **kwds)` | toric quotient by a sublattice, with mutually exclusive codimension-one torsion-free sign-choice inputs |
| 743 | `saturation` | `(self)` | toric saturation when possible, otherwise inherited ambient submodule result |
| 764 | `span` | `(self, gens, base_ring=ZZ, *args, **kwds)` | toric sublattice from generators over `ZZ`; delegates otherwise |
| 808 | `span_of_basis` | `(self, basis, base_ring=ZZ, *args, **kwds)` | toric sublattice with user basis over `ZZ`; delegates otherwise |

### Toric ambient, sublattice, quotient, and element surfaces

| File | Line | Surface | Signature | Notes |
|------|------|---------|-----------|-------|
| `SAGE_LIB/geometry/toric_lattice.py` | 862 | `ToricLattice_ambient` | `(rank, name, dual_name, latex_name, latex_dual_name)` | ambient toric lattice parent; direct class construction is discouraged by docs |
| `SAGE_LIB/geometry/toric_lattice.py` | 900 | `ToricLattice_ambient._sage_input_` | `(self, sib, coerced)` | reproducible Sage input display |
| `SAGE_LIB/geometry/toric_lattice.py` | 923 | `ToricLattice_ambient.__richcmp__` | `(self, right, op)` | compares rank and associated names |
| `SAGE_LIB/geometry/toric_lattice.py` | 964 | `ToricLattice_ambient._latex_` | `(self)` | LaTeX display |
| `SAGE_LIB/geometry/toric_lattice.py` | 978 | `ToricLattice_ambient._repr_` | `(self)` | text display with dimension and name |
| `SAGE_LIB/geometry/toric_lattice.py` | 992 | `ToricLattice_ambient.ambient_module` | `(self)` | returns `self` |
| `SAGE_LIB/geometry/toric_lattice.py` | 1013 | `ToricLattice_ambient.dual` | `(self)` | named Hom-dual toric lattice; dual of dual caches back to `self` |
| `SAGE_LIB/geometry/toric_lattice.py` | 1044 | `ToricLattice_ambient.plot` | `(self, **options)` | plotting/display interop |
| `SAGE_LIB/geometry/toric_lattice.py` | 1070 | `ToricLattice_sublattice_with_basis` | `(ambient, basis, ...)` | sublattice with user-selected basis; intended route is `submodule_with_basis` |
| `SAGE_LIB/geometry/toric_lattice.py` | 1111 | `ToricLattice_sublattice_with_basis._repr_` | `(self)` | text display from selected basis |
| `SAGE_LIB/geometry/toric_lattice.py` | 1131 | `ToricLattice_sublattice_with_basis._latex_` | `(self)` | LaTeX display from selected basis |
| `SAGE_LIB/geometry/toric_lattice.py` | 1152 | `ToricLattice_sublattice_with_basis.dual` | `(self)` | quotient of the ambient dual by the integer kernel; only for saturated sublattices |
| `SAGE_LIB/geometry/toric_lattice.py` | 1174 | `ToricLattice_sublattice_with_basis.plot` | `(self, **options)` | plotting/display interop with lattice filter |
| `SAGE_LIB/geometry/toric_lattice.py` | 1211 | `ToricLattice_sublattice` | `(ambient, gens, ...)` | generated sublattice; intended route is `submodule` |
| `SAGE_LIB/geometry/toric_lattice.py` | 1253 | `ToricLattice_quotient_element` | `FGP_Element` subclass | quotient element with toric display and immutable compatibility |
| `SAGE_LIB/geometry/toric_lattice.py` | 1286 | `ToricLattice_quotient_element._latex_` | `(self)` | LaTeX display using bracketed lift notation |
| `SAGE_LIB/geometry/toric_lattice.py` | 1302 | `ToricLattice_quotient_element._repr_` | `(self)` | text display using bracketed lift notation |
| `SAGE_LIB/geometry/toric_lattice.py` | 1318 | `ToricLattice_quotient_element.set_immutable` | `(self)` | compatibility no-op because quotient elements are already immutable |
| `SAGE_LIB/geometry/toric_lattice.py` | 1338 | `ToricLattice_quotient` | `(V, W, check=True, positive_point=None, positive_dual_point=None, **kwds)` | quotient of a toric lattice by a sublattice; inherits FGP quotient presentation and stores a sign-flip flag only for one-generator torsion-free quotients |
| `SAGE_LIB/geometry/toric_lattice.py` | 1467 | `ToricLattice_quotient.gens` | `(self)` | quotient generators, sign-adjusted when codimension-one orientation data made the selected generator negative |
| `SAGE_LIB/geometry/toric_lattice.py` | 1493 | `ToricLattice_quotient._element_constructor_` | `(self, *x, **kwds)` | quotient element constructor/coercion with Smith-generator coordinate fallback |
| `SAGE_LIB/geometry/toric_lattice.py` | 1543 | `ToricLattice_quotient._latex_` | `(self)` | LaTeX display for quotient parent |
| `SAGE_LIB/geometry/toric_lattice.py` | 1563 | `ToricLattice_quotient._repr_` | `(self)` | text display for quotient parent |
| `SAGE_LIB/geometry/toric_lattice.py` | 1589 | `ToricLattice_quotient._module_constructor` | `(self, V, W, check=True)` | quotient module constructor returning `ToricLattice_quotient` |
| `SAGE_LIB/geometry/toric_lattice.py` | 1613 | `ToricLattice_quotient.base_extend` | `(self, R)` | returns `self` for `ZZ`, vector-space quotient for `QQ`, and raises for other rings |
| `SAGE_LIB/geometry/toric_lattice.py` | 1646 | `ToricLattice_quotient.is_torsion_free` | `(self)` | torsion-free predicate implemented as zero sum of Smith invariants |
| `SAGE_LIB/geometry/toric_lattice.py` | 1666 | `ToricLattice_quotient.dual` | `(self)` | sublattice of the ambient dual determined by the relation matrix kernel |
| `SAGE_LIB/geometry/toric_lattice.py` | 1686 | `ToricLattice_quotient.rank` | `(self)` | free-rank of quotient; `dimension = rank` |
| `SAGE_LIB/geometry/toric_lattice.py` | 1712 | `ToricLattice_quotient.coordinate_vector` | `(self, x, reduce=False)` | quotient coordinates with codimension-one sign adjustment |
| `SAGE_LIB/geometry/toric_lattice_element.pyx` | 142 | `ToricLatticeElement` | `Vector_integer_dense` subclass | toric lattice element class; direct construction is discouraged by docs |
| `SAGE_LIB/geometry/toric_lattice_element.pyx` | 167 | `ToricLatticeElement.__richcmp__` | `(self, right, op)` | compares ambient toric lattice before vector comparison |
| `SAGE_LIB/geometry/toric_lattice_element.pyx` | 205 | `ToricLatticeElement.__hash__` | `(self)` | vector hash compatibility when immutable |
| `SAGE_LIB/geometry/toric_lattice_element.pyx` | 225 | `ToricLatticeElement._act_on_` | `(self, other, self_on_left)` | dual-lattice action, integral-vector dot product interop, and quotient-lift action |
| `SAGE_LIB/geometry/toric_lattice_element.pyx` | 300 | `ToricLatticeElement._dot_product_` | `(self, right)` | raises for same-lattice multiplication; toric convention uses dual action instead |
| `SAGE_LIB/geometry/toric_lattice_element.pyx` | 328 | `ToricLatticeElement._latex_` | `(self)` | LaTeX display with parent subscript |
| `SAGE_LIB/geometry/toric_lattice_element.pyx` | 344 | `ToricLatticeElement._repr_` | `(self)` | text display with parent prefix |
| `SAGE_LIB/geometry/toric_lattice_element.pyx` | 360 | `ToricLatticeElement.__reduce__` | `(self)` | pickle compatibility hook |
| `SAGE_LIB/geometry/toric_lattice_element.pyx` | 373 | `ToricLatticeElement.plot` | `(self, **options)` | plotting/display interop |
| `SAGE_LIB/geometry/toric_lattice_element.pyx` | 397 | `unpickle_v1` | `(parent, entries, degree, is_mutable)` | pickle compatibility helper |

---

## Name-collision boundary — Sage lattice posets (not algebraic lattices)

Sage also uses "lattice" for order-theoretic lattice posets. These category providers
touch the subtree by name only: their objects are partially ordered sets with binary
meet/join, not finite-rank modules with bilinear forms.

| File | Line | Surface | Signature | Notes |
|------|------|---------|-----------|-------|
| `SAGE_LIB/categories/lattice_posets.py` | 19 | `LatticePosets` | category class | order-theoretic category of posets with unique binary join and meet |
| `SAGE_LIB/categories/lattice_posets.py` | 43 | `LatticePosets.super_categories` | `(self)` | returns `[Posets()]` |
| `SAGE_LIB/categories/lattice_posets.py` | 55 | `LatticePosets.Finite` | `LazyImport('sage.categories.finite_lattice_posets', 'FiniteLatticePosets')` | finite order-lattice axiom route |
| `SAGE_LIB/categories/lattice_posets.py` | 60 | `ParentMethods.meet` | `(self, x, y)` | abstract greatest lower bound in the poset order |
| `SAGE_LIB/categories/lattice_posets.py` | 76 | `ParentMethods.join` | `(self, x, y)` | abstract least upper bound in the poset order |
| `SAGE_LIB/categories/finite_lattice_posets.py` | 15 | `FiniteLatticePosets` | category-with-axiom class | finite order-theoretic lattice posets |
| `SAGE_LIB/categories/finite_lattice_posets.py` | 43 | `ParentMethods.join_irreducibles` | `(self)` | order-theoretic join-irreducible elements; source returns elements with exactly one lower cover |
| `SAGE_LIB/categories/finite_lattice_posets.py` | 65 | `ParentMethods.join_irreducibles_poset` | `(self)` | subposet on the source `join_irreducibles()` list |
| `SAGE_LIB/categories/finite_lattice_posets.py` | 86 | `ParentMethods.meet_irreducibles` | `(self)` | order-theoretic meet-irreducible elements; source returns elements with exactly one upper cover |
| `SAGE_LIB/categories/finite_lattice_posets.py` | 108 | `ParentMethods.meet_irreducibles_poset` | `(self)` | subposet on the source `meet_irreducibles()` list |
| `SAGE_LIB/categories/finite_lattice_posets.py` | 129 | `ParentMethods.irreducibles_poset` | `(self)` | poset on the union of join- and meet-irreducibles, with a one-element special case |
| `SAGE_LIB/categories/finite_lattice_posets.py` | 172 | `ParentMethods.is_lattice_morphism` | `(self, f, codomain)` | order-lattice morphism check: iterates two-element subsets and requires `f(join(x,y)) = join(f(x),f(y))` and `f(meet(x,y)) = meet(f(x),f(y))` |

Exact category-qualified aliases:
`FiniteLatticePosets.ParentMethods.join_irreducibles_poset`,
`FiniteLatticePosets.ParentMethods.meet_irreducibles_poset`,
`FiniteLatticePosets.ParentMethods.irreducibles_poset`.

---

## Tier 1 — Finitely generated modules over PID (V/W presentation, possibly torsion)

Top-level functions:

| File | Line | Surface | Signature | Notes |
|------|------|---------|-----------|-------|
| `SAGE_LIB/modules/fg_pid/fgp_module.py` | 233 | `FGP_Module` | `(V, W, check=True)` | public cached factory for quotient `V/W` from free modules over a PID; constructs `FGP_Module_class(V, W, check=check)` keyed by cover and relation basis matrices |
| `SAGE_LIB/modules/fg_pid/fgp_module.py` | 269 | `is_FGP_Module` | `(x)` | deprecated predicate for FGP quotient modules; Sage docs direct callers to `isinstance(..., FGP_Module_class)` |
| `SAGE_LIB/modules/fg_pid/fgp_module.py` | 1977 | `random_fgp_module` | `(n, R=ZZ, finite=False)` | test/sample helper: chooses a random-rank submodule `A` of `(Frac(R))^n`, then random submodule `B <= A`, returns `A/B`, and if `finite=True` loops until `Q.is_finite()`; source signature default is `finite=False` although the docstring text says default `True` |
| `SAGE_LIB/modules/fg_pid/fgp_module.py` | 2026 | `random_fgp_morphism_0` | `(*args, **kwds)` | test/sample helper: forwards arguments to `random_fgp_module`, then returns an endomorphism sending each Smith-form generator to a random `ZZ` multiple of itself |
| `SAGE_LIB/modules/fg_pid/fgp_module.py` | 2065 | `_test_morphism_0` / `test_morphism_0` | `(*args, **kwds)` | internal/deprecated test helper: samples `random_fgp_morphism_0`, asserts kernel invariant divisibility, image submodule containment, and lift correctness for the first Smith-form image generator |

### `FGP_Module_class`
**File:** `SAGE_LIB/modules/fg_pid/fgp_module.py:293`  
**Inherits:** `Module`  
**Role:** Quotient `V/W` for `V`, `W` free modules over a PID. Represents the full
finitely-generated-module-over-PID stratum, including torsion.

| Line | Method | Signature | Notes |
|------|--------|-----------|-------|
| 339 | `__init__` | `(self, V, W, check=True)` | quotient-parent initialization from free PID-module cover `V` and relation submodule `W <= V`; with `check=True`, Sage verifies free-module types, submodule containment, and common base ring |
| 380 | `_module_constructor` | `(self, V, W, check=True)` | derived-class hook for constructing another quotient `V/W`; base implementation calls the cached `FGP_Module(V, W, check)` factory |
| 407 | `_coerce_map_from_` | `(self, S)` | coercion protocol: FGP sources use `S.has_canonical_map_to(self)`, while other sources defer to the cover module coercion map into `V` |
| 447 | `_mul_` | `(self, other, switch_sides=False)` | scalar multiplication of the quotient presentation by a base-ring element: constructs `(other*V + W)/W`; `switch_sides` is accepted by Sage's operator protocol but not used mathematically here |
| 473 | `_repr_` | `(self)` | display protocol using base ring and Smith invariants |
| 487 | `__truediv__` | `(self, other)` | quotient by a submodule of `self` |
| 512 | `__eq__` | `(self, other)` | equality protocol comparing exact cover and relation submodules |
| 532 | `__ne__` | `(self, other)` | inequality protocol as boolean complement of equality |
| 572 | `__lt__` | `(self, other)` | proper-submodule comparison protocol |
| 590 | `__gt__` | `(self, other)` | proper-submodule comparison protocol |
| 608 | `__ge__` | `(self, other)` | submodule comparison protocol |
| 626 | `_element_constructor_` | `(self, x, check=True)` | quotient-element constructor from a cover vector or FGP element; FGP inputs are lifted first, then coerced into the cover `V` |
| 661 | `linear_combination_of_smith_form_gens` | `(self, x)` | element from coordinates in Smith-form generators |
| 678 | `__contains__` | `(self, x)` | membership in quotient parent |
| 707 | `submodule` | `(self, x)` | submodule defined by x |
| 767 | `has_canonical_map_to` | `(self, A)` | natural structure-map predicate for presentations |
| 798 | `is_submodule` | `(self, A)` | inclusion check |
| 837 | `V` | `(self)` | cover module |
| 855 | `cover` | `(self)` | alias for V() |
| 875 | `W` | `(self)` | relations module |
| 893 | `relations` | `(self)` | alias for W() |
| 915 | `_relative_matrix` | `(self)` | presentation-coordinate backend for the relation submodule basis |
| 940 | `_smith_form` | `(self)` | Smith normal form matrices |
| 962 | `base_ring` | `(self)` | base PID |
| 977 | `invariants` | `(self, include_ones=False)` | diagonal of Smith form |
| 1016 | `gens` | `(self)` | generators tuple |
| 1040 | `smith_form_gens` | `(self)` | Smith form generators |
| 1071 | `gens_to_smith` | `(self)` | change-of-basis matrix |
| 1120 | `smith_to_gens` | `(self)` | inverse presentation matrix from Smith-form generators to user generators |
| 1185 | `gens_vector` | `(self, x, reduce=False)` | coordinates w.r.t. gens |
| 1247 | `coordinate_vector` | `(self, x, reduce=False)` | optimized coordinates |
| 1347 | `gen` | `(self, i)` | indexed current presentation generator, raising if `i` is outside the generator tuple |
| 1379 | `smith_form_gen` | `(self, i)` | indexed Smith-form generator, separated so derived classes may override `gen` |
| 1406 | `optimized` | `(self)` | isomorphic module in optimized form |
| 1480 | `hom` | `(self, im_gens, codomain=None, check=True)` | Hom element recovered from images of the current presentation generators; empty images give the zero map to `self` or the supplied codomain, free-module codomains are promoted to `V/0`, and nonzero data dispatch to Smith-form or general generator conversion |
| 1608 | `_hom_general` | `(self, im_gens, check=True)` | backend conversion from current-generator image data to Smith-generator image data; builds the free module on current generators, checks relations map into the codomain relations, then delegates to `_hom_from_smith` |
| 1652 | `_hom_from_smith` | `(self, im_smith_gens, check=True)` | Smith-generator backend Hom construction using the optimized quotient presentation and the cover map sending optimized generators to lifted Smith-generator images |
| 1690 | `_Hom_` | `(self, N, category=None)` | homset construction |
| 1733 | `random_element` | `(self, *args, **kwds)` | samples a random element of the cover module `V` using forwarded randomness arguments, then coerces/reduces it into `V/W` |
| 1755 | `cardinality` | `(self)` | carrier cardinality computed from Smith invariants: `+Infinity` if any invariant is `0`, otherwise the product of invariants |
| 1788 | `list` | `(self)` | materializes `list(self)`; inherits the iterator's finite-over-`ZZ` restrictions |
| 1800 | `__iter__` | `(self)` | finite `ZZ` quotient iterator over product ranges for Smith invariants, using the optimized cover basis; raises for non-`ZZ` base rings or any zero invariant |
| 1832 | `construction` | `(self)` | construction functor data: returns `(QuotientModuleFunctor(self._W), self._V)` for the presentation `V/W` |
| 1867 | `is_finite` | `(self)` | finite-carrier predicate `0 not in self.invariants()` |
| 1886 | `annihilator` | `(self)` | annihilator ideal: `(0)` if infinite, `(1)` for the trivial finite module, otherwise the ideal generated by the lcm of invariants |
| 1920 | `ngens` | `(self)` | number of generators |
| 1944 | `__hash__` | `(self)` | runtime hash of the exact cover and relation submodules |
| 1957 | `quotient_map` | `(self)` | natural map V → V/W |

Exact class-qualified backend aliases:
`FGP_Module_class._module_constructor`, `FGP_Module_class._coerce_map_from_`,
`FGP_Module_class._mul_`, `FGP_Module_class._repr_`,
`FGP_Module_class.__truediv__`, `FGP_Module_class.__eq__`,
`FGP_Module_class.__ne__`, `FGP_Module_class.__lt__`,
`FGP_Module_class.__gt__`, `FGP_Module_class.__ge__`,
`FGP_Module_class._element_constructor_`, `FGP_Module_class._relative_matrix`,
`FGP_Module_class.__hash__`, `FGP_Module_class._hom_general`,
`FGP_Module_class._hom_from_smith`.

### `FGP_Element`
**File:** `SAGE_LIB/modules/fg_pid/fgp_element.py:58`  
**Inherits:** `ModuleElement`

| Line | Method | Notes |
|------|--------|-------|
| 58 | `FGP_Element.__init__` | backend quotient-element constructor from parent `M` and lift `x in M.V()`; `check=True` asserts membership in the cover module |
| 85 | `lift` | returns the stored lift in the quotient cover module `V` |
| 125 | `__neg__` | additive inverse represented by negating the stored cover lift |
| 139 | `_add_` | quotient-element addition represented by adding stored cover lifts |
| 173 | `_sub_` | quotient-element subtraction represented by subtracting stored cover lifts |
| 192 | `_rmul_` | left scalar action represented by applying `_rmul_` to the stored cover lift |
| 237 | `_lmul_` | right scalar action represented by applying `_lmul_` to the stored cover lift |
| 282 | `_repr_` | display protocol using the reduced coordinate vector |
| 294 | `__getitem__` | coordinate indexing delegated to `vector()` |
| 312 | `vector` | cached immutable reduced coordinate vector from `parent().coordinate_vector(self, reduce=True)` |
| 337 | `__hash__` | hash of the reduced coordinate vector |
| 354 | `_vector_` | conversion hook for `vector(x)` and `vector(base_ring, x)`; returns a mutable copy or changed-ring vector |
| 392 | `_richcmp_` | quotient-element comparison protocol by reduced coordinate vector |
| 414 | `additive_order` | lcm of coordinate orders modulo nonzero invariant factors, with `+Infinity` for nonzero coordinates in zero-invariant slots |

Source semantics:

- `lift()` returns the stored representative `_x` in the cover module `V`; it is not a
  canonical dual/rational-lattice lift unless the parent quotient has already been
  identified as the relevant discriminant or quotient presentation.
- `__neg__`, `_add_`, `_sub_`, `_rmul_`, and `_lmul_` construct new parent elements by
  applying the corresponding operation to the stored cover lift and then reducing
  through the parent element class.
- `vector()` caches the reduced coordinate vector
  `self.parent().coordinate_vector(self, reduce=True)` and makes that cached vector
  immutable. `_repr_`, `__getitem__`, `__hash__`, `_vector_`, and `_richcmp_` are
  derived from this reduced coordinate vector.
- `additive_order()` zips the reduced coordinate vector with the parent Smith
  invariants. A nonzero coordinate in a zero-invariant slot has infinite additive
  order; otherwise the order is the lcm of the modular additive orders of the
  coordinates modulo their invariant factors.

Exact class-qualified backend aliases:
`FGP_Element._rmul_`, `FGP_Element._lmul_`, `FGP_Element._richcmp_`.

### `FGP_Morphism`
**File:** `SAGE_LIB/modules/fg_pid/fgp_morphism.py:73`  
**Inherits:** `Morphism`

Top-level Homset factory:

| Line | Surface | Signature | Notes |
|------|---------|-----------|-------|
| 462 | `FGP_Homset` | `(X, Y)` | backend Hom parent factory for FGP modules |
| 485 | `FGP_Homset_class` | `(X, Y, category=None)` | backend Hom parent class for FGP modules |

| Line | Surface | Signature or input shape | Return / notes |
|------|---------|--------------------------|----------------|
| 73 | `FGP_Morphism.__init__` | `(parent, phi, check=True)`, where `phi` maps the optimized cover of the domain to the optimized cover of the codomain and sends relations into relations | Backend Hom-element constructor; public route is Hom-parent construction |
| 122 | `FGP_Morphism._repr_` | `(self)` | display surface from domain/codomain invariant factors and generator images |
| 137 | `im_gens` | `(self)` | Tuple `(f(g_i))` in the codomain for the current domain generators |
| 154 | `_richcmp_` | `(self, right, op)` | Backend morphism comparison by domain, codomain, and generator images |
| 188 | `__add__` | `(self, right)` | Hom-element addition after coercion into the same parent |
| 202 | `__sub__` | `(self, right)` | Hom-element subtraction after coercion into the same parent |
| 215 | `__neg__` | `(self)` | Hom-element additive inverse |
| 226 | `__call__` on elements | `(self, x)` for an element coercible into the domain | Codomain element `f(x)` |
| 226 | `__call__` on submodules | `(self, A)` for an `FGP_Module_class` submodule `A <= domain(f)` | Codomain submodule generated by the images of `A.smith_form_gens()` |
| 299 | `kernel` | `(self)` | Domain submodule `ker(f) = f^{-1}(0)` |
| 327 | `inverse_image` | `(self, A)` for an FGP submodule `A <= codomain(f)` | Domain submodule `f^{-1}(A)`; rejects inputs that are not FGP submodules of the codomain |
| 368 | `image` | `(self)` | Codomain submodule `im(f)` |
| 386 | `lift` | `(self, x)` for a codomain element `x` | Domain element `y` with `f(y)=x`, when such a lift exists |
| 499 | `FGP_Homset_class.__init__` | `(X, Y, category=None)` | backend Hom-parent initialization; chooses a modules or modules-with-basis category when omitted |
| 517 | `FGP_Homset_class._coerce_map_from_` | `(self, S)` | Hom-parent coercion protocol for equal FGP Hom parents and scalar endomorphism coercion |
| 537 | `FGP_Homset_class.__call__` | `(self, x)` | Hom-parent element coercion; delegates to `FGP_Morphism(self, x)` |

No Sage `FGP_Morphism.cokernel()` surface is present in the written reference page or
installed source. The project cokernel obligation is therefore not inherited from Sage
FGP morphisms; it is the category-spec quotient `codomain(f) / image(f)` with
projection, refined by formed-module descent hypotheses when form data are present.

Exact class-qualified backend alias: `FGP_Morphism._richcmp_`.

### Generic Homset backends touching module/lattice Hom/End/Aut routing

`SAGE_LIB/modules/free_module_homspace.py`:

| Line | Surface | Signature | Notes |
|------|---------|-----------|-------|
| 85 | `is_FreeModuleHomspace` | `(x)` | deprecated predicate; Sage docs direct callers to `isinstance(..., FreeModuleHomspace)` |
| 132 | `FreeModuleHomspace` | `HomsetWithBase` subclass | backend Hom parent for free modules |
| 133 | `FreeModuleHomspace.__call__` | `(self, A, **kwds)` with `side='left'` or `'right'` | Hom-element construction from matrix data, generator-image data, or a callable evaluated on domain generators |
| 230 | `FreeModuleHomspace.zero` | `(self, side='left')` | cached zero morphism constructor using the constant-zero callable |
| 276 | `FreeModuleHomspace._matrix_space` | `(self, side='left')` | matrix-space backend for Hom elements |
| 303 | `FreeModuleHomspace.basis` | `(self, side='left')` | basis tuple for the free-module Hom parent from the underlying matrix-space basis |
| 342 | `FreeModuleHomspace.identity` | `(self, side='left')` | identity morphism for endomorphism Hom parents only |

Source semantics:

- `FreeModuleHomspace.__call__(A, **kwds)` has three finite input shapes: a matrix;
  a list/tuple of codomain images of the domain generators; or a callable evaluated on
  each domain generator. For generator images or callables, Sage converts each image to
  the codomain and builds the coordinate matrix, transposing exactly when
  `side == 'right'`. Nonzero maps require a coercion map from the domain base ring to
  the codomain base ring; when no such coercion exists, only the zero morphism is
  accepted.
- `_matrix_space(side)` is the backend orientation witness: for `side='left'` it is
  `MatrixSpace(R, rank(domain), rank(codomain))`, while for `side='right'` it is
  `MatrixSpace(R, rank(codomain), rank(domain))`; other side values raise.
- `zero(side)` constructs the zero Hom element through the constant-zero callable.
  `basis(side)` lifts the underlying oriented matrix-space basis through the Hom
  parent. `identity(side)` is defined only on endomorphism Hom parents and otherwise
  raises a typed failure recommending `natural_map()`.

`SAGE_LIB/modules/free_module_morphism.py`:

| Line | Surface | Signature | Notes |
|------|---------|-----------|-------|
| 51 | `is_FreeModuleMorphism` | `(x)` | deprecated predicate; Sage docs direct callers to `isinstance(..., FreeModuleMorphism)` or categories |
| 74 | `FreeModuleMorphism` | `MatrixMorphism` subclass | backend Hom element for free modules represented by an oriented matrix |
| 76 | `FreeModuleMorphism.__init__` | `(self, parent, A, side='left')` | requires a `FreeModuleHomspace`, coerces `A` through the parent oriented matrix space, then initializes `MatrixMorphism` |
| 100 | `pushforward` | `(self, x)` where `x` is a free submodule of the domain | image of a domain submodule; implemented as `self.restrict_domain(V).image()` after coercing to a domain submodule |
| 136 | `_repr_` | `(self)` | display surface including matrix, domain, codomain, and right-side action wording |
| 198 | `change_ring` | `(self, R)` | changes domain, codomain, and matrix to `R`, then constructs the new Hom element with the same `side` |
| 247 | `inverse_image` | `(self, V)` where `V <= codomain(f)` | domain submodule `f^{-1}(V)`; intersects `V` with the image, solves using linear algebra over fields or Hermite-form data otherwise, then adds the kernel |
| 396 | `lift` / `preimage_representative` | `(self, x)` for `x` in the codomain | preimage representative `y` with `f(y)=x` when one exists; uses side-transposed matrix when needed and Hermite-form data over non-fields |
| 489 | `eigenvalues` | `(self, extend=True)` | vector-space endomorphism spectral values; delegates to the matrix over a field and rejects non-endomorphisms |
| 524 | `eigenvectors` | `(self, extend=True)` | vector-space endomorphism eigenvalue, eigenvector-basis sequence, and algebraic multiplicity data; left/right side selects left/right matrix eigenvectors |
| 582 | `eigenspaces` | `(self, extend=True)` | vector-space endomorphism eigenspace submodules built from `eigenvectors` |
| 647 | `BaseIsomorphism1D` | `Morphism` subclass | ring/free-rank-one-module isomorphism base class |
| 672 | `BaseIsomorphism1D.is_injective` | `(self)` | always `True` for these rank-one base isomorphisms |
| 683 | `BaseIsomorphism1D.is_surjective` | `(self)` | always `True` for these rank-one base isomorphisms |
| 709 | `BaseIsomorphism1D_to_FM` | `(parent, basis=None)` | isomorphism from a ring to its rank-one free module, optionally multiplying by an invertible basis element |
| 766 | `BaseIsomorphism1D_from_FM` | `(parent, basis=None)` | inverse isomorphism from the rank-one free module to the ring, optionally dividing by the invertible basis element |

`SAGE_LIB/modules/matrix_morphism.py` inherited by `FreeModuleMorphism`:

| Line | Surface | Signature | Notes |
|------|---------|-----------|-------|
| 59 | `is_MatrixMorphism` | `(x)` | deprecated predicate; Sage docs direct callers to `isinstance(..., MatrixMorphism_abstract)` or categories |
| 84 | `MatrixMorphism_abstract` | `Morphism` subclass | abstract base for matrix-backed Hom elements; copies characteristic polynomial, determinant, factorization of characteristic polynomial, and trace from finite-dimensional-module-with-basis Hom endomorphism methods |
| 96 | `MatrixMorphism_abstract.__init__` | `(self, parent, side='left')` | backend Hom-element initialization; requires a Hom parent and stores side as either `left` or `right` |
| 121 | `MatrixMorphism_abstract._richcmp_` | `(self, other, op)` | comparison protocol; compares matrices only for matrix morphisms under equality/inequality, otherwise delegates to generic morphism comparison |
| 149 | `_call_` | `(self, x)` | evaluates the Hom element on a domain element using coordinate vectors and the oriented matrix |
| 229 | `_call_with_args` | `(self, x, args=(), kwds={})` | call protocol variant that forwards optional arguments to the codomain element constructor after matrix evaluation |
| 261 | `__invert__` / `inverse` | `(self)` | inverse Hom element when the represented map is invertible; returns an element of the reversed Hom parent |
| 292 | `side` | `(self)` | matrix orientation datum, `left` or `right` |
| 312 | `side_switch` | `(self)` | same Hom element represented on the opposite side by transposing the matrix |
| 466 | `__rmul__` | `(self, left)` | left scalar multiplication of the matrix representative by an element coerced to the base ring |
| 483 | `__mul__` | `(self, right)` | Hom composition when `right` is a matrix morphism; scalar right multiplication otherwise |
| 653 | `__add__`, `__neg__`, `__sub__` | Hom-element additive operations | additive structure on the Hom parent, with mixed sides normalized to the default left-side representation |
| 806 | `base_ring` | `(self)` | base ring of the domain matrix presentation |
| 818 | `decomposition` | `(self, *args, **kwds)` | invariant-subspace decomposition for endomorphisms through matrix decomposition; variadic inputs are passed to the matrix backend |
| 863 | `kernel` | `(self)` | domain submodule `ker(f)`, from left or right matrix kernel according to `side` |
| 913 | `image` | `(self)` | codomain submodule `im(f)`, from row or column space according to `side` |
| 1596 | `matrix` | `(self, side=None)` | immutable matrix representative; `side='left'` and `side='right'` differ by transpose |
| 1025 | `rank` | `(self)` | rank of the matrix representative |
| 1040 | `nullity` | `(self)` | side-sensitive matrix nullity |
| 1649 | `is_injective` | `(self)` | matrix-kernel criterion for injectivity |
| 1674 | `is_surjective` | `(self)` | image-submodule equality criterion for surjectivity |
| 1071 | `is_bijective` | `(self)` | conjunction of injective and surjective |
| 1115 | `is_identity` | `(self)` | equal-domain/codomain basis-action test for the identity function |
| 1189 | `is_zero` | `(self)` | zero matrix criterion for the zero morphism |
| 1231 | `is_equal_function` | `(self, other)` | equality as functions on equal domain/codomain, tested on a basis rather than by raw matrix equality |
| 1322 | `restrict_domain` | `(self, sub)` | restricts the domain to a submodule and rebuilds the Hom element |
| 1371 | `restrict_codomain` | `(self, sub)` | restricts the codomain to a submodule and rebuilds the Hom element |
| 1454 | `restrict` | `(self, sub)` | endomorphism restriction to an invariant submodule, returning an End element of that submodule |
| 1560 | `MatrixMorphism.__init__` | `(self, parent, A, copy_matrix=True, side='left')` | concrete matrix-backed Hom-element constructor; accepts a matrix or matrix morphism, validates orientation-dependent matrix shape against domain/codomain ranks, makes the representative immutable, and stores it |
| 1726 | `MatrixMorphism._repr_` | `(self)` | display surface for a matrix-backed Hom element, including right-side action wording when relevant |

Source semantics:

- The table above is the Sage-discovered method set for this source block. After the
  Sage method set is known, each method is classified by the weakest mathematical
  structure where it is defined, not by the Sage class that happens to implement it.
- Any category with morphisms owns domain, codomain, evaluation/application of a
  morphism, and composition. Sage's `MatrixMorphism._call_` and multiplication methods
  are only the matrix-backed implementation of those category-level operations for free
  modules.
- An additive category owns zero morphisms and addition/negation/subtraction of
  morphisms. Scalar multiplication requires the corresponding linear or enriched Hom
  structure. Sage's free-module matrix methods `__rmul__`, `__mul__` on scalars, and
  matrix addition/subtraction are implementation evidence for that structure, not the
  mathematical owner.
- An abelian category owns kernel, cokernel, image, coimage, monomorphism and
  epimorphism tests, and the usual exactness-shaped preimage/image constructions where
  the category supplies them. Sage realizes these for free modules with row/column
  spaces, matrix kernels, submodule images, and Hermite/linear-solve backends.
- Endomorphism and automorphism refinements own identity and invertibility/isomorphism
  predicates, and inverse maps when the morphism is an isomorphism. These are not
  free-module-local notions.
- The finite free module presentation owns only presentation data and algorithms:
  `MatrixMorphism.__init__`, `matrix(side)`, `side`, `side_switch`, rank/nullity of
  the representative matrix, basis or submodule restriction algorithms, submodule
  pushforward, preimage representatives, and `change_ring(R)` on the displayed
  module/matrix presentation.
  `side` is representation data, not a mathematical option bag: Sage stores one matrix
  orientation and recovers the opposite orientation by transposition.
- `is_MatrixMorphism`, rich comparison, `_repr_`, and `_call_with_args` are
  compatibility, display, comparison, and call-protocol interop surfaces. The forwarded
  optional arguments in `_call_with_args` are codomain element-constructor data after
  the morphism has already been evaluated; they are not public Hom options.
- `lift`/`preimage_representative` returns one representative of a preimage coset when
  one exists, not a canonical inverse map.
- `change_ring(R)` is not a lattice scalar-extension theorem unless the formed or
  lattice structure supplies the corresponding base-change semantics.
- `eigenvalues`, `eigenvectors`, `eigenspaces`, matrix `decomposition`, determinant,
  trace, characteristic polynomial, and related delegated matrix invariants are
  vector-space endomorphism or finite-dimensional-with-basis backend surfaces.
  Public project exposure must name the field, endomorphism hypothesis, side convention,
  extension-field convention, eigenspace subobject, and witness data.
- `BaseIsomorphism1D_to_FM` and `BaseIsomorphism1D_from_FM` are ring-to-rank-one-free
  module isomorphism witnesses produced by Sage's ring `free_module` route. The
  optional basis element is required by Sage examples to be a unit so that the maps are
  true isomorphisms; these are not lattice constructors.

`SAGE_LIB/categories/homset.py`:

| Line | Surface | Signature | Notes |
|------|---------|-----------|-------|
| 87 | `Hom` | `(X, Y, category=None, check=True)` | cached Hom-parent constructor for morphisms from `X` to `Y` in a category |
| 498 | `End` | `(X, category=None)` | cached End-parent constructor `Hom(X, X, category)` |
| 562 | `end` | `(X, f)` | convenience constructor returning `End(X)(f)` for endomorphism data `f` |
| 580 | `Homset` | `(X, Y, category=None, check=True)` | generic Hom parent class storing domain, codomain, category, and dynamic element-class machinery |
| 683 | `Homset.__reduce__` | `(self)` | pickle construction protocol |
| 775 | `Homset.homset_category` | `(self)` | category in which the Hom parent lives |
| 975 | `Homset._abstract_element_class` | `(self)` | dynamic category/morphism element-class synthesis |
| 1057 | `Homset.element_class_set_morphism` | `(self)` | callable/set-morphism element class |
| 1136 | `Homset.natural_map` | `(self)` | coercion morphism backend |
| 1164 | `Homset.identity` | `(self)` | identity morphism for endomorphism sets |
| 1199 | `Homset.one` | `(self)` | alias for identity on endomorphism sets |
| 1214 | `Homset.domain` | `(self)` | Hom parent domain |
| 1235 | `Homset.reversed` | `(self)` | Hom parent with domain/codomain reversed |
| 1267 | `HomsetWithBase` | `(X, Y, category=None, base=None, check=True)` | generic Hom parent subclass carrying base-ring data |
| 1291 | `is_Homset` | `(x)` | deprecated predicate for Hom parents |
| 1316 | `is_Endset` | `(x)` | deprecated predicate for End parents, implemented as a Homset predicate plus `domain is codomain` |

`SAGE_LIB/categories/homsets.py`:

| Line | Surface | Signature | Notes |
|------|---------|-----------|-------|
| 19 | `HomsetsCategory` | `FunctorialConstructionCategory` subclass | generic category machinery for `C.Homsets()` functorial constructions |
| 24 | `HomsetsCategory.default_super_categories` | `(cls, category)` | computes default supercategories for a category's Homsets category from full supercategories, nested Homsets classes, or stub HomsetsOf construction |
| 123 | `HomsetsCategory._test_homsets_category` | `(self, **options)` | generic category test hook |
| 158 | `HomsetsCategory._make_named_class_key` | `(self, name)` | dynamic named-class key delegation to the base category |
| 175 | `HomsetsOf` | `HomsetsCategory` subclass | stub homsets category for a category without its own Homsets class |
| 201 | `HomsetsOf._repr_object_names` | `(self)` | display naming for stub homsets categories |
| 239 | `Homsets` | `Category_singleton` subclass | category of all homsets, a subcategory of sets |
| 285 | `Homsets.SubcategoryMethods.Endset` | `(self)` | endomorphism-set axiom refinement on Homsets |
| 345 | `Homsets.ParentMethods.is_endomorphism_set` | `(self)` | runtime predicate checking whether a Hom parent has identical domain and codomain |

---

## Tier 2 — Torsion bilinear/quadratic modules (discriminant group level)

Top-level constructor:

| Line | Surface | Signature | Notes |
|------|---------|-----------|-------|
| 35 | `TorsionQuadraticForm` | `(q)` | torsion quadratic module from rational Gram matrix with values in `QQ/ZZ` or `QQ/2ZZ` |

### `TorsionQuadraticModule`
**File:** `SAGE_LIB/modules/torsion_quadratic_module.py`  
**Inherits:** `FGP_Module_class`, `CachedRepresentation`  
**Role:** `V/W` with a `Q/Z`-valued quadratic form (or `Q/2Z` for even); the canonical
model for discriminant groups of lattices.

| Line | Method | Signature | Notes |
|------|--------|-----------|-------|
| 230 | `__classcall__` | `(cls, V, W, gens=None, modulus=None, modulus_qf=None, check=True)` | cached-representation normalization and validation |
| 279 | `__init__` | `(self, V, W, gens, modulus, modulus_qf)` | backend parent initialization from cover, relations, optional user generators, and value moduli |
| 300 | `_repr_` | `(self)` | display surface for base ring, inherited invariant factors, and quadratic Gram matrix |
| 321 | `_module_constructor` | `(self, V, W, check=False)` | backend quotient-constructor hook for `V/W`, inheriting or recomputing value moduli |
| 363 | `all_submodules` | `(self)` | all submodules |
| 408 | `brown_invariant` | `(self)` | Brown invariant of a torsion quadratic module with quadratic values in `QQ/2ZZ` |
| 457 | `gram_matrix_bilinear` | `(self)` | Gram matrix of bilinear form (entries in Q/mZ) |
| 487 | `gram_matrix_quadratic` | `(self)` | Gram matrix of quadratic form (diagonal = q values) |
| 520 | `gens` | `(self)` | generators tuple |
| 539 | `genus` | `(self, signature_pair)` | genus from discriminant form + signature |
| 743 | `is_genus` | `(self, signature_pair, even=True)` | test realizability |
| 816 | `orthogonal_group` | `(self, gens=None, check=False)` | Aut of torsion QF |
| 890 | `orthogonal_submodule_to` | `(self, S)` | orthogonal complement of submodule |
| 939 | `normal_form` | `(self, partial=False)` | canonical normal form |
| 1113 | `primary_part` | `(self, m)` | m-primary part |
| 1149 | `submodule_with_gens` | `(self, gens)` | submodule on given generators |
| 1207 | `twist` | `(self, s)` | scale form by s |
| 1251 | `value_module` | `(self)` | `Q/mZ` (bilinear form values) |
| 1271 | `value_module_qf` | `(self)` | `Q/nZ` (quadratic form values) |

### `TorsionQuadraticModuleElement`
**File:** `SAGE_LIB/modules/torsion_quadratic_module.py`  
**Inherits:** `FGP_Element`

| Line | Method | Alias | Notes |
|------|--------|-------|-------|
| 90 | `TorsionQuadraticModuleElement` | class | element type for torsion quadratic modules |
| 121 | `_mul_` / `inner_product` / `b` | lines 151–152 | bilinear form evaluation |
| 154 | `quadratic_product` / `q` | line 185 | quadratic form evaluation |

Exact class-qualified constructor alias: `TorsionQuadraticModule.__classcall__`.
Exact Brown-invariant backend helper: `_brown_indecomposable(q, p)` at line 1292.

---

## Tier 3 — Integral lattices over ZZ (free, symmetric, nondegenerate, integral)

### `FreeQuadraticModule_integer_symmetric`
**File:** `SAGE_LIB/modules/free_quadratic_module_integer_symmetric.py:625`  
**Inherits:** `FreeQuadraticModule_submodule_with_basis_pid`  
**Role:** The canonical "integral lattice" in Sage: `ZZ`-free, finite rank, symmetric
nondegenerate bilinear form with integer values.

| Line | Method | Signature | Notes |
|------|--------|-----------|-------|
| 646 | `__init__` | `(self, ambient, basis, inner_product_matrix, check=True, already_echelonized=False)` | backend class constructor; validates nondegeneracy and integrality after the Sage submodule-with-basis initialization |
| 671 | `_mul_` | `(self, other, switch_sides=False)` | Sage operator surface multiplying the basis matrix by a scalar or matrix; returns `sublattice(...)` for integral data and `span(...)` otherwise |
| 704 | `_repr_` | `(self)` | display surface for degree, rank, basis matrix, and inner-product matrix |
| 736 | `is_even` | `(self)` | diagonal Gram entries all even |
| 753 | `dual_lattice` | `(self)` | `L^∨ = {x ∈ L⊗Q : (x,l) ∈ Z ∀l}` |
| 779 | `discriminant_group` | `(self, s=0)` | `L^∨/L` (s-primary part if s≠0) |
| 839 | `signature` | `(self)` | `n_+ - n_-` |
| 855 | `signature_pair` | `(self)` | `(n_+, n_-)` |
| 871 | `direct_sum` | `(self, M)` | orthogonal direct sum |
| 901 | `is_primitive` | `(self, M)` | M is primitive submodule (quotient torsion-free) |
| 931 | `orthogonal_complement` | `(self, M)` | `M^⊥` inside self |
| 972 | `sublattice` | `(self, basis)` | sublattice spanned by basis |
| 1008 | `overlattice` | `(self, gens)` | lattice spanned by self and extra gens |
| 1030 | `maximal_overlattice` | `(self, p=None)` | max even integral overlattice |
| 1155 | `orthogonal_group` | `(self, gens=None, is_finite=None)` | `O(L)` as matrix group |
| 1313 | `automorphisms` | (alias) | alias for orthogonal_group |
| 1315 | `genus` | `(self)` | genus of the lattice |
| 1332 | `tensor_product` | `(self, other, discard_basis=False)` | tensor product with form |
| 1393 | `quadratic_form` | `(self)` | associated `QuadraticForm` via `q(x)=(x,x)` |
| 1409 | `minimum` | `(self)` | min `{β(x,x) : x ∈ L\{0}}` |
| 1435 | `maximum` | `(self)` | max `{β(x,x) : x ∈ L\{0}}` |
| 1460 | `min`, `max` | (aliases) | compatibility aliases for `minimum` and `maximum` |
| 1463 | `LLL` | `(self)` | LLL-reduced basis |
| 1498 | `lll` | (alias) | |
| 1500 | `short_vectors` | `(self, n, **kwargs)` | vectors of length < n |
| 1541 | `_fplll_enumerate` | `(self, target=None)` | private backend helper: LLL-reduces self, optionally translates a target into coordinates, and invokes `fplll` enumeration for short/close vector iterators |
| 1596 | `enumerate_short_vectors` | `(self)` | iterator, shortest first |
| 1631 | `enumerate_close_vectors` | `(self, target)` | iterator near target |
| 1653 | `twist` | `(self, s, discard_basis=False)` | scale inner product by s |

Exact class-qualified backend alias:
`FreeQuadraticModule_integer_symmetric._fplll_enumerate`.

### Matrix-group isometry backend

**File:** `SAGE_LIB/groups/matrix_gps/isometries.py`
**Role:** GAP-backed matrix group used by Sage lattice orthogonal-group surfaces; records
the invariant bilinear form and optional invariant submodule or quotient actions.

| Line | Surface | Signature | Notes |
|------|---------|-----------|-------|
| 45 | `GroupOfIsometries` | `(degree, base_ring, gens, invariant_bilinear_form, category=None, check=True, invariant_submodule=None, invariant_quotient_module=None)` | matrix group generated by isometries of a bilinear form |
| 91 | `GroupOfIsometries.__init__` | same as class signature | stores immutable invariant form; when `check=True`, checks each generator preserves the form, preserves the optional invariant submodule, and preserves both `V` and `W` of the optional quotient module |
| 134 | `GroupOfIsometries._repr_` | `(self)` | display surface |
| 161 | `GroupOfIsometries.__reduce__` | `(self)` | pickle compatibility surface |
| 183 | `GroupOfIsometries.invariant_bilinear_form` | `(self)` | returns preserved bilinear-form matrix |
| 201 | `GroupOfIsometries._get_action_` | `(self, S, op, self_on_left)` | registers right actions on the invariant submodule, invariant quotient module, or invariant subquotient `S <= T` whose cover `V` is preserved by all generators |
| 239 | `GroupOfIsometries._check_matrix` | `(self, x, *args)` | checks `x F x^T = F` for the invariant form |
| 264 | `GroupActionOnSubmodule` | `(MatrixGroup, submodule, is_left=False)` | right action on an invariant submodule |
| 291 | `GroupActionOnSubmodule.__init__` | `(self, MatrixGroup, submodule, is_left=False)` | backend action constructor for an invariant submodule |
| 313 | `GroupActionOnSubmodule._act_` | `(self, g, a)` | applies matrix-group element and coerces back to the submodule |
| 353 | `GroupActionOnQuotientModule` | `(MatrixGroup, quotient_module, is_left=False)` | right action on an invariant quotient module |
| 378 | `GroupActionOnQuotientModule.__init__` | `(self, MatrixGroup, quotient_module, is_left=False)` | backend action constructor for an invariant quotient module |
| 397 | `GroupActionOnQuotientModule._act_` | `(self, g, a)` | applies matrix-group element to a quotient-element lift, respecting left/right action orientation, and coerces back |

---

## Tier 4 — Quadratic forms (separate Sage type; closely related)

### `QuadraticForm`
**File:** `SAGE_LIB/quadratic_forms/quadratic_form.py:185`  
**Inherits:** `SageObject`  
**Role:** Symmetric bilinear form encoded via upper-triangular coefficient matrix.
Distinct from `FreeQuadraticModule_integer_symmetric` but closely related for ZZ.

Top-level functions:

| Line | Surface | Notes |
|------|---------|-------|
| 49 | `is_QuadraticForm` | deprecated type predicate |
| 72 | `quadratic_form_from_invariants` | rational quadratic form from rank, determinant, Hasse-prime set, and signature count |
| 1750 | `DiagonalQuadraticForm` | diagonal quadratic-form factory from diagonal coefficients |

Package-level exports (`quadratic_forms/all.py`):

| File | Line | Surface | Notes |
|------|------|---------|-------|
| `SAGE_LIB/quadratic_forms/all.py` | 1 | `BinaryQF`, `BinaryQF_reduced_representatives` | integer binary quadratic-form class and discriminant-bounded representatives |
| `SAGE_LIB/quadratic_forms/all.py` | 3 | `BQFClassGroup` | form class group parent for binary quadratic forms by discriminant |
| `SAGE_LIB/quadratic_forms/all.py` | 5 | `TernaryQF`, `find_all_ternary_qf_by_level_disc`, `find_a_ternary_qf_by_level_disc` | integer ternary quadratic-form class and search helpers |
| `SAGE_LIB/quadratic_forms/all.py` | 9 | `random_quadraticform`, `random_quadraticform_with_conditions`, `random_ternaryqf`, `random_ternaryqf_with_conditions` | random/sample constructors for generic and ternary quadratic forms |
| `SAGE_LIB/quadratic_forms/all.py` | 14 | `least_quadratic_nonresidue`, `extend_to_primitive`, `is_triangular_number` | arithmetic and primitive-extension helpers |
| `SAGE_LIB/quadratic_forms/all.py` | 16 | `gamma__exact`, `zeta__exact`, `QuadraticBernoulliNumber`, `quadratic_L_function__exact`, `quadratic_L_function__numerical` | special-value helpers for gamma, zeta, and quadratic Dirichlet L-functions |
| `SAGE_LIB/quadratic_forms/all.py` | 21 | `Genus` | genus constructor/export already mapped through `genera/genus.py` |
| `SAGE_LIB/quadratic_forms/all.py` | 23 | `BezoutianQuadraticForm`, `HyperbolicPlane_quadratic_form` | top-level quadratic-form construction helpers |

Construction and helper modules exported by `quadratic_forms/all.py`:

| File | Line | Surface | Signature | Notes |
|------|------|---------|-----------|-------|
| `SAGE_LIB/quadratic_forms/constructions.py` | 14 | `BezoutianQuadraticForm` | `(f, g)` | constructs a quadratic form over the common polynomial coefficient ring from the Bezoutian of `f` and `g` |
| `SAGE_LIB/quadratic_forms/constructions.py` | 69 | `HyperbolicPlane_quadratic_form` | `(R, r=1)` | constructs the orthogonal sum of `r` copies of the hyperbolic plane form `xy` over `R` |
| `SAGE_LIB/quadratic_forms/random_quadraticform.py` | 16 | `random_quadraticform` | `(R, n, rand_arg_list=None)` | random upper-triangular coefficient quadratic form over a ring `R` |
| `SAGE_LIB/quadratic_forms/random_quadraticform.py` | 76 | `random_quadraticform_with_conditions` | `(R, n, condition_list=[], rand_arg_list=None)` | repeats random generation until boolean conditions on the form hold |
| `SAGE_LIB/quadratic_forms/random_quadraticform.py` | 127 | `random_ternaryqf` | `(rand_arg_list=None)` | random integer `TernaryQF` from six random coefficients |
| `SAGE_LIB/quadratic_forms/random_quadraticform.py` | 166 | `random_ternaryqf_with_conditions` | `(condition_list=[], rand_arg_list=None)` | repeats random ternary generation until boolean conditions hold |
| `SAGE_LIB/quadratic_forms/extras.py` | 11 | `is_triangular_number` | `(n, return_value=False)` | integer triangular-number helper, optionally returning the triangular index |
| `SAGE_LIB/quadratic_forms/extras.py` | 77 | `extend_to_primitive` | `(A_input)` | extends a matrix/list of vectors to a square matrix/list with determinant equal to the gcd of minors |
| `SAGE_LIB/quadratic_forms/extras.py` | 144 | `least_quadratic_nonresidue` | `(p)` | least positive quadratic nonresidue modulo a prime `p > 2` |
| `SAGE_LIB/quadratic_forms/special_values.py` | 25 | `gamma__exact` | `(n)` | exact gamma values at integer or half-integer arguments |
| `SAGE_LIB/quadratic_forms/special_values.py` | 97 | `zeta__exact` | `(n)` | exact Riemann zeta values at critical arguments |
| `SAGE_LIB/quadratic_forms/special_values.py` | 166 | `QuadraticBernoulliNumber` | `(k, d)` | Bernoulli number for the primitive quadratic character attached to `d` |
| `SAGE_LIB/quadratic_forms/special_values.py` | 207 | `quadratic_L_function__exact` | `(n, d)` | exact special value of a quadratic Dirichlet L-function at a critical argument |
| `SAGE_LIB/quadratic_forms/special_values.py` | 269 | `quadratic_L_function__numerical` | `(n, d, num_terms=1000)` | naive numerical quadratic Dirichlet L-function evaluation in the convergence domain |
| `SAGE_LIB/quadratic_forms/binary_qf.py` | 70 | `BinaryQF` | `(a, b=None, c=None)` | specialized integer binary quadratic form from three coefficients, a 3-tuple/list, zero, a homogeneous bivariate integer polynomial, or a PARI binary-form object |
| `SAGE_LIB/quadratic_forms/binary_qf.py` | 182 | `BinaryQF.principal` | `(D)` | principal binary quadratic form of discriminant `D` |
| `SAGE_LIB/quadratic_forms/bqf_class_group.py` | 99 | `BQFClassGroup` | `(D, *, check=True)` | class group parent for positive-definite binary quadratic forms of negative discriminant; positive discriminants are not implemented |
| `SAGE_LIB/quadratic_forms/bqf_class_group.py` | 147 | `BQFClassGroup._element_constructor_` | `(F, *, check=True)` | element constructor from `0`, a `BinaryQF`, or an existing class-group element |
| `SAGE_LIB/quadratic_forms/ternary_qf.py` | 49 | `TernaryQF` | `(v)` | specialized integer ternary quadratic form from a six-coefficient tuple/list |

Specialized binary quadratic-form surfaces:

| File | Line | Surface | Signature | Notes |
|------|------|---------|-----------|-------|
| `SAGE_LIB/quadratic_forms/binary_qf.py` | 100 | `BinaryQF.__init__` | `(self, a, b=None, c=None)` | creates `ax^2 + bxy + cy^2` from coefficients, tuple/list, zero, polynomial, or PARI object |
| `SAGE_LIB/quadratic_forms/binary_qf.py` | 158 | `BinaryQF._pari_init_` | `(self)` | PARI conversion hook |
| `SAGE_LIB/quadratic_forms/binary_qf.py` | 182 | `BinaryQF.principal` | `(D)` | principal binary quadratic form of discriminant `D` |
| `SAGE_LIB/quadratic_forms/binary_qf.py` | 224 | `BinaryQF.__mul__` | `(self, right)` | Gauss composition or right action by a `2 x 2` integer matrix |
| `SAGE_LIB/quadratic_forms/binary_qf.py` | 271 | `BinaryQF.__getitem__` | `(self, n)` | coefficient-index access |
| `SAGE_LIB/quadratic_forms/binary_qf.py` | 296 | `BinaryQF.__call__` | `(self, *args)` | binary-form evaluation at a point |
| `SAGE_LIB/quadratic_forms/binary_qf.py` | 326, 339, 370, 388, 477, 494 | `__hash__`, `__eq__`, `__ne__`, `__lt__`, `_repr_`, `_latex_` | protocol methods | identity, ordering, display, and LaTeX surfaces |
| `SAGE_LIB/quadratic_forms/binary_qf.py` | 409, 435, 463 | `__add__`, `__sub__`, `__neg__` | `(self, Q)`, `(self, Q)`, `(self)` | coefficientwise arithmetic and sign change |
| `SAGE_LIB/quadratic_forms/binary_qf.py` | 508, 523, 549 | `content`, `polynomial`, `from_polynomial` | `(self)`, `(self)`, `(poly)` | coefficient content and homogeneous bivariate polynomial conversion |
| `SAGE_LIB/quadratic_forms/binary_qf.py` | 591, 605, 634, 637 | `discriminant`, `determinant`, `det`, `has_fundamental_discriminant` | `(self)` | discriminant, matrix determinant, determinant alias, and fundamental-discriminant predicate |
| `SAGE_LIB/quadratic_forms/binary_qf.py` | 659, 705, 721, 745, 1217, 1233, 1235, 1250, 1252, 1264, 1266, 1281, 1426 | `is_primitive`, `is_zero`, `is_weakly_reduced`, `is_reducible`, `is_positive_definite`, `is_posdef`, `is_negative_definite`, `is_negdef`, `is_indefinite`, `is_indef`, `is_singular`, `is_nonsingular`, `is_reduced` | `(self)` | coefficient, discriminant, definiteness, alias, singularity, and reduction predicates |
| `SAGE_LIB/quadratic_forms/binary_qf.py` | 767, 835, 981, 1004, 1027, 1043 | `_reduce_indef`, `reduced_form`, `_RhoTau`, `_Rho`, `_Tau`, `cycle` | reduction signatures | indefinite reduction, reduced representative, Rho/Tau operators, and reduced-form cycle |
| `SAGE_LIB/quadratic_forms/binary_qf.py` | 1296, 1503, 1526, 1549 | `is_equivalent`, `complex_point`, `matrix_action_left`, `matrix_action_right` | `(self, other, proper=True)`, `(self)`, `(self, M)`, `(self, M)` | equivalence, upper-half-plane point, and matrix actions |
| `SAGE_LIB/quadratic_forms/binary_qf.py` | 1572, 1608, 1808, 1826 | `small_prime_value`, `solve_integer`, `form_class`, `BinaryQF_reduced_representatives` | `(self, Bmax=1000)`, `(self, n, *, algorithm='general', _flag=2)`, `(self)`, `(D, primitive_only=False, proper=True)` | represented-prime search, integer-solution search, class-group element conversion, and reduced representative enumeration |

Exact class-qualified aliases:
`BinaryQF.from_polynomial`, `BinaryQF.polynomial`, `BinaryQF.content`,
`BinaryQF.discriminant`, `BinaryQF.determinant`, `BinaryQF.det`,
`BinaryQF.is_primitive`, `BinaryQF.is_positive_definite`,
`BinaryQF.is_posdef`, `BinaryQF.is_negative_definite`,
`BinaryQF.is_negdef`, `BinaryQF.is_indefinite`, `BinaryQF.is_indef`,
`BinaryQF.is_weakly_reduced`, `BinaryQF.is_reducible`,
`BinaryQF.reduced_form`, `BinaryQF.cycle`, `BinaryQF.is_equivalent`,
`BinaryQF.is_reduced`, `BinaryQF.complex_point`,
`BinaryQF.matrix_action_left`, `BinaryQF.matrix_action_right`,
`BinaryQF.small_prime_value`, `BinaryQF.solve_integer`,
`BinaryQF.form_class`.

Binary quadratic-form class-group surfaces:

| File | Line | Surface | Signature | Notes |
|------|------|---------|-----------|-------|
| `SAGE_LIB/quadratic_forms/bqf_class_group.py` | 99, 125 | `BQFClassGroup`, `BQFClassGroup.__init__` | `(D, *, check=True)` | unique parent for supported `D < 0` with `D mod 4 in {0,1}`; zero and positive discriminants rejected |
| `SAGE_LIB/quadratic_forms/bqf_class_group.py` | 147, 170, 187 | `_element_constructor_`, `zero`, `random_element` | `(F, *, check=True)`, `(self)`, `(self)` | class construction from `0`, `BinaryQF`, or same-parent element; principal class and random prime-based sample element |
| `SAGE_LIB/quadratic_forms/bqf_class_group.py` | 223, 234, 245, 257, 287, 290, 319, 339 | `__hash__`, `_repr_`, `discriminant`, `order`, `cardinality`, `abelian_group`, `gens`, `_coerce_map_from_` | parent methods | display/runtime, class number alias, abelian-group wrapper from PARI `quadclassunit`, generators, and discriminant-quotient projection maps |
| `SAGE_LIB/quadratic_forms/bqf_class_group.py` | 368, 393, 419 | `BQFClassGroup_element`, `BQFClassGroup_element.__init__`, `form` | `(F, parent, *, check=True, reduce=True)`, `(self)` | primitive positive-definite class element with matching discriminant and reduced-form representative |
| `SAGE_LIB/quadratic_forms/bqf_class_group.py` | 436, 456, 472, 489, 518, 629 | `_neg_`, `_add_`, `_sub_`, `__mul__`, `__rmul__`, `order` | element arithmetic | inverse by `[a,-b,c]`, Gauss composition, subtraction, integer multiple, reflected integer multiple, and element order in the class group |
| `SAGE_LIB/quadratic_forms/bqf_class_group.py` | 520, 540, 556, 574, 589, 604, 616 | `__eq__`, `__ne__`, `__lt__`, `__bool__`, `is_zero`, `_repr_`, `__hash__` | element protocol methods | equality, ordering, principal-class predicate, display, and runtime hashing |
| `SAGE_LIB/quadratic_forms/bqf_class_group.py` | 650, 703, 725 | `BQFClassGroupQuotientMorphism`, `__init__`, `_call_` | `(G, H)`, `(elt)` | morphism between form class groups induced by discriminant quotient data |

Specialized ternary quadratic-form surfaces:

| File | Line | Surface | Signature | Notes |
|------|------|---------|-----------|-------|
| `SAGE_LIB/quadratic_forms/ternary_qf.py` | 78, 101, 129, 150, 246, 265 | `TernaryQF.__init__`, `coefficients`, `coefficient`, `polynomial`, `quadratic_form`, `matrix` | presentation methods | six `ZZ` coefficients `(a,b,c,r,s,t)` for `a*x^2+b*y^2+c*z^2+r*yz+s*xz+t*xy`, coefficient access, polynomial conversion, generic `QuadraticForm` conversion, and Hessian matrix `[[2a,t,s],[t,2b,r],[s,r,2c]]` |
| `SAGE_LIB/quadratic_forms/ternary_qf.py` | 116, 168, 566 | `__hash__`, `_repr_`, `__eq__` | protocol methods | runtime hashing, display, and equality |
| `SAGE_LIB/quadratic_forms/ternary_qf.py` | 189, 397, 464 | `__call__`, `__neg__`, `scale_by_factor` | `(self, v)`, `(self)`, `(self, k)` | vector evaluation; matrix substitution returning `TernaryQF` for `3 x 3` matrices or generic `QuadraticForm` for other `3 x n` matrices; sign change; and value scaling that may leave the ternary integer surface |
| `SAGE_LIB/quadratic_forms/ternary_qf.py` | 297, 314, 340, 371, 417, 439, 609, 661 | `disc`, `is_definite`, `is_positive_definite`, `is_negative_definite`, `is_primitive`, `primitive`, `content`, `level` | invariant and predicate methods | discriminant, definiteness, coefficient content, primitive form, and level |
| `SAGE_LIB/quadratic_forms/ternary_qf.py` | 505, 528, 547, 583, 626, 641, 937, 974 | `reciprocal`, `reciprocal_reduced`, `divisor`, `adjoint`, `omega`, `delta`, `xi`, `xi_rec` | arithmetic-form methods | adjoint/reciprocal constructions and Tornaria genus-character invariants |
| `SAGE_LIB/quadratic_forms/ternary_qf.py` | 675, 747 | `is_eisenstein_reduced`, `reduced_form_eisenstein` | `(self)`, `(self, matrix=True)` | eight-condition Eisenstein reduction predicate and unique reduced representative for positive ternary forms, optionally with unimodular transformation matrix witness |
| `SAGE_LIB/quadratic_forms/ternary_qf.py` | 783, 820, 847, 898, 925 | `pseudorandom_primitive_zero_mod_p`, `find_zeros_mod_p`, `find_p_neighbor_from_vec`, `find_p_neighbors`, `basic_lemma` | prime/local methods | modular zeros for odd primes not dividing the discriminant and the `p=2` branch, p-neighbors from nonsingular conic zeros with optional transformation matrix, and represented-value search coprime to a prime |
| `SAGE_LIB/quadratic_forms/ternary_qf.py` | 989, 1025, 1065, 1255, 1635, 1674, 1740, 1917 | `symmetry`, `automorphism_symmetries`, `automorphism_spin_norm`, `_automorphisms_reduced_fast`, `_automorphisms_reduced_slow`, `automorphisms`, `_number_of_automorphisms_reduced`, `number_of_automorphisms` | automorphism methods | rational symmetry matrices, decomposition into symmetries, spin norm, border-table and slow finite-order automorphism enumeration, and automorphism count for definite forms |
| `SAGE_LIB/quadratic_forms/ternary_qf.py` | 1086, 1196 | `_border`, `_borders` | private helper methods | sixteen Eisenstein boundary conditions used by reduced-form automorphism helper tables |
| `SAGE_LIB/quadratic_forms/ternary_qf.py` | 1956, 1993 | `find_all_ternary_qf_by_level_disc`, `find_a_ternary_qf_by_level_disc` | `(N, d)` | search for reduced ternary forms by level `N` and discriminant `d`, with source condition `N | 4d` and `d | N^2` |

Ternary Cython backend helpers:

| File | Line | Surface | Notes |
|------|------|---------|-------|
| `SAGE_LIB/quadratic_forms/ternary.pyx` | 22, 47, 311 | `red_mfact`, `_reduced_ternary_form_eisenstein_with_matrix`, `_reduced_ternary_form_eisenstein_without_matrix` | Eisenstein reduction helpers |
| `SAGE_LIB/quadratic_forms/ternary.pyx` | 470, 491, 508, 542, 575, 644 | `primitivize`, `evaluate`, `_find_zeros_mod_p_2`, `pseudorandom_primitive_zero_mod_p`, `_find_zeros_mod_p_odd`, `_find_zeros_mod_p` | vector evaluation and modular-zero helpers |
| `SAGE_LIB/quadratic_forms/ternary.pyx` | 675, 806, 933, 984, 1089, 1124 | `_find_all_ternary_qf_by_level_disc`, `_find_a_ternary_qf_by_level_disc`, `extend`, `_find_p_neighbor_from_vec`, `_basic_lemma_vec`, `_basic_lemma` | level/discriminant search, matrix extension, p-neighbor, and basic-lemma helpers |

Key methods relevant to our hierarchy:

| Line | Method | Notes |
|------|--------|-------|
| 516 | `__init__` | constructor from `(R, n, entries)`, homogeneous degree-two polynomial, `(R, symmetric even-diagonal matrix)`, or symmetric even-diagonal matrix alone; `unsafe_initialization` can externally set cached automorphism-count/determinant fields |
| 676 | `list_external_initializations` | audit list of fields set by unsafe external initialization |
| 712, 724 | `__pari__`, `_pari_init_` | PARI Hessian-matrix conversion hooks |
| 736 | `_repr_` | upper-triangular display |
| 787, 812 | `__getitem__`, `__setitem__` | coefficient-index access and mutable coefficient update for upper-triangular presentation data |
| 980 | `__call__` | evaluates at a vector/list/tuple, or pulls back the form along a matrix and returns a new `QuadraticForm` |
| 1093 | `_is_even_symmetric_matrix_` | constructor/validation helper testing symmetry, base-ring coercion, and even diagonal |
| 4, 47 | `QFEvaluateVector` and `QFEvaluateVector_cdef` in `quadratic_form__evaluate.pyx` | internal fast vector-evaluation wrapper and Cython helper called by `QuadraticForm.__call__` |
| 65, 113 | `QFEvaluateMatrix` and `QFEvaluateMatrix_cdef` in `quadratic_form__evaluate.pyx` | internal fast matrix pullback wrapper and Cython helper called by `QuadraticForm.__call__` |
| 927 | `sum_by_coefficients_with` | coefficientwise sum for same-size quadratic forms |
| 1150 | `matrix` | Hessian matrix `A` where `Q(X)=(1/2)X^T A X` |
| 1164 | `Hessian_matrix` | Hessian matrix backing `matrix()` |
| 1190 | `Gram_matrix_rational` | Gram matrix over Frac(R) |
| 1214 | `Gram_matrix` | Gram matrix over base ring |
| 1251 | `has_integral_Gram_matrix` | predicate for existence of a base-ring Gram matrix |
| 1282 | `gcd` | coefficient content over `ZZ` |
| 1301 | `polynomial` | form as polynomial |
| 1353 | `from_polynomial` | static constructor from a homogeneous degree-two multivariate polynomial |
| 1393 | `is_primitive` | form not a scalar multiple of another |
| 1434 | `adjoint_primitive` | primitive adjoint form from the classical adjoint of the Hessian |
| 1451 | `dim` | number of variables |
| 1470 | `base_ring` | |
| 1482 | `coefficients` | upper-triangular coefficients |
| 1495 | `det` | det of Hessian |
| 1523 | `Gram_det` | det of Gram matrix |
| 1541 | `change_ring` | base ring change |
| 1586 | `level` | level over PID |
| 1656 | `level_ideal` | level as an ideal over the base ring |
| 1689 | `bilinear_map` | `B(v,w)` associated bilinear map |

Lazy-imported local-field and signature surfaces
(`quadratic_form__local_field_invariants.py`):

| Line | Method | Notes |
|------|--------|-------|
| 33 | `rational_diagonal_form(return_matrix=False)` | diagonal equivalent form over the fraction field; optionally returns transformation matrix |
| 192 | `_rational_diagonal_form_and_transformation()` | cached diagonalization backend returning `(D, T)` |
| 298 | `signature_vector()` | `(n_+, n_-, n_0)` for the associated symmetric matrix |
| 348 | `signature()` | derived scalar `n_+ - n_-` |
| 385 | `hasse_invariant(p)` | Cassels Hasse invariant at a prime or `-1` for infinity |
| 475 | `hasse_invariant__OMeara(p)` | O'Meara convention for Hasse invariant |
| 559 | `is_hyperbolic(p)` | local hyperbolic-plane predicate over `QQ_p` or `RR` |
| 618 | `is_anisotropic(p)` | local anisotropy predicate over `QQ_p` or `RR` |
| 688 | `is_isotropic(p)` | negation of local anisotropy |
| 735 | `anisotropic_primes()` | primes dividing `2*det(Q)` plus infinity where the form is anisotropic |
| 761 | `compute_definiteness()` | caches positive/negative/indefinite/zero/degenerate string |
| 851 | `compute_definiteness_string_by_determinants()` | Sylvester-style determinant sign classifier |
| 927 | `is_positive_definite()` | positive-definite predicate; zero-dimensional form is treated as positive definite |
| 964 | `is_negative_definite()` | negative-definite predicate; zero-dimensional form is treated as negative definite |
| 1001 | `is_indefinite()` | indefinite predicate; degenerate and zero-dimensional forms are not indefinite |
| 1038 | `is_definite()` | positive-or-negative-definite predicate |

Lazy-imported genus-symbol surfaces (`quadratic_form__genus.py`):

| Line | Method | Notes |
|------|--------|-------|
| 16 | `global_genus_symbol()` | `Genus(self.Hessian_matrix())`; only for quadratic forms over `ZZ` |
| 54 | `local_genus_symbol(p)` | Conway-Sloane local genus symbol of `2Q` at a positive prime `p` |
| 118 | `CS_genus_symbol_list(force_recomputation=False)` | cached local genus-symbol list for primes dividing `2*det(Q)` |

Lazy-imported automorphism and short-vector surfaces
(`quadratic_form__automorphisms.py`):

| Line | Method | Notes |
|------|--------|-------|
| 21 | `basis_of_short_vectors(show_lengths=False)` | PARI `qfminim` basis of short vectors; optional lengths |
| 97 | `short_vector_list_up_to_length(len_bound, up_to_sign_flag=False)` | positive-definite `ZZ` short-vector enumeration by length |
| 221 | `short_primitive_vector_list_up_to_length(len_bound, up_to_sign_flag=False)` | primitive sublist of short-vector enumeration |
| 257 | `_compute_automorphisms()` | PARI `qfauto` backend cache; requires definite form over `ZZ` |
| 289 | `automorphism_group()` | matrix group over the fraction field generated from PARI automorphisms |
| 335 | `automorphisms()` | list of automorphism matrices from the matrix group |
| 373 | `number_of_automorphisms()` | cached automorphism count |
| 401 | `set_number_of_automorphisms(num_autos)` | unsafe external-initialization setter for automorphism count |

Lazy-imported variable-substitution and presentation-transformation surfaces
(`quadratic_form__variable_substitutions.py`):

| Line | Method | Notes |
|------|--------|-------|
| 20 | `swap_variables(r, s, in_place=False)` | swap two variables; returns a new form unless mutating in place |
| 75 | `multiply_variable(c, i, in_place=False)` | substitute `x_i -> c*x_i` over the base ring |
| 117 | `divide_variable(c, i, in_place=False)` | substitute `x_i -> x_i/c` when division is defined in the base ring |
| 162 | `scale_by_factor(c, change_value_ring_flag=False)` | scale all coefficients, preserving the value ring when possible |
| 214 | `extract_variables(QF, var_indices)` | sub-presentation on selected variables |
| 245 | `elementary_substitution(c, i, j, in_place=False)` | substitute `x_i -> x_i + c*x_j` |
| 318 | `add_symmetric(c, i, j, in_place=False)` | compatibility wrapper for symmetric row/column addition; used by local normal form |

Lazy-imported local-normal-form surfaces (`quadratic_form__local_normal_form.py`):

| Line | Method | Notes |
|------|--------|-------|
| 27 | `find_entry_with_minimal_scale_at_prime(p)` | matrix-entry valuation selector at a prime |
| 82 | `local_normal_form(p)` | local integral Jordan form over `ZZ_p`; current source supports forms over `ZZ` |
| 233 | `jordan_blocks_by_scale_and_unimodular(p, safe_flag=True)` | cached list of local Jordan blocks by scale |
| 357 | `jordan_blocks_in_unimodular_list_by_scale_power(p)` | local Jordan blocks grouped by scale power |

Imported congruence-counting and local-density surfaces:

| File | Line | Method | Notes |
|------|------|--------|-------|
| `quadratic_form__count_local_2.py` | 15 | `count_congruence_solutions_as_vector(p, k, m, zvec, nzvec)` | solution counts by vector type modulo powers of `p` |
| `quadratic_form__count_local_2.py` | 73 | `count_congruence_solutions(p, k, m, zvec, nzvec)` | aggregate congruence solution count |
| `quadratic_form__count_local_2.py` | 98 | `count_congruence_solutions__good_type(p, k, m, zvec, nzvec)` | good-type solution count |
| `quadratic_form__count_local_2.py` | 123 | `count_congruence_solutions__zero_type(p, k, m, zvec, nzvec)` | zero-type solution count |
| `quadratic_form__count_local_2.py` | 148 | `count_congruence_solutions__bad_type(p, k, m, zvec, nzvec)` | bad-type solution count |
| `quadratic_form__count_local_2.py` | 173 | `count_congruence_solutions__bad_type_I(p, k, m, zvec, nzvec)` | bad type I count |
| `quadratic_form__count_local_2.py` | 198 | `count_congruence_solutions__bad_type_II(p, k, m, zvec, nzvec)` | bad type II count |
| `count_local_2.pyx` | 9 | `count_modp__by_gauss_sum(n, p, m, Qdet)` | Cython helper for finite-field solution counts by Gauss sum |
| `count_local_2.pyx` | 147 | `CountAllLocalTypesNaive(Q, p, k, m, zvec, nzvec)` | Cython helper counting all local solution types naively |
| `count_local_2.pyx` | 286 | `count_all_local_good_types_normal_form(Q, p, k, m, zvec, nzvec)` | Cython helper counting good local solution types after normal-form preparation |
| `quadratic_form__local_density_congruence.py` | 19 | `count_modp_solutions__by_Gauss_sum(p, m)` | finite-field solution count for nondegenerate forms mod odd `p` |
| `quadratic_form__local_density_congruence.py` | 56 | `local_good_density_congruence_odd(p, m, Zvec, NZvec)` | good-type density for odd `p`, assuming local diagonal form |
| `quadratic_form__local_density_congruence.py` | 142 | `local_good_density_congruence_even(m, Zvec, NZvec)` | good-type density for `p=2`, assuming local block diagonal form |
| `quadratic_form__local_density_congruence.py` | 319 | `local_good_density_congruence(p, m, Zvec=None, NZvec=None)` | dispatcher for good-type density |
| `quadratic_form__local_density_congruence.py` | 394 | `local_zero_density_congruence(p, m, Zvec=None, NZvec=None)` | zero-type density |
| `quadratic_form__local_density_congruence.py` | 467 | `local_badI_density_congruence(p, m, Zvec=None, NZvec=None)` | bad type I density |
| `quadratic_form__local_density_congruence.py` | 630 | `local_badII_density_congruence(p, m, Zvec=None, NZvec=None)` | bad type II density |
| `quadratic_form__local_density_congruence.py` | 776 | `local_bad_density_congruence(p, m, Zvec=None, NZvec=None)` | bad-type density dispatcher |
| `quadratic_form__local_density_congruence.py` | 834 | `local_density_congruence(p, m, Zvec=None, NZvec=None)` | local density subject to congruence conditions |
| `quadratic_form__local_density_congruence.py` | 902 | `local_primitive_density_congruence(p, m, Zvec=None, NZvec=None)` | primitive local density subject to congruence conditions |
| `quadratic_form__local_density_interfaces.py` | 11 | `local_density(p, m)` | public local density interface; first computes local normal form and primitive scale |
| `quadratic_form__local_density_interfaces.py` | 68 | `local_primitive_density(p, m)` | public primitive local density interface; first computes local normal form and primitive scale |

Imported theta-series, p-neighbor, and reduction-theory surfaces:

| File | Line | Method | Notes |
|------|------|--------|-------|
| `quadratic_form__theta.py` | 18 | `theta_series(Max=10, var_str='q', safe_flag=True)` | PARI-backed theta series to precision `O(q^Max)` |
| `quadratic_form__theta.py` | 72 | `theta_by_pari(Max, var_str='q', safe_flag=True)` | cached PARI representation-count vector or power series |
| `quadratic_form__theta.py` | 136 | `theta_by_cholesky(q_prec)` | explicit Cholesky enumeration backend |
| `quadratic_form__theta.py` | 263 | `theta_series_degree_2(Q, prec)` | degree-2 theta series dictionary for positive-definite integral forms |
| `quadratic_form__theta.py` | 341 | `B_v1(v)` | local nested bilinear-pairing helper inside `theta_series_degree_2`; closes over the current Hessian row data |
| `quadratic_form__neighbors.py` | 17 | `find_primitive_p_divisible_vector__random(p)` | random search for a primitive `p`-divisible vector mod `p` |
| `quadratic_form__neighbors.py` | 56 | `find_primitive_p_divisible_vector__next(p, v=None)` | deterministic next primitive `p`-divisible vector up to scaling |
| `quadratic_form__neighbors.py` | 142 | `find_p_neighbor_from_vec(p, y, return_matrix=False)` | `p`-neighbor from vector `y`; optionally returns transformation matrix |
| `quadratic_form__neighbors.py` | 252 | `neighbor_iteration(seeds, p, mass=None, max_classes=None, algorithm=None, max_neighbors=1000, verbose=False)` | explores `p`-neighbor graph by orbit, random, or exhaustion algorithms |
| `quadratic_form__neighbors.py` | 327, 332, 341 | nested `p_divisible_vectors(Q, max_neighbors)` strategy helpers | local generator helpers selected by `neighbor_iteration` algorithm branch: orbit representatives, deterministic exhaustion, or random primitive-vector search |
| `quadratic_form__neighbors.py` | 380 | `orbits_lines_mod_p(p)` | GAP-backed orbit representatives of lines in `L/pL` under the form automorphism group |
| `quadratic_form__reduction_theory.py` | 13 | `reduced_binary_form1()` | proper binary reduction returning form plus determinant-one transform |
| `quadratic_form__reduction_theory.py` | 72 | `reduced_ternary_form__Dickson()` | named ternary Dickson reduction stub with no implemented computation |
| `quadratic_form__reduction_theory.py` | 88 | `reduced_binary_form()` | binary-style reduction returning form plus transformation |
| `quadratic_form__reduction_theory.py` | 142 | `minkowski_reduction()` | positive-definite reduction for dimensions at most four |
| `quadratic_form__reduction_theory.py` | 277 | `minkowski_reduction_for_4vars__SP()` | Schulze-Pillot four-variable Minkowski reduction variant |

Imported ternary, mass, representability, split-covering, and solve surfaces:

| File | Line | Method | Notes |
|------|------|--------|-------|
| `quadratic_form__ternary_Tornaria.py` | 35 | `disc()` | ternary discriminant invariant |
| `quadratic_form__ternary_Tornaria.py` | 63 | `content()` | ternary coefficient content |
| `quadratic_form__ternary_Tornaria.py` | 110 | `adjoint()` | ternary adjoint form |
| `quadratic_form__ternary_Tornaria.py` | 138 | `antiadjoint()` | ternary anti-adjoint form |
| `quadratic_form__ternary_Tornaria.py` | 167 | `is_adjoint()` | ternary adjoint predicate |
| `quadratic_form__ternary_Tornaria.py` | 186 | `reciprocal()` | ternary reciprocal form |
| `quadratic_form__ternary_Tornaria.py` | 212 | `omega()` | ternary Tornaria invariant |
| `quadratic_form__ternary_Tornaria.py` | 227 | `delta()` | ternary Tornaria invariant |
| `quadratic_form__ternary_Tornaria.py` | 242 | `level__Tornaria()` | ternary level convention |
| `quadratic_form__ternary_Tornaria.py` | 269 | `discrec()` | ternary discriminant/reciprocal data |
| `quadratic_form__ternary_Tornaria.py` | 288 | `hasse_conductor()` | ternary Hasse conductor |
| `quadratic_form__ternary_Tornaria.py` | 314 | `clifford_invariant(p)` | ternary Clifford invariant at `p` |
| `quadratic_form__ternary_Tornaria.py` | 351 | `clifford_conductor()` | ternary Clifford conductor |
| `quadratic_form__ternary_Tornaria.py` | 396 | `basiclemma(M)` | Tornaria basic lemma helper |
| `quadratic_form__ternary_Tornaria.py` | 411 | `basiclemmavec(M)` | vector version of Tornaria helper |
| `quadratic_form__ternary_Tornaria.py` | 454 | `xi(p)` | ternary local invariant |
| `quadratic_form__ternary_Tornaria.py` | 484 | `xi_rec(p)` | reciprocal ternary local invariant |
| `quadratic_form__ternary_Tornaria.py` | 510 | `lll()` | ternary LLL-style reduction wrapper |
| `quadratic_form__ternary_Tornaria.py` | 529 | `representation_number_list(B)` | representation counts up to bound `B` |
| `quadratic_form__ternary_Tornaria.py` | 545 | `representation_vector_list(B, maxvectors=10**8)` | representation vectors up to bound `B` |
| `quadratic_form__ternary_Tornaria.py` | 592 | `is_zero(v, p=0)` | zero vector predicate modulo `p` |
| `quadratic_form__ternary_Tornaria.py` | 612 | `is_zero_nonsingular(v, p=0)` | nonsingular zero predicate modulo `p` |
| `quadratic_form__ternary_Tornaria.py` | 635 | `is_zero_singular(v, p=0)` | singular zero predicate modulo `p` |
| `quadratic_form__siegel_product.py` | 36 | `siegel_product(u)` | infinite product of local densities for representation of `u` |
| `quadratic_form__mass.py` | 35 | `shimura_mass__maximal()` | Shimura mass formula for maximal quadratic lattices |
| `quadratic_form__mass.py` | 51 | `GHY_mass__maximal()` | Gan-Hanke-Yu mass formula for maximal quadratic lattices |
| `quadratic_form__mass__Siegel_densities.py` | 26 | `mass__by_Siegel_densities(odd_algorithm='Pall', even_algorithm='Watson')` | mass via Siegel densities with selected local algorithms |
| `quadratic_form__mass__Siegel_densities.py` | 116 | `Pall_mass_density_at_odd_prime(p)` | odd-prime local mass density |
| `quadratic_form__mass__Siegel_densities.py` | 174 | `Watson_mass_at_2()` | 2-adic mass density by Watson |
| `quadratic_form__mass__Siegel_densities.py` | 258 | `Kitaoka_mass_at_2()` | 2-adic mass density by Kitaoka |
| `quadratic_form__mass__Siegel_densities.py` | 341 | `mass_at_two_by_counting_mod_power(k)` | 2-adic mass density by congruence counting |
| `quadratic_form__mass__Conway_Sloane_masses.py` | 14 | `parity(allow_rescaling_flag=True)` | Conway-Sloane parity convention |
| `quadratic_form__mass__Conway_Sloane_masses.py` | 110 | `is_even(allow_rescaling_flag=True)` | Conway-Sloane even predicate |
| `quadratic_form__mass__Conway_Sloane_masses.py` | 129 | `is_odd(allow_rescaling_flag=True)` | Conway-Sloane odd predicate |
| `quadratic_form__mass__Conway_Sloane_masses.py` | 148 | `conway_species_list_at_odd_prime(p)` | Conway-Sloane odd-prime species list |
| `quadratic_form__mass__Conway_Sloane_masses.py` | 217 | `conway_species_list_at_2()` | Conway-Sloane 2-adic species list |
| `quadratic_form__mass__Conway_Sloane_masses.py` | 301 | `conway_octane_of_this_unimodular_Jordan_block_at_2()` | octane invariant for a 2-adic unimodular Jordan block |
| `quadratic_form__mass__Conway_Sloane_masses.py` | 386 | `conway_diagonal_factor(p)` | Conway-Sloane diagonal mass factor |
| `quadratic_form__mass__Conway_Sloane_masses.py` | 426 | `conway_cross_product_doubled_power(p)` | Conway-Sloane cross-product exponent |
| `quadratic_form__mass__Conway_Sloane_masses.py` | 459 | `conway_type_factor()` | Conway-Sloane type factor |
| `quadratic_form__mass__Conway_Sloane_masses.py` | 479 | `conway_p_mass(p)` | Conway-Sloane p-mass |
| `quadratic_form__mass__Conway_Sloane_masses.py` | 508 | `conway_standard_p_mass(p)` | standardized Conway-Sloane p-mass |
| `quadratic_form__mass__Conway_Sloane_masses.py` | 544 | `conway_standard_mass()` | standardized Conway-Sloane mass |
| `quadratic_form__mass__Conway_Sloane_masses.py` | 584 | `conway_mass()` | Conway-Sloane mass |
| `quadratic_form__local_representation_conditions.py` | 20 | `QuadraticFormLocalRepresentationConditions` | local-representation condition object for a quadratic form |
| `quadratic_form__local_representation_conditions.py` | 204 | `QuadraticFormLocalRepresentationConditions.__repr__()` | display protocol for local-representation condition vectors |
| `quadratic_form__local_representation_conditions.py` | 240 | `QuadraticFormLocalRepresentationConditions.__eq__(right)` | equality protocol for local-representation condition objects |
| `quadratic_form__local_representation_conditions.py` | 284 | `squareclass_vector(p)` | squareclass data for local representation at `p` |
| `quadratic_form__local_representation_conditions.py` | 311 | `local_conditions_vector_for_prime(p)` | local condition vector for a prime |
| `quadratic_form__local_representation_conditions.py` | 365 | `is_universal_at_prime(p)` | universality at one prime |
| `quadratic_form__local_representation_conditions.py` | 410 | `is_universal_at_all_finite_primes()` | universality at all finite primes |
| `quadratic_form__local_representation_conditions.py` | 441 | `is_universal_at_all_places()` | universality including the real place |
| `quadratic_form__local_representation_conditions.py` | 481 | `is_locally_represented_at_place(m, p)` | local representation of `m` at one place |
| `quadratic_form__local_representation_conditions.py` | 549 | `is_locally_represented(m)` | local representation of `m` at all places |
| `quadratic_form__local_representation_conditions.py` | 608 | `local_representation_conditions(recompute_flag=False, silent_flag=False)` | cached condition object on `QuadraticForm` |
| `quadratic_form__local_representation_conditions.py` | 716 | `is_locally_universal_at_prime(p)` | wrapper for condition-object prime universality |
| `quadratic_form__local_representation_conditions.py` | 760 | `is_locally_universal_at_all_primes()` | wrapper for finite-prime universality |
| `quadratic_form__local_representation_conditions.py` | 788 | `is_locally_universal_at_all_places()` | wrapper for all-place universality |
| `quadratic_form__local_representation_conditions.py` | 817 | `is_locally_represented_number_at_place(m, p)` | wrapper for local representation of `m` at one place |
| `quadratic_form__local_representation_conditions.py` | 862 | `is_locally_represented_number(m)` | wrapper for local representation of `m` at all places |
| `quadratic_form__split_local_covering.py` | 21 | `cholesky_decomposition(bit_prec=53)` | real Cholesky backend matrix |
| `quadratic_form__split_local_covering.py` | 111 | `vectors_by_length(bound)` | short vectors with values by bound |
| `quadratic_form__split_local_covering.py` | 261 | `complementary_subform_to_vector(v)` | complementary subform to a vector |
| `quadratic_form__split_local_covering.py` | 356 | `split_local_cover()` | split local covering construction |
| `qfsolve.py` | 37 | `qfsolve(G)` | solve a homogeneous quadratic equation represented by Gram matrix `G` |
| `qfsolve.py` | 84 | `qfparam(G, sol)` | parametrization from one solution |
| `qfsolve.py` | 124 | `solve(c=0)` | `QuadraticForm` method solving `Q(x)=c` |

Imported equivalence-testing surfaces (`quadratic_form__equivalence_testing.py`):

| Line | Method | Notes |
|------|--------|-------|
| 25 | `is_globally_equivalent_to(other, return_matrix=False)` | positive-definite integral equivalence test; optionally returns transformation matrix |
| 119 | `is_locally_equivalent_to(other, check_primes_only=False, force_jordan_equivalence_test=False)` | local equivalence over the real place and all p-adic integral places |
| 178 | `has_equivalent_Jordan_decomposition_at_prime(other, p)` | p-adic Jordan-decomposition equivalence test at one prime |
| 304 | `is_rationally_isometric(other, return_matrix=False)` | rational or number-field quadratic-form isometry test; transformation matrix currently only implemented over `QQ` |
| 553 | `_diagonal_isometry(V, W)` | backend transformation between diagonal forms |
| 654 | `_gram_schmidt(m, fixed_vector_index, inner_product)` | backend Gram-Schmidt helper for isometry construction |

Imported genus-package surfaces (`sage/quadratic_forms/genera`):

| File | Line | Surface | Notes |
|------|------|---------|-------|
| `genera/genus.py` | 41 | `genera(sig_pair, determinant, max_scale=None, even=False)` | enumerates non-empty global genera with fixed signature and determinant data |
| `genera/genus.py` | 127 | `_local_genera(p, rank, det_val, max_scale, even)` | helper enumerating local p-adic genus symbols used by `genera` |
| `genera/genus.py` | 226 | `_blocks(b, even_only=False)` | helper enumerating viable 2-adic Jordan-block symbol completions for `_local_genera` |
| `genera/genus.py` | 325 | `Genus(A, factored_determinant=None)` | global genus symbol from a nonsingular symmetric integral Gram matrix |
| `genera/genus.py` | 377 | `LocalGenusSymbol(A, p)` | local Conway-Sloane genus symbol at a prime |
| `genera/genus.py` | 411 | `is_GlobalGenus(G)` | realizability test for a global genus symbol |
| `genera/genus.py` | 464 | `is_2_adic_genus(genus_symbol_quintuple_list)` | 2-adic genus-symbol validity predicate |
| `genera/genus.py` | 524 | `canonical_2_adic_compartments(genus_symbol_quintuple_list)` | canonical 2-adic compartment partition |
| `genera/genus.py` | 592 | `canonical_2_adic_trains(genus_symbol_quintuple_list, compartments=None)` | canonical 2-adic train partition |
| `genera/genus.py` | 694 | `canonical_2_adic_reduction(genus_symbol_quintuple_list)` | canonical 2-adic symbol reduction |
| `genera/genus.py` | 785 | `basis_complement(B)` | field-row-space complement helper for echelonized basis matrices |
| `genera/genus.py` | 825 | `signature_pair_of_matrix(A)` | signature pair of a symmetric matrix |
| `genera/genus.py` | 877 | `p_adic_symbol(A, p, val)` | p-adic genus symbol data from a Gram matrix |
| `genera/genus.py` | 945 | `is_even_matrix(A)` | matrix evenness predicate plus normalization data |
| `genera/genus.py` | 976 | `split_odd(A)` | odd-primary splitting helper |
| `genera/genus.py` | 1064 | `trace_diag_mod_8(A)` | 2-adic trace/oddity helper |
| `genera/genus.py` | 1106 | `two_adic_symbol(A, val)` | 2-adic genus symbol data from a Gram matrix |
| `genera/genus.py` | 1203 | `Genus_Symbol_p_adic_ring` | local p-adic genus-symbol object |
| `genera/genus.py` | 1263, 1295, 1377, 1428, 1463 | `Genus_Symbol_p_adic_ring.__init__(prime, symbol, check=True)`, `__repr__()`, `_latex_()`, `__eq__(other)`, `__ne__(other)` | constructor, display, LaTeX, and equality protocol surfaces for local genus symbols |
| `genera/genus.py` | 1503 | `Genus_Symbol_p_adic_ring.automorphous_numbers()` | spinor-norm square-class generators at one prime |
| `genera/genus.py` | 1666 | `Genus_Symbol_p_adic_ring.canonical_symbol()` | canonical local genus-symbol data |
| `genera/genus.py` | 1732 | `Genus_Symbol_p_adic_ring.gram_matrix(check=True)` | Gram matrix representative for the local symbol |
| `genera/genus.py` | 1765 | `Genus_Symbol_p_adic_ring.mass()` | local mass factor |
| `genera/genus.py` | 1817, 1840 | `Genus_Symbol_p_adic_ring._standard_mass()`, `_species_list()` | backend Conway-Sloane local-mass helpers |
| `genera/genus.py` | 1900 | `Genus_Symbol_p_adic_ring.prime()` | local prime |
| `genera/genus.py` | 1917 | `Genus_Symbol_p_adic_ring.is_even()` | local evenness convention |
| `genera/genus.py` | 1943 | `Genus_Symbol_p_adic_ring.symbol_tuple_list()` | copied local symbol tuple data |
| `genera/genus.py` | 1975 | `Genus_Symbol_p_adic_ring.number_of_blocks()` | number of positive-dimensional Jordan blocks |
| `genera/genus.py` | 2004 | `Genus_Symbol_p_adic_ring.determinant()` | p-part determinant; `det` alias at line 2035 |
| `genera/genus.py` | 2037 | `Genus_Symbol_p_adic_ring.dimension()` | local rank/dimension; `dim` and `rank` aliases at lines 2064-2065 |
| `genera/genus.py` | 2067 | `Genus_Symbol_p_adic_ring.direct_sum(other)` | local direct-sum genus symbol over the same prime |
| `genera/genus.py` | 2124 | `Genus_Symbol_p_adic_ring.excess()` | p-excess or 2-adic oddity |
| `genera/genus.py` | 2197 | `Genus_Symbol_p_adic_ring.scale()` | local scale ideal generator |
| `genera/genus.py` | 2219 | `Genus_Symbol_p_adic_ring.norm()` | local norm ideal generator |
| `genera/genus.py` | 2245 | `Genus_Symbol_p_adic_ring.level()` | maximal local Jordan scale |
| `genera/genus.py` | 2259 | `Genus_Symbol_p_adic_ring.trains()` | 2-adic train indices |
| `genera/genus.py` | 2285 | `Genus_Symbol_p_adic_ring.compartments()` | 2-adic compartment indices |
| `genera/genus.py` | 2312 | `GenusSymbol_global_ring` | global genus symbol from signature and local symbols |
| `genera/genus.py` | 2350, 2384, 2421, 2447, 2494 | `GenusSymbol_global_ring.__init__(signature_pair, local_symbols, representative=None, check=True)`, `__repr__()`, `_latex_()`, `__eq__(other)`, `__ne__(other)` | constructor, display, LaTeX, and equality protocol surfaces for global genus symbols |
| `genera/genus.py` | 2525 | `GenusSymbol_global_ring.is_even()` | global genus evenness |
| `genera/genus.py` | 2539 | `GenusSymbol_global_ring.signature_pair()` | global signature pair; `signature_pair_of_matrix` alias at line 2556 |
| `genera/genus.py` | 2558 | `GenusSymbol_global_ring._proper_spinor_kernel()` | backend proper spinor-kernel data |
| `genera/genus.py` | 2597 | `GenusSymbol_global_ring._improper_spinor_kernel()` | backend improper spinor-kernel data |
| `genera/genus.py` | 2636 | `GenusSymbol_global_ring.spinor_generators(proper)` | primes generating spinor genera |
| `genera/genus.py` | 2677 | `GenusSymbol_global_ring._proper_is_improper()` | backend comparison of proper and improper spinor genus |
| `genera/genus.py` | 2724 | `GenusSymbol_global_ring.signature()` | scalar signature `p-n` |
| `genera/genus.py` | 2741 | `GenusSymbol_global_ring.determinant()` | global determinant; `det` alias at line 2761 |
| `genera/genus.py` | 2763 | `GenusSymbol_global_ring.dimension()` | global rank/dimension; `dim` and `rank` aliases at lines 2777-2778 |
| `genera/genus.py` | 2780 | `GenusSymbol_global_ring.direct_sum(other)` | direct sum of global genus symbols |
| `genera/genus.py` | 2811 | `GenusSymbol_global_ring.discriminant_form()` | discriminant finite quadratic module associated to the genus |
| `genera/genus.py` | 2845 | `GenusSymbol_global_ring.rational_representative()` | rational Gram matrix representative |
| `genera/genus.py` | 2888 | `GenusSymbol_global_ring._compute_representative(LLL=True)` | backend construction of an integral representative using local modification |
| `genera/genus.py` | 2952 | `GenusSymbol_global_ring.representative()` | cached integral Gram matrix representative |
| `genera/genus.py` | 2982 | `GenusSymbol_global_ring.representatives(backend=None, algorithm=None)` | class representatives in the genus via Sage or Magma backends |
| `genera/genus.py` | 3115 | `GenusSymbol_global_ring.local_symbols()` | copied list of local symbols |
| `genera/genus.py` | 3129 | `GenusSymbol_global_ring.local_symbol(p)` | copied or default local symbol at a prime |
| `genera/genus.py` | 3148 | `GenusSymbol_global_ring._standard_mass()` | backend standard-mass helper depending on dimension and determinant |
| `genera/genus.py` | 3187 | `GenusSymbol_global_ring.mass(backend='sage')` | definite genus mass via Sage or Magma backend |
| `genera/genus.py` | 3266 | `GenusSymbol_global_ring.level()` | global level from local levels |
| `genera/genus.py` | 3281 | `GenusSymbol_global_ring.scale()` | global scale from local scales |
| `genera/genus.py` | 3299 | `GenusSymbol_global_ring.norm()` | global norm from local norms |
| `genera/genus.py` | 3319 | `_gram_from_jordan_block(p, block, discr_form=False)` | backend helper constructing Gram matrices for Jordan blocks and discriminant forms |
| `genera/genus.py` | 3434 | `M_p(species, p)` | Conway-Sloane diagonal mass factor helper |
| `genera/normal_form.py` | 98 | `collect_small_blocks(G)` | block decomposition helper for 1-by-1 and 2-by-2 p-adic blocks |
| `genera/normal_form.py` | 129 | `p_adic_normal_form(G, p, precision=None, partial=False, debug=False)` | p-adic normal form and transformation matrix for Gram matrices |
| `genera/normal_form.py` | 293, 354, 389, 441, 554, 630, 734, 758, 851, 978, 1016, 1110, 1375 | `_find_min_p(G, cnt, lower_bound=0)`, `_get_small_block_indices(G)`, `_get_homogeneous_block_indices(G)`, `_homogeneous_normal_form(G, w)`, `_jordan_odd_adic(G)`, `_jordan_2_adic(G)`, `_min_nonsquare(p)`, `_normalize(G, normal_odd=True)`, `_normalize_2x2(G)`, `_normalize_odd_2x2(G)`, `_partial_normal_form_of_block(G)`, `_relations(G, n)`, `_two_adic_normal_forms(G, partial=False)` | private p-adic normal-form backend helpers for pivot search, block indexing, Jordan decomposition, square-class normalization, 2-adic relations, and final normal-form assembly |
| `genera/spinor_genus.py` | 35 | `SpinorOperator` | spinor operator element as a tuple of local square classes |
| `genera/spinor_genus.py` | 50 | `SpinorOperator._repr_()` | spinor-operator display protocol |
| `genera/spinor_genus.py` | 78 | `SpinorOperators(primes)` | internal spinor-operator group for spinor genus computations |
| `genera/spinor_genus.py` | 95, 113, 132 | `SpinorOperators.__init__(primes)`, `SpinorOperators.__reduce__()`, `SpinorOperators._repr_()` | internal spinor-operator constructor, pickle protocol, and display protocol |
| `genera/spinor_genus.py` | 144 | `SpinorOperators.to_square_class(x, p)` | local unit square-class embedding |
| `genera/spinor_genus.py` | 191 | `SpinorOperators.delta(r, prime=None)` | Conway-Sloane diagonal embedding of rational square classes |

---

## Reference: retired project-local `src/lattices/categories/` method surfaces

The `src/lattices/categories/...` paths below are not active files in this checkout.
They are retired project-local provenance for method names mined from the lattice
redesign, not installed Sage providers and not current implementation owners.
The active owner surfaces are split across `category_specs/forms` for generic
formed-module and bilinear/quadratic form structure,
`category_specs/modules/subcategories/finitely_presented_over_pid.py` for
PID-module invariant-factor and torsion structure, and `category_specs/lattices` for
the `Lattices(R)` endpoint, constructor collector, Hom/End/Aut refinements, and
lattice-specific construction categories.

### `BilinearModules` (src/lattices/categories/bilinear_modules.py)

**ParentMethods** (abstract unless noted):
`bilinear_form`, `gens`, `zero`, `base_ring`, `free_part`, `torsion_part`, `Hom`,
`dual`, `twist`, `span`, `cardinality`

**ParentMethods** (derived — one-liners):
`b(v,w)` (delegates to `bilinear_form().evaluate(v,w)`),
`gram_matrix()` (fills matrix with `b(e_i, e_j)` — **note**: this is placed here in
src/, but correct placement is `Free + Bilinear`; see MAPPING.md),
`End()`, `symbolic_form()`, `direct_sum(other)`, `__add__`, `__pow__`, `__mul__`

**ElementMethods** (abstract): `parent`, `__add__`, `__neg__`, `__rmul__`, `__eq__`,
`__hash__`, `to_vector`

**ElementMethods** (derived): `__mul__` (= b(self, other)), `self_product` (= b(v,v)),
`is_isotropic`, `span`, `__sub__`

**MorphismMethods** (abstract): `domain`, `codomain`, `__call__`, `to_matrix`,
`kernel`, `image`, `cokernel`, `is_isometry`

**MorphismMethods** (derived): `is_injective`, `is_surjective`, `is_bijective`,
`is_isomorphism`, `__mul__` (composition), `direct_sum`

### `FreeBilinearModules` (src/lattices/categories/free_bilinear_modules.py)

**ParentMethods** (abstract): `rank`, `is_nondegenerate`, `is_positive_definite`,
`is_negative_definite`

**ParentMethods** (derived — overrides): `free_part` (= self), `torsion_part` (= 0),
`cardinality` (= ∞ if rank > 0)

**ParentMethods** (derived): `is_definite`, `is_indefinite`

**ElementMethods** (abstract): `divisibility`

**ElementMethods** (derived): `is_primitive`, `discriminant_class`

**SubcategoryMethods**: `NonDegenerate()`

### `Lattices` (src/lattices/categories/lattices.py)

**ParentMethods** (abstract): `signature_pair`, `determinant`, `is_even`,
`nikulin_invariants`, `dual`, `inclusion_morphism`, `discriminant_group`,
`is_isometric_to`, `is_rationally_isometric_to`, `is_locally_isometric_to`,
`rational_span`, `to_quadratic_module`

**ParentMethods** (derived): `signature`, `discriminant`, `is_odd`, `is_unimodular`,
`genus`, `O()` / `orthogonal_group()`

**ElementMethods** (abstract): `norm`, `is_root`

**ElementMethods** (derived): `is_isotropic`, `reflection`, `perp`

`reflection` is not an installed Sage `FreeQuadraticModule` method in the audited
source; it is recovered from the preserved lattice spec backup and the reflective
lattice theory note.  The formula is defined in scalar extension for non-isotropic
vectors, and its membership in the original lattice orthogonal group is the separate
root/lattice-preservation condition `2 b(v,x) / b(v,v) in R` for all `x in L`.

**SubcategoryMethods**: `Even()`, `Unimodular()`

### `RationalLattices` (src/lattices/categories/rational_lattices.py)

**ParentMethods** (abstract): `signature_pair`, `base_change_to`, `orthogonal_complement_of`

**ParentMethods** (derived): `signature`, `is_positive_definite`, `is_negative_definite`

**ElementMethods** (abstract): `is_integral`

**ElementMethods** (derived): `perp`

### `TorsionBilinearModules` (src/lattices/categories/torsion_bilinear_modules.py)

**ParentMethods** (abstract): `is_p_elementary`, `p_part`, `jordan_decomposition`.
Invariant-factor surfaces such as `invariants()` are inherited from finitely
presented modules over a PID, not owned by torsion bilinear or discriminant
categories.

**ParentMethods** (derived overrides): `free_part` (= 0), `torsion_part` (= self),
`cardinality` (= product of invariants)

**ElementMethods** (abstract): `additive_order`, `lift`

### `DiscriminantQuadraticForms` (src/lattices/categories/discriminant_quadratic_forms.py)

Thin category: `super_categories` only; no additional method surface yet.
