# Contribution Guidelines and Policy Index

This document defines the contribution policies for the repository.
All contributions must follow the categorized policy index below.
Each policy has a unique alphanumeric identifier.

---

## Policy Index

### 1. Mathematical Architecture & Ownership (`ARC-*`)

#### `ARC-01`: Own Universal Properties and Categories Natively
- **Rule**: Define mathematical categories, morphisms, functors, adjunctions, and universal constructions natively in the repository category framework.
- **Rationale**: Categories and universal properties establish the semantic mathematical foundation. They provide consistent compositional behavior across modules.
- **Violation Example**: Defining an ideal or basis as an isolated tuple or matrix operation without an underlying category, module, or algebra structure.

#### `ARC-02`: Morphism-Centric Subobjects and Witness Placement
- **Rule**: Represent subobjects as pairs $(S, \iota: S \hookrightarrow M)$. Place predicates, isometries, embeddings, and containment checks on morphism spaces or hom-sets.
- **Rationale**: Mathematical invariants depend on the embedding morphism, not on presentation-dependent coordinate choices.
- **Violation Example**: Storing ambient coordinates or adding `ambient=` parameters directly to parent objects.

---

### 2. Computational Backend Delegation (`ENG-*`)

#### `ENG-01`: Delegate Heavy Algorithmic Computations to Exact Engines
- **Rule**: Route algorithmic algebra to established exact backends (SageMath, Singular, OSCAR, Macaulay2, PARI/GP) when a reliable implementation exists.
- **Scope**: Gröbner bases, syzygies, primary decompositions, Hilbert series, polynomial reduction, and local algebra computations.
- **Rationale**: Battle-tested engines provide numerical stability, optimized C/C++ implementations, and mathematical verification.
- **Violation Example**: Writing custom Python algorithms for multivariate polynomial division or Gröbner basis calculation.

#### `ENG-02`: Prohibition of Hand-Rolled Standard Mathematics
- **Rule**: Do not hand-roll algorithms or data structures available in mature upstream dependencies or Mathlib.
- **Rationale**: Custom mathematical algorithms create high maintenance overhead and lack formal verification.
- **Violation Example**: Implementing custom Smith Normal Form or LLL reduction instead of delegating to native library routines.

---

### 3. Interoperability & Bridge Boundaries (`BRG-*`)

#### `BRG-01`: Structured Engine Bridges Over Ad-Hoc Shelling
- **Rule**: Route communication with external systems (such as Julia, OSCAR, or Macaulay2) through persistent bridge interfaces (`sage_julia_bridge`, `JuliaHandle`, or C-APIs).
- **Rationale**: Shelling out via subprocesses with temporary disk files causes process overhead, unmanaged temporary state, and fragile error handling.
- **Violation Example**: Using `subprocess.run(["julia", "script.jl", tmp_file])` inside an inner loop instead of calling a persistent `JuliaHandle`.

#### `BRG-02`: Explicit Mathematical Interface Boundaries
- **Rule**: Translate data explicitly across bridge boundaries. Validate input types and convert results into owned repository types immediately upon return.
- **Rationale**: Keeps engine-specific representation leaks out of the public category API.
- **Violation Example**: Leaking raw engine pointers or un-wrapped backend matrix wrappers into user-facing category elements.

---

### 4. Environment, Execution & Tooling (`ENV-*`)

#### `ENV-01`: Strict Physical Path Resolution for Commands
- **Rule**: Use exact physical filesystem paths (such as `/home/dzack/research`) for shell commands, execution targets, and subprocess invocations.
- **Rationale**: Virtual mount aliases (such as `/research`) fail in standard POSIX shells and background tasks.
- **Violation Example**: Passing virtual root `/research` to a shell execution tool.

#### `ENV-02`: Deterministic Recipe Execution via Justfile
- **Rule**: Declare all project orchestration, gates, and documentation generators in the root [`justfile`](justfile).
- **Rationale**: Ensures reproducible execution across developer environments, CI pipelines, and automation tools.
- **Violation Example**: Running undocumented one-off ad-hoc bash scripts for builds or tests.

---

### 5. Development Discipline & Verification (`DEV-*`)

#### `DEV-01`: Strict Typing Without Opaque Types
- **Rule**: Type all public functions, methods, and classes explicitly. Do not use `Any`, `object`, `unknown`, or silent type ignores.
- **Rationale**: Types communicate mathematical intent and enable static correctness checks.
- **Violation Example**: Annotating a morphism constructor with `def __init__(self, data: Any) -> object:`.

#### `DEV-02`: Specimen-First Falsification Discipline
- **Rule**: Accompany every new category, functor, or operation with a concrete, falsifiable mathematical specimen.
- **Rationale**: Progress is measured by mathematical specimens that can fail, not by uninstantiated schemas.
- **Violation Example**: Adding abstract category definitions without a test specimen or executable verification.

---

## Detailed Documentation References

For in-depth guides and stylistic standards, see the documentation book:

- **Contribution Workflow**: [`docs/contributing/Contribution-Guidelines.md`](docs/contributing/Contribution-Guidelines.md)
- **Categorical Principles**: [`docs/contributing/Categorical-Presentation-Principles.md`](docs/contributing/Categorical-Presentation-Principles.md)
- **Mathematical Style Guide**: [`docs/contributing/Mathematical-Language-Style-Guide.md`](docs/contributing/Mathematical-Language-Style-Guide.md)
- **Design Hazards Ledger**: [`docs/contributing/Design-Hazard-Ledger.md`](docs/contributing/Design-Hazard-Ledger.md)
- **Mathematical Lexicon**: [`docs/contributing/Mathematical-Lexicon.md`](docs/contributing/Mathematical-Lexicon.md)
