---
name: research-software-wiring
description: Use before mathematical implementation work, backend integration, exact algorithm work, or tests that encode mathematical computation, especially when deciding whether to wire Sage, GAP, Singular, Macaulay2, Oscar/Julia, CARAT, or another open-source system instead of writing bespoke code.
---

# Research Software Wiring

This skill enforces the repo's existing-software-first policy for mathematical
implementation.

## Core policy

- Prefer wiring mature open-source mathematical software over writing new mathematical code.
- Bespoke implementation is a last resort, not the default.
- A missing wrapper is not evidence of a missing algorithm.
- A failed quick search is not evidence that all mature software lacks the capability.
- If no preferred wiring is documented, mark implementation blocked and create source-backed research work.
- Do not depend on proprietary systems such as Magma, Mathematica/Wolfram, MATLAB, or closed hosted services unless the user explicitly asks for non-repo exploratory comparison.
- Before any nontrivial implementation or audit, check [EasyBuild's supported software list](https://docs.easybuild.io/version-specific/supported-software/) as a general-purpose discovery step. Many open-source libraries across mathematics, science, and HPC are packaged there.

## Mandatory preflight

Before writing or delegating mathematical implementation work:

- Check [EasyBuild's supported software list](https://docs.easybuild.io/version-specific/supported-software/) for existing packaged implementations of the functionality you need.
- Read `theory/backends/software-capability-map.md`.
- Read any backend note named by that map for the requested domain.
- Check whether the desired operation should be a thin bridge to Sage, GAP, Singular, Macaulay2, Oscar/Hecke/Nemo/AbstractAlgebra, Julia packages, CARAT, PARI/GP, polymake, Normaliz, or another open-source exact system.
- Record the selected backend, evidence docs, bridge surface, and limitation in the plan or card.
- If no wiring exists, stop implementation and file a tracked research card to determine whether this is a true software gap.

## Decision procedure

- Existing exact backend operation exists: implement the minimal semantic adapter or method on the repo's mathematical noun.
- Existing backend exists but bridge is missing: implement the bridge, not the mathematics.
- Backend support is plausible but undocumented: block implementation and create a research card to audit upstream docs, examples, source, and local usage.
- No mature open-source support is found after documented research: ask for human approval before bespoke implementation, then write the smallest auditable core and update the capability map.
- Only proprietary support is known: treat this as a blocker for repo code unless the user authorizes a non-repo exploratory comparison.

## Required card fields for blockers

A backend-gap research card must include:

- Desired mathematical operation.
- Domain and input/output mathematical objects.
- Software checked so far.
- Upstream docs or source paths checked.
- Known candidate packages.
- Why the original implementation task is blocked.
- Acceptance criterion: a documented routing decision of `preferred-backend`, `bridge-needed`, `true-gap`, or `out-of-scope`.

## Anti-patterns

- Writing raw matrix, polynomial, group, orbit, or lattice algorithms before checking backend docs.
- Reimplementing Nikulin theory, Groebner basis workflows, finite-group orbit enumeration, resolution, sheaf cohomology, polyhedral algorithms, or exact number-theory routines locally.
- Porting a mature GAP/Singular/Macaulay2/Julia algorithm into Python just to keep control in one language.
- Creating wrappers that only rename an upstream method without adding repo semantics or hiding an interop boundary.
- Treating Sage as a black box when the appropriate lower-level backend is GAP, Singular, PARI/GP, or another system Sage can call.
- Treating generated code as acceptable mathematics without primary-source and backend evidence.
- Auditing or reviewing code without considering whether complex implementations can be offloaded to a packaged tool from the [EasyBuild supported software list](https://docs.easybuild.io/version-specific/supported-software/).

## Handoff requirement

Every mathematical implementation card must say one of:

- `backend: <tool>` with docs consulted and adapter boundary.
- `backend-research-required` with linked research card.
- `bespoke-approved` with human approval and capability-map entry explaining the true gap.
