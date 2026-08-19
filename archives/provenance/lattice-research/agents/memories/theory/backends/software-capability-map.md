# Open-Source Mathematical Software Capability Map

This is the routing map for mathematical implementation work. It answers one question:
before writing new code, what mature open-source system should we wire?

## General software discovery

Before any nontrivial implementation — whether code or audit — check
[EasyBuild's supported software list](https://docs.easybuild.io/version-specific/supported-software/)
to see if the needed functionality already exists as a packaged open-source tool.
Many mathematical, scientific, and HPC libraries are listed there. If it's on that page,
you can likely wire it rather than build it. In audits, flag complex implementations
that could be offloaded to a tool from this list; consider replacing them.

## Invariant

Do not implement mathematical algorithms locally when a mature open-source exact system
already implements the relevant operation.

Implementation work should normally add:

- a semantic method on the repo's mathematical noun;
- a thin bridge to the external system;
- conversion and validation at the boundary;
- source-backed tests for the mathematical result.

It should not add a new local algorithm unless a documented backend-gap research card
has concluded that no suitable mature open-source implementation exists and the user has
approved bespoke implementation.

## Required reading order

For any mathematical implementation card:

- Read this file.
- Read `theory/backends/library-integration` for current Coble/lattice task routing.
- Read `theory/backends/abstract-to-external-mapping` for method-to-tool mappings.
- Read the specific backend note for the selected tool.
- If the source or theorem basis is uncertain, use `research-source-acquisition` before implementation.

## Preferred systems

Use open-source exact systems. Preferred candidates include:

| Domain | Preferred systems | Repo notes |
| --- | --- | --- |
| General orchestration and Sage categories | SageMath | Use Sage as the orchestration layer when it cleanly exposes GAP, Singular, PARI/GP, or native category machinery. |
| Finite groups, group actions, orbits, stabilizers | GAP and GAP packages | See `gap-orbits.md`. Prefer GAP over custom orbit enumeration. |
| Polynomial ideals, Groebner methods, singularities, local algebra, normalization | Singular through Sage or direct bridge | Use Singular for commutative-algebra kernels rather than local polynomial algorithms. |
| Algebraic geometry, sheaves, Hilbert polynomials, divisors, blowups | Macaulay2 and relevant packages | See `abstract-to-external-mapping.md` and `comprehensive-tool-docs.md`; verify current package support before wiring. |
| Lattices, quadratic forms, number theory, exact algebra | Oscar.jl, Hecke, Nemo, AbstractAlgebra.jl | See `oscar-lattices.md`; prefer Oscar/Hecke for supported lattice and discriminant computations. |
| Indefinite lattice isometry and orbit computations | Indefinite.jl | See `indefinite-jl.md`; do not force CARAT into indefinite-form work. |
| Positive-definite form automorphisms and finite matrix-group auxiliary work | CARAT | See `carat.md`; respect positive-definite and finite-group limitations. |
| Number theory and exact arithmetic kernels | PARI/GP, FLINT, Arb, Nemo, Sage wrappers | Prefer established kernels through Sage or Julia rather than hand arithmetic. |
| Polyhedra, cones, toric and combinatorial geometry | polymake, Normaliz, Sage wrappers, Oscar integration candidates | Treat as candidate routing; audit current docs before implementation. |
| Formal theorem lookup or proof reuse | Lean/mathlib through Aristotle when needed | Check upstream theorem availability before spending proof or implementation effort. |

Excluded as repo dependencies unless explicitly authorized:

- Magma
- Mathematica/Wolfram
- MATLAB
- closed hosted computational services

These may be mentioned as literature or comparison points, but they are not the default
execution substrate for repo code.

## Routing statuses

Use these labels in plans, cards, and backend notes:

| Status | Meaning | Next action |
| --- | --- | --- |
| `preferred-backend` | We know the mature backend and the intended bridge. | Implement adapter or use existing wrapper. |
| `bridge-needed` | Backend capability exists, but repo wiring is missing or too rough. | Build the bridge, not the mathematics. |
| `candidate-backend` | Backend likely exists, but docs/source still need audit. | File or execute backend research before implementation. |
| `true-gap` | Documented research found no suitable mature open-source implementation. | Ask user before bespoke implementation. |
| `out-of-scope` | Capability is unavailable, proprietary-only, or not needed for current repo goals. | Do not implement in the current task. |

## Gap protocol

When an implementation task reaches an undocumented mathematical operation:

- Stop implementation.
- Do not add an ad hoc helper.
- Create or update a tracked research card.
- Record the exact operation, mathematical objects, candidate software, sources checked,
  and why the current work is blocked.
- Resume implementation only after the card establishes a routing decision.

The research card is not bureaucracy. It prevents poisoning downstream mathematical code
with local algorithms that should have been mature backend calls.

## Backend note format

Each backend or domain note should state:

- Mathematical operations supported.
- Exact source docs reviewed.
- Known limitations and input restrictions.
- Preferred bridge path from repo code.
- Native test or verification surface.
- Examples of repo operations that should route there.
- Routing status for unresolved capabilities.

## Current backend notes

- `abstract-to-external-mapping`: method-to-tool mapping for existing abstract surfaces.
- `library-integration`: current Coble/lattice task routing to mature libraries.
- `comprehensive-tool-docs`: extracted upstream tool documentation used by old mapping work.
- `oscar-lattices`: Oscar/Hecke lattice and quadratic-form capabilities.
- `gap-orbits`: GAP group-action, orbit, and stabilizer workflows.
- `carat`: CARAT capability audit and positive-definite limitations.
- `indefinite-jl`: indefinite lattice isometry/orbit backend notes.
- `buildings`: buildings.sage capability notes.
- `vinberg-algorithm`: Vinberg-specific algorithm and backend guidance.

## Updating this map

Update this file when:

- a new mathematical domain enters the spec tree;
- a backend-gap research card resolves;
- a preferred backend changes;
- a limitation is discovered that affects task routing;
- a bespoke implementation is approved because a true open-source gap was established.

Do not leave routing decisions only in chat, commit messages, or isolated task cards.
