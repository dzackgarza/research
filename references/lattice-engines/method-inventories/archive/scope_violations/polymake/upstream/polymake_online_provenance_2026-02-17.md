# polymake Online Provenance Snapshot (2026-02-17 UTC)

Scope: first-class checklist/reference surface creation for missing polymake lattice-polytope methods.

---

## 1. Sources surveyed

Primary package sources:

- `https://polymake.org/`
- `https://github.com/polymake/polymake`

Target API docs discovered:

- `https://polymake.org/release_docs/3.2/polytope.html`

Method-surface evidence captured from indexed release-doc snippets:

- `LATTICE_POINTS(Polytope)`
- `LATTICE_POINTS_GENERATORS(Polytope)`
- `N_LATTICE_POINTS_IN_DILATION(Polytope, Int n)`
- `FACET_POINT_LATTICE_DISTANCES(Polytope, Vector)`
- `EHRHART_POLYNOMIAL`
- `EHRHART_QUASI_POLYNOMIAL`
- `H_STAR_VECTOR`
- `H_STAR_POLYNOMIAL`
- `POLYTOPE_IN_STD_BASIS(Polytope<Rational>)`

---

## 2. Environment access notes

Direct page retrieval of release docs was blocked in this environment (HTTP 403) for discovered URLs, including:

- `https://polymake.org/release_docs/3.2/polytope.html`

Because the URL is canonical but direct fetch is blocked, this pass:

- created first-class checklist/reference surfaces anyway (FIRST GOAL),
- labeled the signature/type fidelity caveat explicitly,
- recorded the exact blocker for follow-up revalidation.

---

## 3. Remaining signature-fidelity gap

- Re-run a direct extraction pass from release docs or local polymake documentation build to confirm complete typed method signatures beyond search-index snippets.
