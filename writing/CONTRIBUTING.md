# Contributing to the book

This is a mathematical book. Contributions are definitions, theorems,
constructions, examples, and remarks in standard mathematical register.
Each entry below has a code, a banned example, and the replacement.

## Prose (`PR-*`)

Bad prose on its own terms. The fix is a rewrite.

### `PR-1`: Self-narration

The prose describes what the document is or does instead of doing it.

**Banned:** "This is the framework that situates the conversion; it is
mathematics, not procedure."

**Preferred:** "The specified forgetful functor, its pullbacks, and the
intersections of replete full subcategories used in the Sage-to-Lean
conversion." State the content; do not characterize the text.

### `PR-2`: Reflexive negative parallelism

A notion is characterized by contrast with the alternative it rejects.

**Banned:** "$a = b$ is a theorem, never a definitional identity."

**Preferred:** state the positive claim and stop. If the contrast carries
information, make it a Remark and explain it in context.

### `PR-3`: Self-certification

The text asserts it satisfies a property — dependency order, completeness,
minimality, "the single source", "canonical", "self-contained" — which no
sentence can make true.

**Banned:** "The definitions and results, in dependency order."

**Preferred:** delete the assertion. If the property is required, record it
where an auditor checks it against the artifact.

### `PR-4`: Theory of mind

The prose tells the reader what the mathematics implies or how to read it.

**Banned:** "equality, isomorphism, and equivalence are distinguished and
named wherever the distinction is content."

**Preferred:** delete. Distinct definitions are already distinct.

### `PR-5`: Puffery and AI-vocabulary

Words that rate the mathematics or belong to the generic LLM register.

**Banned:** "crucial", "pivotal", "powerful", "elegant", "deep", "rich",
"intricate", "interplay", "robust", "seamless", "leverage", "delve",
"underscore", "showcase", "boasts", "foster", "meticulous", "tapestry",
"testament", "landscape", "realm", and the connectives "it is worth noting",
"importantly", "note that", "of course", "clearly" (where it is not).

**Preferred:** delete the word; state the content plainly.

### `PR-6`: Cadence padding

Structure produced for rhythm.

