# TOPCOM Lattice Method Reference
## Triangulations of point configurations and oriented matroids

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[CLI]` | Command-line interface command |
| `[TRI]` | Triangulation construction/enumeration |
| `[OM]` | Oriented-matroid/chirotope surface |
| `[SYM]` | Symmetry-aware enumeration |
| `[SEC]` | Secondary-polytope / flip-graph workflow |

---

## 1. Scope

TOPCOM is a command-line package for triangulations of point configurations and oriented matroids, with symmetry-aware enumeration, regularity checks, and secondary-polytope related computations.

Primary surfaces in scope:

- point-configuration to triangulation command families (`points2*`),
- oriented-matroid/chirotope command families (`chiro2*`),
- full and symmetry-reduced enumeration of (fine/regular/unimodular) triangulations,
- conversion and helper commands (circuits, cocircuits, duals, random generators).

Not in scope:

- indefinite quadratic-form genus mass/isometry classification.

---

## 2. Input/Output Contracts

### 2.1 Input model

| Contract | Source-backed statement |
|----------|-------------------------|
| Point configuration input | Commands in the `points2*` family read point configurations from standard input; outputs are written to standard output. |
| Matrix convention | Input is treated as an `n x d` matrix; for homogenized input the first row consists of all ones. |
| Chirotope input | Commands in the `chiro2*` family operate on chirotopes/oriented-matroid data and support matrix/chirotope-string pathways. |

### 2.2 Type/assumption constraints

| Constraint | Source-backed statement |
|-----------|-------------------------|
| Arithmetic domain | Workflow is combinatorial/polyhedral over finite point configurations and oriented matroids. |
| Output domain | Outputs represent triangulations, circuit/cocircuit data, regularity/flip information, and related polyhedral invariants. |
| Lattice-method caveat | These APIs are lattice-polytope triangulation tools, not arithmetic-lattice genus/isometry methods. |

---

## 3. Command Surfaces

### 3.1 Point/Chirotope conversion and oriented-matroid primitives

| Command | Argument surface | Description | Tags |
|---------|------------------|-------------|------|
| `points2chiro` | `points2chiro [options]` | Compute chirotope data from point-configuration input. | `[CLI, OM]` |
| `chiro2dual` | `chiro2dual [options]` | Construct dual chirotope/oriented-matroid representation. | `[CLI, OM]` |
| `points2circuits` | `points2circuits [options]` | Compute circuits of the input point configuration. | `[CLI, OM]` |
| `chiro2circuits` | `chiro2circuits [options]` | Compute circuits from chirotope input. | `[CLI, OM]` |
| `points2cocircuits` | `points2cocircuits [options]` | Compute cocircuits of point-configuration input. | `[CLI, OM]` |
| `chiro2cocircuits` | `chiro2cocircuits [options]` | Compute cocircuits from chirotope input. | `[CLI, OM]` |

### 3.2 Seed triangulation commands

| Command | Argument surface | Description | Tags |
|---------|------------------|-------------|------|
| `points2triangs` | `points2triangs [options]` | Generate one seed triangulation from points. | `[CLI, TRI]` |
| `chiro2triangs` | `chiro2triangs [options]` | Generate one seed triangulation from chirotope input. | `[CLI, TRI, OM]` |
| `points2ntriangs` | `points2ntriangs [options]` | Seed triangulation in non-symmetric style. | `[CLI, TRI, SYM]` |
| `chiro2ntriangs` | `chiro2ntriangs [options]` | Chirotope variant of non-symmetric seed triangulation. | `[CLI, TRI, OM, SYM]` |
| `points2finetriang` | `points2finetriang [options]` | One seed fine triangulation from points. | `[CLI, TRI]` |
| `chiro2finetriang` | `chiro2finetriang [options]` | One seed fine triangulation from chirotope input. | `[CLI, TRI, OM]` |
| `points2nfinetriang` | `points2nfinetriang [options]` | Non-symmetric seed fine triangulation from points. | `[CLI, TRI, SYM]` |
| `chiro2nfinetriang` | `chiro2nfinetriang [options]` | Non-symmetric seed fine triangulation from chirotope input. | `[CLI, TRI, OM, SYM]` |

### 3.3 Full triangulation enumeration and flip graph

| Command | Argument surface | Description | Tags |
|---------|------------------|-------------|------|
| `points2alltriangs` | `points2alltriangs [options]` | Enumerate all triangulations of a point configuration. | `[CLI, TRI]` |
| `chiro2alltriangs` | `chiro2alltriangs [options]` | Enumerate all triangulations from chirotope input. | `[CLI, TRI, OM]` |
| `points2allfinetriangs` | `points2allfinetriangs [options]` | Enumerate all fine triangulations. | `[CLI, TRI]` |
| `chiro2allfinetriangs` | `chiro2allfinetriangs [options]` | Chirotope variant of all-fine-triangulations enumeration. | `[CLI, TRI, OM]` |
| `points2nalltriangs` | `points2nalltriangs [options]` | Enumerate all triangulations in non-symmetric mode. | `[CLI, TRI, SYM]` |
| `chiro2nalltriangs` | `chiro2nalltriangs [options]` | Chirotope variant of non-symmetric all-triangulations enumeration. | `[CLI, TRI, OM, SYM]` |
| `points2nallfinetriangs` | `points2nallfinetriangs [options]` | Non-symmetric all-fine-triangulations enumeration. | `[CLI, TRI, SYM]` |
| `chiro2nallfinetriangs` | `chiro2nallfinetriangs [options]` | Chirotope variant of non-symmetric all-fine-triangulations enumeration. | `[CLI, TRI, OM, SYM]` |
| `points2flips` | `points2flips [options]` | Enumerate/store flips between triangulations (flip graph surface). | `[CLI, TRI, SEC]` |
| `chiro2flips` | `chiro2flips [options]` | Chirotope variant of flip-graph enumeration. | `[CLI, TRI, OM, SEC]` |

### 3.4 Secondary-polytope and helper utilities

| Command | Argument surface | Description | Tags |
|---------|------------------|-------------|------|
| `points2facets` | `points2facets [options]` | Facet-related computations for secondary-polytope workflows. | `[CLI, SEC]` |
| `points2volume` | `points2volume [options]` | Volume-related computation for point-configuration triangulation contexts. | `[CLI, TRI]` |
| `points2nvolume` | `points2nvolume [options]` | Non-symmetric variant of volume-related computation. | `[CLI, TRI, SYM]` |
| `points2placingtriang` | `points2placingtriang [options]` | Compute placing triangulation for point input. | `[CLI, TRI]` |
| `points2symmetries` | `points2symmetries [options]` | Compute symmetry information of point configurations. | `[CLI, SYM]` |
| `checkregularity` | `checkregularity [options]` | Check whether triangulation input is regular. | `[CLI, TRI]` |
| `allfinetriangs2subdivs` | `allfinetriangs2subdivs [options]` | Convert all-fine-triangulation output into subdivision data. | `[CLI, TRI]` |
| `gen_points` | `gen_points [options]` | Random/synthetic point-configuration generator. | `[CLI]` |
| `gen_chiro` | `gen_chiro [options]` | Random/synthetic chirotope generator. | `[CLI, OM]` |

---

## 4. Common Option Surface (Cross-command)

| Option | Argument/type surface | Source-backed semantics |
|--------|-----------------------|-------------------------|
| `--regular` | boolean flag | Restrict to regular triangulations. |
| `--nonregular` | boolean flag | Restrict to nonregular triangulations. |
| `--unimodular` | boolean flag | Restrict to unimodular triangulations. |
| `--reducepoints` | boolean flag | Reduce points modulo symmetry before triangulation enumeration. |
| `--noinsertion` | boolean flag | Use faster implementation variant that omits insertion checks. |
| `--heights` | string/list argument | Provides lifting heights used for regular triangulation pathways. |
| `--flipdeficiency` | integer argument | Set maximal deficiency parameter in flip generation behavior. |
| `--checktriang` | boolean flag | Validate triangulation admissibility before processing. |
| `-i`, `--input-chiro` | boolean flag | Interpret input as chirotope data instead of points. |
| `-v`, `--verbose` | boolean flag | Emit verbose diagnostics/details. |

---

## 5. Domain Caveat

TOPCOM exposes triangulation/oriented-matroid command surfaces for point-configuration combinatorics. It is not a quadratic-form arithmetic/genus/isometry package.

---

## 6. Sources

- TOPCOM project page: `https://www.wm.uni-bayreuth.de/de/team/rambau_joerg/TOPCOM/`
- TOPCOM manual PDF (command and option inventories): `https://www.wm.uni-bayreuth.de/de/team/rambau_joerg/TOPCOM/TOPCOM-manual.pdf`
- TOPCOM command manual mirror (`topcom(7)`, generated from the upstream manual): `https://manpages.debian.org/testing/topcom/topcom.7.en.html`
- Local provenance snapshot: `docs/archive/scope_violations/topcom/upstream/topcom_online_provenance_2026-02-17.md`
