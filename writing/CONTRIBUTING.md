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

### `SYM-13`: Classical module notation for $\infty$-categorical modules

Classical notation $R\text{-}\mathbf{Mod}$, $R^{(I)}$, and $R^n$ for
modules is the truncation to the heart. The book's default is
$\mathbf{LMod}_R$, $\mathbf{RMod}_R$, ${}_A\mathbf{Bimod}_B$ (or
${}_A\mathbf{BiMod}_B$) for presentable stable $\infty$-categories of
module spectra, and $\bigoplus_{i\in I}R$ (coproduct in
$\mathbf{LMod}_R$) for the free module on a set $I$. $R^{(I)}$ and the
surjection $R^n\twoheadrightarrow M$ are the classical shadows; they are
correct only after truncating to $\pi_0$ or to discrete $R$.

**Banned:** "$R\text{-}\mathbf{Mod}$ for the $\infty$-category;
$R^{(I)}$ for the free module spectrum; $R^n\twoheadrightarrow M$ for an
effective epimorphism in $\mathbf{LMod}_R$ without marking the
truncation."

**Preferred:** "$\mathbf{LMod}_R$ (resp. $\mathbf{RMod}_R$,
${}_A\mathbf{BiMod}_B$) for $\infty$-categories;
$\bigoplus_{i\in I}R\twoheadrightarrow M$ as an effective epimorphism for
finitely generated; $M\simeq\bigoplus_{i\in I}R$ for free." State the
$\infty$-categorical object; note when passage to $\pi_0$ recovers the
classical notation.

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

### `DEF-22`: Characterization presented as definition

A notion is defined by a characterization whose equivalence with the
defining property is a theorem, without stating which is the definition.
"$M$ is a direct summand of a free module" is the theorem "projective
iff retract of free," not the definition. The definition is the lifting
property / $\operatorname{Hom}_R(M,-)$ exact.

Concrete standard: $M\in\mathbf{LMod}_R$ is projective if
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
retract of $\bigoplus_{i\in I}R$ for some set $I$. Similarly, $M$ is
finitely generated if $\operatorname{Hom}_R(M,-)$ preserves filtered
colimits, equivalently the surjection condition above; state the
definition, then cite the characterization as a theorem.

**Banned:** "projective: $M$ is a direct summand of a free module" as the
definition; "finitely generated: some $R^n\twoheadrightarrow M$ is
surjective" as the definition without the generating-set or compactness
formulation.

**Preferred:** define $M$ projective by the lifting property; then
"Theorem: $M$ is projective iff it is a retract of a free module
$\bigoplus_{i\in I}R$." Define $M$ finitely generated by the generating
set; then "iff there exists a finite $I$ and an effective epimorphism
$\bigoplus_{i\in I}R\twoheadrightarrow M$."

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

The fiber $f^{-1}(y)$ is a special case of a fiber product (pullback).
The standard scaffolding defines pullbacks once — the limit of a cospan
$X\xrightarrow{f}Y\xleftarrow{g}Z$ with its universal property via terminal
cones, notation $X\times_Y Z$ — and then recovers the fiber in one
sentence by reference. Defining the fiber as "the apex of the cartesian
square" without first defining fiber products repeats the cone's
universal property that belongs in the general definition and leaves the
general notion undefined.

Concrete standard: define pullbacks as limits of cospans (\ref{def-pullback}):
for $f\colon X\to Y$ and $g\colon Z\to Y$ in an $\infty$-category with
pullbacks, the **pullback** is the limit $X\times_Y Z$ with its cone
$(X\times_Y Z\to X, X\times_Y Z\to Z)$ terminal among cones over the
cospan. Then: "The **fiber** of $f$ over $y\colon1\to Y$ is the pullback
$X\times_Y 1$ of $f$ along $y$ (\ref{def-pullback})."

**Banned:** "Let $\mathcal{C}$ have a terminal object $1$ and the
relevant pullbacks, let $f\colon X\to Y$, and let $y\colon1\to Y$ be a
point. The fiber of $f$ over $y$ is the apex of the cartesian square …"
— defines the special case without the general notion.

**Preferred:** define $X\times_Y Z$ once via terminal cones; then "the
fiber is $X\times_Y 1$, the pullback of $f$ along $y$."

### `PR-27`: "Apex of the cartesian square" for "pullback of $f$ along $y$" or $X\times_Y 1$

"Pullback of $f$ along $y$" and the concise notation $X\times_Y 1$
already encode the universal property. "The apex of the cartesian square"
is a wordy prose paraphrase (PR-15) for the same object that names no
limit and is longer than the notation it paraphrases.

**Banned:** "the fiber of $f$ over $y$ is the apex of the cartesian
square."

**Preferred:** "the fiber of $f$ over $y$ is the pullback of $f$ along
$y$" or "the fiber is $X\times_Y 1$."

### `TERM-7`: "Apex" without definition; standard is terminal cone

"Apex" is not defined in this book. The standard term for the vertex of
a limit cone is the (terminal) cone — the cone
$(P\to X, P\to Z)$ over $X\to Y\leftarrow Z$ that is terminal among
cones. "Apex" alone names no cone and no universal property; it would be
introduced once in the definition of pullbacks as the vertex of the
terminal cone, not repeated in the definition of the fiber.

**Banned:** "the fiber … is the apex of the cartesian square."

**Preferred:** "the fiber is the pullback $X\times_Y 1$ with its terminal
cone $(X\times_Y 1\to X, X\times_Y 1\to1)$."

### `TERM-8`: Colloquial "cartesian square" for pullback square

"Cartesian square" is colloquial for a pullback square and, in the
book's setting, hides a theorem: when a square's projection is a
(co)cartesian fibration and the square is a pullback in
$\mathbf{Cat}_\infty$, the projection is a (co)cartesian fibration. The
precise term is "pullback square," i.e. a square exhibiting a pullback
via its universal property. Use "pullback square," or state the
fibration property as a theorem, not as the name of the square.

**Banned:** "the apex of the cartesian square."

**Preferred:** "the pullback square exhibiting $X\times_Y 1$" or "the
square exhibiting the pullback." Reserve "cartesian fibration" for the
fibration property and prove when a pullback square has that property.

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