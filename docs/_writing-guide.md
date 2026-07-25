# Agent writing and audit guide

This is the non-rendered policy for agents that write, reorganize, or audit the book. The
leading `_` keeps Quarto from publishing it. It is not a human contribution chapter and
none of its threat-model vocabulary, pattern catalogues, audit machinery, or delegation
contracts belongs in the rendered book.

This is a **policy index**. Each item has a citable id, a concrete banned example, and —
where it applies — the remediation, so a single example teaches the pattern. Items are
separated into three kinds by what a violation actually is:

- **Prose tells (`PR-*`)** — recurrent AI-writing register.
- **Evasion tells (`EV-*`)** — prose that stands in for avoided mathematical work; the
  remediation is to *do the work* (name the morphism, write the definition).
- **Mathematical tells (`MA-*`)** — colloquial or reinvented parlance in place of the
  standard notion or the established in-repo definition; the remediation is to *use the
  definition*.

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

## The standard

Write as a mathematician writes: definitions, theorems, constructions, and remarks in
standard register. The book does not describe itself, announce what it is, tell the reader
how to read it, or characterize a notion by contrast with the notion it rejects. A
definition is a sentence with quantifiers and conditions ("Let … . We say … iff …"), not a
string of adjectives. Significance is shown by use, never asserted.

## From agent feedback to policy

Every piece of writing feedback is checked against this index before it is applied: is it
an instance of a recorded item? If so, fix it and cite the item. If it is a **new**
pattern, record it here — forward-facing, with an example and remediation — *before or
alongside* fixing the instance. A correction that fixes one sentence and leaves the pattern
unrecorded will recur; the index is where a one-off correction graduates into a policy an
auditor can apply everywhere. Run the index as part of the fresh-context pass after every
substantive edit; self-review misses these, because the contaminated cadence reads as
fluent.

Each item below reads: **id — name.** the pattern; *Banned:* a real example; *Fix:* the
remediation.

---

## Prose tells (`PR-*`)

Bad prose on its own terms. The fix is a rewrite; no mathematical content changes.

**PR-1 — Self-narration.** The prose describes what the document is or does instead of doing
it. *Banned:* "This is the framework that situates the conversion; it is mathematics, not
procedure." *Fix:* "The specified forgetful functor, its pullbacks, and the intersections
of replete full subcategories used in the Sage-to-Lean conversion." State the content; do
not characterize the text.

**PR-2 — Reflexive negative parallelism.** A notion is characterized by contrast with the
alternative it rejects: "X, not Y" / "is X, never Y" / "not just X but Y" / "X rather than
Y". The most frequent tell in this corpus. *Banned:* "$a = b$ is a theorem, never a
definitional identity." *Fix:* state the positive claim and stop; if the contrast carries
information, make it a Remark and explain it in context.

