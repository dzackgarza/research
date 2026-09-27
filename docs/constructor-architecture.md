# Constructor architecture: source-grounded recommendation

Retain the existing category-generated implementation types and cooperative construction chain. Add constructor discovery to that mechanism. Use keyed registration for named construction families, beginning with named lattice input. Do not introduce a second registry of category inheritance, constructor parameters or implementation providers.

This specifies the proposed change; it does not claim runtime delivery. The governing construction contracts remain in CONTRIBUTING.

## What the history requires

| Inspected change | Concrete lesson for this design |
| --- | --- |
| `7bbf7e60c` added a `BiproductLattices.ParentMethods.__init__` that forwarded `summands` and `biproduct_factors`; `d59eb8ef0` removed it and ordered providers by `_derived_construction_parameters` in `_owned_implementation_bases` | A leaf forwarding constructor duplicated a dependency that belonged in the shared construction chain. Discover and display the existing producer/consumer order rather than registering another forwarding route. |
| `70104eaf6` changed localized-module construction from `Category.join(placement)` to `owned_category_join(placement)` | Having all constructor names was insufficient: the selected implementation had to preserve the provider order. Current `_object_of` normalizes joins through `_owned_realization_of_join`; retain that common entry. |
| `144ba1883` removed the explicit `ModuleMorphism` base, stored lower arrow and repeated methods from `MultiplicativeAlgebraMorphism`, then declared it through `ElementMethods` | Arrow inheritance belongs to the Mor category graph. A constructor decorator must not manufacture a parallel Python inheritance graph or register a concrete arrow class as the public constructor. |
| `09215fd7e` separated algebra framing from module framing; `e8866fb1f` repaired resolution-refactor losses involving selected lifts, bilinear pullbacks and framed-module queries | Similar names and category membership cannot identify the selected datum. Inspection must follow actual retained modules, forms, resolutions and maps. A registry entry cannot certify this. |

These are statements about inspected diffs. Several commits explicitly leave execution pending; their messages are not evidence of a passing current session.

## Reuse the constructor machinery that exists

In `src/dzack_research/preamble/owned_category.py`:

- `_owned_implementation_bases` computes the provider order, including declared derived-data dependencies.
- `ConstructionContract` records parameter names, declaring providers, defaults, variadic and opaque boundaries, and refinement hooks.
- `_construction_contract(C)` reads `C.ObjectType`'s MRO. `_mor_construction_contract(C, A, B)` separately describes the fixed Mor parent.
- `_object_of(C, **data)` normalizes the category, selects its implementation, validates the discovered contract and constructs it.

Expose these facts through the existing megadoc and graph JSON. Do not reconstruct their values from a manually maintained constructor registry. In particular, `required_names()` subtracts declared derived names, and `validate()` accepts additional names at an open variadic boundary. Reports must retain those facts; a successful parameter check does not establish that the data were produced or correctly threaded.

The public input signature and the cooperative initializer contract are different. `Algebras(R)._call_(module, multiplication)` and `FormModules(R)._call_(form)` describe mathematical inputs. The provider initializers describe how their data reach implementation levels. Show both, with the calls connecting them. The megadoc currently reads `type(instance).__call__`; constructor reporting must also resolve the effective `_call_` and its declaring class, rather than displaying only the runtime's generic call signature.

## Discovery decorator: metadata, without method installation

Add a `@constructor` marker to named mathematical construction methods. Treat the category `_call_` hook as an implicit constructor declaration. The marker returns the original callable unchanged. It does not wrap calls, copy functions, use `setattr` on category classes, or accept a second declaration of the owner.

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

The next implementation unit is discovery over existing constructor contracts, with `Algebras(R)` and formed modules as distinct specimens. The named-lattice registry follows as the bounded extension experiment. Neither requires replacing the class builder, moving every constructor, or freezing a universal dispatcher first.
