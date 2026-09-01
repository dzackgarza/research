# Contribution Guidelines and Policy Index

This document defines the contribution policies for the repository.
All contributions must follow the categorized policy index below.
Each policy has a unique alphanumeric identifier.

* * *

## Policy Index

### 1. Mathematical Architecture & Ownership (`ARC-*`)

#### `ARC-01`: Own Universal Properties and Categories Natively

- **Rule**: Define mathematical categories, morphisms, functors, adjunctions, and universal constructions natively in the repository category framework.

- **Rationale**: Categories and universal properties establish the semantic mathematical foundation.
  They provide consistent compositional behavior across modules.

- **Violation Example**: Defining an ideal or basis as an isolated tuple or matrix operation without an underlying category, module, or algebra structure.

#### `ARC-02`: Morphism-Centric Subobjects and Witness Placement

- **Rule**: Represent subobjects as pairs $(S, \iota: S \hookrightarrow M)$.
  Place predicates, isometries, embeddings, and containment checks on morphism spaces or hom-sets.

- **Rationale**: Mathematical invariants depend on the embedding morphism, not on presentation-dependent coordinate choices.

- **Violation Example**: Storing ambient coordinates or adding `ambient=` parameters directly to parent objects.

#### `ARC-03`: Build Structural Objects Before Downstream Numerical Invariants

- **Rule**: Never bypass an intermediate mathematical object or functorial stage (such as the localized module $M_{\mathfrak{p}} = M \otimes_R R_{\mathfrak{p}}$, base-changed algebras $K \otimes_R \mathcal{O}$, or derived complexes) to compute a single numerical scalar or pointwise fiber (such as $\dim_{\kappa(\mathfrak{p})}(M \otimes_R \kappa(\mathfrak{p}))$). Always construct the foundational parent object and base-change/localization functor first; derive pointwise invariants as generic operations on the resulting object.

- **Rationale**: Bypassing structural objects destroys mathematical compression and composability.
  When the structural object exists ($M_{\mathfrak{p}}$ as an $R_{\mathfrak{p}}$-module), all local invariants (rank, minimal generators, local torsion, localization of morphisms) become generic consequences of base change.
  Skipping to point queries forces every downstream invariant to reinvent ad-hoc algorithmic logic.

- **Violation Example**: Implementing `local_number_of_generators(p)` by evaluating the residue field vector-space dimension $M \otimes_R \kappa(\mathfrak{p})$ while the localized module $M_{\mathfrak{p}}$ over the local ring $R_{\mathfrak{p}}$ remains absent from the category layer.

#### `ARC-04`: Owned Objects Over Interchangeable Computational Services

- **Rule**: Mathematical objects, morphisms, categories, subobjects, universal properties, and functors are owned.
  Sage/Singular/GAP/OSCAR/M2/etc.
  are interchangeable computational services behind those objects.
  No CAS-specific category membership should be needed to state what an object is.

- **Rationale**: The owned category graph is the single surface for stating what an object is.
  A computational engine only supplies computations behind that surface, so the engine choice never enters the statement of the mathematics, and engines remain swappable.

- **Violation Example**: Requiring a CAS-specific category membership or class (Sage, Singular, GAP, OSCAR, or Macaulay2-specific) to state, construct, or identify an object.

* * *

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

#### `ENG-03`: Minimal Owned Computation and Ecosystem Offloading

- **Rule**: Keep owned algorithmic logic strictly minimal.
  Always offload engine computations to established computational backends:

  - Upstream SageMath native modules

  - Heavy Python libraries (`networkx`, `numpy`, `scipy`)

  - Julia / OSCAR / Hecke (routed via `sage_julia_bridge`)

  - GAP (routed via `libgap`)

  - Singular, Macaulay2, Maxima, and PARI/GP

- **Rationale**: The preamble owns categorical representations, universal properties, and mathematical structures.
  Concrete computations belong to dedicated, verified engines.

- **Violation Example**: Writing custom graph connectivity or automorphism algorithms instead of delegating to `networkx` or Sage graph backends.

#### `ENG-04`: Native Engine Implementation with Preamble Category Wrappers

- **Rule**: When an algorithm requires multi-step engine computations, implement the engine logic directly in the target engine language (such as Julia/OSCAR or Singular) and wrap it with preamble category interfaces, whenever this reduces complexity or eliminates excessive cross-bridge data transport.

- **Rationale**: Executes compute-heavy algebra natively in the host engine while exposing a uniform categorical interface to Sage sessions.

- **Violation Example**: Transporting intermediate matrices back and forth across a language bridge in a loop when one native Julia routine can perform the reduction and return the final invariant.

* * *

### 3. Interoperability & Bridge Boundaries (`BRG-*`)

