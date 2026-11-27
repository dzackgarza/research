# Topological Spaces Triage

## Current Smoke Frontier

The Sage warning about `Sets.Topological` not being a `CategoryWithAxiom` is still
visible during smoke runs. Under `docs/MAPPING.md`, this is an implementation-frontier
warning for the settled `TopologicalSpaces()` inheritance path, not an unresolved
ownership decision.

## Current Blockers

- `TopologicalSpaces().Constructors()` remains empty by design. Named set constructors
  currently live under `Sets().Constructors()` and refine into topological categories.
- Root topological methods now use the ambient-relative shape
  `X.is_open(U: Subset)`, `X.is_closed(U)`, `X.closure(U)`, `X.interior(U)`, and
  `X.boundary(U)`. No implementation or smoke yet proves recovery of Sage
  `RealSet.is_open()`, `RealSet.closure()`, and related subset methods through this
  ambient route.
- Sage `RealSet(*args)` is variadic and accepts manifold-producing keyword paths. The
  project surface maps admitted real-line subset construction through named
  `Sets().Constructors()` paths and excludes the manifold paths.
- Sage real and complex ball fields are not currently metric spaces in Sage:
  observed `RBF in Sets().Metric()` and `CBF in Sets().Metric()` are both `False`,
  and neither parent exposes `dist`. Their topological recovery belongs through
  topological ring/field work, not through pure topological-space constructors.

## Settled Decisions

- Named real-line and interval constructors live under `Sets().Constructors()` for
  discoverability, then refine into `TopologicalSpaces()` and
  `TopologicalSpaces().Subobjects()` when they carry that structure.
- Keep both the universal endpoint/closure constructor and named interval/ray
  constructors. Named constructors delegate to the universal constructor.
- `metric()` names the metric map `X x X -> RR`; `dist(x, y)` evaluates it.
- Metric point methods such as `x.dist(y)` belong on `MetricSpacesElement` as parent
  delegation. `abs()` stays out of pure metric spaces unless the required zero/norm
  structure is present.
- Metric homsets are short-map homsets. This is currently a spec-level declaration, not
  an effectively enforced constructor behavior.

## Remaining Smoke Design Work

- Choose canonical smoke examples for local `Connected`, `Compact`, and
  `Metric().Complete()` subcategories when smoke coverage is expanded.
