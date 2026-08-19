# CRITICAL: Category Spec Constructor Routes Are Category Owned

## Object of the invariant

Project-owned constructor API design in `category_specs`: Sage-backed object construction must be discoverable from the mathematical owner category.

## False substitute it blocks

Ambient provider mutation: making existing Sage globals, module attributes, dynamic classes, or temporary providers secretly behave like project constructors and then calling that compatibility.

Raw-Sage escape hatches: exposing raw Sage objects to downstream users, making
category-obligation examples or tests use raw Sage objects after admission, or using raw
reconstruction as an undocumented shortcut instead of a mapped category-owned
constructor.

## Correct first question

What existing Sage constructor route is being recovered, what exact finite input shapes does Sage actually accept, and what explicit spec-layer constructor or promotion path exposes each shape without leaving the spec layer once an object has been admitted?

For constructor shapes where Sage accepts another Sage parent object, do not answer from the abstract pattern "`B` is constructed from `A`." First inventory the actual instances in mapping specs and current constructor collectors, then read the corresponding Sage source and run the live spec-owned inputs. The object-level question is instance-specific:

- Does Sage merely recover data from the input parent?
- Does Sage store the input parent as structure on the result?
- Does Sage copy/rebuild from canonical cover/presentation data?
- Does Sage call methods on the input parent that the refined spec object already supplies?
- Does Sage reuse the input parent's category when dynamically building the result class?

These cases have different implementation obligations. A universal demotion, unwrapping, replay, or promotion rule written before this inventory is speculation.

Once an actual parent-input route is inventoried, the implementation order is:

- First, try passing the spec-owned input parent directly to the Sage constructor. If Sage accepts the refined object and produces the right object, there is no bridge problem to solve.
- If direct passage fails, next try canonical representative reconstruction inside the category-owned constructor: recover the ordinary Sage input parent from explicit, spec-visible methods on the refined object, pass that ordinary Sage representative to Sage's original constructor, then refine the returned parent back into the project category hierarchy. If Sage's unique-representation cache returns the already-refined object for the same constructor key, use Sage's constructor-bypass mechanism at the interop boundary, such as `typecall`, rather than exposing raw construction to callers.
- If the refined object does not expose enough canonical data to reconstruct the ordinary Sage input parent, stop and surface the missing data or bridge decision to the user. Do not invent hidden provenance, caches, fallback guesses, or broad unwrapping machinery.

This reconstruction route is not a public escape from the spec layer. It is an implementation bridge hidden behind the already mapped category-owned constructor surface.

## Operative invariant

The public project API for constructors is the category-owned collector. The spec layer is a firewall over Sage implementations: after a Sage object is admitted through a project constructor and refined into spec categories, later project construction must operate on the refined spec object, not peel it back into raw Sage. Sage docs/source are used to recover the original construction semantics, not to justify repeatedly escaping the spec layer.

The point is not to invent new constructors or redefine Sage constructors. The point is to exactly recover every valid way Sage already constructs the object, eliminate constructor-shape ambiguity, eliminate positional public arguments, and expose the recovered routes as explicit named-only category constructors or spec-layer promotion paths.

The required workflow is:

- Read Sage written docs for the constructor family.
- Read the actual Sage factory/source code, especially variadic factories, `create_key`, `create_object`, positional-only signatures, deprecated argument routes, internal argument names, and backend dispatch.
- Enumerate every actually valid input shape. Do not infer from a displayed signature,
  failed category assertion, or old wrapper.
- Write or correct the mapping docs so each source-grounded Sage constructor input
  shape maps to one explicit project constructor overload or spec-layer promotion
  path. Constructor mapping docs are an admission boundary, not a parking lot:
  a constructor shape found and recorded there is mapped by definition.
