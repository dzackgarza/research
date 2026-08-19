# GAP toric Lattice Methods Reference
## toric package surfaces for cone, fan, and lattice-point workflows

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[PKG]` | GAP package method |
| `[TORIC]` | Toric geometry workflow |
| `[POLY]` | Polyhedral/cone/lattice-point workflow |
| `[ZZMOD]` | Integer lattice or integer-coordinate data surface |

---

## 1. Package Scope

| Package | Role | Tags |
|---------|------|------|
| `toric` | Cones, fans, affine toric varieties, divisor-polytopes, and lattice-point routines | `[PKG, TORIC, POLY, ZZMOD]` |

---

## 2. Method Surface

| Method | Contract summary | Tags |
|--------|------------------|------|
| `InsideCone(...)` | Membership test in a cone for integer-coordinate inputs. | `[PKG, TORIC, POLY, ZZMOD]` |
| `InDualCone(...)` | Membership test in dual cone. | `[PKG, TORIC, POLY, ZZMOD]` |
| `PolytopeLatticePoints(...)` | Enumerate/extract lattice points of a polytope. | `[PKG, TORIC, POLY, ZZMOD]` |
| `Faces(...)` | Face extraction in cone/fan/polytope settings. | `[PKG, TORIC, POLY]` |
| `ConesOfFan(...)` | Cone collection of a fan. | `[PKG, TORIC, POLY]` |
| `NumberOfConesOfFan(...)` | Cardinality/level counts for fan cones. | `[PKG, TORIC, POLY]` |
| `ToricStar(...)` | Star construction in fan geometry. | `[PKG, TORIC, POLY]` |
| `DualSemigroupGenerators(...)` | Semigroup generators in dual-cone context. | `[PKG, TORIC, POLY, ZZMOD]` |
| `EmbeddingAffineToricVariety(...)` | Affine toric embedding and ideal data workflow. | `[PKG, TORIC]` |
| `DivisorPolytope(...)` | Polytope associated to toric divisor data. | `[PKG, TORIC, POLY, ZZMOD]` |
| `DivisorPolytopeLatticePoints(...)` | Lattice points of divisor polytope. | `[PKG, TORIC, POLY, ZZMOD]` |
| `RiemannRochBasis(...)` | Basis computation for divisor/Riemann-Roch spaces in toric context. | `[PKG, TORIC, POLY, ZZMOD]` |
| `EulerCharacteristic(...)` | Euler characteristic in toric variety workflows. | `[PKG, TORIC]` |
| `BettiNumberToric(...)` | Betti-number routine for toric varieties/objects. | `[PKG, TORIC]` |
| `CardinalityOfToricVariety(...)` | Counting/cardinality routine for toric varieties (for relevant finite contexts). | `[PKG, TORIC]` |

Signature note:
- Current local evidence for this package is method-name complete in checklist form.
  Full typed argument signatures should be lifted in a future pass from chapter-level
  API pages where needed.

---

## 3. Domain Caveats

- The toric package surface is combinatorial and polyhedral over integer lattices.
- It does not provide arithmetic-lattice signature/genus/isometry classification APIs.
- Methods involving varieties/divisors depend on toric-object model assumptions from the
  package manuals; exact argument-type contracts should be confirmed per chapter.

---

## 4. Consolidated Method Index

- `BettiNumberToric`
- `CardinalityOfToricVariety`
- `ConesOfFan`
- `DivisorPolytope`
- `DivisorPolytopeLatticePoints`
- `DualSemigroupGenerators`
- `EmbeddingAffineToricVariety`
- `EulerCharacteristic`
- `Faces`
- `InDualCone`
- `InsideCone`
- `NumberOfConesOfFan`
- `PolytopeLatticePoints`
- `RiemannRochBasis`
- `ToricStar`

---

## References

- `docs/archive/scope_violations/toric_methods_checklist.md`
- `docs/archive/scope_violations/toric/upstream/toric_online_provenance_2026-02-17.md`
- Existing umbrella mapping:
  `docs/gap/lattice/gap_lattice_methods_reference.md`
- GAP toric package page: `https://gap-packages.github.io/toric/`
- GAP toric manual table of contents: `https://gap-packages.github.io/toric/doc/chap0_mj.html`
