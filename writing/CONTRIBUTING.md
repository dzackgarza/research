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

A notion is characterized by contrast with the alternative it rejects:
"X, not Y" / "is X, never Y" / "not just X but Y" / "X rather than Y"
— including manufactured negative parallelism of the form "their mere
existence supplies no $X$," which negates an expectation no one held.
Existence of objects never supplies an order, a comparison, or extra
structure unless one is defined; stating that it does not is true by
default and adds no claim to the skeleton (SEC-6). The contrast sounds
substantive while carrying no content, and it wastes the reader's
attention on a strawman.

**Banned:** "$a = b$ is a theorem, never a definitional identity";
"Their mere existence supplies no order relation among them" — when
several targets are available, the comparison data are either a chosen
target or a functor comparing the targets; that existence alone supplies
no order is the default and states nothing.

**Preferred:** state the positive claim and stop. "When several targets
are available, the comparison data are either a chosen target or a
functor comparing the targets." If the contrast carries information
(e.g. a genuine non-example where an expected order fails), make it a
Remark and explain the precise obstruction in context.

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

### `TERM-2`: "Homomorphism" for a morphism or map

Modern $\infty$-categorical and spectral literature writes "morphism" or
"map" in the relevant $\infty$-category — a morphism in $\mathbf{CAlg}$,
a map of $\mathbb{E}_\infty$-ring spectra, a morphism of commutative
algebra objects in $\mathbf{Sp}$ — not "homomorphism of commutative
rings." "Homomorphism" is classical universal-algebra language for a
set-map preserving operations, tied to the truncated story where a ring is
a set with addition and multiplication. In this book's ontology where
rings are $\mathbb{E}_\infty$-ring spectra (DEF-13) and maps are maps of
spectra with $\mathbb{E}_\infty$-structure, the standard word is
"morphism" or "map."

**Banned:** "Let $\varphi\colon A\to B$ be a homomorphism of commutative
rings."

**Preferred:** "Let $\varphi\colon A\to B$ be a morphism of commutative
rings" (in a genuinely classical passage where $A = \pi_0 HA$) or "let
$\varphi\colon A\to B$ be a map of $\mathbb{E}_\infty$-ring spectra" / "a
morphism in $\mathbf{CAlg}$." Use "morphism" or "map" with the
$\infty$-category stated; reserve "homomorphism" for no passage in this
book.

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

### `DEF-15`: One notion per definition block

A definition block introduces one notion with its single defining
occurrence. A block that defines left modules, right modules as left
modules over the opposite, bimodules, forgetful functors, the commutative
identification, and a warning about the noncommutative case in one go is
a grab bag, not a definition. Each notion has one block with its type,
data, and universal property; related notions have separate blocks that
cite the first.

**Banned:** "::: {#def-modules-over-ring} ## Modules over a ring — For a
ring $A$, $A\text{-}\mathbf{Mod}$ is … A right $A$-module is … An
$(A,B)$-bimodule therefore has … When $A$ is commutative … For a general
ring, an equivalence …"

**Preferred:** "::: {#def-left-modules} ## Left modules — Let $A$ be an
associative ($\mathbb{E}_1$) ring spectrum. $\mathbf{LMod}_A$ is … :::"
and then separately "::: {#def-right-modules} ## Right modules —
$\mathbf{RMod}_A := \mathbf{LMod}_{A^{\mathrm{op}}}$ :::" and so on, each
with its own defining occurrence.

### `SYM-9`: Parallel notions in uniform notation

Parallel notions use parallel notation. Left and right modules, left and
right actions, opposite categories — each pair has two sides that the
reader must distinguish at a glance. Using $A\text{-}\mathbf{Mod}$ for
left modules but $B^{\mathrm{op}}\text{-}\mathbf{Mod}$ for right modules
is inconsistent: the first names the side by position, the second by an
opposite. The same inconsistency appears in mixing
$\mathbf{LMod}_A$ with $A\text{-}\mathbf{Mod}$ in one passage.

**Banned:** "$A\text{-}\mathbf{Mod}$ for left $A$-modules but
$B^{\mathrm{op}}\text{-}\mathbf{Mod}$ for right $B$-modules in the same
passage."

**Preferred:** "$\mathbf{LMod}_A$ and $\mathbf{RMod}_A$" or
consistently "$A\text{-}\mathbf{Mod}$ and $\mathbf{Mod}\text{-}A$." Choose
one convention for sidedness and use it uniformly in the passage.

### `PR-19`: Logical connective without entailment

A logical connective — "therefore," "hence," "so," "it follows that" —
asserts a consequence. A passage that writes "An $(A,B)$-bimodule
therefore has forgetful functors …" asserts that the bimodule has
forgetful functors as a consequence of the previous line (that a right
module is a left $A^{\mathrm{op}}$-module). The functors are part of the
definition of a bimodule, not a consequence. Do not join a definition to
its own constituent data with a consequence marker.

**Banned:** "A right $A$-module is a left $A^{\mathrm{op}}$-module. An
$(A,B)$-bimodule therefore has forgetful functors …"

**Preferred:** "A right $A$-module is a left $A^{\mathrm{op}}$-module. An
$(A,B)$-bimodule is … It has forgetful functors …" State the definition;
state its data. Use "therefore" only for an actual entailment.

### `SYM-10`: Strict identity versus canonical equivalence

Strict identity ($=$), isomorphism ($\cong$), and equivalence ($\simeq$)
are distinct (NOT-2). "The identity $A=A^{\mathrm{op}}$" for a commutative
ring asserts strict identity where the book's default structure is at most
a canonical equivalence: for an $\mathbb{E}_\infty$-ring spectrum $A$,
$A\simeq A^{\mathrm{op}}$ via the symmetry; for a discrete commutative
ring the equality is strict, but only after truncating to $\pi_0$. Do not
write $A=A^{\mathrm{op}}$ for the derived identification.

**Banned:** "When $A$ is commutative, the identity $A=A^{\mathrm{op}}$
identifies left and right $A$-module conventions."

**Preferred:** "When $A$ is a commutative ($\mathbb{E}_\infty$) ring
spectrum, the symmetry gives a canonical equivalence
$A\simeq A^{\mathrm{op}}$, hence
$\mathbf{LMod}_A\simeq\mathbf{RMod}_A$." Name the equivalence and how it
is produced.

### `DEF-16`: Remark or warning inside a definition block

A definition block defines a notion. A remark about a different notion —
a warning that left and right module categories are not equivalent for a
general ring, a comment on additional data, a pointer to a subtlety —
belongs in a Remark block or in the paragraph following the definition,
not inside the definition's fenced div. A definition that contains its
own counterexample or warning cannot be cited as the defining occurrence
without dragging the warning along.

**Banned:** a "::: {#def-modules-over-ring}" block whose last sentence is
"For a general ring, an equivalence between left and right module
categories is additional data …"

**Preferred:** close the definition after its defining sentences, then
write "::: {.Remark}" or a plain paragraph for the warning. The
definition is citable; the remark is separate.

### `DEF-17`: Reminder masquerading as a definition

A paragraph that writes "For a ring $A$, write $A\text{-}\mathbf{Mod}$
for the category of left $A$-modules" does not define left $A$-modules.
It presupposes the reader already knows what a left $A$-module is and
what the category is — its objects, morphisms, composition, forgetful
functor — and merely assigns notation. No construction is stated, no
universal property is given, no data are introduced. A definition
defines: it states the objects, the structure, and the property that
determines the notion. A reminder says "recall" and cites the defining
occurrence where the notion was defined. If the notion is prerequisite,
write "Recall (@def-left-modules) that …" and cite; if it is being
defined here, construct it. Do not summon a category into existence by
naming its notation.

**Banned:** "For a ring $A$, write $A\text{-}\mathbf{Mod}$ for the
category of left $A$-modules. A right $A$-module is a left
$A^{\mathrm{op}}$-module." — no definition of "module," no construction
of the category, no objects or morphisms stated.

**Preferred:** "Let $A$ be an associative ($\mathbb{E}_1$) ring spectrum.
An $A$-module is … The $\infty$-category $\mathbf{LMod}_A$ has objects …
morphisms are … with forgetful functor …" Or, if prerequisite:
"Recall that $\mathbf{LMod}_A$ denotes … as in @def-left-modules, with
…"

### `SYM-11`: Structured object versus underlying set

A ring presented as a tuple $(|A|,+,0,\cdot,1,\ldots)$ and its opposite
$(|A|,+,0,\cdot^{\mathrm{op}},1,\ldots)$ share the underlying set $|A|$
but are not strictly equal as tuples: the multiplications are opposite,
related by the monoidal twist. Writing "the identity $A=A^{\mathrm{op}}$"
conflates equality of underlying sets with equality of structured objects.
For an $\mathbb{E}_\infty$-ring spectrum the two are canonically
equivalent via the symmetry, not strictly equal; for a discrete
commutative ring strict equality holds only after forgetting to the
underlying set or to $\pi_0$. State equality of the correct underlying
data, and name the canonical equivalence for the structured objects.

**Banned:** "the identity $A=A^{\mathrm{op}}$ identifies left and right
$A$-module conventions" — asserts strict identity of tuples whose
multiplications differ by a twist.

**Preferred:** "the underlying sets of $A$ and $A^{\mathrm{op}}$
coincide and the multiplications are opposite via the twist; for
$\mathbb{E}_\infty$ $A$ the symmetry gives a canonical equivalence
$A\simeq A^{\mathrm{op}}$, hence
$\mathbf{LMod}_A\simeq\mathbf{RMod}_A$." Distinguish the set, the
tuple, and the equivalence.

### `PR-20`: "Identifies conventions" with no mathematical content

A passage states that an identity or equivalence "identifies $X$ and $Y$
conventions" or "identifies the two notions" without naming any functor,
equivalence, or natural isomorphism. "Identifies conventions" names no
mathematical object — no map, no domain, no codomain — and has no
mathematical meaning. The precise statement is a canonical equivalence of
categories or a natural isomorphism, with source, target, and how it is
produced.

**Banned:** "the identity $A=A^{\mathrm{op}}$ identifies left and right
$A$-module conventions."

**Preferred:** "the symmetry induces a canonical equivalence
$\mathbf{LMod}_A\simeq\mathbf{RMod}_A$." Name the functor or equivalence;
do not describe it as "identifying conventions."

### `DEF-18`: Element formula on pure tensors for a functorial construction

A construction that is functorially $B\otimes_A(-)$ — extension of scalars
on modules, base change of a bilinear form as $B\otimes_A b$ — is defined
by an elementwise recipe $b_B(c\otimes x,d\otimes y)=cd\otimes b(x,y)$ on
pure tensors $c\otimes x$. The recipe names no functor, no canonical
isomorphisms, and is well-defined only by $B$-bilinear extension; it fails
outside free modules and hides whether $\otimes_A$ is the derived
($\otimes_A^L$) or underived product. The element formula, when it holds,
is a consequence of the functorial construction, not the definition.
State the functor and the canonical isomorphisms. The construction is
$$
(B\otimes_A M)\otimes_B(B\otimes_A M)\simeq
B\otimes_A(M\otimes_A M)\xrightarrow{B\otimes_A b} B\otimes_A W,
$$
i.e. $b_B$ is $B\otimes_A b$ composed with the canonical
$(B\otimes_A M)\otimes_B(B\otimes_A M)\simeq B\otimes_A(M\otimes_A M)$;
on pure tensors this is $b_B(c\otimes x,d\otimes y)=cd\otimes b(x,y)$
when $B$-bilinear extension is well-defined.

**Banned:** "Its base change is the $B$-bilinear map
$b_B(c\otimes x,d\otimes y)=cd\otimes b(x,y)$, whose value module is
$B\otimes_A W$."

**Preferred:** "Let $M,W\in\mathbf{LMod}_A$ and
$b\colon M\otimes_A M\to W$ be $A$-bilinear. Its base change is
$b_B:=(B\otimes_A b)\circ\text{can}\colon
(B\otimes_A M)\otimes_B(B\otimes_A M)\to B\otimes_A W$." State the
functor and the canonical map; derive the pure-tensor formula as a
consequence.

### `SYM-12`: Derived tensor product not distinguished from underived

In the book's derived and spectral ontology (DEF-13), $\otimes_A$ is the
derived tensor product $\otimes_A^L$; the underived tensor on discrete
modules is the further truncation $\pi_0(-\otimes_A^L-)$. Writing
$B\otimes_A M$ without stating whether it is derived or underived leaves
the reader unable to determine whether the construction is homotopically
correct. State the derived product; note when passage to $\pi_0$ recovers
the classical formula.

**Banned:** "$B\otimes_A M$" and "$b_B(c\otimes x,d\otimes y)=cd\otimes
b(x,y)$" with no indication whether $\otimes_A$ is $\otimes_A^L$.

**Preferred:** "$B\otimes_A^L M$ for derived extension of scalars; its
$\pi_0$ recovers the classical $B\otimes_A M$ for discrete $A,B,M$." Name
the derived product where it is meant.

### `TERM-3`: "Value module" for codomain or target

"Value module" is a coinage for the codomain or target of a bilinear
form. The standard terms are codomain, target, or value object. Do not
coin a synonym for a standard categorical term.

**Banned:** "whose value module is $B\otimes_A W$."

**Preferred:** "with codomain $B\otimes_A W$" or "with target
$B\otimes_A W$."

### `MA-14`: Map out of a product called bilinear versus map out of the tensor product

A bilinear map is presented as a set map $b\colon M\times M\to W$ that
"is $A$-bilinear" in prose, instead of as a morphism
$b\colon M\otimes_A M\to W$ out of the tensor product. The product
$M\times M$ and the prose qualifier "bilinear" bloat the statement: they
introduce the underlying-set product, then add the $A$-bilinearity
conditions in English, instead of using the object that represents
bilinear maps. The tensor product is the representing object:
$\operatorname{Hom}(M\otimes_A M,W)\cong\operatorname{Bilin}_A(M\times
M,W)$ is the universal property that makes bilinearity precise. State the
tensor product and the morphism out of it.

**Banned:** "Let $W$ be an $A$-module and let $b\colon M\times M\to W$ be
$A$-bilinear." — $M$ is unbound, $M\times M$ is the set product, and
"$A$-bilinear" is a prose qualifier for the linearity conditions.

**Preferred:** "Let $M,W\in\mathbf{LMod}_A$ and
$b\colon M\otimes_A M\to W$ in $\mathbf{LMod}_A$" (or
$b\colon M\otimes_A^L M\to W$ for the derived product). The single
morphism out of the tensor product replaces the map out of the product
plus the English "bilinear."

### `DEF-19`: Unconditional, conditional, and meta-remark mixed in one definition block

A definition block mixes notions with different logical status: unconditional
replete full subcategories (finitely generated, projective, free), properties
defined only under a hypothesis (torsion and torsion-free over an integral
domain), and a meta-remark about usage over a general ring. Each status has
its own block: unconditional notions have unconditional blocks; a notion
defined only under a hypothesis states the hypothesis in its block; a usage
rule is a Remark. Do not list them as parallel bullets under "The following
isomorphism-invariant properties define replete full subcategories" when the
list is not uniform.

Concrete standard (establishing the conventions named above): for an
associative ($\mathbb{E}_1$) ring spectrum $R$, $\mathbf{LMod}_R$ is the
presentable stable $\infty$-category of left $R$-module spectra.
$M\in\mathbf{LMod}_R$ is finitely generated if there exists a finite set
$I$ and an effective epimorphism $\bigoplus_{i\in I}R\twoheadrightarrow M$;
projective if $M$ is a retract of a free module
$\bigoplus_{i\in I}R$ for some set $I$; free if $M\simeq\bigoplus_{i\in
I}R$ for some set $I$; finitely generated projective if both hold, i.e.
$\mathbf{LMod}_R^{\mathrm{fg,proj}}=
\mathbf{LMod}_R^{\mathrm{fg}}\cap\mathbf{Proj}_R$, each replete full.
Torsion and torsion-free as stated below are defined only over an
integral domain $R$ (classical, i.e. $R=\pi_0 HR$ discrete): $M$ is
torsion if $\forall m\in M\,\exists\,0\neq r\in R$ with $r\cdot m=0$,
torsion-free if $\forall\,0\neq r\in R$, $r\cdot\colon M\to M$ is
injective. Over a general $\mathbb{E}_1$-ring spectrum a torsion
subcategory is not a property but a torsion theory — a hereditary torsion
pair, a $t$-structure — and is used only after that extra structure has
been specified (DEF-20).

**Banned:** "::: {#def-module-subcategories} The following
isomorphism-invariant properties define replete full subcategories of
$R\text{-}\mathbf{Mod}$: [four bullets] If $R$ is an integral domain, $M$
is torsion when … Over a general ring, a torsion subcategory is used
only after a torsion theory has been specified. :::"

**Preferred:** separate blocks: "::: {#def-fg-modules} ## Finitely
generated modules — Let $R$ be an $\mathbb{E}_1$-ring spectrum and
$M\in\mathbf{LMod}_R$. $M$ is finitely generated if … :::" and
"::: {#def-torsion-modules} ## Torsion modules (integral domain) — Let
$R$ be an integral domain (discrete) and $M\in\mathbf{LMod}_R$. $M$ is
torsion if … :::" and a separate Remark for the general $\mathbb{E}_1$
usage rule.

### `SYM-13`: Classical module notation for $\infty$-categorical modules and terminological drift

Classical notation $R\text{-}\mathbf{Mod}$, $R^{(I)}$, and $R^n$ for
modules is the truncation to the heart. The book's default is
$\mathbf{LMod}_R$, $\mathbf{RMod}_R$, ${}_A\mathbf{Bimod}_B$ (or
${}_A\mathbf{BiMod}_B$) for presentable stable $\infty$-categories of
module spectra, and $\bigoplus_{i\in I}R$ (coproduct in
$\mathbf{LMod}_R$) for the free module on a set $I$. $R^{(I)}$ and the
surjection $R^n\twoheadrightarrow M$ are the classical shadows; they are
correct only after truncating to $\pi_0$ or to discrete $R$. Allowing
$R\text{-}\mathbf{Mod}$, $\mathbf{LMod}_R$, $R^{(I)}$, $\bigoplus_I R$,
and $R^n$ to drift interchangeably is notational drift: fix one
convention for the $\infty$-categorical objects and use it uniformly and
repeatedly, stating the truncation explicitly when the classical shadow
is meant.

**Banned:** "$R\text{-}\mathbf{Mod}$ for the $\infty$-category;
$R^{(I)}$ for the free module spectrum; $R^n\twoheadrightarrow M$ for an
effective epimorphism in $\mathbf{LMod}_R$ without marking the
truncation" — or any of those notations alternating with
$\mathbf{LMod}_R$/$\bigoplus_I R$ in the same chapter.

**Preferred:** "$\mathbf{LMod}_R$ (resp. $\mathbf{RMod}_R$,
${}_A\mathbf{BiMod}_B$) for $\infty$-categories;
$\bigoplus_{i\in I}R\twoheadrightarrow M$ as an effective epimorphism for
finitely generated; $M\simeq\bigoplus_{i\in I}R$ for free." Fix the
$\infty$-categorical convention once and use it uniformly; note when
passage to $\pi_0$ recovers the classical $R\text{-}\mathbf{Mod}$ or
$R^{(I)}$.

### `PR-21`: Definition missing "is … if …" and quantifier, redundant qualifier

A property is defined as "finitely generated: some $R^n\twoheadrightarrow
M$ is surjective" — no "M is … if …", no quantifier for $M$ or $n$, and
redundant "is surjective" after $\twoheadrightarrow$ (which already means
surjective). A property that defines a replete full subcategory is stated
as "$M$ is $P$ if …" with $M$ bound and the quantifiers explicit; the
surjection is written $R^n\to M$ or declared surjective without doubling
the word.

**Banned:** "finitely generated: some $R^n\twoheadrightarrow M$ is
surjective" — $M$ unbound, no "is … if …", redundant "is surjective."

**Preferred:** "$M\in\mathbf{LMod}_R$ is finitely generated if there
exists a finite set $I$ and an effective epimorphism
$\bigoplus_{i\in I}R\twoheadrightarrow M$." Bind $M$, state the
quantifiers, and do not double the surjectivity marker.

### `DEF-20`: Torsion over a general ring is extra structure, not a property