- Use named parameters for every public project constructor overload. If Sage accepted a positional argument, find or coin the mathematical parameter name and make callers name it.
- Put the overloads on the owning category's `Constructors()` surface. Multiple Sage shapes may overload the same constructor name when they construct the same mathematical family.
- When a Sage constructor accepted another already-built Sage parent, the mapping must recover that as a spec-layer promotion/composition path between refined spec objects. For example, Sage's `PuiseuxSeriesRing(LaurentSeriesRing(...))` becomes a `PuiseuxSeriesRing(laurent_series_ring=...)` overload whose input is a spec-owned Laurent-series ring object and whose semantics promote it to the corresponding spec-owned Puiseux-series ring object.
- Before implementing such a path, record the actual Sage behavior for that route. The implementation may not be chosen from an abstract `A -> B` template; it must follow what the Sage constructor actually does with the input parent.
- For implementation, attempt direct spec-owned input passage first. If Sage's dynamic category machinery rejects the refined input, construct the ordinary Sage input parent from canonical methods on the spec-owned object, call Sage's original constructor with that representative, and refine the result. If canonical reconstruction is not possible, escalate the missing bridge rather than guessing.
- Implement each overload as a closed route: validate the named shape, preserve spec-layer inputs as spec-layer objects, perform the required Sage-backed construction behind the category-owned boundary, refine the returned parent into the project category hierarchy, and return it.
- Category-obligation examples and regression tests for project constructors call
  category constructor methods only, never raw Sage constructors.

Do not redefine, monkeypatch, or shadow Sage entry points to make raw Sage syntax satisfy project specs. There is no normal need for "constructor redefinitions" in spec code. Old Sage spellings are migration or compatibility evidence only; they do not become the project API by rebinding `sage.all`, Sage modules, object attributes, temporary providers, or class methods.

Do not fix constructor-composition failures by exposing raw Sage inputs as part of the public project API, by making tests depend on raw Sage routes, or by adding undocumented unwrapping. Canonical representative reconstruction is allowed only inside a mapped category-owned constructor and only from explicit spec-visible data.

A helper used by a constructor collector may exist only as implementation support for a visible category-owned method. If the helper can be imported and used as an independent constructor surface, the ownership is wrong.

## Audit trigger

Any surprise in a constructor interface means the workflow may have been reward-hacked.
Examples: unexpected keyword errors, a positional form not present in mapping docs, a
variadic fallback body, category-obligation examples calling raw Sage constructors, or a
helper module that owns several unrelated constructor families.

When that happens, do not patch the failing signature locally, do not improve the
existing artifact in place, and do not preserve the bad artifact with a more honest
label. Go back to the first workflow step and reconstruct the mapping from source:

- Sage docs/source for the constructor family.
- The mapping docs that should enumerate every valid constructor shape.
- The category `Constructors()` overloads and implementation bodies.
- Category-obligation examples and regression tests, which must exercise category
  constructors only.

The acceptance condition is not "the category-obligation example passes." The acceptance
condition is that the mapping, overloads, implementation, and tests all expose the same
finite, named, category-owned constructor interface.

## Red flags

- `setattr`, `delattr`, `globals()`, `locals()`, `vars(...)`, or direct module/class attribute rebinding in spec code.
- File names or commit messages using “constructor redefinition”, “install constructor refinements”, “patch top-level Sage constructors”, “provider injection”, “temporary provider”, or “generated forwarder” without a mathematical owner route.
- A failed category assertion is fixed by changing ambient behavior rather than by
  adding or correcting a `Cat().Constructors()` method.
- One module owns unrelated constructor families such as finite fields, p-adics, polynomial rings, modules, matrix spaces, and number fields.
- The patch makes existing informal syntax work but does not make the category constructor surface more complete or discoverable.
- A project constructor has `*args`, `**kwargs`, catch-all forwarding, positional public arguments, or type-narrowing `try/except` dispatch.
- Mapping docs do not list the exact Sage input permutations recovered by the implementation.
- Category-obligation examples import or call raw Sage constructors when a
  category-owned constructor exists.
- An agent responds to constructor drift by widening a wrapper signature before verifying Sage docs/source and the mapping row.
- An agent responds to a constructor-composition failure by suggesting public raw Sage reconstruction, unrefinement, hidden provenance, or bypassing the mapped category-owned constructor surface.
- An agent invents a new constructor name by analogy with a nearby Sage family, then
  preserves the invented name as a "deferred" or "gap" surface after Sage source fails
  to establish the constructor shape.
- A mapping doc keeps a rejected constructor idea as a row, section, decision, or
  historical evidence trail. Constructor mapping sources list admitted routes only;
  rejected slop is excised, while durable guidance records the class of agent failure.
- A constructor provenance model contains `status`, `deferred_reason`,
  `deferred()`, "constructor gap frontier", "blocked constructor surface", or any
  equivalent state for a named constructor. These states are nonsensical for
  constructor mapping: once the constructor is mined into the mapping docs, it is
  admitted and mapped; otherwise it is not part of the constructor source material.

