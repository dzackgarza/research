# Contributing to the book

This is a mathematical book. Contributions are definitions, theorems,
constructions, examples, and remarks written in standard mathematical register.
The book does not describe itself, announce what it is, tell the reader how to
read it, or characterize a notion by contrast with the notion it rejects.

## The writing

Write as a mathematician writes. A definition is a sentence with quantifiers
and conditions: "Let … . We say … iff … ." A theorem states every hypothesis
it uses. A construction names its data, its domain, its codomain, and the
equations its morphisms preserve. A remark explains a real subtlety in context.

State the content. Do not characterize the text. "This is the framework that
situates the conversion" is not mathematics. The specified forgetful functor,
its pullbacks, and the intersections of replete full subcategories are.

Do not write what the book does, what a chapter does, what a section provides,
or what the reader will see. Write the mathematics. Significance is shown by
use, never asserted.

## Definitions

Each mathematical notion has one defining occurrence in the book. Later
chapters cite it. They do not restate it, shadow it with a synonym, or write a
second local definition.

A definition is written in a numbered block:

```markdown
::: {#def-universe}
## Universe and decoded objects

Work in an external cartesian closed $(\infty,\infty)$-category $\mathcal K$
with pullbacks and terminal object $*$.
:::
```

Reference it as `\ref{def-universe}` or `\longref{def-universe}`. Labels use
colon separators. Do not start a label with a Quarto-reserved prefix (`def-`,
`thm-`, `lem-`, `cor-`, `prp-`, `cnj-`, `exm-`, `exr-`, `fig-`, `tbl-`,
`eq-`, `sec-`, `lst-`); use a hyphen instead. Quarto hijacks those prefixes
for its own crossrefs and the render fails.

Read the book's defining occurrence and its prerequisites before writing a
dependent passage. A definition reconstructed from training or an external
source is inadmissible even when it resembles a standard definition. If the
book's definition conflicts with the literature, correct it at the defining
occurrence and repair its dependents; do not shadow it locally.

## Theorem-like environments

The same fenced-div syntax applies to theorems, propositions, lemmas,
corollaries, examples, and remarks. The declared block classes are listed at
the bottom of `writing/.book/_quarto.yml`. Add a class there before using it.

## Cross-references

`\ref` and `\longref` are the only two commands that resolve numbered blocks.
They reach any numbered block in the book, in any chapter, in either
direction.

Do not use `\cref` or `\Cref`. They do not match the resolver. Pandoc drops
an unmatched macro silently, so the reference disappears and the sentence
around it is left dangling.

Sections auto-number. Reference a section by link:
`[Lattice Theory](lattice-theory.md#sec:lattice-theory)`.

Figures use Quarto's own numbering. Anchor a figure `{#fig-x}`, with a hyphen,
and reference it `@fig-x`.

## Citations

Use Better BibTeX keys: `[@OR23, Definition 1.5.1]`. Zotero is the source of
truth. If a work is not in Zotero, add it there first.

Never write a citation as an inline URL to arXiv, a DOI, or nLab. The docs gate
rejects it.

## Diagrams

Draw a universal construction as its square. Label every morphism. Mark it
cartesian or cocartesian. Name the resulting object and structure morphism in
the diagram. The prose may state the universal property after the diagram; it
never replaces the diagram.

Use `tikzcd`. A pullback written only as the apex $A \times_C B$, or a family
named only by its classifying map, is not enough.

Every arrow in a diagram names a functor, natural transformation, or map with
the displayed source and target. A construction defined only on cores is drawn
from the cores. An invariant on isomorphism classes is drawn as a map from
$\pi_0$. Membership of an object in a category is not drawn as a functor
between categories.

## Notation

State the mathematical type of every named entity. Distinguish objects and
morphisms in a specified category, categories and functors, natural
transformations, object properties, chosen structures, invariants, sections,
and obstructions.

Use notation with its typed meaning. Literal equality ($=$), isomorphism
($\cong$), and equivalence ($\simeq$) are written with distinct symbols.
$\hookrightarrow$ denotes a stated inclusion, embedding, or monomorphism;
fullness, faithfulness, and repleteness are asserted separately.

The same symbol has the same type and meaning throughout the book. Project
notation is introduced at the defining occurrence, after the underlying
standard construction has been stated.

Use established names in their standard meanings: category of elements,
Grothendieck construction, core, arrow category, full subcategory, replete,
natural isomorphism, automorphism group, torsor, monoidal category, abelian
category, kernel, cokernel, discriminant form, genus, isometry, classifying
object. Do not coin a name for a notion that already has one.

## Properties and structure

Use the forgetful functor to distinguish properties and structure. For a
specified forgetful functor $U\colon\mathcal S\to\mathcal C$, full
faithfulness gives at most property, faithfulness gives at most structure, and
an arbitrary functor gives at most stuff.

Name every chosen structure. A structure on $X$ is a chosen object in the fiber
of a specified forgetful functor over $X$. When several choices exist, name the
one used by the construction. Do not write "carries" or "carrier" for the data
that constitute a structure; name the operations, relations, and axioms, or
specify the forgetful functor and the chosen object in its fiber.

State every hypothesis. If a construction uses a basis, embedding, section,
presentation, or other witness, name that witness in the construction.

## What does not belong

- Self-narration. "This chapter provides …" is not mathematics.
- Reflexive negative parallelism. "X, not Y" / "is X, never Y" / "not just X
  but Y." State the positive claim and stop.
- Puffery. "crucial", "pivotal", "powerful", "elegant", "deep", "rich",
  "interplay", "seamless", "leverage", "delve", "underscore", "showcase".
  Delete the word; state the content plainly.
- Cadence padding. The reflexive rule of three, "not only … but also",
  formulaic transitions ("Additionally", "Moreover", "Furthermore"),
  conclusion-restatement ("in summary", "as we have seen").
- Project process inside mathematical exposition. Rulings, audit procedure,
  implementation status, and editorial policy do not belong in a mathematical
  chapter.
- Process prose. "It is worth noting", "importantly", "note that", "clearly"
  (where it is not). If removing the phrase removes no information, remove it.
- Bold for emphasis in running prose. Use *italic* for a term at its
  definition. Use **bold** only as a run-in label.
- Title Case in headings. Use sentence case.
- Curly quotes. Use straight quotes.