**Banned:** the reflexive rule of three, "not only … but also", formulaic
transitions opening successive sentences ("Additionally", "Moreover",
"Furthermore", "Notably"), conclusion-restatement ("in summary", "as we have
seen"), em-dash or parenthetical density.

**Preferred:** keep what is needed; cut what is there for cadence.

### `PR-7`: Concept defined by notational payoff

A theorem or property is characterized by its effect on notation rather than
by its mathematical content, using a conversational construction ("is what
licenses", "is what allows", "is what lets us") instead of stating the
theorem and deriving the convention from it.

**Banned:** "Coherence is what licenses the notation
$a_1\otimes\cdots\otimes a_n$ without parentheses."

**Preferred:** "By the coherence theorem, any two parenthesizations of
$a_1 \otimes \cdots \otimes a_n$ are connected by a unique composite of
associators, so the expression is independent of parenthesization;
parentheses are omitted." State the theorem — what is well-defined, and in
what sense — then let the notational convention follow as a consequence.
A standard text may explain that a theorem permits a notational shorthand;
it does not define the theorem as that shorthand's justification.

### `PR-8`: Superficial "-ing" analysis

A trailing participial clause performs analysis without adding content.

**Banned:** "the pullback is universal, underscoring the classifier's role."

**Preferred:** delete the clause, or replace it with the statement it gestures
at — a theorem, a cross-reference, an actual consequence.

### `PR-9`: Construction and verification in one sentence

A single sentence simultaneously constructs an object and verifies its
required properties, hiding the logical structure the reader needs to follow.

**Banned:** "A category with finite products is monoidal with
$a\otimes b$ a chosen product $a\times b$ and $e$ a terminal object, the
three isomorphisms being the unique ones commuting with the projections; this
is the cartesian monoidal structure."

**Preferred:** separate the construction from the verification. "The product
functor $\times\colon\mathcal{C}\times\mathcal{C}\to\mathcal{C}$, together
with a terminal object $\mathbf{1}$ as unit, defines a monoidal structure
on $\mathcal{C}$. The associator $\alpha_{a,b,c}$ and the unitors
$\lambda_a$, $\varrho_a$ are the unique isomorphisms supplied by the
universal property of the product." State the functor, then verify the
axioms. A reader follows construction, then verification; a semicolon-joined
sentence conflates them.

### `PR-10`: Undue emphasis

`**bold**` used for emphasis or to mark a defined term in running prose.

**Preferred:** *italic* for a term at its definition; **bold** only as a
run-in label at the start of a list item or paragraph ("**In
$\mathbf{Set}$.**", "**Remark.**"). Never bold to weight a clause.

### `PR-11`: Formatting tells

**Banned:** Title Case in headings; curly quotes; emoji; collaborative or
meta language ("let me know", "I hope this helps"); bold-header bullet lists
where prose is clearer.

**Preferred:** sentence case in headings; straight quotes; no emoji; no
collaborative or meta language.

### `PR-12`: Project process inside mathematical exposition

A mathematical chapter pauses to discuss rulings, audit procedure,
implementation status, or editorial policy.

**Banned:** "This ruling guards the conversion pipeline and is enforced by
the audit."

**Preferred:** state the mathematical proposition. Project process belongs in
agent-facing files, not in a mathematical chapter.

## Evasion (`EV-*`)

Prose that substitutes for mathematical work not done. The tell is stylistic;
the defect is that a definition was not written or an object not named. The
remediation is never a nicer phrase — it is the work.

### `EV-1`: Vibe-adjectives for a definition

Impressive qualifiers replace the definition itself.

**Banned:** "The subcategory is structurally complete under sameness."

**Preferred:** write the definition — "A full subcategory
$\mathcal D \subseteq \mathcal C$ is *replete* if every object of
$\mathcal C$ isomorphic to an object of $\mathcal D$ belongs to
$\mathcal D$." "Structurally complete under sameness" is a mood; the
definition is the work.

### `EV-2`: Carrier / "carries"

"carries" and "carrier" suppress the data that constitute a structure.

**Banned:** "objects that carry both structures"; "an object together with a
carried structure"; "the underlying set carries the operation."

**Preferred:** name the operations, relations, and axioms, or specify the
forgetful functor and the chosen object in its fiber. A structure on $X$ is a
chosen object in the fiber over $X$ of a specified forgetful functor
$U\colon \mathcal S\to\mathcal C$; the underlying set is the value $U(X)$.

### `EV-3`: Engineering collective nouns

"package", "frame", "pipeline", "suite", "layer", and a vague "slice" gather
mathematical objects under a process or software noun instead of naming them.

**Banned:** "the discriminant package"; "the forms frame"; "the equality
slice".

**Preferred:** "the discriminant construction and its exact sequences"; "the
categories $\mathcal B_{R,W}$ and $\mathcal Q_{R,W}$"; the exact chapter,
section, or mathematical construction meant.

### `EV-4`: Vague hedges for precision

**Banned:** "essentially", "basically", "morally", "roughly", "in some sense"
used where an exact statement is owed.

**Preferred:** state it exactly, or, if a genuine approximation is meant,
name the sense ("up to isomorphism", "to first order").

### `EV-5`: Universal construction left in prose

A construction defined by a pullback, pushout, or another universal square is
abbreviated as "obtained by pulling back" or an equivalent prose instruction.

**Banned:** "Define $E\to X$ by pulling back $p\colon U\to B$ along
$f\colon X\to B$."

**Preferred:** draw the actual commutative square, label every morphism, mark
it cartesian or cocartesian, and name the resulting object and structure
morphism in the diagram. The prose may state the universal property after
the diagram; it never replaces the diagram.

### `EV-6`: "Data" for a mathematical object

A construction operates on objects, morphisms, 2-cells, or elements of a
specified category. "Data" names none of them; it is a programmer's
abstraction standing where a mathematical object belongs.

**Banned:** "a construction that transports data along $\alpha$, $\lambda$,
or $\varrho$."

**Preferred:** name the things the construction operates on — "a construction
that composes a cell with $\alpha$, $\lambda$, or $\varrho$." The word "data"
erases the type; the replacement names it.

### `EV-7`: Metaphor for an unnamed operation

A sentence says something "transports", "carries", "flows", or "moves" along
a map or cell without naming the categorical operation — composition,
whiskering, application, base change, conjugation — that performs it.

**Banned:** "transports data along $\alpha$."

**Preferred:** name the operation — "composes with $\alpha$", "applies
$\alpha$ to the cell", "whiskers $\alpha$ against $F$." The metaphor hides
which operation; the replacement states it.

### `EV-8`: Universal property invoked but not stated

A sentence appeals to "the projections", "the universal property", or "the
unique map" without stating which universal property, from which object, to
which target. The uniqueness is real, but the reader cannot verify it
without the property identified.

**Banned:** "the three isomorphisms being the unique ones commuting with the
projections."

**Preferred:** "the associator $\alpha_{a,b,c}$ and the unitors
$\lambda_a$, $\varrho_a$ are the unique isomorphisms supplied by the
universal property of the product." Name the universal property and the
object that supplies it.

## Mathematical tells (`MA-*`)

Colloquial or reinvented parlance in place of the standard notion, or of the
definition the book already fixes. The remediation is the established
definition — cite it.

### `MA-1`: Prior substitution for the book's definition

An agent writes the definition it recalls from training or an external source
without reading the book's defining occurrence.

**Banned:** writing $a=b$ after the book has constructed only an isomorphism
$a\cong b$; calling a map a "classifier" without the universal property
required at its defining occurrence.

**Preferred:** read and cite the book's anchor. If that definition conflicts
with the literature, correct it at the defining occurrence and repair its
dependents; do not shadow it locally.

### `MA-2`: Coinage for a standard notion

A private word stands in for a notion with a standard name.

**Banned:** "cut" / "axiom cut" (→ full subcategory defined by a property, or
specified forgetful functor); "refinement" for a subcategory (→ full
subcategory); "least common category" (→ a greatest lower bound in the
specified preorder of categories, if it exists).

**Preferred:** the standard term or the book's term.

### `MA-3`: Notation colliding with a standard meaning

A symbol is reused against its near-universal reading.

**Banned:** "$\mathbf{Sh}_\Sigma$" for a diagram/functor category ("$\mathbf{Sh}$"
is sheaves).

**Preferred:** a non-colliding symbol ("$\mathbf{Dia}_\Sigma$"), or the plain
construction ($\operatorname{Fun}(\Sigma, \mathcal C)$).

### `MA-4`: Elegant variation

The same object is renamed sentence to sentence to avoid repetition, so one
notion acquires several names.

**Preferred:** repeat the exact term. Notation retains its typed meaning
throughout the book.

### `MA-5`: Borrowed technical term without a definition

A word that carries a specific technical meaning (character, spectrum, kernel,
index, module, classified by) is used loosely to describe something that has
a different, standard name. A mathematician reads it as the technical term
and finds no matching definition — the word signals precision and delivers
none.

**Banned:** "the character of an axiom" (read as a group/representation
character; no such notion is defined); "the bilinear map classified by
$\mu$" (classified by means a classifying object represents a functor;
the correspondence is the tensor-hom adjunction).

**Preferred:** state the actual correspondence or property. "The bilinear
map $A\times A\to A$ corresponding to $\mu$ under the tensor-hom
adjunction." Use the standard name for the standard notion.

### `MA-6`: Cardinality label for an incidental count

Naming a structure by how many things it has — "trichotomy", "dichotomy", "the
three-fold", "$N$-fold" — asserts the count is mathematically load-bearing.

**Banned:** "the stuff / structure / property trichotomy" — nothing turns on
"three"; the classification is by fullness and faithfulness and, in higher
categories, by the truncation level of the homotopy fibers.

**Preferred:** name the classification by content, not by tally.

### `MA-7`: Backwards or premature notation

A symbol is introduced with `:=` pointing from the standard, primitive
notation to the coinage, or coined notation is used before it is defined.

**Banned:** "$E_A := B_A.A$" before either notation has a defining occurrence.

**Preferred:** first specify the family $p_A\colon E_A\to B_A$ and the map
$\chi\colon\mathcal C\to B_A$, then draw their pullback. Only afterward
introduce the shorthand.

### `MA-8`: Compressed notation where the diagram is owed

A pullback written as the apex $A \times_C B$, or a universal family named only
by its classifying map $S \to M$, in place of the cartesian square that
records the projections and the universal property.

**Banned:** "the family is the base change $S \times_M U$"; "$S \to M$
classifies the family" as the whole of it.

**Preferred:** draw the square (`tikzcd`) with both legs and the corner mark,
and use fiber-product notation only as a named shorthand for the apex once its
square is drawn.

### `MA-9`: Colloquial "ownership" for a mathematical relation

"owns", "owned at", and "ownership" replace the relation that should be
stated.

**Banned:** "commutativity is owned at $\mathbf{Mag}$"; "the node that owns
the property"; "the object owns its local invariants".

**Preferred:** name the relation — "commutativity is a property of magmas",
"the category whose objects satisfy the property", "the invariants are
defined on the object".

### `MA-10`: Classifier language without a universal property

"classifier", "classifying category", and "universal family" are used as
labels before a representing or universal property is stated.

**Banned:** "$u_A\colon E_A\to B_A$ is the axiom classifier" with no
description of the objects it classifies or the equivalence it represents.

**Preferred:** state the property or structure directly. If a classifying
object or fibration exists, state its universal property and call a change
along a functor the pullback family.

### `MA-11`: An arrow without a typed map

A diagram connects mathematical nouns because they are related in the author's
head, without naming a functor, natural transformation, or map having the
displayed source and target.

**Banned:** an object-to-category edge for membership; a discriminant arrow
from the full lattice category when the construction is functorial only on its
core; an unlabeled edge whose direction could mean either inclusion or
forgetting structure.

**Preferred:** write the actual source, target, and arrow label. Replace
membership by prose, restrict a construction to its stated domain, and display
a set-valued invariant as a map from $\pi_0$.

### `MA-12`: Named maps referred to by count

Standard maps with standard names — the associator $\alpha$, the left unitor
$\lambda$, the right unitor $\varrho$ — are referred to as "the three
isomorphisms" or "the $n$ maps" instead of by name. The reader must infer
which maps from context.

**Banned:** "the three isomorphisms being the unique ones commuting with the
projections."

**Preferred:** "the associator $\alpha_{a,b,c}$ and the unitors
$\lambda_a$, $\varrho_a$." Name the maps. The count carries no mathematical
information.

### `MA-13`: A structure described pointwise instead of as a structure

A functor is a functor: source, target, name. A natural transformation is a
natural transformation: its components and the naturality square. A monoidal
structure is a tuple $(\mathcal{C}, \otimes, \mathbf{1}, \alpha, \lambda,
\varrho)$ with axioms. Each of these is a mathematical object with a type and
constituent data. A pointwise description — "a choice of $a \otimes b$ for
every $a$, $b$" — replaces the structure with a recipe for its output on
inputs, the way a programmer describes a function by what it returns. State
the structure; its pointwise behavior may follow.

**Banned:** "choose a product $a \times b$ for each pair of objects and set
$\otimes = \times$."

**Preferred:** "the product functor
$\times\colon\mathcal{C}\times\mathcal{C}\to\mathcal{C}$, together with a
terminal object $\mathbf{1}$ and the canonical associator and unitors,
defines a monoidal structure on $\mathcal{C}$."

## Definitions (`DEF-*`)

### `DEF-1`: One defining occurrence

Each mathematical notion has one defining occurrence in the book. Later
chapters cite it. They do not restate it, shadow it with a synonym, or write a
second local definition.

### `DEF-2`: Read the book before writing a dependent passage

Read the book's defining occurrence and its prerequisites before writing a
dependent passage. A definition reconstructed from training or an external
source is inadmissible even when it resembles a standard definition.

### `DEF-3`: Correct at the defining occurrence

If the book's definition conflicts with the literature, correct it at the
defining occurrence and repair its dependents. Do not shadow it locally.

### `DEF-4`: Numbered block syntax

```markdown
::: {#def-universe}
## Universe and decoded objects

Work in an external cartesian closed $(\infty,\infty)$-category $\mathcal K$
with pullbacks and terminal object $*$.
:::
```

The declared block classes are listed at the bottom of
`writing/.book/_quarto.yml`. Add a class there before using it.

## Cross-references (`XREF-*`)

### `XREF-1`: `\ref` and `\longref` only

`\ref` and `\longref` are the only two commands that resolve numbered blocks.
They reach any numbered block in the book, in any chapter, in either
direction.

### `XREF-2`: No `\cref` or `\Cref`

**Banned:** `\cref`, `\Cref`. They do not match the resolver. Pandoc drops an
unmatched macro silently, so the reference disappears and the sentence around
it is left dangling.

### `XREF-3`: Label format

Labels use colon separators: `def:universe`, `thm:coble-cusps`. Do not start a
label with a Quarto-reserved prefix (`def-`, `thm-`, `lem-`, `cor-`, `prp-`,
`cnj-`, `exm-`, `exr-`, `fig-`, `tbl-`, `eq-`, `sec-`, `lst-`); use a hyphen
instead. Quarto hijacks those prefixes for its own crossrefs and the render
fails.

### `XREF-4`: Sections and figures

Sections auto-number. Reference a section by link:
`[Lattice Theory](lattice-theory.md#sec:lattice-theory)`.

Figures use Quarto's own numbering. Anchor a figure `{#fig-x}`, with a hyphen,
and reference it `@fig-x`.

## Citations (`CITE-*`)

### `CITE-1`: Better BibTeX keys

Use Better BibTeX keys: `[@OR23, Definition 1.5.1]`. Zotero is the source of
truth. If a work is not in Zotero, add it there first.

### `CITE-2`: No inline URLs

**Banned:** an inline URL to arXiv, a DOI, or nLab. The docs gate rejects it.

## Diagrams (`DIA-*`)

### `DIA-1`: Draw the square

Draw a universal construction as its square. Label every morphism. Mark it
cartesian or cocartesian. Name the resulting object and structure morphism in
the diagram. The prose may state the universal property after the diagram; it
never replaces the diagram.

### `DIA-2`: Every arrow is typed

Every arrow in a diagram names a functor, natural transformation, or map with
the displayed source and target. A construction defined only on cores is drawn
from the cores. An invariant on isomorphism classes is drawn as a map from
$\pi_0$. Membership of an object in a category is not drawn as a functor
between categories.

## Notation (`NOT-*`)

### `NOT-1`: State the mathematical type

State the mathematical type of every named entity. Distinguish objects and
morphisms in a specified category, categories and functors, natural
transformations, object properties, chosen structures, invariants, sections,
and obstructions.

### `NOT-2`: Typed equality symbols

Literal equality ($=$), isomorphism ($\cong$), and equivalence ($\simeq$) are
written with distinct symbols. $\hookrightarrow$ denotes a stated inclusion,
embedding, or monomorphism; fullness, faithfulness, and repleteness are
asserted separately.

### `NOT-3`: One symbol, one meaning

The same symbol has the same type and meaning throughout the book. Project
notation is introduced at the defining occurrence, after the underlying
standard construction has been stated.

### `NOT-4`: Standard names

Use established names in their standard meanings: category of elements,
Grothendieck construction, core, arrow category, full subcategory, replete,
natural isomorphism, automorphism group, torsor, monoidal category, abelian
category, kernel, cokernel, discriminant form, genus, isometry, classifying
object. Do not coin a name for a notion that already has one.

## Properties and structure (`STR-*`)

### `STR-1`: Use the forgetful functor

For a specified forgetful functor $U\colon\mathcal S\to\mathcal C$, full
faithfulness gives at most property, faithfulness gives at most structure, and
an arbitrary functor gives at most stuff. Repleteness is a separate condition
when an essential image is replaced by a full subcategory.

### `STR-2`: Name every chosen structure

A structure on $X$ is a chosen object in the fiber over $X$ of a specified
forgetful functor. When several choices exist, name the one used by the
construction. For example, tensor product and direct sum give different
monoidal structures on modules.

### `STR-3`: State every hypothesis

A theorem states every object property, characteristic restriction, limit
assumption, flatness assumption, and equality of named morphisms used in its
conclusion. If a construction uses a basis, embedding, section, presentation,
or other witness, name that witness in the construction.

## Examples and presentation (`EX-*`)

### `EX-1`: An example mirrors the definition's form

An example instantiates each slot of the structure it exemplifies. If a
monoidal category was defined as a tuple
$(\mathcal{C}, \otimes, \mathbf{1}, \alpha, \lambda, \varrho)$, the example
presents the tuple: "Let $\mathcal{C}$ be a category with finite products
and terminal object $e$. Then $(\mathcal{C}, \times, e)$ is a monoidal
category." The reader who just read the definition sees which slot is
which without parsing prose. Listing the components in a sentence instead
of presenting the tuple is readable but does not mirror the definition's
grammar.

**Banned:** "A category with finite products is monoidal with $a\otimes b$ a
chosen product $a\times b$ and $e$ a terminal object, the three isomorphisms
being the unique ones commuting with the projections; this is the cartesian
monoidal structure."

**Preferred:** "Let $\mathcal{C}$ be a category with finite products and
terminal object $e$. Then $(\mathcal{C}, \times, e)$ is a monoidal category,
with associator and unitors the canonical isomorphisms supplied by the
universal property of the product."

### `EX-2`: An example is an example, not a proposition

If there is nothing to prove, do not present the passage as a proposition
with a proof. A category with finite products is an example of a monoidal
category, not a theorem. State the definition, then give the example in an
example block. Reserve proposition and proof blocks for statements that
require verification beyond unpacking the definition.

## Axioms and definitions (`AX-*`)

### `AX-1`: A definition that names axioms without stating them

A definition must fully determine the notion it introduces. Referencing
axioms by name — "satisfying the two hexagon conditions", "satisfying the
pentagon axiom" — without stating or drawing the diagrams is not a
definition. The reader cannot evaluate whether a given object satisfies the
definition, because the name of an axiom is not the axiom. State the
equations or draw the diagrams. If they are long, cite the exact diagrams
by reference to where they are written in full.

**Banned:** "A braiding on a monoidal category is a natural isomorphism
$\gamma_{a,b}\colon a\otimes b\cong b\otimes a$ satisfying the two hexagon
conditions relating $\gamma$ to $\alpha$."

**Preferred:** state or draw both hexagon diagrams. The definition names
each component and each axiom; the axioms are commutative diagrams, and a
definition either draws them or cites the exact reference where they are
written.

### `AX-2`: An axiom described by shape instead of by equation

"The hexagon conditions", "the pentagon axiom", "the triangle identities" —
the shape name is a mnemonic, not a mathematical condition. The condition
is a commutative diagram or an equation. Use the shape name alongside the
diagram, not in place of it. A reader who does not already know the shape
cannot reconstruct the axiom from its name.

**Banned:** "satisfying the two hexagon conditions relating $\gamma$ to
$\alpha$."

**Preferred:** draw the two hexagon diagrams, or write the equations they
commute. The name "hexagon" may appear as a label; it may not substitute
for the diagram.

### `AX-3`: "relating" an axiom to its components without stating the relation

"relating $\gamma$ to $\alpha$", "commuting with the projections",
"compatible with the tensor product" — each names a relationship without
stating the equation or diagram that expresses it. A definition or theorem
that invokes a relation states the relation: the commutative diagram, the
equation, or the naturality square. "Relating" and "compatible" gesture at
a mathematical statement that is not written.

**Banned:** "satisfying the two hexagon conditions relating $\gamma$ to
$\alpha$."

**Preferred:** state the relation — the hexagon diagrams express that
specific composites of $\gamma$, $\alpha$, and the tensor product's
functoriality are equal. Draw the diagrams or write the equations.

### `AX-4`: A definition that is not self-contained

A definition must be evaluable from the text plus its cited references. A
definition that references axioms by name without stating them and without
citing where they are written in full gives the reader neither the axioms
nor a pointer. The reader cannot determine whether a given object satisfies
the definition. Self-contained does not mean everything is derived from
first principles in one sentence — it means the text or its cited
references supply every component the definition requires.

**Banned:** "A braiding on a monoidal category is a natural isomorphism
$\gamma_{a,b}\colon a\otimes b\cong b\otimes a$ satisfying the two hexagon
conditions relating $\gamma$ to $\alpha$." No diagrams, no citation.

**Preferred:** draw the hexagon diagrams in the definition, or write
"[@MacLane, Chapter VII, (2.1) and (2.2)]" citing the exact diagrams. The
reader follows the citation and finds the axioms; or the reader reads the
diagrams in the text. Either way the definition is evaluable.

### `AX-5`: An axiom named by count without stating or citing the axioms

"The two hexagon conditions", "the three coherence axioms", "the five
simplicial identities" — a count of axioms without stating or citing them
combines AX-1 and AX-2 with a cardinality label. The count tells the reader
how many axioms to imagine without supplying them. Name each axiom, draw
each diagram, or cite the exact reference for all of them. The count is not
a substitute.

**Banned:** "satisfying the two hexagon conditions."

**Preferred:** draw both hexagon diagrams, or cite the reference where both
are written. The reader does not need to be told there are two; the reader
needs to see them.

## Terminology (`TERM-*`)

Use established mathematical terms in their standard meanings. Do not coin a
name for a notion that already has one. Do not import a term from another
field where the book owes a standard mathematical object. Do not overload a
standard word with a project-management or implementation meaning.

Terminology failures have three recurring forms:

- **Foreign-discipline substitution.** A technical term from another field is
  used where the book owes a standard mathematical object and definition.
- **Project coinage.** An undefined word is made to do mathematical work.
- **Colliding overload.** A standard word such as "kernel", "core", or
  "fiber" is reused with a project-management or implementation meaning.

The citation-backed recurring inventory lives in
`.agents/references/terminology-dictionary.md`. The following replacements
apply to this book:

| Term to avoid | Required mathematical statement |
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

### `TERM-1`: Retired substitutions

These terms survived one round of editing and are withdrawn.

**Banned:** "multi-sorted signature"; "semantic interpretation"; "executable
interpretation"; Mathlib identifiers used as prose nouns.

**Preferred:** state the actual categories, functors, predicates, and
constructions. Name the mathematical functor or the implementation operation
actually meant. Restrict Mathlib identifiers to code-formatted implementation
anchors.

## Parentheticals (`PAR-*`)

A semantic parenthetical is a compression. Prefer expansion over compression:
expanding into explicit mathematics is reversible, whereas a compression is
lossy and usually smuggles an undefined term or an unstated theorem.

### `PAR-1`: Compression artifact

Terse to the point of inscrutability, standing in for a notion that needs
spelling out.

**Banned:** "weak homotopy equivalence (holds; inverts/ignores
directionality) versus categorical equivalence (fails; preserves it)."

**Preferred:** expand into prose or a definition that states the
distinction.

### `PAR-2`: Smuggled theorem or equivalence

"(equivalently, $X$)", an "iff" asserted in a parenthesis, often over
undefined terms.

**Banned:** "full and faithful (equivalently, a replete full subcategory)"
— a functor is identified with its essential image and an equivalence is
asserted aside.

**Preferred:** "If $F\colon\mathcal C\to\mathcal D$ is fully faithful, then
$F$ induces an equivalence from $\mathcal C$ to its replete full essential
image in $\mathcal D$." Cite the result and define any term not already
established. The expanded statement can later be demoted to a remark, cited
theorem, or footnote.

### `PAR-3`: Smuggled example

"(e.g. …)" carrying a genuine example.

**Banned:** "several distinct lifts (e.g. several monoidal structures on one
category)."

