# Variadic Signature Inventory

This inventory records the remaining category-spec surfaces that still look
variadic, or that still collapse Sage's finite constructor casework into one
placeholder signature. It is the input for the follow-up scoping pass; it does not
split or rewrite the specs.

## Scoping Result

The serial scoping pass has split the public surfaces listed below into named
methods or closed overloads and recorded the forward mapping in the owning subtree
mapping files:

| Surface family | Result |
| --- | --- |
| Module constructors and quotient inputs | Split in `modules/__init__.py` and `modules/subcategories/constructions/quotients.py`; mapping recorded in `modules/docs/MAPPING.md`. |
| Ring constructors, p-adic precision tuples, series factories, matrix element construction, and number-field optional arguments | Split in `rings/__init__.py`, `rings/matrix_algebras.py`, `rings/subcategories/number_field.py`, and `rings/subcategories/rational_field.py`; mapping recorded in `rings/docs/MAPPING.md`. |
| Tensor component data | Public catch-all removed in favor of named tensor constructors; mapping recorded in `tensor_algebra_components/docs/MAPPING.md`. |
| Algebra subalgebra and ideal option bags | Split into named subalgebra and left/right/two-sided ideal methods; mapping recorded in `algebras/docs/MAPPING.md`. |
| Lattice `short_vectors(..., **kwargs)` | Split into `short_vectors(bound)` and `short_vectors_up_to_sign(bound)`; mapping recorded in `lattices/docs/MAPPING.md`. |
| Poset constructor variadics | Already split into named constructor families in `posets/docs/MAPPING.md`; no code change in this pass. |
| Set iterator and element-class forwarding variadics | Kept out of public specs; recovery mapping recorded in `sets/docs/MAPPING.md`. |
| Real-set variadics | Already mapped to named `Sets().Constructors()` real-subset constructors in `topological_spaces/docs/MAPPING.md`; no code change in this pass. |

The detailed source inventory below is retained as provenance for the split.

Ordinary typed finite collections are not listed merely because they use
`Sequence`, `tuple`, `list`, or `dict`. The audit only records collection
parameters when they stand in for multiple Sage input shapes or raw coordinate
interop that still needs explicit overload review.

## Original Project Spec Surfaces Scoped

- File: `modules/__init__.py:576`
  Symbol: `Modules(R).Constructors().FreeModule`
  Original signature: `rank_or_basis_keys: Integer | Set | SetFamily | None`,
  `inner_product_matrix: Matrix | Sequence[Sequence[RingElement]] |
  Sequence[RingElement] | None`, plus keyword `rank` and `basis_keys`.
  Why it needed scoping: the first parameter still merges rank construction and
  basis-key construction, while the form data accepts matrix and list shapes in
  one slot.
  Source surface used for scoping: `modules/docs/SAGE_INVENTORY.md` records
  `FreeModule(R, rank_or_basis_keys, ...)` and its dispatch to ordinary free
  modules, finite-rank free modules, combinatorial free modules, and quadratic
  modules.

- File: `modules/__init__.py:609`
  Symbol: `Modules(R).Constructors().VectorSpace`
  Original signature: `dimension_or_basis_keys: Integer | Set | SetFamily |
  None`, `inner_product_matrix: Matrix | Sequence[Sequence[RingElement]] |
  Sequence[RingElement] | None`, plus keyword `dimension` and `basis_keys`.
  Why it needed scoping: this repeats the free-module merged rank/basis-key path
  under field-only vocabulary.
  Source surface used for scoping: `modules/docs/SAGE_INVENTORY.md` records
  `VectorSpace(K, dimension_or_basis_keys, ...)` as a field-checking wrapper
  around `FreeModule`.

- File: `modules/__init__.py:633`
  Symbol: `Modules(R).Constructors().FreeQuadraticModule`
  Original signature: `inner_product_matrix: Matrix |
  Sequence[Sequence[RingElement]] | Sequence[RingElement]`.
  Why it needed scoping: the form input still accepts several coordinate shapes in
  one parameter instead of named matrix/vector cases.
  Source surface used for scoping: `modules/docs/SAGE_INVENTORY.md` records
  `FreeQuadraticModule(R, rank, inner_product_matrix, ...)`.

- File: `modules/__init__.py:723`
  Symbol: `Modules(R).Constructors().FPModule`
  Original signature: `arg0: Algebra | RModule | RModMorphism`,
  `generator_degrees`, `relations`, and `names`.
  Why it needed scoping: `arg0` merges the cokernel-of-map construction with the
  algebra-plus-generators presentation construction.
  Source surface used for scoping: `modules/docs/SAGE_INVENTORY.md` records
  `FPModule(arg0, generator_degrees=None, relations=(), ...)`.

