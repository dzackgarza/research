# Category Spec Refinement Is Category Declaration

## Trigger

Read this before editing `refine_category`, constructor refinement, category-spec
category-obligation examples, or any code that tries to view a Sage object as an object
of a project subcategory.

## Object Of The Invariant

Refinement is a category-membership declaration. It says that an existing Sage object
is now being viewed inside this repo's category universe as an object of a more
specific project category.

False substitute blocked: treating refinement as a programming repair whose purpose is
to make method search succeed, validate implementation completeness, or enforce object
satisfaction.

## Non-Validation Rule

`refine_category(X, C)` does not decide whether `X` satisfies the full specification of
`C`. It declares that `X` is to be regarded as an object of `C`, thereby imposing the
category contract that all objects of `C` must satisfy.

## Single-Category Target Rule

`refine_category(X, C)` must declare the single smallest mathematically correct
category for `X`.
Do not pass several categories, such as `refine_category(X, [Rings(), _Qp()])`.
That manually restates inherited structure and violates the purpose of a category
hierarchy: the target category owns the implementation contract, while its
`super_categories()` graph owns ancestor membership.

If a refinement call appears to need several categories, the category graph is wrong or
the target category is not specific enough.
Fix the graph or name the missing mathematical category; do not stack categories at the
call site.

This declaration is not proof that the current implementation satisfies the contract.
During the spec phase, most refined Sage objects are expected to satisfy only part of
the project contract, because the project invented specifications Sage did not know.
That visible gap is the purpose of refinement together with category-obligation
examples.

Forbidden replacement model:

- do not reject refinement because project abstract methods remain;
- do not interrogate the refined object for method satisfaction;
- do not treat refinement as admission control;
- do not turn `refine_category` into an implementation-completeness validator;
- do not hide missing spec methods with generated bodies, assertions, or
  `NotImplementedError`.

The only semantic act of refinement is category declaration. Completeness is surfaced by
category-obligation examples and later implementation work.

## Spec-Facing Class Boundary

Object preserved: project-owned implementation classes must not bypass Python ABC
instantiation enforcement merely because refinement was applied to an already-created
object.

For project-owned spec implementations, the spec-facing refinement API must accept a
class/type and return the refined class/type. Consumers that want an object must
instantiate that returned class. If project `ParentMethods` obligations remain abstract,
real `ABCMeta` then raises the standard instantiation `TypeError` before any defective
object is created.

This does not make refinement an implementation-completeness validator. Class refinement
may successfully return an abstract refined class. The enforcement event is ordinary
Python instantiation of that class, not a manual refinement-time check over method names.

Instance-level refinement of an already-created Sage parent is a compatibility path for
existing Sage objects and singletons. It must not be treated as the canonical
spec-facing API for project-owned implementation classes, because returning the same
already-created object lets a consumer skip the required refined-class instantiation
step and thereby bypass ABC enforcement.

Canonical project constructor surfaces may still return instances to users. When they
construct project-owned implementations, however, they must construct through the
refined class/type rather than creating a raw object first and refining it afterward.
The raw implementation class should not be the exposed user-facing construction route
for a spec-defective object.

## False Models Corrected

Use these corrections when reviewing refinement, ABCMeta work, constructor-obligation
examples, or agent-produced patches in this subtree.

| False repo model | Correct repo model |
| --- | --- |
| `category_specs` is a runtime enforcement layer. | `category_specs` is a mathematical specification layer inside Sage's category/object universe. |
| Refinement validates that an object satisfies a category. | Refinement declares that an implementation is to be regarded as an object of a category. |
| Category membership means the current implementation is complete. | Category membership imposes the category contract; implementation completeness is a separate question. |
| A refined Sage object should already satisfy the full project category. | Refined Sage objects are expected to be partial because the project specs are new and Sage did not know them. |
| Missing project methods after refinement are refinement failures. | Missing project methods after refinement are visible implementation gaps. |
| Category-obligation examples prove refinement enforcement. | Category-obligation examples instantiate or exercise category objects to reveal gaps between current implementations and the spec. |
| `ParentMethods` are provider implementations. | `ParentMethods` are mathematical object-method obligations. |
| Abstract `ParentMethods` should become runtime failure bodies. | Abstract `ParentMethods` remain abstract specifications unless the spec itself owns a concrete method. |
| ABCMeta should reject bad refinements. | ABCMeta should represent abstract method structure correctly in the class system. |
| The project must compute which abstract methods Sage satisfies. | Python MRO and ABC machinery determine concrete methods and remaining abstractness. |
| Sage's ownership of `DynamicMetaclass` blocks the local strategy. | The project owns this category subtree and can use local dynamic-metaclass variants composed with `ABCMeta`. |
| Changing dynamic metaclasses means globally modifying Sage. | The branch can be local to project-owned category construction. |
| Raw Sage refinement is the relevant boundary. | The relevant boundary is the repo-owned category/refinement/constructor pathway. |
| Current Sage coverage bounds the project spec. | Sage is implementation evidence and a feasibility witness, not the adequacy standard. |
| Passing QC means the category model is aligned. | Alignment means the mathematical architecture is preserved; green checks can still certify slop. |
| Generated-body/assert patches are partial spec progress. | Generated bodies embody the wrong model and must not guide the design. |
| Implementation gaps should be hidden or preempted. | Implementation gaps should remain visible as obligations surfaced by specs and category-obligation examples. |
| Refinement, specification, implementation, and category-obligation examples are one runtime validator. | Specs state obligations; refinement declares category view; implementations satisfy obligations; category-obligation examples expose the gap. |