**PR-3 — Self-certification.** The text asserts it satisfies a property — dependency order,
completeness, minimality, "the single source", "canonical", "self-contained" — which no
sentence can make true; only the artifact and an independent check can. A false
self-certification is worse than none. *Banned:* "The definitions and results …, in
dependency order."; "the single source for the … machinery." *Fix:* delete the assertion;
if the property is required, record it under [Requirements](#requirements) where an auditor
checks it against the artifact.

**PR-4 — Theory of mind.** The prose tells the reader what the mathematics implies or how to
read it — work the definitions already do. *Banned:* "equality, isomorphism, and equivalence
are distinguished and named wherever the distinction is content." *Fix:* delete; distinct
definitions are already distinct.

**PR-5 — Puffery and AI-vocabulary.** Words that rate the mathematics or belong to the
generic LLM register: "crucial", "pivotal", "powerful", "elegant", "deep", "rich",
"intricate", "interplay", "robust", "seamless", "leverage", "delve", "underscore",
"showcase", "boasts", "foster", "meticulous", "tapestry", "testament", "landscape",
"realm", and the connectives "it is worth noting", "importantly", "note that", "of course",
"clearly" (where it is not). *Fix:* delete the word; state the content plainly.

**PR-6 — Cadence padding.** Structure produced for rhythm: the reflexive rule of three, "not
only … but also", formulaic transitions opening successive sentences ("Additionally",
"Moreover", "Furthermore", "Notably"), conclusion-restatement ("in summary", "as we have
seen"), em-dash or parenthetical density. *Fix:* keep what is needed; cut what is there for
cadence.

**PR-7 — Superficial "-ing" analysis.** A trailing participial clause performs analysis
without adding content. *Banned:* "the pullback is universal, underscoring the classifier's
role." *Fix:* delete the clause, or replace it with the statement it gestures at — a
theorem, a cross-reference, an actual consequence.

**PR-8 — Undue emphasis.** `**bold**` used for emphasis or to mark a defined term in running
prose. *Fix:* *italic* for a term at its definition; **bold** only as a run-in label at the
start of a list item or paragraph ("**In $\mathbf{Set}$.**", "**Remark.**"). Never bold to
weight a clause.

**PR-9 — Formatting tells.** Sentence case in headings, not Title Case ("Axiom classifier",
not "Axiom Classifier"); straight quotes, not curly; no emoji; no collaborative or meta
language ("let me know", "I hope this helps", knowledge-cutoff apologies); no bold-header
bullet lists where prose is clearer.

**PR-10 — Project process inside mathematical exposition.** A mathematical chapter pauses
to discuss rulings, audit procedure, implementation status, editorial policy, or the work
needed to maintain the book. *Banned:* "This ruling guards the conversion pipeline and is
enforced by the audit." *Fix:* state the mathematical proposition in the chapter. Put only
the positive mathematical conventions a human contributor needs in the rendered
contributing chapter. Agent threat-model rules and audit instructions stay in this file;
implementation state stays in its execution record.

---

## Evasion tells (`EV-*`)

Prose that substitutes for mathematical work not done. The tell is stylistic; the defect is
that a definition was not written or an object not named. The remediation is never a nicer
phrase — it is the work.

**EV-1 — Vibe-adjectives for a definition.** Impressive qualifiers replace the definition
itself. *Banned:* "The subcategory is structurally complete under sameness." *Fix:* write
the definition — "A full subcategory $\mathcal D \subseteq \mathcal C$ is *replete* if
every object of $\mathcal C$ isomorphic to an object of $\mathcal D$ belongs to
$\mathcal D$." "Structurally complete under sameness" is a mood; the definition is the
work.

**EV-2 — Carrier / "carries".** "carries" and "carrier" suppress the data that constitute a
structure. *Banned:* "objects that carry both structures"; "an object together with a
carried structure"; "the underlying set carries the operation." *Fix:* name the
operations, relations, and axioms, or specify the forgetful functor and the chosen object
in its fiber. A representative of a subobject of $M$ is a monomorphism
$f\colon N\hookrightarrow M$, and subobjects are isomorphism classes of such
monomorphisms. A structure on $X$ is a chosen object in the fiber over $X$ of a specified
forgetful functor $U\colon \mathcal S\to\mathcal C$; the underlying set is the value
$U(X)$. Avoid "carried" even when the structure data have been named. Banned outright in
the [AGENTS.md](../AGENTS.md) index.

**EV-3 — Engineering collective nouns.** "package", "frame", "pipeline", "suite", "layer",
and a vague "slice" gather mathematical objects under a process or software noun instead
of naming them. *Banned:* "the discriminant package"; "the forms frame"; "the equality
slice". *Fix:* "the discriminant construction and its exact sequences"; "the categories
$\mathcal B_{R,W}$ and $\mathcal Q_{R,W}$"; the exact chapter, section, or mathematical
construction meant. The standard slice category $\mathcal C/X$ remains admissible after
it is defined; the failure is the undefined organizational use.

**EV-4 — Vague hedges for precision.** "essentially", "basically", "morally", "roughly", "in
some sense" used where an exact statement is owed. *Fix:* state it exactly, or, if a genuine
approximation is meant, name the sense ("up to isomorphism", "to first order").

---

## Mathematical tells (`MA-*`)

Colloquial or reinvented parlance in place of the standard notion, or of the definition the
repo already fixes. The remediation is the established definition — cite it.

**MA-1 — Prior substitution for the book's definition.** An agent writes the definition it
recalls from training or an external source without reading the book's defining
occurrence. The result may be standard mathematics and still contradict the internal
logic of the book. *Banned:* writing $a=b$ after the book has constructed only an
isomorphism $a\cong b$; calling a map a "classifier" without the universal property
required at its defining occurrence. *Fix:* read and cite the book's anchor. If that
definition conflicts with the literature, correct it at the defining occurrence and then
repair its dependents; do not shadow it locally.

**MA-2 — Coinage for a standard notion.** A private word stands in for a notion with a
standard name. *Banned:* "cut" / "axiom cut" (→ full subcategory defined by a property, or
specified forgetful functor); "refinement" for a subcategory (→ full subcategory); "least common
category" (→ a greatest lower bound in the specified preorder of categories, if it
exists). *Fix:* the standard term or the
repo's term; full inventory and citations in `.agents/references/terminology-dictionary.md`.

