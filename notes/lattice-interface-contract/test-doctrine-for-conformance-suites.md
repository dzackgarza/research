# Lattice Test Quality Standard

This document defines quality requirements for lattice-related reference tests across all supported systems in this repository (Sage, Julia/Oscar/Hecke, GAP, and package ecosystems).

## 0. Coverage Goals (Cross-System)

- Cover every mathematically interesting lattice-related algorithm surfaced by the supported systems, not just Sage.
- Require explicit consideration of optional packages and add-on libraries before declaring documentation/testing complete.
- Prevent mathematically relevant methods from going undocumented or untested when they are useful for lattice research workflows.
- Exclude only generic linear-algebra routines that are standard matrix functionality, unless the method is specialized to nonstandard coefficient domains or structures.

Standard matrix algorithms usually excluded from lattice-method completeness goals:

- generic kernel/image/rank/eigenvalue/eigenvector routines over standard domains (`RR`, `CC`, `QQ`, standard real/float fields)
- generic matrix arithmetic and shape/format conversion methods

Standard matrix algorithms that must be included when specialized:

- methods whose mathematical contract depends on lattice/form structure
- methods tied to integer/number-field/p-adic/finite-form regimes
- methods with lattice-specific semantics (genus, local densities, reduction theory, embeddings, discriminant-form machinery, automorphism/isometry structures)

## 1. Assertions Must Be Mathematically Nontrivial

- Every test must assert a meaningful mathematical property, identity, invariant, or equivalence.
- Assertions should go beyond API existence and check correctness of output content.
- Prefer properties like:
  - invariant preservation (`disc`, `det`, `signature`, rank)
  - algebraic identities (polarization, duality, reciprocity)
  - structural equivalence (same genus/class/isometry class when appropriate)
  - exact reconstruction/roundtrip behavior

## 2. Keep Runtime Small; Mark Heavy Tests

- Avoid tests that take more than ~30 seconds.
- Use minimal examples that still validate correctness.
- For expensive algorithms, test small but representative inputs.
- If a heavy test is unavoidable, mark it explicitly (for example with `pytest.mark.slow`) and keep it out of default fast runs when possible.

## 3. Do Not Use Content-Free Assertions

The following are disallowed as primary assertions:

- `is not None`
- `hasattr(...)`
- `isinstance(...)` (unless type is itself a core mathematical contract and accompanied by a mathematical assertion)
- non-emptiness existence checks such as:
  - `len(x) > 0`
  - `len(x) >= 1`
  - `bool(x)`
  - `x != []`
  - lattice-representative placeholders such as:
    - `assert len(reps) > 0`
  - wrappers of the above like:
    - `actual = len(x) > 0; expected = True; assert actual == expected`

Why this is not useful for mathematical documentation:

- It validates object presence, not mathematical correctness.
- It can pass even when the algorithm is wrong.
- It does not document expected mathematical behavior of the method.

Instead, assert relations between computed values and mathematically expected outcomes.

### 3.1 No Trivial Primary Witnesses

- Do not use trivial objects as the primary witness for a method test.
- Trivial objects include:
  - zero vectors/elements,
  - identity maps/group elements,
  - empty/default structural objects.
- Use nontrivial mathematical witnesses as the primary example (for example nonzero vectors, non-identity automorphisms, nontrivial glue/invariant data).
- Trivial objects may appear only as secondary consistency checks after a nontrivial primary assertion.

Examples of acceptable replacements:

- Verify exact known values for canonical small examples.
- Verify invariants/identities (determinant, discriminant, rank, reciprocity/product formulas).
- Verify reconstruction/roundtrip correctness (map/inverse map, normal-form equivalence).
- For returned collections, assert mathematically meaningful content (specific expected elements/properties), not just non-emptiness.

Representative-list replacement pattern:

- Bad:
  - `reps = method(...)`
  - `assert len(reps) > 0`
- Good:
  - `reps = method(...)`
  - assert at least one representative is exactly the expected canonical object, or
  - assert every representative satisfies the defining invariant and that known inequivalent examples are present/absent as expected, with explicit diagnostics.

## 4. Use Precise Types

- Do not use vague types like `object` or `Any` in test helpers/doc examples where concrete types are known.
- Use explicit Sage/Python types where relevant (`ZZ`, `QQ`, vectors, matrices, tuples of integers, etc.).
- Input types should match method contracts (for example, pass Sage vectors when vector APIs are expected).

## 4.5 Keep Assertions Direct (Avoid Ceremony)

- Avoid synthetic tuple wrappers that restate the same value just to format assertions.
- Do not build helper pairs like `(actual, baseline)` vs `(expected, baseline)` when the contract is a single equality.
- Prefer direct scalar/object assertions with explicit diagnostics.

Why this matters:

- Tuple-wrapper assertions add noise without increasing mathematical signal.
- Repeating the same baseline term in multiple tuple slots can hide what is actually being tested.
- Direct assertions make the contract obvious and reduce accidental tautologies.

Example (pairing contract):

