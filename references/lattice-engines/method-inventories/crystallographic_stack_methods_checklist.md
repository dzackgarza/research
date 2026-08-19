# GAP Crystallographic Stack Method Test Gap Checklist

Tracks GAP crystallographic package surfaces documented in
`docs/crystallographic_stack/lattice/research_readme.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. Package Load Surfaces

- [ ] `LoadPackage("Cryst")`
- [ ] `LoadPackage("CARATInterface")`
- [ ] `LoadPackage("CrystCat")`

---

## 2. Cryst Core Group and Lattice Methods (Canonical)

- [ ] `AffineCrystGroupOnRight(S)`
- [ ] `AsAffineCrystGroupOnRight(S)`
- [ ] `IsAffineCrystGroupOnRight(S)`
- [ ] `AffineCrystGroupOnLeft(S)`
- [ ] `PointGroup(S)`
- [ ] `TranslationsCrystGroup(S)`
- [ ] `SpaceGroupsByPointGroupOnRight(P[, normedQclass[, orbitsQclass]])`
- [ ] `WyckoffPositions(S)`
- [ ] `WyckoffOrbit(G, p)`
- [ ] `WyckoffLattice(G, p)`
- [ ] `WyckoffNormalClosure(G, p)`

---

## 3. CARAT/Bravais Class and Normalizer Methods (Canonical)

- [ ] `BravaisGroup(R)`
- [ ] `PointGroupsBravaisClass(R)`
- [ ] `BravaisSubgroups(R)`
- [ ] `BravaisSupergroups(R)`
- [ ] `NormalizerInGLnZ(R)`
- [ ] `CentralizerInGLnZ(R)`
- [ ] `IsBravaisEquivalent(R, S)`
- [ ] `CaratZClass(R)`
- [ ] `CaratZClassNumber(R)`
- [ ] `CaratQClass(R)`
- [ ] `CaratQClassNumber(R)`
- [ ] `RationalClassesMaximalSubgroups(R)`
- [ ] `ZClassRepsQClass(R)`
- [ ] `MaximalSubgroupsRepresentatives(R)`
- [ ] `AffineNormalizer(R)`
- [ ] `IsCaratZClass(R)`
- [ ] `IsCaratQClass(R)`

---

## Legacy Alias Triage

The following names are tracked as legacy aliases pending explicit confirmation in
current canonical docs; they are not counted as active canonical checklist targets:

- `CrystCatZClass(...)`
- `CrystCatQClass(...)`
- `CrystCatQClasses(...)`

---

## Domain and Constraint Caveats

- These are Euclidean crystallographic and integer-matrix-group workflows.
- The methods are not general indefinite quadratic-form genus/isometry classifiers.
- For `SpaceGroupsByPointGroupOnRight(P[, normedQclass[, orbitsQclass]])`,
  `normedQclass` is `false` or a normalizer-element list in `GL(d,Z)`, and
  `orbitsQclass` is boolean (`true` returns all representatives per orbit).
- Selector arguments `f`, `s`, and `k` are not treated as active canonical contract
  parameters for CARAT methods in this checklist surface.

---

## References

- `docs/crystallographic_stack/lattice/research_readme.md`
- `docs/crystallographic_stack/upstream/crystallographic_stack_online_provenance_2026-02-17.md`
- Existing GAP umbrella reference:
  `docs/gap/lattice/research_readme.md`
- Cryst package page: `https://gap-packages.github.io/cryst/`
- GAP Cryst package manual: `https://docs.gap-system.org/pkg/cryst/htm/CHAP002.htm`
- GAP Reference Manual (CARAT methods): `https://docs.gap-system.org/doc/ref/chap44.html`
- CARATInterface package manual: `https://www.math.rwth-aachen.de/~GAP/WWW2/PackagePages/caratinterface/doc/manual.pdf`
