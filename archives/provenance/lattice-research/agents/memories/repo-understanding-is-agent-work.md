---
title: Repo Understanding Is Agent Work
date: 2026-05-28
status: active
---

# Rule: Do not defer to "someone who understands the repo" when the repo contains the evidence

If the relevant source files, design memories, docs, reports, and tests are available,
understanding them is the agent's job.

## Banned language and behavior

- "This needs someone who understands the repo."
- "This should be documented for future resolution."
- "A future agent should decide."
- "I cannot classify this without owner input" before reading the source and design
  memories.
- producing vague terms like "design question," "variance issue," or "Liskov concern"
  without showing the concrete conflicting definitions.

## Allowed escalation

Only after:

- reading the relevant code;
- identifying the exact mathematical ambiguity;
- stating the smallest coherent alternatives;
- explaining why the repo itself does not decide between them.

If you cannot name the precise missing fact, you are not blocked. You have not understood
the issue yet.
