# Inspecting preamble architecture

Use these commands to assemble a small body of source and mathematical evidence for review. They are opt-in inspection tools. Reports do not run from commit hooks or CI, and a reported candidate does not make a command fail. Invalid inputs and failed computations remain errors.

Start with the mathematical construction and the maps it must retain. Inspect its declared ancestry, its construction calls, and the methods it introduces. Then compare the live survey where execution is permitted. A category edge establishes neither the defining datum nor a correctly transported inclusion.

## Choose the evidence

| Question | Tool | Evidence and limit |
| --- | --- | --- |
| What ancestry does the source declare? | `just category-graph table`, `json`, or `slice` | Python declarations and computed axiom edges; conditional returns are a union, and dynamic expressions still need review |
| Where can an inherited operation be examined? | `just placement` | Introduced object, element and arrow methods, their definitions and candidate upper categories from a saved live survey |
| Where do objects reach an operation's fallback assertion? | `just category-graph routes`, `--operation NAME` | For each object operation whose definition ends in a case/match fallback assertion: where it is defined and overridden, and the topmost categories with no override, hook definition or case of the definition above them; read from source, so a realization class answers only for the objects it constructs |
| What does each operation on objects build, and where is the result placed? | `just category-graph constructions`, `--select CATEGORY` | For each category, every public operation on its objects whose source builds an object, followed through module functions, category methods and category application to `_object_of`, `_with_structure` or the category applied; each line states the category the result is placed in and the properties of an input that change it; read from source |
| Which objects are placed in the wrong property subcategory? | `just category-graph properties` | For each property axiom such as `Sets.Finite`: the categories whose name states it and that do not lie under it, the construction sites that place a result under it from a property of an input, the constructions on a category or object (slice, subobject, coslice, direct sum, G-objects) with the property axioms each places on its objects, and the construction sites that place their result by no property of their input; read from source |
| Where are constructions entered and delegated? | `just refactor-survey --view constructors` | Constructor hooks, lexical owners, arguments, return expressions and calls; public named factories can be queried separately |
| Who calls a method, and on what receiver? | `just refactor-survey METHOD` | Source locations, caller, receiver expression and use of the return value; attribute calls are not statically resolved dispatch |
| Where is private data reached through another expression? | `just refactor-survey --view private` | Private attribute accesses on receivers other than `self`, `cls` and `super()`; the declaration-side protected contract decides legitimacy |
| Where might operations have been copied? | `just refactor-survey --view duplicates` | The existing complexity tool's identical AST-body groups; matching bodies or names do not establish identical mathematics |
| Where can an editor navigate definitions? | `just tags`, `just tags json` | Universal Ctags symbol, scope and source index; use the AST survey for construction expressions and receivers |
| Which dependencies form cycles or isolated pieces? | `just category-graph audit`, `shape`, `cells`; `just preamble-complexity` | Declared category structure and the separate Python import graph; neither is a universal measure of architectural quality |
| What changed between live surveys? | `just placement --compare BEFORE --graph AFTER` | Added and removed categories, supercategory edges, method signatures, arrow types and unthreaded-arrow relations |

Source tables, source slices, source surveys, Ctags, and saved-survey queries run without importing the preamble. The `audit`, `shape`, `cells` and `topology` graph views use Sage's graph algorithms. Live survey generation imports the preamble. Apply `DEV-58` to execution; its suspension does not prevent source inspection.

All source surveys identify their population as Python source. They do not preparse `.sage` files. Parser failures name the file and stop the report. Decorators, generated classes, dynamic imports and receiver-dependent dispatch require declaration or runtime inspection; a call-site match is a lead, not a proved call-graph edge.

## Find where objects reach an operation's fallback assertion

```sh
just category-graph routes --operation cardinality
```

`Sets().cardinality` answers for the objects its cases cover: power sets, function sets, products, coproducts, finite and countably infinite sets, and whatever the `_cardinality_decision` hook decides. Every other object reaches its fallback assertion unless a category above it overrides `cardinality`, for instance by applying a functor to sets and asking the result. The view names those overrides, then the topmost categories whose objects still reach the fallback, with the number of categories below each; one override at such a category covers everything below it. For `cardinality` the list includes `AdditiveMagmas`, `Magmas`, `SliceCategory` and `SubobjectCategory`. Without `--operation`, the view ranks every such operation by the number of topmost categories. The live survey does not construct the categories that take two parameters, such as slices and subobject categories, so `just placement` does not show them.

## Read what each construction places its result in

```sh
just category-graph constructions --select Sets --select PowerSets
```

Each line is a construction and the category the source places its result in. Read it as mathematics. Under `Sets`, `X.condition_set(predicate)` is placed in `Sets.Finite` when `X` is. Under `PowerSets`, `X.from_predicate(predicate)` is an object of `SetSubobjectCategory`, which declares `SliceCategory` and places no property of its base object, so a subset of a finite set is not placed finite. Under `Sets`, `X.power_set()` is an object of `PowerSets`, which declares only `Sets()`, so the power set of a finite set is not placed finite either.

