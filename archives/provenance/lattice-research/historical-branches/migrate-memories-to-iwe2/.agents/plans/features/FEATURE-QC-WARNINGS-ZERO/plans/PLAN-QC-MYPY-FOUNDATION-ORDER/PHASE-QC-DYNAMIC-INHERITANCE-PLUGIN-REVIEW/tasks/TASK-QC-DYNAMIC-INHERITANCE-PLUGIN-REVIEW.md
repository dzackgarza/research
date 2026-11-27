---
id: TASK-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW
trackerStatus:
  type: task
parents:
- '[[PHASE-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW]]'
dependsOn:
- '[[TASK-QC-BASIC-MYPY-HYGIENE-INVENTORY]]'
title: Review dynamic-inheritance mypy plugin findings
status: unstarted
priority: critical
description: 'After basic typing hygiene and plugin completion, classify only override,
  final, abstractmethod, MRO, and base-injection findings as plugin misses or real source
  defects.

  '
activityType: validation
workstreamRole: review
claimStatus: unexamined
uncertaintyState: ordinary-open
successCriteria:
- The basic hygiene phase is complete before this task starts.
- The plugin feature is complete before this task starts.
- Focused mypy reproductions cover each dynamic-inheritance error shape under review.
- Each remaining dynamic-inheritance finding is routed to plugin repair or source repair without including stub-generation issues.
complexity: 45
tags:
- FEATURE-QC-WARNINGS-ZERO
- PLAN-QC-MYPY-FOUNDATION-ORDER
- PHASE-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW
---
# Task: Review Dynamic-Inheritance Mypy Plugin Findings

## Summary

Classify only the dynamic-inheritance mypy subset after earlier prerequisites are
complete: `@override`, `@final`, `@abstractmethod`, method-container MRO
projection, base injection, and plugin-loaded QC config behavior.

## Source Provenance

- `SPEC-SAGE-MYPY-CATEGORY-OVERRIDE`.
- `FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN`.
- `PLAN-QC-MYPY-FOUNDATION-ORDER`.

## Context

This task must not discuss missing annotations, `Any`, generated stubs, invalid
type aliases, or downstream category typing as plugin evidence. Those belong to
other phases.

## Acceptance Criteria

- Dynamic-inheritance findings are reproduced with focused mypy runs.
- Each finding is classified as plugin miss, source defect, or not in this phase.
- Findings outside dynamic inheritance are moved to the correct later phase.

## Dependencies And Boundaries

This task is not selectable until its parent phase dependencies are complete.

## Work Log

- Created 2026-05-13 to narrow plugin-related mypy work to the intended subset.
- 2026-05-23 blocker-forensics classification:
  `PLUGIN-CATEGORY-METHOD-CONTAINER-SELF` is a confirmed plugin-owned family.
  Exact selector covers the 12 current rows whose message is
  `Argument 1 to "category_of" of "FunctorialConstructionCategory" has
  incompatible type "SubcategoryMethods"; expected "Category"` at
  `category_specs/sets/__init__.py:472`, `:482`, `:490`,
  `category_specs/modules/__init__.py:1645`, `:1650`, `:1659`, `:1669`,
  `category_specs/algebras/__init__.py:378`, `:384`,
  `category_specs/rings/__init__.py:2048`, `:2055`, and
  `category_specs/lattices/__init__.py:155`. Inspected source shows these calls
  occur inside nested `SubcategoryMethods` method containers and pass `self` to
  Sage `FunctorialConstructionCategory.category_of`; at runtime Sage installs
  category method-container methods onto category objects, so `self` is the
  category object, while vanilla mypy sees the lexical nested class
  `SubcategoryMethods`. Owner is the plugin, stated generically: model
  category-owned method-container self binding for third-party Sage categories
  without knowing `category_specs`, `Cat`, or local wrapper class names.
  Required work is to project or otherwise type method-container `self` as the
  owning category object where Sage runtime supplies that binding. Acceptance is
  that these 12 rows disappear without local casts, suppressions, or
  consumer-name special cases. Falsifier would be evidence that Sage does not
  bind these `SubcategoryMethods` onto category instances at runtime, or that a
  specific row is actually passing a lexical helper object rather than the
  runtime category object.
