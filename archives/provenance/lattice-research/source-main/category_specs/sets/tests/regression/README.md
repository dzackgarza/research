# Regression Tests — Sets Spec

These files prove that the `Sets()` spec does not break existing Sage code.
Each test takes a constructor that previously worked through bare Sage
(`Primes()`, `IntegerRange(...)`, etc.) and runs the same documented examples
through the spec-wrapped call (`Sets().Constructors().X(...)`).  If anything
breaks, the spec has introduced a regression.

Every assertion was copied verbatim from the Sage source doctests cited below;
no values were invented.  No `try/except` — a failure is a finding.

| File | Sage source |
|------|-------------|
| `primes.sage` | `sage.sets.primes.Primes` |
| `finite_enumerated_set.sage` | `sage.sets.finite_enumerated_set.FiniteEnumeratedSet` |
| `non_negative_integers.sage` | `sage.sets.non_negative_integers`, `sage.sets.positive_integers` |
| `integer_range.sage` | `sage.sets.integer_range` |
| `totally_ordered_finite_set.sage` | `sage.sets.totally_ordered_finite_set` |
| `disjoint_union_enumerated_sets.sage` | `sage.sets.disjoint_union_enumerated_sets` |
| `recursively_enumerated_set.sage` | `sage.sets.recursively_enumerated_set` |
| `condition_set.sage` | `sage.sets.condition_set.ConditionSet` through `Sets().Subobjects().Of(...)` |
| `image_set.sage` | `sage.sets.image_set.ImageSubobject` |
| `finite_set_maps.sage` | `sage.sets.finite_set_maps.FiniteSetMaps` |
| `family.sage` | `sage.sets.family.Family` |
| `enumerated_set_from_iterator.sage` | `sage.sets.set_from_iterator.EnumeratedSetFromIterator` |
| `real_set.sage` | `sage.sets.real_set.RealSet` |
| `cartesian_product.sage` | `sage.sets.cartesian_product.CartesianProduct` |
