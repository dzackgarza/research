# plugin-fixture-requirement

---
title: plugin-fixture-requirement
tags: [plugin, mypy, fixtures, tests, category-specs]
status: active
---

## When this applies

Every `@override` diagnostic in `category_specs` where:
- The intended parent method EXISTS in the local spec graph.
- The graph path from owner to overriding category is mathematically correct and minimal.
- mypy still says "no base method found."

These are NOT stub issues. They are plugin red tests.

## Required output

A **minimal fixture**: LITERAL code defining REAL categories and subcategories with REAL methods exhibiting the exact behavior.

### Fixture template

```python
class A(Category):
    class ParentMethods:
        def f(self) -> int: ...

class B(Category):
    def super_categories(self):
        return [A()]

    class ParentMethods:
        @override
        def f(self) -> int: ...
```

### Fixture must be completable

- Must FAIL under plain mypy.
- Must PASS under the intended plugin.
- Must have a **negative control**: when `A.ParentMethods.f` is removed/renamed, the `B.ParentMethods` override also fails.
- Must be derived from a REAL category in the spec, not synthetic.

## Known current fixtures needed

Based on the reclassification work, the rational-field block is a canonical case:

```text
_Fields.ParentMethods.algebraic_closure
    -> _QQ.ParentMethods.algebraic_closure

_NumberFields.ParentMethods.degree
    -> _QQ.ParentMethods.degree

_NumberFields.ParentMethods.maximal_order
    -> _QQ.ParentMethods.maximal_order
```

Each of these should produce a fixture. If the fixture passes under the current plugin, the diagnostic is stale. If it fails, the plugin needs work.

## Where fixtures go

Contribute to the `sagemath-mypy-plugin` repo test suite. The fixture demonstrates a downstream golden case that the plugin must support.

## Do NOT

- Remove `@override` markers to silence mypy locally.
- Add fake protocol or base class scaffolding.
- Create stub requests for these.
