# Spec Core Query Workflow

`category_specs.spec_core` is the queryable source of truth for category-spec
inspection. Sage category classes expose runtime behavior, but spec-core records the
data an implementer needs before adding or extending a Sage-backed implementation.

## What To Query

Use `Spec.of(report)` when the question is about one object or claimed category:

```python
from category_specs.spec_core import Spec
from category_specs.modules.free_module_witnesses import finite_free_module_report

spec = Spec.of(finite_free_module_report("GF(5)", rank=3, base_cardinality=5))

spec.declared_category
spec.obligations
spec.providers
spec.construction_witnesses
spec.missing_obligations
spec.value("cardinality")
```

The report should answer:

- which category the object claims;
- which obligations it inherits from the category and supercategory closure;
- which providers satisfy obligations directly;
- which construction witnesses satisfy obligations by composition;
- which computed values are known;
- which obligations remain missing.

Use a category constructor collector when the question is how Sage can construct
objects in a category:

```python
from category_specs.cat import Cat
from category_specs.rings import Rings

Rings().Constructors().provenance().constructor("rings.GF")
Cat().Constructors().provenance().by_owner("Rings()")
```

Constructor records expose the mathematical owner, public method name, Sage entry
point, source route, target category, refinement route, and optional provider,
witness, or obligation metadata. The generic adapter derives the target route from
explicit constructor metadata when present and otherwise from the public return
annotation, so the record remains tied to the declared constructor surface.

## Constructor Coverage

Every admitted `Constructors()` surface must return a `ConstructorRegistry` from
`.provenance()`. The current admitted collectors are:

- `Cat().Constructors()`;
- `Rings().Constructors()`;
- `Modules(R).Constructors()`;
- `Sets().Constructors()`;
- `Algebras(R).Constructors()`;
- `Posets().Constructors()`;
- `TopologicalSpaces().Constructors()`;
- `TensorAlgebraComponents(R).Constructors()`;
- `Lattices(R).Constructors()`.

`TopologicalSpaces` and `Lattices` currently have empty constructor registries. Empty
means no standalone constructor has been admitted on that collector; it does not mean
the category is absent. Topological objects currently enter through set constructors
such as real intervals. Lattice objects currently enter through module-side lattice
routes until lattice-native constructors are admitted.

Constructor registries contain admitted constructor routes only. A constructor shape
that is not source-grounded in Sage does not become a registry entry, mapping row,
category-obligation example, or "deferred" record.

## Adding A Sage Implementation

Before adding an implementation, query the spec instead of browsing source by hand.

- Build or retrieve the relevant `SpecReport`.
- Inspect `Spec.of(report).obligations` and `missing_obligations`.
- Inspect `providers` and `construction_witnesses` to reuse existing category-level
  implementations before writing local methods.
- Query the appropriate `Constructors().provenance()` registry to find existing Sage
  constructor routes and refinement targets.
- If a source-grounded Sage constructor route exists, map it to a named-parameter
  category-owned overload and make `.provenance()` expose it through
  `ConstructorRegistry`.
- If Sage lacks the route, do not add a constructor record. Reconstruct the actual
  source task instead of preserving the rejected constructor as a named gap.
- Add or extend focused tests that prove the query result: inherited obligations,
  constructor record, provider or witness evidence, computed values, and missing
  gaps.

Implementation code should satisfy obligations at the highest valid category level.
A free finite-rank module over a countable ring should reuse the countable Cartesian
power witness for set-level enumeration obligations instead of reimplementing
enumeration in the module constructor.

## Validation

Run the focused spec-core check after changing this package or constructor provenance:

```bash
just test-spec-core-vertical-slice
```

This target covers report querying, category obligation closure, generated laws,
constructor registries, Cat aggregation, and the finite/countable free-module witness
slice.
