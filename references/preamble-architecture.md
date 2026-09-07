# Preamble construction and inheritance

Architectural assessment and proposed design, 2026-09-07.
Source revision: `84c8f978`.
The [architecture work queue](../TODO.md#architecture-before-dependent-implementation) owns implementation and completion state.

The principal defect is a separation between category membership, construction of defining data, and the meaning of inherited operations.
Class inheritance now supplies methods, but several constructors still reconstruct their mathematical structure afterward.
Specialized implementations then repair the resulting gaps independently.
The remedy is to make construction establish each category's defining data and to transport operations through the correct structural functors.

## Evidence and scope

- **Searched:** current constructor, action, algebra, Hom, framing, and runtime sources linked below; relevant Git history from August 24 through September 6; the existing threading plan; and the `sage-categories` module, algebra, and leaf specifications.
- **Found:** the concrete construction paths below share ownership failures despite existing common category machinery.
- **Conclusion:** the evidence supports a foundational construction and inheritance repair before dependent API expansion. This is an architectural inference from these paths.
- **Confidence:** high for the stated source behavior and mathematical distinctions; moderate for the proposed migration boundaries.
- **Gaps:** the remaining mathematical subtrees have not received a complete semantic review. Runtime behavior and the proposed replacement interfaces are unverified under the current testing policy.

### Defining actions are reconstructed from stronger structure

[`Modules.ParentMethods._ring_morphism_defining_module_action`](../src/dzack_research/preamble/categories/modules/pure/modules.py)
builds the action with target `Modules(R).End(M)`.
[`GeneralModules.ParentMethods._build_scalar_action_morphism`](../src/dzack_research/preamble/categories/modules/general_modules.py)
and the corresponding [localization method](../src/dzack_research/preamble/categories/modules/localizations.py) repeat this construction.
The general constructor retains the input `rho` separately and constructs another action for its public accessor.
The scalar evaluations pass `verify_linearity=False`.

For a general left module, the target must be the endomorphism ring of its underlying additive group.
Left multiplication by a scalar need not be an endomorphism of the left module.
For example, take the left regular module over `R = M_2(Q)`, with `r = E_12` and `s = E_21`.
Then

\[
L_r(sI)=E_{11},\qquad sL_r(I)=E_{22}.
\]

Thus `L_r` is additive but not `R`-linear.
Testing only commutative scalar rings cannot distinguish these two proposed targets.
Even over a commutative ring, deriving the defining action from an already constructed module reverses the construction dependency.

### General algebra construction depends on a finite presentation

[`algebra_from_multiplication`](../src/dzack_research/preamble/categories/algebras/algebras.py)
accepts a module multiplication morphism, then routes through `_module_presented_by_multiplication`.
That helper requires a finite module generating set and `_same_presentation_module`.
Its default unit recovery solves a finite linear system.
The generic `multiplication_morphism()` accessor can also enumerate pairs of module-generator labels.
By contrast, `own_algebra(structure_map)` constructs an engine-backed algebra directly.

These are different presentation routes with different effective domains.
Finite presentation has reached the definition of an algebra, although it belongs to particular algorithms and input formats.
The existing module, tensor, and algebra owners can provide the common mathematical construction.

### Lie structure bypasses the general multiplication owner

[`LieAlgebras.super_categories`](../src/dzack_research/preamble/categories/algebras/lie_algebras.py)
names `Modules(R)`.
The same file defines a separate Lie morphism class and a bracket-preservation check.
Meanwhile, [`AssociativeAlgebras.super_categories`](../src/dzack_research/preamble/categories/algebras/algebras.py)
places associative algebras in the commutator Lie category.
The [commutator functor](../src/dzack_research/preamble/categories/functors/commutator_lie_algebras.py)
returns its input parent as its object image.

There are two distinct multiplications here: the original product and its commutator.
They define different algebra structures on the same underlying module.
A general multiplication owner would let Lie objects reuse algebra construction while keeping this functor distinct from inclusion.

The [existing algebra conversion](../TODO.md#the-algebra-node-conversion-designed-and-part-built)
already selects this general node and records the unfinished `work/algnode` candidate.
That work is an input to the repair.
The selected-multiplication construction at `57465081` still transports through represented module presentations, so the action and presentation boundaries also need attention.

The inheritance issue also affects universal constructions.
`LieAlgebraMorphism` inherits [`ModuleMorphism.cokernel`](../src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py),
which requests a quotient module by the image.
For a Lie morphism, the cokernel is the quotient by the Lie ideal generated by the image.
For example, include the diagonal Cartan subalgebra in `sl_2(Q)`.
Its linear cokernel has dimension two, while its Lie cokernel is zero: the ideal generated by the diagonal element contains both root vectors.
Sharing evaluation and linear algorithms is useful; transporting a universal construction requires its categorical justification.

### A generic action constructor depends on schemes

[`GSets`](../src/dzack_research/preamble/categories/group/g_sets.py) already uses `GObjects(G, Sets())`.
The general action owner therefore exists.
However, [`GObjects._call_`](../src/dzack_research/preamble/categories/group/g_objects.py)
imports the scheme subtree and dispatches specifically to affine G-schemes.
Its `action()` accessor constructs a set map into endomorphisms and checks the selected group relators when available.

The generic owner should construct an action in the supplied category.
Affine schemes should provide a way to construct that datum through their contravariant ring theory.
Adding another category of acted objects should then require its own mathematical construction, rather than another case in `GObjects`.

### Chosen data can be absent despite inherited accessors

[`FramedModules.ParentMethods.__init__`](../src/dzack_research/preamble/categories/modules/pure/modules.py)
accepts both framing fields as `None`.
Its concrete accessors return those fields unless a descendant overrides them.
This puts a required choice behind optional constructor arguments.

The current code does distinguish `FinitelyGeneratedModules`, `FinitelyPresentedModules`, and `ModulesWithChosenFinitePresentation`.
The [selected-presentation implementation](../src/dzack_research/preamble/categories/modules/framed/finitely_generated/finitely_presented_modules.py)
also returns an isomorphism of presentation arrows during Smith normalization.
These distinctions should survive the repair.
What needs strengthening is construction of the required datum at the level that declares it.

### Class assembly and initialization have separate paths

[`owned_category.py`](../src/dzack_research/preamble/owned_category.py)
already retains category method classes as actual bases and supports an `ABCMeta` crossing.
That crossing depends on abstract declarations in the contributing classes.
The module action and framing accessors examined above are concrete methods, so their existence does not establish valid construction data.

[`refine.py`](../src/dzack_research/preamble/refine.py) runs newly reached `__init_extra__` hooks.
[`CategoricalHomset.__init__`](../src/dzack_research/preamble/categories/abstract_categories/hom_categories.py)
instead calls `CategoryObject._refine_category_` directly after Sage initialization.
`object_of` delegates directly to the generated `ObjectType`.
These paths need one construction contract, including the private Sage initialization boundary.

## What recent changes establish

The relevant history shows useful shared machinery followed by repairs at individual construction routes:

| Change | Architectural consequence visible in current source |
| --- | --- |
| `6382e161`, September 5: category classes retain their construction bases | Cooperative construction can supply inherited state. The runtime substrate already exists. |
| `3d57090e`, September 5: framing owns its epimorphism | A common mathematical owner removes repeated presentation logic. Optional inputs still weaken that owner's contract. |
| `fc3e7c35`, September 6: scalar registration moves to `__init_extra__` | Engine adoption and ordinary construction reach the module level differently. Registration of arithmetic syntax does not establish the defining ring morphism. |
| `3787d8ff`, September 6: refinement runs new construction hooks | Placement can trigger initialization after object construction. A source of repeated route-specific repairs remains. |
| `5cc61c23`, September 6: Lie Hom acquires bracket preservation | Inherited module Hom did not express the added multiplication. A local Hom repair leaves the general algebra owner disconnected. |

The failure mechanism is broader than omitted methods.
Placement supplies an interface before construction has established its meaning.
Local repairs then add state recovery, narrower constructors, or additional dispatch.
The remedy must constrain that dependency, rather than ask contributors to remember more leaf-specific obligations.

## Proposed mathematical construction

### Module actions

For an ordinary unital ring `R`, construct a left module from an additive group `X` and a unital ring morphism

\[
\rho:R\longrightarrow\operatorname{End}_{\mathbf{Ab}}(X).
\]

The target determines `X`, and the source determines `R`.
The additive-group owner constructs its endomorphism ring using pointwise addition and composition.
This supplies the input to module construction before an `R`-module exists.
Every ordinary module constructor must establish this action and expose it through the module-owned `scalar_action()`.
It can construct the morphism lazily from a complete mathematical presentation; it need not enumerate endomorphisms.
Scalar evaluation must use the same action that the accessor returns.
Module morphisms are additive maps satisfying `f rho_M(r) = rho_N(r) f`.

For nonconcrete categories, use the more general action morphism `A bullet X -> X` in a supplied actegory.
The defining parameters include the monoidal category, its action, the monoid object `A`, and their coherence maps.
The endomorphism presentation follows when the required enrichment and adjunction exist.
These are already the definitions in the sibling project's
[module specification](../../gitclones/sage-categories/specs/modules.md).
Ordinary ring modules specialize this construction using abelian groups and their tensor product.
Selecting `Sets()` alone does not specify this module category or its scalar ring.

The one-object formulation uses an **Ab-enriched** category with endomorphism ring `R` and an enriched functor to `Ab`.
Ordinary multiplicative actions omit additivity in the scalar variable.
For groups, an ordinary functor `BG -> C` gives the action, and natural transformations give equivariant morphisms.
The distinction follows the [enriched module definition](https://ncatlab.org/nlab/show/module%2Bover%2Ban%2Benriched%2Bcategory).

### Presentations construct the action

Over a PID, invariant factors and a free rank determine a standard finite presentation.
Construct its cokernel in modules, with the quotient action

\[
\rho_M(r)(q(x))=q(\rho_F(r)(x)).
\]

Stability of the relation submodule makes this action well-defined.
The presentation route must return the same action contract as the direct morphism route.
Restriction of scalars along `a:S -> R` gives `rho_M compose a`.
Transport through an additive isomorphism `h:X -> Y` gives `r |-> h rho_M(r) h^{-1}`.
These constructions belong to their existing functors, with both object and morphism actions.

A framing is a selected epimorphism `F_R(S) -> M`.
A finite presentation additionally selects a finite relation module and the presentation arrow.
Finite generation and finite presentation as properties assert existence of such data.
Their property subcategories retain the original module morphisms.

The proposed category of selected presentations uses commuting diagrams as morphisms.
Its forgetful functor to modules must state which maps it forgets.
If a caller needs every module morphism while retaining a presentation for computation, that is a different category and must be declared as such.
The existing [framing design](../TODO.md#framed-designed-and-not-built) already treats framings as additional structure and uses comma-category language.
Complete its morphism specification before implementation: arbitrary maps between the free modules differ from maps induced by functions between their label sets.
The selected-presentation normalization already uses arbitrary linear changes of basis.

Forgetting a framed associative algebra also changes the presentation data.
An algebra framing by a set `S` induces a module framing indexed by words in `S`.
The [algebra-to-module functor](../src/dzack_research/preamble/categories/functors/algebra_modules.py)
already constructs underlying modules of free algebras through their graded pieces.
Retain that structural construction while moving its input contract to the algebra owner.

Invariant factors classify underlying finitely generated modules over a PID, rather than all selected presentations.
Adding `R --id--> R` as a direct summand to a presentation preserves its cokernel but changes the ranks of its free terms.
Thus those presentations need not be isomorphic as diagrams.
The existing Smith-normalization arrow isomorphism supplies the appropriate model for retaining chosen data.

### Multiplication and algebra axioms

For a commutative base ring, the common algebra datum is an `R`-module and a morphism

\[
m:A\otimes_R A\longrightarrow A.
\]

The proposed `Algebras(R)` owns this general bilinear multiplication.
Associativity and the Lie identities define property subcategories of this category.
In particular, `Algebras(R).Lie()` retains the same multiplication-preserving morphisms.
The [Lie definition](https://doc.sagemath.org/html/en/reference/algebras/sage/algebras/lie_algebras/lie_algebra.html)
includes alternation and Jacobi; skew-symmetry alone is insufficient in characteristic two.
Sage's [magmatic algebra category](https://doc.sagemath.org/html/en/reference/categories/sage/categories/magmatic_algebras.html)
provides an existing implementation reference for the broad multiplication owner.

A unit adds the morphism `R -> A`, with its unit equations and its preservation condition on algebra morphisms.
It must be supplied or constructed by an applicable algorithm.
A multiplicative map need not preserve a unit: the zero map of a nonzero field is a simple counterexample.
Thus adding a unit requires more than copying the Hom of the nonunital category.

For associative unital algebras over commutative `R`, the equivalent central structure datum is

\[
\psi:R\longrightarrow Z(A).
\]

This is the direction stated in the current `Algebras` definition.
The multiplication and central-map constructors must establish the same algebra structure and inherited module action.
The central-map description requires the associative unital context.
For a noncommutative base, a tensor product of arbitrary left modules does not supply this monoidal structure.
Use the specified bimodule construction where appropriate, as in the sibling
[algebra specification](../../gitclones/sage-categories/specs/algebras.md).

The commutator functor sends `(A,m)` to `(A,m-m compose tau)`.
It preserves the underlying module but changes the multiplication.
Its morphism action follows from the multiplication-preservation equation.

The existing algebra-conversion decision changes the present `Algebras` name to this general node.
Both current `main` and the sibling algebra specification still use the associative unital meaning.
Reconcile the sibling specification with the general node and its associative unital subcategory before transferring algebra consumers.
The remaining design issue is the uniform defining-data contract, including the unit-preservation condition on morphisms.

## Construction and enforcement

The defining category owns required constructor inputs, their endpoint conditions, and concrete accessors for the established data.
A leaf supplies its added structure through its immediate mathematical owners.
Alternative constructors produce that same data, including any required transport maps between representations.
The completed object has one public structure regardless of its private representation.

Property refinement retains the existing data and narrows a mathematically stated condition.
Adding an action, multiplication, form, or framing is construction of additional structure.
The common runtime boundary must establish inherited data before returning the object.
Sage arithmetic registration can follow that construction; it must use the established action.
Engine adapters must enter through the same mathematical constructor obligations.

The same discipline applies to elements and fixed-endpoint morphisms.
Their parent, endpoints, evaluation, identity, composition, and preservation equations belong to the corresponding owners.
A Hom constructor must establish the added structure's preservation condition.
Universal constructions can reuse an underlying construction when the relevant functor creates or preserves it, with its canonical maps.
Otherwise the stronger category supplies the required construction, such as ideal closure for Lie cokernels.

| Obligation | Existing mechanism to use | What it establishes |
| --- | --- | --- |
| Required defining data | Category-owned constructor parameters and endpoint checks | The object has the datum its inherited methods use. Accessors are implemented once there. |
| Operations requiring an implementation | Sage `abstract_method`; existing `ABCMeta` support where instantiation must enforce implementation | The declared operation is supplied. It does not prove its mathematical laws. |
| Discoverable required methods | Sage `abstract_methods_of_class` on the actual generated parent and element classes | Contributors can inspect inherited obligations without maintaining a separate list. |
| Mathematical behavior | Inherited Sage `_test_*` methods and public construction examples | Concrete violations of action laws, endpoint conditions, or preservation equations become observable. |
| Public static interfaces | Types at constructors, structure maps, and Hom endpoints; the upstream static projection | Callers see the selected category's operations and mathematical input/output types. |
| Python dependency direction | Focused Import Linter contracts for generic owners and specialization packages | Generic construction code cannot import the specialized consumer it is meant to support. |

Sage's [abstract-method descriptor](https://doc.sagemath.org/html/en/reference/misc/sage/misc/abstract_method.html)
raises when an unimplemented required method is accessed; the decorator alone does not prevent instance construction.
The existing ABC crossing can enforce instantiation obligations, but required stored data should already be supplied by construction.
Avoid making every leaf reimplement an accessor that a common constructor can fulfill.

Sage [discovers inherited `_test_*` methods through `TestSuite`](https://doc.sagemath.org/html/en/thematic_tutorials/coercion_and_categories.html).
Use that discovery instead of a parallel contract registry.
Executable examples must distinguish the intended mathematics, including noncommutative scalar actions and nonidentity morphisms.
Finite calculations establish the cases they decide; arbitrary callable maps need mathematically justified construction rules.
Equality of arbitrary presented structures or maps is not a general decidable Boolean contract.

[Import Linter's forbidden contracts](https://import-linter.readthedocs.io/en/latest/contract_types/forbidden/)
can check indirect dependencies as well as direct imports.
Start with the observed generic-action-to-schemes dependency and generic-module-to-group-module dispatch.
Place specialization constructors and example factories at their own owners so those boundaries express actual ownership.
An import check cannot decide whether a functor preserves a cokernel or whether a category declaration is mathematically correct.
The semantic source review follows the defining datum through construction, a structural functor, and a dependent operation.

The current [verification policy](../TODO.md#testing-is-deferred-until-every-other-item-is-done-always-on)
defers execution until the final phase.
Construction contracts and their falsifying examples can be implemented together, with the examples recorded as unverified.
Automated feedback on their coverage starts when that policy permits execution.
Earlier runtime checking requires a separate decision about that policy.

## Ownership and extension

The existing [framework boundary](../TODO.md#how-much-category-theory-to-implement-here) remains the division of responsibility.
`sage-categories` owns generic structure functors, monoidal actions, class assembly, and static projection.
The preamble owns its mathematical categories, construction data, algorithms, and current consumers.
Repair its existing common construction path where needed to complete an actual dependency.
Transfer a construction when the upstream public interface supplies its objects, morphisms, functors, and inherited behavior.

The foundational order starts with objects, morphisms, and selected categorical products or tensors.
Magma and monoid objects add operations and their equations; additive groups supply the additive structure needed for rings.
Rings and additive endomorphisms supply ordinary module actions.
Modules with the required tensor structure supply bilinear algebras and their axiom subcategories.
Ideals, scalar change, and localization then supply the local algebra used by schemes.
Each level owns the maps that connect it to the preceding structure.

This keeps future extension local to its mathematical owner.
Sheaf modules use internal ring and module structure together with restriction and descent maps.
Scheme operations use those local algebraic constructions through affine charts and gluing.
Changing the category in which objects live should preserve the action-diagram formulation.
Higher or derived settings additionally require their own coherent categorical structure; ordinary equality of composites does not supply it.
The present design therefore exposes the categorical parameters and maps on which those later extensions depend.

The [contribution procedure](../CONTRIBUTING.md#preamble-design-philosophy) directs a writer to the immediate owner and its constructor.
The [work queue](../TODO.md#architecture-before-dependent-implementation) orders the repair by those dependencies.
