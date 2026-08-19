---
title: Mathematics First, Engineering Options Second
date: 2026-05-28
status: active
---

# Rule: The correct abstraction is determined by mathematics, not by local engineering options

When working in `category_specs`, do not begin by enumerating software options such as
overloads, ignores, adapters, wrappers, renames, or suppressions.

First identify the mathematical objects and operations:

- What is `self` mathematically?
- Is this method about the object itself, an ambient object, a subobject, an element, a
  morphism, or a constructor?
- What category should own this operation?
- What would the same operation be called in ordinary mathematical language?
- Is the current code conflating two different operations under one method name?

Only after this may engineering mechanisms be considered.

If a mathematical perspective makes all proposed engineering options look artificial,
discard the options and implement the simpler mathematical design.

## Example

The RealSet collision was between `is_open(self, U: Subset)` (ambient asks about a
subset) and `is_open(self)` (subobject asks about itself in its ambient). The complex
options (variance, Liskov, removing inheritance) only existed because the agent had not
named the actual distinction: ambient predicate on a subspace argument versus
self-predicate on a subobject.
