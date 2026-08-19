---
title: Category Spec Properties, Witnesses, And Equipped Structure
status: active
date: 2026-06-01
included_by: [index]
---
# Category Spec Properties, Witnesses, And Equipped Structure

## Object of the invariant

Property subcategories and equipped-structure subcategories in `category_specs`.

## False substitute it blocks

Collapsing "object has property P" into "object is equipped with a distinguished witness
for P", or conversely allowing an implementation to claim P without any abstract method
that can supply evidence for the claim.

## Correct first question

Is the category asserting existence of structure, or is it adding a chosen structure as
part of the object?

## Operative invariant

Property categories and equipped categories are distinct.

`FinitelyGenerated` means the module is finitely generated.
It does not mean the module is equipped with a specified finite generating set.
`WithFiniteGeneratingSet` or `WithOrderedGeneratingSet` is the smaller category where a
particular generating set or ordered generating family is part of the object.

The spec does not currently enforce full proof-relevance at refinement time.
Refinement is declaration, not validation.
However, a property category must still name the abstract witness-producing operations
that make the claim auditable by downstream consumers.
For example, `FinitelyGenerated.ParentMethods` should require an abstract
`generating_set()` method returning some finite generating set, and a promotion method
such as `with_generating_set(S)` that equips the same module with a chosen witness.

The category edge therefore goes from equipped witness to property:

```text
WithOrderedGeneratingSet <= FinitelyGenerated <= Modules
```

not from property to equipped witness.

The same principle applies to bases, presentations, coordinate charts, decompositions,
finite covers, and matrix representatives.
An object may be known to have such a structure without that structure being a
distinguished part of the object.

## Witness example

Sage's tensor-calculus `FiniteRankFreeModule` is free of finite rank but explicitly has
no distinguished basis at construction.
It lies in finite-dimensional modules/vector spaces, not in `ModulesWithBasis`.
Bases can later be introduced, multiple bases can coexist, and a default basis is only a
convenience for omitted arguments, not the same thing as a distinguished basis.

## Non-example

Do not make `FinitelyGenerated.extra_super_categories()` return
`WithOrderedGeneratingSet`.
That says every finitely generated module is already equipped with an ordered generating
family, which is exactly the property/equipped-structure collapse Sage's tensor-calculus
module avoids.