**Preferred:** promote to a first-class example block.

### `PAR-4`: Legitimate qualification

A small, correct, load-bearing modifier. Keep inline.

**Fine as is:** "fibers are (possibly nontrivial) groupoids."

### `PAR-5`: Padding or tangent

Carries no load.

**Preferred:** delete. A parenthetical is usually wrong when it is a
tangent.

## Not flags

Standard mathematical hedging and signposting that carry real content are not
violations: "provided", "up to isomorphism", "without loss of generality", a
genuine sign or normalization convention, and a Remark that explains a real
subtlety in context. The test is whether removing the phrase removes
information. A tagline removes none.

## Symbols and binding (`SYM-*`)

Mathematical text follows scoping and binding conventions analogous to those
in a formal language. A symbol is bound at the point where the object it
names is declared — with its type, domain, codomain, or constituent data.
Before that point, the symbol is unbound and the reader cannot determine
what it refers to. Naming a type ("let $\mathcal{C}$ be a monoidal
category") does not bind the symbols for that type's constituent data
($\otimes$, $\mathbf{1}$, $\alpha$, $\lambda$, $\varrho$); those are bound
by stating the tuple
$(\mathcal{C},\otimes,\mathbf{1},\alpha,\lambda,\varrho)$. A symbol used
before its binding is an unbound reference; a symbol that changes meaning
within a passage is a shadowing conflict.

### `SYM-1`: A symbol used without being bound

A passage uses a symbol before declaring the object it names. No type, no
domain, no codomain, and no constituent tuple is stated. The reader cannot
determine what the symbol refers to without external knowledge. Bind the
symbol first: state the object, its type, and the map's domain and
codomain (or the structure's tuple). Then use the symbol.

**Banned:** "A monoid in $(\mathbf{Ab},\otimes_{\mathbb Z},\mathbb Z)$ is a
ring, its multiplication being the bilinear map classified by $\mu$ and its
unit the image of $1$ under $\eta$." The symbols $\mu$ and $\eta$ are used
without being introduced; no abelian group $A$ is named; no domains or
codomains are stated.

**Banned:** "Let $S$ be a symmetric monoidal category. … Then $\otimes$
makes $S^{\mathrm{iso}}$ an abelian monoid." The tensor $\otimes$ is used
without being bound — stating the type "symmetric monoidal category" does
not introduce the symbol $\otimes$.

**Preferred:** "A monoid object in
$(\mathbf{Ab},\otimes_{\mathbb{Z}},\mathbb{Z})$ is a triple
$(A,\mu,\eta)$ where $A$ is an abelian group,
$\mu\colon A\otimes_{\mathbb{Z}}A\to A$ is a homomorphism, and
$\eta\colon\mathbb{Z}\to A$ is a homomorphism. The bilinear multiplication
$A\times A\to A$ is the map corresponding to $\mu$ under the tensor-hom
adjunction, and the unit element is $\eta(1)$." Name the data, then use the
symbols.

### `SYM-2`: Data referenced by role instead of by declaration

A passage refers to "the multiplication", "the unit", "the associator", or
"the classifying map" without first declaring the object that plays that
role. The role name presupposes the data without stating it. Declare the
data — the map, its domain, its codomain — then refer to it by name. A role
description is a comment on data that has been stated, not a substitute for
stating it.

**Banned:** "its multiplication being the bilinear map classified by $\mu$"
— "the multiplication" is a role; $\mu$ is undeclared; "the bilinear map
classified by $\mu$" describes what $\mu$ does without stating what $\mu$
is.

**Preferred:** "$\mu\colon A\otimes_{\mathbb{Z}}A\to A$ is a homomorphism;
the corresponding bilinear map $A\times A\to A$ is the multiplication."
Declare the map, then name its role.

### `SYM-4`: A symbol overloaded within one passage

A single symbol is used for two distinct mathematical objects in the same
passage — a terminal object and an identity morphism, a unit element and a
unit map — so the reader cannot determine which referent is in force at
each occurrence. Each symbol has one meaning throughout the book
(`NOT-3`); within a single passage the constraint is tighter, because the
two referents appear side by side.

**Banned:** "Let $\mathcal C$ have finite products and a terminal object
$1$. … $\mu\circ(1\times\zeta)\circ\delta$" — the first $1$ is the
terminal object, the $1$ in $1\times\zeta$ is $\operatorname{id}_c$.

**Preferred:** use distinct symbols. Name the terminal object $e$ or
$\mathbf{1}$, and write $\operatorname{id}_c$ for the identity morphism.
No reader confuses $\operatorname{id}_c\times\zeta$ with
$e\times\zeta$.

### `SYM-5`: A map written without its domain and codomain

A morphism is written as a bare symbol in an equation — $1\times\zeta$,
$\mu\circ\delta$ — without stating its domain and codomain. The reader
must infer the types from context. In a definition, where the reader is
meeting the maps for the first time, state the domain and codomain of
each map before using it in an equation.

**Banned:** "$\mu\circ(1\times\zeta)\circ\delta=\eta\circ{!}_c$" with no
domain or codomain stated for $1\times\zeta$, $\delta$, or $!_c$ before
their use.

**Preferred:** "$\operatorname{id}_c\times\zeta\colon c\times c\to
c\times c$, $\delta\colon c\to c\times c$, and $!_c\colon c\to
\mathbf{1}$" stated before the equations that use them.

### `SYM-6`: A symbol introduced after its first use

A "where" clause defines $\delta$ after $\delta$ has already appeared in
the equations above it. In a definition, every symbol is introduced before
its first use. A "where" clause after an equation is a trailing gloss for
a reader who already knows the notation; it is not a substitute for
stating the data before using it.

**Banned:** equations using $\delta$, then "where
$\delta\colon c\to c\times c$ is the diagonal."

**Preferred:** "Let $\delta\colon c\to c\times c$ be the diagonal and
$!_c\colon c\to\mathbf{1}$ the unique map. Then …" — state the maps,
then write the equations.

### `SYM-7`: A tuple-defined structure referred to in prose instead of by its tuple

A structure that was defined as a tuple — a monoidal category
$(\mathcal{C},\otimes,\mathbf{1})$, an adjunction $(F,G,\eta,\epsilon)$,
a chain complex $(C_\bullet,d)$ — is referred to in prose instead of by
the tuple. The reader must assemble the structure from English instead of
recognizing the tuple that was defined. Refer to a tuple-defined structure
by its tuple.

**Banned:** "a monoid for the cartesian structure"; "the adjunction
between free and underlying"; "the complex with the standard
differential."

**Preferred:** "a monoid object in $(\mathcal{C},\times,\mathbf{1})$";
"the adjunction $(F,G,\eta,\epsilon)$"; "the chain complex
$(C_\bullet,d)$." Name the structure the same way it was defined.

### `SYM-8`: A mathematical object named by a prose qualifier instead of by its type

A mathematical object is named by a bare noun qualified by a prepositional
phrase — "a monoid for the cartesian structure", "a module for the group
action", "a sheaf for the topology" — instead of by its type and the
category it lives in. State the type and the category; do not qualify a
bare noun with prose.

**Banned:** "a monoid for the cartesian structure"; "a module for the
group action"; "a sheaf for the topology."

**Preferred:** "a monoid object in $(\mathcal{C},\times,\mathbf{1})$";
"a module over $R[G]$"; "a sheaf on $(X,\mathcal{O}_X)$." The type names
the kind of object; the category names where it lives.

## Definitions and modern theory (`DEF-*` continued)

### `DEF-5`: A theorem presented as a definition

A construction is defined by a property or identification that is in fact
a theorem — a result that holds under hypotheses, or a consequence of a
deeper construction. The reader receives the theorem as the definition and
has no access to the construction it replaces. Present the construction;
state the theorem that identifies the construction with the simpler
description; do not substitute the theorem for the definition.

**Banned:** "$K_0^{\otimes}(S)$ is the group completion of the monoid of
isomorphism classes." The group completion of $\pi_0(S^\simeq)$ is
$\pi_0 K(S)$, but that identification is a theorem (the group completion
theorem), not the definition. The definition is $K_0(S) = \pi_0 K(S)$,
where $K(S)$ is the $K$-theory spectrum.

**Preferred:** "Let $K(S)$ denote the algebraic $K$-theory spectrum of
the symmetric monoidal category $S$. Define $K_0(S) = \pi_0 K(S)$. By the
group completion theorem, $K_0(S)$ is the group completion of
$\pi_0(S^\simeq)$ under the induced monoid operation." State the
construction, then state the theorem that identifies it with the simpler
description.

### `DEF-6`: A definition that suppresses the governing structure

A construction depends on a richer structure than the definition reveals.
The definition names only the downstream consequence and omits the
structure that governs it, so the reader has no access to the rest of
what that structure provides. State the governing structure; derive the
defined object as a component or consequence of it.

**Banned:** defining $K_0(S)$ as the group completion of a monoid
without introducing the $K$-theory spectrum $K(S)$. The reader has no
access to $K_n(S)$, the higher $K$-groups, or the spectrum-level
structure, because the spectrum was never stated.

**Preferred:** introduce the spectrum $K(S)$, define $K_0(S) = \pi_0
K(S)$, and then identify $\pi_0 K(S)$ with the group completion. The
spectrum governs all $K_n$; $K_0$ is one component.

### `DEF-7`: Nonstandard notation that marks a dependency the standard notation already encodes

A superscript or subscript is added to a standard symbol to mark a
dependency that the standard notation already encodes through its
arguments. The decoration is a project coinage that distinguishes
instances the standard notation does not distinguish, because the
standard notation already parameterizes by the input.

**Banned:** "$K_0^{\otimes}(S)$" — the $\otimes$ superscript marks the
dependency on the monoidal structure, but $K_0(S)$ already takes the
symmetric monoidal category $S$ (with its tensor) as input.

**Preferred:** use the standard notation. If a distinction is needed
between $K$-theories of the same category with different monoidal
structures, name the monoidal structure in the argument:
$K_0(S,\otimes)$, or use distinct symbols for the distinct monoidal
categories.

### `DEF-8`: A definition anchored in a superseded framework

A definition or construction is presented using a framework the field has
replaced, when a modern framework exists and is standard. The superseded
framework is not wrong — it is a shadow or special case of the modern one
— but presenting it as the definition teaches the reader a picture that the
field has moved past. This is especially acute in category theory, where
the modern framework is $\infty$-category theory, derived and spectral
algebraic geometry, and the constructions developed in the last 10-20
years. A construction whose modern home is an $\infty$-categorical or
spectral framework — $K$-theory, derived functors, cohomology, moduli,
intersections, traces — is presented in its classical, pre-derived,
pre-spectral form, and the reader has no access to the generality and
structure the modern framework provides. Anchor definitions in the current
understanding of the subject; present the classical formulation as a
special case or theorem if it is still useful.

**Banned:** defining $K_0(S)$ as the group completion of
$\pi_0(S^\simeq)$ without mentioning the $K$-theory spectrum. $K$ is a
functor from a subcategory of $\mathbf{Cat}$ to spectra; $K_0$ is $\pi_0$
of that functor. The group completion of the monoid is an even more
classical construction that the spectrum recovers. Presenting the
group completion as the definition is anchoring in a framework two stages
out of date.

**Preferred:** define $K$ as a functor to spectra, $K_0(S) = \pi_0 K(S)$,
and state the group completion theorem as a theorem. The
$S_\bullet$-construction [@Wal85] is the standard construction;
Zakharevich [@Zak17] constructs $K(\mathcal{V}_k)$ as a spectrum whose
$\pi_0$ is the Grothendieck ring of varieties, with higher homotopy
groups carrying geometric information; Campbell [@Cam17] produces
$K(\mathbf{Var}_{/k})$ via an $S_\bullet$-type construction with
liftings of motivic measures to the spectrum. A reader trained on the
modern definition can access the generality the functor to spectra
provides; a reader trained on the superseded one cannot.

### `DEF-9`: Classical structure presented where the modern framework gives a richer object

A construction carries additional structure in the modern framework that
the classical presentation suppresses entirely. The classical version
describes a shadow — $\pi_0$ of a richer object — and the reader has no
access to the structure the modern framework provides at higher levels.
Present the richer object; derive the classical structure as a
consequence.

**Banned:** "the group completion inherits a multiplication from it …
$K_0(R)$ is a commutative ring with unit $[R]$." A second symmetric
monoidal product distributing over the first makes $K(S)$ an
$\mathbb{E}_\infty$-ring spectrum, not just $K_0$ a commutative ring.
The ring structure on $K_0$ is $\pi_0$ of the ring spectrum; the higher
$K$-groups are modules over $K_0$; the unit spectrum's $\pi_0$ is $[R]$.
All of this is invisible.

**Preferred:** "A second symmetric monoidal product on $S$ that
distributes over the first makes $K(S)$ an $\mathbb{E}_\infty$-ring
spectrum; in particular $K_0(S)$ is a commutative ring and $K_n(S)$ are
modules over it." The ring spectrum is constructed from the multiplicative
monoidal structure via an $\mathbb{E}_\infty$-operad action
[@EKMM07, @HA]; for $\operatorname{Proj}(R)$ with $\oplus$ and
$\otimes$, $K(R)$ is an $\mathbb{E}_\infty$-ring spectrum whose $\pi_0$
is the classical $K_0(R)$ [@Wei13, §II.2]. State the ring spectrum;
derive the ring on $\pi_0$ from it.

### `DEF-10`: Working truncated while the modern theory is derived and spectral

Modern theory is derived and spectral by default: the objects are
$\infty$-categories, derived stacks, $\mathbb{E}_\infty$-ring spectra, and
module spectra, and the classical objects — ordinary categories, schemes,
commutative rings, abelian groups — are truncations. A passage that
discusses a modern construction entirely in classical terms — rings
instead of $\mathbb{E}_\infty$-ring spectra, abelian groups instead of
spectra, ordinary categories instead of $\infty$-categories — works
truncated without saying so, and the reader cannot recover the derived
structure. Work in the derived and $\infty$-categorical framework
throughout; state classical objects as truncations when the construction
truly requires them, and make the extraction explicit.

**Banned:** "Let $R$ be a commutative ring" — used where $HR$ (the
Eilenberg–Mac Lane $\mathbb{E}_\infty$-ring spectrum of $R$) is the
governing object, without saying whether $R$ is $\pi_0 HR$ or an
$\mathbb{E}_\infty$-ring. "Let $G$ be a group" — used where $BG$ (its
classifying $\infty$-groupoid) is the governing object.

**Preferred:** "Let $R$ be an $\mathbb{E}_\infty$-ring spectrum; write
$\pi_0 R$ for its underlying classical ring when the classical
construction is needed: $R = H(\pi_0 R)$ when $R$ is discrete." State the
derived object; extract the classical shadow explicitly when it is the
object under study, e.g. in the statement of a classical theorem.

### `DEF-11`: Truncation extraction named explicitly

Passing from a derived or spectral object to its classical shadow is a
specific construction, not a silent identification: $\pi_0 HR$ extracts the
classical ring $R$ from the Eilenberg–Mac Lane $\mathbb{E}_\infty$-ring
spectrum; $\Omega BG$ recovers the group $G$ from its classifying
$\infty$-groupoid; the underlying abelian group of an
$\mathbb{E}_\infty$-module spectrum is a further forgetful image. Each
extraction names the functor that performs it. A passage that uses the
classical object without naming the extraction hides the truncation.

**Banned:** "a commutative ring $R$ and its modules" — used where
$\mathbb{E}_\infty$-modules over $HR$ are the governing objects, with no
statement of the truncation.

**Preferred:** "an $\mathbb{E}_\infty$-ring spectrum $R$ and its module
spectra; its $\pi_0$ is the classical commutative ring, and the
heart of the t-structure recovers the classical module category." Name
the derived objects; state the truncation that yields the classical
ones. Do not belabour the extraction at every mention, but make it
explicit where the book first passes from derived to classical.

### `DEF-12`: Level of abstraction calibrated to modern courses and literature

The standard for how much $\infty$-categorical and spectral machinery the
book uses is not the classical textbook from which the author learned
the material, but the level at which the subject is currently taught and
practiced: undergraduate and graduate courses at Harvard, MIT, and
Princeton, and the work of Lurie, Scholze, Gaitsgory, and Haynes Miller.
When in doubt about whether a derived or $\infty$-categorical
presentation is warranted, survey how the notion is presented in those
courses and in that literature, and match their level. A construction
that Lurie's lectures present as a functor between $\infty$-categories
is not presented here as a functor between ordinary categories; a notion
that Scholze's course formulates via derived stacks is not formulated
here via classical schemes. This does not mean every detail is
re-derived — a construction is stated at the modern level, and classical
consequences are extracted — but it means the book does not implicitly
assume everything is truncated everywhere.

**Banned:** presenting a construction at the classical level because the
classical case is "simpler" or "more familiar", when the field's standard
presentation is derived or $\infty$-categorical.

**Preferred:** survey the modern courses and literature (e.g. Lurie's
*Higher Topos Theory* [@Lur09HTT] and *Higher Algebra* [@HA], Gaitsgory–
Rozenblyum, Scholze's courses and the Berkeley lectures, Haynes Miller's
spectral sequences courses) and match their level of abstraction and
presentation.

### `DEF-13`: Everything implicitly or explicitly derived and homotopical

The book works in the derived and homotopical ontology by default. Every
classical term has a derived analogue that is the default meaning; the
classical object is a truncation, and a passage that means the derived
object does not use the classical name. This applies uniformly:

| Classical name | Default meaning in this book |
| --- | --- |
| ring | $\mathbb{E}_\infty$-ring spectrum |
| module | module spectrum |
| category | $\infty$-category |
| functor | total derived functor (e.g. derived tensor product is $\otimes^L$) |
| stack | derived stack |
| space | homotopy type, anima, or $\infty$-topos; write $\mathbf{Top}$ when actual topological spaces are meant |
| topology | Grothendieck topology |
| group | $\infty$-group or loop space; write $\Omega BG$ to recover a discrete group |

A passage that means the derived object does not use the classical name
and rely on the reader to supply the derived upgrade. A passage that
means the classical truncation states it as a truncation — $\pi_0 HR$
for the classical ring $R$, $\tau_{\leq 0}\mathcal{C}$ for the ordinary
category, the heart of the t-structure for classical modules — and makes
the extraction explicit. Do not belabour every derived detail at every
mention, but do not implicitly assume everything is truncated everywhere.

**Banned:** "Let $R$ be a commutative ring and $M$ an $R$-module …
consider the tensor product $M\otimes_R N$" — used where $R$ is an
$\mathbb{E}_\infty$-ring spectrum, $M$ and $N$ are module spectra, and
$\otimes$ is the derived tensor product.

**Preferred:** "Let $R$ be an $\mathbb{E}_\infty$-ring spectrum and $M$
an $R$-module spectrum … consider the derived tensor product
$M\otimes_R^L N$; its $\pi_0$ recovers the classical tensor product of
$\pi_0 R$-modules." Or, in a genuinely classical passage: "Let
$R = \pi_0 HR$ be a classical commutative ring" — state the truncation.

### `PR-13`: "Is an invariant of X" for factoring through a quotient

A map that factors through a quotient or truncation — through
$\pi_0(S^\simeq)$, through a set of isomorphism classes, through a
coarse moduli space — is described in prose as "is an invariant of
isomorphism classes" or "is an invariant of $X$". The phrase names no
domain, no factorization, and no map; the reader cannot determine what
factors through what. State the factorization.

**Banned:** "so $K_0^{\otimes}$ is an invariant of isomorphism
classes."

**Preferred:** "$K_0\colon\mathbf{SymMonCat}\to\mathbf{Ab}$ factors
through $\pi_0\colon\mathbf{SymMonCat}\to\mathbf{Set}$,
$S\mapsto\pi_0(S^\simeq)$." Name the domain, the quotient, and the
factorization. If the factorization is the definition, do not restate it
as an additional property.

### `PR-14`: "Is functorial for X" for being a functor

A functor is described in prose as "is functorial for symmetric monoidal
functors" or "is functorial for $X$ morphisms" instead of being stated
as a functor with its source and target category. The phrase names no
domain, no codomain, and no action on morphisms. State the functor.

**Banned:** "and is functorial for symmetric monoidal functors."

**Preferred:** "$K\colon\mathbf{SymMonCat}\to\mathbf{Spectra}$ is a
functor (hence $K_0 = \pi_0\circ K\colon\mathbf{SymMonCat}\to\mathbf{Ab}$
is a functor)." State the source, the target, and the functor. If the
object was defined as a functor, functoriality is not an additional
property to be asserted in prose.

### `PR-15`: Prose paraphrase of a precise categorical statement

A precise categorical statement — a factorization through a quotient or
$\pi_0$, a functor with source and target, a commutative diagram, a tuple
with its constituents, a natural transformation with its naturality square
— is paraphrased in loose English instead of being stated precisely. The
prose is simultaneously wordier and less precise: it names no domain, no
codomain, no diagram, and the reader cannot reconstruct the precise
statement. State the precise statement.

**Banned:** "is an invariant of isomorphism classes and is functorial for
symmetric monoidal functors"; "relating $\gamma$ to $\alpha$"; "commuting
with the projections"; "is what licenses the notation
$a_1\otimes\cdots\otimes a_n$ without parentheses."

**Preferred:** "factors through $\pi_0\colon S\mapsto\pi_0(S^\simeq)$";
"$K\colon\mathbf{SymMonCat}\to\mathbf{Spectra}$ is a functor"; draw the
hexagon diagrams; state the tuple
$(\mathcal{C},\otimes,\mathbf{1},\alpha,\lambda,\varrho)$; "any two
parenthesizations are connected by a unique composite of associators."
PR-13, PR-14, EV-8, AX-1, and PR-7 are instances of this general pattern:
a precise statement was replaced by a loose English description that is
longer and carries less information.

### `DEF-14`: "General ring" without specifying the $\mathbb{E}_n$ level

"Ring" in this book is an $\mathbb{E}_\infty$-ring spectrum by default
(DEF-13). For an $\mathbb{E}_\infty$-ring spectrum $R$,
$\mathbf{LMod}_R\simeq\mathbf{RMod}_R$ canonically via the symmetry. For a
general associative ($\mathbb{E}_1$) ring spectrum the two
$\infty$-categories $\mathbf{LMod}_R$ and $\mathbf{RMod}_R$ (equivalently
$\mathbf{LMod}_R$ and $\mathbf{RMod}_{R^{\mathrm{op}}}$ for a classical
noncommutative ring) are distinct. A passage that says "for a general
ring, left and right module categories are not canonically equivalent"
without stating the $\mathbb{E}_n$ level is ambiguous on the book's
default reading — and false if read as $\mathbb{E}_\infty$.

**Banned:** "For a general ring, an equivalence between left and right
module categories is additional data."

**Preferred:** "For a general associative ($\mathbb{E}_1$) ring spectrum
$R$, there is no canonical equivalence
$\mathbf{LMod}_R\simeq\mathbf{RMod}_R$." If the $\mathbb{E}_\infty$ case
is meant, state that the symmetry gives the canonical identification, so
the distinction is only for $\mathbb{E}_1$.

### `PR-16`: "Additional data" for a precise moduli of equivalences

A passage states that a comparison "is additional data" or "does not
follow merely from notation" instead of stating what the extra structure
is and what classifies it. The phrase names no data and no moduli, and
"does not follow from notation" negates a premise no one holds: no
mathematician thinks an equivalence
$\mathbf{LMod}_R\simeq\mathbf{RMod}_R$ would follow from writing $R$ on
the left versus on the right. State the structure: there is no canonical
equivalence; an equivalence is equivalent to the data of an invertible
bimodule, a Morita equivalence, an
$\mathbb{E}_1$-equivalence $R\simeq R^{\mathrm{op}}$, or whichever
structure is relevant, and state the universal property that classifies
it.

**Banned:** "an equivalence between left and right module categories is
additional data; it does not follow merely from notation."

**Preferred:** "there is no canonical equivalence
$\mathbf{LMod}_R\simeq\mathbf{RMod}_R$; such an equivalence is equivalent
to the data of an invertible $(R,R)$-bimodule, and in particular to an
$\mathbb{E}_1$-equivalence $R\simeq R^{\mathrm{op}}$ when it is induced
by an anti-automorphism." Name the data and the classification; do not
paraphrase existence of structure as English about notation.

### `PR-17`: Negating a strawman premise about notation

A precise negative existence statement — "there is no canonical
equivalence $\mathbf{LMod}_R\simeq\mathbf{RMod}_R$" — is replaced by
meta-commentary negating a premise no one holds: "it does not follow
merely from notation that …" No mathematician thinks notation produces
equivalences; the notation $\mathbf{LMod}_R$ versus $\mathbf{RMod}_R$
already distinguishes them. The strawman is fabricated — it exists only
to be corrected — and the sentence is incoherent because the premise it
negates is not a view anyone holds. The default for a general
($\mathbb{E}_1$) $R$ is not that an equivalence exists and needs data; it
is that no such equivalence exists. State the precise negative existence
and the moduli when an equivalence does exist.

**Banned:** "it does not follow merely from notation that left and right
module categories are equivalent" — negates a strawman; no one claimed
notation would make them equivalent. "An equivalence is additional data;
it does not follow from notation" — frames existence as the default that
merely needs data, when the default is non-existence.

**Preferred:** "there is no canonical equivalence
$\mathbf{LMod}_R\simeq\mathbf{RMod}_R$; an equivalence, when it exists,
is equivalent to …" State the theorem, not commentary on what notation
does not do.

### `PR-18`: Patronizing dialectic for a sophisticated audience

The book's reader is the audience of DEF-12 and DEF-13: comfortable with
$\infty$-categories, $\mathbb{E}_1$- and $\mathbb{E}_\infty$-ring spectra,
$\mathbf{LMod}_R$ versus $\mathbf{RMod}_R$, derived stacks, and
homotopy types. That reader already distinguishes $\mathbb{E}_1$ from
$\mathbb{E}_\infty$ and left modules from right modules. A passage that
manufactures a naive reader — "you might think $R$ on the left versus on
the right gives an equivalence, but it does not follow merely from
notation" — and then corrects that reader is patronizing. Even if the
premise were coherent, the corrective "you might think $X$, but you would
be wrong" positions the author above a reader who needs to be warned not
to confuse notation with mathematics. A mathematician does not need that
warning; the precise statement already trusts the reader to understand it.

**Banned:** "it does not follow merely from notation that …" — lectures a
reader who already knows $\mathbf{LMod}_R\neq\mathbf{RMod}_R$ as
$\infty$-categories over a general $\mathbb{E}_1$-ring. "For a general
ring, one might expect left and right modules to coincide, but this
requires additional data."

**Preferred:** state the precise theorem and trust the reader:
"there is no canonical equivalence
$\mathbf{LMod}_R\simeq\mathbf{RMod}_R$ for a general
$\mathbb{E}_1$-ring spectrum $R$." Do not manufacture a naive position to
knock down; do not explain what notation does not do. The book assumes
the sophistication of its intended audience (modern graduate courses at
Harvard, MIT, and Princeton; Lurie, Scholze, Gaitsgory, Haynes Miller)
and does not rehearse warnings appropriate to a first encounter with the
distinction.