- Overly verbose:
  - `actual_pairing_pair = (L.pairing(x, y), x * y)`
  - `expected_pairing_pair = (x * y, x * y)`
  - `assert actual_pairing_pair == expected_pairing_pair`
- Preferred:
  - `actual = L.pairing(x, y)`
  - `expected = x * y`
  - `assert actual == expected, f"pairing mismatch: actual={actual}, expected={expected}"`

## 5. Document Entry-Point Interoperability

For each module/entry point, document and test conversion routes into/out of related modules when they are clear and supported.

Examples:

- `IntegralLattice` <-> discriminant module / genus / Gram matrix objects
- `TernaryQF` -> `QuadraticForm`
- `BinaryQF` <-> polynomial representations
- `NumberField` interactions with ideals/modules used by lattice workflows

The goal is to capture mathematical workflow boundaries, not just isolated methods.

## 5.5 Interoperability Checks Are Not Correctness Proofs

- Cross-entry-point equality checks (for example `root.method(...) == lattice.method(root, ...)`) are useful, but weak when used alone.
- Treat these as interface-consistency checks, not mathematical correctness tests.
- Do not rely only on "same result from two APIs" when both APIs may share the same implementation path.

Why this is weak by itself:

- Both calls can return the same wrong result and still pass.
- A single sampled object (for example one simple root) gives narrow behavioral coverage.
- It documents plumbing agreement, not the defining mathematical contract.

Required strengthening for such tests:

- Add at least one independent mathematical oracle assertion:
  - reflection laws (`s(r) = -r`, involution `s^2 = id`, form/invariant preservation),
  - hyperplane contract (elements pair to `0` with the defining root/vector),
  - known canonical small-example outputs.
- Prefer checking multiple representative inputs (for example all simple roots) instead of only index `0`.

Pattern guidance:

- Weak-only pattern:
  - compute `from_root = r.reflection()` and `from_lattice = L.reflection(r)`
  - assert equality between those two values
- Acceptable pattern:
  - keep the cross-entry-point equality assertion
  - and add independent contract assertions that would fail if both entry points are jointly wrong

## 6. No `xfail` or Expected-Failure Masking

- Do not use `pytest.mark.xfail`, `xfail(strict=False)`, or similar expected-failure mechanisms.
- Do not hide known breakage behind pass-by-design markers.
- Suite status must reflect actual runtime functionality:
  - passing tests document behavior that works
  - failing tests document behavior that currently does not work

The target is not an artificial 100% green dashboard. The target is accurate documentation of the current implemented mathematical surface.

## 7. Optional Package Completeness Pass Is Mandatory

Before signing off on coverage/documentation completeness for a system:

- enumerate core methods and optional package methods relevant to lattice research
- check each package for mathematically relevant algorithms, not only commonly used constructors
- classify each discovered method as:
  - tested and documented
  - irrelevant infrastructure
  - missing and requiring a new test/doc entry
- do not assume package methods are out of scope simply because they are add-ons

For GAP specifically, this includes both core integer-lattice/form operations and package surfaces (for example crystallographic, toric/polyhedral, and integer-relation ecosystems) when those methods are mathematically relevant to lattice workflows.

## 8. Method Triage Rule (Interesting vs Generic)

When deciding whether a method must be tested/documented:

- Include if it changes or studies lattice-theoretic invariants/classification/search spaces.
- Include if it is algorithmically nontrivial and used in research workflows (reduction, embedding, genus/local data, automorphisms, discriminant forms, toric/lattice-point arithmetic).
- Exclude if it is purely generic matrix plumbing over standard domains and carries no lattice-specific contract.
- Re-include excluded generic methods if they are specialized to nonstandard domains or have lattice/form-dependent semantics.

## 9. Anti-Obfuscation Checks (Blacklist + Scope)

- Blacklists/irrelevant-method lists must never hide mathematically interesting algorithms.
- Every blacklist entry should be auditable as infrastructure-only; if uncertain, treat it as in-scope and test it.
- Coverage scope must be validated at the right abstraction level:
  - do not over-narrow module prefixes or sample-object types in a way that excludes higher-level algorithms users actually call
  - explicitly check for methods present on higher-level modules/objects even when tests are implemented in narrower files
- Completeness reviews must include a short “hidden surface” pass:
  - methods excluded by blacklist
  - methods omitted due to tight module prefix filters
  - methods available on parent/high-level APIs but absent from current test surfaces

## Practical Author Checklist

Before finalizing a test:

1. Does the assertion prove a nontrivial mathematical fact?
2. Would this still catch an implementation returning arbitrary non-empty junk?
3. Is the claim specific enough to fail on mathematically wrong output?
4. Is the case minimal but representative?
5. Is runtime reasonable for default test runs?
6. Are inputs strongly typed and contract-correct?
7. If this method bridges modules, does the test document the bridge?
8. Is the test result honest (no `xfail`/expected-failure masking)?
9. Was the relevant optional-package surface checked and triaged?
10. If this is a generic matrix-style method, is there a clear reason it is lattice-mathematically relevant?
11. Could blacklist entries or overly narrow scope filters be hiding higher-level interesting methods?
