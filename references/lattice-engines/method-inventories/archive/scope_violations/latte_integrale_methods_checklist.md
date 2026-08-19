# LattE Integrale Method Test Gap Checklist

Tracks LattE Integrale methods/commands documented in `docs/archive/scope_violations/latte_integrale/lattice/latte_integrale_lattice_reference.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. Core CLI Programs

- [ ] `count [options] filename`
- [ ] `integrate [options] filename`
- [ ] `latte-minimize [options] fileName`
- [ ] `latte-maximize [options] fileName`
- [ ] `latte-draw [options]`

## 2. `count` Option Surface

- [ ] `--ehrhart-polynomial`
- [ ] `--multivariate-generating-function`
- [ ] `--interior`
- [ ] `--cdd`
- [ ] `--gmp`

## 3. `integrate` Option Surface

- [ ] `--valuation=integrate`
- [ ] `--valuation=volume`
- [ ] `--cone-decompose`
- [ ] `--triangulate`
- [ ] `--composite-simplicial-cone`

## 4. Optimization Program Surface

- [ ] `latte-minimize [options] fileName` with backend/input-format options (`--cdd`, `--gmp`, `--vrep`, `--hrep`)
- [ ] `latte-maximize [options] fileName` with backend/input-format options (`--cdd`, `--gmp`, `--vrep`, `--hrep`)

---

## Domain Caveats

- LattE Integrale is a polyhedral/lattice-point counting and optimization stack over rational cones/polyhedra.
- It does not provide indefinite arithmetic quadratic-form genus/isometry APIs.

---

## References

- `docs/archive/scope_violations/latte_integrale/lattice/latte_integrale_lattice_reference.md`
- `docs/archive/scope_violations/latte_integrale/upstream/latte_integrale_online_provenance_2026-02-17.md`
- LattE Integrale project site: `https://www.math.ucdavis.edu/~latte/`
- LattE user guide PDF: `https://www.math.ucdavis.edu/~latte/software/download/latte-current/latte-intro.pdf`
