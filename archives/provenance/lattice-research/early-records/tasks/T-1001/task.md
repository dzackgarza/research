# Task T-1001: Standard Lattice Fixtures

## Status

Selected in Wave A. TASK_SPECIFICATION complete as of 2026-04-02.

## Tier

Tier 1.

## Origin

- GOAL.md source: line 19 "Λ_K3 = U³ ⊕ E8² (rank 22, signature (22,0), unimodular)"
- GOAL.md line 60 "Hyperbolic plane U" with Gram [[0,1],[1,0]]
- GOAL.md reference: standard lattice theory (E8 root lattice, A1 = ⟨-2⟩)
- Foundation library already constructs U, E8, A1, Λ_K3

## Objective

Assemble standard lattice fixtures:
- U (hyperbolic plane): rank=2, signature=(1,1), det=-1
- A₁ = ⟨-2⟩: rank=1, signature=(0,1), det=-2
- E8 (root lattice): rank=8, signature=(0,8), det=1 (unimodular)
- E8(-1): rank=8, signature=(0,8), det=1, even
- E8(-2): rank=8, signature=(0,8), det=256 = 2⁸, even
- Λ_K3 = U³ ⊕ E8²: rank=22, signature=(22,0), det=1 (unimodular)

With published rank, signature, determinant, and isometry data from standard references.

## Deliverable Type

fixture data — known-invariant objects for sanity-checking T-0 tools.

## Acceptance Criteria

1. **Fixture inventory**: Document each lattice with exact values:
   - rank (Integer)
   - signature (p,q) tuple
   - determinant (Integer)
   - is_even (Boolean)
   - discriminant group structure (if not unimodular)

2. **Reference source**: Each fixture value traces to a published source (textbook,
   paper, or foundation library docstring)

3. **Test harness**: Create Sage script that loads all fixtures and verifies each
   invariant against expected values

4. **Fixture file**: Save as YAML or JSON in theory/computations/fixtures/ for
   downstream consumption

5. **Import test**: T-1001 fixtures loadable without error

## Non-Goals

- Does not verify correctness (that's T-2001)
- Does not prove isometry (just provides fixtures)
- Does not compute orbits or group actions
- Does not construct embeddings

## Allowed Dependencies

- Prerequisite tasks: none (independent fixture collection)
- Local sources:
  - REFERENCES.md (standard lattice theory references)
  - theory/oscar_lattices.md (Oscar fixture conventions)
  - src/coble_geometry_foundation.sage (already constructs these)

## Required Conventions

- Fixture file format: YAML with keys matching lattice names
- Each fixture entry includes: rank, signature, determinant, evenness, reference
- Test script uses asserts against fixture values

## Failure Conditions

1. If any fixture value doesn't match published source → fail
2. If test harness fails on any fixture → fail
3. If fixture file doesn't parse as valid YAML/JSON → fail
4. If downstream T-0 tool can't load fixtures → fail

## Parent Sufficiency Map

Provides fixtures for:
- T-0001: sanity-checks lattice constructors
- T-0002: sanity-checks invariant computation
- T-0003: sanity-checks embedding test cases
- T-0008: sanity-checks involution test case (Λ_K3)
- T-2001: gates constructor correctness
- T-2008: gates involution correctness

This is fixture collection only — no verification performed.
