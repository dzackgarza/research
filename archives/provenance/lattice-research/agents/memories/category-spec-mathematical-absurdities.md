---
title: Category Spec Mathematical Absurdities — Current Code Defects
date: 2026-05-27
status: active
---
# Mathematical Absurdities in the Current Category Graph

These are not subtle design questions.
They are obvious mathematical errors that any mathematician would immediately recognize.
Their presence indicates that the graph was constructed without mathematical review.

## Absurdity 1: QQ lists Fields and NumberFields as siblings

**Current code:**
```python
# category_specs/rings/subcategories/rational_field.py
_QQ.super_categories() returns [
    _Fields(),
    _QuotientFields(),
    _NumberFields(),
    _GlobalFields(),
    Rings().Characteristic(0),
]
```

**Why this is absurd:** `NumberFields` IS a subcategory of `Fields`. Every number field
is a field. `QQ` IS a number field (the simplest one).
The graph should be:

```text
NumberFields <= GlobalFields <= Fields
QQ <= NumberFields
```

Not:
```text
QQ <= Fields, NumberFields, GlobalFields, QuotientFields (all as siblings)
```

This is like saying "a dog is a mammal, a dog is an animal, a dog is a vertebrate, and a
dog is a dog" instead of "a dog is a mammal, which is an animal, which is a vertebrate."

## Absurdity 2: QuotientFields means fraction fields, not quotients

**Current code:** `category_specs/rings/subcategories/quotient_field.py` defines
`_QuotientFields` with supercategories `[SageQuotientFields(), _Fields()]`.

**Why this is absurd:** A quotient field in the mathematical sense is a quotient of a
ring by an ideal (e.g., Z/nZ). `QQ = Frac(ZZ)` is a **fraction field**, also called a
**localization** of ZZ at the prime ideal (0). It has nothing to do with quotients.
The name `QuotientFields` is Sage's historical error, copied into the spec without
mathematical review.

**What the name should be:** `FractionFields`, `LocalizationsOfDomains`, or
`FieldsOfFractions`.

## Absurdity 3: Fields bundles consequence categories as direct parents

**Current code:**
```python
_Fields.super_categories() returns [
    SageFields(),
    _CommutativeRings(),
    _DivisionRings(),
    _EuclideanDomains(),
    _IntegrallyClosedDomains(),
    _NoetherianRings(),
    _ReducedRings(),
    Rings().KrullDimension(0),
]
```

**Why this is absurd:** Fields are commutative, division rings, Euclidean domains,
integrally closed, Noetherian, reduced, and Krull dimension 0. But these are
**consequences** of being a field, not **parents** of fields.
A field does not inherit from EuclideanDomain; rather, a field happens to satisfy all
the axioms of a Euclidean domain.

This is like saying "a field is a Euclidean domain" as an inheritance statement, when
the truth is "every field satisfies the Euclidean domain axioms."

## Absurdity 4: NumberFields does not inherit from GlobalFields

**Current code:** `_NumberFields.super_categories()` returns
`[SageNumberFields(), _Fields()]`, not `[_GlobalFields(), ...]`.

**Why this is absurd:** Number fields are the prototypical example of global fields.
The graph underencodes the most basic relationship in algebraic number theory.

## Absurdity 5: No minimal supercategory principle is enforced

**Current code:** Categories routinely list redundant direct ancestors.

**Why this is absurd:** There is no architectural rule that `super_categories()` must
return only immediate parents.
The result is a graph that is impossible to reason about mathematically because every
category attaches directly to every ancestor it wants methods from, rather than trusting
the graph to propagate them.

## The root cause

The category graph was built incrementally by agents who:
1. Did not understand that category inheritance is a **mathematical inclusion poset**,
   not a Python MRO grab-bag.
2. Added direct ancestors whenever they needed a method, rather than fixing the
   intermediate graph.
3. Never had the graph reviewed by anyone who understands the mathematics.

## The fix

1. **Adopt a minimal supercategory principle:** `super_categories()` must return only
   immediate mathematical parents.
   Ancestors must be reachable through the graph, not listed directly.

2. **Fix the chain:** `NumberFields <= GlobalFields <= Fields`. Remove redundant direct
   attachments.

3. **Rename `_QuotientFields`:** To `_FractionFields` or `_LocalizationsOfDomains`.

4. **Remove consequence categories from `_Fields`:** `_CommutativeRings`,
   `_DivisionRings`, `_EuclideanDomains`, etc.
   are not parents of fields.
   If methods are needed, they should be inherited through the correct graph or defined
   on `_Fields` directly.

5. **Audit every multi-parent category:** For each, ask: are these truly independent
   structures being combined, or is one a consequence/ancestor of another?

## The tool we need

The repo needs a way to visualize and audit the category graph.
A simple script should:
- Extract all `super_categories()` returns.
- Build the graph.
- Flag categories with more than one local parent.
- Flag categories whose parents are not minimal (i.e., one parent is a descendant of
  another).
- Output a plain-text tree for human mathematical review.

Without this tool, the graph will continue to accumulate absurdities.

## Related

- `mathematical-sanity-check`: the mandatory sanity gate before committing mathematical
  code.
- `category-spec-interface-collisions-are-code-problems`: the rule that method name
  collisions are internal code problems, not design questions.
- `category-spec-graph-minimality`: the rule that super_categories() must list immediate
  parents only.
