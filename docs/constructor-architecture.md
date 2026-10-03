# Constructor architecture on sage-categories

The target is a preamble of mathematical leaves over the public `sage-categories` core. Constructor inheritance, implementation registration, initialization order and collision handling belong to that core. The current research runtime supplies evidence for the rewrite and must keep working until replaced; it is not the owner of a new permanent constructor framework.

This specifies the integration design, not runtime delivery. The research construction contracts remain in CONTRIBUTING. The core sources inspected on `dzack@rack`, `/home/dzack/gitclones/sage-categories`, were at `5867543fc990b017caabdb03d6d82cdf9cc7e5eb`. Its local `main` was ahead of its recorded `origin/main`, `60fc9581477591259ef4fe33ae64eb2de374ecf5`. These observations do not establish publication. A consumer dependency needs an owner-published full SHA under that repository's README; this design does not change a dependency pin or publish its local history.

## Target construction mechanisms

| Mathematical situation | Core mechanism | Preamble leaf responsibility |
| --- | --- | --- |
| A new structure on existing mathematics | A leaf `Category` with local `ObjectType`, `ElementType`, `MorphismType` and selected `structure_functors()` | State the new datum and immediate object/morphism actions; the kernel initializes inherited target structure from those actions |
| A property of an existing structure | `Axiom`, property categories and `construction_owner()` | State the proposition and its computational handlers; inherit the original constructor, including through nested restrictions |
| An implementation of an existing categorical construction | Select `End_Cat(x).one()` first in `structure_functors()`, then `Cat().implement(LeafCategory)` | Add the local mathematics on the exact retained category `x`; do not construct a second category or repeat its constructor |
| A specialized realization of a universal construction | The selected functor's lifting interface, such as `with_limit_lifting` | Supply the new mathematical structure on the retained apex and the corresponding map constructor; reuse the cone and universal map |
| A decision procedure for an existing proposition | The core predicate/query handler interfaces | Add an exact computational case at its predicate owner; do not write another predicate dispatcher in the preamble |

The source owners are `sage_categories/cat/category.py`, `cat/properties.py`, `cat/predicates.py` and the kernel compiler. The consumer contracts are `specs/leaves.md`, `specs/functor.md`, `specs/property-refinement.md` and the pointed-set and poset-product templates on rack.

`03f6a1fd` is directly relevant to constructor loss: `NarrowedProperty.__call__` now constructs through `self.construction_owner()` instead of its immediate ambient category. Module, bimodule, monoid, semiring and ring constructors identify themselves as their construction owner. Nested roots with incompatible owners are rejected. `e13cfa1d` adds the corresponding narrowed-property consumer. Source was inspected here; that consumer was not executed in this research task.

The core's pointed-set template is the model for avoiding repeated constructors. It identifies pointed sets with `Sets().CosliceUnder(Sets().Terminal())`, selects that category's identity and its retained projection composed with evaluation at the codomain, and writes no constructor. Its poset-product template supplies componentwise order through `with_limit_lifting`; the core supplies the cone, projections and universal morphism. These are the extension mechanisms the preamble should consume before adding registration machinery.

## Consequences for the preamble rewrite

For modules, use the core module owner and its action-morphism input. A ring-endomorphism presentation is a named input adapter to that construction, not a competing module implementation. For algebras, supply the multiplication and any chosen unit through the core's structured-object construction. For a bilinear module, supply the selected bilinear form on the actual module and the immediate projections that retain that module and form. For lattices, add the lattice-specific datum and backend computation on those owners. Property restrictions inherit these constructors.

The kernel runs a selected functor's object action after the leaf's own data is initialized. The action returns the public target value; the kernel uses its construction to initialize the inherited target implementation on the source. A lattice projection that uses its underlying module therefore follows that module projection in the selected functor order. This replaces the preamble's `_derived_construction_parameters` and cooperative `super().__init__` engineering; leaves do not translate those fields into another local initialization registry.

