---
title: Category Spec Audit
status: active
date: 2026-05-29
---
# Category Spec Audit

Use this skill when reviewing category-spec work for compliance and downstream risk.

## Required references

Before auditing:

- Read `category_specs/AGENTS.md`.
- Load `category-spec-style` for mathematical and code/spec compliance.
- Read `mem:skills/category-spec-workflow` for card, priority, decision, visual, and
  retirement handling.
- Load `jerry-behaviour` when reviewing agent-produced work.
  The reviewer's criteria must be independent of the producer's assumptions.
  A review that would look the same if the artifact were wrong is Jerry review.

## Audit focus

- Specced vocabulary exists before implementation proceeds.
- Spec claims are written in serious mathematical language: object, hypotheses, required
  data, construction/predicate, and codomain are coherent before Sage evidence is used.
- Mathematical ownership is explicit and placed at the weakest category where the
  operation is defined.
- Foundations are complete enough to avoid downstream rewrites.
- Complexity is hidden behind mathematical nouns, not ad hoc helper sprawl.
- Indirection is minimal and meaningful.
- Sage interop is mapped, not blindly wrapped.
- Docs and references are current enough to prevent backsliding or confabulation.
- Staged changes, unstaged changes, and task-local commits do not weaken specs by
  deleting obligations, narrowing category assertions, or moving method definitions without a
  source-grounded replacement owner.
- Type definitions are centralized, not scattered.
  `category_specs/types.py` is the single authority for project-wide mathematical type
  aliases. A `TypeAlias` or type definition appearing in a subpackage `__init__.py` is
  suspicious: it hides a mathematical noun where downstream code cannot import it
  uniformly. Subpackages should import types from `types.py`, not define them.
  If a type is only needed locally, question whether it is a real mathematical type or
  an implementation detail that should remain private.

## Output routing

- Record defects as `bug` cards when they are concrete failures.
- Record missing work as `task` or `feature` cards.
- Record unresolved mathematical or organizational choices as `decision` cards.
- Add vague or tangential observations to `.agents/TODO.md`.
- Do not create free-form audit reports unless explicitly requested.

## Red Flag Log

When auditing code or specs, produce an explicit list of identified introspection red
flags (`isinstance`, `hasattr`, `getattr`, `type()`, `issubclass`, `callable()`) found
in the audited content.
This log forces visibility into the reasoning and prevents agents from silently
accepting or silently deleting these patterns.

For each occurrence, record:

- **Location**: file path, line number, and the exact expression.
- **Classification**: `boundary-justified` or `design-smell`.
- **Reasoning**: if boundary-justified, what boundary is being crossed and why the check
  cannot be avoided? If a design smell, what is missing (type annotation, predicate
  subcategory, overload, declared attribute, constructor path)?
- **Disposition**: `keep` (boundary-justified), `replace-with-X`, or `needs-decision`
  (unclear whether the pattern is justified).

The red flag log is part of audit output, not a separate file.
Include it immediately after the audit findings.

A red flag log with zero entries is a Jerry signal: it means the auditor either did not
read the code or approved without inspection.
Real code has findings.
If you produced no log, state explicitly which files you read and why none contained
introspection red flags.

Reference: see the `anti-slop` skill,
`references/code-patterns.md#introspection-red-flags` for the full reasoning chain and
acceptance criteria table.
