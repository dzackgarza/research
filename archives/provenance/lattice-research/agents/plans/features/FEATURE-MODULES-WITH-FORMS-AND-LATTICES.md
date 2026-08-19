---
id: FEATURE-MODULES-WITH-FORMS-AND-LATTICES
trackerStatus:
  type: feature
parents: []
dependsOn:
- '[[FEATURE-QC-WARNINGS-ZERO]]'
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
plans:
- '[[PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP]]'
title: Modules with forms and lattices
status: in-progress
priority: critical
description: 'Deliver the typed ModulesWithForms and lattice vocabulary needed before
  downstream lattice-theory implementation: formed modules, quotient-valued forms,
  dual and rational lattice objects, discriminant descent, morphisms, Hom/End/Aut
  surfaces, and orthogonal-group interfaces.'
---
# Feature: Modules with forms and lattices

## Summary

Deliver the typed ModulesWithForms and lattice vocabulary needed before downstream lattice-theory implementation: formed modules, quotient-valued forms, dual and rational lattice objects, discriminant descent, morphisms, Hom/End/Aut surfaces, and orthogonal-group interfaces.

## Acceptance Criteria

- [ ] Lattice and ModulesWithForms plans are represented under this feature.
- [ ] Source-grounded form, lattice, discriminant, and morphism spec cards live under this feature or depend on its phases.
- [ ] Implementation tasks remain phase-local under the lattice roadmap phases.

## Dependencies And Boundaries

This feature is downstream of the root category-spec and Sage-surface vocabulary. It extends that vocabulary with ModulesWithForms, lattice, discriminant, and morphism surfaces; it does not authorize Coble research or raw matrix implementation work.
