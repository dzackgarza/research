# polymake Method Test Gap Checklist

Tracks polymake lattice-relevant methods documented in `docs/archive/scope_violations/polymake/lattice/polymake_lattice_reference.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. Lattice Polytope Enumeration/Counting Surface

- [ ] `LATTICE_POINTS(Polytope)`
- [ ] `LATTICE_POINTS_GENERATORS(Polytope)`
- [ ] `N_LATTICE_POINTS_IN_DILATION(Polytope, Int n)`
- [ ] `FACET_POINT_LATTICE_DISTANCES(Polytope, Vector)`

## 2. Ehrhart and h*-Invariant Surface

- [ ] `EHRHART_POLYNOMIAL`
- [ ] `EHRHART_QUASI_POLYNOMIAL`
- [ ] `H_STAR_VECTOR`
- [ ] `H_STAR_POLYNOMIAL`

## 3. Basis/Coordinate Conversion Surface

- [ ] `POLYTOPE_IN_STD_BASIS(Polytope<Rational>)`

---

## Domain Caveats

- polymake methods listed here are lattice-polytope/combinatorial-geometry surfaces.
- They are not indefinite arithmetic quadratic-form genus/isometry APIs.

---

## References

- `docs/archive/scope_violations/polymake/lattice/polymake_lattice_reference.md`
- `docs/archive/scope_violations/polymake/upstream/polymake_online_provenance_2026-02-17.md`
- polymake release docs (lattice polytope section): `https://polymake.org/release_docs/3.2/polytope.html`