- `PLUGIN-CATEGORY-SUBCATEGORY-METHOD-PROJECTION` is a confirmed plugin-owned
  family. Exact selector covers the nine current rows in
  `category_specs/modules/__init__.py:1280`, `:1306`, `:1334`, `:1362`,
  `:1388`, `:1403`, `:1429`, `:1444`, and `:1467` whose message is
  `"Modules" has no attribute "RingObjectsAsModules"`. Inspected source defines
  `RingObjectsAsModules` in `Modules.SubcategoryMethods` at
  `category_specs/modules/__init__.py:1713-1716`; the failing constructor calls
  use `self.category().RingObjectsAsModules()` from module constructor helpers.
  Owner is the plugin, stated generically: Sage category `SubcategoryMethods`
  are category-owned method containers whose methods are available on category
  instances at runtime, but mypy sees only lexical nested-class membership.
  Required work is namespace-generic projection of category-owned
  `SubcategoryMethods` methods onto the owning category object, not a
  `Modules` or `category_specs` special case. Acceptance is that these nine rows
  disappear without adding fake direct methods to the research class or stubs.
  Falsifier would be runtime/source evidence that `RingObjectsAsModules` is not
  a valid category-owned method or that the local code should call a different
  object entirely.
- `PLUGIN-CATEGORY-SUBCATEGORY-ATTR-PROJECTION` is a confirmed plugin-owned
  family. Exact selector covers the three current
  `"Modules" has no attribute "FinitelyPresentedGradedModules"` rows at
  `category_specs/modules/__init__.py:1015`, `:1026`, and `:1042`, plus the
  five current `"Rings" has no attribute "Characteristic"` rows in
  `category_specs/rings/subcategories/real_precision_field.py:49`,
  `algebraic_field.py:40`, `complex_precision_field.py:47`,
  `rational_field.py:56`, and `integer_ring.py:36`. Inspected source defines
  `FinitelyPresentedGradedModules` in `Modules.SubcategoryMethods` at
  `category_specs/modules/__init__.py:1693-1696` and `Characteristic` in
  `Rings.SubcategoryMethods` at `category_specs/rings/__init__.py:2007-2012`.
  Owner is the plugin: these are category-owned method-container methods that
  Sage exposes on category instances at runtime, and the required behavior is
  namespace-generic projection of `SubcategoryMethods` members onto their owning
  category class. Required work is not to add fake direct methods in stubs or
  hard-code `Modules`/`Rings`, but to project category-owned method containers
  generically. Acceptance is that these eight rows disappear. Falsifier would be
  runtime/source evidence that these methods are not actually category-owned
  methods on the receiver categories.
- `PLUGIN-PARENTMETHODS-SELF-BINDING` is a confirmed plugin-owned family. Exact
  selector covers ten rows whose message says a parent-method container receiver
  (`ParentMethods` or `_AlgebraParentMethods`) lacks `category`, six rows whose
  message says a `ParentMethods`-typed receiver lacks `base_ring`, and four rows
  in `category_specs/lattices/__init__.py:163`,
  `:170`, `:179`, and `:188` whose message says `SubcategoryMethods` lacks
  `base_ring`. Representative inspected sources include set parent methods in
  `category_specs/sets/subcategories/recursively_enumerated.py` and
  `enumerated_from_iterator.py`, ring matrix-algebra parent methods in
  `category_specs/rings/matrix_algebras.py`, and lattice subcategory methods in
  `category_specs/lattices/__init__.py:154-188`. Owner is the plugin: Sage
  installs category `ParentMethods` on parent objects and `SubcategoryMethods`
  on category objects, so `self.category()` and `self.base_ring()` are runtime
  receiver operations, while vanilla mypy sees only the lexical nested method
  class. Required work is generic receiver-self binding for category method
  containers, not consumer-specific names. Acceptance is that these 20
  attr-defined rows disappear without local casts or fake stub members.
  Falsifier would be evidence that a covered method is called on the lexical
  method-container helper rather than on a Sage runtime parent/category object.
