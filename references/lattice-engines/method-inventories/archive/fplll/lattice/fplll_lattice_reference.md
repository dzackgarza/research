# fplll Lattice Reduction Reference
## Core C++/CLI Euclidean lattice algorithms

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[PD]` | Positive-definite Euclidean lattice setting |
| `[ZZMOD]` | Integer basis/Gram matrix model |
| `[RED]` | Reduction algorithms |
| `[ENUM]` | Enumeration search routines |
| `[CLI]` | Command-line front-end |
| `[CPP]` | C++ API surface |

---

## 1. Scope

`fplll` is the core C++ Euclidean-lattice reduction library/toolchain behind `fpylll`.

Primary scope:

- LLL/BKZ/HKZ reduction,
- SVP/CVP-style enumeration backends in Euclidean norm,
- benchmark/instance-oriented CLI workflows.

Not in scope:

- arithmetic indefinite quadratic-form classification,
- genus/classification APIs for integral forms.

---

## 2. CLI Surface

| Command | Canonical synopsis | Notes | Tags |
|---------|--------------------|-------|------|
| `fplll` | `fplll [-a algo] [options] [file]` | Main reduction command; docs list `-a`, `-b`, `-d`, `-e`, `-p`, `-m`, `-z` among core options. | `[CLI, RED, PD]` |
| `bkz` | `bkz [options] [file]` | BKZ command-line driver. | `[CLI, RED, PD]` |
| `hkz` | `hkz [options] [file]` | HKZ reduction driver. | `[CLI, RED, PD]` |
| `svp` | `svp [options] [file]` | Shortest-vector command-line driver. | `[CLI, ENUM, PD]` |

Key documented option meanings on the main command page:

- `-a`: select reduction algorithm,
- `-b`: BKZ block size,
- `-d` / `-e`: Lovasz and size-reduction parameters,
- `-p`: floating-point precision,
- `-m`: floating-point backend,
- `-z`: pruning strategy.

---

## 3. Core C++ APIs

### 3.1 LLL

| API | Description | Tags |
|-----|-------------|------|
| `LLLReduction<ZT, FT>(MatGSOInterface<ZT, FT>& m, double delta, double eta, int flags)` | Stateful LLL reducer over a GSO matrix interface. | `[CPP, RED, PD]` |
| `LLLReduction::lll(int kappa_min=0, int kappa_start=0, int kappa_end=-1, int size_reduction_start=0)` | Main LLL execution entry point. | `[CPP, RED, PD]` |
| `LLLReduction::size_reduction(int kappa_min=0, int kappa_end=-1, int size_reduction_end=-1, int y=0)` | Size-reduction phase helper. | `[CPP, RED, PD]` |
| `LLLReduction::lovasz_tests(int kappa, int kappa_max)` | Lovasz-condition test routine. | `[CPP, RED, PD]` |
| `LLLReduction::swap(int kappa, int kappa_max=-1)` | Basis-vector swap routine used by LLL flow. | `[CPP, RED, PD]` |

### 3.2 BKZ

| API | Description | Tags |
|-----|-------------|------|
| `BKZParam(int block_size, ..., double delta=LLL_DEF_DELTA, int flags=BKZ_DEFAULT, int max_loops=0, double max_time=0, ...)` | BKZ parameter object with block size and control options. | `[CPP, RED, PD]` |
| `BKZReduction<ZT, FT>(MatGSOInterface<ZT, FT>& mat_gso, LLLReduction<ZT, FT>& lll_obj, const BKZParam& param)` | Stateful BKZ reducer. | `[CPP, RED, PD]` |
| `BKZReduction::bkz()` | Run BKZ reduction. | `[CPP, RED, PD]` |
| `BKZReduction::tour(int loop, int param, int min_row, int max_row)` | BKZ tour routine over a row range. | `[CPP, RED, PD]` |
| `BKZReduction::svp_preprocessing(int kappa, unsigned int block_size, const BKZParam& par)` | BKZ SVP preprocessing. | `[CPP, RED, PD]` |
| `BKZReduction::svp_reduction(int kappa, unsigned int block_size, const BKZParam& par, bool dual=false)` | Core BKZ SVP subproblem routine. | `[CPP, RED, PD]` |
| `BKZReduction::rerandomize_block(int min_row, int max_row, int density)` | Block rerandomization helper. | `[CPP, RED, PD]` |

### 3.3 Namespace helpers

| API | Description | Tags |
|-----|-------------|------|
| `lll_reduction(...)` | LLL helper entry point in namespace API. | `[CPP, RED, PD]` |
| `bkz_reduction(...)` | BKZ helper entry point in namespace API. | `[CPP, RED, PD]` |
| `is_lll_reduced(...)` | Predicate for LLL-reduced conditions. | `[CPP, RED, PD]` |

---

## 4. Definiteness and Domain Caveat

`fplll` is a Euclidean-lattice algorithm stack. It does not provide arithmetic indefinite-form classification semantics.

---

## 5. Sources

- fplll docs home: `https://fplll.github.io/fplll/`
- Main command/options page: `https://fplll.github.io/fplll/`
- `fplll` command page: `https://fplll.github.io/fplll/fplll_8h.html`
- `bkz` command page: `https://fplll.github.io/fplll/bkz_8h.html`
- `hkz` command page: `https://fplll.github.io/fplll/hkz_8h.html`
- `svp` command page: `https://fplll.github.io/fplll/svp_8h.html`
- `LLLReduction` C++ class page: `https://fplll.github.io/fplll/classLLLReduction.html`
- `BKZParam` C++ class page: `https://fplll.github.io/fplll/classBKZParam.html`
- `BKZReduction` C++ class page: `https://fplll.github.io/fplll/classBKZReduction.html`
- fplll repository: `https://github.com/fplll/fplll`