For subgroups, use the generic group subobject construction and its retained monomorphism. Its underlying-set image comes from the selected group-to-set functor on that same morphism. A subgroup of `O(L)` specializes that route with its generators or predicate. The object, inclusion and underlying-set map must be followed through the core APIs before declaring the leaf complete; a `Subgroups -> Groups -> Sets` graph path alone does not establish them.

Construction states the defining laws; computations of those laws are separate proposition queries under the core contract. Do not insert constructor-time `ask(...)` gates or new certified/unchecked entrypoints. Engine adapters stay private under the research ownership contract: the core template's `from_sage` example does not by itself authorize a raw-engine public preamble entrypoint.

## Registry and discovery ownership

Use `Cat().implement(...)` for implementation registration against mathematical category identities. It already reads the identity-functor declaration and installs the implementation on the retained category. A preamble string registry mapping category names to classes would compete with it. Predicate handlers likewise use the existing core interface. A small exact-name catalogue, such as lattice names, remains leaf data; it does not own category or constructor inheritance.

A constructor-discovery decorator is optional metadata, not the wiring mechanism. First derive default constructors from `construction_owner()`, public call signatures and implementation declarations. A marker is useful only for named alternative presentations that cannot otherwise be distinguished from ordinary methods. If a shared marker or constructor-introspection protocol is required, define it in `sage-categories` and have research consume it. Do not freeze a research-specific decorator or provider registry before establishing this boundary.

Extend the research megadoc, placement and source-survey tools to report both the current runtime and the target core evidence. The target record includes the selected category, its constructor owner, implementation declaration, role definitions, signature, immediate selected functors and their source locations. Show inherited constructor availability after property narrowing, and compare declarations with runtime bindings. Source-only inspection labels unresolved binding as unobserved.

Keep the structure-functor graph distinct from a property-inclusion poset. Preserve multiple functors with the same endpoints, their chosen actions, and the property that permits implementation inheritance. Up-set/down-set queries apply to the selected inclusion relation; forgetting a form or an action is not merely another subclass edge. This is necessary for auditing retained mathematical data and maps during the rewrite.

Constructor alignment is part of the current discovery and API-freeze work; the full core replacement remains the separately scheduled integration node. Before freezing constructors, trace a module, a formed module and a subgroup through the core's actual APIs, recording any missing public core operation at its owner. A missing operation is core work, not permission to add a second preamble framework. Preserve mathematical specimens across the rewrite and compare retained data and map equations, not old class identities.

## Failure mechanisms this model was learned from

These cases explain the construction principles; they are teaching history rather
than a new incident ledger. They concern inspected diffs, some of which explicitly
left execution pending. Their messages do not establish a passing current session.
The successor stack consumes their lessons, not their Python runtime arrangements;
research's separately assigned construction and integration work remains in force.

### Forwarding duplicated a shared construction responsibility

`7bbf7e60c` added a `BiproductLattices.ParentMethods.__init__` forwarding `summands`
and `biproduct_factors`. That leaf constructor duplicated a dependency of the
shared construction chain. `d59eb8ef0` removed it and ordered providers by
`_derived_construction_parameters` in `_owned_implementation_bases`. Likewise,
`70104eaf6` replaced `Category.join(placement)` with `owned_category_join(placement)`
for localized modules: possessing all constructor names had not preserved their
producer/consumer order. The correction was shared construction at its owner,
not one forwarding accommodation per leaf. Those provider mechanisms are evidence
about this runtime, not a prescribed successor implementation.

### Placement without construction prompted retrospective recovery

Interfaces became visible before their required construction data existed.
`09215fd7e` separated algebra framing from module framing; `e8866fb1f` repaired
resolution-refactor losses involving selected lifts, bilinear pullbacks and
framed-module queries. Similar names and category membership had erased the
identity of the selected datum, leaving consumers to recover missing state.
Construct and retain the actual module, form, resolution, inclusion and action at
their owner and thread them through composition. A registry entry or graph path
cannot reconstruct them. The successor must expose required computational data;
that requirement is not a proof of its backend's correctness.

