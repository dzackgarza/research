---
title: Category Spec Architectural Boundary — Internal Inheritance is Not Stub Work
date: 2026-05-27
status: active
---
# Rule: Internal Method-Container Inheritance is Never `sage-stubs` Work

## The boundary

`category_specs` has a three-layer architecture:

1. **Internal spec layer**: `ParentMethods`, `ElementMethods`, `SubcategoryMethods`
   define mathematical obligations within the local category graph.
   Their inheritance is internal.
   The mypy plugin (`SPEC-SAGE-MYPY-CATEGORY-OVERRIDE`) is designed to make `@override`
   on these containers pass by projecting semantic ancestry.

2. **Plugin layer**: Handles dynamic method-container inheritance that mypy cannot see
   statically. If an `@override` on `C.ParentMethods` fails, the first check is whether
   the base exists in an internal ancestor method container.
   If yes, this is plugin work, not stub work.

3. **Stub layer**: `sage-stubs` provides type information **only** for direct Sage
   runtime API calls at the constructor boundary.
   The boundary is `Cat().Constructors()`, `constructor_adapters.py`, and explicit Sage
   imports used in constructor implementations.

## What this means in practice

- A mypy error of the form
  `Method "X" is marked as an override, but no base method was found` on a
  `category_specs` `ParentMethods` class is **never** automatically `sage-stubs` work.
- The base method may exist in another internal `category_specs` file (plugin work), may
  be missing from the internal graph (spec work), or the graph may be wrong (graph
  work).
- It is stub work **only** if the failing expression is a direct call to an external
  Sage API whose type information is missing.
- Same-named methods on concrete Sage classes are irrelevant.
  `_QQ.ParentMethods.degree` overrides `_NumberFields.ParentMethods.degree`, not
  `sage.rings.rational_field.RationalField.degree`.

## The only legitimate stub oracle

Before adding any row to `sage-stubs`, identify:
- The exact `category_specs` file and line where a Sage symbol is imported or called.
- The constructor or boundary method containing that call.
- The admitted input shape and local refined output type.

If these cannot be named, it is not a stub row.

## Related

- `private-method-containers-are-not-return-types`: private method containers like
  `_RingObjectMethods` are implementation artifacts, not public types in any layer.
- `category-spec-root-bridge-vs-internal`: the binary boundary between root bridges and
  internal inheritance.
