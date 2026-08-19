---
name: interface-design
description: Interface and type-surface design work. Use when assignments define or change API contracts, type signatures, or behavioral guarantees.
---

# Interface Design Skill

**Example tasks:** See `.skills/interface-design/example_tasks/` directory

## FILE SCOPE BOUNDARY (ABSOLUTE — READ FIRST)

**You may only create or modify files under `docs/` or `tests/`.** Never modify any file outside these directories, including:
- `agents/` — any playbook, prompt, or example task file
- `agent_runner/` — any source, config, or test file
- Any file outside the `docs/` or `tests/` directory tree

If you identify what appears to be a structural problem in a prompt, playbook, or example task, you may document it in `docs/TODO.md`. You may not fix it. That is the agent_management agent's job.

Editing `agents/` or `agent_runner/` files is a scope violation regardless of perceived urgency or merit. A run that edits files outside `docs/` or `tests/` has failed its scope boundary.

## Scope

Applies when assignment work defines or changes interface contracts, type surfaces, and behavioral guarantees.

## Core Rule (Non-Negotiable)

- Never prioritize backward compatibility during interface-definition work.
- If interface is still being defined, backward compatibility is not a valid constraint.
- Prioritize mathematical correctness, coherent type ontology, and clear contracts first.
- Remove or rename incorrect interface types immediately rather than preserving legacy names.

## Design Expectations

- Contracts are explicit, mathematically correct, and testable.
- Types and method signatures are coherent and non-contradictory.
- Assumptions/constraints are explicit (domain, definiteness, ring assumptions, etc.).
- Interface docs and tests remain aligned with real behavior.

## Handoff

- Record design decisions and remaining contract gaps in Serena continuity memories.
- Commit assignment-owned interface changes.
