---
title: Category Spec Subtrees
status: active
date: 2026-05-29
---
# Category Spec Subtrees

This skill is the canonical subtree-ownership guide for `category_specs/`.

## Canonical source

The source of truth is this memory plus `mem:skills/category-spec-subtrees/subtrees`.

Read `mem:skills/category-spec-subtrees/subtrees` before editing a category-specific
subtree, moving methods between subtrees, writing subtree-specific tests, or deciding
whether a method belongs in generic Cat/Hom/End/Aut infrastructure or a specialized
category.

## Core policy

- `category_specs/AGENTS.md` is the only subtree AGENTS entry point.
- Lower nested `AGENTS.md` files were migrated here to avoid many always-loaded
  mini-manuals.
- Load `category-spec-style` for spec/code compliance and read
  `mem:skills/category-spec-workflow` for cards, status, plans, failed-assertion
  classification, or delegation.
- Use this skill for local ownership rules: which subtree owns which mathematical
  surface.

## Referenced documents

[Category Spec Subtree Ownership](category-spec-subtrees/subtrees)