## Correct First Question

Before touching refinement code, answer this in ordinary mathematical language:

> Which existing Sage object is being declared to belong to which project category, and
> which parts of the mathematical specification of that category does the Sage object
> already realize?

If the first answer is about method search, cache state, dynamic class mutation,
type-checker appeasement, category-obligation example ordering, hook output, or any other programming
mechanism before it names the category and its mathematical specification, the frame is
already wrong. Concrete examples include `MRO`, `getattr_from_category`,
`_cached_methods`, `cached_method`, Cython, and `can_assign_class`. These are evidence
terms after the category declaration is understood; they are not refinement semantics.

## Purpose Of Refinement

The project spec states the mathematical structure and operations expected of objects
in a category. Existing Sage objects are partial implementations and feasibility
witnesses. Refinement imports the existing Sage object as-is and declares the project
category contract over it. Category-obligation examples expose which parts of the
specification are already realized and which parts remain missing.

Within this repo's constructors, all instantiation goes through the project category
layer. It is acceptable, and often expected in the spec phase, that many refined Sage
objects cannot pass full compliance because the ideal spec asks for methods Sage does
not yet implement. That failure is evidence for later implementation, wrapper,
constructor, or spec-gap work. Refinement must not hide it, and refinement must not
reject it merely because the gap is visible.

Project specs may and often should declare operations that Sage already implements. The
spec records the mathematical structure in this repo's category universe; the existing
Sage method may realize that part of the specification for a refined object. Do not
delete, weaken, or move a spec method merely because Sage already has a method with the
same name. Conversely, do not add programming machinery merely to force a refined
object to look complete.

## Specification And Implementation

There are two trees of work:

- the spec tree states category definitions, method ownership, and mathematical
  structure;
- the implementation tree closes the gap between existing Sage behavior and the
  mathematical specification.

Refinement sits between them. It imports an existing Sage implementation as partial
evidence for the spec and declares the category contract. Category-obligation examples
reveal the remaining implementation gap. A passing implementation later may use
wrappers, constructors, or backend work. Refinement itself should not perform that
implementation work.

If Sage already implements a method specified by the project category, the refined
object may use that implementation. If the project category has a mathematically forced
concrete method, such as `is_finite()` on finite objects, that method is part of the
project category surface. If no implementation exists, the missing method should remain
visible.

## ABCMeta Role

`abc.abstractmethod` belongs to the spec surface because it records abstract object
requirements in Python's class system. ABC machinery must preserve the abstract
structure of project `ParentMethods` under ordinary class construction and MRO.

ABC machinery is not a refinement validator. Refinement should build or expose the
correct category method surface; it should not ask whether the current object satisfies
every abstract method. Instantiation and category-obligation examples are the places
where implementation gaps become observable.

Allowed low-level work:

- project-owned dynamic parent classes may use metaclasses that minimally compose
  Sage's dynamic metaclasses with `ABCMeta`;
- project-owned base category wrappers may route this subtree's `parent_class`
  construction through those metaclasses;
- concrete Sage or project methods may satisfy abstract obligations by normal Python
  MRO.

Forbidden low-level work:

- manual abstract-name satisfaction logic;
- method-name special cases;
- post-hoc mutation to hide abstract obligations;
- generated call-time failure bodies;
- treating `inspect.isabstract(...)`, `__abstractmethods__`, or any equivalent query as
  a reason for `refine_category` to reject the declaration.

## Caching Is Not Refinement

Caching is a runtime/performance concern of implementation code after objects exist. It
is not part of declaring a category, stating a spec method, or deciding whether a Sage
object belongs to a project subcategory.

Do not preserve cache awareness by giving it a more respectable engineering name. A
source-backed task about Sage internals belongs in a separate implementation note; it
does not become part of the mathematical specification or refinement semantics.

## Frame Rejection

Stop immediately if refinement triage starts from method search, cache state, dynamic
class mutation, type-checker appeasement, category-obligation example ordering, hook
output, abstract-method enforcement, or any other programming mechanism instead of the
category declaration.
The specific historical terms `MRO`, `getattr_from_category`, `_cached_methods`,
`cached_method`, Cython, and `can_assign_class` matter because they are precise evidence
of the wrong layer; they are not the new vocabulary of refinement.

Before attempting a technical fix, state the refined object, its previous Sage category,
the project subcategory being declared, the spec methods Sage already implements, and
the spec methods still missing. If that cannot be stated, do not edit refinement code.

An invalid fix makes the repo appear more correct by hiding a missing method, weakening
a spec method, deleting an override marker, adding a cast, or improving QC output
without changing the category declaration or the visible spec gap.

## Witness Discipline

A concrete failure such as `ZZ.ideal_monoid()` is a witness, not the task. Do not
overfit refinement guidance to that method, ring, or object. Use it only to ask the
general question: after declaring an existing Sage object to belong to a project
subcategory, does the category-obligation example expose the actual implemented/missing
parts of the mathematical specification, or did the repo hide the gap with programming
machinery?

## Verification

A future reviewer should be able to inspect a refined object and answer:

- Which existing Sage object is being declared into which project subcategory?
- Which spec methods belong to that project category?
- Which spec methods are already realized by the existing Sage implementation?
- Which spec methods remain missing and visible?
- Why refinement did not validate or enforce satisfaction?
- Why no method-search, cache, or generated-failure mechanism is needed to make that
  classification true?
