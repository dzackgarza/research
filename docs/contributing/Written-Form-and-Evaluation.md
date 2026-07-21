# Written form and evaluation {#sec-written-form}

The computational interface accepts the notation below and attaches mathematical status
and provenance to evaluated results. Mathematical meanings refer to their defining
occurrences in the theory chapters.

## Source form {#sec-source-form}

Input is linear Unicode text with designated LaTeX aliases. Equivalent spellings such as
`ℤ` and `\mathbb{Z}`, or `⊗` and `\otimes`, normalize to the same token. The executable
subset has fixed precedence, associativity, and binder scope. Arbitrary TeX is rendered as
notation but is not executable syntax.

## Written forms {#sec-written-forms}

| written form | mathematical meaning |
| --- | --- |
| `let x ∈ C` | an object or generalized element in the specified category |
| `let x ≔ t` | a definitional binding |
| `let f : X → Y` | a morphism in the stated category |
| `let α : F ⇒ G` | a natural transformation between parallel functors |
| `{x ∈ C : P(x)}` | the full subcategory on objects satisfying $P$ |
| `N ≤ M` | a subobject relation represented by a named monomorphism |
| `=`, `≅`, `≃` | equality, isomorphism, and equivalence, respectively |
| $\sum$, $\int$, $\forall$, `x ↦ e` | binders with grammar-defined scope |

A property annotation refers to the replete full subcategory defined by that property.
A chosen structure refers to an object over the given value of its specified forgetful
functor.

## Parse shape and mathematical meaning {#sec-parse-shape}

Each symbol has one parse shape: its arity, fixity, precedence, associativity, and binder
positions. The mathematical operation is selected only after the argument categories are
known. If arguments are compared after functors to a common category, the input names those
functors and that category as required by @sec-comparison-common-target.

Standard notation is used for kernels, tensor products, Ext groups, fiber products,
limits, and morphism declarations. Commands are reserved for computational requests whose
parameters are not normally written as a mathematical expression, for example:

```text
factor e over R
solve E for x in D
expand e at x = a to order n
approximate e to 100 digits
```

## Evaluation {#sec-evaluation}

An expression may produce one of four kinds of result:

- an exact effective value;
- an exact symbolic value, possibly subject to hypotheses;
- a certified numerical value with a stated error bound or enclosure;
- a symbolic object for which no effective evaluation is supplied.

An exact request returns an exact result or an explicit unevaluated status. Numerical
approximations are labelled with their certification status. A result obtained after base
change names the image object and the functor used. Undischarged hypotheses remain part of
the displayed result.

## Documents {#sec-documents}

A document may combine prose, executable mathematical cells, and displayed results.
Evaluation order is explicit. Prose is inert, and only delimited cells are interpreted.

## Status and provenance {#sec-status}

A nontrivial result records whether it is exact, conditional, certified, numerical,
computed without certification, unevaluated, or unknown. Reproducibility data include the
engine, relevant options, and input representation. A certificate names its checking
procedure. Reusing a stored result preserves its original status unless a new certificate
has been checked.
