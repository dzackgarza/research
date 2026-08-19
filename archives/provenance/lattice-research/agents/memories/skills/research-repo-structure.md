---
title: Research Repo Structure
status: active
date: 2026-05-29
---
# Research Repo Structure

This skill is the canonical repo-structure, cleanup, artifact-preservation, and
directory-placement authority.

## Canonical source

The source of truth is this skill plus `references/repo-structure.md`.

Read `references/repo-structure.md` before creating root-level directories, moving files
between roots, deleting markdown, pruning debris, touching specs, or deciding where an
artifact belongs.

## Core policy

- Root-level `AGENTS.md` stays an index.
  Durable operational detail belongs in skills.
- Specs, review files, theory notes, TODO files, and durable design artifacts are source
  material.
- Never rewrite, modernize, shorten, delete, or align specs to current implementation
  unless the user explicitly asks for that exact edit.
- Broken computations are fixed or deleted; do not preserve broken work with status
  reports, archives, `_old` names, or companion explanations.
- Git history and agent memories are the log.
  The repo should stay forward-facing.
- Do not delete markdown or directories without provenance and user confirmation, except
  pre-authorized pruning of `.orig`, `.sage.py`, and empty directories.

## Placement shortcut

- Reusable trusted code goes in `src/`.
- Verified mathematical tests go in `tests/`.
- Executable plans and cards go in `.agents`; produced artifacts go in their natural
  durable roots.
- The living mathematical paper goes in `paper/`.
- Workstream reports and attachments go in `reports/workstreams/`.
- Exploratory drafts go in gitignored `scratch/`.
- Mathematical notes go in `notes/`.
- Shared theory, reference, and tooling docs go in `theory/`.
- Tracker cards and plans go in `.agents/`.

## Referenced documents

[Research Repo Structure Reference](research-repo-structure/repo-structure)