**MA-3 — Notation colliding with a standard meaning.** A symbol is reused against its
near-universal reading. *Banned:* "$\mathbf{Sh}_\Sigma$" for a diagram/functor category
("$\mathbf{Sh}$" is sheaves). *Fix:* a non-colliding symbol ("$\mathbf{Dia}_\Sigma$"), or the
plain construction ($\operatorname{Fun}(\Sigma, \mathcal C)$).

**MA-4 — Elegant variation.** The same object is renamed sentence to sentence to avoid
repetition, so one notion acquires several names. *Fix:* repeat the exact term. The
rendered [mathematical authoring
conventions](contributing/Mathematical-Language-Style-Guide.md) require notation to retain
its typed meaning; the agent tell here is the reflex to vary the word.

**MA-5 — Borrowed technical term without a definition.** A word that carries a specific
technical meaning (character, spectrum, kernel, index, module) is used loosely and left
undefined, so a mathematician reads it as *the* technical term and hunts for a definition
that is not there — it signals precision and delivers none, describing less than a plain
word would. *Banned:* "the character of an axiom" (read as a group/representation character;
no such notion is defined). *Fix:* state the truncation level of the homotopy fibers of
the specified functor, or name the defined object property actually meant.

**MA-6 — Cardinality label for an incidental count.** Naming a structure by how many things
it has — "trichotomy", "dichotomy", "the three-fold", "$N$-fold" — asserts the count is
mathematically load-bearing. Use it only when the argument turns on exactly that many cases
(the *trichotomy law* of an ordered field, where $<, =, >$ is the content). *Banned:* "the
stuff / structure / property trichotomy" — nothing turns on "three"; the classification is
by fullness and faithfulness and, in higher categories, by the truncation level of the
homotopy fibers. *Fix:* name the classification by content, not by tally.

**MA-7 — Backwards or premature notation.** A symbol is introduced with `:=` pointing from
the standard, primitive notation to the coinage, or coined notation is used before it is
defined (see [Requirements](#requirements), definition before use). *Banned:* "$E_A :=
B_A.A$" before either notation has a defining occurrence. *Fix:* first specify the family
$p_A\colon E_A\to B_A$ and the map $\chi\colon\mathcal C\to B_A$, then draw their pullback.
Only afterward introduce the shorthand $\mathcal C.A$ for its apex. A specialization such
as the pullback along $\operatorname{id}_{B_A}$ is stated with its canonical isomorphism,
not used to define the family backwards.

**MA-8 — Compressed notation where the diagram is owed.** A pullback written as the apex
$A \times_C B$, or a universal family named only by its classifying map $S \to M$, in place
of the cartesian square that records the projections and the universal property. *Banned:*
"the family is the base change $S \times_M U$"; "$S \to M$ classifies the family" as the
whole of it. *Fix:* draw the square (`tikzcd`) with both legs and the corner mark, and use
fiber-product notation only as a named shorthand for the apex once its square is drawn —
the [universal-construction convention](contributing/Mathematical-Language-Style-Guide.md#universal-constructions-and-diagrams).

**MA-9 — Colloquial "ownership" for a mathematical relation.** "owns", "owned at", and
"ownership" replace the relation that should be stated. *Banned:* "commutativity is owned
at $\mathbf{Mag}$"; "the node that owns the property"; "the object owns its local
invariants". *Fix:* name the relation — "commutativity is a property of magmas", "the
category whose objects satisfy the property", "the invariants are defined on the
object".
(Organizational "owned by" a wiki, doc, or issue — surface responsibility, not mathematics —
is a separate, admissible sense.)

**MA-10 — Classifier language without a universal property.** "classifier", "classifying
category", and "universal family" are used as labels before a representing or universal
property is stated. *Banned:* "$u_A\colon E_A\to B_A$ is the axiom classifier" with no
description of the objects it classifies or the equivalence it represents. *Fix:* state
the property or structure directly. If a classifying object or fibration exists, state
its universal property and call a change along a functor the pullback family.

**MA-11 — An arrow without a typed map.** A diagram connects mathematical nouns because
they are related in the author's head, without naming a functor, natural transformation,
or map having the displayed source and target. *Banned:* an object-to-category edge for
membership; a discriminant arrow from the full lattice category when the construction is
functorial only on its core; an unlabeled edge whose direction could mean either inclusion
or forgetting structure. *Fix:* write the actual source, target, and arrow label. Replace
membership by prose, restrict a construction to its stated domain, and display a
set-valued invariant as a map from $\pi_0$.

---

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

- this guide and the [mathematical authoring
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