- File: `modules/__init__.py:754`
  Symbol: `Modules(R).Constructors().IntegerLattice`
  Original signature: `basis: Matrix | Sequence[Sequence[RingElement]]`.
  Why it needed scoping: this admits both matrix and nested-list coordinate data in
  the same constructor parameter.
  Source surface used for scoping: `modules/docs/SAGE_INVENTORY.md` records
  `IntegerLattice(basis, lll_reduce=True)`.

- File: `modules/__init__.py:765`
  Symbol: `Modules(R).Constructors().TorsionQuadraticForm`
  Original signature: `q: Matrix | Sequence[Sequence[RingElement]]`.
  Why it needed scoping: this admits both matrix and nested-list data in one
  constructor parameter.
  Source surface used for scoping: `modules/docs/SAGE_INVENTORY.md` records
  `TorsionQuadraticForm(q)`.

- File: `modules/__init__.py:809`
  Symbol: `Modules(R).Constructors().polynomial_ring_as_module`
  Original signature: overload and implementation paths allow
  `n: Integer | tuple[Integer, ...] | None` with
  `var_array: str | Sequence[str] | None`.
  Why it needed scoping: the module bridge admits the higher-dimensional
  `var_array` tuple shape even though `rings/docs/MAPPING.md` says that Sage's
  unbounded positional `PolynomialRing(R, 2, 3, 4, var_array=...)` shape is not
  admitted yet.
  Source surface used for scoping: `rings/docs/MAPPING.md` and the Sage
  `PolynomialRing` factory casework.

- File: `modules/__init__.py:856`
  Symbol: `Modules(R).Constructors().power_series_ring_as_module`
  Original signature: `name`, `arg2: Integer | str | None`, `names`,
  `num_gens`, and related series options.
  Why it needed scoping: `arg2` is Sage positional plumbing rather than
  mathematical vocabulary.
  Source surface used for scoping: the `PowerSeriesRing` constructor family in
  `rings/docs/SAGE_INVENTORY.md` and the Sage series-ring factory docs/source.

- File: `modules/__init__.py:883`
  Symbol: `Modules(R).Constructors().laurent_series_ring_as_module`
  Original signature: `name`, `arg2: Integer | str | None`, `names`,
  `num_gens`, and related series options.
  Why it needed scoping: this repeats the unsplit series-ring constructor shape
  while routing the result through module refinement.
  Source surface used for scoping: the `LaurentSeriesRing` constructor family in
  `rings/docs/SAGE_INVENTORY.md` and the Sage series-ring factory docs/source.

- File: `modules/__init__.py:910`
  Symbol: `Modules(R).Constructors().puiseux_series_ring_as_module`
  Original signature: `name`, `arg2: Integer | str | None`, `names`,
  `num_gens`, and related series options.
  Why it needed scoping: this repeats the unsplit series-ring constructor shape
  while routing the result through module refinement.
  Source surface used for scoping: the `PuiseuxSeriesRing` constructor family in
  `rings/docs/SAGE_INVENTORY.md` and the Sage series-ring factory docs/source.

- File: `modules/subcategories/constructions/quotients.py:68`
  Symbol: `Modules(R).Quotients().ParentMethods.quotient_module`
  Original signature: `submodule: RModule | Matrix | Sequence[RModuleElement] |
  Sequence[Sequence[RingElement]]`.
  Why it needed scoping: the quotient method accepts an existing submodule,
  generator data, matrix data, and nested coordinate data in one parameter.
  Source surface used for scoping: `modules/docs/SAGE_INVENTORY.md` records
  quotient modules, `FGP_Module`, and quotient syntax on free modules.

- File: `rings/__init__.py:673`
  Symbol: `Rings().Constructors().NumberField`
  Original signature: `polynomial: Polynomial | Sequence[Polynomial]`, with
  sequence-capable `name`, `names`, `embedding`, `latex_name`, `structure`, and
  `latex_names`.
  Why it needed scoping: one constructor still merges simple number fields,
  relative/tower input, and paired sequence metadata.
  Source surface used for scoping: `rings/docs/SAGE_INVENTORY.md` records the
  `NumberField`, `QuadraticField`, and `CyclotomicField` constructor family.

- File: `rings/__init__.py:736`
  Symbol: `Rings().Constructors().Zp`
  Original signature: `prec: Integer | tuple[Integer, Integer] | None` plus
  precision-type and print-mode options.
  Why it needed scoping: the precision parameter accepts a scalar and a two-entry
  tuple shape without a named distinction.
  Source surface used for scoping: the `Zp` p-adic constructor family in
  `rings/docs/SAGE_INVENTORY.md` and Sage p-adic factory docs/source.

