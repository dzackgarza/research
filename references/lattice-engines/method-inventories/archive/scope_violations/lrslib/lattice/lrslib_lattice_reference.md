# lrslib Lattice Method Reference
## Reverse-search polyhedral and lattice-point command surfaces

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[CLI]` | Command-line interface |
| `[POLY]` | Polyhedral H/V representation workflow |
| `[ENUM]` | Vertex/ray/facet/lattice-point enumeration surface |
| `[PAR]` | Parallel/distributed enumeration |
| `[NASH]` | Nash-equilibrium command family |

---

## 1. Scope

`lrslib` implements reverse-search algorithms over rational polyhedra and related combinatorial objects. The documented command surface includes:

- H-representation to V-representation conversion and the reverse direction,
- redundancy removal/minimal representation drivers,
- parallel reverse-search enumeration,
- equilibrium-specific enumeration drivers (`lrsnash`, `nash`, `2nash`),
- helper conversion and script tooling (`xref`/`hvref`, `polyv`, `lrsscripts`).

Not in scope:

- indefinite quadratic-form genus/discriminant/isometry classification APIs.

---

## 2. Core Driver Commands

| Command | Synopsis | Contract | Tags |
|---|---|---|---|
| `lrs` | `lrs [input-file]` | Enumerates vertices/rays from inequalities or facets from vertices/rays using exact arithmetic reverse search. | `[CLI, POLY, ENUM]` |
| `mplrs` | `mplrs [options] input output` | Parallel/distributed reverse-search wrapper for `lrs` jobs. | `[CLI, POLY, ENUM, PAR]` |
| `redund` | `redund [input-file]` | Removes redundant inequalities in H-representation inputs. | `[CLI, POLY]` |
| `minrep` | `minrep [input-file]` | Produces a minimal V-representation by removing redundant generators. | `[CLI, POLY]` |
| `lrsnash` | `lrsnash [input-file]` | Enumerates all equilibria from bimatrix-game inputs via reverse-search pathways. | `[CLI, ENUM, NASH]` |
| `nash` | `nash [input-file]` | Wrapper/driver variant within the same equilibrium family. | `[CLI, ENUM, NASH]` |
| `2nash` | `2nash [input-file]` | Two-player specific driver in the equilibrium toolchain. | `[CLI, ENUM, NASH]` |
| `fel` | `fel [input-file] [output-file]` | Finds all feasible labels for game/polytopal labeling workflows. | `[CLI, ENUM, NASH]` |
| `xref` | `xref [input-file [output-file]]` | Converts cddlib-style H/V format to lrs input format while preserving linearity data. | `[CLI, POLY]` |
| `hvref` | `hvref [input-file [output-file]]` | Converts lrs input format to cddlib-style format. | `[CLI, POLY]` |
| `polyv` | `polyv [flags] [input-file [output-file]]` | Produces random V/H polytope instances for benchmarking/testing reverse-search workflows. | `[CLI, POLY, ENUM]` |

---

## 3. `lrs` Option and Keyword Surface

`lrs` consumes keyword-style options in input command sections; these affect arithmetic backend, objective workflows, output depth, and restart behavior.

### 3.1 Arithmetic and optimization controls

| Surface | Argument contract | Description | Tags |
|---|---|---|---|
| `arithmetic in|mp|lr|gmp|flint|hybrid` | discrete backend selector | Selects integer/rational arithmetic backend (`in`, `mp`, `lr`) and optional GMP/FLINT/hybrid pathways where enabled. | `[CLI, POLY]` |
| `maximize` / `minimize` | objective row in input data | Enables LP objective optimization pathway for the loaded instance. | `[CLI, POLY]` |
| `bound x` | `x` numeric bound | Bounds objective search in optimization mode. | `[CLI, POLY]` |
| `nonnegative` | none | Adds nonnegativity assumptions (`x_i >= 0`) for modeling workflows that require this cone convention. | `[CLI, POLY]` |

### 3.2 Representation and projection controls

| Surface | Argument contract | Description | Tags |
|---|---|---|---|
| `redund <list>` | index list | Restricts/targets redundancy processing by index. | `[CLI, POLY]` |
| `minrep` | none | Requests minimal representation output. | `[CLI, POLY]` |
| `project <list>` | index list | Projects to selected variable coordinates. | `[CLI, POLY]` |
| `eliminate <list>` | index list | Eliminates selected columns/variables from output workflow. | `[CLI, POLY]` |
| `extract <list>` | index list | Extracts selected rows/cobases from output workflow. | `[CLI, POLY]` |
| `truncate <list>` | index list | Truncates selected structures in search/output. | `[CLI, POLY]` |

### 3.3 Enumeration/output controls

| Surface | Argument contract | Description | Tags |
|---|---|---|---|
| `volume` | none | Computes simplex/volume-related output during enumeration where supported by the instance type. | `[CLI, POLY, ENUM]` |
| `voronoi` | none | Enables Voronoi-diagram style output mode. | `[CLI, POLY, ENUM]` |
| `allbases` | none | Enumerates all bases/cobases rather than default subset output. | `[CLI, POLY, ENUM]` |
| `printcobasis` | none | Prints cobasis information in output stream. | `[CLI, POLY]` |
| `printslack` | none | Prints slack-vector information in output stream. | `[CLI, POLY]` |
| `maxoutput n` | integer `n` | Stops output after `n` objects. | `[CLI, POLY, ENUM]` |
| `maxcobases n` | integer `n` | Stops after `n` cobases. | `[CLI, POLY, ENUM]` |
| `prune` | none | Enables pruning strategy controls in reverse search. | `[CLI, POLY, ENUM]` |
| `verbose` | none | Emits additional diagnostics/progress text. | `[CLI]` |
| `time_estimate m` | integer `m` | Requests estimation output over `m` sampled nodes/subproblems. | `[CLI, ENUM]` |

### 3.4 Restart and reproducibility controls

| Surface | Argument contract | Description | Tags |
|---|---|---|---|
| `restart n` | integer `n` | Restart from saved reverse-search state index `n`. | `[CLI, ENUM]` |
| `restartp n` | integer `n` | Parallel-compatible restart variant. | `[CLI, ENUM, PAR]` |
| `seed n` | integer `n` | Sets pseudo-random seed for randomized pathways. | `[CLI, ENUM]` |

---

## 4. `mplrs` Parallel Controls

| Option | Argument type | Description | Tags |
|---|---|---|---|
| `-processes n` | integer | Number of worker processes. | `[CLI, PAR]` |
| `-scale n` | integer | Work-scaling factor for decomposition. | `[CLI, PAR]` |
| `-maxtreesize n` | integer | Maximum subtree size before splitting decisions. | `[CLI, PAR]` |
| `-maxdepth n` | integer | Maximum search depth per job. | `[CLI, PAR]` |
| `-mindepth n` | integer | Minimum depth before split/export. | `[CLI, PAR]` |
| `-checkfrequency n` | integer | Frequency for status/checkpoint checks. | `[CLI, PAR]` |
| `-stop n` | integer | Stop after processing threshold `n`. | `[CLI, PAR]` |
| `-estimatelimit n` | integer | Node/time limit for estimation phase. | `[CLI, PAR]` |
| `-cache n` | integer | Cache size control for worker scheduling. | `[CLI, PAR]` |

---

## 5. Helper Conversion and Script Surfaces

### 5.1 Conversion helpers

- `xref` and `hvref` are format-conversion boundaries between lrs and cdd/cddlib textual formats.
- This conversion boundary is relevant when cross-validating with `cddlib`, `CddInterface`, and other H/V-stack tooling.

### 5.2 `polyv` generation controls

`polyv` accepts a compact flag syntax for random instance generation and output style, including:

- `-L#`, `-M#`, `-l#`, `-m#`, `-q#`, `-S#`, `-s#`, and representation-style flags (`-r` / `-h`),
- with optional input/output file paths.

