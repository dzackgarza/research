---
title: Category Spec Sage Mapping
status: active
date: 2026-05-29
---
# Category Spec Sage Mapping

Use this skill for Sage-source inventory and mapping work in `category_specs`.

## Required references

Before mapping:

- Read `category_specs/AGENTS.md`.
- Load `category-spec-style` for mathematical ownership and constructor rules.
- Read `mem:skills/category-spec-workflow` for cards, priority, and decisions.

## Mapping workflow

- Start with the Sage written docs, source, signature, and local usage. Sage is the
  source for which names exist: methods, constructors, factory branches, accepted
  inputs, return objects, display methods, and computational helpers. Do not begin from
  project files, current specs, TODO wording, or guessed category names.
- Before editing any mapping row, enumerate the Sage names in the relevant source file
  or class. The work target is the set of Sage methods and constructors, not the set of
  rows already present in the mapping document. If the Sage source has not been
  enumerated, do not patch the mapping.
- For each Sage name, first write the mathematical proposition that explains why the
  construction is defined. The proposition must name the weakest standard category and
  the hypotheses under which the construction exists. Do not assign an owner, project
  class, target file, or migration path until this sentence is written in ordinary
  mathematical language:
  - in any category, morphisms have domains and codomains and compose;
  - in a concrete category, a morphism can be evaluated on elements of its domain;
  - in an additive category, each `Hom(X,Y)` is an abelian group and composition is
    bilinear;
  - in an `R`-linear category, each `Hom(X,Y)` is an `R`-module and composition is
    `R`-bilinear;
  - in an abelian category, kernels and cokernels exist, images and coimages are
    defined, and a morphism is mono or epi exactly when the corresponding kernel or
    cokernel condition holds;
  - `End(X) = Hom(X,X)` carries the identity endomorphism;
  - `Aut(X)` is the group of invertible endomorphisms;
  - a matrix for a morphism exists only after finite free presentations or bases have
    been chosen.
- Put the method in the most general category named by that proposition. A Sage class is
  only evidence that Sage implements the construction in one case. It is not the owner
  of the mathematics.
- Push methods upward until the proposition would become false. Evaluation and
  composition are not module methods; Hom addition is not a finitely generated module
  method; kernels and cokernels are not lattice methods merely because Sage exposes
  them on a lattice-like class. The owner is the most general standard category where
  the construction is defined.
- Translate Sage names into project vocabulary only after both pieces are visible: the
  Sage name and the mathematical proposition that explains it.
- A mapping row is not acceptable unless it contains a sentence of mathematics. The
  sentence must have the form "In [standard category], [construction exists/has
  property], under [hypotheses]." A row that only names a Sage class, a project category,
  a software type, or a coined project phrase has not done the mathematical work.
- Use standard mathematical vocabulary. If the phrase would not be natural to a
  mathematician who has never seen this repository or Sage, replace it with the standard
  category-theoretic, algebraic, or geometric term before continuing. Do not introduce
  local phrases such as software-shaped types, typed containers, implementation layers,
  or provider jargon as substitutes for categories, objects, morphisms, Hom objects,
  subobjects, quotient objects, kernels, cokernels, images, tensor products, or chosen
  presentations.
- Treat documentation-only polishing as a failure mode during mapping. Changing path
  spelling, headings, formatting, row labels, or prose tone is not progress unless it
  corrects the Sage method set, the mathematical proposition, the weakest owner, a
  hypothesis, a return object, or the replacement path for a Sage behavior.
- If the standard category is missing from the project vocabulary, record that missing
  category as the obligation. Do not replace it with a Sage class, implementation layer,
  or project-specific phrase.
- Map each constructor or method to one outcome: an existing category method, a named
  project constructor, an explicit mathematical rejection, a decision card, or a
  research card when evidence is missing.
- Preserve old functionality through a documented replacement path.
- Do not admit variadic Sage calls or broad optional argument bags directly.
- Do not invent software-shaped helper types to avoid naming the mathematics.

## Output routing

- Create `task` or `feature` cards for executable mapping/implementation work.
- Create `decision` cards for unresolved ownership, naming, or admission choices.
- Use `.agents/TODO.md` only for vague findings that still need investigation.