- File: `rings/__init__.py:774`
  Symbol: `Rings().Constructors().Qp`
  Original signature: `prec: Integer | tuple[Integer, Integer] | None` plus
  precision-type and print-mode options.
  Why it needed scoping: this repeats the unsplit p-adic precision shape for
  fields.
  Source surface used for scoping: the `Qp` p-adic constructor family in
  `rings/docs/SAGE_INVENTORY.md` and Sage p-adic factory docs/source.

- File: `rings/__init__.py:812`
  Symbol: `Rings().Constructors().Zq`
  Original signature: `q: Integer | tuple[Integer, Integer] |
  Sequence[tuple[Integer, Integer]]`, `prec: Integer | tuple[Integer, Integer] |
  None`, plus p-adic options.
  Why it needed scoping: this merges cardinality, prime-power tuple, and sequence
  data in one `q` parameter, and repeats the unsplit precision tuple shape.
  Source surface used for scoping: the `Zq` p-adic extension constructor family in
  `rings/docs/SAGE_INVENTORY.md` and Sage p-adic factory docs/source.

- File: `rings/__init__.py:856`
  Symbol: `Rings().Constructors().Qq`
  Original signature: `q: Integer | tuple[Integer, Integer] |
  Sequence[tuple[Integer, Integer]]`, `prec: Integer | tuple[Integer, Integer] |
  None`, plus p-adic options.
  Why it needed scoping: this repeats the unsplit p-adic extension and precision
  tuple shapes for fields.
  Source surface used for scoping: the `Qq` p-adic extension constructor family in
  `rings/docs/SAGE_INVENTORY.md` and Sage p-adic factory docs/source.

- File: `rings/__init__.py:1046`
  Symbol: `Rings().Constructors().PowerSeriesRing`
  Original signature: `name`, `arg2: Integer | str | None`, `names`,
  `num_gens`, and related series options.
  Why it needed scoping: `arg2` is positional Sage factory plumbing and should be
  replaced by named closed overload cases.
  Source surface used for scoping: the `PowerSeriesRing` constructor family in
  `rings/docs/SAGE_INVENTORY.md` and Sage series-ring factory docs/source.

- File: `rings/__init__.py:1074`
  Symbol: `Rings().Constructors().LaurentSeriesRing`
  Original signature: `name`, `arg2: Integer | str | None`, `names`,
  `num_gens`, and related series options.
  Why it needed scoping: `arg2` is positional Sage factory plumbing and should be
  replaced by named closed overload cases.
  Source surface used for scoping: the `LaurentSeriesRing` constructor family in
  `rings/docs/SAGE_INVENTORY.md` and Sage series-ring factory docs/source.

- File: `rings/__init__.py:1102`
  Symbol: `Rings().Constructors().PuiseuxSeriesRing`
  Original signature: `name`, `arg2: Integer | str | None`, `names`,
  `num_gens`, and related series options.
  Why it needed scoping: `arg2` is positional Sage factory plumbing and should be
  replaced by named closed overload cases.
  Source surface used for scoping: the `PuiseuxSeriesRing` constructor family in
  `rings/docs/SAGE_INVENTORY.md` and Sage series-ring factory docs/source.

- File: `rings/matrix_algebras.py:84`
  Symbol: `_MatrixAlgebras.ParentMethods.matrix`
  Original signature: `x: Matrix | RingElement | Sequence[RingElement] |
  Sequence[Sequence[RingElement]] | None`.
  Why it needed scoping: the element constructor still accepts scalar, flat
  coordinate, nested coordinate, existing-matrix, and empty/default cases in one
  method.
  Source surface used for scoping: Sage `MatrixSpace` / `MatrixRing` element
  construction docs/source and the local matrix-ring mapping.

- File: `rings/subcategories/number_field.py:170`
  Symbol: `_NumberFields.ParentMethods.discriminant`
  Original signature: `v: Sequence[RingElement] | None = None`.
  Why it needed scoping: optional basis data changes the meaning from field
  discriminant to discriminant of supplied elements.
  Source surface used for scoping: Sage number-field discriminant docs/source.

- File: `rings/subcategories/number_field.py:197`
  Symbol: `_NumberFields.ParentMethods.integral_basis`
  Original signature: `v: RingElement | Sequence[RingElement] | None = None`.
  Why it needed scoping: one parameter merges default integral basis, one element,
  and a finite element list.
  Source surface used for scoping: Sage number-field integral-basis docs/source.

