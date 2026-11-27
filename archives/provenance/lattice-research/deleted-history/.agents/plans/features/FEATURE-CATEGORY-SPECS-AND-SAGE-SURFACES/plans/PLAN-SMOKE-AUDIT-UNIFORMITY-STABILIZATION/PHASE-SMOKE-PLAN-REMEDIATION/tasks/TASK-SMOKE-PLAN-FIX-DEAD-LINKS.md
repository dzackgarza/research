---
id: TASK-SMOKE-PLAN-FIX-DEAD-LINKS
trackerStatus:
  type: task
parents:
- '[[PHASE-SMOKE-PLAN-REMEDIATION]]'
dependsOn: []
title: Remove dead source links and replace vague references in smoke plan
status: complete
priority: high
description: 'Fix G1 source grounding failures: remove 2 dead paths from Source corpus,
  replace 2 vague references with concrete file paths.'
successCriteria:
- Dead path `plans/LATTICE_STYLE_GUIDE.md` removed from Source corpus section.
- Dead path `plans/lattice_redesign_corrections_spec.md` removed.
- The vague "Existing smoke and variadic sprint plans under plans/features/" reference
  replaced with a concrete path to PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT under PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION.
- The vague "Existing implementation cards under plans/features/" reference replaced
  with a concrete reference to PLAN-CATEGORY-FOUNDATION-KERNEL.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION
- PHASE-SMOKE-PLAN-REMEDIATION
---
# Remove dead source links and replace vague references

The 6-gate review G1 found two dead paths and two vague references in the plan's
Source corpus section. Edit the plan body to fix all four.

Dead paths to remove:
- `plans/LATTICE_STYLE_GUIDE.md` (does not exist on disk)
- `plans/lattice_redesign_corrections_spec.md` (does not exist on disk)

Vague references to replace:
- "Existing smoke and variadic sprint plans under `plans/features/`" →
  concrete path to the variadic phase under PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- "Existing implementation cards under `plans/features/`" →
  reference to PLAN-CATEGORY-FOUNDATION-KERNEL
