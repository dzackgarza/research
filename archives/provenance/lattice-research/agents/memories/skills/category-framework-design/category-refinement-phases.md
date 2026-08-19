# Category Refinement Phases

## Goal

Build the Sage category refinement surface as a static mathematical spec before
installing behavior.  The category hierarchy is the source of truth.  Runtime
inspection may be used once to learn Sage's existing method names on examples,
but the resulting method lists are recorded explicitly in the spec.

## Constraints

- `Rings` is only a staging namespace so the spec does not clobber
  Sage's `Rings` category during development.
- Subcategories are mathematical categories, not software categories.
- Predicates are mathematical names such as `is_field`, `is_number_field`,
  `is_complete_ring`, and `is_pid`.
- No runtime method discovery, generic routing tables, or exception-driven type
  checks belong in the spec.
- Constructor interception is deferred until the category hierarchy and method
  surfaces are explicit.

## Phase 1: Static Hierarchy And Method Surface

Define the full ring and module subcategory hierarchy first.  For each
subcategory, statically enumerate the relevant existing Sage method names on
`ParentMethods`, `ElementMethods`, or Hom-category `ElementMethods`.

Runtime examples may be inspected only as source material.  Once selected, each
method is written into the appropriate subcategory by name.  Methods remain
abstract unless the category itself owns a trivial predicate.

Acceptance:
- `category_specs/rings.py` imports.
- `category_specs/sage_modules.py` imports.
- The category spec files themselves are the reviewed artifact.
- There are no runtime method-list discovery checks or generic routing helpers.

## Phase 2: Concrete Category Interceptors

Replace selected abstract methods with concrete methods only when the
subcategory can reuse an existing same-named Sage implementation through the
MRO.

The implementation pattern is:

```python
result = super().method_name(*args, **kwds)
result._refine_category_(target_category)
return result
```

Methods that do not return rings, ideals, or module parents may remain abstract
as documentation.

Acceptance:
- Concrete methods appear only on the mathematically correct subcategory.
- Each concrete method calls the inherited implementation by the same name.
- Result refinement is local to the method that produced the result.

## Phase 3: Top-Level Constructor Redefinitions

Redefine top-level constructors only after Phase 1 and Phase 2 are stable.
Each redefinition has the same shape:

```python
obj = SageConstructor(*args, **kwds)
obj = TargetCategory(...)(obj)
return obj
```

Constructor redefinitions do not contain hierarchy policy.  The category call
performs refinement into the correct mathematical subcategory.

Acceptance:
- `FreeModule(R, n)` refines through `Modules(R)`.
- Ring constructors refine through `Rings`.
- Constructor code contains no generic routing beyond calling the target
  category.