## Find objects placed without the properties of their inputs

```sh
just category-graph properties
```

A subset of a finite set is finite, and so are a quotient, a product and an image of finite sets. The view lists, for each property axiom, where it is propagated and where it is not. Its section on constructions on a category or an object shows `SliceCategory`, `SubobjectCategory` and `SetSubobjectCategory` with no property axiom placed: an element of the power set of `{0, 1, 2}` is an object of `Sets/{0, 1, 2}` and is not placed in `Sets.Finite`, so its cardinality reaches the fallback assertion of `Sets().cardinality`. The first section of the view lists categories whose name states a property that their declarations do not place them under, such as `FiniteEnumeratedCartesianProductsOfSets`, which does not lie under `Sets.Finite`.

## Follow a construction through its general owners

```sh
just category-graph slice --select PredicateSubgroups --direction up
just refactor-survey --root sage_extensions/categories/group \
  --view constructors 'Subgroups.*' 'PredicateSubgroups.*'
just refactor-survey --root ~/gitclones/sage-extensions/src/sage_extensions \
  subgroup preimage_subgroup inclusion _canonical_subgroup_inclusion
just refactor-survey --root ~/gitclones/sage-extensions/src/sage_extensions \
  'SetSubobjectCategory.*' 'Subgroups.*'
```

The source slice and the call census answer different questions. In the inspected subgroup route, `PredicateSubgroups.super_categories()` names `Subgroups`, and `Subgroups.super_categories()` names `OwnedGroups`. Its initializer supplies the ambient facade; its inclusion is constructed through the subgroup's Mor. The set-subobject owner represents a monic arrow into a fixed set. Review how that arrow and its domain are retained or composed by the subgroup construction. Merely adding a category edge would not establish this relationship, and a group object need not literally be an inclusion-arrow object.

For an orthogonal-group specialization, start at its public subgroup operation and follow the reported calls into the general subgroup and set-subobject routes. Inspect defining data, ambient maps, membership and factorization together. The source tools expose the expressions; the mathematical reviewer determines whether the general construction is actually inherited or composed.

To inspect encapsulation around the same route:

```sh
just refactor-survey --root sage_extensions/categories/group \
  --view private --json 'PredicateSubgroups.*'
just refactor-survey --root sage_extensions/categories/group \
  --view duplicates --json
just tags json sage_extensions/categories/group
```

Inspect the receiver and declaration-side contract before calling a private access a violation. The duplicate view retains its original relative source locations and roots. It detects literal AST-body reuse, not all equivalent algorithms. A same-name survey also exposes distinct return shapes: those may indicate different operations that need different names.

## Inspect constructors against their mathematical owners

Use `just refactor-survey --view constructors` to locate the current Python entrypoints, their signatures, lexical owners, return expressions and direct calls. A Python constructor declaration is evidence about the transitional preamble; it does not register a category or operation in the final language. Compare each found construction with the typed declaration and maps in `lean-categories/LeanCategories/Catalogue`, then with the request and result route in `lean-cas-dsl`. [Constructor architecture](constructor-architecture.md) records the ownership and the data that must survive migration.

The current `_object_of` route, `ConstructionContract` and provider order explain how a research object is built today. Inspect them when tracing a consumer, but do not reproduce their MRO or initializer protocol in the kernel. The kernel uses explicit applications of registered functors and comparisons; a leaf can supply only an opaque computation against an already registered operation and input form. A named lattice string can select a private input presentation, as described in the constructor architecture document, without defining the object or its laws.

For a named constructor, record the exact input type and hypotheses, its formal category and declaration, its retained object and morphism data, the result type, and the selected structural path. Read the `lean-categories` registration to establish semantic ownership. Read the `lean-cas-dsl` request path to establish how the typed construction is used. Source inspection does not certify the computation or replace the permanent acceptance assertions.

These research source sites are useful starting points:

| Family | Source specimen | Data to trace |
| --- | --- | --- |
| Sets | `categories/sets/set_categories.py` | Ambient set, selected elements and maps, and the exact category of each set construction. |
| Rings | `categories/rings/rings.py` and its imported owners | The ring, localization map and commutativity hypotheses. |
| Modules | `categories/modules/pure/modules.py`, `Modules._call_` | Base ring, scalar action and underlying object. |
| Algebras | `categories/algebras/algebras.py`, `_call_(module, multiplication)` | Underlying module, multiplication and a chosen unit when one is part of the construction. |
| Formed modules | `categories/modules/framed/formed/form_modules.py`, `_call_(form)` and `from_module` | Underlying module, selected form, symmetry and value-module hypotheses. |
| Lattices | `categories/lattices.py`, `Lattices._call_` | Gram and named presentations, selected form and defining maps. |

The call census distinguishes category methods, object methods, element constructors and private realization functions. It does not infer that two same-named methods have the same mathematical input or that an observed implementation makes an operation available in the public language.

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
