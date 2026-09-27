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

## Constructor discovery: decorators and registries

The constructor audit should compare three mechanisms before changing runtime construction:

| Mechanism | Useful role | Cost or limit |
| --- | --- | --- |
| Ordinary category methods with source introspection | Preserve explicit signatures, inheritance and editor navigation | Hook names alone miss named mathematical constructors |
| A declaration decorator on an existing constructor method | Mark named constructors for collection into help, the megadoc and inspection reports | Decoration alone neither exposes a method on its owner nor establishes inherited construction data |
| An owner-local implementation registry | Add computational cases for one construction without editing its general owner | Requires explicit applicability, ambiguity handling and deterministic loading |

The [source-grounded constructor recommendation](constructor-architecture.md) specifies the implementation boundary: reuse `ConstructionContract` and the existing category-generated provider chain; mark existing methods for discovery; evaluate keyed registration on the exact-name branch of lattice input. It relates those choices to the biproduct, localization, algebra-arrow and resolution repairs in git history. The recommendation does not introduce a general algorithm dispatcher.

Collect declarations into a derived catalogue grouped by mathematical owner. A constructor declared on its owner should obtain that owner from its declaration rather than repeat it in a second hierarchy table. Read its signature, documentation and source location directly. Record additional metadata only when source structure cannot express the construction's role. The same declarations should supply documentation and opt-in inspection, so adding a constructor does not require editing another list.

The [KDnuggets registry-pattern article](https://www.kdnuggets.com/stop-using-if-else-chains-use-the-registry-pattern-in-python-instead) supplies a concrete candidate: implementations register a discrete key beside their definition, and a stable dispatcher looks up the callable. Its reusable version rejects duplicate keys and exposes available entries. It also identifies import-time registration and the limited fit for conditions that are not discrete choices. Apply that pattern directly when a construction has named, interchangeable providers under one contract.

For this repository, distinguish two keys: a constructor name identifies a mathematical operation; a provider key identifies an implementation of that operation. A category's constructor catalogue can collect different signatures for discovery, while each operation's provider registry must preserve that operation's own signature and datum. A named lattice catalogue is a candidate for discrete lookup; selection by ring properties or overlapping category membership still needs mathematical applicability rules. Keep those rules explicit rather than replacing a conditional chain with an ordered list of predicates. Existing `_register_indecomposable_gram` records display names by Gram data; it is not already a constructor-provider registry.

Evaluate explicit decorators before automatic subclass registration: a private implementation subclass need not introduce a public construction, and the category runtime also creates classes. Registering every subclass would confuse those roles. A decorator attached to the actual construction declaration can instead make the intended extension and its owner visible to source inspection.

Inspect these existing routes as initial specimens:

| Family | Source specimen | Question for collection and routing |
| --- | --- | --- |
| Sets | `categories/sets/set_categories.py` | Which named set constructions are category methods, and which require an existing ambient set? |
| Rings | `categories/rings/rings.py` and its imported owners | Which declarations own construction, and which only re-export it? Keep localization on the ring object under its commutativity hypotheses. |
| Modules | `categories/modules/pure/modules.py`, `Modules._call_` | Can discovery explain both the scalar-action datum and the route with its underlying object explicitly supplied? |
| Algebras | `categories/algebras/algebras.py`, `_call_(module, multiplication)` | Can a user discover construction from an existing module and the additional multiplication, including the extra unit datum where required? |
| Bilinear and other formed modules | `categories/modules/framed/formed/form_modules.py`, `_call_(form)` and named `from_module` methods | Does each named route establish the same underlying module and selected form, with its actual symmetry and value-module hypotheses? |
| Lattices | `categories/lattices.py`, `Lattices._call_` | Do named and Gram presentations reach the same formed-module construction and retain its maps? |

These are source specimens, not proof that the routes satisfy their contracts. Collection must distinguish methods on a category, methods on its objects, element constructors, and private realization functions. A catalogue may show all of them with their roles; exposing every descendant constructor on `Sets` would erase that distinction. Place a construction at the highest owner that has its defining data, not the highest owner of its result.

For implementation registration, dispatch must account for category parameters, supplied maps and hypotheses. Python's [`singledispatch`](https://docs.python.org/3/library/functools.html#functools.singledispatch) selects by the first argument's Python type; it is therefore not by itself a dispatcher for this mathematical relation. Compare reuse of existing category dispatch with a local registry before introducing another dispatcher. Distinct named input forms need not be forced into one overloaded call.

An acceptable registry must expose the applicable cases and the reason for its selection. An incomparable overlap needs a declared mathematical resolution; import order or last registration cannot decide it. An extension adds a case while preserving the construction contract and previous cases. Loading must be explicit and reproducible, with the general category independent of imports of its descendants. Source inspection must distinguish declared providers from loaded runtime providers. Python [decorators execute when a definition is evaluated](https://docs.python.org/3/reference/compound_stmts.html#function-definitions), so a runtime registry alone cannot inventory unloaded modules.

Evaluate the candidate on two different families before generalizing it. Exercise help and completion, inherited discovery, exact signatures, source-only collection, runtime binding, duplicate declarations, overlapping cases and module-loading order. Trace the constructed objects and their maps as well. Registration cannot repair a specialization that fails to use its general construction. Add the resulting queries to the existing tools; keep architectural judgments available for review rather than turning them into gates.

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
