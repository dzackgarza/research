---
title: Category Spec Methods Are Abstract Specifications, Not Implementations
date: 2026-05-27
status: active
---
# Rule: Category Spec Methods Define Obligations, Not Implementations

## The principle

Methods in `ParentMethods`, `ElementMethods`, and `SubcategoryMethods` are **abstract
specifications** of what objects in a category must be able to do.
They are not implementations that call Sage runtime code.

The only non-abstract methods in the spec are those that:
1. Can be composed entirely from other abstract methods in the spec.
2. Have logic completely defined by the subcategory itself, without reference to any
   external implementation.

## What this means

### Methods do not call Sage

`_NumberFields.ParentMethods.degree` does not call
`sage.rings.number_field.NumberField.degree`. It declares that every object in the
`NumberFields` category must have a `degree` method, and specifies its return type.
The actual implementation lives in the Sage runtime or in a downstream adapter.

`_Modules.ParentMethods.rank` does not call `sage.modules.free_module.FreeModule.rank`.
It declares that every module in the `Modules` category must have a `rank` method.

### The spec is a mathematical interface

The category spec is a **typed mathematical interface**. It answers the question: "what
operations are meaningful on objects in this category, and what are their types?"

It does not answer: "how is this operation implemented in Sage?"

### Stubs are irrelevant for abstract methods

Since abstract spec methods do not call Sage runtime code, they do not need Sage stubs.
The types of abstract methods are defined entirely within the spec's own type system.

A mypy error on an abstract method definition is a spec issue (missing base, wrong
owner, incomplete graph) — never a stub issue.

### Abstract methods record spec obligations

`ParentMethods` abstract methods are the vocabulary of the category contract.
They say what an object in the category must provide; they do not make any claim that a
particular refined Sage object currently provides it.

This is why most spec methods remain abstract.
A non-abstract method belongs in the spec only when the category itself defines it from
other spec methods or from subcategory-internal mathematics.

Do not replace abstract spec methods with generated bodies, `assert False`, or
`NotImplementedError`. Those are runtime failure mechanisms, not specifications.

### Abstractness is not refinement validation

ABC abstractness belongs to the class model so inherited abstract obligations and
concrete methods interact through normal Python MRO.
It is not a reason for `refine_category` to inspect the object being refined or reject
the declaration.

Correct class-system behavior:

- concrete Sage methods can realize project obligations when ordinary lookup reaches
  them;
- concrete project methods can provide defaults when the spec owns the mathematics;
- missing methods remain abstract and visible;
- category-obligation examples reveal the remaining implementation gap.

## The concrete failure

In the vault conversation, an agent wrote:

> "Module-category methods such as `rank`, `dual`, `basis`, `tensor`, `span`,
> `submodule`, `quotient_module`, finite-rank structure, with-basis structure, or
> formed-module/lattice refinements are internal unless the diagnostic occurs at a
> direct Sage call."

This is wrong.
It treats spec methods as if they might be implementations that call Sage.
They are not. They are abstract interface definitions.

The user corrected this:

> "The spec work does not actually CALL methods on an implementation.
> It is a SPEC. The only non-abstract methods are those which can themselves be composed
> from known existing abstract methods, or have logic completely defined by the
> subcategory itself and not the implementation."

## The test

For any method in `category_specs`:

1. Is it in `ParentMethods`, `ElementMethods`, or `SubcategoryMethods`?
   - If yes: it is an abstract specification.
     It does not need stubs.
2. Is it in a constructor, adapter, or explicit Sage interop helper?
   - If yes: it may need stubs for direct Sage calls.
3. Is it composed entirely from other spec methods?
   - If yes: it is an internal spec method.
     It does not need stubs.

## The rule

**Never ask "does this method call Sage?"
for a `ParentMethods` method.** The answer is always no.
It is an abstract specification.
The question to ask is: "what is the largest category on which this method makes sense,
and does that category define it?"

## Related

- `specs-do-not-contain-runtime-notimplemented-gaps`: the concrete rule that follows
  from this principle — abstract obligations must stay abstract.
- `category-spec-architectural-boundary`: the three-layer architecture that separates
  abstract specs from Sage implementations.