## Verification

A future reviewer must be able to answer from source, without import side effects: "Which Sage constructor shapes are being recovered, where are they enumerated in mapping docs, which named-only category overload exposes each shape, what original Sage constructor does it call, and what project category is the result refined into?"

For constructor shapes that accepted another parent object, the reviewer must also be able to answer: "What spec-owned input category is admitted, what promotion or composition path does the mapping define, and why does the implementation preserve the spec-layer firewall instead of escaping to raw Sage?"

For those parent-input shapes, the reviewer must also see evidence from actual cases: the mapping row, the category constructor body, the Sage source branch, and a live behavior check with a spec-owned input. Negative or positive claims about a general bridge are invalid without that inventory.

QC should reject attribute/global rebinding in `category_specs` as a whole-tree tripwire. Relaxing that rejection requires first proving the manipulation is not a constructor/API substitute and moving the mechanism to an explicit interop boundary with source-grounded justification.

QC must also reject invented constructor names. The machine-readable name inventory belongs in the canonical mapping specs, because constructor-name provenance is part of the documentation workflow source. Every public method on a category `Constructors()` collector must either exactly match an inventoried Sage constructor name or be explicitly classified in that mapping spec as a project-owned construction whose name is not pretending to recover a Sage constructor. Variadic Sage constructor shapes become named-only overloads under the same Sage constructor name; they do not become `FooFromBar`, `FooWithBaz`, or similar renamed routes.

QC must reject deferred-constructor machinery by existence, not model it and count
zero instances. The banned pattern includes `status="deferred"`,
`deferred_reason`, `_deferred_constructor_reasons`, registry `.deferred()` filters,
mapping rows for rejected constructor ideas, and task/decision/spec artifacts whose
purpose is to preserve a constructor that Sage source did not establish.

QC must also reject constructor source artifacts that preserve slop with improved
wording. Phrases such as "deferred constructor", "not admitted", "blocked constructor
surface", and "constructor gap frontier" in constructor mapping/spec/visual sources are
hard failures. They are not future-work markers; they are evidence that an agent is
polishing an artifact that should not exist in the constructor workflow.

When an invented constructor name is found, remove the invented public method,
category-obligation example entry, mapping row, decision card, and task trail. Do not keep a specific "not
admitted" artifact to explain the bad name; git history is enough for the local
incident. The durable memory should capture only the reusable failure mode: an agent
saw a partial analogy or Sage gap and converted it into public API vocabulary without
source-grounded constructor inventory.

## Witness example

A file that installs wrappers by assigning to Sage modules or `sage.all` solves the wrong problem. The proper task is to implement the missing `Rings().Constructors()` or `Modules(R).Constructors()` route and classify old Sage spellings as migration/compatibility paths, not to make raw Sage names secretly pass through project refinement.

Sage's `PuiseuxSeriesRing(LaurentSeriesRing(...))` constructor shape is not evidence for a project constructor named `PuiseuxSeriesRingFromLaurentSeriesRing`, and it is not permission to expose raw Sage Laurent rings to downstream consumers. It is evidence for a documented spec-layer promotion path from a spec-owned Laurent-series ring to a spec-owned Puiseux-series ring under the original `PuiseuxSeriesRing` constructor name.

## Witness implementation pattern

If `PuiseuxSeriesRing(laurent_series_ring=...)` fails with a metaclass conflict because the input is a refined spec-owned Laurent-series ring, first confirm the direct Sage call really fails under the current import/category state. Then reconstruct the ordinary Sage Laurent ring from the spec-owned Laurent ring's canonical methods or underlying power-series-ring data. In the observed Sage unique-representation cache case, `LaurentSeriesRing(base, name, ...)` can return the already-refined Laurent ring; using Sage `typecall` on the Sage Laurent and Puiseux classes bypasses that cache while staying inside the category-owned constructor implementation. Refine the returned Puiseux ring into the project Puiseux-series category. If one of those canonical methods is absent or ambiguous, stop and surface the missing bridge decision.

Do not generalize from this witness before checking other parent-input constructor shapes. Posets from an existing poset, Cartesian products from factor parents, finitely presented modules from morphisms or free graded modules, module quotients, tensor components from a base module, and series-ring parent inputs are not automatically the same engineering problem. They must be classified by what Sage actually does with the input object.
