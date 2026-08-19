---
title: Specs Do Not Contain Runtime NotImplemented Gaps
date: 2026-05-28
status: active
---

# Rule: In `category_specs`, abstract obligations stay abstract

A spec method that cannot be implemented at the current level must be `@abstractmethod`,
not a concrete method that raises `NotImplementedError`.

Do not introduce classes whose purpose is to satisfy abstract methods by raising runtime
errors. That hides the obligation from the type/spec layer and moves a mathematical/API
gap to runtime.

## Banned pattern

```python
def closure_subset(self, U: Subset) -> Subset:
    raise NotImplementedError(...)
```

## Correct pattern

```python
@abstractmethod
def closure_subset(self, U: Subset) -> Subset: ...
```

If a downstream category inherits the abstract method through its supercategory chain,
do not copy in a concrete runtime-gap helper. Let the abstract obligation remain visible.

## Incident

`TopologicalSpaceRuntimeGapObjectMethods` provided concrete methods raising
`NotImplementedError`, and `_TopologicalRings.ParentMethods` copied those methods
instead of inheriting the abstract topological-space obligations. The fix was to delete
the runtime-gap class and remove the copied block.

## Related

- `category-spec-methods-are-abstract`: the rule that category spec methods define
  obligations, not implementations.
- `category-spec-rotten-core-indicators`: red flag 6 (evidence suppression instead of
  evidence creation) — runtime gaps hide obligations.
- `category-spec-interface-collisions-are-code-problems`: the incident that produced the
  `TopologicalSpaceRuntimeGapObjectMethods` anti-pattern.
