---
title: Private Method Containers Are Not Mathematical Return Types
date: 2026-05-28
status: active
---

# Rule: `_SomethingMethods` / `_SomethingObjects` classes are implementation containers, not public semantic types

In `category_specs`, private classes such as `_RingObjectMethods`, `_RModObjects`,
`_RingHomomorphisms`, `_SetObjectMethods`, and `_TopologicalSpaceObjectMethods` are
private method-definition containers. They exist so long method bodies can be defined
outside category class bodies and mixed into public `ParentMethods` /
`ElementMethods` surfaces.

They are not mathematical return types.

If a method annotation returns a private method-container class, the annotation is
wrong. Replace it with the public semantic type (`Ring`, `Module`, `Morphism`, `Set`,
etc.) or the appropriate public `ParentMethods` alias. Do not analyze this as
return-type narrowing, variance, Liskov, or a need for `TYPE_CHECKING`.

Diagnostic:

```text
returns _RingObjectMethods  -> bug in annotation
returns Ring                -> public semantic type
```

## Social provenance

The original bugs were caused by agents not understanding the role of private
method-container classes, allowing methods to return non-mathematical implementation
artifacts. A future agent must not treat the bad annotations as evidence of intent.

## Related

- `private-stubs-are-not-types`: covers the same pattern at the Sage-stub boundary.
  This memory covers the internal `category_specs` pattern more generally.
- `category-spec-architectural-boundary`: the three-layer architecture showing why
  private method containers are not public types.
- `category-spec-root-bridge-vs-internal`: the binary boundary between root bridges and
  internal inheritance.
