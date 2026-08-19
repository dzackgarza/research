# LattE Integrale Online Provenance Snapshot (2026-02-17 UTC)

Scope: first-class checklist/reference surface creation for LattE Integrale command surfaces.

---

## 1. Sources surveyed

- Project home:
  - `https://www.math.ucdavis.edu/~latte/`
- Download/docs hub:
  - `https://www.math.ucdavis.edu/~latte/software/packages/latte_current/`
- User guide:
  - `https://www.math.ucdavis.edu/~latte/software/download/latte-current/latte-intro.pdf`

---

## 2. Extracted command/method surface

From project site feature text:

- Program list includes:
  - `count`
  - `integrate`
  - `latte-maximize`
  - `latte-minimize`
  - `latte-draw`

From user guide command synopsis sections:

- `count [options] filename`
  - includes options such as `--ehrhart-polynomial`, `--multivariate-generating-function`,
    `--interior`, and backend/input-mode options including `--cdd`, `--gmp`.
- `integrate [options] filename`
  - includes `--valuation=integrate|volume`, `--cone-decompose`, `--triangulate`,
    `--composite-simplicial-cone`, and backend/input-mode options.
- `latte-minimize [options] fileName`
- `latte-maximize [options] fileName`
  - both documented with backend/input-format options including `--cdd`, `--gmp`, `--vrep`, `--hrep`.

---

## 3. Domain notes captured for docs

- LattE Integrale is a polyhedral/lattice-point workflow stack (counting, integration, optimization).
- No surveyed source indicates indefinite arithmetic quadratic-form genus/isometry API surfaces.
