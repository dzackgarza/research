# PALP Method Test Gap Checklist

Tracks PALP methods/commands documented in `docs/archive/scope_violations/palp/lattice/palp_lattice_reference.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. Core PALP CLI Programs

- [ ] `poly.x [options] [in-file [out-file]]`
- [ ] `class.x [options] [in-file [out-file]]`
- [ ] `cws.x [options] [in-file [out-file]]`
- [ ] `nef.x [options] [in-file [out-file]]`
- [ ] `mori.x [options] [in-file [out-file]]`

## 2. CLI Option Surface

### 2.1 `poly.x`

- [ ] `-h`
- [ ] `-f`
- [ ] `-g`
- [ ] `-p`
- [ ] `-r`
- [ ] `-v`

### 2.2 `class.x`

- [ ] `-h`
- [ ] `-f`
- [ ] `-m`
- [ ] `-p`
- [ ] `-v`

### 2.3 `cws.x`

- [ ] `-h`
- [ ] `-f`
- [ ] `-w[#]`

### 2.4 `nef.x`

- [ ] `-h`
- [ ] `-f*`
- [ ] `-N`
- [ ] `-H`
- [ ] `-Lv`
- [ ] `-p`
- [ ] `-D`
- [ ] `-P`
- [ ] `-t`
- [ ] `-c*`

### 2.5 `mori.x`

- [ ] `-h`
- [ ] `-f`
- [ ] `-g`
- [ ] `-m`
- [ ] `-P`
- [ ] `-K`
- [ ] `-b`

## 3. Sage Optional-PALP Surface

- [ ] `LatticePolytope.all_points()`
- [ ] `LatticePolytope.all_points_boundary()`
- [ ] `LatticePolytope.all_points_not_interior_to_facets()`
- [ ] `LatticePolytope.integral_points()`
- [ ] `LatticePolytope.fibration_generator(dim)`

---

## Domain Caveats

- PALP is a lattice-polytope and complete-weight-system package; package metadata states practical focus mainly on lattice polytopes in dimensions up to four.
- PALP is not an indefinite quadratic-form genus/isometry classification package.
- Sage `LatticePolytope` methods listed above require optional package `palp` availability.

---

## References

- `docs/archive/scope_violations/palp/lattice/palp_lattice_reference.md`
- `docs/archive/scope_violations/palp/upstream/palp_online_provenance_2026-02-17.md`
- PALP package description (Debian/Ubuntu): `https://packages.ubuntu.com/jammy/math/palp`
- PALP CLI docs (manpages): `https://manpages.debian.org/unstable/palp/palp.1.en.html`
- Sage lattice polytope docs: `https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/lattice_polytope.html`
