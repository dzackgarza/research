---
title: Category Spec Interface Collisions Are Code Problems
date: 2026-05-28
status: active
---

# Rule: Same-name incompatible signatures inside `category_specs` mean two internal interfaces collided

When mypy reports that a method in one `category_specs` method container is incompatible
with a supertype method, do not treat this as an external Sage constraint by default.
`category_specs` owns both sides unless one side is a direct Sage boundary.

First read both definitions. Then ask:

1. Are these the same mathematical operation?
2. Are these two different operations accidentally sharing a name?
3. Does one operation belong on an ambient object and the other on a subobject?
4. Is the current inheritance graph mathematically correct?
5. Is the fix a rename, relocation to the correct category, overload, or deletion of
   spec-rot?

The RealSet/topological-space incident was an internal interface collision:

- ambient/topological-space method: `is_open(self, U: Subset) -> bool`;
- subspace/self method: `is_open(self) -> bool`.

These are not a "variance" problem, not a Sage-stubs problem, and not a reason to remove
topology from real subsets. They are two unreconciled internal interfaces. Resolve the
code.

## Fix pattern

Raw ambient-space predicates should not have the same name as subobject self-predicates
when their semantics differ. Rename the ambient operation, e.g. `is_open_subset` /
`closure_subset`, and let subobjects keep `is_open(self)` / `closure(self)` where
mathematically appropriate. The resolution for this incident was: rename ambient methods,
keep the subspace method, delete `TopologicalSpaceRuntimeGapObjectMethods`, and add a
hook against `NotImplementedError`.

## Collision checklist

Before classifying an incompatible override error, display the two concrete signatures:

```python
# supertype
def method_name(self, <params>) -> <return>:

# subtype
def method_name(self, <params>) -> <return>:
```

If you cannot quote both conflicting definitions from code, you are not allowed to
classify the error.

## Related

- `subobjects-have-ambient-semantics`: the mathematical principle behind
  ambient-vs-subobject method ownership.
- `private-stubs-are-not-types`: covers the adjacent private-container return-type
  misclassification and the topological collision.
- `category-spec-stub-classification-rule`: the override-error comedy and banned
  diagnostic-silencing patterns.
- `category-spec-rotten-core-indicators`: the red flags this incident triggered
  (jargon, count-driven urgency, purpose blindness).

## Banned classifications for internal collisions

- "variance problem"
- "Liskov audit"
- "interface design question"
- "Sage-stubs gap"
- "needs TYPE_CHECKING"
- "topology should not apply to subspaces"

## Incident: RealSet / TopologicalSpaces method collision

The conflict was local and simple:

- `_TopologicalSpaceObjectMethods.is_open(self, U: Subset) -> bool`
- `_RealSets.ParentMethods.is_open(self) -> bool`

The same collision existed for `is_closed`, `closure`, `interior`, and `boundary`.

The wrong responses were:
- classify from the ledger without reading code;
- call it variance/Liskov;
- write a goalcraft goal;
- edit memories instead of fixing code;
- suggest weakening/removing topological inheritance;
- treat concrete `NotImplementedError` methods in a spec as acceptable.

The correct response was:
- read both definitions;
- recognize ambient-space operation vs subobject self-operation;
- rename the ambient operation (`*_subset`);
- leave subspace/self operations on subobjects;
- delete concrete runtime-gap spec code;
- run mypy.
