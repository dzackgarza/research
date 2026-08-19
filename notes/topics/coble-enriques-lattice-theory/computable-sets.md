# Computable Sets in Sage Categories

## Assumption

Unless explicitly stated otherwise, **Sets** in this project's category hierarchy
means the category of **computable sets**: sets whose elements admit algorithmic
membership tests and, when the set is countable, an algorithmic enumeration
witnessed by a function `ℕ → X` or `X → ℕ`.

## Justification

SageMath is a computational framework. Every object in Sage must support
effective operations — membership, iteration, construction. A set that is
countable but not recursively presentable (e.g., a set whose elements exist
set-theoretically but have no computable membership test) cannot be represented
in Sage in any operationally useful way. This restriction loses nothing relevant
to the research project's domain (algebraic geometry, lattice theory, number
theory, and combinatorics), where every set that arises naturally is recursively
presentable.

## Relationship to EnumeratedSets

Sage's `EnumeratedSets` category captures: "there exists an explicit enumeration
(iteration) of the set's elements." In this project, `Sets().Countable()`
identifies with Sage's `EnumeratedSets`: a set is countable iff there exists a
function `X → ℕ` or `ℕ → X`, and we require a witnessing such function. The fact
that Python can only express computable functions is a feature, not a limitation
— it reflects that we work in the computable universe.

Concretely:
- `EnumeratedSets` ↔ `Sets().Countable()`
- `FiniteEnumeratedSets` ↔ `Sets().Countable().Finite()`
- `InfiniteEnumeratedSets` ↔ `Sets().Countable().Infinite()`

Recursively enumerable sets (e.g., `RecursivelyEnumeratedSet` in Sage) are
within this framework: they are countable sets whose enumeration may repeat or
not terminate for absent elements, which is consistent with the constructive
countability requirement.

## What this implies

- Every countable set in the project hierarchy supplies `__iter__` (via
  `__getitem__` and `rank`, or directly).
- Membership `x in X` is required to be computable (terminating for all inputs).
- Finite cardinality, `list(X)`, and `tuple(X)` are defined only when the set is
  finite.
- This restriction is a design decision, not a theorem about sets in general.
  It is documented here so that downstream category definitions and method
  surfaces can rely on effective enumeration and membership without restating
  the computability hypotheses.
