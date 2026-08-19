---
title: Category Spec Ledger Classification — Verify Before Acting
date: 2026-05-27
status: active
---
# Rule: Never Trust a Bucket Name, Count, or Prior Agent Classification

## The principle

A ledger bucket name implies a work type.
A row count implies a scope.
A prior agent's classification implies an owner.
None of these are evidence.
They are hypotheses to be verified before any work is planned or executed.

## The verification step

Before classifying any mypy error into a workstream bucket:

1. **Read the actual error message.** What is the exact code and message text?
2. **Read the failing code.** What file and line is the error on?
   What is the surrounding context?
3. **Trace the intended dependency.** For `@override` errors: where is the base method
   supposed to live? For `attr-defined` errors: what attribute is missing and where is it
   used?
4. **Check the internal graph first.** Does the intended base exist in `category_specs`?
   Does the intended type exist in `category_specs/types.py`?
5. **Only then classify.** If the root cause is internal, it is spec/plugin/graph work.
   If the root cause is a direct external Sage API call with no local type information,
   it is stub work.

## The anti-pattern to avoid

- **Surface-pattern classification**: matching error text to bucket name without reading
  code.
- **Same-name matching**: searching for method names in Sage source and assuming the
  stub is missing them, without checking whether the override chain is internal.
- **Count-driven action**: seeing a large bucket and treating it as a bulk task to be
  cleared, rather than investigating why it is large.
- **Evidence suppression**: removing markers, casts, or annotations to make errors
  disappear rather than fixing the root cause.
- **Authority delegation**: treating prior agent output, issue comments, or ledger
  classifications as ground truth without verification.

## The rule for external workstreams

Before adding any row to an external repo's issue queue (e.g., `sage-stubs`):

1. Can you name the exact `category_specs` file and line where a Sage symbol is called?
2. Can you explain why `category_specs` cannot type the operation without the external
   stub?
3. Have you ruled out internal graph/plugin/spec causes?

If any answer is no, the row does not belong in the external queue.
