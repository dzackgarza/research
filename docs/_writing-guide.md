# Writing guide — prose policy for the docs

Authoring and audit reference for the mathematical prose in this book. It ships with the
docs but is **not a rendered chapter** (the leading `_` keeps Quarto from rendering it):
it is guidance for writers and auditors, not part of the exposition.

This is a **policy index**. Each item has a citable id, a concrete banned example, and —
where it applies — the remediation, so a single example teaches the pattern. Items are
separated into three kinds by what a violation actually is:

- **Prose tells (`PR-*`)** — bad prose regardless of intent: AI-writing register.
- **Evasion tells (`EV-*`)** — prose that stands in for avoided mathematical work; the
  remediation is to *do the work* (name the morphism, write the definition).
- **Mathematical tells (`MA-*`)** — colloquial or reinvented parlance in place of the
  standard notion or the established in-repo definition; the remediation is to *use the
  definition*.

Related references (this guide does not repeat them): admissible vocabulary is the rendered
[Language Style Guide](contributing/Mathematical-Language-Style-Guide.md); citation-backed
drift rows are `.agents/references/terminology-dictionary.md`; code and work-selection
smells are `.agents/references/slop-pattern-index.md` and `displacement-pattern-index.md`;
the fresh-context audit procedure is `.agents/references/mathematical-auditor-priming.md`.
External failure model: [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).

## The standard

Write as a mathematician writes: definitions, theorems, constructions, and remarks in
standard register. The book does not describe itself, announce what it is, tell the reader
how to read it, or characterize a notion by contrast with the notion it rejects. A
definition is a sentence with quantifiers and conditions ("Let … . We say … iff …"), not a
string of adjectives. Significance is shown by use, never asserted.

## From feedback to policy

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
enforced by the audit." *Fix:* state the mathematical proposition in the chapter. Put
contribution rules in the contributing part of the book, implementation state in its
public execution record, and audit instructions in the agent-facing policy that governs
the audit.

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

**EV-2 — Carrier / "carries".** "carries" and "carrier" name a structure without naming the
morphism that is the structure — hand-waving past the precision. *Banned:* "objects that
carry both structures"; "an object together with a carried structure"; "the underlying set
carries the operation." *Fix:* name the morphism or section — a representative of a
subobject of $M$ is a monomorphism $f\colon N\hookrightarrow M$, and subobjects are
isomorphism classes of such monomorphisms; a structure on $X$ is a chosen object in the
fiber over $X$ of a specified forgetful functor $U\colon \mathcal S\to\mathcal C$; the
underlying set is the value $U(X)$ of the forgetful functor. Name a monomorphism or
inclusion directly; avoid "carried" even when the morphism is named. Banned outright in
the [AGENTS.md](../AGENTS.md) index.

**EV-3 — Engineering collective nouns.** "package", "frame", "pipeline", "suite", "layer"
gather mathematical objects under a software noun instead of naming them. *Banned:* "the
discriminant package"; "the forms frame." *Fix:* "the discriminant construction and its
exact sequences"; "the categories $\mathcal B_{R,W}$ and $\mathcal Q_{R,W}$."

**EV-4 — Vague hedges for precision.** "essentially", "basically", "morally", "roughly", "in
some sense" used where an exact statement is owed. *Fix:* state it exactly, or, if a genuine
approximation is meant, name the sense ("up to isomorphism", "to first order").

---

## Mathematical tells (`MA-*`)

Colloquial or reinvented parlance in place of the standard notion, or of the definition the
repo already fixes. The remediation is the established definition — cite it.

**MA-1 — Reinvented established term.** A term the repo defines is used with a meaning from
another notion. *Banned:* writing $a=b$ after constructing only an isomorphism
$a\cong b$; calling a map a "classifier" without stating the universal property it
satisfies. *Fix:* use the standard term and symbol. If a project definition conflicts
with that meaning, repair the defining occurrence; do not propagate the conflict through
later prose.

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
repetition, so one notion acquires several names. *Fix:* repeat the exact term.
(One-term-one-type is the [Language Style Guide](contributing/Mathematical-Language-Style-Guide.md)'s;
the tell here is the reflex to vary the word.)

**MA-5 — Borrowed technical term without a definition.** A word that carries a specific
technical meaning (character, spectrum, kernel, index, module) is used loosely and left
undefined, so a mathematician reads it as *the* technical term and hunts for a definition
that is not there — it signals precision and delivers none, describing less than a plain
word would. *Banned:* "the character of an axiom" (read as a group/representation character;
no such notion is defined). *Fix:* use the defined notion (the *class* of $A$), or, if a new
notion is genuinely meant, define it.

