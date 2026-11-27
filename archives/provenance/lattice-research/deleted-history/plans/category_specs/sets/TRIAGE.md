# Sets Triage

Source: `sage /home/dzack/research/plans/category_specs/sets/smoketest.sage`

This file records the set-side failures exposed by the current smoke test. Every named set constructor currently fails before object-specific ABC validation begins.

## Primary blocker

All smoked named set constructors fail with the same structural assertion:

`AssertionError: <class 'category_specs.sets.specialized._...'> is not a direct subclass of <class 'sage.categories.category_singleton.Category_singleton'>`

This means the named set refinement path is currently broken at category construction time. The smoke test never reaches per-constructor method validation.

## Affected constructors

- `Sets().NamedSets().Set(ZZ)`
- `Sets().NamedSets().Set([1, 2, 3])`
- `Sets().NamedSets().FiniteEnumeratedSet([1, 2, 3])`
- `Sets().NamedSets().IntegerRange(5)`
- `Sets().NamedSets().NonNegativeIntegers()`
- `Sets().NamedSets().PositiveIntegers()`
- `Sets().NamedSets().Primes()`
- `Sets().NamedSets().RealSet((0, 1))`
- `Sets().NamedSets().RecursivelyEnumeratedSet([0], lambda n: [n + 1], enumeration='breadth')`
- `Sets().NamedSets().DisjointUnionEnumeratedSets(Family(...))`
- `Sets().NamedSets().CartesianProduct([IntegerRange(2), IntegerRange(3)])`
- `Sets().NamedSets().ConditionSet(ZZ, lambda n: n % 2 == 0)`
- `Sets().NamedSets().ImageSubobject(lambda n: n + 1, IntegerRange(3))`
- `Sets().NamedSets().TotallyOrderedFiniteSet(['a', 'b', 'c'])`
- `Sets().NamedSets().FiniteSetMaps(IntegerRange(2), IntegerRange(2))`
- `Sets().NamedSets().Family(IntegerRange(3), lambda i: i**2)`
- `Sets().NamedSets().EnumeratedSetFromIterator(lambda: iter([0, 1, 2]))`
- `Sets().NamedSets().cartesian_product(IntegerRange(2), IntegerRange(3))`

## Consequence

The current set subtree has one dominant blocker, not a spread of independent interface gaps. Fixing the named category construction path is a prerequisite for meaningful set-side ABC triage.
