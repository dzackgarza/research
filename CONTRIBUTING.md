# Contribution Guidelines and Policy Index

This document defines the contribution policies for the repository.
All contributions must follow the categorized policy index below.
Each policy has a unique alphanumeric identifier.

For a new addition, begin with
[mathematical dependency tracing](#mathematical-dependency-tracing).
For construction, representation, or engine work, then apply the normative
[preamble architecture specification](#preamble-architecture-specification).
Its `OWN-*` policies specify the intended architecture, not implementation status.
Record observed foundational gaps and papercuts in [COMPLAINTS.md](COMPLAINTS.md)
under [DEV-59](#dev-59-record-observed-foundational-gaps-and-papercuts).

Use the [task complexity guide](COMPLEXITY.md) to score work and select a model and reasoning effort.

For current work selection and corrections, apply `DEV-50` through `DEV-58`:
[future-only TODOs](#dev-50-todos-contain-only-unfinished-work),
[mathematical representation](#dev-51-a-computational-image-is-not-the-object),
and [verification phases](#dev-58-observe-the-current-verification-phase).

* * *

## Preamble design philosophy

**The preamble primarily stitches together, organizes, and composes existing
mathematics and existing implementations behind one fully owned mathematical
interface. It is not a mandate to build another computer algebra system from
first principles.** A feature request ordinarily asks the contributor to make
an established construction available in the right category, with the right
objects, maps, hypotheses, and relationships. It does not ordinarily ask the
contributor to invent or reimplement the algorithm that computes it.

The public language is owned throughout. Sage, GAP, Julia, OSCAR, Singular,
Macaulay2, PARI/GP, and other suitable maintained systems provide private
computation. The preamble supplies the mathematical organization and the
necessary integration between their results and its own objects. A uniform
interface must make these capabilities compose without requiring the researcher
to know which engine was called, speak its vocabulary, or handle its objects.

This is the integration philosophy of `sage-categories`, applied to the
preamble's stricter recursively owned public boundary. Its
[README](https://github.com/dzackgarza/sage-categories/blob/main/README.md)
names categories, functors, and universal constructions as the reuse model;
its [repository-role instructions](https://github.com/dzackgarza/sage-categories/blob/main/AGENTS.md#repository-role-integration-framework-and-engine-delegation)
make stitching and engine delegation the engineering purpose. The
[architecture specification](#preamble-architecture-specification) below turns
that purpose into construction, dependency, and encapsulation contracts.

### Mathematical dependency tracing

**First formulate the addition in mathematics, independently of the current
implementation. Then unfold the mathematics it needs. Only afterwards select
its implementation.** This applies to a new operation, category, object,
morphism, specialization, research example, or repair that introduces new
mathematical behavior. It is not a preliminary search for a convenient class
whose existing methods can be made to resemble the requested answer.

Start with the mathematical question a researcher is asking. State the input
objects and their categories, the desired object or morphism, its defining
datum or universal property, and the hypotheses under which it exists. Include
the maps that make the result useful in subsequent mathematics. Establish these
facts from the project's mathematical specifications and actual mathematical
sources, not from recalled definitions or the current backend's capabilities.

Express the request in the vocabulary an ideal mathematical API should support:
sets, indexed families, maps, categories, functors, groups, actions, rings,
modules, subobjects, quotients, tensor products, schemes, sheaves, complexes,
and the other standard notions the question actually uses. Pseudocode may
express this account, but it is mathematical notation, not a claim that the
displayed Python names exist. Name the mathematical operation before discussing
classes, storage, registration, adapters, callbacks, or dispatch.

For each notion in that account, recursively ask what makes it meaningful:

- What are its defining objects, operations and laws? What additional datum is
  supplied, rather than inferred from a property or chosen silently?
- In which category do its morphisms live? What are their source and target,
  their composition, and the maps retained by the construction?
- Which subobjects, quotients, limits, colimits, or other standard constructions
  does it use? What diagram, indexing object, or equivalence relation defines
  them, and which existence or preservation hypotheses are needed?
- Which structure is forgotten, transported, or added? If a construction on
  underlying objects is used, what theorem supplies the desired structured
  object and its maps? Faithfulness alone does not supply that theorem.
- Which properties refer to which mathematical object? Specify, for example,
  the notion of integrality or reflexivity in use rather than transferring a
  familiar property name between unrelated theories.
- What do these prerequisites themselves require, down to the chosen
  set-theoretic and categorical foundations: sets and families, functions,
  relations, objects and morphisms, identities and composition, and the
  relevant universal constructions? Retain size and finiteness hypotheses;
  a category is not assumed to have a finite enumerable set of objects.

The result is a mathematical dependency account, not a flat list of associated
subjects or a list of files to create. Each dependency must explain what datum,
map, theorem, or construction it supplies to its dependent notion. A phrase
such as "needs category theory" does not explain the dependency. Neither does
adding a class named after the missing notion.

#### Unfold through established foundations, not repeated reconstruction

The trace must reach the foundations, but it need not rewrite their definitions
for every leaf. Follow and cite an existing source-backed mathematical account
when it already unfolds a prerequisite. Make the path to that account explicit;
do not stop at an unexplained term such as module, action, or sheaf because a
similarly named class exists. Expand precisely the uncertain or new part of the
dependency account, and retain consequential choices at the existing mathematical
declaration or specification. No separate trace registry is required.

Distinguish three sorts of dependency without weakening any of them:

- **Defining mathematics:** what the requested object and maps mean, and the
  general theory needed to express them. These requirements do not shrink to
  match the current implementation.
- **A computational realization:** the additional hypotheses, presentation,
  coordinates, resolution, cover, or finiteness that a selected algorithm uses.
  Its comparison with the defined object is part of the obligation.
- **A related extension:** a broader theory or further research question not
  required by this request. Record a concrete discovered need when appropriate,
  but do not make every mathematically related generalization a prerequisite.

Different presentations of the same mathematics may yield different computation
routes. Establish their comparison rather than treating the easiest one as the
definition. Conversely, do not demand every possible computational route before
using one justified route. For example, a particular sheaf-cohomology computation
may use an acyclic cover while another uses a resolution. The underlying sheaf
and complex categories and the comparison remain mathematical requirements;
this does not force every calculation to construct a spectral sequence. An
unimplemented required general interface remains owed even when one computation
can already be performed.

#### An example of the reasoning, not a prescribed workstream

Consider a request involving an equivariant morphism of modules. The existing
[action-functor account](src/dzack_research/preamble/categories/functors/group_actions.py)
describes actions as functors and forgetting the action as evaluation. A
mathematical trace can therefore begin as follows:

```text
Requested: a morphism between two R-modules with G-actions.
Needed: the two R-modules, their G-actions, and an equivariant linear map.
Actions: functors from the one-object category BG to R-modules.
Maps: natural transformations between those functors.
Unfold BG: the group, its elements, multiplication, identity, and inverses.
Unfold R-modules: the ring, underlying additive groups, and scalar actions.
Unfold both: underlying sets, functions, products, and their defining laws.
Unfold the categorical language: objects, Homs, identities, composition,
functors, and naturality, with the actual source and target of each map.
```

If the request also asks for a kernel, scalar change, or invariant submodule,
continue the trace through that construction and its hypotheses. Do not append
an unrelated collection of matrix routines. The point is to identify which
general mathematics supplies the requested result, so that a module action,
a geometric action, and another structured action can share the appropriate
theory without pretending their computations are identical.

The same reasoning applies in geometry, homological algebra, arithmetic,
polyhedral geometry, and every other preamble domain. A sheaf operation unfolds
through its site or space, covering and restriction data, category of values,
and relevant functors. A metric or convex construction must specify its space
and geometric hypotheses before importing a Euclidean computation into another
geometry. These are examples of how to ask the questions, not a fixed list of
foundations to implement on every task, and not a toric-cohomology checklist.

#### Compare the mathematical account with the available language

After the mathematical trace, inspect the owned declarations, generated
reference, live source and consumers, and then the relevant maintained packages.
For each required notion, establish whether the available path supplies its
defining data, maps, hypotheses, inherited structure, and computational case.
The name of a method, a numerical answer, a category label, or a foreign engine
object is not sufficient evidence that the mathematical prerequisite exists.

Distinguish a missing general notion from a missing operation on an existing
notion, a missing comparison or inherited datum, a specialization that bypasses
its foundation, and an unavailable computational case. These require different
repairs. In particular, an operation can exist in Sage while remaining absent
from the owned mathematical language; that calls for integration, not reinvention.
An API may also express the correct object while a requested decision procedure
is unavailable or undecidable. Do not confuse that with nonexistence of the object.

When this comparison exposes an actual gap, record it in
[COMPLAINTS.md](COMPLAINTS.md) under `DEV-59`. Explain the missing general
mathematics and the dependency path that exposed it, not only the failing leaf
method. Search broadly enough to distinguish absent machinery from undiscovered
machinery; record the inspected boundary and unresolved questions honestly.
The complaint should let another mathematician understand the required theory
without first understanding this repository's implementation.

Then select the remaining implementation delta under `OWN-01` and `DEV-56`.
Repair the required foundation through its owner and connect the real consumer.
Record newly discovered independent needs without silently expanding the active
task. Do not turn the trace or complaint into a substitute for a repair already
required by that task. Equally, do not suppress a foundational finding merely
because it is outside the file, workstream, or session currently being edited.

### What the preamble contributes

The distinctive work is making separate capabilities form one usable mathematical
language. That includes identifying the correct owner of an operation, retaining
the data that defines an object, transporting additional structure, constructing
the maps that relate results, and reconciling engine representations with those
requirements. This is substantive mathematical design even when the final
implementation consists mostly of declarations and short compositions.

For a typical feature, the intended contribution consists of:

- An owned mathematical declaration with its defining data and hypotheses.
- Construction through existing categories and sanctioned constructors.
- Reuse of inherited operations, structural functors, and universal maps.
- A private integration of a suitable maintained computational operation.
- Complete raising of results, including elements and constituent maps.
- Mathematical specimens that distinguish the requested construction from a
  plausible substitute, executed only in the authorized verification phase.

These responsibilities do not imply a new file, class, or adapter for every
feature. An existing owner may already supply several of them, and an existing
adapter may already contain the needed computation. The contribution is the
actual missing integration, not a restatement of everything the dependencies do.

### Two kinds of reuse are required together

**Mathematical reuse** means deriving behavior from structure already represented
in the category framework. A differential graded algebra uses the common graded
algebra and complex structures. A special localization uses the general
localization construction. A new structured category uses the existing object,
element, morphism, and functor machinery rather than reimplementing them under
new names. The hypotheses that justify inheritance or transport remain part of
the mathematics; a forgetful functor does not preserve every construction merely
because it forgets structure.

**Computational reuse** means leaving established algorithms with systems that
already maintain them. A generic owned cohomology interface does not justify a
new local homology algorithm. A common owned category does not justify rebuilding
finite-diagram or path-reduction computations. The same prior-art requirement
applies at the framework level as at a specialized mathematical level.

Neither kind substitutes for the other. Calling Sage directly from a specialized
constructor can reuse an algorithm while bypassing the owned mathematical
construction. Conversely, expressing the right mathematical definition in a
generic module can still duplicate an entire maintained computational system.
The intended architecture combines a shared semantic construction with suitable
maintained computations behind its private boundaries.

**Owning an API does not mean owning the algorithm; delegating the algorithm does
not mean surrendering the API.** All publicly reachable constituents remain
preamble objects. A private engine can compute a presentation or representative,
but its result must become the owned object with the structural maps the public
contract requires. Neither a thin facade over foreign objects nor a fresh
implementation of all their arithmetic satisfies this division of responsibility.

### Shared foundations should make later work smaller

The framework exists so that a new mathematical specialization supplies its new
data and immediate structural relationships, then receives the consequences from
the existing construction machinery. The author of a formed module should not
also implement general set behavior. A geometric cohomology consumer should not
also implement general module kernels. A new action should not bring another
implementation of identity, composition, or scalar change.

When several apparent methods require the same missing foundation, treat that
foundation as the common dependency. Supply it at its owner, connect the first
real consumer, and let other consumers use it. Do not preserve a method-by-method
backlog that assumes every consequence needs an independent implementation.
Equally, do not use the word foundation to justify constructing an entire new
framework before the selected mathematical operation can begin. Reuse the
available framework and repair the exact prerequisite that the consumer needs.

A claim of reusable foundations must be visible in a real consumer. The new
construction should obtain its data, maps, and inherited operations through the
shared route. Merely placing duplicate algorithms in one file, adding an abstract
base, or declaring a category does not establish that later work has become
simpler. If each new specialization still needs to understand transitive runtime
initialization or reconstruct structural maps, repair the framework contract.

### Select dependencies by the responsibility they can discharge

A computation package need not implement the preamble's class compiler, public
ontology, or whole research workflow to be useful. Ask whether it supplies the
specific computation with the required inputs, hypotheses, and outputs. A
different object model or method spelling normally calls for an adapter, not
rejection of the computation. A result missing necessary maps calls for further
capability research or a precise integration decision, not an unsupported claim
that an invariant is the full construction.

The [sage-categories complaints](https://github.com/dzackgarza/sage-categories/blob/main/COMPLAINTS.md)
illustrate why this separation matters: inability to use CAP as an abstract
Python class compiler was treated as a reason to discard its concrete category
computations too. The relevant principle is responsibility-specific evaluation.
Inspect the shared framework, Sage, and the appropriate specialized packages for
their respective jobs; no single dependency has to replace the whole project.

The preamble can coordinate more than one engine through the existing private
bridges. Requiring an unnecessary direct connection between every pair of
engines creates work that the mathematical task did not require. Conversely,
inventing a new bridge when a suitable one exists transfers another maintained
responsibility into this repository. Integration follows the established
transport owners and raises owned values before returning to mathematical code.

Search for the full semantic operation, not just its easiest primitive. A
homology package can discharge more responsibility than a matrix routine used
inside a home-written homology implementation. A module-presentation operation
can discharge more than a long local sequence of intermediate syzygy operations.
Use the highest suitable maintained operation that supplies the actual contract;
compose established operations when no single call does. The
[computation references](#existing-computation-references) are starting points,
not a reason to restrict discovery to the first familiar engine.

### Integration code has a specific job

Local code is justified by the semantic difference between an existing capability
and the owned operation. Typical differences include expressing the source and
target as owned objects, reconciling grading or variance conventions, preserving
chosen presentation data, constructing the required comparison maps, and
converting complete results into their owned parents. State that difference at
the construction or adapter that owns it.

An adapter is not a place where arbitrary new algorithms become acceptable by
being hidden. Renaming a computation, moving it to a private helper, translating
it into Julia, or putting it inside the generic category layer does not transfer
its maintenance to an upstream project. A dependency import also proves no such
transfer if the repository still implements most of the dependency's job itself.
Review which system actually performs the semantic operation.

Some integration is necessarily substantial. Engine presentations can differ,
maps may need transport, and exactness or coefficient hypotheses may differ.
Investigate that difficulty rather than assuming every operation is a one-line
call. But the difficulty must be an identified semantic or integration gap, not
an unexamined presumption that locally implementing familiar mathematics is the
normal route. Fix defective packaging or bridges at their established owner;
they are not mathematical evidence that a replacement algorithm is necessary.

### Invention is an explicit research responsibility

The repository supports mathematical research; this philosophy does not prohibit
new mathematics. It distinguishes a research contribution from the ordinary
engineering work of exposing established mathematics. A request to make an
existing construction available does not silently authorize a new algorithm,
new correctness argument, or new long-term maintenance obligation.

When the relevant mature systems and standard compositions do not supply the
required computation, state the precise remaining gap. Preserve the original
mathematical domain while distinguishing the representations and cases for which
an algorithm exists. General undecidability does not invalidate an available
specialized algorithm, and a useful special case does not justify claiming a
general decision procedure.

Owning a genuinely new nontrivial algorithm requires the deliberate decision in
`ENG-06`, its source-grounded mathematical contract, and its own correctness
burden. The decision concerns that algorithm, not permission to rebuild adjacent
infrastructure. Discovery can establish that the operation needs further research;
it cannot turn an unmet interface into a guessed answer, a weaker substitute, or
an assertion that the requested mathematics does not exist.

### Progress means useful composition with controlled ownership

Assess a feature by what mathematical work a researcher can perform through the
owned interface, whether the result retains its required structure, and which
system maintains each necessary computation. This includes the cost imposed on
future changes: a shared correction should reach its consumers through their
existing contracts rather than require the same repair in every theory.

More locally implemented mathematics is not inherently more progress. A feature
that duplicates a mature algorithm adds a correctness and maintenance burden
even when its examples give the right answers. Fewer lines are not inherently
better either: deleting structural maps or exposing raw engine results makes
the implementation shorter by abandoning the contract. The objective is full
mathematical capability through principled composition, not a source-line quota,
dependency count, passing-test count, or administrative completion signal.

Evaluate work over time against that objective. Identify the new usable
construction, the existing capability reused, the necessary local integration,
and whether later work preserves those boundaries. An unexpectedly prolonged
implementation warrants revisiting missing reuse and structural dependencies;
elapsed time alone does not prove reinvention. Returning repeatedly to local
repairs while retaining the same bypass is not a forward trajectory merely
because each repair is individually substantive.

### The artifacts are instruments; the product is a map of Sage

Every task in this repository is a means. A tool that prints its view, a
category that constructs, a notebook cell that reproduces a table: each is an
instrument, and the result it produces is worth very little next to what
producing it teaches about the engine underneath. The product of the work is a
durable map of Sage's ecosystem: which spelling of an operation to route
through, what it demands of its input, what it returns, where it is absent,
where it is present and wrong, and where it is present, correct, and
unaffordable at the size the research runs at. The preamble encodes that map as
one owned name per operation, and every owned name is a place where somebody
found out what Sage does there. Without that finding an owned name is a rename.

This inverts the ordinary cost model. The route that feels cheap, which is to
close the task in front of you by whatever works, yields nothing: the task
closes and the map gains no entry. The route that feels expensive, which is to
stay inside Sage when it resists, find out why, find the keyword, the backend
or the constructor that answers, and write down what was found, is the one that
pays, and it pays long after the task is forgotten. Friction with the engine is
therefore the most informative event a task can produce. A slow call, a rejected
input, a wrong-shaped result: each is a fact about Sage that the map does not
yet hold. Going around it costs nothing visible and destroys the only thing the
task was for.

Two moves throw the knowledge away, and both feel like progress from the
inside. Hand-rolling the algorithm closes the task while leaving the engine's
own routine unexamined: nothing is learned about its speed, its output
convention, its input demands, or its failure modes. Pivoting to a second
library at the first bump leaves the ecosystem the project is mapping, so the
search for the Sage-internal answer is abandoned exactly where it would have
paid, and the dependency surface fragments. The escalation ladder, Sage native,
then the backends Sage ships, then ownership under an audit trail, is not a
convenience ordering. It is the research protocol, and a rung teaches only if
you stand on it. `ENG-07` and `ENG-08` make this reviewable; `DEV-62` says what
counts as a finding and `DEV-63` says where a finding lands.

### Interactive discovery is the user-facing consequence

The preamble is an **interactive discovery language for mathematics**, not a flat library of globally named functions.  A user should be able to start from the mathematical object already in hand and discover the language locally with tab completion.  If `C` is a category, `C.<TAB>` should expose the constructions and structure that `C` knows; if `M` is a module, `M.<TAB>` should expose module-level operations; if `x` is an element, `x.<TAB>` should expose element operations; if `f` is a morphism, `f.<TAB>` should expose morphism operations; and Homsets, functors, subobjects, and other mathematical objects should likewise expose the operations they own.  The receiver is part of the mathematical documentation: it tells the user what kind of thing an operation acts on and sharply narrows the admissible language before any manual or source file is opened.

This is a deliberate contrast with a GAP/Julia-style global operation catalogue.  A global name such as `Product`, `Kernel`, or `Orbit` gives almost no local information about its domain: the user must already know whether it acts on categories, parents, morphisms, elements, families, or some combination.  As the system grows, that design requires memorizing an ever larger language or repeatedly consulting documentation.  The preamble instead scales by **navigating from mathematical objects to their methods**.  The public global namespace therefore exists primarily for canonical mathematical objects, category/object constructors, notation entry points, and genuinely language-level forms—not as a convenience catalogue of operations on objects that already exist.

**Mathematical ownership determines API placement.**  An operation lives on the mathematical object whose structure makes the operation meaningful.  A category that claims products owns the construction of its selected products.  A Homset owns operations whose hypotheses are properties of that Hom.  Morphisms own morphism-level constructions; parents own parent-level constructions; elements own element-level operations; functors own functorial operations.  The code implementing the operation belongs with that owner or in its mathematical subtree.  Free-standing helpers may support notation internally, but they must not become a second public mathematical language.

The same ownership principle determines implementation dataflow.  Code should teach the repository a mathematical fact **where that fact lives**, and downstream behavior should follow from the object/category graph.  If `C` has products, teach `C` how to construct them; do not teach a global `Product(...)` dispatcher every category for which products happen to exist.  If equality of arrows is determined by structure of a Homset, teach that Homset; do not make a root equality helper enumerate concrete theories.  This is mathematical organization used as implementation compression: the general structure is stated once at its owner and inherited or delegated through the ordinary category machinery.


**Mathematical domain and computational domain are different.** Method placement follows the first category/object/element on which the notion is mathematically defined, not the currently decidable or implemented cases. Every set has a cardinality, so `cardinality()` belongs to sets even though no CAS can compute the cardinality of an arbitrary represented set such as `X = {n in NN | n.is_twin_prime()}`. Every formed module has a well-defined degeneracy predicate, so `is_nondegenerate()` belongs with formed modules even when the current implementation only decides finite-rank represented forms. The implementation may therefore route across the cases currently understood and assert-gate the remainder with an informative statement of the missing computational hypothesis. This is not a stub: supported cases must actually compute. Over time the routing table grows so that the computational domain converges toward the mathematical domain.

This is one of the few places where an explicit `case`/`match` or other routing table is positively desirable. It reads like mathematics: identify which represented situation the object lies in, invoke the theorem/algorithm appropriate to that case, and use an exhaustive final assertion for cases not yet computationally covered. The banned shape is a method whose entire body is failure (`assert False`, `NotImplementedError`, or equivalent) and which therefore advertises functionality without implementing any case at all.

**Infinite-compatible semantics come before finite-coordinate algorithms.**  The mathematical layer should be written so that replacing a finite indexing set by an infinite one, a finite basis by a lazy framing, or a matrix realization by an abstract Hom does not force a redesign of unrelated consumers.  Finite coordinates, rows, columns, exhaustive enumeration, and concrete arrays are computational specializations.  They belong behind semantic objects that remain meaningful in infinite settings: owned sets/families, finite-support elements, subobjects, Homs, kernels/images, products/coproducts, tensor/block constructions, actions, and universal properties.  A large blast radius when moving from finite to infinite data is strong evidence that coordinates or enumeration leaked above their proper layer.

**The public API is an adversarial semantic gate.**  It is judged not only by whether correct code can be written through it, but by which mathematically invalid shortcuts it makes easy to write.  If a caller holding a morphism can casually unwrap a matrix, compute a nullspace, and rebuild a pretend kernel, the interface is too permissive even when `f.kernel()` also exists.  If an element constructor accepts a bare coordinate tuple, the API invites callers to forget the parent and framing that make those coordinates meaningful.  Close these hatches structurally: force construction through mathematical data, keep numerical representations private or one-way, and use assertions that reject a predicted shortcut while naming the correct construction.  The goal is not to trust every future consumer to remember the doctrine; the interface should make the semantic route the path of least resistance and the numerical bypass visibly abnormal.

**Repository prescriptions are part of the executable architecture.**  Issue bodies, plan cards, comments, docstrings, examples, tests, and migration notes train later contributors and agents just as neighboring source code does.  Once a mathematical or architectural ruling falsifies a prescription, correct or delete that prescription before implementation continues.  A stale comment that says “shared ambient,” a test that still unwraps coordinates, or an issue body that asks for a deprecated signature can faithfully regenerate the exact defect that the code was meant to remove.

**Diagnose recurring slop by generator, not by instance.**  A new occurrence of a known pattern is repaired by the existing rule; it does not earn another bespoke exception or workaround.  Add a catalogue entry only when review discovers a genuinely new code-shape generator.  The principal generators include presentation/object confusion, theorem proxies replacing definitions, stored or witness-free structure, signature-porting from a foreign ontology, contaminated prescriptions, and laundering mathematically correct failures instead of repairing what they expose.

**Construct the defining data at their mathematical owner.** Start a category contribution by reading its immediate structure owners and constructors.
State the added datum, its domain and codomain, and the equations its morphisms preserve in that category's documentation.
Pass the datum through the owning constructor so its concrete accessors are fulfilled there.
Alternative constructors must establish the same datum, including the maps that transport it between presentations.
An inherited method name alone does not establish its required state.

Distinguish properties from additional choices.
A property refinement retains the existing structure; a selected action, multiplication, framing, or presentation requires construction data.
Specify morphisms as well as objects when adding structure.
Reuse a universal construction through a structural functor only with the corresponding preservation or creation result and canonical maps.

**Keep specialization at its own owner.** A specialized constructor calls its general mathematical construction.
Adding a leaf should ordinarily require changes to that leaf and its immediate mathematical dependencies.
A generic owner importing the new descendant indicates a missing construction interface.
Read the [construction and inheritance proposal](references/preamble-architecture.md) for current examples and the proposed repair.
The [architecture prerequisite](TODO.md#architecture-before-dependent-implementation) sets their implementation order.

For review, follow one public constructor through its defining datum, one nonidentity structural-functor image, and one inherited operation.
Include the resulting objects, morphism endpoints, and defining equations in the mathematical example.
Inspect required operations on the actual generated classes through Sage's abstract-method discovery.
Write the example at the existing owning test surface, subject to the expectation-subtree rules and the current verification policy.
Keep the category declaration, constructor signature, and executable contract as the discoverable source; derive reports from them.

These principles are more important than any current list of prohibited code shapes.  The policy codes below record concrete consequences and reviewable failure modes, but contributors should apply the discovery, ownership, locality, and dependency-direction model to new code even when no existing example names the exact violation.

## Preamble architecture specification

This section is the authoritative specification of construction ownership,
entrypoints, encapsulation, and computational delegation in the preamble.
It applies to new features, repairs, internal consumers, engine adapters,
catalogues, and session integration. An importable implementation is not thereby
a sanctioned entrypoint. A policy permitting private implementation machinery
does not permit a second mathematical API.

`AGENTS.md` routes contributors here. The category declaration, constructor,
and their docstrings give each operation's concrete contract; this specification
gives the architecture those declarations must realize. TODOs contain only the
unfinished delta to that architecture. They do not own architectural decisions
that would disappear when an item is completed. Historical proposals and examples
are reference material, not exceptions to this contract.

### Ownership and permitted dependencies

| Layer | Owns | Permitted dependency | Forbidden responsibility |
| --- | --- | --- | --- |
| Session and notation | The selected preamble language | Owned mathematical entrypoints | Backend exports, adoption helpers, alternative constructor languages |
| Mathematical categories and constructions | Defining objects and maps, hypotheses, elements, functorial behavior, public result types | Immediate mathematical owners and their sanctioned operations | Engine data inspection; reimplementation of inherited structure |
| Shared categorical runtime | Construction dispatch, generated owned types, cooperative initialization | Its declared framework interfaces and private host primitives | Theory-specific branches, backend mathematical identity, a second category graph |
| Private computation adapters | Lowering, established engine calls, representation correspondence, raising | Owned semantic inputs and the selected engines' supported interfaces | Public mathematical identity or taxonomy; raw results returned to mathematical consumers |
| External engines | Their maintained computational algorithms and internal representations | Their own dependencies and supported bridges | Defining the preamble's public API or accepting owned objects as foreign parents |

The shared framework boundary remains `sage-categories`: reuse its suitable
released interfaces for generic categorical/runtime work. Repair an existing
in-repo owner when that is the necessary current integration point; do not build
a competing framework or import a sibling checkout by filesystem path.
Suitability for class construction and suitability for mathematical computation
are separate questions. A package can supply the latter without supplying the
former.

### `OWN-01`: Name the semantic owner before selecting an implementation

- **Rule:** First perform the
  [mathematical dependency trace](#mathematical-dependency-tracing), independent
  of the implementation's current shape. Then read its defining category, immediate
  structure owners, current entrypoints, and consumers. Identify the owned input,
  output, structural maps, and exact operation needed. Search the megadoc and live
  source beyond the selected subtree for that operation, then inspect relevant
  upstream implementations. Reuse both the owned mathematical construction and
  the maintained computation; satisfying only one half is insufficient.
  Record actual missing foundations, missing structural relationships, and
  observed workflow friction in `COMPLAINTS.md` under `DEV-59`, even when found
  outside the selected implementation task. The complaint states the mathematical
  need; it does not authorize a bespoke replacement or a change of scope.
- **Rationale:** A private Sage call can bypass an owned localization just as a
  correctly named owned kernel can conceal a redundant local elimination algorithm.
- **Violation Example:** Start a geometry-specific matrix kernel because the
  selected geometry file does not implement kernels; reject CAP's computational
  categories because CAP does not generate Python classes.
- **Correct Example:** Geometry asks the owned complex for cohomology; the complex
  and module owners supply the structure, and their private adapters reuse an
  applicable established homology or module algorithm.

### `OWN-02`: Every construction route converges on one semantic constructor

- **Rule:** Each mathematical construction has one authoritative construction
  contract at its owning category or object. Operator notation, literal ingress,
  catalogue specimens, functor images, direct morphism construction, and raised
  engine results establish that same contract. Specialized routes supply the
  general constructor's defining datum; they do not allocate an alternative
  parent and attach enough methods to resemble its output.

  The public spelling follows `ARC-07` and `ARC-12`: morphisms are asked through
  `Mor`; operations are asked of their owners. A private implementation function
  is not a second public constructor. A named convenience route requires an
  actual mathematical input form and factors through the owner. No `from_engine`,
  `from_raw`, `trusted`, `unchecked`, or validation-disabling route admits weaker
  data. Host allocation and `_element_constructor_` implement this contract;
  they do not exempt a caller from it.
- **Rationale:** One semantic funnel makes an invariant apply to every way an
  object is obtained, instead of making correctness depend on caller diligence.
- **Violation Example:** The direct module constructor establishes a scalar
  action, but the backend-result constructor returns a parent without it.
- **Correct Example:** The owner establishes the defining action once; each
  supported representation supplies that action through the same construction.
  Backend specialization changes computation, not the constructor obligations.

### `OWN-03`: Construction establishes all inherited data before exposure

- **Rule:** Each category level introduces only its own mathematical datum and
  constructs through its immediate structure owners. The returned object has
  every datum required by its actual placement, including its element and
  morphism structures. Accessors recover that established datum; they do not
  reconstruct it from descendants, probe for hidden state, or repair placement
  when first called. Lazy realization is allowed only from complete defining
  data with a fixed owned codomain, not as delayed provision of missing structure.

  A property refinement retains the existing data. Adding a choice, action,
  multiplication, framing, or presentation supplies that structure through its
  constructor. Category membership alone never supplies missing data. The same
  rules apply to zero objects, empty families, identity maps, and boundary degrees.
  A specialization threads that construction by honest inheritance or composition
  with its actual owned instance, as required by `OWN-14`; equivalent independent
  implementations do not satisfy this rule.
- **Rationale:** Inherited method names without inherited construction data make
  invalid objects available for subsequent features to build upon.
- **Violation Example:** A DGA gets a cochain-complex category label but its
  differential interface cannot supply the zero components its declared grading
  requires; a formed object implements its own set operations.
- **Correct Example:** The DGA construction supplies the graded module and
  differential contract, then adds multiplication; generic complex operations
  consume that same differential. Each lower level owns its own inherited data.

### `OWN-04`: Public ownership is recursive and includes implicit operations

- **Rule:** Every mathematical value reachable through a public preamble operation
  is owned. This includes coefficients, base rings, indexing sets, family values,
  iterated elements, morphism endpoints, structural maps, cycles, boundaries,
  quotients, chosen representatives, and results of arithmetic and coercion.
  A lazy family or callable must return owned values when evaluated; owning its
  outer container is not enough. Public coordinate objects are themselves owned
  mathematics tied to their chosen framing, never foreign arrays.

  Public signatures, inherited methods, parser bindings, introspection-visible
  conveniences, and serialization/reconstruction routes obey the same closure.
  Python syntax/support values expressly allowed by the session contract are
  not permission to return foreign mathematical values. There is no exception
  for small integers, singleton rings, fast arithmetic, or a backend's
  particularly convenient element type.

  Encapsulation hides representation, not the mathematics: the defining action,
  form, framing, inclusion, projection, and other required structure remain
  available through their owned APIs. Returning opaque handles in place of
  these objects is not stronger encapsulation.
- **Rationale:** One reachable foreign constituent gives every downstream consumer
  a second API even when the outer parent appears owned.
- **Violation Example:** An owned cohomology module returns Sage cycle vectors;
  an owned family yields GAP elements; inherited arithmetic returns Sage scalars.
- **Correct Example:** A cycle representative is an element of the owned cycle
  module, its inclusion lands in the owned complex component, and its quotient
  image has the owned cohomology module as parent.

### `OWN-05`: Private means confined to a named owner, not merely underscored

- **Rule:** Store private representation fields only at their owning runtime or
  adapter boundary. Mathematical consumers use owned public operations, including
  when the consumer lives in the same repository or file. An underscore, a helper
  module, a friend-like import, or omission from `preamble.all` is not permission
  to access another owner's storage. Do not expose raw state through a newly
  public accessor, a neutral name such as `data`, an iterator, or a closure.

  A protected framework contract must be declared at its owner with its exact
  purpose, permitted implementing/calling roles, input/output types, maintained
  invariants, and reason ordinary public operations cannot implement that
  framework responsibility. It is invoked through the designated dispatcher.
  A comment at a consuming call site cannot create that authority. Protected
  mathematical contracts exchange owned values. Raw handles may move only among
  helpers of the same declared private computation/transport boundary; they do
  not cross into another mathematical subsystem.
- **Rationale:** Broad permission for a documented private call makes every
  inconvenient public contract optional.
- **Violation Example:** A lattice module imports a ring's private engine accessor
  and documents the import as a protected extension so it can run its own algebra.
- **Correct Example:** The ring or module owner exposes the missing mathematical
  operation. Its private adapter may share transport helpers internally while
  mathematical callers receive only the owned result.

### `OWN-06`: Engine inspection is local to an already selected computation

- **Rule:** Mathematical dispatch follows owned structure and hypotheses. Only
  the designated adapter may inspect foreign representation types or invoke
  engine-specific APIs after the owned operation is selected. Prefer supported
  upstream APIs. If an upstream private function is genuinely required, first
  check the public alternatives; document the exact upstream symbol, source,
  assumptions, and consuming adapter at that adapter's declaration. This grants
  no permission to inspect unrelated preamble internals or to export that function.

  No dynamic attribute forwarding, blanket delegation of unknown methods,
  runtime class mutation, public engine selector, backend option bag, or raw
  adoption constructor belongs on an owned object. Private host initialization
  and dispatch hooks are runtime implementation contracts, not escape routes.
- **Rationale:** Foreign implementation details need one repair site when upstream
  changes, and must not become the language used by mathematical consumers.
- **Violation Example:** Ordinary toric code spreads calls to private Sage sheaf
  helpers through several consumers; `__getattr__` forwards missing owned methods
  to a Sage parent.
- **Correct Example:** One toric adapter calls the source-grounded Sage helper
  when no suitable public operation supplies the needed data; it raises the
  result through the owned complex construction before returning.

### `OWN-07`: Raise results through the same construction without losing maps

- **Rule:** A private adapter lowers already-owned defining data, performs the
  engine computation, and raises the result through the relevant owned
  construction. Preserve the selected base ring, grading, action, presentation,
  and structural arrows. Record actual comparison morphisms whenever a change
  of representation requires them. An engine normal form cannot replace a
  chosen presentation silently. Matching an invariant such as dimension does
  not supply the required chosen isomorphism or presentation-comparison map.

  The computation and construction steps must not recurse: raising computed
  defining data enters the same semantic constructor without requesting the same
  engine computation again. Make that dependency explicit at the owning methods;
  do not solve recursion with a second unchecked constructor. If an engine
  supplies only dimensions, it supplies a dimension computation, not class
  representatives or induced maps. Obtain the missing data through an existing
  suitable operation before claiming the richer construction.
- **Rationale:** Correct numerical answers do not reconstruct the relationships
  that subsequent mathematics needs.
- **Violation Example:** Wrap the dimension of cohomology in a fresh vector space
  and expose it as the cycle quotient; discard basis-change maps during lowering.
- **Correct Example:** Raise the computed cycle and boundary data into the owned
  modules and maps, retain their quotient map, and derive the induced map from
  the supplied chain map through those structures.

### `OWN-08`: Reuse the highest suitable maintained operation

- **Rule:** Search by mathematical operation, equivalent standard formulations,
  required maps, and coefficient hypotheses, not only by the desired Python
  method name. Inspect existing dependencies first, then appropriate maintained
  systems. Compare the full result contract: exactness, characteristic, torsion,
  grading, presentations, representatives, and morphism action where required.
  Compose established operations when that supplies the contract. Calling one
  matrix routine inside a new local homology engine does not establish that
  the existing homology implementations were considered.

  Record the selected upstream operation and its actual uncovered semantic delta
  at the private adapter or owning construction. For a planned task, record the
  selection in the unfinished item and retain the durable contract at delivery.
  A new nontrivial algorithm needs the demonstrated gap and explicit ownership
  decision required by `ENG-06`. Moving a local algorithm to Julia, Singular,
  or a generic helper does not make it upstream-maintained.
- **Rationale:** Mature dependencies reduce the project's algorithmic correctness
  burden only when they actually own the corresponding computation.
- **Violation Example:** Rebuild syzygy or chain-reduction logic because a package
  has an inconvenient return type, a different class model, or missing packaging.
- **Correct Example:** Adapt an existing module-presentation or homology operation,
  adding only the owned construction and map conversion that the engine does not
  supply. Repair a bridge or packaging defect at its existing owner.

### Existing computation references

These are discovery starting points, not claims that one package computes every
instance. Check the relevant current documentation and local adapter contract.

| Required computation | Existing implementations to inspect |
| --- | --- |
| Chain-complex homology and cycle representatives | [Sage chain complexes](https://doc.sagemath.org/html/en/reference/homology/sage/homology/chain_complex.html); its documented implemented homology cases include integer coefficients and fields |
| Commutative DGA cohomology and products | [Sage commutative DGAs](https://doc.sagemath.org/html/en/reference/algebras/sage/algebras/commutative_dga.html); inspect the grading and degree range of each operation |
| Toric sheaf cohomology | [Sage toric divisors](https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/toric/divisor.html) and [equivariant bundle complexes](https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/toric/sheaf/klyachko.html) |
| Linear categories, presented modules, complexes | [CAP constructors](https://homalg-project.github.io/docs/CAP_project-based/constructors): LinearAlgebraForCAP, ModulePresentationsForCAP, FreydCategoriesForCAP, ComplexesAndFilteredObjectsForCAP |
| Polynomial and module algorithms | Sage, Singular, Macaulay2, and OSCAR through the existing private bridges; inspect the needed presentation and map outputs, not only an invariant |
| Standard polynomial-ring completions | [Sage multivariable polynomial completion](https://doc.sagemath.org/html/en/reference/polynomial_rings/sage/rings/polynomial/multi_polynomial_ring_base.html) and [lazy series](https://doc.sagemath.org/html/en/reference/power_series/sage/rings/lazy_series_ring.html) |

The [sage-categories README](https://github.com/dzackgarza/sage-categories/blob/main/README.md),
[complaints and reuse catalogue](https://github.com/dzackgarza/sage-categories/blob/main/COMPLAINTS.md),
and [engine-boundary specification](https://github.com/dzackgarza/sage-categories/blob/main/specs/leaves.md#computation-engine-boundary)
provide additional discovery context. Their historical findings are not a current
capability audit, and their framework-specific exceptions do not relax the
preamble's recursively owned public universe.

### `OWN-09`: Transport through structure, with the actual preservation theorem

- **Rule:** Construct functors on objects and morphisms, with their declared
  domain, codomain, variance, and required comparison maps. Inherited operations
  follow those structural functors only where the relevant preservation or
  creation result applies. Reuse the framework's composition, identities, and
  universal-construction interfaces; a leaf adds its new datum and genuinely
  specialized computation, not another implementation of general map calculus.

  Neither forgetfulness nor faithfulness implies preservation of every limit,
  colimit, quotient, or cohomology operation. State the theorem and its hypotheses
  at the owner; do not generate runtime boolean proofs of general categorical
  identities or undecidable equality. Distinct mathematical choices remain
  distinct even when an engine represents them by the same data.
- **Rationale:** Generic reuse without its hypotheses can propagate incorrect
  mathematics just as efficiently as correct mathematics.
- **Violation Example:** Treat every algebraic cokernel as the cokernel of the
  underlying linear map; implement scalar extension by changing stored ring
  fields without transporting the module and its structure maps.
- **Correct Example:** The relevant quotient owner constructs the required ideal
  closure before the quotient; scalar extension acts on the module and the
  defining action or multiplication through the same functorial construction.

### Required construction factorizations

These are semantic obligations, not additional global function names or a runtime
registry. Each row names the general owner through which its special cases pass.

| Family | Required construction and retained data | Specialization boundary |
| --- | --- | --- |
| Limits and colimits | The owned indexing category, diagram, universal cone/cocone, and induced maps under the [general contract](#limits-colimits-and-structured-specialization) | Product/equalizer and coproduct/coequalizer constructions, directed systems, and category-specific realizations implement the same construction through inheritance or composition |
| Ring localization | The commutative ring's localization at an owned multiplicative submonoid, with its structure map and universal factorization | Element inversion uses the generated submonoid; prime localization uses the prime complement; a domain's fraction field uses its nonzero elements |
| Scalar change | The existing scalar-change construction along an owned ring morphism, acting on objects and morphisms | Module localization uses the localization ring map; extra algebra/action/form structure is transported under the applicable hypotheses |
| Completion | The owned inverse system of ideal-power quotients, its transition maps, limit, source map, and projections | Series and adic engines realize supported instances privately; no finite stage becomes the completed object |
| Complexes and cohomology | The owned graded components and differentials; cycle inclusion, boundary inclusion, quotient, and induced maps | Chain/cochain conventions, coefficient hypotheses, and boundedness belong to the stated construction or computational case, never an implicit matrix convention |
| Differential graded algebras | The common complex and graded algebra structures, with the differential and multiplication compatibility | Cohomology multiplication is induced through those structures; a commutative-DGA engine does not cover arbitrary DGAs by renaming |
| Subobjects, quotients, and Homs | The existing inclusion/projection and fixed-endpoint `Mor` constructions | Coordinates enter only through the appropriate chosen framing/presentation and the same morphism constructor |

For localization, use [Stacks 02C5](https://stacks.math.columbia.edu/tag/02C5).
Locality is a consequence with hypotheses, not a property of every localization:
prime localization is local, whereas `ZZ[1/2]` retains distinct maximal ideals
generated by 3 and by 5. For completion use
[Stacks 00M9](https://stacks.math.columbia.edu/tag/00M9): the objects are the inverse
limits of `R/I^n` and `M/I^n M`. General completion is not assumed exact; comparison
with scalar extension requires its stated hypotheses. The limit contract does
not claim a general algorithm for computing arbitrary inverse limits. This is
not permission to restrict the general mathematical interface to finite diagrams:
apply the general contract below and specialize its realization.

### Limits, colimits, and structured specialization

**Place the theory at its most general mathematical owner, then specialize by
threading that owner through every refinement.** A completion, a directed union,
or a geometric construction does not own a separate theory of diagrams. This
section specifies the common architecture; `OWN-14` makes the same threading
requirement binding on all specialized constructions, not just limits.

#### Diagrams and universal constructions

For an ordinary category `C`, a diagram is a functor `D: J -> C`; maps of
diagrams of fixed shape are natural transformations. A limit is a terminal
cone over `D`; a colimit is an initial cocone under `D`. Their structural maps
and universal factorizations are part of the construction, not optional output.
Use the definitions in [Stacks, Limits and colimits](https://stacks.math.columbia.edu/tag/002D).

The owned language must express the index category, object and arrow families,
their source/target and composition, the functor, cone/cocone legs, and maps
between these objects. All constituents, including lazily returned values, use
the existing owned categories, Homs, functors and indexed families. A Python
iterator of engine values is not a diagram. A finite list of arrows does not
define an arbitrary category without its identities, composites and relations.

Smallness is relative to the declared foundations. Do not confuse small,
finite, countable, enumerable, and computationally presented. Support arbitrary
represented small shapes at this level, including parallel arrows and infinite
indexing; do not define the general interface using integer degrees, a maximum
stage, a matrix size, or finite traversal. Size hypotheses belong to the
mathematical contract; representation limitations belong to specific operations.

Establish functoriality, compatibility and universality through the sanctioned
mathematical constructions and their hypotheses. Do not try to validate an
infinite diagram by traversing every arrow, or treat a finite sample as proof
of its laws. Represented input must meet its declared construction contract;
an arbitrary callable plus a boolean claiming compatibility is not a substitute.
This is not permission to add an unchecked ingress or a runtime theorem registry.

A chosen universal construction retains its actual diagram and universal
cone/cocone, with access to their constituents through owned mathematics. Its
underlying result object alone need not determine its presentation. Distinct
diagrams may have isomorphic results, or share one canonical result object.
Keep each construction's data at that construction; never overwrite shared
object state with the latest caller's diagram. Nor should equality of result
objects be defined by equality of their chosen presentations.

#### Construction theorems supply general realizations

For a small diagram `D: J -> C`, the following formula constructs its limit
when the displayed products and equalizer exist:

```text
P = product over objects j of D(j)
Q = product over arrows a: i -> j of D(j)
u, v: P -> Q
component_a(u) = projection_j
component_a(v) = D(a) composed with projection_i
limit(D) = equalizer(u, v), with its induced projections
```

Thus the appropriate small products and equalizers suffice for small limits.
Empty products include the terminal-object case. The formula is categorical,
not an instruction to enumerate all factors or compute all compatible tuples.
See [Stacks 002N](https://stacks.math.columbia.edu/tag/002N).

The corresponding colimit construction is:

```text
A = coproduct over arrows a: i -> j of D(i)
B = coproduct over objects j of D(j)
u, v: A -> B
restriction_to_a(u) = coprojection_i
restriction_to_a(v) = coprojection_j composed with D(a)
colimit(D) = coequalizer(u, v), with its induced coprojections
```

The appropriate small coproducts and coequalizers suffice; the empty coproduct
supplies the initial object. Products alone do not impose compatibility, and
coproducts alone do not impose identifications. See
[Stacks 002P](https://stacks.math.columbia.edu/tag/002P).
These displays are mathematical pseudocode, not new public factory names.

Implement these theorem-backed realizations through the common construction's
sanctioned specialization boundary. Do not introduce a competing public
product-based limit API. Products and equalizers are themselves limits, so an
implementation must distinguish their defining diagram from a request to solve
that diagram again. The primitive category-specific realization supplies its
universal data to the common constructor without recursively requesting itself.
The same rule applies to coproducts and coequalizers. A general reduction is
not an excuse for constructor recursion or an unchecked allocation path.

For every specialized realization, identify the applicability theorem and the
actual computational operations it delegates to. An optimized realization
overrides the realization step of the inherited general construction, or
operates through the composed general instance under its declared contract.
It does not maintain a parallel limit implementation. Both the generic reduction
and its specialization use the same diagram, map, restriction, and
universal-factorization machinery. Select the applicable realization
by the established category/representation mechanism, not by catching an error
and silently trying a mathematically different construction.

#### Directed systems and finite restrictions

Use the common diagram language for directed and inverse systems. For a directed
poset `I`, direct systems use arrows `i -> j` for `i <= j`; inverse systems
use the opposite direction. Filtered categories generalize directed posets and
need not have at most one arrow between two objects. Their hypotheses must not
be replaced by a sequence convention. See
[Stacks, Filtered categories](https://stacks.math.columbia.edu/tag/002V).

Restriction is precomposition: an indexing functor `u: K -> J` gives `D o u`.
Retain `u` and the restricted diagram. In particular, expose requested finite
restrictions of represented systems without evaluating the whole infinite
diagram. A sequential system admits finite prefixes; a general directed system
requires explicit selected indexing data, not an invented canonical prefix.
A finite selection of objects is not necessarily a finite full subcategory:
its arrow sets can still be infinite. State what was selected.

When the relevant constructions exist, restriction induces

```text
limit_J(D) -> limit_K(D o u)
colimit_K(D o u) -> colimit_J(D)
```

These directions follow the universal maps, not a common untyped projection
operation. Diagram transformations induce maps between limits and between
colimits, preserving identity and composition. Reindexing comparisons follow
the appropriate initial/cofinal theorem when an isomorphism is claimed; neither
a finite sample nor a convenient subsequence is automatically sufficient.
See [Stacks, induced maps](https://stacks.math.columbia.edu/tag/002D).

Separate the full system, a restricted system, a stage object, the (co)limit of
a restriction, and finite information about an element. A stage can itself be
infinite. Finite restriction never turns the full object into a finite stage.
In inverse systems, compatible finite data need not extend to a compatible
global family. In direct systems, later arrows may identify elements distinct
at earlier stages; coprojections are not automatically injections.

For completion, the maps to `R/I^n` come from the retained quotient diagram;
the ideal and its powers supply the interpretation of a stage as precision.
That interpretation is completion-specific, while restriction and comparison
are general. Increasing precision cannot invent a lift from a bare residue or
certify equality from finitely many agreeing components (`OWN-10`).

#### Structured categories specialize the same mathematics

In `R`-modules, equalizers are kernels of differences and coequalizers are
cokernels of differences. Consequently the displayed reductions become a
submodule of a product and a quotient of a direct sum. Preserve the inclusion,
projection and universal maps, not just a module with matching invariants. The
direct-system quotient and its maps are described in
[Stacks 00D5](https://stacks.math.columbia.edu/tag/00D5).

Use the actual categorical products and coproducts. In commutative rings,
products are ring products, while binary coproducts are tensor products over
`ZZ`; the pushout of commutative ring maps `R -> A` and `R -> B` is
`A tensor_R B`. They are not coproducts of underlying modules. See the explicit
cones and universal maps in
[Mathlib's commutative-ring constructions](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/Ring/Constructions.html).
Do not transfer this commutative formula to arbitrary associative algebras.

Limits computed on underlying objects and colimits requiring further algebraic
or sheaf constructions must follow their own creation/preservation theorems
(`OWN-09`). An infinite product of finite-rank modules need not have finite
rank; a subcategory restriction must not silently change the target category.
Use maintained algebra, module, series, and geometric computations privately.
The general constructor owns the mathematical relationships, not a second CAS
implementation of every product or quotient.

#### Representation, existence, and homotopical structure

Keep distinct the ability to represent a diagram, the existence of its universal
object in the declared category, a chosen representation of that object, and
the computability of a requested operation. A source-backed construction may
represent an infinite universal object exactly without an eager enumeration or
general equality algorithm. Conversely, retaining a diagram alone is not a
proof of existence in a category lacking that limit. A formal system must stay
identified as a system; it cannot be relabeled an existing object of that
category. Any use of a different completion of the category requires its actual
mathematical construction and declared target.

Ordinary strict limits and homotopy limits are different mathematical requests.
Name the relevant category, equivalences and coherence before selecting their
realization; the ordinary equalizer formula is not a homotopy-invariant recipe
merely because its factors are spaces. Reuse established homotopical machinery
with its hypotheses. See
[Shulman, Homotopy limits and colimits and enriched homotopy theory](https://arxiv.org/abs/math/0610194).

For example, sequential spectra have pointed spaces and bonding maps
`Sigma X_n -> X_(n+1)`, with morphisms compatible with those maps; they are not
ordinary sequences `X_n -> X_(n+1)` obtained by forgetting suspension. Retain
the suspension/loop relationship and the chosen spectral and homotopical
structure when expressing finite portions or universal constructions. See
[Malkiewich, Definition 2.1.1](https://people.math.binghamton.edu/malkiewich/spectra_book_2026Jan09.pdf#page=84).
This example sets a generality boundary, not a prerequisite to implement stable
homotopy theory before repairing ring completion.

#### Evidence that a specialization remains threaded

For a selected realization, follow its inherited or composed general object
from construction through stage access, restrictions, universal factorization,
and a nonidentity induced morphism. All use the same diagram and structural
maps. A comparison with another valid realization respects those maps; agreement
of dimensions, printed expressions, or finite residues is insufficient.

Distinguishing specimens include a diagram with parallel arrows, both an empty
limit and empty colimit, a directed index with incomparable elements, an inverse
system with non-surjective transitions, and a direct system with non-injective
transitions. Select specimens for the contract being delivered, preserve broader
unfinished cases in TODO, and follow terminal T for execution (`DEV-58`). Record
observed missing foundations in COMPLAINTS, not invented failures inferred merely
from the breadth of this specification.

### `OWN-10`: Representation state cannot alter mathematical meaning

- **Rule:** Defining owned data is authoritative. Backend workspaces, caches,
  finite precision, normalization state, and transport handles are private
  realizations of that data. Reuse existing cache/lifetime mechanisms with keys
  respecting the owned construction's actual choices. Replacing an engine,
  increasing precision, or populating a cache does not by itself change the
  object's mathematical identity, defining maps, or category. A newly established
  mathematical property may justify refinement; engine identity never does.

  Exact equality, zero, membership, and hashing cannot be inferred from a lossy
  projection or an engine's inconclusive boolean. Apply `DEV-51` and `DEV-52`.
  Unsupported computation fails at its documented boundary; it never returns
  a foreign object, an approximation under an exact name, or an invented answer.
- **Rationale:** Private storage otherwise becomes a second source of mathematical
  truth and can contradict the structure the constructor established.
- **Violation Example:** Treat one truncated series residue as the exact element,
  or cache two differently framed objects under the same engine normal form.
- **Correct Example:** Retain the exact defining object and its projection maps;
  precision describes available computational information about its elements.
  A new presentation comes with the owned change-of-presentation map.

### `OWN-11`: A missing shared operation is repaired at its owner

- **Rule:** If the sanctioned path is absent, recursive, awkward, slow, or
  insufficient, identify the exact missing datum or operation at its owner.
  Repair that prerequisite and route the selected consumer through it. Source
  locality, elapsed effort, a passing example, or a smaller diff cannot justify
  a second constructor, a private-field read, or a copied algorithm. Existing
  violations are repair sites, not precedents for new code.

  Keep the repair bounded to the actual dependency and its affected consumers.
  Do not prebuild all of category theory, add a new registry, or start a framework
  rewrite to avoid the concrete construction. If the required owner cannot be
  changed within the granted scope, report that owner and obstruction; continue
  independent work, but leave the dependent capability unfinished. An exception
  requires an explicit user architectural decision, recorded here and at the
  affected contract, not a worker-authored justification for convenience.
- **Rationale:** Otherwise the easiest local route becomes the rewarded route,
  while each apparent feature increases future repair and maintenance work.
- **Violation Example:** Add another direct fraction-field allocation because
  routing through localization would require repairing localization.
- **Correct Example:** Complete that localization case and its map, then obtain
  the fraction field through it; other localization consumers share the repair.

### `OWN-12`: Acceptance includes the path, not just the final invariant

- **Rule:** Review the actual public entrypoint, defining-data construction,
  inherited operation, private lowering/computation/raising boundary, and a
  nonidentity induced map where the feature has one. Compare every alternative
  route touched by the work against the same semantic contract. Reject a correct
  invariant obtained through an unsanctioned path. A conforming specimen must
  expose the owned constituents and their mathematical relationships, not merely
  an outer type, engine call count, or dimension.

  Establish architectural reuse by reading the implementation and upstream
  contract. Mathematical specimens establish observable behavior; do not turn
  them into source scanners or mock expectations that a particular helper was
  called. Respect the protected expectation subtrees and `DEV-58`: written
  specimens remain unverified until the authorized execution phase. A policy
  edit specifies the architecture; it does not establish code conformance.
- **Rationale:** Numerical agreement alone rewards a shortcut that leaves the
  construction and its future consumers structurally wrong.
- **Violation Example:** Close a cohomology task after matching Betti numbers
  while representatives or induced maps still escape to Sage; call a moved
  private algorithm delegated because its Python caller became shorter.
- **Correct Example:** Source review follows the shared construction and real
  maintained algorithm. The mathematical specimen composes the owned inclusion,
  quotient map, and induced morphism and distinguishes the promised behavior
  from a dimension-only substitute.

### `OWN-13`: Declarations identify sanctioned entrypoints and private boundaries

- **Rule:** At each construction's existing declaration, document its owning
  category/object, canonical signature, defining datum and maps, admissible input
  forms, required output structure, and how each specialization factors through
  it. At each adapter declaration, document the semantic operation it implements,
  its owning caller, the upstream operation, representation hypotheses, and
  lowering/raising correspondence. Keep these contracts beside their source,
  not in a second constructor registry or manually synchronized status table.

  Public mathematical names describe mathematics. Private implementation classes,
  allocation helpers, conversions, and adapter-only imported engine symbols use
  leading underscores and are excluded from public exports. Engine names belong
  in private adapter names where that makes their boundary clearer, never in
  public operation names. Internal consumers import the defining owner rather
  than a session aggregator, and invoke its sanctioned operation rather than an
  implementation class. Access scope follows the declared role, not the physical
  file: putting consumer and adapter code together does not authorize raw access.
- **Rationale:** A constructor or helper whose allowed callers are unspecified
  becomes an alternate API through ordinary imports and copied examples.
- **Violation Example:** Export a concrete module implementation because one
  sibling needs its unchecked initializer; call a raw conversion `normalize`
  and omit its backend-specific input/output contract.
- **Correct Example:** The module category documents its presentation constructor;
  a private adapter documents its one computational responsibility. Their source
  declarations and exports make the mathematical entrypoint distinguishable from
  the backend conversion without requiring another policy registry.

### `OWN-14`: Specializations inherit or compose their general construction

- **Rule:** A specialized construction is implemented by honest inheritance from
  the general owned construction, or by composition with an actual instance of
  it. Declare which relationship is used at the existing owner (`OWN-13`). This
  applies to every mathematical refinement, not only the
  [limit and colimit contract](#limits-colimits-and-structured-specialization).

  Inheritance initializes the general defining datum and retains its operational
  contract. Overrides supply only the specialized datum or theorem-backed
  realization. A category label, class ancestry, or copied method body is not
  enough when inherited operations have missing state or disagree with the leaf.

  Composition stores the actual owned general construction and delegates its
  general operations to that instance. The specialized object adds its own
  mathematical structure and the maps relating the two. A diagram accessor or
  metadata-only object attached to an independent implementation is not this
  relationship. Neither is a second general object reconstructed for each call.

  Keep a single authority for defining data, universal maps, restrictions and
  induced morphisms. Do not keep parallel mutable copies in the specialized and
  general objects. A mathematical comparison between distinct presentations is
  allowed and must be owned, but an isomorphism does not excuse duplicating the
  general implementation. Thread specialized computation through the shared
  constructor without eagerly computing a second, generic realization merely
  to prove that the architecture was followed.

  Change the shared contract and its dependent consumers together. A leaf may
  not hide an inherited operation, weaken its inputs, discard its maps, or add
  a second implementation because the general owner is awkward to use. Repair
  that owner under `OWN-11`. Runtime optimization changes a realization, not
  which construction defines the object.
- **Rationale:** Parallel implementations can agree on one answer while drifting
  on inherited operations, maps, precision, and subsequent refinements.
- **Violation Example:** construct a series ring independently, attach an inverse
  system for display, and separately implement truncation and induced maps; claim
  that matching a generic limit on examples establishes architectural reuse.
- **Correct Example:** a completion inherits the chosen inverse-limit
  construction or contains that construction and delegates to it. A maintained
  series engine realizes its supported ring operations privately. Diagram
  restriction and universal maps still come from that same general construction.

### `OWN-15`: The underlying object is defining construction data, never a post-hoc view

- **Rule:** When a mathematical object is obtained by adding structure to an
  existing owned object, construct the weaker object first and retain that exact
  object as part of the stronger object's defining data.  The stronger object
  is then the weaker object together with additional selected datum and the
  canonical structural maps.  An accessor such as `underlying_set()`,
  `unformed_module()`, `base_scheme()`, `source_object()`, or `forget_*()` exposes
  that already-constructed object/map; it does not synthesize a fresh isomorphic
  object from dimensions, labels, coordinates, category membership, or other
  metadata.

  This applies whenever the mathematics has a canonical construction chain:
  `S -> Free_R(S)`, a module plus a form, a module plus a group action, an algebra
  over its underlying module, a graded object over its underlying object, a
  subobject with its inclusion, a quotient with its projection, a scalar change
  with its unit/counit/comparison map, a scheme over its coordinate algebra, or
  a functor image with its source provenance.  The chain is construction data,
  not documentation about a separately implemented object.

  Lazy realization is permitted only for computation *inside* an already fixed
  underlying object.  It is not permission to postpone deciding what the
  underlying mathematical object is until a method is first called.
- **Rationale:** Reconstructing the weaker object later creates a second source
  of identity and lets generic operations drift from the object whose structure
  they are supposed to inherit.
- **Observed defect:** lattice construction already created a concrete
  `FreeModuleOn(R,S)` and stored it as `_module`, but lattice-level accessors then
  maintained parallel generator/index state and `unformed_module()` returned the
  lattice itself rather than that stored module.  The correct underlying module
  existed but was bypassed by the public surface.
- **Correct Example:** construct `M = FreeModuleOn(R,S)` once; construct the
  lattice from `(M,b)`; `unformed_module()` returns `M`; every generic module
  operation is delegated or transported through that same `M` and the canonical
  comparison maps.

### `OWN-16`: Forgetting or adding structure is represented by actual structural maps

- **Rule:** If a stronger object is represented by a distinct parent from its
  weaker object, forgetting and re-equipping structure are real owned morphisms
  between those parents.  Their endpoints are the actual stored objects from
  `OWN-15`, and when the construction is carrier-preserving the maps are the
  canonical mutually inverse identifications of those represented carriers.
  Do not replace them by an identity endomorphism of the stronger parent merely
  because the elements use the same coordinates internally.

  Returning `self` from an underlying-object accessor is correct only when the
  mathematical construction intentionally uses the same owned parent as both
  objects and no distinct choice of added structure must remain observable.
  A category refinement alone does not prove this.  If two different forms,
  actions, gradings, framings, or presentations on the same weaker object must
  be distinguishable, then the stronger objects cannot both forget to themselves.

  Generic algorithms on the weaker theory compose with these structural maps;
  they do not duplicate the algorithm on the stronger parent.  Specialized
  algorithms may improve computation but must agree with the transported generic
  operation.
- **Rationale:** Treating forgetful structure as an identity of the wrong parent
  erases the construction history and makes it impossible to state correctly
  which object a generic map or theorem acts on.
- **Observed defect:** lattice `forget_form_morphism()` and
  `equip_form_morphism()` were both implemented as the identity on the lattice,
  even though the constructor retained a separate free module and the generic
  `FormedModules` implementation already models the two canonical maps correctly.
- **Correct Example:** a formed copy `L` of `M` stores `M`; `forget : L -> M`
  and `equip : M -> L` transport the selected generators/elements and are inverse
  module isomorphisms.  The form lives on `L`; generic module operations may be
  computed on `M` and transported through these maps.

### `OWN-17`: Accessors expose established structure; they never complete construction retroactively

- **Rule:** A public accessor is observational.  It may return stored defining
  data, a canonical map from those data, or a lazy mathematical view whose
  identity was fixed at construction.  It may not create the missing underlying
  object, selected generating set, framing, presentation, category placement,
  or structural map merely because the user asked for it.

  In particular, a method inherited from a category is evidence that the
  constructor already supplied the datum that method names.  If calling
  `module_generators()` causes the object to manufacture a new generator-family
  wrapper because no canonical generator object was retained, or if calling
  `presentation()` first allocates the presentation that should define the
  object, construction is backwards.  Repair the constructor/owner; do not make
  the accessor a hidden second constructor.

  Caching an accessor result does not cure this violation.  “Construct once on
  first query” is still post-hoc construction unless the result is merely a
  realization of defining data whose mathematical identity was already fixed.
- **Rationale:** Retroactive construction makes object validity depend on which
  methods happened to be called and rewards synthetic compatibility layers over
  honest reuse of general constructors.
- **Observed defect:** lattice `module_generators()` constructed a new
  `IndexedFamily` every time its cache was empty, despite the lattice constructor
  already having built the free module and its canonical generating data.
  Similar labels such as `Free-module generator family` and `Presented-module
  generator family` show the same tendency to manufacture an interface object
  instead of exposing the construction that already owns the generators.
- **Correct Example:** `Free_R(S)` owns the canonical basis map at construction;
  `module_generating_set()` exposes `S`, `module_generator(s)` evaluates the
  stored unit/basis map, and `module_generators()` exposes its represented image
  when that image is mathematically a set.

### `OWN-18`: Generic operations are owned by the weakest sufficient structure

- **Rule:** The public meaning and codomain of an operation are determined by the
  weakest mathematical structure that defines it.  A refinement may provide a
  faster implementation or additional specialized operations, but it does not
  silently specialize the generic operation's result type, display vocabulary,
  or ontology.

  If `module_generators()` is defined for framed/free modules, a lattice that is
  a formed free module uses that same module-theoretic operation.  The result is
  not a “lattice generator family” merely because the receiver is internally
  refined as a lattice.  A lattice-specific generating object is justified only
  when extra lattice mathematics is genuinely selected — for example a simple
  root basis carrying root-system structure — and then it belongs to a distinct
  lattice/root operation whose stronger codomain is part of its contract.

  Apply this rule through all forgetful towers: groups versus sets, algebras
  versus modules, formed versus unformed modules, graded versus ungraded objects,
  schemes versus underlying spaces/rings where appropriate, and specialized
  morphism categories versus their underlying Homs.
- **Rationale:** Otherwise every refinement forks generic concepts into a swarm
  of cosmetically specialized wrappers, leaking implementation taxonomy and
  destroying compositional reuse.
- **Observed defect:** `L.module_generators()` returned an `IndexedFamily` named
  `Lattice-generator family`; free modules independently used `Free-module
  generator family`.  Neither name described additional mathematics of the
  returned generators.  The refinement leaked into a generic module operation.
- **Correct Example:** both the free module and a lattice built from it expose
  the same canonical generator set/image at the module level.  A separate
  `simple_roots()` or similarly standard refined operation may return a richer
  root object when that structure actually exists.

### `OWN-19`: One defining datum has one authority throughout a construction chain

- **Rule:** Do not maintain parallel copies or parallel owners of the same
  mathematical datum.  An indexing set `S`, selected generating map, relation
  family, grading, action, form, presentation, or universal arrow is established
  once at its owner and referenced by stronger constructions.  A descendant may
  retain a direct reference or canonical map to it; it may not copy it into a
  second `_indices`, `_generators`, `_presentation`, or equivalent field and then
  implement generic operations against the copy.

  A second datum is legitimate only when it is mathematically distinct: another
  presentation, another basis, another form, another grading, etc.  Then the
  distinction is explicit and the comparison map is first-class.  Equality of
  values or current synchronization is not enough to identify two authorities.

  Review constructors by following defining data forward: each datum should have
  one creation point and thereafter flow by reference, functorial image, or
  canonical morphism.  If two fields can disagree without violating Python type
  invariants, the architecture already permits an impossible mathematical state.
- **Rationale:** Parallel state is the source of drift, duplicated validation,
  accidental recomputation, and contradictory displays.
- **Observed defect:** the lattice stored an actual free module whose
  `module_generating_set()` was authoritative, while `IndexedGenerators` also
  installed a lattice-level `_indices`; lattice module methods then read the
  latter rather than delegating to the former.
- **Correct Example:** `S` belongs to `M = Free_R(S)`; the lattice stores `M` and
  the form.  Any indexing needed for printing or coordinate realization is
  derived from `M.module_generating_set()` rather than stored as an independent
  mathematical authority.

### `OWN-20`: Essential-image claims require using the functorial construction, not imitating it

- **Rule:** When an object is claimed to lie in the image or essential image of
  a standard owned functor/construction, build it through that construction (or
  retain an actual object and specified isomorphism from that construction).
  Do not independently implement an object with equivalent-looking methods and
  then infer after the fact that it “is” a free module, quotient, localization,
  scalar extension, product, completion, or other standard construction.

  For a free object this means the source object and unit are defining data.  If
  the theory says `M = Free_R(S)`, then `S -> U(M)` is not metadata reconstructed
  from a basis after allocation; it is the unit/generating map used to construct
  `M`.  For an object only *isomorphic* to a free object, retain the chosen
  isomorphism rather than silently replacing its presentation by `Free_R(S)`.

  The same distinction applies to equivalence versus equality throughout the
  project.  Being abstractly isomorphic to the output of a construction does not
  license bypassing the construction when its selected source and structural
  maps matter to subsequent mathematics.
- **Rationale:** Method-level imitation loses the universal maps and chosen data
  that make a standard construction reusable and makes later code rediscover
  them from coordinates.
- **Observed defect:** the lattice implementation did create `Free_R(S)` but then
  behaved publicly as though lattice-level generator/index machinery were the
  source of its module structure.  That pattern is the same failure one would
  get from never constructing `Free_R(S)` at all: the functorial construction is
  no longer the authority for its own consequences.
- **Correct Example:** construct `Free_R(S)` with its unit, use that exact module
  as the unformed object of the lattice, and let every generic free-module
  consequence flow from it.  The lattice contributes only the additional form
  and form-specific mathematics.

### `OWN-21`: Interactive display is a semantic projection, not implementation introspection

- **Rule:** `repr`, LaTeX/`show`, rich display, and displays of returned
  collections must present the mathematical object/result at the abstraction
  level of the public operation that produced it.  They may use cheap canonical
  defining data, category placement, invariants, finite members, or a bounded
  lazy window, but they must not expose private class names, storage notation,
  backend coordinates, refinement/classifier names, or implementation-family
  labels unless those are themselves part of the mathematics requested.

  Every default display must provide positive information about the particular
  object.  Repeating the noun phrase of its type is not information.  Removing
  the implementation/type name from the user's memory should still leave the
  display useful.  Conversely, adding more internal words does not make a display
  informative if those words describe routing rather than mathematics.

  A public preamble-owned object must never fall back to Python's object-address
  representation (`<... object at 0x...>`), and a public `_repr_`/`_latex_` must
  never delegate wholesale to a private backend/engine object's display.  Even
  when that backend currently prints familiar mathematics, its notation and
  future changes are implementation details.  Cross the represented data back
  into owned mathematical syntax and render that syntax here.

  Display must not perform expensive classification, enumerate an unknown or
  infinite object, mutate caches in a mathematically significant way, or create
  missing structure.  It observes the defining data fixed under `OWN-15` through
  `OWN-20`.
- **Rationale:** Interactive display is part of the mathematical API.  A user
  inspects an object to learn what was constructed, not to discover which
  internal refinement or sparse representation happened to implement it.
- **Observed defects:** `Lattice-generator family` and `Natural numbers` merely
  renamed types; `1*B['alpha']` exposed sparse free-module storage; `placed map`
  hid even the map's domain/codomain.  Each output discarded mathematical data
  already available at negligible cost.
- **Correct Examples:** `{e_0, e_1}` for the canonical finite generator image;
  `NN = {0,1,2,...}` for the natural numbers; a pointwise-defined map displays
  its source and target when no closed formula is represented; a free object may
  display `Free_R(S)` together with a useful view of `S`.

### Construction-chain review protocol

For any constructor that adds structure, review the construction chain before
reviewing leaf methods.  This is a source-review discipline, not a request for a
new static checker, certificate, registry, or generated compliance report.

1. **Write the mathematics first.** State the weaker object `Y`, the added datum
   `d`, the stronger object `X=(Y,d)`, and every canonical map relating them.
   If the construction is functorial, name the functor/unit/counit or structural
   arrow that supplies the relationship.
2. **Find the unique construction of `Y`.** There must be one owned source of
   truth.  If no actual `Y` is constructed, determine whether honest inheritance
   supplies it; otherwise the stronger constructor is imitating a weaker theory.
3. **Follow identity, not equality.** Confirm that `X` retains that exact owned
   `Y` or an explicit chosen isomorphism when only equivalence is intended.
   Reconstructing an equal/isomorphic object later is not reuse.
4. **Follow every defining datum forward.** Index set, framing, presentation,
   grading, form, action, inclusion/projection, and source/codomain data should
   be created once and thereafter referenced or transported.  Search for parallel
   fields and parallel constructor calls that can drift.
5. **Inspect the forgetful direction.** `underlying_*`, `unformed_*`, `forget_*`,
   restrictions, and generic inherited operations must land in/use the actual
   weaker object.  Returning `self` requires a mathematical reason, not shared
   coordinates or class ancestry.
6. **Inspect the structure-adding direction.** The unit/equip/inclusion/comparison
   map must have the actual weaker and stronger objects as endpoints.  Test a
   nontrivial element/map, not only identities or dimensions.
7. **Inspect generic methods at the weakest owner.** A descendant should normally
   inherit/delegate module/set/group/etc. operations.  An override needs genuinely
   stronger mathematics, not access to more internal state.
8. **Inspect accessors for hidden construction.** A getter may realize a lazy
   computation but may not create the first canonical underlying object, family,
   presentation, or structural map.  `@cached_method` does not make such creation
   legitimate.
9. **Inspect the displayed result.** The display should reveal the mathematical
   result of the public operation and cheap defining data, not the internal leaf
   category, implementation class, backend notation, or a noun phrase naming its
   type.
10. **Inspect downstream consumers.** They should compose the retained objects
    and maps rather than reopening coordinates or reconstructing the same
    construction independently.

Immediate red flags discovered in prior repository work include:

| Red flag | Architectural diagnosis | Required direction |
| --- | --- | --- |
| A structured object stores `_module`, `_underlying`, `_source`, etc., but its `underlying_*()` accessor returns `self` | the real weaker object exists but the public construction bypasses it | return/reuse the stored object and build the actual structural maps |
| A constructor builds `Free_R(S)` while the descendant also stores `_indices` or another copy of `S` | two authorities for one defining datum | make `Free_R(S).module_generating_set()` authoritative |
| `module_generators()` / `relations()` / `presentation()` first allocates a wrapper describing data that should already define the object | accessor is acting as a hidden constructor | construct/retain the mathematical datum at the owning constructor |
| Generic operation results are named `Lattice-*`, `Group-*`, `Scheme-*`, etc. only because the receiver is refined | internal category refinement leaked into a weaker public operation | return the result type/display owned by the weakest sufficient structure |
| A free-module generator prints as `1*B['alpha']` | storage coordinates escaped as mathematical syntax | render the selected formal generator/linear combination |
| A display says only `Lattice-generator family`, `Natural numbers`, `placed map`, or another type paraphrase | zero mathematical information gain | show defining data, endpoints, members/window, invariants, or canonical notation |
| An isomorphic replacement is reconstructed from rank/dimension/labels while the original object is available | equality/isomorphism substituted for construction provenance | retain the original object or explicit chosen comparison map |
| Category membership is used as evidence that framing/action/form/presentation data must exist | property/type label substituted for selected structure | require the constructor to supply the actual datum |

These are examples of the general policies `OWN-15` through `OWN-21`, not an
exhaustive blacklist.  When a new instance has the same generator, repair the
construction owner; do not mint a narrower exception or a detector for the one
spelling that happened to expose it.

### Contributing a category: the procedure

This is the order of work for adding, moving, splitting or retiring a category.
It exists because the declared graph read on 2026-09-16 was the sum of locally
defensible edits: thirty categories under `Sets()`, a hand-meshed block of 135,
four notions each under two names, restriction of scalars declared on three
bases, a diamond through two different objects.  None of those was wrong at the
moment it was written, from where its author stood.  The procedure moves the
author to where the errors are visible, which is the mathematics first and the
whole graph second, and it makes each step leave evidence in the commit body.

**How the graph drifts, so that the steps below read as remedies.**  A
category is minted where a consumer needs it and named from that vantage, so
one notion acquires a second name (`FormedModules` beside `FormModules`).  A
property is written as a class because a class is what the language offers,
and then a class per combination follows, so a product of independent axes
becomes a mesh of hand-declared diamonds (`FinitelyPresentedQuadraticFormModules`).
A supercategory is chosen because it makes construction succeed or a method
resolve, so `Sets()` and `Objects()` become placeholders and `Schemes` is
declared beside `QuasiAffineSchemes` for safety.  A functor across a base is
declared as an inclusion because both are true sentences (`Modules(R) ->
Modules(S)`).  A consumer is left behind by a rename, and a lazy export table is
added so the package still imports, which hides the dangling import for a year.
Each step is local, each is defensible, and the disorder is only visible in
aggregate, which is why the instrument runs on every declaration change.

1. **State the notion in the field's words, with no implementation names.**
   Objects, morphisms, the defining datum, the hypotheses, and the reference
   that defines it (Stacks tag, Bourbaki chapter, the paper).  Apply
   [mathematical dependency tracing](#mathematical-dependency-tracing): the
   categories the definition passes through, down to ones the tree must own,
   each a real category with a literature name.  Do not open the tree yet;
   reading the tree first makes its current contents decide what is true.
2. **Classify every level of that chain.**  A property of the objects with no
   chosen datum is an axiom on the base that first states it (`CAT-17`).  A
   chosen datum is a data subcategory, a class that declares the axiom it
   truncates to.  A construction on a category (G-objects, direct-sum
   decompositions, arrows, presheaves) is parameterized by that category and
   declares it (`CAT-20`).  An object constructor is the category applied to
   the object's data and is not a category at all.  A combination of
   properties is a join and gets no class (`CAT-18`).
3. **Survey the tree, level by level.**  `just category-graph by-supercategory`
   for the parent each level would declare; `just category-graph json` with
   `jq` for who owns an operation; `rg` on the nouns of each definition across
   `categories/`; the expectation files under `tests/constructions/`,
   `tests/user_simulations/` and `tests/conftest.py` for the names the
   specification uses.  Record each level as: exists; exists under another
   name, which is retired into the owner (`CAT-22`); or missing.
4. **Reuse axioms before naming any.**  `sage.categories.category_with_axiom.all_axioms`
   and the base's nested axiom classes first.  A new name is the reference
   text's word, registered once; a property relative to a different structure
   is qualified in Sage's idiom (`FinitelyPresentedAsAlgebra`) so that it does
   not collide with the module meaning (`CAT-19`).  Two established names is a
   choice, not coining.
5. **Build what is missing from the top down.**  The deepest missing
   intermediate category first, declaring its one immediate parent, then the
   next, then the leaf.  A leaf written before its intermediates is a leaf that
   declares two levels up, and that edge is never removed later.
6. **Wire the leaf onto the deepest existing node.**  Its declaration is the
   most specific category the tree can spell, as a join where it is one:
   `Schemes(R).Affine().FiniteType().Smooth()`, not `AffineSchemes(R)` beside a
   list of properties the join already composes.  One entry, unless the object
   is genuinely two structures at once (a ring and a module), in which case
   write both and say in the commit body why the two routes are the same
   functor (`CAT-21`).
7. **Keep every change of base or parameter out of the list.**  Restriction of
   scalars, base change, the passage from an ideal to a fractional ideal or from
   an `R[G]`-module to a `G`-object over `R`: each is a functor obtained from
   the category by a method named for the construction (`CAT-16`).  Sage
   applies every axiom along a declared edge, so such an entry is a false
   theorem for every relative property.
8. **Write the declaration as expressions a reader can resolve** (`CAT-24`):
   names and parameters, no locals, no method calls on `self` that compute a
   category.  `extra_super_categories` on an axiom class states a genuine
   implication over the same base and nothing Sage's join already supplies.
9. **Read the graph before and after** (`CAT-25`): `shape`, `cells`, `audit`,
   and `just preamble-imports`.  The breadth of the target does not grow, no
   shortcut appears, no piece splits off, and any new generator owing a cell is
   named in the commit body with the theorem that fills it.
10. **Deliver the consequences in the same commit.**  Consumers of a retired or
    renamed name are rewritten (`CAT-26`); a name the specification requires
    survives as a thin function returning the category (`CAT-27`); the TODO
    node the change delivers is removed with its edges; the delta from step 9
    is in the body.
11. **When the honest parent is not in the tree, stop and say so.**  Build it
    if steps 1 to 5 defined it; otherwise leave `super_categories` abstract so
    the category refuses to construct, and record the missing category in
    `COMPLAINTS.md` with its dependency path and in `TODO.md` as a node the
    consumer needs.  Never a placeholder, never a mechanism that makes the
    construction proceed (`DEV-65`).

The procedure in one line: define, classify, survey, reuse, build top-down,
wire to the deepest node, keep functors out of the list, write resolvable
expressions, read the graph, deliver the consequences, and stop where the
mathematics is missing.

## Corrective implementation style guide (`STY-*`)

This is a **living catalogue of concrete code shapes**.  Add a new entry whenever review identifies a recurring implementation pattern whose replacement is known.  Do not wait for the same mistake to recur in several files.  The point is to teach the repository's preferred constructions—not merely to ban today's instances.

The default order of preference is:

1. an owned mathematical operation on the category/parent/element/morphism/Homset/functor that owns the notion;
2. a mature library abstraction (`itertools`, `collections`, `functools`, graph/group/CAS APIs, etc.);
3. a declarative Python expression (comprehension, generator expression, `any`, `all`, `sum`, `min`, `max`, `next`, dictionary union, etc.);
4. an explicit stateful loop only when state evolution is actually the algorithm.

An explicit loop is not intrinsically bad.  Search, fixed-point iteration, backtracking, dynamic programming, state-machine protocols, and backend algorithms may be clearest as loops.  The smell is an imperative loop whose only job is to spell a standard map/filter/fold/group/traversal operation manually.

### One-shot red-flag lookup

Use this table during review before reading the longer entries below.  Each left-hand shape should immediately suggest the right-hand replacement; if the replacement is mathematical data rather than private Python data, use the owned mathematical construction first.

| Red flag | First replacement to consider |
| --- | --- |
| `result = []; for x in xs: result.append(f(x))` | `[f(x) for x in xs]`, `map(f, xs)`, generator, or owned image/family |
| `result = []; ... if p(x): result.append(x)` | `[x for x in xs if p(x)]` / `filter(p, xs)` |
| `result = []; for block in blocks: result.extend(block)` | `itertools.chain.from_iterable(blocks)` |
| `sum(rows, [])` | `itertools.chain.from_iterable(rows)` |
| `result = set(); ... result.add(f(x))` | `{f(x) for x in xs}` / `set(map(...))` / owned set |
| `result = {}; ... result[key] = f(x)` | dict comprehension |
| `d.setdefault(key, []).append(value)` | `collections.defaultdict(list)` or `itertools.groupby` for sorted streaming input |
| `d[key] = d.get(key, 0) + 1` | `collections.Counter` |
| `d[key] = d.get(key, zero) + value` | finite-support abstraction / `defaultdict` |
| `total = zero; ... total += term` | owned finite sum/`linear_combination`; otherwise `sum(..., start=zero)` |
| `product = one; ... product *= factor` | owned `product`; numeric `math.prod(..., start=one)`; otherwise `reduce(mul, ..., one)` |
| nested `for a in A: for b in B:` producing all pairs | `itertools.product(A, B)` or owned Cartesian product |
| hand-built subsets/tuples of fixed size | `itertools.combinations` / `combinations_with_replacement` / `permutations` |
| manual first `n` values | `itertools.islice` |
| manual running partial sums/products | `itertools.accumulate` |
| `for x in xs: if not p(x): return False` | `all(p(x) for x in xs)` |
| `for x in xs: if p(x): return True` | `any(p(x) for x in xs)` |
| `for x in xs: if p(x): return x` | `next((x for x in xs if p(x)), default)` |
| manual count with `count += 1` | `sum(p(x) for x in xs)` / `Counter` |
| manual min/max tracking | `min` / `max(..., key=...)` |
| `for x in xs: yield x` | `yield from xs` |
| `for x in xs: yield f(x)` | generator expression / `map(f, xs)` |
| `for i in range(len(xs))` only to pair position/value | `enumerate(xs)` |
| indexing two equal-length collections in parallel | `zip(left, right, strict=True)` |
| repeated `labels.index(x)` inside a loop | owned `rank(x)` or one precomputed rank map |
| list used as FIFO frontier | `collections.deque` |
| hand-built orbit closure | owned action/G-set `.orbit(...)` or GAP/Sage backend |
| hand-built connected components/reachability | Sage/networkx graph API |
| hand-built multiplicity map | `Counter` / owned multiset |
| hand-built ordered deduplication | owned ordered set; private `dict.fromkeys` when appropriate |
| `try/except` in mathematical code | remove exception-driven control flow; assert the mathematical hypotheses and call code that is total under them; catch/translate failures only in engineering adapters |
| `x = f(...); return x` | `return f(...)` unless `x` names a mathematical intermediate |
| `if p: return True; return False` | `return p` |
| whole method is `assert False` / immediate failure | Sage `@abstract_method` for a genuine abstract contract, or correct mathematical placement; an assertion fallback is valid only after real implemented computational cases |
| `assert mathematical_hypothesis` | normally **keep or add it**: assertions loudly state the proof context; move the method only when the operation itself belongs to a narrower mathematical category |
| `hasattr/getattr/isinstance` to discover owned structure | category/method placement; private engine dispatch only at backend boundary |
| module-global `*_CACHE = {}` for canonical objects | shared memoization / `UniqueRepresentation` / `cached_function` |
| repeated `foo = OtherClass.foo` | common superclass/category implementation/delegation |
| repeated cross-engine convert→compute→convert stages | one adapter crossing around the complete engine computation |
| `f.matrix()` followed by nullspace/kernel rows and reconstructed submodule | `f.kernel()`; improve the Hom kernel implementation if necessary |
| structural predicate implemented by determinant/rank/gcd/minors | spell the categorical/module-theoretic definition; hide the numerical criterion underneath it |
| downstream code branches finite/infinite then performs coordinates | semantic owner routes representation cases; caller stays representation-oblivious |
| local `_..._from_matrix/_rows/_coordinates` helper recreates a standard construction | add/fix the kernel/image/pullback/cokernel/quotient/block-Hom/etc. API |
| same numerical workaround appears in a second consumer | treat it as missing semantic API and factor it immediately |
| subobject equality ignores its inclusion morphism | equality in the owned subobject/slice construction; the mono is part of the data |
| quotient equality ignores its projection | equality in the owned quotient/coslice construction; the epi is part of the data |
| normal form mutates/replaces chosen presentation | return a new represented object together with the isomorphism from the source |
| kernel/cokernel/product/etc. returned without canonical arrows | return/attach inclusion, projection, injections/projections, or other universal structure maps |
| test of isomorphism/isometry/genus uses equal objects | use distinct objects/presentations related by the weaker relation |
| `provider`/`manager`/`evidence`/`context` object in math layer | identify the actual morphism/functor/family/choice/standard mathematical datum |
| review finding is patched by moving code to a helper/registry | identify and repair the architectural generator/owner; migrate consumers |
| functor accepts `C` but rejects every non-isomorphism | declare the domain `C.core()` (or the actual slice/coslice/subcategory) |
| parameter redefines a canonical mathematical notion | derive it from existing structural data; use a new name only for genuinely different mathematics |
| deep specialized file computes generic set/Hom/quotient/product semantics | stop local patching and audit the general owner |
| universal construction gains arrows by product/matrix analogy | write the universal diagram and expose only the canonical maps it actually supplies |
| public `*args` / `**kwargs` forwards backend options | replace by closed named mathematical signatures; keep option forwarding private to adapters |
| `None` sentinel changes object/witness/return shape | split operations or accept the actual mathematical datum; only canonical defaults may be omitted |
| boolean mode flag changes mathematical result | named operations/constructors or precise literal overload at a compatibility boundary |
| `not is_X()` where the complementary mathematical property has a standard name | expose the positive predicate; preserve three-valued semantics where relevant |
| one-line `same_*` / per-element action wrapper hides value/morphism object | expose the composable value/morphism/Hom identity directly |
| supplied generators are returned as `O(L)` / `Aut(X)` | canonical group object plus `.subgroup(gens)`; completeness is a separate theorem |
| `Random*` / `Example*` / `Test*` type/category | process generates defining data for the ordinary constructor; named specimens go in catalogues |
| negative/absence test passes if object/result is empty/dead | prove a positive live surface/completeness witness first; prefer the positive universal property |
| easy determinant/count/fingerprint used to prove stronger claim | definition, cited complete invariant, or explicit witness |
| algorithm must exhaust `G`, `M`, `L`, etc. | structural/generator/presentation/theorem-backed check; explicit lazy enumeration only when enumeration is the operation |
| public name contains `partial`/`fast`/`cached`/engine name | use the stable mathematical noun/verb; put algorithm routing in implementation |
| “tensor product of matrices” | Kronecker product of matrices; tensor product belongs to represented maps/modules |
| `dot_product`/Euclidean norm/projection on arbitrary formed object | use the object's declared form/correlation; Euclidean algorithms only under the correct refinement |
| definite/nondegenerate restriction comes only from backend routine | keep general semantic domain; localize current algorithm case beneath it |
| owned upstream defect gets local Protocol/wrapper workaround | repair the authoritative source as part of the dependent task |
| long-lived stored backend twin drives ordinary math | prefer ephemeral construct-compute-convert-discard; durable backend state has one private owner |
| Sage `super_categories()` edge copied as “is-a” | classify actual structural functor first; Sage graph is runtime evidence only |
| Sage category equality/identical parents treated as mathematical equivalence | compare owned normalized constructions/functors |
| runtime bundled type/presentation called the category | separate category, object, runtime type, chosen presentation, property refinement |
| exact upstream class/name not found | compose standard mathematics from existing constructions before declaring a gap |
| mature dependency rejected mainly for package/build weight | compare owned LOC/reasoning, future blast radius, and reuse instead |
| local helper appears before checking Sage/stdlib/upstream idiom | inspect/probe the host first; use native capability behind owned semantics |
| scanner finding “fixed” only by syntax/suppression | diagnose against policy and repair the structural generator |
| generated certificate/status ledger mirrors live category/code facts | encode invariant structurally; live tests/on-demand report; no stored second ledger |
| category constructibility proved by graph BFS/name presence | derive the required canonical structural maps/category expression |
| repeated compliance checks grow around same violation | strengthen type/category/constructor/API so violation is structurally exposed |
| upstream tether shows duplicate general operation but local alias is preserved | delete/resite the local declaration; alignment can expose a defect |
| `pass` in mathematical implementation | implement/delete; genuine contract uses Sage `@abstract_method` + `...` |
| exact predicate returns `False`/`Unknown` because algorithm is missing | assertion-gate the computational frontier; reserve `Unknown` for explicitly soft knowledge predicates |
| `list(...)` / `tuple(...)` only to iterate | keep owned collection/generator lazy |
| multiple eager map/filter stages | generator/`map`/`filter` pipeline |
| raw `while` used only for ordinary iteration | `for`/iterator construct; retain `while` only for genuine evolving state |

### API and ownership patterns

#### `STY-01`: Global operation function -> method on the mathematical owner

**Bad:**

```python
Product(X, Y)
Kernel(f)
Orbit(G, x)
BaseChange(M, S)
```

**Preferred:**

```python
C.product([X, Y])
f.kernel()
G.orbit(x)
M.base_change(S)
```

The receiver supplies domain information and makes the operation discoverable by `<TAB>`.  A public global helper is not justified merely because it can dispatch correctly.

#### `STY-02`: Global dispatcher -> category/Hom/parent method dispatch

**Bad:**

```python
def Product(X, Y):
    if X in Modules(R) and Y in Modules(R):
        return module_product(X, Y)
    if X in Sets() and Y in Sets():
        return set_product(X, Y)
    if X in Schemes(S) and Y in Schemes(S):
        return scheme_product(X, Y)
```

**Preferred:**

```python
C = X.ambient_category()
return C.product([X, Y])
```

and each category subtree defines its own `product` implementation.  The global switchboard is usually a consequence of putting the operation on no mathematical owner.

#### `STY-03`: Ancestor imports descendant -> descendant imports/refines ancestor

**Bad:**

```python
# Cat/products.py
from ...lattices.my_special_lattices import MySpecialLattices
```

**Preferred:**

```python
# lattices/my_special_lattices.py
from ...abstract_categories.products import ProductsOfCategory

class MySpecialLattices(...):
    ...
```

A new specialized subtree should normally be addable without semantic edits to its ancestors or unrelated siblings.  Upward knowledge is a code smell even when not categorically forbidden.

#### `STY-04`: Export convenience operation -> keep global namespace sparse

**Bad:**

```python
# preamble/all.py
from .foo import Product, Kernel, Cokernel, Orbit, Stabilizer, BaseChange
```

**Preferred:** expose constructors/objects/categories globally and discover operations from the object already in hand:

```python
C = Modules(R)
C.<TAB>
f.<TAB>
G.<TAB>
```

A session namespace should not become a catalogue of every verb in the system.

#### `STY-05`: Runtime capability probing -> category-owned operation

**Bad:**

```python
if hasattr(M, "presentation_matrix"):
    return algorithm(M)
```

or:

```python
try:
    presentation = M.presentation_matrix()
except AttributeError:
    ...
```

**Preferred:** put the operation on the category that supplies the hypothesis:

```python
class ModulesWithChosenFinitePresentation(...):
    class ObjectType:
        def operation(self):
            ...
```

If a caller genuinely must branch, branch on owned mathematical category membership, not Python method presence.

#### `STY-06`: Manual sibling-method grafting -> common implementation/inheritance/category mixin

**Bad:**

```python
class GroupModuleHomset(...):
    base_ring = ModuleHomset.base_ring
    scalar_multiple = ModuleHomset.scalar_multiple
    elementwise = ModuleHomset.elementwise
    zero = ModuleHomset.zero
```

**Preferred:**

```python
class GroupModuleHomset(ModuleHomset, ...):
    ...
```

or move the shared API to the common Hom/category abstraction.  Assigning methods one-by-one is manual inheritance.

#### `STY-07`: Hidden source/provenance attributes -> explicit chosen-image/witness object

**Bad:**

```python
image._preamble_scalar_extension_source_module = M
...
M = image._preamble_scalar_extension_source_module
```

**Preferred:**

```python
selected_image = F.Image(M)
M = selected_image.preimage()
image = selected_image.image_object()
```

If later mathematics requires a chosen source, presentation, decomposition, or witness, that datum is part of the mathematical object model.

#### `STY-08`: Import-order-dependent refinement -> stable dependency DAG

**Bad:**

```python
try:
    from .modules import Modules
except ImportError:
    return R   # try again on a later lookup
```

**Preferred:** reorganize dependencies so the canonical structure is available deterministically from the defining object/category.  Function-local imports are for optional/heavy implementation dependencies, not a general cycle-breaking architecture.

### Collection construction patterns

#### `STY-09`: `append(f(x))` loop -> list comprehension or lazy image

**Bad:**

```python
images = []
for x in xs:
    images.append(f(x))
```

**Preferred:**

```python
images = [f(x) for x in xs]
```

or, when materialization is unnecessary:

```python
images = (f(x) for x in xs)
```

If this is a mathematical image/family, use the owned image/indexed-family construction instead of a Python list.

#### `STY-10`: Conditional `append` loop -> filtered comprehension/generator

**Bad:**

```python
compatible = []
for candidate in candidates:
    if agrees(candidate):
        compatible.append(candidate)
```

**Preferred:**

```python
compatible = [candidate for candidate in candidates if agrees(candidate)]
```

or lazily:

```python
compatible = (candidate for candidate in candidates if agrees(candidate))
```

#### `STY-11`: Dict assignment loop -> dictionary comprehension

**Bad:**

```python
images = {}
for label in labels:
    images[label] = f(label)
```

**Preferred:**

```python
images = {label: f(label) for label in labels}
```

This applies only when the loop is a direct map.  Multi-step coefficient accumulation may instead belong to a finite-support or linear-combination abstraction.

#### `STY-12`: Set `add` loop -> set comprehension/constructor

**Bad:**

```python
category_types = set()
for category in categories:
    category_types.add(type(category))
```

**Preferred:**

```python
category_types = {type(category) for category in categories}
```

or simply `set(values)` when no transformation occurs.

#### `STY-13`: Two disjoint dict-building loops -> dict union/comprehensions

**Bad:**

```python
images = {}
for label in left_labels:
    images[("left", label)] = left_map(label)
for label in right_labels:
    images[("right", label)] = right_map(label)
```

**Preferred:**

```python
images = {
    **{("left", label): left_map(label) for label in left_labels},
    **{("right", label): right_map(label) for label in right_labels},
}
```

or Python 3.9+ dictionary union:

```python
images = left_images | right_images
```

If the keys are mathematically tagged coproduct labels, prefer the owned coproduct/family construction.

#### `STY-14`: `extend` flattening loop -> `itertools.chain.from_iterable`

**Bad:**

```python
flat = []
for block in blocks:
    flat.extend(block)
```

**Preferred:**

```python
from itertools import chain
flat = chain.from_iterable(blocks)
```

Materialize with `list(...)` only at an explicitly finite private boundary that requires a Python sequence.

#### `STY-15`: `sum(rows, [])` flattening -> `chain.from_iterable`

**Bad:**

```python
entries = sum(rows, [])
```

This is quadratic for lists and hides flattening as addition.

**Preferred:**

```python
entries = chain.from_iterable(rows)
```

or a nested comprehension when a concrete private array is actually needed:

```python
entries = [entry for row in rows for entry in row]
```

#### `STY-16`: Nested Cartesian loops -> `itertools.product`

**Bad:**

```python
for a in A:
    for b in B:
        use(a, b)
```

**Preferred:**

```python
from itertools import product
for a, b in product(A, B):
    use(a, b)
```

If `A × B` is itself mathematical data used downstream, use the owned Cartesian-product object rather than `itertools.product`.

#### `STY-17`: Hand-built combinations/permutations -> `itertools`

**Bad:** recursive/index code whose only purpose is to enumerate subsets, fixed-size subsets, tuples, or permutations.

**Preferred:**

```python
from itertools import combinations, combinations_with_replacement, permutations
```

For mathematical finite/infinite combinatorial families, wrap or implement the corresponding owned enumerated set rather than leaking raw tuples as the public object.

#### `STY-18`: Slice-by-loop -> `itertools.islice`

**Bad:**

```python
result = []
for i, x in enumerate(xs):
    if i == n:
        break
    result.append(x)
```

**Preferred:**

```python
from itertools import islice
result = islice(xs, n)
```

Again, materialize only if the consumer actually needs a concrete finite sequence.

#### `STY-19`: Forwarding generator loop -> `yield from`

**Bad:**

```python
def values():
    for value in source:
        yield value
```

**Preferred:**

```python
def values():
    yield from source
```

If there is only a transformation, consider returning a generator expression directly.

#### `STY-20`: Consecutive-pair index arithmetic -> `itertools.pairwise`

**Bad:**

```python
for i in range(len(values) - 1):
    compare(values[i], values[i + 1])
```

**Preferred:**

```python
from itertools import pairwise
for left, right in pairwise(values):
    compare(left, right)
```

This is private finite-sequence syntax; mathematical ordered sets should expose their own adjacency/successor structure where appropriate.

#### `STY-21`: Running prefix accumulation -> `itertools.accumulate`

**Bad:**

```python
total = zero
prefixes = []
for value in values:
    total += value
    prefixes.append(total)
```

**Preferred:**

```python
from itertools import accumulate
prefixes = accumulate(values, initial=zero)
```

Use the mathematical additive operation when Python `+` is not the owned operation.

### Predicate/search patterns

#### `STY-22`: Boolean scan -> `all`

**Bad:**

```python
for x in xs:
    if not predicate(x):
        return False
return True
```

**Preferred:**

```python
return all(predicate(x) for x in xs)
```

#### `STY-23`: Existence scan -> `any`

**Bad:**

```python
for x in xs:
    if predicate(x):
        return True
return False
```

**Preferred:**

```python
return any(predicate(x) for x in xs)
```

#### `STY-24`: Find first matching element -> `next`

**Bad:**

```python
answer = None
for x in xs:
    if predicate(x):
        answer = x
        break
return answer
```

**Preferred:**

```python
return next((x for x in xs if predicate(x)), None)
```

If absence is exceptional, omit the default and let `StopIteration` be converted at the appropriate API boundary.

#### `STY-25`: Count matching elements -> `sum`

**Bad:**

```python
count = 0
for x in xs:
    if predicate(x):
        count += 1
```

**Preferred:**

```python
count = sum(predicate(x) for x in xs)
```

For mathematical cardinality, do not enumerate merely to count; ask the owned set/family for its cardinality.

#### `STY-26`: Manual minimum/maximum tracking -> `min`/`max` with `key=`

**Bad:**

```python
best = None
for candidate in candidates:
    if best is None or score(candidate) < score(best):
        best = candidate
```

**Preferred:**

```python
best = min(candidates, key=score)
```

Use `default=` when the empty case is meaningful and Python's API supports it.

#### `STY-27`: `if condition: return True; return False` -> return the predicate

**Bad:**

```python
if condition:
    return True
return False
```

**Preferred:**

```python
return condition
```

Negate directly when needed: `return not condition`.

### Folding and algebraic accumulation patterns

#### `STY-28`: Additive accumulator -> owned sum/linear combination or `sum`

**Bad:**

```python
total = target.zero()
for label, coefficient in coefficients.items():
    total += target.scalar_multiple(coefficient, basis[label])
return total
```

**Preferred:**

```python
return target.linear_combination(coefficients)
```

If this is plain private Python arithmetic:

```python
return sum(terms, start=zero)
```

A manual accumulator should not reimplement a parent/category operation.

#### `STY-29`: Multiplicative accumulator -> owned product or `reduce`

**Bad:**

```python
result = target.one()
for factor in factors:
    result *= factor
return result
```

**Preferred:**

```python
return target.product(factors)
```

At a plain Python/backend boundary:

```python
from functools import reduce
from operator import mul
return reduce(mul, factors, target.one())
```

#### `STY-30`: Nested bilinear sum -> `sum`/linear-combination abstraction

**Bad:**

```python
total = W.zero()
for i, a in left_coefficients.items():
    for j, b in right_coefficients.items():
        total += a * b * gram(i, j)
return total
```

**Preferred:**

```python
return sum(
    (a * b * gram(i, j)
     for i, a in left_coefficients.items()
     for j, b in right_coefficients.items()),
    W.zero(),
)
```

Better still, when this is evaluation of a represented pairing, call the pairing/Hom object rather than reimplementing coordinate evaluation.

#### `STY-31`: Useless identity-update loop -> delete it

**Bad:**

```python
for label in right.support():
    if left.multiplicity(label) == 0:
        coefficient *= 1
```

**Preferred:** delete the loop.  LLM-generated code often contains semantically inert bookkeeping left over from a more complicated derivation; simplify algebraically before preserving control flow.

### Grouping/counting/mapping patterns

#### `STY-32`: `setdefault(..., []).append(...)` -> `defaultdict(list)`

**Bad:**

```python
grouped = {}
for key, value in pairs:
    grouped.setdefault(key, []).append(value)
```

**Preferred:**

```python
from collections import defaultdict

grouped = defaultdict(list)
for key, value in pairs:
    grouped[key].append(value)
```

If input is already sorted by key and streaming behavior matters, consider `itertools.groupby`.

#### `STY-33`: Manual multiplicity dictionary -> `Counter`

**Bad:**

```python
counts = {}
for label in labels:
    counts[label] = counts.get(label, 0) + 1
```

**Preferred:**

```python
from collections import Counter
counts = Counter(labels)
```

If multiplicity is mathematical structure, prefer the owned multiset/fixed-size-selection object.

#### `STY-34`: Manual default-valued accumulation -> `defaultdict`

**Bad:**

```python
coefficients = {}
for label, value in terms:
    coefficients[label] = coefficients.get(label, zero) + value
```

**Preferred:**

```python
from collections import defaultdict
coefficients = defaultdict(lambda: zero)
for label, value in terms:
    coefficients[label] += value
```

Better still, use the parent's finite-support or `linear_combination` machinery if these are mathematical coefficients.

#### `STY-35`: Manual ordered deduplication -> owned ordered set or `dict.fromkeys` privately

**Bad:**

```python
result = []
for x in xs:
    if x not in result:
        result.append(x)
```

**Preferred mathematical form:** construct the owned ordered set.

For private hashable Python data where first-occurrence order is merely serialization order:

```python
result = list(dict.fromkeys(xs))
```

Do not use a Python sequence as the public representation of a mathematical set.

### Indexing and parallel-iteration patterns

#### `STY-36`: Parallel indexing -> `zip(..., strict=True)`

**Bad:**

```python
for i in range(len(labels)):
    use(labels[i], coefficients[i])
```

**Preferred:**

```python
for label, coefficient in zip(labels, coefficients, strict=True):
    use(label, coefficient)
```

If the two families are mathematically indexed by the same set, prefer that common index set directly instead of positional Python synchronization.

#### `STY-37`: Position counter -> `enumerate`

**Bad:**

```python
i = 0
for value in values:
    use(i, value)
    i += 1
```

**Preferred:**

```python
for i, value in enumerate(values):
    use(i, value)
```

Again, if `i` is mathematically a label rather than incidental Python position, use the owned rank/unrank/index set.

#### `STY-38`: Repeated full index lookup -> precomputed mathematical rank map / owned rank

**Bad:**

```python
for label in labels:
    position = labels_list.index(label)
```

**Preferred:** use the owned ordered set's `rank(label)`, or construct a private `{label: position}` mapping once when crossing into a backend that requires dense positions.

Do not force an infinite or abstract framing into a list merely to gain `.index`.

### Stateful traversal patterns

#### `STY-39`: FIFO worklist -> `collections.deque`

**Bad:**

```python
frontier = [seed]
while frontier:
    x = frontier.pop(0)
    ...
    frontier.append(y)
```

**Preferred:**

```python
from collections import deque
frontier = deque([seed])
while frontier:
    x = frontier.popleft()
    ...
```

#### `STY-40`: Bespoke orbit closure -> action/G-set `orbit`

**Bad:**

```python
seen = {seed}
frontier = deque([seed])
while frontier:
    point = frontier.popleft()
    for g in group_generators:
        image = act(g, point)
        if image not in seen:
            seen.add(image)
            frontier.append(image)
```

**Preferred:**

```python
return action.orbit(seed)
```

or the corresponding GAP/Sage group-action routine behind the owned action API.  If a generic orbit algorithm is missing, implement it once on the G-set/action abstraction.

#### `STY-41`: Bespoke connected-components/reachability -> graph library

**Bad:** local DFS/BFS code whose mathematical input is already a graph.

**Preferred:** use the owned graph object, Sage graph API, or `networkx` operation such as connected components, shortest paths, transitive closure, topological sorting, etc.  Do not maintain generic graph algorithms in a mathematical theory module.

#### `STY-42`: Bespoke group stabilizer/orbit algorithm -> GAP/Sage group backend through owned API

**Bad:** enumerate group action manually to recover an orbit or stabilizer when GAP/Sage already implements it.

**Preferred:**

```python
orbit = G.orbit(x)
stabilizer = G.stabilizer(x)
```

with the implementation delegated through the private group backend.  The preamble owns the mathematical object; GAP owns the generic finite-group algorithm.

#### `STY-43`: Genuine fixed-point/search algorithm -> keep explicit loop

Not every `while` should disappear.

**Appropriate:**

```python
changed = True
while changed:
    changed = False
    ...  # one mathematically meaningful closure step
```

when the fixed-point iteration itself is the algorithm and no standard library/upstream routine already owns it.  Use explicit names for state and invariants; do not contort such code into nested `reduce`/lambda expressions.

### Control-flow cleanup patterns

#### `STY-44`: `try`/`except` in mathematical code -> asserted hypotheses and total code

Exception-driven control flow is an engineering pattern, not a mathematical one.  In mathematical code, state the assumptions that make the next construction valid, assert them, and then execute code that is total under those assumptions.

**Bad mathematical code:**

```python
try:
    return optional_construction(X)
except (TypeError, ValueError, AttributeError):
    return fallback(X)
```

**Preferred:**

```python
assert X in CategoryWhereCurrentAlgorithmIsTotal(), (
    "the current implementation assumes ..."
)
return construction(X)
```

If the construction is mathematically defined only on that narrower category, move the method there instead.  `try`/`except` and `contextlib.suppress` remain legitimate inside engineering kernels—backend adapters, parsers, filesystem/network/process interfaces—where the failure is an external protocol event rather than part of the mathematics.

#### `STY-45`: Temporary immediately returned -> direct return

**Bad:**

```python
result = normalize(value)
return result
```

**Preferred:**

```python
return normalize(value)
```

Keep the temporary when its name records a real mathematical intermediate or materially improves readability/debugging.

#### `STY-46`: Nested guard-only `if` -> combined condition

**Bad:**

```python
if x in C:
    if predicate(x):
        return f(x)
```

**Preferred:**

```python
if x in C and predicate(x):
    return f(x)
```

Do not combine conditions when the inner branch represents a distinct mathematical case worth naming.

#### `STY-47`: `if/else` assignment -> conditional expression when both branches are expressions

**Bad:**

```python
if index >= 0:
    name = f"x_{index}"
else:
    name = f"x_m{-index}"
```

**Preferred:**

```python
name = f"x_{index}" if index >= 0 else f"x_m{-index}"
```

#### `STY-48`: Whole-method failure stub -> real implementation cases, `@abstract_method`, or correct placement

A visible mathematical method may legitimately fail on *currently uncomputable instances* of a mathematically meaningful notion. What is forbidden is advertising a method whose implementation contains no successful mathematical case at all.

**Bad deceitful stub:**

```python
def tensor_shape(self):
    assert False, "a tensor supplies the ranks of its indices"
```

or:

```python
def kernel(self):
    raise NotImplementedError
```

These methods expose a name under tab completion but implement no mathematics.

**Preferred for a genuine abstract implementation contract:**

```python
from sage.misc.abstract_method import abstract_method

@abstract_method
def tensor_shape(self):
    ...
```

**Preferred when the notion is only mathematically defined on a narrower category:** put/mix the method only on that category.

**Preferred when the notion is mathematically general but only some cases are currently computable:** keep the method at the mathematically correct owner and implement those cases, with an informative assertion only for the unhandled remainder. A final `assert False, ...` is acceptable *after real implemented cases* as an exhaustiveness/computability fallback; it is not acceptable as the whole implementation.

#### `STY-49`: Mathematical and algorithmic hypotheses -> assert them loudly

Assertions are executable mathematical commentary. Use them liberally to state category membership, finiteness, nondegeneracy, compatibility, shape, parentage, and identities on which the following derivation relies.

**Good proof-context assertions:**

```python
assert lattice in Lattices(R)
assert f.domain() is M
assert result in TargetCategory()
```

**Good algorithm-domain assertion:**

```python
def is_nondegenerate(self):
    assert self in FiniteRankFormedModules(R), (
        "nondegeneracy is currently decidable here only for finite-rank formed modules"
    )
    return self.gram_tensor().determinant() != 0
```

The method remains on the category where nondegeneracy is mathematically meaningful; the assertion states only the narrower domain of the current algorithm.

Do **not** replace these statements by exception-valued mathematical branches. The assertion records the proof/computability context and should fail loudly at the first unmet assumption.

### Representation and DRY patterns

#### `STY-50`: Parallel representation of a canonical object -> reuse the canonical construction

**Bad:** maintain a tensor-based matrix object with its own determinant/rank/kernel API while `M_{m,n}(R)` is already `Hom_R(F_R([n]), F_R([m]))`.

**Preferred:** the matrix is the Hom element.  Put matrix operations on the appropriate Hom/category refinement and delete the parallel representation.

#### `STY-51`: Equivalent universal data implemented independently -> derive one from the other

**Bad:** every adjunction subclass independently implements:

```python
unit(...)
counit(...)
hom_set_isomorphism_forward(...)
hom_set_isomorphism_inverse(...)
```

**Preferred:** choose one authoritative presentation, e.g. unit+counit, and derive the transpose maps generically:

```python
Phi(f) = U(f) * eta_A
Phi_inverse(g) = epsilon_B * F(g)
```

Do not spend hundreds of lines maintaining mathematically forced coherence by hand.

#### `STY-52`: Duplicate additive object implementation -> reuse/refine the existing additive construction

**Bad:** implement a second class with its own normalization, homogeneous components, addition, negation, scalar multiplication, equality, and display when it is already a graded direct sum with extra multiplication.

**Preferred:** use the existing graded-direct-sum parent/element as the additive/module object and refine/equip it with the additional algebra structure.

#### `STY-53`: Repeated parameterized-category boilerplate -> common parameterized base

**Bad:** several categories each repeat:

```python
@staticmethod
def __classcall_private__(cls, base_ring, group): ...
def __init__(self, base_ring, group): ...
def base_ring(self): ...
def acting_group(self): ...
```

**Preferred:** factor the common `(R, G)`-parameterized category abstraction once and derive `GroupModules`, `GroupLattices`, chosen-finite variants, etc. from it.

#### `STY-54`: Same algorithm in method and functor -> one canonical operation, functor delegates

**Bad:** `M.base_change(S)` and `ScalarExtensionFunctor._apply_object(M)` independently rebuild the same transported action/presentation.

**Preferred:** one is authoritative:

```python
class ScalarExtensionFunctor(...):
    def _apply_object(self, M):
        return M.base_change(self.target_ring())
```

or conversely the object method delegates to the functor if the functor is the mathematical owner.  There must be one implementation.

#### `STY-55`: Theory-local identity cache -> shared memoization/`UniqueRepresentation`

**Bad:**

```python
_MODULE_TENSOR_PRODUCT_CACHE = {}
_POWER_CACHE = {}
_FORM_SPACE_CACHE = {}
```

with custom `id(...)` keys and stale-entry checks in each file.

**Preferred:** `cached_function`, `cached_method`, `UniqueRepresentation`, or one shared identity-sensitive memoization helper with explicit lifetime semantics.

#### `STY-56`: Hand-written generic utility already in stdlib/dependency -> import it

**Bad:** local implementations of graph traversal, topological sort, union-find, memoization, flattening, pairwise traversal, combinations, queues, grouping, or multidispatch.

**Preferred:** use `itertools`, `collections`, `functools`, Sage/networkx, GAP, OSCAR/Singular, or another mature dependency.  Adding a dependency is preferable when it deletes substantial generic machinery and has a better semantic fit.

### Backend and boundary patterns

#### `STY-57`: Cross-backend ping-pong -> one crossing around the complete computation

**Bad:**

```python
A_engine = to_engine(A)
B_engine = engine_step_one(A_engine)
B = from_engine(B_engine)
C_engine = to_engine(B)
D_engine = engine_step_two(C_engine)
return from_engine(D_engine)
```

**Preferred:**

```python
return from_engine(adapter.complete_algorithm(to_engine(A)))
```

When practical, implement the multi-stage routine natively in Singular/Julia/OSCAR/GAP/etc. and return only the final data needed to reconstruct the owned result.

#### `STY-58`: Backend workspace leaks into mathematical code -> private adapter owns it

**Bad:** several mathematical modules directly read `_engine`, construct engine matrices, and continue computation on engine elements.

**Preferred:** one private adapter converts owned inputs, computes, and crosses back.  Ordinary mathematical consumers never receive or manipulate backend parents/elements.

#### `STY-59`: Python loops serialize every intermediate backend object -> batch/native engine operation

**Bad:** repeatedly cross individual rows/elements in a Python loop when the backend accepts a matrix/family and can execute the whole reduction internally.

**Preferred:** serialize the finite input once, invoke one engine routine, deserialize the final result once.

### Laziness and mathematical collections

#### `STY-60`: Eager `list`/`tuple` just to iterate -> iterate the owned collection

**Bad:**

```python
labels = tuple(M.module_generating_set())
for label in labels:
    ...
```

**Preferred:**

```python
for label in M.module_generating_set():
    ...
```

Use `rank`/`unrank`, indexed families, or finite support when positional access is mathematically required.  Materialize only in a private backend serializer after finiteness and order are established.

#### `STY-61`: Eager intermediate list -> generator pipeline

**Bad:**

```python
rows = [transform(x) for x in xs]
nonzero = [row for row in rows if any(row)]
return backend(nonzero)
```

**Preferred:**

```python
rows = (transform(x) for x in xs)
return backend(row for row in rows if any(row))
```

provided the backend/consumer can stream.  Do not create Python containers that have no mathematical identity and exist only to feed the next expression.

#### `STY-62`: Enumerate to decide cardinality/finiteness -> use cardinality/category

**Bad:**

```python
items = list(S)
return len(items)
```

**Preferred:**

```python
return S.cardinality()
```

or dispatch from the appropriate finite/infinite category.  Enumeration is not a proof of finiteness and may be impossible for a perfectly valid infinite object.

### String/display and small-expression patterns

#### `STY-63`: Append strings then concatenate -> comprehension + `join`

**Bad:**

```python
terms = []
for label in support:
    terms.append(format_term(label))
return " + ".join(terms)
```

**Preferred:**

```python
return " + ".join(format_term(label) for label in support)
```

#### `STY-64`: Repeated membership normalization loop -> constructor/comprehension when semantics are simple

**Bad:**

```python
normalized = []
for x in xs:
    x = normalize(x)
    if x:
        normalized.append(x)
```

**Preferred:**

```python
normalized = [y for x in xs if (y := normalize(x))]
```

Use this only when the assignment expression improves clarity; otherwise use a small helper plus comprehension.  If normalization has multiple semantic branches or mathematical assertions, retain explicit code rather than obscuring those hypotheses inside an expression.

#### `STY-65`: Repeated `.get(key, zero) + value` -> finite-support abstraction or `defaultdict`

**Bad:**

```python
result[key] = result.get(key, zero) + value
```

repeated throughout an algorithm.

**Preferred:** use the object's finite-support coefficient type.  At a private Python layer:

```python
result = defaultdict(lambda: zero)
result[key] += value
```

#### `STY-66`: Empty mutable accumulator immediately followed by a loop -> classify before accepting

The shapes `result = []`, `result = {}`, and `result = set()` immediately before an iteration are **review triggers**.  They are not automatically wrong, but they very often mean Python is being used to spell map/filter/group/fold semantics manually.

**Red flags:**

```python
result = []
for x in xs:
    ...

result = {}
for x in xs:
    ...

result = set()
for x in xs:
    ...
```

Before keeping the loop, classify the mutation:

```text
append(f(x))                 -> comprehension / map / owned image
conditional append           -> filtered comprehension / filter
extend(f(x))                 -> chain.from_iterable
add(f(x))                    -> set comprehension / owned set
d[key] = f(x)                -> dict comprehension
d[key] += value              -> defaultdict / Counter / finite-support sum
acc += term                  -> sum / linear_combination / owned fold
acc *= factor                -> product / math.prod / reduce / owned fold
queue append + pop-left      -> deque or higher traversal API
```

If none of these describe the mutation because the evolving state is the algorithm, keep the explicit state machine.

#### `STY-67`: Raw `for x in xs` -> first test map/filter/fold/quantifier/traversal forms

Every new explicit `for` loop in ordinary transformation code is a review trigger.  First ask whether the body is one of the standard forms catalogued here.

**Bad default:**

```python
for x in xs:
    result.append(f(x))
```

**Preferred:**

```python
result = [f(x) for x in xs]
```

The same trigger applies to `for key, value in mapping.items()`, nested `for` loops, and loops over mathematical generating sets.  The explicit loop is appropriate when the iteration carries genuine mutable state, early multi-branch control flow, backtracking, a protocol, or another algorithm whose transitions are the point.

#### `STY-68`: Raw `while` -> require a genuine evolving-state invariant

A `while` loop should normally correspond to a stateful algorithm: fixed point, worklist search, backtracking, iterative refinement, parsing/protocol state, or backend iteration.

**Suspicious:**

```python
while i < len(xs):
    consume(xs[i])
    i += 1
```

**Preferred:**

```python
for x in xs:
    consume(x)
```

**Legitimate:**

```python
while frontier:
    state = frontier.popleft()
    ...
```

provided the search itself is not already owned by a graph/action/group abstraction or dependency.

#### `STY-69`: `.append(...)` inside a loop -> comprehension, filter, or owned image

Treat `.append(...)` inside an ordinary `for` loop as a specific red flag.

**Bad:**

```python
rows = []
for relation in relations:
    rows.append(transform(relation))
```

**Preferred:**

```python
rows = [transform(relation) for relation in relations]
```

If the result is consumed once, prefer the lazy form:

```python
rows = (transform(relation) for relation in relations)
```

If the values form a mathematical image/family/set, construct that owned object instead of a Python list.

#### `STY-70`: `.extend(...)` inside a loop -> `chain` / `chain.from_iterable`

**Bad:**

```python
flat = []
for block in blocks:
    flat.extend(block)
```

**Preferred:**

```python
from itertools import chain
flat = chain.from_iterable(blocks)
```

For a fixed small number of iterables:

```python
flat = chain(left, middle, right)
```

Materialize with `list(...)` only at a private finite serialization boundary.

#### `STY-71`: `.add(...)` inside a loop -> set comprehension / set constructor

**Bad:**

```python
seen_types = set()
for C in categories:
    seen_types.add(type(C))
```

**Preferred:**

```python
seen_types = {type(C) for C in categories}
```

If the set is mathematical, use the owned set construction rather than Python `set`.

#### `STY-72`: `result[key] = expression` in a simple loop -> dict comprehension

**Bad:**

```python
images = {}
for label in labels:
    images[label] = f(label)
```

**Preferred:**

```python
images = {label: f(label) for label in labels}
```

If each key is assigned more than once, this is no longer a simple dict-construction pattern; use the grouping/accumulation rules instead.

#### `STY-73`: `acc += term` inside a loop -> sum/fold/owned additive operation

**Bad:**

```python
total = zero
for term in terms:
    total += term
```

**Preferred for ordinary additive values:**

```python
return sum(terms, start=zero)
```

**Preferred for module coefficients:**

```python
return M.linear_combination(coefficients)
```

Do not force Python `sum` when the mathematical parent has a more informative finite-sum or linear-combination operation.

#### `STY-74`: `acc *= factor` inside a loop -> owned product, `math.prod`, or `reduce`

**Bad:**

```python
product = one
for factor in factors:
    product *= factor
```

**Preferred when the mathematical parent owns the product:**

```python
return parent.product(factors)
```

**Preferred for ordinary numeric scalars:**

```python
from math import prod
return prod(factors, start=one)
```

**Preferred for arbitrary Python objects with associative multiplication but no owner fold:**

```python
from functools import reduce
from operator import mul
return reduce(mul, factors, one)
```

Use `math.prod` rather than `reduce(mul, ...)` for ordinary numbers.  Use the owned mathematical product rather than either Python form when it exists.

#### `STY-75`: `.get(key, zero) + value` / repeated coefficient mutation -> finite-support abstraction first

**Bad:**

```python
coefficients = {}
for key, value in terms:
    coefficients[key] = coefficients.get(key, zero) + value
```

**Preferred mathematical form:** use the repository's finite-support/linear-combination object.

**Private Python fallback:**

```python
from collections import defaultdict
coefficients = defaultdict(lambda: zero)
for key, value in terms:
    coefficients[key] += value
```

For integer multiplicities, use `Counter` instead.

#### `STY-76`: `setdefault(key, []).append(value)` -> `defaultdict(list)`

**Bad:**

```python
grouped = {}
for key, value in pairs:
    grouped.setdefault(key, []).append(value)
```

**Preferred:**

```python
from collections import defaultdict
grouped = defaultdict(list)
for key, value in pairs:
    grouped[key].append(value)
```

If the input is already sorted by the grouping key and streaming behavior is useful, consider `itertools.groupby` instead.

#### `STY-77`: Sorted streaming grouping -> `itertools.groupby`

**Bad:**

```python
# hand-maintain current_key/current_bucket while walking sorted records
```

**Preferred:**

```python
from itertools import groupby
for key, group in groupby(records, key=key_function):
    consume_group(key, group)
```

`groupby` groups adjacent equal keys; sort first only when sorting is mathematically/algorithmically appropriate.  For unsorted accumulation, `defaultdict` is usually the correct tool.

#### `STY-78`: Repeated integer counting -> `Counter` / `Counter.update`

**Bad:**

```python
counts = {}
for label in labels:
    counts[label] = counts.get(label, 0) + 1
```

**Preferred:**

```python
from collections import Counter
counts = Counter(labels)
```

For repeated batches:

```python
counts.update(more_labels)
```

Use an owned multiset when multiplicity is mathematical data in the public preamble.

#### `STY-79`: Named pure transformation -> `map`; named predicate -> `filter`

Use `map` and `filter` when they expose an already named operation directly; use comprehensions when the expression or condition is clearer inline.

**Verbose:**

```python
normalized = []
for x in xs:
    normalized.append(normalize(x))
```

**Concise:**

```python
normalized = map(normalize, xs)
```

**Verbose:**

```python
finite = []
for x in xs:
    if is_finite(x):
        finite.append(x)
```

**Concise:**

```python
finite = filter(is_finite, xs)
```

Do not wrap `list(...)` around these merely by habit; retain laziness unless a concrete sequence is actually required.

#### `STY-80`: Tuple-unpacking transformation -> `itertools.starmap` when clearer

**Bad:**

```python
values = (f(a, b) for a, b in pairs)
```

**Alternative when `f` is already named and the tuple-unpacking is the only syntax:**

```python
from itertools import starmap
values = starmap(f, pairs)
```

Prefer the generator expression when it is more readable.  The point is to recognize the standard higher-order iterator rather than build a helper loop.

#### `STY-81`: Fixed-size chunking loop -> `itertools.batched`

**Bad:**

```python
batch = []
for x in xs:
    batch.append(x)
    if len(batch) == n:
        yield tuple(batch)
        batch.clear()
```

**Preferred:**

```python
from itertools import batched
yield from batched(xs, n)
```

Use `strict=True` when an incomplete final batch is invalid.

#### `STY-82`: Repeated constant values -> `itertools.repeat`

**Bad:**

```python
values = (zero for _ in range(n))
```

**Preferred:**

```python
from itertools import repeat
values = repeat(zero, n)
```

Use this only for immutable values or when sharing the repeated object is intended.

#### `STY-83`: Manual running index paired with values -> `enumerate`; two streams -> strict `zip`

**Bad:**

```python
i = 0
for value in values:
    consume(i, value)
    i += 1
```

**Preferred:**

```python
for i, value in enumerate(values):
    consume(i, value)
```

For two logically equal-length streams:

```python
for left, right in zip(lefts, rights, strict=True):
    ...
```

Do not silently truncate mathematical data with plain `zip` when equal cardinality is part of the contract.

#### `STY-84`: Manual list concatenation with `+` in a loop -> `chain`; repeated string `+=` -> `join`

**Bad:**

```python
result = []
for block in blocks:
    result = result + block
```

**Preferred:**

```python
from itertools import chain
result = chain.from_iterable(blocks)
```

**Bad:**

```python
text = ""
for part in parts:
    text += part
```

**Preferred:**

```python
text = "".join(parts)
```

#### `STY-85`: Manual product/sum of a transformed family -> generator directly into the fold

Do not build a temporary list just to fold it.

**Bad:**

```python
terms = [weight(x) * value(x) for x in xs]
return sum(terms, start=zero)
```

**Preferred:**

```python
return sum((weight(x) * value(x) for x in xs), start=zero)
```

For ordinary numeric products:

```python
from math import prod
return prod((weight(x) for x in xs), start=one)
```

Again, an owned `linear_combination` or `product` outranks the Python fold when the family belongs to a mathematical parent.

#### `STY-86`: Multiple simple stages -> lazy generator pipeline, not repeated materialization

**Bad:**

```python
mapped = [normalize(x) for x in xs]
filtered = [x for x in mapped if valid(x)]
keys = [key(x) for x in filtered]
```

**Preferred:**

```python
mapped = map(normalize, xs)
filtered = filter(valid, mapped)
keys = map(key, filtered)
```

or a readable generator pipeline.  Materialize only the stage whose concrete sequence semantics are actually required.

#### `STY-87`: Collection-building loop with no mutation except construction -> assume a declarative replacement exists

The general red flag is:

```python
result = <empty collection>
for x in xs:
    result.<single construction mutation>(...)
return result
```

Before accepting it, prove that it is *not* one of:

- list/set/dict comprehension;
- `map` / `filter`;
- `chain` / `chain.from_iterable`;
- `defaultdict` / `Counter`;
- `sum` / `math.prod` / `reduce`;
- `any` / `all` / `next` / `min` / `max`;
- an owned set/image/family/linear-combination/product;
- a graph/action/group traversal already implemented elsewhere.

This is deliberately a review trigger because this exact “walk and accrue” pattern is heavily overproduced by generated code.

### Current live-tree exemplars behind the catalogue

The catalogue above is not hypothetical.  These are concrete patterns already observed in the current preamble; they serve as regression examples for future review.

| Current case | What is wrong | Preferred direction | Catalogue |
| --- | --- | --- | --- |
| `categories/abstract_categories/constructions.py`: global `Product`, `Coproduct`, `TensorProduct`, `Subobjects`, `Kernel`, `Cokernel`, `Pushout`; `rings/commutative_algebra.py`: global `Localization`, `PrimeLocalization`, `QuotientRing` | Free-standing operations force callers to know a global language and force implementation to rediscover mathematical ownership.  Each of these has an owner in argument position | Put the construction on the category/object/Hom/morphism that owns it; operator notation may delegate there, a named global may not | `ARC-12`, `STY-01`–`04` |
| `abstract_categories/arrow_categories.py::_morphisms_agree` | Root helper knows schemes, finite sets, groups, and modules to decide arrow equality | Homset/category owns extensional equality | `STY-02`, `05` |
| `tensors/tensor.py` determinant/rank/solve/kernel/trace/row/transpose/inverse methods | A type-(1,1) tensor is being used as a second matrix/linear-map representation | `M_{m,n}(R)=Hom_R(F_R([n]),F_R([m]))`; matrix operations live on that Hom refinement | `STY-50` |
| `categories/forms/forms.py` represented `PairingSpace`/`BilinearFormSpace` hierarchy | Parallel Hom-like representation remains after tensor products exist | Represented pairing is literally `Hom_R(X tensor Y, W)`; quadratic maps use the appropriate universal square where represented | `STY-50`–`52` |
| `functors/core.py::Adjunction` and its subclasses | Unit, counit, forward transpose, and inverse transpose are independently implemented despite determining each other | Choose one standard presentation and derive the rest by the adjunction formulas | `STY-51` |
| `ContravariantFunctor` / `Bifunctor` in `functors/core.py` | Reimplement ordinary functor cache/validation for structures already represented by opposite/product categories | Thin convenience interface over `Functor(C.op(),D)` / `Functor(C×D,E)` | `STY-51`, `54` |
| functor modules attaching `_preamble_*_source_*` attributes | Chosen preimages/provenance are hidden side channels | Explicit functor-image/chosen-preimage object, or derive maps from unit/counit | `STY-07` |
| `schemes.py` `_preamble_coordinate_algebra_morphism` and related attached structure | Affine-Spec contravariance/provenance is reconstructed by side-channel metadata | Actual `Spec` functor and scheme Hom whose pullback is intrinsic | `STY-07`, `17` |
| `rings.py::_refine_canonical_self_module_and_algebra` | Canonical structure can depend on import success and later lookups | Deterministic structure/category packet independent of import history | `STY-08` |
| pervasive `refine(...)` calls that mutate classes/state after construction | Runtime refinement can become a second history-dependent object system | Stable implementation/category structure; refinement only for genuinely established mathematical structure | `STY-08`, `18` |
| `PowerAlgebraElement` versus `GradedDirectSumElement` | Same additive/module implementation repeated in a richer object | Reuse the graded direct sum and add algebra multiplication/unit structure | `STY-52` |
| `GroupModules`, finite/free/presented group-module categories, `GroupLattices` | Same `(R,G)` canonicalization/storage/accessors repeated | Common parameterized category abstraction | `STY-53` |
| `GroupModuleHomset` / `GradedModuleHomset` assignments from `ModuleHomset` | Manual inheritance by method grafting | Common Hom implementation/category inheritance | `STY-06` |
| group-module `base_change` versus scalar-extension functor | Same action-transport algorithm implemented twice | One canonical base-change implementation; functor/object method delegates | `STY-54` |
| `_MODULE_TENSOR_PRODUCT_CACHE`, `_MODULE_POWER_CACHE`, form/Kähler/de Rham/etc. caches | Every theory invents identity/lifetime semantics | Shared identity memoization, `UniqueRepresentation`, `cached_function`/`cached_method` where correct | `STY-55` |
| Fourier/Hermite/Laurent/sinc enumerated-function parents | Same infinite indexed-parent implementation repeated | One indexed-symbol/indexed-function-set abstraction | `STY-52`, `56` |
| `_singular_presentation_kernel` | Python orchestrates a long multi-stage Singular workflow | Native/batched Singular routine behind one adapter crossing | `STY-57`–`59` |
| torsion-form orbit/stabilizer code | Specialized theory directly performs GAP orbit/stabilizer work despite owned action infrastructure | Action/G-set orbit/stabilizer API delegating privately to GAP | `STY-40`–`42`, `57`–`59` |
| `forms.py::_coordinate_values` nested `total += ...` | Hand-written finite bilinear sum | Pairing/Hom evaluation or declarative finite sum | `STY-28`, `30`, `73` |
| `sparse_free_algebras.py::_multiply_in_target` | `result=one; for factor: result *= factor` is pure fold boilerplate | Parent-owned product, otherwise `reduce`; `math.prod` for ordinary numbers | `STY-29`, `74` |
| `modules/powers.py::_divided_product_coefficient` | Manual product fold plus a second loop that only multiplies by `1` | Owned/numeric product fold; delete algebraically inert loop | `STY-29`, `31`, `74` |
| `lattices.py::decomposition_names` | `names=[]; ... names.extend(...)` flattening | Lazy owned family or `chain.from_iterable` at a private Python layer | `STY-14`, `60`, `70` |
| profinite embedding filters | `compatible=[]; for candidate: if all(...): append(candidate)` | filtered comprehension/generator or `filter` | `STY-10`, `22`, `69`, `79` |
| `schemes.py::refine_scheme` category-type accumulation | `set(); for ...: add(type(...))` | set comprehension, subject to broader refinement redesign | `STY-12`, `71` |
| multiple `setdefault(...).append(...)` / `.get(...)+...` coefficient/grouping sites | Repeated generic grouping/accumulation machinery | `defaultdict`, `Counter`, or owned finite-support object | `STY-32`–`34`, `65`, `75`–`78` |
| multiple frontier/seen loops in G-sets, orthogonal quotients, discriminant modules | Generic traversal/orbit machinery is repeatedly open-coded | owned action/G-set/graph operation or mature traversal dependency; explicit loop only if algorithm is genuinely special | `STY-39`–`43`, `68` |
| `assert False` stubs in tensor methods | A visible method is being used as a deceitful placeholder rather than a mathematical promise | Sage `@abstract_method` for a genuine abstract contract, or remove/move the method if it is not defined there | `STY-48` |
| finite-rank/nondegeneracy/category-containment assertions | These loudly record the proof context of an implementation | **Keep/add informative assertions**; move the method only when the operation itself belongs to a narrower mathematical category | `STY-49` |
| `preamble/utilities.py` helpers such as `lmap`/`lzip` have no backend callers | Internal-use grep does not measure a REPL/notebook preamble API | Preserve deliberate session conveniences and ensure they are actually exported/tested as session vocabulary | `STY-88` |

These examples are evidence for the general rules, not a finite whitelist.  When the same code shape appears elsewhere, apply the rule without waiting for that file to be named here.

#### `STY-88`: No internal callers does not imply dead code on a session surface

This repository is a research preamble.  Names may exist specifically so they are available interactively in notebooks and REPL sessions; such functions can correctly have zero call sites in `src/` and `tests/`.

**Bad review heuristic:**

```text
rg finds no internal calls to lmap/lzip -> delete them as dead code
```

**Preferred:** determine whether the name is deliberate session vocabulary.  If it is, ensure it is exported by `preamble.all`, has obvious stable semantics, and is exercised as part of the session surface.  Internal call graphs measure implementation reuse, not interactive usefulness.

Thin wrappers are therefore judged by **session ergonomics**, not by whether backend code calls them.  `lmap(f, xs)` and `lzip(xs, ys)` can be legitimate preamble conveniences precisely because their meanings are obvious and they save repetitive REPL typing.

#### `STY-89`: Method visibility follows mathematical definability, not current decidability

A method visible under tab completion says: **this notion is mathematically defined for this object**. It does *not* promise that the CAS can decide or compute it for every represented instance today.

Canonical example: a set such as

```python
X = {n in NN | n.is_twin_prime()}
```

unquestionably has a cardinality. Hiding `cardinality()` behind a fictional `SetsWithComputableCardinality` category would misstate the mathematics. A user may reasonably encounter an assertion explaining that the current algorithm does not cover this representation.

Likewise `is_nondegenerate()` belongs on formed modules/lattices where nondegeneracy is a defined property, even if an infinite-rank callable form is outside today's decision procedures.

The long-term goal is **hope matches reality**: every mathematically natural method is visible where it belongs, common cases compute correctly, unsupported computational cases fail immediately and informatively, and the implemented case family expands over time.

Never use `NotImplementedError` as the fallback. Never expose a method whose only behavior is failure.

#### `STY-90`: Computability routing may use explicit mathematical case tables

Most switchboards that rediscover category ownership are architectural smells. Computational routing *within an already correctly owned mathematical method* is different and often desirable.

**Good shape:**

```python
def cardinality(self):
    match self:
        case FiniteEnumeratedSet():
            return NN(self._known_size())
        case IntervalIntersectionSet():
            return self._interval_cardinality()
        case RecursivelyEnumerableSet() if self._enumeration_terminates():
            return self._enumerated_cardinality()
        case _:
            assert False, (
                "cardinality is mathematically defined for every set, but the current "
                "implementation has no algorithm for this represented case"
            )
```

The exact cases/algorithms must reflect real repository mathematics; the point is the architecture. The method is owned by `Sets`, implemented on genuine supported cases, and the final assertion documents the current computational frontier.

When static typing genuinely makes the final branch `Never`, prefer `typing.assert_never` as the exhaustiveness marker. When the runtime category/representation partition is not statically expressible, an informative final `assert False, ...` is reasonable here. The distinction from a stub is that preceding branches implement real mathematics.

Similarly:

```python
def is_nondegenerate(self):
    match self:
        case FiniteRankRepresentedForm():
            return self.gram_tensor().determinant() != 0
        case _:
            assert False, (
                "nondegeneracy is currently decidable only for represented finite-rank forms"
            )
```

Prefer specialized subcategory overrides when they give a cleaner implementation, but do not move the *mathematical notion* into a fake computability category merely because one algorithm is partial.

Mathematical code still avoids exception-driven fallback, `hasattr` probing, and try/catch routing. Engineering adapters may catch external failures; the mathematical layer routes by declared mathematical representation/category and asserts the unsupported remainder.

### Finitary-overfitting and semantic-lowering patterns

#### `STY-91`: Eagerly materialize a mathematical family -> keep the owned set/family lazy

**Red flag:**

```python
labels = tuple(M.module_generating_set())
generators = list(G.group_generators())
objects = tuple(C.object(x) for x in C.object_set())
```

The coercion silently changes "this mathematical family exists" into "this family can be exhausted now."  That is a much stronger assumption and often the source of infinite-case blast radius.

**Preferred:** keep the owned set/indexed family itself and use iteration, membership, `cardinality`, `rank`/`unrank`, finite support, images, or lazy enumeration as needed.  If a backend requires a finite array, assert the required finiteness and serialize at that private boundary only.

Concrete smell: `DiscreteCategory.objects()` must not turn an arbitrary enumerable object set into a tuple; the objects of a discrete category are the owned image of its object set, which can be infinite.

#### `STY-92`: Finite-support elements -> do not require a finite indexing set

Many mathematical objects have **finite support over an infinite family**.  Do not confuse these two notions.

**Bad:**

```python
def FormalDivisorGroup(R, prime_divisors):
    return FreshFreeModuleOn(R, finite_ordered_set(prime_divisors))
```

if the intended divisor group is the free module on an arbitrary set of prime divisors.  Individual divisors have finite support; the set of possible prime divisors need not be finite.

**Preferred:** the parent is free on the owned prime-divisor set; each divisor element stores only its finite support.  The same principle applies to free modules, group rings, sparse polynomials, formal sums, configurations, and indexed families.

#### `STY-93`: Raw matrix rows/columns implement a theorem -> ask the semantic mathematical objects instead

Rows, columns, basis matrices, and coordinate vectors are representations.  If the theorem can be stated without coordinates, the implementation should be stated that way too.

**Bad:**

```python
image_rows = matrix_of(d1).row_module()
relation_rows = presentation_matrix(M).row_module()
return image_rows == relation_rows
```

**Preferred:**

```python
return d1.image() == augmentation.kernel()
```

with subobject/Hom equality owning whatever finite-coordinate algorithm is presently available.  This allows future infinite/theorem-backed equality algorithms without rewriting `FreeResolution.is_exact()`.

#### `STY-94`: Assemble block matrices by hand -> construct the block morphism on biproducts/direct sums

**Bad:** concatenate row arrays, slice columns, or call a matrix `stack` operation to represent a map

\[
A_1\oplus A_2 \longrightarrow B_1\oplus B_2.
\]

**Preferred:** construct the morphism from its four components

\[
f_{ij}:A_j\to B_i
\]

through the Hom/biproduct API.  A finite matrix backend may realize this as a block matrix privately.  The public object remains a morphism between biproducts, so the same construction can represent an infinite block family or a formal block Hom without changing consumers.

#### `STY-95`: Compute cohomology from kernel basis matrices -> `ker/im/quotient` semantics

**Bad:** build lift matrices, take a backend right kernel, choose a basis matrix, project rows, append denominator rows, re-coordinate them, and finally synthesize a presentation.

**Preferred mathematical definition:**

```python
cycles = d_n.kernel()
boundaries = d_previous.image()
return cycles.quotient(boundaries)
```

or the corresponding subobject/quotient construction already owned by the complex.  A finite-presentation backend may optimize this entire construction, but it belongs behind `kernel`, `image`, subobject inclusion, and quotient.  `Cohomology` should not know row orientation or basis-matrix conventions.

#### `STY-96`: Compute an intersection/preimage from kernel rows -> categorical pullback/kernel

The current coordinate identity may be correct while still being the wrong abstraction.

**Bad:** form matrices for inclusions, stack `(i,-j)`, compute a left kernel, extract half the coordinates, turn its rows back into generators.

**Preferred:** the intersection of subobjects is the pullback of their inclusions; the inverse image of `S -> N` along `f:M->N` is the pullback of `f` and the inclusion, equivalently the appropriate kernel construction when additive structure is available.  Construct that pullback/kernel as a subobject.  Let the finite-free Hom implementation choose the matrix algorithm privately.

Concrete current sites: `modules/subobjects.py::intersection` and `functors/subobject_images.py::_inverse_image_subobject` already describe this universal property in comments but then drop to raw rows.

#### `STY-97`: Invariants/coinvariants require finite generators -> use the action's equalizer/coequalizer semantics

**Bad:** require a chosen finite group generating set, build one kernel for every generator, intersect them, or build all relations `(g,m) -> gm-m` from a finite Cartesian product of generator sets.

**Preferred:** `M^G` is the fixed-point/equalizer subobject of the action; `M_G` is the corresponding coequalizer/quotient.  The action object owns these constructions.  A finitely generated group gives a convenient finite algorithm, but finite generation must not define the existence or public shape of invariants/coinvariants.

This also avoids the blast radius when `G` is infinitely generated but represented by a stronger action theorem/backend.

#### `STY-98`: Exhaustively test every element to recognize structure -> structural maps/theorems first, finite exhaustion only as a fallback case

**Bad default:** enumerate every element of a finite underlying set and every scalar, then test all triples to decide associativity/module laws or enumerate every element to compute an annihilator.

**Preferred:** express the structure by the mathematical maps that make the law meaningful and use category/theorem-backed algorithms.  For a module, the scalar action is `rho:R -> End(M)`; for the annihilator, use the kernel/ideal of the scalar-action morphism where represented.  An exhaustive finite check can remain one explicit computability case in a routing table, but must not become the ontology or the only architecture.

Concrete smell: `GeneralModuleParent.annihilator()` currently enumerates the scalar ring and entire module; `_verify_module_laws_when_decidable()` performs cubic scans of the underlying set.  Those are acceptable finite diagnostics/fallbacks, not the general mathematical implementation strategy.

#### `STY-99`: Return `tuple`/`list` for a mathematical set/family -> return an owned set/family or lazy enumeration

**Bad:**

```python
def roots_of_square(...):
    return tuple(...)

def vector_orbit_representatives(...):
    return tuple(representatives)
```

unless the Python tuple is explicitly private serialization.

**Preferred:** return the relevant owned finite set, ordered set, indexed family, orbit-representative set, or lazy enumerated set.  Finiteness is a property of that mathematical collection, not a reason to replace it by a Python sequence.

#### `STY-100`: Presentation matrix is an implementation of a presented object, not the object itself

A chosen finite presentation legitimately has a finite matrix realization.  The error is letting ordinary mathematical consumers treat that matrix as the only interface to the presentation.

**Bad:** consumer code calls `.rows()`, slices columns, counts row lengths, takes row modules, and reconstructs subobjects manually.

**Preferred:** consumers ask for the presentation morphism, its image/kernel/cokernel, its relation subobject, base change, or the corresponding universal construction.  The presentation subsystem may use a matrix internally when the chosen framings are finite.

#### `STY-101`: Fiber/rank/minimal-generators via hand-specialized relation matrix -> construct the fiber/residue module and ask it

**Bad:** specialize every relation row modulo a prime/maximal ideal, build a backend matrix, compute its rank, then subtract from a generator count inside `fiber_dimension()` or `minimal_number_of_generators()`.

**Preferred:**

```python
fiber = M.fiber(p)
return fiber.dimension()
```

and for a local ring use `M.residue_module().dimension()` as Nakayama dictates.  The vector-space/presented-module implementation may compute that dimension by matrix rank privately.  This keeps localization, base change, residue fields, and dimension as the semantic spine.

#### `STY-102`: Verify structure by checking every pair of chosen basis generators -> verify the structure morphism

**Bad:** for every chosen group generator and every pair of lattice generators, compare all pairings to verify that an action preserves the form.

**Preferred:** the action is a morphism

\[
G \longrightarrow \operatorname{Aut}(L,b)
\]

or its image maps are verified by the formed-module Hom/automorphism category.  Form preservation is equality/commutation of the correlation/form morphism, not a nested finite basis loop.  A finite Gram check may be the implementation of that Hom predicate, but callers should not know it.

Concrete current site: `group_modules/group_lattices.py::GroupLattice` explicitly assumes finite rank and finite group generation solely to run this exhaustive check.

#### `STY-103`: Coordinate/numeric algorithm appears above the semantic owner -> push it down behind the owner

Use this as the general review test.  If code in cohomology, exactness, lattice structure, group actions, subobjects, or geometry manipulates raw `rows`, `columns`, `basis_matrix`, flattened entries, or coordinate vectors, ask whether that numeric code belongs instead in the Hom/module/tensor/subobject/backend operation it is trying to compute.

**Preferred layering:**

```text
mathematical consumer
    -> semantic operation (kernel/image/pullback/product/dimension/...)
        -> category/representation-specific algorithm
            -> finite coordinates / matrix / CAS backend
```

not:

```text
mathematical consumer
    -> rows/columns/coordinates
        -> manually reconstruct the semantic result
```

The latter makes every consumer finite-coordinate-aware and gives infinite generalization a repository-wide blast radius.


#### `STY-104`: `morphism -> matrix -> nullspace -> rebuilt submodule` -> `morphism.kernel()`

This is a canonical LLM over-lowering pattern.

**Bad:**

```python
A = f.matrix()
rows = A.right_kernel().basis_matrix().rows()
K = FreeModule(R, len(rows))
inclusion = ...  # rebuild the vectors as elements of f.domain()
return K, inclusion
```

**Preferred:**

```python
return f.kernel()
```

The kernel implementation owns coordinate algorithms and returns an honest subobject/inclusion. A caller that only needs the kernel never sees a matrix.

#### `STY-105`: Numerical criterion for a structural predicate -> spell the mathematical definition

**Bad:**

```python
def is_primitive(i):
    A = i.matrix()
    return gcd(maximal_minors(A)) == 1
```

**Preferred:**

```python
def is_primitive(i):
    return i.cokernel().is_torsion_free()
```

Similarly, prefer `f.kernel().is_zero()` to rank comparison for injectivity, the correlation morphism to determinant tests for nondegeneracy, and `correlation.is_isomorphism()` to determinant-unit tests for unimodularity. Numerical criteria belong inside the implementations of these semantic predicates, where their hypotheses can be routed correctly.

#### `STY-106`: Consumer extracts coordinates because the semantic operation is missing -> add the semantic operation first

**Bad development behavior:**

```python
# There is no useful Subobject.pullback yet, so this one caller manually
# stacks inclusion matrices and takes a kernel.
```

**Preferred:** implement/fix the pullback, kernel, subobject, or other semantic operation at its mathematical owner, then make the consumer one or two semantic calls.

A missing semantic API is not external scope. It is evidence that the local feature has reached a foundational abstraction that must be strengthened. The smallest architecturally correct patch may therefore touch a lower-level category/Hom/subobject module before simplifying the original caller.

#### `STY-107`: Downstream finite/infinite case split -> move representation routing into the semantic owner

**Bad:**

```python
if M.module_rank().is_finite():
    A = f.matrix()
    ...
else:
    ...  # every consumer invents another infinite branch
```

**Preferred:**

```python
K = f.kernel()
```

with `kernel()` itself routing finite-free, finitely-presented, sparse/infinite, theorem-backed, or engine-specific cases. Downstream mathematics should normally be representation-oblivious.

#### `STY-108`: Local helper that reconstructs a universal construction -> delete it in favor of the universal construction

**Red flags:** helpers named or behaving like `_kernel_from_matrix`, `_intersection_from_rows`, `_preimage_from_coefficients`, `_quotient_from_relations`, `_image_basis`, `_block_matrix_for_map`, or `_rank_from_presentation` in a downstream theory module.

Before retaining such a helper, ask whether it is merely rebuilding `kernel`, `image`, `pullback`, `cokernel`, `quotient`, biproduct/block-Hom, `fiber`, `dimension`, or another existing universal construction. If yes, use or repair that construction instead.

#### `STY-109`: A theorem stated semantically but implemented numerically in the caller -> make the code resemble the theorem

**Bad:** a comment says “the intersection is the pullback” or “cohomology is cycles modulo boundaries,” followed by dozens of lines manipulating matrices.

**Preferred:** the executable code should retain the same nouns and arrows as the mathematical statement:

```python
intersection = pullback(i, j)
H_n = d_n.kernel().quotient(d_previous.image())
exact = d1.image() == augmentation.kernel()
```

If these calls are not yet capable enough, repair them. A comment stating the correct abstraction does not excuse implementation at the wrong layer.

#### `STY-110`: Repeated numerical extraction is API feedback, not a reason for another extraction

The first downstream `.matrix()`/`.rows()` workaround may reveal a missing method. The second occurrence is strong evidence of a missing semantic abstraction. Do not copy the workaround into a third consumer.

When several callers need “kernel as subobject,” “span as subobject,” “block morphism,” “dimension after base change,” “torsion-free quotient,” or another recurring mathematical result, promote that operation to the common owner and delete the caller-specific numeric implementations.

#### `STY-111`: Optimize the semantic method, not each consumer

If a semantic composition is mathematically right but slow, preserve it as the mathematical route and optimize underneath it.

**Bad:** replace `i.cokernel().is_torsion_free()` in one lattice routine by a hand-written gcd/minor test because it is faster there.

**Preferred:** teach `cokernel()`/`is_torsion_free()` the efficient finite-presentation or Smith-form case. Every caller then gets the optimization, and future infinite cases still have one routing point.

This remains the preferred direction even when the low-level optimization internally collapses several semantic stages into one backend call.

#### `STY-112`: Coordinate tuple/vector as element input -> construct the element in its parent

Coordinates are observations relative to chosen data, not a second element language.

**Bad:** `x = L([1, 2])` or `y = M(tuple(coefficients))` when the bare sequence is admitted as an alternate public spelling for an element.

**Preferred:** use the parent's named generators / finite-support mathematical construction and form the element in the parent's language, e.g. `x = e + 2*f`, or an owned finite-support coefficient datum whose parent/index set is explicit.  A private backend adapter may serialize that element to a vector after construction.

#### `STY-113`: Matrix -> morphism may be construction; morphism -> matrix -> conclusion is a red flag

The coordinate boundary is directional.  A finite framed Hom constructor may consume matrix data to construct the actual morphism, validate domain/codomain/relations, and return the Hom element.  Once `f` exists, stay with `f`.

**Bad:** `A = f.matrix()` followed by a conclusion about injectivity, image, kernel, cokernel, primitivity, or form preservation.

**Preferred:** `f.kernel()`, `f.image()`, `f.cokernel()`, `f.is_injective()`, `f.is_surjective()`, composition, and Hom predicates.  The owner may internally return to a matrix for the finite case.

#### `STY-114`: Zero-matrix/entry-fill loops -> whole-object constructor, then semantic wrapper

Inside a private finite-coordinate boundary, do not manually own standard row/column layout when Sage already names it.

**Bad:** allocate a zero matrix and fill diagonal/block/column entries with nested index loops.

**Preferred finite backend idioms:** `matrix(rows)`, `column_matrix(columns)`, `diagonal_matrix`, `block_matrix`, `block_diagonal_matrix`, `identity_matrix`, `zero_matrix`, sparse constructors, `.apply_map`, and slicing.  Better still, if the object is mathematically a biproduct morphism, form, or endomorphism, construct that semantic object and let its backend choose the matrix constructor.

#### `STY-115`: Ported Sage signature -> resite the mathematics; never port the ontology

A foreign method name/signature is evidence about available computation, not a contract for the owned API.

**Red flags:** `ambient=`, `in_ambient=`, `even=`, `negative=`, mode booleans naming category membership, or a method on a bare object whose actual datum is an inclusion/morphism/base change.

**Bad:** `L.saturation(in_ambient=M)` or `Lattice(G, even=True)` when the parameter compensates for missing categorical structure.

**Preferred:** saturation on the subobject/inclusion; construct the general lattice/form and let category refinement record evenness or other derived structure.  Port **semantic capability**, not signature parity.

#### `STY-116`: Structure/category membership flag -> infer/refine it as output

Do not ask the caller to state a property the constructed mathematical datum already determines.

**Bad:** `Lattice(G, even=True)`, `Form(..., nondegenerate=True)`, `Module(..., torsion=True)` when those facts are decidable/declared from the datum.

**Preferred:** construct from the defining datum, then place/refine the result into the strongest justified categories.  A genuinely chosen structure is different and must be supplied as its actual datum, not as a boolean.

#### `STY-117`: Witness-compensating parameter -> first-class witness object

**Bad:** an operation on `A` accepts `ambient=B`, `inclusion=...`, or another optional parameter solely because `A` does not carry the relationship the operation needs.

**Preferred:** construct/use the subobject, morphism, functor image, base-changed object, or other witness-bearing object and put the operation there.  For a subobject, the “ambient” is simply `inclusion().codomain()`.

#### `STY-118`: Compatibility shim/alias after a redesign -> update callers and delete the old route

**Bad:** keep an obsolete ambiguous API and add the precise name as a wrapper over it, or retain an old constructor solely so internal callers continue to work.

**Preferred:** make the precise/canonical API the implementation, migrate all callers in the same change, and delete the superseded route.  Deliberate REPL conveniences such as `lmap` are not compatibility shims; they are intentional session vocabulary.

#### `STY-119`: Tiny internal wrapper with no semantic role -> call the existing operation directly

A short function is justified when it is a canonical semantic owner, a boundary, a constructor, or deliberate session notation.  It is not justified merely to rename an already-clear operation locally.

**Bad:** `def _make_identity(n): return identity_matrix(ZZ, n)`.

**Preferred:** call `identity_matrix(ZZ, n)` directly, or introduce a wrapper only when it centralizes mathematical validation/ownership that every caller must share.

#### `STY-120`: `globals()` mutation / dynamic sibling import -> static names and a repaired DAG

**Bad:** `globals().update(...)`, `global X` used to install exports dynamically, or `importlib.import_module(...)` used to postpone a sibling import and hide a cycle.

**Preferred:** ordinary module-scope imports/type aliases, or move the shared definition into a dependency-light defining module.  Optional external plugins may require dynamic loading at an engineering boundary; ordinary mathematical modules do not.

#### `STY-121`: QC-only statement/suppression -> fix the code or the shared tooling

Do not add executable or annotation noise whose only purpose is to silence a checker.

**Red flags:** `del arg` in an abstract/overload body, gratuitous casts, broad `Any`, `# type: ignore`, `# noqa`, or compatibility wrappers introduced only to reduce a warning count.

**Preferred:** if the diagnostic exposes a real mathematical/API defect, repair it.  If the checker lacks knowledge of Sage/category machinery, repair the shared stub/plugin/QC configuration.  A narrow suppression is admissible only for a genuinely untyped external boundary and must document that boundary.

#### `STY-122`: Test unwraps coordinates/matrices to state a semantic claim -> test the mathematical object

**Bad:** a test claims something about a kernel/image/subobject/isometry but compares matrix ranks, coordinate tuples, kernel basis rows, or raw backend objects.

**Preferred:** construct typed elements/morphisms and assert `f.kernel()`, `f.image()`, `f.cokernel()`, `f.is_surjective()`, subobject equality, isomorphism witnesses, or the named invariant.  If the test cannot state the claim without unwrapping coordinates, add the missing semantic noun/verb first.

#### `STY-123`: Numerical shadow used as the test claim -> assert the named invariant/structure

Determinants, ranks, coordinate lists, and cardinalities are legitimate when *they are the mathematical invariant under test*.  They are not substitutes for a stronger structural claim.

**Bad:** determinant equality as the sole claim that two lattices are isometric; row equality as the sole claim that two morphisms agree; rank equality as surjectivity.

**Preferred:** assert the actual isomorphism/equality/morphism predicate, and optionally cross-check the numerical shadow as a secondary invariant.

#### `STY-124`: Stale issue/docstring/comment/test after a ruling -> repair the prescription before code

A prescription that describes the rejected model is a code generator for future regressions.

**Red flags:** issue bodies naming old constructor signatures, comments explaining a coordinate workaround that policy has rejected, dead docstrings claiming a semantic implementation above numerical proxy code, generated/reference tests preserving a superseded API.

**Preferred:** update or delete the authoritative record immediately when the ruling lands, then continue implementation from the corrected record.

#### `STY-125`: Correct failure is inconvenient -> repair the defect; never launder the failure

**Bad remediation:** delete/weaken a mathematically correct assertion or red test, narrow the stated requirement after implementation fails, patch an unrelated symptom, or make the condemned representation “work” just enough to turn the check green.

**Preferred:** preserve the proposition/contract, treat the failure as evidence locating the real defect, and repair that defect.  Restarting an implementation while preserving the contract is acceptable; manufacturing success by weakening truth is not.

#### `STY-126`: Copy/port old implementation structure -> semantic reconciliation

When absorbing archived/legacy code, first map every notion onto the current owned ontology.

**Bad:** copy a module/class hierarchy because it already implements the algorithm, or quarantine only a tiny slice while leaving duplicate notions.

**Preferred:** reuse current categories/functors/Homs where the notion already exists; rewrite only genuinely missing mathematics into current owners and style.  Preserve semantics, not directory layout, class names, or historical architecture.

#### `STY-127`: Bare multi-structure generator name -> qualify the structure

**Bad owned vocabulary:** `generator`, `generators`, `generating_set`, `ngens`, `embedded_gens` when an object can simultaneously carry module, algebra, and group structures.

**Preferred:** `module_generator`, `module_generating_set`, `group_generators`, `algebra_generating_set`, `number_of_module_generators`, etc.  Do not keep the bare name as a compatibility alias.  Native Sage `.gens()` names remain native inside backend calls.

#### `STY-128`: Public presentation-facing constructor -> canonical constructor from mathematical datum

**Bad primary API:** `from_matrix`, `from_relations`, `with_action(G, matrices)`, or a subobject constructor from raw rows when the actual datum is a morphism/action/inclusion/presentation.

**Preferred:** construct the defining morphism in its Hom, then pass that object to the canonical constructor.  Coordinate/matrix conveniences, where mathematically unambiguous for a canonically framed Hom, immediately produce the mathematical object and are not a second downstream language.

#### `STY-129`: “Not computable in full” -> still construct the predicate-defined mathematical object

Do not confuse inability to enumerate/generate an object with inability to represent it.

**Bad:** refuse to construct `O(L)`, a stabilizer, a center, or another predicate carve-out because generators/relations are unavailable.

**Preferred:** construct the owned predicate-defined subgroup/subset/category with membership and the operations that are available.  Add enumeration/generator algorithms as computable cases later.  A predicate must not claim `True` merely on trust; construction-time trust, when unavoidable, is a separately documented choice.

#### `STY-130`: Definition hard-codes a removable hypothesis -> formulate generally, recover the special case by refinement

**Red flags:** a framing requires a finite/ordered set although the definition only needs a set; a direct-sum notion is defined only for finite families because the first backend is matrix-based; a construction is named after one base ring even though its definition works over a wider ring class.

**Preferred:** state the notion at the weakest hypotheses under which it remains mathematically meaningful, then recover finite/free/projective/ordered/enumerable/commutative special cases as axioms, subcategories, or algorithmic cases.  Use extreme infinite/nonenumerable objects as stress tests of the interface even when the current computation does not handle them.

#### `STY-131`: Hidden mathematical choice / definite article -> name the selecting datum

**Red flags:** “the dual”, “the extension”, “the normalization”, `normalize=True`, `map=True`, or another flag whose value changes which mathematical object/morphism is selected, without the choice being represented explicitly.

**Preferred:** determine whether the object is canonical.  If not, give the alternatives distinct mathematical names or accept/store the selected morphism/object/structure as first-class data.  A normalization/re-presentation is a new object together with its isomorphism; a chosen framing, orientation, action, embedding, closure presentation, or section is an actual datum, not a boolean mode.

#### `STY-132`: Subobject equality that forgets the inclusion -> compare the slice object

A subobject is not merely an object that happens to be isomorphic to something inside another object.  It is the object **together with its witnessing monomorphism**.

**Bad:**

```python
def __eq__(self, other):
    return self.underlying_object() == other.underlying_object()
```

for subobjects `i:S -> M` and `j:T -> M`.  Two isomorphic copies of the same abstract module embedded differently in `M` are different subobjects.

**Preferred:** equality of subobjects is equality in the relevant slice/subobject category: compare the underlying owned object together with the inclusion morphism (or delegate to the owned subobject/category equality that already does so).  Never reconstruct equality from common coordinates in the codomain.

#### `STY-133`: Quotient equality that forgets the projection -> compare the coslice/quotient object

The dual error occurs for quotients.  A quotient is not just its abstract codomain `Q`; it is the epimorphism `p:M ->> Q` together with that codomain.

**Bad:** treat two quotient presentations as the same quotient because their codomains are isomorphic or have equal invariant factors.

**Preferred:** keep the quotient/projection morphism first-class.  Equality as quotient objects includes the epi; an abstract codomain may be isomorphic while representing a different quotient of `M`.

#### `STY-134`: Identify an object with its image -> keep the morphism and image subobject distinct

**Bad:** because `f:X -> Y` is injective or surjective, silently identify `X` with `f(X)` or `Y` with the image, then let later code use equality where a morphism is the actual relationship.

**Preferred:** `f` is the relationship; `f.image()` is a subobject of the codomain; `X` remains the domain object.  Even when `f` is an isomorphism, equality and the exhibited isomorphism are different mathematical statements unless the construction is canonically identical by repository policy.

This applies to dual inclusions, rationalization/base change maps, quotient projections, embeddings, and all other arrows.  Do not erase the arrow merely because its image has a familiar description.

#### `STY-135`: Normalization mutates the object / hides behind a flag -> return the new object and isomorphism

A normal form or re-presentation changes chosen data.  That means it produces a different object of the framed/presented category, related to the source by an isomorphism.

**Bad:**

```python
M.normalize(in_place=True)
M.normal_form(transformation=False)
```

or replacing `M`'s chosen framing/presentation internally by a Smith/Hermite/canonical one.

**Preferred:**

```python
iso = M.invariant_factor_form()
normalized = iso.codomain()
```

where the returned isomorphism is part of the mathematical result.  The transformation is not optional metadata: it is what states why the new presentation represents the same abstract mathematics.

#### `STY-136`: Universal construction returns only a naked object -> return/attach its canonical structure morphism

A kernel, image, cokernel, quotient, pullback, pushout, product, coproduct, or similar construction is incomplete if the universal structure maps have been discarded.

**Bad:** `f.kernel()` returns a module whose basis happens to span the nullspace but has no inclusion into `f.domain()`; `f.cokernel()` returns an abstract presented module with no canonical projection from `f.codomain()`.

**Preferred:** the owned result carries or canonically exposes the relevant maps: kernel inclusion, image inclusion/factorization, cokernel projection, product projections, coproduct injections, pullback legs, pushout legs, and so on.  Downstream code should be able to use the universal property without reconstructing those arrows from coordinates.

A quotient element's `lift()` may select a representative; it is not a canonical inverse to the quotient projection and must not be presented as one.

#### `STY-137`: Test a weaker equivalence relation on equal objects -> use genuinely different objects

**Bad:** test `is_isomorphic`, `is_isometric`, same-genus, or another relation weaker than equality using `X` and `X` or two constructions that canonicalize to the same owned object.  Equality makes the weaker claim tautological.

**Preferred:** choose distinct objects/presentations known to be related in the weaker sense: two differently framed but isomorphic modules, two different Gram presentations of isometric lattices, or genuinely distinct representatives in one genus.  The test must be capable of falsifying the weaker-relation implementation.

#### `STY-138`: Implementation-role noun -> identify the standard mathematical object or datum

LLM-generated code often invents an implementation ontology around words such as `provider`, `manager`, `context`, `evidence`, `knowledge`, `metadata`, `payload`, or `wrapper` when the thing is already a standard mathematical object.

**Bad:** ask a caller for a `SubobjectEvidence`, `GeneratorProvider`, or `NormalizationContext` when the actual datum is an inclusion morphism, indexed family, isomorphism, framing, or functor.

**Preferred:** name and type the actual mathematics.  Before introducing a helper noun, ask whether a mathematician could define it independently of this codebase and whether an existing category/object/morphism/functor already is that thing.  Engineering records may exist at engineering boundaries; they do not become public mathematical ontology.

#### `STY-139`: Brainstorm wrappers/overloads/adapters before stating the mathematics -> state the mathematical model first

**Bad review sequence:** encounter a signature collision or missing operation and immediately compare overloads, optional arguments, wrappers, adapters, casts, aliases, registries, or dispatch tricks.

**Preferred sequence:** first state what `self` is mathematically, what datum the operation consumes, where it is well-defined, what object owns it, and what its mathematical return object is.  Only after that model is fixed choose the smallest Python/Sage mechanism that realizes it.  If naming the mathematics makes the engineering alternatives disappear, discard them.

#### `STY-140`: Reviewer names one symptom -> patch only that symptom while preserving the contaminated implementation

A review finding is evidence about a generator, not a specification saying “remove this exact line and preserve everything else.”

**Bad:** a reviewer flags matrix-based kernel reconstruction, so move the same reconstruction into a helper/adapter and leave all callers and tests semantically unchanged; a reviewer flags a global dispatcher, so hide the switchboard behind a registry without changing ownership.

**Preferred:** identify the architectural generator that produced the finding, inspect sibling instances and consumers, repair the semantic owner, and simplify the callers.  Do not make preservation of the currently contaminated implementation or its representation-level tests an unstated acceptance criterion.

#### `STY-141`: Invent canonical arrows from analogy -> read the actual universal diagram

Do not infer structure maps because an object “looks like” a product, quotient, tensor, or coordinate construction.  The universal property determines the canonical arrows.

**Bad:** treat `M tensor N` like a Cartesian product and invent projections `M tensor N -> M`, `M tensor N -> N`, or canonical maps `M -> M tensor N` without chosen elements.

**Preferred:** state the defining diagram.  For a tensor product, the canonical map is the bilinear set map

\[
M\times N \longrightarrow M\otimes_R N,
\]

and maps out of `M tensor N` correspond to bilinear maps out of `M × N`.  No map from either factor alone is canonical without extra selected data.  Apply the same discipline to every universal construction.

#### `STY-142`: Functor accepts too broad a category then rejects arrows -> restrict the domain category

**Bad:** define `F:C -> D`, then inside `_apply_morphism` assert/reject every non-isomorphism because the construction is only functorial on isomorphisms.

**Preferred:** declare `F:C.core() -> D`.  If the mathematical variance/domain is a slice, coslice, arrow category, subgroupoid, or other subcategory, make that the functor's actual domain.  Runtime assertions may still document internal assumptions, but they do not substitute for a mathematically wrong functor signature.

#### `STY-143`: Parameterize an intrinsic notion -> derive it from the existing structural maps

A notion with an a priori mathematical meaning is not a customization hook.

**Bad:** ask for an `integrality_submodule`, an `integral_over=` mode, or another parameter redefining what “integral” means when the existing ring map already determines integrality.

**Preferred:** derive the notion from the relevant structure already present—for example integrality in a ring extension from the specified ring morphism.  If a genuinely different notion is wanted, give it a different mathematical name rather than parameterizing the standard one into ambiguity.

#### `STY-144`: “Safe” horizontal patch during an architectural migration -> make the breaking vertical move

**Bad:** preserve every old caller, wrapper, and intermediate representation while moving one method at a time because each commit is expected to remain locally green, even though the target architecture makes much of that code disappear.

**Preferred:** move the mathematical responsibility to its final owner, migrate the affected vertical slice, delete superseded routes, and allow intermediate repository states to be broken when the active architectural work explicitly permits it.  Do not spend effort polishing code scheduled for deletion merely to preserve incremental compatibility.

#### `STY-145`: Deep specialized file owns an obviously general concern -> stop and audit placement

**Red flag:** a lattice-only file contains generic cardinality/set logic; a subobject implementation contains generic quotient machinery; a scheme leaf implements a generic product/Hom construction.

**Preferred:** stop before patching the local code and ask which more general category/object should own the concern.  Search sibling implementations for duplication and move the abstraction upward/downward to its mathematical owner.  A misplaced concern is evidence that the architecture around the site may be wrong.

#### `STY-146`: Exact mathematical result vs soft knowledge result -> use the correct codomain

Do not force every question into a Python boolean, and do not use `Unknown` to replace an exact mathematical value.

**Exact operation/predicate:** `cardinality()`, `is_nondegenerate()`, `kernel()`, etc. retain their mathematical codomain.  If today's algorithm does not cover a represented case, route known cases and assertion-gate the unsupported computational remainder as specified by `CAT-01`.

**Soft knowledge/computability predicate:** a deliberately epistemic API such as `generators_are_computable()` or `has_computed_group_generators()` may have the explicit three-valued codomain `True | False | Unknown` when “not currently known/decided” is itself what the method is asking.

**Bad:** return `False` from `is_nondegenerate()` because no algorithm is known; return `Unknown` as the “cardinality” of a set; return `True` from a soft predicate merely because construction trusted an input.

#### `STY-147`: Universal-property test checks one factorization only -> test existence and uniqueness

**Bad:** construct one factorization through a tensor product/kernel/product/etc. and assert that it commutes, while never testing the uniqueness clause—or compare the same generated map to itself twice.

**Preferred:** test the actual universal property: construct the canonical factorization, verify the diagram, and verify uniqueness against a genuinely independently constructed competing morphism where practical.  Choose nonzero/nontrivial specimens so uniqueness is not vacuous.

#### `STY-148`: Parallel Set Hom / exponential / power-set objects -> canonical identification

**Bad:** implement `Hom_Set(X,Y)`, an independent function-set parent `Y^X`, and a separate power-set parent `P(X)` with overlapping iteration/cardinality/map behavior.

**Preferred:** represent the canonical identities

\[
\operatorname{Hom}_{\mathbf{Set}}(X,Y)=Y^X,
\qquad
P(X)=2^X=\operatorname{Hom}_{\mathbf{Set}}(X,2)
\]

as object identity/one owned construction with the relevant category placements.  Cardinality and set operations then follow once from that object.  Do not preserve parallel parents merely because different callers arrived through different notation.

#### `STY-149`: Literal mathematical expected values scattered through tests -> cited reusable fact data

**Bad:** dozens of tests independently write facts such as named-lattice ranks, discriminants, orbit counts, genus classes, number-field invariants, or classification-table rows as inline literals, often with duplicated or missing provenance.

**Preferred:** put the independently verified mathematical fact in the repository's topic-organized fixture/fact corpus with its construction/identifier, value(s), citation/oracle provenance, and verification status.  Tests become thin parametrized drivers that compute the repository result and compare it to that fact.

#### `STY-150`: Current implementation output used as its own expected value -> independent source/oracle

**Bad:** run the method being tested, copy its output into a fixture, then assert future runs reproduce that output; or treat a Sage result as mathematical truth merely because Sage is the current backend under test.

**Preferred:** expected mathematical values come from an independent cited source, a separately justified oracle/reference implementation, or a migrated source-system test corpus appropriate to the task.  The implementation under test is never the provenance for its own expected result.

#### `STY-151`: Element repr exposes coordinate storage -> render the mathematical expression

**Bad:** an element of a framed/free module or lattice prints as `(2, -1, 0)` or as a backend vector, making its storage representation look like the element itself.

**Preferred:** render the owned formal linear combination in the selected generator/framing symbols, using the coefficient ring's own representation and the symbols' own representation.  Coordinates may be inspectable through an explicit framing/coordinate operation, but ordinary `repr`/LaTeX presents the mathematical element.

Do not hard-code integer-specific sign/absolute-value formatting into a generic `R`-module printer; an arbitrary coefficient ring need not have those notions.

#### `STY-152`: “Framing” stored as a finite generator list -> selected epimorphism from a free module

**Bad:** define a framed module as `M` plus `tuple(generators)` and then infer that the tuple is finite, ordered, injectively labelled, or a basis.

**Preferred:** a framing is the selected epimorphism

\[
\operatorname{Free}_R(S) \twoheadrightarrow M
\]

for an owned set `S`.  The distinguished-generator map is the underlying-set image of this morphism.  `S` may be infinite, nonenumerable, unordered, and different labels may map to the same module element.  A basis/free framing is a stronger refinement, not the generic meaning of “framed.”

#### `STY-153`: Backend-category graph used as mathematical taxonomy -> capability correspondence

**Bad:** mirror Sage's `super_categories()` graph, manufacture owned categories solely so every Sage name has a destination, or use Sage category equality/edge layout to decide mathematical identity.

**Preferred:** the owned category/functor graph defines the mathematics.  A private/versioned correspondence records which Sage categories/implementations can compute for which owned categories and operations.  Several Sage categories may provide one owned capability; one Sage category may require a normalized owned expression.  Backend taxonomy is empirical implementation data, not ontology.

#### `STY-154`: Descendants repeat inherited operations -> fulfill obligations through the preferred functor

**Bad:** lattices reimplement cardinality/iteration, modules reimplement generic set products, every structured category writes its own version of an operation already owned below a forgetful/structure functor.

**Preferred:** declare the semantic operation once and identify a preferred structure-forgetting/projection functor at the appropriate rollup point.  Delegate `X.operation()` through that functor when the target category already owns the operation.  A descendant implements only the new structure or a genuinely better algorithm justified by its refinement.

#### `STY-155`: Constructor named after a derived subcategory -> construct at the owning root and refine the result

**Bad:** require the user to choose `RootLattice(...)`, `EvenLattice(...)`, `TorsionModule(...)`, or another specialized constructor merely because the resulting object happens to satisfy that property.

**Preferred:** construct through the ordinary owning category/object constructor from the defining datum, then let the resulting object acquire every justified refinement.  The researcher should construct the mathematics they know, not predict the internal category routing first.

A specialized constructor remains justified only when the specialized name denotes genuinely additional **input structure**, not a property derivable from the supplied datum.

#### `STY-156`: Hand-authored forgetful/projection graph -> derive structural arrows from category expressions

**Bad:** maintain one table saying `C.A -> C`, another registry of ancestor forgetful functors, and hand-written forwarding paths that duplicate what the category/classifier construction already determines.

**Preferred:** if `C.A` is defined as a classifier application/pullback, its projection to `C` is part of that definition; ancestor projections are compositions of those structural arrows.  Store/implement the defining category expression and derive the canonical projection hierarchy from it rather than maintaining a second graph that can drift.

#### `STY-157`: Public `*args` / `**kwargs` option bag -> closed mathematical signature

**Red flag:**

```python
def construct(x, *args, **kwargs):
    return backend_constructor(x, *args, **kwargs)
```

on a public mathematical surface.

**Preferred:** enumerate the actual mathematical input shapes the preamble supports and give them precise signatures, named constructors, or source-grounded overloads.  A homogeneous variadic family is acceptable only when the mathematics itself is genuinely variadic and the element type/meaning is fixed; arbitrary backend option forwarding is not.

Private backend adapters may use `*args`/`**kwargs` when their entire job is literal protocol forwarding inside the boundary and the option bag cannot escape into the public mathematical contract.

#### `STY-158`: `None` sentinel selects a different mathematical operation/object -> split or make the datum explicit

**Bad:**

```python
def normalize(M, map=None): ...
def construction(X, ambient=None): ...
```

where `None` versus a value changes the mathematical object, witness, domain, codomain, or return shape.

**Preferred:** use distinct mathematical operations/constructors or accept the actual selected datum (morphism, ambient object when genuinely part of the definition, section, framing, etc.).  If omission means a genuinely canonical default such as the unit `1` or identity morphism, that default may be stated explicitly by the API; do not use `None` to conceal a noncanonical choice.

#### `STY-159`: Boolean mode flag changes mathematics or return type -> named operations / literal overloads

**Bad:** `normal_form(transformation=True)`, `roots(all=True)`, `galois_closure(map=True)` when the flag selects a different mathematical result or tuple shape.

**Preferred:** expose the mathematical objects/witnesses directly (`normal_form_isomorphism()`, chosen closure with its embedding, all-roots set, etc.), or—when compatibility with a source-level operation is intentionally retained at a non-mathematical boundary—use precise literal overloads there.  Do not make ordinary preamble callers memorize boolean modes.

#### `STY-160`: `pass` in a mathematical implementation -> implement, delete, or mark a genuine abstract contract

**Bad:** a visible concrete method/class body contains `pass` merely to postpone mathematics, silence a branch, or satisfy syntax.

**Preferred:** a genuine abstract category contract uses Sage `@abstract_method` with an ellipsis body; a concrete mathematical method is implemented; an impossible branch is asserted with its mathematical invariant; an unnecessary empty wrapper/class is deleted or replaced by the actual category refinement it represented.

`pass` remains ordinary Python in private engineering situations where “do nothing” is literally the intended protocol behavior, but it is a review flag in the mathematical subtree.

#### `STY-161`: Negated predicate where the complementary mathematical notion has a name -> expose the positive predicate

**Bad:** force users/callers to write `not L.is_nondegenerate()`, `not f.is_injective()`, or another negation when the complementary mathematical property has a standard name used in the field.

**Preferred:** expose the named positive concept (`is_degenerate()`, etc.) at its natural owner.  Do not implement a genuinely three-valued/partially decidable concept merely by Python negation: the positive predicates must preserve the intended mathematical/knowledge semantics of their codomains.

#### `STY-162`: One-use convenience wrapper hides a composable mathematical object -> expose the object

**Bad:**

```python
L1.same_genus(L2)
g.action_on_discriminant_group(x)
f.from_identity_matrix()
```

when the real mathematics is a genus value object, a group morphism, or an identity element of a Homset.

**Preferred:**

```python
L1.genus() == L2.genus()
rho = L.O().action_on(L.discriminant_module())
rho(x)
L.Hom(L).identity()
```

Expose the value/morphism/universal object because it can then be compared, composed, restricted, factored, have kernel/image taken, etc.  A wrapper that only packages one obvious use hides that structure and adds another name to memorize.

#### `STY-163`: Generic software-role suffix in the public mathematical API -> name the actual mathematical noun

**Red flags:** public names ending in or centered on `Model`, `Descriptor`, `Record`, `Info`, `Result`, `Context`, `Manager`, `Factory`, `Payload`, `Adapter`, `Backend`, `Provider`, or `Evidence` when those words merely describe the software role.

**Preferred:** identify the standard mathematical object/data: category, family, morphism, section, presentation, isomorphism, stratification, graph, action, form, quotient, etc.  If the object is genuinely an engineering record/adapter/backend, keep it private in the engineering subtree/boundary instead of promoting it into the mathematical language.

#### `STY-164`: Supplied generators returned as a canonical group -> construct a typed subgroup

**Bad:**

```python
O_L = L.orthogonal_group(generators=user_generators)
```

and then use `O_L` for canonical-group orbit/stabilizer/kernel/invariant statements.

**Preferred:**

```python
O_L = L.O()                         # canonical group object exists independently
H = O_L.subgroup(user_generators)  # exactly the group the supplied data proves
```

The supplied generators certify only `H = <generators> <= O(L)`.  Equality `H = O(L)` is a separate mathematical claim requiring an independent group-generation algorithm/theorem.  Downstream computations name the group they actually use.

#### `STY-165`: `Random*` / `Example*` / `Test*` mathematical type or category -> generate input data for the ordinary constructor

Randomness, example status, and fixture status describe a **process/use**, not a new mathematical kind.

**Bad:** `RandomLattice`, `ExampleModule`, `TestGroup`, `RandomLattices()`.

**Preferred:** a random/example generator produces legitimate defining data (Gram form, presentation, polynomial, relations, etc.) and feeds that data into the existing canonical constructor.  The returned object is an ordinary lattice/module/group and is refined by its mathematics.  Named standard examples belong in catalogues when useful; they do not automatically create new category vocabulary.

#### `STY-166`: Absence/rejection assertion can pass on a dead object -> assert positive capability/witness first

**Bad:**

```python
assert not hasattr(T, "projection")
assert invalid not in results
```

when an empty/broken `T` or empty `results` would pass equally well.

**Preferred:** state the positive mathematical structure that makes the negative claim meaningful, then test the actual positive universal/property statement.  For a tensor product, test the bilinear universal factorization and uniqueness rather than the absence of product projections.  For a filtered enumeration, first assert a sourced/nonzero expected population or independently established completeness before exclusions count as evidence.

A test of code removal that only asserts the removed name is absent is a closed loop around the edit, not a mathematical regression test.

#### `STY-167`: Sage `Element.__eq__` -> `_richcmp_` plus compatible `__hash__`

This rule is specifically for subclasses/runtime types of `sage.structure.element.Element`, not ordinary Python records or Sage `Parent` classes.

**Bad:**

```python
class MyElement(Element):
    def __eq__(self, other):
        return self.data == other.data
```

Sage's inherited zero/truthiness/coercion machinery compares elements through `_richcmp_`, so a bespoke Python `__eq__` can disagree with `is_zero()` and `bool(x)`.

**Preferred:** implement the one Sage comparison primitive:

```python
def _richcmp_(self, other, op):
    return richcmp(self.data, other.data, op)

def __hash__(self):
    return hash(self.data)
```

using the same immutable mathematical data for equality and hashing.  Let Sage's inherited `is_zero()`/`__bool__`/comparison machinery delegate to that primitive.  Put the implementation at the highest owned element type where the equality semantics are shared, not on every leaf.

#### `STY-168`: Hand-built linear-combination `repr` -> the host's symbolic representation helper

**Bad:** manually join coefficients/signs/generator labels in `_repr_`, usually assuming integer signs, absolute value, unit coefficients, or string labels.

**Preferred:** represent the element as the actual finite formal combination of its owned symbols and coefficients, and use Sage's `repr_lincomb` (or the corresponding owned formal-sum renderer) when its semantics match.  Let the coefficient ring and symbol objects supply their own representations.  Do not rebuild sign/`±1`/zero formatting by hand in every module/lattice/algebra element class.

This is not cosmetic: a symbolic `2*e - f` display reinforces that the element is a formal mathematical element, while a raw tuple or hand-formatted coordinate vector trains the numerical ontology the API is trying to prevent.

#### `STY-169`: Algorithm exhausts an entire mathematical object -> use structural data/theorem or make enumeration the explicit operation

**Red flag:**

```python
for x in G:
    ...
for x in M:
    ...
all(property(x) for x in X)
```

where correctness/termination requires eventually visiting **every** element of a group, module, lattice, ring, or other potentially infinite object.

**Preferred:** ask what finite/structural datum actually proves the claim: a chosen generating family when a finite-generation theorem makes that sufficient, a presentation/relation check, a morphism identity, category membership, a backend theorem, finite support of the particular element, or another semantic invariant.  If the operation genuinely is “enumerate all elements,” return/use the owned enumerated set lazily and let the caller explicitly request/consume enumeration.

A lazy `__iter__` implementation is not the smell; an unrelated algorithm whose success assumes the iterator terminates is.  An upstream `assert X.is_finite()` added solely because a loop needs exhaustion is the loop confessing that it lowered the mathematical domain.

#### `STY-170`: “Tensor product of matrices” -> Kronecker product / tensor product of the represented morphisms

Matrices as arrays have a **Kronecker product**.  Tensor product is the mathematical construction on modules/vector spaces/algebras and on linear maps between them.

**Bad:** describe `A.tensor_product(B)` or a block array `(a_ij B)` as “the tensor product of matrices,” then reason about it as though matrices themselves carried that universal construction.

**Preferred:** if `A` and `B` are matrices representing `f:V1->W1` and `g:V2->W2`, construct/consider the tensor morphism

\[
f\otimes g:V_1\otimes V_2\to W_1\otimes W_2.
\]

In chosen finite bases, its representing matrix is the Kronecker product of `A` and `B`.  Backend calls may use the engine's historical `.tensor_product` spelling privately, but public prose/API names the correct mathematical operation.

#### `STY-171`: Euclidean vector operation on a formed object -> use the object's actual form

**Red flags:** `dot_product`, standard-coordinate `norm`, Euclidean projection, Gram-Schmidt, shortest-vector language, or orthogonality code applied to an object carrying an arbitrary bilinear/quadratic form without explicitly routing through that form.

**Preferred:** ask the formed object for `b(x,y)`, `q(x)`, its correlation morphism, orthogonal complement, radical, or the appropriately named form operation.  A Euclidean/positive-definite algorithm lives only at the mathematical subcategory where that extra structure makes it valid, and its private backend may then use standard inner-product routines after the correct form has been transported/normalized.

#### `STY-172`: Definite/nondegenerate assumption appears because the backend wants it -> keep the general form semantics and localize the algorithmic case

**Bad:** make the base formed-object API positive definite or nondegenerate because the first available matrix routine needs an invertible/PD Gram matrix.

**Preferred:** arbitrary (including degenerate/indefinite) forms are first-class at the general owner.  Methods whose **mathematical definition** requires definiteness/nondegeneracy live on that narrower category; methods defined generally keep their general name/domain and route/assertion-gate the currently computable cases.  Backend assumptions never redefine the base mathematical object.

#### `STY-173`: Defect found in an owned dependency -> local facade/protocol workaround -> fix the owner

**Bad:** discover that the preamble lacks an annotation/semantic method, then add a local `Protocol`, stub, wrapper, copied helper, or workaround in the downstream consumer and merely file/report the upstream defect.

**Preferred:** if the defective dependency is part of the user's owned project stack and the fix is within the active task's mathematical dependency, correct it at its authoritative source, then consume the repaired interface.  A TODO/report is useful only when the source genuinely cannot be changed in the current ownership boundary.

#### `STY-174`: Stored backend object as long-lived implementation twin -> reconstruct ephemeral computation state when practical

**Bad:** an owned mathematical object stores a Sage/GAP/etc. twin and ordinary downstream methods repeatedly dig into it, allowing the backend ontology to become durable hidden state.

**Preferred:** for large standard algorithms whose inputs/outputs are mathematical data, construct the private backend representation from the owned data at the computation boundary, perform the complete operation, convert back, and discard it.  Durable backend state is justified only when the representation itself is a required long-lived computational resource and then remains behind one private owner/boundary (`BND-01`).

#### `STY-175`: Read every Sage `super_categories()` edge as inclusion -> classify the structural map first

Sage uses one graph edge mechanism for mathematically different relationships: full-subcategory inclusion, forgetting one operation/projection from a structured object, parameterized-family relationships, and implementation/MRO organization.

**Bad:** see `A in B.super_categories()` and conclude “every `B` is an `A`” or copy the edge directly into the owned category graph.

**Preferred:** determine the actual mathematical map represented by that Sage declaration—subcategory inclusion, forgetful/projection functor, reindexing/base-family map, or merely host implementation organization—then encode that owned construction/functor.  The Sage edge is empirical evidence about Sage, not the mathematical theorem.

#### `STY-176`: Sage category equality/parent lists used as category equivalence -> compare owned mathematical constructions

**Bad:** conclude two categories are mathematically different because Sage `C != D`, or identical because `C.super_categories() == D.super_categories()`.

**Preferred:** identify the owned normalized mathematical construction each Sage category models and compare those.  Two different Sage presentations of one pullback/category may compare unequal; two genuinely different refinements can have identical declared parents.  Missing Sage edges are implementation gaps, not mathematical non-inclusions.

#### `STY-177`: Bundled object type/presentation called “the category” -> keep the levels separate

Before naming an implementation artifact, separately identify:

1. the mathematical category;
2. an object of it;
3. the runtime/bundled Python/Sage type representing such objects;
4. any category structure placed on that runtime type;
5. any chosen presentation (basis, enumeration, coordinates, generators);
6. any property-cut full subcategory.

**Bad:** call a `Fintype`-like presentation “the category of finite sets,” or identify based modules with finite free modules because choice can produce a basis.

**Preferred:** name each level explicitly.  Equivalence between presentations does not erase which choice/structure the API actually carries.

#### `STY-178`: Exact upstream name not found -> compose standard mathematics before declaring a gap

**Bad:** search Sage/Mathlib for one class/function with the exact local spelling, find none, and conclude the concept must be newly implemented or contributed upstream.

**Preferred:** attempt to express it as a standard composition: a full subcategory cut out by a property, structured objects, a Hom/category construction, slice/coslice, inclusion/forgetful functor, base change, or transport through an equivalence.  A missing packaged noun is not a missing mathematical primitive.

#### `STY-179`: Upstream correspondence found -> preserve redundant local declaration -> delete/resite it if the correspondence exposes wrong ownership

**Bad:** discover that a ring-specific `size()` is exactly underlying-set cardinality and “fix” the design by delegating `Ring.size()` to that set cardinality, preserving the duplicate public word.

**Preferred:** use the correspondence diagnostically.  If the standard owner is `Sets`, remove the ring-local synonym and let the ring recover `cardinality()` through the forgetful/structural functor.  Alignment can prove a declaration redundant or misplaced; it does not automatically justify keeping it.

#### `STY-180`: Avoid a mature dependency because it is “heavy” -> compare human ownership and blast radius instead

**Bad reasoning:** reject `networkx`, a parser/grammar package, a multidispatch library, or another mature dependency because it adds packages, a build toolchain, or installation scaffolding, then implement the generic machinery locally.

**Preferred reasoning:** treat ordinary dependency/build/package substrate as baseline engineering.  Compare designs by the mathematics/generic logic the repository must now own and review, the blast radius of adding/changing a case, and whether other consumers can reuse the external abstraction instead of relearning it.  Use the mature dependency when it removes substantial owned machinery and is semantically appropriate.

#### `STY-181`: Hand-roll against Sage because the relevant host idiom was not checked -> inspect the host first

**Bad:** manually implement generator naming, identity construction, conformance checking, matrix reshaping, coercion, graph traversal, or another operation before checking Sage/stdlib/upstream for the native idiom.

**Preferred:** inspect the live host API/source and, when behavior matters, run a distinguishing probe.  Use the host operation where its semantics match; wrap it only at the owned mathematical boundary if vocabulary/ontology differs.  Lack of familiarity with Sage is not a reason to create a second local language.

#### `STY-182`: Nontrivial local algorithm appears before backend search -> map the semantic operation to mature software first

**Red flag:** a new multi-step algorithm for groups, ideals, lattices/forms, polyhedra, number theory, symbolic algebra, or graph structure appears in Python without any indication that the installed/open-source capability stack was checked.

**Preferred:** name the semantic operation, search the repository capability map and relevant mature exact systems, then either delegate through the owned boundary or document the true gap that forces local ownership.  “It was straightforward to code here” is not evidence that the repository should own it.

#### `STY-183`: Named composite/classifier spelling -> duplicate category vertex -> preserve one identity

**Bad:** represent `Semigroups` and `Magmas.Associative` as two independent categories connected by an equivalence/alias edge; similarly create a second category solely for every readable composite name.

**Preferred:** the standard name and the classifier expression are two presentations of **one category identity**.  The public name may be `Semigroups`; the defining expression may be `Magmas.Associative`; no second vertex/object is created.

#### `STY-184`: Same axiom word reused globally -> interpret classifier relative to its host category

Names such as `Commutative`, `Distributive`, `Graded`, `Finite`, etc. have meaning only together with the mathematical category/construction they classify.

**Bad:** create one global `Commutative` node because Sage happens to reuse that axiom spelling across unrelated theories.

**Preferred:** `Groups.Commutative`, `Rings.Commutative`, a lattice-poset classifier, etc. are classifier applications whose actual mathematics is determined by the host/defining morphism.  Transport a classifier to another category via the corresponding pullback when that is the mathematics; do not identify classifiers by string.

#### `STY-185`: Readable name for a pullback/refinement -> independent species -> retain the defining category expression

**Bad:** mint `FiniteRings`, `GradedAlgebras`, `BasedModules`, etc. as unrelated categories merely because a readable plural name is convenient.

**Preferred:** first represent the actual expression, e.g. `Rings.Finite` or `Algebras(R).Graded`, with the appropriate classifier/pullback structure.  A standard established plural may be registered as the public name/alias of that same identity; the name does not replace or duplicate the construction.

#### `STY-186`: Generated “certificate/evidence/status” artifact for facts derivable from live code -> live semantic structure plus on-demand report

**Bad:** add a per-object certificate/attestation JSON, proof-metadata ABC, generated status ledger, or stored compliance manifest whose fields are all recomputable from category placement, MRO, constructors, functors, and runtime behavior.

**Preferred:** put the actual invariant into the type/category/constructor language; verify live behavior with mathematical specimens or the host's native conformance mechanism; generate any human-readable inventory on demand.  Store only genuinely authored mathematical design commitments that cannot be derived from the live system.  Do not create a second ledger that must be synchronized forever.

#### `STY-187`: Category constructibility decided by graph reachability/name lookup -> derive canonical structural maps

**Bad:** say a category/refinement is “constructible” because a named node exists or because BFS finds some path through an implementation graph; traverse projection arrows backwards to manufacture structure.

**Preferred:** use the owned category expression/finite-limit grammar: canonical structural maps compose in their declared direction; classifiers/refinements are introduced only when the required map to their host exists; pullback/classifier constructions create their own projections.  Constructibility is derivability in this typed structural calculus, not arbitrary graph connectivity.

#### `STY-188`: Default display repeats the type/role -> expose mathematical data of this object

The default display of every preamble-owned object must reduce mathematical uncertainty about the **particular object being displayed**.  A class name, noun phrase, constructor family, or paraphrase of the object's type is not a display.  The researcher already knows that a value returned by `module_generators()` is a generator family and that an object constructed by `Lattices(R)(...)` is a lattice.  Printing only `"Lattice-generator family"`, `"Lattice"`, `"placed map"`, or an equivalent type-renaming is therefore a failed display.

**Preferred:** show independently useful mathematical information that distinguishes this object from another object of the same type.  Use whichever data are already cheap and canonical for the object, for example:

- defining data or a mathematical expression/presentation;
- source and target of a map/functor, index set of a family, or selected generators/relations;
- cheap characterizing invariants such as rank, signature, degree, cardinality, or category placement;
- the actual members/values of a finite family or finite set;
- for an infinite/lazy object, a defining formula, indexing datum, or bounded cheap window when one is canonically and safely available.

An optional human-readable name may prefix this information, but it may never be the entire payload.  Category membership alone is acceptable only when it adds genuine information not already tautological from construction and no more informative cheap defining datum exists.  A canonical symbolic spelling is also meaningful data: `NN = {0, 1, 2, ...}` communicates a mathematical object; `Natural numbers` merely renames its type.

Displays must remain semantic rather than computationally invasive.  Do not enumerate an unknown/infinite set, trigger an expensive classification merely to print an object, expose backend coordinates/storage, or make display depend on nondeterministic engine state.  Prefer a concise view into already-owned defining data.  `repr`, LaTeX/`show`, rich display, and container/family displays are all governed by this rule.

Review display methods adversarially: ask what a mathematician learns from the output after deleting the Python class/type name from their memory.  If the answer is “nothing”, the display is not acceptable.

#### `STY-189`: Display leaks an internal refinement/type owner -> render through the public mathematical operation

The object that implements a result may live in a highly refined category without that refinement being part of the result the user asked to see.  Displays follow the **semantic operation and its mathematical codomain**, not the most specific internal parent/classifier that happened to compute it.

**Bad:** `L.module_generators()` for a lattice prints `"Lattice-generator family"` merely because the module is currently refined as a lattice.  The operation is module-theoretic: every represented free module `Free_R(S)` has its canonical generating set/image.  The lattice refinement adds no new datum to that result, so mentioning it leaks implementation/type-theoretic routing into the public view.

**Preferred:** display the generic mathematical result, e.g. the generator image `{e_0, e_1}` (or the indexing set/presentation when that is the operation requested).  If a genuinely stronger construction exists — for example a selected root basis with root-specific operations or invariants — then a root-specific method may return and display that refined object because the refinement is mathematically part of that result.

Use the same rule for forgetful images, underlying objects, Hom-elements, functor images, subobjects, and classifier refinements: internal refinement is allowed to improve implementation and available methods, but it does not automatically earn a word in the default display.  A public display should be invariant under replacing the implementation by an equivalent stronger internal refinement whenever the mathematical result requested by the user is unchanged.

#### `STY-190`: Derived accessor reconstructs a canonical underlying object -> construct once and reuse it

When a mathematical object is defined by applying an existing construction and then adding structure, that underlying construction is part of the object's construction data, not something to be synthesized later when an accessor is called.

**Bad:** construct a lattice from ad hoc coordinate/index fields, then have `module_generating_set()`, `module_generators()`, or `unformed_module()` manufacture module-like views post hoc.  This duplicates `Free_R(S)`, permits the synthetic view to drift from the object that should define it, and hides whether the stronger object really lies over the claimed weaker one.

**Preferred:** construct `M = Free_R(S)` first, then construct the lattice/form/module refinement from the actual object `M` and the additional form datum.  Store `M` (or the canonical forgetful image/morphism supplied by the categorical construction) as part of the structured object's defining data.  Every generic module operation delegates to or transports along that same object/map.  `module_generating_set()` returns `M.module_generating_set()`; forgetting structure returns `M`; the structure/forgetful morphisms identify the two represented carriers.  Do not keep a second indexing set, generator family, presentation, or coordinate parent merely to make inherited methods appear to work.

The same rule applies to free objects, quotients, localizations, scalar restriction/extension, formed objects, group actions, graded objects, subobjects, and functor images: if `X` is mathematically constructed as `G(Y, datum)`, then `Y` and the canonical structural map(s) are first-class construction data.  An accessor exposes those data; it does not recreate an isomorphic substitute from metadata.

A stronger object may of course use a distinct parent so that two choices of added structure remain distinct.  That does not make its underlying object fictitious: the distinct structured parent must still retain and reuse the actual weaker object and the canonical comparison maps.

#### `STY-191`: Comment or docstring teaches standard mathematics -> state the convention, cite the source, delete the lesson

The reader of this repository's source is a mathematician.  A comment or docstring states what the reader cannot supply from the code and their own training: the convention chosen where several exist (reduced or unreduced homology, left or right action, which duality functor), an engine's input demand or output shape (with its `TRAPS.md` row), the hypothesis under which a criterion applies, and the citation.  It never derives, motivates, or teaches the mathematics the code uses.

**Bad:** a docstring explaining that a graph is a 1-dimensional complex, that \(H_1\) is therefore the whole cycle space, and that \(\pi_1\) is free of rank \(E - V + C\), above a function that calls `minimum_cycle_basis`.

**Preferred:** "Sage returns reduced homology, so \(H_0\) has rank one less than the number of components." followed by the call.

The test: delete the paragraph and ask whether a mathematician reading the code loses anything they could not supply.  If not, it was a lesson.  A derivation that genuinely belongs somewhere belongs in the docs book or a cited source, and the code cites it.

### Review rule for new imperative code

Before accepting a new global helper, explicit `for`/`while`, mutable accumulator, cache, registry, runtime probe, or bespoke data structure, check the catalogue above and answer:

1. Which mathematical object owns this operation?
2. Can the user discover it from that object with tab completion?
3. Is this exactly map/filter/fold/search/group/flatten/count/queue/traversal syntax already named by Python or a dependency?
4. Is there already a repository abstraction for the same mathematical operation?
5. Does the same skeleton occur elsewhere, implying a missing abstraction rather than several loops to shorten?
6. Can the computation remain lazy or finite-support instead of materializing a whole family?
7. Is the loop genuinely stateful mathematics/algorithmics?  If yes, keep it explicit and use the standard worklist/data structure.
8. Does adding this specialized feature force an ancestor to import or name the descendant?  If yes, recheck dependency direction.
9. Does a backend already own the generic algorithm?  If yes, delegate and cross back.

A construct that survives these questions is allowed.  The catalogue exists to make the routine cases routine and to keep review attention on the mathematics.

* * *


## Policy Index

| Family | Governs |
| --- | --- |
| `OWN-*` | [normative architecture](#preamble-architecture-specification): sanctioned construction paths, recursive ownership, encapsulation, and reuse |
| `ARC-*` | mathematical architecture and ownership |
| `API-*` | the public mathematical surface of owned objects |
| `CON-*` | constructors, witnesses, actions, and structural transport |
| `CAT-*` | category placement, chosen data, and computational capability |
| `DEF-*` | definitions, predicates, structural results, and special cases |
| `LEX-*` | mathematical vocabulary and public type names |
| `SET-*` | mathematical collections, underlying sets, and cardinality |
| `ENG-*` | delegation of heavy computation to exact engines |
| `BND-*` | private engine crossings and representation boundaries |
| `BRG-*` | external-system interoperability and bridge transport |
| `ENV-*` | repository execution and environment conventions |
| `DEV-*` | development, verification, migrations, and policy promotion |
| `STY-*` | corrective implementation style and declarative Python patterns |
| `FRM-*` | formal definitions, proof-assistant statements, and external citation |
| `FDC-*` | formalization decomposition, scoping, and foundations audit |
| `FRD-*` | fraud precursors in formalization work, and their observable signs |
| `FSC-*` | formalization scale, calibration, and the scaffold that holds project state |
| `FSV-*` | semantic verification of formal statements; the review surface and its audit |
| `FSA-*` | formalization search and acquisition; found versus owned mathematics, and the provenance of a definition |

### 1. Mathematical Architecture & Ownership (`ARC-*`)

#### `ARC-00`: The Preamble Is a Closed Mathematical Universe

- **Rule**: Once code enters the public preamble API, it remains in the preamble universe.
  The preamble does not extend Sage, wrap Sage's public object model, or provide an interoperability layer with ordinary Sage objects.
  It is an independent mathematical system built on top of computational services such as Sage, Singular, GAP, Julia, OSCAR, or Macaulay2.
  Every publicly constructible parent, element, morphism, category, subobject, tensor, ideal, group, ring, module, algebra, scheme, and derived construction is a preamble object and composes only through preamble APIs.

- **Rationale**: The backend boundary is an implementation boundary, not part of the mathematical language available to users or ordinary repository code.
  If a mathematical operation must leave the preamble universe in order to continue, then the missing result, operation, or construction belongs in the preamble and must be owned there.
  Backend choice must be replaceable without changing any caller-visible object, element, signature, or method.

- **Violation Example**: Treating preamble `ZZ` as a view of Sage `ZZ`; `from sage.all import *` inside the public preamble session; leaving Sage's preparser binding `Integer` or `RealNumber` to raw Sage element constructors; returning a Sage integer, vector, ideal, group element, matrix, or homset from a public operation; requiring callers to construct a Sage object and pass it into a preamble constructor; documenting a method as "use Sage's object here"; exposing an engine so downstream code can continue the computation outside the preamble.

- **Correct Example**: `ZZ(3)` is an element of preamble `ZZ`; the session's integer-literal constructor resolves to that same owned integer construction; `ZZ**2` has preamble module elements; `Groups.C(4)` has preamble group elements.  A Smith-form implementation may privately translate these objects to Sage `ZZ`, Sage free modules, and FGP data, but the caller sees only preamble inputs and preamble outputs.

#### `ARC-01`: Own Universal Properties and Categories Natively

- **Rule**: Define mathematical categories, morphisms, functors, adjunctions, and universal constructions natively in the repository category framework.

- **Rationale**: Categories and universal properties establish the semantic mathematical foundation.
  They provide consistent compositional behavior across modules.

- **Violation Example**: Defining an ideal or basis as an isolated tuple or matrix operation without an underlying category, module, or algebra structure.

#### `ARC-02`: Morphism-Centric Subobjects and Witness Placement

- **Rule**: Represent subobjects as pairs $(S, \iota: S \hookrightarrow M)$.
  Place predicates, isometries, embeddings, and containment checks on morphism spaces or hom-sets.

- **Rationale**: Mathematical invariants depend on the embedding morphism, not on presentation-dependent coordinate choices.

- **Violation Example**: Storing ambient coordinates or adding `ambient=` parameters directly to parent objects.

#### `ARC-03`: Build Structural Objects Before Downstream Numerical Invariants

- **Rule**: Never bypass an intermediate mathematical object or functorial stage (such as the localized module $M_{\mathfrak{p}} = M \otimes_R R_{\mathfrak{p}}$, base-changed algebras $K \otimes_R \mathcal{O}$, or derived complexes) to compute a single numerical scalar or pointwise fiber (such as $\dim_{\kappa(\mathfrak{p})}(M \otimes_R \kappa(\mathfrak{p}))$). Always construct the foundational parent object and base-change/localization functor first; derive pointwise invariants as generic operations on the resulting object.

- **Rationale**: Bypassing structural objects destroys mathematical compression and composability.
  When the structural object exists ($M_{\mathfrak{p}}$ as an $R_{\mathfrak{p}}$-module), all local invariants (rank, minimal generators, local torsion, localization of morphisms) become generic consequences of base change.
  Skipping to point queries forces every downstream invariant to reinvent ad-hoc algorithmic logic.

- **Violation Example**: Implementing `local_number_of_generators(p)` by evaluating the residue field vector-space dimension $M \otimes_R \kappa(\mathfrak{p})$ while the localized module $M_{\mathfrak{p}}$ over the local ring $R_{\mathfrak{p}}$ remains absent from the category layer.

#### `ARC-04`: Owned Objects Over Interchangeable Computational Services

- **Rule**: Mathematical objects, elements, morphisms, categories, subobjects, universal properties, and functors are owned.
  Sage/Singular/GAP/Julia/OSCAR/M2/etc. are interchangeable computational services behind those objects.
  The preamble neither subclasses their mathematical universe nor exposes it as an alternate API.
  No CAS-specific object, element, category membership, constructor, or coercion is needed to state, construct, or use preamble mathematics.

- **Rationale**: The owned category graph is the single surface for stating what an object is.
  A computational engine only supplies computations behind that surface, so the engine choice never enters the statement of the mathematics, and engines remain swappable.

- **Violation Example**: Requiring a CAS-specific category membership or class (Sage, Singular, GAP, OSCAR, or Macaulay2-specific) to state, construct, or identify an object.

#### `ARC-05`: Owned Parents and Elements Are Outside Every Engine

- **Rule**: An owned mathematical object is a parent constructed through the owned category chain, and its elements are elements of that owned parent.
  Backend parents and backend elements are private computational representations only.
  No Sage/Julia/GAP/OSCAR object is the public parent or public element merely because an internal algorithm delegates to that system.
  No backend constructor receives an owned parent or owned element directly; private adapter code first converts every input to backend representations.

- **Rationale**: Ownership is a firewall around the whole mathematical universe, not only around parent objects.
  If an owned parent returns Sage elements, then Sage's element parent, coercion graph, methods, and representation remain part of the effective public ontology even when the parent itself is nominally owned.
  That is the same ownership inversion at the element level.

- **Violation Example**: `ZZ(3).parent() is SageZZ`; an owned free module whose `module_generator(i)` is a Sage free-module element; an owned group whose `group_generators()` are GAP/Sage group elements; passing an owned ring element directly to `FGP_Module`, `FreeModule`, or a GAP constructor.

- **Correct Example**: Owned `ZZ` has owned integer elements.  An owned free module has owned module elements whose coefficients lie in owned `ZZ`.  A private FGP adapter converts the owned ring, presentation matrix, and elements to Sage `ZZ`, a Sage free module, and Sage FGP elements, performs the computation, and converts the answer back to owned elements and morphisms before returning.


#### `ARC-06`: Backend Adoption Creates a New Owned Object; It Is Never Reclassification or a Facade

- **Rule**: Importing or selecting a backend representation constructs or attaches private computational state for an independently owned object.
  It does not reclass the backend parent, expose the backend parent as a facade, or reuse backend elements as the owned object's elements.
  Backend identity is never owned-object identity.

- **Rationale**: Reclassification and facade parenting both leave the backend's ontology in the public object model: reclassification mutates the backend object, while a facade leaves backend elements and coercions authoritative.
  The owned category must instead control parents, elements, operations, equality, morphisms, and public return types; the backend is only an implementation service behind private crossings.

- **Violation Example**: A post-init hook that refines a Sage group in place; `Parent(..., facade=sage_free_module)` for an owned module; `OwnedRingView._element_constructor_` returning `SageZZ(value)`; rebuilding or preserving a Sage Cython element class as the element class of an owned group.

- **Correct Example**: `own_group(G_backend)` returns an owned group with owned group elements and a private conversion between those elements and `G_backend` elements.  `own_free_module(F_backend)` returns an owned free module with owned coefficient-bearing elements and privately records `F_backend` only as an optional computation service.  Neither backend parent nor its elements are changed or exposed.


#### `ARC-07`: A Morphism Is Asked of Its Endpoints

- **Rule**: The morphisms from `A` to `B` are asked of the endpoints, `A.Mor(B)`, so the owned hook of their category chooses the object.
  A category is named at the call site only when the morphism deliberately lives in a coarser owned category, for a map of underlying sets.
  **`Mor` is the only spelling the preamble universe ever uses.**  `Hom` names Sage's construction, which is a backend engine if it is used at all: it may appear inside a private adapter and nowhere else.

- **Rationale**: `Mor(A, B)` is a category, not a set.  Its objects are the morphisms $A \to B$, and every set is a category -- the discrete one -- so the set case is an instance rather than a competing kind of answer, and enrichment is structure carried by the same object rather than a different return.  Naming a category at the call site restates what the endpoints already know, and when the name is Sage's it asks Sage to admit owned objects it does not hold.

  Reserving `Hom` for Sage is what makes the boundary hold by construction rather than by vigilance.  Sage's coercion machinery calls `X.Hom(Y, category)` internally, naming its own `SetsWithPartialMaps`; while `Hom` was the owned spelling, those internal calls landed in owned code and failed there.  With `Mor` owned and `Hom` left to Sage, an engine call reaches the engine and an owned call reaches the owned category, and neither can be mistaken for the other.

- **Violation Example**: defining or calling `A.Hom(B)` anywhere in the preamble; `Hom(source, target, Groups())` with owned groups as endpoints; `Hom(base_ring, self, Rings())` inside an owned algebra; a category carrying `Hom` as an alias for its own morphism construction.

- **Correct Example**: `A.Mor(B)` for the morphisms between two owned objects; `Hom` appearing only where a private adapter hands objects to Sage.

#### `ARC-08`: Engine Availability Does Not Define Mathematical Existence

- **Rule**: The mathematical data of an owned object is sufficient to state and construct that object independently of any computation engine.
  A backend may be present, absent, or replaceable without changing the object's defining mathematical data or identity.
  A backend may establish an additional mathematical property that justifies a valid category refinement, but the backend's class or availability is never itself category data.
  Missing backend support limits a computation; it does not turn the mathematical object into a backend object or make the object cease to exist.

- **Rationale**: A chosen presentation `F_1 -> F_0 -> M`, for example, already defines the presented module.
  A Sage FGP module can accelerate Smith-form computations when the coefficient ring admits that engine, but it is not the definition of `M`.
  Keeping those facts separate makes backend choice genuinely optional and interchangeable.

- **Violation Example**: Refusing to construct a presented module because Sage cannot build an FGP module over its coefficient ring; selecting the public class or category by checking which Sage implementation class happened to be available.

- **Correct Example**: Retain the owned presentation morphism and tensor-valued relation matrix independently of any Smith engine.  Expose an algorithmic method only where its implementation is supplied by category structure, or keep a mathematically general method with an informative assertion stating the stronger mathematical hypothesis under which the current algorithm is total.  Missing engine support is handled at the private engineering boundary, never represented as a mathematical `NotImplementedError` result.

#### `ARC-09`: Fundamental Mathematical Objects Are First-Class Before Their Refinements

- **Rule**: When a standard mathematical object is not already canonically an instance of an owned universal construction, give that object an owned parent and category before implementing any of its specializations.
  When it *is* canonically an existing construction, use that construction rather than minting a parallel parent.
  Additional algebraic, geometric, topological, smooth, scheme-theoretic, group, or representation-theoretic structures are refinements or functorial constructions on the same mathematical object; they do not replace its underlying identity.
  Do not force the object to live as a backend object or one particular richer structure, but equally do not duplicate an object already supplied by `Hom`, `End`, tensor product, quotient, subobject, free object, or another universal construction.

- **Rationale**: A fundamental mathematical object can be the common domain on which many theories meet.
  If it is absent, every higher construction invents its own representation and API, so backend matrix methods appear in tensors, matrix multiplication appears in generic rings, and geometric structure has nowhere canonical to attach.
  Owning that object first lets later category refinements contribute exactly the operations justified by their hypotheses.

- **Violation Example**: Implementing every finite matrix as `tensor.matrix(...)`; returning Sage `MatrixSpace(R,m,n)` for rectangular matrices; creating a second matrix parent even though `Hom_R(F_R([n]),F_R([m]))` already is the canonical matrix object; encoding a matrix scheme or matrix group as a separate unrelated object.

- **Correct Example**: For the canonical finite ordered set `[n]`, `F_R([n])` is the free module with its canonical framing.  Define `M_{m,n}(R)` as the existing Hom object `Hom_R(F_R([n]),F_R([m]))`; its elements acquire matrix entry/row/column/normal-form methods from the Hom category when both endpoints have these canonical framings.  `M_n(R)=End_R(F_R([n]))` inherits composition as multiplication and may acquire further algebra/Lie/geometric refinements without changing object identity.

#### `ARC-10`: Canonical Identifications Are Object Identity, Not Conversion APIs

- **Rule**: When standard notation names an object that is canonically an existing owned construction, implement the notation as that construction itself rather than as a new parent plus conversion maps.
  Preserve the canonical chosen data that makes the identification literal.

- **Rationale**: Parallel parents for canonically identical objects create artificial coercions, duplicate APIs, and force downstream code to choose representations that mathematics does not distinguish.

- **Violation Example**: Creating a distinct `MatrixSpace(R,m,n)` parent plus `as_module_morphism()` even though the canonical framings identify it with `Hom_R(F_R([n]),F_R([m]))`; creating a separate endomorphism-matrix ring instead of using `End_R(F_R([n]))`.

- **Correct Example**: `[n]` is the canonical finite ordered set, `F_R([n])` is the corresponding canonically framed free module, and `MatrixSpace(R,m,n)` returns `F_R([n]).Hom(F_R([m]))` with the matrix-Hom refinement installed.  A matrix element *is* that module morphism; `matrix()` is its coordinate array/object only when such a coordinate view is requested, not another mathematical object.

#### `ARC-11`: Export Aggregators Are Not Architectural Dependencies

- **Rule**: Internal code imports a mathematical construction from the module that defines it, or from a deliberately dependency-light core module for that theory.
  Package `__init__.py` files, session aggregators such as `preamble.all`, catalogues, and convenience export surfaces are leaves of the dependency graph; foundational category/module/ring/algebra code never imports through them.

- **Rationale**: An aggregator describes what a user may import together; it does not state a mathematical dependency.  Using it internally makes every exported higher construction an implicit dependency of every lower one, creates circular imports, and lets import order determine which mathematical structures exist.

- **Violation Example**: `modules/connections.py` importing `KahlerDifferentials` from `categories.algebras.__init__`, while that aggregator imports finitely presented algebras which import the modules package; a core functor importing through `preamble.all`; loading the lattice catalogue before the categories on which its objects depend.

- **Correct Example**: A connection module imports `KahlerDifferentials` from `algebras.kahler_differentials`; the session aggregator imports both only after their defining modules are available.  The dependency graph follows mathematical construction dependencies and is independent of session import order.

#### `ARC-12`: Mathematical Operations Live on Their Mathematical Owners

- **Rule**: Public mathematical operations are methods on the element, parent/object, category, morphism, Homset, functor, or other mathematical object whose structure determines the operation and its admissible inputs.  If a category `C` has products, `C` owns its product construction, e.g. `C.product(factors)`; if a morphism has a kernel in its category, expose that through the morphism/Hom/category API; if an element has an operation, expose it on the element.

  **The free-standing global name is itself the defect.**  It is a violation whether or not the body is correct, whether or not the dispatch is generic, and whether or not it forwards immediately to the right owner.  A global that forwards perfectly still publishes a second name for the operation, and the second name is the thing being banned.  Judging such a global by the quality of its implementation is the standard misreading of this rule.

  The ban covers every public global whose arguments include a mathematical object, with no exemption by kind: constructions (`Product`, `Coproduct`, `TensorProduct`, `Subobjects`, `Kernel`, `Cokernel`, `Pushout`), ring and module constructors (`Localization`, `PrimeLocalization`, `QuotientRing`, `FractionField`), category factories, adopters and refiners, and predicates alike.  Reading "operations" as though it excluded constructors is the second standard misreading.  A constructor is an operation on the object it is handed.

- **Call-site test**: ask whether an object already in hand determines the operation.  `Localization(A, f)`, `Subobjects(X)`, `Product(X, Y)`, `Kernel(f)` each name their owner in argument position, so each must be written `A.localization(f)`, `X.Subobjects()`, `C.product([X, Y])`, `f.kernel()`.  Where no object is in hand, the name builds a specimen out of plain data -- `AffineSpace(2, QQ)`, `Lattices(ZZ)("E8")` -- and belongs to a catalogue namespace rather than to a global function.  There is no third case.  Reserving `Hom` for Sage so that the owned spelling is `C.Mor(A, B)` is this same rule already applied, and is why the boundary there holds by construction.

- **Notation, and its limit**: operator syntax may delegate to the owner: `X * Y`, `L + M`, `L ** n`, `~S`.  An operator publishes no name to look up, so it adds no second language.  A named global does.  "It delegates immediately to the owning object" describes how a violation is implemented; it is not a licence to write one.

- **Rationale**: Sage is a discovery-oriented mathematical language.  In an interactive session the user should be able to construct the mathematical object they know, type `<TAB>`, and discover the operations that make sense for that object.  The owning object supplies both namespace and domain information: `C.<TAB>` answers what the category can construct; `M.<TAB>` what the module supports; `f.<TAB>` what can be done with the morphism; `H.<TAB>` what the Homset knows; `x.<TAB>` what operations belong to the element.  A flat global namespace destroys that locality.  Seeing `Product`, `Kernel`, `Orbit`, or `TensorProduct` globally does not tell the user whether the function expects categories, parents, elements, morphisms, finite families, or some mixture, so using the language requires prior knowledge of the entire global API or constant documentation lookup.  This is the GAP/Julia-style failure mode the preamble is specifically intended to avoid.

  Mathematical ownership and implementation dataflow follow from the same rule.  Saying that `C` has products includes teaching the implementation of `C` how its selected products are constructed.  The information flows from `C` to `C.product(...)`, not from a global `Product(...)` dispatcher back into every possible category.  Consequently the code implementing the operation belongs in the subtree for the mathematical owner, and adding the operation to a new category does not require extending a global switchboard.

- **Violation Example**: Exporting a global `Product(X, Y)` leaves its domain unknowable from the name alone: does `Product(x, y)` multiply natural-number elements, form a categorical product of `Sets()` with itself, construct a product of two objects of a category, or accept a family of categories?  Likewise global `Kernel(f)`, `TensorProduct(X, Y)`, `Orbit(G, x)`, or `_morphisms_agree(f, g)` force the user or caller to know an external function catalogue and force the implementation to rediscover the relevant mathematical owner from its arguments.  A stand-alone `Product` that imports modules, sets, schemes, and algebras is one concrete consequence of this wrong API shape, but the free-standing operation is already the primary defect even if its dispatcher were perfectly generic.

  Two further shapes, both of which have passed review by being argued rather than seen.  Keeping `Localization(A, f)` on the grounds that its dispatch was cleaned up, or that it now forwards to `A.localization(f)`: the surviving global name is the violation, and a clean body only makes it harder to notice.  Building new code on an already-catalogued global -- writing `Subobjects(X)`, `Pushout(f, g)` or `TensorSquare(M)` in a fresh category because those names are importable -- which spreads the defect while adding a feature, and cites the presence of the global as its own justification.

- **Correct Example**: Write `C = Sets()` and inspect `C.<TAB>` to discover `C.product(...)`; if `X` and `Y` are objects with `C = X.ambient_category()`, notation such as `X * Y` may delegate to `C.product([X, Y])`.  `Modules(R)` supplies its own product/biproduct method in the module-category subtree; a scheme category supplies its product/fiber-product method in the scheme subtree.  A morphism exposes `f.kernel()` when its category supports kernels; a Homset exposes Hom-level constructions and equality; an element exposes its own operations.  The user discovers valid mathematics by navigating from objects already in hand rather than searching a global language.

#### `ARC-13`: Mathematical Structure Is Independent of Import Order and Call History

- **Rule**: The mathematical structure and category placement of an owned object are determined by its construction data and explicit mathematical refinements, not by which module happened to finish importing first or which accessor was called earlier in the session.
  Do not use import-cycle flags, `ImportError` fallbacks, lazy "try again on the next lookup" installation, or incidental method calls to make standard structure appear on an already existing object.
  A legitimate later refinement must correspond to newly established mathematical data or a proved property, not merely to runtime availability of implementation code.

- **Rationale**: Import order and call history are properties of the Python process, not of the mathematical object.
  If `R` is canonically an `R`-module and `R`-algebra, or an object carries a selected decomposition, those facts cannot depend on whether the module/algebra package had completed importing when `R` was first requested.
  History-dependent mutation makes identical mathematical expressions expose different APIs in different sessions and turns initialization order into hidden state.

- **Violation Example**: `_own_ring()` attempting to install the canonical self-module/self-algebra structure, catching `ImportError`, and deferring that mathematical structure until a later lookup; an accessor that calls `refine(...)` merely because asking the question made another category implementation importable.

- **Correct Example**: Canonical self-structure is part of the ring construction/category packet from the outset, or is supplied by a dependency-safe structure functor whose result is deterministic for the same ring.  A later refinement occurs only when a new chosen datum is attached or a mathematical predicate has actually been established.

#### `ARC-14`: Equivalent Universal Data Has One Authoritative Representation

- **Rule**: When standard mathematics gives equivalent presentations of the same universal structure, choose one authoritative datum and derive the others mechanically.
  Do not require subclasses or sibling implementations to independently encode mutually determining units, counits, Hom-set bijections, opposite/product-domain functor machinery, or parallel Hom-like parents for the same universal object.

- **Rationale**: Equivalent formulations are mathematical compression.  Implementing every equivalent formulation independently creates coherence obligations that the mathematics already solves and multiplies LOC without adding expressive power.
  The derived interfaces should be consequences of one structure, not separate sources of truth that can drift apart.

- **Violation Example**: Every adjunction subclass independently implementing `unit`, `counit`, `hom_set_isomorphism_forward`, and `hom_set_isomorphism_inverse`; a separate `ContravariantFunctor` reimplementing functor caching and endpoint checks instead of using a functor on `C^op`; a separate `Bifunctor` object model instead of a functor on `C x D`; represented pairings using a second `PairingSpace` even when `Hom_R(X tensor Y, W)` exists.

- **Correct Example**: An adjunction records one standard presentation—e.g. the adjoint functors with unit and counit—and derives the Hom bijection by composition, with triangle identities tested as the coherence law.  Contravariant and bifunctor convenience syntax delegates to ordinary `Functor` on the owned opposite/product category.  A represented bilinear pairing is literally an element of `Hom_R(TensorProduct(X,Y), W)`.

#### `ARC-15`: Upward Knowledge of Descendants Is an Architectural Smell

- **Rule**: Treat knowledge flowing from a general category, construction, or foundational module toward one of its specialized descendants as suspicious by default.  This is a code-smell heuristic, not an absolute prohibition: there are legitimate exceptional cases, but a supercategory or generic construction should normally not import, name, enumerate, or branch on its subcategories.  Adding a new specialized category should ordinarily consist of adding a modular subtree whose imports point inward toward existing foundations; it should not require edits to unrelated ancestors merely so they learn that the new category exists.

- **Rationale**: Category inheritance and mathematical specialization are naturally extensible when dependencies point from specialized theories toward the general structures they refine.  If an ancestor must know every descendant, the blast radius of adding one new research category grows with the size of the entire hierarchy, generic code accumulates special cases, and independent subtrees cease to be independently loadable or maintainable.  The smell is especially strong when a generic construction such as products, Homs, kernels, scalar extension, or equality must be edited to mention a highly specialized descendant.

- **Smell Example**: `Cat.Products` or another generic categorical layer importing `MyVerySpecialResearchLatticeCategory` so that products work there; `Modules(R)` importing a particular arithmetic-lattice subcategory merely to recognize it; a root construction maintaining a registry or conditional chain of every specialized theory that supports it.

- **Healthy Shape**: `MyVerySpecialResearchLatticeCategory` imports the general category machinery, declares its supercategories, and supplies its specialized methods/refinements inside its own subtree.  Existing ancestors remain unchanged.  Imports therefore flow from the specialized subtree toward the stable foundation, while generic ancestors stay oblivious to the existence of the new descendant unless there is a specific mathematical reason otherwise.

#### `ARC-16`: Finitary Coordinates Are Computational Specializations, Not the Mathematical Architecture

- **Rule**: State objects and operations through their mathematical semantics first: owned sets/families, finite-support elements, Homs, subobjects, kernels/images, products/coproducts, actions, quotients, tensor constructions, and universal maps.  Finite enumeration, bases, coordinates, rows/columns, block matrices, and exhaustive checks are algorithms/representations supplied underneath those objects.  Ordinary mathematical consumers do not lower to finite coordinates merely because today's easiest algorithm is finite.

- **Rationale**: Premature lowering makes finiteness contagious.  Once cohomology, exactness, intersections, actions, or divisor groups know about row counts and Python tuples, extending the underlying object to an infinite framing or a theorem-backed representation requires rewriting every consumer.  A semantic layer localizes the finite assumption: a finite-free Hom may use matrices while an infinite Hom later uses formal blocks, sparse operators, callable maps, or another theorem/engine without changing callers.

- **Violation Example**: `FreeResolution.is_exact()` comparing backend row modules instead of image and kernel subobjects; `Cohomology` rebuilding cycles/boundaries from basis matrices; a formal divisor group forcing its entire prime-divisor index set to be finite because individual divisors have finite support; constructing a block morphism by concatenating finite row arrays.

- **Correct Example**: State exactness as `im(d_1)=ker(epsilon)`, cohomology as `ker(d_n)/im(d_{n-1})`, subobject intersection as a pullback, and a divisor group as the free module on its owned prime-divisor set with finite-support elements.  The finite represented cases dispatch internally to matrix/Sage/Singular algorithms; future infinite cases supply different implementations of the same semantic methods.


#### `ARC-17`: Repair the Semantic API Before Writing a Local Numerical Workaround

- **Rule**: When a consumer needs a mathematical result canonically expressed through an owned semantic construction, the consumer calls that construction. It does not extract coordinates, matrices, rows, columns, basis vectors, engine objects, or finite presentations and reimplement the construction locally. If the required semantic method is missing, incomplete, or awkward to compose, improving that lower-level API is part of the implementation task. Do not preserve a local numerical workaround merely to keep the patch geographically small.

- **Rationale**: A common LLM failure mode is **myopic semantic lowering**: receive an honest mathematical object, immediately forget its semantics, compute on a convenient finite representation, and reconstruct an approximation to the mathematical result. One such patch looks harmless; dozens produce a second numerical implementation layer scattered through consumers. Every consumer then learns finiteness, basis choice, row/column conventions, matrix algorithms, and backend details, so an infinite or theorem-backed implementation requires a repository-wide rewrite. The semantic API is the compression boundary: only `kernel`, `cokernel`, `image`, `pullback`, `quotient`, `torsion_subobject`, `is_torsion_free`, `dimension`, `Hom`, and analogous owners should know how their current representations are computed.

- **Violation Example**: Given `f : M -> N`, call `f.matrix()`, compute a backend nullspace, construct a free module on the nullspace rows, and manufacture an inclusion into `M`. This duplicates `f.kernel()` and hard-codes finite free coordinates in the caller. Likewise, decide whether an inclusion is primitive by taking gcds/minors of its matrix rather than asking whether its cokernel is torsion-free.

- **Correct Example**: `K = f.kernel()` returns the owned kernel together with its inclusion. A subobject inclusion `i : S -> M` is primitive exactly when `i.cokernel().is_torsion_free()`. The finite-free implementation of `kernel()` or `is_torsion_free()` may privately use nullspaces, Smith form, or determinants; an infinite implementation may use a theorem, sparse operator, formal presentation, or another engine. The consumer does not change.
  The live `ModuleMorphism.is_primitive()` already has the right shape: it asks injectivity and then returns `self.cokernel().is_torsion_free()`. Treat this as a model for structural predicates rather than replacing it with a matrix criterion in specialized consumers.

- **Extension Test**: After writing a consumer, mentally replace every finite-rank object by a plausible infinite analogue. If the consumer itself must change because it knows about matrix sizes, complete bases, exhaustive generator lists, or backend rows, the numerical boundary is probably too high. If only a low-level semantic method needs a new case, the architecture is correctly localized.


#### `ARC-18`: The Interface Is Judged by the Invalid Mathematics It Permits

- **Rule**: Design public constructors and methods adversarially against representation shortcuts.  A semantic API is insufficient if an equally public coordinate/vector/matrix path lets downstream code bypass the mathematical object and reimplement its theorems locally.  Close or privatize such hatches; force callers through parents, elements, Homs, structure morphisms, universal constructions, and owned collections.

- **Rationale**: Encapsulation by convention does not survive repeated local implementation pressure.  An exposed numerical representation becomes training data for the next patch, and each patch silently acquires theorem hypotheses, basis conventions, and finite assumptions.  Semantic gating concentrates those proof obligations once.  The interface is therefore evaluated by asking not only “can correct mathematics be expressed?” but also “what plausible nonsense does this API make easy to express?”

- **Violation Example**: A public lattice element constructor accepts arbitrary coordinate lists; an owned morphism exposes a convenient raw matrix accessor used by ordinary consumers; a group action constructor accepts raw matrices without first constructing `rho:G->Aut(M)`.

- **Correct Example**: Elements are formed in their parent from named/owned generators and finite-support mathematical data; matrix data may enter only at the narrow finite-framed Hom construction that returns a genuine morphism; all downstream operations stay on that morphism.  Assertions at likely misuse sites explain the mathematical ambiguity and name the correct construction.


#### `ARC-19`: Formulate at the Generality That Survives Relaxing a Hypothesis

- **Rule**: Define each mathematical notion at the weakest natural hypotheses under which its definition remains valid, then recover stronger cases by parameter, axiom, subcategory, chosen structure, or algorithmic specialization.  Before accepting an interface, test it conceptually by removing common accidental assumptions: finiteness, finite generation, freeness, projectivity, orderedness, enumerability, commutativity, and concrete coordinate realization.

- **Rationale**: Overfitting the definition to today's fixtures or backend makes every later generalization a migration.  A mathematically general semantic owner localizes future work: the finite/free case can have an optimized implementation without teaching every consumer that those hypotheses exist.  Extreme examples are design tests, not necessarily currently computable workloads.

- **Violation Example**: Define a framed module only for a finite ordered basis because the first implementation uses matrices; define a free module only from an integer rank; define formal divisors only over a finite list of possible prime divisors; place an operation on lattices when its definition only uses module structure and a form morphism.

- **Correct Example**: A framing is a selected epimorphism `Free_R(S) -> M` for an arbitrary set `S`; `[n]` is the canonical finite ordered specialization.  Individual elements have finite support even when `S` is infinite or nonenumerable.  Finite matrix realizations and rank-based algorithms live in the finite/framed subcategories while callers retain the same semantic construction.

- **Sweep Question**: “If I drop one hypothesis from the current examples, does the definition still make sense?”  If yes, that hypothesis belongs to an implementation/subcategory, not the definition.



#### `ARC-20`: Structured Objects Include Their Witnessing Arrows

- **Rule**: When the mathematical object is a subobject, quotient, image, re-presentation, or other structured occurrence of an underlying object, the witnessing morphism is part of the mathematical data and therefore part of identity/equality at that structured level.  Do not collapse the structured object to its underlying abstract object or to the image subset suggested by a coordinate realization.

- **Rationale**: A subobject of `Y` is represented by a monomorphism `i:X -> Y`; two copies of the same abstract `X` embedded by different monomorphisms are distinct subobjects.  Dually, quotients remember the epimorphism `Y -> Q`.  Forgetting the arrow loses exactly the relationship that downstream constructions—intersection, saturation, quotienting, pullback, factorization—consume.

- **Violation Example**: Compare subobjects only by their domains or Gram data; identify `L` with the image of `L -> L^#`; compare quotients only by invariant factors while ignoring the quotient maps.

- **Correct Example**: Subobject equality is equality in the owned subobject/slice construction and includes the inclusion; quotient equality includes the projection.  The underlying-object forgetful operation may return equal/isomorphic abstract objects without making the structured objects equal.


#### `ARC-21`: Categories of Arrows, Homs, and Functors Are First-Class Objects of `Cat`

- **Rule**: Treat `Ar(C)`, `Fun(C,D)`, Hom categories, endomorphism/automorphism arrow categories, cores, slices, coslices, and analogous category constructions as actual owned objects of `Cat`, not as implementation namespaces around special Python classes.  Their objects/elements inherit ordinary categorical structure through the same graph as every other category.

- **Rationale**: A morphism is an element of a Hom object, Hom objects themselves participate in arrow-category structure, and functors/natural transformations form ordinary categories.  Making these constructions first-class centralizes method inheritance and eliminates parallel “morphism methods” or “functor utility” mechanisms that bypass the category graph.

- **Violation Example**: Treat morphisms as a third API species unrelated to Hom elements; attach special methods directly to a morphism wrapper because arrow categories are not represented; implement `Fun(C,D)` as a utility registry rather than a category.

- **Correct Example**: `Ar(C)` and `Fun(C,D)` are owned categories; `Hom_C(A,B)` is the appropriate owned Hom/category object; `End`/`Aut` refinements and their elements inherit through the same categorical construction machinery.  Convenience aliases may expose familiar syntax without creating a second ontology.


#### `ARC-22`: Inherited Mathematics Propagates Through Named Functors and Composition

- **Rule**: When a structured category obtains operations from a less-structured mathematical object, represent the passage by the appropriate owned functor and let operations propagate through composition.  Do not make every descendant independently reimplement obligations from `Sets`, modules, groups, or another underlying structure, and do not confuse a faithful/forgetful functor with literal object identity or a backend inheritance edge.

- **Rationale**: The same module can be viewed through its underlying additive group and set without those categories being identical.  A named functor records exactly what structure is forgotten and gives one route for cardinality, iteration, set maps, and other inherited operations.  Composition creates rollup points where a whole family of obligations is discharged once rather than leaf-by-leaf.

- **Violation Example**: A lattice implements `cardinality()` independently of its underlying module/set; every algebraic category duplicates set iteration; Python MRO order silently chooses one of several possible forgetful routes.

- **Correct Example**: Lattice structure maps to the underlying module by an owned functor, module structure maps toward its underlying set, and generic set operations are answered there.  Alternative canonical routes either coincide by construction or are related by an owned natural isomorphism; MRO order never decides the mathematics.

#### `ARC-23`: Additional Structure Refines One Mathematical Object; It Does Not Create Wrapper Ontologies

- **Rule**: Prefer one generic owned representation of a mathematical object together with categorical refinements for additional properties/structure.  Do not create a new concrete wrapper class for every combination of symmetric, alternating, integral, torsion, group-equivariant, graded, or similar refinements when the underlying datum is the same object plus additional structure/properties.

- **Rationale**: Parallel wrapper classes duplicate element behavior, Hom behavior, equality, construction, and backend conversion while obscuring the common object.  Category refinement lets one represented form/module/etc. acquire exactly the additional operations justified by its structure without changing identity or forcing conversions between wrappers.

- **Violation Example**: Separate concrete classes `SymmetricBilinearForm`, `IntegralBilinearForm`, `GroupLatticeForm`, and `TorsionBilinearForm` each storing the same module/form data and copying methods.

- **Correct Example**: Use one generic represented form/morphism object and one formed-module construction; refine it into symmetric/integral/nondegenerate/lattice/group-action categories as the defining data establishes those properties.


#### `ARC-24`: Structural Functors Are Outputs of Category Constructions, Not a Parallel Hand-Written Graph

- **Rule**: A named category expression—root, classifier application, product/pullback, slice/coslice, core, or other owned construction—is authoritative.  Canonical projection/forgetful/structural functors implied by that expression are derived from the construction and composed recursively.  Do not maintain a second manually authored “forgets-to” or preferred-path graph encoding the same relationships.

- **Rationale**: If `C.A` is defined by a classifier pullback over `C`, the projection `C.A -> C` is part of the mathematical definition.  Re-entering that edge in a separate registry duplicates truth and invites mismatches between category identity, method inheritance, and functor routing.  Structural recursion also makes adding a new category expression local rather than requiring registration in every ancestor/path table.

- **Violation Example**: Add `forgets_to = Modules(R)` beside a category whose defining expression already projects to modules; maintain BFS/preferred-functor tables for ancestor routes that the category expression canonically composes; hand-author every axiom projection.

- **Correct Example**: classifier/category constructors create their primary structural maps; `project(C.A,K)` composes the primary projection with `project(C,K)`.  Explicit alternative functors remain first-class when they are genuinely different mathematics, rather than entries in a duplicate hierarchy table.


#### `ARC-25`: Formed Mathematics Starts With the Arbitrary Form Actually Carried by the Object

- **Rule**: In formed-module/lattice mathematics, the base semantics use the declared bilinear/quadratic/sesquilinear form itself.  Do not silently import the standard Euclidean inner product, positive definiteness, nondegeneracy, or finite-dimensional coordinate geometry.  Additional hypotheses refine the category exactly where the mathematical notion requires them.

- **Rationale**: CAS vector APIs are saturated with Euclidean defaults (`dot_product`, standard norms, projections, Gram-Schmidt) whose answers are unrelated to an arbitrary form on the same underlying module.  Letting those operations leak into general formed code is a pervasive silent-wrongness source and makes degenerate/indefinite/infinite analogues impossible without rewriting consumers.

- **Violation Example**: Compute orthogonality by a backend vector dot product rather than `b`; define all lattices as nondegenerate because dual-coordinate code needs an inverse Gram matrix; use a positive-definite shortest-vector routine as the meaning of `roots()` or `norm()` on the base category.

- **Correct Example**: pairings/norms route through the owned form/correlation; radical and orthogonal complement are morphism/subobject constructions; positive-definite reduction/shortest-vector algorithms live behind the definite refinement while the general formed object remains valid for arbitrary forms.


#### `ARC-26`: Category, Object, Runtime Representation, and Presentation Are Distinct Levels

- **Rule**: Keep distinct the mathematical category, an object of that category, the runtime type representing such objects, the owned/Sage category structure attached to that runtime type, chosen presentation data, and property-cut subcategories.  Equivalences or convenient representations do not collapse these levels into one noun or one identity relation.

- **Rationale**: Chosen enumeration/basis data can represent a finite set/free module without being the category itself; a runtime class can represent category objects without being the category; an object and its chosen presentation can be equivalent while carrying different structure.  Collapsing the levels promotes implementation choices into ontology and makes later changes of representation appear to change the mathematics.

- **Violation Example**: Call the Python class of bundled finite-set objects “the category of finite sets”; identify finite free modules with based modules because a basis exists by choice; treat `Cat.of(SomeType)` as the mathematical category rather than one representation of its objects.

- **Correct Example**: explicitly name the owned category and its morphisms, the objects it contains, the generated `ObjectType`/`ElementType` used at runtime, and any framing/enumeration/presentation as additional data/refinement.


* * *

### 2. Public Mathematical API (`API-*`)

#### `API-01`: Public Methods Return Owned Mathematics, Never Backend Objects or Elements

- **Rule**: Every public method on an owned object returns a value in the owned mathematical ontology.
  Public methods never return a Sage module, Sage submodule, Sage vector, Sage matrix, Sage/GAP/Julia element, GAP model, engine pointer, engine parent, or another backend structure merely because that representation is convenient internally.
  Elements returned by an owned parent are owned elements parented by that owned parent.
  There is no public engine accessor or public engine-element escape hatch.

- **Rationale**: Once a raw backend parent or element escapes, every consumer can speak the engine's ontology and the category layer no longer controls what can be stated.
  Public ownership therefore includes element identity and return types, not only method names on the parent.

- **Violation Example**: Public `cover()`, `relation_submodule()`, `coordinate_vector()`, `optimized()`, or `engine()` methods returning Sage objects from an owned presented module; `module_generator(i)` returning a Sage vector; `group_generators()` returning GAP/Sage elements; returning `kernel.V()` or a Sage submodule from an owned Hom computation.

- **Correct Example**: `presentation()` returns the owned relation morphism, `presentation_matrix()` returns a tensor, `module_generator(i)` returns an element parented by the owned module, `group_generators()` returns elements parented by the owned group, `smith_form_module_generators()` returns owned module elements in an owned set, and `invariant_factor_form()` returns an owned isomorphism.


#### `API-05`: Public APIs Accept Preamble Data, Never Raw Backend Objects

- **Rule**: The public boundary is closed on inputs as well as outputs.
  A public constructor or method does not accept a raw Sage/Singular/GAP/Julia/OSCAR/Macaulay2 parent, element, vector, matrix, ideal, morphism, category, or handle as an alternate input form.
  There are no convenience constructors whose purpose is to adopt, wrap, refine, or coerce a backend object into the preamble universe.
  Backend representations are created only by private adapters from already-owned preamble data.

- **Rationale**: Accepting raw backend data makes the backend object model a second public constructor language and forces public code to decide how backend identity, categories, coercions, elements, and chosen data map into owned mathematics.
  That is the same backdoor as returning backend data, only on ingress.

- **Violation Example**: Public `own_ring(SageZZ)`, `own_group(SagePermutationGroup(...))`, `refine_free_module(SageFreeModule(...))`, `FinitelyPresentedModule(sage_submodule)`, or a morphism constructor that accepts a Sage `Map` as a supported public datum.

- **Correct Example**: Public `PolynomialRing(ZZ, "x")`, `FreeModule(ZZ, 3)`, `Groups.S(4)`, `presentation_morphism.cokernel()`, and `A.Hom(B)(...)` consume preamble objects and mathematical data.  Any Sage/GAP representation needed to execute them is selected and constructed privately after the public call has crossed the API boundary.

#### `API-02`: Coordinates Are Framing Data; Coordinate Objects Keep Their Mathematical Type

- **Rule**: Coordinates of an element are exposed through the chosen framing as the owned `module_coefficients` map.
  When an algorithm genuinely requires an ordered coordinate array, use the owned object whose mathematics describes that array.
  A coordinate vector may be a typed tensor when only variance/index data is intended.  A matrix of a linear map between finitely generated framed free modules is the corresponding Hom element
  `Hom_R(F_R(S), F_R(T))`, framed by the matrix units indexed by `T × S`; it is not replaced by a tensor or backend matrix.
  A public coordinate operation never returns a Sage vector or Sage matrix.

- **Rationale**: Coordinates depend on chosen framings, but the coordinate object can itself have intrinsic mathematics.
  Raw backend arrays erase that structure; treating every array as a tensor erases it in a different way.
  The coefficient map records the framing, tensors record variance when that is the intended structure, and matrices retain their canonical Hom interpretation.

- **Violation Example**: `M.coordinate_vector(x)` returning `M_engine.V().coordinate_vector(...)`; representing `Hom_R(R^n,R^m)` by `tensor.matrix(...)`; passing a raw Sage matrix downstream to reconstruct a morphism later.

- **Correct Example**: Use `module_coefficients(x, M)` for the finite support of an element.  Use a typed tensor for a genuine tensor coordinate array.  For finite framed free modules, `MatrixSpace(R,m,n)` is literally `Hom_R(F_R([n]),F_R([m]))`, and a matrix element is that module morphism itself.

#### `API-06`: The Session Namespace and Literal Constructors Are Owned

- **Rule**: The public session module exports only preamble mathematics and ordinary Python support objects explicitly chosen by the preamble.
  It never wildcard-imports a backend namespace.
  Interactive literal constructors installed or consulted by the host parser/preparser (`Integer`, `RealNumber`, complex-number constructors, generator syntax hooks, and analogous names) resolve to preamble-owned constructions or ordinary Python literals according to the preamble language contract.

- **Rationale**: A closed object universe cannot be enforced only at method signatures if the session itself still publishes backend constructors or silently creates backend elements before the first preamble call.
  The parser is part of the public mathematical language.

- **Violation Example**: `from sage.all import *` followed by selectively shadowing a few names; leaving `Integer(3)` as Sage's integer while `ZZ(3)` is owned; allowing `matrix(...)` to remain Sage's constructor because no owned matrix spelling has shadowed it yet.

- **Correct Example**: The session binds `Integer` to the owned integer constructor, binds `MatrixSpace`/matrix notation to the matrix-Hom construction, and omits backend constructors that have no owned preamble meaning.  Backend imports remain module-private implementation dependencies.

#### `API-07`: The Global Session Namespace Is Not an Operation Catalogue

- **Rule**: Keep the public session namespace sparse in mathematical operations.  Global names are appropriate for canonical mathematical objects, category/object constructors, notation entry points, and deliberately chosen **session-language conveniences**; ordinary mathematical operations on already-constructed objects belong to methods on their mathematical owners.  Do not export a free-standing `Product`, `Kernel`, `Orbit`, etc. merely to shorten `owner.operation(...)` or to reproduce a GAP/Julia-style global operation catalogue.

- **Rationale**: Tab completion on a global namespace scales with the entire library and provides no type/domain context.  Tab completion on an owned mathematical object is contextual documentation: the receiver already tells the user what kind of mathematics is being acted on and narrows the valid operations before any documentation is opened.  A small personal preamble may still deliberately include obvious ergonomic forms such as `lmap`/`lzip`; those are language conveniences, not alternative homes for mathematical operations that already have an owner.

- **Violation Example**: Adding `Product`, `Coproduct`, `Kernel`, `Cokernel`, `Orbit`, `Stabilizer`, `DirectSum`, `BaseChange`, `Dual`, or analogous operation functions to `preamble.all` so users call them by remembering global spellings.  Even if each function internally performs perfect categorical dispatch, the public interface still requires the user to know which arguments make each global meaningful.

- **Correct Example**: The session exposes `Sets`, `Modules`, `Groups`, rings such as `ZZ`, constructors needed to create mathematical objects, and a small deliberate set of obvious personal conveniences such as `lmap` and `lzip`.  From mathematical objects the user discovers `C.product`, `M.base_change`, `f.kernel`, `G.orbit`, `G.stabilizer`, Hom-level operations, or element methods by tab-completing the object in hand.

#### `API-08`: Session Use Is First-Class Use

- **Rule**: Do not classify a public preamble name as dead merely because repository source and tests do not call it.  The preamble exists to populate notebooks and REPL sessions, so deliberate session-only constructors, aliases, formatting helpers, and convenience functions are first-class API even when their internal call count is zero.  Before deleting an apparently unused public name, determine whether it is intentional session vocabulary and inspect its export/documentation history.

- **Rationale**: Static internal call graphs measure implementation reuse, not interactive usefulness.  A convenience such as `lmap(f, xs)` can be valuable precisely because a researcher types it at a prompt rather than because backend code imports it.  Treating all internally unused names as dead would systematically erase the purpose of a preamble.

- **Violation Example**: Running `rg lmap src tests`, finding only its definition, and deleting it as dead code without checking whether `preamble.all` is intended to expose it in research sessions.

- **Correct Example**: Keep a deliberate session helper with obvious stable semantics, export it from `preamble.all`, and assess it as part of the interactive language.  Remove a public name only after establishing that it is neither used internally nor intended as session vocabulary.

#### `API-09`: Interactive Representation Shows the Mathematical Element, Not Its Storage Coordinates

- **Rule**: Ordinary `repr`/LaTeX of owned elements should display the mathematical expression in the object's selected symbols/structure rather than a Python tuple, backend vector, flattened coordinate array, or implementation class.  Coordinate representations are explicit derived views through the selected framing and are never allowed to become the default identity of the element.

- **Rationale**: The first thing a researcher sees in a notebook trains how the object is conceptualized.  Printing `(1,2)` for elements of two different framed modules makes equal coordinate strings look like equal mathematical objects and encourages downstream coordinate programming.  A formal linear combination keeps the parent/framing semantics visible.

- **Violation Example**: A lattice element prints as `[1, 2]`; a quotient element prints only its Smith-coordinate vector; a generic module printer applies integer sign tricks that assume an ordered coefficient ring.

- **Correct Example**: An element of `Free_R(S)` renders as its finite formal `R`-linear combination of the actual symbols in `S`, using each coefficient/symbol's own representation.  Explicit `module_coefficients(...)` exposes coordinates when the researcher asks for them.

#### `API-10`: Public Mathematical Signatures Are Closed and Precise

- **Rule**: Public mathematical constructors and methods enumerate the exact mathematical inputs they accept and the mathematical result they return.  Do not expose arbitrary `*args`/`**kwargs` option bags, backend constructor passthrough, sentinel-driven polymorphism, or mode flags that change mathematical meaning/return shape.  Split genuinely different constructions into named methods/constructors or precise source-grounded overloads.

- **Rationale**: An open option bag delegates the definition of the preamble API to whichever backend version happens to receive it and hides required hypotheses/choices from both tab completion and static inspection.  Sentinel/mode polymorphism makes one name denote several different mathematical operations and encourages downstream branch-heavy handling.

- **Violation Example**: `NumberField(*args, **kwargs)` forwarding Sage's whole constructor surface; `foo(x, ambient=None)` where the optional ambient is actually the missing subobject witness; `normal_form(map=True)` changing the return object from a normal form to `(normal_form, map)`.

- **Correct Example**: provide named constructors for the exact number-field/presentation shapes the preamble owns; make subobject structure an inclusion morphism; return a normal-form isomorphism as the canonical result when the witness is mathematically part of the construction.  Private engine adapters may retain exact protocol-level option forwarding when it is quarantined behind the owned operation.

#### `API-11`: Expose Composable Mathematical Objects, Not Convenience Wrappers Around One Use

- **Rule**: When the useful result is itself a standard mathematical object—an invariant/value object, morphism, action, identity, inclusion, quotient map, functor, decomposition, etc.—expose that object directly.  Do not proliferate convenience predicates/actions whose bodies merely perform one obvious comparison/application of the richer object.

- **Rationale**: The object carries additional mathematics for free: equality, composition, kernel/image, restriction, factorization, transport, and reuse.  A one-use wrapper hides this structure and creates a parallel vocabulary that does not compose.

- **Violation Example**: `same_genus(other)` instead of comparing genus objects; `action_on_discriminant_element(g,x)` instead of exposing `O(L) -> O(A_L)`; constructing identity through an identity matrix instead of asking the Homset.

- **Correct Example**: return `genus()`, the induced action morphism/functor, and `Hom.identity()`; callers compose/apply/compare those objects using their ordinary mathematical APIs.

#### `API-12`: Prefer Named Positive Mathematical Predicates Over Negated API Expressions

- **Rule**: When the literature has a standard name for a complementary property, expose that positive predicate rather than requiring users to express it as `not is_X()`.  The two names retain their proper mathematical/computability semantics; do not assume ordinary Python negation is a valid implementation when the predicate is three-valued or assertion-gated.

- **Rationale**: `is_degenerate()` communicates the mathematical concept directly; `not is_nondegenerate()` makes the reader reconstruct a logical complement and can become wrong when “unknown/not currently computable” is distinct from false.

- **Violation Example**: require `not L.is_nondegenerate()` throughout code/notebooks even though degeneracy is a named property; define `is_degenerate = lambda: not self.is_nondegenerate()` across a soft/three-valued boundary.

- **Correct Example**: expose and implement the named positive predicates at their mathematical owner, sharing semantic lower-level constructions where appropriate.

#### `API-03`: Engine Vocabulary Is Not a Compatibility Surface

- **Rule**: An owned API is not a name-for-name facade over Sage.
  Consumers speak the repository's mathematical vocabulary even when the engine has an analogous operation under another name.
  Do not add a public delegation solely because existing Sage code expects `.gen()`, `.gens()`, `.V()`, `.optimized()`, `.basis_matrix()`, `.coordinate_vector()`, `.submodule()`, or `.hom()`.

- **Rationale**: Compatibility delegations preserve the engine as the effective API and make later consumers depend on representation accidents.
  The owned spelling must be the only ordinary route, so a wrong consumer fails visibly instead of silently crossing the boundary.

- **Violation Example**: Adding `M.gen(i)` to an owned free module because one lattice invariant still calls Sage's free-module API; adding `M.submodule(vectors)` because a discriminant-form routine expects Sage submodules.

- **Correct Example**: Rewrite the consumers to use `module_generator`, `module_generating_set`, `framing_morphism`, `subobject_on`, `module_coefficients`, `presentation_matrix`, `invariant_factors`, `smith_form_module_generators`, and `invariant_factor_form` as the mathematics requires.

#### `API-04`: Chosen Presentations Survive Engine Normalization

- **Rule**: A chosen framing or presentation is mathematical data and is never silently replaced by an engine's optimized, Smith-normalized, reduced, or otherwise canonicalized representation.
  A normalization that changes the chosen data produces a new owned object together with the owned morphism or isomorphism relating it to the original.

- **Rationale**: Isomorphic presentations are not identical chosen presentations.
  Engine normalization is algorithmic and choice-bearing; overwriting the original framing loses exactly the data the framed category says the object carries.

- **Violation Example**: Replacing the selected module generators by `smith_form_gens()` after constructing an FGP engine; mutating the relation matrix to the Smith matrix and then treating it as the original presentation; feeding the selected relation rows into a backend submodule constructor that canonicalizes its basis and then treating the backend Smith change-of-basis matrices as changes from the original selected relations.

- **Correct Example**: Keep the selected presentation unchanged and let `invariant_factor_form()` return an explicit owned isomorphism from the original framed module to the Smith-normalized framed module.  A private backend either reduces the selected presentation matrix itself or records the explicit change from the selected relation framing to any canonical backend relation basis before composing normal-form witnesses.

* * *

### 3. Construction & Witness Interfaces (`CON-*`)

#### `CON-01`: Canonical Constructors Consume the Mathematical Datum

- **Rule**: A canonical public constructor takes the datum that defines the mathematical object: a morphism, action, form, inclusion, presentation, generating map, or other named structure.
  A coordinate matrix, row list, backend object, or collection of implementation fields does not replace that datum merely because it can encode it.
  A coordinate convenience constructor is admissible only when the coordinates genuinely determine the mathematical datum, it immediately constructs that datum, and it delegates to the canonical constructor without establishing a second object model.

- **Rationale**: The constructor is where invalid states become unrepresentable.
  If the public constructor accepts a weaker representation, callers can bypass the homset, relation checks, form-preservation checks, or other structure that makes the datum mathematically meaningful.

- **Violation Example**: Constructing a presented module directly from a Sage relation submodule; `with_action(G, matrices)` constructing the group morphism internally; `submodule_from_rows(matrix)` treating rows as the subobject rather than constructing the inclusion.

- **Correct Example**: `presentation.cokernel()` consumes the selected morphism `F_1 -> F_0`; a module with a `G`-action consumes `rho: G -> Aut(M)`; a Gram-matrix convenience first constructs the corresponding form morphism on the specified framed free module and then invokes the canonical formed-module constructor.

#### `CON-02`: Structure Maps Are First-Class Morphisms Constructed by Their Caller

- **Rule**: Actions, representations, inclusions, scalar actions, form maps, comparison maps, and other structure maps exist as morphisms in their own homsets before another object consumes them.
  An object does not accept a source object plus raw generator images and secretly construct a morphism belonging to another category.

- **Rationale**: The morphism carries information that its image does not.
  For a group action `rho: G -> Aut(M)`, for example, `rho` need not be injective; replacing `G` by the subgroup generated by action matrices silently replaces the acting group by `rho(G)` and loses the kernel.

- **Violation Example**: `M.with_action(G, images)` constructing `rho` inside the module; recovering "the acting group" from the matrices appearing in a representation.

- **Correct Example**: Construct `G`, construct `Aut(M)`, construct `rho` in `G.Hom(Aut(M))`, then pass `rho` to the structured-module construction.  If the intended group literally is a subgroup of `Aut(M)`, construct that subgroup and use its inclusion.

#### `CON-03`: Transport Existing Structure Functorially

- **Rule**: When a construction changes an object carrying structure, transport that structure by the corresponding functor or named morphism construction.
  Do not reconstruct the transported structure from coordinate matrices when the defining morphism is already available.

- **Rationale**: Coordinate reconstruction duplicates the mathematics and introduces convention-dependent formulas at every consumer.
  Functorial transport states the definition once and automatically preserves composition and change of presentation.

- **Violation Example**: Building the form on a lattice direct sum by manually assembling a block Gram matrix; constructing the form on a subobject by slicing a matrix; implementing scalar extension by copying coefficients into a fresh matrix without applying the scalar-extension functor to the form morphism.

- **Correct Example**: Direct sum, tensor product, duality, and base change act on the module and on its form morphism; for an inclusion `i: S -> M` and bilinear form `b: M tensor M -> W`, the induced form is `b * (i tensor i)` in the appropriate Hom object.

#### `CON-05`: Chosen Preimages and Construction Provenance Are First-Class Data

- **Rule**: If a later mathematical operation requires not merely an output `F(A)` but the chosen presentation of that output as an image of `A`, represent the pair `(A, F(A))` or the corresponding functor-image object explicitly.
  Do not recover mathematically required preimages by attaching ad-hoc `_preamble_*_source_*` attributes to ordinary output objects and probing those attributes later.
  Incidental diagnostic provenance that is never part of a mathematical operation may remain private metadata, but it cannot be the hidden witness on which an adjunction, inverse transpose, or constructor depends.

- **Rationale**: A general functor output need not determine its preimage.  When a chosen preimage matters, that choice is mathematical data and deserves a type/construction that states it.
  Hidden source attributes create a second undocumented object model and make ordinary codomain objects behave differently depending on which constructor happened to produce them.

- **Violation Example**: Scalar extension setting `_preamble_scalar_extension_source_module` and the inverse Hom transpose later reading it; induction/coinduction attaching `_preamble_induction_source_group_module` or `_preamble_coinduction_source_group_module`; free/cofree `G`-set functors attaching source sets solely so an adjunction can recover them.

- **Correct Example**: Use the existing functor-image construction (or another explicit chosen-image object) when a chosen preimage is required, and let the adjunction consume that selected presentation.  If the inverse transpose can be derived from the unit/counit without recovering a hidden source object, derive it directly instead.  For `Spec`, make the contravariant functor's action on an algebra morphism produce the scheme morphism whose pullback is intrinsic to that morphism, rather than attaching `_preamble_coordinate_algebra_morphism` afterward as a side channel.


#### `CON-06`: Constructor Admission Is a Semantic Firewall

- **Rule**: Judge a constructor by the invalid states and alternate ontologies it admits.  The canonical constructor consumes the defining mathematical datum and performs the containment/well-definedness check exactly once.  Do not broaden constructor inputs for convenience when doing so lets callers bypass that datum.

- **Rationale**: Construction is the point where “this is an element of Hom”, “this map preserves the form”, “this action respects the relations”, or “this is the stated subobject” becomes true.  If arbitrary objects with a `.matrix()` method, coordinate arrays, or loose image lists are also admitted, every downstream caller can bypass the proof encoded by construction.

- **Violation Example**: A Hom accepting any object with matching endpoints and a matrix; `with_action(G, images)` constructing the group morphism internally; an element constructor accepting a bare vector whose parent/framing is unstated.

- **Correct Example**: `G.Hom(Aut(M))(generator_images)` constructs and validates the action morphism, and the structured module consumes that `rho`; a free/presented module consumes its framing/presentation morphism; a matrix convenience, when mathematically unambiguous for a canonically framed Hom, immediately constructs that Hom element and returns no parallel representation.

#### `CON-07`: Chosen Structure Is Data; Derived Subcategory Membership Is Output

- **Rule**: Do not encode a derived mathematical property or category membership as a mode boolean or constructor switch.  Construct from the defining datum and refine/place the resulting object according to properties established from that datum.  If an additional *choice* is genuinely part of the structure, accept the actual chosen datum, not a boolean claiming it exists.

- **Rationale**: Flags such as `even=True`, `negative=True`, `torsion=True`, or `nondegenerate=True` make the caller duplicate facts the object/category should own and permit contradictions between the flag and the data.  Conversely, a selected orientation, framing, action, embedding, or volume form is real extra data and must remain explicit.

- **Violation Example**: `Lattice(G, even=True)`; `Form(..., nondegenerate=True)`; `saturation(in_ambient=M)` where the missing datum is actually an inclusion morphism.

- **Correct Example**: Construct `Lattice(G)` and refine it into `EvenLattices` when justified; pass an actual `rho:G->Aut(M)` for an action; call saturation on the subobject/inclusion that already carries its codomain.


#### `CON-08`: A Mathematical Choice Is Represented by Its Selecting Datum

- **Rule**: Whenever several mathematically valid objects/maps could satisfy a phrase such as “the extension”, “the lift”, “the normalization”, “the dual”, “the section”, or “the presentation”, either identify the canonical construction that removes the choice or represent the chosen datum explicitly.  Do not hide a choice in a boolean, mode string, import state, or undocumented constructor convention.

- **Rationale**: A definite article silently asserts uniqueness/canonicity.  When the mathematics supplies only a family of choices, downstream functoriality and equality depend on which one was selected.  First-class selected data makes that dependency visible and composable.

- **Violation Example**: `normalize=True` mutates/re-presents an object without returning the isomorphism; `map=True` changes a constructor's mathematical return object; `dual()` ambiguously chooses among module, metric, or Pontryagin duals; a chosen preimage is recovered from hidden provenance.

- **Correct Example**: `invariant_factor_form()` returns the normalized framed module with its explicit isomorphism; different dual functors have distinct owned names; a selected section/lift/preimage is stored as a morphism or functor-image datum.


#### `CON-09`: Universal Constructions Return Complete Mathematical Data

- **Rule**: A universal construction returns an owned object together with the canonical arrows that make it that construction, either as explicit components of the returned construction or as intrinsic methods on the returned structured object.  Never return only a presentation, basis, underlying abstract object, or numerical representative and require callers to reconstruct the universal maps.

- **Rationale**: The kernel is not merely an isomorphic module of solutions; it is a subobject with a canonical inclusion.  The cokernel is not merely an abstract quotient module; it comes with the canonical projection.  Products have projections, coproducts have injections, pullbacks/pushouts have their legs.  These maps are what make the construction composable and let callers state universal properties without descending to coordinates.

- **Violation Example**: `f.kernel()` returns generators/basis rows with no inclusion into `domain(f)`; `f.cokernel()` returns a normalized module but drops `codomain(f) -> coker(f)`; a pullback returns an object but not the maps to the two factors.

- **Correct Example**: `K = f.kernel()` is an owned subobject whose `inclusion()` has codomain `f.domain()`; `Q = f.cokernel()` owns `Q.projection(): f.codomain() -> Q`; a quotient element may provide a chosen `lift()` as representative selection, explicitly not as an inverse to the projection.


#### `CON-10`: Do Not Parameterize a Notion Already Determined by Existing Mathematical Data

- **Rule**: If the current object, morphism, base map, or category structure already determines the standard mathematical notion uniquely, derive it from that data.  Do not add a parameter, flag, policy object, or user-selected convention that silently redefines the notion.  Extra input is accepted only when the mathematics genuinely contains a choice, in which case `CON-08` requires the selecting datum itself.

- **Rationale**: Parameters suggest a family of legitimate meanings.  For intrinsic notions this creates false degrees of freedom and lets callers contradict the structure already present.  It also encourages API proliferation (`foo(..., mode=...)`) where distinct mathematical operations should either be derived canonically or have distinct names.

- **Violation Example**: Add `integral_over=D` to redefine integrality of a ring-valued form when the structural map `R -> W` already determines integrality over `R`; pass `even=True` or `torsion=True`; make “the dual” selectable by a mode string instead of using distinct dual functors.

- **Correct Example**: Compute integrality from the specified ring extension; derive evenness/torsion as properties; represent a genuinely chosen orientation, embedding, section, framing, or presentation by its actual mathematical datum.


#### `CON-11`: A Framing Is a Selected Epimorphism `Free_R(S) -> M`

- **Rule**: Model a framed module by an actual owned set `S` and a selected epimorphism `Free_R(S) -> M`.  The framing set is the domain of the distinguished-generator map; generator evaluation is the image of its free generators.  Do not identify a framing with a Python sequence, an ordered basis, or a reversible label-to-element correspondence unless stronger chosen structure supplies those properties.

- **Rationale**: Finite generation, freeness, a basis, order, and enumerability are independent hypotheses.  A generic framing may use an infinite/nonenumerable set, and an epimorphism may identify distinct free generators.  Treating a framing as a tuple/basis silently adds all of those hypotheses and creates exactly the finite-coordinate blast radius `ARC-16` forbids.

- **Violation Example**: `self._module_generators = tuple(generators)` as the definition of framing; recover a framing label from every generator image; require a rank integer when the natural input is an arbitrary set `S`.

- **Correct Example**: retain `S`, `Free_R(S)`, and the selected epimorphism.  The canonical rank-`n` free module is the specialization `S=[n]`; a based module is the refinement in which the framing morphism is an isomorphism and the additional ordering/indexing data is actually present.



#### `CON-12`: Public Construction Enters Through the Owning Mathematical Root; Refinement Is an Output

- **Rule**: Public constructors are owned by the natural general category/object whose defining datum the caller has.  The construction validates that datum, builds the object, and places/refines it into every stronger category justified by the result.  Do not require callers to choose a specialized subcategory or concrete implementation class before construction unless that choice is itself additional mathematical input.

- **Rationale**: A researcher who knows a Gram form, presentation, group action, polynomial, scheme datum, etc. should not need to predict which internal refinement or backend class the finished object will occupy.  Constructors on every subcategory duplicate routing knowledge and make refinement a user obligation instead of a consequence of construction.

- **Violation Example**: Require `RootLattice("E8")` instead of constructing the lattice and discovering/refining its root-lattice structure; expose a private `BasedFreeModuleImpl(...)` alongside the owned free-module constructor; ask the caller to select `Even`/`Nondegenerate` constructor variants from properties the datum determines.

- **Correct Example**: construction enters through `Lattices(R)`, `Modules(R)`, the appropriate Hom/category root, or a canonical object constructor such as `Lattice(...)`; the constructor returns the owned object already placed in its strongest established refinements.  Private implementation selection occurs after mathematical construction/routing.



#### `CON-13`: Supplied Generating Data Constructs the Generated Subobject/Subgroup, Never the Canonical Whole

- **Rule**: Caller-supplied generators, relations, samples, or other uncertified finite data construct exactly the mathematical object generated by that data.  They do not stand in for a canonical ambient object/group whose completeness is a separate theorem/computation.  Canonical objects exist independently at their natural owner even when enumeration/generator computation is unavailable.

- **Rationale**: A list of isometries proves only a subgroup `H <= O(L)`.  Treating it as `O(L)` makes every orbit, stabilizer, kernel, index, and invariant computation silently answer the wrong group when the list is incomplete, while each local operation can remain internally valid.  The same distinction applies to supplied spanning data versus an entire canonical subobject whenever completeness is not established.

- **Violation Example**: `L.O(generators=gens)` returns the canonical orthogonal group; `Aut(X, generators=...)` substitutes a finitely generated subgroup for the automorphism group; downstream invariants are labeled as canonical-group invariants.

- **Correct Example**: `L.O()` is the canonical predicate-defined group object with membership/element operations available; `L.O().subgroup(gens)` is the supplied subgroup.  A specialized algorithm may later compute/prove a generating family for `L.O()` and then its own `group_generators()` method returns that chosen family.



#### `CON-14`: A Free Object Is Built on a Set; an Arity Is a Chosen Set

- **Rule**: The free functor takes a set.  There is no canonical set of cardinality \(n\), so `R^n` names no object on its own, and an integer arity is sugar for *choosing* one -- it must resolve to a named set and route through the set-taking constructor.  Any construction indexed by an arity states the chosen set in its docstring, and its endpoints are the free objects on those sets.  Where the choice is what the construction records -- matrix entries indexed by row and column labels, a framing, a chosen presentation -- name the sets, never the integers.

- **Rationale**: Two free modules of the same rank on different label sets are isomorphic and not equal, and the owned parents are deliberately not interned so that two structures on isomorphic underlying objects stay distinct.  A construction that identifies free objects by rank has thrown away the labels its own data is indexed by, and every downstream operation that reads a matrix entry, a coordinate, or a generator by name is then reading from an object the caller cannot name.

- **Violation Example**: `M_{m x n}(R) = Hom_R(R^m, R^n)` in a docstring; a matrix constructor that builds a rank-\(n\) parent directly instead of through the set-taking one; a test asserting `f.domain() is ZZ**2`, which passes for an implementation that identified free modules by rank alone.

- **Correct Example**: `M_{m x n}(R) = Hom_R(F_R(S), F_R(T))` for chosen finite sets; `FreeModule(R, n)` resolving to `FreeModuleOn(R, Sets.Delta[n-1])` through one constructor; a test asserting `FreeModule(ZZ, 2) is FreeModuleOn(ZZ, Sets.Delta[1])` and that a free module on another two-element set is not it and has a different Hom.

#### `CON-15`: A Tuple Is an Element of a Product; Name the Product

- **Rule**: An operation that yields several values yields **one element of the product of a family over an index set**.  Before writing a tuple, ask which product it is a point of *and over which index set*: a pair of naturals is the constant family \(\mathbb N\) over a chosen two-element set; a tensor's shape is the constant family \(\mathbb N\) over that tensor's own index set; the components of a commutative square are the family of its two homsets.  A bare Python tuple never appears in a public signature, a return, or an annotation.

  Ask the objects, never a global constructor.  `STY-02` governs the call: `C = X.ambient_category()` and then the category's own product, the way `ARC-07` has a homset asked of its endpoints as `A.Hom(B)`.  A free `Product(A, B)`, `CartesianProductOfSets(...)` or `CartesianProductOfFamily(...)` is the global-dispatcher shape `STY-02` names, and the binary forms additionally pick `Sets.Δ[n-1]` silently, which is the arity-for-a-set substitution `CON-14` forbids.

  **Known gap.** The owned categorical hook is binary -- `_categorical_product(left, right)`, whose body calls the binary sugar -- so a category cannot currently be asked for a product over an index set, and this rule has no compliant spelling for the general case.  That is the finding, not a licence to use the free constructor: the hook wants a family form before the conversions this policy implies can be written.

- **Rationale**: \((0, 2)\) is not a container holding two integers.  It is a point of \(\mathbb N^2\), and \(\mathbb N^2\) is an object of a category with projections, a universal property, its own equality, and morphisms into and out of it.  Writing the point as a Python tuple discards its parent, so the value arrives with no category and no equality of its own, and every caller must re-derive what it was a point of -- which is why a test given such a return has nothing owned to compare against and is forced out of the universe (`DEV-37`).  The repair needs no new type: `Product` is already an owned construction, so the work is naming the product that was always implied.  Minting a bespoke class per invariant is the wrong repair and the characteristic over-compliance with this rule; the question is never "what type should this be" but "which product is this an element of".

- **Violation Example**: `return (0, 2)` from a valence; `def signature_pair(self) -> tuple[int, int]`; returning `self.left(), self.right()` for a square's components; a shape returned as `(rank, rank)`; a test comparing any of these against a tuple display, which is the same defect observed from the far end.

- **Correct Example**: a valence as an element of `CartesianProductOfFamily(Sets.Δ[1], lambda _: NN)`, with the two-element index set written down; a tensor's shape over that tensor's own index set, so the order-2 case is a specialisation rather than the definition; a square's components as the product of the two homsets, so that projecting recovers each morphism in its own homset; invariant factors as the indexed family they are, ordered by divisibility, with the divisibility chain a property of the family rather than of a Python sequence.

#### `CON-16`: One Constructor Entry per Category; Every Other Route Computes Its Datum

- **Rule**: A category has one constructor, and it takes the datum that defines its objects (`CON-01`).  Every other way of building an object -- a convenience on presented data, a functor image, an object adopted from the engine, a universal construction -- computes that datum from its own inputs and calls the one constructor.  An input object a convenience received (the module a multiplication was stated on, the module a form or a group action equips) may be retained as data and returned by the accessor the specification names, `unformed_module()`; the object never exposes an identification map back to it.  `equip_*` and `forget_*` morphisms, `*_source_module` accessors and `from_*`/`to_*` identifications are the tell that construction was duplicated rather than routed.  A data subcategory `XWithChosenY` is admissible only when `Y` is a choice beyond the defining datum of `X` -- a presentation of a module, a basis of a free object; the defining datum itself never names a subcategory.  A constructor's admission check decides on finitary data and otherwise records `Unknown` as the hypothesis the object carries; it never asserts a finite framing as the only route.
  An \(R\)-algebra is the instance that fixed this rule: its datum is an additive group \(A\) with a biadditive multiplication together with \(\rho\in\operatorname{Hom}_{\mathbf{Rings}}(R, Z(A))\), \(Z(A)\) the centroid of \(A\) (the additive endomorphisms commuting with left and right multiplication, Mathlib `CentroidHom`), which is the centre when \(A\) is unital associative.  No unit, associativity or commutativity is assumed; those are axioms above the node, and a Lie bracket is the multiplication of its algebra.  Over commutative \(R\), which is the case this tree works in, this is nothing more than an \(R\)-module \(M\) with an \(R\)-bilinear \(m\colon M\otimes_R M\to M\): the datum \((M, m)\) already is the structure, \(\rho\) is the scalar action of \(M\), and the textbook definition of a Lie algebra over a field carries over unchanged.  The centroid is only the name of where \(\rho\) lands; it is not machinery the construction needs.

- **Rationale**: Two constructors for one category produce two kinds of object with different capabilities, and consumers start routing by which one they hold.  A copy of the input needs a map back to the input, and that map needs a name, and the name names nothing in mathematics.  The specification writes `form.unformed_module() is module` and `Modules(R[G])(M, action)`: the retained input is data, the structured object is built on that data, and elements pass between them by coercion.

- **Violation Example**: `Algebras(R)(M, m)` building a second module and retaining `M` as a "multiplication source" with `from_multiplication_source`/`to_multiplication_source`; `AlgebrasWithChosenMultiplication` as a subcategory of `Algebras(R)`, with the algebra Hom, `product` and the unit routing on membership in it; `forget_form_morphism`/`equip_form_morphism` on formed modules and lattices and `forget_action_morphism`/`equip_action_morphism` on group modules; a structure-map constructor (`_own_algebra`) that exists only for engine-adopted rings; a multiplicativity check that asserts a finite module framing.

- **Correct Example**: `Algebras(R)(A, m)` as the one entry, with \(A\) an \(R\)-module and \(m\) an \(R\)-bilinear multiplication, producing \(\rho\colon R\to Z(A)\) from \(m\) (for \(R\) over itself, \(A=R\) as the free rank-one module with its multiplication, so \(\rho=\mathrm{id}_R\)); `M.algebra_from_multiplication(m)` calling that entry; `M.equip_bilinear_form(R, b)` calling the form-module entry with `(M, b)`, whose result answers `unformed_module()` with `M`; a Sage polynomial ring constructed as its module with its own multiplication through the same entry; a Hom admitting a linear map by asking the module Hom whether `f m_A = m_B (f (x) f)`, and carrying `Unknown` as its hypothesis when that is not decidable.

* * *

### 4. Category Placement & Capability (`CAT-*`)

#### `CON-04`: Coordinate Matrices Belong Exactly to Free-Module Homs

- **Rule**: A matrix of a linear map is the element of `Hom_R(F_R(S),F_R(T))` determined by chosen free framings.  Do not assign a coordinate matrix to an arbitrary morphism of finitely generated or finitely presented modules merely because source and target have generating sets.  Constructions on nonfree modules use their presentations, generating morphisms, and relations directly.

- **Rationale**: A generating family of a nonfree module is not a basis.  Recording images of generators is sufficient to define a morphism subject to the source relations, but it is not a matrix in a Hom between free modules.  Confusing the two silently treats a presentation as an isomorphism with a free module.

- **Violation Example**: Constructing `coker(f: M -> N)` for presented modules by calling `f.matrix()` and appending its rows to a presentation matrix, even though `M` or `N` is not free.

- **Correct Example**: If `N` has selected presentation relations and `M` has a chosen generating morphism, present `coker(f)` by the existing relations of `N` together with the coefficient rows of `f(m_s)` in the chosen framing of `N`.  Only when both endpoints are framed free modules is that same data literally the matrix of `f`.


#### `CAT-01`: Place the Method by Mathematical Domain; Route Algorithms by Computable Case

- **Rule**: Put a mathematical method on the first category/object/element where the notion itself is well-defined. Do not invent computability categories merely to hide methods whose values mathematically exist more generally. Inside that correctly owned method, route among the cases for which exact algorithms are currently implemented, preferably by category/representation-aware `match`/`case` or specialized overrides. The unhandled remainder may terminate with an informative assertion stating the current computational limitation. A method whose entire implementation is immediate failure is forbidden; `NotImplementedError` is not a mathematical implementation strategy.

- **Rationale**: Mathematical domain and computational domain are different. Every set has a cardinality, but exact cardinality is undecidable/unavailable for arbitrary represented sets. Every formed module has a well-defined nondegeneracy property, but a callable form on an infinite-rank projective module may be outside current algorithms. Hiding such methods on `SetsWithComputableCardinality` or `FormedModulesWithDecidableNondegeneracy` would encode today's software limitations as false mathematics. Assertion-gated case routing instead keeps the ontology correct while making the present computational frontier explicit and auditable.

- **Violation Example**: Creating `SetsWithCardinality` so only those sets expose `cardinality()`; moving `is_nondegenerate()` off general formed modules merely because the current implementation needs a finite Gram tensor; exposing `kernel()` with a body consisting only of `NotImplementedError`; using `hasattr`/exception fallback to discover an algorithm.

- **Correct Example**: `Sets().ObjectType.cardinality` routes finite/enumerated/symbolic cases to exact algorithms and ends with an informative assertion for a represented case not yet handled. `FormedModules(R).ObjectType.is_nondegenerate` computes from the correlation/Gram tensor where available and assertion-gates currently undecidable representations. A truly positive-definite-only construction, by contrast, belongs on `PositiveDefiniteLattices` because its **mathematical definition**, not merely its algorithm, has that hypothesis.

#### `CAT-09`: Semantic Parity Never Means Signature Parity

- **Rule**: When importing capability from Sage, archived code, another CAS, or a reference implementation, first determine the mathematical entity on which the operation is well-defined and the datum it actually consumes.  Recreate that semantic capability in the owned category graph; do not copy the foreign method signature, placement, mode flags, or witness-compensating parameters merely because the upstream implementation exposes them.

- **Rationale**: A signature embodies an ontology.  APIs without first-class subobjects/morphisms often hang morphism-dependent operations on bare objects and add `ambient=` parameters; APIs without category refinement often add `even=`/`negative=` modes.  Porting those signatures imports the old mathematical model along with the computation.

- **Violation Example**: Port Sage's `saturation(in_ambient=...)` directly onto an owned lattice; mirror an upstream `even=` constructor flag; expose `is_submodule(M)` on a bare object rather than an embedding/existence question in the appropriate Hom.

- **Correct Example**: Site saturation on the subobject/inclusion, derive category membership from the constructed object, and represent embedding existence by the relevant `Emb(A,B)`/Hom object.  Reuse the upstream algorithm privately after the semantic interface has been corrected.

#### `CAT-10`: The Owned Category Type Protocol Is `ObjectType` / `ElementType` / Hom-Category Types

- **Rule**: The public owned category architecture speaks in the preamble's type protocol: `ObjectType`, `ElementType`, `HomCatType`, `EndCatType`, `AutCatType`, and the corresponding arrow types (`ArrowType`, `EndArrowType`, `AutArrowType`).  `ArrowType` is conceptually the element type of the Hom-category object, not an independent third method mechanism.  Sage `ParentMethods`, `ElementMethods`, `MorphismMethods`, dynamic classes, and related machinery may remain private runtime implementation details while this protocol is completed; new doctrine and APIs do not treat those Sage names as the mathematical architecture.

- **Rationale**: The owned category graph is supposed to describe objects, elements, and Homs uniformly.  Reusing Sage's method-container vocabulary as public ontology repeatedly causes contributors to think of attached mixin buckets rather than instantiated implementation types generated by the category graph.

- **Violation Example**: Specify a new preamble feature as “put this in `MorphismMethods`” without first stating the Hom/arrow category that owns it; document `ParentMethods` as a public mathematical type; build a separate morphism-class hierarchy because the Hom-category element type was not considered.

- **Correct Example**: State that category `C` supplies an `ObjectType`; `Hom_C` supplies its object/element types; arrows are elements of the Hom-category construction.  Map those owned declarations onto Sage's dynamic method installation privately until the runtime migration is complete.

#### `CAT-11`: Functorial Domain Restrictions Are Categories, Not Runtime Rejection Branches

- **Rule**: A functor's declared domain is the most general category on which the mapping is actually functorial.  If a construction transports only isomorphisms, declare it on `C.core()`; if it needs a slice/coslice/arrow category or a parameterized base-change category, use that category.  Do not advertise a functor on a larger domain and reject ordinary morphisms inside `_apply_morphism`.

- **Rationale**: Functoriality is part of the mathematical type.  A runtime branch that says “this morphism is unsupported” after accepting it into the functor's domain encodes a false signature and moves a categorical hypothesis into control flow.

- **Violation Example**: Define the center as a functor on all rings and assert that each incoming ring map happens to preserve centers; define a construction on `C` while every non-isomorphism branch immediately fails.

- **Correct Example**: When only isomorphisms transport the construction, use `C.core()` as the domain.  Other restrictions are modeled by the appropriate owned subcategory/category construction, after which the functor action is total on its declared arrows.

#### `CAT-12`: Sage's Category Graph Is Empirical Runtime Evidence, Not Mathematical Authority

- **Rule**: Read Sage source/runtime behavior to learn exactly what Sage encodes and which algorithms/methods a Sage category supplies.  Decide mathematical category identity, inclusions, forgetful/projection functors, and equivalences in the owned graph independently.  Never treat Sage `==`, `is_subcategory`, `super_categories()`, `all_super_categories()`, or absence/presence of an edge as proof of the corresponding mathematical statement.

- **Rationale**: Sage's graph is intentionally shaped by dynamic dispatch/MRO and historical API choices.  A `super_categories()` edge can represent several kinds of structural maps; “immediate” parents are a generating set selected for linearization; equal parent lists do not imply equal categories; mathematically required edges can be absent; two presentations of the same construction can compare unequal.

- **Violation Example**: copy Sage's `Modules(R) -> Bimodules(R,R)` or a facade/category edge into the owned graph merely from its spelling; infer that two refinements are equivalent because their Sage parent lists coincide; infer a mathematical non-inclusion because Sage lacks the edge.

- **Correct Example**: first identify the normalized mathematical objects/structures and their actual functors; then maintain a backend correspondence that records how Sage's declarations/behaviors realize or approximate those owned categories for computation.

#### `CAT-13`: Category Identity, Standard Name, and Classifier Expression Are Three Distinct Layers

- **Rule**: Maintain one mathematical category identity.  Attach an established public noun/notation when one exists, and separately retain the classifier/category expression that defines or constructs that identity.  A named composite or alias does not create another category object.  Classifier names are interpreted relative to their host/defining morphism, not as globally meaningful Boolean labels.

- **Rationale**: `Semigroups` and `Magmas.Associative` can be a standard name and a defining presentation of one category.  `Commutative` on groups and a similarly spelled property in another theory need not be the same classifier.  Conflating name, identity, and presentation creates duplicate vertices, string-based ontology, and ad-hoc alias edges.

- **Violation Example**: create separate `Semigroups` and `Magmas.Associative` vertices; mint one global `Finite`/`Commutative` classifier keyed only by its word; make `GradedAlgebras` an independent species instead of the relevant classifier pullback/refinement.

- **Correct Example**: one owned category identity carries its standard name and its definitional expression; classifiers are declared at their natural host and transported by pullback/composition to categories where the same structure/property is induced.

#### `CAT-14`: Category Constructibility Is Derivability of Canonical Structural Maps, Not Graph Reachability

- **Rule**: Determine whether a classifier/category expression can be formed from the canonical structural maps supplied by the owned grammar: projections/forgetful functors, composition, classifier application/pullback, slice/coslice/core/etc. as defined.  Do not use arbitrary graph reachability, name presence, reverse traversal of projections, or Sage MRO paths as a proof that the mathematical construction exists.

- **Rationale**: A graph can connect vertices by arrows whose direction/type do not provide the data required by a pullback/classifier.  Reachability forgets roles and universal properties, and reverse traversal fabricates structure.  Typed structural derivation keeps construction aligned with the actual mathematical diagram and makes ephemeral classifier towers possible without minting named nodes.

- **Violation Example**: infer `C.A` because a path from `C` eventually reaches a node named `A`; search backwards from a classifier projection to claim the classified structure; require every constructible classifier tower to have a named category vertex.

- **Correct Example**: the defining structural functor `C -> H` together with classifier `H.A -> H` yields `C.A = C x_H H.A` and its projection; ancestor routes are compositions of those canonical maps.  No extra named node or graph-search witness is required.

#### `CAT-15`: A Supercategory Declaration Is a Theorem, Never a Route to a Method

- **Rule**: `super_categories()` returns the categories that every object of this one is an object of, by the definition in the docstring, over the same parameters.  Nothing else goes in the list: not the category whose `__init__` makes construction succeed, not the one that owns a method the leaf wants, not `Sets()` or `Objects()` as a root because the real parent is not in the tree yet.  When the honest parent does not exist, build it or leave the declaration abstract so the category refuses to construct (AGENTS.md, *A supercategory declaration is a mathematical claim*).

- **Rationale**: Sage reads the list by inheritance, so every entry installs the target's operations and axioms on every object and every descendant.  An entry chosen for convenience is a false theorem that every later reader inherits and that no test can see, because each object still answers.  On 2026-09-16 thirty categories declared `Sets()`, among them sheaves, ringed spaces, pairings, arrow categories and a semiring, and twenty-one declared `Objects()`; nothing was wrong with any of their objects, only with what had been claimed about them.

- **Violation Example**: `PairedModules -> OwnedSets()` because a pairing needs a parent; `OrdinalSemirings -> Objects()` for a semiring; `AffineGroupSchemes -> Objects()` with a comment that forgetting the group structure "is a functor, not an inclusion"; `Algebras -> Sets()` for modules with a multiplication.

- **Correct Example**: `OrdinalSemirings -> OwnedSemirings()`; `Algebras(R) -> Modules(R)`; `AffineGroupSchemes -> AffineSchemes(R)`; a pairing left undeclared until the comma category over the tensor functor exists, with the missing construction recorded.

#### `CAT-16`: Structure Forgotten in Place Is a Declaration; a Change of Base or Parameter Is a Functor

- **Rule**: Declare `C -> D` exactly when an object of `C`, with the structure `C` adds forgotten and every parameter unchanged, is an object of `D`: an `R`-algebra is an `R`-module, an affine group scheme over `S` is an affine scheme over `S`.  Never declare a relation whose objects change base or parameter: restriction of scalars along `S -> R`, base change of a scheme, the passage from an `R[G]`-module to a `G`-object over `R`, from an ideal to the fractional ideal it generates.  Each of those is a functor obtained from its category by a method named for the construction, with its preservation theorems stated on the functor.

- **Rationale**: the two are easy to confuse because both are forgetful and both are true sentences.  They differ in what inheritance does with them.  In place, the inherited operations and axioms are the object's own.  Across a base, Sage applies every axiom of the source to the target (`CategoryWithAxiom.super_categories`, category_with_axiom.py), so `Modules(QQ).FinitelyGenerated()` would inherit `Modules(ZZ).FinitelyGenerated()`, and `Modules(R[G]).FinitelyGenerated()` the R-module property, both false.  The tree had it backwards in both directions: `Algebras` refused the in-place declaration and made the cross-base one.

- **Violation Example**: `Modules(R) -> Modules(S)` for a restriction base; `Schemes(R) -> Schemes(ZZ)`; `Modules(R[G]) -> GObjects(G, Modules(R))`; `Ideals -> FractionalIdeals`; the `Algebras` docstring reasoning that the relation to modules "is the forgetful functor, not a category inclusion" and declaring `Sets` instead.

- **Correct Example**: `Algebras(R) -> Modules(R)`, and `Modules(S).restriction_of_scalars(f)` for `f: S -> R` returning the functor with its image category; `Schemes(R).base_change_functor(ring_map)`; `CommutativeIdeals(R).extension_to_fraction_field()`; `GObjects(G, Modules(R)) ≃ Modules(R[G])` as an explicit equivalence with both directions.

#### `CAT-17`: A Property Is an Axiom on Its Base; a Chosen Datum Is a Subcategory Class That Declares the Axiom

- **Rule**: Before writing a class for "the `X`s that are `P`", decide whether `P` is a property of the objects or a chosen datum.  A property (finitely generated, torsion, free, Noetherian, separated, symmetric, countable) is a nested `class P(CategoryWithAxiom)` on the base that first defines it, with a `SubcategoryMethods` accessor and, for a new name, one `all_axioms` registration; there is no standalone class.  A chosen datum (a framing, a presentation, a chosen multiplication, a differential, an augmentation, an enumeration, an order, a Koszul parity) is a class, and it declares the axiom category of the property it truncates to.  The crossing from property to datum is one named method that computes the datum once (AGENTS.md, *Property subcategories vs data subcategories*).  A property with more than one established name in the literature takes the reference text's name; choosing between Bourbaki's "alternating" and Sage's "strictly commutative" is not coining, and a property class kept "because no axiom was coined" is this rule violated, not respected.

- **Rationale**: a property is the propositional truncation of the datum ("some finite framing exists"), so the two are one notion at two levels, and the class-per-notion instinct writes them as unrelated siblings.  Sage's axiom mechanism exists so that properties compose without classes; a hand-written property class cannot be joined with another and must restate every diamond.

- **Violation Example**: `class FinitelyPresentedModules(...)` beside `class ModulesWithChosenFinitePresentation(...)` with no declaration between them; `OwnedNoetherianRings`, `SeparatedSchemes`, `InfiniteEnumeratedSets` as classes; a `GradedCommutativeAlgebras(R, M, parity)` class whose parity was a category parameter, so that a parameterless axiom could not later state it.

- **Correct Example**: `OwnedRings.Noetherian`, `Schemes.Separated`, `Modules.FinitelyPresented` as nested axiom classes; `ModulesWithChosenFinitePresentation(R) -> Modules(R).FinitelyPresented(), FramedModules(R)`; the parity as part of the grading datum on `GradedModules`, read by the `Supercommutative` axiom.

#### `CAT-18`: No Class Is Named for a Combination of Properties; Joins Are Computed

- **Rule**: The category of objects with properties `P` and `Q` is spelled `Base().P().Q()`, and Sage constructs it as the join.  Writing a class for the combination is banned, whatever its docstring says, and so is writing a class for one property on a subcategory that is itself one property.  A combination that needs operations of its own puts them on the nested join class Sage already provides for it (`class Q` nested inside `class P`), never on a new top-level class.

- **Rationale**: the product of independent property axes, flattened into names, is what produced the block of 135 categories: every square in it was the same diamond declared twice, and every new axis multiplied the classes.  Computed joins are also the only place where the commutativity of the diamond is a theorem of the mechanism rather than an assertion at each site.

- **Violation Example**: `FinitelyPresentedQuadraticFormModules`, `FinitelyGeneratedFreeFormModules`, `OwnedCompleteLocalRings`, `CommutativeDifferentialGradedAlgebras`, `StrictlyCommutativeDifferentialGradedAlgebras` as classes, each declaring two parents.

- **Correct Example**: `FormModules(R).FinitelyPresented()`, `OwnedRings().Commutative().Local().Complete()`, `DifferentialGradedAlgebras(R).Supercommutative()`; a name the specification requires kept as a thin function returning that join.

#### `CAT-19`: An Axiom Name Is Global and Means What Its Defining Base Means

- **Rule**: Sage applies an axiom to every subcategory of the base that defines it, with that base's meaning, and it walks declared supercategories to find the definition.  So an axiom named `FinitelyGenerated` on `Modules` means "finitely generated as a module" on every algebra, lattice and group module too.  A property that is relative to a different structure gets a qualified name in Sage's own idiom (`FinitelyGeneratedAsMagma`, `FinitelyPresentedAsAlgebra`), registered once.  Before adding a name, check `sage.categories.category_with_axiom.all_axioms` and reuse Sage's when the meaning matches.

- **Rationale**: two bases defining the same axiom name with different meanings make one of them false on every category that declares both, and the falsehood is silent because the join still constructs.

- **Violation Example**: a `FinitelyPresented` axiom on `Algebras.Associative.Unital` while `Modules` defines `FinitelyPresented`, so that `R[x]` claims a finitely presented underlying module; a `Free` axiom on algebras meaning "free algebra".

- **Correct Example**: `FinitelyPresentedAsAlgebra` on the unital associative algebras and `FinitelyPresented` on modules; `Complete` nested under `OwnedRings.Commutative.Local` so that it means complete as a local ring.

#### `CAT-20`: A Construction on a Category Is Parameterized by It and Declares It

- **Rule**: A category whose objects are objects of `C` with added structure or selected data (`G`-objects of `C`, objects of `C` with a chosen direct-sum decomposition, arrows of `C`, presheaves on `C`) takes `C` as a parameter and declares `C` as its immediate supercategory.  Its instances then reach `C` through it; an instance does not declare `C` a second time.

- **Rationale**: the construction is a functor of `C`, and forgetting the added structure lands in `C` itself.  Declaring `Objects()` instead makes every instance restate the base, and hides that the construction is one thing across all `C`.

- **Violation Example**: `GObjects(G, C) -> Objects()` with `FiniteGSets` declaring `EnumeratedSets` itself and `ModulesOverGroupAlgebra` declaring `AdditiveGroups`; `DirectSumObjects -> Objects()` unparameterized, with `BiproductModules` declaring `Modules` beside it.

- **Correct Example**: `GObjects(G, C) -> C`; `DirectSumObjects(C) -> C` once the specification's spelling admits the parameter.

#### `CAT-21`: A Second Route Between Two Categories Is an Obligation, and a Route Through Different Objects Is Banned

- **Rule**: Before adding a declaration that creates a second path from `C` to some `D`, write down both composites of forgetful functors and why they are the same functor.  If they agree because one is an axiom join Sage computes, the edge is fine.  If they agree because a category on one route is the same category as one on the other, delete the edge: it is a shortcut (`just category-graph shape` lists them) and adds a cycle with no reachability.  If they do not agree, the declaration is false: the two routes send an object to different objects of `D`.

- **Rationale**: Sage resolves a diamond by C3 linearization and never checks that it commutes; the object's inherited operations are whichever route the ordering picked.  A shortcut edge is a redundant assertion; a non-commuting one is a wrong answer waiting for the method that exposes it.

- **Violation Example**: `Ideals -> FractionalIdeals` beside `Ideals -> CommutativeIdeals`, both reaching `ModuleSubobjects`, one as a subobject of `R` and the other of `Frac R`; `AffineSchemes -> Schemes, SeparatedSchemes, QuasiAffineSchemes` when `QuasiAffineSchemes` declares the first two; `OwnedFields -> OwnedIntegralDomains` beside `OwnedPrincipalIdealDomains`.

- **Correct Example**: `AffineSchemes -> QuasiAffineSchemes` alone; `Ideals` retired into `CommutativeIdeals`, with the fractional ideal a functor image; a lattice declaring `FreeFormModules` and the symmetric axiom, both routes to `Modules(R)` being the same forgetful functor through a computed join.

#### `CAT-22`: One Notion Has One Category; a Duplicate Is Retired Into Its Owner

- **Rule**: Before minting a category, search for its owner: `just category-graph by-supercategory` for the parent it would declare, `rg` on the nouns of its definition across `categories/`, and the specification files for the name they use.  A category whose definition matches an existing one is not written; if it already exists, it is retired into the owner, its non-duplicate operations moved to the owner at the weakest sufficient structure (`OWN-18`), and its consumers rewritten.  A name the specification requires survives only as a thin function returning the owner.

- **Rationale**: duplicates arise when a category is minted where a consumer needs it and named from that vantage.  Each duplicate is a second authority for one notion, and the graph then holds diamonds that are the same category twice.

- **Violation Example**: `FormedModules` ("modules with a bilinear form") beside `FormModules`; `InfiniteEnumeratedSets` beside `CountablyInfiniteSets`; `Ideals` beside `CommutativeIdeals`; a `LieAlgebras` class beside the `Lie` axiom on `Algebras`.

- **Correct Example**: `FormModules` with the parent-level `q(v) = b(v, v)` moved onto `BilinearFormModules`; `LieAlgebras` as the name of `Algebras.Lie`; `CountablyInfiniteSets` as the name of the join of `Countable` and `Infinite`.

#### `CAT-23`: Membership Is Placement, Never a Predicate Computed at Runtime

- **Rule**: `x in C` is decided by the category `x` was placed in at construction and by the declared graph.  A `__contains__` that walks a ring's base tower, probes an attribute, or evaluates a property of the candidate is banned: it answers a membership question the graph does not state, and it answers it differently from inheritance.  Where a wider membership is true (a QQ-scheme is a ZZ-scheme), it is reached through the functor of `CAT-16`, not by a predicate.

- **Rationale**: a predicate membership makes `x in C` true while `x` has none of `C`'s operations, so the two meanings of membership diverge exactly where a consumer relies on them agreeing.

- **Violation Example**: `Schemes.__contains__` answering lower-base membership by the candidate ring's base tower; `RepresentedToricSchemes.__contains__` probing `getattr(candidate, "scheme_base_ring", None)`; `QuasiCoherentSheaves.__contains__` duck-typing for want of a placement.

- **Correct Example**: `x in Schemes(R)` true because `x` was constructed in `Schemes(R)` or a declared subcategory; a candidate over a lower base admitted through `base_change_functor`.

#### `CAT-24`: Every Declaration Is an Expression the Reader Can Resolve

- **Rule**: the entries of `super_categories()` and `extra_super_categories()` are category expressions built from names and parameters (`Modules(self.base_ring())`, `Schemes(R).Projective()`), never local variables, `supers + [...]`, `self.base_category().ArrowCategory()`, or anything a reader must execute to learn.  The declared graph is read from source; a declaration only a running session can evaluate is an edge the graph cannot state and the audit cannot check.

- **Rationale**: the audit's "declared from a local expression" list held twenty-six categories whose placement was invisible to every reader and every review.

- **Violation Example**: `algebra = Algebras(...).Associative().Unital(); return [algebra, graded_modules]`; `return supers or [Objects()]`; `return [self.base_category().ArrowCategory()]`.

- **Correct Example**: `return [Algebras(self.base_ring()).Associative().Unital(), GradedModules(self.base_ring(), self.grading_monoid())]`.

#### `CAT-25`: A Declaration Change Is Read on the Graph Before and After

- **Rule**: Any edit to a `super_categories()` or `extra_super_categories()` return, any new category, and any retirement is preceded and followed by `just category-graph shape` and `just category-graph cells`, and the change is judged on their delta: the breadth of the target must not grow, the shortcut list must not gain an entry, the list of generators owing a 2-cell must not gain one that is not a genuine join stated in the commit body, and the largest 2-connected block must not grow.  A grown block is the finding, never a cost to route around.

- **Rationale**: the invariant this architecture asks for, deep and narrow with computed joins, is a property of the whole graph, and every local edge is defensible on its own.  Nobody saw thirty-one declarations into `Sets` or a block of 135 categories until the graph was rendered.

- **Violation Example**: adding a supercategory because the leaf needed a method, without looking at who else declares that target; retiring a class and leaving its consumers to a later reader.

- **Correct Example**: the commit body of a declaration change quotes the before and after of `shape` (declarations, longest chain) and `cells` (H_1 rank, largest block, count owing a cell), and names each edge as shortcut, false, or new-and-immediate.

#### `CAT-26`: A Retirement or Rename Rewrites Its Consumers in the Same Delivery

- **Rule**: When a category is retired into its owner, renamed, or moved between modules, every consumer of the old name is rewritten in the delivery commit: source, the session surface `preamble/all.py` and the package export tables, and every test outside the expectation subtrees (a test's claim is preserved and only its spelling changes; a claim with no surviving spelling is reported, never deleted).  `just preamble-imports` exits zero before the commit.  Notebooks under `computations/notebooks/` are the user's; a notebook that names the old spelling is reported with its cell, not edited.

- **Rationale**: a consumer left behind is invisible while the tree cannot be run, and a lazy export table added so the package still imports hides it indefinitely; on 2026-09-16 the import audit found seventeen such imports, all older than that day, including `DeRhamAlgebra` and `KahlerDifferentials`, names no module had defined for months.  The consumer sweep that followed the axiom passes touched two source files and fourteen test files that the passes had each reported as "outside my tree".

- **Violation Example**: retiring `FormedModules` and leaving five tests importing it; renaming `DeRhamAlgebras` and leaving five modules importing `DeRhamAlgebra`; adding `_EXPORTS` with `__getattr__` so the package imports while a name in the table no longer exists.

- **Correct Example**: the retirement of `Ideals` rewrites `test_fractional_ideals_archive.py` to `CommutativeIdeals(ZZ).extension_to_fraction_field()(I) in FractionalIdeals(ZZ)`, restating the same claim, in the commit that retires the class.

#### `CAT-27`: A Name the Specification Requires Survives as a Thin Function, Never as a Class With a Body

- **Rule**: When a class becomes an axiom category or a join and the expectation files name the class, the name survives as a function of the same parameters returning that category (`def OwnedFields(): return OwnedRings().Division().Commutative()`), or as the axiom class itself under its plural name.  It never survives as a class with its own body, methods, or `super_categories`: a second implementation under the old name is the duplicate `CAT-22` retires.  Operations the retired class owned move to the axiom class at the weakest sufficient structure (`OWN-18`); a join category holds no methods, so an operation a join needs is placed on the nested join class Sage generates or on the data class that consumes the datum.

- **Rationale**: the specification is written blind and its names are the contract; the implementation meets the contract by resolving the name to the right category, not by keeping the old class alive beside the new one.

- **Violation Example**: `OwnedOrders` kept as a class "because a join holds no methods" while also declaring the join, so the name is both the join and a second class over it.

- **Correct Example**: `StrictlyCommutativeDifferentialGradedAlgebras(R)` returning `DifferentialGradedAlgebras(R).Supercommutative().Alternating()`; `PrimeFields` as the plural name of `OwnedRings.Division.Commutative.Prime`.

#### `CAT-28`: An Engine Class Is Not a Category, and It Is Never Removed for Not Being One

- **Rule**: A class that realizes objects -- a condition set driving subsets, the class computing a glued scheme, the groups \(\operatorname{Aut}(L/K)\), a module of global sections, \(L^p\) -- is an engine.  Its objects belong to a category that already exists (`Sets()`, groups, `Schemes(R)`, `Modules(R)`), and the engine is repaired by threading: its objects are constructed by that category's entry (`_object_of(C, **data)` holding the engine privately, or an engine class statically extending `C.ObjectType`), with cooperative `super().__init__`, no non-root `Parent.__init__`, and no side attributes.  The class of objects an engine or a construction produces is a class, never a category: no category is declared for it.  An engine class is never deleted because it is not a category, and a count of classes on `Parent` is never a target.  A new category class carries, in its commit body, a literature definition giving its objects and its morphisms and the `CAT-22` owner search.
- **Rationale**: the category graph states what objects are; an engine states how one object is realized.  Turning an engine into a category makes a realization choice into ontology, and consumers start routing on how an object was built (`CON-16`, `CAT-01`).  Deleting the engine is the same inversion from the other side.
- **Violation Example**: 2026-09-17, converting hand-assembled parents: `ConditionSets`, `ImageSets`, `BlackBoxGroups` (a model of computation), `FiniteExtensionAutomorphismGroups`, `GeneratedSubmonoids`, `PredicateSubmonoids`, `GluedSchemes`, `GlobalSectionModules`, `QuasiCoherentSheavesWithChosenDescentDatum`, `LebesgueSpaces`, `SequenceSpacesOfExponent`, `DifferentiabilityClassesOfOrder`, `FixedSizeSelections`, `CurvesWithChosenNormalization` (a normalization is canonical, never chosen); and, in the other direction, ruling that the engine ring class must go.
- **Correct Example**: categories defined by mathematical data whose morphisms come from morphisms of that data, such as symmetric groups \(\mathrm{Sym}(\Omega)\) on sets, general linear groups \(\mathrm{GL}_n(R)\), and quotients \(F/\langle\!\langle R\rangle\!\rangle\) of free groups, are mathematics and may be owned categories whose levels build their engines privately from the datum; a black-box group, whose datum is an encoding with oracles, is not.  Also: a glued scheme constructed as `_object_of(Schemes(R), scheme_base_ring=R, scheme_engine=_GluedScheme(datum))`; \(\Gamma(X, F)\) a `GeneralModules(A)` module on the set equalizer of the overlap readings; `class _ConditionSet(Sets().ObjectType)` constructed by `X.condition_set(P)`, which computes its placement from the universe.

#### `CAT-02`: Property Categories Do Not Manufacture Chosen Data

- **Rule**: Distinguish a property from a chosen witness of that property.
  A property category such as finitely generated or finitely presented states existence; a data category such as framed or chosen-presentation carries a specified generating morphism or presentation and owns operations that consume that choice.
  A property category never silently computes or selects the witness on demand.

- **Rationale**: Existence of a presentation is weaker than a chosen presentation.
  Conflating them makes algorithms depend on arbitrary hidden choices and incorrectly turns unavailable witness computation into failure of the mathematical property.

- **Violation Example**: `FinitelyPresentedGroups().ObjectType.presenting_free_group()` computing a presentation merely because the group is known finitely presented; asking every finitely generated module for a preferred generating set.

- **Correct Example**: `FinitelyPresentedGroups()` records the property; `GroupsWithChosenFinitePresentation()` carries and exposes the selected presentation.  `FramedModules(R)` carries the chosen epimorphism from a free module, while `FinitelyGeneratedModules(R)` only states existence of some finite framing.

#### `CAT-03`: Constructibility Does Not Require Enumeration or Generators

- **Rule**: A mathematically defined object may be useful and constructible through membership, universal properties, or predicate carve-outs even when no algorithm enumerates it or returns a finite generating set.
  Do not identify "construct the object" with "compute a presentation of all of its elements."

- **Rationale**: Many important objects are first-class long before a full presentation is available.
  Orthogonal groups, stabilizers, centralizers, kernels, and ring centers can support containment, individual elements, morphisms, and further subobjects without globally enumerating generators.

- **Violation Example**: Refusing to provide `O(L)` because the available backend cannot compute generators for an indefinite lattice; replacing it by `None` or by a tuple of known isometries.

- **Correct Example**: Represent `O(L)` as the subgroup of `GL(L)` cut out by the form-preservation predicate, so membership and individual isometries are meaningful; a definite-lattice subcategory may additionally compute a finite generating set.

#### `CAT-04`: Category Placement Is a Mathematical Declaration, Not a Proof-Certificate System

- **Rule**: Category membership is an auditable mathematical declaration enforced by the category's operational contracts and, where appropriate, a participant's named predicate.
  Do not invent proof objects, evidence records, certificate registries, or trust ontologies to justify ordinary category placement.

- **Rationale**: Runtime certificate machinery duplicates the category graph without proving the mathematics it purports to certify.
  The useful contract is the mathematical operation itself: an object claiming a data-bearing category supplies its datum; an object claiming a predicate subcategory supplies the named predicate or algorithm required there.

- **Violation Example**: Introducing `FinitePresentationCertificate`, `ProofOfNondegeneracy`, or an evidence registry that must accompany refinement into the corresponding category.

- **Correct Example**: A finitely generated formed module computes `is_nondegenerate` from the defining correlation when that is decidable; an object whose nondegeneracy is a theorem may explicitly provide the named predicate returning `True`, with the claim visible on the participant and reviewable as mathematics.

#### `CAT-05`: Operations Live on the First Category Where They Are Mathematically Defined

- **Rule**: Put an operation on the appropriate owned `ObjectType`, `ElementType`, Hom-category/arrow type, or functor type of the most general owned category on which the operation is actually defined.
  A more structured subcategory inherits that API and adds only the operations supplied by the additional structure.  Sage method-container classes may realize this privately but are not the public placement vocabulary.
  Do not place an operation on a ubiquitous underlying object and guard it with shape, type, backend, or capability tests when category placement can state the hypothesis.

- **Rationale**: The category graph is the API graph.
  An element should acquire methods because of what mathematical object it is, not because a monolithic implementation class recognizes a special runtime case.
  This also keeps multiple independent refinements composable: algebraic, Lie, scheme, smooth, topological, and arithmetic APIs can coexist on one mathematical object without one implementation pretending to own the others.

- **Violation Example**: A generic tensor element exposes `smith_form()` only when `hasattr(engine_matrix, "smith_form")`; every matrix exposes `determinant()` and raises unless it happens to be square over a commutative ring; `MatrixSpace` always installs Lie methods merely because `m == n`.

- **Correct Example**: Entry access, rows, columns, and transpose live on matrix spaces; square-matrix multiplication lives on square matrix rings; determinant lives where square matrices over commutative scalars have it; Smith normal form is available because the coefficient ring is a PID and its matrix-reduction operation acts on `M_{m,n}(R)`; the commutator bracket is inherited from a suitable associative algebra; scheme/manifold/topological methods come from their respective refinements.

#### `CAT-06`: Structure Induced by Parameters Belongs to the Parameter Categories

- **Rule**: When an operation on a mathematical object exists because one of its parameters has a mathematical property, model that capability on the parameter category and let the object use it; do not manufacture a parallel object category whose only purpose is to restate the parameter hypothesis.
  Shape-dependent structure may refine the object itself when shape changes the operations on its elements, but coefficient-ring properties remain properties of the coefficient ring.

- **Rationale**: `M_{m,n}(R)` is the same kind of matrix space whether or not `R` is a PID.  The PID hypothesis explains why Smith reduction is available; it does not create a new species of matrix.  Conversely, the distinction `m=n` genuinely changes the matrix object's intrinsic multiplication and can justify square-matrix-ring structure.

- **Violation Example**: Introducing `PIDMatrices`, `MatricesOverFields`, `MatricesOverEuclideanDomains`, or similar parallel matrix categories solely so ordinary matrices acquire algorithms implied by the coefficient ring.

- **Correct Example**: `M_{m,n}(R)=Hom_R(F_R([n]),F_R([m]))` remains the same Hom object.  When `R` is a PID, an element `A` presents `coker(A)`; invariant-factor normalization of that presentation yields the Smith diagonal and its source/target basis changes.  When `m=n`, the same object is `End_R(F_R([n]))`, whose multiplication is already composition.

* * *

### 5. Definition Fidelity (`DEF-*`)

#### `CAT-07`: Owned Category Types Supply the Object and Element API

- **Rule**: Operations shared by every element of a mathematical category belong on that category's owned `ElementType`; object-wide constructions belong on its `ObjectType`; arrow operations belong on the element type of the appropriate Hom/arrow category.  Concrete/runtime classes store only representation-specific data/primitives that the categorical API delegates to.

- **Rationale**: The category graph states the mathematics and is therefore the correct place for uniform syntax and operations.  Duplicating scalar multiplication, inversion, bracket, matrix entry, or similar methods on each concrete representation class makes those classes define the theory and causes one representation to miss operations another happens to implement.

- **Violation Example**: Adding Python-literal scalar multiplication separately to presented-module, lattice, tensor-product, and localized-module element classes; putting matrix operations on a backend matrix wrapper instead of the matrix-Hom category.

- **Correct Example**: the `ElementType` supplied by `Modules(R)` carries left scalar syntax through the object's scalar action; the matrix-Hom element type supplies entries/rows/columns; a concrete presented-module runtime element supplies only the representation primitive needed by those owned methods.


#### `DEF-01`: A Predicate's Body Is Its Definition, Not a Recognition Criterion

- **Rule**: Implement a mathematical predicate from its definition, expressed through the owned objects and morphisms that occur in that definition.
  Do not substitute a theorem-equivalent determinant, rank, gcd, coordinate, or matrix criterion as the predicate body merely because it is cheaper in a familiar special case.  Such criteria are permitted **underneath the semantic owner** as implementation cases or cross-check assertions once their hypotheses are explicit; downstream callers never see or repeat them.

- **Rationale**: A recognition criterion used as the public definition carries an unstated theorem and its hypotheses at every call site.
  A semantic definition has one visible proof obligation: that the body spells the definition correctly.  The low-level operations named by that definition may route to theorem-equivalent exact criteria in the represented categories where those theorems apply, so the optimization/theorem is stated once and remains private forever.

- **Violation Example**: `is_nondegenerate()` as `gram.det() != 0`; `is_unimodular()` as `abs(gram.det()) == 1`; `is_primitive()` as a gcd of coordinates; `is_injective()` as a matrix-rank comparison.

- **Correct Example**: Nondegeneracy asks whether the correlation `M -> dual_module(M)` is injective; unimodularity asks whether that correlation is an isomorphism; primitivity asks whether the cokernel of the inclusion is torsion-free; injectivity asks whether the kernel is zero.

#### `DEF-02`: Numerical Data Does Not Replace the Structural Object It Describes

- **Rule**: When a numerical invariant or normal form is derived from a structural object, keep the structural object as the public mathematical result and quarantine the numerical computation behind its owner.
  Do not let a matrix, basis, rank, content, determinant, or invariant-factor tuple stand in for a kernel, cokernel, subobject, quotient, normal form, or morphism.

- **Rationale**: Numerical data often determines the desired object only under additional hypotheses and chosen coordinates.
  Returning the structural object preserves its universal property and lets downstream code compose mathematically instead of re-proving the reconstruction theorem.

- **Violation Example**: Returning kernel basis vectors instead of `ker(f)` with its inclusion; implementing saturation as `Matrix.saturation()`; returning a Smith matrix as "the normalized module."

- **Correct Example**: `f.kernel()` returns the owned kernel subobject; saturation is the kernel of `M -> M/S -> (M/S)/Tor(M/S)`; invariant-factor form returns a new framed module together with the explicit isomorphism from the original.

#### `DEF-03`: Derive Special Cases from the General Construction; Do Not Presume Them

- **Rule**: A constructor or general operation returns the object dictated by its definition and then refines the result when a stronger property is established.
  Do not construct the result directly in a special subcategory merely because current examples usually land there.

- **Rationale**: Presuming the special case turns an accidental property of test data into part of the operation's codomain.
  General construction followed by valid refinement keeps the mathematical codomain correct and lets special algorithms remain available when justified.

- **Violation Example**: Defining every cokernel of a lattice embedding as a torsion module even when the quotient can have positive rank; constructing a quotient as finite because all current fixtures are finite.

- **Correct Example**: Construct the cokernel as a finitely presented module from the presenting morphism, then refine it into the torsion category exactly when its invariant factors establish torsion.

#### `DEF-04`: Matrix Normal Forms Are Presentation Normalizations

- **Rule**: For a matrix representing a morphism of finite free modules, define Smith/invariant-factor normal form through equivalence of the corresponding presentation, not as an unrelated primitive matrix routine.
  Over a PID, `A : R^n -> R^m` presents `coker(A)`; the structure theorem for finitely generated `R`-modules gives an invariant-factor presentation.  The normal-form witness consists of the diagonal presentation together with the source and target basis-change isomorphisms relating it to `A`.
  A backend matrix routine may compute those basis changes privately, but the public mathematical construction is the presentation normalization.

- **Rationale**: The diagonal entries are the invariant factors of the presented module, and left/right multiplication are changes of chosen bases in the two free modules.  Treating Smith form as a standalone array algorithm duplicates the module-classification theorem and disconnects the witness from the cokernel it classifies.

- **Violation Example**: Defining `R.smith_form(A)` as a primitive ring method whose contract is merely whatever triple Sage returns; computing invariant factors separately in the presented-module layer and Smith matrices separately in the tensor layer.

- **Correct Example**: Normalize the presentation `R^n -> R^m -> coker(A)` to its invariant-factor presentation, retaining isomorphisms of the presenting free modules.  `A.smith_form()` is then the coordinate matrix of that normalized presentation together with the coordinate matrices of those basis changes.  If a backend canonicalizes a relation submodule before reduction, its basis change must be included in this presentation isomorphism; it may not be discarded.


#### `DEF-05`: A Normal Form Is a New Object Together With an Isomorphism

- **Rule**: When normalization, reduction, canonicalization, or re-presentation changes chosen framing/presentation data, the result is a new owned object of the same mathematical category together with an explicit isomorphism from the original.  Do not mutate the source into its normal form and do not make the comparison morphism an optional flag.

- **Rationale**: Chosen presentations are structure.  Smith/Hermite/invariant-factor reduction may produce an isomorphic abstract module while changing its framing and relations.  Without the isomorphism there is no mathematical statement connecting the two represented objects, and downstream transported structures have no witness along which to move.

- **Violation Example**: Replace a module's selected presentation with its Smith matrix in place; `normal_form(transformation=False)` returns only the diagonal object; use `normalize=True` to alter constructor semantics without representing the map.

- **Correct Example**: `M.invariant_factor_form()` returns an isomorphism `M -> M_normal`; the matrix normal form is the private/coordinate computation used to construct that arrow.  Normal forms of actual matrix objects may remain matrix operations, while normal forms of framed modules are object-plus-isomorphism constructions.



#### `DEF-06`: Exact Mathematical Questions and Soft Knowledge Questions Have Different Codomains

- **Rule**: Preserve the actual mathematical codomain of an exact operation or predicate.  Do not return `False`, `None`, or `Unknown` merely because the current implementation cannot decide/compute a represented case; use the assertion-gated computational frontier of `CAT-01`.  Separately, an explicitly **soft knowledge/computability predicate** may be designed with a three-valued codomain `True | False | Unknown` when the proposition being returned is itself “what is currently known/computable/available.”

- **Rationale**: “The object is not nondegenerate” and “the current system does not know whether it is nondegenerate” are different statements.  So are “this group is not finitely generated” and “no generating-set algorithm is currently available.”  Collapsing them creates confident mathematical falsehoods; returning `Unknown` from an exact-valued operation changes its mathematics just as badly.

- **Violation Example**: `is_nondegenerate()` returns `False` when no algorithm handles an infinite callable form; `cardinality()` returns `Unknown`; `generators_are_computable()` returns `True` merely because the constructor trusted external input.

- **Correct Example**: `is_nondegenerate()` computes known cases and assertion-gates the current frontier.  A distinct `generators_are_computable()` or `has_computed_group_generators()` may return Sage's `Unknown` when that explicitly three-valued knowledge question has not been decided.


#### `DEF-07`: An Operation's Codomain Is the Union Over Its Implementations

- **Rule**: Before naming the object an operation lands in, read every implementation and take the codomain that covers all of them.  The typical case is not the codomain; it is a specialisation of it.  State the general object, then let the categories that guarantee more say so.

- **Rationale**: An operation is usually written first for the case at hand, so its apparent codomain is the one the author had in view, and the general one is discovered later by a caller who gets a value that does not fit.  `signature_pair` looks \(\mathbb N^2\)-valued from eight of its implementations, and `_ColimitGram` returns `(Infinity, large_negative)`, `(large_positive, Infinity)`, or `(Infinity, Infinity)`.  Its values are therefore extended naturals, and a design that had committed to \(\mathbb N \times \mathbb N\) on the strength of the common case would have had to be undone or, worse, would have pushed the colimit case out of the operation.

- **Violation Example**: choosing a return object from the implementation in front of you; annotating from the first case; a general operation whose type excludes an implementation that already exists in the tree.

- **Correct Example**: reading all implementations first, siting the operation in the object that admits every value they produce, and recovering the finite case as an axiom-gated refinement rather than as the definition.  See `CON-15` for naming the product once the codomain is known.

* * *

#### `CAT-08`: Mathematical Enumeration Is Lazy; Materialization Is Backend-Only

- **Rule**: Mathematical code never replaces an owned set, framing, basis, generating family, index set, group, Hom index, or other mathematical collection by `tuple(...)`, `list(...)`, or another eagerly materialized Python container, even when the collection is known finite.  Consumers iterate the owned collection lazily or use its membership, cardinality, rank/unrank, indexing, finite-support, image, product, or family structure.  Whole-family materialization is permitted only inside a private backend adapter whose external API specifically requires a finite concrete array; that adapter must establish finiteness before serialization and the Python container must not escape it.
- **Rationale**: Finiteness does not turn a mathematical collection into a Python sequence.  Keeping one collection interface for finite and infinite cases prevents downstream code from acquiring accidental `len`, slicing, whole-family traversal, or representation assumptions.  Enumerability, order, cardinality, and finiteness remain mathematical structure; backend arrays are only a final serialization format.
- **Violation Example**: `labels = tuple(M.module_generating_set())` before ordinary module logic, even when `M` is finite; storing `self._generators = list(generators)`; converting a finite index set to a tuple merely to enumerate it twice; checking a callable section by evaluating it at every index; implementing `Sym^n(M)` by first materializing the framing.
- **Correct Example**: Keep `M.module_generating_set()` as the owned ordered/indexed set and iterate it directly.  Use `rank(label)`/`unrank(i)` or finite support when positional access is needed.  A private Sage/GAP/Julia bridge may serialize a mathematically finite ordered set to a Python row/column array immediately before the backend call and discard that array on return.  A finite-presentation algorithm dispatches from `ModulesWithChosenFinitePresentation`, not merely from a weaker existence property.

### 6. Mathematical Vocabulary & Public Types (`LEX-*`)

#### `LEX-01`: Every Public Name and Type Has a Standard Mathematical Referent

- **Rule**: A public name denotes a standard mathematical object, morphism, construction, invariant, property, or chosen structure with its defining data understood from the category.
  Do not mint public wrapper types or names for implementation roles, storage formats, backend distinctions, or local workflow conveniences.

- **Rationale**: A type name is part of the mathematical theory exposed by the repository.
  An implementation-flavored noun creates a parallel ontology that downstream code will start treating as mathematics.

- **Violation Example**: `ExactScalar`, `NativeLattice`, `DiscriminantGroup` as a new type distinct from the finite abelian group underlying a discriminant form, or a wrapper whose only purpose is to package a tuple of constructor arguments.

- **Correct Example**: Use `RingElement`, `RealApproximation`, `FiniteAbelianGroup`, `DiscriminantForm`, `ModuleMorphism`, and the existing categorical constructions whose definitions state the actual mathematics.

#### `LEX-02`: Names State the Structure They Belong To

- **Rule**: When the same noun exists for several structures on one object, the public name states the structure explicitly.
  Use `group_generators`, `module_generators`, `algebra_generators`, `module_generating_set`, and similarly qualified dual or action names.
  Do not keep a bare ambiguous name as a compatibility alias underneath the precise one.
  When one predicate name is true of an object under two of its structures -- `is_framed` on a framed module that is also a framed algebra -- qualify both (`is_framed_module`, `is_framed_algebra`); never resolve the collision by deleting one in favour of category membership, and never by surveying Sage, which has no such notion: this rule is the standard.

- **Rationale**: An algebra can simultaneously have group, module, and algebra generators; an object can carry several dualities.
  A bare `generators()` or `dual()` therefore has no stable mathematical referent even when today's concrete class happens to have only one candidate.

- **Violation Example**: `generators()`, `gens()`, `generating_set()`, or `dual()` on an owned multi-structured object; `module_generators()` implemented as a delegation to the still-public ambiguous `generators()`.

- **Correct Example**: The module framing exposes `module_generating_set()` and `module_generator(label)`; a group exposes `group_generators()`; metric, module, and group dualities have distinct names tied to the functors that produce them.

#### `LEX-03`: Exact Mathematics Is the Default; Approximation Carries the Adjective

- **Rule**: Public mathematical nouns denote exact objects unless approximation is explicitly part of the type or operation name.
  Approximate numerical representations are extracted at plotting, display, numerical-analysis, or other explicitly approximate boundaries.

- **Rationale**: Marking the exact case as exceptional reverses the mathematical default and can make exact objects such as algebraic or symbolic reals impossible to state.

- **Violation Example**: Using `RealNumber` to mean an MPFR approximation while exact `sqrt(2)` needs a separate exceptional type; a public `ExactScalar = Integer | Rational` union that describes implementation classes rather than the mathematical field `QQ`.

- **Correct Example**: `RealNumber` denotes an exact real in the repository's mathematical vocabulary where represented; `RealApproximation` or an explicitly precision-bearing operation denotes an MPFR approximation.


#### `LEX-04`: Software Roles Do Not Define Mathematical Ontology

- **Rule**: Interpret fields, accessors, aliases, wrappers, helper classes, registries, and implementation edges by the mathematics they denote, not by their software role.  Public mathematical nouns must be standard mathematical objects/data whenever such a referent exists.  Do not create an epistemic or administrative vocabulary (`knowledge`, `evidence`, `provider`, `manager`, `context`, `metadata`, `model`, `descriptor`, `record`, `info`, `result`, `factory`, `payload`, `adapter`, `backend`) to stand in for morphisms, functors, bases, sections, predicates, isomorphisms, or other standard data.

- **Rationale**: Code is one presentation of mathematics.  Treating declaration shape as ontology causes real mathematical content to be demoted to “plumbing” and then replaced by project-private concepts.  That private vocabulary expands rapidly because every later operation has to translate between it and the actual mathematical objects.

- **Violation Example**: `SubobjectEvidence` containing an inclusion; `GeneratorProvider` containing an indexed family; `NormalizationContext` containing an isomorphism; dismissing a local functor as a mere “realization edge” because it is stored in a helper field.

- **Correct Example**: Name the inclusion morphism, indexed family, isomorphism, or functor directly.  An engineering cache/adapter may have engineering vocabulary privately, but the mathematical layer exposes the standard object it implements.



#### `LEX-05`: Standard Mathematical Vocabulary Outranks Backend Vocabulary

- **Rule**: Public names follow the standard terminology of the mathematical literature and the repository's mathematical lexicon, even when Sage or another backend uses a different historical spelling.  Backend class/method names are preserved only inside backend calls and adapters; they do not determine the owned public noun or verb.

- **Rationale**: The preamble is a mathematical language, not a compatibility facade.  Importing backend terminology into the public API imports its historical conventions, implementation distinctions, and sometimes mathematically misleading names.  Standard vocabulary makes the same concept recognizable independently of the current engine.

- **Violation Example**: Call invariant factors merely `invariants` because Sage does; expose an FGP/backend class name as a mathematical category; retain an implementation-specific normal-form name for the object rather than the literature's object/invariant.

- **Correct Example**: Use `invariant_factors`, standard signature terminology, standard dual/functor names, and ordinary categorical nouns.  Private adapters may call Sage's `.invariants()`, `.gens()`, or exact backend class names while converting the result back into owned vocabulary.



#### `LEX-06`: Processes and Named Examples Do Not Become Mathematical Kinds

- **Rule**: A public type/category/constructor name must denote a reusable mathematical concept, not the process by which an ordinary object was generated or its role in a test/example.  Randomness, fixture/example status, “standard test object”, and similar modifiers generate/select data for existing constructors.  A named specimen may live in a catalogue without becoming a new category-level concept.

- **Rationale**: Reifying process labels produces artificial `Random*`, `Example*`, `Test*`, `Factory*` ontologies and then forces routing, methods, and documentation to distinguish objects that are mathematically just ordinary members of an existing category.

- **Violation Example**: `RandomLattices`, `RandomLatticeOfSignature`, `ExampleModule`, or a category API obligation for a local `rankTwo` example.

- **Correct Example**: `random_gram(...)` produces legitimate construction data and the ordinary lattice constructor consumes it; named objects such as `E8` live as catalogue specimens constructed by the same public lattice language.



#### `LEX-07`: Public Mathematical Names Never Encode the Current Algorithm or Computability Frontier

- **Rule**: Name a public operation by the mathematical concept it denotes.  Words describing the present decision procedure, engine, performance profile, or implementation branch—`partial`, `fast`, `cached`, `sage`, `gap`, `brute`, `PDOnly`, theorem-name-as-algorithm-adjective, etc.—belong in implementation notes/private adapters, not in the mathematical noun/verb.

- **Rationale**: The mathematical predicate stays the same as algorithms improve.  Encoding today's route in the name freezes a temporary computational boundary into the ontology and invites duplicate methods when a second algorithm arrives.

- **Violation Example**: `eichler_partial_is_isometric`, `sage_computable_genus`, `fast_kernel`, `cached_discriminant_group` as public mathematical operations.

- **Correct Example**: `is_isometric`, `genus`, `kernel`, `discriminant_group`; their implementations route among exact algorithms and assertion-gate the current frontier as needed.  The docstring/private implementation records which theorem/backend handles each case.

#### `LEX-08`: Distinguish a Mathematical Construction From the Numerical Operation Representing It

- **Rule**: When a numerical operation is the coordinate representation of a mathematical construction, name each at its own level.  In particular, matrices have a **Kronecker product**; linear maps/modules have tensor products.  Similar distinctions apply to Gram matrices versus forms, Smith matrices versus invariant-factor presentations, and coordinate vectors versus elements.

- **Rationale**: Reusing the mathematical noun for its representation makes callers reason about arrays as if they satisfied the universal property themselves and obscures where basis choices entered.

- **Violation Example**: “tensor product of two matrices”; “the Smith form of the module” when referring to the backend matrix; “the vector is primitive because its coordinate gcd is one.”

- **Correct Example**: the tensor product of morphisms has a Kronecker matrix in chosen bases; Smith normal form is the matrix computation producing an invariant-factor re-presentation; primitivity is the cokernel torsion-freeness predicate.



#### `LEX-09`: Public Category Names Are Standard Names for Identities, Not Substitutes for Their Definitions

- **Rule**: Use the standard plural/category notation when established, but retain the underlying owned construction/classifier expression as the mathematical definition.  Project/Sage aliases are metadata/presentations on that identity, never extra categories whose existence must be reconciled later.

- **Rationale**: Good names make the interactive language readable; definitions make the graph coherent.  Treating either as the other yields the two bad extremes: unreadable classifier-only APIs or a forest of independently named categories with duplicated semantics.

- **Violation Example**: expose only `Magmas.Associative.Unital.Inverse` when `Groups` is the established mathematical noun; or create `Groups` as a separate wrapper category around that classifier expression.

- **Correct Example**: `Groups` is the standard public name of the one owned category whose definition is the corresponding classifier/category expression; aliases and backend names resolve to that identity.


#### `LEX-10`: Every Generator, Dual and Basis Names Its Structure -- and No Alias Omits It

- **Rule**: Public accessors for generated or derived structure state which structure they mean: `module_generators`, `group_generators`, `algebra_generators`, `ideal_generators`, `monoid_generators`, `dual_module`, `dual_lattice`, `dual_group`.  A bare `gens`, `generators`, `dual`, `basis` or `ngens` is not a public method, **and not a permitted alias for one**.

- **Rationale**: Every object here sits in several categories at once, so an unqualified request names no operation.  `ZZ` is at once a ring, a rank-one \(\mathbb Z\)-module, a rank-one \(\mathbb Z\)-algebra, a group and a monoid; its module generators are \(\{1\}\) and its multiplicative monoid generators are the primes together with \(-1\).  An ideal of \(R\) is both an ideal and an \(R\)-submodule of \(R\), with different generating sets.  The question has no answer until the structure is named.  An alias is worse than a bad name: it makes an ill-posed question answerable, and whatever it returns is a silent choice of one structure among several, made by the implementer and invisible at the call site.  Sage can afford `gens()` because a Sage object usually has one privileged structure baked into its class; the preamble cannot, because multi-category placement is the design.

- **Violation Example**: `gens = ideal_generators` or `generators = gens` on an owned class; `def basis(self)` on an object that is a module and a formed module at once; a caller reaching for `.gens()` because the class offers it.

- **Correct Example**: `ideal_generators()` as the only accessor, with callers renamed; Sage's `.gens()` retained only on an engine handle inside a private adapter, where the receiver is a Sage object with one structure.

#### `LEX-11`: One Name, One Operation -- a Different Codomain Is a Different Operation

- **Rule**: Every definition sharing a name implements the **same** operation: the same mathematical question, answered in the same codomain.  Specialisation is welcome -- a concrete representation may answer faster, and a category may answer generically -- but a definition that lands somewhere else is not an override of that operation, it is a different operation, and it takes its own name.  When adding a definition of an existing name, read the others and confirm the codomain agrees.

- **Rationale**: Overriding is how specialisation is supposed to look here, so a long list of definitions is not itself a smell and the real defect hides among them.  `signature_pair` had ten definitions: six per-Gram shortcuts, a category-level owner, a stored value on a genus -- all returning a pair -- and one on `CoxeterDiagram` returning `(positive, negative, zero)`, the inertia including the degenerate part.  Nine implementations of one operation and one of another, indistinguishable at every call site, and a rename or a return-type change applied across the name would silently corrupt the tenth.  The shared name also concealed that the two answers live in different objects, \(\mathbb N^2\) against \(\mathbb N^3\), which is the same defect `CON-15` names from the other side.

- **Diagnostic**: count the definitions of a name and compare their codomains before touching any of them.  Divergence in arity, in value type, or in what the answer is *of* means the name covers more than one operation.

- **Violation Example**: `signature_pair` returning a pair on nine owners and a triple on a tenth; a predicate that answers `bool` on one class and a three-valued unknown on another; an accessor returning an element on one owner and a family on another.

- **Correct Example**: the inertia named as the inertia, distinct from the signature pair; `tensor_valence`, whose four definitions are a contract, a computation, a delegation and a constant, all answering the same question in the same place.

#### `LEX-12`: An Annotation Names the Codomain, and Its Reader Is a Mathematician

- **Rule**: A return annotation states **which mathematical object the value belongs to**, so that a reader can check the method against the definition it implements without executing anything.  Write the annotation for that reader first.  Whether a checker accepts it is a second, weaker requirement, and an annotation chosen to satisfy the checker rather than the reader has been chosen against its purpose.

- **Rationale**: In this repository the type surface is a mathematical claim: `-> tuple[int, int]` on a valence says the answer is a pair of integers, and a mathematician auditing the method compares that claim with the definition of the operation.  Optimising instead for "will this typecheck" reliably produces the annotations that convey least, because the easiest way to be accepted is to say nothing.  The checker is a machine that will accept the empty statement; the reader is the one who can tell that the empty statement is empty.

- **Violation Example**: choosing an annotation by trying candidates until the checker stops complaining; annotating a mathematical operation with the most general thing that fits; leaving the signature uninformative because the body is short and "obvious".

- **Correct Example**: an annotation a mathematician can read off against the operation's stated codomain, and which they would notice was wrong if the operation changed.

#### `LEX-13`: A Type That Excludes Nothing Asserts Nothing

- **Rule**: Before writing an annotation, answer: **which wrong implementation does this reject?**  If no plausible wrong return is excluded, the annotation is empty and does not count as typed.  `object`, `Any`, and framework universals used as returns -- `Element`, `Parent`, `SageObject`, `CategoryObject` -- are all in this class.

- **Rationale**: `object` is banned because a function annotated with it "passes on literally anything, which means it asserts nothing".  A framework universal fails the same test and hides it better.  Every element of every parent in Sage is an `Element`: an integer, a matrix, a polynomial, a group automorphism, a scheme point, a lattice vector.  So `-> Element` admits every value the preamble produces, catches no wrong return ever, and reads to a reviewer like a real type.  The class-tree ancestry is irrelevant; the discrimination is what matters, and there is none.

- **Violation Example**: `-> Element`, `-> Parent`, `-> SageObject` on a mathematical operation; a union so wide that every plausible return satisfies it; a bound so loose that the checker could not fail.

- **Correct Example**: an annotation naming the codomain, or -- where that is not yet expressible -- the named alias of `LEX-15`, which is honest about asserting nothing instead of disguising it.

#### `LEX-14`: Do Not Annotate From the Framework's Class Tree

- **Rule**: When the mathematical type is hard to name, do not walk up the implementation's class hierarchy until something fits.  Sage's class tree is a taxonomy of *representation*; a return annotation is a claim about a *codomain*.  The two are different questions, and an answer to the first is not an answer to the second.

- **Rationale**: This is the characteristic engineering-brained substitution, and it feels like diligence because the result is a real class that really is an ancestor.  But `Element` records that the value participates in Sage's coercion system, which is an implementation fact true of everything, while the question was which object the value is a point of.  The obstacle that prompts the walk -- "the parent is constructed at runtime, so there is no static name" -- is an implementation obstacle, and the mathematics does not move to accommodate one.  A codomain that cannot be named statically is a finding about the type surface, never a licence to write the universal base class.

- **Violation Example**: reaching for `Element` because the concrete element class is generated at runtime; annotating with a Sage abstract base because it is the nearest common ancestor of the observed returns; picking the ancestor that makes `mypy` quiet.

- **Correct Example**: naming the mathematical object -- the product, the homset, the module -- and, where the static surface cannot yet express it, recording that as a gap under `LEX-15` rather than papering it with an ancestor.

#### `LEX-15`: An Inexpressible Mathematical Type Aliases `Any` Once, Under Its Own Name

- **Rule**: When a value's mathematical type is known but not yet statically expressible, declare **one** alias in the central typing layer, named for the mathematics and carrying a comment stating what it stands for, and use that name in every signature:

  ```python
  # (n_1, ..., n_k) in the product monoid NN^k
  ProductOfNaturalNumbers = Any
  ```

  Never inline `Any` at the signature, never substitute a framework universal, and never leave the annotation off.

- **Rationale**: The alias and the base class both check nothing, so the alias costs nothing the universal was buying -- and on every other axis it dominates.  It names the codomain, so the reader learns it.  It is falsifiable by a human: change the return to a triple or to a pair of rationals and the name is visibly wrong in review, where `Element` could never become wrong and so could never flag anything.  It quarantines the ignorance to one site, which is what this repository already requires of a genuine `Any`.  It provides a single upgrade point, so that when the type becomes expressible one line improves every signature at once, instead of a hunt in which each site's intent must be re-derived because the annotation destroyed it.  And it makes the gap countable: `grep ProductOfNaturalNumbers` measures exactly how much of the surface is deficient and where, while a base class is indistinguishable from correct code and so cannot be paid down deliberately.

  This is not the invention `LEX-10` bans.  That prohibition is on minting a name to satisfy a rule -- `MyCustomClassCreationDatum` -- which has no referent.  `ProductOfNaturalNumbers` denotes \(\mathbb N^k\), which a mathematician recognises.  Naming real mathematics is the welcome case even when the name is currently an alias.

  The trade is explicit and correct: it costs minting one name, it buys zero code guarantees, and it buys mathematical expressiveness.  Do not weigh the zero guarantees against the cost -- the guarantees were never available at that site, and expressiveness is what is being purchased.  What the name additionally buys is set out in `LEX-17` and `LEX-18`: the alias is not a placeholder waiting to be tidied but a staging ground for a refinement whose errors are its yield.

- **Violation Example**: `-> Any` written at the signature; a different ad-hoc alias per file; an alias named for its representation (`IntPair`) rather than its mathematics; an alias with no comment saying what it stands for.

- **Correct Example**: one aliased name per mathematical notion, in the central layer, with its comment; every site using it; the alias replaced by the real type in a single edit when the surface grows to carry it.

#### `LEX-16`: An Annotation Falsified by a Change Is Corrected, Never Deleted

- **Rule**: When a change makes an existing annotation false, correct it to the new codomain.  Deleting it, widening it to a universal, or replacing it with `Any` are all prohibited, and deleting is the worst of the three because it leaves no trace that a claim was ever made.

- **Rationale**: A falsified annotation is a signal that the change is incomplete -- it is the type surface reporting that the codomain moved -- and the three prohibited responses all discard the signal instead of acting on it.  `AGENTS.md` names deleted annotations alongside `Any` and `# type: ignore` for exactly this reason.  A false annotation is at least a falsifiable claim that review can catch; an absent one asserts nothing and looks deliberate.  The observed sequence, which is the one to recognise: a correct annotation, made false by an edit, deleted to make the edit go through, then replaced with a base class to look typed again -- three moves, each worse than the last, two of them explicitly banned.

- **Violation Example**: removing `-> tuple[int, int]` because the return became an owned element; changing it to `-> Any` or `-> Element` for the same reason; leaving the old annotation in place and false.

- **Correct Example**: the annotation updated to name the new codomain in the same edit that changes the return, or the `LEX-15` alias introduced if that codomain is not yet expressible.

#### `LEX-17`: The Central Typing Layer Is an Independently Auditable Artifact

- **Rule**: The typing layer is reviewed, refined and improved **on its own schedule**, as an object of study separate from any call site.  An audit of it asks a mathematical question -- does this name admit a sharper referent than it currently carries -- and answering that question is ordinary maintenance, not a change to the code that uses it.  A `LEX-15` alias is deliberately left in place until such an audit refines it; it is not debt awaiting cleanup.

- **Rationale**: Once the mathematics is named in one place, the collection of names becomes a readable account of what the repository believes its objects are, and it can be improved by reading it alone.  `ProductOfNaturalNumbers` can be recognised as admitting a much better refinement without opening a single consumer, because the name already states the intent that the refinement must respect.  This is only possible when the ignorance was localised: inlined `Any`, ad-hoc per-file aliases, and framework universals leave nothing to audit, since each site must first be reverse-engineered to learn what it meant.

- **Violation Example**: treating the alias file as scaffolding to be minimised; refining a type only when a call site forces it; discovering the intent of a site by reading its body because its annotation records none.

- **Correct Example**: a scheduled read of the typing layer that proposes refinements from the names alone; an alias that survives several releases because no sharper referent has yet been established, and is none the worse for it.

#### `LEX-18`: Narrowing a Type Is a Designed Experiment; Its Errors Are the Result

- **Rule**: When a `LEX-15` alias is refined to a real type, the errors that appear are the **output of the experiment**, not damage to be minimised.  Read every one before changing anything.  Suppressing them, widening the refinement to make them stop, or reverting the narrowing discards the result.

- **Rationale**: Because every consumer already declared its intent by using the name, the checker is doing two things at once when the name narrows: it is checking the new definition, and it is checking each site's declared intent against that definition.  Each error is therefore a specific disagreement between a usage and the refinement, and lights up the complete census of consumers at once.  Three kinds of finding come out of it, and each is worth more than the narrowing itself:

  - a call site needs an operation the refined type does not offer, which names a **missing API** and is a gap discovered rather than guessed;
  - a call site uses less structure than the refinement supplies, which distinguishes the sites needing only the **set** structure from those needing the **monoid** structure -- a mathematical distinction across the corpus that no reading of individual files would surface;
  - a call site is simply wrong, and was wrong before, invisibly.

  A narrowing that produces no errors has told you something too, but a narrowing whose errors are suppressed has told you nothing and cost the opportunity.

- **Violation Example**: narrowing an alias and immediately loosening it until the suite is quiet; adding `# type: ignore` at the sites that failed; treating the error count as the cost of the change rather than as its findings.

- **Correct Example**: narrowing, then reading the errors as a census -- these sites want an operation we do not have, these sites only ever needed the underlying set, this one is a real defect -- and letting that reading determine what changes, including possibly the refinement itself.

#### `LEX-19`: Accumulated Usage Is Evidence for the Theorem

- **Rule**: Treat the corpus of call sites of a named mathematical type as **evidence about what the operation actually is**, and consult it when deciding the operation's real definition.  The code is a place to reason about and experiment with a proposed mathematical statement before committing to it.

- **Rationale**: A named type accumulates, at every call site, a record of what consumers needed from the object.  That record answers questions a definition alone cannot settle.  If one later wants to define a valence as an honest morphism into a monoid, or into a product of monoids, the usages say whether the monoid structure is ever used, whether anything relies on more than the underlying set, and whether the proposed morphism would in fact be natural in the ways the callers assume.  A refinement can then be tried against the corpus and the outcome read off, so the theorem is developed with evidence instead of asserted and patched afterwards.

- **Violation Example**: settling an operation's definition from one implementation and one caller; proposing a structural refinement without checking which structure the existing sites use; treating call sites purely as work to update rather than as data about the notion.

- **Correct Example**: before promoting a valence to a morphism of monoids, reading its sites to see which of them use addition of valences at all, and letting the answer decide whether the monoid structure belongs in the definition or is being imported for tidiness.

* * *

### 7. Sets, Collections & Cardinality (`SET-*`)

#### `SET-01`: Mathematical Collections Are Owned Sets or Families, Never Python Sequences

- **Rule**: Every mathematical collection inside the preamble—not only a public return value—is represented by its mathematical collection object: set, ordered set, multiset, ordered multiset, indexed family, image, product, coproduct, or another named construction.  Raw Python `list` and `tuple` are not mathematical storage types.  They may appear only as transient serialization at a private backend boundary after finiteness and ordering have already been established mathematically.

- **Rationale**: The mathematical collection determines equality, multiplicity, order, membership, cardinality, ranking/unranking, and available morphisms.  A Python sequence silently supplies finiteness and eager materialization.  Once a mathematical family is stored as a sequence, every downstream consumer is encouraged to use `len`, indexing, slicing, and whole-family traversal even when the same construction should work for an infinite ordered/indexed set.

- **Violation Example**: `self._generators = tuple(generators)`; `labels = list(M.module_generating_set())`; `module_generators() -> tuple[...]`; returning a list of subgroup representatives; converting an index set to a tuple merely to enumerate it twice; widening an input type to `Sequence` because callers pass lists.

- **Correct Example**: A generating family is an owned ordered/indexed set with `__iter__`, membership, cardinality, and when appropriate `rank`/`unrank`; repeated framing images form an indexed family over the framing set; conjugacy representatives form an owned set.  Consumers iterate lazily.  A private CAS adapter may finally serialize a *known finite* ordered set to the row/column array demanded by that backend, and that sequence does not escape the adapter.

#### `SET-02`: Cardinality and Order Are Cardinal-Valued; Finiteness Is Never Smuggled in by `len`

- **Rule**: Cardinality, group order, and element order use the repository's mathematical cardinal/integer objects appropriate to their definitions and do not silently assume finiteness.
  Use `cardinality()` for mathematical sets; use sequence length only for a private implementation container already known to be finite.

- **Rationale**: `len` is a programming operation with a finite machine-integer result.
  Treating it as cardinality makes infinite ordinary inputs unanswerable or converts a missing enumeration algorithm into a false mathematical finiteness claim.

- **Violation Example**: `order() -> int: return len(elements)`; raising from `cardinality()` merely because a module has positive rank; refusing to state the cardinality of a finitely generated infinite group because only finite groups are enumerable by the current engine.

- **Correct Example**: A finite free module over `F_q` has cardinality `q^n`; a finitely generated infinite group has countable underlying set when that theorem applies; an unknown cardinality is represented as unknown rather than forced through `len`.

#### `SET-03`: Set-Level Operations Are Owned Once by Sets and Standard Constructions

- **Rule**: Cardinality, finiteness, countability, membership, enumeration, products, coproducts, and other generic set operations live at the owned set layer or the standard construction that first has enough data to implement them.
  Structured descendants obtain those operations through their canonical forgetful/construction path rather than reimplementing the same set theory at every leaf.

- **Rationale**: A lattice, module, algebra, or group has an underlying set; it does not acquire a second definition of cardinality because it has extra structure.
  Centralizing set behavior prevents coordinate models and leaf-specific enumerators from becoming alternate definitions of the underlying set.

- **Violation Example**: A lattice-specific `cardinality()` multiplying invariant factors directly while the underlying finite group already owns cardinality; a module-level iterator returning coordinate tuples instead of module elements because a basis is available.

- **Correct Example**: A discriminant form inherits cardinality from its underlying finite abelian group; a chosen basis may supply an isomorphism with a coordinate product for computation, but iteration crosses back through the inverse and returns elements of the owned module.

#### `SET-04`: Finite Support Does Not Imply a Finite Underlying Family

- **Rule**: Distinguish an element having finite support from its parent/indexing set being finite.  Free modules, formal divisor groups, group/algebra monoid rings, sparse polynomial-like objects, and indexed sums may be built on infinite owned sets while each represented element uses only finitely many indices.  Do not coerce the whole indexing family to a finite ordered set merely because the current element or backend input is finite.

- **Rationale**: Conflating finite support with finite parent data is one of the main ways finitary assumptions spread through the API.  The correct abstraction keeps the parent infinite/lazy and lets each element expose its finite support.

- **Violation Example**: Defining the group of formal divisors by `finite_ordered_set(prime_divisors)`; materializing every module generator before forming a sparse linear combination; requiring a group ring's entire group to be enumerable in order to represent one finite group-ring element.

- **Correct Example**: `FormalDivisorGroup(R,S)` is the free `R`-module on the owned set `S`; a divisor is a finite-support coefficient map on `S`.  Algorithms consume only that support unless their theorem genuinely requires a finite parent.


#### `SET-05`: The Set API Is Closed Under Standard Set Constructions and Canonical Identifications

- **Rule**: Every owned object that is mathematically a set—ordinary sets, exponentials/function sets, Set-Homs, power sets, Cartesian products, coproducts, images, subobjects, and similar constructions—participates in the same owned set API.  Canonically identical set constructions are represented by one parent/object, not parallel implementations reached through different notation.

- **Rationale**: Set-level operations such as membership, cardinality, enumeration, indexing, maps, products, and coproducts should propagate through the standard construction graph.  If `Hom_Set(X,Y)` and `Y^X` are implemented separately, each acquires its own cardinality/enumeration/equality behavior and the architecture immediately forks.

- **Violation Example**: Maintain an independent power-set implementation beside exponentials; make Set-Homs a Homset object that does not receive ordinary set methods; compute function-set cardinality separately from Set-Hom cardinality.

- **Correct Example**: Own the canonical identifications `Hom_Set(X,Y)=Y^X` and `P(X)=2^X`; the one resulting parent has both Hom/exponential placements and inherits the complete set interface.  Cartesian products/coproducts likewise own their standard projections/injections and cardinal arithmetic at the set-construction level.



* * *

### 8. Computational Backend Delegation (`ENG-*`)

#### `ENG-01`: Delegate Heavy Algorithmic Computations to Exact Engines

- **Rule**: Route algorithmic algebra to established exact backends (SageMath, Singular, OSCAR, Macaulay2, PARI/GP) when a reliable implementation exists.

- **Scope**: Gröbner bases, syzygies, primary decompositions, Hilbert series, polynomial reduction, and local algebra computations.

- **Rationale**: Battle-tested engines provide numerical stability, optimized C/C++ implementations, and mathematical verification.

- **Violation Example**: Writing custom Python algorithms for multivariate polynomial division or Gröbner basis calculation.

#### `ENG-02`: Prohibition of Hand-Rolled Standard Mathematics

- **Rule**: Do not hand-roll algorithms or data structures available in mature upstream dependencies or Mathlib.

- **Rationale**: Custom mathematical algorithms create high maintenance overhead and lack formal verification.

- **Violation Example**: Implementing custom Smith Normal Form or LLL reduction instead of delegating to native library routines.

#### `ENG-03`: Minimal Owned Computation and Ecosystem Offloading

- **Rule**: Keep owned algorithmic logic strictly minimal.
  Always offload engine computations to established computational backends:

  - Upstream SageMath native modules

  - Heavy Python libraries (`networkx`, `numpy`, `scipy`)

  - Julia / OSCAR / Hecke (routed via `sage_julia_bridge`)

  - GAP (routed via `libgap`)

  - Singular, Macaulay2, Maxima, and PARI/GP

- **Rationale**: The preamble owns categorical representations, universal properties, and mathematical structures.
  Concrete computations belong to dedicated, verified engines.

- **Violation Example**: Writing custom graph connectivity or automorphism algorithms instead of delegating to `networkx` or Sage graph backends.

#### `ENG-04`: Native Engine Implementation with Preamble Category Wrappers

- **Rule**: When an algorithm requires multi-step engine computations, implement the engine logic directly in the target engine language (such as Julia/OSCAR or Singular) and wrap it with preamble category interfaces, whenever this reduces complexity or eliminates excessive cross-bridge data transport.
  First apply `OWN-08`: use an existing suitable high-level engine operation.
  Native engine glue composes maintained operations; writing a replacement
  algorithm in the engine's language still requires the `ENG-06` ownership decision.
  The Python mathematical layer should prepare the owned mathematical input, cross once into the engine routine, and reconstruct the owned mathematical output; it should not become a line-by-line orchestration language for the engine's matrices, syzygies, lifts, or stabilizer workspaces.

- **Rationale**: Executes compute-heavy algebra natively in the host engine while exposing a uniform categorical interface to Sage sessions.
  A long Python routine whose dominant content is translating and reshaping intermediate engine objects is backend code in the wrong language and location.

- **Violation Example**: Transporting intermediate matrices back and forth across a language bridge in a loop when one native Julia routine can perform the reduction and return the final invariant; a hundreds-of-lines Python kernel routine manually building Singular augmented matrices, calling `syz` twice, reshaping every intermediate result, and calling `lift` before finally reconstructing the owned kernel.

- **Correct Example**: Pass the finite presentation and morphism data through one private Singular adapter whose native routine computes kernel generators, their relations, and lift data; cross back once and construct the owned presented kernel together with its inclusion and lifting morphism.

#### `ENG-05`: Rank Architectures by Human-Owned Complexity and Change Blast Radius, Not Dependency Weight

- **Rule**: Do not count an ordinary external dependency, build toolchain, package scaffold, or install step as an architectural disadvantage by itself.  When choosing between mature reusable infrastructure and a local implementation, compare the amount/scrutability of logic humans in this project must own, the future edit/review blast radius, and whether understanding is centralized for reuse rather than reimplemented by each consumer.

- **Rationale**: Most substrate complexity is shifted rather than eliminated.  Avoiding one dependency by writing a parser, graph algorithm, dispatcher, traversal, or algebra engine locally transfers the same conceptual cost into bespoke code that this project must reason about indefinitely and often multiplies it across consumers.

- **Violation Example**: reject a maintained tree-sitter grammar because it adds a C/build dependency and instead maintain handwritten parsing logic; avoid `networkx` to save a package while owning DFS/SCC/toposort implementations; avoid a mature dispatch library and accumulate hand-written case registries.

- **Correct Example**: prefer the dependency when it centralizes the generic problem and leaves the preamble owning only its mathematical semantics/adaptation.  Reject a dependency for semantic mismatch, correctness, maintenance/reliability, or inability to satisfy the owned boundary—not merely because it exists.



#### `ENG-06`: A New Nontrivial Mathematical Algorithm Requires a Demonstrated Backend Gap

- **Rule**: Before the preamble owns a new nontrivial mathematical algorithm, search the repository's backend/capability references and the relevant mature open-source systems for the semantic operation.  If a suitable exact implementation exists, wire it behind the owned mathematical method.  Bespoke implementation is justified only after the relevant alternatives have been checked and a real semantic/capability gap is established; if owning the algorithm materially expands the project's correctness burden, it requires an explicit project/user decision rather than an agent convenience choice.

- **Rationale**: The preamble should own the mathematical ontology and thin semantic routing, not duplicate decades of exact algebra/group/geometry algorithms.  LLMs readily write plausible local algorithms because doing so completes the immediate method; that silently transfers correctness, performance, and edge-case responsibility into this repository.

- **Violation Example**: implement local orbit/stabilizer enumeration without checking GAP; write polynomial syzygy/Groebner logic instead of Singular; implement lattice/form equivalence from scratch while Oscar/Hecke/Indefinite.jl/Sage already provide an exact route.

- **Correct Example**: identify the owned operation first, inspect the capability map/upstream documentation, add the narrow backend crossing, and return the owned result.  If no mature implementation actually exists, record that concrete gap and only then design the smallest source-grounded algorithm the project deliberately chooses to own.

#### `ENG-07`: Friction With the Engine Is the Datum; It Is Never Routed Around

- **Rule**: When a Sage route is slow, rejects an input, or returns a result of the wrong shape, the task changes at that point.  Before any other edit: isolate the engine from the preamble on a specimen of the same order and shape; measure the cost as wall time against the size parameter, at more than one size; search inside Sage for the alternate route (the method's `algorithm=` choices, a backend Sage ships reached through Sage's own interface, a different constructor, a sibling module), reading the source; and record what was found under `DEV-63`.  Only then choose the route the owned name delegates to.  Replacing the library, hand-rolling the routine, adding a cache, or deleting the call that exposed the cost before that record exists is banned, whatever the size of the tool and whether or not the code is preamble mathematics.

- **Rationale**: A gap in Sage has three kinds, absent, present and wrong, and present but unaffordable, and the owned name exists to absorb whichever one is found.  The measurement is the admission ticket: `ENG-06` lets the preamble own an algorithm only on a demonstrated gap, so discarding the measurement forecloses the one route by which the project could ever legitimately take the computation on.  The finding is also the most durable thing the task can produce: it does not expire, it does not depend on the state of the tree, and it costs a researcher's afternoon to rediscover every time it is lost.  See *The artifacts are instruments; the product is a map of Sage* under the design philosophy.

- **Observed**: the declared-category-graph tool, 2026-09-16.  The first version hand-rolled a spanning forest and a cycle basis where `Graph.minimum_cycle_basis` exists; the second, on a speed complaint, replaced Sage's graph library with `networkx`.  Neither examined the Sage routine.  The result was zero knowledge of `Graph.minimum_cycle_basis`, `longest_path`, or `SimplicialComplex.homology` on the one graph that Sage itself traverses to join and linearize the preamble's own categories, and the swap would have left the tool looking fine while the fact stayed hidden.  The measurement is scheduled as the TODO node `category-graph-engine`.

- **Violation Example**: `import networkx` added to a module because a Sage call felt slow; a depth-first search written in place of the Sage routine because a Sage constructor rejected the input as given; a `cached_method` added to a slow path before anyone found out why it is slow; a slow view deleted from a tool so that the tool passes.

- **Correct Example**: build a Sage graph of the same order and shape with no preamble in the process, time the call at three sizes, read the method's source for its `algorithm=` choices, record the curve and the chosen route in `TRAPS.md`, and route the owned operation through that spelling.  If the route is unaffordable at every size the research uses, that record is the `ENG-06` gap, and owning the algorithm becomes a decision the project can now make.

#### `ENG-08`: A Second Engine Is Adopted Only on a Recorded Measurement

- **Rule**: The Sage ecosystem is searched to exhaustion before any computation leaves it: Sage's own spelling, then the backends Sage ships and reaches through its own interface (GAP through `libgap`, PARI, Singular, its graph and numerical backends).  A library outside that ecosystem is adopted for an operation only when a `DEV-63` record shows the Sage route absent, wrong, or unaffordable at the sizes the research uses, and the adoption is recorded beside that measurement with the route it replaces.  `ENG-03` and `ENG-05` say which engines are acceptable; this rule says when a change of engine is.

- **Rationale**: The preamble routes one name to one computation so that the researcher never learns there was a choice.  That works only when the choice was made on evidence and written down.  An engine swapped in to dodge an unmeasured cost is a second computation path with no reason attached, and it removes the site at which the Sage fact would have been measured.  The fragmentation is also real: two graph libraries in one tree are two sets of input conventions, two output shapes, and two homes for the same defect.

- **Violation Example**: replacing `sage.graphs.graph.Graph` with `networkx.Graph` in a tool because one view was slow, with no timing of the Sage call; adding `sympy` for a factorization Sage's rings already perform; a justfile recipe that installs a package to run a computation Sage's own interpreter already provides.

- **Correct Example**: measure the Sage route first; if a shipped backend answers, select it through Sage's own keyword and record that; if nothing inside the ecosystem answers, record the gap with its measurement, then adopt the outside library under `ENG-05` with the record cited at the crossing.



* * *

### 9. Engine Crossing Boundaries (`BND-*`)

#### `BND-01`: Backend State Has One Private Owner and One Controlled Crossing

- **Rule**: Durable backend state is private to the owned object or private adapter that owns that computational realization.
  A backend datum has one private accessor or boundary helper at its owning layer; do not create public accessors, aliases, or unrelated direct field reads.
  Protected contracts satisfy `OWN-05`: name the owner, permitted roles, exact
  types and invariants at the declaration. Mathematical subsystems exchange
  owned values, not raw handles. A comment authorizing a convenient private
  read is not a protected contract.

- **Rationale**: Multiple ways to reach the same engine are multiple APIs.
  A single visible crossing makes the representation dependency auditable and prevents backend operations from spreading through ordinary mathematical consumers.

- **Violation Example**: Reading `_preamble_pid_engine` directly from discriminant modules while Internal Hom uses a separate engine accessor and a third consumer reaches Sage's `V()` through the owned module.

- **Correct Example**: A private presented-module adapter owns one optional Smith engine and one documented conversion boundary used by the few algorithms that require the FGP implementation; ordinary consumers never receive its parent or elements.


#### `BND-02`: Cross In, Compute, Cross Back

- **Rule**: A backend crossing converts owned inputs to the backend representation, performs the backend computation, and converts the result back before the boundary returns.
  Backend parents, elements, vectors, matrices, submodules, homsets, normal-form workspaces, GAP objects, and all other representation structures do not propagate past that computation site.
  There is no element exception: a backend element is backend data and must be converted to an owned element before return.

- **Rationale**: Backend delegation is safe only when the backend computes for the owned mathematics rather than becoming a second mathematical universe used by downstream code.
  Immediate conversion back keeps representation-specific assumptions local and makes backend replacement possible without changing mathematical callers.

- **Violation Example**: Internal Hom computes an FGP kernel and returns that Sage FGP module or its elements for later consumers to inspect; a lattice invariant returns a Sage kernel basis and expects its caller to reconstruct the lattice; an owned group operation returns a GAP element because GAP performed the multiplication.

- **Correct Example**: Cross an owned module morphism and its owned coefficients into Sage's FGP representation to compute a kernel, then construct the owned presented kernel, owned kernel elements, and owned inclusion before returning.


#### `BND-05`: Backend Conversion Is Private and Non-Exported

- **Rule**: Conversions such as "owned ring to Sage ring", "owned element to Sage element", "owned group to GAP group", and their inverses are private implementation functions or private adapter methods.
  They are not exported from `preamble.all`, package `__init__` modules, public classes, or notebook-facing namespaces.
  Ordinary repository code outside the owning adapter does not call them merely to continue computation in the backend.

- **Rationale**: A public `engine_ring`, `engine_element`, `engine_group`, `to_sage`, `from_sage`, or similar helper is an intentional escape hatch even if individual parents hide their `_engine` field.
  The firewall is real only when backend representations are unreachable through the public API and crossings are confined to the implementation that immediately converts back.

- **Violation Example**: Exporting `engine_ring(R)` so callers can construct Sage matrices over it; exposing `_smith_engine()` broadly enough that unrelated modules perform FGP operations directly; retaining `own_ring(raw_sage_ring)` as a notebook-facing adoption constructor.

- **Correct Example**: A private FGP adapter owns `_to_sage_ring`, `_to_sage_element`, and `_from_sage_element` locally, performs the whole Smith computation, and returns an owned tensor/module/morphism.  No public caller can obtain or supply those Sage objects.

#### `BND-03`: Dispatch on Declared Owned Mathematics, Never by Type Peeking

- **Rule**: Public and category-level behavior is selected by owned category membership, owned structure, or the object's owned operations.
  Do not use `isinstance`, `type(...)`, `hasattr`, `getattr`-probing, or `try/except AttributeError` to discover what mathematical structure an owned object has or which mathematical operation it supports.
  Matching on engine classes is permitted only inside a private engine boundary whose job is to select an engine-specific implementation after the mathematical operation has already been chosen.

- **Rationale**: Python class identity and method presence answer how an object happened to be implemented, not what mathematical structure it carries.
  Type- and capability-peeking recreate implementation hierarchies as hidden second category graphs and let consumers infer stronger structure than was declared.

- **Violation Example**: A scalar-multiplication routine branches on `FreeModule_generic`, FGP module, and quotient-module classes after receiving an owned module; code asks `hasattr(M, "presentation_matrix")` to decide whether `M` is presented; a public group method decides group structure by inspecting the Sage class of the owned parent.

- **Correct Example**: Ask the owned module for its scalar action or `scalar_multiple`; inside the private group-engine boundary, match on the Sage engine class only to choose the corresponding GAP/Sage algorithm and return owned results.

#### `BND-06`: Backend Correspondence Provides Capabilities; It Does Not Define the Category Taxonomy

- **Rule**: Maintain backend mappings as implementation/capability correspondences from owned mathematical categories/constructions to available Sage/GAP/Julia/etc. realizations and algorithms.  The correspondence need not be injective and is not an equality of taxonomies.  Backend category names, graph edges, MRO order, and equality do not create or identify owned mathematical categories.

- **Rationale**: Several backend categories may implement the same normalized mathematics, and one backend category may package a combination of structures differently from the owned graph.  The useful question is “which backend capabilities are available for this owned object/operation?”, not “how do I make the owned hierarchy mirror Sage's?”.

- **Violation Example**: Add an owned category only because a Sage category has no current target; require one-to-one mapping between Sage category names and owned categories; copy `super_categories()` edges into the mathematical graph as authoritative inclusions.

- **Correct Example**: the owned graph is fixed by mathematics; a private/versioned bridge records each meaningful backend realization and the operations it can supply.  Multiple backend realizations may inhabit the same capability fiber, and updating Sage versions changes only the bridge, not the mathematical ontology.

#### `BND-07`: Reuse Engine Computation Without Adopting Its Public Objects

- **Rule**: The preamble owns mathematical identity and all public objects;
  maintained engines own their computations. Private engine representations
  may be ephemeral or privately cached under `OWN-10`. Reuse of host runtime
  primitives for generated owned types does not authorize adopting, reclassing,
  subclassing, or returning an engine's concrete mathematical parent or elements
  as preamble objects. An audit does not waive `ARC-05`, `ARC-06`, or `OWN-04`.

- **Rationale**: Algorithm reuse and independent public ownership are simultaneous
  requirements. Treating runtime adoption as another public ownership mode
  makes an engine's inherited API an alternate mathematical language.

- **Violation Example**: Replace a Sage algorithm with local Smith reduction to
  obtain owned elements; alternatively, return Sage elements from an owned parent
  because its concrete runtime type was declared audited.

- **Correct Example**: The preamble owns the module and its selected presentation;
  a private Sage/Singular computation returns data that the adapter raises into
  owned elements and an owned normalization isomorphism through the sanctioned
  constructor. Sage `Parent`/`Element` primitives may implement the owned runtime
  without making Sage's concrete modules the public objects.

#### `BND-04`: Never Repair an Ownership Violation with Compatibility Machinery

- **Rule**: When an owned object or element has been placed inside an engine object, an engine object has been reclassed as owned, or an owned parent has been made a facade over backend elements, fix that ownership seam.
  Do not compensate by joining Sage categories into owned parents, teaching Sage constructors to accept owned rings, adding coercion hooks, skipping problematic engine element types, preserving backend elements through facade parents, or installing backend protocol methods solely to keep the invalid embedding working.

- **Rationale**: These patches are symptoms of the same inversion: the engine has become responsible for understanding the owned universe.
  Each workaround expands the coupling and creates the next failure at coercion, element identity, category comparison, or constructor dispatch.

- **Violation Example**: Joining a Sage engine category into an owned ring so `FreeModule(owned_ring, n)` succeeds; skipping Cython element refinement because a reclassed permutation group loops in coercion; declaring Sage vectors to be the elements of an owned free module; adding `_im_gens_` only because a Sage algebra constructor received an owned module parent.

- **Correct Example**: A private adapter converts owned ring elements to Sage ring elements, builds a Sage free module or FGP workspace entirely on the backend side, computes there, and converts all outputs back.  A private group adapter may use a Sage/GAP group model, but public group parents and elements remain owned.  No backend category join, facade parent, reclassification, or backend-element exception is required.


#### `BRG-01`: Structured Engine Bridges Over Ad-Hoc Shelling

- **Rule**: Route communication with external systems (such as Julia, OSCAR, or Macaulay2) through persistent bridge interfaces (`sage_julia_bridge`, `JuliaHandle`, or C-APIs).

- **Rationale**: Shelling out via subprocesses with temporary disk files causes process overhead, unmanaged temporary state, and fragile error handling.

- **Violation Example**: Using `subprocess.run(["julia", "script.jl", tmp_file])` inside an inner loop instead of calling a persistent `JuliaHandle`.

#### `BRG-02`: Explicit Mathematical Interface Boundaries

- **Rule**: Translate data explicitly across bridge boundaries.
  Validate input types and convert results into owned repository types immediately upon return.

- **Rationale**: Keeps engine-specific representation leaks out of the public category API.

- **Violation Example**: Leaking raw engine pointers or un-wrapped backend matrix wrappers into user-facing category elements.

* * *

### 11. Environment, Execution & Tooling (`ENV-*`)

#### `ENV-01`: Strict Physical Path Resolution for Commands

- **Rule**: Use exact physical filesystem paths (such as `/home/dzack/research`) for shell commands, execution targets, and subprocess invocations.

- **Rationale**: Virtual mount aliases (such as `/research`) fail in standard POSIX shells and background tasks.

- **Violation Example**: Passing virtual root `/research` to a shell execution tool.

#### `ENV-02`: Deterministic Recipe Execution via Justfile

- **Rule**: Declare all project orchestration, gates, and documentation generators in the root [`justfile`](justfile).

- **Rationale**: Ensures reproducible execution across developer environments, CI pipelines, and automation tools.

- **Violation Example**: Running undocumented one-off ad-hoc bash scripts for builds or tests.

* * *

### 12. Development Discipline & Verification (`DEV-*`)

#### `DEV-01`: Strict Typing Without Opaque Types

- **Rule**: Type all public functions, methods, and classes explicitly.
  Do not use `Any`, `object`, `unknown`, or silent type ignores.

- **Rationale**: Types communicate mathematical intent and enable static correctness checks.

- **Violation Example**: Annotating a morphism constructor with `def __init__(self, data: Any) -> object:`.

#### `DEV-02`: Specimen-First Falsification Discipline

- **Rule**: Accompany every new category, functor, or operation with a concrete, falsifiable mathematical specimen.

- **Rationale**: Progress is measured by mathematical specimens that can fail, not by uninstantiated schemas.

- **Violation Example**: Adding abstract category definitions without a test specimen or executable verification.

#### `DEV-03`: Consult Megadoc, TODOs, Reuse Constructions, and Implement at Maximal Generality

- **Rule**: Before adding or changing code under `src/dzack_research/preamble/`, read the generated megadoc output `docs/preamble-megadoc.md` and the root [TODO.md](TODO.md), including its unfinished constructions, input contracts, priorities, dependencies, acceptance criteria, and active file reservations.
  Reading the generator `src/dzack_research/utilities/megadoc.py` does not satisfy the megadoc requirement; if the generated document may be stale, run `just preamble-megadoc` and then read the generated output.
  Always reuse existing constructions when they are mathematically correct and principled.
  When a required construction does not exist, implement it at its most mathematically general level (in its native abstract category or module layer) and progressively specialize and share it across concrete domains.

- **Rationale**: Prevents duplicate definitions, competing APIs, already-recorded remediation from being reintroduced, and siloed mathematical implementations while ensuring global functorial coherence.

- **Violation Example**: Implementing an ad-hoc direct sum or orthogonal quotient exclusively for lattices without checking the megadoc for the general construction; adding a new tuple-valued framing helper while `TODO.md` already records the owned-family remediation; recreating a known architecture problem already catalogued in [the organization findings](TODO.md#organization-findings).

- **Correct Example**: Read the generated construction inventory and active remediation queues first; reuse the existing tensor product, Hom, subobject, or functor when it already expresses the mathematics, and add a missing operation at the category where its definition belongs rather than at the first concrete consumer that needs it.

#### `DEV-04`: Real Sets Over Manual Deduplication

- **Rule**: Never manually use "iterate + seen" patterns to deduplicate. Always form actual sets, usually a one-liner with a comprehension, or map/filter/reduce equivalents.

- **Rationale**: Forming a set states the mathematical operation — the collection, its membership, its cardinality — in one expression. A hand-written "seen" loop re-implements set semantics silently, hiding the operation and inviting order- and mutability-dependent bugs.

- **Violation Example**: Accumulating into a `seen` list with `if x not in seen` inside a loop instead of writing `set(xs)` or a set comprehension.

#### `DEV-05`: Architecture Conformance Precedes Suite Counts

- **Rule**: For an architectural change, first state what the affected mathematical object is: its owned data, category, public operations and return types, optional private engine state, and permitted engine crossings.
  Implement to that statement and read the resulting code against it before using aggregate test or type-error counts as feedback.
  Only then run tests as falsifiable specimens of the mathematics and its real consumers.

- **Rationale**: A pass count over a wrong architecture measures compatibility with the wrong architecture.
  Treating failures as a work queue encourages adding delegations, coercions, and backend aliases until the number falls, which can make the ownership defect deeper while making the suite greener.

- **Violation Example**: Seeing 53 failures after an ownership refactor and adding `coordinate_vector`, `gen`, `cover`, and Sage-category delegations one-by-one because each makes several tests pass.

- **Correct Example**: State that a presented module owns its presentation and framing, has only a private optional Smith engine, and returns no Sage module/vector/submodule; inspect every public method and consumer against that statement, then run the module, Hom, discriminant, and lattice specimens.

#### `DEV-06`: Tests Specify Mathematics and Consumer Contracts, Not Delegation

- **Rule**: Tests of owned mathematics assert mathematical objects, morphisms, categories, domains and codomains, chosen data, invariants, subobjects, tensors, and actual downstream operations.
  Do not add a test whose claim is merely that an owned object still carries an engine method or delegates to the engine under Sage's spelling.

- **Rationale**: A delegation test converts an implementation leak into a compatibility promise and makes deleting the leak look like a regression.
  Tests should fail when the mathematics is wrong, not when a backend escape hatch has been closed.

- **Violation Example**: Asserting `M.coordinate_vector(x) == M._engine.coordinate_vector(x)`, `hasattr(M, "gen")`, or that an owned subobject is a Sage submodule.

- **Correct Example**: Assert that `module_coefficients(x, M)` gives the coefficients in the selected framing, that a presentation matrix is the expected tensor, that a computed kernel comes with the correct owned inclusion, or that an invariant-factor normalization is connected to the original module by the claimed isomorphism.

#### `DEV-07`: Ownership Migrations Rewrite Their Consumers; They Do Not Preserve the Leak

- **Rule**: When an owned representation or boundary changes, sweep the repository for consumers of the old representation and rewrite those consumers to the owned operations in the same architectural change.
  Do not retain or reintroduce a public compatibility alias merely to defer that consumer migration.

- **Rationale**: A public compatibility layer makes the old representation a supported second API and guarantees that new code will continue to use it.
  The purpose of an ownership migration is to remove that route, so downstream breakage identifies consumers that must be repaired rather than methods that must be delegated.

- **Violation Example**: After replacing a reclassed or backend-element free module by a genuinely owned module, keep `.gen()`, `.basis_matrix()`, and `.coordinate_vector()` because Internal Hom, free resolutions, and lattice invariants still use those names.

- **Correct Example**: Rewrite those consumers to `module_generator`, `module_coefficients`, morphism tensors, `presentation_matrix`, `subobject_on`, and the documented private engine crossing where a specialized Smith computation is genuinely irreducible; then delete the old engine spellings from the public surface.

#### `DEV-08`: Promote Durable Repository Memory into Concrete Policy Codes

- **Rule**: Agent memory records history, rationale, traps, and prior decisions; it is not the repository's contributor-policy surface.
  When a ruling is stable, repository-wide, repeatedly relevant, and recognizable from concrete code or API shape, promote it into a uniquely named policy code in this document with a rule, rationale, violation example, and correct example.
  Task-local decisions, historical implementation details, contradictory records, and superseded rulings remain memory and are not promoted.

- **Rationale**: A durable architectural rule that exists only in agent memory is invisible to contributors who do not retrieve that exact record and will be rediscovered after the same mistake recurs.
  Concrete policy codes make the rule reviewable at the point of contribution while memory remains the provenance and historical explanation.

- **Violation Example**: Relying on a memory titled "close the coordinate hatch" to reject public Sage vectors while `CONTRIBUTING.md` contains only a generic backend-encapsulation rule; copying an old contradictory memory into policy without checking the current architecture.

- **Correct Example**: Promote the stable coordinate ruling as `API-02`, the constructor/witness rulings as `CON-*`, and the definition-vs-criterion ruling as `DEF-01`; leave episode-specific history and superseded mechanisms in the memory vault.

#### `DEV-09`: Promote Newly Discovered Architectural Rules Before Continuing the Remediation

- **Rule**: When investigation or a failed remediation reveals a repository-wide architectural principle that is absent, ambiguous, or contradicted in this document, update the relevant policy code before continuing implementation.
  The implementation then proceeds against the corrected written rule.
  Do not rely on the current conversation, agent memory, or an informal correction as the only statement of a newly discovered invariant.

- **Rationale**: Architectural remediation is iterative: a local failure can expose a missing lower-level object or an incorrect ontology.
  If that discovery is not immediately made durable, the next contributor or agent can repeat the same mistake while still technically following the written policies.

- **Violation Example**: Discovering that matrices need a first-class owned category, discussing that conclusion in chat, and then continuing to patch `tensor.matrix` while `CONTRIBUTING.md` still teaches only generic backend encapsulation.

- **Correct Example**: Add the fundamental-object/refinement and category-method rules (`ARC-09`, `CAT-05`) first, then implement owned matrix spaces and rewrite tensor/module consumers to those rules.

#### `DEV-10`: Repeated Mathematical Implementations Signal a Missing Abstraction

- **Rule**: When two or more implementations repeat the same mathematical state and operations, factor the shared mathematics into the appropriate category, common parent/element implementation, universal construction, or parameterized abstraction.
  Do not preserve duplication by copying methods, assigning sibling methods one-by-one, or maintaining parallel classes whose differences are only additional structure.
  The abstraction must remove implementations, not merely add another wrapper around the duplicates.

- **Rationale**: DRY in this repository is mathematical, not textual.  Repeated code for the same finite-support graded sum, Homset module structure, indexed enumeration, or transported action means the common mathematical object has not been represented strongly enough.
  Copying the implementation makes later fixes theory-by-theory and lets supposedly identical operations drift.

- **Violation Example**: `PowerAlgebraElement` reimplementing the component normalization, homogeneous pieces, addition, negation, scalar multiplication, equality, and display already implemented by `GradedDirectSumElement`; `GroupModuleHomset` and `GradedModuleHomset` copying a dozen `ModuleHomset` methods by assignments such as `base_ring = ModuleHomset.base_ring`; four indexed symbolic-function parents each reimplementing the same `rank`/`unrank`/membership/infinite iteration loop.

- **Correct Example**: Use the graded direct sum as the additive/module realization of a power algebra and refine it with multiplication/unit structure; express specialized module Homsets through the common module-Hom category/implementation; provide one parameterized indexed-symbol set whose prefix/indexing data specializes to Hermite, Fourier, Laurent, and sinc families.

#### `DEV-11`: Assertions State Proof Context and the Current Computational Frontier

- **Rule**: Use assertions liberally throughout mathematical code to state hypotheses, category containments, parentage relations, finiteness/nondegeneracy assumptions, shape constraints, derived identities, and the hypotheses under which the selected algorithm is currently total. Assertions are part of the readable proof skeleton of the code. They are not exception-style control flow and are not used as whole-method placeholders.

- **Rationale**: This repository is a Sage research preamble used interactively. Mathematical code should read like a derivation under explicit assumptions. The implementation should loudly expose both what mathematics is being assumed and where current computability stops. This keeps API placement mathematically correct without pretending that every mathematically defined operation is currently decidable for every represented object.

- **Violation Example**: Omitting a finite-rank hypothesis and letting a later matrix constructor fail opaquely; replacing `assert self.is_nondegenerate()` by exception-valued mathematical control flow; defining a method whose first and only statement is `assert False`; using `NotImplementedError` as the default implementation.

- **Correct Example**: Keep `cardinality()` on all sets and assertion-gate only a represented case not covered by current algorithms. Keep `is_nondegenerate()` on formed modules and assert the representation/finite-rank hypothesis needed by the current decision procedure. Use Sage `@abstract_method` only for a genuine implementation contract, and place genuinely narrower mathematics on the narrower category.

#### `DEV-12`: Canonical Identity and Memoization Use One Shared Mechanism

- **Rule**: Do not invent a new module-global `dict` cache for each mathematical construction when the repository or Sage already provides the required canonicalization/memoization semantics.
  Identity-sensitive constructions use one shared identity-memoization helper or an appropriate `UniqueRepresentation`/`cached_function`/`cached_method` mechanism with an explicit lifetime and identity policy.
  A theory-local cache is justified only when its semantics genuinely differ and that difference is documented at the cache definition.

- **Rationale**: Ad-hoc `id(obj)` dictionaries repeatedly reimplement weak identity checks, stale-entry handling, ownership of cached results, and lifetime policy.
  Different theories then acquire subtly different notions of when "the same construction" returns the same object.
  Canonical object identity is architectural behavior and should be reviewable in one place.

- **Violation Example**: Separate `_MODULE_TENSOR_PRODUCT_CACHE`, `_MODULE_POWER_CACHE`, `_DIVIDED_SQUARE_CACHE`, `_KAHLER_CACHE`, `_DE_RHAM_CACHE`, three form-space caches, and similar dictionaries each implementing their own identity-key convention and cached-object verification.

- **Correct Example**: Route identity-sensitive mathematical factories through one shared identity cache that verifies referent identity (and uses weak references where appropriate), or use `UniqueRepresentation`/`cached_function` when their equality/key semantics are mathematically correct.  A specialized cache documents why the shared mechanism cannot express its required semantics.

#### `DEV-13`: A Missing Semantic Abstraction Is Part of the Current Task

- **Rule**: Do not optimize for the smallest local diff when the requested feature exposes a missing or defective semantic API. Strengthen the common mathematical owner first, then implement the feature through it. A task that needs `f.kernel()`, a subobject pullback, a block Hom, an owned orbit set, or a theorem-backed predicate includes making that operation usable if the alternative is a local coordinate workaround.

- **Rationale**: LLMs strongly prefer completing the visible local TODO with information already at hand. In mathematical software this produces papercuts that permanently encode implementation accidents. Repository quality improves only if local work is allowed to reveal and repair lower-level semantic gaps. This is not uncontrolled scope growth: the lower-level change is justified exactly by the mathematical dependency of the requested feature and should make the original caller simpler.

- **Violation Example**: A cohomology task discovers that `image()`/`kernel()` do not compose cleanly, so it builds a bespoke augmented matrix and returns a presentation. An isotypic-component task lacks a suitable subobject kernel and writes `_kernel_subobject_of_matrix`. A lattice predicate lacks a structural cokernel predicate and computes minors locally.

- **Correct Example**: Repair `kernel`/`image`/subobject quotient composition, then define cohomology by those operations; improve the common module-Hom kernel and delete `_kernel_subobject_of_matrix`; expose torsion-freeness on the cokernel and define primitivity through it. The local feature becomes shorter while the semantic spine becomes more capable for every future consumer.

- **Review Question**: “If the low-level semantic API were complete, would most of this new code disappear?” If yes, repair that API before accepting the local implementation.


#### `DEV-14`: Contaminated Prescriptions Are Architecture Defects

- **Rule**: Treat issue bodies, plans, comments, docstrings, examples, tests, migration notes, and generated/reference artifacts as executable prescriptions for future contributors.  When a ruling falsifies one, repair or delete it at the source before implementation continues.  Do not leave contradictory prose beside corrected code.

- **Rationale**: Agents and humans correctly follow authoritative-looking records.  A stale prescription therefore has multiplicative blast radius: it recruits compliant future work to recreate a rejected ontology.  Documentation consistency is not cleanup after implementation; it is part of preventing recurrence.

- **Violation Example**: Correct the subobject implementation but leave an issue body requiring “shared ambient coordinates”; replace a numerical `is_primitive` implementation but retain a docstring describing its old matrix criterion; delete an API while preserving a generated reference test that demonstrates it.

- **Correct Example**: Update the governing issue/plan/docstring/test in the same ruling/migration, remove fossils, and ensure every surviving example teaches the current semantic route.

#### `DEV-15`: Mathematically Correct Failures Are Evidence, Never Targets for Weakening

- **Rule**: If a mathematically correct assertion, sourced test, or original acceptance claim fails, preserve the proposition and repair the code/architecture it falsifies.  Do not delete the assertion, weaken the test, narrow the claimed requirement after the fact, or patch an unrelated symptom merely to make the run green.

- **Rationale**: The failure is the information.  Weakening the proposition destroys the evidence and converts an incomplete implementation into a false success.  Once that weakened record becomes authoritative, it contaminates future work as well.

- **Violation Example**: A correct subobject test fails because ambient-coordinate machinery is wrong, so the test is removed as “oversized”; a true assertion is called incidental and deleted; a PR description silently drops a requirement that the implementation missed.

- **Correct Example**: Keep the assertion/test/contract fixed, trace the failure to the semantic defect, and repair or restart the implementation while preserving the original mathematics.

#### `DEV-16`: No Compatibility Shims for Superseded Preamble APIs

- **Rule**: When the owned API is corrected, migrate all repository callers and remove the superseded spelling/representation.  Do not preserve aliases, adapters, fallback signatures, or old constructor forms solely for backward compatibility unless the user explicitly designates a stable compatibility surface.

- **Rationale**: This research preamble is allowed to make breaking corrections.  A shim leaves the rejected ontology constructible, creates two sources of truth, and teaches new code to keep using the route the migration was meant to eliminate.

- **Violation Example**: Keep `generators()` and add `module_generators()` as a wrapper over it; retain `from_matrix()` publicly after introducing the presentation-morphism constructor; accept both `ambient=` and the new inclusion object.

- **Correct Example**: Make the precise semantic API canonical, update every caller, remove the old route, and let failures expose any consumer that has not migrated.  Deliberate session shorthand is judged separately as language design, not compatibility debt.

#### `DEV-17`: QC Findings Never Justify Semantically Empty Code

- **Rule**: Do not add code, wrappers, casts, suppressions, dynamic imports, or annotations whose only function is to silence a linter/type checker or reduce a diagnostic count.  First decide whether the diagnostic exposes a real mathematical/API defect or a missing fact in shared tooling.  Repair the appropriate layer.

- **Rationale**: Local suppression launders useful evidence in exactly the same way as weakening a mathematical test.  In a Sage-heavy dynamic system, checker gaps should be repaired in stubs/plugins/configuration rather than by corrupting otherwise correct mathematical source.

- **Violation Example**: `del x` inside an `@abstract_method`; a broad `cast(Any, ...)` around a category operation; `# type: ignore` on every dynamic category method; an import wrapper created solely because static analysis cannot follow Sage.

- **Correct Example**: Fix the real signature/owner when wrong; otherwise improve the Sage stub/plugin/QC rule centrally.  A narrow external-boundary suppression requires an explicit boundary reason and must not mask owned mathematical structure.

#### `DEV-18`: Nontrivial Mathematical Claims and Manual Algorithms Are Source-Grounded

- **Rule**: A nontrivial mathematical test, hand-coded criterion, or owned algorithm is grounded in a definition/theorem already encoded by the semantic API or in an authoritative mathematical source.  Prefer delegating to an existing trusted implementation.  When project code must own a nontrivial computation, record the theorem/hypotheses it implements and test sourced specimens.

- **Rationale**: LLM recall reliably preserves the shape of conclusions while dropping hypotheses.  Source grounding makes the theorem and its domain reviewable and prevents an attractive numerical criterion from silently becoming a universal claim.

- **Violation Example**: Implement a lattice predicate by a remembered determinant/gcd criterion with no cited hypotheses; add a fixture whose expected invariant was guessed from another example; manually diagonalize a quadratic form when Sage already provides the exact invariant.

- **Correct Example**: Implement the predicate from its mathematical definition through owned operations; let the low-level owner use a sourced criterion in the category where its hypotheses hold; cite/test canonical literature specimens for any genuinely owned nontrivial mathematics.


#### `DEV-19`: Stress-Test New Abstractions Against Infinite and Weak-Hypothesis Examples

- **Rule**: During design/review of a new mathematical interface, deliberately test examples outside the easiest finite-coordinate regime: infinite or nonenumerable index sets, nonfree/projective modules, noncanonical presentations, infinitely generated groups/actions, and base rings outside the first engine's sweet spot.  The example need not be currently computable; it tests whether the API states the mathematics without accidental hypotheses.

- **Rationale**: Ordinary fixtures overwhelmingly come from finite free objects and therefore fail to expose representational assumptions.  A stress object such as `Free_R(S)` for a nonenumerable set `S`, or an infinite-rank callable formed module, reveals immediately whether the proposed API incorrectly stores tuples, assumes complete enumeration, or identifies a morphism with a matrix.

- **Violation Example**: Approve an indexing API because all tests use `[n]`; approve `is_nondegenerate()` only after testing finite Gram matrices; define a group-action construction solely from finite generator images because every current group fixture is finitely generated.

- **Correct Example**: Ask whether the same method signature and mathematical return type still make sense for arbitrary `S`, infinite rank, or a predicate-defined group.  Keep the semantic API if it does; assertion-gate or specialize only the current algorithmic cases.



#### `DEV-20`: Tests of Weaker Equivalence Relations Use Distinct Objects

- **Rule**: A test of isomorphism, isometry, same-genus, equivalence, conjugacy, or another relation weaker than equality uses specimens that are not already equal by the repository's equality semantics.  Prefer independently constructed presentations/objects so the tested relation has real work to do.

- **Rationale**: Equality implies every weaker equivalence relation.  Testing `X.is_isomorphic(X)` or testing two inputs that canonicalize to identical objects cannot falsify the nontrivial algorithm and gives a misleading green result.

- **Violation Example**: Test lattice isometry using the same lattice object twice; test invariant-factor classification only by normalizing one module and comparing it with itself.

- **Correct Example**: Construct two non-equal framed modules known to be isomorphic and test the returned witness; construct two different Gram presentations of an isometry class; use distinct representatives known to lie in one genus when testing genus equivalence.

#### `DEV-21`: The Mathematical Model Precedes Engineering Mechanism

- **Rule**: Before proposing overloads, optional parameters, adapters, wrappers, registries, casts, dispatch tables, or inheritance changes, state the mathematical objects involved, the defining datum, the natural owner of the operation, its domain hypotheses, and its mathematical codomain.  Choose engineering machinery only after this model is fixed.

- **Rationale**: Many apparent software-design dilemmas disappear when two conflated mathematical operations are named correctly.  Starting from Python mechanisms encourages preserving the accidental current signature and solving around it; starting from mathematics determines whether the method should move, split, disappear, or become a standard categorical construction.

- **Violation Example**: Debate overload signatures for `is_open` before distinguishing an ambient-space predicate `X.is_open(U)` from a subobject predicate `U.is_open()`; design adapters around a matrix-returning API before asking whether the result is actually a Hom element.

- **Correct Example**: Write the intended mathematical signature first—object/morphism/Hom/functor and codomain—then select the simplest implementation mechanism that realizes it.  If the mathematical statement makes the proposed machinery unnecessary, delete the machinery from the plan.

#### `DEV-22`: Review Findings Diagnose Generators; They Are Not Local Patch Specifications

- **Rule**: When review reports an architectural violation, do not turn the literal finding into a work unit whose hidden constraint is “remove this occurrence while preserving the current implementation and tests.”  Reconstruct the governing mathematical rule, inspect sibling instances/consumers, and repair the generator/owner that produced the finding.

- **Rationale**: A local remediation prompt makes an agent optimize the contaminated tree.  Responsibility then migrates from one helper to another—wrapper, adapter, alias, registry, fixture—while the same semantic defect survives.  Architectural review is useful precisely because the reported occurrence points beyond itself.

- **Violation Example**: Move an illicit matrix kernel from `cohomology()` into `_kernel_helper()` and call the finding resolved; replace a global switchboard by a registry that still owns every descendant; remove an old public API while forbidding edits to all of its known consumers.

- **Correct Example**: Identify the missing `kernel`/subobject/category abstraction, fix it at its mathematical owner, migrate all consumers, then delete the local workaround.  Treat representation-level tests that only preserve the condemned implementation as migration targets rather than immutable acceptance criteria.



#### `DEV-23`: Architectural Migrations Are Allowed to Be Sweeping and Breaking

- **Rule**: During an explicitly architectural preamble migration, optimize for the final mathematical architecture rather than for a sequence of horizontally “safe” compatibility-preserving edits.  Move responsibility to its final owner, migrate the vertical consumer slice, and delete superseded machinery.  Do not invent an incremental-green requirement that the user/project has not imposed.

- **Rationale**: A local compatibility constraint causes work to be spent stabilizing code that the correct architecture will delete and encourages wrappers/shims that preserve the rejected model.  Long-horizon research infrastructure may legitimately be temporarily inconsistent while a coherent vertical migration is in progress.

- **Violation Example**: Keep the public coordinate-vector API because rewriting all kernel consumers in one pass would temporarily break tests; add adapters around a global dispatcher instead of moving each operation to its owner; refactor code scheduled for deletion merely to keep every intermediate commit green.

- **Correct Example**: Make the owner/category change, migrate all affected consumers in that architectural slice, remove the old route, and evaluate correctness against the final mathematical model.  Verification requirements remain whatever the active repository instructions actually state; “safe” incrementalism is not assumed.

#### `DEV-24`: A Misplaced Mathematical Concern Triggers an Ownership Audit

- **Rule**: When a specialized/deep module is performing mathematics that obviously belongs to a more general construction, stop local implementation and audit ownership before adding another patch.  Search for sibling copies, identify the general semantic owner, and determine why the abstraction failed to propagate there.

- **Rationale**: Misplaced concerns are high-signal architecture defects.  A lattice leaf calculating generic set cardinality, or a subobject leaf implementing generic quotient machinery, means downstream code has crossed a boundary that should have been closed.  Fixing only the immediate line makes the architecture harder to see and usually leaves duplicates elsewhere.

- **Violation Example**: Optimize a cardinality algorithm inside a lattice-specific file; add another quotient helper to a deeply nested subobject implementation; repair a scheme-specific product routine without checking the generic categorical product owner.

- **Correct Example**: Pause the local change, trace the operation to `Sets`, `Hom`, quotient/cokernel, product, or other general owner, repair that layer, then let the specialized code reduce to delegation or disappear.



#### `DEV-25`: Verified Mathematical Facts Are Reusable Data; Tests Are Thin Drivers

- **Rule**: Stable externally verified mathematical facts used as test expectations belong in a centralized topic-organized fact/fixture corpus independent of any one implementation spike.  Each fact records enough mathematical identification to reconstruct the specimen, the expected value/statement, provenance (literature bibkey, source-system doctest, or independent oracle as appropriate), and verification status.  Tests consume this corpus parametrically rather than scattering literal expectations throughout test bodies.

- **Rationale**: A named invariant, classification row, orbit count, discriminant form, genus separation, or number-field fact is mathematical data reusable by multiple implementations and frontends.  Embedding it separately into individual tests duplicates provenance and allows contradictory expectations to accumulate.  A centralized corpus also prevents the implementation under test from silently becoming its own oracle.

- **Violation Example**: Copy `240`, a discriminant tuple, or a list of genus representatives into several test functions with no citation; generate a “golden” expected value by running the same method and saving its output.

- **Correct Example**: Store the cited/verified fact once in the mathematical fixture corpus; a thin test constructs the specimen through the current preamble API and checks the computed invariant against the fixture.  Backend parity data is clearly marked as such and is not promoted to mathematical truth without an independent basis.




#### `DEV-26`: Scope Defaults to the Strongest Coherent Mathematical Interpretation

- **Rule**: When a requested mathematical capability has a clear coherent general meaning, implement/analyze that capability rather than silently reducing it to representative examples, a percentage target, a wrapper, an audit artifact, or the currently easiest backend-supported subset.  Decomposition into work units is allowed; relaxation/removal of the mathematical target requires an explicit user/project ruling.

- **Rationale**: LLMs often convert difficult implementation obligations into tractable proxies and then optimize the proxy.  In a long-horizon research workbench this permanently shrinks the language around today's implementation limitations and produces exactly the local-special-case architecture the project is designed to avoid.

- **Violation Example**: Replace “support arbitrary framed modules” by “support the finite free fixtures”; turn “implement all relevant set constructions” into an inventory report; declare an infinite analogue out of scope solely because the current matrix engine is finite.

- **Correct Example**: keep the general semantic object/API as the target, implement the currently computable cases with the documented assertion frontier, and leave genuinely unimplemented cases as explicit remaining work rather than redefining the feature downward.



#### `DEV-27`: Mathematical Verification Uses a Definition, Complete Invariant, or Explicit Witness—Never an Easier Necessary Proxy

- **Rule**: A test/check claiming a mathematical property must be capable of failing on a false instance of that property.  Verify through the definition/universal property, an explicit witness, or a cited complete invariant/classification theorem whose hypotheses are stated.  A necessary but insufficient numerical invariant is not verification merely because it is easy to compute.

- **Rationale**: The characteristic LLM shortcut under mathematical difficulty is to replace “find/prove the isometry”, “prove completeness”, or “check reducedness” by a determinant, count, fingerprint, invariant-factor, or cardinality comparison.  Such checks can remain true for mathematically false outputs and therefore certify nothing about the claimed result.

- **Violation Example**: equal discriminant-group invariant factors used as proof that two discriminant **forms** are isometric; determinant preservation used as proof of basis reducedness; equal cardinalities used to certify a computed orbit/root/vector set is complete; a tautological `|H|^2=|A|` check used as proof that a generated subgroup has the required property.

- **Correct Example**: exhibit/check the isometry; call a genuine reducedness verifier; compare against an independent complete enumeration; or invoke a cited complete classification invariant at its semantic owner.  Difficulty of the correct check is a blocker/algorithmic frontier, never permission to weaken the proposition.

#### `DEV-28`: Negative Tests Must Establish a Live Positive Surface First

- **Rule**: A test whose main claim is absence, rejection, non-membership, or lack of a capability must also establish enough positive behavior that a dead/empty/misconstructed object could not pass it.  Prefer testing the positive mathematical universal property that implies the intended absence rather than testing deletion itself.

- **Rationale**: `not hasattr`, empty-result exclusions, and “this removed API is absent” assertions pass on objects with no functionality at all.  They are especially dangerous after refactors because they test the agent's own deletion rather than the behavior the deletion was meant to protect.

- **Violation Example**: assert a tensor product has no projections by `not hasattr`; assert a forbidden element is not in a result without proving the enumerator returned the expected nonempty/complete population; fabricate a removed compatibility artifact and assert the new code ignores it.

- **Correct Example**: test the tensor-product universal property positively; establish a sourced positive result/count/completeness witness before exclusions; regression-test the owned behavior that previously failed instead of the textual absence of the old code.



#### `DEV-29`: Use Sage's Native Conformance/TestSuite Machinery for Sage Runtime Contracts

- **Rule**: When verifying that an adopted/generated Sage `Parent` or `Element` satisfies Sage-level abstract/runtime obligations, use Sage's existing `TestSuite` / `_test_not_implemented_methods` / category tests rather than hand-rolling `dir()`, `getattr`, exception filtering, or a parallel conformance checker.  This is host-runtime verification only; mathematical behavior still uses the repository's sourced specimens and semantic tests.

- **Rationale**: Sage already knows how its dynamic category/abstract-method machinery is surfaced.  A custom introspection sweep is narrower, duplicates framework behavior, and tends to turn host implementation details into a second project ontology.

- **Violation Example**: loop over `dir(obj)`, call each attribute, catch `NotImplementedError`, and maintain a project list of “required Sage methods.”

- **Correct Example**: use Sage's native conformance test for the adopted runtime object, while separate mathematical tests assert kernels, universal properties, invariants, morphisms, and other owned semantics.



#### `DEV-30`: Fix Owned Defects at Their Authoritative Source During the Task

- **Rule**: When implementing a feature exposes a concrete defect/papercut in an authoritative component of the user's owned project stack and that defect lies on the feature's actual dependency path, repair it at its source before continuing.  Recording it in a TODO, filing an issue, reporting it, or adding a downstream workaround is not completion of the discovered defect.  Preserve unrelated dirty work and normal scope boundaries; this rule is about following the real mathematical/implementation dependency to its owner, not gratuitous cleanup.

- **Rationale**: Reporting a fixable upstream defect as “known” feels cautious to an agent but leaves every downstream caller compensating for it.  The resulting Protocols, local stubs, facades, aliases, and copied computations turn one source defect into permanent distributed complexity.

- **Violation Example**: the preamble's type/API is wrong, so a downstream research script defines a local Protocol instead of repairing the preamble; a missing semantic `kernel` capability is noted in `TODO.md` while the current feature ships a matrix workaround; a clean reference mirror is known to be on the wrong pinned revision and the mismatch is merely documented.

- **Correct Example**: repair/wire the authoritative preamble annotation or semantic method, consume it normally downstream, and keep only genuinely deferred research work in the TODO.  If the source cannot be modified because it is external/unowned, use the narrow documented boundary appropriate to that external dependency.



#### `DEV-31`: Missing Packaging Is Not a Mathematical Gap

- **Rule**: Before declaring that Sage/another library lacks a mathematical concept because no exact class/function/name matches the preamble's desired noun, attempt to build the notion compositionally from standard categories, properties, Homs, structured-object constructions, functors, or universal constructions already available.  Only a genuinely missing primitive/theorem/reusable construction is an upstream mathematical gap.

- **Rationale**: Standard mathematics is often expressed compositionally rather than by one canonical software constant.  Exact-name search encourages unnecessary new wrapper types and duplicated categories merely because another library packages the same mathematics differently.

- **Violation Example**: declare “enumerated finite sets” or “symmetric bilinear objects” absent because no upstream class has exactly that phrase while existing finite-set/property/structured-form machinery already composes to the notion.

- **Correct Example**: write the mathematical construction from existing primitives first; if that construction itself cannot be expressed because a primitive/theorem is missing, record the actual missing primitive rather than the absent spelling.

#### `DEV-32`: Completion Metrics Do Not Change Their Denominator to Make the Residue Vanish

- **Rule**: For audits, migrations, replacement/parity sweeps, and architectural inventories, freeze the original population/success condition before classifying the residue.  An unresolved item leaves the denominator only when evidence establishes that it never belonged to the original semantic domain, not merely because it can be relabeled “helper”, “plumbing”, “example”, “alias”, “implementation detail”, or “deferred research.”

- **Rationale**: LLMs under completion pressure can make a metric reach zero by reclassifying difficult cases rather than resolving them.  The resulting count can be internally correct under the new taxonomy while being false relative to the user's original question.

- **Violation Example**: report “zero unanchored mathematical concepts” after moving every difficult unmatched declaration into an “implementation-only” bucket without proving those declarations are semantically irrelevant.

- **Correct Example**: report the raw residue, separately argue any proposed reclassification against the original scope, and update the denominator only after that semantic judgment is established.



#### `DEV-33`: Understand and Probe the Host System Before Writing Code Around It

- **Rule**: Before implementing a low-level operation that plausibly belongs to Sage, Python stdlib, or another installed mathematical system, inspect the host documentation/source/API and run a small distinguishing probe when semantics/conventions are uncertain.  Do this before inventing wrappers, compatibility shims, local algorithms, or claims that the host cannot support the desired mathematics.

- **Rationale**: Many slop patterns are knowledge gaps disguised as implementation: explicit rational constructors in preparsed Sage, positional generator APIs instead of named-generator syntax, identity matrices instead of Hom identities, custom conformance sweeps instead of `TestSuite`, row loops instead of matrix constructors.  A quick host probe can delete whole designs before they are written.

- **Violation Example**: claim a Sage category/matrix operation behaves a certain way from its name/docstring alone; hand-roll a transformation because the native method was never searched; speculate that a dependency cannot handle Sage objects without installing/probing it.

- **Correct Example**: inspect the exact Sage implementation and test a specimen that distinguishes the competing interpretations, then use or quarantine the verified native capability through the owned semantic API.

#### `DEV-34`: Automated Findings Are Inputs to Structural Diagnosis, Not Syntax-Golf Targets

- **Rule**: When a linter/scanner/static analysis flags a recurring code shape, first disposition it against source semantics and repository policy.  If it is a real violation, fix the underlying state/ownership/mathematical model.  Do not make code denser, indirect, suppressed, or syntactically different merely so the detector stops matching, and do not treat a clean rerun alone as proof of remediation.

- **Rationale**: Detector-first remediation optimizes a proxy.  The offending shape usually exists because the architecture made it natural; syntax substitution can silence the signal while preserving the defect and making source harder to inspect.

- **Violation Example**: replace an accumulator loop with obscure mutation solely to evade a pattern check; add `# noqa`/`type: ignore`; inspect detector internals and rewrite around its exact AST pattern before deciding whether the code violates policy.

- **Correct Example**: decide whether the finding represents eager enumeration, hidden structure, wrong ownership, a typing-boundary gap, etc.; apply the corresponding `STY`/architectural correction, then rerun the detector as confirmation rather than as the definition of correctness.



#### `DEV-35`: Enforce Architecture in the Mathematical Language; Keep Compliance Machinery Thin

- **Rule**: Prefer stronger owned types/categories, constructors, signatures, visibility, and semantic APIs that make an invalid state/shortcut difficult or impossible to express.  Audits, reflection gates, manifests, source-pattern scans, and compliance reports are secondary backstops.  When a compliance mechanism repeatedly catches the same generator, move the invariant into the language rather than expanding the auditor.

- **Rationale**: Downstream enforcement machinery grows into a second project: it gains schemas, tests of tests, suppression rules, and gameable metrics.  Structural domain modeling makes the desired behavior the ordinary construction path and turns violations into obvious boundary escapes instead of compliance puzzles.

- **Violation Example**: add a generated certificate to each category stating which methods it supposedly supports; write runtime tests that inspect source layout/method placement instead of constructing mathematical specimens; add another reflection gate for coordinate leakage while keeping public coordinate escape hatches.

- **Correct Example**: close the coordinate constructor, put the operation on its mathematical owner, require the defining morphism/structure in the constructor, and keep one lightweight static inventory/report as a review aid.  Architecture is checked by source inspection and mathematical behavior, not by making the runtime suite prove the repository organization to itself.

#### `DEV-36`: Judge Preamble Health Against Upstream Sage, Never Against Zero

- **Rule**: The goal is source a mathematician can read against a definition.  Every numerical measure is a weak proxy for that goal, so a measure is admissible only as a differential signal naming a site to go and read, and only beside a calibrated comparator.  The comparator is upstream Sage under the same instrument (`python3 -m dzack_research.utilities.complexity_analysis <tree>`), never zero and never the previous run alone.  Report a measure with its comparator or do not report it.  Before treating any measure as a defect signal, establish that the healthy comparator does not exhibit it.

- **Rationale**: A mathematical universe is intrinsically interconnected, so measures borrowed from ordinary software carry assumptions that do not hold here.  Acyclicity is the type case: `sage/categories` runs 154 of its 229 modules in one strongly-connected component and `sage/rings` 116 of 239, and both have been in service for over a decade.  Mutual reference between the set and ring layers is not evidence of a defect.  An uncalibrated measure invites optimizing a number that the field's own reference implementation would fail, which is `DEV-32` and `DEV-34` arriving through the assessment surface instead of the detector surface.

- **Observed comparator** (`sage-dev-allopts` checkout, 2026-09-04):

  | measure | `sage/categories` | `sage/rings` | what it is evidence for |
  | --- | ---: | ---: | --- |
  | largest strongly-connected component | 154 / 229 | 116 / 239 | **nothing** — cycles are normal here |
  | imports through package aggregators | 3 | 63 | real: aggregator routing is avoidable and Sage largely avoids it |
  | function complexity p90 / p95 / p99 / max | 4 / 7 / 14 / 49 | 7 / 10 / 23 / 70 | real: docstring-immune, counts branches a reader holds |
  | non-code share of physical lines | 79% | 74% | real: worked mathematical examples per operation |

  Function-length percentiles are **not** comparable across these trees.  Sage carries its doctests inside function bodies, so its lengths measure documentation, not logic.  Use complexity instead.

- **Violation Example**: reporting a strongly-connected-component count as a health result; setting a target such as "reduce probe sites below 217"; treating a falling `tuple(...)` count as evidence that collection ownership improved, without opening a converted site; comparing this quarter's number to last quarter's with no external comparator.

- **Correct Example**: measuring dependency direction against the mathematical dependency order — an import from `categories/rings/` up into `categories/modules/` is a signal, an import from `categories/modules/` down into `categories/rings/` is not — then reading the flagged file to decide whether the edge is a filing error or correct mathematics.  Quoting a complexity percentile beside Sage's.  Naming what a count made you go and read, and what you found there.



#### `DEV-37`: A Test Stays Inside the Mathematical Universe

- **Rule**: `ARC-00` governs the proof surface.  Do not apply `tuple`, `list`, `sorted`, `len` or a comprehension to an owned object in order to make an assertion.  Ask the object: `cardinality()` rather than `len`; equality of owned objects rather than equality of materialised sequences; `Set(...)`, `finite_ordered_set(...)` or the relevant family on the right-hand side.  `len` remains correct on a Python container the test itself constructed as syntactic ingress, and on nothing else.

- **Rationale**: `tuple(X)` yields a value with no parent, no category, no cardinality and no homs -- an object of no category in this repository.  The assertion that follows is a statement about Python data structures, and because the test *is* the proof surface, that is what has been proved.  `len` carries the same exit one level down, and additionally asserts finiteness at a site that never stated it: a length is an `int`, a cardinality is a cardinal, and the roots of an indefinite lattice are infinite.  The order underlying a materialisation being genuine -- a framing is ordered, invariant factors are ordered by divisibility -- does not license the exit; order is not what is at issue.

  Comparing after extraction is not merely differently spelled, it is **strictly weaker**.  `tuple(a) == tuple(b)` passes whether or not `a == b` is implemented, and whether or not it is implemented correctly, so the assertion silently declines to exercise the equality the preamble owns -- the very operation a mathematical test of two objects exists to check.  Extraction thus removes proof burden unilaterally: it can only admit more implementations than the direct comparison, never fewer.

  When there is nothing owned to compare against -- the operation hands back a bare tuple, so no equality, parent or cardinality is available to ask for -- the defect is upstream and the rule is not satisfiable in the test.  That is `CON-15`: the tuple is an element of a product nobody named, and the repair is to name it, after which the test states equality of owned elements.  A finding here and a tuple-valued return are one defect seen from two ends, so a test-side workaround for it is not a fix.

  There is also no occasion for a test to assert about a non-owned value in the first place.  Every claim worth making here is a claim about an owned object -- its equality, its parent, its cardinality, its category, a law it satisfies.  A test that needs a Python container to phrase its assertion has either not identified the mathematical statement, or is reaching for one the owned interface does not yet express, which is a finding to report rather than to route around.

- **Violation Example**: `assert tuple(m.module_generators()) == (x, y)`; `assert len(lattice.roots()) == 6`; `assert len(tuple(pairs)) == 10`; reading the collection class to find out which accessor exists, then asserting against that.

- **Correct Example**: `assert lattice.roots().cardinality() == 6`; `assert L.inverted_elements() == Set((ZZ(2),))`; `assert R.algebra_generating_set() == finite_ordered_set(("x", "y"))`; `assert homset.is_empty()`.  If two families should be equal, write `==` between them; whether the equality is implemented is the implementation's obligation to meet, not the test's to work around.


#### `DEV-38`: Assert the Object, Not a Chosen Presentation

- **Rule**: Assert the mathematical entity and its defining property.  Do not assert a presentation, a chosen datum that is not unique, or an implementation class.  An ideal is compared to an ideal, a subobject to a subobject, a morphism through its defining law.  Where a datum is a choice -- a minimal generating set, a basis, a set of orbit representatives -- assert what the choice must satisfy, never which choice was made.

- **Rationale**: A presentation-pinned assertion fails on an equal object presented differently and passes for reasons unrelated to the claim, so it discriminates against correct implementations while admitting wrong ones.  A minimal generating set is not unique: an implementation that legitimately selects another generator fails a test that named one.  An `isinstance` check asserts an implementation accident, and one mathematical notion is realised here by several unrelated classes; the category is the type, so membership is the statement and the defining property is the proof.

  A private implementation class is a presentation too.  Assert through the public mathematical surface a consumer would actually use -- category objects, category-owned constructors, refinement declarations, and the membership and methods reached through them -- never a nested method-container class, a handwritten dummy subclass, or a concrete type that happens to realise the notion today.

- **Violation Example**: `assert tuple(I.ideal_generators()) == (ring(y),)`; `assert tuple(M.minimal_module_generators()) == (M.module_generator(0),)`; `assert isinstance(genus, Genus)`; asserting against a nested `ParentMethods` class or a dummy subclass as if it were category membership; `assert not hasattr(tensor, "morphism")`, which records a deletion and keeps the removed name alive for every later reader.

- **Correct Example**: `assert I.colon(divisor) == ring.ideal(ring(y))`; `assert M.submodule(M.minimal_module_generators()) == M` beside the asserted number of generators; `assert genus.signature_pair() == (0, 2)` and `genus.representative().genus() == genus`; for a derivation, the graded Leibniz rule and `d^2 = 0` rather than its class.

#### `DEV-39`: Test a Weaker Notion on Objects That Are Not Equal

- **Rule**: Isometry, isomorphism, same genus and same class are equivalence relations weaker than equality, and equality implies every one of them.  Assert a weaker notion only between objects that are **not equal** -- two constructions of the same lattice (Cartan against gluing, two decompositions), two lattices of the same genus built differently, two non-equal isomorphic objects.  The same applies to every other witness: a non-trivial morphism rather than the identity, a lattice with non-trivial discriminant rather than a unimodular one, an invariant whose value is a known theorem rather than one visible by inspection.

- **Rationale**: The value of an assertion is proportional to how surprising its passage would be.  `L` is isometric to `L` by definition, so the assertion cannot fail and proves nothing about the isometry code; the identity morphism satisfies every morphism property trivially; a unimodular lattice has a trivial discriminant group, so a discriminant test on one exercises nothing.  A test built from the most convenient specimen is a test that passes whether or not the operation works.

- **Violation Example**: `assert L.is_isometric_to(L)`; checking `is_primitive` on the identity; testing the discriminant group of a unimodular lattice; asserting that at least one element of an enumeration exists when the statement is about the whole enumeration.

- **Correct Example**: build `U + E8(-1)` two ways and assert the two are isometric; a reflection or a swap where a morphism is needed; \(E_8\) has 240 roots; `D4` or `A2` where the discriminant is the point.

- **Provenance**: `mem:global/advice/testing-weaker-notions-use-different-objects-not-equal-objects`, `mem:global/advice/choose-informative-cases-not-trivial-ones`.

#### `DEV-40`: Do Not Unwrap Coordinates or a Matrix to Make a Mathematical Claim

- **Rule**: An assertion about an element, morphism, image, kernel, cokernel or subobject is made through the semantic interface, never by comparing coordinates, a Gram or morphism matrix, a rank, a matrix kernel, a matrix image, or an eigenvalue list.  Construct the element in its parent and compare through the element interface; construct the Hom element and compare, compose or apply through the Hom interface; ask `f.kernel()`, `f.image()`, `f.cokernel()`, `f.is_surjective()` rather than reconstructing them from a matrix.  Raw unwrapping is permitted only inside the one canonical representation boundary that implements the semantic operation.

- **Rationale**: Coordinates identify an element only after a parent and a basis have been chosen, and a matrix represents a morphism only after domain, codomain, side convention and bases have been chosen.  An assertion made on the unwrapped data therefore proves a property of a chosen presentation, and repeated unwrapping spreads those choices across call sites, so a test can pass while checking a different mathematical object than the one its name claims.

- **Violation Example**: comparing `f.matrix()` entries to assert two morphisms agree; deriving surjectivity from a rank comparison; asserting an image by its spanning coordinates; `{tuple(v.to_tuple()) for v in representatives} == {...}`.

- **Correct Example**: `f == g` between Hom elements; `f.is_surjective()`; `f.cokernel().is_torsion_free()` for primitivity; comparing owned subobjects.  After the rewrite the assertion names the mathematical object or morphism property it proves, and any surviving coordinate comparison is visibly inside the representation boundary with its parent data fixed in one place.

- **Provenance**: `mem:global/traps/coordinate-and-matrix-unwrapping-in-tests-hides-math-objects`.

#### `DEV-41`: A Mathematical Expectation Is Cited Data; the Test Is a Thin Driver

- **Rule**: Verified mathematical facts -- named-lattice invariants, \((r,a,\delta)\) classes, genus separations, discriminant forms, cusp and orbit results, number-field facts -- are **data**, not test code.  They live in one centralised fixtures subtree organised by mathematical topic, each fact carrying its value, its citation and its verification status, and importing nothing from the code under test.  The consuming test is a thin parametrised driver containing no literal expected values.  The expected value comes from the cited source; it is never harvested by running the implementation and recording what it printed.

- **Rationale**: The same fact corpus is shared by every consumer -- each spike, the preamble, future category work -- and must remain browsable and queryable independently of any of them, so scattering hand-written value assertions through suite code both duplicates the corpus and binds it to one caller.  An expectation recorded from the implementation's own output is not an oracle: it passes by construction and cannot detect the error it was copied from.

- **Violation Example**: a literal invariant written inline in an assertion with no citation; a fixture that imports the module it is used to test; recording an expected value by running the code and pasting the result.

- **Correct Example**: a fixture entry carrying construction, \((r,a,\delta)\), citation key and verified flag, with a short parametrised driver over it; a new fact greppable in the fixtures subtree beside its citation, and a consuming test with no literal values in it.

- **Provenance**: `mem:projects/github.com__dzackgarza__research/decisions/testable-mathematical-facts-are-data-centralized-deep-fixtures-subtree-spike-independent` (user decision 2026-07-09, research#47); `mem:projects/github.com__dzackgarza__research/advice/what-a-test-cites`.

#### `DEV-42`: Prove a New Check Fires Before Trusting It to Pass

- **Rule**: Before a check, gate, scan or audit is relied on, confirm it reports a **known instance**.  A clean result from a check that has never been shown to fire is not evidence.  When a check has a target-selection step -- a file list, a glob, a scan root, an ignore file -- report how many targets it examined alongside how many findings it produced, so that "nothing wrong" is distinguishable from "nothing looked at".

- **Rationale**: The dangerous failure of a check is not a false positive, which is visible and annoying, but a silent pass, which is invisible and reassuring.  Target selection is where it happens: a scanner with a built-in ignore list that excludes the very directory being scanned reports zero findings over zero targets, and the output is indistinguishable from success.  A pattern language supplies the same failure from the other side -- an exclusion clause that is broader than intended disables its whole rule while the run still exits clean.  Both were observed while building `just test-universe`: semgrep's default ignore list excludes `tests/`, and a `pattern-not` of the form `tuple((...))` matches any single-argument call.  Each reported a clean scan.

- **Violation Example**: adding a rule and concluding from a clean run that the code is clean; reporting a finding count with no target count; tuning a pattern until the output is empty and treating that as the fix.

- **Correct Example**: running the new rule against a file known to contain the shape and seeing it reported; printing "checked N files" with the count; when a clean result arrives unexpectedly, breaking the rule down until the part that stopped matching is identified, rather than accepting it.

#### `DEV-43`: A Phase's Acceptance Must Be Sensitive to Its Repair, Not Only Its Removal

- **Rule**: When a plan pairs a destructive step with a repair -- remove an edge and restore what it carried, delete a layer and re-site its behaviour, drop a dependency and own what it provided -- the phase's executable acceptance must be able to fail while the repair is unfinished.  A criterion that measures only the removal is not acceptance for the phase, and a phase that names no criterion sensitive to the repair has none.

- **Rationale**: An implementer who has performed the removal and hit the resulting gap has two moves: do the repair, which requires deciding where the behaviour belongs, or install the cheapest local substitute that keeps the criterion green.  If the criterion cannot tell those apart, the plan rewards the substitute -- not by anyone's choice, but because that is the only thing being measured.  The observed instance: `Priority 3` named the graph-purity specimen as its only executable acceptance, and that specimen asserts what the category graph does *not* contain, so it passes identically on a graph that is pure and answering and on one that is pure and unloadable.  It stayed green through a period in which capability probes nearly doubled.

- **Violation Example**: a negative specimen (no forbidden node appears, no banned import remains, the count fell) as a phase's sole gate; declaring a migration phase complete on the strength of what is gone.

- **Correct Example**: pairing the purity specimen with one that constructs the affected objects and asks them for the operations their categories promise, so the phase cannot pass until the removed behaviour has been restored at its owner.  See `DEV-28`, which is the same requirement stated for an individual test.

#### `DEV-44`: A Catalogued Defect Gets an Owner in the Execution Order

- **Rule**: When an assessment enumerates defects and an execution order is written from it, every catalogued defect appears in that order -- as a step, as an explicitly deferred item with the reason, or as a decision that it is not a defect.  A defect that survives the assessment but not the ordering is unowned, and unowned defects grow.

- **Rationale**: Producing the assessment is the visible work and feels like the hard part, so the ordering is written from the severe rows and the rest fall out silently.  Nothing then measures the dropped ones, and every new file adds to them.  The observed instance: of seventeen defects catalogued in [the historical organization assessment](https://github.com/dzackgarza/research/blob/b5ff721fb94b030a637a527d449e628003c2b842/TODO.md#earlier-assessment), three reached no priority.  One of them was the duck-typed capability probing that grew from 52 recorded sites to 78 in a single day of work on the very subsystem the assessment had examined.

- **Violation Example**: an execution order derived only from the items marked severe; a defect whose absence from the plan is discovered by re-reading the assessment months later.

- **Correct Example**: a plan whose items and the assessment's rows are in correspondence, deferrals included, so that a reader can check the mapping in both directions.

#### `DEV-45`: A Tool's Failure Is a Fact About the Tool, Not About the Task

- **Rule**: When a tool cannot answer a question, that establishes the tool's limits.  It establishes nothing about the difficulty, size, or riskiness of the underlying work.  Before concluding that a task is hard, state the property of the *task* that makes it so, in terms that do not mention the tool.

- **Rationale**: A failed measurement is evidence, and the temptation is to promote it into evidence about the thing measured, because the failure is concrete and the alternative is thinking about the task directly.  Observed: jedi resolved 1 of 53 call sites for `tensor_valence`, and that measurement became "changing this return type touches every caller" as though the work were correspondingly large.  It does not follow.  Refactoring edits text on disk; for a duck-typed call the safety of a rewrite depends on whether the name denotes one operation, not on whether an inference engine can type the receiver -- and the real job was 21 definitions and three syntactic call-site shapes, all mechanical.  The same move in the other direction is equally wrong: a scanner that silently reported nothing became a reason to abandon syntax awareness entirely, when the failures were that scanner's alone.

- **Violation Example**: "the type checker cannot verify this, so the design is wrong"; "the language server cannot rename it, so the refactor is large"; "the linter has no rule for this, so it is not checkable"; concluding from one tool's silence that a class of tools does not apply.

- **Correct Example**: naming what actually governs the work -- here, whether a name denotes one operation, and how many definitions and call-site shapes exist -- then choosing a tool that answers *that*.  A name-based structural rewrite was the right instrument all along, and the type-inference failure was irrelevant to it.

#### `DEV-46`: A Banned Shape Is a Pattern; Tooling Must Close a Class

- **Rule**: A one-off shape that should not appear goes in the declarative pattern catalogue -- the `ast-grep` patterns behind `just test-universe` -- where it costs a line and states its own scope.  Tooling beyond roughly twenty lines must justify that size by preventing an entire **class** of semantic behaviour.  Before writing it, name the faulty mental model that produces the shape, and name the variations that model will produce which you have *not* seen.  If the tool would not report an instance nobody has written yet, it is a pattern, not a tool.

- **Rationale**: The instances in front of you are a sample of what a mental model generates, never the population.  A detector built by generalising from the sample catches the sample, and its clean run afterwards is uninformative: the model that produced those instances is still there and still generating.  Measured here: a 200-line AST checker for assertions that recover their own input, whose logic was a hand-typed list of eight accessor names, reported ten findings -- every one of them written the same afternoon by the author of the checker -- and never reported `X = [X0, X1]; assert X[0] == X0`, the canonical form of the very defect it was built for, because that shape touches no accessor.  A declarative pattern would have cost one line and been honest about covering one shape.

  The size threshold is about what the tool *decides*.  A pattern matches syntax and says so.  Code that earns two hundred lines decides something syntax cannot enumerate -- it evaluates, it folds, it resolves, it follows a definition -- and therefore reports instances in forms its author never wrote down.  A checker whose finding count equals the number of instances that prompted it has not crossed that line, whatever its length.

- **Violation Example**: a checker whose logic is a list of names harvested from the current tree; a tool whose findings are exactly the instances that motivated it; two hundred lines to catch what one `ast-grep` pattern states; concluding from such a tool's clean run that the class is closed.

- **Correct Example**: adding a row to the `ast-grep` catalogue for a shape just seen, and leaving it at that; for anything larger, first writing down the mental model and the unseen variations, then choosing an algorithm that evaluates rather than enumerates -- and confirming it reports a variation nobody has written.

#### `DEV-47`: An Oracle and Its Subject May Not Share a Source

- **Rule**: The expected value in an assertion must come from somewhere the code under test did not.  A test may not construct an object from ingredients and then assert that the object yields those ingredients back, and it may not compare two accessors that read the same stored datum.  State, for each assertion, where the expectation came from and where the actual value came from; if the answer is the same place, the assertion cannot fail.

- **Rationale**: This is the general form of both the catalogue error and the tautology it decays into under correction.  `lattice = A1 + A2 + U_2` followed by `assert lattice.indecomposable_summands()[0] is A1` asserts that `+` remembers its arguments; a transcribed Gram matrix compared to its transcribed signature asserts that one file agrees with itself.  Both pass by construction, and `DEV-41` names why that disqualifies them: an expectation taken from the implementation's own output is not an oracle and cannot detect the error it was copied from.

- **Violation Example**: `m = A + B; assert m.factors()[0] is A`; `assert L.rank() == L.module_generating_set().cardinality()` where the rank is defined as that cardinality; asserting a fixture value against the constructor the fixture was written from.

- **Correct Example**: a value from a cited source against a value the repository computed; two independent constructions of one object asserted equal; a theorem's prediction against an enumeration.



#### `DEV-48`: A Refactor Is Finished Before It Is Measured

- **Rule**: Commit to the refactor, carry it through the whole tree, and review it **by hand**.  Until the conceptual change is completely applied, do not run the suite, the gates, or any other aggregate signal, and do not treat their output as work.  An isolated syntax or type check on a file you just edited is fine, and so is a one-off script written to answer a specific question; a whole-suite run is not, because during a refactor its output is a function of how far through you are rather than of what is wrong.  The primary job is **rewriting**.  Getting the code to run again is what happens *after* the rewrite is complete, not the activity you are engaged in.  A refactor breaks things along the way, and that is the expected state, not a defect to repair as it appears.

- **Rationale**: Mid-refactor errors arrive because the change is half-applied: a call site still expects the shape you are replacing.  Fixing one therefore means writing code to reconcile the new shape with a caller that has not been converted yet -- an adapter for a state that will not exist once the refactor lands, which must itself be removed later.  Such work is not merely orthogonal to the goal; it is negative, because it entrenches the intermediate state and adds to what must be undone.

  The queue is also self-replenishing and self-directing, which is what makes the drift unbounded.  Each fix exposes the next error, so the list never empties and never hands control back.  The refactor's remaining work lives in a plan or in your head; the error list is on the screen, concrete and immediately actionable, and the screen wins every time.  Because each error is *locally* falsifiable -- real, reproducible, and verifiably fixed -- the loop supplies a continuous sense of gradient while the direction is orthogonal.  Local verifiability is not direction, and this is the standing mechanism behind `DEV-32` and `DEV-34`: a number that moves, taken for progress.

  The loop has no completion condition, only exhaustion or interruption.  So it ends with the architecture half-applied *and* a layer of adapters written for the intermediate state -- strictly worse than either the old design or the new one, and the reason a repository accumulates perpetual half-finished refactors.  Observed here: a `Hom`-to-`Mor` conversion was interrupted after the first suite run and became a day of unrelated repairs -- scalar ingress, natural-number construction, a quotient lift, relation coefficients, glue classes -- each a genuine defect that the conversion was always going to surface, none of them the conversion.

- **Violation Example**: running the suite while a rename is half-applied and working the failure list; fixing a caller that the same refactor is about to rewrite; adding a compatibility branch so an unconverted site keeps working; reporting a mid-refactor failure count as status.

- **Correct Example**: converting every site, reading the diff end to end, then running the suite once and diagnosing what remains against a settled architecture; writing a throwaway script to answer one question about an object's behaviour while the rewrite continues.

#### `DEV-49`: Architecture Is Decided by Analysis, Never by a Tool

- **Rule**: The design comes first, and it comes from reading the code and the mathematics and reasoning about them.  No checker, type error, finding count, coverage figure or failing test decides what the architecture should be.  Those instruments report on the code that exists; the question of what should exist is not one they can answer.  Metrics are consulted after the design is settled and applied, to find out whether the applied design is correct -- never to discover what it is.

- **Rationale**: An automated signal ranges over the current implementation, so any design read off it is a description of what is already there.  That is the wrong direction: a refactor exists precisely because what is already there is wrong, and the instrument cannot see the object that does not exist yet.  Deferring to it therefore converts a design decision into a repair of the present design, which is how a rewrite silently becomes maintenance.

  The failure is seductive because the instrument's output is specific and the analysis is not yet written down.  Observed here across one session: a `just test-universe` count taken as the objective and driven from 118 to 58 while the proof surface was unchanged; a detector's ten findings taken as evidence of its value when all ten were the author's own work from that afternoon; a mutation score that would have reported the motivating defect as well tested.  In each case a real number stood in for a judgement nobody had made.

- **Violation Example**: choosing a return type because it silences a type error; deciding a Hom belongs in one place because a checker complains about another; letting a failing test dictate the shape of the operation it tests; treating a finding count as the definition of done.

- **Correct Example**: deciding that a rank is a cardinal because ranks can be infinite and the repository owns cardinals, then applying that and using the type checker to find the sites; settling the design in discussion, then measuring.

#### `DEV-50`: TODOs Contain Only Unfinished Work

- **Rule**: Write each TODO from the current implementation and the desired mathematical behavior. Remove delivered work; do not retain checked boxes, completion claims, release histories, or retrospective audits in the queue. The implementation commit records the evidence and reasoning. For a partial delivery, remove only the delivered obligations and retain every required unfinished object, map, hypothesis, and generalization. A newly observed defect gets a new task describing the current source and the required repair, not a reopened historical claim.

  Read the current owner before scheduling it. A stale unchecked row does not establish missing implementation, and an old checked row does not establish correctness. Preserve already supplied constructions as inputs to the remaining work. Under deferred verification, delivery of implementation and written specimens does not discharge the separate terminal execution obligation. Keep that obligation open without retaining a history of implemented tasks.

- **Rationale**: A TODO directs the next action. Mixing it with past work makes future contributors either repeat finished constructions or inherit unsupported assumptions from status labels. Removing completed work must not remove broader requirements that one example did not satisfy.

- **Violation Example**: restoring an old release row to unchecked after discovering a new defect; leaving a completed toric algorithm as work to implement again; deleting the general non-toric requirement because its toric specialization exists.

- **Correct Example**: name the present completion constructor, the finite quotient it currently uses, and the new exact completion behavior required. Keep completed implementation history in git and pending execution in terminal T.

#### `DEV-51`: A Computational Image Is Not the Object

- **Rule**: Before substituting an engine representation or a derived object, identify the mathematical map into that representation and what information it loses. A consumer may infer a property back at the source only with the theorem that makes that inference valid under its actual hypotheses. Implement the object at its mathematical owner and expose projections, localization, scalar extension, or other comparison maps explicitly. A convenient computation cannot silently change the parent, category, or codomain promised to the user.

  Apply this to new instances, not only familiar names: a finite quotient is not a completion; a fraction field is not a prime-local ring; a finite group image is not the group; and cohomology dimensions are not cohomology modules or their induced maps. More methods on the substitute do not recover information it discarded.

- **Rationale**: The same wrong representation can produce many individually plausible downstream operations. Each new consumer then compounds one foundational error instead of extending the intended construction.

- **Violation Example**: computing in an exact quotient by a power of an ideal and advertising its arithmetic as completed-ring arithmetic; deciding a local-ring unit question after moving to the fraction field.

- **Correct Example**: construct the completion and its separate finite quotients, with source and projection maps. A polynomial image can be nonzero in the completion while its projection to one finite quotient is zero. Use the definition in [Stacks 00M9](https://stacks.math.columbia.edu/tag/00M9).

#### `DEV-52`: Exact Decisions Require Sufficient Information

- **Rule**: State what makes each implemented equality, zero, unit, membership, or isomorphism decision decidable on its represented input. Finite agreement proves agreement at that finite level; it does not prove exact equality. A detected difference may prove inequality, but exhausting a bounded search does not prove nonexistence. Keep computational precision separate from exact defining relations. When a supported exact answer cannot be obtained, use the established assertion-gated computational frontier, never a guessed boolean, fabricated witness, or silent change of output type.

  Propagate the same semantics through element arithmetic, projections, refinement, comparisons, and hashing where defined. Increasing available precision must not change an exact mathematical object or invalidate its identity in a cache. Do not infer unseen coefficients from one finite residue.

- **Rationale**: Relabeling a parent leaves its element decisions unchanged. An interface is still wrong if a low-precision zero becomes an exact zero through truthiness, membership, or inherited quotient arithmetic.

- **Violation Example**: treating a series as exactly zero because its available coefficients vanish; treating a failed search for an isometry as proof that the lattices are not isometric.

- **Correct Example**: distinguish an actual zero, an element that first differs from zero beyond the initial precision, and a genuinely nilpotent element in a ring with nilpotents. State exact equality only when the represented data or a valid decision algorithm establishes it.

#### `DEV-53`: A Correction Must Survive Other Construction Routes

- **Rule**: Translate a correction into the invariant it establishes, then follow that invariant through the affected public constructor, alternative constructors, elements, morphisms, and structural functors. Repair the common mathematical owner where the invariant belongs. Preserve both the new behavior and the already required behavior at that boundary; a fix to one route must not silently leave a second route with the same defect.

  Write separating mathematical specimens at the existing proof surface, subject to `DEV-58`. Include a nontrivial positive case and a nearby case that would expose overgeneralization. Migrate implementation consumers, not the mathematician's expectations. The protected expectation subtrees and their catalogue remain unchanged except for a justified mathematical correction recorded in its commit, as required by `AGENTS.md`.

- **Rationale**: A local spelling or constructor repair can leave the generating error intact. Another coefficient regime, direct Hom constructor, or dependent functor then recreates the violation without copying its original code.

- **Violation Example**: repairing transported local-module kernels while direct local-module Homs still use the wrong scalar ring; making only the principal completion route distinguish truncation from completion.

- **Correct Example**: preserve the local ring and its structural maps in both directly constructed and transported module morphisms, and express their compatibility through the actual comparison maps. Add the corresponding multivariable completion specimen when changing the shared completion contract.

#### `DEV-54`: Repair a Required Input Before Extending Its Consumers

- **Rule**: Before extending a dependent construction, read the particular upstream path it will consume and establish its required objects, maps, and hypotheses by source analysis. A method name, category label, completed TODO row, or upstream specification is not that input. If the required path constructs the wrong mathematical object, repair it and adapt the first dependent construction before expanding the dependent API.

  Dependencies attach to specific mathematical outputs. Do not wait for an unrelated upstream workstream to finish, and do not let one broken input freeze consumers that do not use it. A computational specialization is acceptable only when its stated regime actually supplies the required input; it is not permission for a fallback object.

- **Rationale**: Adding module completion, formal fibers, and flatness decisions on top of finite-quotient arithmetic multiplies the repair surface. Fixing the shared input first removes the cause rather than requiring a separate correction in every consumer.

- **Violation Example**: extending formal-family operations because a completion class and truncation accessors exist, without inspecting its element arithmetic; declaring all geometry blocked by a completion defect.

- **Correct Example**: establish the corrected ring completion before finite-module completion, and use the Noetherian finite-module comparison with its actual hypotheses ([Stacks 00MA](https://stacks.math.columbia.edu/tag/00MA)). Independent scheme gluing proceeds on its own established inputs.

#### `DEV-55`: Review the Complete Affected Control Flow

- **Rule**: After editing a shared source file, read the complete affected methods and enclosing class boundaries, not only added diff lines. Follow conditionals, indentation, early returns, and the paths that equip returned objects with inherited structure. Review neighboring operations whose control flow or shared helpers changed. Compare with the relevant pre-edit contract and retain its mathematical obligations.

  Write preservation specimens for exposed regressions at their existing mathematical owner. During deferred verification, perform the source review and leave those specimens explicitly unverified; do not claim that reading source proves runtime correctness.

- **Rationale**: An operation can retain its name, most of its body, and its tests while an indentation or return-path edit makes its essential construction unreachable. A diff limited to the intended new operation can miss that loss.

- **Violation Example**: adding an ideal quotient beside an algebra center and reviewing only the quotient lines, while a changed return path prevents the center from receiving algebra structure.

- **Correct Example**: read the full center and quotient methods, including all branches that produce the central submodule or subalgebra; retain specimens for the inclusion, multiplication, and the unit when required, alongside the new quotient specimen.

#### `DEV-56`: Decide the Next Construction in the TODO

- **Rule**: A substantive TODO names its current owner, the remaining mathematical delta, required input maps and hypotheses, the chosen representation boundary, and an acceptance statement that a mathematician could falsify. Name the first concrete specimen and the neighboring case that distinguishes the intended construction from its tempting substitute. Settle consequential mathematical forks before delegating the item; when source research is genuinely necessary, name the exact unresolved question and the construction it blocks.

  Preserve the full requested regime. State what an existing specialization supplies and what remains to generalize. Derive dependency order from the maps the consumer actually needs. Name the sanctioned constructor, reusable owned operations, selected upstream computation, and the actual missing integration; an unresolved backend search names the specific capability question, not a presumed mandate to implement an algorithm. Link the durable architecture contract in this document and the declaration-side contract required by `OWN-13`, so removing a delivered item does not erase its architectural decisions. Keep task details with the unfinished item; do not create a parallel readiness ledger, checklist system, or new gate to certify the prose.

- **Rationale**: A heading such as "add completion" leaves the next worker to choose between an exact object and the easiest finite approximation. Explicit mathematical decisions prevent that choice from being made implicitly inside an adapter.

- **Violation Example**: "finish local geometry" with no next object or input; "verify the new API" without a proposition; treating a toric dimension formula as completion of general geometric cohomology.

- **Correct Example**: require the image of a specific polynomial to remain nonzero in its adic completion while its projections at two stated orders differ, then require the completed module maps that consume that ring. This defines both the first repair and its downstream obligation.

#### `DEV-57`: Judge Progress by Mathematical Change Over Time

- **Rule**: Select work and assess trajectory against the user's substantive objective and the time-ordered mathematical changes. Distinguish newly supplied behavior, preserved behavior, regressions, their repairs, and dependencies that remain unresolved. Commit counts, checkbox counts, document volume, and the fraction of administrative commits do not measure that trajectory. A short repair interval does not erase productive work elsewhere; a long unobserved interval is not evidence of inactivity.

  A blocker names the exact unavailable input or authority, its owner, the affected construction, and the next action that can change it. Read the current scope and verification rules before treating a tool or hook failure as a blocker. Continue independent required work when its inputs exist. Assess a repeated failure as a recurrence of its mathematical or operational cause, not as a new spelling-specific exception.

- **Rationale**: Local activity can move a proxy while leaving the intended construction wrong. Conversely, counting administrative artifacts can hide genuine mathematical progress between them. Time-ordered evidence is needed to distinguish those cases.

- **Violation Example**: inferring stagnation from many documentation commits; inferring correctness from a shrinking TODO; stopping all work because one engine operation or an inapplicable hook is unavailable.

- **Correct Example**: identify which constructions became available during the observed interval, whether later edits preserved them, and whether dependent work consumed the repaired contract. State unobserved intervals and runtime verification gaps without converting them into conclusions about effort.

#### `DEV-58`: Observe the Current Verification Phase

- **Where the condition is checked**: this rule suspends execution *while the architecture,
  implementation, integration and transfer work remains open*, and whether it is open is not
  recorded here — it is the state of the work nodes in [TODO.md](TODO.md). Read them before
  concluding the suspension applies. A worker that treats the suspension as permanent has no
  way to reach T, and the repository accumulates unexecuted constructions for as long as that
  lasts; on 2026-09-13 it had banked sixty of them after the condition was already satisfied.
  Closing a node does not reopen the condition, and neither does discovering a further repair.

- **Rule**: Terminal T is the final verification phase of the preamble programme, after the required architecture, mathematical implementation, integration, and transfer work in `TODO.md`. While that work remains open, run no preamble tests, QC gates, Sage executions, or notebooks. Write and commit the construction and the mathematical specimens that would falsify it, explicitly unverified. References in other contribution policies to testing a work unit do not override this phase rule.

  Retain the two narrow operational exceptions: one short import check of a merged tree, and provisioning a tool required by a selected task. Neither is mathematical verification or permission to run a suite. Source review and checking a prose diff remain applicable. At T, execute the required mathematical evidence on the integrated architecture, diagnose actual failures, and establish the failed propositions at their owners. Do not restart repeated verification cycles against intermediate architectures.

  Classify hook applicability by the staged paths, not unrelated dirty files or a remembered failure. Under `AGENTS.md`'s QC integration rule, a prose-only commit uses `--no-verify`; the explicit notebook/preamble scope exemption also remains binding. Do not change shared QC configuration to obtain that authorized path, and do not extend an exemption to unrelated executable changes.

- **Rationale**: Runtime checks during the unsettled rewrite can redirect work into repairing a temporary architecture. Forgetting a declared exemption can also make an irrelevant hook result stop work that is expressly authorized. Neither error is repaired by adding another tracking artifact.

- **Violation Example**: running Sage to obtain a green completion specimen while required architecture remains open; repeatedly invoking whole-repo hooks for a TODO-only commit; describing a written but unexecuted assertion as a passing regression test.

- **Correct Example**: review the source and new mathematical assertions, commit them as unverified under the current scope rule, retain terminal T as unfinished work, and execute the required evidence only at that phase. For a TODO and policy edit, inspect the intended diff and commit only those prose paths with the prescribed hook exemption.

#### `DEV-59`: Record Observed Foundational Gaps and Papercuts

- **Rule**: [COMPLAINTS.md](COMPLAINTS.md) is the repository's canonical local
  record of unresolved observed problems, primarily missing foundational
  mathematics and missing structural relationships, and also actual papercuts
  in research use or contribution workflows. Record a finding when it arises
  during mathematical tracing, source reading, implementation, review, notebook
  use, or permitted execution. Discovery is not restricted to the selected TODO
  item. Capture before leaving the relevant work, not at a future audit.

  For a foundational complaint, begin with the desired mathematics in standard
  terminology. State the input/output objects and maps, hypotheses, and the
  recursive dependency path exposing the gap. Identify the earliest missing
  general construction or relationship, with the mathematical sources that
  justify it. Include a small ideal-API mathematical expression or specimen
  where useful, explicitly distinguishing illustrative pseudocode from an
  existing callable API. Do not title the complaint after a proposed manager,
  registry, helper, adapter, or feature-specific programming class.

  Then give the observed evidence: inspected source and symbols or the actual
  workflow and output, the existing partial construction, the precise unmet
  contract, affected consumers, confidence, and uninspected scope. Distinguish
  source evidence from executed failures. For an absence claim, use the
  epistemic-integrity fields Searched, Found, Conclusion, Confidence, and Gaps;
  a failed name search alone does not establish absent mathematics. An unresolved
  availability question may be recorded as such, but not as a confirmed defect.
  Name relevant maintained implementations and the exact capability question
  where known; their presence is not permission to leak foreign objects.

  A papercut entry names the real user action, expected behavior, actual friction,
  owning boundary, and observed example. Record it even when it is small. Do not
  invent a defect from a possible future inconvenience, and do not inflate a
  local ergonomic issue into a missing theory without a mathematical trace.

  Search existing complaint headings and the related TODO before adding an
  entry. Extend the existing mathematical complaint when a new consumer exposes
  the same missing foundation; retain genuinely different hypotheses or gaps.
  One general complaint can link several consumers. Its title and links should
  remain useful when those consumers move between files.

  **Division of responsibility:** CONTRIBUTING and mathematical declarations
  specify the enduring design; COMPLAINTS explains the observed unmet need and
  its evidence; TODO supplies selected execution work, dependencies and acceptance.
  Link the existing TODO item when it already owns remediation. If the current
  task requires the fix, update that item with the actual remaining delta and
  continue it. An independent finding can remain recorded without starting a new
  workstream. External issues own upstream repair; link them from the local
  complaint without copying their live status or surrendering the owned API's
  obligation. Filing or recording a complaint never completes its repair.

  **Maintenance:** use the shared-checkout transaction mutex for edits and commits
  of COMPLAINTS, as for TODO. Preserve concurrent entries. On delivery, compare
  the fix with the complaint's full mathematical requirement and its affected
  paths, then remove the resolved entry in that commit or an immediate companion.
  For partial delivery, retain only the unresolved need, evidence and links.
  Keep diagnosis and resolution history in git, not in resolved sections or
  completion rows. Preserve enduring mathematical decisions at their declaration
  before removing the entry. Source-based remediation does not certify runtime
  behavior; required execution remains in terminal T under `DEV-58`. An observed
  runtime failure is not resolved merely because a speculative source fix exists.

- **Rationale**: A leaf-level workaround can hide a reusable mathematical
  prerequisite from every later contributor. Recording the underlying theory
  makes that prerequisite visible without confusing discovery with implementation
  or turning an isolated symptom into another bespoke subsystem.
- **Violation Example**: discover that a specialization bypasses localization,
  add another fraction constructor, and mention the missing relationship only
  in chat; record "needs a backend manager" instead of the missing morphism.
- **Correct Example**: record the missing localization factorization with its
  submonoid and universal map, link the existing repair item, and complete the
  shared construction with its consumer. Remove the complaint only when that
  requirement is delivered, retaining any still-unverified execution obligation.

#### `DEV-60`: Close One Front at a Time in Dependency Order

- **Rule**: Work exactly one `TODO.md` node at a time, in the DAG's dependency
  order, and drive it to its stated acceptance before opening any other front.
  Shared-substrate (preamble) edits are in scope only when the current node's
  contract requires them. If multiple fronts are already open, close the
  nearest-to-acceptance front before any new authoring. During the refactor,
  commits use `--no-verify` per `DEV-58`; address real defects observed in the
  work itself as they arise, but do not run hooks, test suites, or type-check
  gates mid-refactor, and do not spend effort making files pass checks while
  the architecture around them is incomplete.

- **Rationale**: Parallel half-open fronts multiply integration debt, hide
  which mathematical contract is actually blocked, and leave abandoned
  mid-flight work that no later contributor can distinguish from delivered
  construction. One closed node is progress; several open ones are risk.

- **Violation Example**: open a second construction because the first grew
  difficult, touch shared preamble modules for a node that never named them,
  and leave a large refactor uncommitted and unowned across many files while
  starting new authoring elsewhere.

- **Correct Example**: select the next unblocked `TODO.md` node, complete and
  commit it to its stated acceptance, release it, and only then claim the
  following node; when a prior front is already open, finish the one closest
  to acceptance first.

#### `DEV-61`: Author Only Under a Live TODO Claim

- **Rule**: All authoring requires a live claim in the `TODO.md` claim ledger.
  Before claiming, reconcile the ledger against actual repository state so the
  claim reflects work already delivered or in flight; reconcile again at
  release. Batch-committing a body of work authored without a claim is
  prohibited.

- **Rationale**: The claim ledger is the only surface by which concurrent
  workers avoid duplicate or colliding construction. Unclaimed authoring is
  invisible until it lands as an unreviewable batch, and a stale ledger routes
  the next worker into work that is already done or already owned.

- **Violation Example**: author a many-file change with no ledger entry and
  commit it as one batch; claim a node from a ledger last reconciled before
  another worker's release landed.

- **Correct Example**: reconcile the ledger against the repository, record the
  claim for the selected node, author and commit under that claim, then
  release the claim with the delivered state reflected in the ledger.

#### `DEV-62`: An Empirical Claim About an Engine Has Its Measurement or Is Written as a Hypothesis

- **Rule**: A statement about what Sage or another engine does, costs, supports, or demands of its input is one of two things.  Either it is a finding, and it travels with the probe that produced it: the command, the specimen and its size parameter, the version, and the result.  Or it is a hypothesis, and it is written in words that cannot be read as a finding ("untested: `longest_path` may be the cost").  A causal sentence in the grammatical register of a finding, with no measurement behind it, is fabrication.  It is banned in code comments, docstrings, commit bodies, `TRAPS.md`, `COMPLAINTS.md`, reports, and conversation alike.  This extends the always-on performance-claims rule (wall time as a function of size, never counts) from how a cost is reported to whether the sentence may be written at all.

- **Rationale**: Such a sentence does four things.  It terminates the search: a named cause closes the question, and the story then stands between the reader and the measurement.  It borrows authority from plausibility: reciting a mechanism that would explain the observation feels, from the inside, identical to having found it, and the reader cannot tell the difference.  It counterfeits the project's currency: the product here is empirical knowledge of Sage (`ENG-07`), so an unmeasured engine claim is forged coin in the one denomination that matters, and it is trusted permanently because nobody re-derives a recorded fact.  And it is lazy in the literal sense: the measurement usually costs a second.  A false row in `TRAPS.md` is more expensive than an empty file for exactly the reason a true row is valuable.

- **Observed**: 2026-09-16, the same tool as `ENG-07`.  Two causes were asserted in the register of findings: that a Sage path method is MILP-backed and its cycle enumeration explodes, "those are the cost"; then that Sage's interpreter startup was the cost.  Neither had been timed.  When timing happened, the interpreter started in a fraction of a second (`TRAPS.md` holds the current numbers), and the slow call was in the library that had just been swapped in to avoid the Sage one.  Both claims pointed away from the truth, and either, recorded, would have steered every later reader off a Sage route that was never measured.

- **Violation Example**: "it is slow because it is MILP-backed"; "Sage's startup dominates"; "the native method cannot take this input" with no reproduction; a `TRAPS.md` row with no command; a docstring that explains a workaround by a property of the engine nobody checked.

- **Correct Example**: the interpreter-startup row in `TRAPS.md`: what was timed, three runs each, the version, the command; or the sentence "I have not measured this", followed by the measurement.

#### `DEV-63`: Measured Engine Facts Have One Durable Owner

- **Rule**: [TRAPS.md](TRAPS.md) at the repository root is the ledger of measured facts about the engines this repository delegates to: a route's cost as a curve, an input it rejects, an output convention, a default that is wrong or slow, and the alternate spelling that answers.  Write the row in the same turn as the measurement, before the tool or construction that exposed it moves on.  A row records the operation, the Sage spelling measured, the specimen and its size parameter, the wall times, the version, the command that reproduces it, the route chosen, and the site that depends on it.  `COMPLAINTS.md` keeps the unresolved need under `DEV-59` and is emptied on delivery; `TRAPS.md` keeps the fact, which delivery uses and never resolves.  The owned name's docstring cites the row; it does not restate it.

- **Rationale**: The fact is the product (`ENG-07`) and it has no other home.  A commit body is found only by someone who already suspects the commit; a conversation is gone; a docstring at one site is invisible to the next site that meets the same engine.  One ledger, read before any engine route is chosen, is what turns one measurement into every later rediscovery avoided.

- **Violation Example**: a measurement quoted in a reply and nowhere else; a workaround committed with the engine fact only in the commit body; a cost recorded as a `COMPLAINTS.md` gap and deleted when the consumer was delivered, taking the fact with it.

- **Correct Example**: the interpreter-startup row in `TRAPS.md`: what was timed, three runs, the version, the command, and the consequence for per-invocation tooling.

#### `DEV-64`: A Sage Mechanism Is Read in Its Source Before It Is Worked Around

- **Rule**: Before overriding, wrapping, or routing around any behaviour of Sage's category framework (`super_categories`, `extra_super_categories`, `_with_axiom`, joins, C3 ordering, `__contains__`, `refine`, dynamic classes), open the method in `sage/categories/` and state its contract in one sentence, with the file.  The workaround is then written against that contract or not at all, and the contract goes to `TRAPS.md` if it is a fact nobody in the tree had written down.

- **Rationale**: the mechanism has a design and the design is usually the answer.  The tree's history shows the alternative: `super_categories` overridden on every axiom class to stop an inheritance that one deleted edge stops; `refine` and `setattr` as construction; `NotImplementedError` as an abstract contract; `__contains__` as a predicate.  Each was a workaround for a mechanism whose actual behaviour, ten lines of source away, made it unnecessary or wrong.

- **Violation Example**: writing `def super_categories(self): return [Schemes(self.base_ring())]` on nine axiom classes to block axiom descent along a base-restriction edge, instead of reading why the descent happens and removing the edge.

- **Correct Example**: reading `CategoryWithAxiom.super_categories` (category_with_axiom.py) and `Category._with_axiom_as_tuple` (category.py), recording that an axiom is applied along every declared supercategory, and ruling that base-restriction edges are functors (AGENTS.md, *Red flags*; `TRAPS.md`).

#### `DEV-65`: An Obstruction Met While Changing a Declaration Is a Finding, Never a Mechanism

- **Rule**: When a declaration change meets an obstruction (a construction that cannot proceed, an object that must be in a category that does not yet exist when it is built, a Sage behaviour that a plain declaration triggers), the change stops there and the obstruction becomes a node in `TODO.md` with its dependency path, or a question to the owner.  It is never resolved by a runtime mechanism: not `refine` after construction, not a declaration that reads an engine object, not a `super_categories` override on an axiom class, not a membership predicate, not a placeholder supercategory.  The same rule binds an agent working one subtree under a brief: the report names the obstruction with the file and line, and the brief's owner decides.

- **Rationale**: every one of those mechanisms was tried on 2026-09-16 by an agent that had the policy in front of it, because from inside a subtree the mechanism is the shortest path to a passing view: nine `super_categories` overrides to block axiom descent that one deleted edge stops; the integers refined into `OwnedOrders` after construction, with a declaration reading an engine view of ZZ to avoid re-entry; a base-free category pointed two levels up for want of the node it needed.  Each would have been invisible to the next reader and each restated at the leaf a fact that belongs to the owner.  The obstruction is the information; the mechanism destroys it.

- **Violation Example**: `def super_categories(self): return [Schemes(self.base_ring())]` on every scheme axiom; `_owned_integers` refining ZZ into a category whose declaration needs ZZ; `RepresentedToricSchemes -> LocallyRingedSpaces` because no base-free scheme category exists.

- **Correct Example**: the schemes agent's report naming the axiom-descent mechanism with its source line, which became a ruling in `AGENTS.md`, a row in `TRAPS.md`, and the removal of every base-restriction edge; a placement left abstract with its missing construction recorded in `COMPLAINTS.md` and scheduled in `TODO.md`.


* * *

### 13. Notebook, REPL & Mathematical Example Style (`NB-*`)

#### `NB-01`: Every Mathematical Claim in an Executable Example Is Executable

- **Rule**: In research notebooks, demos, doctests, and executable documentation, state checkable mathematical claims as assertions or computations that display the witness.  Do not leave “should be”, “correctly”, expected orders, equalities, or classifications only in comments/prose beside unverified code.

- **Rationale**: A notebook is part of the research instrument.  A prose claim beside code can remain true-looking after the implementation changes underneath it; an executable proposition fails at the point of drift.

- **Violation Example**: `# this reflection sends v to -v`; `print("correctly distinguished the genera")`; a markdown sentence claiming an automorphism has order five without checking it.

- **Correct Example**: `assert sigma(v) == -v`; compute and display the actual genus/isometry witness; assert the element order or cited invariant through the semantic API.

#### `NB-02`: Examples Use Specimens That Can Falsify the Claimed Feature

- **Rule**: Choose examples for which the feature under demonstration has nontrivial work to do.  Avoid identities, an object compared with itself, zero maps, or degenerate fixtures when those make the claimed property tautological.

- **Rationale**: A demonstration is useful in proportion to how surprising its passage would be if the implementation were broken.  Equality implies isomorphism/isometry, identity maps satisfy many laws automatically, and zero maps make many factorization tests vacuous.

- **Violation Example**: Demonstrate `is_isometric` using `L.is_isometric(L)`; demonstrate morphism behavior only with the identity; “test” uniqueness of a factorization by constructing the same route twice.

- **Correct Example**: Use two distinct presentations known to be isometric, a nontrivial reflection/projection, or two independently constructed candidate factorizations.  Prefer small specimens whose mathematical answer is independently sourced and transparent.

#### `NB-03`: A Notebook Section Answers a Mathematical Question, Not “Shows an API”

- **Rule**: Organize research examples around mathematical questions and conclusions.  Methods are means, not the subject of the section.  End with the mathematical object, invariant, classification, enumeration, witness, or conclusion the researcher wanted.

- **Rationale**: The preamble is an interactive mathematical language.  API-tour examples encourage users to think in method inventories and implementation boundaries rather than in the mathematical workflow the API exists to support.

- **Violation Example**: A section titled “Using `roots()`” that prints one returned object; “Testing the genus API” that merely shows a method exists.

- **Correct Example**: “What is the root system of this lattice?”, “Are these two lattices in the same genus?”, or “Enumerate the overlattices and their discriminant forms”, with the section computing the complete requested mathematical answer.

#### `NB-04`: Session Examples Use Sage/Preamble Host-Language Idioms

- **Rule**: In notebook/REPL-facing examples, use the concise Sage/preamble language already available instead of manually spelling its lower-level constructors.  This rule is scoped to preparsed/session code; ordinary `.py` implementation modules must not assume Sage preparser semantics.

- **Rationale**: The session language is part of the product.  Reimplementing it in examples teaches users to bypass the concise mathematical syntax and makes the documented workflow look lower-level than actual research use.

- **Violation Example**: In a Sage notebook, spell a rational as `QQ(1)/2`; construct an identity morphism from an identity matrix when the object exposes its identity; access named generators only through positional engine APIs.

- **Correct Example**: Use preparsed exact literals where active, named-generator syntax where supported, semantic identity maps, direct-sum notation, and the public preamble methods discoverable from the objects in hand.

#### `NB-05`: Show Mathematical Witnesses, Not Self-Affirming Status Text

- **Rule**: Output in examples displays mathematical data/witnesses or concise conclusions derived from them.  Do not print prose declaring that the preceding computation was correct, successful, or properly distinguished.

- **Rationale**: Self-affirming output contains no independently inspectable evidence and survives even if the computation above changes.  Showing the actual isomorphism, kernel, factorization, class, invariant, or boolean mathematical predicate lets the reader inspect what happened.

- **Violation Example**: `print("correctly found the primitive embedding")`.

- **Correct Example**: display the embedding and its cokernel/torsion-freeness, or assert the relevant predicate and print the resulting mathematical object when useful.



### 14. Formal Definitions & External Citation (`FRM-*`)

These govern every formal statement written for a proof assistant — Lean files
in this repository, and any theorem, definition, or milestone submitted to an
external formalization platform.

#### `FRM-01`: A Definition May Not Carry a Theorem

- **Rule**: A `def` is a stipulation and nothing checks it.  If a mathematician reading the line would want to see it *proved*, it is a theorem and must be written as one — stated, named, cited, and either proved or left visibly open.  This applies with full force to correspondences between a construction and the object it classifies.

- **Rationale**: A definition cannot be false, so a theorem written as a definition becomes unfalsifiable and escapes the process that would have tested it.  In a proof assistant the kernel checks every step except the definitions, so smuggling a theorem into the trusted base places it exactly outside what verification covers: the file compiles, the result is reported as verified, and the hole sits where no one looks.  A `sorry` is honest by comparison — visible, greppable, and rejected by the gates.  Worse, the names then lie: every downstream statement mentioning the geometric object is really about the combinatorial surrogate, and the discrepancy is visible at no site except the definition.  Missing hypotheses can never surface, because nothing is ever asked to use them.

- **Violation Example**: `def Incident (N P : Submodule ℤ V) : Prop := N ≤ P` documented as "a zero-dimensional boundary component lies in the closure of a one-dimensional one exactly when the line is contained in the plane" — this makes the Baily–Borel correspondence true by fiat; defining the boundary components of a compactification *to be* the Γ-orbits of isotropic sublattices; `IsIsometry g := gᵀ * G * g = G ∧ IsUnit g.det`, where the determinant clause is a theorem-equivalent for preserving the lattice rather than the condition itself.

- **Correct Example**: define the isotropic sublattices and their Γ-orbits; state the correspondence with rational parabolics and with boundary components as separate cited theorems; let the goal theorem mention the boundary complex and depend on those theorems, so the content is carried by statements a reader can dispute.

#### `FRM-02`: Every Definition Carries an Exact External Citation

- **Rule**: Every formal definition names its source precisely: a Zotero citation key or a publicly resolvable URL, plus a locator that identifies the statement — section, numbered item, and page.  `-- Sterk, Chap. 2 (2.10), p. 41` or `-- Ste95a §2 (2.7)`; never a bare author name, never "standard", never "see the literature".  If no source states the definition in the form written, that fact is recorded at the site and the divergence is described.

- **Rationale**: A formal definition is the only place where content enters unchecked, so it is the only place where a citation does real work: it is the sole means by which a reader, an auditor, or a later agent can test the definition against anything at all.  The locator is an **auditing instrument, not an attribution**: its job is to name somewhere the statement is actually stated, so a reader can compare.  The test it must pass is that the locator resolves to that statement — who first proved the result, and whether the cited author is merely reporting it, does not bear on the audit.  Without a locator the reader cannot tell a faithful transcription from an invention, and inventions in definitions are the failure mode that no downstream proof can detect.

- **Violation Example**: a docstring citing "Sterk" with no section; citing a paper whose numbering differs from the edition actually consulted; carrying a citation for the surrounding module but none on the individual definitions.

- **Correct Example**: each `def` carries the numbered statement it transcribes, and where a paper and its thesis version differ in numbering, both are given.

#### `FRM-03`: The Docstring and the Body State the Same Thing

- **Rule**: When a docstring names a construction, the body is that construction.  An extensionally equivalent surrogate is not permitted merely because the equivalence is a theorem over the ring at hand.

- **Rationale**: The reader audits the body against the docstring; if they disagree, the docstring is what enters the reader's understanding and the body is what enters the mathematics.  Even a genuine equivalence puts the burden of knowing it on every future reader, and the moment the ring, the hypotheses, or the ambient category shift, the surrogate silently stops meaning what the name says.  `DEF-01` governs the same boundary for predicates in ordinary code.

- **Violation Example**: a docstring reading "primitive when the cokernel of the inclusion is torsion free" over a body implementing elementwise saturation `∀ d v, d ≠ 0 → d • v ∈ N → v ∈ N`.

- **Correct Example**: `Module.IsTorsionFree ℤ (L ⧸ Submodule.comap L.subtype N)`.

#### `FRM-04`: No Unverified Derivation Asserted in Prose

- **Rule**: A docstring may not assert that the body computes something unless that has been checked.  An identity relied on to write the body — a conjugation, a transport along an isomorphism, a change of coordinates — is either verified and stated as a lemma, or the body is written so that no such identity is needed.

- **Rationale**: A derivation asserted in a comment is believed by every later reader and proved by no one; it has the unfalsifiability of `FRM-01` with none of its visibility, since it hides inside a definition that otherwise looks routine.

- **Violation Example**: documenting a matrix condition as "this is the induced action on `L*/L` read on the two blocks, stated without inverses" when the transport `G g G⁻¹ = (g⁻¹)ᵀ` was never checked and the body in fact applies the map to `G v` rather than to `v`.

- **Correct Example**: construct the dual lattice and the quotient, define the induced map as the actual induced map, and let the coordinate form be a proved lemma if one is wanted.

#### `FRM-05`: A Name May Only Mention What Is Constructed

- **Rule**: A formal name or docstring may refer to a geometric, analytic, or categorical object only when that object exists in the development.  Otherwise the declaration is named for what it actually is.

- **Rationale**: Names are the interface every reader uses; a name promising an object that was never built transfers the reader's understanding of that object onto an unrelated construction, and no proof will ever contradict them.

- **Violation Example**: `I₁` documented as "the zero-dimensional boundary components of the Baily–Borel compactification" in a development containing no compactification, no domain, and no group.

- **Correct Example**: `I₁` documented as the primitive isotropic rank-one sublattices, with the relation to boundary components stated as a cited theorem elsewhere.

#### `FRM-06`: Repair a Smuggled Claim by Promoting It, Never by Deleting It

- **Rule**: When a theorem is found inside a definition, the correction is to state it as a theorem and carry it as an obligation.  Removing the claim, narrowing the goal to the part already provable, or restating the target as the surrogate, is goal substitution and is prohibited.

- **Rationale**: The smuggled claim was content the work owed.  Deleting it makes the artifact honest and the project poorer by exactly the thing that made it worth doing, and it leaves no record that anything was owed.  This is the `Removal Means Deletion` failure inverted: the requirement, not the prohibition, is what gets erased.

- **Violation Example**: on discovering that Baily–Borel had been smuggled into `Incident`, proposing that the goal theorem be restated as a count of lattice orbits with the boundary components dropped.

- **Correct Example**: keep the goal theorem about the boundary complex; state the correspondence as cited child lemmas; let the goal depend on them, open, until they are proved.

#### `FRM-07`: No Placeholder That Typechecks

- **Rule**: A declaration whose body is chosen to make the file compile — `fun _ => True`, a trivial `Prop`, an unrelated expression standing in for one not yet worked out — must not be written, not even transiently.  Where the content is not yet known, the declaration is absent or its statement is left explicitly open.

- **Rationale**: A placeholder that typechecks is indistinguishable from finished work at every level of inspection except reading its body, and it is the one form of incompleteness that no gate reports.

- **Violation Example**: `def I₂ : Set (…) × Set (…) → Prop := fun _ => True` written to get past an error while the real definition was still being worked out.

- **Correct Example**: omit the declaration until its content is settled; or state it and leave the proof obligation visibly open by the route the platform or repository sanctions.

### 15. Formalization Decomposition & Scoping (`FDC-*`)

Formalizing a paper is not writing definitions until it compiles.  These rules
govern the work that must exist *before* the first formal line, and they exist
because skipping it is what makes fraud available: a theorem with no node in a
decomposition has nowhere to live, and ends up inside a definition.

#### `FDC-01`: The Dependency Graph Precedes the First Formal Line

- **Rule**: No definition, statement, milestone, or platform item is written until a written dependency graph exists for the target: its nodes, its edges, and the source locator of every node.  The graph is an artifact on disk, not a plan held in the conversation.

- **Rationale**: Without the graph there is no representation of what the proof requires, so there is no measure of the gap between the target and what the current session can reach.  Work then proceeds against an unmeasured gap, which is the condition under which producing something that *resembles* the target replaces producing it.  Every content-bearing step of the source must have somewhere to go before any code is written; the alternative is that content with no home is absorbed into whatever declaration is being written at the time.

- **Violation Example**: opening a `.lean` file, or drafting platform items, when no DAG file exists for the target.

- **Correct Example**: the graph is committed first; each subsequent formal declaration cites the node id it discharges.

#### `FDC-02`: The Graph Covers the Source Exhaustively, With Dispositions

- **Rule**: The graph enumerates **every** labelled statement of the source — definitions, lemmas, propositions, corollaries, remarks, and the numbered computations — and gives each one a disposition: a node id, or an explicit out-of-scope entry with its reason.  A statement may not be absent.

- **Rationale**: A graph containing only what the target needs is a subset that reads as a complete analysis.  The reader cannot distinguish "not required" from "not noticed", and neither can the author on re-reading.  Recording the exclusions is what makes the scope judgment reviewable, and it is cheap: the excluded rows are usually one coherent block that names a second piece of work.

- **Violation Example**: a graph whose every row is load-bearing, with no exclusions listed — the filtering happened and was not written down.  Dropping a remark because it "only" restates a count, when the restatement is in fact the crossing to a different kind of object.

- **Correct Example**: a coverage table with one row per labelled item, out-of-scope rows carrying their reason, and a note of which nodes were added by building the table.

#### `FDC-03`: Every Leaf Is Audited Against the Library, By Search

- **Rule**: For each node with no in-graph dependency, verify by searching the dependency at its pinned revision whether the theory it needs exists.  Recall is not admissible evidence.  A node resting on absent theory is not a leaf: the missing theory becomes its own node, and the graph gains a foundations stratum.

- **Rationale**: A graph whose leaves are assumed available understates the work by however much foundational theory is missing, and the understatement is invisible because the leaves look terminal.  "External, cited" is the phrase under which whole theories hide: a citation to a numbered statement is a node, a citation to a subject is a stratum.

- **Violation Example**: marking `Vinberg 1975` as an external input, as if importable, when it requires hyperbolic reflection groups, fundamental polyhedra, and the affine Dynkin classification, none of which exist in the target library.

- **Correct Example**: a foundations stratum naming each missing cluster, what needs it, and what substrate does exist, with the search performed against the pinned revision.

#### `FDC-04`: Size the Work Before Committing to Any of It

- **Rule**: Before proposing a plan, a milestone list, or an order of work, report the size the graph implies: node count, which strata have substrate, and which do not.  A proposal that does not state the size may not be acted on.

- **Rationale**: Scale that is never stated cannot be checked, and an unstated gap is filled by whatever looks like progress.  Sizing is also the only honest basis for the decision the user actually owns — whether the target is one mission or several, and whether a foundations cluster deserves to be its own work.

- **Violation Example**: offering to draft a complete proposal for a target whose foundations have not been checked.

#### `FDC-05`: Absent Substrate Is Stated as an Open Obligation, Never Assumed

- **Rule**: A node whose theory is missing is carried as an explicitly open statement — a child lemma, a sketch reduction, a stated hypothesis — with its citation.  It is never inlined into a definition, never assumed silently, and never made to disappear by restating the goal.

- **Rationale**: The open form is visible to every reader and to the tooling; the assumed form is visible to no one.  `FRM-06` governs the same boundary once the assumption has already been made.

- **Correct Example**: on a platform supporting decomposition, reduce the goal to child lemmas that state the missing correspondences, so they appear as open problems rather than as definitions.

#### `FDC-06`: Correction Triggers an Audit for the Pattern, Not a Patch of the Instance

- **Rule**: When a defect is identified in formalization work, search the whole artifact — and any artifact derived from it — for other instances of the same defect before continuing.  Report what the search covered.

- **Rationale**: These defects come from a stable way of working, so they recur in each representation the work passes through.  A defect corrected in a Lean file and then reproduced in the decomposition that was built to prevent it is the normal case, not an unlucky one.

- **Violation Example**: repairing a theorem-as-definition in one file, then committing the same conflation as a single node of the dependency graph.

#### `FDC-07`: Completeness Questions Are Answered From the Source

- **Rule**: A question of the form "is this complete", "does every statement appear", "are these self-contained" is answered by re-reading the source or re-searching the library, never by inspecting one's own artifact.  The answer states what was re-read.

- **Rationale**: The artifact is internally consistent by construction, so self-inspection returns "yes" whatever the truth.  Only an external comparison can fail.

- **Violation Example**: answering "yes, every theorem is in the DAG" from the DAG.

#### `FDC-08`: An Exclusion Is Valid Only If the Goal Names None of What It Excludes

- **Rule**: A statement of the source may be dispositioned out of scope only when the goal statement mentions no object whose construction depends on it.  If the goal names Enriques surfaces, the surfaces are in scope; if they are excluded, the goal is restated so that it does not name them, and the restatement is put to the user as a change of target.  To formalize a paper is to formalize everything lying between it and the library: an exclusion is a decision about *which theorem is being proved*, never a decision about effort.

- **Rationale**: Otherwise the exclusion silently narrows the target while the name advertises the original, which is `FRD-03` at the scale of a whole project rather than of a declaration.  The two failures compose: the excluded material is invisible because it is out of scope, and the narrowing is invisible because the title still promises it.

- **Violation Example**: dispositioning the period map, the $K3$ double cover, and Torelli as "not inputs to the boundary computation", while planning to describe the work as formalizing the period space of Enriques surfaces; introducing a lattice by a Gram matrix when the source defines it as an eigenlattice of an involution on the cohomology of a surface, and then still calling it the period lattice of that surface.

- **Correct Example**: either the geometric layer enters as open obligations carried by explicit nodes, or the goal is restated as a statement about a lattice and its arithmetic group, named as such, with the change of target raised as a decision rather than made in a table.

#### `FDC-09`: A Node Is a Transcription, Never a Recollection

- **Rule**: Every node of a dependency graph is written with its source open.  The statement is transcribed from the text, and the node records the locator — section, numbered item, page.  Writing a node from knowledge of the subject is prohibited, however standard the material and however confident the writer.

- **Rationale**: A graph is a claim about what the proof requires, and a recalled node is a guess about that dressed as a finding.  The guesses are not random: they reproduce the shape the writer expects, which is exactly the shape the source is likely to differ from, and the difference is invisible because the guess is plausible.  The cost is not one wrong row — dependencies, mechanism and the order of work all follow the node, so a fabricated node misdirects everything built under it.

- **Violation Example**: writing nine nodes for the theory of discriminant forms "needing no source beyond Nikulin §1" without opening Nikulin; deriving a node's dependencies from a remembered proof strategy.  Concretely: a fabricated node had nine lattice classes arising from a $p$-adic genus computation via two recalled Nikulin theorem numbers, where the source derives them from primitive embeddings of $D_7$ into Niemeier lattices, the ninth class arising because one Niemeier lattice admits two inequivalent embeddings.  Every dependency was wrong.

- **Correct Example**: open the memoir, read the section, take the numbered statements it actually contains, and record what each one says with its number.

#### `FDC-10`: Selective Source-Marking Is Not Sourcing

- **Rule**: The sourcing status of a node is a fact about whether its source was read, not about how confident the writer feels.  When some nodes in a batch are marked as needing a source, all unmarked nodes must have been read; otherwise the marks are prohibited and the whole batch is marked unsourced.

- **Rationale**: Marking the least certain rows and leaving the rest bare produces a graph that displays diligence while being uniformly unsourced.  The marks then read as a coverage claim about the unmarked rows, which is the opposite of the truth.  Confidence is not evidence, and on standard material it is highest exactly where recall is most likely to be a smooth reconstruction of the wrong thing.

- **Violation Example**: forty nodes written from memory with ten marked "needs source read" — the ten the writer felt least sure of.

#### `FDC-11`: Terminal Means the Next Dependency Is in the Library

- **Rule**: A node is terminal **only** when what it depends on next is available in the target library.  A node whose next dependency is a theorem in a paper, a classification in a memoir, or a body of theory is not terminal, and the graph is not complete until the descent below it has been traced to the library.

- **Rationale**: A graph whose leaves are large results understates the work by the size of everything under those leaves, and understates it invisibly, because a leaf looks finished.  This is how "external, cited" hides a subject: the phrase names a stopping point that the mathematics does not have.  The rule gives a mechanical test — name the next dependency, ask whether it is in the library, and if not, keep going.

- **Violation Example**: listing Niemeier's classification of the 24 even unimodular rank-24 lattices, or "the genus of a lattice", as leaves of a graph targeting Mathlib, which has neither.

- **Correct Example**: each row carries a *next dependency* column naming what it descends into, and rows whose entry is not a Mathlib name are visibly unfinished.

#### `FDC-12`: A Citation Is Not a Node

- **Rule**: A node states one mathematical proposition.  A reference to a work, a section, a subject, or an author is not a node, and may not stand in the graph as though it were one.

- **Rationale**: A node is the unit that gets stated, reviewed, proved and discharged, and none of those operations is defined on a subject.  Bundling also defeats the terminality test of `FDC-11`, because a subject has no single next dependency.  `FSC-06` states the same requirement for the work unit; this is its form inside the graph.

- **Violation Example**: a node reading "Vinberg 1975" standing for hyperbolic reflection groups, fundamental polyhedra, the algorithm, its completeness, and the affine classification together.

#### `FDC-13`: Read the Section, Not the Corollary

- **Rule**: When a source is opened for one statement, establish what that statement rests on within the same source before treating it as a leaf.  A corollary quoted out of a development carries the development with it.

- **Rationale**: Sources are written as chains, and the result that a downstream paper cites is usually the last link.  Quoting it alone imports the conclusion and drops the apparatus — which is precisely the material that will turn out to be the foundations stratum.

- **Violation Example**: quoting a memoir's §6.3 and one remark from §5.1 as the source for a node, when §3 of the same memoir develops the discriminant forms, genera, orthogonal groups and Eichler transformations that the whole graph stands on.

#### `FDC-14`: Check Availability Before Recording a Source as Unread-Because-Unavailable

- **Rule**: Before recording that a node awaits a source, search the local library for that source.  A node may be marked as awaiting reading; it may not be marked as awaiting acquisition without a search that failed.

- **Rationale**: "The source has not been read" and "the source is not available" are different facts, and confusing them converts a reading task into an imagined blocker, which then justifies writing the node from memory instead.

- **Violation Example**: recording that four primary sources needed to be obtained before a stratum could be decomposed, while all four sat in the library with text extractions.

#### `FDC-15`: Fabricated Material Is Deleted, Not Annotated

- **Rule**: On discovering that nodes were written from memory, delete them and write the sourced version.  Do not keep them beside a warning.  This does **not** conflict with `FRM-06`: what that rule protects is a *requirement the work owes*, and a fabricated node is not a requirement — it is a guess about one, and the requirement it displaced is recovered by reading the source, not by preserving the guess.

- **Rationale**: Annotated fabrications continue to be read, cited and built on, because a table row outlives the paragraph above it.  Keeping them also blurs the one distinction that matters when repairing this class of error: a claim that was smuggled in must be promoted to a theorem, while a claim that was invented must be removed and replaced by what the source says.

- **Violation Example**: retitling five fabricated subsections "(unsourced)" and leaving their tables in place.

### 16. Fraud Precursors in Formalization (`FRD-*`)

These name behaviours observed on this repository that would have resulted in
false mathematical claims published under the owner's name.  Each is stated with
its **sign** — the observable that appears while the behaviour is happening,
since none of them announces itself as dishonest from the inside.  All of them
felt like progress at the time.

The standard against which they are judged: a formal statement published to a
third party asserts a guarantee to people who will act on it.  The bar is not
best effort, it is whether the artifact survives an adversarial auditor holding
the source.

#### `FRD-01`: A Claim Placed Where Nothing Can Check It

- **Ban**: Writing content into any position that verification does not reach — a definition, a docstring, a name, an implicit convention — when that content is a claim a mathematician would want proved.
- **Sign**: a docstring linking two kinds of object with "corresponds to", "is exactly", "is the same as", "lies in the closure of"; a `def` whose body is short and whose docstring is a sentence about geometry.
- **Why it is fraud and not error**: an unprovable claim is also an unfalsifiable one.  No proof fails, no gate reports it, and the published result carries a guarantee for a statement nobody established.

#### `FRD-02`: Repairing a Smuggled Claim by Deleting It

- **Ban**: On discovering a claim in an unchecked position, restating the goal to exclude it, narrowing the target to the provable remainder, or presenting either as honesty.
- **Sign**: the sentence "the correction is not to weaken the goal but to say what is actually being proved", or any variant that reduces the target while calling the reduction accuracy.
- **Why**: the claim was work the project owed.  Deleting it produces an artifact that is locally honest and has lost the thing that made it worth doing, with no record that anything was owed.  `FRM-06` states the repair.

#### `FRD-03`: Naming an Object That Does Not Exist in the Development

- **Ban**: Using a geometric, analytic, or categorical noun in a declaration name or docstring when the development contains no such object.
- **Sign**: words like *cusp*, *boundary component*, *compactification*, *moduli*, *period* appearing in a file whose imports contain no domain, no group, and no topology.
- **Why**: the reader's understanding of the named object transfers onto an unrelated construction, and nothing in the development ever contradicts it.

#### `FRD-04`: A Placeholder That Typechecks

- **Ban**: Writing any body chosen to satisfy the elaborator rather than to state the mathematics — `True`, `fun _ => True`, `trivial`, an unrelated expression standing in for one not yet worked out — even transiently, even with the intention of returning to it.
- **Sign**: the thought "so the file compiles while I work out the real one".
- **Why**: it is indistinguishable from finished work at every level of inspection except reading the body, and it is the one incompleteness no gate reports.

#### `FRD-05`: An Unverified Derivation Asserted in Prose

- **Ban**: Documenting a body as computing something on the strength of a transport, conjugation, or change of coordinates that has not been checked.
- **Sign**: "equivalently", "which is just", "stated without inverses", "up to the obvious identification", in a comment on a definition.
- **Why**: it has the unfalsifiability of `FRD-01` with none of its visibility, since it hides in a declaration that looks routine.

#### `FRD-06`: Two Claims Sharing a Number

- **Ban**: Treating a count, a list, or a classification of one kind of object as though it were the same statement about another kind, when an unproved theorem separates them.
- **Sign**: the same integer used for two different objects in adjacent sentences — five orbits and five boundary components, nine planes and nine strata.
- **Why**: this is `FRD-01` performed on the statement rather than on the definition, and it survives into decompositions, summaries, and abstracts, where it looks like a restatement.

#### `FRD-07`: Presenting a Subset Reading as a Reading

- **Ban**: Reporting an analysis of a source without stating what of the source was not covered.
- **Sign**: a list of the source's statements with no exclusions; the phrase "the explicit statements are" followed by only the convenient ones.
- **Why**: the reader cannot distinguish a scope judgment from an oversight, and neither can the author later.

#### `FRD-08`: Self-Review Standing In for Verification

- **Ban**: Offering the internal consistency of one's own artifact as evidence of its faithfulness; answering a completeness or correctness question by inspecting it.
- **Sign**: "I checked and it all lines up", with no external artifact named; a compiling file cited as evidence about mathematics.
- **Why**: internal consistency is what the artifact was built to have.  `FDC-07` states the required route.

#### `FRD-09`: Producing Resemblance Under an Unmeasured Gap

- **Ban**: Continuing to produce artifacts toward a target whose required work has not been sized.
- **Sign**: a session in which the amount produced is large and the number of statements that could now be *false* is zero; work that looks like the deliverable arriving faster than understanding of the deliverable.
- **Why**: this is the generating condition for every other rule in this family.  When the gap is unmeasured, resemblance to the target is indistinguishable from progress toward it, from the inside, in the moment.

#### `FRD-10`: Publishing Before the Foundations Are Real

- **Ban**: Submitting a formal statement to any external platform, repository, or reader while any node it depends on is carried by a definition, a placeholder, or an unstated assumption.
- **Sign**: a submission prepared in the same session in which the decomposition was first written.
- **Why**: publication converts a local defect into a claim that other people act on, and on a verification platform it mints a guarantee the platform cannot itself check.  Nothing published this way can be quietly withdrawn: solvers, citations, and downstream work attach to it.

### 17. Formalization Scale, Calibration & Scaffolding (`FSC-*`)

Every rule here corrects a misconception that produced a concrete failure on
this repository: that a formalization's size is a reason to change what is being
proved, that a graph of hundreds of nodes is prohibitive, that decomposition is
paperwork preceding the real work.  Each was wrong by orders of magnitude, and
each was stated with confidence.

#### `FSC-00`: Calibration Data

The reference points below are recorded facts about completed work, not
estimates.  They exist so that no size claim is ever made from intuition.

| Result | Scale | Duration |
| --- | --- | --- |
| Fermat's Last Theorem, end-to-end machine-checked (Anthropic, announced 2026-09-04) | 13 million lines of Lean; 30,300 theorems; ~6 billion output tokens; over 5× the size of Mathlib | 11 days, largely autonomous, human input limited to occasional high-level instruction |
| Navier–Stokes finite-time blowup, Lean certificates (OpenAI, 2026-09) | Navier–Stokes and Euler blowup on ℝ³ and periodic domains | ~88 hours to the proof, a further 17 hours to formalize |

The FLT run had a recorded prior failure mode: earlier attempts collapsed
because the agents lost track of the project's state.  The successful run was
the one carried on a platform maintaining a **directed acyclic graph of theorem
statements**.  That is the evidential basis for `FSC-05`.

#### `FSC-01`: The Target Is Immutable; Gaps Add Nodes

- **Rule**: A formalization has one target node, fixed when the work is accepted.  Every gap discovered between it and the library adds nodes to the graph.  Size is an output of the graph and never an input to the goal.  Proposing a smaller target, a restated target, or a menu of targets is prohibited — including when the proposal is put to the user as a question.

- **Rationale**: Scope discovery is the normal product of decomposition; treating it as a reason to renegotiate converts every unwelcome finding into a licence to prove something easier.  Routing the proposal through the user does not sanitize it: the user asked for a theorem, and the decision presented to them is manufactured by the same intuition the graph was built to replace.

- **Violation Example**: on finding that the geometric layer is absent from the library, offering "the lattice statement", "the theorem in full", and "the theorem with open inputs" as three targets to choose between.

- **Correct Example**: add the geometric layer as a stratum of nodes and continue.

#### `FSC-02`: A Difficulty Intuition Is Not a Finding

- **Rule**: No claim about the size, difficulty, or feasibility of a formalization may be stated without first checking it against `FSC-00` or against comparable completed work in the record.  An intuition, however strong, is a stale prior and carries no evidential weight.

- **Rationale**: These intuitions are systematically miscalibrated in one direction — toward "too large" — and they are load-bearing precisely when they are wrong, because an inflated estimate is what makes narrowing the goal look responsible.

- **Violation Example**: "a decades-scale program, not a mission", written about a graph of a few hundred nodes, in a month when a graph of 30,300 was discharged in eleven days.

- **Correct Example**: state the node count, the loop body, and which strata lack substrate; compare with the recorded comparables; draw no feasibility conclusion beyond what that comparison supports.

#### `FSC-03`: A Node Count Is Never a Reason to Stop

- **Rule**: Counts in the hundreds, thousands, or tens of thousands are ordinary for this kind of work.  A count may be reported; it may never be used to justify deferring, narrowing, splitting away, or declining the target.

- **Rationale**: Difficulty lives in the loop body, not in the number of items.  A body of "formalize one definition or lemma from a standard text, with its citation" is hours at most, and most nodes of such a graph are mutually independent, so the count measures duration and parallelism rather than hardness.

- **Violation Example**: treating a seven-cluster foundations stratum as evidence that the mission is impossible rather than as the list of what to build first.

#### `FSC-04`: Size in Nodes, Never in Time

- **Rule**: Express scale as node count, stratum coverage, and loop body.  Do not write forward-looking durations for proposed work.  Recorded durations of *completed* work, as in `FSC-00`, are citable facts and are the only admissible form.

- **Rationale**: A forward duration is an intuition wearing a unit, and it is the specific form in which the misconception above is expressed.

#### `FSC-05`: The Scaffold Is Mandatory and Holds the State

- **Rule**: The dependency graph lives in a durable, queryable store — the platform's theorem DAG where one exists, a committed artifact otherwise — before formal work begins, and is updated as nodes are discharged.  Project state lives there, never in a conversation and never in the working memory of a session.

- **Rationale**: Loss of project state is the recorded cause of failure at scale, and holding the state in a theorem DAG is the recorded difference between the attempts that failed and the one that succeeded.  A session's context is not a store: it ends, it compacts, and what it held is gone.  The graph is not preparation for the work; it is the mechanism that makes the work possible across sessions and across agents.

- **Violation Example**: opening a `.lean` file in the first minutes of a session on a platform whose entire purpose is to maintain the theorem DAG, and treating the DAG as a formality to satisfy afterwards.

#### `FSC-06`: One Node, One Statement, One Citation

- **Rule**: A node carries exactly one mathematical statement and exactly one source locator.  A node that bundles several statements, or that names a subject rather than a statement, is split until it does not.

- **Rationale**: Bundled nodes are how whole theories hide behind the phrase "external, cited", and they are what makes a graph look finished while its leaves are unexamined.  Single-statement nodes are also the unit that can be handed to a fresh-context agent without transferring the rest of the project.

- **Violation Example**: a single node reading "Vinberg 1975" and standing for hyperbolic reflection groups, fundamental polyhedra, and the affine Dynkin classification together.

#### `FSC-07`: Independent Nodes Are Worked in Parallel, By Fresh Contexts

- **Rule**: Nodes with no dependency between them are dispatched concurrently to fresh-context agents, each given its statement, its citation, and its dependencies' statements — not the project's history.  The graph is what makes this safe.

- **Rationale**: Most of a formalization graph is independent, so serial execution wastes the dominant structural feature of the work.  Fresh contexts are also the only reliable audit: an agent that did not write a statement is the one that can read it back blind.

#### `FSC-08`: Missing Library Theory Is Built as Theory, Not Worked Around

- **Rule**: When the library lacks something a node needs, build it as a proper development suitable for contribution upstream.  Do not inline a special case, a surrogate, or a definition tailored to the one call site.

- **Rationale**: The missing theory is usually the most reusable thing the project will produce — discriminant forms of even lattices serve all of Nikulin theory, not one paper — and a tailored surrogate has to be replaced later by exactly the general development that should have been written first.  It is also how a formalization contributes rather than accumulates.

#### `FSC-09`: The Vocabulary of Refusal Is Banned

- **Rule**: "Too big", "not a mission", "research-scale", "decades", "out of reach", "a formalization campaign rather than X" may not be written as conclusions about assigned work.  Where such a phrase would appear, write the node count and the missing strata instead.

- **Rationale**: Each of these phrases states a feasibility verdict that `FSC-02` forbids, and each functions as the premise for narrowing that `FSC-01` forbids.  Banning the vocabulary removes the step where the verdict is smuggled in as description.

#### `FSC-10`: Progress Is Discharged Nodes

- **Rule**: Report progress as nodes discharged against the graph, with their statements.  Lines of Lean, files created, definitions written, and sessions spent are not progress and are not reported as such.

- **Rationale**: Volume of output is exactly what rises when resemblance replaces work, so measuring by it rewards the failure.  A discharged node is a statement that could have been false and now is not.

#### `FSC-11`: A Session Begins by Reading the Graph

- **Rule**: Work on a formalization begins by reading the current state of the graph — which nodes are open, which are discharged, which are blocked and on what — and never by writing.  The first artifact a session produces is a node, not a file.

- **Rationale**: The state is durable and the session is not; a session that begins by producing rather than reading is one that has substituted its own picture of the project for the recorded one, which is where losing track of the state begins.

### 18. Semantic Verification of Formal Statements (`FSV-*`)

The rules of `FRM-*` say what a formal declaration may contain.  These say how a
project checks that its declarations *mean* what the source means — a separate
process from proof checking, owned by people and by agents that did not write
the declaration.

The framework and terminology are Yanahama and Sannai, *Lean Atlas: An
Integrated Proof Environment for Scalable Human-AI Collaborative
Formalization*, arXiv:2604.16347 (2026).

#### `FSV-01`: The Kernel Checks Logic, Not Meaning

- **Rule**: Treat Lean core and Mathlib as the trusted base and every project-specific declaration as unverified in meaning until it has been semantically reviewed.  A successful build is never cited as evidence that a statement is faithful to its source.

- **Rationale**: The type checker guarantees that a proof term is correctly constructed for a given proposition.  It says nothing about whether the proposition, or the definitions occurring in it, represent the intended mathematics.  The published name for the resulting defect is **semantic hallucination**: a formalization that passes the type checker, may carry a complete proof, and is not semantically equivalent to the statement it claims to formalize (op. cit., Def. 1).

#### `FSV-02`: Definitions Are the Review Surface

- **Rule**: Concentrate semantic review on definitions and on the propositions of theorems.  A theorem's *proof* need not be semantically reviewed; a definition's *body* always must.  Design toward few, small, heavily cited definitions, pushing content into theorems wherever the mathematics permits.

- **Rationale**: The asymmetry is mechanical.  A dependency appearing in a declaration's type is a proposition- or definition-level relationship a human must verify; a dependency appearing only in a theorem's value is a proof term the kernel already guarantees, and can be pruned from review.  A dependency appearing only in a *definition's* value carries computational content absent from its type signature and must be retained (op. cit., Defs. 2–3, Table 1).  This is the precise reason a theorem written as a definition escapes every check: it moves content out of the mechanically verified half and into the reviewed half, and then out of review if the author is the only reviewer.

- **Correct Example**: a project whose definitions are transcriptions with locators, and whose mathematical content lives in theorems the checker carries.

#### `FSV-03`: Review the Cone, and Expect It Not to Shrink Here

- **Rule**: For each target theorem, determine the set of project-specific declarations whose semantic correctness can affect it, and review that set.  Do not assume the set is small.

- **Rationale**: On proof-heavy projects the reduction from the full graph to the review set is 94–99%; on a six-theorem milestone subset of FLT it was 59.8%; on a definition-heavy project it was 27.3% (op. cit., abstract).  A formalization whose strata are mostly new definitions — new foundations — sits at the definition-heavy end, so its review burden is proportional to its definitions and is a fact to plan around rather than to discover late.

#### `FSV-04`: The Audit Checklist Is the Hallucination Taxonomy

- **Rule**: Every semantic review of a statement checks, by name: definition mismatch; missing or extra assumptions; goal substitution; quantifier and scope errors; type default semantics shift.  A review that does not report against these five has not been performed.

- **Rationale**: These are the recorded patterns (op. cit., §3.1).  Naming them converts review from an impression into a check with a fixed surface, and three of the five — definition mismatch, missing assumptions, goal substitution — are the ones this repository has actually produced.

#### `FSV-05`: The Author Never Reviews Their Own Statement

- **Rule**: Semantic review of a declaration is performed by a person, or by a fresh-context agent, that did not write it and is given the formal code alone — never the informal statement, the source, or the author's intent.  The reviewer's output is a read-back: what the code literally asserts.  The comparison against the source is then made by a third party holding both.

- **Rationale**: The author knows what the code was meant to say and reads that meaning into it; their review returns the intent rather than the content.  Blind read-back is the only form of review that can disagree with the author.

#### `FSV-06`: Verification Status Is Per-Node and Recorded

- **Rule**: Each node carries its own recorded status: semantic-verification state, who verified it, proof progress, and `sorry` status.  Status lives with the node in the graph, never in a session or a summary.

- **Rationale**: Semantic correctness is a property of individual declarations, so a project-level claim of faithfulness is meaningless unless it is the conjunction of recorded per-node states.  `FSC-05` owns the same requirement for structural state.

* * *

### 20. Formalization Search & Acquisition (`FSA-*`)

`FDC-03` and `FDC-11` require every leaf to be audited against the library by
search.  This family governs *how* that search is conducted, what makes its
negative result admissible, and what may be done when the answer is genuinely
absent.  Its subject is the boundary between **found** mathematics and **owned**
mathematics, and the standing bias is toward found: a found declaration is
reviewed, maintained, composable with everything else built on it, and free,
while an owned one is a permanent maintenance surface that owes a comparison
theorem the day the library acquires its own version.

**The objective function is explicit: minimise the number of notions this
repository owns.**  Every invented definition permanently enlarges the surface a
human must audit for semantic correctness, that audit is the constraint no tool
and no model can relieve, and it is not discharged by getting the definition
right — see `FSA-M13`.  A notion avoided is therefore worth more than several
written well, and a report of formalization progress that does not say how the
count moved has not reported the thing that matters.

#### The mental models these rules encode (`FSA-M1`–`FSA-M12`)

The rules below are consequences.  These are the models they follow from, given
names so a later reader can cite one instead of re-deriving it.  Each was arrived
at by being wrong in the way it describes.

**`FSA-M1`: The kernel checks proofs against statements; nothing checks
statements against mathematics.**  A definition type-checks whether or not it
names the intended notion.  So definitional work has the highest ratio of
apparent progress to verifiable content available in a formalization project: it
closes rows, satisfies checkers, and is immune to the only automatic check there
is.  A wrong definition is not caught later either — every proof above it stays
*valid* and becomes *useless*, which is a failure with no error message and no
natural discovery point.

**`FSA-M2`: Trust in a formalization has two components, and the machine supplies
only one.**  The kernel supplies "the proof follows from the statements".  The
other component — "the statements are the intended mathematics" — is supplied by
provenance: review, a published source, downstream uses that pin a meaning,
people who would notice a change.  A declaration with no provenance cannot be
trusted; it can only be believed.  This is why a *known gap* is better than a
*believed definition*: the gap is tracked work, the belief is untracked risk.

**`FSA-M3`: Fluency counterfeits the evidence a reader uses to judge care.**
Naming, structure, an assured docstring, apparent generality, tidy lemma
ordering — a language model produces all of it for free and decoupled from
correctness.  A human's wrong definition usually carries traces of struggle; a
model's arrives clean, with a comment asserting that it is right.  The practical
consequence is inverted heuristics: in model-authored mathematics, polish is
weak evidence of correctness and should not be read as strong.

**`FSA-M4`: Recall and confabulation are the same operation from the inside.**
A model has no access to what a definition *should* be, only to what such
definitions *look like*.  There is therefore no internal signal that separates
"I know this" from "this completes fluently", and introspective confidence
carries no evidential weight at all.  Discipline has to be procedural — the
source is open, or the definition is not written — because judgment is exactly
the faculty that is unavailable.

**`FSA-M5`: Calibration observed on checkable claims transfers downward, never
upward.**  In one session: an absent declaration that existed under a namespace,
a cited class name that did not exist at all, an "exists nowhere" for a notion
present in hundreds of lines, and a height/coheight confusion — each asserted
with exactly the confidence of the true claims beside them.  If confidence fails
to separate true from false on claims that take thirty seconds to check, it
cannot be relied on for claims that cannot be checked mechanically at all.

**`FSA-M6`: Finding and writing have opposite cost profiles, at roughly fifty to
one.**  A found declaration costs minutes and arrives reviewed, maintained, and
composable with everything already built on it.  A written one costs a session of
compile cycles and arrives composable with nothing, owed a comparison theorem,
and permanently maintained here.  Both close the same row.

**`FSA-M7`: Search compounds; authoring anti-compounds.**  A hit teaches the
file, its neighbours, the vocabulary the region is phrased in, and what the
region lacks — which makes the next twenty lookups cheaper and tells you whether
a nearby gap is real.  Every owned line, by contrast, is surface that must be
kept consistent, migrated, and eventually reconciled: it makes future work more
expensive.  Velocity on a long-horizon formalization is therefore mostly a
function of how much was found rather than how much was written.

**`FSA-M8`: Writing early destroys the information needed to write well.**  The
correct formulation of a notion is determined by what it must compose with:
downstream theorems, the surrounding library API, its categorical placement.  All
of that becomes known by searching.  Fixing a formulation first guarantees
rework, and rework on a definition is not local — it invalidates whatever was
built above, silently.  So the expected cost of a premature definition is not
"write it twice" but "write it twice and lose confidence in a subtree".

**`FSA-M9`: An unapproved definition transfers labour rather than saving it.**
Checking a model-authored definition against a source costs the reviewer about
what writing it themselves would cost.  So the artifact provides no leverage, and
it adds the risk that the check is skipped because the thing looks finished.  At
any accuracy short of perfect, and with a nonzero chance of the check being
skipped, the expected value is negative.

**`FSA-M10`: A wrong definition recruits; a wrong proof does not.**  The kernel
stops a bad proof at the door.  Nothing stops a plausible definition, and other
agents — and later sessions of the same one — then build on it faithfully, cite
it, extend it, and phrase new work in its vocabulary.  The error propagates while
remaining invisible, so definitional mistakes compound where proof mistakes
merely fail.

**`FSA-M11`: Delegate to a model by checkability, not by subject.**  What a model
can be trusted with is characterised by one property: the cost of checking the
output is far below the cost of producing it, or the machine does the checking.
Locating a declaration — checkable by opening the file.  Transcribing what a
source says, with the locator.  Falsifiable claims, which can be refuted.  Proofs
of statements a human fixed, which the kernel checks.  What fails the test is
exactly the definition: not machine-checkable, expensive to check by hand, and
authoritative the moment it lands.

**`FSA-M12`: Context is the scarce resource, and it is spent very differently.**
Compile-error ping-pong — a tactic name, an import path, a linter — produces
nothing that outlives the turn.  Reading a subtree of the library produces
durable knowledge that changes several later verdicts at once.  Both consume the
same budget.  Preferring the second is not patience; it is the higher-yield use
of the only thing that runs out.

**`FSA-M13`: Every owned definition permanently enlarges the human audit
surface, and that surface is the binding constraint.**  A formalization is
trusted when a human has satisfied themselves that its *statements* say the
intended mathematics (`FSA-M2`).  Nothing automates that, and no model can
supply it, so the total quantity of owned notions requiring semantic audit is
denominated in the one resource the project cannot buy more of.  Four properties
make it the constraint rather than a cost:

- **Additive.**  Each invented notion adds its own audit, and the additions never
  cancel.  Fifty small definitions are fifty audits.
- **Permanent and repeatedly paid.**  The audit is re-paid every time the
  definition is refactored, every time a new person or agent builds on it, and
  every time the library acquires its own version and the two must be compared.
- **Coupled.**  Owned notions must be audited against *each other* for coherence,
  not only against sources, so the cost grows faster than the count: changing one
  invalidates the audits of everything phrased in terms of it.
- **Not discharged by correctness.**  A perfectly correct invented definition
  costs a full audit, because the reader cannot know it is correct without
  performing one.  Getting it right reduces the risk, not the burden.

The consequence is the objective function of this family, and it is not "invent
carefully": **minimise the number of notions this repository owns.**  A
definition avoided is worth more than several written well.  Concretely, the
moves that reduce the surface are, in order: find the notion in a library; weaken
or reformulate what the project needs so that an existing notion suffices;
express the notion as a construction over existing ones rather than a new
primitive; contribute it upstream so the audit is performed by reviewers and
shared; and only then own it.  The moves that *look* like progress but leave the
surface untouched are writing it well, documenting it thoroughly, and proving
lemmas about it.

* * *

#### `FSA-01`: Search Is the Instrument; Authoring Is the Last Resort

- **Rule**: The response to a missing dependency is to search for it, and to keep searching until the named surfaces of `FSA-02` are exhausted.  Authoring the missing notion is the final option, taken after the search has failed and been recorded, not the first.

- **Rationale**: The two acts have opposite cost profiles.  Finding a declaration costs minutes and yields an object the whole library already composes with; writing one costs a session of compile cycles and yields an object that composes with nothing, must be maintained, and will later require a comparison theorem or be discarded along with whatever was built on it.  Searching also compounds — a hit teaches the file, its neighbours and the vocabulary that corner of the library is phrased in, which makes the next twenty lookups cheaper — while authoring anti-compounds, since every owned line is a tax on future work.  This is the same principle as the registry's own first instruction to minimise owned lines, stated as an order of operations.

- **Violation Example**: on finding that Mathlib has no orthogonal group of a bilinear form, writing one; on finding no Weil divisor, writing one; closing a graph's open rows by authoring sixteen definitions in a session.

- **Correct Example**: reporting that the notion is absent, with the searches that establish it and the declarations a future definition would rest on, and stopping there.

#### `FSA-02`: Exhaust the Named Surfaces Before Any Absence Claim

- **Rule**: "This does not exist" is admissible only after all of: the pinned library searched by path *and* by semantic query; the registry's linked repositories; the package index as cloned; the index refreshed against its live source; the project-tracker and coverage lists; and the community forum, which the registry names explicitly as the place to search before concluding nonexistence.  A surface not searched is named in the claim.

- **Rationale**: Each surface fails differently.  A path search misses a notion under another name; a semantic search misses one nobody has phrased that way; a cloned index misses what was published since; the forum catches work in progress that exists nowhere else yet.  An absence claim is load-bearing — it is the premise on which authoring becomes permissible — so it must be the best-supported claim in the document, not the weakest.

- **Violation Example**: concluding that almost-complex structures, analytic spaces and Weil divisors exist in no Lean code anywhere, on the strength of identifier greps for guessed names, with the semantic search tools available and unused and the forum never opened.

#### `FSA-03`: An Identifier Grep Is Not a Search

- **Rule**: Search for the *notion*, not for a spelling you predicted.  Use type-pattern and natural-language search over the library before any grep, and when grepping, search for the mathematical words and the neighbourhood, never only for the identifier you expect.

- **Rationale**: Declarations are namespaced, renamed, deprecated behind aliases, and phrased in vocabulary a reader would not guess.  A grep for a predicted name tests your prediction, not the library, and it fails in the direction that licenses the most expensive action.

- **Violation Example**: `rg "def Commensurable"` returning nothing, and the absence recorded as a missing primitive, when the declaration is `def Subgroup.Commensurable`; citing `JordanRing` on the strength of a file name when the class is `IsJordan`.

- **Correct Example**: a natural-language query for "commensurable subgroups", a type-pattern query for the shape of the statement, then a grep for the word `commensurab` over the tree, and only then a conclusion.

#### `FSA-04`: A Negative Result Names Its Instrument, Surface and Revision

- **Rule**: Every recorded absence states what was searched, with what tool, over which revision or snapshot, and what the search does **not** cover.

- **Rationale**: A negative result is a claim about the world made from a partial view, and its value to a later reader is exactly the part that says where the view ended.  Without the instrument named, a reader cannot tell a thorough search from a guessed grep, and will either redo it or trust it — both wrong.

- **Correct Example**: "searched 94,764 `.lean` files in 734 packages, the index as cloned on a stated date, by identifier and word search, no build; does not cover packages added since, a formalization under a name none of these searches guessed, or unpublished work."

#### `FSA-05`: Tooling Silently Falsifies Searches; Defeat It Explicitly

- **Rule**: Assume the search tool is lying by default.  Disable ignore rules over vendored and cloned trees; distinguish matches in prose from matches in code; and never treat a build artifact's absence as a declaration's absence.

- **Rationale**: Three independent mechanisms produce empty results over full trees: ignore files suppress whole clones, a word match counts documentation that says the opposite of what is being looked for, and a partial build means a module that exists cannot be elaborated.  Each of them produces the same output as genuine absence, and each of them was mistaken for genuine absence in practice.

- **Violation Example**: a search over cloned repositories returning zero files because ignore rules applied; counting occurrences of `sorry` and finding files whose text reads "no `sorry` in this file"; recording a notion as unavailable because its module had no compiled artifact locally.

#### `FSA-06`: A Definition Is Transcribed From a Source Open at the Time

- **Rule**: Write no definition, and no citation key, from memory.  Open the source — the library declaration, the paper, the textbook, the repository's own defining occurrence — and transcribe.  `FRM-02` requires the citation; this rule requires the reading that makes it true.

- **Rationale**: A definition recalled is a definition generated, and the generated one is fluent, idiomatic and plausible whether or not it is right.  There is no internal signal separating the two cases, so the only available discipline is procedural: the source is open, or the definition is not written.

- **Violation Example**: writing a normal analytic space, a Weil divisor, a germ ring and the statement of Milgram's theorem in one sitting without opening a text, and afterwards being unable to say whose definition was written.

#### `FSA-07`: A Model-Authored Definition Requires Explicit Approval Before It Lands

- **Rule**: A definition produced by a language model is a proposal, not a contribution.  It is presented for approval with its source and its alternatives, and it does not enter a durable file, a shared document, or another agent's dependency chain until a human has accepted it.  The default deliverable for a discovered gap is the gap, its locators, and the declarations a definition would rest on.

- **Rationale**: A model's output reproduces the surface features by which a reader judges care — naming, structure, a confident docstring, apparent generality — decoupled from correctness, so the usual signals of trustworthiness are not merely absent but counterfeited.  The failure mode is the confident near-miss, and it is invisible at the point of use: proofs built on a wrong definition remain valid and become useless, and nothing downstream detects it.  Verification also costs the reviewer what writing it themselves would cost, so an unapproved definition is not labour saved but labour transferred, with the risk that the check is skipped because the artifact looks finished.

- **Violation Example**: sixteen definitions landing in a repository in one session, each with a docstring asserting what it means, none reviewed, several chosen for tooling convenience, and a design document then citing them as substrate.

#### `FSA-08`: Definitions Cannot Fail; Prefer the Theorem, and Anchor the Definition

- **Rule**: Prefer work whose product can be wrong in a way the machine detects.  Where a definition must be written, land beside it a theorem that would fail if the definition were wrong, and prefer stating the theorem the definition exists to serve over elaborating the definition further.

- **Rationale**: The kernel checks proofs against statements; nothing checks statements against mathematics.  A definition therefore type-checks whether or not it names the intended notion, which makes definitional work the activity with the highest ratio of apparent progress to verifiable content available.  A theorem beside it converts some of that unfalsifiable content into content the machine can refute.

- **Correct Example**: a proved statement about the object — that the negative cone of an index-one form has exactly two components, or that the Gauss sum of the zero form is the group's order — landing with the definition it exercises.

#### `FSA-09`: The Environment Never Chooses the Mathematics

- **Rule**: A definition says what the mathematics says.  Local build state, a missing artifact, tactic friction, or elaboration cost may never select between formulations, and an obstacle of that kind is fixed, worked around locally, or reported — never accommodated by restating a notion.

- **Rationale**: Selecting the formulation that is cheapest for the current tooling is a selection rule anti-correlated with correctness: it picks whichever spelling is easiest right now, which has no relationship to which one is right or which composes with the rest of the program.  It is also self-concealing, because the accommodation compiles and therefore reads as progress.

- **Violation Example**: spelling normality out as an unfolded integral-closure condition instead of the library's `IsIntegrallyClosed` because that module had no compiled artifact in the working checkout.

- **Correct Example**: using the library's declaration, verified by reading its source, and building the missing artifact — or leaving it unbuilt and saying so outside the mathematics.

#### `FSA-10`: Environment State Never Enters a Durable Document

- **Rule**: What a particular machine has compiled, installed, cached or configured is not recorded in a design document, a docstring, a policy file, or a verdict about what exists.

- **Rationale**: Durable documents are read by people and agents on other machines and at other times, for whom such a statement is false or meaningless, and it is read as a fact about the mathematics because that is what surrounds it.

- **Violation Example**: a design document recording that a library module is "present as source and not built in this checkout" as though that were a property of the library.

#### `FSA-11`: Owned Code Is Never a Supplier

- **Rule**: Keep three provenance categories distinct and never let one stand for another: **found** — it exists in the library or a corpus, verified by reading; **owned** — this project wrote it; **absent** — nobody has it.  A locally authored file never appears as substrate in a dependency cell, never satisfies an availability verdict, and never changes an absence claim.

- **Rationale**: The purpose of an availability audit is to say what the project would not have to write.  A file the project wrote answers a different question, and counting it collapses the only distinction the audit exists to draw.  The pressure to collapse it is structural, not accidental: any locally written definition sits in the repository looking exactly like substrate.

- **Violation Example**: a dependency cell reading "realized as `Sterk.WeilDivisor`"; a node's greenfield verdict softened because a local definition now exists.

- **Correct Example**: a separate status marker meaning "a definition for this is written here", defined at the point of use as explicitly not a supplier, with the availability verdict left untouched.

#### `FSA-12`: A Foundational Definition Passes the Architecture Gate

- **Rule**: What an object *is* — which formulation, which generality, which categorical placement — is an architectural decision, discussed and decided with the user before it is written, not chosen while writing.

- **Rationale**: Every theorem above a definition inherits its formulation, so the cost of choosing wrong is paid across the whole subtree and paid late.  A choice made in minutes, alone, while optimising for something else is the worst available process for the decision with the longest reach.

- **Violation Example**: choosing between a locally-ringed-space presentation of an analytic space, a chart presentation, and a reduced-only presentation on the basis of which one avoided needing a sheaf quotient.

#### `FSA-13`: Under Completion Pressure, Search — Never Produce

- **Rule**: When a checker, a stop condition, a reviewer or a deadline reports the work unfinished, the admissible responses are to search further, to state what the condition requires and why it is or is not satisfiable, and to report.  Producing new owned artifacts in response to that pressure is not among them.

- **Rationale**: Production is the activity with unbounded cost, no compounding return and a silent failure mode, so pressure that selects for it selects for the worst use of the remaining budget.  A condition that asks for work already done by others is an instruction to search; reading it as an instruction to write inverts it.

- **Violation Example**: a stop condition requiring leaves to rest on pre-existing code, answered by authoring the code — which cannot satisfy it by construction, as the author had already observed.

#### `FSA-14`: Genuinely Absent Notions Go Upstream, or Carry a Decision Record

- **Rule**: Where a notion is absent from the library and the project genuinely needs it, the first option is to contribute it upstream, where it is reviewed and becomes everyone's.  Local ownership is the fallback and carries a decision record: the source its definition is transcribed from, why upstreaming was not taken, and the condition under which the local copy is retired.

- **Rationale**: An upstreamed definition acquires review, downstream users that pin its meaning, and maintenance by others; a local one acquires none of these and silently becomes load-bearing.  The decision record is what makes the local copy retirable later instead of permanent by default.

#### `FSA-15`: Report the Neighbourhood, Not Only the Hit

- **Rule**: A search that succeeds reports what else is there: the file, the adjacent declarations, the vocabulary the area is phrased in, and what the area does *not* contain.

- **Rationale**: This is where the compounding lives.  The value of finding a declaration is mostly in what the finding teaches about the region, which is what makes the next search cheap and what tells a later reader whether a nearby gap is real.  A bare hit throws that away and the region has to be learned again.

- **Correct Example**: reporting not just that a lemma exists but that its subtree also holds a sorry-free classification, seven files of decomposition machinery, and no analogue of the notion actually wanted.

#### `FSA-16`: Introspective Confidence Is Never Offered as Evidence

- **Rule**: Do not report that a definition, name, statement or absence is right because it is recalled, familiar, or standard.  A claim carries a locator — file, declaration, section, page — or it is marked unverified.  Phrases asserting recalled correctness are banned outright: "this is the standard definition", "as usual", "the canonical form is", "I'm confident that", "obviously", said of anything not just read.

- **Rationale**: `FSA-M4`.  The faculty being appealed to does not exist: recall and confabulation are the same operation from the inside, so the assertion adds no information while consuming a reader's trust.  `FSA-M5` shows the calibration empirically — confident false claims about file contents appeared beside confident true ones, indistinguishable.

- **Violation Example**: "normality is integral closedness of the local ring, which is standard", written without opening a source; "`JordanRing` is the class", from a filename.

- **Correct Example**: "Grauert–Remmert Ch. 6 §2 defines it as …, transcribed"; or "unverified: no source consulted, do not build on this".

#### `FSA-17`: Do Not Manufacture the Appearance of Care

- **Rule**: Never dress an unverified artifact in the marks of a verified one.  A definition written without a source gets no docstring asserting what it means, no claim of canonicity or generality, no citation-shaped comment, and no confident naming borrowed from the literature.  If it must exist at all, it is labelled unverified at the declaration.

- **Rationale**: `FSA-M3`.  Polish is produced for free and decoupled from correctness, so adding it to unverified work is not neutral presentation — it actively disables the reader's only heuristic.  This is the mechanism by which model-authored mathematics is more dangerous than model-authored code: the surface is indistinguishable from careful work and the substance is not checkable.

- **Violation Example**: a definition of a normal analytic space carrying a docstring explaining what analytic spaces are, in the voice of a textbook, with no source read.

#### `FSA-18`: A Model May Not Supply the Approval for Its Own Definition

- **Rule**: A model's review of its own definition is not the approval `FSA-07` requires, and neither is compiling it, nor re-reading it, nor stating that it looks right.  The approval is a human's, or it is the kernel's against a statement a human fixed.  Self-review may be reported as a proposal's reasoning; it may never be recorded as verification.

- **Rationale**: `FSA-M2` and `FSA-M4` together.  The missing component of trust is provenance, and provenance cannot be supplied by the same process that produced the artifact; a second pass by the same model reproduces the same priors and the same blind spots, with more confidence rather than more evidence.

- **Violation Example**: "checked it again and it's correct"; treating "compiles with no `sorry`" as verification of a definition; a design document recording a self-authored file as substrate on the strength of its author's confidence.

#### `FSA-19`: Choose Work by Checkability, Not by Difficulty

- **Rule**: When selecting what to do next, prefer the task whose output can be checked far more cheaply than it can be produced: locating a declaration, transcribing a source with its locator, making a falsifiable claim, proving a statement someone else fixed.  Deprioritise work whose output is expensive to check and authoritative once written, whatever its apparent difficulty or convenience.

- **Rationale**: `FSA-M11`.  Checkability, not subject matter or effort, is what makes model output worth having; a hard task with a cheap check is a good use of a model, and an easy task with no check is the worst one.  This is also the practical form of `FSA-13`: under pressure the tempting work is always the unfalsifiable kind, because it always succeeds.

- **Correct Example**: reporting that a notion is absent, with the instruments used and the declarations a definition would rest on, in place of the definition — the absence is checkable, the definition is not.

#### `FSA-20`: A Proposal to Own a Notion States the Audit It Adds and the Avoidances Tried

- **Rule**: No new owned definition is proposed without stating, in the same message: what human audit it adds and who would perform it; and which surface-reducing alternatives were attempted and why each failed — a library notion, a weakening or reformulation of what the project needs so an existing notion suffices, a construction over existing notions instead of a new primitive, and upstream contribution.  A proposal that omits the audit cost may not be accepted, and one that omits the avoidances has not been tried.

- **Rationale**: `FSA-M13`.  The quantity to minimise is the count of owned notions, so a proposal that does not price its addition cannot be weighed against the alternative of not making it.  Naming the avoidances also prevents the common shape where a notion is invented because inventing was the first thing attempted.

- **Violation Example**: proposing sixteen definitions as the natural completion of a graph's open rows, with no statement of who audits them and no attempt to reformulate the graph's needs onto existing notions.

- **Correct Example**: "this needs a Weil divisor; Mathlib has none, searched thus; the two statements that need it can instead be phrased over `Finsupp` on the height-one points directly, which owns nothing; recommend that, and if rejected, upstreaming before local ownership."

#### `FSA-21`: Where a Notion Must Be Owned, Prefer the Forced Formulation

- **Rule**: An owned definition is chosen to have as few free choices as possible: pinned by a universal property, matching the library's own spelling of the nearest notion, or determined by the construction it must interoperate with.  Where choices remain, they are enumerated at the declaration as the things an auditor must check.

- **Rationale**: `FSA-M13`, the coupling and the audit clause.  What a human must audit is exactly the free choices — a formulation forced by a universal property or copied from the library carries almost no audit, while one with several defensible variants carries the full burden and transmits it to everything built on it.  Enumerating the residual choices converts an unbounded review into a checklist.

- **Violation Example**: choosing between three presentations of analytic space on convenience grounds and recording none of the choice; a definition whose docstring explains the notion but not what was decided.

- **Correct Example**: "this is the reduced presentation; the free choices are (i) reduced rather than with nilpotents, (ii) structure functions by ambient extension rather than as a sheaf quotient, (iii) finitely many equations rather than an ideal.  An auditor should check those three against Grauert–Remmert."

#### `FSA-22`: The Count of Owned Notions Is Reported, and Its Growth Is Justified

- **Rule**: Any status report, plan, or completion claim for formalization work states the number of notions the repository owns and how that number changed.  Growth is justified in the same breath or it is treated as a regression, whatever else the work achieved.

- **Rationale**: `FSA-M13`.  A quantity that is the binding constraint and is never reported will be traded away silently for things that are reported, such as closed rows and compiling files.  Making it a headline number is what keeps "we finished nine nodes" from concealing "we acquired nine audits".

- **Violation Example**: a report leading with sixteen definitions written, a thousand lines compiled and no `sorry`, without stating that the repository's audit surface grew by sixteen notions.

* * *

## Detailed Documentation References

For in-depth guides and stylistic standards, see the documentation book:

- **Contribution Workflow**: [`writing/category-theory/contributing/Contribution-Guidelines.md`](writing/category-theory/contributing/Contribution-Guidelines.md)

- **Categorical Principles**: [`writing/category-theory/contributing/Categorical-Presentation-Principles.md`](writing/category-theory/contributing/Categorical-Presentation-Principles.md)

- **Mathematical Style Guide**: [`writing/category-theory/contributing/Mathematical-Language-Style-Guide.md`](writing/category-theory/contributing/Mathematical-Language-Style-Guide.md)

- **Design Hazards Ledger**: [`writing/category-theory/contributing/Design-Hazard-Ledger.md`](writing/category-theory/contributing/Design-Hazard-Ledger.md)

- **Mathematical Lexicon**: [`writing/category-theory/contributing/Mathematical-Lexicon.md`](writing/category-theory/contributing/Mathematical-Lexicon.md)
