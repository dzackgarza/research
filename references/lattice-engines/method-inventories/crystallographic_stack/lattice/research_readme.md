# GAP Crystallographic Stack Lattice Methods Reference
## Cryst, CARAT/Bravais, and CrystCat-related surfaces

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[PKG]` | GAP package method |
| `[EUCLID]` | Euclidean crystallographic setting |
| `[PD]` | Positive-definite crystallographic regime |
| `[ZZMOD]` | Integer matrix or Z-module style workflow |
| `[GRP]` | Matrix-group/classification workflow |
| `[LEGACY]` | Name appears in older mirrors but is not confirmed in current canonical docs |

---

## 1. Package Scope

| Package | Role | Tags |
|---------|------|------|
| `Cryst` | Affine crystallographic groups, space-group and Wyckoff workflows | `[PKG, EUCLID, PD, GRP]` |
| `CARATInterface` | CARAT-backed class and normalizer workflows for integral matrix groups | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `CrystCat` | Catalog/index support for crystallographic classes and data | `[PKG, EUCLID, PD, ZZMOD, GRP]` |

---

## 2. Canonical Cryst Method Surface (GAP Ref Chap. 35)

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `AffineCrystGroupOnRight(gens[, identity])` | `gens`: list of matrices (generators); `identity`: matrix (optional) | `AffineCrystGroup` (right-action) | Construct an affine crystallographic group with right action convention from generators; optionally specify identity matrix. | `[PKG, EUCLID, PD, GRP]` |
| `AsAffineCrystGroupOnRight(S)` | `S`: matrix group | `AffineCrystGroup` (right-action) | Coerce existing matrix group `S` to right-action affine crystallographic representation. | `[PKG, EUCLID, PD, GRP]` |
| `IsAffineCrystGroupOnRight(S)` | `S`: any object | `Boolean` | Predicate: whether `S` is an affine crystallographic group with right action convention. | `[PKG, EUCLID, PD, GRP]` |
| `AffineCrystGroupOnLeft(gens[, identity])` | `gens`: list of matrices (generators); `identity`: matrix (optional) | `AffineCrystGroup` (left-action) | Construct an affine crystallographic group with left action convention from generators. | `[PKG, EUCLID, PD, GRP]` |
| `PointGroup(S)` | `S`: `AffineCrystGroup` | GAP group (quotient group S/T) | Return the point-group quotient $S/T$ where $T$ is the translation subgroup. | `[PKG, EUCLID, PD, GRP]` |
| `TranslationsCrystGroup(S)` | `S`: `AffineCrystGroup` | list (integer lattice generators of translation subgroup) | Return the translation subgroup (integral lattice) of the crystallographic group `S`; generators form a basis for the translation lattice. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `SpaceGroupsByPointGroupOnRight(P[, normedQclass[, orbitsQclass]])` | `P`: finite subgroup of $GL(d,\mathbb{Z})$; `normedQclass`: `false` or list of elements in $N_{GL(d,\mathbb{Z})}(P)$ (optional); `orbitsQclass`: boolean (optional; `true` returns all representatives in each normalizer orbit) | list of `AffineCrystGroup` objects | Enumerate space groups with point group `P`; optional selector arguments control normalizer orbit filtering. | `[PKG, EUCLID, PD, GRP]` |
| `WyckoffPositions(S)` | `S`: space group (`AffineCrystGroup`) | list of Wyckoff position records | Compute the list of Wyckoff-position class representatives for space group `S`. | `[PKG, EUCLID, PD, GRP]` |
| `WyckoffOrbit(G, p)` | `G`: `AffineCrystGroup`; `p`: Wyckoff position representative | list of Wyckoff position representatives | Return the orbit of Wyckoff position `p` under group `G`. | `[PKG, EUCLID, PD, GRP]` |
| `WyckoffLattice(G, p)` | `G`: `AffineCrystGroup`; `p`: Wyckoff position representative | record (lattice/stabilizer data) | Return the lattice and stabilizer data for the Wyckoff computation at `(G, p)`. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `WyckoffNormalClosure(G, p)` | `G`: `AffineCrystGroup`; `p`: Wyckoff position representative | `AffineCrystGroup` (normal closure) | Compute the normal-closure group in the Wyckoff workflow for `(G, p)`. | `[PKG, EUCLID, PD, GRP]` |

---

## 3. Canonical CARAT/Bravais Surface (GAP Ref Chap. 44.6)

| Method | Argument Types | Return Type | Description | Tags |
|--------|----------------|-------------|-------------|------|
| `BravaisGroup(R)` | `R`: finite integer matrix group | integer matrix group (Bravais group of `R`) | Compute the Bravais group of `R`: the largest integer matrix group with the same rational span as `R` (44.6-11). | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `PointGroupsBravaisClass(R)` | `R`: finite integer matrix group | list of integer matrix groups | Return point-group representatives in the Bravais class of `R` (44.6). | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `BravaisSubgroups(R)` | `R`: finite integer matrix group | list of integer matrix groups (Bravais subgroups) | Enumerate subgroups of the Bravais group of `R` that are themselves Bravais groups (44.6-12). | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `BravaisSupergroups(R)` | `R`: finite integer matrix group | list of integer matrix groups (Bravais supergroups) | Enumerate subgroups of $GL(n,\mathbb{Z})$ that contain the Bravais group of `R` and are themselves Bravais groups (44.6-13). | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `NormalizerInGLnZ(R)` | `R`: integer matrix group of dimension n | integer matrix group (normalizer of `R` in $GL(n,\mathbb{Z})$) | Compute the normalizer of `R` in $GL(n,\mathbb{Z})$ (44.6-7). | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `CentralizerInGLnZ(R)` | `R`: integer matrix group of dimension n | integer matrix group (centralizer of `R` in $GL(n,\mathbb{Z})$) | Compute the centralizer of `R` in $GL(n,\mathbb{Z})$ (44.6-8). | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `IsBravaisEquivalent(R, S)` | `R`, `S`: finite integer matrix groups | `Boolean` | Decide whether `R` and `S` belong to the same Bravais class (i.e., their Bravais groups are $GL(n,\mathbb{Z})$-conjugate). | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `CaratZClass(R)` | `R`: finite integer matrix group | record (CARAT Z-class data) | Return the CARAT Z-class object for `R` (conjugacy class in $GL(n,\mathbb{Z})$). | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `CaratZClassNumber(R)` | `R`: finite integer matrix group | integer (CARAT Z-class index) | Return the CARAT Z-class index/number for `R`. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `CaratQClass(R)` | `R`: finite integer matrix group | record (CARAT Q-class data) | Return the CARAT Q-class object for `R` (conjugacy class in $GL(n,\mathbb{Q})$). | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `CaratQClassNumber(R)` | `R`: finite integer matrix group | integer (CARAT Q-class index) | Return the CARAT Q-class index/number for `R`. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `RationalClassesMaximalSubgroups(R)` | `R`: finite integer matrix group | list of integer matrix groups | Return representatives of maximal-subgroup classes across rational ($GL(n,\mathbb{Q})$) conjugacy classes for `R`. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `ZClassRepsQClass(R)` | `R`: finite integer matrix group | list of integer matrix groups | Return representative groups for all $\mathbb{Z}$-conjugacy classes (Z-classes) within the $\mathbb{Q}$-conjugacy class (Q-class) of `R` (44.6-9). | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `MaximalSubgroupsRepresentatives(R)` | `R`: finite integer matrix group | list of integer matrix groups | Return representatives of maximal subgroups of `R`. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `AffineNormalizer(R)` | `R`: finite integer matrix group | affine group (normalizer in affine context) | Compute the affine normalizer of `R` in the crystallographic class context. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `IsCaratZClass(R)` | `R`: any object | `Boolean` | Predicate: whether `R` is a CARAT Z-class record object. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |
| `IsCaratQClass(R)` | `R`: any object | `Boolean` | Predicate: whether `R` is a CARAT Q-class record object. | `[PKG, EUCLID, PD, ZZMOD, GRP]` |

---

## 4. Legacy and Non-Canonical Signature Triage

The following names appear in older/historical materials but are not documented as
current canonical signatures in GAP Reference Chapter 44.6:

- `CrystCatZClass(...)`
- `CrystCatQClass(...)`
- `CrystCatQClasses(...)`

These are tracked as legacy aliases, not canonical active-surface contracts.

The following selectorized CARAT signatures are also treated as non-canonical in this
surface because current GAP reference and CARATInterface docs expose one-argument forms:

- `BravaisGroup(R[, f])`
- `PointGroupsBravaisClass(R[, f[, s]])`
- `BravaisSubgroups(R[, f[, s[, k]]])`
- `BravaisSupergroups(R[, f[, s[, k]]])`
- `NormalizerInGLnZ(R[, f])`
- `CentralizerInGLnZ(R[, f])`

---

## 5. Definiteness and Domain Caveats

- These APIs are crystallographic and integer-matrix-group workflows in Euclidean settings.
- They are not the same contract surface as indefinite arithmetic-lattice genus,
  discriminant-form, or local-global isometry APIs.
- For `SpaceGroupsByPointGroupOnRight(P[, normedQclass[, orbitsQclass]])`:
  `normedQclass` is `false` or a list of normalizer elements in `GL(d,Z)`, and
  `orbitsQclass` is boolean (`true` returns all representatives in each normalizer orbit).
- Optional selector arguments `f`, `s`, and `k` are not retained as active contracts for
  CARAT methods in this surface because no accepted value domains are documented in current
  canonical references for these methods.

---

## 6. Consolidated Method Index

- `AffineCrystGroupOnLeft`
- `AffineCrystGroupOnRight`
- `AffineNormalizer`
- `AsAffineCrystGroupOnRight`
- `BravaisGroup`
- `BravaisSubgroups`
- `BravaisSupergroups`
- `CaratQClass`
- `CaratQClassNumber`
- `CaratZClass`
- `CaratZClassNumber`
- `CentralizerInGLnZ`
- `IsAffineCrystGroupOnRight`
- `IsBravaisEquivalent`
- `IsCaratQClass`
- `IsCaratZClass`
- `MaximalSubgroupsRepresentatives`
- `NormalizerInGLnZ`
- `PointGroup`
- `PointGroupsBravaisClass`
- `RationalClassesMaximalSubgroups`
- `SpaceGroupsByPointGroupOnRight`
- `TranslationsCrystGroup`
- `WyckoffLattice`
- `WyckoffNormalClosure`
- `WyckoffOrbit`
- `WyckoffPositions`
- `ZClassRepsQClass`

---

## Sources

### Core GAP documentation
- Cryst package: https://gap-packages.github.io/cryst/
- CARATInterface: https://gap-packages.github.io/carat/
- CrystCat: https://gap-packages.github.io/crystcat/

### Local upstream snapshots
- Crystallographic packages: `docs/crystallographic_stack/upstream/cryst/`, `docs/crystallographic_stack/upstream/caratinterface/`, `docs/crystallographic_stack/upstream/crystcat/`

---

## References

- `docs/crystallographic_stack_methods_checklist.md`
- `docs/crystallographic_stack/upstream/crystallographic_stack_online_provenance_2026-02-17.md`
- Existing umbrella mapping:
  `docs/gap/lattice/research_readme.md`
- Cryst package page: `https://gap-packages.github.io/cryst/`
- GAP package install index (Cryst/CARATInterface/CrystCat):
  `https://www.math.rwth-aachen.de/~Greg.Gamble/gap4r3/pkg/inst.htm`
- GAP Cryst package manual:
  `https://docs.gap-system.org/pkg/cryst/htm/CHAP002.htm`
- GAP3 Cryst chapter mirror (supporting detail for normalizer/orbit selector semantics):
  `https://webusers.imj-prg.fr/~jean.michel/gap3/htm/chap061.htm`
- GAP Reference Manual (CARAT methods):
  `https://docs.gap-system.org/doc/ref/chap44.html`
- CARATInterface package manual:
  `https://www.math.rwth-aachen.de/~GAP/WWW2/PackagePages/caratinterface/doc/manual.pdf`
