# Lattice Wrapper TDD Test Program Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Define a backend-agnostic, mathematically honest, strongly typed lattice wrapper test contract that standardizes capabilities and recovers the full known Sage+Julia documented lattice functionality at equal-or-better coverage.

**Architecture:** Build a capability-first test architecture. First define typed wrapper surfaces (including strict definite/indefinite split), then map legacy documented functionality into canonical capabilities, then enforce parity and quality with hard failing gates. Use strict TDD for each capability family (red-green-refactor).

**Tech Stack:** `pytest`, Sage (`conda -n sage`), Julia/Oscar test catalogs, Python static/parity tooling, repository test quality rules (`TEST_QUALITY.md` + AGENTS playbook).

---

## Approach Options
1. Capability Registry + Parity Matrix (Recommended)  
Tradeoff: highest upfront taxonomy effort; best long-term standardization and hard coverage guarantees.
2. Scenario Corpus Only  
Tradeoff: easier startup; weaker traceability and easier to miss surface drift.
3. Method Name Parity  
Tradeoff: fastest initially; violates requirement because backend method names are explicitly irrelevant.

Chosen: `1`.

## Task 1: Freeze Rules and Baseline Inputs

**Files:**
- Read: `AGENTS.md`
- Read: `TEST_QUALITY.md`
- Read: `tests/sage_doc/conftest.py`
- Read: `tests/julia_doc/coverage_utils.jl`
- Read: `tests/julia_pytest/test_oscar_bridge_static.py`

**Step 1: Write the failing test**
- Add a new test asserting baseline source-list constants are defined and non-empty.

**Step 2: Run test to verify it fails**
- Run: `HOME=/tmp/sage-home conda run -n sage python -m pytest -q tests/new_lattice_interface/test_functionality_parity_static.py::test_baseline_source_list_nonempty`
- Expected: FAIL due to missing constants.

**Step 3: Write minimal implementation**
- Add canonical baseline source globs/constants in parity tooling.

**Step 4: Run test to verify it passes**
- Re-run targeted test and confirm PASS.

**Step 5: Commit**
```bash
git add tests/new_lattice_interface/test_functionality_parity_static.py tests/new_lattice_interface/capability_mapping.py
git commit -m "test: add baseline source-list gate for parity tooling"
```

## Task 2: Define Canonical Typed Contract Surface

**Files:**
- Create/Modify: `tests/new_lattice_interface/types.py`
- Modify: `tests/new_lattice_interface/conftest.py`
- Test: `tests/new_lattice_interface/test_type_surface_separation_static.py`

**Step 1: Write the failing test**
- Add tests asserting:
  - definite-only methods are absent from indefinite type.
  - indefinite-only methods are absent from definite type.

**Step 2: Run test to verify it fails**
- Run targeted test file; expect missing/incorrect placement failures.

**Step 3: Write minimal implementation**
- Move abstract interfaces into `types.py`.
- Place methods on proper classes (`DefiniteLattice` vs `IndefiniteLattice`).

**Step 4: Run test to verify it passes**
- Re-run targeted separation tests and confirm PASS.

**Step 5: Commit**
```bash
git add tests/new_lattice_interface/types.py tests/new_lattice_interface/conftest.py tests/new_lattice_interface/test_type_surface_separation_static.py
git commit -m "test: enforce typed definite/indefinite surface separation"
```

## Task 3: Define Capability Registry Schema

**Files:**
- Create/Modify: `tests/new_lattice_interface/capability_registry.py`
- Test: `tests/new_lattice_interface/test_capability_registry_static.py`

**Step 1: Write the failing test**
- Add schema tests for:
  - unique IDs
  - valid domain values
  - non-empty input/output contracts
  - assertion profile and description presence

**Step 2: Run test to verify it fails**
- Run targeted registry tests; expect missing schema failures.

**Step 3: Write minimal implementation**
- Implement `CapabilitySpec` dataclass and core capability registry entries.