- File: `rings/subcategories/number_field.py:249`
  Symbol: `_NumberFields.ParentMethods.ring_of_integers`
  Original signature: `v: Integer | Sequence[Integer] | None = None`.
  Why it needed scoping: one optional parameter merges default construction,
  algorithm/control integer, and sequence data.
  Source surface used for scoping: Sage number-field order docs/source.

- File: `rings/subcategories/number_field.py:256`
  Symbol: `_NumberFields.ParentMethods.maximal_order`
  Original signature: `v: Integer | Sequence[Integer] | None = None`.
  Why it needed scoping: one optional parameter merges default construction,
  algorithm/control integer, and sequence data.
  Source surface used for scoping: Sage maximal-order docs/source.

- File: `rings/subcategories/rational_field.py:190`
  Symbol: `_QQ.ParentMethods.discriminant`
  Original signature: `v: Sequence[RingElement] | None = None`.
  Why it needed scoping: this override forwards the unsplit number-field
  discriminant surface through `as_number_field()`.
  Source surface used for scoping: scope with `_NumberFields.ParentMethods.discriminant`.

- File: `rings/subcategories/rational_field.py:233`
  Symbol: `_QQ.ParentMethods.integral_basis`
  Original signature: `v: RingElement | Sequence[RingElement] | None = None`.
  Why it needed scoping: this override forwards the unsplit number-field
  integral-basis surface through `as_number_field()`.
  Source surface used for scoping: scope with `_NumberFields.ParentMethods.integral_basis`.

- File: `rings/subcategories/rational_field.py:317`
  Symbol: `_QQ.ParentMethods.ring_of_integers`
  Original signature: `v: Integer | Sequence[Integer] | None = None`.
  Why it needed scoping: this override forwards the unsplit number-field order
  surface through `as_number_field()`.
  Source surface used for scoping: scope with `_NumberFields.ParentMethods.ring_of_integers`.

- File: `rings/subcategories/rational_field.py:326`
  Symbol: `_QQ.ParentMethods.maximal_order`
  Original signature: `v: Integer | Sequence[Integer] | None = None`.
  Why it needed scoping: this override forwards the unsplit number-field order
  surface through `as_number_field()`.
  Source surface used for scoping: scope with `_NumberFields.ParentMethods.maximal_order`.

- File: `tensor_algebra_components/__init__.py:176`
  Symbol: `TensorAlgebraComponents(R).Constructors().from_components`
  Original signature: `components: Matrix | Sequence[RingElement] |
  Sequence[Sequence[RingElement]] | Sequence[Sequence[Sequence[RingElement]]] |
  Sequence[Matrix]`.
  Why it needed scoping: this public constructor still accepts all component
  coordinate shapes in one method, even though named tensor constructors already
  exist for matrices, module-element matrices, multidimensional lists, and
  lists of matrices.
  Source surface used for scoping: `tensor_algebra_components/docs/SAGE_INVENTORY.md`
  records component assignment `t[:] = ...` and matrix/list interop.

## Private Or Closed Surfaces Reviewed

- File: `posets/__init__.py:249`
  Symbol: `Posets().Constructors()._raw_poset`
  Original signature: `data: Any` plus Sage `Poset` option keywords.
  Why reviewed: it is a private helper that centralizes Sage's variadic
  `Poset(data=None, ...)` dispatch. The public constructors around it are
  already split into named finite cases in `posets/docs/MAPPING.md`.
  Follow-up condition: keep this private; do not expose `data` as a public
  constructor surface.

- File: `sets/subcategories/finite_set_maps.py:75`
  Symbol: `_FiniteSetMapsSets.ParentMethods._element_constructor_`
  Original signature: closed implementation signature
  `data: FiniteSetMap | Callable[[SetElement], SetElement] |
  Sequence[SetElement]` after three explicit overload declarations.
  Why reviewed: the final abstract signature is broad, but the overloads
  enumerate the admissible cases. This is the AGENTS.md closed-overload pattern,
  not an unscoped variadic public constructor.
  Follow-up condition: do not replace the overloads with a catch-all body.

- File: `sets/__init__.py:513`
  Symbol: `Sets().Constructors().RealSet`
  Original signature: `intervals: Sequence[RealInterval]`.
  Why reviewed: it routes to Sage `RealSet(*tuple(intervals))`, but the public
  input is a typed finite union of interval objects. The catch-all
  `RealSet(*args)` is already rejected in `topological_spaces/docs/MAPPING.md`.
  Follow-up condition: keep arbitrary symbolic/manifold `RealSet(...)` inputs
  out of this constructor.

## Inventoried Sage Variadics Scoped Or Mapped

