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
procedure." *Fix:* "The classifier, transport, and intersection machinery for the Sage →
Lean conversion." — state the content, do not characterize the text.

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

---

## Evasion tells (`EV-*`)

Prose that substitutes for mathematical work not done. The tell is stylistic; the defect is
that a definition was not written or an object not named. The remediation is never a nicer
phrase — it is the work.

**EV-1 — Vibe-adjectives for a definition.** Impressive qualifiers replace the definition
itself. *Banned:* "Equality of objects is contextual and witnessed, given as data." *Fix:*
write the definition — "Let $\mathcal C$ be a category and $a,b \in \operatorname{Ob}(\mathcal
C)$; then $a = b$ in $\mathcal C$ if there is an isomorphism $a \to b$." "Contextual and
witnessed" is a mood; the definition is the work.

**EV-2 — Carrier / "carries".** "carries" and "carrier" name a structure without naming the
morphism that is the structure — hand-waving past the precision. *Banned:* "objects that
carry both structures"; "an object together with a carried structure"; "the underlying set
carries the operation." *Fix:* name the morphism or section — a subobject is a pair $(N,
f\colon N \hookrightarrow M)$; a structure is a named lift of a classifier; the underlying
set is the value $U(X)$ of the forgetful functor. ("carried monomorphism/inclusion", where
the morphism *is* named, is fine.) Banned outright in the [AGENTS.md](../AGENTS.md) index.

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
priors instead of that definition. *Banned:* "$a = b$ is a proposition" (a prior — the repo
defines equality as an isomorphism, `@def-equality-of-objects`); "axiom" used loosely, where
the repo's axiom is the universal classifier $u_A \colon E_A \to B_A$
(`@def-axiom-classifier`). *Fix:* use the in-repo definition and cite it; if the definition
seems wrong, fix it at its source, do not shadow it with a prior.

