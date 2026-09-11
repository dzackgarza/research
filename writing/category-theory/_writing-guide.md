# Agent writing and audit guide

This is the non-rendered policy for agents that write, reorganize, or audit the book. The
leading `_` keeps Quarto from publishing it. It is not a human contribution chapter and
none of its threat-model vocabulary, pattern catalogues, audit machinery, or delegation
contracts belongs in the rendered book.

The shared style policy — prose tells, evasion tells, mathematical tells, axiom rules,
example presentation, definitions, cross-references, citations, diagrams, notation, and
properties/structure — lives in [`../CONTRIBUTING.md`](../CONTRIBUTING.md). That file is
the single source of truth for those entries. This file holds only what is agent-specific:
audience boundary, prior-grounding controls, terminology replacements, the delegated
rewrite contract, and agent verification obligations.

Related references: the positive mathematical conventions for human contributors are the
rendered [Mathematical authoring
conventions](contributing/Mathematical-Language-Style-Guide.md); citation-backed recurring
drift rows are `.agents/references/terminology-dictionary.md`; code and work-selection
smells are `.agents/references/slop-pattern-index.md` and `displacement-pattern-index.md`;
the fresh-context audit procedure is `.agents/references/mathematical-auditor-priming.md`.
External failure model: [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).

## Audience boundary

A convention belongs in the rendered guide only when a mathematician needs it to state
the mathematics correctly: types, chosen structure, model choices, universal properties,
diagrams, notation, or the relation between a primitive construction in
the chosen category of higher categories and its cited specialization in
$\mathbf{Spaces}$.

A rule stays here when its purpose is to counter an agent failure: prose generated from a
language-model cadence, undefined vocabulary imported from priors, a book definition
replaced by a remembered external definition, process text inserted into exposition, or
an audit and delegation control. When the two surfaces touch, the rendered guide states
the positive mathematical convention once; this guide names the agent failure and links
to that convention.

## Prior-grounding controls

These controls govern agents, issue bodies, plans, docstrings, and implementation maps.
They are not mathematical conventions for a human contribution chapter.

- Read the book's defining occurrence and its prerequisites before writing a dependent
  passage. A definition reconstructed from training priors is inadmissible even when it
  resembles a standard definition.
- Check mathematical nouns against literature a working mathematician can audit: standard
  texts and papers, the Stacks Project, Kerodon, and nLab. A term borrowed from model
  theory, type theory, formal logic, universal algebra, or programming-language theory is
  not a substitute for the book's mathematical object merely because that term is defined
  in its own field.
- Lean, Mathlib, and Sage identifiers are code-formatted implementation anchors. They do
  not become prose names or definitions.
- Each mathematical notion has one anchored defining occurrence in the book. Agents cite
  it, preserve its hypotheses, and repair it at that occurrence when it is wrong; they do
  not shadow it with a second local definition or a synonym.
- Implementation vocabulary stays in implementation pages. Mathematical vocabulary is
  not overloaded to name manifests, dispatch rules, conformance records, review routes,
  or other project machinery.

Agent terminology failures have three recurring forms:

- **Foreign-discipline substitution.** A technical term from another field is used where
  the book owes a standard mathematical object and definition.
- **Project or model coinage.** An undefined word such as "spine", "cut", "seat", vague
  "slice", or "carrier" is made to do mathematical work.
- **Colliding overload.** A standard word such as "kernel", "core", or "fiber" is reused
  with a project-management or implementation meaning.

The citation-backed recurring inventory belongs in
`.agents/references/terminology-dictionary.md`. The following book-specific replacements
preserve the controls removed from the former rendered language guide; they are audit
input, not vocabulary for the book.

