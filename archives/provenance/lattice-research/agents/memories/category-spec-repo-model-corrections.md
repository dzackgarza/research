---
title: Category Spec Repo Model Corrections
status: active
---

# Category Spec Repo Model Corrections

## Object preserved

This memory preserves corrected repo-level semantics for `category_specs`.
It is not a task-state note.
Use it when refinement, `ParentMethods`, ABCMeta, constructor-obligation examples, Sage
interop, or object-method resolution are discussed.

## Core model

`category_specs` is mathematical specification work.
It defines category vocabulary, method ownership, object-method obligations, and
mathematical interfaces inside Sage's category/object universe.
It is not an enforcement framework.

The project owns the relevant boundary.
For project categories, the repo owns the category subtree, base wrappers,
`ParentMethods` classes, constructor/refinement wrapper path, and any local dynamic
class/metaclass bridge needed for that subtree.
Do not analyze the boundary as raw Sage refinement unless the work is explicitly about
raw Sage itself.

Refinement is declaration.
`refine_category(X, C)` says that an existing implementation `X` is to be regarded as
an object of category `C`.
That declaration imposes the category contract, but it does not validate that `X`
satisfies the contract.
It does not instantiate an implementation, interrogate method satisfaction, or perform
admission control.

Category-obligation examples surface the gap.
They instantiate or exercise project category objects to show which project obligations
current Sage/project implementations realize and which remain missing.

ABCMeta participates at the class-system boundary.
Its role is to make project abstract methods live in Python's normal abstractmethod
machinery so instantiation and ordinary MRO reveal which obligations remain abstract.
ABCMeta is not a reason to add project-specific satisfaction logic to refinement.

Most `ParentMethods` in specs are abstract obligations.
A non-abstract `ParentMethods` method is a real default implementation only when the
spec itself mathematically defines that method from other spec code.
When a concrete Sage or project method exists, it satisfies a matching obligation only
through ordinary lookup and ABC/MRO behavior.

## Minimality and reuse philosophy

The category-spec code exists to enable mathematical research, not to become an
exercise in Sage/Python internals.
Ordinary spec files should remain understandable as mathematical category definitions
by a reader who is not an expert in Sage dynamic classes.

The repo owns this category subtree and the project constructor/refinement path.
That ownership is a reason to choose the natural low-level bridge, not a reason to
invent local enforcement machinery.
When an external system already solves the relevant problem, let that system own it:
Sage owns dynamic category/parent-class construction, and Python owns abstract-method
semantics through `ABCMeta`.
Project code should add the smallest glue needed to compose those mechanisms inside the
owned subtree.

Complexity is acceptable only where the boundary forces it.
If Sage/Python interop requires metaclass work, quarantine that work in the interop
layer and keep category specs, refinement semantics, and category-obligation examples
mathematically legible.
Do not spread method-resolution, cache-state, abstract-name, or class-mutation logic
through ordinary spec code.

Before accepting an implementation, ask:

- Does this reuse the mature Sage/Python mechanism that already owns the problem?
- Is the project-owned code only the minimal bridge needed to connect those mechanisms?
- Is unavoidable complexity quarantined at the interop/class-construction boundary?
- Would a mathematician reading ordinary spec files see category obligations rather than
  engineering machinery?
- Did the patch reduce local concepts agents must understand, or add a parallel local
  system?

If the answer depends on a repo-local algorithm for abstract-method satisfaction,
method-name subtraction, refinement admission, generated failure bodies, or cache/MRO
manipulation outside the bridge, the solution is misaligned even if tests pass.

## False models and corrected models

