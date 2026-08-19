# Category Spec Style Reference

This is the canonical detailed style reference for category-spec work.

Internal historical mentions of `STYLE.md` refer to this skill reference unless they explicitly name another path.

## Contents

- [Type System Rules](#type-system-rules)
- [Spec Philosophy](#spec-philosophy)
- [Category Architecture](#category-architecture)
- [Axiom Philosophy and Mathematical Precision](#axiom-philosophy-and-mathematical-precision)
  - [Direct implementation categories vs. axiomatic restrictions](#direct-implementation-categories-vs-axiomatic-restrictions)
- [Hom, End, and Aut Categories](#hom-end-and-aut-categories)
  - [File organization](#file-organization)
  - [Aut Categories Are Wired Repo-Wide](#aut-categories-are-wired-repo-wide)
  - [What subtrees own vs. what the top level owns](#what-subtrees-own-vs-what-the-top-level-owns)
  - [Morphism, Endomorphism, and Automorphism element types](#morphism-endomorphism-and-automorphism-element-types)
- [File Tree](#file-tree)
- [Implementation Rules](#implementation-rules)
- [super_categories](#supercategories)
- [Refinement](#refinement)
- [Overall Design](#overall-design)
- [Category Structure](#category-structure)
- [Sage Naming Disambiguation](#sage-naming-disambiguation)
- [Sage Inventory and Mapping](#sage-inventory-and-mapping)
- [Error Handling](#error-handling)
- [Axiomatic Subcategory Registration](#axiomatic-subcategory-registration)
- [Method Classes](#method-classes)
- [No Splicing](#no-splicing)
- [Method Overrides](#method-overrides)
- [Method Placement](#method-placement)
- [Testing (sage_gaps)](#testing-sagegaps)
- [Testing (regression)](#testing-regression)
- [Testing (new_spec)](#testing-newspec)
- [TYPE_CHECKING](#typechecking)
- [Type Annotations](#type-annotations)

## Reference Body

# STYLE.md - category_specs

Read this file before editing, reviewing, or authoring category specs, implementations,
tests, category-obligation examples, Sage inventory/mapping docs, type packages, or code organization in
this subtree.

This file records conventions, banned patterns, mathematical naming rules, and local
spec structure. It preserves style and compliance material extracted from `AGENTS.md`.

## Mathematical Sentence Rule

Every sentence about category-spec work should be expressible as one of:

- a definition;
- a construction;
- a theorem-shaped assertion;
- a hypothesis;
- a proof obligation;
- a source citation;
- an implementation witness;
- an implementation gap.

For every Sage name, first write the mathematical statement in a standard category
under explicit hypotheses. Only after that sentence is stated may the document mention
Sage realization, implementation gaps, tests, tracker state, or agent procedure.

Avoid coined workflow vocabulary in mathematical documentation. Replace vague terms by
the object meant: object, morphism, constructor, operation, predicate, category,
subcategory, Hom object, automorphism group, discriminant form, orthogonal complement,
source method, implementation witness, or implementation gap. Terms such as "surface",
"admission", "frontier", "lane", "gate", "routing", and "artifact" are allowed only
when they name agent procedure rather than the mathematical claim.

## Type System Rules

- **Type Signatures Are Proof Obligations**: A type annotation, type alias, overload,
  or cast is a claim about the mathematical object being expressed. It is not a
  comment for mypy and not a local escape hatch. Every typing change must be checked
  against the design philosophy before editing:
  - Does this make the mathematical structure, owner, codomain, or hypothesis more
    explicit?
  - Does this preserve the smallest readable mathematical claim, without adding
    software-engineering boilerplate around a correct category expression?
  - Is the type checker surfacing a real source defect that implementers downstream
    should see, such as a missing abstract obligation, wrong owner, missing named
    mathematical type, invalid constructor input, or unsourced broad codomain?
  - Or is the code conceptually right while the checker lacks Sage/category knowledge,
    such as dynamic inheritance, method-container projection, `_with_axiom`,
    `category_of`, `refine_category`, `LazyImport`, or `@classcall_private`?

  If the error is caused by missing static knowledge of correct Sage mathematics, the
  required fix is to teach the checker through the plugin, global QC config, generated
  stubs, or a tracked static-model task. Do not scatter `cast(Category, ...)`,
  `cast(Ring, ...)`, `cast(Any, ...)`, or equivalent local assertions around already
  valid category selectors merely to reduce a mypy count. A local cast is allowed only
  at a genuinely untyped interop boundary or a documented narrow refinement where the
  code needs a stricter mathematical type than the source API can express, and the
  task card must state the exact checker error, why the code is mathematically correct,
  and why no plugin/static-model fix is the right owner.
- **Casting Is a Red Flag**: Treat casts as evidence requiring review, not as routine
  typing hygiene. A single isolated cast can be valid at a true Sage interop boundary,
  at a constructor validation point that has just validated raw data, or at a narrow
  override-and-promote point where spec-level code combines inherited methods whose
  mathematical contracts guarantee a more structured result. Non-isolated casts, a
  repeated casting pattern, or casts around ordinary category selectors usually signal
  QC-silencing or code contortion.

  Before accepting a cast inside a spec implementation, decide whether the spec is
  doing too much implementation work. If the operation is a trivial combination of
  methods/properties guaranteed by the subcategory hierarchy, the better design may be
  to leave the implementation to the downstream object that must override the relevant
  ABCs anyway, so the type work lives at the real implementation boundary. Another
  possible owner is QC tooling: the checker may need to learn that inherited specs are
  promoted to objects in the current category, rather than forcing every local spec
  body to restate that promotion by cast. These are decision points. Record the choice
  as source-correct implementation placement, a narrow documented promotion exception,
  or a dedicated QC-tooling/static-model task.
- **Type-Checker Tension Is Expected**: Static type checkers encode ordinary software
  subtype rules, while this project is specifying mathematical categories and
  dynamically inherited implementations. Mathematical obligations are not identical to
  software substitutability obligations. A square is a rectangle, a group is a set, and
  a subcategory object must satisfy upstream obligations; any method that works on the
  underlying set should be available to a group when the hypotheses are met. But a
  refined method in a subcategory may intentionally restrict inputs and strengthen
  outputs: if `A' <= A`, `B' <= B`, and `F: A -> B`, a mathematically correct
  restriction may have type `F': A' -> B'`. That can conflict with ordinary function
  variance or Liskov-style method interchangeability even when it is the correct
  category-theoretic operation. Treat those conflicts as classification points, not as
  automatic permission to cast.

  The intended architecture also depends on dynamic inheritance of specs and, later,
  implementations. A new subcategory should be able to declare its position in the
  category graph and receive upstream obligations, tests, and canonical implementations
  where applicable without explicit subclassing, trivial re-call wrappers, or knowledge
  of the implementation source tree. Aggregate category namespaces such as `Cat` and
  category `Constructors()` should provide discoverable, opinionated entry points and
  implementation-provider registration. For example, a module `R^n` has an underlying
  set recognized as `R x ... x R`; if `R` is countable and has an enumeration, an
  upstream provider should eventually be able to construct product enumeration once
  and make `R^n` enumerable when the registered implementations integrate correctly.

  Therefore, when mypy or another checker objects to a category method, ask first
  whether the objection exposes a real mathematical/spec defect or whether the checker
  lacks the project's category/provider model. In the second case, the tracked fix is
  a dedicated plugin, generated-stub, static-model, global-QC, or focused-reproducer
  task that teaches the checker the intended Sage mathematics and makes future QC
  enforce the convention. Do not record these as "expected" failures to ignore, and do
  not silence them locally. Replacing the mathematical claim with explicit wrappers,
  local casts, or provider subclassing merely to satisfy software subtype rules is
  design drift. QC-zero is not a license to brutalize the codebase into warning-free
  shape; it is a requirement that either the source expresses the mathematics correctly
  or the QC tools are improved until they can enforce the correct convention.
- **No Duck-Typing**: We do not "believe" in duck-typing in mathematical code, or
  variadic signatures, including Sage interop constructors or methods.
  Prefer explicit types and signatures everywhere. Duck-typing is a runtime concern:
  if a third party provides an implementation that quacks like ours, they can use
  the category methods, but we never rely on duck-typing for design or architecture.
- **No Variadic Signatures**: We do not accept variadic type signatures (`*args`,
  `**kwargs`) on our spec.
  1.  **Verify Sage Actuals**: Check the Sage source and written documentation for
      the corresponding method. Typically, Sage methods that appear variadic are
      actually constrained to a finite set of input patterns and shapes.
  2.  **Named, Non-Positional Arguments**: The spec must force named,
      non-positional arguments that remain compatible with existing positional
      calls in Sage.
  3.  **Use @overload**: When there are truly multiple input patterns, split them
      into an `@overload` pattern documenting each specific mathematical
      signature.
  4.  **Closed Implementation**: The final concrete implementation of a method
      with overloads MUST be "closed": it should handle exactly the patterns
      defined in the overloads (typically using `match/case` on types or data
      shapes) and must NOT use `*args` or `**kwargs` for catch-all forwarding.
  5.  **Mathematical Types Only**: Never add "shortcut" types (e.g.,
      `MyCategoryInputDataShape`) that have no mathematical meaning and only serve
      as software engineering helpers. Every type must reflect a real mathematical
      concept.
- **Sage Interop Uses Overloads, Not Variadics**: When a Sage method or constructor is
  variadic, the exposed project API still is not. Convert the variadic Sage constructor or method to
  explicit `@overload` cases that cover the finite set of input patterns actually
  accepted by Sage.
  1.  **Research Before Designing Overloads**: Read the Sage signature, written Sage
      documentation, Sage implementation, and existing local usage before choosing the
      overloads. Do not infer overloads by blindly matching the signature.
  2.  **Treat Overload Design As Its Own Task**: Designing the overload set is a
      significant research subtask. Use a subagent by default when available, and make
      the task contract require source reading, written-doc interpretation, usage
      survey, and a proposed closed overload set.
  3.  **Preserve Old Calls With Tests**: Add regression tests for every previously
      supported variadic-style construction so each old call path is proven to pass
      through one of the explicit overload cases.
  4.  **Avoid Type-Narrowing `try/except`**: Because overload cases are explicit and
      closed, do not use monolithic variadic bodies with `try/except` branches to guess
      or narrow input types. Use explicit typed dispatch that matches the overload set.
- **Binary Operations Are Foldable**: A binary operation must expose the binary
  operation itself and, when an aggregate operation is mathematically meaningful, a
  separate sequence overload that folds over the binary operation.
  - Example pattern: `op(x: XElement, y: XElement) -> XElement` and
    `op(elements: Sequence[XElement]) -> XElement`.
  - The sequence overload is an explicit fold over the binary overload. It is not a
    variadic signature and not an optional-argument compatibility path such as
    `op(x, y=None)`.
  - Do not replace the binary operation with only an aggregate operation. The binary
    operation is the primitive mathematical operation.
- **True Sage Wrappers**: A wrapped Sage class must subclass the Sage class it
  re-exports, add only the project-specific registration or predicate, and then
  be re-exported under the Sage-compatible name. Do not reconstruct a Sage class by
  combining wrapper pieces, and do not copy upstream implementation hacks unless no
  true subclass wrapper can preserve Sage behavior.
  - Singleton axiom categories are mathematically singleton categories. They must use
    `CategoryWithAxiom_singleton` up front instead of relying on Sage's
    `CategoryWithAxiom.__init__` class-base mutation to repair a plain
    `CategoryWithAxiom` after construction.
  - Base-ring axiom categories must use `CategoryWithAxiom_over_base_ring`; do not force
    base-ring categories through the singleton wrapper.
- **`isinstance` as a Design Signal, Not a Ban**: `isinstance` checks are not banned —
  they are diagnostic flags that the code is guessing about an object's category at
  runtime rather than expressing membership through the category system. Each
  occurrence triggers a specific reasoning chain (see the `anti-slop` skill,
  `references/code-patterns.md#introspection-red-flags` for the full framework,
  including `hasattr`, `getattr`, `type()`, `issubclass`, and `callable()`).

  **Boundary vs. interior**: `isinstance` is acceptable at the typed/untyped
  boundary — inside `__contains__` (which takes `Any`), in Sage interop wrappers
  that receive untyped raw Sage objects, and at constructor validation points that validate
  input shapes once. Outside these boundary sites, each `isinstance` should be
  questioned as a signal that the category system is not carrying enough information.

  **Preferred replacement**: When a categorical predicate exists (e.g.,
  `C in Cat().JoinCategories()` or `C.is_join_category()`), use it instead of
  `isinstance(C, JoinCategory)`. When no predicate exists yet, treat repeated
  `isinstance` checks as a design smell and add the missing category operation
  rather than copying the runtime check through the codebase.

  **Assert vs. branch**: `assert isinstance(x, T)` documents a precondition and
  fails loudly. This is different from a branch that silently produces different
  behavior based on type — the latter should usually be an overload, a tagged
  union, or an explicit dispatch path.
  - Example: `isinstance(C, JoinCategory)` may be acceptable inside the implementation
    of `Cat().JoinCategories().__contains__`, but ordinary code should say
    `C in Cat().JoinCategories()` or `C.is_join_category()`.
  - If no mathematically meaningful category or predicate exists yet, treat repeated
    `isinstance` checks as a design smell and add the missing category operation instead
    of copying the runtime check through the codebase.
- `__contains__` always takes `Any` as its argument type.
  Never use `object`.
- **Standard Type Packages**: Each category or subcategory module owns a uniform local
  package of mathematical type names for the category it defines.  For a category
  named `X`, the standard package is:
  `XCategory`, `XObject`, `XElement`, `XMorphism`, `XHomCategory`,
  `XEndCategory`, `XAutCategory`, `XHom`, `XEnd`, `XAut`,
  `XEndomorphism`, and `XAutomorphism`.
  These names are direct pointers to the category class, its method classes, and its
  Hom/End/Aut category objects; they are not software helper aliases.
- `types.py` imports and re-exports standard type packages, then decides conventional
  mathematical aliases such as `Ring = RingsObject`, `RModule = ModulesObject`, or
  `Polynomial` as an element type in the appropriate polynomial-ring subcategory.
  Outside a category module's standard package and `types.py`, do not define type
  aliases, `TypeAlias` definitions, or ad-hoc types — not in `TYPE_CHECKING` blocks,
  not at the top of axiom or other files, not inline. Import from `types.py`.
- **No `__all__` Export Lists**: Do not use an explicit all-export pattern in this
  subtree. Public and private APIs are communicated by names: `_PrivateName` is a
  private implementation or local spec entry point, and `PublicName` is importable.
  Package `__init__.py` files may re-export public names with ordinary imports, but
  they must not maintain `__all__` allowlists. Type checkers should warn when code
  imports a private name; do not hide ownership mistakes by exporting private names.
- **No Private-Class/Public-Alias Indirection**: Do not define a top-level class with a
  private name and then immediately publish it through a public alias such as
  `PublicClass = _PrivateClass` or `PublicClassCategory = _PrivateClass`. This adds
  needless indirection and defeats the naming convention above. If a class is public,
  declare it with the public name. The public API is already visible by reading the
  file's top-level functions and classes and filtering out names that begin with `_`.
  Use the file-level docstring to document the public API and its organization; do not
  recreate an export list through alias bookkeeping.
- **No Python Native Scalar Types In Signatures**: Never use native Python scalar
  types (`int`, `float`, `complex`) as type annotations when a Sage equivalent exists.
  Use the Sage types from `types.py` instead, e.g. `Integer` instead of `int`.
  Literal scalar values are allowed as defaults and examples: `n: Integer = 3` is
  valid Sage-style spec notation and should not be rewritten to `Integer(3)` merely to
  satisfy this rule.
- **Typed Finite Collections Are Mathematical Vocabulary**: The ban is on
  untyped or non-mathematical primitive containers, not on finite collection
  notation itself.  A typed finite collection such as `list[Field]`,
  `tuple[RingElement, ...]`, `tuple[SetMorphism, RingMorphism]`, or
  `dict[RingElement, Integer]` is acceptable when it transparently states the
  mathematical data returned by the method.
  - Do not treat Sage's Python return container as a typed source of truth.
    Sage source is usually untyped; Sage code and written docs are evidence to
    translate into project mathematical vocabulary.
  - Do not invent wrapper names merely to avoid `list`, `tuple`, or `dict`.
    A name such as `GaloisClosureWithEmbedding` hides the obvious product
    `tuple[Field, RingMorphism]` unless it is already a standard mathematical
    object with independent structure and methods.
  - Bare `list`, bare `tuple`, bare `dict`, containers whose entries are not
    mathematical types, and containers used as vague implementation data shapes
    are noncompliant. Replace them with typed finite collections or with the
    actual mathematical object.
  - Python `set[...]` is almost never correct in signatures. Sets in this
    subtree should be Sage/project set objects in `Sets()`, not Python hash-set
    containers.
  - Use **Ordered Sets** when the object itself is a finite set with no
    duplicates and mathematically meaningful order. Use **Families** when the
    object is indexed by another set or when repetitions matter. Use typed
    `list`, `tuple`, or `dict` when the intended finite data is exactly an
    ordered list, finite product, or finite association.
- **Prefer Generators for Infinite or Lazy Collections**: For infinite or lazily
  enumerated collections, prefer returning Python generators over explicit
  finite containers. This supports lazy evaluation and allows filtering or
  mapping without prematurely unwrapping infinite objects into memory.
- **Deep ConditionSet Integration**: Predicate-defined subsets and filtered
  subobjects are public subobjects, not raw `ConditionSet` API. For subsets or
  filtered collections (e.g., even integers, automorphisms within an endset), use
  Sage's `ConditionSet` only as localized interop backing for containment via
  predicates. This allows clean mathematical expressions (e.g., `1+i in (CC -
  RR)`) and deferred evaluation while preserving the public vocabulary:
  `Sets().Subobjects().Of(ambient, predicates)` for subsets, and the analogous
  subobject category operation for other categories. Raw `ConditionSet.arguments()`
  and symbolic predicate plumbing stay in Sage inventory or interop files; they
  are not category-spec methods.
- Type names reflect **real mathematical vocabulary**, inspired by the SageMath
  **written docs** (not just type signatures — read the actual mathematics):
  - Objects: `Polynomial`, `RealNumber`, `ComplexNumber`, `RingElement`, `PowerSeries`,
    `Module`, `Ring`, `Set`, `FiniteSet`, `FinitelyGeneratedFreeModule`
  - Categories: `RMod`, `Rings`, `Sets`, `RAlgebras`, etc.
    (semantically named)
  - Morphisms: named after the mathematical morphism, e.g. `RModMorphism`,
    `RModAutomorphism` — never `HomsetElement` or `AutsetElement`
- Programmer-shaped type names are audit red flags. Names such as
  `PolynomialRingElement`, `HomsetElement`, or `CategoryInputData` usually mean an
  agent pattern-matched a Sage class or a software role instead of reading the
  mathematical docs and naming the mathematical object. Prefer the mathematical noun
  (`Polynomial`, `Morphism`, `Category`, etc.) unless a sharper mathematical
  distinction is actually needed.
- Every type in `types.py` must be anchored to a real Sage object — `Any` is never
  acceptable. A type only appears in a signature because something in Sage already
  represents it; the written docs identify the vocabulary, and Sage provides the anchor.
  Precision tiers, in increasing preference:
  1. **Minimum**: the relevant SageMath base class (e.g. `sage.structure.parent.Parent`,
     `sage.structure.element.Element`)
  2. **Better**: the relevant SageMath subcategory's `ParentMethods` or `ElementMethods`
     (e.g. `sage.categories.posets.Posets.ParentMethods`)
  3. **Best**: a class from **our own hierarchy** that properly refines the Sage object
     (e.g. `_TotallyOrdered.ParentMethods` for `Poset`)

## Spec Philosophy

The spec's job is to formally declare what objects in a category **are** and **must
have** through mathematically natural category/refinement structure - not to implement
hard algorithms by wishful API design. A category spec is a Sage-grounded mathematical
interface inside Sage's category/object universe. Current Sage implementation coverage
is not the standard of adequacy.

Sage interop is still a design constraint. The project extends Sage without editing
upstream source yet, and refined objects should remain usable by existing Sage code
when mathematically appropriate. Existing Sage implementations show methods,
constructors, algorithms, categories, and documented behaviors that are already
mathematically useful and often implementable. They help prevent an unbounded wishlist
of methods with no credible implementation path. Treat Sage as implementation evidence
and a realization witness, not as mathematical admissibility and not as a license to
place objects in stronger categories without the required proof or witness data.

The spec therefore has two simultaneous obligations:

- preserve existing Sage functionality by inventorying and mapping Sage methods,
  constructors, and documented behavior into project vocabulary; and
- state mathematically required methods and laws with the category membership,
  hypotheses, and witness data that make them category facts.

A subcategory definition should read as a mathematical document: what the subcategory
is, what its supercategories are, what methods an object in it must have, what
witness data the category includes, and what methods Sage already provides.
Subcategory definitions focus on categorical declaration; non-trivial software
engineering belongs in `utils.py`.

Refinement is also categorical declaration. It takes an existing Sage object and says
that the object is now viewed as lying in a project subcategory of its Sage-backed
category. The existing Sage object is a partial implementation of the project spec:
some specified methods are already present, and category-obligation examples should
expose the missing ones.

Refinement does not interrogate the object being refined. It does not validate that the
object satisfies the project category, reject because project methods remain abstract,
or instantiate the missing implementation. The declaration imposes the category
contract; it does not certify satisfaction of that contract.

This distinction is structural. The project invented specifications Sage does not know,
so most refined Sage implementations are expected to be incomplete relative to the
project spec. That incompleteness is the evidence category-obligation examples are
meant to expose, not a reason to weaken the spec or add refinement-time checks.

Do not turn refinement into method-search repair. If a refinement task starts with
method search, cache state, dynamic class mutation, type-checker appeasement,
test-ordering output, hook output, or any other programming mechanism before it names
the category and its mathematical specification, stop and restate the ordinary category
declaration.
Concrete examples include `MRO`, `getattr_from_category`, `_cached_methods`,
`cached_method`, Cython class assignment, and `can_assign_class`:

> Existing Sage object ___ is declared to belong to project category ___; Sage already
> realizes spec methods ___; spec methods ___ remain missing.

Those terms are examples of the wrong layer, not an exhaustive list and not invented
jargon to preserve as the refinement model. A source-backed Sage-framework task may
discuss the runtime mechanism separately, but that discussion must remain outside the
mathematical specification.

Method-ownership rows must be mathematical sentences, not software-routing guesses.
For a method, first identify the object it is called on, the mathematical data it
requires, the object or morphism it constructs or observes, and the hypotheses under
which that operation is well-defined. The owner is the category where that sentence is
first true. Sage inventory can then witness implementation realization or existing
interop, but it cannot replace the mathematical sentence.

`ParentMethods` is the method class for mathematical objects in a category. Do not
describe it primarily as a method-provider class, dispatch layer, integration hook, or
implementation hook. Those are implementation witnesses after the mathematical sentence
has been stated.

Abstract `ParentMethods` are not runtime failure hooks. Use Python `abc.abstractmethod`
to represent abstract obligations in the class system, then let Python MRO and ABC
machinery carry abstractness. Do not generate failure bodies, add `assert False`,
insert `NotImplementedError`, manually compute which abstract names are satisfied, or
special-case method names.

Every added helper, test, category-obligation example, task title, and guidance phrase
touching category methods must read like a mathematical fact, proposition, operation,
requirement, or counterexample. Names that describe appeasing code machinery instead
of the mathematical operation are hard slop signals in category-spec work. Do not
launder them by adding caveats, quotes, or surrounding mathematical prose. Stop,
discard the phrasing, and reconstruct the task from the object/category sentence:

> For object ___ in category ___, method ___ expresses mathematical operation/fact/
> requirement ___ under hypotheses ___.

Only after that sentence is true may programming details be used as implementation
evidence. A helper name should expose the mathematical relation it computes or checks.

This is not an optics rule. Strange Python class manipulation inside mathematical spec
code is itself presumptive evidence of slop. It usually means the agent is trying to
force a runtime shape instead of stating the category fact. Stop unless source
reconstruction proves that the mathematical object cannot be expressed without the
mechanism.

**Mathematical Specification, Not Generic Software Engineering**:
Switch mentalities before auditing this subtree. These files are mathematical
specifications, not ordinary software interfaces. The first question is never "where
can this be implemented?" or "where is the code easiest to share?" The first question
is: **where is this statement first mathematically true, and which category owns that
truth?**

Specs force implementation of the mathematics. If a property is mathematically true
for every object in a category, the spec should require it even when implementation is
hard or currently missing. Do not weaken, relocate, or omit a method merely because it
is inconvenient. For example, if the spec category says countable/enumerated sets have
an `n`th element operation, implementers of that category must provide it; the absence
of implementations is an implementation gap, not a reason to remove the mathematical
requirement.

Do not use failed category assertions as a negative vote on the spec. If a refined
Sage object fails because it lacks an ABC method, record the
implementation/wrapper/constructor gap or ground a replacement weakest category that
preserves the obligation. Deleting an abstract method, weakening a category, or moving
a method without a source-backed replacement weakest category is spec regression.

**Definition Grounding Required Data**:
Before adding or changing a category, method, predicate, invariant, constructor,
Hom/End/Aut structure, migration rule, or mapping decision, identify the exact
mathematical definition being specified.

The grounding record must name:

- the canonical source path or reference: repo theory, `theory/references/`,
  `theory/spec_backups/`, Sage written docs/source, or an approved decision card;
- the mathematical object and owner category;
- the codomain/return object, not just an implementation-shaped return type;
- the hypotheses under which the statement is meaningful;
- the invariance or equivalence proof obligation when the object or operation is claimed to be
  independent of choices or equal to another notion;
- the migration consequence for any old Sage/project operation.

Migrations from old `.agents/plans/todo.md`, deleted triage files, category-test output,
inline cards, or user-chat summaries preserve provenance, but they are not definition authority. A
source line saying "move divisibility to X" is not enough to specify what
`divisibility` means, whether it is choice-independent, what object it returns, or
when it coincides with another divisibility notion.

If two meanings are plausible, keep them as separate named mathematical operations unless
an explicit source-backed proof gives the exact hypotheses under which they coincide.
Examples of high-risk words include `divisibility`, `primitive`, `rank`, `degree`,
`dimension`, `dual`, `basis`, `isometry`, `orthogonal`, `content`, `support`,
`order`, `kernel`, and `image`.

If the exact definition cannot be grounded, do not edit the spec. Create or update a
decision, research, or source-mining card and mark only that leaf blocked. Continuing
with the most familiar interpretation of a term is a spec failure.

**Inventory, Mapping, and Category-Obligation Examples Are Different Documents**:
Do not import generic software-engineering meanings of "inventory", "mapping", or
quick-liveness testing into this subtree. Tests in `category_specs` are category-obligation
examples: they assert that representative Sage/project objects instantiate declared
categories and satisfy the obligations of those categories.

- **Sage inventory** records Sage facts only: source files, documented constructors,
  signatures, classes, categories, methods, and observed Sage behavior. It is not the
  place to decide project inclusion, deprecation, interop status, or mathematical
  replacement. Do not write phrases such as "not included", "project operation",
  "target mapping", or "excluded interop" in `SAGE_INVENTORY.md`.
- **Mapping docs** translate each inventoried Sage constructor, method, or class into the project
  mathematics. Every Sage class and method in the inventory must map to exactly one
  of: a project category operation, a mathematically justified non-mapping, or an
  explicit `NEEDS_DECISIONS.md` item. Constructor mappings are stricter: a
  source-grounded Sage constructor shape recorded in mapping docs maps to a named
  constructor path or spec-layer promotion path by definition. An ungrounded or
  rejected constructor idea is removed from constructor mapping source material
  rather than preserved as `not included`, `deferred`, or a decision-shaped gap.
  If an existing constructor document looks suspect, do not edit it into a cleaner
  document. Reconstruct the source mapping from Sage docs/source first, then replace
  the document with the source-grounded mapping result.
  Never delete or ignore a Sage method because the Sage class or constructor around it
  is mathematically wrong.
- **Mapping starts with a theorem-shaped sentence, not a project label.** For every
  Sage name, write the ordinary mathematical statement before assigning an owner:
  "In [standard category], [construction exists/has property], under [hypotheses]."
  The category must be the weakest standard category where the statement is true. For
  example, composition belongs to any category; addition of morphisms belongs to
  additive categories; kernels and cokernels belong to abelian categories; eigenvalue
  and eigenspace data for an endomorphism belong first to finite-dimensional vector
  spaces over a field, with scalar-extension hypotheses stated when needed. A row that
  says only a Sage class, a project category, a software type, or a coined project
  phrase has not stated the mathematics and must not be accepted.
- **Mappings must preserve old functionality in migration-grade form.** Breaking API
  changes are allowed when they modernize, standardize, or uniformize old Sage
  behavior, but the old functionality must still have a documented replacement path.
  If an old method is not represented as a project method, the mapping must name the
  new method, protocol, constructor, or refinement path that recovers its behavior.
  This is what later supports migration-guide entries such as
  `old_name(...) -> new_name(...)`.
- **Every inventoried Sage class must remain constructible or explicitly rejected.**
  A Sage class may become an explicit mathematical subcategory, or it may become a
  named constructor that builds the original Sage object and refines it into the
  correct project subcategory. Spec work stops at recording this contract: later
  implementation work must patch or wrap refined Sage objects so they satisfy the ABC
  contract of the category they are placed in.
- **Rejecting an invalid Sage constructor does not reject its method evidence.** For
  example, generic `Set(X)` wrapping is ill-defined as a mathematical constructor, but
  `Set_object.__contains__`, `__iter__`, `cardinality`, `is_empty`, `is_finite`,
  `subsets`, `subsets_lattice`, `_sympy_`, Boolean operations, and rich comparisons
  still inform where those methods belong in the project category hierarchy.
- **Invalid or variadic Sage constructors must be enumerated into named mathematical
  paths.** Do not preserve an arbitrary variadic wrapper and do not replace it with
  another implementation-shaped alias. For instance, `Set(ZZ)` maps to `ZZ in Sets()`
  because `ZZ` is already a set object, while finite iterable inputs such as
  `Set([1, 2, 3])` map to a named finite-enumerated constructor such as
  `Sets().Constructors().from_iterable(elements)`.
- **Sage constructor families are not automatically project subcategories.** A Sage
  implementation class or named constructor family becomes a project subcategory only
  when it names a real mathematical category. For example,
  `CombinatorialFreeModule(R, basis_keys)` is a constructor on `Modules(R)`: it builds
  a free module with explicit basis keys and then refines that object into existing
  module categories such as `Modules(R).Free()` and
  `Modules(R).WithOrderedGeneratingSet()`. Do not create a
  `CombinatorialFreeModules` category.
- **Unrecorded mapping decisions are failures.** If an agent decides a Sage constructor, method, or class is
  non-mapped, moved to a strict supercategory, or replaced by a named constructor, that
  decision must appear in mapping docs or `NEEDS_DECISIONS.md` with the mathematical
  reason. Do not hide decisions by deleting category-obligation examples, deleting
  abstract methods, or reclassifying evidence as "interop".

**Category-Obligation Examples Classify Failed Assertions**:
Category-obligation examples in this subtree are not liveness probes or generic
pass/fail implementation tests. Their purpose is to run representative Sage/project
objects through the upgraded category spec and assert which category definitions,
constructors, inherited ABC obligations, and Hom/End/Aut laws the current
implementation satisfies. Most raw Sage refinements are expected to be incomplete
relative to this spec. The failed-obligation list is useful only when it is classified
by mathematical cause.

- A category-obligation example uses the project category operation and asserts
  mathematical facts: membership in project categories, cardinalities, rankings,
  subset relations, form laws, Hom/End/Aut semantics, constructor routing to named
  mathematical objects, and other obligations stated by the spec.
- A category-obligation example should collect all labeled failures it can reach, so
  one run exposes the current missing-obligation list. The shared collection helper
  exists for this purpose: do not stop after the first missing method when setup can be
  moved into labeled statements.
- Refinement into a category brings the whole inherited ABC contract, not only the
  headline methods of the subtree being edited. A tensor component example may expose
  `__richcmp__`, for example, because tensor component parents are still categorical
  objects that inherit comparison obligations from set/module structure.  This is not
  incidental implementation noise. It records that any later tensor-component wrapper
  or implementation must satisfy the inherited comparison/subobject contract even
  though the method name is not tensor-specific.
- A category-obligation example must not assert that an object "exists", is non-`None`,
  is truthy, or merely constructs without raising. It must not use raw Python
  containers or raw Sage quirks as the main oracle when a project category predicate or
  method should express the claim.
- If an example cannot state the intended claim using project category vocabulary, the
  result is not a weaker example. The result is a missing category-method finding that
  must be mapped, added to the spec, or recorded as a decision.
- A failed assertion should be classified as: missing implementation, missing
  constructor/refinement, wrong weakest category, missing definition, missing source
  evidence, or invalid assertion.
- Avoid assertion-wrapper ceremony in category-obligation examples. A helper is
  acceptable only when it preserves mathematical content and materially improves
  missing-obligation reporting. Do not add generic `require`, `assert_not_none`,
  truthiness checks, or other software-testing scaffolding that hides the mathematical
  assertion.
- Regression tests are separate from category-obligation examples. Regression tests
  may use Sage examples as source evidence, but they still prove project-owned
  mathematical behavior through project vocabulary. They are not a license to compare
  against raw Python containers or current Sage implementation quirks as a substitute
  for a spec assertion.

Audit with a reference-textbook mindset. Ask what Bourbaki, Atiyah-MacDonald,
Dummit-Foote, Hatcher, Hartshorne, the Stacks Project, or the relevant Sage written
documentation would consider part of the structure. Use "theory of mind" for the
mathematician implementing that category: a module implementer should be thinking like
someone doing algebra, not like someone rebuilding set theory, function application,
or basic category theory.

For broad or contentious audits, use a fresh mathematically primed reviewer when
delegation is available and appropriate. The review contract is not "find code
duplication" or "make tests pass"; it is:
- classify each method by the mathematical category where the statement first becomes
  true;
- reject invented terminology when a standard category name exists;
- compare the constructor, method, or operation against standard mathematical
  references and Sage written docs;
- flag implementation-convenience ownership, missing strict-supercategory owners, and
  programmer-shaped vocabulary;
- ignore current implementation difficulty until the mathematical owner is settled.

When spawning a subagent from an interactive chat, always call `wait_agent` and keep the
main turn open until the subagent returns or reaches an explicit blocker. Do not spawn a
subagent, report only that it was spawned, and end the turn while the user has no
in-thread completion summary. If asynchronous delegation is explicitly requested, state
that exception before ending the turn.

When subagent model selection is available, attempt to use Codex Spark for bounded
audit, review, and exploration work before spending higher-cost model budget. Its usage
is metered separately from the main Codex budget and currently has substantial cheap
capacity. Escalate only when the task requires deeper reasoning than Spark can
reasonably provide.

Subagent audit prompts must transfer the actual judgment required for the task, not
just a word prohibition or a regex-shaped hunt. Before asking a subagent to find or
fix violations, state the governing source of truth, the mathematical or architectural
principle being audited, the ownership boundary, and the distinction between a wrong
object and a right object in the wrong place. Require classification before remedy:
each finding should say whether the object is correct and correctly owned, correct but
misplaced, incorrect in substance, merely compatibility/runtime detail, or outside the
audit scope. Do not prime a subagent toward deletion, replacement, or mechanical
compliance before that classification is made. Correct vocabulary, theory, and source
material must be preserved; when the problem is ownership or placement, the expected
remedy is to move or centralize it, not erase it.

**Strict-Supercategory Separation of Concerns**:
A category spec should define only structure that first becomes meaningful at that
category, and not in any strict supercategory. This is the main category-theoretic
filter for deciding whether a method belongs in the current file.

Use the perspective of the mathematical implementer for that category:
- A module implementer should think about algebra and commutative algebra, not basic
  set membership, function-call semantics, or the existence of domains and codomains.
- A set designer should think about set-level questions such as intersections,
  complements, common ambients, and coercions between universes. For example,
  `{1, 2} ∩ {a, b}` and `[0, 1] ∩ {z in CC | |z - i| <= 1}` are real set-theoretic
  questions because they depend on common universes and embeddings.
- A hom-category/end-category/aut-category designer should own the generic facts that
  homs have domains and codomains, endomorphisms compose with themselves, and
  automorphisms are invertible. A set designer may declare that homs of sets are sets;
  a module designer may declare that `Hom_R`, `End_R`, and `Aut_R` have new
  module-theoretic or algebraic structure.
- A set designer should not own the fact that `End(X)` is a monoid or that `Aut(X)` is
  a group; those are category-theoretic facts. The set-level question is what extra
  set-theoretic structure these objects have and how set-theoretic constructions
  interact with ambients and coercions.
- A module hom-category designer should focus on module-theoretic enrichment and
  representability: for example, `R-Mod` is enriched over itself, `End_R(M)` is an
  `R`-module with ring structure and hence an `R`-algebra when appropriate, and
  `Aut_R(M)` may be representable as a matrix group. It should not redefine generic
  morphism mechanics such as `__call__`, `domain`, or `codomain`.

Audit question: "Would this method still make sense in a strict supercategory?" If
yes, it belongs there or in a universal construction, not in the current
subcategory. If the answer is "it makes sense there, but this category refines it with
new laws," the current category may state only those new laws and refined return
types.

**Spec vs. Implementation Dichotomy**:
- **Specs**: Read like mathematical properties, assertions, wiring, and methods one
  can expect on subcategories. They are intended for implementers and consumers.
  Virtually no categories should define `__init__` methods, UNLESS the
  implementation is truly trivial (e.g., just bootstrapping or wrapping some other
  existing implementation).
- **Implementations**: Read like mathematical algorithms (e.g., calling GAP for
  orbits, finding automorphism generators). They contain minimal software
  engineering, wiring, or glue, and zero new mathematical assumptions or public
  methods beyond the spec. They are intended to be rarely read.
- **Group refinements**: Full generator lists, presentations,
  arithmetic-group orbit decompositions, Vinberg chambers, Coxeter parabolics, and
  hyperbolic-lattice automorphism-group algorithms are not structure of an abstract
  group object. They appear exactly when the object is placed in a category such as
  finitely generated group, finitely presented group, finite group, generated matrix
  group, or a project-specific generated arithmetic group.
- **Categorical Glue**: Categories handle "software engineering" principles like
  routing constructors (e.g., determining if $R$ is a PID to route `FreeModule(R, n)`
  to a specialized constructor).

**Implementations in Specs**:
Some implementations CAN go into category specs when they are suitably abstractly
defined in terms of other ABCs, abstract methods, or existing implementations.
Example: if `Modules(R).FreeModule(R, n)` exists, defining `Ring.__pow__` to return
`R^n` within the category spec is permitted as it is mostly trivial wiring with no
"real" mathematical work beyond the glue.

**Final Concrete Methods**:
Any concrete method implementation in a category spec MUST be decorated with
`@final` by default. This includes trivial categorical glue, predicates,
construction selectors, and methods implemented purely in terms of abstract methods
on the same method class. The purpose is architectural: category-obligation examples
and audits must flag cases where multiple specs are trying to provide competing
concrete implementations of the same method.

Only omit `@final` when the method is intentionally an extension hook or constructor
plumbing whose subclasses must provide their own mathematical signature. Such
exceptions must be documented at the method or in the local wrapper documentation.

**Correction-Derived Audit Rubric: Mathematical Ownership Before Edits**:
This rubric records the main failure pattern from the Cat/homsets audit: local patches
look plausible when the agent has not first classified the mathematical object and its
owning layer. Future audits should reproduce the corrective reasoning, not only check
wording style.

If this rubric is being updated from a conversation history, recover the actual
transcript first. A compaction summary, subagent summary, or final chat recap is not
enough evidence for a historical policy change. Use the transcript parser, identify the
specific corrective turns, and then encode the repeated reasoning pattern. If full
transcript recovery fails, state the gap explicitly and do not present the policy as an
exhaustive analysis of the conversation.

Before editing a category spec, answer these questions in order:

- **What mathematical object is this?** Classify it as one of: a category, an object of
  a category, a morphism/functor between category objects, a functorial construction
  category, a constructor namespace, a predicate subcategory, a compatibility
  supercategory, or an implementation gap. Most bad edits in this subtree came from
  confusing these: e.g. treating `Constructors` as a category, treating Sage
  construction-category values as Sage `ConstructionFunctor` instances, inventing a
  category-level `C.Hom()` selector, or confusing object-level `C.Hom(D)` with
  `C.HomCategory()`.
- **Which layer uniquely owns it?** Do not patch below that layer. Sage category-base
  wrapping belongs in `cat/base_category_types.py`; universal construction selectors
  belong in `cat/universal_subcategory_methods.py`; root category-object semantics
  belong in `cat/`; generic `Hom`/`End`/`Aut` semantics belong in `homsets/`; subtree
  `homsets.py` files own only additional laws such as set-map, ring-homomorphism, or
  module-homomorphism structure; constructor entry points belong only in
  `Constructors`.
- **Does the code shape already reveal the wrong layer?** Treat the shape of the code
  as evidence, not mere style. Large software-engineering blocks inside category
  definitions, repeated domain/codomain methods in specialized morphism categories,
  or duplicated construction selectors across subtrees are usually not local cleanup
  problems. They are clues that the method belongs in a base category type, a
  universal method class, or a higher categorical abstraction.
- **Does the method pass the strict-supercategory test?** If the method makes sense in
  a strict supercategory, the current category should not define it except to refine
  the return type or add genuinely new laws. Category specs are not checklists of
  everything an object can do; they declare the new mathematical structure that begins
  at that category.
- **Is the proposed ownership mathematical, or merely implementable?** Do not accept a
  location because the code can be shared there. Accept it only if the mathematical
  statement first becomes true there. Conversely, do not move a method downward because
  implementations are missing; missing implementations are exactly what specs and
  category-obligation examples are meant to expose.
- **What Sage mechanism is being extended?** Read the written Sage docs, source, and
  local usage before deciding. Do not infer architecture from a single signature or a
  failing traceback. Sage compatibility supercategories may remain raw Sage
  supercategories, but constructions produced from the project hierarchy must land
  back in the project hierarchy.
- **Is a simpler mathematical design change available?** Many wrong fixes in this
  subtree came from adding machinery around a bad model: helper registries, classcall
  gymnastics, local construction wrappers, fallback imports, post-hoc mixin splicing,
  or one-off subtree patches. Before adding any such machinery, ask whether the right
  move is a smaller design change: make the wrapper a real subclass of the Sage base,
  use the singleton Sage base up front, let Sage's `_with_axiom` resolve the axiom,
  move a repeated construction to `UniversalSubcategoryMethods`, or reclassify the
  object as a constructor namespace, predicate subcategory, or endset subcategory.
- **Are we reimplementing Sage instead of exposing Sage?** This spec wraps and
  constrains Sage's category machinery; it should not recreate that machinery in local
  code. If the proposed fix manually reproduces method-provider lookup, axiom
  resolution, supercategory traversal, singleton promotion, or construction-category
  behavior, stop and find the smallest hook where Sage already performs that work.
- **Is the nontrivial code actually forced?** The default design is the naive explicit
  pattern: subclass the relevant wrapped Sage base, call the relevant Sage method or
  `super()`, register with `Cat()` only at the wrapper boundary, and keep literal
  methods such as `self._with_axiom("Finite")` or
  `SomeConstruction.category_of(self)`. Anything beyond that must document why the
  naive pattern fails, what breaks without the nontrivial code, and which Sage source
  line or documented behavior forces the departure.
- **Is the proposed fix deleting the evidence?** Removing `NEEDS_DECISIONS` before the
  mathematical issue is fixed, relaxing `@final`, deleting an `@abstract_method`,
  weakening a category assertion, adding `hasattr` checks, or catching errors to keep
  going are false resolution. Such edits make the current failure disappear while
  moving the spec away from its intended mathematics.
- **Would the same reasoning find the next instance?** Encode the correction as a
  local ownership rule or audit question, not as a one-off patch. The reusable lesson
  from `Autset` is not only "`Autset` sits under `Endset`"; it is "identify whether a
  construction is a category, subcategory, object-level parent, or predicate subset
  before choosing where to wire it."

Audit red flags are diagnostic, not cosmetic. Use them as an early-warning system:
when you see the code shape below, suspect the named design failure and inspect the
owning layer before editing locally.

- **Extensive software-engineering code in a category definition**:
  - What makes it a red flag: category specs should read like mathematical
    declarations. Elaborate routing, registries, fallback logic, class surgery, or
    large imperative glue means the category definition is doing integration work.
  - Suspect: the real design belongs in `cat/base_category_types.py`,
    `cat/universal_subcategory_methods.py`, `utils.py`, or an `implementations/`
    subtree.
  - Audit response: do not polish the local code. Ask which base wrapper,
    universal method class, or implementation layer should own the behavior.
- **Complex class manipulation**:
  - What makes it a red flag: `__class__` mutation, class-base mutation, classcall
    internals, generated provider classes, post-hoc splicing, or broad fallback logic
    are brittle and usually recreate Sage internals.
  - Suspect: the design was invented from a clean-slate Python model instead of from
    Sage's existing category patterns.
  - Audit response: read the relevant Sage source and try ordinary subclassing,
    singleton bases, `Parent` registration, `_with_axiom`, and Sage method providers
    before accepting any class manipulation.
- **Explicit provider subclassing inside category specs**:
  - What makes it a red flag: a nested `ParentMethods`, `ElementMethods`,
    Hom-category `ElementMethods`, `SubcategoryMethods`, or construction-specific method provider
    explicitly subclasses another provider class, helper class, or mixin. Sage treats
    these nested classes as flat method providers and builds the actual generated-class
    inheritance from `super_categories()` through `_make_named_class`.
  - Suspect: the category relation, axiom relation, or method owner is missing or
    modeled at the wrong layer. A provider superclass is usually an attempt to patch
    the Python MRO instead of stating the mathematical category graph.
  - Audit response: remove the Python inheritance from the provider design. Put shared
    methods on the lowest mathematically correct category, express the relationship via
    `super_categories()`, `_with_axiom`, or the proper Sage construction category, or
    document the missing owner as a design decision. Do not copy provider methods or
    splice method-provider bases to make a category assertion pass.
- **Strict-supercategory leaks**:
  - What makes it a red flag: a category defines methods that already make sense in a
    strict supercategory. For example, module morphisms should not be the first place
    one worries about `domain`, `codomain`, `__call__`, identity, composition, inverse,
    or invertibility.
  - Suspect: a missing generic hom category, end category, aut category, morphism,
    Cat-object, or universal subcategory-method class, or a subtree spec written
    from the wrong mathematical point of view.
  - Audit response: lift the method to the lowest mathematically correct common
    category and leave specialized subtrees to state only additional laws. Ask what a
    qualified implementer of this category should have to think about: a module spec
    should expose module-theoretic enrichment, not basic category-theoretic mechanics.
- **Implementation-convenience ownership**:
  - What makes it a red flag: an argument says a method belongs somewhere because it is
    easier to implement, easier to share, already available in a helper, or hard to
    provide for all objects at the mathematically correct level.
  - Suspect: generic software-engineering reasoning has replaced mathematical
    specification. A spec is allowed to demand missing implementations when the demand
    is mathematically correct.
  - Audit response: ignore implementation convenience until the mathematical owner is
    fixed. Then decide whether the implementation lives on the category definition,
    `utils.py`, or an `implementations/` subtree.
- **Duplicated code across categories or subtrees**:
  - What makes it a red flag: repetition of the same method, construction selector,
    predicate, or abstract declaration shows that no high-level owner was identified.
  - Suspect: hacking by local normalization instead of review of the subcategory
    hierarchy.
  - Audit response: do not normalize duplicates one by one. Move the behavior to the
    shared category, universal method class, or wrapped base layer that explains all
    occurrences at once.
- **Programmer-brained vocabulary**:
  - What makes it a red flag: type names, method names, or docs describe storage
    shape, implementation role, or mechanically expanded Sage class names instead of
    mathematical nouns.
  - Suspect: shallow pattern matching on source names or signatures rather than
    reading the written mathematics. `PolynomialRingElement` is usually just
    `Polynomial`; `HomsetElement` is usually a morphism.
  - Audit response: rename from Sage docs and mathematical vocabulary, and reject
    software-only helper types unless they are private implementation details.
- **Downstream symptom patches**:
  - What makes it a red flag: a fix changes `Cat()` to compensate for an ordinary
    construction escape, changes a category assertion to avoid a failure, or explains
    a traceback by the last class named in the error rather than by the construction
    path.
  - Suspect: the observed object is only a symptom. Raw Sage supercategories,
    join-category supercategories, and project construction results are different
    questions.
  - Audit response: trace whether the failing object was produced from this hierarchy.
    Project constructions must stay in the local hierarchy; raw Sage supercategories
    may remain compatibility declarations.
- **Set-level ownership of categorical facts**:
  - What makes it a red flag: set specs define or justify facts such as the existence
    of Hom/End/Aut, `End(X)` being a monoid, or `Aut(X)` being a group.
  - Suspect: category-theoretic structure is being pushed into a concrete subtree.
  - Audit response: move the generic fact to Hom/End/Aut or the appropriate
    categorical owner. Let set specs state only the new set-theoretic content, such as
    ambient/coercion-sensitive operations, intersections, complements, and whether
    homsets of sets are sets.
- **Functorial construction categories treated as functors**:
  - What makes it a red flag: a construction category is expected to have functor
    methods such as domain, codomain, callability, `pushout`, or `merge` without first
    proving it is an actual functor/morphism object.
  - Suspect: ontology confusion between a category object, a functorial construction
    category, and a construction functor.
  - Audit response: read Sage docs/source for the construction in question and record
    whether the object is a category, a functor, or only a construction parameterizing
    categories.
- **Helper framework growth around a bad model**:
  - What makes it a red flag: `_registered_*`, source-shape registries, local
    dispatchers, catch-all wrappers, broad classcall hooks, or fallback imports appear
    while the mathematical owner is still unclear.
  - Suspect: the simple design change has not been considered: real subclassing,
    `Parent` registration, using the singleton Sage base, routing through
    `UniversalSubcategoryMethods`, or reclassifying the object.
  - Audit response: find the smaller mathematical redesign that removes the need for
    the framework.
- **Runtime checks outside categorical predicates**:
  - What makes it a red flag: `isinstance`, `hasattr`, `getattr`, `type()`, or
    `callable()` appear in code where the prose wants category membership, typed
    attribute access, or declared structure. Each is a signal that the code is
    guessing about shape at runtime rather than carrying that information through
    the type/category system.
  - Suspect: a missing predicate subcategory, such as `Cat().JoinCategories()`; a
    missing `is_*` predicate pattern; an undeclared optional attribute; or a
    function signature that accepts too-broad a type.
  - Audit response: apply the introspection red-flag reasoning chain from the
    `anti-slop` skill (`references/code-patterns.md#introspection-red-flags`).
    Centralize legitimate boundary checks and replace interior checks with
    categorical membership, typed access, or explicit overloads.
- **Engineering names in mathematical contexts**:
  - What makes it a red flag: category, axiom, or method names contain words that
    describe code structure rather than mathematical structure: `Base`, `Abstract`,
    `Impl`, `Concrete`, `Manager`, `Factory`, `Registry`, `Handler`.
  - Suspect: the agent is thinking in implementation architecture terms (class
    hierarchies, design patterns) when the task requires mathematical vocabulary
    (axioms, predicates, categories). The name `FiniteTotallyOrderedBase` smuggles
    "Base" (a programming concept) into what should be axioms (`finite`,
    `totally_ordered`).
  - Audit response: remove the engineering word and check whether the remaining
    name still expresses a complete mathematical concept. If yes, rename. If no,
    the concept is underspecified — the agent is using engineering structure as
    a substitute for mathematical precision. See the `anti-slop` skill,
    `references/code-patterns.md#engineering-names-in-mathematical-contexts`.
- **Reward-hacking edits**:
  - What makes it a red flag: removing `NEEDS_DECISIONS`, relaxing `@final`, deleting
    an `@abstract_method`, weakening a category assertion, adding `hasattr`, or
    catching errors makes the failure disappear without resolving the mathematical
    issue.
  - Suspect: the edit is optimizing for the current tool result, not for the spec.
  - Audit response: restore the sensor and fix the missing implementation,
    mathematical owner, or wrapper integration it exposed.

**Explicit Method Classes**:
Each subcategory MUST explicitly state its `ParentMethods`, `ElementMethods`,
Hom-category refinements, and `SubcategoryMethods` classes (as applicable).
To document the full method set inherited from supercategories and facilitate future
refactoring, every subcategory must list **ALL methods inherited that it can
override**.
Methods that are not currently being overridden with a concrete implementation or a
refined `@abstract_method` signature MUST be included with a `...` body.
This ensures the subcategory file serves as a complete map of its own method set.

**One Source of Truth for Utils**:
All **truly reusable GENERAL logic** belongs in the top-level `utils.py`. This is
reserved for software engineering tasks like converting data types (generators, lists,
etc.), category refinement machinery, and project-wide ABC validation.

**Nontrivial Implementations**:
Implementations that are not trivial (as defined in "The Art of Trivial
Implementations") must be factored into an `implementations/` subdirectory within
each subtree. The structure and naming of this directory MUST mirror the
`subcategories/` hierarchy exactly.
Categorical glue that is trivial (<= 10 lines) and specific to a subtree belongs on
the category definition itself.

**Completeness**: the spec must fully capture all existing Sage methods on objects in
each subcategory as `@abstract_method` declarations.
Existing Sage objects must pass regression tests with nearly all methods declared
abstract. The only allowed violations are genuine Sage gaps, which are recorded
exclusively in `sage_gaps/` tests.

**The Art of Trivial Implementations**:
Mostly trivial implementations (<= 10 lines) MUST remain on the category definition
when they express basic categorical identity or definition. Moving such glue to
`utils.py` is an anti-pattern that obscures the mathematical structure of the spec.

Permitted concrete bodies on category and subcategory method classes include:
- Trivially true/false predicates (e.g., `is_finite() -> True`)
- Explicit `match/case` logic for category membership or simple dispatch
- Methods defined purely in terms of other `@abstract_method` declarations on the
  same method class (e.g., `is_bijective` defined via `is_injective` and
  `is_surjective`)
- Simple transformations and pass-throughs
- Wraps and refinements (e.g., calling `refine_category` with fixed arguments)

**Truly complex implementations are banned.** Anything involving iteration logic
(loops), heavy computation, or substantial branching belongs in the top-level
`utils.py`.
`try/except` is banned everywhere.

## Category Architecture

Each top-level category (`Sets`, `Rings`, `Modules`, etc.)
is defined in its subtree's `__init__.py`. That file defines exactly:

- Private method classes: `_XParentMethods`, `_XElementMethods`, and
  `_XHomElementMethods` when a Hom-category element method class is needed.
- The category class itself, which must include:
  - A `__contains__` predicate implemented with `match/case`
  - A `Constructors` inner class (see below)
- Imports of subcategory classes from `subcategories/` to wire them into the hierarchy

**`__init__.py` is the public API document.** Reading it must be sufficient to
understand the full public API of the category: its method classes, its axiomatic
subcategories, its constructions, and its constructors.
Keep it readable — only include the trivial categorical glue and wiring permitted by
the Spec Philosophy.

The module docstring of `__init__.py` must faithfully record the full subcategory
hierarchy as a tree, showing the mathematical relationships between all subcategories
defined in that subtree.

**SubcategoryMethods** is an inner class defined in every top-level category's
`__init__.py`. Its methods are available on every subcategory instance (e.g.,
`Sets().Finite().Subobjects()` returns the category of finite subsets).

**Universal Construction Methods**: The following methods are universal category-object
constructions. They are defined once in `cat/universal_subcategory_methods.py` and are
automatically mixed into the `SubcategoryMethods` provider of every wrapped category.
Do not copy these methods into individual subtrees unless the subtree is deliberately
overriding the universal behavior with a more specific mathematical construction.

Universal methods:
- `Subobjects()` (and aliases like `Subsets = Subobjects`)
- `Quotients()`
- `Subquotients()`
- `ObjectsOver()`
- `ObjectsUnder()`
- `CartesianProducts()`
- `HomCategory()`
- `EndCategory()`
- `AutCategory()`

Literal implementation example:
```python
class UniversalSubcategoryMethods:
    @cached_method
    @final
    def Subobjects(self):
        from .base_category_types import SubobjectsCategory
        return SubobjectsCategory.category_of(self)

    Subsets = Subobjects

    @cached_method
    @final
    def HomCategory(self):
        from ..homsets import HomCategoryConstruction
        return HomCategoryConstruction.category_of(self)
```

Note that these are distinct from the attributes on the category class itself
(e.g., `Sets().HomCategory`), which return the base construction category for that
subtree (e.g., `HomCategory = SetHomCategory`). The universal
`SubcategoryMethods` method class is what enables navigation like
`Sets().Finite().HomCategory()`.

`C.Hom()` is not a category-level construction. For category objects `C, D in Cat()`,
`C.Hom(D)` is the object-level functor category `Hom_{Cat}(C, D)`. The category-level
functorial construction is `Hom_*: Cat -> Cat`, sending `C` to
`C.HomCategory() = Hom_C`; its evaluated constructor is
`C.HomCategory().Of(A, B)` for objects `A, B in C`.

Other constructions like `TensorProducts()` should be added to
`SubcategoryMethods` only where mathematically appropriate, following the same
pattern.

**Axiomatic subcategories** must be wired to real classes that add genuine spec work.
E.g. `Sets().Finite()` is not just structural — the linked class must declare that
`is_finite()` returns `True`, `is_countable()` returns `True`, `__len__` is defined,
etc.

## Axiom Philosophy and Mathematical Precision

- **Axiom Reuse**: Prefer to reuse existing axiom names (e.g., `Commutative`,
  `FiniteDimensional`, `Semisimple`, `WithBasis`) rather than redefining new names for
  each category. Define and register each axiom name exactly once in `axioms.py`, then
  reuse it across subtrees when it expresses the same mathematical restriction.
  If the same word would mean fundamentally different mathematics in two category
  families, choose a more specific name instead of overloading the axiom.
- **Axioms Carry Witnesses**: Every axiom is interpreted as carrying a witness. For
  example, `FinitelyGenerated` doesn't just mean the abstract existence of a
  generating set; it means the objects in that category MUST carry the actual **data**
  of a finite generating set witnessing the property.
- **Terminology**: Axioms like `WithBasis` (which could equally be `HasBasis`) imply
  the object carries the data of a witnessing set.
- **Mathematical Precision vs. Sage Looseness**: Do not use "basis" or "dimension"
  as loosely as Sage:
  - Modules can have generating sets that are NOT bases.
  - Rings may not satisfy the Invariant Basis Property (IBP).
  - `dimension` is strictly defined for free $R$-modules (or in specific geometric
    contexts like topological spaces), not as a general synonym for "size".
- **Documentation of Discrepancies**: Be careful with Sage's terminological looseness.
  Any discrepancies or inaccuracies in Sage's model compared to precise mathematics
  MUST be documented in the subtree's `MAPPING.md` when they affect mathematical
  mapping, or as a Nimbalyst tracker item when they are implementation-gap,
  decision, or deferred-work findings.

### Direct implementation categories vs. axiomatic restrictions

Use a direct category class when the category is a genuine implementation target.
For example, a category such as `FinitelyGeneratedFreeModulesOverPID` is a concrete
mathematical and computational class of objects: there is one such category, it may be
reachable by a chain such as `Modules(R).FinitelyGenerated().Free().OverPIDs()` or by a
shortcut, and it is the category whose objects should eventually be implemented by the
corresponding finite-generation/PID free-module machinery.

Use a `with_axiom` restriction when the adjective must be attachable to any existing
subcategory. `Free` is the model case. `Modules(R).Free()` exists for mathematical and
spec reasons even when arbitrary free `R`-modules have little computable structure
without hypotheses on `R`. More importantly, any subcategory `C` of `Modules(R)` must be
allowed to form `C.Free()` to declare "free objects inside `C`". When `C = Modules(R)`,
Sage's `base_category_with_axiom`/`_base_category_class_and_axiom` registration may
return the registered class. For other `C`, the construction primarily records the
mathematical restriction and enforces a consistent method class; it is not the
assertion that Sage has already implemented every project method for that category.

Do not collapse axiomatic restrictions into implementation categories merely because
some restricted cases are computable. Further restrictions such as finite generation,
basis data, or base-ring hypotheses determine the algorithms.

### Naming: Mathematics, Not Implementation

Mathematical category, axiom, and method names MUST express mathematical structure,
not implementation architecture. Words that describe code (class, base, abstract,
impl, manager, factory, registry, handler) do not belong in category or axiom names.

**The anti-pattern**: an agent thinks "I need a base category for finite totally
ordered sets" and names it `FiniteTotallyOrderedBase`. The word "Base" describes
the implementation artifact (a base class), not the mathematical property. The
mathematical concept is "finite" and "totally ordered" — these are axioms, not
class hierarchy positions.

**Signal detection**: if a category, axiom, or method name contains a word that
would appear in an object-oriented design pattern textbook but not in a
mathematics textbook, it is an engineering name smuggled into mathematical code.
Common smuggled words: `Base`, `Abstract`, `Impl`, `Concrete`, `Manager`,
`Factory`, `Registry`, `Handler`, `Structured`, `Configurable`.

**Correct approach**: separate the mathematical claim from the implementation
artifact. The mathematical claim (finite, totally ordered, countable, free) is
a category axiom or restriction. The implementation artifact (which Python class
satisfies it in Sage's category framework) is a separate engineering decision
that does not dictate the name.

See the `anti-slop` skill, `references/code-patterns.md#engineering-names-in-mathematical-contexts`
for the general pattern and additional signals.

**Subobject types in `types.py`**: types like `Subset`, `Submodule`, `QuotientModule`
must be defined in `types.py` and used explicitly in method signatures to express
mathematical restrictions.
E.g. `intersection(self, other: Subset) -> Subset`, not
`intersection(self, other: Set) -> Set`.

**`Constructors`** is an inner class on the category, not a subcategory.
It organizes all entry points into Sage constructions: each method calls the original
Sage constructor and refines the result into the correct place in the hierarchy.
Accessed as `Sets().Constructors()`, `Rings().Constructors()`,
`Modules(R).Constructors()`. Examples:
- `Rings().Constructors().ZZ()` — wraps Sage's `ZZ` and refines it
- `Modules(R).Constructors().FreeModule(R, 5)` — wraps Sage's `FreeModule` and refines
  it

`Constructors` replaces all previous `NamedSets`, `NamedRings`, `NamedModules`
sub-namespaces uniformly.

**`subcategories/`** is a plain directory (no `__init__.py`) containing one `.py` file
per mathematical subcategory, named using real mathematical vocabulary (e.g.
`finite.py`, `totally_ordered.py`, `free.py`). The parent `__init__.py` imports from
these files directly.
Nothing in `specialized.py`, `named.py`, or any other flat aggregator file.

## Hom, End, and Aut Categories

Hom categories (`Hom_C`), end categories (`End_C`), and aut categories (`Aut_C`) each
have their own separate files at both the top level and within each subtree, following
the same organizational principle as other category objects.

### File organization

- **Top level**: `homsets/` defines the generic wiring shared across all subtrees —
  `HomCategoryOf(C)`, `HomCategoryOf(C).EndCategory()`,
  `HomCategoryOf(C).EndCategory().AutCategory()`, evaluated constructors `Of(...)`,
  and the aut-category integration layer. This is the single place where `Aut_C(A)`
  as a `ConditionSet` over `End_C(A)` is implemented.
- **Per subtree**: `<subtree>/homsets.py` defines subtree-specific hom categories
  (e.g. `SetHomCategory`, `RingHomCategory`) and their
  `ParentMethods`/`ElementMethods`. These import and inherit from `HomCategoryOf`,
  `GenericEndCategory`, and `GenericAutCategory`.

### Aut Categories Are Wired Repo-Wide

Sage has no native generic aut category — it provides `Homsets` and the `Endset` axiom
hook, but nothing for generic automorphism-group generators.
**Aut categories must be integrated at the top level, once, so that individual subtrees never
reinvent this wiring.**

An aut category object is mathematically an end category object with an underlying `ConditionSet` that checks
invertibility: `Aut(X) = {f ∈ End(X) | f is invertible}`. The top-level `homsets/`
subtree must define:

- The `Aut` parent class, constructed from an `End` plus an invertibility condition.
- Generic `ParentMethods` and `ElementMethods` available on all aut categories
  regardless of the ambient category (e.g. `end_category`, `domain`, `codomain`, `identity`, `inverse`,
  `composition`, `is_invertible`, `group_structure`, and `order`).
- Generic element methods on aut categories (i.e. `Automorphism` methods like `inverse` and
  `order`, including predicates such as `is_involution`).

Sage still requires the axiom hook names `Endset` and `Autset` for `_with_axiom(...)`.
Those names are interop hooks, not public project selectors. Public navigation is
`HomCategory()`, `EndCategory()`, `AutCategory()`, and evaluated constructors
`HomCategory().Of(A, B)`, `EndCategory().Of(A)`, `AutCategory().Of(A)`.

This wiring defines `Aut(X)` as an object of `Groups`. It is not the assertion that
`Aut(X)` lies in `FinitelyGeneratedGroups`, `FinitelyPresentedGroups`, a finite-group
category, or a generated matrix-group category. Those category memberships carry the
corresponding generator, presentation, finiteness, or chosen-generator structure.

### What subtrees own vs. what the top level owns

| Concern | Owner | Examples |
| --- | --- | --- |
| Generic Hom/End/Aut construction and dispatch | Top-level `homsets/` | `HomCategoryOf(C)`, `AutCategory().Of(A)`, ConditionSet integration |
| Generic methods on all aut categories | Top-level `homsets/` | `Aut.ParentMethods.identity`, `Aut.ElementMethods.inverse` |
| Category-specific aut properties | Subtree `<subtree>/homsets.py` | `Aut_{Set}(X).ParentMethods.is_transitive`, `Aut_{Ring}(X).ElementMethods.preserves_units` |
| Category-specific Hom/End/Aut definitions | Subtree `<subtree>/homsets.py` | `SetHomCategory`, `RingHomCategory`, `RModuleHomCategory` |
| Wiring Hom/End/Aut into a subtree's category namespace | Subtree `<subtree>/__init__.py` | `Sets().HomCategory()`, `Sets().EndCategory()`, and `Sets().AutCategory()` delegate to the subtree hom category |

Subtrees focus on **categorical properties**: what methods should `Aut_{Set}(X)` have,
what supercategories and additional structure it carries, how it refines the generic
aut category. They must never reimplement the generic ConditionSet-on-End machinery that
produces `Aut_C(A)` from `End_C(A)`.

The first model for extra structure is `R-Mod`: `Modules(R).HomCategory()` inherits
the generic `HomCategoryOf(Modules(R))` hierarchy and also declares the module
structure on `Hom_R(M, N)`. Its end subcategory additionally declares the algebra
structure on `End_R(M)`. Other subtrees follow the same rule: declare only the
additional mathematical structure that genuinely exists in that category.

### Morphism, Endomorphism, and Automorphism element types

The element types follow the same naming convention as other morphism types (see Type
System Rules):

- `Morphism` — element of `Hom_C(A, B)`
- `Endomorphism` — element of `End_C(A) = Hom_C(A, A)`
- `Automorphism` — element of `Aut_C(A)`, the invertible part of `End_C(A)`

These are defined in `types.py` and used in method signatures throughout.
Each subtree's `homsets.py` declares `ElementMethods` for its specific
Hom/End/Aut element types, inheriting from the top-level base methods.

## File Tree

```
category_specs/
├── AGENTS.md
├── __init__.py           # imports all subtrees, calls register_all()
├── axioms.py             # ALL axiom definitions and registration — single source of truth
├── types.py              # ALL type aliases — single source of truth
├── utils.py             # shared utilities (refine_category, etc.)
├── cat/                 # category of categories; shared category-object boilerplate
├── homsets/             # generic Hom/End/Aut category dispatch, Autset interop wiring, base classes
│   ├── AGENTS.md
│   ├── __init__.py
│   ├── category_obligations.sage
│   ├── docs/
│   └── tests/
├── justfile
└── <subtree>/            # e.g. sets/, rings/, modules/, algebras/, posets/, topological_spaces/
    ├── AGENTS.md         # subtree goals and task list
    ├── __init__.py       # defines category, ParentMethods, ElementMethods,
    │                     # Constructors; imports from subcategories/
    ├── homsets.py        # subtree-specific HomCategory/EndCategory/AutCategory refinements
    ├── subcategories/    # one .py file per mathematical subcategory (no __init__.py)
    │   ├── finite.py
    │   ├── constructions/
    │   │   ├── subobjects.py
    │   │   ├── subquotients.py
    │   │   ├── quotients.py
    │   │   ├── objects_over.py
    │   │   ├── objects_under.py
    │   │   └── cartesian_products.py
    │   ├── free.py
    │   └── ...
    ├── implementations/  # nontrivial implementations (mirrors subcategories/ hierarchy)
    │   ├── finite/       # implementations of finite objects
    │   ├── free/         # implementations of free objects
    │   └── ...
    ├── category_obligations.sage # asserts representative category obligations
    ├── docs/
    │   ├── SAGE_INVENTORY.md # Sage classes, methods, on-disk paths
    │   └── MAPPING.md        # decisions mapping Sage categories -> our hierarchy, with mathematical justification
    └── tests/
        ├── new_spec/     # tests of the new category spec (see Testing rules)
        ├── regression/   # per-constructor regression tests
        └── sage_gaps/    # raw Sage gap assertions (see Testing rules)
```

- Axioms are defined and registered **only** in the root `axioms.py`. No subtree defines
  or registers axioms.
- Axiom names are global mathematical vocabulary. Define and register each axiom name
  exactly once, then reuse it across categories when it expresses the same restriction.
  Examples: `Commutative`, `FiniteDimensional`, `Semisimple`, and `WithBasis`.
  If the same word would mean different mathematics in two category families, choose a
  more specific name instead of overloading the axiom.
- No `specialized.py`, `named.py`, `constructions.py`, or other flat aggregator files.
- `subcategories/` may nest arbitrarily to reflect the mathematical hierarchy.
  A subcategory with many sub-subcategories gets its own subdirectory (e.g.
  `subcategories/free/over_pids/`). A single file suffices when the subcategory is a
  leaf or has few children.
- Construction-style subcategories live under `subcategories/`, split by mathematical
  notion. Use `subcategories/constructions/<notion>.py` for attachable Sage
  construction categories such as subobjects, quotients, subquotients, hom categories,
  end categories, aut categories, objects-over, and objects-under. These classes may extend Sage
  functorial construction classes and use `category_of`; the target organization
  still places the category object by mathematical notion.

- If a subcategory introduces a genuinely independent and complex method class (new
  `ParentMethods`, `ElementMethods`, or Hom-category element methods), promote it to its own top-level
  subtree rather than burying it.
  E.g. `lattices/` and `algebras/` are top-level, not nested inside
  `modules/subcategories/`.

## Implementation Rules

Nontrivial implementations (those in the `implementations/` subdirectory) must follow
these technical requirements:

1.  **Direct Extension**: Every implementation must extend a class that exists as a
    spec file in the `subcategories/` hierarchy.
2.  **Completeness**: Implement ALL `@abstractmethod` declarations from the spec
    and any parent specs.
3.  **No Sage abstract_method**: `@abstractmethod` from `abc` is the only acceptable
    abstract method decorator. `from sage.misc.abstract_method import abstract_method`
    is banned — it was cargo-culted from Sage's category code and provides no
    functionality that `abc.abstractmethod` doesn't. `category_specs/utils.py` is the
    sole file that imports `AbstractMethod` (the class, for isinstance checks in the
    validation machinery) — do not touch that import.
4.  **Pydantic Only**: Use **Pydantic ONLY** for data modeling and state management.
    `dataclasses`, raw classes, or other modeling libraries are banned.
5.  **Classmethod Constructors**: Use `classmethod` constructors for all object
    creation (e.g., `MyImpl.from_data(...)`).
6.  **Post-init Validation**: Use a **single post-init validator**
    (`model_post_init` in Pydantic v2) for all state validation after construction.
7.  **Constructor Collectors**: `Constructors` is a simple opt-in collection class on
    selected category objects. It is not a category, not a functorial construction,
    and not a refinement target. The declaration is the existence of an explicit
    nested `Constructors` class on a category object; do not add a separate public
    registration method, flag, or construction category for this. In this spec work,
    constructor collectors should live on explicit top-level category objects by style
    and readability, rather than on deeply nested subcategories. Do not add assertion
    guards or other runtime enforcement whose only purpose is to prove that a
    constructor collector is top-level.
8.  **Constructor Collection**: The intended public constructor namespace is the canonical collection
    exposed directly from `Cat().Constructors()`: Cat backend code observes category
    objects, collects methods under each explicit `C.Constructors`, and exposes
    prefixed forwarding methods such as `C_x_y_z`. There is no public
    `Aggregate()`/`AggregateFor(...)` layer. Do not repeat the category noun in
    generic constructor names: prefer `C.Constructors().from_xyz(...)`, which Cat
    exposes as `cat_prefix_from_xyz(...)`, rather than
    `C.Constructors().category_from_xyz(...)`.
9.  **No Subcategory Constructor Namespaces**: Subcategories are refinement targets and
    method owners, not constructor namespaces. Do not add or propose constructor paths
    such as `Algebras(k).FiniteDimensional().WithBasis().Constructors()` merely because
    Sage has a constructor family or because an implementation can refine into that
    subcategory. Put the advertised constructor on the chosen category collector and
    refine the constructed object afterward.

## super_categories

`super_categories()` must return a plain list of category instances, e.g.
`[CategoryA(), CategoryB()]`. Never call `Category.join` inside `super_categories()` —
Sage's framework handles the join internally.
`_joined_super_categories` is banned.

Each subcategory must declare **both** its parent in our hierarchy and the corresponding
Sage supercategory (or categories).
This ensures:
- Existing upstream `@abstract_method` declarations and unimplemented methods from Sage
  are exposed on our objects.
- Objects refined into our subcategory still register as members of the corresponding
  Sage category (e.g. `ZZ in SageRings()` still holds after refinement into our
  `Rings()`).

Example:
```python
def super_categories(self):
    return [Sets().Finite(), SageFiniteSets()]
```

## Refinement

All refinement goes through `utils.refine_category` directly.
No per-subtree `_refine_named_X` wrapper functions (e.g. `_refine_named_set`,
`_refine_named_ring`, `_refine_named_module`). These are banned — they are redundant
indirection over the same call.

Refinement declares one category, not a manually assembled category list.
Always refine to the smallest mathematically correct category for the object.
Do not write `refine_category(X, [Rings(), _Qp()])`, `refine_category(X,
[Sets(), _FiniteSets()])`, or any equivalent multi-category list.
The specific target category's `super_categories()` graph is the source of inherited
membership; restating ancestors at the call site defeats the purpose of the category
hierarchy and hides graph defects.

## Overall Design

This hierarchy is a **non-destructive staged replacement** for Sage's category system.
The pattern is: expose category-owned wrappers for existing Sage constructor shapes,
call the original implementation behind that category boundary, then refine the result
into the new subcategory hierarchy.
Never destructively replace or monkey-patch Sage internals.

## Category Structure

- Every object category exposes object and element method classes via inner classes:
  `ParentMethods` and `ElementMethods`. Morphism abstract methods belong on the
  relevant Hom-category `ElementMethods`.
- Every category exposes a `Constructors()` sub-namespace
  (e.g. `Sets().Constructors()`, `Rings().Constructors()`,
  `Modules(R).Constructors()`) for all Sage constructor entry points known to that
  category. Constructor wrappers must be collected here, not scattered.
- Method-class separation is strict: a method belongs in the category whose axioms are
  the minimum required for it to be well-defined.
  Ring-theoretic methods must not appear in `Sets`; module-theoretic methods must not
  appear in `Rings`; etc.

## Sage Naming Disambiguation

When importing a Sage category that shares a name with one of ours, alias it as `SageX`:
```python
from sage.categories.sets_cat import Sets as SageSets
from sage.categories.modules import Modules as SageModules
```
Never let Sage and local names collide silently.

## Sage Inventory and Mapping

Each subtree maintains a `docs/` folder with two canonical files:

- **`SAGE_INVENTORY.md`**: indexes Sage method clusters under semantic extraction or
  compatibility audit for that subtree — full class name, method signatures, examples,
  behavior notes, and on-disk path to the implementation (e.g.
  `$SAGE_ROOT/src/sage/categories/sets_cat.py:142`). It must support mathematical
  extraction from source behavior, not merely collect names and signatures.

- **`MAPPING.md`**: records, for each Sage category, the mathematical justification for
  how it maps to our hierarchy.
  Must document: what Sage provides, the correct mathematical concept, the
  justification, and the consequence for refinement and regression tests.
  Mapping starts from Sage method behavior, not from the Sage class where a name happens
  to be implemented, not from rows already written in the project document, and not from
  an abstract category primer. Before editing a mapping row, read the relevant Sage
  body, examples, and written docs deeply enough to record inputs, outputs, branch
  cases, return objects, side conventions, helper behavior, and compatibility details.
  Then extract the mathematical operation, introduce or reference only the vocabulary
  required by that behavior, and state the weakest structure, hypotheses, claimed
  category/refinement membership, and witness data.
  For every method row, the correct mathematical concept must be a complete sentence
  that would make sense without Sage. Examples: "In any category, morphisms compose";
  "In an additive category, `Hom(X,Y)` is an abelian group and composition is
  bilinear"; "In an abelian category, kernels and cokernels exist." A row that only
  names a Sage class, source file, project category, or migration consequence has not
  stated the mathematics.
  Assign the method to the most general standard category where that sentence is true.
  If the method belongs to a stronger category, record that category/refinement and its
  witness data rather than adding an external computability label.
  Do not leave evaluation, composition, Hom addition, kernels, cokernels, images, or
  analogous standard constructions on a special Sage class merely because that is where
  Sage implements them.
  Do not replace standard mathematical language with local jargon: use categories,
  objects, morphisms, Hom objects, subobjects, quotient objects, kernels, cokernels,
  images, tensor products, and chosen presentations when those are the notions meant.
  Path spelling, row formatting, headings, and prose polish are not mapping progress
  unless they correct the Sage method set, the mathematical proposition, the weakest
  owner, the hypotheses, the return object, or the replacement path for Sage behavior.
  Example: Sage's `EnumeratedSets` → our `Countable` axiom, because countability =
  existence of an enumeration f: X → ℕ; the spec must exhibit such a function; all Sage
  enumerated sets must refine to `Sets().Countable()`.

## Error Handling

- No `try/except` blocks anywhere.
- Use `assert` to enforce preconditions and requirements.
- Any method that is meant to raise an error must remain `abstract`.

## Axiomatic Subcategory Registration

- Each axiom class must declare `_base_category_class_and_axiom` as a **class-level
  attribute** on itself, e.g.:
  ```python
  class _FiniteSets(CategoryWithAxiom):
      _base_category_class_and_axiom = (Sets, "Finite")
  ```
- Never splice `_base_category_class_and_axiom` onto classes at module level after their
  definition. That pattern is banned.

## Method Surface Classes

For top-level categories, `ParentMethods` and `ElementMethods` must be factored into
named private classes and assigned, not defined inline.
The names must be mathematically explicit:
- `_SetObjectMethods` (not `ParentMethods`) — methods on objects in `Sets()`
- `_SetElementMethods` (not `ElementMethods`) — methods on elements of sets
- `_SetMorphismMethods` is banned. Methods on morphisms between objects of `Sets()`
  belong on `Sets().HomCategory().ElementMethods`, because morphisms are elements of
  Hom objects, not elements or morphisms of the object category itself.

These are then assigned inside the category:
```python
class Sets:
    ParentMethods = _SetObjectMethods
    ElementMethods = _SetElementMethods
```

This is self-documenting: the class name explicitly states what the methods are for.

## No Splicing

Never add methods or classes to a category class after its definition (e.g.
`MyCategory.ParentMethods.foo = ...` or `MyCategory.MySubcategory = ...` at module level).
All methods and subcategory attributes must be declared inside the class body.
Splicing fragments documentation and makes the spec impossible to read as a single
coherent document.

**The LazyImport Pattern**:
To wire subcategories into a category while avoiding circular imports (e.g., when a
subcategory file needs to import the parent category for registration), use
`sage.misc.lazy_import.LazyImport` at the class level:

```python
class MyCategory(Category):
    # ...
    MySubcategory = LazyImport("category_specs.subtree.subcategories.file", "_MySubcategoryClass")
```

This ensures the subcategory module is only loaded when the attribute is accessed,
breaking the import cycle and keeping the category definition clean and centralized.
All subcategory wiring must follow this pattern instead of module-level assignment or
splicing.

## Method Overrides

- When a subcategory provides a concrete implementation of a method declared
  `@abstract_method` in a parent category, it must be decorated with `@override` (from
  `typing` or `typing_extensions`).
- **Trivial answers are overrides, not exemptions.** When an `@abstract_method` is
  mathematically well-defined for all objects in a parent category, subcategories where
  the answer is trivial must still override with the concrete trivial implementation —
  they must never weaken or remove the abstract requirement.
  E.g. `completion()` is defined for any ring and any ideal; fields override it to
  handle the trivial case (only ideals are 0 and R), rather than being exempted from the
  requirement entirely.

## Method Placement

- All methods must be defined at the **highest category** for which they are universally
  well-defined.
- Before placing a method, state the mathematical sentence that makes it exist. If the
  sentence is "in any category, morphisms compose," the method cannot be owned by
  modules or lattices. If the sentence is "in an additive category, `Hom(X,Y)` is an
  abelian group," Hom addition belongs to additive categories. If the sentence is "in
  an abelian category, kernels and cokernels exist," kernel and cokernel methods belong
  there unless the row explicitly records a weaker sourced hypothesis.
- The placement check is a falsification test: push the method upward until the
  mathematical sentence would become false, then place it at the last valid category.
  Sage's implementation class is evidence that the method exists in that example; it is
  not evidence that the example owns the method.
- Every subcategory should declare the object and element method-class entry points
  it owns: `ParentMethods`, `ElementMethods`, and the Hom/End/Aut subcategory
  overrides when those method classes exist. Do not declare `MorphismMethods`; true morphism
  methods are Hom-category element methods.
- A lower category may override a universal method class to specialize the
  mathematics, refine codomains, expose enriched structure, or declare extra
  supercategories. For example, an `R`-module hom category may record that the category
  is self-enriched instead of merely inheriting the ambient Hom object unchanged.
- If a subcategory has no new methods or refinements yet, still create the explicit
  entry point with a `...` body. The stub marks where future specs belong.
- Do not copy inherited method logic at lower levels only to restate behavior. Stub the
  entry point, or override only the part where the lower category adds genuine
  mathematical content.

## Testing (sage_gaps)

Files in `sage_gaps/` directories test raw Sage objects directly — no new category
namespace, no `refine_category`. Their sole purpose is to assert that specific methods
are missing or broken in Sage as-is, proving the motivation for the spec.

- Use bare Sage globals (`ZZ`, `QQ`, `GF(...)`, etc.)
  directly here.
- `with raises(...)` / `pytest.raises(...)` constructions are **only** permitted in
  `sage_gaps/` files. They are banned everywhere else.
- Do not import or use any class from this spec hierarchy in `sage_gaps/` tests.

## Testing (regression)

Regression tests verify that objects constructed through our refined API behave
identically to the original Sage objects and meet all mathematical invariants.

- **Canonical Constructors Only**: Every test must construct its objects through the
  category namespace (e.g., `Rings().Constructors().ZZ()`). Never bypass the API
  with bare Sage globals or ad-hoc creation (`Matrix(...)`, `QuadraticForm(...)`).
- **Use JSON Fixtures**: Use JSON fixture data from `tests/fixtures/` for
  parametrized tests. Assert results against known literature values or proven
  Sage outputs.
- **Expose API Gaps**: If the canonical API is insufficient to express a test, do
  not use a workaround. This is a signal that the spec or its constructors need
  extension; document the gap and expose it for review.

## Testing (new_spec)

Files in `new_spec/` directories test the new category spec, not raw Sage objects.
The objects under test are refined objects exposed on category namespaces.

**Constructor Rule**: Construct test objects through the category namespace entry points
(e.g. `Sets().Constructors().X()`, `Rings().Constructors().X()`,
`Rings().Hom(...)`, etc.).
Never start from bare Sage globals (`ZZ`, `QQ`, `GF(...)`, `PolynomialRing(...)`, etc.)
when the category namespace has the corresponding constructor.
Never call `refine_category(...)` in tests when a category-owned constructor already
exists — the namespace constructor is the implementation witness being tested.

**What to Assert**: Assert properties directly on the refined objects returned by the
category spec. Do not weaken tests by switching to raw Sage constructors.

**Recording Gaps**: When the current implementation does not satisfy the spec, expose
the failure through the category spec itself — build the object through the category
namespace, then let the assertion reflect the gap.
Do not bypass the namespace layer and claim the result says something about the new
spec.

## TYPE_CHECKING

`if TYPE_CHECKING:` blocks are only permitted to resolve a concrete circular import.
Never use them as a general mechanism to defer imports or to define type aliases.
If a type can be imported at runtime without a circular dependency, it must be imported
unconditionally at the top of the file.

The priority is that the definition of e.g. `Polynomial`, `RModule`, `Set`, `Matrix`,
`ModuleMorphism`, `RingEndomorphism`, etc. should all be uniform and global.
Use `if TYPE_CHECKING:` where TRULY needed to avoid circularity and help enforce that
uniformity, not as an escape hatch, for defensive hedging, or as an excuse to redefine
basic nouns/verbs hidden away in subcategory files.

## Type Annotations

- Every method argument must have a type annotation.
- Every method must have a well-defined return type annotation.
- Every argument and return type must use a named mathematical type from `types.py`.
  `Any` is forbidden in method signatures (except `__contains__`).
