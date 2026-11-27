---
id: TASK-QC-GENERATE-TYPE-STUBS
trackerStatus:
  type: task
parents:
- '[[PHASE-QC-STUB-GENERATION]]'
dependsOn:
- '[[TASK-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW]]'
title: Generate or repair static type stubs
status: unstarted
priority: high
description: 'Create or repair Sage/pytest/category static type surfaces after basic hygiene
  and dynamic-inheritance plugin review are complete.

  '
activityType: implementation
workstreamRole: implementation
claimStatus: unexamined
uncertaintyState: ordinary-open
successCriteria:
- Stub-generation candidates are drawn from post-plugin mypy output, not pre-plugin aggregate noise.
- Sage, pytest, .pyi, TypeAlias, and generated category-surface needs are separated by source path.
- Generated or handwritten stubs are validated through `just test` or a documented focused equivalent.
- No plugin/base-injection failure is hidden by a stub.
complexity: 55
tags:
- FEATURE-QC-WARNINGS-ZERO
- PLAN-QC-MYPY-FOUNDATION-ORDER
- PHASE-QC-STUB-GENERATION
---
# Task: Generate or Repair Static Type Stubs

## Summary

Create or repair static type surfaces only after the basic hygiene and
dynamic-inheritance plugin frontiers are complete. This includes Sage/pytest
stubs, `.pyi` files, `TypeAlias` intermediaries, and generated representations
of category method surfaces.

## Source Provenance

- `FEATURE-QC-WARNINGS-ZERO`, valid-type and missing-stub sections.
- `SPEC-SAGE-MYPY-CATEGORY-OVERRIDE`, which makes stub generation out of scope
  for the plugin.
- `PLAN-QC-MYPY-FOUNDATION-ORDER`.

## Context

Pre-plugin aggregate mypy output cannot be used as the stub queue. Stub work
starts from post-basic, post-plugin evidence so it does not mask ordinary type
hygiene or dynamic-inheritance failures.

## Acceptance Criteria

- Stub candidates are listed by path and error shape.
- The plan distinguishes external dependency stubs from repo-generated category
  static surfaces.
- Validation proves the stubs resolve the targeted errors without suppressions.

## Dependencies And Boundaries

Depends on `TASK-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW`. This task does not own
missing annotations, `Any` hygiene, or plugin base injection.

## Work Log