Arrow construction suffered the same substitution of placement for data.
`144ba1883` removed the explicit `ModuleMorphism` base, stored lower arrow and
repeated methods from `MultiplicativeAlgebraMorphism`, declaring it through
`ElementMethods` instead. Arrow inheritance belongs to the Mor construction,
not a parallel Python graph manufactured by decorators. Merely changing a base
while retaining the old mechanism does not complete that semantic repair.

### Invented law checking generated an escape framework

In `sage-categories`, `27b3e507` required an Equifier constructor to decide its
defining equation before admitting a value. Turning a mathematical specification
into a runtime admission burden generated a `certified_structures` escape route;
`96054a58` removed that route and returned consumers to ordinary constructors.
Before improving an exception framework, inspect whether its prerequisite belongs
at that boundary. Formal definitions and genuinely proof-producing computations
have proof obligations; an external realization is not automatically required to
prove its universal correctness. Preserve defining data and protocol checks
without promoting unchecked data to theorems.

### Role labels did not prevent implementation-shaped mathematics

The supplied binder history used separate authors while the orchestrator prescribed
row choices, obligation shapes and proof goals until a downstream tactic succeeded.
An authorship gate admitted nominally separate roles while the implementation
still determined the upstream question. Authority concerns who determines meaning,
not who signs a file. Independently motivated upstream computational API improvement
is necessary; tailoring mathematics to a failing implementation is not that work.

### Verification activity displaced the required construction

The research postmortem records selection by availability, throughput mistaken for
progress, verification becoming the target, and literal compliance with a
structural task. On 2026-09-26, 402 single-surface test commits accompanied about
sixteen lines of source change to architecture nodes and one closed node. A base
class swap retaining the stored lower arrow similarly satisfied task wording
without generating arrow types from the Mor graph. The consequence was churn
around an unchanged cause. Judge the required operation and its compositions by
what they now do. Counts and local checks cannot make that judgment, and this
lesson does not authorize detectors, hooks or mandatory checklists.

The supplied B0 intervention repeated the prerequisite error by prescribing
runtime reconstruction and independent proof obligations for computed results,
then treating reconstruction and approval machinery as progress. Remediation
plans are fallible engineering designs. Remove an invented responsibility and
its dependent machinery when they obstruct the intended capability; do not
weaken the capability or retain the machinery merely because a plan named it.

## Evidence from the current research runtime

In `src/dzack_research/preamble/owned_category.py`:

- `_owned_implementation_bases` computes the provider order, including declared derived-data dependencies.
- `ConstructionContract` records parameter names, declaring providers, defaults, variadic and opaque boundaries, and refinement hooks.
- `_construction_contract(C)` reads `C.ObjectType`'s MRO. `_mor_construction_contract(C, A, B)` separately describes the fixed Mor parent.
- `_object_of(C, **data)` normalizes the category, selects its implementation, validates the discovered contract and constructs it.

Expose these facts through the existing megadoc and graph JSON while this runtime remains in use. Do not reconstruct their values from a manually maintained constructor registry. In particular, `required_names()` subtracts declared derived names, and `validate()` accepts additional names at an open variadic boundary. Reports must retain those facts; a successful parameter check does not establish that the data were produced or correctly threaded.

The public input signature and the cooperative initializer contract are different. `Algebras(R)._call_(module, multiplication)` and `FormModules(R)._call_(form)` describe mathematical inputs. The provider initializers describe how their data reach implementation levels. Show both, with the calls connecting them. The megadoc currently reads `type(instance).__call__`; constructor reporting must also resolve the effective `_call_` and its declaring class, rather than displaying only the runtime's generic call signature.

## Discovery decorator: metadata, without method installation

If named-constructor discovery requires a marker, use the shared core metadata protocol on named mathematical construction methods. Treat the current category `_call_` hook as an implicit constructor declaration. Such a marker returns the original callable unchanged. It does not wrap calls, copy functions, use `setattr` on category classes, or accept a second declaration of the owner.

Derive the owner and receiver kind from the declaration: category method, `ParentMethods`, `ElementMethods`, or Mor provider. Preserve the existing category runtime's binding. Thus a marked ring `localization` remains a method of a ring, while a marked category construction remains a method of that category. A list of constructors on `Sets` may provide navigation to stronger owners; it must not install every stronger constructor on every set.

