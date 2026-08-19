---
title: Diagnostics are navigation, not data
---

# Diagnostics are navigation, not data

## The failure

An agent was given 64 override errors with file paths and line numbers. Instead of
opening the files, the agent:

1. Parsed the error messages into a JSON ledger
2. Invented a taxonomy ("return-type narrowing", "signature-incompatible",
   "argument-type incompatible")
3. Wrote a 3,000-character goalcraft goal structured around the taxonomy
4. Edited memories to document the taxonomy
5. Proposed decision cards and variance analyses

The actual problem: `is_open(self, U: Subset)` and `is_open(self)` had different
arities. Reading both files took 30 seconds. The fix took two renames and a
deletion.

## The pattern

When an agent sees a diagnostic — a mypy error, a test failure, a ledger row — the
reflex is to classify it: put it in a bucket, give it a category name, estimate
its complexity, plan the work. This is software project management. It treats
diagnostics as data to be organized.

Diagnostics are not data. Each one is a pointer — a file path and a line number —
that says "look here." The only correct response to a diagnostic is to follow the
pointer and read the code. Classification, taxonomy, and planning come AFTER
understanding, not before.

## The test

Before you name a problem, before you categorize it, before you estimate it: have
you read both files? The one with the error AND the one the error points at? If
not, you are not solving a problem. You are moving data around.

## Related

- `category-spec-rotten-core-indicators`: Red flag 2 (cross-referencing as
  substitute for reasoning), red flag 4 (strategy documents instead of concrete
  deliverables), red flag 10 (word salad complexity for simple issues).
- `mathematical-sanity-check`: "Is this absurd?" before committing.
- `category-spec-stub-classification-rule`: The specific override-error comedy
  narrative where the same pattern — classifying instead of reading — produced a
  contaminated stub queue and a rejected 99-file tail.