| Agent or organizational term | Required mathematical statement |
| --- | --- |
| ontology | a specified functor, strict 2-functor, or pseudofunctor into $\mathbf{Cat}$; say *presentation of a category or 2-category by generators and relations* only after specifying those generators, relations, and closure operations |
| project lexicon | the defined categories, functors, predicates, and constructions, each with its type |
| corpus, when used for a generated object | the generated sub-2-category |
| graph or tree, when used for the whole object | a specified functor $I\to\mathbf{Cat}$, or a specified strict 2-functor or pseudofunctor $\mathcal I\to\mathbf{Cat}$; for a finite indexing poset $I$, say *tree-shaped* only when its undirected Hasse diagram is connected and acyclic |
| node | category or object, whichever is meant |
| edge | functor or morphism, whichever is meant |
| seed | generator |
| constructor | the named categorical construction or 2-functor |
| cut or axiom cut | a replete full subcategory defined by an object property, or a specified forgetful functor from structured objects |
| cut owner | the category whose objects satisfy the property, or the domain of the forgetful functor |
| cut instantiation | for $F\colon\mathcal D\to\mathcal C$ and a full subcategory $\mathcal C_P\hookrightarrow\mathcal C$, the full subcategory of $\mathcal D$ on objects $D$ satisfying $P(FD)$; or the pullback of $p\colon E\to B$ along a named map $f\colon X\to B$ |
| implication edge | the inclusion induced by a stated implication, with its proof |
| generation rule or square | the pullback of a replete full subcategory along a functor |
| minimal graph | an inclusion-minimal generating subdiagram relative to stated targets, permitted closure operations, and a specified equivalence relation on the class of presentations; uniqueness is a separate claim |
| Level-0 generic | the general construction and the parameter choice producing the instance |
| operation home | the domain, codomain, and type of the functor, natural transformation, object property, invariant, or operation |
| route | a composite or factorization of functors |
| preferred route or preferred functor | a distinguished functor or factorization with comparison maps, or an implementation dispatch policy confined to an implementation page |
| routing diamond | a commutative square, strictly or up to a specified natural isomorphism |
| tether or alignment | the specified equality, isomorphism, equivalence, natural isomorphism, or factorization |
| realization functor | the actual functor with source and target; use *forgetful functor* only when structure is forgotten and *realization* only for a defined realization construction |
| witness-level datum | the chosen basis, enumeration, presentation, section, or other auxiliary datum |
| free or torsion fiber | for a named functor $F\colon\mathcal D\to\mathcal C$, the full subcategory of $\mathcal D$ on objects mapped into the specified free or torsion full subcategory of $\mathcal C$; add finiteness only when it is a hypothesis |
| unified O | for an ordinary category $\mathcal C$, $\operatorname{Aut}\colon\mathcal C^{\simeq}\to\mathbf{Grp}$, with $O(X):=\operatorname{Aut}(X)$ as an instance |
| homsets-as-parents | the hom-bifunctor, the core groupoid, or $\operatorname{Iso}_{\mathcal C}(X,Y)$, which is a bitorsor under $\operatorname{Aut}(Y)$ on the left and $\operatorname{Aut}(X)$ on the right when $X\cong Y$ |
| residue | the missing definition or unformalized theorem |
| gap row | a documented missing formalization; this already has a precise implementation meaning |
| Synthetic layer | a provisional axiomatization, with its axioms and conjectures declared |
| base of an axiom | the property or structure and the category whose objects satisfy or support it; for a classifying fibration, its domain, codomain, and universal property |
| transport of an axiom | the pullback of the specified family along the named functor, when that family and its universal property have been defined |
| owned at or ownership, when used mathematically | the property of objects of the named category, or a chosen structured object in the fiber of a specified forgetful functor |

### Retired agent substitutions

These corrections remain here because they identify priors that already survived one
round of editing:

- "multi-sorted signature" was introduced as a replacement for "project lexicon" and is
  withdrawn. State the actual categories, functors, predicates, and constructions.
- "semantic interpretation" and "executable interpretation" were retained by appeal to
  model-theoretic terminology and are withdrawn. Name the mathematical functor or the
  implementation operation actually meant.
- Mathlib identifiers were used as prose nouns and are restricted to code-formatted
  implementation anchors.

## From agent feedback to policy

Every piece of writing feedback is checked against the policy index in
[`../CONTRIBUTING.md`](../CONTRIBUTING.md) before it is applied: is it an instance of a
recorded item? If so, fix it and cite the item. If it is a **new** pattern, record it in
`CONTRIBUTING.md` — forward-facing, with an example and remediation — *before or
alongside* fixing the instance. A correction that fixes one sentence and leaves the
pattern unrecorded will recur; the index is where a one-off correction graduates into a
policy an auditor can apply everywhere. Run the index as part of the fresh-context pass
after every substantive edit; self-review misses these, because the contaminated cadence
reads as fluent.

## Parentheticals

A semantic parenthetical is a compression. Before relocating or deleting one, classify it,
and prefer **expansion over compression**: expanding into explicit mathematics is
reversible — the content can be *demoted* to a remark, a footnote, or a parenthetical
later, by choice — whereas a compression is lossy and usually smuggles an undefined term or
an unstated theorem. When in doubt, expand; demotion is a later editorial decision. This
concerns *semantic* parentheticals; a citation or cross-reference that merely sits in
parentheses is not one and is out of scope.

- **Compression artifact** — terse to the point of inscrutability, standing in for a notion
  that needs spelling out. *Banned:* "weak homotopy equivalence (holds; inverts/ignores
  directionality) versus categorical equivalence (fails; preserves it)." *Fix:* expand into
  prose or a definition that states the distinction.