**MA-2 — Coinage for a standard notion.** A private word stands in for a notion with a
standard name. *Banned:* "cut" / "axiom cut" (→ full subcategory defined by a property, or
classifier); "refinement" for a subcategory (→ full subcategory / classifier); "least common
category" (→ the **Meet** of the argument categories). *Fix:* the standard term or the
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
defined (see [Requirements](#requirements), definition before use). *Banned:* "the total
$E_A := B_A.A$" — $E_A$ is the standard universal-bundle total space, $B_A.A$ the coined
shorthand, so the `:=` is reversed; and $\mathcal C.A$ is only defined in the next sentence.
*Fix:* define the primitive directly ($E_A$ is the total), introduce the shorthand once it
has a definition ($\mathcal C.A := \mathcal C \times_{B_A} E_A$), and state the identity in
the correct direction ($B_A.A = E_A$).

**MA-8 — Compressed notation where the diagram is owed.** A pullback written as the apex
$A \times_C B$, or a universal family named only by its classifying map $S \to M$, in place
of the cartesian square that records the projections and the universal property. *Banned:*
"the family is the base change $S \times_M U$"; "$S \to M$ classifies the family" as the
whole of it. *Fix:* draw the square (`tikzcd`) with both legs and the corner mark, and use
fiber-product notation only as a named shorthand for the apex once its square is drawn — the
vertical-presentation convention, [Categorical Presentation Principles
M6](contributing/Categorical-Presentation-Principles.md#sec-draw-the-square).

**MA-9 — Colloquial "ownership" for an axiom's base.** "owns", "owned at", "ownership" name
where an axiom or predicate lives, but there is no ownership relation in the mathematics: an
axiom is a universal fibration (`@def-axiom-classifier`), *defined on* its base $B_A$ by its
universal property, and on any other category it is the pullback (`@def-axiom-through-functor`).
*Banned:* "commutativity is owned at $\mathbf{Mag}$"; "the node that owns the property";
"the object owns its local invariants". *Fix:* name the base — "commutativity is *based at*
$\mathbf{Mag}$", "the node where the property is *defined*", "the invariants *live on* the
object"; the universal property already fixes the base, so no ownership notion is needed.
(Organizational "owned by" a wiki, doc, or issue — surface responsibility, not mathematics —
is a separate, admissible sense.)

**MA-10 — "base" or "transport" for an axiom.** An axiom *is* the universal fibration
$u_A \colon E_A \to B_A$ (`@def-axiom-classifier`); it has no "base" — $B_A$ is the
*classifying category*, $E_A$ the *total category* — and it is not "transported": the *axiom
on $\mathcal C$* is the pullback along the classifying functor, and "axiom transported to
$\mathcal C$" names nothing further (nor is it transport-of-structure,
$a \ast_R b := f(a) \ast_S f(b)$). *Banned:* "$\mathrm{Assoc}$ has base $\mathbf{Mag}$"; "the
property transports to $\mathcal C$". *Fix:* "$\mathrm{Assoc}$ has classifying category
$\mathbf{Mag}$"; "the axiom on $\mathcal C$ is the pullback" — full vocabulary in the
[Language Style Guide](contributing/Mathematical-Language-Style-Guide.md#sec-replacement-dictionary).

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
  replete full subcategory)" — "replete" and "subcategory" are undefined and an equivalence
  is asserted aside. *Fix:* expand into explicit mathematics — "Let $F \colon \mathcal C \to
  \mathcal D$ be a functor; $F$ is *replete* if …, and $\mathcal C$ is a *subcategory* of
  $\mathcal D$ if …; then $F$ is fully faithful iff $\mathcal C$ is a replete subcategory of
  $\mathcal D$." The explicit formalization is the safe default: precise, and demotable to a
  remark, a cited theorem, or a footnote later.
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
  (including the ambient universe $\mathcal U$), and chapters and definitions are ordered so
  that dependencies precede dependents (what "dependency order" would have asserted).
- **Foundational order: primitives before derived.** The ambient weak higher category
  $\mathbf{Cat}_\omega$ is defined before anything internal to it and before "morphism," which
  presupposes it: $\mathbf{Cat}_\omega \to$ internal hom $\to$ cells $\to$ the enrichment tower
  $\mathbf{Cat}_0, \dots, \mathbf{Cat}_\omega := \lim_n \mathbf{Cat}_n$, then "a
  *category* is an object of $\mathbf{Cat}_1$," then equality/equivalence of objects
  immediately. Never define
  the ambient in terms of categories — a category is an object of $\mathbf{Cat}_1$, so that
  inverts the dependency and is circular.
- **Define intrinsically in $\mathbf{Cat}_\omega$; recover the space-level notion as a
  $\Pi$-image.** The theory is synthetic — no simplicial, quasicategorical, or type-theoretic
  model is primitive. Every notion is defined intrinsically at the level of $\mathbf{Cat}_\omega$
  first; the functor $\Pi \colon \mathbf{Cat}_\omega \to \mathbf{Spaces}$ sends a category to its
  homotopy type, and a notion usually stated in $\mathbf{Spaces}$ is the $\Pi$-image of a
  $\mathbf{Cat}_\omega$ notion — defined upstairs, with the space-level version recovered by
  applying $\Pi$, never taken as primitive. Truncation is the endofunctor
  $\tau_{\le n} \colon \mathbf{Cat}_\omega \to \mathbf{Cat}_\omega$ (an object is $n$-truncated
  iff the unit $C \to \tau_{\le n} C$ is an equivalence), not an operation on spaces that objects
  are then tested against.
- **Do not detect by homs; reformulate as a property of a functor, and keep detection a
  theorem.** A definition of the shape "$X$ has $P$ iff $\operatorname{Hom}_C(Y, X)$ has $P$ for
  every $Y$" is detection-by-probes — it reads $X$ through every other object. Reformulate it as
  "$X$ has $P$ iff the representable $h_X = \operatorname{Hom}_C(-, X)$ has $P$", reducing to a
  property of a *functor*, and define $P$ there. The probe form is non-ideal for two reasons: it
  hides the intrinsic $\mathbf{Cat}_\omega$ definition that generalizes and recovers it, and it
  promotes to a definition what should be a theorem. **Detection by probes is a theorem, not a
  definition**: "$P$ holds iff $\operatorname{Hom}(D, -)$ (or its $\Pi$-image) has $P$ for all
  $D$" is a characterization to be proven; using it to *define* $P$ inverts the definition/theorem
  order. A terminal object is $[D, T] \simeq *$; a contractible object is $C \to *$ an equivalence
  in $\mathbf{Cat}_\omega$ — not "$\operatorname{Map}(X, t)$ is contractible for all $X$". Mapping
  spaces are themselves *derived*, $\operatorname{Maps} = \Pi_\infty[-, -]$.
- **Definitions are corpus-grounded, never invented.** A definition, like a term (Style
  Guide [P1](contributing/Mathematical-Language-Style-Guide.md#p1)), comes from the declared
  corpus (Kerodon, HTT, the Stacks Project, nLab, standard texts) with a citation; a
  plausible definition reconstructed from memory is a defect even when close — the nerve is
  *not* "composable chains," it is the homotopy coherent nerve (Kerodon tag `00KS`), of which
  the ordinary nerve is a restriction.
- **A reduction is a lemma, not a definition.** Define the general construction; that it
  restricts or reduces to a familiar special case is a remark. Do not present the special
  case as the definition and the general construction as a generalization (Kerodon 002Y,
  "Recovering a Category from its Nerve," is a lemma about the definition `00KS`).
- **Everything checkable resolves.** Citations, cross-references, and anchor links resolve,
  and rendered output is inspected — enforced by `just docs-check` and the fresh-context
  audit, not by prose claiming correctness.
- **One home per fact.** A definition, ruling, or requirement lives in one place and is
  referenced elsewhere, never restated.
- **Adjunctions are drawn, not named.** An adjunction $F \dashv G$ is written as the diagram
  $\adj{\mathcal C}{\mathcal D}{F}{G}$ — the shared `\adj` macro in `docs/_mathjax-macros.html`,
  which renders $\mathcal C$ and $\mathcal D$ with $F$ (right, on top) and $G$ (left, below) —
  with the $\dashv$ stated, never only the prose "$F$ is left adjoint to $G$." Reusable
  notation lives in that macro file, not re-spelled per use.

Record a requirement here when one is introduced; do not let it re-enter the prose as a
self-certification.

## Not flags

Standard mathematical hedging and signposting that carry real content are not flags:
"provided", "up to isomorphism", "without loss of generality", a genuine sign or
normalization convention, and a Remark that explains a real subtlety in context. The test
is whether removing the phrase removes information. A tagline removes none.
