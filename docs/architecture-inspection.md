# Inspecting preamble architecture

Use these commands to assemble a small body of source and mathematical evidence for review. They are opt-in inspection tools. Reports do not run from commit hooks or CI, and a reported candidate does not make a command fail. Invalid inputs and failed computations remain errors.

Start with the mathematical construction and the maps it must retain. Inspect its declared ancestry, its construction calls, and the methods it introduces. Then compare the live survey where execution is permitted. A category edge establishes neither the defining datum nor a correctly transported inclusion.

## Choose the evidence

| Question | Tool | Evidence and limit |
| --- | --- | --- |
| What ancestry does the source declare? | `just category-graph table`, `json`, or `slice` | Python declarations and computed axiom edges; conditional returns are a union, and dynamic expressions still need review |
| Where can an inherited operation be examined? | `just placement` | Introduced object, element and arrow methods, their definitions and candidate upper categories from a saved live survey |
| Where are constructions entered and delegated? | `just refactor-survey --view constructors` | Constructor hooks, lexical owners, arguments, return expressions and calls; public named factories can be queried separately |
| Who calls a method, and on what receiver? | `just refactor-survey METHOD` | Source locations, caller, receiver expression and use of the return value; attribute calls are not statically resolved dispatch |
| Where is private data reached through another expression? | `just refactor-survey --view private` | Private attribute accesses on receivers other than `self`, `cls` and `super()`; the declaration-side protected contract decides legitimacy |
| Where might operations have been copied? | `just refactor-survey --view duplicates` | The existing complexity tool's identical AST-body groups; matching bodies or names do not establish identical mathematics |
| Where can an editor navigate definitions? | `just tags`, `just tags json` | Universal Ctags symbol, scope and source index; use the AST survey for construction expressions and receivers |
| Which dependencies form cycles or isolated pieces? | `just category-graph audit`, `shape`, `cells`; `just preamble-complexity` | Declared category structure and the separate Python import graph; neither is a universal measure of architectural quality |
| What changed between live surveys? | `just placement --compare BEFORE --graph AFTER` | Added and removed categories, supercategory edges, method signatures, arrow types and unthreaded-arrow relations |

Source tables, source slices, source surveys, Ctags, and saved-survey queries run without importing the preamble. The `audit`, `shape`, `cells` and `topology` graph views use Sage's graph algorithms. Live survey generation imports the preamble. Apply `DEV-58` to execution; its suspension does not prevent source inspection.

All source surveys identify their population as Python source. They do not preparse `.sage` files. Parser failures name the file and stop the report. Decorators, generated classes, dynamic imports and receiver-dependent dispatch require declaration or runtime inspection; a call-site match is a lead, not a proved call-graph edge.

## Follow a construction through its general owners

```sh
just category-graph slice --select PredicateSubgroups --direction up
just refactor-survey --root src/dzack_research/preamble/categories/group \
  --view constructors 'Subgroups.*' 'PredicateSubgroups.*'
just refactor-survey --root src/dzack_research/preamble \
  subgroup preimage_subgroup inclusion _canonical_subgroup_inclusion
just refactor-survey --root src/dzack_research/preamble \
  'SetSubobjectCategory.*' 'Subgroups.*'
```

The source slice and the call census answer different questions. In the inspected subgroup route, `PredicateSubgroups.super_categories()` names `Subgroups`, and `Subgroups.super_categories()` names `OwnedGroups`. Its initializer supplies the ambient facade; its inclusion is constructed through the subgroup's Mor. The set-subobject owner represents a monic arrow into a fixed set. Review how that arrow and its domain are retained or composed by the subgroup construction. Merely adding a category edge would not establish this relationship, and a group object need not literally be an inclusion-arrow object.

For an orthogonal-group specialization, start at its public subgroup operation and follow the reported calls into the general subgroup and set-subobject routes. Inspect defining data, ambient maps, membership and factorization together. The source tools expose the expressions; the mathematical reviewer determines whether the general construction is actually inherited or composed.

To inspect encapsulation around the same route:

```sh
just refactor-survey --root src/dzack_research/preamble/categories/group \
  --view private --json 'PredicateSubgroups.*'
just refactor-survey --root src/dzack_research/preamble/categories/group \
  --view duplicates --json
just tags json src/dzack_research/preamble/categories/group
```

Inspect the receiver and declaration-side contract before calling a private access a violation. The duplicate view retains its original relative source locations and roots. It detects literal AST-body reuse, not all equivalent algorithms. A same-name survey also exposes distinct return shapes: those may indicate different operations that need different names.

## Slice the category relation and method surface

Edges run from a more structured category to a supercategory. `--direction up` includes the chosen category and reachable supercategories; `down` includes its descendants; `both` takes their union. `--between LOWER UPPER` selects a closed interval. Category arguments and `--select` accept quoted glob patterns.

```sh
just category-graph slice --select Subgroups --direction both
just category-graph slice --between PredicateSubgroups OwnedGroups
just placement --direction up --method inclusion '*Subgroup*'
just placement --direction down --method '*quotient*' --format json Groups
just placement --between Groups Sets --format dot
```

Source class names and live exported names can differ (`OwnedGroups` and `Groups`, for example). Discover the names in the relevant JSON surface rather than guessing a crosswalk. Source projection also unions conditional declarations and does not instantiate category parameters. Cycles prevent treating that projection as a partial order; inspect the raw declarations or the cycle audit first.