**Step 4: Run test to verify it passes**
- Re-run targeted tests; confirm PASS.

**Step 5: Commit**
```bash
git add tests/new_lattice_interface/capability_registry.py tests/new_lattice_interface/test_capability_registry_static.py
git commit -m "test: add capability registry schema and validation gates"
```

## Task 4: Build Legacy Method Extraction + Normalization

**Files:**
- Create/Modify: `tests/new_lattice_interface/capability_mapping.py`
- Create: `tests/new_lattice_interface/tools/extract_method_tags.py`

**Step 1: Write the failing test**
- Add parser tests for:
  - only real `method:` lines are accepted
  - `runtime_coverage` is ignored
  - signatures are normalized correctly

**Step 2: Run test to verify it fails**
- Run targeted parser tests; expect normalization failures.

**Step 3: Write minimal implementation**
- Implement extraction regex, token normalization, and utility functions.

**Step 4: Run test to verify it passes**
- Re-run parser tests; confirm PASS.

**Step 5: Commit**
```bash
git add tests/new_lattice_interface/capability_mapping.py tests/new_lattice_interface/tools/extract_method_tags.py tests/new_lattice_interface/test_functionality_parity_static.py
git commit -m "test: implement method-tag extraction and normalization"
```

## Task 5: Build Functionality Catalog Generator

**Files:**
- Create/Modify: `tests/new_lattice_interface/tools/build_functionality_catalog.py`
- Update artifact: `tests/new_lattice_interface/docs/legacy_functionality_catalog.md`

**Step 1: Write the failing test**
- Add a test asserting catalog generation produces non-empty mapped output.

**Step 2: Run test to verify it fails**
- Run targeted test; expect missing file/content.

**Step 3: Write minimal implementation**
- Implement generator consuming legacy source globs and mapping rows.

**Step 4: Run test to verify it passes**
- Generate catalog and run targeted test.

**Step 5: Commit**
```bash
git add tests/new_lattice_interface/tools/build_functionality_catalog.py tests/new_lattice_interface/docs/legacy_functionality_catalog.md
git commit -m "test: add legacy functionality catalog generator"
```

## Task 6: Build Method -> Capability Mapping Rules

**Files:**
- Modify: `tests/new_lattice_interface/capability_mapping.py`
- Modify: `tests/new_lattice_interface/test_functionality_parity_static.py`

**Step 1: Write the failing test**
- Add parity gates for:
  - all methods mapped to known capabilities
  - no catch-all bucket
  - no default fallback reason

**Step 2: Run test to verify it fails**
- Run parity tests; capture uncovered/default lists.

**Step 3: Write minimal implementation**
- Add exact and keyword mapping rules until defaults/catch-all drop to zero.

**Step 4: Run test to verify it passes**
- Re-run parity tests; confirm PASS.

**Step 5: Commit**
```bash
git add tests/new_lattice_interface/capability_mapping.py tests/new_lattice_interface/test_functionality_parity_static.py tests/new_lattice_interface/docs/legacy_functionality_catalog.md
git commit -m "test: enforce explicit full legacy method-to-capability mapping"
```

## Task 7: Enforce Capability Coverage Tags in New Wrapper Tests

**Files:**
- Create: `tests/new_lattice_interface/test_capability_coverage_static.py`
- Modify: `tests/new_lattice_interface/test_*.py`

**Step 1: Write the failing test**
- Add checks:
  - every wrapper test has `method:` doc tag
  - required capability families appear in wrapper tests

**Step 2: Run test to verify it fails**
- Run targeted coverage static test; expect missing tag/capability failures.

**Step 3: Write minimal implementation**
- Add/repair tags and missing family representation.

**Step 4: Run test to verify it passes**
- Re-run targeted test; confirm PASS.

**Step 5: Commit**
```bash
git add tests/new_lattice_interface/test_capability_coverage_static.py tests/new_lattice_interface/test_*.py
git commit -m "test: gate wrapper test tagging and capability representation"
```

## Task 8: Add Quality Guardrails as Tests