Over an integral domain $R$ (discrete, $R=\pi_0 HR$), torsion and
torsion-free are properties of $M\in\mathbf{LMod}_R$: $M$ is torsion if
$\forall m\,\exists\,0\neq r$ with $r\cdot m=0$, equivalently
$\operatorname{Ann}_R(m)\neq0$ for every $m$ (see MA-15); $M$ is
torsion-free if $\operatorname{Ann}_R(m)=0$ for $m\neq0$. Over a general
associative ($\mathbb{E}_1$) ring spectrum $R$, a "torsion subcategory"
is not a property of $M$ but extra structure: a hereditary torsion pair
$(\mathcal{T},\mathcal{F})$, a $t$-structure, or a localizing
subcategory with its torsion functor — not "a torsion theory," which has
no referent (TERM-4). The last sentence of {#def-module-subcategories}
is a prose usage rule with no construction. State the precise structure
and cite its definition; put the usage rule in a Remark, not in the
definition of finitely generated projective modules.

**Banned:** the last sentence of {#def-module-subcategories} as part of
the definition of $R\text{-}\mathbf{Mod}$ subcategories, and "a torsion
theory has been specified" with no definition of "torsion theory."

**Preferred:** "::: {.Remark} Over a general $\mathbb{E}_1$-ring spectrum
$R$, a torsion subcategory means a hereditary torsion pair
$(\mathcal{T},\mathcal{F})$ on $\mathbf{LMod}_R$ (see @def-torsion-pair)
or the corresponding $t$-structure, and is used only after that pair has
been specified. :::"

### `SEC-8`: Specialization of a general construction with no new claim

A general construction is already defined — extension of scalars
$B\otimes_A^L-\colon\mathbf{LMod}_A\to\mathbf{LMod}_B$ left adjoint to
restriction along $A\to B$, base change of a bilinear form as
$B\otimes_A^L b$, etc. Stating its specialization at specific constants
with no new definition, theorem, or computation is filler: it restates
the definiens on objects ("sends $L$ to $L\otimes_{\mathbb Z}\mathbb
Z_p$") that is already the definition of the functor on objects, and
contributes no fenced unit to the skeleton (SEC-6).

Concrete standard: define $B\otimes_A^L-$ once as the left adjoint to
$\operatorname{Res}_\varphi$; then write $L\otimes_{\mathbb Z}\mathbb Z_p$
or $L\otimes_{\mathbb Z}^L\mathbb Z_p$ without a separate sentence
announcing that this is what the functor does for $\mathbb Z\to\mathbb
Z_p$.

**Banned:** "Extension of scalars along $\mathbb Z\to\mathbb Z_p$ sends a
$\mathbb Z$-module $L$ to $L\otimes_{\mathbb Z}\mathbb Z_p$" as a
standalone sentence.

**Preferred:** define $B\otimes_A^L-$ once; then use
$L\otimes_{\mathbb Z}\mathbb Z_p$ inline. If the specialization has a
claim, make it a fenced unit: "::: {#exm-extension-Zp} ## Extension to
$\mathbb Z_p$ — For $L\in\mathbf{LMod}_{\mathbb Z}$, $L\otimes_{\mathbb
Z}^L\mathbb Z_p$ is $p$-adic completion when $L$ is finitely generated;
$\operatorname{Tor}_1^{\mathbb Z}(L,\mathbb Z_p)=0$ iff … :::" — a
Proposition/Example with a precise claim, not a restatement of the
general definiens.

### `TERM-4`: "Torsion theory" with no referent

"Torsion theory" is not a mathematical object. There are hereditary
torsion pairs, $t$-structures, and localizing subcategories with torsion
functors — each with a definition. A passage that writes "a torsion
theory has been specified" invents a term with no definition, no
citation, and no construction, and uses it as if it were standard.
Name the precise structure.

**Banned:** "Over a general ring, a torsion subcategory is used only
after a torsion theory has been specified."

**Preferred:** "Over a general $\mathbb{E}_1$-ring spectrum $R$, a
torsion subcategory is used only after a hereditary torsion pair
$(\mathcal{T},\mathcal{F})$ on $\mathbf{LMod}_R$ (see @def-torsion-pair)
has been specified" or "after a $t$-structure
$(\mathbf{LMod}_R^{\ge0},\mathbf{LMod}_R^{\le0})$ has been specified."

### `DEF-21`: Compound term defined by "both conditions hold"

A new term "finitely generated projective" is introduced as "both of the
first two conditions hold," referencing bullet order, instead of defining
"finitely generated" and "projective" and noting the subcategory of
objects satisfying both is the intersection. The compound is not
primitive; its meaning is the conjunction, and the equivalence with other
characterizations (dualizable, compact projective) is a theorem.

**Banned:** "finitely generated projective: both of the first two
conditions hold."

**Preferred:** "An $R$-module $M$ is finitely generated projective if it
is finitely generated and projective, i.e.
$M\in\mathbf{LMod}_R^{\mathrm{fg}}\cap\mathbf{Proj}_R$, each replete
full." Define each property separately; the conjunction is the
intersection, not a new primitive.

### `PR-22`: "Some … is …" for $\exists$

A property quantified by "there exists" is written as "some
$R^n\twoheadrightarrow M$ is surjective" — colloquial quantification that
picks a morphism $R^n\to M$ and then asks whether that already-surjective
arrow is surjective. Standard sources write the quantifier explicitly and
do not double the surjectivity marker ($\twoheadrightarrow$ already means
surjective).

**Banned:** "finitely generated: some $R^n\twoheadrightarrow M$ is
surjective."

**Preferred:** "there exists a finite set $I$ and an effective
epimorphism $\bigoplus_{i\in I}R\twoheadrightarrow M$" (classical shadow:
"there exists $n$ and a surjection $R^n\to M$"). State "there exists"
and the surjection once; do not write "$\twoheadrightarrow$ is
surjective."

### `DEF-22`: Characterization presented as definition, freely interchanging equivalent definitions

A notion is defined by a characterization whose equivalence with the
defining property is a theorem — often a theorem that is not proved or
cited here, and whose equivalence is assumed to still hold in this highly
specialized context (e.g. $\infty$-categorical, derived) without
argument. "$M$ is a direct summand of a free module" is the theorem
"projective iff retract of free," not the definition. Freely
interchanging such characterizations as if they were the same definition
hides the theorem.

Concrete standard: $M\in\mathbf{LMod}_R$ is **projective** if
$\operatorname{Hom}_R(M,-)$ preserves effective epimorphisms,
equivalently every diagram
$$
\begin{tikzcd}
& M\arrow[d]\\
N\arrow[r,two heads]&P
\end{tikzcd}
$$
with $N\twoheadrightarrow P$ lifts, equivalently every surjection
$N\twoheadrightarrow M$ splits. Theorem: $M$ is projective iff it is a
retract of $\bigoplus_{i\in I}R$ for some set $I$ — stated and proved or
cited, and checked to hold in the $\infty$-categorical/derived context
where it is used. Similarly, $M$ is finitely generated if
$\operatorname{Hom}_R(M,-)$ preserves filtered colimits, equivalently the
surjection condition above; state the definition, then cite the
characterization as a theorem and do not freely substitute one for the
other.

**Banned:** "projective: $M$ is a direct summand of a free module" as the
definition; "finitely generated: some $R^n\twoheadrightarrow M$ is
surjective" as the definition without the generating-set or compactness
formulation; using either characterization later as if it were the
definition without citing the equivalence.

**Preferred:** define $M$ projective by the lifting property; then
"Theorem: $M$ is projective iff it is a retract of a free module
$\bigoplus_{i\in I}R$." Define $M$ finitely generated by the generating
set; then "iff there exists a finite $I$ and an effective epimorphism
$\bigoplus_{i\in I}R\twoheadrightarrow M$." State which is the definition
and which is the theorem, and ensure the cited equivalence holds in the
specialized context where it is used.

### `MA-15`: Prose to avoid defining the annihilator

A paragraph of English — "every element is annihilated by a nonzero
element of $R$," "multiplication by every nonzero element of $R$ is
injective" — is used to avoid defining the annihilator ideal. The ideal
is the standard algebraic object; defining it once makes every later
torsion statement precise and short. Define the ideal.

Concrete standard: for $R$ an integral domain (discrete) and
$m\in M\in\mathbf{LMod}_R$, put
$\operatorname{Ann}_R(m):=\{r\in R\mid r\cdot m=0\}\trianglelefteq R$.
Then $M$ is torsion if $\operatorname{Ann}_R(m)\neq0$ for every $m\in M$
($\forall m\,\exists\,0\neq r$ with $r\cdot m=0$), torsion-free if
$\operatorname{Ann}_R(m)=0$ for $m\neq0$, equivalently
$r\cdot\colon M\to M$ injective for $0\neq r\in R$.

**Banned:** "M is torsion when every element is annihilated by a nonzero
element of $R$, and torsion-free when multiplication by every nonzero
element of $R$ is injective" — two English paragraphs with per-element
quantifiers hidden in prose.

**Preferred:** define $\operatorname{Ann}_R(m)$ once, then "$M$ is
torsion if $\operatorname{Ann}_R(m)\neq0$ for every $m\in M$;
torsion-free if $\operatorname{Ann}_R(m)=0$ for $m\neq0$."

## Section structure (`SEC-*`)

A $\S$ is its fenced logical units. The book's logical units are fenced
blocks — Definition (`::: {#def-...}`), Theorem (`::: {.Theorem
#thm:...}`), Lemma, Proposition, Corollary, Example (`::: {#exm-...}`),
Remark (`::: {.Remark}`) — each with an ID and a title, citable via
`\ref`/`\longref` or `@`. Running prose that points at a definition
elsewhere, cites a theorem elsewhere, or paraphrases either in English is
not a logical unit that belongs to this book.

### `SEC-1`: A section with no fenced logical unit has no content

A $\S$ that contains only prose paragraphs — "Preservation, reflection,
and creation of limits are defined in @def-...," "A monadic functor
creates any limits [@Rie16]," "Hence a limit in $R\text{-}\mathbf{Mod}$
is computed on underlying sets," "The kernel … is a limit — the equalizer
… — so it is the set-theoretic kernel …," "Creation is a statement about
limit cones: a subgroup … need not be a submodule …" — has no Definition,
no Theorem, no Example, and no Remark that belongs to this $\S$. The
title "Creation of limits" is then a heading over filler. Every $\S$
introduces at least one fenced unit of its own; a $\S$ that only cites
and paraphrases is not a $\S$.

**Banned:** "## Creation of limits {#sec-creation}" followed by five
paragraphs, none fenced, that cite @def-preserve-reflect-create,
[@Rie16, Theorem 5.6.5], [@Rie16, Corollary 5.5.3], then "Hence …" and
"The kernel … so it is …" in prose.

**Preferred:** "::: {#def-create} ## Creation of limits — … :::" or
"::: {.Proposition #prp-limit-created} ### Limits in $R\text{-}\mathbf{Mod}$
— … :::" with proof that cites the monadicity theorem and explains how
it applies. The $\S$'s content is the fenced unit; the paragraphs are the
proof or the remarks that follow it, not the $\S$ itself.

### `SEC-2`: Example and remark inside a mathematical section must be fenced

"For example, the additive and multiplicative monoids of a ring define
distinct functors $\mathbf{Ring}\to\mathbf{Mon}$" is an example without
an `{#exm-...}` block. "If no comparison is specified, $F$ and $G$ remain
distinct" is a remark about parallel functors without a `{.Remark}`. An
example and a remark that belong to a $\S$ are fenced and typed, not
"For example, …" or "If … remain distinct" in running prose. An
extended remark that is fenced is fine to leave unlabeled as a Remark;
an unfenced paragraph is not a Remark.

**Banned:** "For example, the additive and multiplicative monoids …" as a
closing sentence of $\S$ Parallel functors.

**Preferred:** "::: {#exm-add-vs-mult} ## Additive versus multiplicative
— The functors $\mathbf{Ring}\to\mathbf{Mon}$ sending $R$ to
$(|R|,+,0)$ and to $(|R|,\cdot,1)$ are distinct; no natural isomorphism
is specified. :::"

### `SEC-3`: Writing requirement not inside a mathematical section

"A construction whose value happens to agree on underlying sets across
two categories names the functor along which it is created" and "If no
comparison is specified, $F$ and $G$ remain distinct" are writing
requirements about how to speak about constructions versus statements and
about when parallel functors are distinct. They belong in a requirements
section (@sec-statements-vs-constructions) or in CONTRIBUTING.md
(PR-15, PR-16), not as closing morals of $\S$ Creation and $\S$ Parallel
functors. A $\S$ that states a theorem about monadic functors does not
close with a style rule.

**Banned:** the last paragraph of each $\S$ in the quoted block as a
prose moral inside a mathematical $\S$.

**Preferred:** state the theorem, prove it, give the example and the
non-example (kernel versus subgroup — the latter as a fenced
non-example or Remark that a subgroup of the underlying abelian group
need not be a submodule), then close. Put the writing requirement in the
requirements $\S$ where it is defined and cite it.

### `SEC-4`: Arbitrary breaking of a work into sections

A work is broken into titled $\S$'s that do not reflect logical
dependency or coherent grouping of units, but partition prose arbitrarily
to create length or satisfy a template. Standard textbooks and papers
organize $\S$'s around dependency: foundations (what a functor,
natural transformation, and comparison are) before general notions
(preservation/reflection/creation), before theorems (monadic functors
create limits), before applications (limits in $R\text{-}\mathbf{Mod}$
computed on underlying sets). A titled $\S$ that exists to house a few
paragraphs of paraphrase is not a $\S$.

Concrete standard (amsthm): a $\S$ title names the mathematics its fenced
units develop, and its position in the chapter reflects what those units
define and what they use. Hartshorne, EGA, Lurie *Higher Topos Theory* and
*Higher Algebra*, Riehl *Category Theory in Context* each place
$2$-categorical foundations (parallel functors, natural isomorphisms)
before any use of monadicity; creation via monadicity is in the
monadicity chapter, not adjacent to the definition of a comparison.

**Banned:** the quoted block's consecutive siblings "Creation of limits
{#sec-creation}" and "Parallel functors {#sec-parallel-functors}" — the
first is a specific application of monadicity, the second is a
foundational $2$-categorical distinction that belongs in foundations, and
neither contains a primary fenced unit of its own.

**Preferred:** place "Parallel functors / comparisons / natural
isomorphisms" in categorical foundations before any use of preservation
or creation; place "Creation of limits via monadic functors" after the
monadicity theorem, with its corollary (limits in algebraic categories)
and its example (kernel) and non-example (subgroup need not be
submodule), in the chapter where limits in algebraic categories are
developed, at the point where the dependency is satisfied.

### `SEC-5`: A section that is entirely remarks

A $\S$ whose only content would be Remarks — or whose unfenced prose is
all remarks, morals, and writing requirements ("Creation is a statement
about limit cones: a subgroup … need not be a submodule …", "If no
comparison is specified, $F$ and $G$ remain distinct," "A construction
whose value happens to agree … names the functor …") — has no primary
mathematical content. In amsthm style a Remark is secondary to a
Definition, Theorem, Lemma, Proposition, Corollary, or Example; a $\S$ of
only Remarks has nothing to remark on. If there is a precise claim, state
it as the $\S$'s primary unit; if there is not, the $\S$ should not
exist.

**Banned:** a titled $\S$ whose paragraphs are all of the form "Creation
is a statement about …" / "A construction whose value happens to agree
…" / "If no comparison is specified …" — remarks without a primary
Definition/Theorem/Example that belongs to this $\S$.

**Preferred:** either state the primary claim as a fenced Proposition,
Example, or Remark attached to a primary unit ("The forgetful
$U\colon R\text{-}\mathbf{Mod}\to\mathbf{Sets}$ creates limits; the
underlying set of a kernel carries a unique $R$-module structure making
it the kernel" as Corollary with proof), or do not create the $\S$. A
genuine meta-remark about how to speak about created limits versus
underlying-set agreement belongs in the requirements $\S$ or in a
Remark attached to the corollary, not as a standalone $\S$.

### `SEC-6`: The skeleton is the fenced logical units

The underlying skeleton of a paper or book is the set of fenced logical
units — Definition (`::: {#def-...}`), Theorem (`::: {.Theorem
#thm:...}`), Lemma, Proposition, Corollary, and Example (`:::
{#exm-...}`) — each with its ID, title, hypotheses, quantifiers, and
types. Their dependency graph is the work: every term used in a theorem
is defined in a prior definition, every lemma used in a proof is proved
earlier, every example instantiates a definition. The skeleton must be
logically coherent and mathematically complete when every non-unit is
removed — connecting prose, motivation, transitions, and Remarks. If the
skeleton is not coherent on its own, the work is incomplete.

Concrete standard (amsthm): Hartshorne, EGA, Lurie *Higher Topos Theory*
and *Higher Algebra*, Riehl *Category Theory in Context* each present a
chapter as a sequence of fenced units with proofs; the prose between them
is glue. Deleting the glue and the Remarks leaves a citable, checkable
graph that still defines every term and proves every claim. A section
contributes to that graph only through its fenced units.

**Banned:** a manuscript where the fenced units alone — Definitions,
Theorems, and Examples with their IDs stripped of surrounding prose — do
not define every term, do not state every claim, or do not prove every
theorem.

**Preferred:** write the fenced units first as the skeleton; then add
prose and Remarks as glue. Test by deleting every non-unit: the remaining
fenced units with their proofs still form a complete, dependency-ordered
mathematical text.

### `SEC-7`: Remarks are for pedagogy, not for primary claims

A Remark (`::: {.Remark}`) is secondary to the skeleton: pedagogy,
intuition, a warning that a subgroup of the underlying abelian group need
not be a submodule, a note that two parallel functors are distinct unless
a comparison is specified, an alternative viewpoint. A Remark does not
introduce a new definition, a new theorem, or a new example that belongs
to the book. A $\S$ whose fenced content would be only Remarks, or whose
unfenced prose is all remarks and morals, has no primary claim and is out
of place in a standard text.

**Banned:** a titled $\S$ that would contain no Definition, Theorem,
Lemma, Proposition, Corollary, or Example even after fencing — only
"Creation is a statement about limit cones …" and "If no comparison is
specified, $F$ and $G$ remain distinct" as Remarks.

**Preferred:** attach the remark to its primary unit: the subgroup
non-example as a Remark following the Corollary that $U$ creates limits
(and the kernel Example), the parallel-functors distinction as a Remark
following the definition of a natural transformation. If there is no
primary unit to attach to, the $\S$ should not exist; the remark belongs
in the requirements $\S$ or in CONTRIBUTING.md.

### `TERM-5`: Colloquial "lands", "property", "structure" without a precise definition

Colloquial terms "lands (in)", "property", "structure", "stuff" are used
as if their meaning were obvious — "a theorem that $F$ lands in $D_P$ is
a factorization," "being torsion-free is a property," "being a torsor is
structure" — without ever giving the precise categorical definition. In
this book each has a precise meaning: "$F$ lands in $D_P$" means a
factorization $F\simeq i\circ\bar F$ through the replete full inclusion
$i\colon D_P\hookrightarrow D$ (with $\bar F$ the corestriction and
$\alpha\colon F\simeq i\circ\bar F$ the specified equivalence);
"property" means the forgetful functor $U\colon\mathcal{S}\to\mathcal{C}$
is fully faithful, "structure" means $U$ is faithful, "stuff" means
$U$ is arbitrary (STR-1), each with its fiber condition. Do not use the
colloquial term in a definition, theorem, or title before the precise
term has been fenced and defined.

**Banned:** "A theorem that $F\colon\mathcal{C}\to\mathcal{D}$ lands in a
replete full subcategory $i\colon D_P\hookrightarrow D$ is a factorization
$F=i\circ\bar F$" — uses "lands in" as if defined, with no fenced
definition of "lands in" as factorization.

**Preferred:** first define: "::: {#def-lands} ## Lands in — A functor
$F\colon\mathcal{C}\to\mathcal{D}$ **lands in** a replete full
subcategory $i\colon D_P\hookrightarrow\mathcal{D}$ if there exists a
functor $\bar F\colon\mathcal{C}\to D_P$ and a specified natural
equivalence $\alpha\colon F\simeq i\circ\bar F$. The triple
$(\bar F,\alpha)$ is a factorization of $F$ through $D_P$. :::" Then
later: "Proposition: The functor $F$ lands in $D_P$ via $\bar F$ with
$\alpha$."

### `DEF-29`: Definition in running prose without a fenced block is not a definition

A sentence in running prose that looks like a definition — "A
factorization of $F$ through $D$ consists of functors $H$ and $G$
together with …," "A theorem that $F$ lands is a factorization" — is not
a definition. A definition is a fenced block `::: {#def-...} ## Title`
with the definiendum bold at its first introduction, a single defining
occurrence (DEF-1), and citable via `\ref`/`\longref`. Running prose
cannot be cited, has no ID, and has no logical status. Colloquial
"property," "structure," and "lands" definitions in prose are not
definitions.

**Banned:** "## Landing statements and constructions {#sec-statements-vs-
constructions} A theorem that $F\colon\mathcal{C}\to\mathcal{D}$ lands in
$D_P$ is a factorization $F=i\circ\bar F$. This theorem does not redefine
$F$ or $D_P$." — two sentences of prose, no fenced `{#def-lands}` or
`{.Theorem}`, no bold term.

**Preferred:** "::: {#def-lands} ## Lands in — … :::" as above, and
"::: {.Proposition #prp-lands} ### Landing — … :::" with proof exhibiting
$\bar F$ and $\alpha$. The prose between fenced units is glue, not the
definition.

### `XREF-5`: Use of a defined term linked to its defining occurrence

Any use of a term that is defined within the book — "lands in,"
"replete full subcategory," "factorization," "torsion," "basis,"
"based module," "distinguished" — is linked to that definition via
`\ref{def-...}`, `\longref{def-...}`, or `@def-...`. The link makes the
defining occurrence citable and lets the reader navigate to the precise
meaning (DEF-1); an unlinked use leaves the reader to guess which
occurrence is defining and whether the term is being used in its defined
sense. This applies to every occurrence that relies on the defined
meaning, not just the first.

**Banned:** "A theorem that $F$ lands in $D_P$ is a factorization" with
no link to `{#def-lands}`; "a torsion module" with no link to the
torsion definition; "a basis indexed by $I$" with no link to the basis
definition.

**Preferred:** "A theorem that $F$ **lands in** $D_P$ (\ref{def-lands})
is a factorization"; "a **torsion** module (\ref{def-torsion})"; "a
**basis** indexed by $I$ (\ref{def-basis})". Link the term at its use to
its fenced defining occurrence.

### `XREF-6`: "Is defined in …; it is …" for recall

A defined term whose defining occurrence is elsewhere is referred back to
as "A generalized element with domain $T$ is defined in
@def-generalized-element; it is a morphism $T\to X$" — two clauses, the
first meta-commentary about where the definition lives, the second
restating the definiens. The standard rhetorical device in papers and
textbooks for a non-defining use that reminds the reader is "Recall."

**Banned:** "A generalized element with domain $T$ is defined in
@def-generalized-element; it is a morphism $T\to X$." — wordy, two
clauses where one does the work, with a semicolon joining meta-commentary
to definiens; $T$ unbound.

**Preferred:** "Recall that a generalized element with domain $T$
(\ref{def-generalized-element}) is a morphism $T\to X$" or "Recall
(@def-generalized-element) that a generalized element of $X$ with domain
$T$ is a morphism $T\to X$." One clause, "Recall" signals this is not the
defining occurrence but a reminder that cites it, and the parenthetical
`\ref` is the link.

### `DEF-30`: Circular definition via diagram label

The definiendum appears as a label in the diagram that is supposed to
define it — the square's apex is already labeled $f^{-1}(y)$ and then the
text says "the fiber of $f$ over $y$ is the apex." The diagram
presupposes the notation being defined. Label the apex neutrally (e.g.
$P$) in the diagram that defines it; introduce the notation
$f^{-1}(y):=P$ after the universal property is stated.

**Banned:** the quoted square with apex $f^{-1}(y)$ and the sentence
"The fiber of $f$ over $y$ is the apex of the cartesian square" — the
apex is already called $f^{-1}(y)$.

**Preferred:** "The **fiber** $f^{-1}(y)$ is the pullback $X\times_Y 1$,
i.e. an object $f^{-1}(y)$ equipped with projections
$p_1\colon f^{-1}(y)\to X$, $p_2\colon f^{-1}(y)\to1$ and a specified
equivalence $f\circ p_1\simeq y\circ p_2$ exhibiting the square as
(homotopy) cartesian. In the diagram write the apex as $X\times_Y 1$ or
$P$, then put $f^{-1}(y):=X\times_Y 1$."

### `DEF-31`: "The relevant pullbacks" as a hypothesis

A definition assumes "let $\mathcal{C}$ have a terminal object $1$ and
the relevant pullbacks" without stating which pullbacks are assumed to
exist. "The relevant" names no class of diagrams and the reader cannot
determine whether the particular pullback needed for the definition
exists. State the hypothesis: either "$\mathcal{C}$ has all pullbacks"
or "assume the pullback of $f$ along $y$ exists."

**Banned:** "Let $\mathcal{C}$ have a terminal object $1$ and the
relevant pullbacks, let $f\colon X\to Y$, and let $y\colon1\to Y$ be a
point."

**Preferred:** "Let $\mathcal{C}$ be an $\infty$-category with terminal
object $1$ and assume the pullback of $f\colon X\to Y$ along
$y\colon1\to Y$ exists" or "Let $\mathcal{C}$ be an $\infty$-category
with all pullbacks, terminal object $1$, $f\colon X\to Y$, and
$y\colon1\to Y$."

### `DEF-32`: Fiber as apex alone, without its projections and homotopy

The fiber is defined as "the apex of the cartesian square," naming only
the object $f^{-1}(y)$. The fiber is the object *equipped with* its
projections $f^{-1}(y)\to X$, $f^{-1}(y)\to1$ and the specified
equivalence $f\circ\mathrm{pr}_X\simeq y\circ\mathrm{pr}_1$ that exhibits
the square as cartesian. In the book's default
$\mathcal{C}:=\mathbf{Cat}_\infty$ the square is a homotopy pullback,
unique up to a contractible space of equivalences, not a strict pullback
with a unique apex on the nose.

Concrete standard: for $f\colon X\to Y$ and $y\colon1\to Y$ in an
$\infty$-category with pullbacks, the **fiber** is the homotopy pullback
$f^{-1}(y):=X\times_Y 1$ with its projections and the specified
$2$-cell $f\circ p_1\Rightarrow y\circ p_2$ (marked $\lrcorner$).

**Banned:** "The fiber of $f$ over $y$ is the apex of the cartesian
square" with the square's two projections and $2$-cell unstated.

**Preferred:** "The **fiber** of $f$ over $y$ is the homotopy pullback
$X\times_Y 1$, i.e. the object $f^{-1}(y)$ with $p_1\colon f^{-1}(y)\to X$,
$p_2\colon f^{-1}(y)\to1$, and $\alpha\colon f\circ p_1\simeq y\circ p_2$
exhibiting the square as cartesian."

### `DEF-33`: Special case without scaffolding from the general notion

A general construction is introduced at its special case. The fiber
$f^{-1}(y)$ is a special case of a fiber product (pullback); freeness is
a special case of the free-forgetful adjunction; being a basis is a
special case of a generating family. The standard is to state the general
construction first, with its universal property and notation, and then
specialize by reference — not to use the special case as the place to
introduce the general construction. Defining the special case without the
general notion repeats the cone's universal property that belongs in the
general definition and leaves the general notion undefined.

Concrete standard: define pullbacks as limits of cospans (\ref{def-pullback}):
for $f\colon X\to Y$ and $g\colon Z\to Y$ in an $\infty$-category with
pullbacks, the **pullback** is the limit $X\times_Y Z$ with its cone
$(X\times_Y Z\to X, X\times_Y Z\to Z)$ terminal among cones over the
cospan. Then: "The **fiber** of $f$ over $y\colon1\to Y$ is the pullback
$X\times_Y 1$ of $f$ along $y$ (\ref{def-pullback})." This pattern is
general: the free module functor $F\colon\mathbf{Sets}\to\mathbf{LMod}_R$,
the notion of generating family, and freeness are defined before
"basis" and "based module" (DEF-23).

**Banned:** "Let $\mathcal{C}$ have a terminal object $1$ and the
relevant pullbacks, let $f\colon X\to Y$, and let $y\colon1\to Y$ be a
point. The fiber of $f$ over $y$ is the apex of the cartesian square …"
— defines the special case without the general notion.

**Preferred:** define $X\times_Y Z$ once via terminal cones; then "the
fiber is $X\times_Y 1$, the pullback of $f$ along $y$."

### `PR-27`: Long prose where concise notation already exists

Concise notation already encodes the universal property. "Pullback of $f$
along $y$" and $X\times_Y 1$, $M\otimes_A N$ for $\operatorname{Hom}(M\otimes_A
M,W)$, $\bigoplus_{i\in I}R$ for $R^{(I)}$, a tuple
$(\mathcal{C},\otimes,\mathbf{1},\alpha,\lambda,\varrho)$ for a monoidal
category — each replaces a paragraph of English. Using long prose where
that notation exists bloats the text and is the general pattern behind
"the apex of the cartesian square" for $X\times_Y 1$, "a map
$M\times M\to W$ that is $A$-bilinear" for $M\otimes_A M\to W$ (MA-14),
and "a choice of $a\otimes b$ for every $a,b$" for the functor
$\otimes\colon\mathcal{C}\times\mathcal{C}\to\mathcal{C}$ (MA-13).

**Banned:** "the fiber of $f$ over $y$ is the apex of the cartesian
square"; "let $b\colon M\times M\to W$ be $A$-bilinear" for
$b\colon M\otimes_A M\to W$; "a monoid for the cartesian structure."

**Preferred:** "the fiber is the pullback $X\times_Y 1$ of $f$ along $y$";
"$b\colon M\otimes_A M\to W$"; "a monoid object in
$(\mathcal{C},\times,\mathbf{1})$." Use the concise notation that already
exists for the precise object.

### `TERM-7`: Colloquial term without definition, and confabulated term that hides necessary details

A term is used as if its meaning were obvious when it is not defined
anywhere in this book and is not obvious to an undergraduate. Colloquial
terms — "apex" for the vertex of a cone, "carries," "transports,"
"identifies conventions," "value module" — and confabulated terms that
sound technical but have no referent — "torsion theory," "apex" as a
standalone noun for a terminal cone — hide necessary details. "Apex"
alone names no cone and no universal property; its standard counterpart
is the (terminal) cone $(P\to X, P\to Z)$ over $X\to Y\leftarrow Z$ that
is terminal among cones, introduced once in the definition of pullbacks.
Every technical term beyond what an undergraduate would know is fenced
and defined before use; a colloquial term is not used in its place.

**Banned:** "the fiber … is the apex of the cartesian square";
"objects that carry both structures" (EV-2); "the discriminant package"
(EV-3); "a torsion theory has been specified" (TERM-4).

**Preferred:** "the fiber is the pullback $X\times_Y 1$ with its terminal
cone $(X\times_Y 1\to X, X\times_Y 1\to1)$"; "a structure on $X$ is a
chosen object in the fiber over $X$ of $U\colon\mathcal{S}\to\mathcal{C}$";
"a hereditary torsion pair $(\mathcal{T},\mathcal{F})$ has been
specified."

### `TERM-8`: Colloquial "cartesian square" and technical term not defined in this book

"Cartesian square" is colloquial for a pullback square and, when used
without definition, also hides a theorem: when a square's projection is
a (co)cartesian fibration and the square is a pullback in
$\mathbf{Cat}_\infty$, the projection is a (co)cartesian fibration. More
generally, any technical term beyond what an undergraduate would know —
"pullback," "cartesian fibration," "torsion pair," "annihilator," "basis"
— must be fenced and defined in this book before use, not used as if
its meaning were obvious or as if the reader will supply the definition
from prior knowledge. Colloquial and undefined technical terms are not
interchangeable with the precise defined terms.

**Banned:** "the apex of the cartesian square"; "a torsion theory has
been specified" (TERM-4); "$\mathbf{Sh}_\Sigma$ for a diagram category"
(MA-3) without definition.

**Preferred:** "the pullback square exhibiting $X\times_Y 1$" (with
`{#def-pullback}` defined) or "the square exhibiting the pullback."
Reserve "cartesian fibration" for the fibration property and prove when a
pullback square has that property. Define every non-undergraduate
technical term in a fenced block before its first use.

### `PR-24`: Self-referential meta-prose about the text's structure, notation, or theorems

A professional mathematics text extremely rarely is self-referential,
describes its own structure, notation, or what its theorems do or do not
do. If ever such things are included, they are at best very small
footnotes, but should be avoided altogether. Prose that talks about the
text — "is defined in @def-…; it is …" (where the definition lives),
"This theorem does not redefine $F$ or $D_P$" (what the theorem does not
do), "Their mere existence supplies no order relation" (what existence
does not do), "is what licenses the notation $a_1\otimes\cdots\otimes a_n$"
(what the theorem does for notation), "A construction whose value happens
to agree on underlying sets … names the functor" and "If no comparison is
specified, $F$ and $G$ remain distinct" (writing requirements as closing
morals), "is additional data; it does not follow merely from notation"
(what notation does not do, with strawman) — is meta-prose, not
mathematics. The text states the mathematics via fenced units and links;
it does not describe its own structure.

Concrete standard: Hartshorne, EGA, Lurie *Higher Topos Theory* and
*Higher Algebra*, Riehl *Category Theory in Context* state definitions,
theorems, and examples with fenced units and parenthetical `\ref`s; they
do not narrate where a definition lives, what a theorem does not
redefine, or what notation does not imply. Cross-references via
`\ref`/`\longref`/`@` are not self-reference; they are citations.

**Banned:** all of the above meta-sentences as running prose inside
mathematical $\S$'s.

**Preferred:** state the mathematics — a fenced `::: {#def-...}` with the
term bold, a Proposition with proof exhibiting the factorization, an
Example, a Remark attached to its primary unit — and link with
`(\ref{def-...})` or "Recall that … (\ref{def-...})". If a notational
clarification is truly needed, put it in a footnote `[^1]` and keep it to
one clause, but prefer to avoid it by stating the mathematics precisely.

### `PR-25`: "Names the …" for specifies/exhibits/is equipped with

"Names" has no established mathematical meaning — nothing in mathematics
"names" anything else. A construction does not "name the functor along
which it is created," "name the comparison," or "name the factorization."
The standard verbs for extra structure on a construction each have a clear
a priori mathematical meaning: **specifies** (gives the data),
**exhibits** (provides a witness), **is given by** (is presented as),
**is equipped with** / **comes with** (carries as extra structure),
**determines** / **is determined by** (is equivalent to the data),
**is witnessed by**, **is classified by** (when there is a classifying
object). If a verb is used for extra structure, it must have that clear
meaning.

**Banned:** "names the functor along which it is created"; "names the
comparison with this composite"; "names the factorization"; "names a
particular monomorphism."

**Preferred:** "specifies the functor $\bar F$ and the equivalence
$\alpha\colon F\simeq i\circ\bar F$"; "exhibits the factorization
$(\bar F,\alpha)$"; "is equipped with the comparison $2$-cell
$\gamma$"; "is determined by the invertible bimodule"; "comes with a
specified natural equivalence"; "specifies a particular monomorphism
$f\colon A\rightarrowtail B$ with $\operatorname{isMono}(f)$" / "is
equipped with a chosen monomorphism." Use "determines" / "is determined
by" only when the data are equivalent.

### `PR-26`: "Some … exists is a proposition" with unbound variables and no truncation

An existence statement "some monomorphism $A\to B$ exists is a
proposition" leaves $A,B$ unbound (SYM-1), writes "some … exists" for
$\exists$ (PR-22), and calls the existence "a proposition" without
stating the truncation level. In this book a proposition is a
$(-1)$-truncated type (a mere proposition); the structure is the type
$\sum_{f\colon A\to B}\operatorname{isMono}(f)$, and the proposition
(mere existence) is its $(-1)$-truncation
$\bigl\|\sum_{f}\operatorname{isMono}(f)\bigr\|_{-1}$.

**Banned:** "The assertion that some monomorphism $A\to B$ exists is a
proposition" — $A,B$ unbound, "some … exists" for $\exists$, no type for
the monomorphisms, no $(-1)$-truncation.

**Preferred:** "Let $A,B\in\mathcal{C}$. The type
$\sum_{f\colon A\to B}\operatorname{isMono}(f)$ is the structure of a
monomorphism $A\rightarrowtail B$; its $(-1)$-truncation
$\bigl\|\sum_{f}\operatorname{isMono}(f)\bigr\|_{-1}$ is the proposition
that there merely exists a monomorphism $A\rightarrowtail B$."

### `TERM-6`: "Embedding" for "monomorphism" without definition or identification

"Monomorphism" and "embedding" are used interchangeably mid-passage —
"some monomorphism $A\to B$ exists" then "a construction that uses an
embedding names a particular monomorphism" — without ever defining
either term or stating the identification. In this book a monomorphism is
a $(-1)$-truncated map ($f$ is mono if …), an embedding is a fully
faithful functor (or, for spaces, an embedding as a $(-1)$-truncated
map with extra condition) — each with its fenced definition. Do not
switch terms without defining the identification.

**Banned:** "some monomorphism $A\to B$ exists … a construction that
uses an embedding names a particular monomorphism" — switches from
"monomorphism" to "embedding" with no definition of either and no link
between them.

**Preferred:** choose one term and define it, or define both and state
the identification: "A **monomorphism** ($f\colon A\rightarrowtail B$)
is … (\ref{def-mono}). An **embedding** is … (\ref{def-embedding}). In
$\mathbf{Sets}$, every monomorphism is an embedding; in general …" Link
each use to its defining occurrence (XREF-5).

### `DEF-27`: Distinguished object introduced only in the title

A block titled `{#def-distinguished-factorization}` defines "a
factorization of $F\colon\mathcal{C}\to\mathcal{E}$ through $\mathcal{D}$"
but never defines what "distinguished" means. The title is not the
definition. A distinguished, canonical, or standard object is a chosen
object in its category — here a chosen factorization
$(H_{\mathrm{dist}},G_{\mathrm{dist}},\alpha_{\mathrm{dist}})$ among all
factorizations of $F$ through $\mathcal{D}$ — with its construction and
the universal property or comparison that makes it distinguished stated
explicitly.

Concrete standard: for $R$ an associative ($\mathbb{E}_1$) ring spectrum,
the distinguished underlying-set functor is the composite of forgetful
functors
$$
\mathbf{LMod}_R \xrightarrow{U_{R/\mathbf{Ab}}}
\mathbf{Ab}\xrightarrow{U_{\mathbf{Ab}/\mathbf{Grp}}}
\mathbf{Grp}\xrightarrow{U_{\mathbf{Grp}/\mathbf{Sets}}}
\mathbf{Sets},
$$
each $U$ with its left adjoint $F$ (free $R$-module, free abelian group,
free group), and the factorization is distinguished among factorizations
of $U_{\mathbf{LMod}_R/\mathbf{Sets}}$ (see @def-factorization).

**Banned:** "::: {#def-distinguished-factorization} A factorization of
$F\colon\mathcal{C}\to\mathcal{E}$ through $\mathcal{D}$ consists of …
The underlying-set functor of an $R$-module is the composite
$R\text{-}\mathbf{Mod}\to\mathbf{Ab}\to\mathbf{Grp}\to\mathbf{Set}$. :::"
— the distinguished composite is asserted inside the general definition and
never defined as the distinguished object.

**Preferred:** separate blocks: "::: {#def-factorization} ## Factorization
— A factorization of $F\colon\mathcal{C}\to\mathcal{E}$ through
$\mathcal{D}$ is a tuple $(H,G,\alpha)$ with $H\colon\mathcal{C}\to
\mathcal{D}$, $G\colon\mathcal{D}\to\mathcal{E}$, and a specified natural
equivalence $\alpha\colon F\simeq G\circ H$. :::" and "::: 
{#exm-distinguished-underlying-set} ## Distinguished underlying-set
factorization — The distinguished factorization of
$U_{\mathbf{LMod}_R/\mathbf{Sets}}$ is
$(U_{\mathbf{LMod}_R/\mathbf{Ab}},U_{\mathbf{Ab}/\mathbf{Grp}}\circ
U_{\mathbf{Grp}/\mathbf{Sets}},\operatorname{id})$ as above. :::"

### `STR-4`: Strict equality versus specified natural equivalence for a factorization

A factorization is described as "an equality $F=G\circ H$ or a specified
natural isomorphism $F\Rightarrow G\circ H$" as alternatives, conflating a
property (strict equality, which does not exist in the book's
$\infty$-categorical default where $\mathbf{Cat}:=\mathbf{Cat}_\infty$)
with extra structure (a specified $2$-cell). In $\mathbf{Cat}_\infty$ a
factorization is always a tuple $(H,G,\alpha)$ with $\alpha$ a specified
natural equivalence.

**Banned:** "together with an equality $F=G\circ H$ or a specified natural
isomorphism $F\Rightarrow G\circ H$."

**Preferred:** "together with a specified natural equivalence
$\alpha\colon F\simeq G\circ H$." If the $1$-categorical strict case is
meant, state it as the truncation "$F=G\circ H$ on the nose, i.e.
$\alpha=\operatorname{id}$ in $\mathbf{Cat}_1$," not as an alternative to
the $\infty$-categorical structure.

### `PR-23`: "Accompanied by its comparison" for a specified $2$-cell

An alternative factorization's comparison with the distinguished one is
described as "is accompanied by its comparison with this composite"
instead of naming the natural transformation or equivalence and its source
and target. "Is accompanied by" is the "carries"/"transports" metaphor
(EV-7) for an unnamed $2$-cell and hides whether the comparison is a
morphism of factorizations, a natural transformation, or an equivalence.

**Banned:** "An alternative forgetful functor is accompanied by its
comparison with this composite."

**Preferred:** "An alternative factorization
$(H',G',\alpha')$ of the same $F$ comes with a specified comparison
$2$-cell $\gamma\colon(H',G',\alpha')\Rightarrow
(H_{\mathrm{dist}},G_{\mathrm{dist}},\alpha_{\mathrm{dist}})$ in
$\mathbf{Fact}_D(F)$, i.e. natural equivalences
$H'\simeq H_{\mathrm{dist}}$ and $G'\simeq G_{\mathrm{dist}}$ compatible
with $\alpha',\alpha$." Name the $2$-cell, its source, and its target.

### `DEF-28`: Example and remark inside a definition block

A general definition, its example (the underlying-set functor as the
composite through $\mathbf{Ab}$ and $\mathbf{Grp}$), and a remark about
alternative factorizations are in one fenced `{#def-...}`. Each has its
own block: the general notion has a definition block, the composite has
an example block that cites the definition, and the comparison of
alternative factorizations has a remark.

**Banned:** the quoted `{#def-distinguished-factorization}` block that
contains both the general factorization definition and the two paragraphs
about $R\text{-}\mathbf{Mod}\to\mathbf{Ab}\to\mathbf{Grp}\to\mathbf{Set}$.

**Preferred:** close the definition after the tuple
$(H,G,\alpha)$, then "::: {.Example}" for the distinguished composite,
then "::: {.Remark}" for alternative factorizations and their comparison
$2$-cells.

### `DEF-23`: Specialized notion without scaffolding from general notions

A specialized notion — a basis, a based module — is defined without first
defining the general notions it depends on: the free module functor,
the universal property of freeness, what a generating family is, and
whether "being a basis" is a property of a family, a chosen structure, or
an existence statement. The definition jumps to "a basis indexed by $I$ is
an isomorphism $e\colon R^{(I)}\xrightarrow{\sim}M$" without ever saying
what $R^{(I)}$ is. Scaffold from the general: define the free functor,
then the generating notions, then freeness, then basis.

Concrete standard: the free $R$-module functor
$F\colon\mathbf{Sets}\to\mathbf{LMod}_R$, $I\mapsto R^{(I)}:=
\bigoplus_{i\in I}R$, is defined by the universal property
$\operatorname{Hom}_R(F(I),M)\cong\operatorname{Hom}_{\mathbf{Sets}}(I,
U(M))$ where $U\colon\mathbf{LMod}_R\to\mathbf{Sets}$ is the underlying-
set functor. $R^{(I)}$ means the finite-support sum
$\bigoplus_{i\in I}R$, not the product $R^I:=\prod_{i\in I}R$; they are
not equal without a finiteness hypothesis on $I$, and a generating family
as a map $\bigoplus_{i\in I}R\to M$ requires $I$ to be a set with that
finite-support condition.

**Banned:** "A basis of an $R$-module $M$ indexed by $I$ is an
isomorphism $e\colon R^{(I)}\xrightarrow{\sim}M$" with no prior definition
of $R^{(I)}$ or of $F$.

**Preferred:** "Let $F\colon\mathbf{Sets}\to\mathbf{LMod}_R$,
$F(I):=\bigoplus_{i\in I}R$, be the free functor. For $M\in\mathbf{LMod}_R$
and a set $I$, a family $(m_i)_{i\in I}$ in $M$ is a basis if the induced
$F(I)\to M$ is an equivalence; equivalently the $R$-linear map is an
isomorphism."

### `DEF-24`: Property versus structure versus existence for a basis

"Being a basis" is used without stating whether it is a property of a
family ($ (m_i)_{i\in I}$ is a basis iff the induced map is an iso), a
chosen structure (a specific isomorphism $e\colon F(I)\xrightarrow{\sim}M$),
or an existence statement ($I$ is a basis of $M$ if there exists an
isomorphism $F(I)\xrightarrow{\sim}M$). The same English — "a basis indexed
by $I$ is an isomorphism $e$" — collapses the family $(e(1_i))_{i\in I}\subset
M$ with its classifying map $e$, and the quantifier ("there exists $e$" vs
"a chosen $e$") is not stated.

**Banned:** "A basis of an $R$-module $M$ indexed by $I$ is an
isomorphism $e\colon R^{(I)}\xrightarrow{\sim}M$, and a based module is a
pair $(M,e)$" — unclear whether "is" means property, chosen structure, or
existence, and conflates the elements $e(1_i)\in M$ with the map $e$.

**Preferred:** state which is meant. Property: "A family $(m_i)_{i\in I}$
in $M$ is a basis if the induced $F(I)\to M$ is an equivalence." Structure:
"A based $R$-module is a pair $(M,e)$ with $M\in\mathbf{LMod}_R$ and a
chosen equivalence $e\colon F(I)\xrightarrow{\sim}M$; write the underlying
family as $e_i:=e(1_i)$." Existence: "$I$ is a basis of $M$ if there
exists an equivalence $F(I)\xrightarrow{\sim}M$."

### `DEF-25`: A category defined pointwise by its objects

A structure that should be a category — based $R$-modules — is defined
only by its objects $(M,e)$, with no morphisms, no composition, no
identities, and no forgetful functors. The set $\operatorname{Bas}_I(M)$
of bases is introduced as an afterthought for fixed $I$. A category has
objects and morphisms; defining only the objects is pointwise, not
categorical, and the functoriality in $I$ is lost.

**Banned:** "A basis … is an isomorphism $e\colon R^{(I)}\xrightarrow{\sim}M$,
and a based module is a pair $(M,e)$. Write $\operatorname{Bas}_I(M)$ for
the set of such isomorphisms."

**Preferred:** define the category $\mathbf{BMod}_R$ of based $R$-modules:
objects are pairs $(M,e)$ with $M\in\mathbf{LMod}_R$ and
$e\colon F(I)\xrightarrow{\sim}M$ for some set $I$; a morphism
$(M,e)\to(N,e')$ over $\varphi\colon I\to J$ is an $R$-linear
$f\colon M\to N$ with $f\circ e = e'\circ F(\varphi)$, with
$F(\varphi)\colon F(I)\to F(J)$. The forgetful functors
$\mathbf{BMod}_R\to\mathbf{LMod}_R$, $(M,e)\mapsto M$, and
$\mathbf{BMod}_R\to\mathbf{Sets}$, $(M,e)\mapsto I$, are part of the
data. Then put $\operatorname{Bas}_I(M):=\operatorname{Iso}(F(I),M)$,
which is a torsor under $\operatorname{Aut}(F(I))$ when nonempty.

### `DEF-26`: Bold the term being defined

In a definition, the term being defined is bold at its first
introduction. This marks the definiendum for the reader and for
cross-referencing. The surrounding text states the quantifiers and
conditions; the bold names which word is being introduced.

**Banned:** "An $R$-module $M$ is torsion when …" — the term "torsion"
is not marked.

**Preferred:** "An $R$-module $M$ is **torsion** if
$\operatorname{Ann}_R(m)\neq0$ for every $m\in M$." Similarly, "A family
$(m_i)_{i\in I}$ in $M$ is a **basis** if …," "A **based module** is a
pair $(M,e)$ …," "A $t$-structure is **hereditary** if …" Bold the term;
do not bold surrounding prose.

### `PR-28`: "Requires a stated descent/local-to-global theorem with its hypotheses" is not a theorem

Meta-commentary that a conclusion requires a theorem with hypotheses
contributes no fenced unit to the skeleton (SEC-6) and says a theorem
must exist instead of stating it. The standard is to state the descent
theorem with its hypotheses once, then apply it — not to warn that one
is needed.

Vacuous generality is the other half: "a conclusion about $L$ from
either image" quantifies over no specified conclusion (isomorphism,
projectivity, rank, form, basis), no specified images (under which
functors $B\otimes_A^L-$), and no specified hypotheses (faithfully flat,
finite presentation, etc.). Each conclusion has different hypotheses; no
single sentence covers them. "Either image" is false as stated — one
image $L\otimes_{\mathbb Z}\mathbb Z_p$ alone never recovers $L$; descent
recovers $L$ from the collection plus gluing.

Concrete standards (state one, then apply it):

* **fpqc descent for $\mathbf{LMod}$** [@Stacks-023N, Tag 023N; Lurie
  DAG, descent for $\mathbf{LMod}_R$]: for faithfully flat
  $R\to S$, $\mathbf{LMod}_R \xrightarrow{\sim}
  \lim\bigl(\mathbf{LMod}_S \rightrightarrows \mathbf{LMod}_{S\otimes_R
  S} \substack{\to\\ \to\\ \to} \cdots\bigr)$ via
  $M\mapsto S\otimes_R^L M$ with descent datum. In particular,
  $M\simeq N$ in $\mathbf{LMod}_R$ iff $S\otimes_R^L M\simeq
  S\otimes_R^L N$ compatibly.

* **Beauville–Laszlo / Milnor patching for $\mathbb Z$**:
  for $M\in\mathbf{LMod}_{\mathbb Z}$ finitely presented,
  $M \simeq (M\otimes_{\mathbb Z}^L\mathbb Z_p)\times_{M\otimes_{\mathbb
  Z}^L\mathbb Q_p}(M\otimes_{\mathbb Z}^L\mathbb Q)$ as a pullback in
  $\mathbf{LMod}_{\mathbb Z}$; equivalently $M$ is recovered from the
  pair $(M\otimes\mathbb Z_p, M\otimes\mathbb Q)$ plus an identification
  over $\mathbb Q_p$. Hypotheses: finite presentation (or perfect) for
  the pullback to be exact; without it the square need not be cartesian.

* **Local-to-global for lattices:** $L\simeq L'$ as $\mathbb Z$-lattices
  iff $L\otimes\mathbb Z_p\simeq L'\otimes\mathbb Z_p$ for all $p$ and
  $L\otimes\mathbb Q\simeq L'\otimes\mathbb Q$ compatibly over
  $\mathbb Q_p$ — a conjunction, not "either image."

**Banned:** "A conclusion about $L$ from either image requires a stated
descent or local-to-global theorem with its hypotheses."

**Preferred:** "::: {#thm-descent} **Theorem (fpqc descent).** For
faithfully flat $R\to S$, $R\to S$ is of effective descent for
$\mathbf{LMod}$: $M\mapsto S\otimes_R^L M$ induces
$\mathbf{LMod}_R\simeq\lim \mathbf{LMod}_{S^{\otimes_R\bullet+1}}$. In
particular, for finitely presented $M,N$, $M\simeq N$ iff the base
changes are compatibly isomorphic. :::" Then: "::: {#cor-ZpQ} By
Beauville–Laszlo, for finitely presented $M$,
$M\simeq (M_p)\times_{M_{\mathbb Q_p}}(M_{\mathbb Q})$. Hence
$L\simeq L'$ iff … :::" State which conclusion, which images, which
theorem, which hypotheses; then apply it. Do not state that a theorem is
required.

### `PR-29`: Vague "either" / "a conclusion" with unquantified hypotheses

"A conclusion," "either image," "some theorem with its hypotheses" are
unbound: no domain, no codomain, no quantifier, no hypothesis list. This
is the general form of PR-28 and of PR-22 ("some … is …" for $\exists$):
using English indefinite for a mathematical quantifier so that no claim
is falsifiable. Each "a" hides a $\forall$ or $\exists$ and a condition.

**Banned:** "A conclusion about $L$ from either image requires a stated
descent or local-to-global theorem with its hypotheses"; "some
$R^n\twoheadrightarrow M$ is surjective" (PR-22); "the relevant
pullbacks" (DEF-31).

**Preferred:** quantify: "For every finitely presented $M$ and every
faithfully flat $R\to S$, $M\simeq0$ iff $S\otimes_R^L M\simeq0$";
"There exists a finite set $I$ and an effective epimorphism
$\bigoplus_{i\in I}R\twoheadrightarrow M$"; "For the pullback squares
exhibiting $X\times_Y 1$ in {#def-pullback}." Write $\forall$/$\exists$
and the hypothesis list; do not use "a"/"either"/"relevant"/"some"
standing for them.

### `PR-30`: Indefinite "a conclusion" with no proposition is unfalsifiable

"A conclusion about $L$" names no proposition: no quantified statement,
no domain, no codomain, no property (isomorphism, projectivity, rank,
form, freeness). Any counterexample can be deflected as "not the
intended conclusion," and any true fact can be claimed ex post as the
intended one. A mathematical sentence is falsifiable because it states
which proposition is claimed; an indefinite noun phrase is not.

This is the general form behind PR-28/PR-29 and PR-22 ("some
$R^n\twoheadrightarrow M$ is surjective") and DEF-31 ("the relevant
pullbacks"): an English indefinite standing for a quantifier so that no
checkable claim is made.

**Banned:** "A conclusion about $L$ from either image requires …";
"A result about $M$ follows from …"

**Preferred:** state the proposition with quantifiers: "For finitely
presented $M$, $M\simeq0$ iff $S\otimes_R^L M\simeq0$ for faithfully
flat $R\to S$"; "For $\mathbb Z$-lattices $L,L'$,
$L\simeq L'$ iff $L\otimes\mathbb Z_p\simeq L'\otimes\mathbb Z_p$ for
all $p$ and $L\otimes\mathbb Q\simeq L'\otimes\mathbb Q$ compatibly
over $\mathbb Q_p$." Name the conclusion; do not use "a conclusion" /
"a result."

### `PR-31`: Tautological "with its hypotheses" does no mathematical work

"With its hypotheses" is true of every stated theorem and adds no
hypothesis list, no condition, and no check. It occupies the grammatical
slot where the hypotheses belong while stating none, so the sentence
cannot be used: a reader cannot verify, apply, or falsify it. It is the
same device as "under the appropriate conditions" or "where defined"
standing for the actual conditions.

**Banned:** "requires a stated descent or local-to-global theorem with
its hypotheses"; "holds with its hypotheses / under its hypotheses."

**Preferred:** either list the hypotheses ("for faithfully flat $R\to S$
and finitely presented $M$") or state the theorem that carries them
({#thm-descent} above). Do not add a clause that is true of every
theorem and therefore says nothing. If no specific hypotheses are meant,
delete the clause.

### `PR-32`: Internal doctrine and preemptive correction posing as mathematical content

A sentence whose only coherent audience is an internal contributor or
agent — "requires a stated theorem," "must be justified," "with its
hypotheses" as a reminder to include them — is contributor governance,
not mathematics. Importing it into the book leaks runtime control into
the text. Its rhetoric is a preemptive scolding: it assumes a frame in
which the reader has made or is about to make a mistake and corrects
that mistake before it is committed, though the reader never made it or
thought about making it. It does not address the reader as an equal
pursuing the mathematics, but as a lesser to be controlled, steered, and
corrected.

Standard mathematical prose never does this. A textbook states the
theorem with hypotheses, proves it, and applies it; it does not tell the
reader that a theorem is required or that hypotheses are required. The
governance belongs in `CONTRIBUTING.md`, not in the book.

This generalizes PR-24 (self-referential meta-prose about the text's
structure) and PR-16–18 (strawman negation of a premise no one held):
here the premise is that the reader would draw a conclusion about $L$
from one image without a theorem, which no reader in this book's
audience was going to do.

**Banned:** "A conclusion about $L$ from either image requires a stated
descent or local-to-global theorem with its hypotheses" in a
mathematical section; any sentence that tells the reader that a theorem,
proof, or hypothesis is required instead of giving it.

**Preferred:** in the book, state the mathematics: "::: {#thm-descent}
**Theorem.** … :::" then "By {#thm-descent}, for finitely presented $L$,
… holds because $R\to S$ is faithfully flat." In `CONTRIBUTING.md`,
state the governance once: "Every local-to-global conclusion is a
fenced Theorem with quantified hypotheses; do not draw it from one image
alone."

### `PR-33`: "Are distinct constructions" is true by definition — the claim is about the comparison map

$M\mapsto M\otimes_{\mathbb Z}^L\mathbb Z_p$ and
$M\mapsto \widehat M_p:=\lim_n M\otimes_{\mathbb Z}^L\mathbb Z/p^n$ are
different functors, defined differently. Saying they "are distinct
constructions" without or with a hypothesis states a tautology that
holds regardless. The substantive mathematics is whether the canonical
comparison map is an equivalence.

Concrete standards:

* **Scalar extension:** $-\otimes_{\mathbb Z}^L\mathbb Z_p\colon
  \mathbf{LMod}_{\mathbb Z}\to\mathbf{LMod}_{\mathbb Z_p}$ (underived
  $-\otimes_{\mathbb Z}\mathbb Z_p$ on discrete modules). Left adjoint
  to restriction.

* **$p$-adic completion:** $\widehat{(-)}_p:=\lim_n (-\otimes_{\mathbb
  Z}^L\mathbb Z/p^n)$ in $\mathbf{LMod}_{\mathbb Z}$, resp.
  $\lim_n M/p^nM$ for discrete $M$.

* **Comparison map:** the natural $c_M\colon M\otimes_{\mathbb Z}^L
  \mathbb Z_p \to \widehat M_p$ induced by
  $\mathbb Z_p\simeq\lim_n\mathbb Z/p^n$ and
  $M\otimes^L\lim_n\mathbb Z/p^n\to\lim_n(M\otimes^L\mathbb Z/p^n)$.

Do not state that the functors are distinct. State what $c_M$ does.

**Banned:** "Without the finite-generation hypothesis, scalar extension
and completion are distinct constructions."

**Preferred:** "::: {#thm-complete-vs-basechange} **Theorem.** For
$M\in\mathbf{LMod}_{\mathbb Z}$ perfect (in particular, for discrete
finitely generated $M$ over Noetherian $\mathbb Z$), $c_M\colon
M\otimes_{\mathbb Z}^L\mathbb Z_p \xrightarrow{\sim}\widehat M_p$ is an
equivalence; in particular $M\otimes_{\mathbb Z}\mathbb Z_p\simeq\widehat
M_p$ for discrete finitely generated $M$. :::" Then apply or refute:
"$c_M$ is not an equivalence in general: for
$M=\bigoplus_{\mathbb N}\mathbb Z$,
$M\otimes\mathbb Z_p=\bigoplus_{\mathbb N}\mathbb Z_p$ (finite support)
while $\widehat M_p$ strictly contains it; for $M=\mathbb Q$,
$\mathbb Q\otimes_{\mathbb Z}\mathbb Z_p\simeq\mathbb Q_p$ while
$\widehat{\mathbb Q}_p\simeq0$ [@Stacks-0A05, Tag 0A05; Lurie DAG, formal
completion]." Name the functors, the map, and the quantified
equivalence; do not say the definitions are distinct.

### `PR-34`: "Without the $H$ hypothesis" is true of every theorem with hypothesis $H$

"Without the finite-generation hypothesis, $A$ and $B$ are distinct / do
not coincide / fail" is true of any theorem "$H\Rightarrow A\simeq B$"
and therefore says nothing: it restates that the theorem has a
hypothesis (PR-31) while naming neither the theorem, the quantified $H$
(finitely generated vs. finitely presented vs. perfect vs. coherent),
nor the quantified claim $A\simeq B$ (which $A$, which $B$, which map),
so it is unfalsifiable (PR-30) and can be deflected to any intended
meaning.

This is the general form behind PR-28/PR-31: a sentence that is true
by definition of "distinct constructions" or true by logic of
"theorems have hypotheses," and hence vacuous.

**Banned:** "Without the finite-generation hypothesis, scalar extension
and completion are distinct constructions"; "Without $H$, $A$ and $B$
are different."

**Preferred:** state the quantified theorem with $H$ and the comparison
map (PR-33), then state the quantified failure without $H$ with a
counterexample: "Without finite generation $c_M$ need not be an
equivalence; e.g. $M=\bigoplus_{\mathbb N}\mathbb Z$ as above." Do not
use "without $H$, $A$ and $B$ are distinct" standing for a theorem plus
a counterexample.

### `DEF-34`: "Finite-generation hypothesis" with no quantified finiteness notion

"Finite-generation hypothesis" names no notion: finitely generated vs.
finitely presented vs. perfect (compact in $\mathbf{LMod}_{\mathbb Z}$)
vs. coherent are distinct, and over a general $\mathbb E_1$-ring
spectrum $R$ the correct condition is perfectness, not discrete finite
generation. The book's default is $\mathbf{LMod}_R$ stable; discrete
finite generation is a property of $\pi_0M$ after truncating.

**Banned:** "the finite-generation hypothesis" unqualified.

**Preferred:** quantify: "for $M$ perfect in $\mathbf{LMod}_{\mathbb Z}$
(in particular, for discrete $M$ finitely generated over Noetherian
$\mathbb Z$)" or "for $M$ finitely presented" — name which finiteness,
in which category, and whether derived or discrete, at each use.

### `PR-35`: Stating the complement of a positive coincidence theorem is obviated

Once $A$ and $B$ are presented as distinct constructions — here
$-\otimes_{\mathbb Z}^L\mathbb Z_p$ and $\widehat{(-)}_p$ with different
definitions — their distinctness as definitions is already established;
no sentence is needed to say they are distinct. Stating the positive
quantified theorem with the comparison map (PR-33) — "$c_M\colon
M\otimes^L\mathbb Z_p\to\widehat M_p$ is an equivalence for $M$ perfect
(in particular discrete finitely generated over Noetherian $\mathbb Z$)"
— already makes the complement implicit and obvious to any reader: without
$H$, the theorem does not apply and $c_M$ need not be an equivalence.
Adding "Without $H$, $A$ and $B$ are distinct" is structurally redundant:
it repeats what presentation already shows and what the quantified
theorem already delimits.

This is the general scaffolding principle behind SEC-8 and PR-33/PR-34:
present distinct objects as distinct, state when the canonical comparison
is an equivalence with quantified $H$ and the map, and stop — the
failure outside $H$ is then understood without being stated, and a
counterexample is given only when it teaches (e.g. $M=\bigoplus_{\mathbb
N}\mathbb Z$, $M=\mathbb Q$ in PR-33), not as a separate tautological
sentence.

**Banned:** "Without the finite-generation hypothesis, scalar extension
and completion are distinct constructions" alongside the definitions and
"For finitely generated $M$, $M\otimes\mathbb Z_p\simeq\widehat M_p$."

**Preferred:** present the two functors with different definitions (hence
distinct), then state one quantified theorem with the map:
"::: {#thm-complete-vs-basechange} **Theorem.** … $c_M$ is an
equivalence for $M$ perfect … :::" No additional sentence is needed to
say they differ without $H$; the quantified theorem already obviates it.
Give a counterexample only as an illustration of the boundary, not as a
restatement that the definitions are distinct.

### `PR-36`: Negative framing bloats the text, ruins the tone, and undermines standard exposition structure

The general device behind PR-2, PR-16–18, PR-24, PR-28, PR-30–35, and
SEC-8: instead of the positive quantified statement the mathematics
requires, the text adds a negative sentence — "$a=b$ is a theorem,
never a definitional identity," "does not follow merely from notation,"
"is additional data," "their mere existence supplies no order relation,"
"requires a stated descent theorem with its hypotheses," "without $H$,
$A$ and $B$ are distinct constructions," "a conclusion about $L$ from
either image requires …" Each is a negation, a "without," or a
"requires" standing for a positive Definition or Theorem not stated.

Three costs, all general:

**1. Bloat.** A positive theorem $H\Rightarrow (c_M\text{ is an
equivalence via the named map})$ has infinitely many true negatives you
could state — without $H$ it need not hold, without $H_1$ it fails,
without notation it is not defined, existence alone supplies no relation,
etc. Stating any of them doubles the text while adding no fenced unit to
the skeleton (SEC-6). Standard exposition states the quantified positive
once and stops; the complements are implicit and obvious to any reader
who has read the definitions as distinct and the theorem as quantified.

**2. Tone.** Each negative assumes a reader who was about to make a
mistake — conflate $A$ and $B$, think notation supplies structure, draw
a conclusion from one image, think existence supplies order — and
corrects that mistake before it is made, though the reader never made it
or thought about making it. It does not address the reader as an equal
pursuing the mathematics, but as a lesser to be controlled, steered, and
corrected (PR-32). Standard prose never scolds preemptively; it states
the mathematics and lets the reader use it.

**3. Structure.** A negative sentence is not a Definition, Theorem, or
Example with a named map, quantified $H$ (perfect / finitely presented /
finitely generated, faithfully flat, etc.), and a checkable claim. It is
unfalsifiable (PR-30) — "a conclusion" names no proposition, "either
image" names no functor, "with its hypotheses" names no list — and often
true by definition ("are distinct constructions," PR-33) or true by logic
of "theorems have hypotheses" (PR-34, PR-31) and therefore contributes no
proof obligation while hiding that the actual obligation (name the map,
quantify $H$, state iso vs. not, give the boundary counterexample only
when it teaches) was not met. It is doctrine posing as content, leaking
contributor governance into the book.

Concrete standard: standard mathematical exposition is positive and
constructive — definitions as data/tuples
$(\mathcal{C},\otimes,\mathbf{1},\alpha,\lambda,\varrho)$ with
diagrams (SYM-1), theorems as quantified implications with the comparison
map, proofs, then boundary examples/counterexamples at the quantified
edge when they teach. Stacks Project, EGA, Serre, Hartshorne, Lurie
HTT/HA, EKMM never write "without $H$, $A$ and $B$ are distinct" or
"this requires a theorem with hypotheses"; they write
"::: {#thm-descent} **Theorem (fpqc descent).** For faithfully flat
$R\to S$, … :::" and "::: {#thm-complete-vs-basechange} **Theorem.**
$c_M$ is an equivalence for $M$ perfect … :::" and apply them.

**Banned:** "Without the finite-generation hypothesis, scalar extension
and completion are distinct constructions"; "A conclusion about $L$ from
either image requires a stated descent or local-to-global theorem with
its hypotheses"; "$a=b$ is a theorem, never a definitional identity";
"does not follow merely from notation"; "is additional data"; "their mere
existence supplies no order relation."

**Preferred:** delete every negative standing for a positive not stated,
and state the positive once, quantified, with the named map: present
$-\otimes^L_{\mathbb Z}\mathbb Z_p$ and $\widehat{(-)}_p$ with different
definitions (hence distinct), then one fenced theorem with $c_M$ and
quantified $H$ (PR-33), then apply it. No sentence is needed to say what
does not follow, what is not supplied, what is distinct without $H$, or
what is required. The positive theorem already says it, without bloat,
without condescension, and with a checkable claim.

### `PR-37`: Sign-posting "Fix $R$ and $W$, the value module of the forms below" is not a mathematical unit

A setup sentence that fixes variables for upcoming material — "Fix a
commutative ring $R$ and an $R$-module $W$, the $*$-module of the $*$s
below" — is an imperative to the reader to hold variables across a
section, not a Definition/Theorem/Example with a checkable claim. Delete
all glue and the skeleton must remain complete (SEC-6); here every form
below would then lose its $R,W$ quantifier, so the skeleton is
incomplete without glue. "Of the forms below" is a forward reference to
no specified label, names $W$ by a future description, and fixes a single
$W$ where the mathematics requires a *parameter* quantifying over
$\mathbf{LMod}_R$.

This is the general form behind SEC-8/PR-33: prose that holds variables
outside any fenced unit instead of quantifying them inside the unit that
uses them. It creates ambiguous scope — is $W$ fixed for the section,
the chapter, or one definition? — and forces later text to rely on
ambient context.

Concrete standards:

* **$W$-valued bilinear form:** for $R$ an $\mathbb E_\infty$-ring
  spectrum and $W,M\in\mathbf{LMod}_R$,
  a $W$-valued bilinear form on $M$ is a morphism
  $b\colon M\otimes_R M\to W$ in $\mathbf{LMod}_R$ (equivalently,
  $M\otimes_R^L M\to W$). For $R$ discrete and $M,W$ discrete, this is
  an $R$-bilinear $M\times M\to W$. The datum is the map $b$; $W$ is its
  codomain, varying with $b$, not a once-fixed module. Similarly a
  quadratic or symmetric form is a map from the appropriate
  classifying object for that flavour, valued in varying $W$.

* **Quantification belongs inside the unit.** Standard texts never write
  a free-floating "Fix $R$ and $W$ for below." They quantify inside
  each fenced unit or make the section header the formal quantifier.

**Banned:** "Fix a commutative ring $R$ and an $R$-module $W$, the value
module of the forms below" as a standalone setup sentence; "Fix $R$ for
the forms below; let $W$ be the value module."

**Preferred:** quantify inside the fenced unit, with varying $W$:

"::: {#def-bilinear} **Definition.** Let $R$ be a commutative ring (resp.
$\mathbb E_\infty$-ring spectrum) and let $W,M\in\mathbf{LMod}_R$. A
**$W$-valued bilinear form** on $M$ is a morphism
$b\colon M\otimes_R M\to W$ in $\mathbf{LMod}_R$. :::"

Or, when a section works over one $R$, make the header the quantifier
once and keep $W$ varying:

"::: {.Remark} Throughout §2, $R$ denotes a fixed commutative ring;
$W$ varies over $\mathbf{LMod}_R$ and all forms are $W$-valued as in
{#def-bilinear}. :::"

Do not fix a single $W$ for "the forms below"; let $W$ be a parameter
of the form. Do not forward-reference "below"; label the definitions
and refer to them.

### `TERM-9`: "Value module" with no definition, fixing a single $W$

"Value module" is not a standard term with a defined referent and, as
used in "the value module of the forms below," asserts a single $W$
fixed for a section where the mathematics requires $W$ varying over
$\mathbf{LMod}_R$ (PR-37). Forms are $W$-valued for varying $W$; the
codomain is part of the datum $b\colon M\otimes_R M\to W$, not a global
choice.

**Banned:** "the value module $W$ of the forms below"; "fix the value
module $W$."

**Preferred:** "let $W\in\mathbf{LMod}_R$ and let $b\colon M\otimes_R
M\to W$ be a $W$-valued bilinear form" (PR-37); or "a bilinear form
valued in $W$" with $W$ quantified in the definition. Do not reify "the
value module" as a once-fixed object.

### `PR-38`: "With pointwise operations" / "with its $R$-module structure via $W$" does zero work — $\mathbf{Mod}_R$ is enriched over itself

The $R$-module structure on a Hom is not an extra datum imposed pointwise
via the codomain $W$ that needs to be announced. For commutative $R$,
$\mathbf{Mod}_R$ is closed symmetric monoidal, hence enriched over
itself; $\operatorname{Hom}_R(M,N)\in\mathbf{Mod}_R$ is the internal hom,
full stop (stably $\mathbf{LMod}_R$ is closed symmetric monoidal for
$\mathbb E_\infty$ $R$; for general $\mathbb E_1$ $R$,
$\mathbf{LMod}_R$ is enriched over $\mathbf{Sp}$ and tensored over it).
Its underlying set is the set of $R$-linear maps and its $R$-action is
the canonical one — no "via $W$" and no alternative to contrast
"pointwise" with. "With pointwise operations" therefore occupies the slot
where a non-trivial structure would be specified while specifying no
choice, and mislocates the structure in the codomain.

This is the general form of PR-31 (tautological "with its hypotheses"):
a clause that restates what the ambient closed structure already gives,
so deleting it leaves the mathematics unchanged.

Concrete standard — state the closed structure once as scaffolding, then
there is nothing to say at the point of use:

* **Scaffolding (once, fenced, in the module-theory setup):**
  "::: {#thm-mod-closed} **Theorem.** For commutative $R$,
  $\mathbf{Mod}_R$ (resp. stably $\mathbf{LMod}_R$ for
  $\mathbb E_\infty$ $R$) is closed symmetric monoidal and self-enriched.
  In particular $\operatorname{Hom}_R(M,N)\in\mathbf{Mod}_R$ is the
  internal hom. :::" [@Stacks-0B8A; Lurie HA 4.2.1]

* **At the point of use:** no clause needed:
  "::: {#def-bil} **Definition.** Let $R$ be commutative and
  $W,M\in\mathbf{Mod}_R$. Put
  $\operatorname{Bil}_{R,W}(M):=\operatorname{Hom}_R(M\otimes_R M,W)$ as
  $R$-module. Its elements are the $R$-bilinear $M\times M\to W$. :::"
  The "as $R$-module" already is the self-enrichment; no "with
  pointwise operations" and no "structure via $W$."

The missing one-time scaffolding is what forced the filler: without
{#thm-mod-closed}, every Hom later needs a tautological qualifier to
compensate. Put the enrichment once where it belongs and every later
"with pointwise operations" / "with its $R$-module structure" is
obviated.

**Banned:** "Let $\operatorname{Bil}_{R,W}(M)$ be the $R$-module of
$R$-bilinear maps $M\times M\to W$, with pointwise operations";
"with its $R$-module structure via $W$ / induced by $W$."

**Preferred:** state {#thm-mod-closed} once in the module-theory setup;
then "Let $\operatorname{Bil}_{R,W}(M):=\operatorname{Hom}_R(M\otimes_R
M,W)$ be the $R$-module of $R$-bilinear maps $M\times M\to W$." No
trailing clause. If the reader needs the formula,
"$(b_1+b_2)(x,y)=b_1(x,y)+b_2(x,y)$" is a property of the internal hom,
not part of the definition.

### `PR-39`: Prose "the $R$-module of $R$-bilinear maps $M\times M\to W$" for $\operatorname{Hom}_R(M\otimes_R M,W)$

One symbol already is the $R$-module with its structure; the prose
paraphrase re-spells it in English and then needs a filler clause to
rebuild the structure (PR-38).

**Banned:** "Let $\operatorname{Bil}_{R,W}(M)$ be the $R$-module of
$R$-bilinear maps $M\times M\to W$, with pointwise operations."

**Preferred:** "Put $\operatorname{Bil}_{R,W}(M):=
\operatorname{Hom}_R(M\otimes_R M,W)$ as $R$-module" — or, if a name is
unneeded, just $\operatorname{Hom}_R(M\otimes_R M,W)$. Domain
($M\otimes_RM$), codomain ($W$), linearity, and $R$-module structure via
the self-enrichment ({#thm-mod-closed}) are already in the symbol; no
"$R$-bilinear," no "$M\times M\to W$," no "with pointwise operations"
to add. Stably
$\operatorname{Bil}_{R,W}(M):=\mathbf{RHom}_R(M\otimes^L_RM,W)$. This is
the standard: Stacks, Bourbaki, Lurie HA define $W$-valued bilinears as
the hom object from the tensor square and stop (PR-27 is the general
form: concise notation obviates prose).

### `PR-40`: Discussing "$R$-bilinear maps $M\times M\to W$" instead of standing on the tensor product

$R$-bilinear $M\times M\to W$ is not a primitive notion to re-describe
on each use; it is classified by the tensor product, defined once with
its universal property. Re-describing bilinears in prose on every
occurrence — checking "$R$-bilinear," listing "$M\times M\to W$," adding
"with pointwise operations" to make the set an $R$-module — chooses not
to stand on that one-time scaffolding and replicates it each time.

Concrete standards — state the scaffolding once, then use homs from the
tensor to encode bilinearity from then on:

* **Scaffolding (once, fenced, before any form):**
  "::: {#def-tensor} **Definition/Theorem.** For $M,N\in\mathbf{Mod}_R$
  there is $M\otimes_R N\in\mathbf{Mod}_R$ with a universal $R$-bilinear
  $M\times N\to M\otimes_R N$, i.e.
  $\operatorname{Hom}_R(M\otimes_R N,W)\cong R\text{-Bil}(M\times N,W)$
  naturally in $W\in\mathbf{Mod}_R$. :::"
  [@Stacks-0B8A; Lurie HA 4.2.1]

* **From then on, no "bilinear maps" prose:** a $W$-valued bilinear
  form on $M$ is a morphism $b\colon M\otimes_R M\to W$; its $R$-module
  of all such is $\operatorname{Hom}_R(M\otimes_R M,W)$ as $R$-module.
  Bilinearity, domain, codomain, and $R$-module structure are already in
  the Hom from the tensor; nothing to spell out, no clause to add.

Stably the same: $M\otimes^L_RM$ classifies derived bilinears,
$\mathbf{RHom}_R(M\otimes^L_RM,W)$ is the $R$-module of them.

**Banned:** "the $R$-module of $R$-bilinear maps $M\times M\to W$" as a
recurring definition; "$R$-bilinear maps $M\times M\to W$ with pointwise
operations" (PR-38) on each use.

**Preferred:** define $M\otimes_R M$ once via {#def-tensor}; then
"a $W$-valued bilinear form on $M$ is $b\colon M\otimes_R M\to W$"
and "$\operatorname{Bil}_{R,W}(M):=\operatorname{Hom}_R(M\otimes_R M,W)$."
Never re-describe bilinearity in prose once the tensor classifies it.

### `TERM-10`: "Presheaf" overloaded for $\mathbf{Mod}_R^{\mathrm{op}}\to\mathbf{Mod}_R$ / "$R$-module of maps" functor

A presheaf on $\mathcal C$ is a functor $\mathcal C^{\mathrm{op}}\to
\mathbf{Set}$ (stably $\mathcal C^{\mathrm{op}}\to\mathcal S$). An
$R$-module-valued functor $\mathcal C^{\mathrm{op}}\to\mathbf{Mod}_R$
is an $\mathbf{Mod}_R$-valued presheaf, or an $\mathbf{Mod}_R$-enriched
presheaf when the enrichment from {#thm-mod-closed} is meant — not a
"presheaf" unqualified. Overloading the generic name hides which
enrichment and which $\operatorname{Bil}$ is named (the $R$-module
$\operatorname{Bil}_{R,W}(M)$ vs. the functor
$M\mapsto\operatorname{Bil}_{R,W}(M)$) and adds no content beyond
"functor," since
$\operatorname{Bil}_{R,W}(M)=\operatorname{Hom}_R(M\otimes_R M,W)$ is
already functorial in $M$ by the Hom — $f\mapsto (f\otimes f)^*$.

Concrete standards:

* **Presheaf:** $\operatorname{PSh}(\mathcal C):=
  \operatorname{Fun}(\mathcal C^{\mathrm{op}},\mathbf{Set})$, stably
  $\operatorname{Fun}(\mathcal C^{\mathrm{op}},\mathcal S)$ [@Stacks-00VG;
  Lurie HTT 0.6.5].

* **$R$-module-valued:** a functor $\mathbf{Mod}_R^{\mathrm{op}}\to
  \mathbf{Mod}_R$ is an $\mathbf{Mod}_R$-valued presheaf on
  $\mathbf{Mod}_R$, equivalently an $\mathbf{Mod}_R$-enriched presheaf via
  the self-enrichment {#thm-mod-closed}. Name the enrichment when it
  matters.

* **At the point of use:** no "defines a presheaf" to name functoriality
  that is already the Hom's.

**Banned:** "Pullback along $f\colon M\to N$ sends $b$ to
$f^*b(x,y)=b(fx,fy)$, and defines a presheaf
$\operatorname{Bil}_{R,W}\colon(R\text{-}\mathbf{Mod})^{\mathrm{op}}\to
R\text{-}\mathbf{Mod}$."

**Preferred:** "$\operatorname{Bil}_{R,W}(M):=
\operatorname{Hom}_R(M\otimes_R M,W)$ as $R$-module, functorial in $M$
by $(f\colon M\to N)\mapsto (f\otimes f)^*\colon
\operatorname{Hom}_R(N\otimes_R N,W)\to\operatorname{Hom}_R(M\otimes_R
M,W)$, $f^*b(x,y)=b(fx,fy)$ as the element formula for $(f\otimes f)^*b$."
If the word is needed, "as an $\mathbf{Mod}_R$-valued presheaf on
$\mathbf{Mod}_R$ (resp. $\mathbf{Mod}_R$-enriched presheaf via
{#thm-mod-closed})"; otherwise just "as a functor
$\mathbf{Mod}_R^{\mathrm{op}}\to\mathbf{Mod}_R$."

### `TERM-11`: Bare "maps $M\to W$" with no category — egregiously imprecise, and wrong for quadratics

"Map $M\to W$" unqualified in $\mathbf{Mod}_R$ means morphism in
$\mathbf{Mod}_R$ — i.e. $R$-linear. A quadratic $q\colon M\to W$ is
*not* $R$-linear (and not a morphism in $\mathbf{Mod}_R$); it is a
function on underlying sets for the forgetful
$U\colon\mathbf{Mod}_R\to\mathbf{Set}$ satisfying $q(rx)=r^2q(x)$ and
$R$-bilinearity of the polarization
$b_q(x,y):=q(x+y)-q(x)-q(y)$. "Maps $M\to W$" without "of sets" / "of
underlying sets" / "in $\mathbf{Set}$ after $U$" therefore names the
wrong hom, hides which forgetful is meant (Set vs. $\mathcal S$ vs.
anima stably matters), and leaves no object to enrich — the later "as
$R$-module, under pointwise operations" then has no category to attach
to.

This is the general form behind PR-37/PR-38: a set-level datum
described as if it were a morphism in the ambient $R$-linear category,
mislocating structure and forcing filler.

Concrete standards — name the category, and use the classifier so no
"maps $M\to W$" is needed:

* **Underlying sets:** let $U\colon\mathbf{Mod}_R\to\mathbf{Set}$ be the
  forgetful. A quadratic function is a map $U(M)\to U(W)$ in
  $\mathbf{Set}$ with those two conditions. Stably $U\colon\mathbf{LMod}_R
  \to\mathcal S$.

* **Classifier (so no "maps $M\to W$" to describe):** fix the divided
  power (Whitehead) classifier $\Gamma^2_R$ once, fenced, with its
  universal property. Then
  $\operatorname{Quad}_{R,W}(M):=\operatorname{Hom}_R(\Gamma^2_R(M),W)$
  as $R$-module (stably
  $\mathbf{RHom}_R(\mathbf{\Gamma}^2_R(M),W)$). Its underlying set is the
  set of functions $U(M)\to U(W)$ satisfying the quadratic condition;
  its $R$-module structure is the self-enrichment {#thm-mod-closed} on
  that Hom, not "pointwise via $W$" on a set of maps whose category was
  never named. Similarly $\operatorname{Sym}_{R,W}(M):=
  \operatorname{Hom}_R(\operatorname{Sym}^2_R(M),W)$ for symmetric,
  $\operatorname{Bil}_{R,W}(M)=\operatorname{Hom}_R(M\otimes_R M,W)$ as
  above — each Hom classifies the flavour, no element-level "maps
  $M\times M\to W$ / $M\to W$" to re-spell.

**Banned:** "of maps $q\colon M\to W$ for which $q(rx)=r^2q(x)$ and …"
with no "of sets / of underlying sets / in $\mathbf{Set}$ after $U$";
"Let $\operatorname{Quad}_{R,W}(M)$ be the $R$-module, under pointwise
operations, of maps $M\to W$ …"

**Preferred:** "Let $U\colon\mathbf{Mod}_R\to\mathbf{Set}$ be the
forgetful. A **quadratic form** on $M$ valued in $W$ is a function
$q\colon U(M)\to U(W)$ with $q(rx)=r^2q(x)$ and $b_q(x,y)$ $R$-bilinear"
— or, classifier-first and with no "maps $M\to W$": "Put
$\operatorname{Quad}_{R,W}(M):=\operatorname{Hom}_R(\Gamma^2_R(M),W)$ as
$R$-module. Its elements are the functions $U(M)\to U(W)$ with that
condition." Name $\mathbf{Set}$ / $U$ when the map is not $R$-linear;
for bilinear/symmetric/quadratic never write bare "maps $M\to W$" or
"$M\times M\to W$" once the classifier ($\otimes$, $\operatorname{Sym}^2$,
$\Gamma^2$) is defined.

### `PR-43`: Element-wise $b(x,y)=b(y,x)$, $b(x,x)=0$, $q(rx)=r^2q(x)$ for $b\circ\tau=b$, $b\circ\Delta=0$ — concrete shadow for the categorical diagram

Listing symmetric / skew / alternating / even as equalities on elements
$x,y\in M$ ties the notion to $\mathbf{Set}$-concrete $M$ with an
underlying set $U(M)$ and makes it inextensible to non-concrete
$\mathcal C$ — $\mathcal O_X\text{-}\mathbf{Mod}$, local systems,
$\mathbf{Sp}$, $\mathbf{Grpd}$, $\infty$-categories,
$\mathbf{Sch}_{/S}$, etc., where $x,y\colon 1\to M$ may not exist as set
elements. The element formulas are the *evaluation* of one diagram on
generalized elements, not the definition, and they elide the single
non-lax symmetric monoidal structure $(\otimes,1,\tau)$ that makes the
notion portable.

This is the general form of PR-39/PR-40 and TERM-11: re-describing in
prose on elements what the tensor classifier and the symmetry already
encode as a morphism.

Concrete standards — state the diagrammatic notion once via the
symmetric monoidal structure (non-lax: $\tau\colon M\otimes M\to
M\otimes M$ is an isomorphism with $\tau^2=\mathrm{id}$, not a lax
comparison), then derive the element formula as its unwrapping when
$U$ exists:

* **Scaffolding (once, fenced):** $(\mathbf{Mod}_R,\otimes_R,R,\tau)$
  (stably $(\mathbf{LMod}_R,\otimes^L_R,R,\tau)$) symmetric monoidal
  closed and self-enriched {#thm-mod-closed}, with $M\otimes_R M$
  classifying bilinears {#def-tensor}. Let $\tau_{M,M}\colon M\otimes
  M\to M\otimes M$ be the symmetry, $\Delta\colon M\to M\otimes M$ the
  diagonal for alternating, and $\Gamma^2_R(M)\xrightarrow{\gamma}
  \operatorname{Sym}^2_R(M)\to M\otimes M$ the divided-power classifier
  for even/quadratic.

* **$W$-valued bilinear $b\colon M\otimes_R M\to W$ is:**
  — **symmetric** if $b\circ\tau = b\colon M\otimes M\to W$;
  — **skew-symmetric** if $b\circ\tau = -b$;
  — **alternating** if $b\circ\Delta =0$ (equivalently $b\circ\tau=-b$
  and $b\circ\Delta=0$; in $2$ invertible alternating $=$ skew);
  — **even** if $b$ factors through $\operatorname{Sym}^2_R(M)$ and
  $b(x,x)\in2W$ is the element shadow of the factorization through
  $\Gamma^2_R(M)$ — never as primary.

  Stably the same with $\tau$ the symmetric monoidal braiding in
  $\mathbf{LMod}_R$.

* **Element unwrapping (only after, when $U$ exists):** for $x,y\colon
  R\to M$ in $\mathbf{Mod}_R$ (i.e. $x,y\in U(M)$), $b\circ\tau=b$
  evaluates to $b(x,y)=b(y,x)$, etc. This is a property of the diagram,
  not the definition.

**Banned:** "For $b\colon M\times M\to W$: $b$ is *symmetric* if
$b(x,y)=b(y,x)$; $b$ is *skew* if $b(x,y)=-b(y,x)$; $b$ is *alternating*
if $b(x,x)=0$; $b$ is *even* if $b(x,x)\in2W$" as definitions.

**Preferred:** "Let $b\colon M\otimes_R M\to W$ be $W$-valued bilinear.
$b$ is **symmetric** if $b\circ\tau=b$, **skew** if $b\circ\tau=-b$,
**alternating** if $b\circ\Delta=0$, **even** if $b$ lifts through
$\Gamma^2_R(M)$." Then, if pedagogically useful: "On elements this is
$b(x,y)=b(y,x)$, $b(x,x)=0$, etc., as the evaluation of those equalities
on $x\otimes y\colon R\to M\otimes M$."

### `PR-44`: "$b$ is *even* if $b(x,x)\in2W$" breaks the value-module abstraction just built

$W$ was introduced as a *parameter* varying over $\mathbf{Mod}_R$ (stably
$\mathbf{LMod}_R$) via $\operatorname{Hom}_R(M\otimes_RM,W)$ as
$R$-module ({#thm-mod-closed}, {#def-tensor}) — no elements, no
"$\in$." "$b(x,x)\in2W$" immediately concretizes that $W$ to
$U(W)$ with a subset $2W:=\operatorname{im}(2\colon W\to W)$, i.e. the
$\mathbf{Set}$-shadow of a diagram, meaningless stably (for
$\mathbf{LMod}_R$, $\mathbf{Sp}$, $\mathcal O_X\text{-}\mathbf{Mod}$
there is no "$\in$") and tied to $R=\mathbb Z$ with $2\in\mathbb Z$ acting
via $\mathbb Z\to R$. It re-describes as an element condition what the
classifier already encodes as a factorization.

This is the general form of PR-43 and PR-37/TERM-9: prose on elements
that collapses the abstraction just built for $W$-valued forms.

Concrete standard — evenness is a lift of the morphism
$b\colon M\otimes M\to W$, not a pointwise divisibility:

* **Classifiers (once, fenced):**
  $\Gamma^2_R(M)\xrightarrow{\gamma}\operatorname{Sym}^2_R(M)
  \twoheadrightarrow M\otimes_R M$ with $\tau$ on $M\otimes M$ as in
  PR-43; stably $\mathbf{\Gamma}^2_R(M)\to\mathbf{Sym}^2_R(M)$. Then
  $\operatorname{Quad}_{R,W}(M):=\operatorname{Hom}_R(\Gamma^2_R(M),W)$,
  $\operatorname{Sym}_{R,W}(M):=\operatorname{Hom}_R(\operatorname{Sym}^2_R(M),W)$,
  $\operatorname{Bil}_{R,W}(M):=\operatorname{Hom}_R(M\otimes_RM,W)$.

* **$W$-valued symmetric $b\colon M\otimes_RM\to W$ is even** if $b$
  factors through $\operatorname{Sym}^2_R(M)$ and lifts through
  $\Gamma^2_R(M)$ — equivalently $b$ is in the image of
  $\operatorname{Hom}_R(\operatorname{Sym}^2_R(M),W)$ and of
  $\operatorname{Hom}_R(\Gamma^2_R(M),W)$ via $\gamma^*$. No
  $b(x,x)\in2W$ to state; its evaluation on $x\colon R\to M$ when
  $U$ exists is $b(x,x)=2\cdot\tilde b(x)$ for some
  $\tilde b\in\operatorname{Hom}_R(\Gamma^2_R(M),W)$, whose shadow is
  "$\in2W$" only for discrete $W$ with $U$.

**Banned:** "$b$ is *even* if $b(x,x)\in2W$ for every $x$" as
definition while $W$ is the varying value module of
$\operatorname{Hom}_R(M\otimes_RM,W)$.

**Preferred:** "$b\colon M\otimes_RM\to W$ symmetric is **even** if it
lifts through $\Gamma^2_R(M)$ (i.e. $b$ is in the image of
$\operatorname{Hom}_R(\Gamma^2_R(M),W)\xrightarrow{\gamma^*}
\operatorname{Hom}_R(M\otimes M,W)$)." Then, only after and only for
discrete $W$ with $U$: "On elements this is $b(x,x)\in2W$."

### `PR-45`: Carrying $b(x,x)\in2W$ on every use instead of naming the governing $R$-submodule $\operatorname{Val}(b)\subseteq W$ — local thinking for a global object

The element condition is the unpacked shadow of one global $R$-submodule
of $W$. Carrying the shadow on every occurrence — "for every $x$,
$b(x,x)\in2W$," "check $b(x,x)\in2W$," etc. — never names the object that
governs the condition, so every argument must drop to $U(M)$ and re-check
at a point $x$. That re-expansion is where hand-waving enters: is $x$ in
$M$, in $U(M)$, in $M\otimes_R\kappa(p)$? Is $2W$ the image
$2\colon W\to W$ or the subset? Does it vary functorially in $W$? With
no $\operatorname{Val}(b)$ as an $R$-submodule there is nothing to make
precise, and the quantifier "for every $x$" can slide, exactly as "a
conclusion from either image" slid.

Naming the object once is the scaffolding that lets a long-form textbook
not drop to first principles cognitively: the abstraction is introduced,
internalized, and then carries the load — like a scheme for its points,
a section of the tangent bundle for a "continuously varying choice," a
groupoid for a group.

Concrete standard — name the value / scale submodule once, fenced, as a
categorical image, then evenness and all later uses are containments of
$R$-submodules, not pointwise checks:

* **Scaffolding (once, fenced):**
  "::: {#def-val} **Definition.** Let $R$ be commutative and $b\colon
  M\otimes_RM\to W$ $W$-valued bilinear. Put
  $\operatorname{Val}(b):=\langle b(x,x)\mid x\in M\rangle_R\subseteq W$
  the $R$-submodule spanned by the diagonal — equivalently the image
  $R$-submodule of $b\circ\Delta\colon M\to W$ for
  $\Delta\colon M\to M\otimes M$, i.e. the image of
  $\operatorname{Hom}_R(\Gamma^2_R(M),W)\xrightarrow{\gamma^*}W$ under
  evaluation. It is an $R$-submodule of $W$, functorial in $W$ via
  $\operatorname{Hom}$. :::" Stably the image $R$-submodule of
  $b\colon M\otimes^L_RM\to W$ in $\mathbf{LMod}_R$.

  Similarly $\mathfrak s(b)$, $N(b)$, $\operatorname{scale}(b)$ per
  flavour; the name is the point — one governing object.

* **From then on:** "$b$ is **even** if $\operatorname{Val}(b)\subseteq
  2W$ as $R$-submodules of $W$" (for $2W:=\operatorname{im}(2\colon
  W\to W)$). No $x$, no "for every $x$," no "$\in$." Functoriality
  $\operatorname{Val}(f^*b)\subseteq\operatorname{Val}(b)$,
  $\operatorname{Val}(b\perp b')$, containments, etc., are then statements
  about $R$-submodules, not re-expansions.

This is the global (scheme / Hom from $\Gamma^2$ / $\operatorname{Val}$)
versus local (set of points $x\in U(M)$) move: collect all points once
as the object, then work with the object — 50+ years standard since
Grothendieck.

**Banned:** " $b$ is *even* if $b(x,x)\in2W$ for every $x$" as the
recurring definition and every later "check $b(x,x)\in2W$ for every $x$."

**Preferred:** define $\operatorname{Val}(b)\subseteq W$ once via
{#def-val}; then "$b$ is **even** if $\operatorname{Val}(b)\subseteq2W$."
Never carry $b(x,x)\in2W$ on every use once $\operatorname{Val}(b)$ is
available — use the submodule.

### `PR-50`: Nominalizing the adjective/verb — "satisfies the evenness / injectivity / exactness / commutativity condition" for "is even / injective / exact" / "commutes / factors"

"Even" is an adjective on $b$ ($b$ **is even**,
$b\in\operatorname{EvBil}$); "commutes" / "factors" are verbs on the
diagram. Nominalizing to "evenness," "injectivity," "exactness,"
"commutativity," "factorization" + "condition" forces a light verb
"satisfies / has / exhibits / possesses" to re-predicate it — one
checkable predicate becomes three words for no new content, with no
named subobject to check (same device as "with its hypotheses," PR-31).
Standard is the un-nominalized predicate.

Concrete bad / standard pairs (transcribe, do not invent):

* **Banned:** "When $2W=W$, every bilinear form satisfies the evenness
  condition."
  **Preferred:** "When $2W=W$, every $W$-valued bilinear $b$ is even"
  (i.e. $\operatorname{EvBil}_{R,W}(M)=\operatorname{Bil}_{R,W}(M)$ as
  $R$-submodules; element shadow "$b(x,x)\in2W$ $\forall x$" vacuous) —
  or, for the non-vacuous content: "the quadratic refinement
  $\operatorname{Quad}_{R,W}(M)=\operatorname{Hom}_R(\Gamma^2_R(M),W)$
  still distinguishes forms via $\gamma^*$." One adjective, one membership
  $b\in\operatorname{EvBil}$.

* **Banned:** " $f$ satisfies the injectivity condition / satisfies
  injectivity."
  **Preferred:** "$f$ is injective" ($f\colon M\hookrightarrow N$ as
  monomorphism, $\ker f=0$).

* **Banned:** "the sequence satisfies exactness at $M$."
  **Preferred:** "the sequence is exact at $M$" ($\operatorname{im}=\ker$).

* **Banned:** "the diagram satisfies the commutativity condition /
  exhibits commutativity."
  **Preferred:** "the diagram commutes" ($g\circ f = h$).

* **Banned:** " $b$ satisfies the factorization condition through
  $\Gamma^2$."
  **Preferred:** "$b$ factors through $\Gamma^2_R(M)$"
  / "$b$ lifts through $\Gamma^2_R(M)$."

In each case delete the noun "…ness / …ivity / …ion" + "condition" + light
verb, and keep the adjective/verb that already is the claim with its
named subobject/diagram.

### `TERM-12`: "Quadratic refinements" with no defined refinement relation — fossilized adjective with no map

"Refinement" is plausible because the polar
$b_q(x,y):=q(x+y)-q(x)-q(y)$ does give a map
$\gamma^*\colon\operatorname{Quad}_{R,W}(M)\to\operatorname{Bil}_{R,W}(M)$,
$q\mapsto b_q$, so a $q$ with $b_q=b$ can be called a quadratic refinement
of $b$. That meaning requires the named $R$-linear
$\gamma^*\colon\operatorname{Hom}_R(\Gamma^2_R(M),W)\to\operatorname{Hom}_R(M\otimes_RM,W)$
(induced by $\Gamma^2_R(M)\xrightarrow{\gamma}\operatorname{Sym}^2_R(M)\to M\otimes M$)
to be defined, with its (non-)injectivity/surjectivity and fiber discussed —
is a refinement a section, a lift, a fiber over $b$? No $\gamma^*$ was named
and no $\ker(\gamma^*)/\operatorname{coker}(\gamma^*)$ was stated, so there
is no sense, even informally, in which either direction could be called a
refinement, and "quadratic refinements" is just "quadratics" preceded by a
math-adjacent word with no referent. It is also nonstandard in the
direction used here: the associated object is the bilinear *polar* $b_q$
of $q$, not $q$ "refining" $b$ without the map.

Concrete standard — name $\gamma^*$ and its fiber, then "refinement" is
the fiber:

"::: {#def-quad-polar} **Definition.** Put
$\operatorname{Quad}_{R,W}(M):=\operatorname{Hom}_R(\Gamma^2_R(M),W)$ and
$\operatorname{Bil}_{R,W}(M):=\operatorname{Hom}_R(M\otimes_RM,W)$ as
$R$-modules. The $R$-linear
$\gamma^*\colon\operatorname{Quad}_{R,W}(M)\to\operatorname{Bil}_{R,W}(M)$
sends $q$ to its polar $b_q(x,y)=q(x+y)-q(x)-q(y)$. A **quadratic
refinement** of $b\in\operatorname{Bil}_{R,W}(M)$ is a $q$ with
$\gamma^*(q)=b$ — i.e. a point in the fiber over $b$. :::"

**Banned:** "quadratic refinements retain …" with no $\gamma^*$,
no $b$, no fiber.

**Preferred:** "the fiber of $\gamma^*\colon\operatorname{Quad}_{R,W}(M)\to
\operatorname{Bil}_{R,W}(M)$ over $b$" / "the set of $q$ with $b_q=b$"
with $\gamma^*$ named; or just "$q\in\operatorname{Quad}_{R,W}(M)$."

### `PR-51`: "Retain additional information" is empty filler — not a submodule, kernel, fiber, or invariant

"Information" is not an $R$-submodule, kernel, cokernel, fiber, or
invariant, so "retain additional information" cannot be true or false;
additional *relative to what* — to $\operatorname{EvBil}$, to
$\operatorname{SymBil}$, to the element condition $b(x,x)\in2W$ just
declared vacuous? The precise content is the (non-)isomorphism between
*named* $R$-modules and its obstruction.

Concrete standard — state the (non-)isomorphism and its fiber:

"::: {#prop-quad-vs-bil} **Proposition.** $\gamma^*$ is not an
isomorphism in general; when $2\colon W\to W$ is invertible,
$\operatorname{EvBil}_{R,W}(M)=\operatorname{Bil}_{R,W}(M)$ as element
condition but $\gamma^*\colon\operatorname{Quad}_{R,W}(M)\to
\operatorname{EvBil}_{R,W}(M)$ still has non-trivial fiber: the set of
quadratic refinements of $b$ is a torsor under
$\operatorname{Hom}_R(M,W/2W)$ (discrete case), with obstruction
$\ker(\gamma^*)/\operatorname{coker}(\gamma^*)$. :::"

**Banned:** "quadratic refinements retain additional information."

**Preferred:** "$\gamma^*$ is not an isomorphism; its fiber over $b$
(retaining the extra invariant) is …" / "$\ker(\gamma^*)$ is …" — name
the $R$-module map and its fiber/kernel, not "information."

### `TERM-13`: "Discriminant setting" is not a mathematical object — the object is the category of torsion bilinear/quadratic modules

There is no mathematical object called a "setting." What is meant is a
*category* — torsion $R$-modules with nondegenerate $W$-valued forms,
e.g. finite $\mathcal O_X$-modules, $D_L:=L^\vee/L$ with
$\mathbb Q/\mathbb Z$- or $\mathbb Q/2\mathbb Z$-valued form — which
has not been defined. Sign-posting it here in a sentence about $2W=W$
also inverts dependency order and violates theory-of-mind: only
$\operatorname{Bil}_{R,W}(M)$ for general $M\in\mathbf{Mod}_R$ has been
defined; lattices, duals $L^\vee:=\operatorname{Hom}_R(L,R)$, finite
quotients $D_L$, and their induced torsion forms are later, so the
reader does not yet know what "discriminant" means. A general
$\operatorname{Bil}/\operatorname{Quad}$ cannot be motivated by a
specialization that has not been introduced.

Concrete standards:

* **Object, not setting:**
  "::: {#def-disc-cat} **Definition.** Let $\mathbf{TorBil}_{R,W}$ (resp.
  $\mathbf{TorQuad}_{R,W}$) be the category whose objects are pairs
  $(T,\bar b)$ with $T\in\mathbf{Mod}_R$ torsion of finite length and
  $\bar b\colon T\otimes_R T\to W/\operatorname{Val}$ nondegenerate
  $W$-valued torsion bilinear (resp. quadratic) form. :::"

* **Discriminant as object of that category, defined later:**
  "::: {#def-discriminant} For a lattice $L$ with $b\colon L\otimes L\to R$
  nondegenerate, put $D_L:=L^\vee/L$ and let $\bar b$ / $\bar q\colon
  D_L\to\mathbb Q/\mathbb Z$ ($\to\mathbb Q/2\mathbb Z$ for quadratic) be
  the induced torsion form. :::"

**Banned:** "in the discriminant setting."

**Preferred:** name the category
$\mathbf{TorBil}_{R,W}$ / $\mathbf{TorQuad}_{R,W}$ when it is defined,
and the object $(D_L,\bar q)$ when $L$ is defined; do not sign-post
discriminants in the general $\operatorname{Bil}/\operatorname{Quad}$
section before lattices and $L^\vee/L$ exist.

### `PR-52`: Weasel mass nouns — "information," "data," "setting," "condition," "property," "structure," "notion," … with no fixed referent

The instances we know today — "information" (PR-51),
"data" (EV-6, PR-20), "setting" (TERM-13), "condition" / "hypotheses"
(PR-31, PR-50), "conclusion" (PR-30), "value module" (TERM-9), "torsion
theory" (TERM-4), "operations / structure via $W$" (PR-38),
"presheaf" for $\mathbf{Mod}_R^{\mathrm{op}}\to\mathbf{Mod}_R$ (TERM-10) —
will change. The underlying problem is timeless and is detected by
semantic indicators, not by a word list: a mass noun with no fixed
extension in $\mathbf{Mod}_R$ / $\mathbf{Cat}_\infty$ that exploits
colloquial understanding so the sentence can be defended as "true under
some interpretation" while naming no $R$-submodule, functor, category, or
invariant to check.

Timeless indicators that a clause is weasel-wording (any one suffices to
flag):

* **No fixed referent in the book.** The noun has no fenced definition
  with a type — no $R$-submodule $\operatorname{Val}(b)\subseteq W$ for
  "information," no $W\in\mathbf{Mod}_R$ for "value module," no category
  $\mathbf{TorBil}_{R,W}$ for "setting," no list "$2\colon W\hookrightarrow
  W$ injective" for "hypotheses."

* **Truth / meaning is context-dependent where the context is never fixed
  or stated.** "Retain additional information" is true of any true
  statement; "with its hypotheses" is true of every theorem; "in the
  discriminant setting" is true in any ambient the reader imagines.

* **Unfalsifiable.** Any counterexample can be deflected as "not the
  intended information / setting / condition" because no quantified
  proposition was stated (PR-30).

* **Abuse of colloquial understanding.** The reader is expected to supply
  the mathematical meaning from ordinary English ("information" = "something
  true," "setting" = "where this happens") instead of from a defined
  morphism.

* **Occupies the slot where a named object belongs.** The noun sits where
  an $R$-submodule, functor, category, or diagram is owed, so the sentence
  is unfalsifiable without ever being precise (PR-30–32).

Concrete bad / standard pairs are instances of the same timeless check —
replace the mass noun by the named object that already has a type:

* **Banned:** "quadratic refinements retain additional information."
  **Preferred:** "$\gamma^*\colon\operatorname{Quad}_{R,W}(M)\to
  \operatorname{EvBil}_{R,W}(M)$ is not an isomorphism; its fiber over $b$
  is a torsor under $\operatorname{Hom}_R(M,W/2W)$" (PR-51).

* **Banned:** "is additional data / does not follow from notation."
  **Preferred:** "$b\in\operatorname{EvBil}_{R,W}(M)$ is the lift through
  $\Gamma^2_R(M)$" (EV-6, PR-20).

* **Banned:** "in the discriminant setting."
  **Preferred:** "in $\mathbf{TorQuad}_{R,W}$, for $(D_L,\bar q)$ with
  $D_L:=L^\vee/L$" (TERM-13).

* **Banned:** "with its hypotheses / satisfies the evenness condition."
  **Preferred:** "for $2\colon W\hookrightarrow W$ injective" /
  "$b$ is even ($b\in\operatorname{EvBil}$)" (PR-31, PR-50).

New weasel nouns will appear; audit by the indicators, not the list.
When a new mass noun is found, replace it by the $R$-submodule / functor /
category that already has a name, or define that object fenced if it does
not yet exist — do not add the noun to a list and keep the sentence.

### `PR-46`: "For every $x$, a choice of …" for the global functor / bundle / section / natural transformation

"For every $x$, a choice of $b_x$ / basis / complement / $b(x,x)\in2W$ /
isomorphism $M_x\simeq N_x$" is the element-wise unwrapping of one global
object that already has a name. Carrying the unwrapping instead of naming
the object leaves the quantifier, topology/continuity, and functoriality
($x\mapsto b_x$ natural in $x$, $f\mapsto f^*$) unspecified, so there is
nothing to check — exactly where hand-waving enters. It is the local
(points $x\in U(M)$) for global (scheme / Hom from $\Gamma^2$ /
$\operatorname{Val}$ / section) move, 50+ years standard since
Grothendieck (PR-45 is the case $\operatorname{Val}(b)$).

This is the general form of PR-37/PR-43/PR-45 and PR-30/PR-41: prose on
elements that collapses the abstraction just built for a $W$-valued,
$\mathbf{Mod}_R$-valued, or sheaf-valued construction.

Concrete standards — name the global object once, fenced, then "for every
$x$" is its evaluation on $U$-points $x\colon 1\to M$ when $U$ exists:

* **Functor, not family:** $M\mapsto\operatorname{Bil}_{R,W}(M):=
  \operatorname{Hom}_R(M\otimes_RM,W)$ as functor
  $\mathbf{Mod}_R^{\mathrm{op}}\to\mathbf{Mod}_R$ with
  $f\mapsto(f\otimes f)^*$ — not "for every $M$, the $R$-module …
  and for every $f\colon M\to N$, $f^*b(x,y)=b(fx,fy)$."

* **Submodule, not pointwise membership:** $\operatorname{Val}(b)\subseteq
  W$ as $R$-submodule for $b\colon M\otimes M\to W$ — not "for every
  $x$, $b(x,x)\in2W$."

* **Section, not pointwise choice:** a "continuously varying choice of
  basis / complement / $b_x$ for every $x\in X$" is a section of the
  frame / Grassmann / Hom-bundle $\operatorname{Fr}(E)\to X$ /
  $\underline{\operatorname{Hom}}(E,F)\to X$ — an object in
  $\mathbf{Bun}_X$, not a family $x\mapsto b_x$.

* **Sheaf morphism, not stalkwise isomorphisms:** "for every $x$, an
  isomorphism $M_x\simeq N_x$" is an isomorphism $M\simeq N$ in
  $\mathbf{Sh}(X)$ (stalkwise iso + gluing), not a family on stalks.

* **Natural transformation, not pointwise maps:** "for every $x$, a map
  $F(x)\to G(x)$" functorial in $x$ is a natural transformation
  $F\Rightarrow G$ / morphism in $\operatorname{Fun}(\mathcal C,\mathcal D)$.

In each case $x$ is a $U$-point $x\colon 1\to M$ (or $x\colon\ast\to X$)
for $U\colon\mathcal C\to\mathbf{Set}$ ($\to\mathcal S$ stably). State
the global object with its type in $\mathcal C$ ($R$-submodule, functor,
bundle, section, natural transformation), then "for every $x$" is its
evaluation, if pedagogically useful.

**Banned:** "for every $x$, choose $b_x$ / $b(x,x)\in2W$ / a complement /
an isomorphism $M_x\simeq N_x$" as the definition and every later use
without ever naming the functor / bundle / section / $R$-submodule /
natural transformation that it unwraps.

**Preferred:** name the global object once, fenced, with its category and
universal property ( $\operatorname{Val}(b)\subseteq W$ as $R$-submodule,
$\operatorname{Bil}_{R,W}\colon\mathbf{Mod}_R^{\mathrm{op}}\to\mathbf{Mod}_R$
as functor, section $s\colon X\to\operatorname{Fr}(E)$ as object in
$\mathbf{Bun}_X$, natural transformation $\eta\colon F\Rightarrow G$);
then, only after and only when $U$ exists: "On $U$-points this is for
every $x$, $b(x,x)\in2W$ / $b_x$ / $f^*b(x,y)=b(fx,fy)$."

### `PR-47`: Element quantifiers $\forall x\in M$ in the *definition* are anathema to generalization — $b\circ\tau=b$ works in every symmetric monoidal $\mathcal C$, $b(x,y)=b(y,x)$ only in $\mathbf{Set}$-concrete $\mathcal C$

"$\forall x\in M$, $b(x,y)=b(y,x)$ / $b(x,x)=0$ / $q(rx)=r^2q(x)$ /
$b(x,x)\in2W$" presupposes a concretization
$U\colon\mathcal C\to\mathbf{Set}$ with points $x\colon1\to M$
($x\in U(M)$) and the definition *is* that concretization. There is then
nothing to interpret when $U$ does not exist — $\mathrm{QCoh}(X)$ has no
underlying set of global points, $\mathbf{Sp}$ has no elements $x$, a
stack / $\infty$-category / sheaf has $U$-points only over a test
object — so the notion must be re-defined separately for
$\mathcal O_X\text{-}\mathbf{Mod}$, local systems, $\mathbf{Sp}$,
$\mathbf{Grpd}$, $\infty\text{-}\mathbf{Cat}$, $\mathbf{Sch}_{/S}$, and
functoriality / base change proved anew each time.

The diagram $b\colon M\otimes M\to W$ with $b\circ\tau=b$ /
$b\circ\tau=-b$ / $b\circ\Delta=0$ / lift through $\Gamma^2_R(M)$ names
no $x$ and no $U$ — it is a commuting diagram in the non-lax symmetric
monoidal $(\mathcal C,\otimes,1,\tau)$ ($\tau\colon M\otimes M\to M\otimes
M$ an isomorphism, $\tau^2=\mathrm{id}$). It *is* the definition in every
symmetric monoidal $\mathcal C$ at once, and its evaluation on
$U$-points $x\otimes y\colon1\to M\otimes M$ when $U$ *does* exist
recovers the element formula as a theorem, not a definition, so one
general concept does the work everywhere.

This is the general form behind PR-43/PR-44 and PR-39/PR-40/TERM-11: the
tensor classifier $M\otimes M$ and $\tau$ already encode bilinears and
symmetry; re-spelling them as "$\forall x,y\in M$" concretizes the
abstraction just built.

Concrete standards — define diagrammatically once, derive elements as
shadow when $U$ exists:

* **Scaffolding (once, fenced):** $(\mathbf{Mod}_R,\otimes_R,R,\tau)$
  (stably $(\mathbf{LMod}_R,\otimes^L_R,R,\tau)$) symmetric monoidal
  closed and self-enriched {#thm-mod-closed}, with $M\otimes_RM$
  classifying bilinears {#def-tensor} and $\tau_{M,M}$ the symmetry,
  $\Delta$, $\Gamma^2_R$ as in PR-43. The same structure exists in
  $(\mathrm{QCoh}(X),\otimes_{\mathcal O_X},\mathcal O_X,\tau)$,
  $(\mathbf{Sp},\wedge,\mathbb S,\tau)$, etc. — no $U$ needed.

* **$W$-valued $b\colon M\otimes_RM\to W$ is symmetric / skew /
  alternating / even** as in PR-43: $b\circ\tau=b$, $b\circ\tau=-b$,
  $b\circ\Delta=0$, lift through $\Gamma^2_R(M)$. No $x,y$.

* **Element shadow (only after, when $U\colon\mathcal C\to\mathbf{Set}$
  exists):** for $x,y\colon1\to M$ (i.e. $x,y\in U(M)$),
  $b\circ\tau=b$ evaluates to $b(x,y)=b(y,x)$, etc. This is a property of
  the diagram, proved by applying $U$ to $x\otimes y\colon1\to M\otimes
  M$, not the definition.

**Banned:** definitions quantified as "for every $x\in M$, $b(x,y)=b(y,x)$
/ $b(x,x)=0$ / $q(rx)=r^2q(x)$ / $b(x,x)\in2W$ for every $x$."

**Preferred:** "Let $b\colon M\otimes_RM\to W$ be $W$-valued bilinear. $b$
is **symmetric** if $b\circ\tau=b$ (resp. skew if $b\circ\tau=-b$,
alternating if $b\circ\Delta=0$, even if it lifts through
$\Gamma^2_R(M)$)." Then, if pedagogically useful and only when
$U$ exists: "On $U$-points this is $b(x,y)=b(y,x)$ $\forall x,y\in
U(M)$."

### `PR-53`: A definition is a general building block, not the minimal element condition that lets the next paragraph type-check

"$\{x\mid b(x,N)=0\}$ / $b(x,x)=0$ / $\forall x\in M$" is the cheapest
sentence that lets this page proceed for $\mathbf{Mod}_R$ and matches the
classical $b(x,N)=0$ literature, but it is not a building block — it
names no $R$-linear $b^{\sharp}\colon M\to\underline{\operatorname{Hom}}(M,W)$,
no kernel, no dual, no $\operatorname{Val}(b)$, no $\Gamma^2_R$ — so every later
notion (radical, nondegenerate, $L^\vee$, $D_L$, discriminant form) must
be rebuilt elementwise and cannot be transported to
$\mathrm{QCoh}(X)$, $\mathbf{Sp}$, sheaves, $\infty\text{-}\mathbf{Cat}$,
$\mathbf{Sch}_{/S}$ without re-defining. The time saved today is the
applicability lost tomorrow, next week, and across a research career.

A definition in a long-form book is the reusable interface the rest of
the book *and* future work build on: state it once, diagrammatically,
with its universal property, so that later definitions are instances and
element formulas are shadows, not re-definitions.

Concrete standard — name the adjoint and its kernel as the building
blocks (all do the work of the elementwise $N^{\perp}$ / isotropic), then
later theory is immediate:

* **Scaffolding (once, fenced):**
  $\operatorname{Hom}_R(M\otimes_RM,W)\cong\operatorname{Hom}_R(M,
  \underline{\operatorname{Hom}}_R(M,W))$ via the closed structure
  {#thm-mod-closed} / {#def-tensor}. For $b\colon M\otimes_RM\to W$ put
  $b^{\sharp_{\!L}},b^{\sharp_{\!R}}\colon M\to\underline{\operatorname{Hom}}_R(M,W)$,
  $x\mapsto b(x,-)$ and $x\mapsto b(-,x)$, the two adjoints. When $b$
  symmetric they agree and are written $b^{\sharp}$.

* **Then, as $R$-submodules / kernels (no $x$):**
  $N^{\perp_{\!L}}:=\ker(M\xrightarrow{b^{\sharp_{\!L}}}
  \underline{\operatorname{Hom}}_R(N,W))$ (and $\perp_{\!R}$ via the other
  adjoint), the $R$-submodule classified by the universal property for
  "$b(x,N)=0$";
  $Q_{R,W}(M):=\ker(M\xrightarrow{\Delta}M\otimes M\xrightarrow{b}W)$ for
  $q:=b\circ\Delta$ (quadratic diagonal) — $x$ isotropic iff
  $x\in\ker(q)$ as $U$-shadow, and $b$ anisotropic iff $\ker(q)=0$ as
  subobject of $M$ (not "$0$ is the only isotropic element");
  $M$ nondegenerate iff $b^{\sharp}$ is iso; $M^\vee:=
  \underline{\operatorname{Hom}}_R(M,R)$; $D_L:=L^\vee/L$ with
  $\bar b$ / $\bar q$ induced via $b^{\sharp}$ — all as kernels /
  cokernels of the named $b^{\sharp}$, not as sets $\{x\mid\ldots\}$.

* **Element shadow (only after, when $U$ exists):** for $x\colon R\to M$
  ($x\in U(M)$), $x\in N^{\perp}$ evaluates to $\forall n\in U(N)$,
  $b(x,n)=0$, and $x\in\ker(q)$ to $b(x,x)=0$.

**Banned:** "$N^{\perp}:=\{x\in M\mid b(x,N)=0\}$" / "$x$ isotropic if
$b(x,x)=0$, $b$ anisotropic if $0$ is its only isotropic element" as the
*definitions* that later theory must reuse.

**Preferred:** define $b^{\sharp}$ once, then
$N^{\perp}:=\ker(b^{\sharp})$, " $x$ isotropic if $x\in\ker(b\circ\Delta)$,"
"$b$ anisotropic if $\ker(b\circ\Delta)=0$ as subobject of $M$." The element
formulas are the $U$-evaluation of those kernels, proved as a property,
not the building block.

### `PR-54`: Long-term general applicability is an explicit design goal — write it down or no agent will know it

The implicit goal behind PR-43/PR-47/PR-53 — one definition that works
in every symmetric monoidal abelian $\mathcal C$ at once ($\mathbf{Mod}_R$,
$\mathbf{LMod}_R$, $\mathrm{QCoh}(X)$, $\mathbf{Sp}$-modules, sheaves,
$\infty\text{-}\mathbf{Cat}$, $\mathbf{Sch}_{/S}$) so that later theory
($\operatorname{Val}(b)$, $b^{\sharp}$, $M^\vee$, $D_L$, discriminant
forms) is an instance, not a re-definition — is not inferable from the
current page's minimal needs. No agent can know it unless it is written
down in this document and in the book's scaffolding section.

When a definition admits an easy, no-harder generalization that
immediately recovers the classical element formula (here
$b\circ\tau=b$ for $b(x,y)=b(y,x)$, $b^{\sharp}$ for $N^{\perp}$,
$\ker(b\circ\Delta)$ for isotropic) and drastically increases
applicability down the line, the general form *is* the definition.
Saving time today with the minimal "$\forall x\in M$" costs re-definition
for every future $\mathcal C$ and degrades a forward-thinking research
program that will live with these interfaces for years.

**Standard:** in the book's introduction / scaffolding preamble and in
this `CONTRIBUTING.md`, state explicitly: "All bilinear/quadratic
notions are defined diagrammatically via $(\otimes,1,\tau)$ and
$b^{\sharp}$ in a closed symmetric monoidal abelian $\mathcal C$, so as
to apply to $\mathbf{Mod}_R$, $\mathrm{QCoh}(X)$, $\mathbf{Sp}$, etc.,
with element formulas only as the $U$-evaluation when $\mathcal C$ is
$\mathbf{Set}$-concrete. Minimal elementwise definitions are not the
goal; reusable building blocks are." Then enforce it: every new
definition is reviewed against that stated goal, not against the cheapest
sentence that lets the next paragraph proceed.

### `PR-55`: Hygiene and foresight — building on the $\mathbf{Set}$-shadow instead of on the named categorical object that classifies it

The lack of hygiene in "$M=N\oplus N^{\perp}$," "$b(x,y)=b(y,x)$," "$b(x,x)\in2W$," "$\{x\mid b(x,N)=0\}$," "$b$ satisfies the evenness condition," "pullback defines a presheaf," "retain additional information in the discriminant setting" is one pattern: the definition / theorem is stated on the evaluation of a categorical object on $U$-points $x\colon1\to M$ ($U\colon\mathcal C\to\mathbf{Set}$), not on the object that classifies that evaluation. The shadow is locally correct for $\mathbf{Mod}_R$ and matches classical $b(x,N)=0$ literature, but it names no $b^{\sharp}$, no $\ker$, no $\operatorname{Val}(b)$, no $\operatorname{Bil}_{R,W}$, no $\Gamma^2_R$, so it cannot be reused and cannot be transported: every later notion must be re-spelled elementwise and every $\mathcal C$ without $U$ (e.g. $\mathrm{QCoh}(X)$, $\mathbf{Sp}$-modules, sheaves, $\infty\text{-}\mathbf{Cat}$) needs a new definition.

Foresight is stating the scaffolding and the governing object once, diagrammatically, with its universal property, so that the element formula is its shadow — not its definition — and later theory is an instance.

Concrete scaffolding that was owed once, fenced, before any $b(x,y)$ or $N^{\perp}$:

* $(\mathbf{Mod}_R,\otimes_R,R,\tau)$ symmetric monoidal closed and self-enriched, $M\otimes_RM$ classifying $R$-bilinears, $\underline{\operatorname{Hom}}_R(M,W)\in\mathbf{Mod}_R$ as internal hom {#thm-mod-closed}/{#def-tensor}; $\operatorname{Hom}_R(M\otimes M,W)\cong\operatorname{Hom}_R(M,\underline{\operatorname{Hom}}_R(M,W))$ giving $b^{\sharp_{\!L}},b^{\sharp_{\!R}}\colon M\to\underline{\operatorname{Hom}}_R(M,W)$.
* $\operatorname{Bil}_{R,W}(M):=\operatorname{Hom}_R(M\otimes M,W)$ and its named $R$-submodules $\operatorname{SymBil}:=\ker(\tau^*-\mathrm{id})$, $\operatorname{SkewBil}:=\ker(\tau^*+\mathrm{id})$, $\operatorname{AltBil}:=\ker(\Delta^*)$, $\operatorname{EvBil}:=\operatorname{im}(\gamma^*)$ with $\Gamma^2_R\xrightarrow{\gamma}\operatorname{Sym}^2_R\to M\otimes M$; $\operatorname{Quad}_{R,W}(M):=\operatorname{Hom}_R(\Gamma^2_R(M),W)$ and $\gamma^*\colon\operatorname{Quad}\to\operatorname{Bil}$.
* $\operatorname{Val}(b)\subseteq W$ as $R$-submodule $\langle b(x,x)\rangle$ i.e. image of $\gamma^*$; $N^{\perp}:=\ker(M\xrightarrow{b^{\sharp}}\underline{\operatorname{Hom}}_R(N,W))$; isotropic as $\ker(M\xrightarrow{\Delta}M\otimes M\xrightarrow{b}W)$, anisotropic as $\ker=0$; nondegenerate as $b^{\sharp}$ iso; $M^\vee:=\underline{\operatorname{Hom}}_R(M,R)$; $(M,b)\perp(N,c)$ as orthogonal sum in $\mathbf{Bil}_{R,W}$.

With those named, hygiene is: every definition is membership in a named $R$-submodule / kernel of a named $R$-linear map; every theorem is a containment of named subobjects or a statement about a named map $2_*$ / $\gamma^*$ being (non-)iso with obstruction $\ker/\operatorname{coker}$; every "for every $x$" is the $U$-evaluation of that diagram when $U$ exists. The minimal "$\forall x\in M$, $b(x,y)=b(y,x)$ / $b(x,N)=0$ / $b(x,x)\in2W$" is then never the definition.

**Banned:** any definition / theorem that quantifies $\forall x\in M$ / $\{x\mid\ldots\}$ / "$b\colon M\times M\to W$" / "$b$ satisfies the … condition" / "pullback … defines a presheaf" / "retain additional information in the … setting" / "$M=N\oplus N^{\perp}$ and the sum is orthogonal" as prose without the named $b^{\sharp}$, $\ker$, $\operatorname{Bil}$ / $\operatorname{Alt}/\operatorname{Skew}/\operatorname{EvBil}$, $\operatorname{Val}(b)$, $\Gamma^2_R$, and the proved biproduct $\perp$ vs. $\oplus$ in $\mathbf{Bil}_{R,W}$ vs. $R\text{-}\mathbf{Mod}$.

**Preferred:** state the scaffolding once; then every bilinear/quadratic notion is a named $R$-submodule / kernel / image with its universal property, every implication is a Lemma/Proposition about containments of those named subobjects or about $\gamma^*$ / $2_*$ between named objects with quantified hypotheses and proof, and element formulas appear only as "on $U$-points $x\colon R\to M$ this is $b(x,y)=b(y,x)$."

### `PR-56`: "$N\subseteq M$ be a submodule" / "$M/N$" for $i\colon N\hookrightarrow M$ and $\operatorname{coker}(i)$ — subobjects as monos and quotients as cokernels

"$N\subseteq M$" is the $\mathbf{Set}$-shadow of a mono $i\colon
N\hookrightarrow M$ ($U(i)\colon U(N)\hookrightarrow U(M)$ injective for
$U\colon\mathbf{Mod}_R\to\mathbf{Set}$), and "$M/N$" the shadow of its
cokernel $M\twoheadrightarrow\operatorname{coker}(i)$ (the set of cosets
$[x]=x+N$). The elementwise induced form
"$\bar b([x],[y]):=b(x,y)$ well-defined iff $b(N,M)=0$" re-spells the
universal property of the cokernel on representatives $x,y\in U(M)$.

Stated with $i$ and $\operatorname{coker}(i)$ the notion is one diagram
in any abelian $\mathcal C$ (stably any stable $\mathcal C$) — no $U$,
no representatives — and $N$ need not be a subset: a subobject is an
equivalence class of monos, not $N\subseteq U(M)$ ($\mathrm{QCoh}(X)$,
$\mathbf{LMod}_R$ stably, $\mathbf{Sp}$-modules, sheaves have no
underlying set $M/N$).

Concrete standards — name the mono and its cokernel, then the induced
form is the unique factorization through $\pi\otimes\pi$:

* **Scaffolding (once, fenced):** in abelian $\mathcal C$, a subobject of
  $M$ is a mono $i\colon N\hookrightarrow M$ up to iso over $M$; its
  **quotient** is $\operatorname{coker}(i)\colon M\twoheadrightarrow
  \operatorname{coker}(i)$ with universal property: $f\colon M\to T$
  factors uniquely through $\operatorname{coker}(i)$ iff $f\circ i=0$.

* **Forms on quotients:** for $b\colon M\otimes M\to W$ symmetric (or
  any $b$), and $i\colon N\hookrightarrow M$, the **restriction** is
  $i^*b:=b\circ(i\otimes i)\colon N\otimes N\to W$; $i$ is **isotropic**
  ($N\subseteq N^{\perp}$) iff $b\circ(i\otimes\mathrm{id}_M)=0\colon
  N\otimes M\to W$ (i.e. $i^*b$ and the cross terms vanish as $b\circ
  (i\otimes\mathrm{id})=0$). Then $b$ **induces** $\bar b\colon
  \operatorname{coker}(i)\otimes\operatorname{coker}(i)\to W$ iff
  $i^*b=0$ in that sense, and $\bar b$ is the unique $R$-linear with
  $\bar b\circ(\pi\otimes\pi)=b$ for $\pi:=\operatorname{coker}(i)$. No
  $[x]$ to choose, no well-definedness to check.

  Stably $\operatorname{cofib}(i)$ for $i\colon N\to M$ in
  $\mathbf{LMod}_R$.

**Banned:** "Let $b$ be symmetric on $M$ and let $N\subseteq M$ be a
submodule. … forms on quotients $M/N$ … $\bar b([x],[y])=b(x,y)$."

**Preferred:** "Let $b\colon M\otimes M\to W$ be symmetric and let
$i\colon N\hookrightarrow M$ be a mono (a subobject). Put
$\pi\colon M\twoheadrightarrow\operatorname{coker}(i)$ for the quotient.
Then $b$ induces $\bar b\colon\operatorname{coker}(i)\otimes
\operatorname{coker}(i)\to W$ iff $i^*b=0$ (i.e. $b\circ(i\otimes
\mathrm{id}_M)=0$), uniquely with $\bar b\circ(\pi\otimes\pi)=b$."
Then, only after and only when $U$ exists: "On $U$-points this is
$\bar b([x],[y])=b(x,y)$ for $[x]=\pi(x)$."

### `PR-57`: "$N^{\perp}$" alone is not well-defined — even when $N$ abstractly a submodule of $M$ — it is $(M,b,i\colon N\hookrightarrow M)^{\perp}$

"$N^{\perp}$" as written suggests a function of the abstract $R$-module
$N$ (or of $N$ up to isometry as lattice), but
$N^{\perp}:=\ker(M\xrightarrow{b^{\sharp}}\underline{\operatorname{Hom}}_R(N,W))$
with $b^{\sharp}=b\circ(i\otimes\mathrm{id}_M)$ depends on the triple
$(M,b,i)$ — the ambient $M$, the $W$-valued
$b\colon M\otimes M\to W$, and the mono $i\colon N\hookrightarrow M$ that
makes $N$ a *subobject*, not on $N$ abstractly. Change $b$ or change $i$
and the kernel moves while abstract $N$ does not. "Abstractly a submodule
of $M$" (i.e. $N\cong N'$ as $R$-module / as lattice) does not determine
$i$, and even $N\subseteq M$ as a *subset* (so $i$ is the inclusion) does
not determine $b$.

Concrete standards — name the triple, and keep $N^{\perp}$ with its
ambient:

* **Object:** for $i\colon N\hookrightarrow M$ and
  $b\colon M\otimes M\to W$, put
  $N^{\perp_{b}}:=N^{\perp_{i}}:=
  (i\colon N\hookrightarrow(M,b))^{\perp}:=
  \ker(M\xrightarrow{b^{\sharp}}\underline{\operatorname{Hom}}_R(N,W))\subseteq M$
  as $R$-submodule of $M$ (stably fiber in $\mathbf{LMod}_R$). Write
  $N^{\perp_b}$ / $N^{\perp_i}$ / $(i)^{\perp}$, never bare
  "$N^{\perp}$."

* **Lattices where the distinction matters:**

  — $M=U:=\mathbb Z e\oplus\mathbb Z f$, $b(e,f)=1$, $b(e,e)=0=b(f,f)$.
  $i_1\colon N_1:=\mathbb Z e\hookrightarrow M$, $N_1\cong\langle0\rangle$
  isotropic, $N_1^{\perp}=N_1$ ($b(ae+bf,e)=b$).
  $i_2\colon N_2:=\mathbb Z(e+f)\hookrightarrow M$, $N_2\cong\langle2\rangle$
  as lattice but $U(N_2)\cong\mathbb Z\cong U(N_1)$ as $\mathbb Z$-module —
  abstractly the same $N$ — yet
  $N_2^{\perp}=\mathbb Z(e-f)\cong\langle-2\rangle\neq N_1^{\perp}$.

  — Same $M=\mathbb Z^2$, same $N=\mathbb Z(1,0)\subseteq M$ as subset, but
  $b_1=\operatorname{diag}(1,1)$ gives $N^{\perp_{b_1}}=\mathbb Z(0,1)$ while
  hyperbolic $b_2(e_i,e_j)=\delta_{i\neq j}$ gives
  $N^{\perp_{b_2}}=\mathbb Z(1,-1)$ as $R$-submodules of the same $M$;
  $N^{\perp}$ moved with $b$ while $N$ did not.

  — Primitive vs. non-primitive embeddings of the same abstract
  $A_1\langle-2\rangle$ in $U$ or $E_8$ have different $N^{\perp}$ (different
  rank, different $D_{N^{\perp}}$), so "$N^{\perp}$" without $i$ is
  ambiguous even up to isometry.

**Banned:** "$N^{\perp}$" with $N\subseteq M$ understood as abstract
$N$, or "$N^{\perp}$" with $b$ left implicit.

**Preferred:** "$N^{\perp_b}$" / "$N^{\perp_i}$" / "$(i\colon
N\hookrightarrow(M,b))^{\perp}\subseteq M$ as $R$-submodule" and, when
quoting the lattice, "the abstract lattice $N\cong\langle2\rangle$ embeds
via $i_1,i_2$ with $N^{\perp_{i_1}}\not\cong N^{\perp_{i_2}}$."

### `PR-58`: $\operatorname{Gram}(b)$ is ill-defined on $(M,b)\in\mathbf{Bil}_{R,W}$, well-defined on $((M,e),b)$ in $\mathbf{Bil}_{R,W}^{\mathrm{fr}}$ — it is $e^*b$, not a property of $(M,b)$

"$\operatorname{Gram}(b)$" as a matrix $(b(e_i,e_j))$ presupposes a finite
ordered basis $e\colon R^n\xrightarrow{\sim}M$, i.e. an object of
$\mathbf{FMod}_R^{\mathrm{fr}}$ / $\mathbf{BMod}_R$, not of
$\mathbf{Mod}_R$. An object $(M,b\colon M\otimes M\to W)$ in
$\mathbf{Bil}_{R,W}$ has $M$ arbitrary — $M=\mathbb Q$,
$\mathbb Q/\mathbb Z$, $\bigoplus_{\mathbb N}\mathbb Z$, non-free
projective all carry $W$-valued $b$ with no $n$ and no $(e_i)$ — so no
$n\times n$ matrix exists. The functor $(M,b)\mapsto\operatorname{Gram}(b)$
has no domain on $\mathbf{Bil}_{R,W}$.

On $\mathbf{Lat}_R\subseteq\mathbf{Bil}_{R,W}$ — finite free over $\mathbb Z$
(resp. $\mathbb Z_{(p)}$) with nondegenerate $b$ — an $n$ *does* exist, but
still no distinguished $e$: the $n\times n$ matrix is defined only *after*
choosing an ordered basis. Framed, it is well-typed as the pullback
$G_e(b):=e^*b:=b\circ(e\otimes e)\in M_n(W)=\operatorname{Hom}_R(R^n\otimes R^n,W)$,
i.e. $(b(e_i,e_j))$, and then $\det$, $\operatorname{rk}$, etc. are
$\operatorname{GL}_n(R)$-invariants of the isometry class $[G_e(b)]$.

Concrete standards — name the framing, then Gram is the pullback:

* **Bare $(M,b)$:** no Gram matrix.
* **Framed $((M,e),b)$:** for ordered basis $e=(e_1,\dots,e_n)\colon R^n\xrightarrow{\sim}M$,
  put $G_e(b):=e^*b\in M_n(W)$, $G_e(b)_{ij}:=b(e_i,e_j)$.

**Banned:** "$\operatorname{Gram}(b)$" for $(M,b)\in\mathbf{Bil}_{R,W}$
with no $e$.

**Preferred:** "Let $((M,e),b)$ be framed, $e\colon R^n\xrightarrow{\sim}M$.
Put $G_e(b):=e^*b\in M_n(W)$."

### `PR-59`: Without an explicit ordered basis / generating set, $\operatorname{Gram}(b)$ is well-defined only up to $\operatorname{GL}_n(R)$-congruence

Without the ordered frame $e$ the matrix has no size and no value; with
$e$ it is $G_e(b)=e^*b$ and changes by congruence when $e$ changes.
For ordered bases $e' = e\circ P$ with
$P\in\operatorname{GL}_n(R)=\operatorname{Aut}_R(R^n)$,
$G_{e'}(b)=P^{\!t}G_e(b)P$ in $M_n(W)$. So without $e$, $\operatorname{Gram}(b)$
is well-defined only as the isometry class $[G_e(b)]\in M_n(W)/\operatorname{GL}_n(R)$
— i.e. up to $\operatorname{GL}_n(R)$-congruence, with $n=\operatorname{rk}M$ itself
defined only after the framing — not as a matrix. With only a generating
set $S$ and $F(S)\twoheadrightarrow M$, the $|S|\times|S|$ matrix on
$F(S)$ is well-defined only up to $\operatorname{Aut}_R(F(S))$ and up to
stabilization by the relations of $M$; different $S$ give different sizes,
so the assignment is a function on $((M,e_S),b)$ in $\mathbf{Mod}_R^{\mathrm{fr}}$,
not on $(M,b)$.

**Banned:** "$\operatorname{Gram}(b)$" for $(M,b)$ with no $e$ (PR-58);
"the Gram matrix of $(M,b)$ is …" with no $e$ / $S$ to make the congruence
class a matrix.

**Preferred:** always name $e$: "$G_e(b)$," "$G_{e'}(b)=P^{\!t}G_e(b)P$ for
$P\in\operatorname{GL}_n(R)$," "the isometry class $[G_e(b)]$."

### `PR-60`: When a construction *chooses* data, state how it varies with the choice — or form the category whose objects carry the choice

Choosing an ordered basis $e$, a generating set $S$, a presentation
$F_2\to F_1\to X$, a point $x_0\in X$, a trivialization, etc., is not an
innocent "let $e$ be …" — it is extra data. The standard pattern is
always one of the two, stated explicitly:

* **(A) Comment on the choice:** after $G_e(b):=e^*b$, state how $G_e(b)$
  varies — $G_{e'}(b)=P^{\!t}G_e(b)P$ for $e'=e\circ P$, so $G_e(b)$ is
  well-defined up to $\operatorname{GL}_n(R)$-congruence (similarity,
  conjugacy, isometry, etc., per flavour), and invariants ($\det$,
  isometry class $[G_e(b)]$, $\operatorname{Val}(b)$) are independent of
  $e$. Without that, "$\operatorname{Gram}(b)$" with no $e$ is ill-typed
  (PR-58/PR-59).

* **(B) Form the category whose objects *carry* the choice, define the
  construction there, and study fibers/sections:** the Grothendieck
  construction whose objects are $(M,e)$ with $e$ the chosen data — e.g.
  framed $R$-modules $\mathbf{FMod}_R^{\mathrm{fr}}$ (objects $(M,e\colon
  R^n\xrightarrow{\sim}M)$), based modules (objects $(M,e)$ with $e$ a
  basis), pointed spaces $(X,x_0)$, presented modules/algebras/groups
  ($F_2\to F_1\to X$ with $X=\operatorname{coker}(F_2\to F_1)$), etc. Define
  e.g. $G\colon\mathbf{FMod}_R^{\mathrm{fr}}\to M_n(W)$,
  $((M,e),b)\mapsto G_e(b)$, then well-definedness on
  $\mathbf{Mod}_R$ is the study of the fiber over $M$ (the
  $\operatorname{GL}_n(R)$-torsor of frames) and its $\operatorname{GL}_n$-orbits,
  sections picking a frame, descent for the construction.

Either (A) or (B) is required whenever a construction chooses data.
Stating "$\operatorname{Gram}(b)$," "choose a presentation," "choose a
point" with no variance clause and no named $\mathbf{FMod}^{\mathrm{fr}}$ /
$\mathbf{PresMod}$ to host it leaves the construction ill-defined and its
dependence on the choice unfalsifiable.

**Banned:** "Put $G(b):=(b(e_i,e_j))$" with no $e$ and no
"$G_{e'}=P^{\!t}G_eP$ / well-defined up to $\operatorname{GL}_n$-congruence";
"choose a presentation $F_1\to X$ and define …" with no category whose
objects are $(X,F_1\to X)$ and no fiber/section discussion.

**Preferred:** (A) "For ordered basis $e\colon R^n\xrightarrow{\sim}M$, put
$G_e(b):=e^*b$. For $e'=e\circ P$, $G_{e'}(b)=P^{\!t}G_e(b)P$, so $[G_e(b)]$
is well-defined up to $\operatorname{GL}_n(R)$-congruence." Or (B) "Let
$\mathbf{FMod}_R^{\mathrm{fr}}\xrightarrow{U}\mathbf{Mod}_R$,
$(M,e)\mapsto M$ be the Grothendieck construction for frames. Define
$G\colon\mathbf{FMod}_R^{\mathrm{fr}}\to M_n(W)$ by $G((M,e),b):=G_e(b)$.
Then $G$ factors through $U$-fibers as $[G_e(b)]\in M_n(W)/\operatorname{GL}_n$."

### `PR-61`: $\operatorname{Gram}$ as written is overfit to free finite $W=R$ — $b\in\mathbf{Bil}_{R,W}(M)$ is a $W$-valued $(0,2)$-tensor, not a matrix, and $b(v,w)=\sum a_iG_{ij}c_j$ assumes $M=R^{(I)}$ and discrete finite support

The block "Let $M$ be free on $E=\{e_i\}_{i\in I}$, $b$ with values in $R$, $G_{ij}=b(e_i,e_j)$, $b(v,w)=\sum_{i,j}a_iG_{ij}c_j$ finite by finite support, every $(G_{ij})$ arises" is the $W=R$, free, $M=R^{(I)}$ specialization of $b\in\mathbf{Bil}_{R,W}(M):=\operatorname{Hom}_R(M\otimes_RM,W)$ written as if it were $\mathbf{Bil}_{R,W}$. An arbitrary $(M,b)$ — $M=\mathbb Q$, $\mathbb Q/\mathbb Z$, $\bigoplus_{\mathbb N}\mathbb Z$, $\mathcal O_X$-module, $\mathbf{Sp}$-module — has no $E$ and no $I\times I$ matrix, and a $W\neq R$ even on a free $M$ has $G_{ij}\in W$, not $R$.

Philosophy — never overfit to finite / finitely generated / finitely presented subcategories, never assume convergence or that topologies are discrete, never conflate a tensor with a multidimensional array or matrix unless extremely specific about the map from a matrix algebra to a Hom space / space of tensors, in which case its kernel and cokernel are the content (well-definedness, ambiguity).

Concrete standards:

* **$b$ as $W$-valued $(0,2)$-tensor.** For $R$ commutative and $W,M\in\mathbf{Mod}_R$, $b\colon M\otimes_RM\to W$ is $W$-valued covariant $2$-tensor — in index notation $b_{ij}$ with two *down* indices. When $W=R$ and $M\cong R^n$ finite free, $\operatorname{Hom}_R(M\otimes M,R)\cong M^\vee\otimes M^\vee$ is the $(0,2)$-tensor $b_{ij}$; an endomorphism is $(1,1)$-tensor $T^i_j\in\operatorname{Hom}_R(M,M)\cong M\otimes M^\vee$. $G_{ij}=b(e_i,e_j)$ as $(0,2)$ transforms by **congruence** $G_{e'}=P^{\!t}G_eP$ for $e'=eP$, $P\in\operatorname{GL}_n(R)$, i.e. $G_{e'\,kl}=\sum_{i,j}P^i_kP^j_lG_{e\,ij}$, while $(1,1)$ transforms by **similarity** $T_{e'}=P^{-1}T_eP$, $T^i_j\mapsto\sum_{k,l}(P^{-1})^i_kT^k_lP^l_j$. Writing both as "$G_{ij}$" and "$\sum a_iG_{ij}c_j$" conflates $(0,2)$ with $(1,1)$ (and with $(2,0)$ $W^\vee$-valued) and hides which $P$ acts on which side and whether $W$ is involved.

* **The map from matrices to tensors, not the identification.**
  Fix an ordered basis $e\colon R^n\xrightarrow{\sim}M$ (framed $((M,e),b)$). The $R$-linear $\Phi_e\colon M_{n\times n}(W):=W^{I\times I}\to\operatorname{Hom}_R(M\otimes M,W)$, $\Phi_e((G_{ij})):=e^*b$ with $b(e_i,e_j)=G_{ij}$, is an *isomorphism* only when $M=R^{(I)}$ free on $I$ and $W$ is discrete with $M^{(I)}$-finite support; its kernel/cokernel are the well-definedness/ambiguity content. For general $M$ the domain $M_{n\times n}(W)$ has no map to $\operatorname{Hom}_R(M\otimes M,W)$ at all — the matrix algebra and the space of $W$-valued $(0,2)$-tensors are not the same object.

* **The sum and $(L^2(\mathbb R),\int)$.** "$b(v,w)=\sum_{i,j}a_iG_{ij}c_j$, finite by finite support" is the coordinate shadow of $b\circ(e\otimes e)$ for $v=\sum_ia_ie_i$ with $a_i$ finitely supported — i.e. $M=R^{(I)}$ as *algebraic* free module with discrete topology. $(L^2(\mathbb R),\langle f,g\rangle:=\int_{\mathbb R}fg\in\mathbb R)$ is a perfectly reasonable $\mathbb R$-valued bilinear $\mathbb R$-module — $M:=L^2(\mathbb R)\in\mathbf{Mod}_{\mathbb R}$, $b(f,g):=\int fg\in\mathbb R$, $b\in\operatorname{Hom}_{\mathbb R}(L^2\otimes L^2,\mathbb R)$ stably — but $L^2$ is not $\mathbb R^{(I)}$ for any $I$ (no Hamel basis gives $f=\sum a_ie_i$ finitely; no orthonormal basis gives algebraic finite sums; $f=\sum\langle f,e_i\rangle e_i$ is $L^2$-convergent, not finite). No $I\times I$ family $G_{ij}\in\mathbb R$ and no finite $\sum a_iG_{ij}c_j$ computes $\int fg$; the Gram "matrix" is the integral kernel $K$ with $\int fg=\iint f(x)K(x,y)g(y)$, i.e. the $(0,2)$-tensor as distribution, whose map $M_{I\times I}(\mathbb R)\to\operatorname{Hom}(L^2\otimes L^2,\mathbb R)$ has huge kernel/cokernel. Never assume finite support / discrete topology.

**Banned:** the block as stated in $\mathbf{Bil}_{R,W}$ — "$M$ free on $E$, $b$ with values in $R$, $G_{ij}=b(e_i,e_j)$, $b(v,w)=\sum a_iG_{ij}c_j$ finite, every $(G_{ij})$ arises" as the definition of $\operatorname{Gram}$ for $(M,b)\in\mathbf{Bil}_{R,W}$.

**Preferred:** for $R$ commutative and $W,M\in\mathbf{Mod}_R$, put $b\in\mathbf{Bil}_{R,W}(M):=\operatorname{Hom}_R(M\otimes M,W)$ as $W$-valued $(0,2)$-tensor $b_{ij}$ with two down indices; for framed $((M,e),b)$, $e\colon R^n\xrightarrow{\sim}M$, put $G_e(b)_{ij}:=b(e_i,e_j)\in W$ and state $\Phi_e$ and its variance $G_{e'}=P^{\!t}G_eP$ (congruence, not similarity), with kernel/cokernel of $\Phi_e$ as the well-definedness content. Never write $G_{ij}$ for a $(1,1)$-tensor and a $(0,2)$-tensor without distinguishing, and never assume $M=R^{(I)}$ or finite $I$.

### `PR-62`: "$b(v,w)=\sum_{i,j}a_iG_{ij}c_j$" smuggles a Riesz theorem and the canonical $\langle v,w\rangle_0:=\sum_ia_ic_i$ on $F=R^{(I)}$ — eliding its hypotheses, completions, and the operator form $b(v,w)=\langle v,Aw\rangle$

The double sum as *definition* of how $b$ is evaluated assumes the
theorem "$\Phi_e\colon W^{I\times I}\xrightarrow{\sim}\operatorname{Hom}_R(R^{(I)}\otimes R^{(I)},W)$ and
$b(v,w)=\sum_{i,j}a_iG_{ij}c_j$" — i.e. that $b$ is determined by
$G_{ij}$ and evaluation pulls through the finite $a_i,c_j$. For
$F:=R^{(I)}$ algebraic free with discrete $W$, $\sum a_iG_{ij}c_j$ is
finite by finite support, so the statement holds with no convergence.
For non-free / non-algebraic $M$ it is a Riesz-type identification that
need not hold without honest hypotheses (finite $I$, $M$ finitely
generated projective, $W$ discrete, continuity, completeness).

What is elided is that $F$ already carries the *canonical* $R$-bilinear
$\langle v,w\rangle_0:=\sum_{i\in I}a_ic_i$ for $v=\sum a_ie_i$,
$w=\sum c_ie_i$ ($G_{ij}=\delta_{ij}$) — itself a $(0,2)$-tensor — well-defined
only with those finiteness/discreteness hypotheses ($a_i,c_i$ finitely
supported; for $I$ infinite or after completion to $\widehat F$,
$\sum a_ic_i$ is an infinite series whose existence *is* convergence in
$R$'s topology). Given that $\langle\,,\,\rangle_0$, any $b$ is
$b(v,w)=\langle v,Aw\rangle_0$ where $A\colon F\to F$ is the $R$-linear
with matrix $G_{ij}$ — $(Aw)_i=\sum_jG_{ij}c_j$ — i.e. $G$ is the
$(1,1)$-tensor $A$ seen as $(0,2)$ via $\langle\,,\,\rangle_0$:
$b_{ij}=\langle e_i,Ae_j\rangle_0$. The double sum is the coordinate
expansion of the single operator evaluation $\langle v,Aw\rangle_0$, and
"every $(G_{ij})$ arises" is the Riesz identification
$\mathbf{Bil}_{R,R}(F)\cong\operatorname{Hom}_R(F,F)$ via $\langle\,,\,\rangle_0$,
which is perfect on $F$.

Riesz as usually stated never writes the double sum: it is
"$b(v,w)=\langle v,Aw\rangle$ for a unique $A$ with … (symmetric $\iff$
$A$ self-adjoint, bounded / Hilbert-Schmidt / Fredholm / elliptic per the
topological hypotheses)," with the map $W^{I\times I}\to\operatorname{Hom}(F\otimes F,W)$
and its kernel/cokernel, and the convergence/completion hypotheses, made
explicit. The "$b(v,w)=\sum a_iG_{ij}c_j$ finite by finite support" elides
all of that, and defers the research extensions — completions,
topological tensor products, continuity — that will be needed anyway for
e.g. $(L^2(\mathbb R),\int)$ where $f=\sum\langle f,e_i\rangle e_i$ is
$L^2$-convergent, not finite.

Concrete standard — make the canonical form and the operator form
explicit, with hypotheses:

"::: {#rmk-canonical} **Remark.** $F:=R^{(I)}$ carries the tautological
$\langle v,w\rangle_0:=\sum_{i\in I}a_ic_i$ for $v=\sum a_ie_i$,
$w=\sum c_ie_i$ with $a_i,c_i$ finitely supported; it is the
$(0,2)$-tensor $\delta_{ij}$, well-defined only for $F$ algebraic free
discrete. For $b\in\mathbf{Bil}_{R,R}(F)$, put $A$ with
$A(e_j):=\sum_iG_{ij}e_i$; then $b(v,w)=\langle v,Aw\rangle_0$. Stably /
topologically this is $b\in\operatorname{Hom}_{\mathrm{cont}}(\widehat
F\hat\otimes\widehat F,W)\cong\{\text{matrices with summability}\}$. :::"

**Banned:** "$b(v,w)=\sum_{i,j}a_iG_{ij}c_j$, a finite sum by finite support
of the coordinates. Every family $(G_{ij})$ arises uniquely" as the
*definition* of evaluation for $(M,b)\in\mathbf{Bil}_{R,W}$.

**Preferred:** for $F=R^{(I)}$ state the Proposition with honest
hypotheses — "$\Phi_e\colon W^{I\times I}\xrightarrow{\sim}
\operatorname{Hom}_R(F\otimes F,W)$ via $G_{ij}=b(e_i,e_j)$ is an iso for
$F$ free on finite $I$ (resp. algebraic $R^{(I)}$ discrete), with
$b(v,w)=\langle v,Aw\rangle_0$ for $A$ as above" — and for general
$(M,b)$ keep $b\colon M\otimes M\to W$ as $(0,2)$-tensor, not a double
sum.

### `PR-63`: One bilinear setup must simultaneously generalize the arithmetic local, the geometric global, and the analytic — do not overfit to finite / discrete and defer the extensions that will be needed anyway

The Gram block as written is overfit to the arithmetic *finite* free
$W=R$ case ($M=R^{(I)}$ algebraic, $I$ finite, $W$ discrete,
$b(v,w)=\sum a_iG_{ij}c_j$ finite) and elides that the same $b\colon
M\otimes M\to W$ must already work for the geometric and analytic
specializations that the book will need anyway. Any definition that does
not immediately generalize to topological groups/modules/algebras,
schemes/stacks, sheaves, derived categories, infinite-dimensional/rank
modules should be taken as a sign the definition is overfit.

Philosophy — never overfit to finite / finitely generated / finitely
presented subcategories, never assume convergence or that topologies are
discrete (PR-61/PR-62), and always ask if the statement immediately
generalizes:

* **Arithmetic local theory:** finitely generated $R$-modules, tensors
  $M\otimes_RM$, $W$-valued forms $b\colon M\otimes M\to W$,
  $\operatorname{Val}(b)$, $b^{\sharp}$, $M^\vee$, $D_L$, Grothendieck–Witt
  theory as the study of $(M,b)$ over local $R$ (strict henselizations,
  completions).

* **Geometric global theory:** schemes/stacks, $\mathrm{QCoh}(X)$,
  $M\in\mathrm{QCoh}(X)$ with $\mathcal W$-valued $b\colon M\otimes_{\mathcal
  O_X}M\to\mathcal W$, where taking stalks / local rings recovers the
  arithmetic theory, or manifolds with bundles $E\to X$ assembling the
  local $(V,b_V)$ continuously/smoothly — symplectic manifolds as the
  geometric instance of a nondegenerate alternating $b$ on $TX$, etc.

* **Analytic theory:** functional analysis, $L^p$/Hardy spaces,
  (partial) differential operators, Banach/Hilbert $R$-modules
  $(L^2(\mathbb R),\int)$, $b(f,g)=\int fg$, where
  $b(v,w)=\langle v,Aw\rangle$ is Riesz with $A$ bounded / self-adjoint /
  Hilbert-Schmidt / Fredholm / elliptic and the double sum is $L^2$-convergent,
  not finite.

One conjoined general categorical setup — $M\in\mathcal C$ in a closed
symmetric monoidal $\mathcal C$ with $b\colon M\otimes M\to W$ as
$W$-valued $(0,2)$-tensor, self-enrichment, $\Gamma^2_R$, etc. — does all
three at once, and recovers symplectic manifolds as the geometric theory,
Grothendieck–Witt as the arithmetic local, and Riesz theorems as the
analytic. Overfitting to $M=R^{(I)}$ finite, $W=R$ discrete with
$\sum a_iG_{ij}c_j$ finite defers the geometric/analytic extensions that
will be needed anyway and forces a rewrite.

**Standard:** define $b\in\mathbf{Bil}_{R,W}(M)$ once as above for
$W,M\in\mathcal C$ arbitrary; prove the finite free $W=R$ Gram matrix
and the finite-sum evaluation as the *specialization* to
$M=R^n$ discrete, not as the definition. Then ask of every new statement:
does it hold for $\mathrm{QCoh}(X)$, for $L^2(\mathbb R)$ with its
Hilbert topology, and for $M$ not finitely generated? If not, the
statement is overfit.

### `PR-66`: Every definition must be valid in the functional-analytic setting — finite collapse is a Proposition, not a definition, and is why diagrammatic / categorical definitions are preferable

A definition that is correct for $R^n$ ($W^{I\times I}\to\operatorname{Hom}(R^{(I)}\otimes R^{(I)},W)$ is an iso, $x^{\!t}Ay:=\sum_{i,j}x_iG_{ij}y_j$ finite, every $G$ bounded, symmetric $=$ self-adjoint, $\det$ defined on all $G$) need not be correct for $L^2(\mathbb R)$, $\mathrm{QCoh}(X)$, $\mathbf{Sp}$-modules — where $b(f,g)=\int fg$ has no finite $G_{ij}$, no finite $\sum a_iG_{ij}c_j$, and bounded $\neq$ symmetric $\neq$ self-adjoint $\neq$ normal thread apart, $x^{\!t}Ay$ has no $x_i$, and the matrix is replaced by the kernel $K$ with $b(f,g)=\iint f(x)K(x,y)g(y)$ and $K$ is $L^2$ / distribution per summability (Schwartz kernel theorem). All definitions in this book must work at that precision — i.e. as stated they must be equally valid for $L^2(\mathbb R)$ / $C^0$ / $\mathcal S$ / $\mathrm{QCoh}(X)$ / $\mathbf{LMod}_R$ — and when they do collapse in the finite ($I$ finite, $R^n$ discrete, $M$ finitely generated projective) specialization, that collapse is a *Proposition* to be stated with honest hypotheses and either cited or proved, not the definition.

This is why categorical / diagrammatic definitions are preferable when available: $b\colon M\otimes M\to W$ with $b\circ\tau=b$ / $b^{\sharp}\colon M\to\underline{\operatorname{Hom}}(M,W)$ / $\ker(b^{\sharp})$ / $\Gamma^2_R(M)$ are already valid in every closed symmetric monoidal $\mathcal C$ (arithmetic, geometric, analytic) and their $U$-evaluation on $x\otimes y$ recovers the finite $b(x,y)=b(y,x)$ / $\sum a_iG_{ij}c_j$ as a theorem, not a definition; the converse — defining by the finite sum and hoping it generalizes — does not work.

**Banned:** a definition quantified as "$\forall x\in M$, $b(x,y)=b(y,x)$ / $b(x,x)\in2W$ / $M$ free on $E$, $G_{ij}=b(e_i,e_j)$, $b(v,w)=\sum a_iG_{ij}c_j$" that is correct only for $R^n$ / $R^{(I)}$ discrete and is used as the general $W$-valued bilinear on $M\in\mathbf{Bil}_{R,W}$.

**Preferred:** define $b\colon M\otimes_RM\to W$ as $W$-valued $(0,2)$-tensor, $b^{\sharp}$, $\Gamma^2_R$, $\operatorname{Val}(b)$, $N^{\perp}:=\ker(b^{\sharp})$, etc., diagrammatically in a closed symmetric monoidal $\mathcal C$ so that the statement is valid for $L^2(\mathbb R)$ / $\mathrm{QCoh}(X)$ / $\mathbf{LMod}_R$; then prove as a *Proposition* (with hypotheses: $I$ finite, $M\cong R^n$, $M$ finitely generated projective, $W$ discrete, continuity / boundedness): "$\Phi_e\colon W^{I\times I}\xrightarrow{\sim}\operatorname{Hom}_R(R^{(I)}\otimes R^{(I)},W)$ is an iso, every $b$ has a $G_{ij}$, $b(v,w)=\sum a_iG_{ij}c_j$ finite, and $x^{\!t}Ay$ is $b(v,w)=\langle v,Aw\rangle$ with $A$ symmetric $\iff$ self-adjoint," etc. — the finite accident as a theorem, not the definition.

### `PR-67`: Twist is any $\varphi\colon W\to W'$ — $\mathbf{Bil}_R(-)$ is functorial in $W$ — not just $\lambda\in R$ and not just $\lambda\in R^\times$ / $\mathbf{Pic}$

For $R$ commutative, $\mathbf{Bil}_{R,W}$ is functorial in the *value
module* $W\in\mathbf{Mod}_R$: any $R$-linear $\varphi\colon W\to W'$
induces $\varphi_*\colon\mathbf{Bil}_{R,W}\to\mathbf{Bil}_{R,W'}$,
$(M,b\colon M\otimes M\to W)\mapsto(M,\varphi\circ b\colon M\otimes M\to W')$
by post-composition. When $W'=W$, an endomorphism $\varphi\colon W\to W$
induces an endofunctor $\varphi_*$ on $\mathbf{Bil}_{R,W}$; *any*
$\varphi\in\operatorname{End}_R(W)$ defines a twist. The usual
"$\lambda b$" is the specialization $\varphi:=\lambda\cdot_W\colon W\to W$,
$w\mapsto\lambda w$ via the $R$-action $R\to\operatorname{End}_R(W)$ — one
endomorphism among all $\operatorname{End}_R(W)$, and not requiring
$W=R$ or $\lambda$ invertible.

Stating twist as "$\lambda\in R$, $b(\lambda):=\lambda b$ on the same
$M$, $G\mapsto\lambda G$" fixes $W=R$ and a global element $\lambda$ and
hides the functoriality that is already in the type $b\colon M\otimes M\to W$.

Concrete standard — name $\varphi$ and $\varphi_*$:

"::: {#def-twist} **Definition.** For $\varphi\colon W\to W'$ in
$\mathbf{Mod}_R$, put
$\varphi_*\colon\mathbf{Bil}_{R,W}\to\mathbf{Bil}_{R,W'}$,
$\varphi_*(M,b):=(M,\varphi\circ b)$. When $W'=W$, $\varphi_*$ is the
**twist by $\varphi$** of the $W$-valued form. In particular for
$\lambda\in R$, $\varphi:=\lambda\cdot_W$ gives $(M,b)(\lambda):=
(M,\lambda b)$ with $\lambda b:=\varphi\circ b$ and
$G_e(\lambda b)=\lambda G_e(b)$, $(\lambda b)^{\sharp}=\lambda\cdot b^{\sharp}$.
:::"

**Banned:** "For $\lambda\in R$ the twist $b(\lambda)$ of $(M,b)$ is
$\lambda b$ on the same module, $M(\lambda)$, with $\lambda G$ and
$\det(b(\lambda))=\lambda^n\det(b)$" as the *definition* of twist for
$(M,b)\in\mathbf{Bil}_{R,W}$.

**Preferred:** define $\varphi_*$ for any $\varphi\colon W\to W'$ as above;
then note $\lambda\cdot_W$ as the case $\varphi:=\lambda\cdot_W$, and
prove $G_e(\lambda b)=\lambda G_e(b)$ and, only for framed finite free
$M\cong R^n$ with $W=R$, $\det(G_e(\lambda b))=\lambda^n\det(G_e(b))$ as a
*consequence* with hypotheses, not as the definition.

### `PR-68`: Heuristic that makes the generalization obvious — read the type of every parameter as an object, then ask variance

The twist generalization is not a trick to remember — it is forced by
one habit: read every parameter of a definition as an *object* of a
category, then ask how the construction varies functorially in that
parameter. That habit, applied systematically, rediscovers the
generalisations in this document without remembering them.

Timeless heuristics that generalize (use on every new definition):

* **Functoriality in the parameter.** $b\colon M\otimes M\to W$ exhibits
  $W$ as the codomain object $W\in\mathbf{Mod}_R$ of
  $\operatorname{Hom}_R(M\otimes M,W)=\mathbf{Bil}_{R,W}(M)$. Any
  $R$-linear $\varphi\colon W\to W'$ post-composes to
  $\varphi_*\colon\operatorname{Hom}(M\otimes M,W)\to\operatorname{Hom}(M\otimes M,W')$,
  $b\mapsto\varphi\circ b$. So $\mathbf{Bil}_R(-)$ is a functor
  $\mathbf{Mod}_R\to\mathbf{Cat}$ in $W$ by definition — $W\mapsto\mathbf{Bil}_{R,W}$,
  $\varphi\mapsto\varphi_*$ — and a twist is $\varphi_*$ when $W'=W$.

* **Element $\to$ morphism.** "$\lambda\in R$" acting as "$\lambda b(x,y)$"
  is the shadow of the morphism $\varphi:=\lambda\cdot_W\colon W\to W$
  in $\mathbf{Mod}_R$ ($R\to\operatorname{End}_R(W)$). Replace the element
  by the morphism it names; the general is any $\varphi\in\operatorname{End}_R(W)$,
  not just $\lambda\cdot_W$.

* **Variance.** $\mathbf{Bil}_{R,W}(M)=\operatorname{Hom}_R(M\otimes M,W)$ is
  covariant in $W$ (post-composition) and contravariant in $M$
  ($(f\otimes f)^*$), so $W\to W'$ gives $\mathbf{Bil}_W\to\mathbf{Bil}_{W'}$
  and $f\colon M\to N$ gives $\mathbf{Bil}(N)\to\mathbf{Bil}(M)$.

* **Grothendieck construction for the parameter.** The categories
  $\mathbf{Bil}_{R,W}$ assemble to the fibered category
  $\int_{W\in\mathbf{Mod}_R}\mathbf{Bil}_{R,W}$ whose fiber over $W$ is
  $\mathbf{Bil}_{R,W}$ and whose cartesian transport is $\varphi_*$. A
  definition that fixes $W$ and $\lambda$ is the fiber at one $W$ with one
  $\varphi$.

To rediscover a forgotten generalization: re-read the definition as a Hom
in its codomain, list the categories of its parameters ($W\in\mathbf{Mod}_R$,
$M\in\mathbf{Mod}_R$, $b\in\operatorname{Hom}(M\otimes M,W)$), and ask "what
$\operatorname{Hom}$-maps in those categories could act here?" The answer is
forced by type: $W\to W'$ must act by $\varphi\circ b$, $M\to N$ by
$b\circ(f\otimes f)$, and the special $\lambda$ is the single $\varphi$
coming from $R\to\operatorname{End}(W)$.

### `PR-69`: Prose "greatest dimension of a subspace on which $b$ is positive definite" for the hard equations $V\cong P\perp Q\perp\operatorname{rad}(V)$ and $G_e(b)\cong\operatorname{diag}(1^p,-1^q,0^r)$ — Sylvester's law hand-waved as language

"Write $p$ for the greatest dimension of a subspace on which $b$ is
positive definite" looks like a definition by a set-theoretic $\max$,
but the content is the *existence* of an orthogonal decomposition
$V\cong P\perp Q\perp\operatorname{rad}(V)$ in $\mathbf{Bil}_{F,F}$ with
$b_{|P}>0$, $b_{|Q}<0$, and its invariance — Sylvester's law — i.e.
$G_e(b)\cong\operatorname{diag}(1^p,-1^q,0^r)$ for a framed $((V,e),b)$
and $(p,q,r)$ with $p+q+r=n$ as the $\operatorname{GL}_n(F)$-congruence
invariant, with $p=\max\{\dim U\mid b_{|U}>0\}$ *attained* and
$p+q+r=n$. The prose hides that a maximum (not just supremum) exists,
that $p,q$ are well-defined (independent of the $U$ attaining them),
that $p+q+r=n$, and that $(p,q,r)$ classifies $b$ up to isometry — all
of which are the orthogonal diagonalization, not language.

Concrete standard — state the equations, then $p,q,r$ are the normal
form:

"::: {#def-signature} **Definition.** Let $F$ be ordered, $V\in\mathbf{Vect}_F$
finite-dimensional, $b\colon V\otimes V\to F$ symmetric. Put
$\operatorname{rad}(V):=\ker(V\xrightarrow{b^{\sharp}}V^\vee)$,
$r:=\dim_F\operatorname{rad}(V)$. By Sylvester there exists an orthogonal
$V\cong P\perp Q\perp\operatorname{rad}(V)$ with $b_{|P}>0$,
$b_{|Q}<0$; put $p:=\dim_FP$, $q:=\dim_FQ$. Then $p+q+r=\dim_FV$ and
$G_e(b)\cong\operatorname{diag}(1^p,-1^q,0^r)$ for any ordered basis $e$.
The triple $(p,q,r)$ is the **signature** of $b$. In particular
$p=\max\{\dim U\mid b_{|U}>0\}$ and $q=\max\{\dim U\mid b_{|U}<0\}$ are
attained. :::"

**Banned:** the block as stated — "$p$ is the greatest dimension of a
subspace on which $b$ is positive definite" with no $V\cong P\perp
Q\perp\operatorname{rad}$, no $G_e(b)\cong\operatorname{diag}(1^p,-1^q,0^r)$,
no Sylvester.

**Preferred:** define $p,q,r$ via the orthogonal sum and the Gram normal
form as above, with $b_{|P}>0$ / $b_{|Q}<0$ as $R$-submodule conditions,
then note $p,q$ as the attained maxima as a *consequence*.

### `PR-70`: Overly restricted hypotheses to avoid the sup — $F$ ordered, $V$ finite-dimensional, "$\max$" instead of "$\sup$" on $F$ / the flag variety

"Let $F$ be an ordered field and $V$ finite-dimensional, $p:=\max\dim U$
with $b_{|U}>0$" restricts to the case where the invariant is a
*maximum* over subspaces, so it can be stated as "$\max$" with
$p+q+r=n<\infty$ without ever saying "sup." The general
($F$ ordered, $b\colon V\otimes V\to F$ symmetric, $V$ arbitrary
$F$-vector space, possibly infinite-dimensional) is not harder: put

* $p:=\sup\{\dim_FU\mid U\subseteq V,\ b_{|U}>0\}$ and
  $q:=\sup\{\dim_FU\mid b_{|U}<0\}$ as suprema in $\mathbf{Card}$ (or
  $\mathbb N\cup\{\infty\}$ in the countable case), $r:=\dim_F\operatorname{rad}(V)$
  with $\operatorname{rad}(V):=\ker(b^{\sharp})$,

as suprema over the flag variety $\operatorname{Gr}(V)$ of subspaces /
over $F$-points of the variety of $b$-positive flags — i.e. a sup in $F$
with its order topology / on $\mathrm{Fl}(V)$. The signature is
$(p,q,r)\in\mathbf{Card}^3$.

Then the finite-dimensional case is the *remark* that the suprema are
attained and $p+q+r=\dim_FV=n$, so "$\sup$" can be written "$\max$" and
$G_e(b)\cong\operatorname{diag}(1^p,-1^q,0^r)$ via Sylvester; the
definition itself needs no finiteness.

Stating it only for $V$ finite-dimensional and as "$\max$" avoids ever
saying "sup" (in $F$ or on $\mathrm{Fl}(V)$) and lets well-definedness be
the elementary "$\max$ over finitely many dimensions" instead of the
one-line sup that already works generally.

**Banned:** the block as stated with "$F$ ordered, $V$ finite-dimensional,
$p$ is the greatest dimension …" as the *definition* of signature.

**Preferred:** define $(p,q,r)$ via the suprema as above for arbitrary
$V$ (fenced, with $\operatorname{rad}(V)$ via $b^{\sharp}$), then add:
"::: {.Remark} When $\dim_FV=n<\infty$, the suprema are attained, $p$ and
$q$ are the greatest dimensions, $p+q+r=n$, and $G_e(b)\cong\operatorname{diag}
(1^p,-1^q,0^r)$. :::" The finite case as specialization, not the
definition.

### `PR-71`: For any stated result or definition, ask if it can be reasonably extended — if "hypothesis $X$ relaxed, is it that much harder?" is no, do it and recover the special case

For every Definition / Proposition / Theorem as stated, go through all
permutations of its hypotheses and ask: "Is the statement with $X$
relaxed / removed that much harder to state or prove?" If the answer is
no — and it is surprisingly often no — state the general form and
recover the desired specialization as a Remark / Corollary. Choosing the
restricted form to avoid the general sup / infinite-dimensional / $W\neq
R$ / non-free case saves nothing and forces a rewrite when the
geometric / analytic specialization is needed anyway (PR-63, PR-66, PR-70).

This is the general form behind PR-61/PR-63 (free $W=R$ finite $M=R^{(I)}$
discrete vs. $M\in\mathbf{Mod}_R$ arbitrary with $b\colon M\otimes M\to W$),
PR-66/PR-70 ($V$ finite-dimensional ordered $F$ with $\max$ vs. $V$
arbitrary with $\sup$ in $\mathbf{Card}$ / on $\mathrm{Fl}(V)$),
PR-58/60 (no framing vs. framed $((M,e),b)$ with variance clause), and
PR-69 (prose $\max$ vs. hard $V\cong P\perp Q\perp\operatorname{rad}$).

Concrete check — on every new unit, ask explicitly:

* Finite $\to$ arbitrary ($n<\infty$ vs. $I$ arbitrary, $M$ finite free vs.
  $M\in\mathbf{Mod}_R$, $V$ finite-dimensional vs. arbitrary, $\max$ vs.
  $\sup$)?
* $W=R$ vs. $W\in\mathbf{Mod}_R$ varying (PR-37)?
* Free $M=R^{(I)}$ vs. $M$ arbitrary (projective / not free vs. $L^2$)?
* Discrete topology / finite support vs. topological / $L^2$-convergent
  (PR-61/PR-62)?
* $R$ commutative / $2$ invertible vs. general $R$ / $2$ not invertible
  (PR-48)?

If the general $W$-valued $(0,2)$-tensor $b\colon M\otimes M\to W$ as
$R$-module, or the sup $(p,q,r)\in\mathbf{Card}^3$ on $\mathrm{Gr}(V)$,
is one line more and the proof is Sylvester with the same $b^{\sharp}$
/ $\Gamma^2_R$, state the general and add "::: {.Remark} When
$\dim_FV=n<\infty$, this gives $p=\max\ldots$, $p+q+r=n$, and
$G_e(b)\cong\operatorname{diag}(1^p,-1^q,0^r)$. :::" — the special case
desired is recovered without loss.

**Banned:** the block as stated with "$F$ ordered, $V$ finite-dimensional,
$M$ free on $E$, $b$ with values in $R$, $p$ is the greatest dimension …"
as the *definition*, when the sup / $W$-valued / $M$ arbitrary form is
one line more and the same proof works.

**Preferred:** state the general $b\colon M\otimes M\to W$ / $\sup$ /
$M$ arbitrary / $W$ varying form fenced, then the finite $W=R$ / $V$
finite-dimensional / $M=R^n$ / $G_{ij}$ / $\max$ specialization as a
fenced Remark / Corollary that recovers the desired case. Always perform
the permutation check; if not much harder, the general is the definition.

### `PR-72`: Premature specialization as the definition — signature $(p,q,r)$ for $F$ ordered finite-dimensional, and $\operatorname{sig}(L)$ for $L\in\mathbf{Lat}_R$ — and the explicit scope that was owed

The block "`$F$ ordered, $V$ finite-dimensional, $p:=\max\dim U$ with
$b_{|U}>0$" is *sound* for $F$ a field — every field has IBN, so
$\dim_FU$ is well-defined and $\{\dim U\mid b_{|U}>0\}\subseteq
\{0,\dots,n\}$ has a $\max$ — and Sylvester's law makes $(p,q,r)$ an
isometry invariant, so it does define the expected $GW(F)\to\mathbb Z$
(for the fixed ordering, $r:=\dim\operatorname{rad}$) for any ordered
field. It is not ill-typed in its stated scope. What it *is* is a
one-real-place, finite-dimensional, $W=F$ specialization presented as
*the* definition, so it quietly fixes the book to $F=\mathbb Q$ / $\mathbb R$
and cuts off the arithmetic the lattice theory is about.

Concretely:

* **Soundness vs. IBN.** "$\dim$" in the definition assumes IBN for $F$.
  Every field has IBN, so for $F$ a field the $\max$ is well-defined; if
  the same "$\max\dim$" were used for an ordered *ring* $R$ without IBN,
  "$\dim_RU$" would have no referent and $(p,q,r)$ would be ill-defined.
  Soundness as written is exactly the field case.

* **$\operatorname{sig}(L)$ not over $R$.** For $L\in\mathbf{Lat}_R$ ($R$ a
  domain, e.g. $\mathbb Z$, $\mathcal O_K$, $\mathbb Z_p$) the $R$-linear
  $b\colon L\otimes_RL\to R$ has no "$b_{|U}>0$" — $R$ is not ordered.
  The invariant is $\operatorname{sig}(L):=\operatorname{sig}(L\otimes_RF,
  b_F)$ for $F:=\operatorname{Frac}(R)$ via change-of-rings
  $-\otimes_RF\colon\mathbf{Mod}_R\to\mathbf{Vect}_F$, $b_F:=b\otimes_RF
  \colon L_F\otimes_FL_F\to F$ (PR-69/70 with $F$ ordered, $L_F$ finite-
  dimensional where the $\max$ is attained). Writing "$\operatorname{sig}(L)$"
  without the $-\otimes_RF$ is ill-typed.

* **Specialization, not the notion.** As the definition of signature it
  rules out the cases where signature has no meaning and hides the cases
  where it has a *family* of meanings:

  — $F=\mathbb F_q$ ($\operatorname{Frac}(R)=\mathbb F_q$ for
  $R=\mathbb F_q$) is a field but not ordered, so "$b_{|U}>0$" is not
  typed and there is no $(p,q,r)$; $W(\mathbb F_q)$ is detected by
  $\dim\bmod2$ and discriminant in $\mathbb F_q^\times/(\mathbb F_q^\times)^2$
  (Arf when $2=0$), not a signature — correctly ruled out.

  — $F=\mathbb C$ is a field but not ordered, so no $(p,q,r)$;
  $W(\mathbb C)\cong\mathbb Z/2$ via $\dim\bmod2$.

  — $F=\operatorname{Frac}(R)$ for $R=\mathcal O_K$, $K$ a number field,
  has $[K:\mathbb Q]$ real embeddings $\sigma\colon K\hookrightarrow\mathbb R$
  (and complex pairs). The $F$-linear $b_F$ has no single $(p,q,r)$; it
  has a family $(p_\sigma,q_\sigma,r_\sigma)_{\sigma\text{ real}}$ with
  $p_\sigma:=\sup\dim_{K_\sigma}U$ where $\sigma(b)_{|U}>0$ in the ordered
  $K_\sigma\cong\mathbb R$ — i.e. $\operatorname{sig}_\sigma(L):=
  \operatorname{sig}(L\otimes_RK\xrightarrow{\sigma}L\otimes_R\mathbb R)$.
  Lattices over $\mathcal O_K$ are the arithmetic case where signature is a
  vector over the real places.

* **Explicit scope that was owed, and flagging.** The local/arithmetic
  object is $L\in\mathbf{Lat}_R$ for $R$ a Dedekind domain — $\mathbb Z$,
  $\mathbb Z_{(p)}$, $\mathbb Z_p$, $\mathcal O_K$ (often
  $\operatorname{cl}(R)=1$ so $L\cong R^n$ as $R$-module, but the theory must
  not assume it), $R=\mathbb Z_p$, $\mathbb Q_p$, $\mathbb C_p$,
  $\mathbb A_{\mathbb Q,f}$, $\mathbb A_K$, etc. — with $b\colon L\otimes_RL
  \to R$ (or $W$ invertible). For $R=\mathbb Z_p$, $\operatorname{Frac}(R)=
  \mathbb Q_p$ is not ordered, so again no $(p,q,r)$; the $p$-adic
  invariants are rank, discriminant, Hasse. A definition fitted to
  "$\mathbb Z\to\mathbb Q$ plus a little more" ($F$ ordered finite-dimensional
  with $\max$) therefore presents the $\mathbb R$-specialization as if it
  were the notion and lets the book proceed without ever naming the general
  $W$-valued $b\colon M\otimes M\to W$ over a Dedekind $R$, its base changes
  $L\otimes_RF$, $L\otimes_RK_\sigma$, $L\otimes_R\mathbb Q_p$,
  $L\otimes_R\mathbb A$, and the invariants that actually do the work there.
  It should have been flagged at the point of writing as *needs research* /
  *needs generalization* — not as a definition to build on — with the
  explicit note that the arithmetic local theory (arbitrary Dedekind $R$,
  $p$-adic $R$, adeles) requires the sup-on-$\mathrm{Fl}$ / $b^{\sharp}$ /
  $\Gamma^2_R$ setup and a separate treatment of $(p,q,r)$ as the
  $\mathbb R$-fiber of that setup.

**Standard:** in the book's scaffolding and in this `CONTRIBUTING.md`,
state the explicit generalization scope most definitions should be at:

> "Bilinear/quadratic notions are $W$-valued $b\colon M\otimes_RM\to W$
> for $R$ a Dedekind domain (in particular $\mathbb Z$, $\mathcal O_K$,
> $\mathbb Z_p$) and $W\in\mathbf{Mod}_R$ invertible, with
> $M\in\mathbf{Mod}_R$ arbitrary; signature $(p,q,r)$ is the
> $\mathbb R$-fiber $L\mapsto(L\otimes_RF_\sigma,b_{F_\sigma})_{\sigma
> \text{ real}}$ for $F=\operatorname{Frac}(R)$ ordered at $\sigma$,
> $p_\sigma:=\sup\dim_{F_\sigma}U$ on $\mathrm{Gr}(L_{F_\sigma})$, and is
> not defined for $F=\mathbb C$, $\mathbb F_q$, $\mathbb Q_p$."

Then every new definition is reviewed against that scope, and a block that
only does $F$ ordered finite-dimensional with $\max$ is flagged *outside*
the book (GitHub issue with `needs-research`, not a fenced Definition)
until the $R$ Dedekind / $\mathbb Z_p$ / $\mathbb A$ / $W$-varying form is
supplied. The finite $W=R$, $V$ finite-dimensional, $\max$ specialization
is then a fenced Remark / Corollary that recovers the desired case.

**Banned:** the block as stated with "$F$ ordered, $V$ finite-dimensional,
$p$ is the greatest dimension … triple $(p,q,r)$ is the signature" as the
*definition* of signature for $L\in\mathbf{Lat}_R$.

**Preferred:** define $(p,q,r)$ via the suprema on $\mathrm{Gr}(V)$ /
$\mathrm{Fl}(V)$ for $F$ ordered arbitrary $V$ as in PR-70, then add the
fenced scope note above and the flagged `needs-research` for the
Dedekind / $p$-adic / adele generalization; define
$\operatorname{sig}(L):=\operatorname{sig}(L\otimes_R\operatorname{Frac}(R))$
only when $\operatorname{Frac}(R)$ is ordered at the relevant $\sigma$,
with $r:=\dim\operatorname{rad}$ via $b^{\sharp}$, and note that for
$F=\mathbb C$, $\mathbb F_q$, $\mathbb Q_p$ the invariant is not
$(p,q,r)$.

### `PR-64`: Definitions are atomic units — one definition per fenced block, with only rare grouping of tightly related definitions; Lemmas / Propositions / Remarks are never in a Definition block

A fenced `Definition` is an atomic unit with one logical status: it
introduces one notion (or one tightly related family, e.g. the four
flavours symmetric / skew / alternating / even via the same
$b\colon M\otimes M\to W$, $\tau$, $\Delta$, $\Gamma^2$). Grouping
several *related* definitions in one block is the rare exception and
requires each to be clearly enumerated as a definition. A Lemma,
Proposition, Theorem, or Remark is never in that block — not even as a
trailing sentence.

This is the explicit form of DEF-15/DEF-19 and SEC-6 (one notion per
fenced block, skeleton complete after deleting glue): a Definition block
defines; implications between defined subobjects ($\operatorname{Alt}\subseteq
\operatorname{Skew}$, converse when $2$ injective), obstructions
($2_*$ / $\gamma^*$), and side observations ("when $2W=W$ every $b$ is
even") are separate fenced `Lemma` / `Proposition` / `Remark` blocks
with quantified hypotheses and proofs, even when the material is "not
hard to prove — but that does not give license to hand-wave it" (PR-48).

**Banned:** `::: {#def-form-axioms} For b: … - b symmetric if …; …;
Alternating forms are skew-symmetric. The converse holds when 2 injective.
When 2W=W, every b satisfies …; quadratic refinements retain … :::`
— four definitions plus a Lemma plus a Proposition plus a Remark in one
`Definition`.

**Preferred:** `::: {#def-symmetric} b is symmetric if $b\circ\tau=b$ :::`
(and similarly for skew / alternating / even, either as four fenced
`Definition`s or as one fenced `Definition` that clearly enumerates the
four related definitions), then separate
`::: {#lem-alt-skew} Lemma. AltBil⊆SkewBil. Proof. … :::`,
`::: {#prop-skew-alt} Proposition. Skew=Alt iff 2:W↪W injective. … :::`,
`::: {.Remark} When 2W=W the element condition is vacuous; the content
is the fiber of γ^* … :::` — one status per block.

### `PR-65`: A free-floating "`**Remark.**` … $G_e(b)=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ … $b(e_1+e_2,e_1+e_2)=2$" with no claim has almost no epistemic status and is not self-contained

A fenced unit has epistemic status only as an instance or counterexample
*to* a quantified proposition. The block as written gives data
$((\mathbb Z^2,e),b)$ with $G_e(b)=\begin{pmatrix}0&1\\1&0\end{pmatrix}$
and computes $b(e_i,e_i)=0$ ($G_{ii}=0$) and $b(e_1+e_2,e_1+e_2)=2$, but
states no universal it exemplifies — not "there exists $b$ symmetric with
$G_{ii}=0$ but $b\notin\operatorname{AltBil}$," not "vanishing on a basis
does not imply $b\circ\Delta=0$," not
"$\{b\mid\forall i\,b(e_i,e_i)=0\}\not\subseteq\operatorname{AltBil}$ as
$R$-submodules" — so deleting it leaves the skeleton unchanged (SEC-6) and
meeting it alone a reader cannot tell why the calculation is being done or
what it shows.

It is also not self-contained: a self-contained `Example` states what it
is an example *of*, why the calculation is done, and what it shows,
without external prose. And it repeats the $((M,e),b)$ vs. $(M,b)$
conflation (PR-58/60): "$\operatorname{Gram}$" with no $e$, "$\mathbb Z^2$
with Gram matrix …" instead of "$((\mathbb Z^2,e),b)$ with
$G_e(b)=\dots$," and "$b(e_1+e_2,e_1+e_2)=2$" as the $U$-evaluation of
$b\circ\Delta\neq0$ instead of "$b\notin\operatorname{AltBil}$."

Concrete standard — fenced, labelled, with the quantified claim and its
negated containment made explicit:

"::: {#exm-U-not-alternating} **Example.** Vanishing on a basis does not
imply alternating. Let $e=(e_1,e_2)\colon\mathbb Z^2\xrightarrow{\sim}
\mathbb Z^2$ be the standard ordered basis and put
$G_e(b):=\begin{pmatrix}0&1\\1&0\end{pmatrix}=e^*b\in M_2(\mathbb Z)$ for
$b\colon\mathbb Z^2\otimes\mathbb Z^2\to\mathbb Z$. Then $b$ is symmetric
($b\circ\tau=b$) with $G_{ii}=b(e_i,e_i)=0$ for $i=1,2$, but
$b\notin\operatorname{AltBil}_{\mathbb Z,\mathbb Z}(\mathbb Z^2)$ since
$(b\circ\Delta)(e_1+e_2)=b(e_1+e_2,e_1+e_2)=2\neq0$. Hence
$\{b\mid\forall i\,b(e_i,e_i)=0\}\not\subseteq\operatorname{AltBil}$ as
$R$-submodules. :::"

A `Remark` is secondary pedagogy *after* the primary Definition/Lemma/
Proposition/Example it remarks on, not a primary Example smuggled as a
bold-`Remark.` sentence.

**Banned:** "`**Remark.**` The symmetric form on $\mathbb Z^2$ with Gram
matrix $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ has vanishing diagonal and
$b(e_1+e_2,e_1+e_2)=2$."

**Preferred:** the fenced `Example` above — names $((\mathbb Z^2,e),b)$ and
$G_e(b)$, states the quantified universal it refutes, shows
$b\notin\operatorname{AltBil}$ via $b\circ\Delta$, and is self-contained.

### `PR-48`: Mixing a Lemma / Proposition / Remark about $\operatorname{Alt}\Rightarrow\operatorname{Skew}$ and $2$-obstructions into the definition block

"Alternating $\Rightarrow$ skew" is not a definition and not a comment —
it is a Lemma ($\operatorname{AltBil}\subseteq\operatorname{SkewBil}$ as
$R$-submodules, proved from $\tau$ and $\Delta$: $b\circ\Delta=0\Rightarrow
b\circ\tau=-b$ via $b(x+y,x+y)$). "Converse holds when $2$ injective on
$W$" and "when $2W=W$ every $b$ is even; quadratic refinements retain
…" are a more nuanced Proposition / Remark about the map induced by
$2\colon W\to W$ and its obstruction to being iso — each warrants its
own fenced block with quantified hypothesis and proof, not two sentences
appended to `{#def-form-axioms}`.

This is the general form of DEF-15/DEF-19 and SEC-6: one fenced block per
notion with one logical status. A Definition block defines; implications
between defined subobjects are Lemmas/Propositions with proofs; side
observations are Remarks.

Concrete standard — define the four named $R$-submodules once, then
containments are $R$-submodule inclusions and the $2$-discussion is a map
between named objects:

* **Scaffolding (once, fenced):**
  $\operatorname{Bil}_{R,W}(M):=\operatorname{Hom}_R(M\otimes_RM,W)$ as
  $R$-module. Put
  $\operatorname{SymBil}_{R,W}(M):=\ker(\tau^*-\mathrm{id})$,
  $\operatorname{SkewBil}_{R,W}(M):=\ker(\tau^*+\mathrm{id})$,
  $\operatorname{AltBil}_{R,W}(M):=\ker(\Delta^*)$,
  $\operatorname{EvBil}_{R,W}(M):=
  \operatorname{im}(\operatorname{Hom}_R(\operatorname{Sym}^2_R(M),W)\to
  \operatorname{Bil})$ (i.e. image of
  $\operatorname{Hom}_R(\Gamma^2_R(M),W)\xrightarrow{\gamma^*}\operatorname{Bil}$
  for the even lift), all $R$-submodules of $\operatorname{Bil}_{R,W}(M)$
  via $b\mapsto b\circ\tau$, $b\mapsto b\circ\Delta$.

* **Then, separate fenced units:**
  "::: {#lem-alt-skew} **Lemma.** $\operatorname{AltBil}_{R,W}(M)
  \subseteq\operatorname{SkewBil}_{R,W}(M)$ as $R$-submodules. *Proof.*
  … :::"
  "::: {#prop-skew-alt} **Proposition.** The $R$-linear
  $2_*\colon\operatorname{Bil}_{R,W}(M)\to\operatorname{Bil}_{R,W}(M)$,
  $(2_*b)(x,y)=2b(x,y)$ induced by $2\colon W\to W$, controls the converse:
  $\operatorname{SkewBil}=\operatorname{AltBil}$ iff $2\colon W\to W$ is
  injective; the obstruction to
  $\operatorname{EvBil}\xrightarrow{\sim}\operatorname{Bil}$ is
  $\ker/\operatorname{coker}(2_*)$. In particular if $2W=W$ then every
  $b$ is even as an element condition, but the quadratic refinement
  $\operatorname{Quad}_{R,W}(M)=\operatorname{Hom}_R(\Gamma^2_R(M),W)$
  retains information via $\gamma^*$. :::"

  No Lemma/Proposition inside the Definition; no "Alternating forms are
  skew" as a comment.

**Banned:** the three sentences appended to `{#def-form-axioms}` — neither
fenced nor proved, with no named $\operatorname{AltBil}$ /
$\operatorname{SkewBil}$ / $\operatorname{EvBil}$ or $2_*$ to refer to.

**Preferred:** keep `{#def-form-axioms}` to the four diagrammatic
definitions $b\circ\tau=b$ / $b\circ\tau=-b$ / $b\circ\Delta=0$ / lift
through $\Gamma^2$; then separate `Lemma` for
$\operatorname{Alt}\subseteq\operatorname{Skew}$ and `Proposition/Remark`
for the $2$-obstruction with the named $R$-submodules and the map
$2_*$ between named objects.

### `PR-49`: Pithy prose that avoids naming $\operatorname{Bil}^{ev}$, $\operatorname{AltBil}$, $\operatorname{SkewBil}$, $\operatorname{SymBil}$ and the map $2_*$ between them, and restates $b\colon M\times M\to W$ instead of $b\in\operatorname{Bil}$

Once $\operatorname{Bil}_{R,W}(M):=\operatorname{Hom}_R(M\otimes_RM,W)$ is
named, membership $b\in\operatorname{Bil}_{R,W}(M)$ *is* the signature
$b\colon M\otimes_RM\to W$ — no "$b\colon M\times M\to W$" to restate.
More generally, definitions should state objects and $R$-submodule
containments, not signatures. Pithy prose "Alternating forms are skew;
converse holds when $2$ injective; when $2W=W$ every $b$ is even"
avoids ever naming
$\operatorname{AltBil}_{R,W}(M)$, $\operatorname{SkewBil}_{R,W}(M)$,
$\operatorname{SymBil}_{R,W}(M)$, $\operatorname{EvBil}_{R,W}(M)$ and the
$R$-linear $2_*\colon\operatorname{Bil}\to\operatorname{Bil}$
(resp. $\operatorname{Hom}_R(\Gamma^2,W)\xrightarrow{\gamma^*}
\operatorname{Bil}$) induced by $2\colon W\to W$, whose (non-)isomorphism
is the actual content. The categorical definitions are then phrased as
$R$-submodule isomorphisms/equalities of those named objects, not as
element conditions on an unwrapped $b$.

This is the general form of PR-40/PR-45 and PR-30: eliding the governing
object that would make the statement checkable, so hand-waving can occupy
its place.

**Banned:** "For $b\colon M\times M\to W$: $b$ is symmetric if …;
Alternating forms are skew-symmetric. The converse holds when $2$
injective …" with no named $\operatorname{AltBil}$ / $\operatorname{SkewBil}$
/ $\operatorname{EvBil}$ and no $2_*$.

**Preferred:** "Let $b\in\operatorname{Bil}_{R,W}(M)$. $b$ is
**symmetric** if $b\in\operatorname{SymBil}_{R,W}(M)$ ($b\circ\tau=b$),
**skew** if $b\in\operatorname{SkewBil}_{R,W}(M)$, **alternating** if
$b\in\operatorname{AltBil}_{R,W}(M)$, **even** if
$b\in\operatorname{EvBil}_{R,W}(M)$." Then
"$\operatorname{AltBil}\subseteq\operatorname{SkewBil}\subseteq\operatorname{Bil}$
as $R$-submodules; $2_*$ induces …; $\operatorname{EvBil}= \operatorname{Bil}$
iff …" — objects and containments, not signatures and element formulas.

### `PR-41`: "Pullback … defines a presheaf $\mathbf{Mod}_R^{\mathrm{op}}\to\mathbf{Mod}_R$" is incoherent — pullback is not a presheaf, and one $f^*$ is not a functor

Unwrapping the abstract $(f\otimes f)^*$ as $f^*b(x,y)=b(fx,fy)$ is
pedagogically fine *after* the Hom is defined (PR-39/PR-40) — the
incoherence is not the element formula but the clause that the
pullback/formula "defines a presheaf."

* **Pullback** is a limit of $A\to C\leftarrow B$ in $\mathcal C$,
  $A\times_C B$, or as an operation the functor
  $f^*\colon\mathcal C_{/Y}\to\mathcal C_{/X}$ for $f\colon X\to Y$
  (more generally $\operatorname{Span}(\mathcal C)\to\mathcal C$). It is
  not a functor $\mathcal C^{\mathrm{op}}\to\mathbf{Set}$.

* **Presheaf** on $\mathcal C$ is a functor
  $\mathcal C^{\mathrm{op}}\to\mathbf{Set}$ (stably $\to\mathcal S$);
  $\mathcal C^{\mathrm{op}}\to\mathbf{Mod}_R$ is an
  $\mathbf{Mod}_R$-valued / $\mathbf{Mod}_R$-enriched presheaf via
  {#thm-mod-closed} (TERM-10). A limit / slice functor cannot be a
  presheaf — types do not match — and a single
  $f^*b(x,y)=b(fx,fy)$ for one $f$ cannot be a functor
  $\mathbf{Mod}_R^{\mathrm{op}}\to\mathbf{Set}$ / $\to\mathbf{Mod}_R$.

What is intended is the functoriality already in the Hom:
$M\mapsto\operatorname{Bil}_{R,W}(M)$ with
$(f\colon M\to N)\mapsto (f\otimes f)^*$. The element formula is the
unwrapping of that $(f\otimes f)^*$, not its definition.

Concrete standards [@Stacks-04E9, Tag 04E9; Lurie HTT 6.1] — state the
functor data explicitly, with types, domains, codomains, and referents:

**Banned:** "Pullback along $f\colon M\to N$ sends $b$ to
$f^*b(x,y)=b(fx,fy)$, and defines a presheaf
$\operatorname{Bil}_{R,W}\colon(R\text{-}\mathbf{Mod})^{\mathrm{op}}\to
R\text{-}\mathbf{Mod}$."

**Preferred:** "Put $\operatorname{Bil}_{R,W}(M):=
\operatorname{Hom}_R(M\otimes_R M,W)$ as $R$-module. For $f\colon M\to N$
in $\mathbf{Mod}_R$, put $f^*:=(f\otimes f)^*\colon
\operatorname{Bil}_{R,W}(N)\to\operatorname{Bil}_{R,W}(M)$. As a
functor $\mathbf{Mod}_R^{\mathrm{op}}\to\mathbf{Mod}_R$
($\mathbf{Mod}_R$-valued presheaf via {#thm-mod-closed}) it satisfies
$\mathrm{id}^*=\mathrm{id}$ and $(g\circ f)^*=f^*\circ g^*$ by Hom. On
elements, $(f^*b)(x,y)=b(f(x),f(y))$." Name on objects, on morphisms with
domain/codomain, and the element unwrapping; do not say a pullback or a
single $f^*$ "defines" the presheaf/functor.

### `PR-42`: Hand-waving a functor without naming types, domains, codomains, and referents

The general form behind PR-41, PR-30/PR-31, PR-37, and SYM-4–11: a
sentence that says a construction "defines a …" while naming no object
assignment, no morphism assignment with domain/codomain, no variance, no
enrichment, and no referent for each symbol ($b\in\operatorname{Bil}(N)$
vs. $f^*b\in\operatorname{Bil}(M)$, $f\colon M\to N$ in which
$\mathcal C$). The same device as "with its hypotheses" occupying the
hypothesis slot while stating none — here occupying the functor-data slot
while stating only one element formula.

Every functor $\mathcal C^{\mathrm{op}}\to\mathcal D$ owes, fenced where
it is introduced: (i) on objects $M\mapsto F(M)$ with its type in
$\mathcal D$, (ii) on morphisms $(f\colon M\to N)\mapsto F(f)\colon
F(N)\to F(M)$ with domain/codomain, (iii) element formula if
pedagogically useful as unwrapping of (ii), (iv) $\mathrm{id}$ and
composition. "Defines a presheaf/functor" with only (iii) for one $f$
does not define it.

**Banned:** any "…defines a presheaf/functor $\mathcal C^{\mathrm{op}}\to
\mathcal D$" with only an element formula and no object/morphism
assignments with types.

**Preferred:** as in PR-41 — state (i)–(iv) with types; reserve
"presheaf" for $\mathcal C^{\mathrm{op}}\to\mathbf{Set}$ ($\to\mathcal S$
stably) and otherwise say "$\mathbf{Mod}_R$-valued presheaf" / "functor
$\mathbf{Mod}_R^{\mathrm{op}}\to\mathbf{Mod}_R$" with the enrichment
from {#thm-mod-closed} named when needed.

## Contributing to this document

When reading the corpus, audit for new instances of the general patterns
below and always mint general policies grounded in examples that illustrate
them. Extremely importantly, every corrected example stored in this document
must be grounded in a standard pattern — a formulation, structure,
rhetorical device, or convention — found by reading actual textbooks and
papers, e.g. in Zotero. Do not invent the preferred form from memory; read
the standard source and transcribe from it.

The universal themes seen in slop writing, based on this session and the
contributing document, are:

**1. Truncated ontology where the modern is derived/spectral.** Rings for
$\mathbb{E}_\infty$-ring spectra, modules for module spectra, categories
for $\infty$-categories, $K_0$ as group completion for $\pi_0 K(S)$, $K_0$
as a ring for $K(S)$ as an $\mathbb{E}_\infty$-ring spectrum (DEF-10,
DEF-13, DEF-8, DEF-9, DEF-14, SEC-6). Anchoring in a superseded framework
(1970s group completion vs $S_\bullet$ and Zakharevich/Campbell) and
working truncated without marking $\pi_0 HR$ or $H(\pi_0R)$.

**2. Prose paraphrase of a precise categorical statement** (PR-15 general
pattern). Vague English — "is an invariant of isomorphism classes," "is
functorial for …," "relating $\gamma$ to $\alpha$," "commuting with the
projections," "is what licenses $a_1\otimes\cdots\otimes a_n$," "is
additional data / does not follow from notation" — for a precise
factorization through $\pi_0$, a functor
$\mathbf{SymMonCat}\to\mathbf{Spectra}$, a hexagon diagram, a tuple
$(\mathcal{C},\otimes,\mathbf{1},\alpha,\lambda,\varrho)$, or a moduli of
equivalences ($\mathbf{LMod}_R\simeq\mathbf{RMod}_R$ as an invertible
bimodule). Wordier and less precise than the statement; names no domain,
codomain, or diagram.

**3. Binding, scoping, and notation.** Symbols used without being bound —
stating a type "symmetric monoidal category" does not bind $\otimes$; the
tuple does (SYM-1, SEC header). Overloaded $1$ for terminal object and
$\operatorname{id}$, maps without $\operatorname{dom}/\operatorname{cod}$,
symbols introduced after use in a "where" clause, $R^{(I)}$ invented
without the free functor $F\colon\mathbf{Sets}\to\mathbf{LMod}_R$
($F(I)=\bigoplus_I R$, not $R^I$), inconsistent
$A\text{-}\mathbf{Mod}$ vs $B^{\mathrm{op}}\text{-}\mathbf{Mod}$, and
strict $A=A^{\mathrm{op}}$ for the canonical $A\simeq A^{\mathrm{op}}$
of tuples (SYM-4–11, SYM-13, DEF-23, SYM-12 for $\otimes_A$ vs
$\otimes_A^L$, MA-14 for $M\times M\to W$ "bilinear" vs $M\otimes_A M\to
W$).

**4. Structural and scaffolding failures.** One block for many notions with
mixed logical status — unconditional replete full subcategories,
integral-domain-conditional torsion, and a meta-remark about general
rings — instead of one notion per fenced block (DEF-15, DEF-19, DEF-1);
reminder masquerading as definition that merely assigns notation
$A\text{-}\mathbf{Mod}$ without constructing $\mathbf{LMod}_R$ (DEF-17);
category defined pointwise by objects $(M,e)$ and
$\operatorname{Bas}_I(M)$ without morphisms or forgetful functors to
$\mathbf{LMod}_R/\mathbf{Sets}$ (DEF-25); missing scaffolding — free
functor before basis, generating family before freeness,
$\operatorname{Ann}_R(m)$ before torsion (DEF-23, MA-15); sections with no
fenced unit, arbitrary breaking that inverts dependency, and sections
that are entirely remarks with no primary unit to remark on (SEC-1–7).
The skeleton — fenced units with proofs — must be complete after deleting
glue; remarks are secondary pedagogy.

**5. Terminological slippage and characterization as definition.** Coinage
with no referent — "value module," "torsion theory," "homomorphism" for
"morphism/map in $\mathbf{CAlg}$," "carries," "data," "identifies
conventions" (TERM-2–4, EV-6, PR-20); compound terms by bullet order
("finitely generated projective: both conditions hold," DEF-21); "some
$R^n\twoheadrightarrow M$ is surjective" for $\exists$ (PR-22);
presenting a characteristic equivalence as the definition — projective as
direct summand of free instead of the lifting property, with
"$\text{direct summand iff projective}$" as a theorem (DEF-22).

**6. Rhetorical slop.** Manufactured negative parallelism — "their mere
existence supplies no order relation," "$a=b$ is a theorem, never a
definitional identity" (PR-2) — contentless because existence never
supplies structure unless defined, and patronizing strawman negation —
"does not follow merely from notation," "is additional data" negating a
premise no one held, with corrective dialectic for an audience that
already distinguishes $\mathbb{E}_1$ from $\mathbb{E}_\infty$ and
$\mathbf{LMod}_R$ from $\mathbf{RMod}_R$ (PR-16–18).

**7. Specialization with no new claim, and meta-requirement for a
theorem.** A general construction $B\otimes_A^L-$ already defined; its
specialization at $\mathbb Z\to\mathbb Z_p$ with no new definition,
theorem, or computation restates the definiens on objects and contributes
no fenced unit (SEC-8). Likewise, "a conclusion about $L$ from either
image requires a stated descent theorem with its hypotheses" says a
theorem must exist instead of stating it, with unquantified "a
conclusion" / "either image" and no hypothesis list (PR-28, PR-29); the
correct form states fpqc descent / Beauville–Laszlo with faithfully flat
/ finitely presented hypotheses, then applies it — and notes that one
image alone never suffices, only the compatible pair with gluing.

**8. Indefinite referent, tautological qualifier, and doctrine posing as
content.** "A conclusion" with no proposition is unfalsifiable (PR-30);
"with its hypotheses" is true of every theorem and adds no hypothesis
list, so it does no work (PR-31); together they are internal governance
leaking into the book — runtime control whose only coherent audience is
contributors/agents, not the mathematical reader, with a preemptive,
condescending tone that assumes the reader was about to make a mistake
never committed (PR-32). Standard prose states the theorem with
hypotheses and applies it; it does not tell the reader that a theorem is
required. Governance belongs in `CONTRIBUTING.md`, not in the
mathematical text (cf. PR-24, PR-16–18).

**9. "Are distinct constructions" tautology and "without $H$" vacuity.**
Two functors defined differently are distinct by definition, with or
without any hypothesis; the substantive claim is whether the canonical
comparison map $c_M\colon M\otimes^L\mathbb Z_p\to\widehat M_p$ is an
equivalence (PR-33). "Without the finite-generation hypothesis, $A$ and
$B$ are distinct" is true of every theorem $H\Rightarrow A\simeq B$ and
says nothing, with unquantified $H$ (finitely generated vs. presented
vs. perfect) and no map or counterexample (PR-34, PR-33). State the
quantified theorem ($c_M$ an iso for perfect $M$) and the quantified
failure with a counterexample ($\bigoplus_{\mathbb N}\mathbb Z$,
$\mathbb Q$), not that the definitions are distinct. Once the distinct
definitions and the positive theorem are stated, the complement without
$H$ is implicit and obvious and needs no separate sentence (PR-35).

**10. Negative framing as bloat, tone, and structural defect.** Every
"is not," "does not follow," "without $H$ distinct," "requires a
theorem with hypotheses," "mere existence supplies no …" is a negative
standing for a positive Definition/Theorem not stated (PR-36, general
form of PR-2, PR-16–18, PR-24, PR-28, PR-30–35, SEC-8). Each doubles the
text (infinitely many true negatives per positive theorem), assumes a
reader mistake never made and scolds preemptively instead of addressing
an equal, and contributes no fenced unit with a named map and quantified
$H$ — hiding that the actual proof obligation was not met. Standard
exposition is positive: definitions as tuples, theorems as quantified
implications with the comparison map, proofs, then boundary
counterexamples when they teach.

**11. Sign-posting that fixes variables for "below."** "Fix $R$ and $W$,
the value module of the forms below" is not a unit; it holds variables
outside any fenced Definition and forward-references an unspecified
"below," with a single fixed $W$ where $W$ must vary over
$\mathbf{LMod}_R$ as the codomain $b\colon M\otimes_R M\to W$ (PR-37,
TERM-9). Correct is quantified fenced units — "Let $R$ be …, let
$W,M\in\mathbf{LMod}_R$; a $W$-valued bilinear form is
$b\colon M\otimes_R M\to W$" — or a section header that quantifies $R$
once while $W$ varies; the skeleton is then complete after deleting
glue.

**12. Tautological "with pointwise operations" for the canonical
enrichment.** "With pointwise operations" / "with its $R$-module
structure via $W$" does zero work: for commutative $R$,
$\mathbf{Mod}_R$ is closed symmetric monoidal and self-enriched, so
$\operatorname{Hom}_R(M,N)\in\mathbf{Mod}_R$ is the internal hom, full
stop (PR-38); $\operatorname{Bil}_{R,W}(M)=\operatorname{Hom}_R(M\otimes_R
M,W)$ already is the $R$-module. The clause mislocates the structure in
$W$ and restates what the ambient enrichment already gives. Put the
closed structure once as fenced scaffolding in the module-theory setup
and every later "with pointwise operations" is obviated.

**13. Hom notation vs. prose paraphrase, and tensor product as
scaffolding.** "The $R$-module of $R$-bilinear maps $M\times M\to W$,
with pointwise operations" is prose for one symbol that already is that
$R$-module with its structure — $\operatorname{Hom}_R(M\otimes_RM,W)$
(PR-39, PR-27 general form). $R$-bilinear $M\times M\to W$ is not
primitive to re-describe each time; it is classified by $M\otimes_RM$
defined once with its universal property $\operatorname{Hom}_R(M\otimes_R
M,W)\cong R\text{-Bil}(M\times M,W)$, and from then on a $W$-valued
form is just $b\colon M\otimes_RM\to W$ (PR-40). Define the tensor
once, then use homs from the tensor to encode bilinearity implicitly.
Calling the resulting functoriality "defines a presheaf
$\mathbf{Mod}_R^{\mathrm{op}}\to\mathbf{Mod}_R$" overloads the generic
name for $\mathbf{Mod}_R^{\mathrm{op}}\to\mathbf{Set}$ and adds no
content beyond "functor" — name the enrichment when needed as
$\mathbf{Mod}_R$-valued / $\mathbf{Mod}_R$-enriched presheaf (TERM-10).

**14. Bare "maps $M\to W$" with no category.** "Maps $q\colon M\to W$"
unqualified in $\mathbf{Mod}_R$ means $R$-linear; a quadratic $q$ is not
$R$-linear — it is a function $U(M)\to U(W)$ in $\mathbf{Set}$ for the
forgetful $U\colon\mathbf{Mod}_R\to\mathbf{Set}$ (TERM-11). The
classifier $\Gamma^2_R$ already gives $\operatorname{Quad}_{R,W}(M):=
\operatorname{Hom}_R(\Gamma^2_R(M),W)$ as $R$-module; never write bare
"maps $M\to W$" or "$M\times M\to W$" once $\otimes$, $\operatorname{Sym}^2$,
$\Gamma^2$ classify the flavour. Name $\mathbf{Set}$ / $U$ when the map
is not $R$-linear.

**15. "Pullback defines a presheaf" type error and hand-waving functor
data.** Pullback is a limit / slice functor, presheaf is
$\mathcal C^{\mathrm{op}}\to\mathbf{Set}$ — types do not match, and one
$f^*b(x,y)=b(fx,fy)$ does not define a functor (PR-41). Every functor
owes on objects with type, on morphisms $(f\colon M\to N)\mapsto
(f\otimes f)^*\colon\operatorname{Bil}(N)\to\operatorname{Bil}(M)$ with
domain/codomain, element unwrapping if useful, and
$\mathrm{id}^*/(g\circ f)^*$ — not "defines a presheaf" with only an
element formula (PR-42). Unwrapping $f^*b(x,y)=b(fx,fy)$ *after* the
Hom is pedagogically fine; the incoherence is claiming that formula
defines the presheaf.

**16. Element-wise $b(x,y)=b(y,x)$ for $b\circ\tau=b$ — concrete shadow
for the categorical diagram.** $b(x,y)=b(y,x)$, $b(x,x)=0$, $q(rx)=r^2q(x)$
as definitions tie the notion to $\mathbf{Set}$-concrete $M$ with
$U(M)$ and hide the single non-lax symmetric monoidal
$(\otimes,1,\tau)$ that makes it portable (PR-43). Standard is the
diagram $b\colon M\otimes_RM\to W$, $b\circ\tau=b$ / $b\circ\tau=-b$ /
$b\circ\Delta=0$ / lift through $\Gamma^2_R(M)$, with element formulas
only as the evaluation on $x\otimes y\colon R\to M\otimes M$ when $U$
exists. "$b$ is even if $b(x,x)\in2W$" collapses the $W$-parameter
abstraction just built for $W$-valued forms to $U(W)$ and "$\in2W$"
(PR-44); even is the lift through $\Gamma^2_R(M)$, and carrying
$b(x,x)\in2W$ everywhere instead of naming $\operatorname{Val}(b)\subseteq
W$ once is local thinking for a global object (PR-45). In general "for
every $x$, a choice of …" is the unwrapping of one global functor /
bundle / section / natural transformation / $R$-submodule; name it once
and "for every $x$" is its evaluation on $U$-points (PR-46). Quantifying
$\forall x\in M$ in the *definition* presupposes $U\colon\mathcal
C\to\mathbf{Set}$ and blocks the one general concept from applying to
$\mathcal O_X\text{-}\mathbf{Mod}$, $\mathbf{Sp}$, stacks, etc., where
no such $U(M)$ exists (PR-47) — the diagram $b\circ\tau=b$ works in every
symmetric monoidal $\mathcal C$, the element formula only in the concrete
ones. A definition is not the minimal element condition that lets the next
paragraph proceed; it is the general building block — $b^{\sharp}$,
$\ker(b^{\sharp})$, $\ker(b\circ\Delta)=0$ — that later theory
($N^{\perp}$, isotropic, anisotropic, $M^\vee$, $D_L$) reuses in every
$\mathcal C$ (PR-53), and that long-term applicability must be written
down or no agent will know it (PR-54).

**17. Mixing Lemma/Proposition into the Definition and not naming the
subobjects and the map $2_*$ between them.** "Alternating $\Rightarrow$
skew" is a Lemma
$\operatorname{AltBil}\subseteq\operatorname{SkewBil}$ as $R$-submodules,
and "converse when $2$ injective" / "when $2W=W$ every $b$ even" is a
Proposition about $2_*\colon\operatorname{Bil}\to\operatorname{Bil}$
induced by $2\colon W\to W$ and its obstruction (PR-48); neither belongs
in the Definition block, which is atomic — one definition per fenced
block, rarely a tightly related family, never a Lemma/Proposition/Remark
(PR-64). Pithy prose avoids naming
$\operatorname{SymBil}$, $\operatorname{SkewBil}$, $\operatorname{AltBil}$,
$\operatorname{EvBil}$ and $2_*$ between named $R$-submodules of
$\operatorname{Bil}_{R,W}(M):=\operatorname{Hom}_R(M\otimes M,W)$, and
restates $b\colon M\times M\to W$ instead of $b\in\operatorname{Bil}$
(PR-49) — definitions as objects and containments, not signatures and
element formulas.

**29. Free-floating Remark with a calculation but no claim has no
epistemic status and is not self-contained.** "`**Remark.**` The symmetric
form on $\mathbb Z^2$ with Gram matrix $\begin{pmatrix}0&1\\1&0\end{pmatrix}$
has vanishing diagonal and $b(e_1+e_2,e_1+e_2)=2$" gives $G_e(b)$ and two
equalities but states no quantified universal it exemplifies — not
"$\exists b$ symmetric with $G_{ii}=0$ but $b\notin\operatorname{AltBil}$"
(PR-65). It is not a Definition, Lemma, or Example, contributes no
fenced unit to the skeleton, and is not self-contained (does not say what
it is an example *of* or what the calculation shows). Standard is a fenced,
labelled `Example` that names $((\mathbb Z^2,e),b)$ and $G_e(b)$, states
"vanishing on a basis does not imply $b\circ\Delta=0$," and shows
$b\notin\operatorname{AltBil}$ via $b\circ\Delta$.

**18. Nominalizing the adjective/verb — "satisfies the evenness
condition."** "Even" is an adjective ($b$ is even,
$b\in\operatorname{EvBil}$); nominalizing to "evenness" + "condition" +
"satisfies" makes one predicate three words with no named subobject to
check (PR-50). Standard is "is even / injective / exact" / "commutes /
factors," with bad/standard pairs: "satisfies the evenness condition"
$\to$ "is even ($\operatorname{EvBil}=\operatorname{Bil}$)"; "satisfies
injectivity" $\to$ "is injective"; "satisfies exactness" $\to$ "is
exact"; "exhibits commutativity" $\to$ "commutes"; "satisfies the
factorization condition" $\to$ "factors through $\Gamma^2$."

**19. "Quadratic refinements retain additional information in the
discriminant setting."** "Refinement" with no named
$\gamma^*\colon\operatorname{Quad}\to\operatorname{Bil}$ has no defined
relation to check (TERM-12); "retain additional information" names no
$R$-submodule, kernel, fiber, or invariant and is not falsifiable
(PR-51); "in the discriminant setting" is not a mathematical object —
the object is the category $\mathbf{TorBil}_{R,W}$ /
$\mathbf{TorQuad}_{R,W}$ of torsion forms, with discriminant object
$D_L:=L^\vee/L$ (TERM-13) — and sign-posting it in the general
$\operatorname{Bil}/\operatorname{Quad}$ section before lattices and
$L^\vee/L$ exist inverts dependency order and violates theory-of-mind.
All three are the weasel mass-noun pattern (PR-52).

**20. Hygiene and foresight — the Set-shadow vs. the categorical
object.** Every "$b(x,y)=b(y,x)$ / $b(x,x)\in2W$ / $\{x\mid b(x,N)=0\}$ /
$b$ satisfies the evenness condition / pullback defines a presheaf /
retain additional information / $M=N\oplus N^{\perp}$" in the block is
the same failure: the statement on $U$-points $x\colon1\to M$ instead of
on the named object that classifies it — $b^{\sharp}$, $\ker(b^{\sharp})$,
$\ker(b\circ\Delta)$, $\operatorname{Bil}_{R,W}$, $\operatorname{Val}(b)$,
$\Gamma^2_R$, $\perp$ as biproduct in $\mathbf{Bil}_{R,W}$ vs. $\oplus$
in $R\text{-}\mathbf{Mod}$ (PR-55). Locally correct for $\mathbf{Mod}_R$,
it bypasses the adjoint/dual/orthogonal subtheory, avoids one general
building block ($b^{\sharp}$, $\ker$, $\operatorname{Val}$) that later
theory and every non-concrete $\mathcal C$ would reuse, and trades
applicability tomorrow for the minimal sentence that lets this page
proceed — the opposite of long-term hygiene.

**21. Submodules and set quotients $N\subseteq M$, $M/N$ vs. monos and
cokernels $i\colon N\hookrightarrow M$, $\operatorname{coker}(i)$.** "$N\subseteq
M$ be a submodule" is the $U$-shadow of a mono, "$M/N$" of its cokernel;
the elementwise $\bar b([x],[y])=b(x,y)$ re-spells the universal property
of the cokernel on representatives (PR-56). Stated with $i$ and
$\operatorname{coker}(i)$, the induced $W$-valued form $\bar b$ on the
quotient is the unique factorization of $b$ through
$\pi\otimes\pi$ for $\pi:=\operatorname{coker}(i)$ when $i^*b=0$ —
immediate in $\mathrm{QCoh}(X)$, $\mathbf{LMod}_R$, $\mathbf{Sp}$, sheaves,
where $N\subseteq M$ has no meaning as a subset.

**22. "$N^{\perp}$" alone is not well-defined.** $N^{\perp}$ depends on
the triple $(M,b,i\colon N\hookrightarrow M)$ — ambient, $W$-valued form,
and mono making $N$ a subobject — not on abstract $N$ (PR-57).
$M=U$ with $N_1:=\mathbb Z e$ vs. $N_2:=\mathbb Z(e+f)$ has
$U(N_1)\cong U(N_2)\cong\mathbb Z$ abstractly but
$N_1^{\perp}=N_1\cong\langle0\rangle$ vs.
$N_2^{\perp}=\mathbb Z(e-f)\cong\langle-2\rangle$; same $N\subseteq
\mathbb Z^2$ has $N^{\perp_{b_1}}\neq N^{\perp_{b_2}}$ for
$b_1\neq b_2$ on the same $M$. Write $N^{\perp_b}$ /
$N^{\perp_i}$ / $(i\colon N\hookrightarrow(M,b))^{\perp}\subseteq M$,
never bare "$N^{\perp}$."

**23. $\operatorname{Gram}(b)$ is not a function of $(M,b)$.** $M$ in
$\mathbf{Bil}_{R,W}$ need not be free and has no distinguished basis, so
no $n\times n$ matrix exists; $\operatorname{Gram}(b)$ as $(b(e_i,e_j))$
is $G_e(b)=e^*b$ for a framed $((M,e),b)$ with ordered basis
$e\colon R^n\xrightarrow{\sim}M$, and without $e$ is well-defined only
up to $\operatorname{GL}_n(R)$-congruence $G_{e'}=P^{\!t}G_eP$ (PR-58,
PR-59). Write $G_e(b)$ and $[G_e(b)]$, never "$\operatorname{Gram}(b)$"
for $(M,b)$.

**24. Choosing data in a construction requires the variance clause or the
category that carries the choice.** Any construction that chooses an
ordered basis $e$, generating set $S$, presentation $F_2\to F_1\to X$,
point $x_0$, trivialization, etc., owes either (A) how the result varies
with the choice — well-defined up to $\operatorname{GL}_n$-congruence /
similarity / conjugacy, with invariants independent of the choice — or
(B) the Grothendieck construction whose objects are $(M,e)$ / $(X,F_1\to X)$
/ $(X,x_0)$ on which the construction is a functor, with well-definedness
as the study of its fibers / $\operatorname{GL}_n$-orbits / sections
(PR-60). Without (A) or (B) the construction is ill-defined and its
dependence on the choice unfalsifiable.

**25. Never overfit to free / finite / finitely generated, never assume
discrete topology / finite support, never conflate a $W$-valued
$(0,2)$-tensor with a matrix.** The block "$M$ free on $E$, $b$ with
values in $R$, $G_{ij}=b(e_i,e_j)$, $b(v,w)=\sum a_iG_{ij}c_j$ finite,
every $(G_{ij})$ arises" is the $W=R$, $M=R^{(I)}$ specialization of
$b\in\mathbf{Bil}_{R,W}(M):=\operatorname{Hom}_R(M\otimes M,W)$ as
$W$-valued $(0,2)$-tensor $b_{ij}$ (two down indices, $G_{e'}=P^{\!t}G_eP$
congruence) conflated with a $(1,1)$-tensor $T^i_j$ ($P^{-1}T_eP$
similarity) and with the matrix algebra $M_{I\times I}(W)$ itself
(PR-61). The map $\Phi_e\colon M_{I\times I}(W)\to\operatorname{Hom}_R(M\otimes M,W)$
is an isomorphism only for $M=R^{(I)}$ discrete; its kernel/cokernel are
the well-definedness content, and $(L^2(\mathbb R),\int)$ is a valid
$\mathbb R$-valued bilinear $\mathbb R$-module with no finite $G_{ij}$
and no finite $\sum a_iG_{ij}c_j$.

**26. The double sum smuggles a Riesz theorem and the canonical
$\langle v,w\rangle_0$ on $F=R^{(I)}$; the operator form
$b(v,w)=\langle v,Aw\rangle$ is the honest statement.** "$b(v,w)=\sum
a_iG_{ij}c_j$" as definition assumes
$\Phi_e\colon W^{I\times I}\xrightarrow{\sim}\operatorname{Hom}_R(F\otimes F,W)$
and hides that $F$ already carries $\langle v,w\rangle_0:=\sum a_ic_i$
($\delta_{ij}$) well-defined only for $a_i,c_i$ finitely supported
discrete; for $\widehat F$ / $L^2$ the sum is infinite and convergence
in $R$'s topology / completion is the content (PR-62). Standard is
"$b(v,w)=\langle v,Aw\rangle$ for a unique $A\colon F\to F$ with $A$
self-adjoint / bounded / Hilbert-Schmidt / Fredholm per the
topological hypotheses" — the double sum is the coordinate expansion of
that single operator evaluation.

**27. One setup must do arithmetic local, geometric global, and analytic
at once.** Overfitting to finite free $W=R$ discrete with $\sum
a_iG_{ij}c_j$ finite defers the extensions that will be needed anyway
(PR-63). Always ask if the statement immediately generalizes to
topological modules/algebras, $\mathrm{QCoh}(X)$ / schemes/stacks /
sheaves where stalks recover the arithmetic, and $L^p$ / Hilbert /
Banach with (partial) differential operators — symplectic manifolds as
the geometric, Grothendieck–Witt as the arithmetic local, Riesz theorems
as the analytic instance of the same $b\colon M\otimes M\to W$ in a
closed symmetric monoidal $\mathcal C$.

**28. Every definition must work in the functional-analytic setting;
finite collapse is a Proposition.** A definition correct for $R^n$ with
finite $G_{ij}$ and $\sum a_iG_{ij}c_j$ need not be correct for
$L^2(\mathbb R)$ / $\mathrm{QCoh}(X)$ where no finite $G_{ij}$ and no
finite sum computes $\int fg$, and bounded $\neq$ symmetric $\neq$
self-adjoint $\neq$ normal thread apart (PR-66). Define diagrammatically
($b\colon M\otimes M\to W$, $b^{\sharp}$, $\ker$, $\Gamma^2_R$) so the
statement is valid in every $\mathcal C$; then prove the finite
specialization ($W^{I\times I}\cong\operatorname{Hom}(R^{(I)}\otimes
R^{(I)},W)$, $b(v,w)=\langle v,Aw\rangle$ with $A$ symmetric $\iff$
self-adjoint) as a Proposition with honest hypotheses, not as the
definition. The diagram is preferable because it already is the general
case.

**31. Signature as prose "greatest dimension" vs. hard equations, and
overly restricted $V$ finite-dimensional.** "$p$ is the greatest dimension
of a subspace on which $b$ is positive definite" hand-waves the
orthogonal $V\cong P\perp Q\perp\operatorname{rad}(V)$ and
$G_e(b)\cong\operatorname{diag}(1^p,-1^q,0^r)$ (Sylvester's law) that
makes $p,q,r$ well-defined and isometry-invariant (PR-69). The general
$F$ ordered, $V$ arbitrary, is no harder: $p:=\sup\{\dim U\mid b_{|U}>0\}$,
$q:=\sup\{\dim U\mid b_{|U}<0\}$ in $\mathbf{Card}$ / on
$\mathrm{Gr}(V)$ / $\mathrm{Fl}(V)$, $r:=\dim\operatorname{rad}(V)$,
$(p,q,r)\in\mathbf{Card}^3$ (PR-70); the finite $V$ with "$\max$" and
$p+q+r=n$ is the specialization where the suprema are attained, not the
definition.

**32. Signature is not over $R$; premature specialization to one
ordered $F$ hides the arithmetic scope.** The block as the definition of
signature quietly fixes the book to $F=\mathbb Q$ / $\mathbb R$ (one real
place, $W=F$, $V$ finite-dimensional). In fact $(p,q,r)$ is sound for
$F$ a field (IBN) and defines $GW(F)\to\mathbb Z$, but it is a
specialization: $\operatorname{sig}(L)$ for $L\in\mathbf{Lat}_R$ is
$\operatorname{sig}(L\otimes_R\operatorname{Frac}(R),b_{\operatorname{Frac}(R)})$
when $\operatorname{Frac}(R)$ is ordered at the relevant place, not
$\max\dim_RU$ over $R$; it rules out (correctly) $F=\mathbb F_q$,
$\mathbb C$ where no order exists, and for $R=\mathcal O_K$ it is a
family $(p_\sigma,q_\sigma,r_\sigma)_{\sigma\text{ real}}$ over the real
places $\sigma\colon K\hookrightarrow\mathbb R$, not a single triple.
The local theory belongs over arbitrary Dedekind $R$ ($\mathbb Z$,
$\mathcal O_K$ with $\operatorname{cl}(R)=1$ not assumed, $\mathbb Z_p$,
$\mathbb Q_p$, $\mathbb C_p$, $\mathbb A$) with $b\colon L\otimes_RL\to
W$ $W$-varying — a scope that should be stated explicitly and, when the
$W\neq R$ / $\mathbb Z_p$ / adele form is not yet supplied, flagged as
needs-research outside the book (PR-72).

**32. Always ask if the statement generalizes without much more
difficulty — if not, state the general and recover the special case.**
For every Definition / Proposition, go through all permutations of its
hypotheses ("finite $\to$ arbitrary," "$W=R$ $\to$ $W$ varying," "free
$M=R^{(I)}$ $\to$ $M$ arbitrary," "discrete / finite support $\to$
topological / $L^2$-convergent," "$2$ invertible $\to$ general $R$")
and ask "is it that much harder with $X$ relaxed?" If no, the general
is the definition and the desired special case is a Remark / Corollary
(PR-71) — as with $b\colon M\otimes M\to W$ vs. $M$ free $W=R$ finite,
and $\sup$ vs. $\max$ for signature.

**33. Premature specialization of signature hides the Dedekind /
$p$-adic / adele scope and should be flagged as needs-research.**
The quick "$F$ ordered, $V$ finite-dimensional, $p:=\max\dim U$" as the
definition of signature fixes the book to $F=\mathbb Q$ / $\mathbb R$
and presents the one-real-place specialization as if it were the notion,
when the notion for $L\in\mathbf{Lat}_R$ is
$\operatorname{sig}(L):=\operatorname{sig}(L\otimes_R\operatorname{Frac}(R))$
only when $\operatorname{Frac}(R)$ is ordered, is a family
$(p_\sigma,q_\sigma,r_\sigma)_{\sigma\text{ real}}$ for $R=\mathcal O_K$,
is not defined for $F=\mathbb C$, $\mathbb F_q$, $\mathbb Q_p$ (which
have $\dim\bmod2$ / discriminant / Hasse, not $(p,q,r)$), and belongs
over arbitrary Dedekind $R$ (in particular $\operatorname{cl}(R)=1$ not
assumed), $\mathbb Z_p$, $\mathbb Q_p$, $\mathbb C_p$, $\mathbb A$
(PR-72). State the explicit scope most definitions should be at and flag
a block that only does the ordered-field finite case outside the book
until the $R$ Dedekind / $p$-adic / adele generalization is supplied.

**29. Twist is any $\varphi\colon W\to W'$, not just $\lambda\in R$.**
$\mathbf{Bil}_{R,W}$ is functorial in $W$ — $\varphi\colon W\to W'$
gives $\varphi_*\colon(M,b\colon M\otimes M\to W)\mapsto(M,\varphi\circ
b)$ by post-composition, and a twist is $\varphi_*$ when $W'=W$
(PR-67); $\lambda b$ is the case $\varphi:=\lambda\cdot_W$. State
$\varphi_*$ for any $\varphi$, then note $\lambda\cdot_W$ as a
specialization.

**30. Heuristic: read every parameter as an object and ask variance.**
The twist is forced by reading $W$ as $W\in\mathbf{Mod}_R$ and
$b\in\operatorname{Hom}_R(M\otimes M,W)$ and asking how $\operatorname{Hom}$
varies covariantly in $W$ ($\varphi\circ b$) and contravariantly in $M$
($b\circ(f\otimes f)$) — i.e. replace "$\lambda\in R$" / "$\forall x\in
M$" by the morphisms $\varphi\colon W\to W'$ / $x\colon1\to M$ they
shadow (PR-68). That habit rediscovers $\varphi_*\colon\mathbf{Bil}_W\to
\mathbf{Bil}_{W'}$, $W\mapsto\mathbf{Bil}_{R,W}$ as a fibered category,
and the element $\lambda$ as the single $\varphi:=\lambda\cdot_W$ among
all $\operatorname{End}_R(W)$ without remembering it.
All three are instances of the timeless weasel mass-noun problem:
"information," "data," "setting," "condition," … with no fixed referent,
context-dependent truth where the context is never stated, and no named
$R$-submodule / functor / category to check (PR-52) — audit by those
semantic indicators, not by the word list, which will change.