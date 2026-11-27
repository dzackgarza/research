---
id: TASK-QC-DOWNSTREAM-TYPE-CLEANUP
trackerStatus:
  type: task
parents:
- '[[PHASE-QC-DOWNSTREAM-TYPE-CLEANUP]]'
dependsOn:
- '[[TASK-QC-GENERATE-TYPE-STUBS]]'
title: Clean remaining downstream category type defects
status: unstarted
priority: high
description: 'After basic hygiene, plugin review, and stub generation, fix or split the
  remaining category/type defects from post-stub mypy output.

  '
activityType: implementation
workstreamRole: implementation
claimStatus: unexamined
uncertaintyState: ordinary-open
successCriteria:
- Post-stub mypy output is collected through the repo-approved validation path or a documented focused equivalent.
- Remaining defects are grouped by real source responsibility, not by aggregate pre-stub error shape.
- Each defect group is fixed or split into executable child tasks.
complexity: 55
tags:
- FEATURE-QC-WARNINGS-ZERO
- PLAN-QC-MYPY-FOUNDATION-ORDER
- PHASE-QC-DOWNSTREAM-TYPE-CLEANUP
---
# Task: Clean Remaining Downstream Category Type Defects

## Summary

Fix or split the remaining mypy defects only after the earlier frontiers are
complete. This task covers defects that remain real after basic hygiene,
dynamic-inheritance plugin review, and stub generation.

## Source Provenance

- `FEATURE-QC-WARNINGS-ZERO`, Category C and D.
- `PLAN-QC-MYPY-FOUNDATION-ORDER`.

## Context

Examples may include incompatible signatures, constructor call mismatches,
remaining `attr-defined` findings, and category-specific type defects, but only
when they survive the earlier phases.

## Acceptance Criteria

- Post-stub validation output identifies remaining defects.
- Each defect is routed to a concrete owner or child task.
- No task in this phase hides or recategorizes earlier-phase work.

## Dependencies And Boundaries

Depends on `TASK-QC-GENERATE-TYPE-STUBS`.

## Work Log

