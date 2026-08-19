# GAP toric Package Method Test Gap Checklist

Tracks GAP `toric` package methods documented in
`docs/archive/scope_violations/toric/lattice/gap_toric_lattice_reference.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. Package Load Surface

- [ ] `LoadPackage("toric")`

---

## 2. Cone and Dual-Cone Membership

- [ ] `InsideCone(...)`
- [ ] `InDualCone(...)`

---

## 3. Fan, Cone, and Lattice-Point Operations

- [ ] `PolytopeLatticePoints(...)`
- [ ] `Faces(...)`
- [ ] `ConesOfFan(...)`
- [ ] `NumberOfConesOfFan(...)`
- [ ] `ToricStar(...)`
- [ ] `DualSemigroupGenerators(...)`

---

## 4. Toric Variety and Divisor Workflows

- [ ] `EmbeddingAffineToricVariety(...)`
- [ ] `DivisorPolytope(...)`
- [ ] `DivisorPolytopeLatticePoints(...)`
- [ ] `RiemannRochBasis(...)`

---

## 5. Invariant and Counting Surfaces

- [ ] `EulerCharacteristic(...)`
- [ ] `BettiNumberToric(...)`
- [ ] `CardinalityOfToricVariety(...)`

---

## Domain and Constraint Caveats

- `toric` is a combinatorial/polyhedral lattice package over integer lattices and fans.
- These methods are not quadratic-form signature/genus/isometry APIs.
- Method-level signatures are represented in runtime-name form where current docs expose
  name-level inventories instead of full typed prototypes.

---

## References

- `docs/archive/scope_violations/toric/lattice/gap_toric_lattice_reference.md`
- `docs/archive/scope_violations/toric/upstream/toric_online_provenance_2026-02-17.md`
- Existing GAP umbrella reference:
  `docs/gap/lattice/gap_lattice_methods_reference.md`
- GAP toric package page: `https://gap-packages.github.io/toric/`
- GAP toric manual table of contents: `https://gap-packages.github.io/toric/doc/chap0_mj.html`
