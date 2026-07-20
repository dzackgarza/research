# Written Form and Evaluation {#sec-written-form}

The implementation map from written source to the mathematics of the [Framework](../framework/Mathematical-Framework.md): what parses, how a written form reaches its definition, and how evaluated results are labeled.
Everything on this page is implementation register, quarantined per [Style Guide P6](Mathematical-Language-Style-Guide.md#sec-governing-principles); the meanings themselves are owned by the framework pages linked throughout, and nothing here adds to them.

## Source form {#sec-source-form}

Source is linear text admitting Unicode mathematical symbols and designated LaTeX aliases, normalized to one token stream (`ℤ` / `\mathbb{Z}`, `⊗` / `\otimes`, `∈` / `\in`). The stored form is the linear text and is losslessly parseable; a structured editor may render two-dimensionally, but rendering is a view.
Arbitrary TeX is not executable syntax: the executable subset has fixed precedence, associativity, and binder scopes, and whitespace never carries meaning.

## Written forms and their meanings {#sec-written-forms}

Each surface form denotes a framework definition; the map is one-to-one and the right-hand column owns the meaning.

| written form | meaning |
| --- | --- |
| `let x ∈ C` | a generic member of $C$ — an object, element, generalized element, or lift per [Elements and Containment](../framework/Elements-and-Containment.md) |
| `let x ≔ t`, `let x ∈ C ≔ t` | definitional binding ([Identification](../framework/Identification.md#sec-identification)); the membership annotation is optional where determined |
| `let f : X → Y`, `let α : F ⇒ G` | hom- and transformation-membership, in the standard arrow notation |
| `let M ∈ Modules.FinitelyGenerated(R)` | membership in a classifier — a lift through the named $\iota_A$ ([Framework](../framework/Mathematical-Framework.md#sec-axiom-classifiers)) |
| `{ x ∈ C : P(x) }` | the full subcategory of $C$ cut out by $P$ — replete full when $P$ is isomorphism-invariant, ill-formed when it is not, since a non-invariant predicate defines no subcategory ([Presentation Principles](Categorical-Presentation-Principles.md#sec-classifiers)) |
| `N ≤ M`, `A ⊆ B`, `x ∈ X` in formulas | the containment relations of [Elements and Containment](../framework/Elements-and-Containment.md#sec-containment) |
| `=`, `≅`, `≃` | the typed identification claims of [Identification](../framework/Identification.md#sec-identification) |
| $\sum$, $\int$, $\forall$, `x ↦ e` | the standard binders, with grammar-fixed scopes |

There is one introducer: no `assume`, `given`, or `suppose`. A hypothesis is membership in a classifier or a formal proposition; a local setting is a scope block together with the named base-change functor ([Generic Elements](../framework/Generic-Elements.md#sec-localization)). Adjectival declarations ("a field of characteristic $p$", "with $x$ positive") are not grammar; each is written as the membership that carries it.

## Parse shape and meaning {#sec-parse-shape}

Every symbol has exactly one *parse shape* — arity, fixity, precedence, associativity, binder positions — held in a single global registry, independent of context: a line parses identically everywhere.
What a symbol *means* is owned by categories: applied to arguments in a category $\mathcal C$, it denotes the operation $\mathcal C$ declares for it, under the named-lift discipline where the operation is structure ([Style Guide P4](Mathematical-Language-Style-Guide.md#sec-governing-principles)); arguments in different categories resolve at the Meet — their common base ([Distinguished Functors](../framework/Distinguished-Functors.md#sec-resolution-site)). A `with 𝒞:` block makes $\mathcal C$'s declarations locally primary and may rebind a symbol to a named operation; no construct alters a parse shape.
A library whose symbol collides in parse shape with the registry is rejected at load.

Standard notation is primary wherever mathematics has it — $\ker f$, $M \otimes_R N$, $\operatorname{Ext}^n_R(M,N)$, $X \times_S Y$, $\lim F$, arrow declarations — and requests that name a transformation rather than an object use a small fixed command grammar with fixed slots, not interpreted prose:

```text
factor e over R
solve E for x in D
expand e at x = a to order n
approximate e to 100 digits
```

A custom-notation declaration supplies the parse pattern, precedence and associativity, binder positions, the declaring category and operation denoted (a named lift where structure), the rendered form, and conflict behavior.

## Evaluation {#sec-evaluation}

A bare top-level expression is a computational request — an integral, an $\operatorname{Ext}$ group, a kernel, a fiber product is entered as itself.
Evaluation-control forms (forcing, precision, engine selection) exist but are not the default surface.
Four regimes coexist and are distinguished in every displayed result: exact effective computation; exact symbolic computation (possibly conditional or deliberately unevaluated); certified numerical computation with stated precision or enclosure; and formal manipulation of objects with no effective evaluation, which remain valid symbolic objects.
An exact request is never answered by an unmarked approximation, and a symbolic object is never rejected for being symbolic.

Displayed results carry their mathematical content as the framework defines it: undischarged hypotheses ([Generic Elements](../framework/Generic-Elements.md#sec-hypotheses)), the category of evaluation for transported statements ([Distinguished Functors](../framework/Distinguished-Functors.md#sec-statements-vs-constructions)), the stage of a generalized element, the named lift, witness, or convention consumed.

## Documents {#sec-documents}

The same source serves an interactive worksheet and a static, reproducible document with explicit evaluation order.
A document mixes formally delimited mathematical cells, typeset but inert prose, displayed results, and certification metadata; only the delimited cells are interpreted, and prose may explain a computation but never changes its meaning.
The document renders as conventional mathematics — the written forms of @sec-written-forms are already the notation of the rendered page — without exposing implementation representations.

## Status, provenance, and certification {#sec-status}

Every nontrivial result carries a status — exact by normalization; exact under carried hypotheses; certified, with the certifying procedure named; numerical, with its bound; computed without certification; unevaluated; unknown — and provenance sufficient to reproduce it: engine identity, options, and representation used.
No status is silently upgraded.
Stored results are keyed by the normal form of the request together with engine identity, so definitionally equal requests share one record, and storage preserves status: a stored uncertified computation re-served from the fact store is still "computed," with its original provenance, unless a certificate accompanies it.

Certification is separable.
A result may be produced bare; with a machine-checkable certificate; re-checked by a certified procedure; or exported as a formal statement through the routing model of the [Lean–Sage Integration Model](../lean/Lean-Sage-Integration-Model.md#sec-abc-model), where proof-shaped claims acquire formal statements as authority.
The migration from computed to certified proceeds fact by fact and is legible fact by fact through the status machinery; the formal layer consumes the same elaborated objects the computations produce, and nothing is re-entered in a second syntax.