Extend `megadoc.Survey.describe` and its existing declared-method survey to collect these markers. Extend `refactor_survey` to read the same marker syntactically without import. The JSON record needs the declaration source, receiver kind, public signature, effective binding, and direct call expressions. For live category construction add the existing `ConstructionContract` and ordered providers. For source-only results mark runtime binding and provider order as unobserved. Keep parameterized categories parameterized; a sample over `ZZ` does not describe every `R`.

The immediate useful output for `Algebras(R)` is:

```text
public input: _call_(module, multiplication)
declaration: categories/algebras/algebras.py: Algebras._call_
direct realization call: _algebra_on_module(module, multiplication, ...)
retained datum to inspect: unformed_module(), multiplication()
implementation: sampled ObjectType MRO and ConstructionContract
```

The retained-data line is a mathematical review question, not inferred proof. Construction expressions cannot establish identity of the retained module.

## Registry: a specific extension point in lattice input

`categories/_lattice.py::_lattice` already separates forms, tensors, free modules, named input, ranks and row data. Those branches have different mathematics. Preserve that classification.

Extract only its exact-name branch into an owner-local named-lattice registry. The initial entries are `U` and `H`, currently one branch leading to `_hyperbolic_plane_gram_tensor` and `_lattice_from_gram_tensor`. A provider accepts the selected lattice category and the existing `names` and `module_generators` parameters, then returns the owned lattice through that same construction. Registration adds a new exact name without editing `_lattice`.

String parsing has an explicit grammar: reserved exact names first; otherwise the existing finite crystallographic Cartan-type parser. Reject duplicate exact names. Reject a new exact name that the Cartan parser already accepts, so registration cannot silently change the meaning of `A2` or another established Cartan descriptor. That check belongs to the owner of named input, not a generic registry utility. `CartanType_abstract` input keeps its current route.

Declare the initial `U` and `H` provider beside `_hyperbolic_plane_gram_tensor` in `_lattice.py`, which the public `lattices.py` already imports. Additional provider modules register with that owner and are loaded explicitly by the session composition root, `preamble/all.py`, after its lattice imports. Direct category imports expose the built-ins; a separately imported provider extends them explicitly. Expose registered names and source locations, including the loaded-module scope. Source inventory can also show declared providers whose modules have not loaded. Do not use subclass discovery: lattice implementation classes are not named input forms.

This applies the [keyed registry pattern](https://www.kdnuggets.com/stop-using-if-else-chains-use-the-registry-pattern-in-python-instead) to an actual discrete branch. Do not turn all tensor/category predicates into a list of registered predicates with first-match dispatch. A general category-aware algorithm dispatcher is a separate design problem and is not justified by this named-input case.

## Concrete inspection against the historical failures

Extend the existing tools with these views, rather than introducing gates:

1. **Declared versus bound constructors:** compare marked source declarations with effective live methods. Report shadowed declarations, same-name incomparable owners, and unloaded providers separately.
2. **Construction-data flow:** display each initializer's consumed parameters, declared derived parameters and final provider order. Link each declaration to source. Use the lattice biproduct and localized-module histories as review slices; do not infer correct value transport from matching parameter names.
3. **Realization call sites:** index calls to `_object_of`, `_algebra_on_module`, `_form_module` and `_lattice_object`, along with direct `ObjectType`/`parent_class` calls. Preserve unresolved receiver expressions. Review which callers use the shared construction and which allocate through another route.
4. **Subgroup structure:** inspect `groups.py::Subgroups.ParentMethods.__init__`, its retained `supergroup`, and `_canonical_subgroup_inclusion`; compare that inclusion's underlying set map with the set-subobject construction. `Subgroups.super_categories()` currently names `OwnedGroups`. Neither adding a registry entry nor adding a set-subobject category edge establishes the missing map comparison.

The next constructor design unit maps the existing module, formed-module and subgroup routes to the core consumer contracts. Discovery tools expose both sides of that mapping. The exact-name lattice registry is a separate bounded leaf extension, not a prerequisite for core integration.