**MA-6 — Cardinality label for an incidental count.** Naming a structure by how many things
it has — "trichotomy", "dichotomy", "the three-fold", "$N$-fold" — asserts the count is
mathematically load-bearing. Use it only when the argument turns on exactly that many cases
(the *trichotomy law* of an ordered field, where $<, =, >$ is the content). *Banned:* "the
stuff / structure / property trichotomy" — nothing turns on "three"; the classification is
by fullness and faithfulness and extends to $k$-stuff. *Fix:* name by content ("the property
/ structure / stuff classification"), not by tally.

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
fiber-product notation only as a named shorthand for the apex once its square is drawn — the
vertical-presentation convention, [Categorical Presentation Principles
M6](contributing/Categorical-Presentation-Principles.md#sec-draw-the-square).

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

## Requirements

Properties the docs must satisfy are recorded here, not asserted inside the prose (PR-3).
Each is auditable against the artifact; independent reality, not a sentence, determines
whether one holds.

- **Definition before use.** A term *and every symbol* is defined before it is used
  (including the universe $\mathcal U$), and chapters and definitions are ordered so that
  dependencies precede dependents (what "dependency order" would have asserted).
- **Models and derived constructions are named.** A weak higher category, mapping space,
  homotopy type, truncation, limit, or completion is not determined by its name alone.
  State the chosen model or universal property, the diagram and transition functors for a
  limit, and the exact functor used for every derived construction. Do not make a
  model-specific formula into an unqualified definition.
- **Definitions and characterizations are distinct.** Define a notion from a cited source
  before giving representable, Yoneda, mapping-space, or other detection criteria. A
  characterization is stated and proved as a theorem with its hypotheses; it is not
  silently promoted to the definition, and an arbitrary property of objects is not
  transferred to representable functors without defining the corresponding functor
  property.
- **Classifier terminology states what is represented.** "Classifier", "classifying
  object", "classifying category", and "universal family" are used only with the
  represented functor or explicit universal property. A specified forgetful functor is
  not called a classifier merely because its fibers record properties or structure.
- **Definitions are corpus-grounded, never invented.** A definition, like a term (Style
  Guide [P1](contributing/Mathematical-Language-Style-Guide.md#p1)), comes from the declared
  corpus (Kerodon, HTT, the Stacks Project, nLab, standard texts) with a citation; a
  plausible definition reconstructed from memory is a defect even when close. For an
  ordinary category, the ordinary nerve is the simplicial set of composable chains. When
  using simplicial categories to model $\infty$-categories, specify the homotopy coherent
  nerve (Kerodon tag `00KS`); on an ordinary category regarded as a simplicial category
  with discrete mapping spaces, it agrees with the ordinary nerve.
- **A reduction is a lemma, not a definition.** Define the general construction; that it
  restricts or reduces to a familiar special case is a remark. Do not present the special
  case as the definition and the general construction as a generalization (Kerodon 002Y,
  "Recovering a Category from its Nerve," is a lemma about the definition `00KS`).
- **Everything checkable resolves.** Citations, cross-references, and anchor links resolve,
  and rendered output is inspected — enforced by `just docs-check` and the fresh-context
  audit, not by prose claiming correctness.
- **Acyclic exposition order.** The chapter and section hierarchy places every
  load-bearing definition, hypothesis, and construction before its first use. A forward
  reference may point to a later example, proof, implementation note, or elaboration only
  when the current statement is already meaningful without it. Moving prose does not
  discharge this requirement until its symbols, anchors, and mathematical prerequisites
  have been checked in the new order.
- **One defining occurrence per fact.** A definition, ruling, or requirement has one anchored defining
  occurrence and is cited elsewhere. A later use may repeat its established notation or
  type signature when needed to parse the sentence; it may not present a second
  definition, redraw the defining diagram as though new, or introduce a synonym. A worked
  example must cite the defining occurrence and contribute an instance or consequence,
  not a disguised restatement.
- **Mathematics and project process occupy separate surfaces.** Mathematical chapters
  contain definitions, constructions, examples, propositions, proofs, and mathematical
  remarks. Contribution rules, editorial decisions, audit instructions, implementation
  status, issue history, and remediation queues belong to their respective contributing,
  agent-facing, or public execution surfaces (`PR-10`).
- **Headings distinguish their contents.** Headings use sentence case and are unique
  within a chapter. A definition, theorem, example, or callout title does not repeat its
  immediately enclosing heading unless the block itself is the only content of that
  section.
- **Adjunctions are drawn, not named.** An adjunction $F \dashv G$ is written as the diagram
  $\adj{\mathcal C}{\mathcal D}{F}{G}$ — the shared `\adj` macro in `docs/_mathjax-macros.html`,
  which renders $\mathcal C$ and $\mathcal D$ with $F$ (right, on top) and $G$ (left, below) —
  with the $\dashv$ stated, never only the prose "$F$ is left adjoint to $G$." Reusable
  notation lives in that macro file, not re-spelled per use.

Record a requirement here when one is introduced; do not let it re-enter the prose as a
self-certification.

## Delegated rewrite contract

Before assigning a chapter or section rewrite, the coordinator gives the writer the
artifact itself, not a summary, together with:

- this guide and the [Language style
  guide](contributing/Mathematical-Language-Style-Guide.md), read in full;
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