### 5.3 `lrsscripts`

Manpage-documented command set:

- `projred`, `mfel`, `mlrs`, `tlrs`, `plotV`, `plotR`, `plotL`.

These scripts orchestrate common preprocessing/reduction/plotting pipelines around the core `lrs` engines.

---

## 6. Assumptions and Constraints

- Input data is expected in lrs/cdd-style rational H/V formats with command blocks understood by the corresponding driver.
- Arithmetic backend availability (`gmp`, `flint`, `hybrid`) is build-dependent.
- `volume`/enumeration-style options apply to suitable polyhedral instance classes; malformed or incompatible data must be treated as out-of-contract inputs.

---

## 7. Sources

- lrslib package and user guide index: `https://cgm.cs.mcgill.ca/~avis/C/lrslib/USERGUIDE.html`
- lrslib package page: `https://cgm.cs.mcgill.ca/~avis/C/lrslib/lrslib.html`
- `lrs` man page: `https://cgm.cs.mcgill.ca/~avis/C/lrslib/man/man1/lrs.1`
- `mplrs` man page: `https://cgm.cs.mcgill.ca/~avis/C/lrslib/man/man1/mplrs.1`
- `lrsnash` man page: `https://cgm.cs.mcgill.ca/~avis/C/lrslib/man/man1/lrsnash.1`
- `fel` man page: `https://cgm.cs.mcgill.ca/~avis/C/lrslib/man/man1/fel.1`
- `polyv` man page mirror: `https://www.mankier.com/1/polyv`
- `xref`/`hvref` man page mirror: `https://manpages.debian.org/testing/lrslib/xref.1.en.html`
- `lrsscripts` man page mirror: `https://www.mankier.com/1/lrsscripts`
- local provenance snapshot: `docs/archive/scope_violations/lrslib/upstream/lrslib_online_provenance_2026-02-17.md`
