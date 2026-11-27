# Sets Triage

Source for this pass: `sets/docs/SAGE_INVENTORY.md` and `sets/docs/MAPPING.md`.

This triage records the current `sets/smoketest.sage` frontier. Mathematical mapping
decisions live in `sets/docs/MAPPING.md`.

## Current Smoke Frontier

- `sets/smoketest.sage` now uses the mapped enumeration surface: indexed access,
  rank, iteration, cardinality, and Python conversion protocols. It no longer uses
  Sage `first`, `next`, `unrank`, `list`, `tuple`, range, or fallback-helper names.
- `ZZ in Sets()` currently fails at the root containment statement.
- Most refined set constructors currently expose missing `__richcmp__`.
- `Primes()` currently exposes missing `__iter__`.
- `RealSet([RealSet.open(0, 1).get_interval(0)])` currently exposes missing
  `_element_constructor_`.
- Sage emits a topological axiom warning because `Sets.Topological` resolves to
  `TopologicalSpaces` rather than a local `CategoryWithAxiom` subclass.
- Set partitions now have an inventory and mapping target.  Fixed-base
  `SetPartitions(s)` routes to `Sets().Partitioned()`, while `SetPartitions()` remains
  the countable all-partitions parent because it has no single base-set powerset
  ambient.
