# Theory Index

This directory is the visible, human-facing mathematical knowledge base for the research repo. It is not a task tracker, agent process log, implementation manual, or onboarding README.

Detailed implementation notes, backend manuals, algorithm plans, and preserved spec backups live in the IWE memory library under `.agents/memories/theory/`. Use `iwe tree` from the repo root to navigate them.

Implementation in this repo is agent-driven. Visible theory docs should support human direction, design, steering, source validation, and spec review rather than step-by-step implementation execution.

Use this routing:

- `references/` for source authority: literature index, BibTeX, claim map, and extracted literature.
- `foundations/` for durable mathematical background and definitions that humans may review directly.
- `moduli/` for Coble/K3/Enriques moduli claims and period-domain background.

External source code belongs under `src/external/`, not `theory/`. If non-code external
reference payloads are needed later, route them through `references/` or a clearly named
theory subdirectory whose role is source authority rather than executable code.

Before using a visible theory file as authority, identify its role. Source authority comes from `references/`; IWE memories explain how agents should compute or implement, but they do not replace literature-backed claims.
