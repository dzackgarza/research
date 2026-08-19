---
title: Category Spec Root Bridge vs Internal Inheritance — A Binary Boundary
date: 2026-05-27
status: active
---
# Root Bridge vs Internal Inheritance

## The boundary is binary, not a spectrum

There are only two kinds of category edges:

### 1. Root bridge (legitimate, necessary)

**Where:** Entry points like `Rings`, `Sets`, `Modules`.

**What they do:** Attach to Sage root categories (`SageRings`, `SageSets`,
`SageModules`) to avoid reimplementing trivial upstream categories (monoids, semigroups,
additive groups, magmas, etc.).

**Why they exist:** Sage already has these categories.
Reimplementing them in the spec would be pure overhead with no mathematical value.

**Rule:** Only root entry points may have Sage bridge edges.

### 2. Internal inheritance (the norm)

**Where:** Everything below the root.

**What they do:** Inherit through local spec parents only (`_Fields`, `_NumberFields`,
`_QQ`, etc.).

**Why:** After the constructor boundary, the object is refined into the local spec
surface. It lives in the internal hierarchy.
Its method obligations, override chains, and category refinements are entirely internal.

**Rule:** Internal subcategories almost never need to declare a Sage supercategory
outside the spec.

## Why internal Sage edges are wrong

The ENTIRE point of the architecture is:

1. `Cat().Constructors()` calls a Sage constructor.
2. The constructor gets a raw Sage object.
3. `refine_category(...)` casts the raw object into the local spec category.
4. After step 3, the object is **internal**. It has no further dependency on Sage
   categories, Sage method containers, or Sage stubs.

An internal subcategory that declares a Sage supercategory is breaking this boundary.
It is saying: "I need Sage's category machinery for my inheritance."
But the subcategory never directly uses Sage machinery.
It only sees the refined output of constructors.

## Examples

**Legitimate root bridge:**
```python
Rings.super_categories() -> [Sets(), SageRings()]
```
`Rings` is an entry point.
It bridges to Sage to avoid reimplementing monoids, semigroups, etc.

**Wrong internal Sage edge:**
```python
_Fields.super_categories() -> [SageFields(), _CommutativeRings(), ...]
```
`_Fields` is not a root entry point.
It is an internal subcategory under `Rings`. It should inherit through local parents,
not re-attach to Sage.
The fact that Sage has a `Fields` category is irrelevant to the internal spec hierarchy.

**Corrected:**
```python
_Fields.super_categories() -> [Rings(), ...]  # or appropriate local parents
```

## The test

For any category with a `SageXxx()` parent, ask:

1. Is this category a root entry point (e.g., `Rings`, `Sets`, `Modules`)?
   - If yes: the Sage edge is legitimate.
   - If no: the Sage edge is suspicious and probably wrong.

2. If the Sage edge is removed, can the category still reach all necessary methods
   through local parents?
   - If yes: remove the Sage edge.
   - If no: the local graph is incomplete.
     Fix the graph, do not add a Sage workaround.

## The anti-pattern

Agents have treated category graph construction as a spectrum where "some Sage edges are
okay" and "maybe mixed edges are needed."
This is false. The boundary is binary:

- Root entry points bridge to Sage.
- Everything else inherits locally.

Any agent who suggests adding Sage edges to internal subcategories has lost the plot.