**Files:**
- Create/Modify: `tests/new_lattice_interface/test_quality_guardrails_static.py`
- Modify wrapper tests as needed

**Step 1: Write the failing test**
- Add static checks forbidding:
  - content-free non-emptiness assertions
  - `actual/expected` ceremony as primary pattern
  - interop-only equality checks without independent oracles

**Step 2: Run test to verify it fails**
- Run quality guardrails test; confirm violations found.

**Step 3: Write minimal implementation**
- Refactor offending tests to mathematically meaningful assertions.

**Step 4: Run test to verify it passes**
- Re-run guardrail tests; confirm PASS.

**Step 5: Commit**
```bash
git add tests/new_lattice_interface/test_quality_guardrails_static.py tests/new_lattice_interface/test_*.py
git commit -m "test: enforce wrapper assertion-quality guardrails"
```

## Task 9: Implement Runtime Contract Backend for Wrapper Tests

**Files:**
- Modify: `tests/new_lattice_interface/conftest.py`
- Optional: `tests/new_lattice_interface/provider_protocol.py`
- Test: all `tests/new_lattice_interface/test_*.py`

**Step 1: Write the failing test**
- Ensure full wrapper test suite is run with current stubs to capture failures.

**Step 2: Run test to verify it fails**
- Run:
  - `HOME=/tmp/sage-home conda run -n sage python -m pytest -q tests/new_lattice_interface`
- Expected: FAIL due to runtime stubs.

**Step 3: Write minimal implementation**
- Implement minimal mathematically consistent runtime backend for:
  - constructors (`from_gram`, `U`, `hyperbolic`, root constructors in scope)
  - pairing/norm/dual/discriminant
  - orbit/stabilizer/reflection/hyperplane
  - Vinberg/root-system contracts required by tests

**Step 4: Run test to verify it passes**
- Re-run `tests/new_lattice_interface`; confirm PASS.

**Step 5: Commit**
```bash
git add tests/new_lattice_interface/conftest.py tests/new_lattice_interface/provider_protocol.py
git commit -m "test: implement executable contract backend for wrapper tests"
```

## Task 10: Domain Alignment Gates

**Files:**
- Create/Modify: `tests/new_lattice_interface/test_capability_domain_alignment_static.py`

**Step 1: Write the failing test**
- Add tests that validate domain metadata aligns with type/group surfaces.

**Step 2: Run test to verify it fails**
- Run targeted test; expect mismatches.

**Step 3: Write minimal implementation**
- Correct expectations and ownership boundaries (e.g. orbit ops on `OrthogonalGroup`).

**Step 4: Run test to verify it passes**
- Re-run domain alignment tests; confirm PASS.

**Step 5: Commit**
```bash
git add tests/new_lattice_interface/test_capability_domain_alignment_static.py tests/new_lattice_interface/capability_registry.py
git commit -m "test: add capability-domain alignment gates"
```

## Task 11: Expand Capability Families to Full Legacy Union

**Files:**
- Modify/add tests under `tests/new_lattice_interface/`
- Update registry/mapping/catalog files

**Step 1: Write the failing test**
- For each missing capability family, add one failing contract test with independent oracle.

**Step 2: Run test to verify it fails**
- Run each new targeted test and confirm red.

**Step 3: Write minimal implementation**
- Add minimal backend behavior and/or test fixtures needed to satisfy each new contract.

**Step 4: Run test to verify it passes**
- Re-run targeted tests.

**Step 5: Commit**
```bash
git add tests/new_lattice_interface/*
git commit -m "test: extend wrapper capability families across legacy union"
```

## Task 12: Coverage Parity Gates

**Files:**
- Modify: `tests/new_lattice_interface/test_functionality_parity_static.py`

**Step 1: Write the failing test**
- Add non-regression gates:
  - mapped method count floor
  - nontrivial capability distribution
  - explicit no-unmapped guarantee

**Step 2: Run test to verify it fails**
- Run targeted parity tests; confirm regressions caught.