- File: `algebras/docs/SAGE_INVENTORY.md`
  Sage surface: `sage.categories.algebra_functor.AlgebrasCategory(category, *args)`.
  Mapping status before this pass: source-category algebra construction maps through
  `Algebras(R).Constructors().free_algebra_from_*`.
  Scoping result: source-category subtrees must expose only the admitted
  `S.free_algebra(R)` methods when those categories exist.

- File: `algebras/docs/SAGE_INVENTORY.md`
  Sage surface: `Sets.ParentMethods.algebra(base_ring, category=None, **kwds)`.
  Mapping status before this pass: plain sets route to `S.free_module(R)`; structured
  source categories route to explicit free-algebra constructors.
  Scoping result: no project API should expose the Sage `category=` or `**kwds`
  path.

- File: `algebras/docs/SAGE_INVENTORY.md`
  Sage surface: `CombinatorialFreeModule(..., **kwds)`.
  Mapping status before this pass: constructor ownership lives in
  `Modules(R).Constructors().CombinatorialFreeModule`.
  Scoping result: the mathematical constructor data is the base ring, basis-key
  set, optional element class, optional category refinement, prefix, and names.
  Sage's remaining keyword bag is display/provenance plumbing for
  `IndexedGenerators` (`bracket`, `latex_bracket`, `latex_names`, ordering aliases,
  `key`, and related print options). It is intentionally not a project category
  constructor surface; display behavior is recovered through the constructed Sage
  parent and its `print_options(...)` API, while mathematical basis/order behavior
  is mapped in `modules/docs/MAPPING.md`.

- File: `algebras/docs/SAGE_INVENTORY.md`
  Sage surfaces: `subalgebra(gens, category=None, *args, **opts)`,
  `ideal_submodule(gens, side='left', category=None, *args, **opts)`, and
  `principal_ideal(a, side='left', *args, **opts)`.
  Mapping status before this pass: algebra subobjects and algebra ideals are mapped, but
  the extra Sage option bags have not been split.
  Scoping result: finite-dimensional algebra source dispatches only through the
  generator data, optional category refinement, and the finite `side` choices
  `left`, `right`, and `twosided`. The public project surface keeps
  `subalgebra(generators)` and splits ideals into `left_ideal`, `right_ideal`,
  `two_sided_ideal`, `principal_left_ideal`, `principal_right_ideal`, and
  `principal_two_sided_ideal`; category and option bags remain Sage
  implementation plumbing.

- File: `lattices/docs/SAGE_INVENTORY.md`
  Sage surface: `short_vectors(self, n, **kwargs)`.
  Mapping status before this pass: inventoried only.
  Scoping result: Sage forwards only `up_to_sign_flag` to the quadratic-form
  enumerator in the installed source. The project surface keeps
  `short_vectors(bound)` and adds the named `short_vectors_up_to_sign(bound)`;
  other keyword forwarding is not public.

- File: `posets/docs/SAGE_INVENTORY.md`
  Sage surfaces: `MeetSemilattice(data=None, *args, **options)`,
  `JoinSemilattice(data=None, *args, **options)`, and
  `LatticePoset(data=None, *args, **options)`.
  Mapping status before this pass: already split into named constructor families in
  `posets/docs/MAPPING.md`.
  Scoping result: no additional public variadic surface remains. Sage's finite
  constructor shapes are already mapped to named `Posets().Constructors()` methods
  and meet/join/lattice refinement methods; the private `_raw_poset(data, ...)`
  bridge stays private.

- File: `sets/docs/MAPPING.md`
  Sage surface: `EnumeratedSetFromIterator(f, args=..., kwds=...)`.
  Mapping status before this pass: public constructor admits a nullary
  `iterator_factory` and omits arbitrary callable plumbing.
  Scoping result: preserve old functionality through wrapper factories in
  migration docs or regression tests without exposing `args`/`kwds`.

- File: `sets/docs/MAPPING.md`
  Sage surface:
  `Sets.ParentMethods._element_constructor_from_element_class(*args, **keywords)`.
  Mapping status before this pass: omitted as Sage element-class forwarding.
  Scoping result: keep it out of category specs unless a concrete mathematical
  element constructor is named.

- File: `topological_spaces/docs/SAGE_INVENTORY.md`
  Sage surfaces: `RealSet(*args)` and named `RealSet` constructors with
  `**kwds`.
  Mapping status before this pass: mapped to named `Sets().Constructors()` real-line
  subset constructors, with manifold-producing keyword paths rejected from the
  pure topological-space subtree.
  Scoping result: keep the named interval/ray constructors as the only admitted
  pure real-subset paths and avoid reintroducing a catch-all `RealSet(...)`.
