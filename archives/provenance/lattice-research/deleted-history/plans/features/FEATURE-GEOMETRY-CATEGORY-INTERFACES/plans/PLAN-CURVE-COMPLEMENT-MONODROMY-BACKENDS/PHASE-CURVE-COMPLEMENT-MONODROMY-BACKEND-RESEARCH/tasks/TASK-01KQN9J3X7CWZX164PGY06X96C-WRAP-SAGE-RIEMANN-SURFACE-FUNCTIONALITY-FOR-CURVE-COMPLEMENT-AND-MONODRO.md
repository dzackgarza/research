---
id: TASK-01KQN9J3X7CWZX164PGY06X96C-WRAP-SAGE-RIEMANN-SURFACE-FUNCTIONALITY-FOR-CURVE-COMPLEMENT-AND-MONODRO
trackerStatus:
  type: task
parents:
- '[[PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH]]'
dependsOn: []
title: Wrap Sage Riemann surface functionality for curve-complement and monodromy
  workflows
status: unstarted
priority: critical
description: The source backlog identifies category-spec design work around dual objects
  as Hom objects, method ownership generalization, centralized type aliases, and a
  TwistedForms category.
successCriteria:
- The research result cites the exact sources searched and separates source evidence
  from inference.
- 'Negative findings use the repository five-field format: Searched, Found, Conclusion,
  Confidence, Gaps.'
- Any admitted design consequence is linked to a spec-work or design-decision item
  rather than buried in prose.
- Review the affected public type aliases and category methods against plans/todo.md
  before closing.
- Run the relevant category_specs smoke file for any changed subtree.
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
- PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS
- PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH
---
# Wrap Sage Riemann surface functionality for curve-complement and monodromy workflows
## Summary

The source backlog identifies category-spec design work around dual objects as Hom
objects, method ownership generalization, centralized type aliases, and a TwistedForms
category.

## Source Provenance

- `plans/todo.md`
- Original migrated line: `Wrap Sage Riemann surface functionality for curve-complement and monodromy workflows from plans/todo.md`

## Context

- Dual objects should route through Homsets: M* = Hom_R(M, R), so dual-object category wiring must not bypass the hom-category surface.
- Methods should move to the most general category where they make mathematical sense, rather than remaining on forms-specific wrappers.
- types.py should own standard mathematical aliases for module objects, elements, Hom/End/Aut objects, dual modules, forms, and scalar categories.
- TwistedForms should be a real form-object category rather than ad hoc form handling inside ModulesWithForms.

## Acceptance Criteria

- [ ] The research result cites the exact sources searched and separates source evidence from inference.
- [ ] Negative findings use the repository five-field format: Searched, Found, Conclusion, Confidence, Gaps.
- [ ] Any admitted design consequence is linked to a spec-work or design-decision item rather than buried in prose.
- [ ] Review the affected public type aliases and category methods against plans/todo.md before closing.
- [ ] Run the relevant category_specs smoke file for any changed subtree.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