- **Smuggled theorem or equivalence** — "(equivalently, $X$)", an "iff" asserted in a
  parenthesis, often over undefined terms. *Banned:* "full and faithful (equivalently, a
  replete full subcategory)" — a functor is being identified with its essential image and
  an equivalence is asserted aside. *Fix:* expand into explicit mathematics — "If
  $F\colon\mathcal C\to\mathcal D$ is fully faithful, then $F$ induces an equivalence from
  $\mathcal C$ to its replete full essential image in $\mathcal D$." Cite the result and
  define any term not already established. The expanded statement can later be demoted to
  a remark, cited theorem, or footnote.
- **Legitimate qualification** — a small, correct, load-bearing modifier; keep inline.
  *Fine as is:* "fibers are (possibly nontrivial) groupoids."
- **Smuggled example** — "(e.g. …)" carrying a genuine example. *Fix:* promote to a
  first-class example block. *Banned:* "several distinct lifts (e.g. several monoidal
  structures on one category)." *Fix:* an Example environment for the monoidal-structures
  case.
- **Padding or tangent** — carries no load. *Fix:* delete (`PR-6`); a parenthetical is
  usually wrong when it is a tangent.

Judgment is required and the classes overlap; the safe default, when a parenthetical carries
real content, is to expand it into precise mathematics, then choose whether to demote — a
footnote or margin note (`reference-location: margin`) being the home for a genuine but
secondary aside, never for padding.

## Agent verification obligations {#requirements}

The rendered [Mathematical authoring
conventions](contributing/Mathematical-Language-Style-Guide.md) own the positive rules for
types, chosen structure, higher-categorical primitives and space-level specializations,
universal constructions, diagrams, and notation. Definition ownership, source transfer,
and audit procedure are agent obligations:

- Read the complete defining occurrence and its prerequisites before writing a dependent
  passage. A remembered external definition never substitutes for that read.
- Use an external source to support or correct the book's defining occurrence, not to
  introduce a second local definition.
- Check the actual hierarchy for definition-before-use and one defining occurrence. Do
  not certify either property in prose.
- Check that composites, induced functors, inclusions, projections, and whiskered natural
  transformations are derived from their declared constructions rather than introduced as
  unrelated primitives. Natural transformations may be whiskered; functors are composed.
- Compare every relocated destination against its source for definitions, hypotheses,
  domains, codomains, diagrams, citations, examples, warnings, and stable anchors.
- Check every realization claim against the current implementation or generated data.
  State the implemented boundary separately from proposed extensions.
- Keep agent prompts, audits, terminology controls, editorial status, and remediation
  queues out of the rendered book. A rendered contribution page contains only the
  conventions and mathematical information a human contributor needs.
- Resolve citations, cross-references, and anchors; render and inspect the result through
  the repository's declared documentation checks.
- When a diagram fails, render that diagram in isolation and read the first TeX
  diagnostic. A later converter failure is downstream evidence, not the cause.
- Use sentence-case, nonduplicate headings and the book's shared macros. Do not infer
  correctness from formatting or a successful build.
- Send every substantive rewritten artifact through the exact fresh-context audit
  protocol after source comparison.

These are agent obligations, not prose to copy into the book.

## Delegated rewrite contract

Before assigning a chapter or section rewrite, the coordinator gives the writer the
artifact itself, not a summary, together with:

- [`../CONTRIBUTING.md`](../CONTRIBUTING.md) and the [mathematical authoring
  conventions](contributing/Mathematical-Language-Style-Guide.md), read in full;
- the approved chapter → section → subsection slice, including the mathematical purpose
  and prerequisites of each node;
- the exact source files and passages whose mathematical content must be preserved;
- the anchors that own definitions used by the slice, and the facts the writer may move
  but may not redefine;
- explicit non-goals and adjacent files the writer must not edit; and
- acceptance evidence: every source proposition is either preserved, corrected with
  mathematical justification, or recorded as an unresolved contradiction; citations and
  cross-references resolve; the rendered pages are inspected.

After the edit, the coordinator compares the destination against the source for lost
definitions, hypotheses, codomains, diagrams, citations, examples, warnings, and anchors.
An independent fresh-context auditor then receives the rewritten artifact and the
verbatim priming prompt from
`.agents/references/mathematical-auditor-priming.md`. The auditor does not edit the
artifact. Its findings are corrected at the defining occurrence or rejected with a
source showing that the questioned term is standard.

## Not flags

Standard mathematical hedging and signposting that carry real content are not flags:
"provided", "up to isomorphism", "without loss of generality", a genuine sign or
normalization convention, and a Remark that explains a real subtlety in context. The test
is whether removing the phrase removes information. A tagline removes none.