---
id: DECISION-QADIC-LATTICE-PRECISION
trackerStatus:
  type: decision
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
title: Decide disposition of deferred q-adic lattice precision constructors
status: decided
priority: medium
description: Resolve the status of ZqWithPrecisionCaps and QqWithPrecisionCaps constructor
  names that are admitted in the spec but not supported by installed Sage.
resolution: "- `ZqWithPrecisionCaps` and `QqWithPrecisionCaps` are mathematically\
  \ meaningful \n  constructor names for q-adic rings/fields with lattice (pair) precision\
  \ caps. \n  They are ADMITTED as deferred names: the spec records them, but they\
  \ are blocked \n  until Sage upstream supports the construction.\n- The installed\
  \ Sage 10.7 environment does not support direct q-adic pair precision \n  construction.\
  \ Scalar precision routes (Zp, Qp, Zq, Qq with integer `prec`) work.\n  Pair precision\
  \ `(cap, prec)` raises `TypeError` for q-adic.\n- The five-field negative finding\
  \ in SPEC-MAPPING-RINGS.md lines 378-431 documents \n  the Sage upstream gap with\
  \ concrete evidence (factory.py source inspection, \n  error reproduction).\n- No\
  \ implementation task should attempt to build these constructors until Sage \n \
  \ upstream supports the pair-precision route or a project-side bridge is designed\
  \ \n  and approved.\n- The deferred names serve as documentation of the intended\
  \ surface and prevent \n  silent omission of these constructors from the spec.\n"
evidence:
- 'Sage source: sage/rings/padics/factory.py -- Zq(q, prec, type, ...) supports scalar
  precision only; pair precision raises TypeError'
- 'SPEC-MAPPING-RINGS.md lines 378-431: five-field negative finding'
- 'TASK-01KQN9YGCJ26WJ2044DVNVNE87: research card for q-adic precision caps in Sage
  upstream'
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Decide q-adic lattice precision disposition

## Question

What is the status of `ZqWithPrecisionCaps` and `QqWithPrecisionCaps` — admitted 
constructor names that installed Sage cannot construct?

## Decision

ADMITTED as deferred. The names are mathematically meaningful and documented as a 
Sage upstream gap. No implementation until Sage supports pair-precision q-adic 
construction.

## Work Log

- 2026-05-07: Created from Gate 5 review finding on SPEC-MAPPING-RINGS.