#### `BRG-01`: Structured Engine Bridges Over Ad-Hoc Shelling

- **Rule**: Route communication with external systems (such as Julia, OSCAR, or Macaulay2) through persistent bridge interfaces (`sage_julia_bridge`, `JuliaHandle`, or C-APIs).

- **Rationale**: Shelling out via subprocesses with temporary disk files causes process overhead, unmanaged temporary state, and fragile error handling.

- **Violation Example**: Using `subprocess.run(["julia", "script.jl", tmp_file])` inside an inner loop instead of calling a persistent `JuliaHandle`.

#### `BRG-02`: Explicit Mathematical Interface Boundaries

- **Rule**: Translate data explicitly across bridge boundaries.
  Validate input types and convert results into owned repository types immediately upon return.

- **Rationale**: Keeps engine-specific representation leaks out of the public category API.

- **Violation Example**: Leaking raw engine pointers or un-wrapped backend matrix wrappers into user-facing category elements.

* * *

### 4. Environment, Execution & Tooling (`ENV-*`)

#### `ENV-01`: Strict Physical Path Resolution for Commands

- **Rule**: Use exact physical filesystem paths (such as `/home/dzack/research`) for shell commands, execution targets, and subprocess invocations.

- **Rationale**: Virtual mount aliases (such as `/research`) fail in standard POSIX shells and background tasks.

- **Violation Example**: Passing virtual root `/research` to a shell execution tool.

#### `ENV-02`: Deterministic Recipe Execution via Justfile

- **Rule**: Declare all project orchestration, gates, and documentation generators in the root [`justfile`](justfile).

- **Rationale**: Ensures reproducible execution across developer environments, CI pipelines, and automation tools.

- **Violation Example**: Running undocumented one-off ad-hoc bash scripts for builds or tests.

* * *

### 5. Development Discipline & Verification (`DEV-*`)

#### `DEV-01`: Strict Typing Without Opaque Types

- **Rule**: Type all public functions, methods, and classes explicitly.
  Do not use `Any`, `object`, `unknown`, or silent type ignores.

- **Rationale**: Types communicate mathematical intent and enable static correctness checks.

- **Violation Example**: Annotating a morphism constructor with `def __init__(self, data: Any) -> object:`.

#### `DEV-02`: Specimen-First Falsification Discipline

- **Rule**: Accompany every new category, functor, or operation with a concrete, falsifiable mathematical specimen.

- **Rationale**: Progress is measured by mathematical specimens that can fail, not by uninstantiated schemas.

- **Violation Example**: Adding abstract category definitions without a test specimen or executable verification.

#### `DEV-03`: Consult Megadoc, Reuse Constructions, and Implement at Maximal Generality

- **Rule**: Always consult the preamble megadoc (`just preamble-megadoc`) before adding code.
  Always reuse existing constructions when they are mathematically correct and principled.
  When a required construction does not exist, implement it at its most mathematically general level (in its native abstract category or module layer) and progressively specialize and share it across concrete domains.

- **Rationale**: Prevents duplicate definitions, competing APIs, and siloed mathematical implementations while ensuring global functorial coherence.

- **Violation Example**: Implementing an ad-hoc direct sum or orthogonal quotient exclusively for lattices without connecting to the general module or categorical construction.

#### `DEV-04`: Real Sets Over Manual Deduplication

- **Rule**: Never manually use "iterate + seen" patterns to deduplicate. Always form actual sets, usually a one-liner with a comprehension, or map/filter/reduce equivalents.

- **Rationale**: Forming a set states the mathematical operation — the collection, its membership, its cardinality — in one expression. A hand-written "seen" loop re-implements set semantics silently, hiding the operation and inviting order- and mutability-dependent bugs.

- **Violation Example**: Accumulating into a `seen` list with `if x not in seen` inside a loop instead of writing `set(xs)` or a set comprehension.

* * *

## Detailed Documentation References

For in-depth guides and stylistic standards, see the documentation book:

- **Contribution Workflow**: [`docs/contributing/Contribution-Guidelines.md`](docs/contributing/Contribution-Guidelines.md)

- **Categorical Principles**: [`docs/contributing/Categorical-Presentation-Principles.md`](docs/contributing/Categorical-Presentation-Principles.md)

- **Mathematical Style Guide**: [`docs/contributing/Mathematical-Language-Style-Guide.md`](docs/contributing/Mathematical-Language-Style-Guide.md)

- **Design Hazards Ledger**: [`docs/contributing/Design-Hazard-Ledger.md`](docs/contributing/Design-Hazard-Ledger.md)

- **Mathematical Lexicon**: [`docs/contributing/Mathematical-Lexicon.md`](docs/contributing/Mathematical-Lexicon.md)