**Step 3: Write minimal implementation**
- Tighten mapping/catalog until all parity gates pass.

**Step 4: Run test to verify it passes**
- Re-run parity tests; confirm PASS.

**Step 5: Commit**
```bash
git add tests/new_lattice_interface/test_functionality_parity_static.py tests/new_lattice_interface/docs/legacy_functionality_catalog.md
git commit -m "test: add parity non-regression gates for wrapper capabilities"
```

## Task 13: Full Verification and DoD Lock

**Files:**
- No intentional edits (unless fixing discovered failures)

**Step 1: Run full baseline suite**
- Run: `just test`
- Expected: PASS.

**Step 2: Run full suite including wrapper tests**
- Run: `just test-full`
- Expected: PASS.

**Step 3: Run wrapper gate subset**
- Run:
  - `HOME=/tmp/sage-home conda run -n sage python -m pytest -q tests/new_lattice_interface/test_capability_registry_static.py tests/new_lattice_interface/test_type_surface_separation_static.py tests/new_lattice_interface/test_capability_coverage_static.py tests/new_lattice_interface/test_functionality_parity_static.py tests/new_lattice_interface/test_quality_guardrails_static.py tests/new_lattice_interface/test_capability_domain_alignment_static.py`
- Expected: PASS.

**Step 4: If failure occurs**
- Return to owning task, apply strict TDD loop, and re-verify all three commands.

**Step 5: Final commit**
```bash
git add tests/new_lattice_interface docs/project/plans/2026-02-15-lattice-wrapper-tdd-implementation.md
git commit -m "test: finalize lattice wrapper capability-first TDD program"
```

## Large Checklist

### A. Contract and typing
- [ ] Definite/indefinite split is explicit in types.
- [ ] Definite-only methods unavailable on indefinite type.
- [ ] Indefinite-only methods unavailable on definite type.
- [ ] Root/group/discriminant types explicitly modeled.
- [ ] Provider layer is backend-agnostic.

### B. Capability registry
- [ ] Every capability has ID/domain/input/output/assertion profile.
- [ ] No duplicate IDs.
- [ ] Domain partition is coherent.
- [ ] Registry schema tests fail on incomplete entries.

### C. Legacy union recovery
- [ ] Baseline includes all documented Sage + Julia suites.
- [ ] Extractor parses only valid `method:` tags.
- [ ] Token normalization is deterministic.
- [ ] Every token maps to a known capability.
- [ ] No catch-all mapping.
- [ ] No default fallback mapping.
- [ ] Catalog artifact is generated and versioned.

### D. Test quality compliance
- [ ] No content-free assertion patterns.
- [ ] No weak type/introspection assertions as primary claims.
- [ ] Interop checks include independent mathematical oracle.
- [ ] Assertion messages are explicit and diagnostic.
- [ ] Runtime of default suite remains practical.

### E. Coverage and parity gates
- [ ] Every wrapper test has a `method:` tag.
- [ ] Required core capability families represented.
- [ ] Parity count threshold enforced.
- [ ] Capability distribution threshold enforced.
- [ ] Missing coverage emits actionable lists.

### F. Runtime wrapper viability
- [ ] Wrapper contract backend executes all wrapper tests.
- [ ] Definite and indefinite algorithm paths are separate at runtime.
- [ ] Canonical invariants hold on small examples.

### G. Verification
- [ ] `just test` passes.
- [ ] `just test-full` passes.
- [ ] Wrapper static gate suite passes.
- [ ] Catalog is fresh for current mapping.
- [ ] DoD criteria fully satisfied.

## Acceptance Criteria
1. Wrapper tests define a mathematical interface independent of legacy method names.
2. Definite vs indefinite separation is enforced by both type shape and tests.
3. Legacy documented functionality is recovered by capability mapping and parity gates.
4. Tests comply with AGENTS playbook and `TEST_QUALITY.md`.
5. Coverage parity is equal-or-better than documented baseline, with hard non-regression checks.