- Created 2026-05-13 as the last mypy cleanup leaf.
- 2026-05-23 blocker-forensics classification: the current
  `category_specs/cat` frontier has 141 ordinary diagnostics. The rows below
  are the research-owned local subset for that frontier; they intentionally
  exclude the separately recorded `sage-stubs` rows for `LazyImport`,
  `Category.join`/`meet`/`&`, and Sage `category_types` constructors.

  - `RESEARCH-CAT-MIXIN-SELF-TYPE`: exact selector covers
    `category_specs/cat/base_category_types.py:474`, `:475`, `:495`, and `:511`.
    The inspected source defines local `_CatObjectMixin._init_cat_object`,
    `Hom`, and `_make_named_class` methods at lines 439-517, then calls unbound
    Sage `Parent`, `CategoryObject`, and local wrapper helper APIs with `self`
    statically typed only as `_CatObjectMixin`. Owner is research code/typing:
    this is the local wrapper's self-type contract, not a generic plugin rule
    and not a missing Sage API. Required work is to redesign or annotate the
    local mixin/wrapper boundary so the required `Parent`/`CategoryObject`/
    wrapped-category relationship is explicit without weakening Sage stubs.
    Acceptance is that these four rows disappear while preserving runtime-valid
    Sage category behavior. Falsifier would be a minimized third-party Sage
    wrapper pattern, independent of `Cat`, proving the plugin contract must
    synthesize this self-type relationship generically.

  - `RESEARCH-CAT-MRO-METHOD-CONFLICTS`: exact selector covers the 103 current
    `category_specs/cat/**` rows whose message starts `Definition of ... in base
    class ... is incompatible`, including the repeated `Hom`,
    `_make_named_class`, singleton `__classcall__`, `base_ring`, and `__call__`
    conflicts. Inspected source lines 590-593 state that wrapper bases
    intentionally use `_CatObjectMixin, SageCategoryBase, Parent`; the concrete
    classes from `Category` through the construction categories inherit that
    local mixin together with Sage category bases and `Parent`. Owner is
    research code/design: these rows arise from local multiple-inheritance
    method compatibility, and the refreshed structural projection canary reports
    zero missing provider graph edges or TypeInfos. Required work is to make the
    local wrapper MRO/signatures type-consistent or redesign the wrapper layer;
    the plugin must not learn `Cat` or `_CatObjectMixin`. Acceptance is that the
    103 MRO conflict rows disappear without narrowing Sage base stubs or
    suppressing override checks. Falsifier would be evidence that the same
    namespace-generic Sage provider pattern fails for a minimized non-research
    wrapper even when ordinary Python MRO signatures are compatible.

  - `RESEARCH-CAT-SINGLETON-CLASSCALL-LOCAL-TYPE`: exact selector covers
    `category_specs/cat/base_category_types.py:548` and `:579`. The inspected
    source in `_SingletonClasscallMixin.__classcall__` and
    `_SingletonAxiomClasscallMixin.__classcall__` conditionally replaces `cls`
    with `cls.__base__` after a `DynamicMetaclass` check. Owner is research
    typing/design: the local singleton bridge changes the static type of `cls`;
    this is not a missing Sage method or plugin category-provider projection.
    Required work is to express or isolate the local dynamic-metaclass branch
    without degrading Sage singleton stub types. Acceptance is that both
    assignment rows disappear. Falsifier would be evidence that current Sage
    stubs type `DynamicMetaclass.__base__` incorrectly for all Sage singleton
    category classcall implementations.

  - `RESEARCH-CAT-DEFINING-PREDICATE-NARROWING`: exact selector covers
    `category_specs/cat/base_category_types.py:648`, `:686`, and `:718`. The
    local wrapper overrides `CategoryWithAxiom.defining_predicate` with
    `candidate: CategoryObject`, while the Sage supertype accepts `object`.
    Owner is research code/typing: this is an explicit parameter narrowing in
    local overrides, not a missing external surface. Required work is to keep
    the override contravariant with Sage while performing local category-object
    checks internally. Acceptance is that these three override rows disappear
    without weakening the Sage supertype. Falsifier would be source evidence
    that Sage's public supertype now narrows `defining_predicate` to
    `CategoryObject`.

  - `RESEARCH-CAT-LOCAL-CATEGORY-RETURN-SURFACES`: exact selector covers
    `category_specs/cat/__init__.py:290` and `:330`. The associated Cat
    `super_categories` and `extra_super_categories` override/list-item rows are
    owned below by `RESEARCH-LOCAL-CATEGORY-AS-SAGE-CATEGORY`; the remaining
    inspected source returns local `JoinCategories` and `EmptyCategory` objects
    from methods whose local signatures promise the project `Category` wrapper.
    Owner is research code/design unless the local wrapper is separately proven
    to be a valid generic Sage category object pattern; no such proof exists,
    and importing `category_specs.cat.base_category_types` currently fails
    during package-level axiom registration with `ImportError: cannot import name
    Category`. Required work is to either make the local wrappers valid Sage
    `Category` participants at runtime and then reduce any remaining failure to
    a generic plugin issue, or change these local return contracts. Acceptance
    is that both rows disappear and the wrapper import/runtime relation is
    demonstrably valid. Falsifier would be a runtime-valid minimized third-party
    category wrapper where the only failing static relation is generic Sage
    provider/category projection.

  - `RESEARCH-CAT-HOMSETS-SPEC-MISMATCH`: exact selector covers the six
    non-return-surface rows in `category_specs/cat/homsets.py`: the missing
    return and `__call__` override rows at lines 27 and 40, plus
    `category_of` at line 112. The inspected source defines functor homset
    behavior for `Cat()` by overriding universal hom object/element methods
    with functor/category-specific call signatures. Owner is research
    mathematical/spec design: this is a local question about whether Cat
    morphisms are modeled as functors and whether they can validly refine the
    universal homset contracts. Required work is to settle the local homset
    contract and then align signatures or split the abstraction. Acceptance is
    that these six rows disappear through a coherent local homset design.
    Falsifier would be evidence that Sage's generic homset method-container
    semantics explicitly permits these incompatible `__call__` refinements and
    the plugin is expected to model that rule namespace-generically.

  - `RESEARCH-CAT-LOCAL-SPECIAL-OVERRIDES`: exact selector covers
    `category_specs/cat/base_category_types.py:781`,
    `category_specs/cat/empty_category.py:42`, and
    `category_specs/cat/__init__.py:214`. The inspected source gives local
    special-case overrides for `Homsets.Endset`, bottom-category
    `is_subcategory`, and Cat-root `_make_named_class`; each narrows or changes
    a Sage supertype contract for local Cat semantics. Owner is research
    code/spec design. Required work is to rewrite these local overrides so they
    obey the Sage supertype contracts or split the local semantics out of the
    inherited method surface. Acceptance is that the three override rows
    disappear without changing Sage stubs to accept the narrower local contract.
    Falsifier would be source evidence that the Sage supertype signatures are
    wrong for these exact public methods.

  - `RESEARCH-LOCAL-CATEGORY-AS-SAGE-CATEGORY`: exact selector covers the 144
    current `override` rows whose message contains
    `Return type "list[category_specs.cat.base_category_types.Category]"` and a
    Sage `list[sage.categories.category.Category]` supertype expectation, plus
    all 143 current `list-item` rows. The list-item rows split into 124
    non-`cat/**` rows where local category instances are placed in lists
    expected as Sage `Category`, three `cat/**` rows with the same shape, 15
    rows where Sage `Category` values are placed in lists expected as the
    project `Category` wrapper, and one lattice construction row where generic
    `Category` is placed in a `LatticesCategory` list. Representative inspected
    lines include `category_specs/sets/__init__.py:382-384`,
    `category_specs/homsets/homsets.py:112-115`,
    `category_specs/cat/join_categories.py:30-34`,
    `category_specs/cat/homsets.py:123-125`, and construction/homset
    `extra_super_categories` methods such as
    `category_specs/sets/homsets.py:95-97`. Common cause is the local wrapper
    hierarchy using project `Category`/specialized category classes and Sage
    `Category` interchangeably in category-list return contracts without first
    proving that relationship. Owner is research code/design unless the wrapper
    layer is first proven to be a runtime-valid, namespace-generic Sage category
    object pattern. Required work is to either make the local wrapper hierarchy
    genuinely satisfy the Sage `Category` contract and then reduce remaining
    generic failure to the plugin, or change these local method
    signatures/returns to Sage-compatible category objects. Acceptance is that
    these 287 rows disappear without weakening Sage `Category` stubs to accept
    research-local wrappers or weakening project category contracts to accept
    arbitrary Sage categories. Falsifier would be a minimized non-research
    third-party category wrapper proving that the plugin should project this
    local wrapper relationship generically.

  - `RESEARCH-MODULES-ABSTRACT-CATEGORY`: exact selector covers the 38 rows
    whose message is `Cannot instantiate abstract class "Modules" with abstract
    attributes "R", "torsion_module" and "zero_module"`. Inspected source shows
    `Modules` is the local category class at `category_specs/modules/__init__.py:471`,
    while `zero_module`, `R`, and `torsion_module` are declared directly on that
    category class as abstract methods at lines 1476-1485. Owner is research
    code/design: the local category class is made abstract by methods that
    appear to be constructor/provider requirements, not by missing Sage stubs or
    plugin projection. Required work is to decide whether these methods belong
    on a constructor/provider surface, a parent method container, or a concrete
    category implementation, then move/implement them accordingly. Acceptance is
    that the 38 abstract-instantiation rows disappear. Falsifier would be
    evidence that Sage category classes are supposed to remain abstract while
    still being directly instantiated by Sage classcall.

  - `RESEARCH-MODULES-BASE-RING-DOMAIN`: exact selector covers the 33 rows whose
    message starts `Argument 1 to "Modules" has incompatible type ...; expected
    "CategoryObject"`. Inspected source shows local `Modules.__classcall_private__`
    at `category_specs/modules/__init__.py:481-483` requires `base_ring: Ring`;
    representative callers pass `_RingObjectMethods` or `Category | Parent` from
    local category/refinement contexts such as
    `category_specs/modules/subcategories/ring_objects_as_modules.py:26-28` and
    `category_specs/algebras/__init__.py:124-127`. Owner is research typing/design:
    the call sites have not established the local `Ring`/`CategoryObject`
    contract before constructing `Modules(R)`. Required work is to narrow or
    redesign the local base-ring protocol at those call sites without weakening
    Sage `Modules` or treating arbitrary categories as rings. Acceptance is that
    these 33 rows disappear and `Modules` is called only with values proven to
    satisfy the local ring/category-object contract. Falsifier would be source
    evidence that the local `Ring` alias is incorrectly narrower than the real
    Sage `Modules` public constructor and the current calls are valid Sage
    surfaces.

  - `RESEARCH-NONCAT-CAT-MRO-METHOD-CONFLICTS`: exact selector covers the 42
    non-`category_specs/cat/**` rows whose message starts `Definition of ... in
    base class "_CatObjectMixin" is incompatible`, across
    `objects_over`/`objects_under` construction categories for sets, modules,
    algebras, rings, posets, lattices, and topological spaces. Representative
    inspected source is `category_specs/modules/subcategories/constructions/objects_over.py:1-33`,
    where `_ObjectsOver` inherits both a local Cat-backed
    `RegressiveCovariantConstructionCategory` and local `Category_over_base`.
    Owner is research code/design for the same reason as the Cat wrapper MRO
    rows: these are ordinary Python MRO method conflicts introduced by the local
    wrapper hierarchy, and the plugin must not learn `_CatObjectMixin` or
    `category_specs`. Required work is to make the construction-category wrapper
    MRO/signatures consistent or redesign the local wrapper composition.
    Acceptance is that the 42 rows disappear without changing Sage base stubs or
    adding consumer-specific plugin rules. Falsifier would be a minimized
    namespace-generic Sage construction-category wrapper with compatible Python
    signatures whose provider projection still fails only because of plugin
    semantics.

  - `RESEARCH-LOCAL-FINAL-REFINEMENT-CONFLICTS`: exact selector covers the 155
    rows whose message starts `Cannot override final attribute`. Inspected
    representative sources show the finality is introduced by local
    `category_specs` method surfaces: `_SetObjectMethods` in
    `category_specs/sets/__init__.py:136-333` marks methods such as
    `_element_constructor_`, `is_parent_of`, `some_elements`, set operations,
    and `_sympy_` as `@final`, while subcategories later refine those methods;
    `_SetMorphisms` in `category_specs/sets/homsets.py:37-67` marks
    `is_isomorphism` as final while homset refinements override it. The same
    pattern appears in module, algebra, ring, form, poset, lattice, and
    topological-space method containers. Owner is research code/design: the
    local spec simultaneously declares provider methods final and refines them
    downstream. Required work is to decide which methods are true non-refinable
    final implementations and which are category-provider extension points, then
    remove or move local `@final` accordingly without weakening external Sage
    stubs. Acceptance is that all 155 final-override rows disappear and no
    method is marked final where a current subcategory intentionally refines it.
    Falsifier would be evidence that a covered final declaration comes from
    Sage source/stubs rather than local `category_specs`, in which case that row
    must be split to stubs or plugin only after source proof.

  - `RESEARCH-SETS-PROVIDER-SIGNATURE-MISMATCHES`: exact selector covers the
    106 rows with `root_area == "sets"` and code `override`, excluding rows
    whose message contains
    `list[category_specs.cat.base_category_types.Category]` because those are
    already owned by `RESEARCH-LOCAL-CATEGORY-AS-SAGE-CATEGORY`. The inspected
    representative source `_SetObjectMethods` in
    `category_specs/sets/__init__.py:136-333` declares local set parent methods
    returning project `_SetElementMethods`, Sage `Integer`, `Cardinality`, or
    local `Category`; representative subcategory files such as
    `category_specs/sets/subcategories/integer_range.py`,
    `finite_enumerated_set.py`, `partitioned.py`, and `real_set.py` refine
    those methods with still narrower local signatures. The supertypes named in
    the diagnostics are Sage/local method contracts such as
    `sage.categories.sets_cat.Sets.ParentMethods`,
    `sage.categories.enumerated_sets.EnumeratedSets.ParentMethods`,
    `sage.categories.facade_sets.FacadeSets.ParentMethods`, and local
    topological/subobject contracts. Owner is research code/design: these rows
    are local provider method signature choices and local element/category type
    relationships, not missing Sage surfaces. Required work is to make the set
    method containers obey the inherited contracts or split local specialized
    operations away from override surfaces; in particular, do not weaken Sage
    `Element`, `Parent`, or Python `int` return contracts to accept project
    aliases. Acceptance is that all 106 covered override rows disappear while
    the public Sage method signatures remain source-backed. Falsifier would be a
    specific covered row whose supertype signature is absent or wrong in current
    Sage source/stubs; such a row must be split to `sage-stubs` only with source
    evidence.

  - `RESEARCH-INTEGER-LOCAL-NORMALIZATION`: exact selector covers 45 rows:
    twelve rows where Python builtins/indexing reject Sage `Integer` or
    `Integer | InfinityElement` (`range(Integer)`, `int(Integer |
    InfinityElement)`, and `__getitem__` with `Integer`), 26 assignment rows
    where a parameter is annotated `Integer` but has a Python `int` default, and
    seven return-value rows where a method annotated as returning `Integer` or
    `Integer | InfinityElement` returns Python `int`. Representative inspected
    source includes `category_specs/algebras/__init__.py:598-619`, where a Sage
    `Integer` rank is used in Python `range`; `category_specs/rings/__init__.py:733-742`,
    where `prec: Integer = 53`; and
    `category_specs/sets/subcategories/finite.py:50`, where a Sage cardinality
    delegate returns an `int` into an `Integer | InfinityElement` annotation.
    Owner is research code/typing: the remaining rows are local boundary choices
    about when a value is a Sage `Integer` and when Python builtins require
    `int`; they are not evidence that `int` and `Integer` are interchangeable
    and they are not missing `sage-stubs` constructor/protocol rows. Required
    work is to choose and enforce the local boundary per method: convert to
    `int` before Python builtins/indexing, use Sage `Integer(...)` where the
    contract is truly Sage-integer-valued, or annotate Python defaults/returns
    as `int` when that is the actual interface. Acceptance is that all 45 rows
    disappear without weakening Sage numeric stubs or using opaque types.
    Falsifier would be source/runtime evidence that a covered Python builtin
    should accept Sage `Integer` statically as part of the Sage public API rather
    than requiring local normalization.

  - `RESEARCH-GENERIC-CATEGORY-RECEIVER-TOO-BROAD`: exact selector covers 28
    attr-defined rows where the receiver has already been erased to generic
    `Category` or a broad local category wrapper before calling a
    receiver-specific subcategory method: rows `186`, `187`, `204`, `321`,
    `330`, `849`, `850`, `851`, `1087`, `1088`, `1089`, `1090`, `1091`,
    `1092`, `1209`, `1305`, `1335`, `1336`, `1398`, `1413`, `1419`, `1426`,
    `1441`, `1543`, `1554`, `1555`, `1568`, and `1608`. Inspected source
    includes
    `category_specs/modules/subcategories/finitely_presented_over_pid.py:64-68`
    and the related module-category files `over_dedekind_domain.py`,
    `over_pid.py`, `free.py`, `finitely_generated.py`,
    `finitely_presented.py`, `r_ideals.py`, and `with_basis.py`, where
    `base_category()` is typed as generic `Category` before calling
    module-specific selectors such as `FinitelyPresented`, `OverPID`,
    `Projective`, `Free`, `WithBasis`, `WithOrderedGeneratingSet`,
    `FinitelyGenerated`, or `Subobjects`; `category_specs/rings/__init__.py:2071-2140`,
    where construction selectors return generic `Category` before calling
    ring-specific `RingsUnder`, `Quotients`, or `Subobjects`; and homset/tensor
    category code at
    `category_specs/modules/homsets.py:380`,
    `category_specs/tensor_algebra_components/__init__.py:166`, and
    `category_specs/lattices/homsets.py:62`, plus lattice construction files
    calling `Rational` or `Lattice`, where the receiver is generic before the
    specialized category method call. Owner is research typing/design: these
    chains have
    already erased the receiver to generic `Category`, so the immediate required
    work is to preserve or prove the more specific local category protocol at
    the call site. Acceptance is that these 28 attr-defined rows disappear
    through precise local category return/protocol types or local narrowing,
    without adding broad methods to Sage `Category`. Falsifier would be a
    plugin-level generic rule proving that Sage category axiom/functor methods
    preserve receiver-specific subcategory method surfaces across these chains.

  - `RESEARCH-CONSTRUCTOR-BASE-RING-CONTRACT`: exact selector covers 15 current
    rows where module, matrix, and algebra constructors receive local
    `_RingObjectMethods` values but the external Sage constructor stubs expect a
    real Sage `Ring` or `Field`: `FreeModule` rows at
    `category_specs/modules/__init__.py:682`, `:700`, `:719`, and `:1148`;
    `VectorSpace` rows at `:771`, `:790`, and `:805`; `matrix` rows at
    `:737`, `:754`, `:823`, `:840`, `:878`, and `:892`, plus
    `category_specs/algebras/__init__.py:609` and
    `category_specs/tensor_algebra_components/__init__.py:148`. Inspected
    source shows these calls are inside local constructor collectors whose
    `base_ring()` method returns `cast("Ring", self.category().base_ring())`,
    but the receiver is statically `_RingObjectMethods` or a local category
    method container rather than a proven Sage ring/field. Owner is research
    code/typing: the missing fact is the local contract that these method
    receivers carry an actual Sage base ring, not a missing constructor surface.
    Required work is to make the local base-ring protocol explicit at the
    constructor boundary, and for `VectorSpace` additionally prove the base ring
    is a field before calling the Sage vector-space constructor. Acceptance is
    that these 15 rows disappear without broadening Sage constructors to accept
    arbitrary `_RingObjectMethods`. Falsifier would be source/runtime evidence
    that `_RingObjectMethods` is itself a concrete Sage `Ring`/`Field` subtype
    in every covered call path.

  - `RESEARCH-MODULE-CONSTRUCTOR-REFINEMENT-CONTRACT`: exact selector covers 27
    current rows in `category_specs/modules/__init__.py` where
    `_categories_for_free_module`, `_categories_for_quotient_module`, or
    `_refine_constructed_module` receives a Sage object typed as
    `FreeModule_generic`, `FreeModule_generic_field`, `CombinatorialFreeModule`,
    `Parent`, `ParentMethods`, or `_RingObjectMethods`, while the local helper
    requires `RModule`/`_RModObjects`. Inspected source defines
    `_refine_constructed_module(self, M: RModule, categories: Sequence[Category])`
    and `_categories_for_free_module(self, M: RModule)` inside
    `Modules._Constructors`, then immediately passes raw Sage constructor
    results such as `SageFreeModule(...)`, `SageVectorSpace(...)`,
    `CombinatorialFreeModule(...)`, quotient modules, and ring objects into the
    local refinement helper. Owner is research code/design: the helper assumes
    the constructed Sage parent already satisfies the local `RModule` method
    protocol before `refine_category` has supplied that category refinement.
    Required work is to split the pre-refinement Sage parent input type from
    the post-refinement `RModule` output type, or otherwise prove and encode
    the local protocol at the boundary. Acceptance is that all 27 helper rows
    disappear while preserving source-backed Sage constructor return types.
    Falsifier would be plugin evidence that `refine_category` should
    namespace-generically project the target method-container protocol onto a
    raw Sage parent before the call is type-checked.

  - `RESEARCH-CONSTRUCTORS-METHOD-CONFLICT`: exact selector covers the 16
    current `Constructors` method conflicts: the paired writable-final `misc`
    and incompatible-signature `override` rows at
    `category_specs/sets/__init__.py:1334` and `:1336`,
    `category_specs/topological_spaces/__init__.py:231` and `:233`,
    `category_specs/modules/__init__.py:1470` and `:1472`,
    `category_specs/algebras/__init__.py:679` and `:681`,
    `category_specs/rings/__init__.py:1965` and `:1967`,
    `category_specs/tensor_algebra_components/__init__.py:415` and `:417`,
    `category_specs/posets/__init__.py:753` and `:755`, and
    `category_specs/lattices/__init__.py:120` and `:122`. The inspected source
    declares local final cached `Constructors` methods returning
    category-specific constructor collectors such as `Sets._Constructors`,
    `Modules._Constructors`, and `Rings._Constructors`, while the Sage
    `Category` supertype already exposes a writable `Constructors` surface with
    a different callable contract. Owner is research code/design: this is a
    local API name collision with Sage's category constructor surface, not a
    missing external stub. Required work is to rename or re-home the local
    constructor collector, or align it with Sage's existing
    `Category.Constructors` contract without marking a writable inherited
    attribute final. Acceptance is that these 16 rows disappear without
    weakening Sage `Category` or making the plugin special-case local
    constructor collectors. Falsifier would be source evidence that the Sage
    `Category.Constructors` stub is wrong and the real Sage supertype has the
    same final cached-method contract as the local code.

  - `RESEARCH-HOM-END-AUT-CONSTRUCTION-CONTRACT`: exact selector covers 16
    current homset construction rows in `category_specs/homsets/homsets.py`,
    `endsets.py`, and `autsets.py`: local `ParentMethods`/`ElementMethods`
    assignments at `homsets.py:117`; `Of` signature conflicts at
    `homsets.py:144`, `endsets.py:147`, and `autsets.py:205`; the
    `default_super_categories` override row at `homsets.py:153`; local
    `HomCategory`, `EndCategory`, and `AutCategory` return rows at
    `homsets.py:161`, `endsets.py:113`, `:116`, `autsets.py:167`, and `:170`;
    and local `AutCategory*`/`EndCategory*` argument rows at `autsets.py:58`,
    `:131`, `:154`, `:160`, `:202`, and `:208`. Inspected source shows the
    project defines its own universal Hom/End/Aut object and element method
    surfaces in `category_specs/homsets/homsets.py`, `endsets.py`, and
    `autsets.py`, then maps them onto local category wrappers using narrowed
    `Of`, `from_end_category`, and refinement helpers. Owner is research
    mathematical/spec design: this is the local decision about whether Hom,
    End, and Aut categories are Sage categories, parents, condition subsets, or
    project method containers, and the current static contracts mix those roles.
    Required work is to settle the local Hom/End/Aut construction model and
    align `Of`, `default_super_categories`, provider method containers, and
    refinement helpers with the chosen Sage-compatible contracts. Acceptance is
    that these 16 rows disappear without weakening Sage `Category`, `Homsets`,
    or provider stubs. Falsifier would be a minimized namespace-generic Sage
    construction pattern proving that the plugin must project these narrowed
    `Of` and provider assignments generically despite ordinary Python supertype
    incompatibility.

  - `RESEARCH-AUTSET-INVERTIBILITY-PREDICATE`: exact selector covers
    `category_specs/homsets/autsets.py:36`, where `_is_invertible_endomorphism`
    calls `is_invertible` on a value typed as Sage `Morphism`. Sage runtime
    confirms `sage.categories.morphism.Morphism` does not expose
    `is_invertible`; the project-defined `UniversalHomElementMethods` declares
    `is_invertible`, and `UniversalEndElementMethods`/`UniversalAutElementMethods`
    refine that local protocol. Owner is research code/spec design: the
    predicate is typed against the wrong boundary if it intends a project
    endomorphism protocol, and it is not a missing Sage `Morphism` surface.
    Required work is to type the predicate input as the local endomorphism
    protocol actually required, or use a Sage-supported isomorphism/inversion
    predicate if this is meant to accept arbitrary Sage morphisms. Acceptance is
    that this row disappears without adding `is_invertible` to Sage `Morphism`
    stubs. Falsifier would be current Sage source/runtime evidence that the base
    `sage.categories.morphism.Morphism` class really provides
    `is_invertible`.

  - `RESEARCH-MATRIX-ALGEBRA-DELEGATE-CONTRACTS`: exact selector covers 12
    current rows in `category_specs/rings/matrix_algebras.py`: the
    `MatrixSpace` factory assignment at line `:57`, the `dims` callable
    assignment at `:109`, six `MatrixSpace.matrix` delegate assignments at
    `:119`, `:129`, `:139`, `:149`, `:196`, and `:203`, the `column_space` and
    `row_space` delegate assignments at `:173` and `:180`, the
    `diagonal_matrix` delegate assignment at `:188`, and the `from_vector`
    delegate assignment at `:228`. Inspected source declares local matrix-ring
    parent methods in `_MatrixAlgebras.ParentMethods` as returning project
    `RingElement`, `FreeModule`, or Sage `Integer` shapes, then assigns unbound
    Sage `MatrixSpace` methods whose source/runtime return ordinary Sage
    matrices, `FreeModule_generic`, or Python `int` tuples. Owner is research
    code/design: the local matrix-algebra method surface is claiming tighter
    project ring/module/Integer contracts than the delegated Sage methods
    provide. Required work is to decide whether matrix-space elements are
    represented as project `RingElement`s through a refinement step, or whether
    these methods should return the Sage matrix/free-module/int surfaces
    directly; then encode that boundary without weakening Sage stubs. Acceptance
    is that these 12 assignment rows disappear and the matrix-algebra wrapper
    has a coherent local element/module contract. Falsifier would be source
    evidence that the Sage `MatrixSpace` stubs currently return the wrong
    concrete types for these public methods.

  - `RESEARCH-SETPARTITION-ELEMENT-BRIDGE`: exact selector covers six
    non-override rows in `category_specs/sets/subcategories/partitioned.py`:
    the unsupported `self * other` operation at line `:201`, the two
    `is_less_than(self, other)` calls at lines `:216` and `:221`, and the three
    `Sets().Constructors().from_iterable(...)` calls over `list[SetPartition]`
    at lines `:226`, `:231`, and `:301`. Inspected local source defines
    `PartitionsCategory.ElementMethods` at lines `:165-305` while annotating
    the Sage element operations against the concrete Sage `SetPartition` alias
    from `category_specs/types.py:536`; the project constructors still type
    `from_iterable` as accepting project `SetElement` values at
    `category_specs/sets/__init__.py:558`. Sage runtime confirms actual Sage
    `SetPartition` objects support `*`, `sup`, `refinements`, `coarsenings`,
    `strict_coarsenings`, and `SetPartitions().is_less_than(p, q)`. Owner is
    research code/design: the local method-container `self` is not statically
    established as the Sage `SetPartition` element it is trying to refine, and
    the local finite-set constructor contract expects project set elements
    rather than concrete Sage `SetPartition` values. Required work is to make
    the local partition element boundary explicit: either model partition
    elements as the Sage `SetPartition` surface where these operations are used,
    or introduce a project partition-element protocol/adapter that owns `*`,
    `sup`, refinement lists, and parent order comparisons without weakening
    Sage stubs. Acceptance is that these six rows disappear while direct
    `SetPartition(...)` construction remains owned by
    `STUB-SETPARTITION-DIRECT-CLASSCALL` and the two `random_element` override
    rows remain covered by `RESEARCH-SETS-PROVIDER-SIGNATURE-MISMATCHES`.
    Falsifier would be evidence that current Sage stubs omit one of the
    concrete `SetPartition` methods used here; that specific row would then
    split to `sage-stubs` with Sage source/runtime proof.

  - `RESEARCH-RATIONALFIELD-NONPUBLIC-NUMBERFIELD-OVERRIDES`: exact selector
    covers the 27 current missing-base override rows in
    `category_specs/rings/subcategories/rational_field.py` for local
    `_QQ.ParentMethods` methods that are not public methods on Sage `QQ`:
    `is_algebraically_closed` at line `:75`, `is_quadratic` at `:96`,
    `is_cyclotomic` at `:101`, `trace_pairing_discriminant` at `:126`,
    `galois_group` at `:144`, `galois_closure` at `:155`, `integral_basis` at
    `:196`, `integral_basis_at_prime` at `:201`,
    `integral_basis_at_primes` at `:208`, `reduced_basis` at `:222`,
    `different` at `:227`, `real_embeddings` at `:239`,
    `complex_embeddings` at `:244`, `roots_of_unity` at `:249`, `regulator` at
    `:254`, `units` at `:259`, `unit_group` at `:264`, `conductor` at `:269`,
    `prime_above` at `:274`, `primes_above` at `:281`, `S_units` at `:288`,
    `S_class_group` at `:295`, `ring_of_integers_at_prime` at `:314`,
    `ring_of_integers_at_primes` at `:327`, `maximal_order_at_prime` at `:352`,
    `maximal_order_at_primes` at `:365`, and `absolute_field` at `:378`.
    Inspected local source implements these methods by first constructing
    `as_number_field()` at lines `:84-91` and then delegating many methods to
    that auxiliary number field. Sage runtime evidence for the claimed QQ
    surface is negative:
    Searched: `sage.all.QQ` with `hasattr` for all 40 override names, current
    `sage-src/src/sage/rings/rational_field.py`, and current
    `sage-stubs/rings/rational_field.pyi`.
    Found: these 27 names are absent from `QQ`; several exist only on number
    field classes or on the locally constructed `as_number_field()` target.
    Conclusion: inference based on the inspected runtime/source/stub surface:
    these are local research/spec decisions about whether the rational field
    category should expose number-field-like operations through its own provider
    surface, not real `RationalField` methods that stubs should add.
    Confidence: High for absence from current QQ runtime; Medium for the
    mathematical/spec decision about which of these operations should be local
    category methods.
    Classification boundary: no Sage design documentation found in this pass
    makes these absent QQ methods external stub or plugin work.
    Owner is research mathematical/spec design. Required work is to decide
    which number-field operations belong on the local rational-field category,
    remove `@override` from methods that intentionally introduce new local
    provider methods, and avoid advertising methods as Sage QQ overrides when
    the QQ parent does not expose them. Acceptance is that these 27 rows
    disappear without adding non-runtime QQ methods to `sage-stubs` and without
    asking the plugin to validate project-specific number-field delegation.
    Falsifier would be current Sage runtime/source evidence that a covered name
    is actually a public QQ/RationalField method; that row must then split to
    `STUB-RATIONALFIELD-MISSING-PUBLIC-METHODS` or provider override-base
    visibility depending on whether the stub already exposes it.

  - `RESEARCH-PYTHON-DUNDER-INT-CONTRACTS`: exact selector covers five current
    rows where local specs annotate Python dunder methods with Sage `Integer`
    where Python and Sage supertypes require builtin `int`: `__hash__` in
    `category_specs/sets/__init__.py:343` and
    `category_specs/sets/subcategories/image.py:78`, plus `__len__` in
    `category_specs/sets/subcategories/recursively_enumerated.py:55`,
    `category_specs/sets/subcategories/finite.py:53`, and
    `category_specs/sets/subcategories/family.py:83`. Inspected source shows
    the local annotations use the project/Sage `Integer` alias even when the
    implementation delegates to Python `hash(...)`, `len(...)`, or Sage
    enumerated-set methods whose stubs return `int`. Owner is research
    code/typing: this is the local boundary between Sage numeric values and
    Python protocol methods; `int` and `ZZ`/`Integer` are not interchangeable,
    but Python dunder protocols specifically require builtin `int` return
    values. Required work is to type `__hash__` and `__len__` as returning
    `int`, and convert explicitly only at non-dunder Sage cardinality/rank
    boundaries where a Sage `Integer` is mathematically required. Acceptance is
    that these five rows disappear without weakening Sage `Integer` stubs or
    treating all integer-like values as interchangeable. Falsifier would be
    source-backed evidence that one of these rows is not a Python protocol
    method and is instead a Sage-specific method whose public contract really
    returns `Integer`.

  - `RESEARCH-CONSTRUCTION-SELECTOR-CLASSCALL-BRIDGE`: exact selector covers
    eleven current `Too few arguments` call rows where a local category
    construction selector is called with no explicit base category but the
    static surface resolves to the raw construction-category class initializer:
    `Sets().Constructors()._real_set_categories` calls
    `topological_spaces.Subobjects()` at `category_specs/sets/__init__.py:654`;
    ring and lattice homset refinement calls use `Rings().HomCategory()` at
    `category_specs/rings/homsets.py:60` and `Modules(R).HomCategory()` at
    `category_specs/lattices/homsets.py:63`; module constructor helpers call
    `C.Subobjects()` and `C.Quotients()` at `category_specs/modules/__init__.py:592`
    and `:601`; tensor component categories call
    `Modules(R).HomCategory().Forms().Integral()` and `RMod.TensorProducts()` at
    `category_specs/tensor_algebra_components/__init__.py:167` and `:195`;
    algebra ideals call `Modules(self.base_ring()).Subobjects()` at
    `category_specs/algebras/subcategories/constructions/ideals.py:41`;
    orthogonal direct sums call `Lattices(self.base_ring()).CartesianProducts()`
    at `category_specs/lattices/subcategories/constructions/orthogonal_direct_sums.py:30`;
    integer lattices call `Modules(R).Subobjects()` at
    `category_specs/modules/subcategories/integer_lattices.py:31`; and real
    sets call `TopologicalSpaces().Subobjects()` at
    `category_specs/sets/subcategories/real_set.py:51`. Inspected source shows
    local category classes assign construction-category classes directly, e.g.
    `TopologicalSpaces.Subobjects = _Subobjects`,
    `Modules.Subobjects = _Subobjects`, `Modules.Quotients = _Quotients`,
    `Modules.TensorProducts = _TensorProducts`, `Rings.HomCategory =
    RingHomCategory`, and `Lattices.CartesianProducts = _CartesianProducts`;
    the wrapped construction bases in `category_specs/cat/base_category_types.py`
    require `__init__(self, category: SageCategory)`. Owner is research
    code/design: this is the local bridge between zero-argument category
    selector syntax and raw construction-category classes requiring a base
    category, not a named missing Sage stub surface and not a plugin request to
    understand `category_specs` class aliases. Required work is to make local
    construction selectors type as cached category-owned methods calling
    `category_of(base_category)` or otherwise separate selector methods from
    construction-category class objects so zero-argument calls do not target raw
    initializers. Acceptance is that these eleven `Too few arguments` rows
    disappear without weakening the construction-category `__init__` signatures
    or adding fake zero-argument constructors. Falsifier would be a minimized
    namespace-generic Sage category pattern, independent of these local aliases,
    proving the plugin must rewrite raw construction-class attributes into
    selector methods generically.

  - `RESEARCH-MODULE-SUBOBJECT-CATEGORY-ABSTRACT-CONTRACT`: exact selector
    covers the three current rows reporting `Cannot instantiate abstract class
    "_Subobjects" with abstract attribute "as_subobject_of_self"` at
    `category_specs/modules/__init__.py:592`,
    `category_specs/algebras/subcategories/constructions/ideals.py:41`, and
    `category_specs/modules/subcategories/integer_lattices.py:31`. Inspected
    source shows
    `category_specs/modules/subcategories/constructions/subobjects.py:20-90`
    defines `_Subobjects(SubobjectsCategory)` and declares
    `as_subobject_of_self` as an abstract method directly on the construction
    category class, not in `ParentMethods`; the call sites are constructing or
    selecting the module subobject category itself. Owner is research
    mathematical/spec design: the current local contract has not decided
    whether `as_subobject_of_self` is a concrete category-level helper, a
    parent/provider method, or a required method on some concrete submodule
    category. Required work is to place or implement this obligation at the
    correct local surface before `Modules(R).Subobjects()` is treated as an
    instantiable category. Acceptance is that these three abstract-class rows
    disappear without deleting the mathematical obligation or hiding it behind
    a stub/plugin change. Falsifier would be source evidence that Sage's
    `SubobjectsCategory` itself declares the same abstract method and expects
    downstream construction-category classes to remain abstract at selector
    call sites.

  - `RESEARCH-ABSTRACT-PLACEHOLDER-FALLTHROUGH`: exact selector covers four
    current `Missing return statement` rows in abstract method bodies, excluding
    the Cat homset row already owned by `RESEARCH-CAT-HOMSETS-SPEC-MISMATCH`:
    `category_specs/sets/subcategories/recursively_enumerated.py:125`,
    `category_specs/modules/subcategories/integer_lattices.py:49`,
    `category_specs/modules/subcategories/integer_lattices.py:65`, and
    `category_specs/lattices/subcategories/over_integers.py:56`. Inspected
    source shows each method is decorated `@abstractmethod` but contains one or
    more `del ...` statements before the placeholder ellipsis, so mypy treats
    the body as executable fallthrough rather than a pure stub-style abstract
    placeholder. Owner is research code/typing: these are local abstract
    provider placeholders, not missing Sage methods or plugin dynamic-category
    semantics. Required work is to make abstract placeholder bodies type-correct
    without weakening the method signatures, e.g. remove the `del` statements
    from abstract placeholders or use a non-returning abstract placeholder body
    consistently. Acceptance is that these four missing-return rows disappear
    while the abstract obligations and signatures remain present. Falsifier
    would be evidence that a covered method is not abstract local spec surface
    but a concrete Sage-backed implementation whose body should delegate to a
    real Sage method instead.

  - `RESEARCH-REFINE-CATEGORY-NON-PARENT-PROTOCOLS`: exact selector covers nine
    current type-variable rows where `category_specs.utils.refine_category` is
    called on values typed as local provider protocols or method-container
    surfaces that are not statically Sage `Parent`s:
    `category_specs/homsets/autsets.py:58` (`UniversalAutObjectMethods`),
    `category_specs/sets/__init__.py:680` (`_RealSets.ParentMethods`),
    `category_specs/rings/homsets.py:60` (`_RingHomCategoryObjectMethods`),
    `category_specs/rings/homsets.py:87` (`RingEndCategory.ParentMethods`),
    `category_specs/sets/subcategories/constructions/subobjects.py:53`
    (`Subsets.ParentMethods`), `category_specs/modules/__init__.py:573`
    (`_RModObjects`), `category_specs/algebras/__init__.py:429`
    (`_AlgebraParentMethods`), `category_specs/algebras/__init__.py:437`
    (`_MagmaticAlgebraParentMethods`), and
    `category_specs/tensor_algebra_components/__init__.py:263`
    (`_TensorAlgebraComponentParentMethods`). Inspected source shows
    `refine_category` is explicitly typed as
    `def refine_category[_ParentT: Parent](X: _ParentT, ...) -> _ParentT` in
    `category_specs/utils.py:241-252`, while these call sites pass local
    category provider protocols or method containers rather than values whose
    local type establishes the Sage `Parent` base. Owner is research
    code/typing: the local type aliases and helper signatures are conflating
    provider-method surfaces with the runtime parent objects being refined.
    Required work is to make the runtime parent boundary explicit at each call
    site or in the relevant local type aliases, without relaxing
    `refine_category` to accept non-parent objects and without adding fake
    parent bases to local protocols. Acceptance is that these nine type-variable
    rows disappear while `refine_category` remains bounded to real Sage
    parents. Falsifier would be source/runtime evidence that a covered local
    protocol is itself a concrete Sage `Parent` class rather than a provider
    surface; that row must then split to a stub hierarchy issue if the stub
    omits the parent base.

  - `RESEARCH-CATEGORY-RETURN-CONTRACT-BOUNDARIES`: exact selector covers 15
    current `return-value` rows where local category methods return concrete
    Sage/project category objects or category containers that do not match the
    local annotation: `category_specs/sets/__init__.py:378`, `:462`;
    `category_specs/rings/subcategories/constructions/rings_over.py:34`;
    `category_specs/rings/subcategories/constructions/rings_under.py:28`;
    `category_specs/modules/__init__.py:477`;
    `category_specs/algebras/__init__.py:115`, `:324`, `:390`;
    `category_specs/rings/__init__.py:1973`;
    `category_specs/posets/__init__.py:251`; and
    `category_specs/forms/subcategories/bilinear.py:145`, `:152`, `:159`,
    `:166`, and `:173`. Inspected source shows three concrete shapes: local
    `_sage_super_categories` methods annotated with project `Category` return
    raw Sage categories such as `SageSets()`, `SageBimodules(...)`,
    `SageAlgebras(...)`, `SageRings()`, or `SagePosets()`; construction
    `default_super_categories` methods are annotated as `list[Category]` but
    return `Category.join(...)`; and local cached category methods such as
    `GSets`, `Ideals`, and bilinear form refinements are annotated as project
    `Category` while returning concrete local category classes. Owner is
    research code/design: these rows are caused by local return annotations and
    wrapper/category boundary choices, not by a single missing Sage API surface
    and not by a generic plugin rule. Required work is to split the local
    category return contracts so Sage super-category hooks return Sage category
    objects where appropriate, local category factories return project category
    wrappers with an explicit common base/protocol, and `default_super_categories`
    either returns a list or changes its declared contract if a joined category
    is the intended value. Acceptance is that these 15 return rows disappear
    without weakening Sage category stubs to accept arbitrary project wrappers
    and without using broad casts to hide an unresolved wrapper relation.
    Falsifier would be a row-specific proof that the returned concrete class is
    already a subtype of the annotated local category surface and the error is
    solely due to a missing source-backed Sage stub base.

  - `RESEARCH-SETPARTITION-BASE-NORMALIZATION-UNION`: exact selector covers the
    single current `return-value` row at `category_specs/sets/__init__.py:549`,
    where `_set_partitions_base` returns a `CategoryObject` branch for fixed
    base sets but the declared first tuple component excludes `CategoryObject`.
    Inspected source at `category_specs/sets/__init__.py:540-551` admits three
    input shapes: Sage `Integer`, `CategoryObject` in `Sets()`, and iterable
    element data. Owner is research code/typing: the helper's local normalized
    return union does not match one of its documented branches. Required work
    is to include the `CategoryObject` branch in the normalized return type or
    normalize that branch into one of the existing admitted shapes before
    returning. Acceptance is that this row disappears while the fixed-base
    `SetPartitions` constructor keeps the three intended input cases.
    Falsifier would be source/runtime evidence that the `CategoryObject` branch
    is impossible or should be rejected before return.

  - `RESEARCH-FIELD-COMPLETION-ZERO-IDEAL-BRANCH`: exact selector covers the
    single current `return-value` row at
    `category_specs/rings/subcategories/field.py:144`, where
    `_Fields.ParentMethods.completion` is annotated as returning `CompleteRing`
    but returns `self` for the zero ideal branch. Inspected source at
    `category_specs/rings/subcategories/field.py:139-145` explicitly splits
    zero and nonzero/unit ideal cases; the zero branch returns the original
    field provider surface, while the other branch returns the zero ring
    constructor. Owner is research mathematical/spec design: the local spec must
    decide whether a field is already complete in this category sense, whether
    the zero-ideal completion should be represented by a complete-ring
    refinement of `self`, or whether the method return contract is broader than
    `CompleteRing`. Required work is to record and encode that branch contract
    without adding fake Sage completeness stubs. Acceptance is that this row
    disappears and the zero-ideal branch has an explicit local type/spec
    justification. Falsifier would be source-backed evidence that
    `_Fields.ParentMethods` is already a subtype of `_CompleteRings.ParentMethods`
    in the current local category hierarchy.

  - `RESEARCH-HOMCATEGORY-CLASS-ATTRIBUTE-CONTRACT`: exact selector covers the
    nine current `assignment` rows where a local category class assigns a
    concrete Hom-category class object to `HomCategory` while the inherited
    local/Sage category surface expects a zero-argument callable returning a
    category: `category_specs/sets/__init__.py:1340`,
    `category_specs/topological_spaces/subcategories/metric.py:75`,
    `category_specs/topological_spaces/__init__.py:184`,
    `category_specs/modules/__init__.py:1724`,
    `category_specs/algebras/__init__.py:347`,
    `category_specs/rings/__init__.py:2165`,
    `category_specs/tensor_algebra_components/__init__.py:423`,
    `category_specs/posets/__init__.py:790`, and
    `category_specs/lattices/__init__.py:197`. Inspected source shows each row
    is a local class-level assignment such as `HomCategory = SetHomCategory` or
    `HomCategory = RModuleHomCategory`, not a call to a missing Sage API.
    Owner is research code/design: the local category framework must decide
    whether Hom-category selectors are callable cached methods, class attributes
    containing construction classes, or lazy interop hooks, then make the base
    and subclasses agree. Required work is to align the local HomCategory
    selector/class-attribute contract across category classes without changing
    Sage stubs to accept project-specific assignment patterns. Acceptance is
    that these nine assignment rows disappear and Hom-category construction
    still routes through the intended Sage-compatible category selector.
    Falsifier would be source-backed evidence that Sage's public `Category`
    class itself declares `HomCategory` as a class object slot compatible with
    these assignments rather than a callable/category selector surface.

  - `RESEARCH-LOCAL-BOUNDARY-ASSIGNMENT-LEAKS`: exact selector covers six
    current `assignment` rows where local code assigns a broader Sage/project
    value to a narrower project alias without proving the boundary:
    `category_specs/homsets/autsets.py:28` and `:30` assign Sage `Category`
    results through `EndCategory()`/`HomCategory()` branches to a local
    `Category`-typed variable; `category_specs/sets/__init__.py:984` widens a
    cartesian-product `product_category` control-flow variable to
    `tuple[Any, ...]`; `category_specs/tensor_algebra_components/__init__.py:235`
    and `category_specs/lattices/__init__.py:117` assign `Category | Parent` or
    Sage `Ring` base-ring values to local `_RingObjectMethods`/`Ring` surfaces;
    and `category_specs/rings/subcategories/polynomial_ring.py:88` assigns a
    generic local `_RingElementMethods` ideal generator to the narrower
    `Polynomial` alias. Owner is research code/typing: each row is a local
    boundary proof or narrowing obligation between Sage objects, project
    aliases, and wrapper/provider protocols, not a named missing Sage surface.
    Required work is to add source-grounded local narrowing or adjust the local
    alias/helper return contracts so each assignment target is justified by the
    value actually produced, without using broad opacity or weakening Sage
    stubs. Acceptance is that these six assignment rows disappear with the
    boundary made explicit at each source location. Falsifier would be
    row-specific Sage source/runtime evidence that the right-hand side already
    has the narrower assigned type and the current error is solely caused by a
    missing external stub base.

  - `RESEARCH-LOCAL-PREDICATE-OVERRIDE-MARKERS`: exact selector covers 33
    current `misc` rows whose message is `Method "<predicate>" is marked as an
    override, but no base method was found with this name` for local predicate
    or truth-marker methods outside the separately classified rational-field
    block: `is_facade`, `is_countable`, `is_uncountable`, `is_metric`,
    `has_form`, `is_quadratic`, `is_bilinear`, `is_symmetric`, `is_rational`,
    `is_nondegenerate`, `is_integral`, `is_alternating`, `is_free`,
    `is_local_field`, `is_complete_discrete_valuation_field`,
    `is_ring_object_as_module`, `is_representation_module`, `is_ore_module`,
    `is_lattice`, `is_graded`, `is_free_graded_module`,
    `is_finitely_presented_graded_module`, `is_indefinite`, `is_definite`,
    `is_positive_definite`, `is_negative_definite`, and `is_anisotropic`.
    Inspected representative source shows these are local category predicates:
    `category_specs/forms/subcategories/with_forms.py:34-40` records
    `_defining_predicates = ("has_form",)` and returns `True`;
    `category_specs/forms/subcategories/bilinear.py:36-48` records
    `_defining_predicates = ("is_bilinear",)` and returns `True`;
    `category_specs/modules/subcategories/free_graded_modules.py:38-47`
    locally introduces `is_graded` and `is_free_graded_module`;
    `category_specs/modules/subcategories/integer_lattices.py:39-43`
    locally introduces `is_lattice`; and
    `category_specs/topological_spaces/subcategories/metric.py:27-33`
    locally introduces `is_metric`. Owner is research code/spec design: these
    methods either introduce local category predicates or assert membership in
    a local subcategory, but they are marked as overriding an inherited provider
    method that the current static base chain does not contain. Required work is
    to decide, per predicate, whether it should be declared on an upstream local
    provider base, kept as a new local method without `@override`, or routed to
    a real Sage provider method if one exists on the relevant category. Acceptance
    is that these 33 no-base rows disappear without adding fake predicate
    methods to Sage stubs and without deleting the mathematical predicates.
    Falsifier would be row-specific Sage source evidence that the exact
    predicate is a real method on the relevant Sage category provider base; that
    row must then split to `sage-stubs` if the stub omits it, or to plugin if
    the stub has it but provider-base projection hides it.

  - `RESEARCH-LOCAL-PROVIDER-PROTOCOL-MRO-CONFLICTS`: exact selector covers the
    83 current non-`cat/**` `misc` rows whose message starts `Definition of`
    and does not involve `_CatObjectMixin`. Representative rows include
    `category_specs/rings/subcategories/constructions/rings_over.py:22` and
    `rings_under.py:18`, where local construction categories inherit both a
    construction category and `Category_over_base_ring` whose `base_ring`
    contract conflicts with `Parent`; set finite/enumerated subcategories such
    as `category_specs/sets/subcategories/finite_enumerated_set.py:32`, where
    local `ParentMethods` refine `__len__`, `_an_element_`, and
    `random_element` across multiple provider bases; module/algebra protocol
    compositions such as `category_specs/algebras/subcategories/with_basis.py:53`
    and `finite_dimensional_with_basis.py:35`, where local algebra,
    ring-object, set-object, and module-object provider protocols expose
    incompatible `cardinality`, `intersection`, `one`, `quotient_module`,
    `submodule`, `tensor`, `zero`, and related methods; and hom-with-basis
    compositions such as `category_specs/modules/subcategories/with_basis.py:140`
    and `:148`, where local hom and element protocols disagree on `__call__`,
    `zero`, `parent`, and `tensor`. Owner is research code/design: these are
    ordinary Python MRO conflicts introduced by composing local provider
    protocols and method containers with incompatible method signatures, not a
    single missing Sage API and not a namespace-generic plugin projection gap.
    Required work is to split or reconcile the local provider protocols so each
    concrete method container has one coherent method contract for every
    inherited name, preserving real Sage signatures where they are source-backed
    and moving mathematical refinements to distinct local names or narrower
    protocols when needed. Acceptance is that these 83 MRO rows disappear
    without weakening existing Sage/provider stubs, deleting method obligations,
    or using opaque escape types. Falsifier would be row-specific evidence that
    all conflicting base methods are actually the same runtime Sage provider
    method and current stubs/plugin projection, rather than local protocol
    composition, caused mypy to see incompatible contracts.

  - `RESEARCH-LOCAL-CATEGORY-HOOK-MARKERS`: exact selector covers three current
    no-base override rows where the method name is a local category framework
    hook rather than an external Sage API currently available on the inherited
    static base: `category_specs/homsets/homsets.py:153`
    (`default_super_categories` on local `HomCategoryConstruction`),
    `category_specs/modules/__init__.py:476` (`_sage_super_categories`), and
    `category_specs/algebras/__init__.py:323` (`_sage_super_categories`).
    Inspected source shows `HomCategoryConstruction` deliberately models the
    project-owned functorial assignment `Hom_*: Cat -> Cat` and says Sage's
    `HomsetsCategory` is inventory/interop vocabulary, not the source of
    mathematical inheritance; the two `_sage_super_categories` methods are
    project-local bridges for choosing Sage supercategories while the public
    Sage hook remains `super_categories`. Owner is research code/design: these
    override markers assert a local framework contract that is not present in
    the inherited local base. Required work is to make the local framework base
    declare these hooks, rename them to non-override helpers, or route them
    through the actual Sage hook with a source-backed contract. Acceptance is
    that these three rows disappear without adding fake `_sage_super_categories`
    methods to Sage stubs or asking the plugin to know local hook names.
    Falsifier would be source/runtime evidence that the exact local receiver
    class should inherit Sage `HomsetsCategory.default_super_categories` or a
    Sage `_sage_super_categories` method with this spelling.

  - `RESEARCH-IDEAL-GENERATORS-AS-FREE-MODULE-ELEMENTS`: exact selector covers
    the single current `misc` row at `category_specs/modules/__init__.py:1149`
    where `SageFreeModule(R, 1).submodule([[generator] for generator in
    ideal.gens()])` is inferred as `List[list[_RingElementMethods]]` but the
    free-module submodule surface expects `List[FreeModuleElement]`. Inspected
    source shows this is local bridge code converting ideal generators into a
    rank-one module subobject; the missing fact is not a named Sage API but the
    local representation boundary between ring elements used as coordinates and
    actual free-module elements. Owner is research code/typing. Required work
    is to construct or coerce rank-one free-module elements through a
    source-backed Sage entry point, or change the local helper contract so the
    coordinate-list form is explicitly accepted at this boundary. Acceptance is
    that the line `:1149` row disappears without weakening `FreeModuleElement`
    or replacing ring/module element contracts with opacity. Falsifier would be
    Sage source/stub evidence that `FreeModule_generic.submodule` is currently
    supposed to accept raw coordinate rows typed as `list[RingElement]` under
    this public signature.

  - `RESEARCH-FOLDABLE-OPERATION-TYPE-SIGNATURE`: exact selector covers the two
    current overload-implementation rows at
    `category_specs/posets/subcategories/meet_semilattice.py:61` and
    `category_specs/posets/subcategories/join_semilattice.py:61`. Inspected
    source shows each method declares both binary and sequence overloads, but
    under `TYPE_CHECKING` the local `foldable_operation` decorator is typed as
    identity, so mypy checks the undecorated implementation
    `(self, x, y)` against the one-argument sequence overload. Owner is research
    code/typing: the runtime decorator in `category_specs/utils.py:119-146`
    really wraps the binary operation into a foldable binary-or-sequence
    method, but the static decorator signature intentionally hides that
    transformation. Required work is to give the decorator a source-backed
    overloaded type that reflects the wrapper, or write an explicit
    implementation signature accepting both call shapes. Acceptance is that
    these two rows disappear while keeping the binary and sequence semantics.
    Falsifier would be evidence that Sage itself supplies this decorator and
    current stubs misrepresent it; current source shows the decorator is local.

  - `RESEARCH-REAL-PRECISION-CHANGE-METHOD`: exact selector covers the single
    no-base override row at
    `category_specs/rings/subcategories/real_precision_field.py:71` for
    `change_precision`. Inspected source shows the local method delegates to
    Sage `to_prec` branches after asserting the optional `precision_type` is
    `None`. Negative finding:
    Searched: `rg change_precision` over Sage source and stubs under
    `/home/dzack/sage-mypy-plugin/sage-stubs`, plus Sage runtime on
    `RealField(53)`, `RealIntervalField(53)`, `RealBallField(53)`, and `RDF`.
    Found: no Sage source/stub method named `change_precision`; runtime reports
    `hasattr(..., "change_precision") == False` for the tested real fields,
    while `precision` and `prec` exist. Conclusion: inference, this is a local
    convenience method over Sage `to_prec`, not an external Sage method. Confidence:
    High for the tested real precision fields. Classification boundary: the
    receiver family used by this local category does not expose
    `change_precision`; unrelated Sage classes are outside this current row
    family. Owner is research
    code/design. Required work is to remove the `@override`, declare the local
    method in a local base protocol, or rename the helper to avoid claiming a
    Sage override. Acceptance is that the line `:71` row disappears without
    adding fake `change_precision` to Sage stubs. Falsifier would be current
    Sage source/runtime evidence that one of the real precision-field parent
    classes exposes `change_precision`.

  - `RESEARCH-PUISEUX-SERIES-EXTENSION-CONTRACT`: exact selector covers the
    single no-base override row at
    `category_specs/rings/subcategories/puiseux_series_ring.py:55` for
    `extension`. Negative finding: Searched: Sage source/stubs for
    `PuiseuxSeriesRing` and `def extension`, plus Sage runtime on
    `PuiseuxSeriesRing(QQ, "t")`. Found: Sage source
    `sage/rings/puiseux_series_ring.py` defines Puiseux series ring
    construction, base extension, change ring, and fraction field behavior, but
    no `extension` method on `PuiseuxSeriesRing`; runtime reports
    `hasattr(PuiseuxSeriesRing(QQ, "t"), "extension") == False`. Conclusion:
    inference, the local method is a research/spec convenience surface, not a
    public Sage Puiseux-series method. Confidence: High for the current
    PuiseuxSeriesRing receiver. Classification boundary: this row concerns only
    the PuiseuxSeriesRing receiver; extension methods on other ring families are
    separate families when they appear in the current ledger. Owner is research
    code/spec design. Required work
    is to remove or locally declare this method instead of marking it as a Sage
    override, or redesign the Puiseux-series subcategory if the intended
    operation is `base_extend`, `change_ring`, or `fraction_field`. Acceptance
    is that the line `:55` row disappears without adding a fake Puiseux
    `extension` stub. Falsifier would be current Sage source/runtime evidence
    that `PuiseuxSeriesRing` exposes an `extension` method.

  - `RESEARCH-CAT-WRAPPER-OVERRIDE-BOUNDARIES`: exact selector covers ten
    current `override` rows in `category_specs/cat/**` that remain after the
    separately recorded category-return-list and Hom-category rows: indices
    `9`, `21`, `26`, `30`, `60`, `117`, `157`, `160`, `161`, and `163`.
    Representative rows are `base_category_types.py:602` and `cat/__init__.py:250`,
    where local `join`/`meet` narrow Sage `Category` arguments to local
    `Category`; `base_category_types.py:648`, `:686`, and `:718`, where local
    `defining_predicate` narrows Sage's `object` predicate argument; and
    `cat/__init__.py:214`, where local `_make_named_class` narrows the method
    provider argument. Owner is research code/design: these rows are caused by
    the local Cat wrapper layer tightening Sage category signatures at the
    wrapper boundary. Required work is to make the wrapper API
    Liskov-compatible with Sage where it overrides Sage methods, and move
    project-specific narrowing behind local helpers or checked adapters.
    Acceptance is that these ten rows disappear without weakening Sage stubs or
    asking the plugin to know `Cat`. Falsifier would be row-specific evidence
    that Sage runtime itself exposes the narrower local signature on the same
    upstream method.

  - `RESEARCH-HOMSET-SPECIALIZATION-OVERRIDE-CONTRACTS`: exact selector covers
    ten current `override` rows where local hom-object and morphism providers
    specialize the universal homset contracts too narrowly: indices `153`,
    `154`, `155`, `156`, `322`, `323`, `324`, `325`, `845`, and `846`.
    Representative rows include `category_specs/cat/homsets.py:27` and `:40`,
    where Cat hom objects/elements return `Functor` or `Category` where the
    universal hom surface expects `Morphism` or `Element`;
    `category_specs/modules/homsets.py:68-80`, where module homsets narrow
    domain/codomain/call results to local module protocols; and
    `category_specs/algebras/homsets.py:31`, where algebra kernels refine
    module/ring kernel return contracts inconsistently. Owner is research
    code/spec design: these rows are not plugin projection failures, because
    mypy is seeing the relevant local bases and rejecting incompatible local
    refinements. Required work is to split universal hom contracts by hom
    flavor, introduce variance-compatible local protocols, or adjust the local
    mathematical claim for Cat/module/algebra homsets. Acceptance is that these
    ten rows disappear without weakening the universal hom surface to accept
    unrelated category, element, and morphism concepts. Falsifier would be
    evidence that Sage's runtime homset hierarchy permits these exact
    incompatible specializations under a generic category-provider rule that the
    plugin should model.

  - `RESEARCH-CONSTRUCTION-CATEGORY-OVERRIDE-BOUNDARIES`: exact selector covers
    five current `override` rows in construction-category classes: indices
    `213`, `298`, `299`, `856`, and `1412`. These rows are
    `extra_super_categories` returning `list[LatticesCategory]` instead of
    Sage `list[Category]`, and `default_super_categories` methods on local
    rings-over/rings-under construction categories whose signatures disagree
    with Sage `CovariantConstructionCategory` /
    `RegressiveCovariantConstructionCategory`. Owner is research code/design:
    these are local construction category signatures that narrow Sage
    construction-category hooks. Required work is to make local construction
    categories return/source Sage-compatible category lists and match Sage
    classmethod signatures, while keeping local lattice/ring categories
    available through checked local adapters. Acceptance is that these five
    rows disappear without changing Sage construction stubs to accept local
    category aliases. Falsifier would be current Sage source/stub evidence that
    the upstream construction hook is typed with the narrower local category
    signature.

  - `RESEARCH-SETS-PARENTMETHODS-OVERRIDE-REFINEMENTS`: exact selector covers
    99 current `override` rows under `category_specs/sets/**` after excluding
    already-recorded local category-list returns and Python-dunder rows. The
    row set is `246`, `247`, `248`, `249`, `259`, `260`, `261`, `262`, `263`,
    `348`, `349`, `350`, `351`, `352`, `354`, `359`, `360`, `361`, `363`,
    `364`, `367`, `369`, `370`, `387`, `388`, `389`, `396`, `411`, `412`,
    `423`, `424`, `425`, `426`, `428`, `429`, `431`, `437`, `438`, `439`,
    `440`, `448`, `449`, `452`, `453`, `456`, `458`, `459`, `470`, `475`,
    `476`, `480`, `482`, `483`, `484`, `490`, `496`, `498`, `499`, `503`,
    `504`, `512`, `515`, `539`, `540`, `542`, `544`, `546`, `547`, `555`,
    `563`, `564`, `567`, `568`, `580`, `581`, `593`, `594`, `604`, `605`,
    `607`, `608`, `610`, `612`, `613`, `616`, `617`, `618`, `619`, `816`,
    `817`, `818`, `819`, `820`, `822`, `824`, `826`, `829`, `831`, and `833`.
    Representative inspected source shows local set provider methods narrowing
    Sage `object`/`Element`/`Parent`/`int` surfaces to project aliases such as
    `SetElement`, `_SetElementMethods`, `_SetObjectMethods`, `Integer`,
    `SetMorphism`, and local real-set subset protocols. Owner is research
    code/typing and mathematical contract design: the local set hierarchy must
    decide where project-specific element/set protocols are proven subtypes of
    Sage `Element`/`Parent`, and where public Sage override signatures must
    remain broad. Required work is to make each local set provider override
    signature compatible with the Sage/local base it claims to override, adding
    checked local wrappers or separate local methods where narrower contracts
    are mathematical conveniences. Acceptance is that all 99 rows disappear
    without weakening Sage stubs, using opaque escape types, or pretending
    `Integer` and Python `int` are interchangeable. Falsifier would be
    row-specific evidence that a Sage stub gives the wrong upstream signature
    for the exact set-provider method.

  - `RESEARCH-POSETS-PARENTMETHODS-OVERRIDE-REFINEMENTS`: exact selector covers
    28 current `override` rows under `category_specs/posets/**` after excluding
    already-recorded category-list returns. The row set is `1246`, `1247`,
    `1248`, `1249`, `1250`, `1251`, `1252`, `1253`, `1254`, `1255`, `1256`,
    `1257`, `1258`, `1259`, `1265`, `1280`, `1284`, `1289`, `1298`, `1299`,
    `1302`, `1379`, `1380`, `1381`, `1382`, `1383`, `1384`, and `1385`.
    Representative rows show local poset provider methods narrowing Sage
    `Iterable[object]`, `object`, `Parent`, and `list[object]` surfaces to
    `_PosetElementMethods`, `_PosetParentMethods`, or local `Category` return
    aliases. Owner is research code/typing and spec design: these are local
    poset/lattice protocol refinements against visible Sage category-provider
    methods, not missing base discovery. Required work is to reconcile the
    local poset element/parent protocols with Sage's broad public
    `Posets.ParentMethods`, `FinitePosets.ParentMethods`, and
    `FiniteLatticePosets.ParentMethods` signatures, using checked adapters for
    local mathematical refinements. Acceptance is that these 28 rows disappear
    without degrading Sage method signatures or erasing local poset semantics.
    Falsifier would be row-specific Sage source/stub evidence that the upstream
    method signature is wrong or absent.

  - `RESEARCH-MODULE-RING-ALGEBRA-FORM-OVERRIDE-REFINEMENTS`: exact selector
    covers the remaining 26 current `override` rows outside `cat`, `sets`,
    `posets`, and the separately recorded homset/construction/rational-field
    families: indices `312`, `526`, `533`, `631`, `633`, `635`, `636`, `648`,
    `838`, `862`, `876`, `877`, `987`, `992`, `1117`, `1187`, `1345`, `1403`,
    `1404`, `1545`, `1635`, `1636`, `1637`, `1651`, `1730`, and `1736`.
    Representative rows include local module subobject methods narrowing set
    subset operators, local ring/algebra methods narrowing Sage `Parent` or
    ring-object returns, algebra generator methods returning `AbstractFamily`
    where Sage expects tuples of elements, form methods returning local
    bilinear forms where module form protocols expect module morphisms, and
    real/algebraic field `nth_root` signatures disagreeing with local ring
    element contracts. Owner is research code/typing and mathematical contract
    design: each row is an incompatible local override refinement against a
    visible Sage or local provider method, not a missing Sage surface or a
    plugin inability to find the base. Required work is to make the local
    module/ring/algebra/form protocols variance-compatible with their visible
    bases, or split local mathematical conveniences into non-override methods
    with explicit adapters. Acceptance is that these 26 rows disappear without
    type weakening, `Any`/`object` opacity, or deleting source-backed method
    obligations. Falsifier would be row-specific evidence that the upstream
    Sage stub/source signature is wrong for the exact receiver, in which case
    that row must move to the stubs card.

  - `RESEARCH-CAT-ARGTYPE-WRAPPER-BOUNDARIES`: exact selector covers 14 current
    `arg-type` rows where the local Cat wrapper boundary passes local wrapper
    objects or local category collections to Sage APIs whose static surface
    expects Sage `Category`, `CategoryObject`, `Parent`, or `list[Category]`:
    rows `0`, `1`, `2`, `3`, `10`, `34`, `39`, `44`, `49`, `125`, `162`,
    `164`, `306`, and `311`. Representative inspected source includes
    `_CatObjectMixin.Hom` at `category_specs/cat/base_category_types.py:495`,
    local `join`/`meet` wrappers at `base_category_types.py:602-604` and
    `category_specs/cat/__init__.py:250-255`, and local category-over-base
    constructors in `base_category_types.py:736-746`. Owner is research
    code/design: these are local wrapper boundary obligations, not plugin
    requests to understand `Cat`. Required work is to adapt or prove local
    wrapper objects at the Sage boundary while keeping project-specific
    narrowing behind local helpers. Acceptance is that these 14 rows disappear
    without weakening Sage stubs or using opacity. Falsifier would be
    row-specific Sage evidence that the upstream method accepts the narrower
    local wrapper type directly under the same static contract.

  - `RESEARCH-LOCAL-CATEGORY-AND-BASE-RING-CONSTRUCTOR-ARGS`: exact selector
    covers 57 current `arg-type` rows where local category constructors or Sage
    category constructors receive project-local ring/category aliases that are
    not statically proven to be Sage `CategoryObject`, `Category`, `Parent`,
    `Ring`, or local `Ring`: rows `252`, `253`, `661`, `756`, `765`, `769`,
    `837`, `844`, `867`, `886`, `888`, `891`, `904`, `913`, `917`, `922`,
    `923`, `924`, `929`, `930`, `931`, `939`, `941`, `955`, `958`, `959`,
    `990`, `995`, `998`, `999`, `1002`, `1070`, `1086`, `1216`, `1353`,
    `1356`, `1359`, `1362`, `1365`, `1368`, `1371`, `1417`, `1420`, `1424`,
    `1427`, `1440`, `1559`, `1563`, `1566`, `1571`, `1576`, `1579`, `1582`,
    `1585`, `1595`, `1601`, and `1604`. Representative inspected source
    includes `Modules(R)` and `SageMagmaticAlgebras(R)` in
    `category_specs/algebras/__init__.py:127`, `AssociativeAlgebras(R)`,
    `Rings().RingsUnder(R)`, and `Modules(R)` at `:339-341`,
    `Modules(M.base_ring())` in `category_specs/modules/__init__.py:573`, and
    `_MatrixAlgebras(R.base_ring(), R.nrows(), R.ncols())` at
    `category_specs/rings/__init__.py:1960`. Owner is research code/typing:
    the local ring/category aliases are too weak at constructor boundaries.
    Required work is to centralize checked local adapters for local ring and
    category objects before passing them to Sage or project constructors.
    Acceptance is that these 57 rows disappear with explicit local boundary
    proof. Falsifier would be row-specific evidence that a named Sage
    constructor is actually missing a supported argument form in stubs.

  - `RESEARCH-CONSTRUCTED-MODULE-REFINEMENT-ARGTYPES`: exact selector covers 44
    current `arg-type` rows where module constructors produce Sage module
    parents or local module-related values that are then passed to local
    refinement/category helpers expecting project `_RModObjects`, `RModule`,
    or local rank/element types: rows `188`, `197`, `674`, `677`, `678`,
    `679`, `680`, `681`, `682`, `683`, `686`, `694`, `697`, `698`, `699`,
    `700`, `701`, `702`, `705`, `722`, `723`, `725`, `726`, `736`, `737`,
    `739`, `740`, `746`, `757`, `759`, `762`, `770`, `772`, `774`, `776`,
    `778`, `780`, `782`, `784`, `786`, `792`, `794`, `1342`, and `1344`.
    Representative inspected source includes `_refine_constructed_module(M,
    categories)` and `_categories_for_free_module(M)` in
    `category_specs/modules/__init__.py:570-640`, Sage `FreeModule`,
    `VectorSpace`, and `span` calls in `:681-912`, quotient-module refinement
    at `:968-979`, and local finite/free-module methods at
    `category_specs/modules/subcategories/free.py:155-161`. Owner is research
    code/typing: these are local refinement-boundary obligations after Sage
    constructs a parent. Required work is to narrow Sage-created module parents
    through checked `refine_category` boundaries before consuming them as local
    protocols, and to normalize rank/element arguments deliberately. Acceptance
    is that these 44 rows disappear while preserving real Sage constructor
    signatures. Falsifier would be source/runtime evidence that a Sage
    constructor return is incorrectly stubbed and should already satisfy the
    local `_RModObjects` protocol without local refinement.

  - `RESEARCH-SETS-POSETS-PARTITION-ARGTYPES`: exact selector covers 25 current
    `arg-type` rows in set, partitioned-set, and poset helpers after the
    stubs-owned `Subsets`, `SetPartition`, and `ConditionSet` rows are
    excluded: rows `255`, `279`, `285`, `366`, `368`, `371`, `377`, `379`,
    `384`, `402`, `446`, `466`, `471`, `495`, `507`, `570`, `571`, `572`,
    `573`, `574`, `1266`, `1300`, `1301`, `1386`, and `1387`.
    Representative inspected source includes set category comparisons at
    `category_specs/sets/__init__.py:373`, cartesian-product category
    inference at `:980`, countable-set `map` at
    `sets/subcategories/countable.py:105-112`, partition refinement helpers at
    `sets/subcategories/partitioned.py:216-231`, and poset/lattice morphism
    predicates at `category_specs/posets/subcategories/finite.py:175` and
    `finite_lattice.py:206`. Owner is research code/typing: these are local
    element, parent, category, and morphism protocol boundary mismatches.
    Required work is to add checked adapters or revise local helper signatures
    where public Sage methods require broad `object`, callable, category, or
    parent surfaces. Acceptance is that these 25 rows disappear without
    weakening Sage stubs. Falsifier would be row-specific evidence that a Sage
    stub has a too-narrow signature for the named public method.

  - `RESEARCH-PARTITIONED-SET-ELEMENT-MEET-OPERATOR`: exact selector covers
    `category_specs/sets/subcategories/partitioned.py:201`, where
    `PartitionedSetsCategory.ElementMethods.meet` returns `self * other`.
    Inspected source lines 198-210 define this as a local final helper over the
    same local `ElementMethods` protocol, which declares `sup` but does not
    declare `__mul__`. Owner is research code/typing: this row is a local
    partitioned-set element protocol mismatch, not evidence that Sage stubs need
    to add multiplication to arbitrary local element-method containers. Required
    work is to express the Sage set-partition meet operation through a local
    method/protocol that actually contains the operation, or call the
    source-backed Sage operation through an explicitly typed adapter. Acceptance
    is that the single operator row disappears without adding opaque
    multiplication to broad element protocols. Falsifier would be source/runtime
    evidence that the local element method container is a Sage set-partition
    element class whose public static surface should include `__mul__`.

  - `RESEARCH-WITH-BASIS-SEQUENCE-KEYS-BRANCH`: exact selector covers
    `category_specs/modules/subcategories/with_basis.py:186` for the
    `Sequence[_RModElements]` branch of the union-attr diagnostic. The sibling
    `AbstractFamily.keys()` branch is owned by
    `STUB-ABSTRACTFAMILY-KEYS`; the inspected local source declares
    `basis_order` as `tuple(self.basis().keys())` while `basis()` can also be a
    `Sequence[_RModElements]`. Owner is research code/typing: Python sequences
    do not expose `keys`, so this branch needs local normalization or a
    sequence-specific ordering path rather than a Sage stub. Required work is to
    branch on the actual basis container shape or tighten the local `basis()`
    contract before calling `keys`. Acceptance is that the single
    `Sequence[_RModElements]` union-attr row disappears while the
    `AbstractFamily` row remains stubs-owned. Falsifier would be source evidence
    that the local `basis()` contract cannot return a sequence at this point.

  - `RESEARCH-LOCAL-PARENT-ELEMENT-PROTOCOL-ATTRS`: exact selector covers 14
    attr-defined rows where local provider methods call methods or side-channel
    attributes that are not established by the local static receiver protocol:
    rows `194`, `195`, `196`, `326`, `646`, `649`, `908`, `909`, `910`,
    `1349`, `1490`, `1664`, `1773`, and `1618`. Inspected representative
    sources include quotient-module helpers in
    `category_specs/modules/subcategories/constructions/quotients.py:92-132`
    calling `self.submodule`, module tensor helpers in
    `category_specs/modules/__init__.py:240-261` calling same-provider
    `tensor_power`, image/hom helpers calling `inclusion` and `Hom`,
    free-algebra construction at `category_specs/algebras/__init__.py:496-500`
    attaching project-local `_category_specs_*` attributes to a Sage parent,
    ring extension helpers calling `self.base_ring().extension` through the
    local `_RingObjectMethods` protocol, and definite-form element methods
    calling `self.is_zero` without the local element receiver being typed as a
    Sage element protocol. Owner is research code/typing: each row needs a local
    protocol boundary or checked adapter proving the specific module/ring/parent
    or element surface before the call; these rows are not enough to add broad
    methods to arbitrary Sage `Parent`, arbitrary `_RingObjectMethods`, or all
    element-method containers. Required work is to split these helper surfaces
    so the receiver type names the actual required Sage/local capability
    (`submodule`, `tensor_power`, `Hom`, `gens`, `change_ring`/`extension`, or
    `is_zero`) before use. Acceptance is that these 14 rows disappear without
    broad `Any`/`object` opacity or fake external stub members. Falsifier would
    be row-specific Sage source/stub evidence that the named method is a real
    method on the exact public receiver type already present at the call site.

  - `RESEARCH-INFINITY-OO-IMPORT-SURFACE`: exact selector covers
    `category_specs/rings/subcategories/polynomial_ring.py:83`, where the
    source imports `oo` from `sage.rings.infinity`. Negative finding: Searched:
    `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src/src/sage/rings/infinity.py`,
    `sage/rings/all.py`, and `sage/all.py` for an `oo` assignment or export.
    Found: `sage.rings.infinity.py` defines `infinity`, `Infinity`, and
    `minus_infinity`, but no top-level `oo` assignment; `sage/all.py:306`
    defines `oo = infinity`, while `sage/rings/all.py` imports `infinity` but
    not `oo`. Conclusion: inference, `oo` is an aggregator alias from
    `sage.all`, not a public member of `sage.rings.infinity` to request from
    `sage-stubs`. Confidence: High for current Sage source. Classification
    boundary: this row concerns the current `sage.rings.infinity.oo` import;
    other infinity aliases would require their own current diagnostic. Owner is
    research import hygiene. Required work is to import `infinity` from
    `sage.rings.infinity` or import `oo` from the aggregator surface that
    actually defines it. Acceptance is that the single attr-defined row
    disappears without adding a fake `oo` export to `sage.rings.infinity`.
    Falsifier would be current Sage source/runtime evidence that
    `sage.rings.infinity.oo` is a real module export.

  - `RESEARCH-HOM-END-AUT-ARGTYPE-BOUNDARIES`: exact selector covers eight
    current `arg-type` rows in hom/end/aut construction after the stubs-owned
    `ConditionSet` rows are excluded: rows `130`, `131`, `141`, `142`, `143`,
    `146`, `149`, and `151`. Representative inspected source includes
    `_end_categories_of(super_category)` in
    `category_specs/homsets/endsets.py:118-142`, where Sage category values
    from `base_category().super_categories()` are consumed by a helper typed
    for local `Category`, and `AutCategoryConstruction.from_end_category` at
    `category_specs/homsets/autsets.py:151-154`, where the construction object
    itself is passed as a local category argument. Owner is research
    code/design: these rows arise from local hom/end/aut helpers drawing a
    boundary between Sage categories and local category wrappers. Required work
    is to prove or adapt Sage category results into local category wrappers at
    the helper boundary, or loosen the helper to accept Sage category surfaces
    and normalize internally. Acceptance is that these eight rows disappear
    without asking the plugin to know local hom/end/aut wrapper classes.
    Falsifier would be evidence that the helper argument should be a generic
    plugin-projected runtime category relation rather than an explicit local
    conversion.

  - `RESEARCH-RING-NUMBERFIELD-TENSOR-ARGTYPE-NORMALIZATION`: exact selector
    covers 11 current `arg-type` rows where local constructor inputs use broad
    `Sequence` or Python `int` shapes while the current local/Sage call surface
    expects lists/tuples or Sage `Integer` tuples: rows `637`, `1035`, `1036`,
    `1037`, `1038`, `1039`, `1040`, `1071`, `1072`, `1223`, and `1227`.
    Representative inspected source includes `NumberFieldTower(...)` in
    `category_specs/rings/__init__.py:949-958`,
    `_MatrixAlgebras(..., R.nrows(), R.ncols())` at `:1960`, tensor component
    `_from_components` calls at
    `category_specs/tensor_algebra_components/__init__.py:326` and `:380`, and
    module tensor power at `category_specs/modules/__init__.py:243`. Owner is
    research code/typing: local helper signatures promise broader shapes than
    they pass downstream. Required work is to normalize sequences to accepted
    list/tuple forms and choose/convert integer domains deliberately at local
    boundaries, without asserting that Python `int` and Sage `Integer` are
    interchangeable. Acceptance is that these 11 rows disappear with explicit
    normalization or adjusted local signatures. Falsifier would be Sage
    source/runtime evidence that one downstream constructor accepts the broader
    shape and the current stub is too narrow.

  - `RESEARCH-LOCAL-ALGEBRA-RING-ARGTYPE-REFINEMENTS`: exact selector covers 11
    current `arg-type` rows in local algebra/ring construction and refinement
    helpers: rows `303`, `905`, `907`, `911`, `914`, `915`, `916`, `920`,
    `921`, `927`, and `928`. Representative inspected source includes
    `category_specs/algebras/__init__.py:431-440`, where local algebra
    constructors refine Sage algebras through local `MagmaticAlgebras`, and
    `:514-569`, where Sage algebra targets and local algebra categories are
    mixed in `_sage_algebra_from_source_with_target`. Owner is research
    code/typing: these rows are local refinement-boundary mismatches between
    Sage algebra/category values and project algebra/ring protocols. Required
    work is to add local adapters or revise helper signatures so Sage category
    and algebra results are normalized before being consumed as local
    categories. Acceptance is that these 11 rows disappear without weakening
    external Sage method signatures. Falsifier would be source-backed evidence
    that a particular Sage stub has the wrong accepted parameter for the exact
    public method.
