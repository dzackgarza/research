# polymake Lattice Method Reference
## Lattice-polytope counting and Ehrhart/h* surfaces

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[API]` | polymake property/method surface |
| `[POLY]` | Polytope workflow |
| `[ENUM]` | Lattice-point enumeration/counting |
| `[EHR]` | Ehrhart/quasi-polynomial surface |

---

## 1. Scope

`polymake` provides extensive polyhedral/combinatorial-geometry tooling. This surface captures lattice-polytope methods with explicit lattice-point and Ehrhart semantics.

Not in scope:

- indefinite quadratic-form genus/discriminant/isometry classification APIs.

---

## 2. Lattice-Point and Distance Methods

| Method | Argument surface | Return/Type surface | Contract | Tags |
|---|---|---|---|---|
| `LATTICE_POINTS(Polytope)` | polytope object | matrix of lattice points (documented as rational matrix in release docs) | Enumerates lattice points associated to the polytope. | `[API, POLY, ENUM]` |
| `LATTICE_POINTS_GENERATORS(Polytope)` | polytope object | array of integer-set generators | Returns generator structure for lattice-point set representation. | `[API, POLY, ENUM]` |
| `N_LATTICE_POINTS_IN_DILATION(Polytope, Int n)` | polytope and integer dilation parameter `n` | integer count | Counts lattice points in dilated polytope. | `[API, POLY, ENUM]` |
| `FACET_POINT_LATTICE_DISTANCES(Polytope, Vector)` | polytope and vector argument | integer | Computes lattice distance data to facets from a point/vector argument. | `[API, POLY, ENUM]` |

---

## 3. Ehrhart / h* Surfaces

| Property/Method | Surface | Contract | Tags |
|---|---|---|---|
| `EHRHART_POLYNOMIAL` | lattice-polytope property | Provides Ehrhart polynomial data when polynomial regime applies. | `[API, POLY, EHR]` |
| `EHRHART_QUASI_POLYNOMIAL` | lattice-polytope property | Provides quasi-polynomial count data in periodic regimes. | `[API, POLY, EHR]` |
| `H_STAR_VECTOR` | lattice-polytope property | h*-vector/invariant surface associated to Ehrhart data. | `[API, POLY, EHR]` |
| `H_STAR_POLYNOMIAL` | lattice-polytope property | h*-polynomial representation of Ehrhart/h* invariants. | `[API, POLY, EHR]` |

---

## 4. Basis Conversion Surface

| Method | Argument surface | Contract | Tags |
|---|---|---|---|
| `POLYTOPE_IN_STD_BASIS(Polytope<Rational>)` | rational polytope object | Converts a lattice polytope given in a lattice basis into standard-coordinate basis representation. | `[API, POLY]` |

---

## 5. Assumptions and Constraints

- These methods/properties are tied to polymake's polytope application and lattice-polytope object models.
- Several surfaces are property-style APIs (not standalone CLI commands), so contracts are object-context dependent.
- In this environment, direct fetch of release-doc pages was access-restricted (`403`) and method/type extraction relies on search-index snapshots plus package metadata; this is explicitly tracked in provenance and should be revalidated with direct page retrieval in a follow-up pass.

---

## 6. Sources

- polymake repository: `https://github.com/polymake/polymake`
- polymake package page: `https://polymake.org/`
- polymake release docs (lattice polytope section): `https://polymake.org/release_docs/3.2/polytope.html`
- local provenance snapshot: `docs/archive/scope_violations/polymake/upstream/polymake_online_provenance_2026-02-17.md`
