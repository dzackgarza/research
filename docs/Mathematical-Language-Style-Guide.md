# Mathematical Language Style Guide

Normative for all issue bodies, comments, plan cards, docstrings, and manifest prose in the Lean/Sage alignment work (#251 and descendants).
This is the **final edition** of the guide developed on [#251](https://github.com/dzackgarza/research/issues/251) (2026-07-17): it supersedes the two earlier editions posted there, and its own recorded reversals are kept visible (§ self-audit) because the failure mode they name — auditor vocabulary escaping its own audit — is the one this guide exists to prevent.

## 1. Governing principles

**P1 — Standard-first, relative to a declared corpus and auditor.** Grounding is not bare citability; it is citability *within the reference corpus the intended auditor commands*. The declared corpus is the working mathematician's literature: nLab, the Stacks Project, Kerodon, the standard canon (Higher Algebra/HTT, EGA/SGA-class references, standard textbooks), and math.xx arXiv papers, including specialized ones.
Advanced or niche *mathematics* is fair game; the corpus excludes, as grounding sources for prose: model theory / type theory / formal logic literature, programming-language theory, and Mathlib's naming conventions (anchors, not vocabulary — P1b).

A term is admissible in mathematical prose iff **(i)** it has a definition in the corpus, and **(ii)** a working mathematician can check any particular use against that definition — misuse must be *detectable* by the intended auditor.
A term with a rigorous definition the auditor does not command is an unauditable degree of freedom — the original disease (inert, unpoliceable assertions) in citation-laundered form.
Citing a corpus the auditor cannot police is authority-laundering, not grounding.
A noun failing (i) or (ii) is a defect; the nearest corpus-standard term is used even when imperfect, with the mismatch stated explicitly.
Coinage is forbidden.

**P1b — Mathlib names are anchors, not prose.** Mathlib declarations appear only code-formatted in identification columns (`ObjectProperty.inverseImage`, `FullSubcategory`), never as prose nouns.
Prose says "isomorphism-invariant predicate on objects", "inverse image of a full subcategory".
The mathematical text stays auditable by mathematicians who have never opened Mathlib — the population the DSL exists to serve.

**P2 — One term, one type.** Every term carries a declared categorical type: object of **Cat**, 1-morphism (functor), 2-morphism (natural transformation), object property (predicate / replete full subcategory), invariant (function on isomorphism classes), section (named lift of a classifier), or witness (chosen auxiliary data).
Using a term at the wrong type is a language error with the same severity as a mathematical error, because it becomes one downstream.

**P3 — Uniform formalism, differentiated vocabulary.** All classifiers are functors `ι_A : S_A → Cat`. The property / structure / stuff trichotomy is *computed* from `ι_A` (full + replete ⇒ property; faithful ⇒ structure; general ⇒ stuff), never declared.
But prose must respect the computed class: property-language ("C is P") is legal only when the fiber is contractible; otherwise structure-language is mandatory ("C equipped with", plus a named section — P4). The formalism does not case-split; the vocabulary must.

**P4 — Name every section.** When `ι_A` is not full, lifts are choices and may be many (R-Mod is monoidal under ⊗, ⊕, …). Every lift is a separate theorem row with a name (`RMod^(⊗)`, `RMod^(⊕)`), and every consumer of structure references the named lift, never "the" structure.
Unnamed structure-reference is a defect class (lift ambiguity), detectable by grep.
Property-level facts are exempt because contractibility of the fiber — itself a theorem, discharged once from fullness of `ι_A` — makes the reference unambiguous.

**P5 — Notation carries claims.** Symbols are typed: `↪` asserts full + replete; `=` vs `≅` vs `≃` are distinct claims; strict vs pseudo (2-)pullback is stated.
Writing `↪` for a non-full forgetful is a false assertion, not a stylistic liberty.

**P6 — Layer quarantine.** Mathematical prose and implementation prose never share vocabulary.
Terms with no mathematical analogue (rollup owner, route audit, anti-bypass, conformance, manifest, dispatch) are legal only in the implementation map from the presentation to code, and mathematical terms are never overloaded to mean implementation artifacts.
The gradient never flows upward: a term needed to talk about the machinery must not appear in the mathematics the machinery expresses.

## 2. The admissibility taxonomy (three ways a term fails)

**Class A — foreign-discipline technical terms.** Rigorously defined, but in a literature the auditor does not command: model theory ("interpretation", "signature", "sort", "theory" in the logician's sense), type theory ("judgment", "elaboration" as prose), universal-algebra register, PL theory.
The *most* dangerous class, strictly worse than nonsense: they read as either colloquial or authoritative, the auditor cannot tell which, and cannot detect abuse — any concept can be tagged with them, unfalsifiably.
Banned in mathematical prose regardless of correctness.
(Niche mathematics is not in this class: "corestriction", "replete", "isofibration", "pseudo-pullback" sit in the declared corpus, one nLab lookup from auditable.
The boundary is *which literature*, not *how well-known*.)

**Class B — coinage and LLM-isms.** No definition anywhere: "landing refinement", "specimen", "spine", "cut", "seed", "tether".
Audit against these is vacuous — nothing to check a use against.
Visibly nonstandard, hence less dangerous than Class A; still banned, with the §3 replacements.

**Class C — colliding overloads.** A corpus word repurposed with a second meaning ("kernel" for a codebase, "core" for centrality, "fiber" for a locus).
Audit is actively misled: the auditor applies the corpus definition and reaches wrong conclusions.

## 3. Replacement dictionary (organizational → standard)

| Deprecated | Replacement |
| --- | --- |
| ontology | categorical presentation / diagram in **Cat** |
| project lexicon | the defined terms of the presentation: its generators (categories, functors), predicates, and named constructions — a glossary with types, not a logic-theoretic "signature" (that translation itself violated P1 and is withdrawn) |
| corpus (for the generated object) | generated sub-2-category |
| graph, tree (for the whole object) | 2-diagram in **Cat**; "tree" only for an actual poset that is one |
| node | category (object of **Cat**) |
| edge | functor (1-morphism of **Cat**) |
| seed | generator |
| constructor | categorical construction / 2-functor |
| cut, axiom cut | replete full subcategory defined by a property (full case); forgetful classifier (non-full case) |
| cut owner | category on which the object property is defined |
| cut instantiation | inverse image of an object property (`ObjectProperty.inverseImage`); pullback of the full subcategory |
| implication edge | inclusion induced by P ⇒ Q, with witness |
| generation rule / square | pullback of a replete full subcategory along a functor |
| Level-0 generic | generic construction; its uses are instances |
| operation home | typed signature: functor / natural transformation / object property / invariant on the core / n-ary operation with typed source |
| route | composite / factorization of functors |
| preferred route, preferred functor | distinguished functor or factorization (mathematical, with comparison isomorphisms to alternatives) — or dispatch policy (implementation layer; quarantined) |
| routing diamond | commutative square (strict or up to a specified natural isomorphism — say which) |
| tether, alignment | specified equality / isomorphism / equivalence / natural isomorphism / factorization — name the actual claim |
| realization functor | forgetful / underlying-object functor; concrete realization |
| witness-level datum | chosen auxiliary data: basis, enumeration, presentation, section |
| free/torsion fiber | restriction to the finite-free / finite-torsion locus (inverse image of the full subcategory; not a fiber) |
| unified O | the construction Aut : Core(C) → Grp; O(X) := Aut(X) an instance |
| homsets-as-parents | hom-bifunctor; isomorphism groupoid; torsor of isomorphisms |
| residue | missing definition / unformalized theorem |
| gap row | documented missing formalization (keep — already precise) |
| Synthetic layer | provisional axiomatization (declarations with unproved theorems) |

Rules following from the table:

- An invariant is never phrased as "an operation whose home is X"; it is a function on π₀ of the core, with any evaluation witness (a chosen `X ≃ Fin n`) recorded as witness data, never as the home.

- A comparison is never drawn as an edge between objects; it is a 2-cell, usually generated by whiskering, and generated 2-cells are marked as such.

- A theorem about where a construction lands is a lift through a replete full inclusion, with a citation as witness — never graph data.

- Set-level and groupoid-level constructions are not interchanged: π₀ does not commute with homotopy pullbacks; state which truncation is meant and where it is applied.

- "Minimal graph" is meaningless unqualified: minimality is relative to required targets, permitted closure operations, and an equivalence on presentations — an inclusion-minimal generating subdiagram, not necessarily unique.

## 4. Formation conventions

- **Ambient 2-category**: `Cat_𝒰` of 𝒰-small categories, functors, natural transformations; coherence claims name their 2-cells.

- **Pullbacks**: pseudo-pullbacks unless the leg is an isofibration; replete full inclusions are isofibrations, so for properties strict = pseudo.

- **Repleteness**: every property-defined subcategory is closed under isomorphism; a predicate not invariant under isomorphism may not define a subcategory.

- **Generation**: declared 1-cells are adjacent forgetfuls only; all other functors are composites, inverse images, Grothendieck constructions, or induced/whiskered — marked generated.
  A declared item provably generable one level down is a defect regardless of correctness.

- **Presheaf-level primitives**: form families are declared as presheaves (valued in R-Mod when their comparison identities require it, e.g. `polar ∘ diag = 2`); element categories, projections, and induced functors are generated from presheaf-level natural transformations.

## 5. Standard terms to keep unchanged

category of elements, Grothendieck construction, core, arrow category, full subcategory, replete, natural isomorphism, automorphism group, torsor, monoidal / abelian / preadditive category, kernel, cokernel, discriminant form, genus, isometry.
These are already the standard names; do not re-coin them.

## 6. Audit hooks (each rule induces a mechanical check)

1. **Grounding**: every noun resolves via the dictionary or a corpus citation; unresolved noun ⇒ red.

2. **Typing**: every registry row carries a declared kind; grammar violations (invariant phrased as operation, comparison drawn as edge) ⇒ red.

3. **Section naming**: any use of structure without a named lift ⇒ red (grep-detectable).

4. **Arrow honesty**: `↪` on a non-full functor ⇒ red.

5. **Level check**: every declared item is at the lowest level at which it is generated; a declared composite, whiskering, induced functor, or witnessed implication ⇒ red.

6. **Layer quarantine**: implementation vocabulary in mathematical prose (or conversely) ⇒ red.

## Self-audit (recorded reversals, kept visible)

- "multi-sorted signature" (first edition's replacement for "project lexicon"): Class A, model theory.
  Withdrawn and replaced.

- "semantic / executable interpretation": the first edition explicitly *kept* it on the ground that model theory defines "interpretation" — a textbook Class A error (grounding claimed in a corpus the audience does not command).
  Reversed, and recorded rather than silently edited.

- Mathlib identifiers as prose nouns: demoted to code-formatted anchors (P1b).

Sweep obligation: the guide's dictionary grows by adding any further coinage found in older artifacts here, never by adjudicating it ad hoc.
