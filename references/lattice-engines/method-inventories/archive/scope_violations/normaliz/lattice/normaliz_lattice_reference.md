# Normaliz Lattice and Polyhedral Reference
## CLI, Python, and GAP wrapper surfaces relevant to lattice/combinatorial workflows

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[CONE]` | Cone/polyhedron workflow |
| `[MONOID]` | Affine monoid / Hilbert-basis workflow |
| `[LPT]` | Lattice-point counting/enumeration |
| `[CLI]` | Command-line surface |
| `[PY]` | Python interface |
| `[GAP]` | GAP interface |

---

## 1. Scope

Normaliz is a discrete-convex-geometry engine for affine monoids, vector configurations, rational polyhedra, and rational cones. Lattice-relevant surfaces include:

- Hilbert basis and Hilbert/Ehrhart-style computations,
- support hyperplanes, triangulations, and cone/lattice data,
- lattice-point/volume computations,
- lattice and toric ideal support in the broader Normaliz ecosystem.

---

## 2. Normaliz CLI Surface

| API | Description | Tags |
|-----|-------------|------|
| `normaliz <project>` | Runs Normaliz on a project input, typically loading `<project>.in`. | `[CONE, MONOID, LPT, CLI]` |
| `normaliz --HilbertBasis <project>` | Explicit computation-goal request for Hilbert basis. | `[CONE, MONOID, CLI]` |
| `normaliz --SupportHyperplanes <project>` | Explicit computation-goal request for support hyperplanes. | `[CONE, CLI]` |
| `normaliz --HilbertSeries <project>` | Explicit computation-goal request for Hilbert series. | `[MONOID, LPT, CLI]` |
| `normaliz --OutputDir=<outdir> <project>` | Redirect output files to a selected directory. | `[CLI]` |
| `normaliz --help` / `normaliz --version` | CLI help/version reporting. | `[CLI]` |

Documented execution rules include:

- if no `<project>` is given, program terminates,
- options from command line and input file accumulate,
- Normaliz searches for `<project>.in` as canonical project input,
- if explicitly requested goals are impossible (for example missing required grading), computation can terminate.

---

## 3. PyNormaliz Surface

| API | Description | Tags |
|-----|-------------|------|
| `Cone(**input_types)` | Construct cone/lattice object from Normaliz input-type keywords. | `[CONE, PY]` |
| `Cone.Compute(*goals_or_options)` | Compute one or more properties/goals in a single call. | `[CONE, MONOID, LPT, PY]` |
| `Cone.IsComputed(goal)` | Query whether a specific goal is already computed. | `[PY]` |
| `Cone.HilbertBasis()` | Retrieve Hilbert basis vectors. | `[MONOID, PY]` |
| `Cone.HilbertSeries(HSOP=True)` | Retrieve Hilbert-series encoding (with option flags). | `[MONOID, LPT, PY]` |
| `Cone.LatticePoints()` | Enumerate lattice points (when defined/finite under chosen goals). | `[LPT, PY]` |
| `Cone.Volume()` | Retrieve lattice-normalized volume. | `[LPT, PY]` |
| `Cone.EuclideanVolume()` | Retrieve Euclidean volume; formatted floating output may be string-encoded. | `[LPT, PY]` |
| `Cone.SupportHyperplanes()` / `Cone.SuppHypsFloat()` | Exact and floating support-hyperplane outputs. | `[CONE, PY]` |
| `NmzResult(cone, property)` | Low-level property retrieval from the wrapped Normaliz cone object. | `[PY]` |

PyNormaliz contract caveats documented upstream:

- algebraic/fractional inputs for number-field workflows are string-encoded,
- some floating outputs are string-formatted in high-level wrappers,
- full property inventory is delegated to the Normaliz manual/API.

---

## 4. GAP NormalizInterface Surface

| API | Description | Tags |
|-----|-------------|------|
| `NmzCone(list)` | Create a Normaliz cone object from alternating input-type strings and integer matrices. | `[CONE, GAP]` |
| `NmzCompute(cone[, propnames])` | Trigger computation of default or selected cone properties. | `[CONE, MONOID, LPT, GAP]` |
| `NmzConeProperty(cone, property)` | Compute/retrieve a named property result. | `[GAP]` |
| `NmzKnownConeProperties(cone)` | Enumerate properties currently known for a cone object. | `[GAP]` |
| `NmzHasConeProperty(cone, property)` | Check whether a property is already known/computed. | `[GAP]` |
| `NmzSupportHyperplanes(cone)` | Support-hyperplane property alias. | `[CONE, GAP]` |
| `NmzHilbertBasis(cone)` | Hilbert-basis property alias. | `[MONOID, GAP]` |
| `NmzNumberLatticePoints(cone)` | Lattice-point counting property alias. | `[LPT, GAP]` |
| `NmzProjectCone(cone)` | Project-cone property alias (version-dependent support). | `[CONE, GAP]` |

GAP wrapper caveat:

- `Nmz*` property aliases and availability are tied to the linked Normaliz version, as documented in the package manual.

---

## 5. Domain Caveat

Normaliz surfaces here are polyhedral/monoid/lattice-point computational APIs. They are not high-level indefinite arithmetic-lattice genus/discriminant/isometry classification APIs.

---

## 6. Sources

- Normaliz README and feature scope: `https://github.com/Normaliz/Normaliz`
- Normaliz command-line option/manual text (upstream-packaged docs): `https://sources.debian.org/src/normaliz/3.10.4%2Bds-1/doc/Options.tex`
- PyNormaliz README/API examples: `https://github.com/Normaliz/PyNormaliz`
- GAP NormalizInterface function docs: `https://docs.gap-system.org/pkg/normalizinterface/doc/chap2_mj.html`