| False model | Correct model |
| --- | --- |
| `category_specs` enforces implementation completeness. | `category_specs` states mathematical category contracts. |
| Refinement checks whether an object satisfies a category. | Refinement declares that an implementation is viewed as an object of a category. |
| Category membership certifies current implementation completeness. | Category membership imposes a contract; implementation completeness is separate. |
| Refined Sage objects should already satisfy the full project spec. | Refined Sage objects are expected to be partial because the project specs are new. |
| Missing project methods after refinement are refinement failures. | Missing methods are implementation gaps exposed by specs and category-obligation examples. |
| Category-obligation examples prove a refinement enforcement boundary. | Category-obligation examples expose which obligations current implementations miss. |
| `ParentMethods` are provider implementations. | `ParentMethods` are mathematical object-method obligations. |
| Abstract methods should become generated failure bodies. | Abstract methods should remain abstract unless the spec itself owns a concrete method. |
| ABCMeta should reject bad refinements. | ABCMeta should represent project abstractness in the Python class system. |
| Refinement should instantiate the implementation to trigger ABCMeta. | Instantiation-time ABC behavior belongs to construction, category-obligation examples, or runtime exercise, not refinement. |
| The project needs custom logic to decide which abstract methods Sage satisfies. | Python MRO and ABC machinery determine concrete methods and remaining abstractness. |
| Sage's `DynamicMetaclass` ownership blocks the simple strategy. | The project owns its subtree and can use local dynamic metaclasses composed with `ABCMeta`. |
| Local dynamic-metaclass work requires modifying Sage globally. | The branch can be local to project-owned category construction. |
| Raw Sage refinement is the project boundary. | The project boundary is the repo-owned constructor/refinement/category pathway. |
| A raw-Sage refinement experiment proves the project strategy viable or blocked. | Viability evidence must exercise the project-owned subtree and refinement/constructor pathway. |
| Source work should copy abstract requirements into final namespaces. | Let Sage's parent-class construction and Python ABC/MRO carry requirements through bases. |
| The repair requires MRO surgery or hand-written abstract-name subtraction. | The desired repair is local metaclass/class construction that delegates ordinary behavior to Sage and ABCMeta. |
| An abstract implementation parent is a category-refinement failure. | Abstractness is class-system state surfaced by construction/runtime exercise, not a refinement blocker. |
| The project should reimplement Sage/Python internals so tests can target them. | The project should minimally compose existing Sage/Python mechanisms at the owned interop boundary. |
| Complex class logic is acceptable wherever it makes the category-obligation example pass. | Complex interop logic must be quarantined; ordinary specs should remain mathematical. |
| Current Sage coverage bounds the spec. | Sage is implementation evidence and a feasibility witness, not the adequacy standard. |
| Green QC or passing tests prove alignment. | Alignment means preserving the mathematical architecture; green checks can certify slop. |
| Generated-body/assert patches are partial progress. | Generated bodies encode the wrong model and must not guide design. |
| Implementation gaps should be hidden or preempted. | Implementation gaps should remain visible until implementation work supplies them. |
| Refinement, specification, implementation, and category-obligation examples form one runtime validator. | Specs state obligations; refinement declares category view; implementations satisfy obligations; category-obligation examples expose gaps. |

## Consequences for source work

- Do not make `refine_category` inspect abstract-method satisfaction.
- Do not reject refinement because project methods remain abstract.
- Do not call a refined Sage object "invalid" merely because it lacks project methods.
- Do not invent "admission control" for category refinement.
- Do not instantiate inside refinement to force ABC checks.
- Do not use generated failure bodies, `assert False`, or `NotImplementedError` as spec
  substitutes.
- Do not add cache priming, lookup-state hacks, source-shape tests, casts, type ignores,
  or method-name special cases to hide the gap.
- Do not copy abstract requirements directly into the final refined-class namespace to
  simulate satisfaction or failure.
- Do not manually subtract, filter, or special-case abstract method names based on Sage
  lookup results.
- Do not use raw Sage refinement experiments as evidence about the project-owned
  category/refinement/constructor boundary.
- Do not add MRO surgery when ordinary Sage parent-class construction plus ABCMeta
  metaclass composition can express the class relation.
- Do not test raw Sage refinement when the question is the project-owned
  category/refinement/constructor pathway.
- Do not add import-time eager refinement to hide, pre-trigger, or relabel missing
  obligations.
- Do not weaken or delete a spec method because current Sage lacks it.
- Do not treat a Sage method with the same name as a reason to remove the abstract spec
  obligation.
- Do not solve a problem locally when Sage or Python already has the natural mechanism
  for it.
- Do not spread unavoidable Sage/Python interop complexity outside the owned bridge.
- Do use project-owned ABC-compatible dynamic metaclasses when the task is to make
  project abstract methods participate correctly in class construction.
- Do compose or replace the project-owned dynamic metaclass path locally for this
  subtree when source evidence shows Sage's dynamic class mechanism can be delegated to
  while adding `ABCMeta`.
- Do let ordinary MRO decide whether concrete Sage/project methods realize obligations.
- Do let category-obligation examples report missing implementations.

## Allowed low-level strategy shape

The preferred strategy, when source research confirms the mechanics, is local and
structural:

- branch from Sage's dynamic category construction only inside the project-owned
  category subtree;
- construct project `parent_class` objects with a metaclass compatible with both Sage's
  dynamic class expectations and `ABCMeta`;
- delegate non-ABC dynamic behavior back to Sage;
- rely on `ABCMeta` abstract-set computation, `abc.update_abstractmethods` when
  source-justified, and normal MRO to determine concrete realization;
- keep refinement as declaration and let category-obligation examples, construction, and
  runtime exercise reveal
  remaining abstract obligations.

This is not a request for wrappers around final classes, copied method bodies, cache
priming, or post-hoc mutation that hides missing obligations.
The point of the low-level bridge is to delete local cleverness everywhere else.

## Consequences for review

Review category-spec work by asking:

- What category contract is being declared?
- Which object-method obligations does the category impose?
- Which obligations does current Sage already realize?
- Which obligations remain missing and visible?
- Did the patch preserve the spec/category-obligation-example gap, or did it hide the gap with runtime
  machinery?
- Did the patch reuse the simplest existing mechanism at the owned boundary, or did it
  add a local substitute for Sage/Python behavior?

Do not review this work by asking whether refinement rejects incomplete objects.
That question belongs to the wrong repo model.
