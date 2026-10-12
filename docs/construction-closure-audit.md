# Preamble construction-closure audit

## Purpose

Inventory **construction schemes** available in the owned preamble, including
category families, axiom subcategories, inherited operations, morphism and
element operations, source-level return branches, and subsequent operations on
their results. This is a durable inspection surface for mathematical architecture
review, not a substitute for reading the specific owner when deciding whether
its statements are mathematically correct.

Run from the repository root:

```bash
just category-universe
```

Optional output directory: `just category-universe .tmp/other-universe`.

The command writes three mutually consistent artifacts:

- `.tmp/construction-closure/universe.json`: stable, searchable inventory of
  category declarations, inclusion relations, operation input ports, source
  locations, return expressions, explicit result categories, unresolved
  destinations, conditions, and derivation witnesses.
- `.tmp/construction-closure/universe.dot`: labeled directed graph; operation
  boxes mediate category-to-result relations. Convert with Graphviz if desired.
- `.tmp/construction-closure/index.html`: self-contained, offline, searchable
  inspector with category, construction, unresolved, and reachable-scheme views.

This command **parses source only**. It does not import the preamble, instantiate
Sage categories, evaluate arbitrary user methods, or run mathematical tests.

## Model and closure

A category instance, an object of that category, an element of an object,
and a morphism are distinct kinds of mathematical things. The inventory records
the method receiver (`Category`, `ParentMethods`, `ElementMethods`, or
`MorphismMethods`) and never identifies an object of `C` with a category
`C` itself. Return statements of the form `C(parameters)` construct a
category value (an object of `Cat`); applying that category to data
constructs an object of `C(parameters)`.

The primary relation is a **conditional construction hyperedge**. Every method
has a declaring category, a receiver sort, a list of argument ports, zero or
more syntactic guards, and one source-evidenced result expression per return
branch. Supercategory and axiom-inclusion edges are a separate relation.
The audit retains symbolic parameters and does not collapse isomorphic
objects into equal objects.

For the recursive view, start from all declared category *schemes* and
propagate explicit method-result schemes through available operations. Whenever
a result has a recognizable declared category family, its methods and
inherited methods become available at the next iteration. Local method
dispatch is followed through same-object and inherited methods, with
cycle detection. This computes a finite least fixed point over the
**abstract domain of type schemes**, not over all possible Python values.

The HTML inspector can search for an operation, its owner, its result type,
or a source file, then display the exact return branch and the reachability
witness. The JSON is suitable for downstream comparison between Git revisions.

## Soundness and coverage limitations

The universe of concrete objects is generally infinite. Exact static
reachability of arbitrary Python methods is undecidable. Accordingly:

- A declared category is a **symbolic seed**, not proof that a concrete
  inhabitant can be constructed.
- A method with arguments or guards yields a **candidate** output and retains
  those obligations. It is not asserted to be executable for arbitrary inputs.
- A syntactically unresolved return or dynamic dispatch remains an
  **unresolved** record; it must not be silently discarded or classified
  as proof that no result exists.
- Imported factories, implementation callbacks, dynamically added category
  methods, generic collection contents, and value-dependent returns may
  require deeper interprocedural analysis. The JSON does not assert complete
  static recovery of those paths.
- A class's inferred result category is a source placement claim, not a proof
  of mathematical correctness. Compare against the category's defining
  construction and its consumers before judging it.
- A method returning a tuple of objects is currently classified as a
  container. Recursive extraction of its members is not yet included.
- The static audit is independent of the existing live-session
  `category_inference` and `megadoc` probes. Their empirical results can
  supplement, but cannot replace, symbolic reasoning over guarded operations.

These limitations are deliberate: an audit that presents missing or guessed
results as verified mathematics is worse than one that reports uncertainty.

## Relationship to existing tools

The implementation reuses `category_graph.read_tree` and
`category_graph._all_edges` for category vertices, axioms, joins, and
supercategories. It adds a machine-readable rule layer over the same source
tree and fixed-point propagation, rather than duplicating category extraction.
The existing `category-graph constructions` and `properties` reports remain
valuable as independent source-review views. The live `megadoc` remains the
authoritative introspection of dynamic method-resolution order when execution
is permitted.

Implementation: `src/dzack_research/utilities/construction_closure.py`.

Source-only regression specimens:
`tests/utilities/test_construction_closure_source.py`.
