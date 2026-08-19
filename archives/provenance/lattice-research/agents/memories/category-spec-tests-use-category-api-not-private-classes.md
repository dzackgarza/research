---
title: Category Spec Tests Use Category APIs, Not Private Classes
status: active
date: 2026-06-01
included_by: [index]
---
# Category Spec Tests Use Category APIs, Not Private Classes

## Object of the invariant

Category-obligation examples and regression tests for downstream category-spec
consumer behavior.

## False substitute it blocks

Testing private Python implementation classes, nested `ParentMethods` classes, or
handwritten dummy subclasses as if they represented mathematical category membership.

## Correct first question

What public mathematical category, axiom, constructor, or refinement path would a
downstream consumer actually use?

## Operative invariant

Category-spec tests must use the public mathematical API:

- category objects such as `Modules(R).WithBasis()`;
- category-owned constructors such as `Modules(R).Constructors().VectorSpace(...)`;
- category refinement declarations such as `refine_category(X, C)`;
- membership, methods, and constructions reached through those category surfaces.

Tests must not instantiate fake witnesses by literally inheriting from implementation
classes such as `_WithBasis.ParentMethods` or `_WithOrderedBasis.ParentMethods`.
Those class names are engineering internals, not research-facing vocabulary.
A downstream consumer should think "what is the smallest correct category for this
object?", not "which Python class should I subclass?"

Direct class-name assertions are allowed only for narrow internal route examples where
the object being tested is explicitly the route table itself, such as verifying that a
root category's axiom attribute points at the intended project class.
They are not valid evidence for object behavior, inherited category methods, or
downstream usability.

## Witness example

A category-obligation example for basis helper behavior should construct or refine an
actual module in `Modules(QQ).WithBasis()` or `Modules(QQ).WithOrderedBasis()`, then call
`basis_index_set()` or `basis_order()` on that object.
It should not define `class _OrderedBasisWitness(_WithOrderedBasis.ParentMethods)`.

## Non-example

```python
class _OrderedBasisWitness(_WithOrderedBasis.ParentMethods):
    def basis(self):
        return {"a": a, "b": b}
```

This bypasses the category graph, bypasses constructor/refinement, exposes private class
names, and proves nothing about the intended consumer experience.
