# Task T-2009: Reduction-Ledger Gate

## Status

Selected in Wave A. This is scaffolded for TASK_SPECIFICATION; detailed acceptance and
failure criteria must be finalized before PRE_AUDIT.

## Tier

Tier 2.

## Origin

- Canonical backlog source:
  [tasks/goal_expansion.md](/home/dzack/research/tasks/goal_expansion.md)
- GOAL.md origin (exact lines):
  - STATE_MACHINE.md R5: "Every T-3 task must have a reduction ledger linking each exact
    computation to its GOAL.md rationale"
  - STATE_MACHINE.md R7: "The ledger must contain: (1) which GOAL.md item is being
    addressed, (2) why exact computation was needed vs.
    approximation, (3) what the computed value is, (4) how it strengthens the claim"
- GOAL linkage: Gate for theorem-support promotion in T-3002, T-3003, and T-3011

**NOTE**: This is a policy gate, not a computational gate.
Per audit findings, it has no T-0 tool and no T-1 fixtures.
It verifies ledger presence, not mathematical correctness.

## Objective

Require a reduction ledger for every T-3 task that promotes exact computation toward a
stronger GOAL.md statement.

## Parent Sufficiency Map

Prevents proof-burden laundering across activated mathematical tasks.

## Deliverable Type

assertion gate

## Current Dependencies

- Prerequisite tasks: none
- Local sources:
- STATE_MACHINE.md
- GOAL.md

## Acceptance Scaffold

- The task must stay within the objective and sufficiency map above.
- Tier semantics from [STATE_MACHINE.md](/home/dzack/research/STATE_MACHINE.md) are
  binding.
- Detailed acceptance criteria, non-goals, and failure conditions remain to be pinned in
  TASK_SPECIFICATION.

## Acceptance Criteria (TASK_SPECIFICATION)

For T-2009 as a policy gate, acceptance criteria verify ledger structure rather than
mathematical properties:

1. **Ledger Presence**: Every activated T-3 task (T-3001, T-3002, T-3003, T-3011) must
   have a `reduction_ledger.md` file in its task directory.
2. **Required Ledger Fields**: Each reduction_ledger.md must contain:
   - `GOAL.md linkage`: which GOAL.md item the task addresses
   - `necessity statement`: why exact computation was required vs.
     approximation
   - `computed value`: the exact numerical or structural result
   - `strengthening claim`: how the computation strengthens the GOAL.md claim
3. **Ledger Consistency**: The GOAL.md items referenced in ledgers must exist and be
   valid.
4. **Audit Trail**: Ledgers must be created before task moves to IMPLEMENT state.

## Non-Goals

- T-2009 does NOT verify mathematical correctness of the computations (this is the T-2
  gate's job).
- T-2009 does NOT validate the numerical values in reduction ledgers.
- T-2009 does NOT require ledger entries to cite specific theorems (beyond GOAL.md
  items).
- T-2009 does NOT check computational methodology, only the existence and structure of
  rationale.

## Failure Conditions

- If a T-3 task lacks a reduction_ledger.md file, T-2009 FAILS and the T-3 task cannot
  proceed to IMPLEMENT.
- If a reduction_ledger.md exists but omits any of the four required fields, T-2009
  FAILS.
- If the GOAL.md linkage in a ledger references a non-existent GOAL.md item, T-2009
  FAILS.

## Required Conventions

- Ledger files must be named exactly `reduction_ledger.md`.
- Ledger format: markdown with four required sections (GOAL.md linkage, necessity
  statement, computed value, strengthening claim).
- Ledgers must be created during PRE_AUDIT phase, before IMPLEMENT begins.

## Failure Mode

When T-2009 fails, the dependent T-3 task remains in PRE_AUDIT. The failure is reported
to the orchestrator with specific missing fields or missing ledger files identified.
The T-3 task must create or 修正 the reduction_ledger.md before retrying the T-2009 gate.

## Tier Constraints

- Must remain a thin gate over T-0 primitives and T-1 fixtures.
- Must not replace object-level primitives with task-shaped black boxes.
- Must define what happens when a downstream T-3 task fails the gate.