- `PLUGIN-CATEGORY-SUBCATEGORY-ATTR-PROJECTION-EXTENDED` is a confirmed
  plugin-owned family. Exact selector covers eight current rows whose receiver
  is the owning local category instance and whose missing attribute is defined
  in that category's `SubcategoryMethods`: two `"Modules" has no attribute
  "FreeGradedModules"` rows at `category_specs/modules/__init__.py:1037` and
  `:1059`, two `"Modules" has no attribute "IntegerLattices"` rows at
  `:1079` and `:1103`, two `"AssociativeAlgebras" has no attribute
  "WithBasis"` rows at `category_specs/algebras/__init__.py:532` and `:564`,
  one `"MagmaticAlgebras" has no attribute "FiniteDimensional"` row at
  `:657`, and one `"AssociativeAlgebras" has no attribute "FiniteDimensional"`
  row at `:665`. Inspected source defines `Modules.SubcategoryMethods`
  methods `FreeGradedModules` and `IntegerLattices` at
  `category_specs/modules/__init__.py:1689-1705`, and defines
  `Algebras.SubcategoryMethods.WithBasis` and `FiniteDimensional` at
  `category_specs/algebras/__init__.py:352-359`; the failing call sites call
  these methods through `self.category()` or algebra subcategory instances.
  Owner is the plugin, stated generically: category-owned `SubcategoryMethods`
  methods must be projected onto the owning category and its valid subcategory
  instances, independent of package or class names. Required work is to extend
  namespace-generic category method-container projection so these methods are
  visible on category instances. Acceptance is that these eight rows disappear
  without adding fake direct methods to the research classes or stubs.
  Falsifier would be runtime/source evidence that one of these receivers is not
  an owning category/subcategory instance for the named method-container method,
  in which case that row must move to research-owned local receiver typing.
- `PLUGIN-CATEGORY-SUBCATEGORY-ATTR-PROJECTION-SECONDARY` is a confirmed
  plugin-owned family. Exact selector covers four current attr-defined rows
  where the receiver is a concrete local category instance and the missing
  method is defined in that category's `SubcategoryMethods`: `"Modules" has no
  attribute "OreModules"` at `category_specs/modules/__init__.py:1067`,
  `"Modules" has no attribute "TorsionQuadraticModules"` at `:1120`, and
  `"Rings" has no attribute "KrullDimension"` at
  `category_specs/rings/subcategories/field.py:65` and
  `category_specs/rings/subcategories/dedekind_domain.py:40`. Inspected source
  defines `OreModules` and `TorsionQuadraticModules` in
  `Modules.SubcategoryMethods` at `category_specs/modules/__init__.py:1699-1710`
  and `KrullDimension` in `Rings.SubcategoryMethods` at
  `category_specs/rings/__init__.py:2017-2021`. Owner is the plugin, stated
  generically: category-owned `SubcategoryMethods` methods must be projected
  onto the owning category instance independent of package names. Required work
  is the same namespace-generic method-container projection as the primary and
  extended category-subcategory projection families. Acceptance is that these
  four rows disappear without adding fake direct methods to research classes or
  Sage stubs. Falsifier would be runtime/source evidence that the receiver is
  not the owning category instance for the named method-container method.
- `PLUGIN-SUBCATEGORYMETHODS-CATEGORY-SELF-ATTR`: exact selector covers two
  current attr-defined rows where a method body inside a `SubcategoryMethods`
  container calls `self.base_category()`: `category_specs/modules/__init__.py:1554`
  and `category_specs/modules/subcategories/with_basis.py:51`. Inspected source
  defines these methods inside local `SubcategoryMethods` containers, and Sage
  category runtime binds such methods onto category objects whose public surface
  includes `base_category`. Owner is the plugin, stated generically: method
  container `self` must be modeled as the runtime category object, not the
  lexical nested helper class. Required work is namespace-generic
  `SubcategoryMethods` self binding for ordinary category-object methods.
  Acceptance is that both rows disappear without adding fake `base_category`
  members to lexical helper stubs. Falsifier would be evidence that these
  methods execute on lexical helper objects rather than Sage category objects.
- `PLUGIN-PARENTMETHODS-AS-SAGE-PARENT-DELEGATE`: exact selector covers three
  current rows in `category_specs/rings/matrix_algebras.py` where a
  category-owned `ParentMethods` method delegates to an unbound Sage
  `MatrixSpace` method and mypy treats `self` as the lexical provider class
  instead of the runtime parent: `MatrixSpace.nrows(self)` at line `:97`,
  `MatrixSpace.ncols(self)` at line `:103`, and
  `MatrixSpace.matrix_space(self, ...)` at line `:216`. Inspected source shows
  these calls occur inside `_MatrixAlgebras.ParentMethods`, whose methods are
  intended to run on the matrix-space parent object; Sage source defines the
  delegated public methods on `MatrixSpace` at
  `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/matrix/matrix_space.py:2314`,
  `:2337`, and `:2349`. Owner is the plugin, stated generically: when Sage
  installs category `ParentMethods` on a parent object, `self` inside those
  provider methods must be typed as the runtime parent for unbound Sage method
  delegation, not as the lexical nested provider class. Required work is
  generic provider-self binding for unbound base-method calls, independent of
  matrix algebra or research package names. Acceptance is that these three
  receiver rows disappear without adding fake methods to `ParentMethods`.
  Falsifier would be evidence that these provider methods are called on the
  lexical provider object rather than the matrix-space parent at runtime.
- `PLUGIN-PARENTMETHODS-AS-SAGE-PARENT-BASIC-SELF`: exact selector covers the
  single current row at `category_specs/sets/subcategories/partitioned.py:69`
  where `PartitionedSetsCategory.ParentMethods.partition` calls
  `self.an_element()` and mypy reports that lexical `ParentMethods` has no
  attribute `an_element`. Inspected source shows the method is inside a Sage
  category `ParentMethods` container at
  `category_specs/sets/subcategories/partitioned.py:65-69`; Sage source and
  stubs expose `an_element` on the runtime parent surface at
  `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/structure/parent.pyx:2759`
  and
  `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/structure/parent.pyi:134`.
  Owner is the plugin, stated generically: category `ParentMethods` bodies are
  executed on Sage parent objects, so provider-method `self` must include the
  runtime parent API such as `an_element`, independent of package or class
  names. Required work is generic provider-self binding for `ParentMethods`,
  not a `PartitionedSetsCategory` or `category_specs` special case. Acceptance
  is that the line `:69` attr-defined row disappears without adding fake
  `an_element` members to lexical provider classes. Falsifier would be runtime
  evidence that this category method is invoked on the lexical provider helper
  rather than on a Sage parent object, or source evidence that `an_element` is
  not part of Sage's parent surface.
- `PLUGIN-PARENTMETHODS-OVERRIDE-BASE-VISIBILITY`: exact selector covers the
  three current missing-base override rows in
  `category_specs/rings/subcategories/rational_field.py` where the local
  `_QQ.ParentMethods` provider overrides Sage QQ methods that are already
  present in the current RationalField stub: `signature` at line `:116`,
  `discriminant` at `:121`, and `class_number` at `:184`. Inspected local
  source defines these inside a category `ParentMethods` container at
  `category_specs/rings/subcategories/rational_field.py:72-184`; current
  `sage-stubs/rings/rational_field.pyi` exposes `RationalField.signature`,
  `discriminant`, and `class_number`, and Sage runtime confirms the same names
  on `sage.all.QQ`. Owner is the plugin, stated generically: category
  `ParentMethods` override checks must see the runtime parent base surface when
  the provider method intentionally refines a real Sage parent method. This is
  not a `QQ` or `category_specs` special case, and it is not caused by missing
  stubs for these three names. Required work is generic provider-to-parent
  override-base visibility for method containers. Acceptance is that these
  three rows disappear without adding fake base classes to the lexical
  `ParentMethods` class or hard-coding the downstream package. Falsifier would
  be evidence that Sage category provider methods are not allowed to override
  existing parent methods, or that one of these three names is absent from both
  current Sage runtime and the RationalField stub.
- `PLUGIN-CLASSCALL-PRIVATE-KEYWORD-PROPAGATION`: exact selector covers the two
  current `call-arg` rows
  `category_specs/forms/__init__.py:147` and
  `category_specs/lattices/__init__.py:242`, where
  `Modules(base_ring, dispatch=False)` is rejected with `Unexpected keyword
  argument "dispatch" for "Modules"`. Inspected source shows the local category
  class declares `Modules.__classcall_private__(cls, base_ring: Ring,
  dispatch: bool = True)` at `category_specs/modules/__init__.py:481-483`, and
  `SPEC-SAGE-MYPY-CATEGORY-OVERRIDE.md` records the generic rule that public
  construction through Sage `__classcall_private__` should expose that
  classcall signature at call sites rather than checking the ordinary category
  initializer. Owner is the plugin, stated generically: model Sage
  classcall-private constructor keyword propagation for classes that define a
  classcall bridge; this is not a `Modules`, `category_specs`, or local-wrapper
  special case. Required work is to make constructor-call analysis use the
  matching `__classcall_private__` parameter surface where Sage runtime
  construction does. Acceptance is that these two `dispatch` keyword rows
  disappear without adding fake zero-argument or opaque constructor stubs and
  without suppressing local type checks. Falsifier would be source/runtime
  evidence that the covered calls bypass the classcall bridge, that `dispatch`
  is not part of the classcall-private surface, or that a matching
  classcall-private signature is already projected and the rows instead arise
  from a local invalid constructor call.
- `PLUGIN-PROVIDER-OVERRIDE-BASE-VISIBILITY-MISC`: exact selector covers the
  eight current `misc` rows where a category-owned provider method overrides a
  real Sage parent/provider method but mypy reports no base method:
  `category_specs/modules/subcategories/constructions/quotients.py:80`
  (`quotient_module`), `modules/subcategories/constructions/cartesian_products.py:37`
  (`__init_extra__`), `modules/subcategories/constructions/cartesian_products.py:53`
  (`_lmul_`), `sets/subcategories/countable.py:141` (`__len__`),
  `sets/subcategories/countable.py:146` and `:177` (`random_element`), and
  `sets/subcategories/cartesian_product.py:93` (`_coerce_map_from_`), plus
  `category_specs/topological_spaces/subcategories/metric.py:92`, where the
  projected topological `SubcategoryMethods.Compact` base method is not
  visible while checking metric-space subcategory methods. Inspected Sage
  source/stubs show the external methods exist: `Parent.quotient_module` is in
  `sage-stubs/structure/parent.pyi`; `Modules.CartesianProducts.ParentMethods.__init_extra__`
  and `.ElementMethods._lmul_` are in Sage source
  `sage/categories/modules.py:859` and `:917` and current
  `sage-stubs/categories/modules.pyi`; `FiniteEnumeratedSets.ParentMethods`
  and `InfiniteEnumeratedSets.ParentMethods` expose `__len__` /
  `random_element`; `Parent._coerce_map_from_` exists in Sage parent source and
  stubs; and `TopologicalSpaces.SubcategoryMethods.Compact` exists in Sage
  source and current `sage-stubs/categories/topological_spaces.pyi`. Owner is
  the plugin, stated generically: provider method-container override checks
  must see the runtime Sage parent/category/provider base surfaces already
  present in stubs, independent of downstream names. Required work is generic
  provider-base visibility for category `ParentMethods`, `ElementMethods`, and
  `SubcategoryMethods` override checking, not fake direct methods on local
  lexical provider classes. Acceptance is that these eight rows disappear
  without changing research method bodies or weakening Sage stubs. Falsifier
  would be row-specific evidence that a named Sage method is absent from both
  current runtime and stubs, or that the local category is not a valid provider
  context for that method.
- `PLUGIN-PARENTMETHODS-FREE-MODULE-BASE-VISIBILITY`: exact selector covers
  three current `misc` rows in `category_specs/modules/subcategories/free.py`
  and `category_specs/forms/subcategories/free_bilinear.py` where the Sage
  method is already present in stubs but the category-owned local provider
  cannot see it as an override base: `dimension` at
  `modules/subcategories/free.py:128`, `gram_matrix` at
  `forms/subcategories/free_bilinear.py:82`, and `inner_product_matrix` at
  `forms/subcategories/free_bilinear.py:98`. Sage source defines these methods
  on free-module parents in
  `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/modules/free_module.py:2940`,
  `:3100`, and `:3301`; current `sage-stubs/modules/free_module.pyi` exposes
  `FreeModule_generic.dimension`, `Module_free_ambient.gram_matrix`, and
  free-module `inner_product_matrix`. Owner is the plugin: these rows are not
  missing-stub rows; they need the generic rule that category `ParentMethods`
  installed on a Sage parent can override/refine existing parent methods. The
  plugin must express that relation without knowing `category_specs` or local
  free-module class names. Acceptance is that these three rows disappear while
  finite-rank methods absent from stubs remain in the stubs-owned family until
  their source-backed surfaces exist. Falsifier would be evidence that the
  current free-module stubs no longer expose one of these methods, or that the
  local provider method is not meant to run on a Sage free-module parent.
- `PLUGIN-SUBCATEGORYMETHODS-CATEGORY-SELF-ARG`: exact selector covers six
  current `arg-type` rows where a category-owned `SubcategoryMethods` method
  passes `self` to a category constructor/helper and vanilla mypy sees the
  lexical provider class rather than the runtime category object: row `265` at
  `category_specs/sets/__init__.py:462`, where `_GSets(acting_group, self)`
  expects a category; and rows `1310`, `1313`, `1316`, `1319`, and `1322` at
  `category_specs/forms/subcategories/bilinear.py:145`, `:152`, `:159`,
  `:166`, and `:173`, where `OverPID...BilinearModulesCategory(self)` expects
  a category. Inspected source shows all six calls occur inside nested
  `SubcategoryMethods` containers. Owner is the plugin, stated generically:
  Sage category method-container methods execute with `self` bound to the
  owning category object, so constructor-call argument typing must use that
  runtime category receiver, independent of consumer package or class names.
  Required work is to extend namespace-generic method-container self binding
  from attribute access and `category_of` calls to ordinary constructor/helper
  arguments. Acceptance is that these six rows disappear without local casts,
  fake direct methods, or downstream-name hard-coding. Falsifier would be
  runtime evidence that these methods are invoked on lexical
  `SubcategoryMethods` helper objects rather than category instances, or
  source evidence that a specific constructor should not accept the owning
  category.
