---
title: Private method-container stubs are not valid types
---
# Private method-container stubs are not valid types

A recurring misclassification: treating private Sage method-container stubs as valid
return types, and then interpreting incompatible return annotations as a variance or
Liskov problem requiring analysis.
This is a category error: the private stubs are an implementation detail with no
mathematical meaning; they should never appear in any return type annotation.

## Origin of the bug

A prior agent did not understand the point of these private classes.
When writing method annotations, it used `_RingObjectMethods`, `_RModObjects`, etc.
as return types — names that make no mathematical sense.
No method returns a "RingObjectMethods"; a method returns a Ring.
These annotations were committed and propagated through the codebase, producing the 25
"return-type narrowing" errors in the override ledger.

## What is a private method-container stub?

Sage's category framework works via dynamic method mixing.
When `Rings` is defined, its `ParentMethods` class receives methods from:

- `Rings.ParentMethods` (defined inline in the category body)
- `_RingObjectMethods` (defined in a private class outside the body, purely to improve
  readability of the category definition file)

At runtime, `_RingObjectMethods` is mixed into `Rings.ParentMethods`, and
`Rings.ParentMethods` IS the public type.
The name `Ring` in the repo's type aliases refers to `Rings.ParentMethods`. Objects in
the Rings category get `Rings.ParentMethods` as their type via dynamic inheritance.

`_RingObjectMethods` has **no independent existence** as a type that any object actually
is. No object is an instance of `_RingObjectMethods`. No method returns a
`_RingObjectMethods`. It is a code organization device, not a type.

The same applies to every `_*Methods`, `_*Objects`, `_*Elements`, `_*Morphisms`,
`_*Homomorphisms` suffix in `category_specs/`:

- `_RModObjects` / `_RModElements` (Modules.ParentMethods / Elements)
- `_RingHomomorphisms` / `_RModMorphisms` (parent/element methods for Homsets)
- `_SetObjectMethods` / `_SetElementMethods`
- `_RingElementMethods`
- `_TopologicalSpaceObjectMethods`
- `_RingIdealParentMethods`
- `_BilinearForm`

## The hard rule

Any method whose declared return type is one of the above private names has a **bug in
the annotation**. The return type must be the **public type**: `Ring`, `Module`,
`Morphism`, `Set`, `RingElement`, etc.

The fix is mechanical: replace the private name with the public name.
No decision card needed.
No variance analysis.
No `# type: ignore`.

## What this is NOT

This is NOT:
- A variance problem (covariant returns needing explicit type variables)
- A Liskov substitution question
- Something needing a mathematical decision
- Something that should trigger a `TYPE_CHECKING` block or a `TypeVar`

It IS:
- A bug where a prior agent used the private implementation stub name instead of the
  public type in a return annotation

## How this pattern causes wrong analysis

The 25 "return-type narrowing" errors in the override ledger are ALL of this form.
Example:

```
Return type "_RingObjectMethods" of "base_ring" incompatible with
return type "Ring" in supertype "category_specs.sets.Sets"
```

Previous (wrong) interpretation: "Hmm, the subclass narrows the return from Ring to
_RingObjectMethods, which mypy rejects.
Is _RingObjectMethods a legitimate subtype of Ring?
Do I need covariance or a decision card?"

Correct interpretation: "The return type should be Ring, not _RingObjectMethods. Fix the
annotation."

## The topological method name collision (fixed)

The RealSet topological override errors (`is_open`, `is_closed`, `closure`, `interior`,
`boundary`) were a simple name collision: `_TopologicalSpaceObjectMethods` defined
`is_open(self, U: Subset)` (ambient-centric) and `_RealSets.ParentMethods` defined
`is_open(self)` (subspace self-centric).
Same method name, different arities.
Resolution: renamed ambient methods to `closure_subset`, `is_open_subset`, etc.
RealSet keeps the zero-argument subspace versions.
`TopologicalSpaceRuntimeGapObjectMethods` (concrete `NotImplementedError`-raising class)
was deleted.

Lesson: before classifying any override error, read both files — the one with the error
and the one with the supertype.
The arity conflict was visible in 30 seconds of reading two files.
An agent spent hours on ledger taxonomy instead.

## Related

- `category-spec-stub-classification-rule`: Three banned diagnostic-silencing patterns
  and the full override-error comedy narrative.
- `category-spec-mathematical-absurdities`: The multi-parent redundancy and
  consequence-as-parent patterns that produced Product A.
- `category-spec-root-bridge-vs-internal`: The boundary between category_specs internal
  types and Sage external surfaces.
- `private-method-containers-are-not-return-types`: the internal category_specs
  version of the same rule (not just Sage stubs).
- `category-spec-interface-collisions-are-code-problems`: the topological method
  name collision and the rule that internal collisions are code problems.
- `specs-do-not-contain-runtime-notimplemented-gaps`: the abstract-method rule
  violated by `TopologicalSpaceRuntimeGapObjectMethods`.
