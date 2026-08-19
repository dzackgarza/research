# process-before-patches-policy

---
title: process-before-patches-policy
tags: [process, policy, qc, category-specs, bugs]
status: active
---

## The policy

When encountering embarrassing, fundamental errors (e.g. `_QQ` declaring both `_Fields` and `_NumberFields` as supercategories, which is mathematically idiotic for a category tree), the correct response is NOT to patch the individual bug.

The correct response is to patch the PROCESS that allowed it.

## How to execute

1. **Do not immediately edit the file** to fix the typo/graph error.
2. **Create the inspection tooling** so the error is discoverable in the future without an agent stumbling across it.
   - A script that renders the category inheritance graph.
   - A minimal check that flags categories with redundant supercategory lists.
   - A test that fails when a subcategory directly lists an ancestor it could inherit.
3. **Only then** fix the concrete instance.
4. **The fix must include a test** that would have caught the original error.

## Rationale

The presence of the bug is evidence that the process is broken. A world where agents individually patch such bugs one at a time is a world where they will be reintroduced. The only solution is tooling.

## Trigger

This policy applies to any category graph defect, any misnamed category, any mathematically absurd supercategory list, any duplicate method owner, or any inheritance violation that a human would immediately identify as "embarrassing, idiotic."

For process defects caused by agent reasoning, patch the retrieval path, not a
historical case-study file. The rule must appear where a future agent doing the same
kind of work will naturally look: startup purpose, category-spec workflow, sanity
checks, red flags, correction handling, or the relevant domain-specific memory.