For a method-placement review, read its mathematical definition and hypotheses beside each candidate upper category. The worksheet cannot decide where a method is well-defined. It shows same-name introductions on incomparable pairs, including such pairs within a family that also contains comparable owners. Inspect signatures and codomains before identifying those operations. An override may supply a specialized algorithm without introducing a new mathematical operation.

The live survey records the parameters in `probed_as` and any construction problem in `problem`. An entry with no observed instance contains only class declarations: its empty ancestry is not evidence of incomparability or a root category. The worksheet labels it, JSON lists the unobserved population, and automatic incomparable-owner comparisons use observed entries. Use source slices for uninstantiated parameterized families such as the subgroup entries in the saved survey. One sampled base ring is not evidence for all rings. New surveys also carry a fingerprint of the preamble's Python source and a source location for each introduced method. Queries report `matches source`, `stale`, or an unrecorded fingerprint. Source agreement does not establish identical dependency versions or prove correctness.

Compare two explicitly saved survey JSON files with:

```sh
just placement --compare .tmp/before-preamble-graph.json \
  --graph docs/preamble-graph.json
```

The comparison is a relation diff, not a regression verdict. It intentionally leaves mathematical meaning to the reviewer. Saved specimens and source commits supply the evidence for that decision. Temporary captures belong in `.tmp/` and are disposed of with their consuming task.

## Interpret cycles and higher-dimensional structure

Select a modest source slice before computing topology:

```sh
just category-graph topology --select 'OwnedGroups*' --direction up \
  --complex graph --max-vertices 40
just category-graph topology --select 'OwnedGroups*' --direction up \
  --complex flag --max-vertices 40
just category-graph topology --select 'OwnedGroups*' --direction up \
  --remove Objects --complex order --max-vertices 40
```

These are different constructions:

- The **graph complex** retains vertices and undirected edges, including isolated vertices. Its first homology records graph cycles; higher homology vanishes.
- The **flag complex** fills each clique by a simplex. A clique on `n` vertices contributes an `(n-1)`-simplex. Its boundary can participate in a cycle, but the filled simplex makes its own boundary null-homologous.
- The **order complex** has finite chains of the represented partial order as simplices. It is the nerve of that thin category. A greatest or least element makes this complex contractible, so a global computation can hide the local structure of interest. Proper intervals, selected subposets and explicit removal of an extremum answer different, stated questions.

The report gives the selected vertices, facets, face counts, integral unreduced homology and connected components. `--fundamental-group` requests a presentation for a connected slice, without automatic group simplification. The explicit vertex bound controls the scope; clique and chain populations can still grow quickly. The tool does not infer general higher homotopy groups from homology.

The legacy `cells` view supplies graph-cycle witnesses. A cycle in the undirected declaration graph is not automatically a pair of parallel directed functors, a failed coherence law, or a missing category. To pose a coherence question, name the actual functors, their common endpoints, and the required equality or natural transformation. The order complex's simplices follow from the chosen relation; they do not prove that implementation maps commute.

Computation uses maintained implementations: [Sage finite posets and order complexes](https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/posets/posets.html), [Sage clique complexes](https://doc.sagemath.org/html/en/reference/graphs/sage/graphs/graph.html#sage.graphs.graph.Graph.clique_complex), and [Sage simplicial homology and fundamental groups](https://doc.sagemath.org/html/en/reference/topology/sage/topology/simplicial_complex.html). Source traversal uses [Python AST visitors](https://docs.python.org/3/library/ast.html#ast.NodeVisitor); symbol navigation uses [Universal Ctags JSON output](https://docs.ctags.io/en/latest/man/ctags-json-output.5.html).

## Questions grounded in this repository's history

| Evidence | Review question | Useful slice |
| --- | --- | --- |
| `6005c4c58` removed repeated finiteness methods from finite and infinite group refinements | Is a refinement repeating the general operation, or providing a needed algorithm case? | Same-name source definitions and live introductions against their up-sets |
| `b6cda3321` required actual lower-arrow construction; `3e1916263` changed endpoint transport along forgetful categories | Does declared inheritance carry the lower arrow's defining data and correctly transported endpoints? | Mor ancestry, arrow types, constructor calls, and source of forgetful transport |
| `61011b141` replaced the survey's uninformative arrow-method population with actual Mor arrow types | Does the inspection tool observe the runtime object that owns the operation? | Snapshot `arrow_type`, `arrow_mor_class`, `arrow_unthreaded` and method source locations |
| The set-engine complaint records local membership, enumeration and set operations alongside maintained implementations | Is an owned operation reusing its computational owner, or rebuilding a general algorithm? | Source return/call expressions, import graph and duplicate bodies, followed by the engine's contract |
| The discrete-category complaints distinguish inherited universal-operation names from their realizations | Does a visible method reach a construction with the required maps and universal property? | Public method, construction hook and consumer expressions; then a mathematical specimen |

Historical repairs motivate questions, not assertions that the same defect remains. Source review establishes the construction route; mathematical exercises establish its promised behavior. Retain actual unresolved findings at their owning complaint and DAG node. Add a new query when a concrete review needs it, rather than building a catalogue of every hypothetical violation.
