# Language style guide

Normative for all issue bodies, comments, plan cards, docstrings, and manifest prose in the Lean/Sage alignment work (#251 and descendants).
The guide incorporates the revisions developed on [#251](https://github.com/dzackgarza/research/issues/251) (2026-07-17). Recorded reversals remain visible in @sec-self-audit because they are evidence for the terminology failures the guide addresses.

## Governing principles {#sec-governing-principles}

[]{#p1}**P1 — Standard-first, relative to a declared corpus and auditor.** Grounding is not bare citability; it is citability *within the reference corpus the intended auditor commands*. The declared corpus is the working mathematician's literature: nLab, the Stacks Project, Kerodon, the standard canon (Higher Algebra/HTT, EGA/SGA-class references, standard textbooks), and math.xx arXiv papers, including specialized ones.
Advanced or niche *mathematics* is fair game; the corpus excludes, as grounding sources for prose: model theory / type theory / formal logic literature, programming-language theory, and Mathlib's naming conventions (anchors, not vocabulary — [P1b](#p1b)).

A term is admissible in mathematical prose iff **(i)** it has a definition in the corpus, and **(ii)** a working mathematician can check any particular use against that definition — misuse must be *detectable* by the intended auditor.
A term with a rigorous definition the auditor does not command is an unauditable degree of freedom — the original disease (inert, unpoliceable assertions) in citation-laundered form.
Citing a corpus the auditor cannot police is authority-laundering, not grounding.
A noun failing (i) or (ii) is a defect; the nearest corpus-standard term is used even when imperfect, with the mismatch stated explicitly.
Coinage is forbidden — and so is invented *definition*: a construction is stated as its corpus definition with a citation, never reconstructed from memory. For an ordinary category, the ordinary nerve is the simplicial set of composable chains. When using simplicial categories to model $\infty$-categories, specify the homotopy coherent nerve ([Kerodon `00KS`](https://kerodon.net/tag/00KS)); on an ordinary category regarded as a simplicial category with discrete mapping spaces, it agrees with the ordinary nerve. A special-case reduction is recorded as a lemma, never presented as the definition.

[]{#p1b}**P1b — Mathlib names are anchors, not prose.** Mathlib declarations appear only code-formatted in identification columns (`ObjectProperty.inverseImage`, `FullSubcategory`), never as prose nouns.
Prose says "isomorphism-invariant predicate on objects", "inverse image of a full subcategory".
The mathematical text stays auditable by mathematicians who have never opened Mathlib — the population the DSL exists to serve.

[]{#p2}**P2 — One term, one type.** Every term carries a declared mathematical type. Common types include an object or morphism in a specified category, an object of **Cat**, a 1-morphism (functor), a 2-morphism (natural transformation), an object property (predicate / replete full subcategory), an invariant (a set-valued function on isomorphism classes, or a specified functorial construction with named codomain), a section (named right inverse to a specified functor), a witness (chosen auxiliary data), or an **obstruction** (a specified class or map together with a theorem stating whether its vanishing is necessary, sufficient, or equivalent to the lifting or extension property under the cited hypotheses).
Using a term at the wrong type is a language error with the same severity as a mathematical error, because it becomes one downstream.

[]{#p3}**P3 — Forgetful functors determine the vocabulary.** For a specified forgetful functor $\iota_A\colon\mathcal S_A\to\mathcal C$, the property / structure / stuff classification is computed from $\iota_A$: full and faithful gives at most property, faithful gives at most structure, and an arbitrary functor gives at most stuff. Repleteness is checked separately when the essential image is replaced by a full subcategory.
But prose must respect the computed class: property-language ("C is P") is legal only when the fiber is contractible; otherwise structure-language is mandatory ("C equipped with", plus a specified choice — [P4](#p4)). The formalism does not case-split; the vocabulary must.

[]{#p4}**P4 — Name every chosen structure.** When $\iota_A$ is not full, lifts are choices and may be many. For a commutative ring $R$, $(R\text{-}\mathbf{Mod},\otimes_R,R)$ and $(R\text{-}\mathbf{Mod},\oplus,0)$ are distinct monoidal categories; for a noncommutative ring, state the appropriate bimodule or right/left module setting. Every chosen lift is specified and named, and every consumer of structure references that lift, never "the" structure.
Unnamed structure-reference is a defect class (lift ambiguity), detectable by grep.
Property-level references are exempt for an object whose fiber is nonempty and contractible. Full faithfulness of `ι_A` proves that every nonempty fiber is contractible; fullness alone does not.

[]{#p5}**P5 — Notation carries claims.** Symbols are typed: $\hookrightarrow$ denotes an inclusion, embedding, or monomorphism; `=` vs `≅` vs `≃` are distinct claims; strict vs pseudo (2-)pullback is stated.
Fullness, faithfulness, and repleteness are stated explicitly; the arrow glyph does not assert them by itself.

[]{#p6}**P6 — Layer quarantine.** Mathematical prose and implementation prose never share vocabulary.
Terms with no mathematical analogue (rollup owner, route audit, anti-bypass, conformance, manifest, dispatch) are legal only in the implementation map from the presentation to code, and mathematical terms are never overloaded to mean implementation artifacts.
The gradient never flows upward: a term needed to talk about the machinery must not appear in the mathematics the machinery expresses.

[]{#p7}**P7 — One name, one definition site.** Each object, notion, or construction has exactly one name or notation and one anchored defining occurrence across the corpus.
The defining occurrence gives the full definition and may introduce one shorthand. Later uses cite that occurrence and reuse the established name or shorthand. A local reminder may repeat the type signature or notation needed to parse a sentence, but it does not state a second definition or redraw the defining diagram as though new. A worked example may instantiate the definition when it cites the defining occurrence and adds new mathematical content. A second name or definition for the same object is a defect; replace it with the established name and reference its defining occurrence.

## The admissibility taxonomy (three ways a term fails) {#sec-admissibility}

**Class A — foreign-discipline technical terms.** Rigorously defined, but in a literature the auditor does not command: model theory ("interpretation", "signature", "sort", "theory" in the logician's sense), type theory ("judgment", "elaboration" as prose), universal-algebra register, PL theory.
The *most* dangerous class, strictly worse than nonsense: they read as either colloquial or authoritative, the auditor cannot tell which, and cannot detect abuse — any concept can be tagged with them, unfalsifiably.
Banned in mathematical prose regardless of correctness.
(Niche mathematics is not in this class: "corestriction", "replete", "isofibration", "pseudo-pullback" sit in the declared corpus, one nLab lookup from auditable.
The boundary is *which literature*, not *how well-known*.)

**Class B — project-specific coinage and LLM-isms.** "Landing refinement", "specimen",
"spine", "cut", "seed", and "tether" may have standard meanings elsewhere, but the
ungrounded project-specific meanings at issue here have no definition to audit.
Those uses are visibly nonstandard, hence less dangerous than Class A; they remain banned,
with the @sec-replacement-dictionary replacements.

**Class C — colliding overloads.** A corpus word repurposed with a second meaning ("kernel" for a codebase, "core" for centrality, "fiber" for a locus).
Audit is actively misled: the auditor applies the corpus definition and reaches wrong conclusions.

## Replacement dictionary (organizational → standard) {#sec-replacement-dictionary}

| Deprecated | Replacement |
| --- | --- |
| ontology | diagram in **Cat**; categorical presentation only when generators, relations, and closure operations are specified |
| project lexicon | the defined terms of the presentation: its generators (categories, functors), predicates, and named constructions — a glossary with types, not a logic-theoretic "signature" (that translation itself violated [P1](#p1) and is withdrawn) |
| corpus (for the generated object) | generated sub-2-category |
| graph, tree (for the whole object) | 2-diagram in **Cat**; "tree" only for an actual poset that is one |
| node | category (object of **Cat**) |
| edge | functor (1-morphism of **Cat**) |
| seed | generator |
| constructor | categorical construction / 2-functor |
| cut, axiom cut | replete full subcategory defined by an object property; specified forgetful functor from a category of structured objects |
| cut owner | category whose objects satisfy the property, or domain of the specified forgetful functor |
| cut instantiation | inverse image of an object property (`ObjectProperty.inverseImage`); pullback of a specified family $E\to B$ when its universal property is stated |
| implication edge | inclusion induced by P ⇒ Q, with witness |
| generation rule / square | pullback of a replete full subcategory along a functor |
| Level-0 generic | general construction; a parameter choice gives an instance |
| operation home | domain, codomain, and type: functor / natural transformation / object property / invariant on the core / n-ary operation with typed source |
| route | composite / factorization of functors |
| preferred route, preferred functor | distinguished functor or factorization (mathematical, with comparison isomorphisms to alternatives) — or dispatch policy (implementation layer; quarantined) |
| routing diamond | commutative square (strict or up to a specified natural isomorphism — say which) |
| tether, alignment | specified equality / isomorphism / equivalence / natural isomorphism / factorization — name the actual claim |
| realization functor | name the actual functor and its source and target; use forgetful or underlying-object functor only when structure is being forgotten, and reserve realization for a defined realization construction |
| witness-level datum | chosen auxiliary data: basis, enumeration, presentation, section |
| free/torsion fiber | restriction to the free / torsion locus (inverse image of the specified full subcategory; not a fiber); add finite only when it is part of the definition |
| unified O | the construction Aut : Core(C) → Grp; O(X) := Aut(X) an instance |
| homsets-as-parents | hom-bifunctor; isomorphism groupoid; torsor of isomorphisms |
| residue | missing definition / unformalized theorem |
| gap row | documented missing formalization (keep — already precise) |
| Synthetic layer | provisional axiomatization (declared axioms and conjectures) |
| base (of an axiom) | state the property or structure and the category whose objects satisfy or support it; for a classifying fibration, name its domain, codomain, and universal property |
| transport (of an axiom); "axiom transported to $\mathcal C$" | pullback of the specified family along the named functor, when that family and its universal property have been defined |
| owned at / ownership (of an axiom) | property of objects of the named category; chosen structured object in the fiber of a specified forgetful functor $U\colon\mathcal S\to\mathcal C$ |

Rules following from the table:

- A set-valued isomorphism invariant is a function $\pi_0(\operatorname{Core}(\mathcal C))\to S$, with any evaluation witness recorded as auxiliary data. An invariant construction with a richer codomain states its source, target, and functoriality.

- A comparison between functors, regarded as 1-cells in **Cat**, is a natural transformation or other specified 2-cell. A map between objects of a category is a morphism in that category. Generated 2-cells are marked as such.

- When the target is a replete full subcategory, a theorem about where a construction lands is stated as a factorization through its inclusion, established by a proof or cited theorem. For any other target, state the actual codomain or subobject.

- Set-level and groupoid-level constructions are not interchanged: $\pi_0$ need not commute with homotopy pullbacks; state which truncation is meant, where it is applied, and any hypotheses under which it preserves the construction.

- "Minimal graph" is meaningless unqualified: minimality is relative to required targets, permitted closure operations, and an equivalence on presentations — an inclusion-minimal generating subdiagram, not necessarily unique.

## Formation conventions {#sec-formation-conventions}

- **Working 2-category**: `Cat_𝒰` of 𝒰-small categories, functors, natural transformations; coherence claims name their 2-cells.

- **Pullbacks**: use pseudo-pullbacks unless the relevant leg is an isofibration. A strict pullback along an isofibration represents the pseudo-pullback up to equivalence; a replete full inclusion is an isofibration. Never write literal equality between the strict and pseudo constructions.

- **Repleteness**: a full subcategory defined by an isomorphism-invariant object property is replete. A predicate not invariant under isomorphism may define a full subcategory, but that subcategory need not be replete.

- **Generation**: declared 1-cells are adjacent forgetful functors only; other functors are exhibited as composites or named induced functors. Inverse-image subcategories and Grothendieck constructions contribute inclusion and projection functors. Natural transformations may be whiskered; functors are not. Every generated item is marked as such.
  A declared item provably generable one level down is a defect regardless of correctness.

- **Presheaf-level primitives**: each family of forms is a named presheaf $F\colon\mathcal C^{\mathrm{op}}\to R\text{-}\mathbf{Mod}$ when its comparison identities require $R$-module values. Every identity states the domains and codomains of the named natural transformations involved. For each presheaf $F$, form its category of elements and projection; a natural transformation of presheaves induces the corresponding functor between their categories of elements.

## Standard terms to keep unchanged {#sec-standard-terms}

category of elements, Grothendieck construction, core, arrow category, full subcategory, replete, natural isomorphism, automorphism group, torsor, monoidal / abelian / preadditive category, kernel, cokernel, discriminant form, genus, isometry, classifying object, classifying space, classifying category, total category.
These are already the standard names; do not re-coin them.
Classifying terminology is admissible only when the represented functor or universal property is stated. Otherwise state the property, structure, functor, or family directly.

## Audit hooks (each rule induces a mechanical check) {#sec-audit-hooks}

1. **Grounding**: every noun resolves via the dictionary or a corpus citation; unresolved noun ⇒ red.

2. **Typing**: every registry row carries a declared kind; grammar violations (invariant phrased as operation, comparison drawn as edge) ⇒ red.

3. **Chosen-structure naming**: any use of structure without a specified lift or structured object ⇒ red (grep-detectable).

4. **Arrow honesty**: every arrow glyph matches the stated inclusion, embedding, monomorphism, or functor; fullness, faithfulness, and repleteness are checked from prose or proof, never inferred from the glyph.

5. **Level check**: every declared item is at the lowest level at which it is generated; a declared composite, whiskering, induced functor, or witnessed implication ⇒ red.

6. **Layer quarantine**: implementation vocabulary in mathematical prose (or conversely) ⇒ red.

7. **Kernel–cokernel characterization**: in an abelian category, express monicity, epicity, or isomorphism through kernel and cokernel vanishing when that characterization is used. Outside an additive or abelian setting, state the applicable categorical definition instead.

## Self-audit (recorded reversals, kept visible) {#sec-self-audit}

- "multi-sorted signature" (first edition's replacement for "project lexicon"): Class A, model theory.
  Withdrawn and replaced.

- "semantic / executable interpretation": the first edition explicitly *kept* it on the ground that model theory defines "interpretation" — a textbook Class A error (grounding claimed in a corpus the audience does not command).
  Reversed, and recorded rather than silently edited.

- Mathlib identifiers as prose nouns: demoted to code-formatted anchors ([P1b](#p1b)).

Sweep obligation: the guide's dictionary grows by adding any further coinage found in older artifacts here, never by adjudicating it ad hoc.
