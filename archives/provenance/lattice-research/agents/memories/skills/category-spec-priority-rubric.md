---
title: Category Spec Priority Rubric
status: active
date: 2026-05-29
---
# Category Spec Priority Rubric

Use this skill to set the `priority` metadata field on category-spec tracker cards.
Priority orders work; it does not measure size.

## Core Policy

- Encode priority only in `priority`, never as `priority-*` tags.
- Use tags for topic, domain, workstream, and workflow class.
- Use the plan/work dependency graph before sorting individual cards.
- Raise priority when unfinished work can poison downstream mathematical meaning.
- Do not raise priority for presentation polish, incidental QC noise, or cleanup that
  does not affect active workflows.

## Rubric

Set `critical` when unfinished work can poison downstream work:

- Foundational spec and design work.
- Mathematically correct and complete definitions.
- Specced vocabulary required before implementation can proceed.
- Uniformity rules that determine future work trajectories.
- Theoretical background sources, curated BibTeX, and canonical references needed to
  prevent confabulation.
- Canonical docs and anti-staleness work needed to prevent backsliding.
- Any ambiguity that can cause agents to implement the wrong mathematics.

Set `high` when other work depends on the item or delay creates redo risk:

- Dependency roots in the plan/work graph.
- Cross-domain or low-level category/code changes.
- Simplification or consolidation work that prevents technical debt.
- Work that, if postponed, will force later work to be rewritten.
- Known constructor-routing, mapping, failed-category-assertion, and ownership issues
  that affect several downstream cards.

Set `medium` for ordinary bounded work:

- Local implementation work with clear definitions and limited blast radius.
- Research that informs work but does not currently block foundations.
- Cleanup that improves maintainability without changing downstream direction.

Set `low` for work that should not steer the project:

- World-facing READMEs and presentation polish.
- Internal consistency checks that are not real mathematical tests.
- Edge-case handling or tests outside main workflows.
- Bugs that do not affect current main workflows.
- Rewriting Sage core classes to avoid local patching/refinement when the current
  approach is serviceable.
- Trivial formatting and non-critical linting such as line length.
- De-slopifying local code when it is not poisoning active work.
- Resolving every git commit verification issue when it does not affect correctness,
  review, or traceability.

## Validation Checklist

- [ ] The chosen priority reflects dependency risk, not task size.
- [ ] The card has topic/workstream tags separate from priority.
- [ ] Critical/high cards explain the downstream work they protect or unblock.