- Created 2026-05-13 as the explicit stub-generation task tree.
- 2026-05-23 blocker-forensics classification: refreshed
  `category_specs` ordinary mypy frontier has 1791 ordinary diagnostics on
  `sagemath-mypy-plugin` `c231ac89da769434380dd95e499f5b64680636ae` and
  `sage-stubs` `72e6cf8b2bf131df5cb44ae1713e304a4a5f7a67`; full structural
  projection check reports zero graph-absent providers, zero missing TypeInfos,
  zero projected-ancestor gaps, and zero mismatched providers. The families
  below are the full current evidence-backed `sage-stubs`-owned external
  subset. Plugin-owned blockers are recorded in
  `TASK-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW`; research-owned,
  mathematical/spec-decision, and stale/non-external blockers are recorded in
  `TASK-QC-DOWNSTREAM-TYPE-CLEANUP`.

  - `STUB-LAZYIMPORT-CALLABLE`: exact selector is any current diagnostic whose
    message contains `LazyImport`, covering 208 rows: 206 `"LazyImport" not
    callable` operator rows plus assignment rows at
    `category_specs/homsets/homsets.py:122` and
    `category_specs/cat/__init__.py:314` where a `LazyImport` is assigned to a
    `Callable[[], Category]` provider slot. Inspected Sage source
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/misc/lazy_import.pyx:400`
    defines `LazyImport.__call__`, and Sage runtime confirms
    `callable(LazyImport('sage.categories.sets_cat', 'Sets'))` and calling it
    both succeed. Owner is `sage-stubs`: current
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-stubs/misc/lazy_import.pyi`
    exposes only `__init__`, so the real callable Sage surface is absent from
    the stub. Required work is to type `LazyImport` as callable with a return
    type precise enough for factory/category use. Acceptance is that these 208
    rows disappear without local suppressions or consumer-specific special
    cases. Falsifier would be evidence that a covered row uses a non-Sage local
    object or that current Sage `LazyImport` is not callable.

  - `STUB-RECURSIVELY-ENUMERATED-EXPORTS`: exact selector is current diagnostics
    mentioning `sage.sets.recursively_enumerated_set` missing
    `RecursivelyEnumeratedSet` or `RecursivelyEnumeratedSet_generic`, covering
    `category_specs/sets/__init__.py:907` and
    `category_specs/sets/subcategories/recursively_enumerated.py:19`. Sage
    source provides
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/sets/recursively_enumerated_set.pyx`,
    and Sage runtime imports both names. Owner is `sage-stubs`: current
    `sage-stubs/sets/recursively_enumerated_set.pyi` exposes only
    `RecursivelyEnumeratedSet_forest`. Required work is to expose the two real
    top-level Sage names. Acceptance is that the two `attr-defined` rows
    disappear. Falsifier would be current Sage no longer exporting those names.

  - `STUB-SUBSETS-INTEGER-K`: exact selector is the row
    `category_specs/sets/__init__.py:304` where argument 2 to `Subsets` is
    `Integer` but the stub accepts only `int | None`. The research source passes
    a Sage `Integer | None` size into `sage.combinat.subset.Subsets`. Sage source
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/combinat/subset.py:49`
    defines `Subsets(s, k=None, ...)`, and lines 152 and 601 coerce `k` through
    `Integer(k)`; Sage runtime accepts `Subsets([1, 2, 3], Integer(2))`. Owner
    is `sage-stubs`: current `sage-stubs/combinat/subset.pyi` narrows `k` to
    `int | None`. Required work is to include Sage `Integer` in the accepted
    constructor surface without treating `int` and `Integer` as interchangeable.
    Acceptance is that this row disappears. Falsifier would be current Sage
    rejecting Sage `Integer` for `k`.

  - `STUB-ABSTRACTFAMILY-KEYS`: exact stub-owned selector is the
    `AbstractFamily` half of the current `.keys()` diagnostics at
    `category_specs/modules/subcategories/with_basis.py:66` and the
    `Item "AbstractFamily" ... has no attribute "keys"` row at line 186. The
    companion `Item "Sequence[_RModElements]" ... has no attribute "keys"` row
    at line 186 is not covered by this family and remains local narrowing/design
    work. Sage source
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/sets/family.pyx`
    implements family objects, and Sage runtime confirms
    `Family({1: 'a'}).keys()` works on an `AbstractFamily`. Owner is
    `sage-stubs`: current `sage-stubs/sets/family.pyi` leaves `AbstractFamily`
    empty. Required work is to expose `keys` on the real family surface.
    Acceptance is that the two `AbstractFamily.keys` rows disappear while the
    Sequence branch is addressed separately. Falsifier would be evidence that
    the covered object is not a Sage `AbstractFamily` at runtime.

  - `STUB-CATEGORY-JOIN-MEET-AND`: exact stub-owned selector covers
    `category_specs/cat/base_category_types.py:602` and `:604`,
    `category_specs/cat/__init__.py:250`, `:252`, `:255`, and `:265`, where
    `Category.join` or `Category.meet` receives an iterable/tuple of category
    objects but the stub supertype expects `list[Category]`, plus
    `category_specs/sets/__init__.py:986`, where `Category & Category` is
    rejected. It covers seven rows. It excludes
    `category_specs/homsets/homsets.py:162`, whose expected type involves the
    local research `Category` wrapper and is not proven stub-owned. Sage source
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/categories/category.py:2298`
    defines `__and__`, line 1977 defines `meet(categories)`, and line 2329
    defines `join(categories, ...)`; Sage runtime via `sage -c` accepts
    `Category.join((Sets(), Sets().Finite()))`,
    `Category.meet((Sets(), Sets().Finite()))`, and `Sets() & Sets().Finite()`.
    Owner is `sage-stubs`: current `sage-stubs/categories/category.pyi` types
    `join` and `meet` as `list[Category]` and omits `__and__`. Required work is
    to type the real iterable join/meet and category operator surface.
    Acceptance is that the seven covered rows disappear without broadening local
    wrapper semantics. Falsifier would be evidence that Sage only accepts lists,
    lacks `Category.__and__`, or that one of the covered rows is caused by the
    research-local `Category` wrapper rather than the Sage supertype surface.

  - `STUB-CATEGORY-TYPES-BASE-OBJECTS`: exact selector covers
    `category_specs/cat/base_category_types.py:730`, `:738`, `:746`, and `:754`,
    where local category wrappers pass a `CategoryObject` into Sage
    `Category_over_base`, `Category_over_base_ring`, or `Category_in_ambient`
    initializers, but current stubs require `Category | Parent` or `Parent`.
    Sage source
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/categories/category_types.py:153`
    documents `base` as a category or an object of such a category, line 172
    defines `Category_over_base.__init__(self, base, name=None)`, line 348
    defines `Category_over_base_ring.__init__(self, base, name=None)`, and line
    535 defines `Category_in_ambient.__init__(self, ambient, name=None)`.
    Owner is `sage-stubs`: current `sage-stubs/categories/category_types.pyi`
    narrows these public constructor parameters to `Category | Parent` or
    `Parent`, excluding ordinary Sage category objects. Required work is to type
    the source-documented category-or-object constructor surface without
    weakening the local wrapper relationship. Acceptance is that these four rows
    disappear. Falsifier would be evidence that the local argument is not a real
    Sage category object or that Sage source imposes a stricter public
    constructor type than the docs/source signature indicate.

  - `STUB-COMBINATORIAL-FREE-MODULE-CONSTRUCTOR`: exact selector covers the
    three diagnostics at `category_specs/modules/__init__.py:926` for unexpected
    `element_class`, unexpected `prefix`, and multiple values for `category` on
    `CombinatorialFreeModule`. Sage source
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/combinat/free_module.py:373`
    defines `__init__(self, R, basis_keys=None, element_class=None,
    category=None, prefix=None, names=None, **kwds)`, and line 273 defines the
    matching classcall surface. Sage runtime accepts these keyword arguments
    when the category is a module-with-basis category. Owner is `sage-stubs`:
    current `sage-stubs/combinat/free_module.pyi` has no constructor/classcall
    surface for these keywords. Required work is to expose the source-backed
    constructor/classcall signature. Acceptance is that these three rows
    disappear. Falsifier would be evidence that the research call passes a
    category outside the Sage constructor contract rather than hitting a missing
    stub surface.

  - `STUB-MATRIXSPACE-IMPLEMENTATION`: exact selector is
    `category_specs/rings/__init__.py:1954`, where `implementation` is
    `str | type[Matrix] | None` but current stubs expect only `type`. Sage
    source
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/matrix/matrix_space.py:663`
    accepts `implementation=None` in `__classcall__`, documentation at lines
    444-445 says it may be a string or matrix class, and Sage runtime accepts
    `MatrixSpace(ZZ, Integer(2), Integer(2), implementation='generic')`. Owner
    is `sage-stubs`: current `sage-stubs/matrix/matrix_space.pyi` narrows the
    instance initializer to `implementation: type`. Required work is to model
    the public classcall/constructor boundary without weakening the internal
    post-selection implementation class invariant. Acceptance is that this row
    disappears. Falsifier would be evidence that the row targets the internal
    initialized object signature rather than the public constructor boundary.

  - `STUB-POSETS-PARENTMETHODS-ORDER`: exact selector is the eight missing-base
    override rows in `category_specs/posets/__init__.py:88-134` for `le`, `lt`,
    `ge`, `gt`, `upper_covers`, `lower_covers`, `order_ideal`, and
    `order_filter`. Sage source
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/categories/posets.py:160-290`
    defines these methods on `Posets.ParentMethods`. Owner is `sage-stubs`:
    current `sage-stubs/categories/posets.pyi` omits these real provider methods
    from `ParentMethods`, while the refreshed structural projection report shows
    no missing provider graph edge. Required work is to expose the real provider
    methods in the stub. Acceptance is that the eight override rows disappear.
    Falsifier would be evidence that mypy is missing the provider base despite
    the stub method being present.

  - `STUB-INTEGER-CONSTRUCTOR-AND-PROTOCOL`: exact stub-owned selector covers
    the 17 rows whose message is exactly `Too many arguments for "Integer"`,
    plus these nine current operator rows:
    `category_specs/modules/__init__.py:250` (`int <= Integer`),
    `category_specs/modules/__init__.py:251` (`Integer * list[_RModObjects]`),
    `category_specs/modules/__init__.py:252` (`int >= Integer`),
    `category_specs/modules/__init__.py:253` (`-Integer`),
    `category_specs/modules/__init__.py:259` (`int <= Integer`),
    `category_specs/modules/__init__.py:1496` (`Integer * list[ParentMethods]`),
    `category_specs/rings/matrix_algebras.py:154` (`Integer * ...`),
    `category_specs/tensor_algebra_components/__init__.py:243` (`int <= Integer`),
    and `category_specs/lattices/subcategories/over_dedekind.py:122`
    (`Integer - ...`). This family therefore covers 26 rows. It does not cover
    Python builtins rows such as `range(Integer)` or
    `int(Integer | InfinityElement)`, which require separate local narrowing or
    return-type decisions. Sage source
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/rings/integer.pyx:498`
    defines `Integer(x=None, base=0)`, line 791 defines `__index__`, line 1955
    defines `__neg__`, line 2016 defines multiplication, and line 3684 defines
    `__int__`; Sage runtime confirms `Integer('10', 10)`, `-Integer(3)`,
    `int(4) <= Integer(5)`, and `Integer(2) * ['x']`. Owner is `sage-stubs`:
    current `sage-stubs/rings/integer.pyi` lacks the constructor and operator
    protocol. Required work is to add source-backed constructor and numeric
    protocol methods without collapsing Sage `Integer` into Python `int` or
    replacing domain types with opacity. Acceptance is that the covered
    constructor/protocol rows disappear while Python-builtin coercion rows stay
    separately owned. Falsifier would be evidence that a covered row depends on
    Sage preparser behavior or local code should normalize before the call.

  - `STUB-MATRIX-CONSTRUCTOR-AND-BASE-TYPE`: exact stub-owned selector covers
    30 current `arg-type` rows involving the real Sage matrix constructor/base
    type: rows `676`, `687`, `688`, `689`, `690`, `691`, `692`, `693`, `696`,
    `706`, `707`, `708`, `709`, `710`, `711`, `712`, `715`, `716`, `717`,
    `718`, `719`, `720`, `721`, `749`, `750`, `753`, `754`, `933`, `934`,
    and `1207`. These are rows where `matrix` rejects row-sequence entries
    because the stub treats argument 2 as only `int | None`, rows where
    `matrix` rejects Sage `Integer` row/column dimensions, and rows where
    values from `sage.matrix.constructor.matrix` are typed as
    `sage.matrix.matrix.Matrix` while local and Sage APIs expect
    `sage.matrix.matrix2.Matrix`. Representative
    rows are `category_specs/modules/__init__.py:737`, `:754`, `:823`, `:840`,
    `:878`, `:892`, `:1092`, `:1130`,
    `category_specs/algebras/__init__.py:608` and `:610`, and
    `category_specs/tensor_algebra_components/__init__.py:148`. Sage source
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/matrix/constructor.pyx:20`
    defines `matrix(*args, **kwds)` and documents row-list entries, optional
    ring, dimensions, dictionary/callable entries, and keyword forms; Sage
    runtime confirms `matrix(ZZ, [[1, 0], [0, 1]])` returns
    `sage.matrix.matrix_integer_dense.Matrix_integer_dense`, and importing
    `sage.matrix.matrix.Matrix` fails while `sage.matrix.matrix2.Matrix` is the
    matrix base used by the research type surface. Owner is `sage-stubs`: the
    current `sage-stubs/matrix/constructor.pyi` narrows `matrix` to
    `def matrix(ring: Ring | None, nrows: int | None, ncols: int | None,
    entries: object) -> sage.matrix.matrix.Matrix`, which excludes supported
    row-sequence and Sage `Integer` dimension forms and returns a non-runtime
    base module. Required work is to type the real public constructor overloads
    and use the runtime-backed matrix base consistently. Acceptance is that the
    30 covered rows disappear without weakening local ring-object contracts.
    Falsifier would be evidence that a covered row depends on local
    `_RingObjectMethods` being a Sage ring rather than on the constructor shape
    or matrix base-type mismatch.

  - `STUB-FREEMODULE-VECTORSPACE-CONSTRUCTORS`: exact stub-owned selector covers
    six current rows in `category_specs/modules/__init__.py`: `FreeModule` and
    `VectorSpace` reject Sage `Integer` ranks/dimensions at lines `:683`,
    `:719`, `:772`, and `:805`, and reject `with_basis=None` at lines `:719`
    and `:805`. Sage source
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/modules/free_module.py:231`
    coerces `rank` through `sage.rings.integer.Integer(rank)`, line 310 defines
    `FreeModule(base_ring, rank_or_basis_keys=None, sparse=False,
    inner_product_matrix=None, *, with_basis='standard', rank=None,
    basis_keys=None, **args)`, and the `FreeModule` docs explicitly allow
    `with_basis=None`; `VectorSpace` delegates to `FreeModule` with the same
    `with_basis` option around lines 594-612. Sage runtime confirms
    `FreeModule(ZZ, Integer(2))`, `FreeModule(ZZ, Integer(2),
    with_basis=None)`, `VectorSpace(QQ, Integer(2))`, and
    `VectorSpace(QQ, Integer(2), with_basis=None)` all succeed. Owner is
    `sage-stubs`: current `sage-stubs/modules/free_module.pyi` restricts the
    rank/dimension forms to Python `int | Iterable[object] | None` and
    `with_basis` to `str`. Required work is to expose Sage `Integer` and
    `with_basis=None` on the public constructors while preserving the field
    requirement for `VectorSpace`. Acceptance is that these six rows disappear.
    Falsifier would be evidence that any covered call is invalid because its
    first argument is not a Sage ring/field rather than because of rank or
    `with_basis` typing.

  - `STUB-CONDITIONSET-UNIVERSE-PREDICATES`: exact stub-owned selector covers
    four current rows where `sage.sets.condition_set.ConditionSet` rejects
    project universe/predicate types:
    `category_specs/homsets/autsets.py:46` and `:47`, and
    `category_specs/sets/subcategories/condition.py:31` twice. Sage source
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/sets/condition_set.py:132`
    defines `__classcall_private__(cls, universe, *predicates, vars=None,
    names=None, category=None)`, line 200 defines `__init__(self, universe,
    *predicates, names=None, category=None)`, and lines 205-209 only use a
    parent facade when `universe` is a `Parent`; non-`Parent` universes are still
    accepted. Runtime confirms `ConditionSet((1, 2, 3), lambda x: x != 2)`
    works. Owner is `sage-stubs`: current
    `sage-stubs/sets/condition_set.pyi` narrows the public constructor to
    `ambient: Parent` and `Callable[[Element], bool] | Expression`, but Sage
    accepts a general hashable universe and predicates over that universe.
    Required work is to type the real public constructor/classcall surface
    without pretending every universe is a `Parent` or every predicate is over
    Sage `Element`. Acceptance is that these four rows disappear while
    retaining precise overloads for the common `Parent`/`Element` case.
    Falsifier would be evidence that a covered universe is invalid at Sage
    runtime, or that the public constructor is intentionally limited to
    `Parent` despite the current source and runtime behavior.

  - `STUB-MATRIXSPACE-MATRIX-SPACE-INTEGER-DIMS`: exact selector covers four
    current rows: `category_specs/rings/matrix_algebras.py:216` rejects
    `nrows: Integer | None` and `ncols: Integer | None`, and
    `category_specs/rings/__init__.py:1954` rejects Sage `Integer` matrix-space
    dimensions for the public `MatrixSpace(...)` constructor. The row indices
    are `984`, `985`, `1066`, and `1067`.
    Sage source
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/matrix/matrix_space.py:2314`
    defines `matrix_space(self, nrows=None, ncols=None, sparse=False)` and
    delegates to `MatrixSpace(base, nrows, ncols, sparse=sparse)`; Sage runtime
    confirms `MatrixSpace(ZZ, 2).matrix_space(nrows=Integer(2),
    ncols=Integer(2))` succeeds. Owner is `sage-stubs`: current
    `sage-stubs/matrix/matrix_space.pyi` narrows these dimension parameters to
    Python `int | None`, while the public method accepts Sage `Integer` through
    the same constructor-normalization path as `MatrixSpace`. Required work is
    to include Sage `Integer` for these public dimension parameters without
    treating all `Integer`/`int` boundaries as interchangeable. Acceptance is
    that the four dimension rows disappear. Falsifier would be current
    Sage runtime rejecting Sage `Integer` dimensions for `matrix_space`.

  - `STUB-FINITEPOSETS-SEMILATTICE-AND-CERTIFICATES`: exact selector covers
    eight current rows involving `sage.combinat.posets.posets.FinitePoset`:
    four rows in `category_specs/posets/__init__.py:348`, `:367`, `:382`, and
    `:385` where `FinitePoset` lacks `is_meet_semilattice` or
    `is_join_semilattice`; two rows in
    `category_specs/posets/subcategories/finite.py:200` and `:217` where
    `type[FinitePoset]` lacks the same methods for unbound delegation; and two
    rows at `finite.py:144` and `:157` where `height` and `width` reject the
    `certificate` keyword. Sage source
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/combinat/posets/posets.py:3193`
    defines `height(self, certificate=False)`, line `:4541` defines
    `is_meet_semilattice(self, certificate=False)`, line `:4614` defines
    `is_join_semilattice(self, certificate=False)`, and line `:4880` defines
    `width(self, certificate=False)`. Sage runtime confirms these methods exist
    and `height(certificate=True)` / `width(certificate=True)` return
    certificate pairs. Owner is `sage-stubs`: current
    `sage-stubs/combinat/posets/posets.pyi` omits the semilattice predicates
    and narrows `height`/`width` to no-certificate signatures. Required work is
    to expose these real `FinitePoset` methods with certificate-aware overloads
    or unions. Acceptance is that these eight rows disappear. Falsifier would be
    current Sage source/runtime lacking these methods or rejecting the
    `certificate` keyword.

  - `STUB-INFINITY-NEGATION`: exact selector covers the three current unary
    minus rows for `PlusInfinity` at `category_specs/sets/__init__.py:848`,
    `:858`, and `:888`. Sage source
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/rings/infinity.py:1673`
    defines `PlusInfinity._neg_`, and line `:1563` defines the corresponding
    `MinusInfinity._neg_`; Sage runtime confirms `-infinity` returns a
    `MinusInfinity` and `-minus_infinity` returns a `PlusInfinity`. Owner is
    `sage-stubs`: current `sage-stubs/rings/infinity.pyi` defines
    `PlusInfinity` and `MinusInfinity` but omits the negation operator surface.
    Required work is to type unary negation precisely between the two infinity
    singleton classes. Acceptance is that these three operator rows disappear.
    Falsifier would be current Sage source/runtime lacking the negation
    behavior or returning a different public infinity type.

  - `STUB-SETPARTITION-DIRECT-CLASSCALL`: exact selector covers the two current
    rows at `category_specs/sets/__init__.py:1225` where direct
    `SetPartition(blocks, check=check)` construction is checked against
    `SetPartition.__init__(parent, s, check)` and therefore reports both a
    missing positional argument `s` and an incompatible first argument expected
    to be `Parent`. Sage source
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/combinat/set_partition.py:539`
    defines `class SetPartition(..., metaclass=InheritComparisonClasscallMetaclass)`,
    lines `:602-611` define `__classcall_private__(cls, parts, check=True)`,
    and the class docstring explicitly documents direct `SetPartition([[1,3],
    [2,4]])` construction. Sage runtime confirms
    `SetPartition([[1, 2], [3]], check=True)` returns a
    `sage.combinat.set_partition.SetPartitions_all_with_category.element_class`.
    Owner is `sage-stubs`: the public Sage classcall surface accepts the direct
    block iterable, while the static constructor surface falls through to the
    internal `__init__(parent, s, check)` shape. Required work is to expose the
    direct classcall/constructor behavior precisely, without deleting the
    internal initializer shape and without using `Any` or broad `object`
    opacity for the block elements. Acceptance is that both line `:1225` rows
    disappear. Falsifier would be current Sage runtime rejecting direct
    `SetPartition(parts, check=...)`, or evidence that the research call is not
    using the public Sage `SetPartition` class.

  - `STUB-RATIONALFIELD-MISSING-PUBLIC-METHODS`: exact selector covers ten
    current missing-base override rows in
    `category_specs/rings/subcategories/rational_field.py` for methods that
    exist on Sage `QQ`/`RationalField` at runtime but are absent from the
    current `sage-stubs/rings/rational_field.pyi`: `algebraic_closure` at line
    `:80`, `degree` at `:106`, `absolute_degree` at `:111`,
    `absolute_discriminant` at `:139`, `automorphisms` at `:179`,
    `class_group` at `:189`, `power_basis` at `:217`, `places` at `:232`,
    `ring_of_integers` at `:302`, and `maximal_order` at `:340`. Sage source
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/rings/rational_field.py`
    defines `algebraic_closure` at line `1073`, `degree` at `939`,
    `absolute_degree` at `950`, `absolute_discriminant` at `552`,
    `automorphisms` at `623`, `power_basis` at `1034`, `places` at `638`, and
    `maximal_order` at `1007`; runtime confirms all ten names are present on
    `sage.all.QQ`, with `class_group` provided through
    `PrincipalIdealDomains.ParentMethods` and `ring_of_integers` through the
    number-field parent surface. The current RationalField stub only exposes
    `discriminant`, `class_number`, `signature`, and unrelated basic field
    methods from this family. Owner is `sage-stubs`: these are real Sage
    public surfaces missing from the static QQ/RationalField surface needed by
    provider override checking. Required work is to add source-backed,
    non-opaque signatures for these RationalField methods without inventing the
    methods that runtime lacks. Acceptance is that these ten rows no longer
    fail because the projected QQ parent base lacks the named method. Falsifier
    would be current Sage runtime/source lacking one of these methods on QQ, or
    a row depending instead on a local `category_specs` method with the same
    name.

  - `STUB-REALSET-PARENT-AN-ELEMENT`: exact selector covers the single current
    missing-base override row at `category_specs/sets/subcategories/real_set.py:205`
    for `_RealSets.ParentMethods._an_element_`. Inspected local source places
    the method in the real-subset parent provider at
    `category_specs/sets/subcategories/real_set.py:31-211`; Sage source
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/sets/real_set.py:888`
    defines `class RealSet(..., Parent, ...)`, and line `:2348` defines
    `RealSet._an_element_`. Runtime via `sage.all.RealSet.open(0, 1)` confirms
    the resulting Sage real set has `_an_element_`. Stub evidence is negative:
    Searched: `find /home/dzack/sage-mypy-plugin/sage-stubs/sage-stubs -path
    '*real*set*.pyi'`, `rg RealSet` under current stubs, and current
    `sage-stubs/sets`.
    Found: no `sage-stubs/sets/real_set.pyi` sidecar; only downstream imports
    of `InternalRealInterval`/`RealSet` through `category_specs/types.py`.
    Conclusion: inference based on current stub tree: the real Sage
    `sage.sets.real_set.RealSet` parent surface is missing from `sage-stubs`,
    so provider override-base checking cannot see `_an_element_`.
    Confidence: High for the missing sidecar and runtime method presence.
    Classification boundary: this family owns the current `_an_element_` row,
    not a full `RealSet` parity pass.
    Owner is `sage-stubs`: this row depends on a real Sage parent method absent
    from the stub package, not on a local `Cat` concept. Required work is to add
    the source-backed `RealSet` parent stub surface at least for `_an_element_`
    and any directly required top-level methods, without broad generated
    opacity. Acceptance is that the line `:205` missing-base override row
    disappears. Falsifier would be evidence that the local `_RealSets` provider
    is not intended to refine Sage `RealSet` parents, or that current Sage
    runtime lacks `RealSet._an_element_`.

  - `STUB-IMAGESUBOBJECT-PARENT-AN-ELEMENT`: exact selector covers the single
    current missing-base override row at `category_specs/sets/subcategories/image.py:116`
    for `_ImageSets.ParentMethods._an_element_`. Inspected local source imports
    `sage.sets.image_set.ImageSubobject` and defines the project wrapper at
    `category_specs/sets/subcategories/image.py:10-43`, then declares the image
    parent provider surface at lines `:45-120`. Sage source
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/sets/image_set.py:28`
    defines `class ImageSubobject(Parent)`, and lines `:272`, `:291`, `:324`,
    `:372`, `:401`, and `:414` define `lift`, `retract`, `cardinality`,
    `__iter__`, `_an_element_`, and `_sympy_`. Runtime confirms an
    `ImageSubobject(lambda x: 2*x, ZZ, inverse=lambda x: x/2)` has
    `_an_element_`. Stub evidence is negative:
    Searched: `find /home/dzack/sage-mypy-plugin/sage-stubs/sage-stubs -path
    '*image_set*.pyi'` and `sage-stubs/sets`.
    Found: no `sage-stubs/sets/image_set.pyi` sidecar.
    Conclusion: inference based on current stub tree: the real Sage
    `sage.sets.image_set.ImageSubobject` parent surface is missing from
    `sage-stubs`, so provider override-base checking cannot see `_an_element_`.
    Confidence: High for missing sidecar and runtime method presence.
    Classification boundary: this family owns the current QC-blocking
    `_an_element_` row, not a full `ImageSubobject` parity pass.
    Owner is `sage-stubs`. Required work is to add source-backed
    `ImageSubobject` stubs for the parent methods currently needed by the
    research provider surface, starting with `_an_element_`, without generated
    `Any`/`object` opacity. Acceptance is that the line `:116` missing-base
    override row disappears. Falsifier would be evidence that the project image
    wrapper is not intended to refine Sage `ImageSubobject` parents, or that
    current Sage runtime lacks `ImageSubobject._an_element_`.

  - `STUB-REAL-ABC-TO-PREC`: exact selector covers the three current
    `union-attr` rows at
    `category_specs/rings/subcategories/real_precision_field.py:81` where
    `_RealPrecisionFields.ParentMethods.change_precision` calls
    `self.to_prec(precision)` after narrowing `self` to
    `sage.rings.abc.RealField | RealDoubleField | RealIntervalField`. Sage
    source defines `to_prec` on the corresponding concrete parents at
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/rings/real_mpfr.pyx:1054`,
    `real_double.pyx:422`, and `real_mpfi.pyx:1054`; current concrete stubs
    expose `to_prec` in `sage-stubs/rings/real_mpfr.pyi`,
    `real_double.pyi`, and `real_mpfi.pyi`. Runtime confirms
    `RealField(53).to_prec(80)`, `RDF.to_prec(80)`, and
    `RealIntervalField(53).to_prec(80)` all succeed. Owner is `sage-stubs`:
    the abstract protocol surface in `sage-stubs/rings/abc.pyi` defines
    `RealField`, `RealDoubleField`, and `RealIntervalField` without the
    `to_prec` method that the concrete Sage classes share. Required work is to
    add source-backed `to_prec` methods to the relevant real-field ABC stubs
    with precise return shapes, not to cast around the union or weaken the
    research type. Acceptance is that the three line `:81` union-attr rows
    disappear. Falsifier would be current Sage runtime/source showing one of
    these ABC classes intentionally excludes `to_prec`, or that the narrowed
    receiver can include another real-field type without this method.

  - `STUB-MATRIXSPACE-PARENT-BASE`: exact selector covers the single current
    type-variable row at `category_specs/rings/__init__.py:1958` where
    `refine_category` rejects a value typed as `MatrixSpace` because
    `_ParentT` is bounded by Sage `Parent`. Sage source
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/matrix/matrix_space.py:426`
    defines `class MatrixSpace(UniqueRepresentation, Parent)`, and runtime
    confirms `isinstance(MatrixSpace(ZZ, 2), sage.structure.parent.Parent)`.
    Current `sage-stubs/matrix/matrix_space.pyi` defines `class MatrixSpace`
    without inheriting from `Parent`. Owner is `sage-stubs`: the real Sage
    parent base is missing from the MatrixSpace stub hierarchy. Required work
    is to preserve the source-backed `MatrixSpace` parent relationship in the
    stub class, without weakening `refine_category`'s `Parent` bound and
    without treating arbitrary non-parent helper protocols as parents.
    Acceptance is that the line `:1958` type-variable row disappears while the
    other non-parent `refine_category` rows remain local unless separately
    proven external. Falsifier would be current Sage source/runtime showing
    MatrixSpace is not a `Parent`.

  - `STUB-SAGE-CATEGORY-MEMBERSHIP-SURFACES`: exact selector covers 23 current
    operator rows whose message starts `Unsupported right operand type for in`
    and whose right-hand side is a Sage category object: `Infinite`,
    `FiniteSets`, `PrincipalIdealDomains` twice, `DedekindDomains` twice,
    `CommutativeRings` twice, `Rings`, `MagmaticAlgebras`, `SubcategoryMethods`,
    `DivisionRings`, `NoetherianRings`, `GcdDomains`, `EuclideanDomains`,
    `DiscreteValuationRings`, `CompleteDiscreteValuationRings`,
    `QuotientFields`, `DiscreteValuationFields`,
    `CompleteDiscreteValuationFields`, `EnumeratedSets`,
    `AlgebrasWithBasis`, and `SemisimpleAlgebras`. Representative inspected
    call sites include `S in SageSets().Infinite()` at
    `category_specs/sets/subcategories/infinite.py:36`,
    `base_ring in SagePrincipalIdealDomains()` at
    `category_specs/modules/__init__.py:504`, and
    `A in SageAlgebrasWithBasis(self.base_ring())` at
    `category_specs/algebras/subcategories/with_basis.py:49`. Runtime confirms
    Sage category membership works for representative categories such as
    `ZZ in PrincipalIdealDomains()`, `ZZ in DedekindDomains()`, `ZZ in
    CommutativeRings()`, and `ZZ in Rings()`. Current stubs define many of
    these category classes as plain classes without inheriting from
    `sage.categories.category.Category` or otherwise exposing `__contains__`;
    examples include `sage-stubs/categories/sets_cat.pyi` where
    `Sets.Infinite` is a plain nested class, and
    `principal_ideal_domains.pyi`, `dedekind_domains.pyi`,
    `commutative_rings.pyi`, `rings.pyi`, `division_rings.pyi`, and
    `algebras_with_basis.pyi` where the category classes do not expose the
    base `Category.__contains__` surface. Owner is `sage-stubs`: these are real
    Sage category membership surfaces missing from category stub inheritance or
    protocols, not local research category-wrapper work. Required work is to
    preserve the source-backed `Category` relationship or a precise
    `__contains__` protocol for these Sage category classes, without adding
    project-specific category aliases or weakening membership operands to
    `Any`. Acceptance is that all 23 covered membership rows disappear.
    Falsifier would be current Sage runtime/source rejecting membership for a
    covered category, or a covered right-hand side being a local
    `category_specs` category rather than a Sage category object.

  - `STUB-TENSORPRODUCTFUNCTOR-CALLABLE`: exact selector covers the three
    current operator rows reporting `"TensorProductFunctor" not callable` at
    `category_specs/modules/__init__.py:251`, `:253`, and `:261`. Inspected
    local source uses Sage's `tensor` functor in module tensor-power helpers.
    Sage source
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/categories/covariant_functorial_construction.py:205`
    defines `CovariantFunctorialConstruction.__call__`, and
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/categories/tensor.py:16`
    defines `TensorProductFunctor(CovariantFunctorialConstruction)` with the
    singleton `tensor = TensorProductFunctor()` at line `:56`. Runtime confirms
    `sage.categories.tensor.tensor` is callable. Current
    `sage-stubs/categories/covariant_functorial_construction.pyi` defines
    `CovariantFunctorialConstruction` without `__call__`, so the inherited
    callable surface is absent from `TensorProductFunctor`. Owner is
    `sage-stubs`: this is a real Sage functor callable surface missing from the
    stub base class. Required work is to type
    `CovariantFunctorialConstruction.__call__` or the tensor functor callable
    precisely enough for parent/morphism functorial construction calls, without
    using opaque catch-all signatures where a source-backed parent/morphism
    shape is available. Acceptance is that the three covered callable rows
    disappear. Falsifier would be current Sage source/runtime showing
    `TensorProductFunctor` is not callable, or evidence that these call sites
    should use a different local tensor helper rather than the Sage functor.

  - `STUB-CATEGORY-BASE-ADDITIONAL-STRUCTURE`: exact selector covers the single
    current no-base override row at `category_specs/modules/__init__.py:526`
    for `Modules.additional_structure`. Sage source
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/categories/modules.py:181`
    defines `Modules.additional_structure`, and
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/categories/category.py:1053`
    defines the base `Category.additional_structure` hook. Current
    `sage-stubs/categories/category.pyi` exposes `super_categories` and
    `extra_super_categories` but not `additional_structure`, and
    `sage-stubs/categories/modules.pyi` also omits the method on `Modules`.
    Owner is `sage-stubs`: the public Sage category hook exists in source and
    is absent from the static category surface. Required work is to add the
    source-backed category `additional_structure` surface without weakening
    local category contracts or inventing project-specific methods. Acceptance
    is that the line `:526` row disappears and other local `_sage_*` hook rows
    remain separately owned. Falsifier would be current Sage source/runtime
    lacking `additional_structure` on `Category`/`Modules`, or evidence that
    the row is caused solely by a local method name that Sage does not expose.

  - `STUB-FINITE-RANK-FREE-MODULE-METHODS`: exact selector covers five current
    no-base override rows in `category_specs/modules/subcategories/free.py` for
    source-backed Sage finite-rank free-module methods missing from stubs:
    `bases` at line `:99`, `default_basis` at `:107`, `set_default_basis` at
    `:115`, `exterior_power` at `:196`, and `alternating_form` at `:210`.
    Sage source
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/tensor/modules/finite_rank_free_module.py`
    defines `exterior_power` at line `:1618`, `alternating_form` at `:2369`,
    `default_basis` at `:2759`, `set_default_basis` at `:2797`, and `bases` at
    `:2873`. Current `sage-stubs/tensor/modules/` has no
    `finite_rank_free_module.pyi`, and `sage-stubs/modules/free_module.pyi`
    does not expose these finite-rank methods. Owner is `sage-stubs`: the
    research provider delegates to real Sage finite-rank module surfaces that
    the stub package does not currently expose. Required work is to stub the
    finite-rank free-module class and these public methods with source-backed
    signatures, preserving the distinction between finite-rank tensor modules
    and ambient/free modules. Acceptance is that these five rows disappear
    without replacing finite-rank module types by opaque parent/object types.
    Falsifier would be current Sage source/runtime lacking one of these
    methods, or evidence that after the finite-rank stub exists the same rows
    persist solely because plugin provider-base projection is missing.

  - `STUB-COMMUTATIVE-RING-EXTENSION-AND-POLYNOMIAL-COMPLETION`: exact selector
    covers three current rows in `category_specs/rings/subcategories/polynomial_ring.py`:
    the no-base override row for `extension` at line `:58`, the no-base
    override row for `completion` at line `:82`, and the `"completion"
    undefined in superclass` row at line `:92`. Sage runtime reports
    `PolynomialRing(QQ, "x").extension` as
    `sage.rings.ring.CommutativeRing.extension` and
    `PolynomialRing(QQ, "x").completion` as
    `sage.rings.polynomial.polynomial_ring.PolynomialRing_generic.completion`;
    Sage source defines `CommutativeRing.extension` in
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/rings/ring.pyx`
    and defines `PolynomialRing_generic.completion` at
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/rings/polynomial/polynomial_ring.py:620`.
    Current `sage-stubs/rings/ring.pyi` puts `extension` only on `Field`, not
    on `CommutativeRing`, and current
    `sage-stubs/rings/polynomial/polynomial_ring.pyi` omits `completion` on
    `PolynomialRing_generic`. Owner is `sage-stubs`: these are real Sage ring
    methods missing from the relevant public stub surfaces. Required work is to
    expose `CommutativeRing.extension` and univariate
    `PolynomialRing_generic.completion` precisely enough for polynomial-ring
    parents, without treating Puiseux or other local ring subcategories as
    having the same methods unless Sage source proves it. Acceptance is that
    these three rows disappear. Falsifier would be current Sage runtime/source
    lacking either method on the stated receivers, or evidence that the local
    `super().completion(...)` call is not meant to target the Sage polynomial
    completion method.
