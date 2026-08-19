---
title: Subobjects Have Ambient Semantics
date: 2026-05-28
status: active
---

# Rule: For subobjects, self-predicates are interpreted relative to the ambient object

If `A` is a subobject of `B`, then `A` is not just an isolated object with the same
bare-space predicates as `B`. It carries ambient structure. In this repo, a subobject
predicate such as:

```python
A.is_open()
```

should be read as:

```python
A.ambient().is_open_subset(A)
```

or the corresponding ambient-relative operation.

Do not ask whether a bare topological space is open in itself as if that were the
interesting operation. That is trivial. The nontrivial operation is whether a
subspace/subobject is open, closed, dense, etc. in its ambient.

## Rule for method ownership across ambient/subobject boundaries

When a subobject category and an ambient category both define methods with the same
English name, check whether they mean different mathematical functions. If so, separate
the names or owners rather than forcing one signature to override the other.

## The RealSet incident

The agent considered whether `RealSet` should not inherit topological methods, which is
degradation. A subset of ℝ is a topological space and a subspace; the bug was the
unreconciled method names, not the mathematical inheritance. The correct structure is
ambient-centric versus self-centric subspace distinction:

- Ambient: `is_open_subset(self, U: Subset) -> bool` — ask whether a subset is open in
  this ambient space.
- Subobject: `is_open(self) -> bool` — ask whether this subspace is open in its ambient.

These must be different method names.

## Related

- `category-spec-interface-collisions-are-code-problems`: the full incident analysis and
  collision checklist.
- `mathematical-sanity-check`: the method ownership sanity gate that would have caught
  this.
- `analysis-must-be-grounded`: the rule that ledger rows are not evidence until code is
  read.
