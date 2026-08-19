# Normaliz Method Test Gap Checklist

Tracks Normaliz-relevant methods/commands documented in `docs/archive/scope_violations/normaliz/lattice/normaliz_lattice_reference.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. Normaliz CLI Surface

- [ ] `normaliz <project>`
- [ ] `normaliz --HilbertBasis <project>`
- [ ] `normaliz --SupportHyperplanes <project>`
- [ ] `normaliz --HilbertSeries <project>`
- [ ] `normaliz --OutputDir=<outdir> <project>`
- [ ] `normaliz --help`
- [ ] `normaliz --version`

## 2. PyNormaliz Surface

- [ ] `Cone(**input_types)`
- [ ] `Cone.Compute(*goals_or_options)`
- [ ] `Cone.IsComputed(goal)`
- [ ] `Cone.HilbertBasis()`
- [ ] `Cone.HilbertSeries(HSOP=True)`
- [ ] `Cone.LatticePoints()`
- [ ] `Cone.Volume()`
- [ ] `Cone.EuclideanVolume()`
- [ ] `Cone.SupportHyperplanes()`
- [ ] `Cone.SuppHypsFloat()`
- [ ] `NmzResult(cone, property)`

## 3. GAP NormalizInterface Surface

- [ ] `NmzCone(list)`
- [ ] `NmzCompute(cone[, propnames])`
- [ ] `NmzConeProperty(cone, property)`
- [ ] `NmzKnownConeProperties(cone)`
- [ ] `NmzHasConeProperty(cone, property)`
- [ ] `NmzSupportHyperplanes(cone)`
- [ ] `NmzHilbertBasis(cone)`
- [ ] `NmzNumberLatticePoints(cone)`
- [ ] `NmzProjectCone(cone)`

---

## Domain Caveat

- Normaliz and its interfaces here are cone/polyhedron/affine-monoid and lattice-point computation surfaces, not indefinite arithmetic-lattice genus/isometry classifiers.

---

## References

- `docs/archive/scope_violations/normaliz/lattice/normaliz_lattice_reference.md`
- Normaliz repository/readme: `https://github.com/Normaliz/Normaliz`
- PyNormaliz repository/readme: `https://github.com/Normaliz/PyNormaliz`
- GAP NormalizInterface docs: `https://docs.gap-system.org/pkg/normalizinterface/doc/chap2_mj.html`
