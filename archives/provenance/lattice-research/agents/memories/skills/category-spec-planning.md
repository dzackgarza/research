---
title: Category Spec Planning
status: active
date: 2026-05-29
---
# Category Spec Planning

Use this skill for planning and plan decomposition around `category_specs`.

## Planning gate

Plans are human + LLM collaborative artifacts.
Do not create or enact an operative plan unilaterally.

Before implementation:

- Switch to planning mode when creating or materially revising a plan.
- Iterate with the user until the plan is explicitly approved.
- Store the approved plan under root `.agents/plans/features/FEATURE-ID/plans/PLAN-ID/`.
- Decompose the approved plan into concrete tracked cards.

## Decomposition rules

- Use `feature` cards only for feature roots.
- Use `spec` cards for feature-owned spec surfaces.
- Use `task` cards for executable implementation, research, bug-fix,
  category-obligation-example triage, and audit work.
- Use `decision` cards for unresolved mathematical or organizational choices.
- Put executable tasks under the relevant plan phase's `tasks/` directory.
- Add acceptance criteria and source provenance to every executable card.
- Link cards back to the approved plan.

## Anti-trigger: do not plan instead of understanding

Do not invoke this skill merely because the issue is confusing, multi-step, or
uncomfortable.

Do not create a plan/card/decision artifact when:
- the user asked for a fix;
- the issue is a local source conflict;
- both sides of the conflict are repo-controlled;
- the next useful action is reading source code;
- the apparent decision may disappear after naming the mathematics.

Planning is for coordination after the mathematical/source issue is understood.
It is not an avoidance mechanism.

## References

Read `mem:skills/category-spec-workflow` for the canonical planning workflow, priority
rubric, theme grouping, and card requirements.
