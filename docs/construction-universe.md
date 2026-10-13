# Preamble construction-universe audit

## Purpose

The preamble has many category families, axiom refinements, objects, elements
and morphisms. Its mathematical construction language is not a finite set of
instances: taking products, forming Mor objects, repeating functors and asking
methods of their results produces potentially unbounded expressions.

**This tool inventories the finite system of construction rules**, with
symbolic parameters and a least fixed point over *type families*. It does not
manufacture sample objects or assume that a passing example certifies a whole
category.

Run from the repository root:

```sh
just construction-universe
```

Open `.tmp/construction-universe.html` in a browser. The generated
`.tmp/construction-universe.json` is the complete machine-readable audit.
Both are reconstructed from the current source on each run. Optional arguments
are `just construction-universe .tmp 8` to increase return tracing depth,
and `just construction-universe docs` to create files under `docs/`.
The static analyzer uses the standard library and the repository's existing
`category_graph`; it does not load Sage or execute the preamble.

## Mathematical model

The underlying structure is a typed directed hypergraph:

- A category-family vertex is one declared category, axiom refinement,
  parameter-dependent category or constructed join, e.g. `Modules`,
  `Modules.FinitelyGenerated`, or a join with two simultaneously held
  placements. An arrow between category vertices is **subcategory inclusion**,
  not a new mathematical construction.

- A type vertex is `category:C`, `object:C`, `element:C` or
  `morphism:C`. They are distinct sorts. Mor objects are not confused with
  the elements (arrows) of those objects.

- An operation is a hyperedge represented by a separate operation vertex.
  Its subject and every required argument are input ports. Its return branches
  are outgoing *result* edges with source expression, lexical conditions,
  category ownership and delegation path. Several source-return alternatives
  are retained rather than arbitrarily choosing one.

- Constructing an object with multiple declared placements yields one join
  object whose membership projects to all of those categories, not multiple
  alternative objects. The source analyzer also follows local category
  lists built with `append` or `extend`, retaining branch predicates.
  In particular, a discriminant module of an even lattice can have a
  quadratic-form placement unavailable to the odd case: those are *two
  conditional join outcomes*, not one unconditional placement.

The closure starts with declared category families and category constructors
(`an_object`, the category's object ingress), adding conditionally constructible
object sorts. Once an object family is reachable its element and identity
morphism sorts are possible. The closure follows inherited operations and
their typed results until its finite *type-family* graph stabilizes.
Parameterized instances are represented by a single symbolic family; this
is not a proof that every parameter admits a constructed object.

The JSON contains `categories`, `rules`, `inclusions`, `edges`,
`closure`, `unresolved`, and `summary`. The graph relations include
`subcategory`, `declares-method`, `subject-input`,
`argument-input`, `result`, `delegates` and
`constructed-join-projection`. The underlying method class and source
line accompany each rule. The HTML offers a category browser, focused
construction graph, all-operations inventory, reachable families and
unresolved source paths.

## Audit interpretation

The manifest states **what the source says and what could be inferred**,
not that every placement is mathematically correct. No rule is certified by
its name: a method called `free_module` does not automatically produce an
object of `FreeModules` unless its constructor/return trace or an explicit
type establishes that.

A method's `result_status` is:

| Status | Meaning |
| --- | --- |
| `classified` | All found return branches have a recognized kind. |
| `partial` | Some branches are classified; others are unresolved. |
| `unresolved` | No return branch has been classified. |

`classified` does **not** mean “proved mathematically correct”: one may
still have a wrong or insufficient category placement. Every unresolved
branch is separately recorded with its original expression, guard and
failure reason. A result labeled `broad-annotation` states only a general
type. Observations imported from the earlier runtime
`category_inference.py` are attached separately and never turned into a
general claim.

The `contract` entry for category constructors records their *intended*
mathematical output, distinguished from the source-level result. A
construction may have a narrower mathematical target than the category
constructor superficially visible in source, particularly when its owner
passes additional category data through helper functions. Audit the complete
constructor path before treating a missing fine placement as a false
mathematical claim.

## Boundaries and next levels of precision

The inventory visits all Python files below `src/dzack_research/preamble/`
and extracts the source-defined category and method containers, including
Mor-category implementation classes named by `ElementMethods = ...`.
Built-in Sage methods absent from the owned source are not falsely counted as
new declarations. The current static model does not fully solve arbitrary
Python dispatch, higher-order function calls, callbacks, general symbolic
parameter unification, actual guards, Cython-generated methods or
value-dependent choices. Each such limit appears as an unresolved return,
an unknown input contract or a conditional reachability witness.

No finite static analyzer can enumerate individual objects obtainable from
arbitrary executable Python, or decide every branch predicate. The honest
exhaustiveness claim is **coverage of source-declared rule sites and explicit
uncertainty**, not the decidability of every return type or the finiteness
of the mathematical object universe.

The repo already includes the static category graph in
`src/dzack_research/utilities/category_graph.py`, runtime result sampling
in `category_inference.py` and the live reference in `megadoc.py`. This
source-only closure reuses those declarations; it does not fork category
semantics into a second hand-maintained inventory. These complementary
views can be compared when the repository's verification phase permits
Sage execution.
