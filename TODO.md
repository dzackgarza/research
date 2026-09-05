# Preamble remediation queue

## Work selection

Use [the workstream board](TODO-WORKSTREAMS.md) to identify parallel work, claim edit paths, release reservations, and update overall progress.
Read its active claims before editing a shared mathematical owner.

Follow [the execution priorities](TODO-PRIORITIES.md#current-objective-and-order) and its boundary for local category work.
The active work is a general scheme-theory toolkit built on coherent module and affine-local algebra constructions.
Select a reported defect below when it blocks those constructions or causes dependent implementations to repeat an algorithm.
The witness observations record earlier findings; inspect the current owner before treating one as an outstanding defect.

## Active scheme and inheritance work

The source-grounded dependency assessment is [PORT_TODO.md §8.4](PORT_TODO.md#84-commutative-algebra-foundation-required-by-scheme-theory).
Use the existing quotient, localization, differential, and presented-module constructions as the starting point.

- [ ] Repair the shared prime-local unit and ideal operations in `rings/ring_foundation.py` and `rings/commutative_algebra.py`.
  Extend prime localization to reducible and nonreduced polynomial quotients, with their residue and comparison maps.
- [ ] Connect localized-module equality and vanishing to exact presentation algorithms in `modules/localizations.py`.
  Retain the existing localization functor and its transport of morphisms and exact constructions.
- [ ] Route successive affine closed embeddings through the existing quotient-of-presentation operation in `algebras/free_algebras.py`.
  Preserve relative presentations through parameter maps and scalar change, and connect all required owned map types to affine `Spec` and pushouts.
- [ ] Complete the underlying-module construction for each algebra used by the geometry, including its action on morphisms and initialized module state.
  Reuse module arithmetic, presentations, and linear-map algorithms through that structure.
  Inspect `categories/algebras/algebras.py` together with `categories/functors/algebra_modules.py`.
- [ ] Repair the shared constructor or functor path when an inherited operation cannot use its required state.
  Keep the repair in `owned_category.py`, `refine.py`, or the owning functor as appropriate.
  Use the [local Cat work criteria](TODO-PRIORITIES.md#how-much-category-theory-to-implement-here) to decide between automatic inheritance and explicit functor application.
- [ ] Extend existing affine structure-sheaf values to restriction morphisms, compatible covers, and sheaf gluing in `PORT_TODO.md` §§8.4–10.
  Restriction to charts and stalks must expose the same algebraic objects and inherited algorithms used outside scheme theory.
- [ ] Build the general actions, toric lattices, divisors, cycles, cohomology, local singularity theory, covers, and families in `PORT_TODO.md` §§11–16.
  Expose the resulting objects and maps through the notebook session as each construction becomes usable.
  Keep the detailed requirements and supported computational hypotheses in that file.

## Collection and finiteness remediation

Apply this queue to the active construction and its shared owners. Broad sweeps follow the surviving framework interfaces.

`CONTRIBUTING.md` policies `SET-01` and `CAT-08` are authoritative for this queue: mathematical collections in the preamble are owned sets/families, not Python sequences; iteration is lazy; whole-family `list`/`tuple` materialization is allowed only as transient private serialization after finiteness and order have been established mathematically.

- [x] Rebuild the ordered/enumerated-set spine so finite and infinite ordered sets share `__iter__`, membership, `cardinality`, `rank`/`unrank`, and positional access without requiring eager materialization.  `FiniteOrderedSet` must not store a mathematical collection as a Python list/tuple or silently consume an iterable of unknown cardinality.
- [x] Add/use owned indexed-family/image objects for families whose labels are distinct even when values repeat; in particular framing images and morphism generator images are indexed families rather than tuples or deduplicating sets.
- [x] Migrate free-module/framing APIs to retain their owned index sets/families throughout.  Finish the owned-`NN` positional-basis route, remove eager generator-position tables for infinite framings, and make bounded/finite convenience APIs explicit.
- [x] Repair `CartesianProductOfFamily`: callable sections over arbitrary index sets remain lazy; sequence-valued construction and full enumeration are finite specializations; never enumerate the index set merely to validate a section.
- [x] Rebuild module biproduct framings as tagged coproducts of framing sets and tensor-product framings as owned Cartesian products.  Dispatch finite presentation matrix backends only from `ModulesWithChosenFinitePresentation`, not the weaker existence property `FinitelyPresentedModules`.
- [x] Apply the same chosen-finite-presentation routing to `InternalHom` and the tensor/Hom adjunction; the Hom carrier remains constructible without enumerating either framing.
- [x] Rebuild `Sym^n`, `Lambda^n`, `Gamma^n`, and tensor-power indexing from actual combinatorial index sets (products, subsets, finite-support exponent families) rather than `len(tuple(framing))`; specialize to finite presentation matrices only at the finite backend boundary.
- [x] Rebuild alternating/divided-power algebra generator sets and construction comparison maps so they operate from graded/indexed sets and the finite support of the element being evaluated, never by enumerating the complete algebra generating set.
- [x] Make connection data an indexed family/callable over the module framing.  Do not evaluate a callable connection on every generator at construction time; finite relation checks consume only a chosen finite presentation.
- [x] Separate general callable forms/pairings from finite coordinate matrices.  `values_matrix`, coordinate pullback, and extensional equality must either require finite framing explicitly or return/use an indexed value family rather than exhaust an infinite framing.
- [x] Rewrite finite submodule basis computation over an infinite free module to restrict the backend coordinate problem to the finite union of supports of the supplied generators, rather than materializing the ambient basis.
- [ ] Replace mathematical tuples/lists of group generators, cosets, orbits, class-function values, discriminant elements/subgroups, lattice roots/orbits, Coxeter vertices, and catalogue configurations by owned sets or indexed families.  Finite GAP/Sage/OSCAR arrays remain private serialization only.
- [ ] Audit tensor component/shape/index storage and abstract product/direct-sum factor storage under `SET-01`; retain owned index/family objects and serialize finite arrays only in private tensor/CAS adapters.
- [ ] Finish scheme/polytope collection ownership (facets/fans and remaining factor collections) and profinite/Galois stage/embedding/conjugacy collections under the same rule.
- [ ] Final mechanical sweep of every remaining `tuple(...)`/`list(...)` occurrence under `src/dzack_research/preamble`: each survivor must be either syntactic ingress immediately parsed into an owned object or a private finite backend serialization boundary.

## Typing and witnesses

`just preamble-megadoc` constructs every owned category from a running session.  What it
cannot construct, it reports.  Both causes below are the same defect seen twice: the code
does not say, in a form anything can read, what a mathematical parameter *is*.

- [ ] **`LEX-12`, `LEX-14`: annotate the active construction and its shared interfaces.**
  Name the mathematical parameter domains and result categories as their owners are repaired.
  Preserve those domains when categories become `sage-categories` leaves.
  Complete the broad annotation pass against the surviving interfaces after transfer.

- [ ] **`LEX-01`, `LEX-12`: `OwnedParameterizedCategory` erases what its parameter is.**
  Every subclass declares `(parameter)` whatever the mathematics is, and the four in the
  session want four different structures: `Subgroups` a group, `DifferentialGradedModules`
  a DGA, `GradedAlgebraModules` a graded algebra, and `PredicateSubgroups` an entire
  category.  A wrong argument then fails deep inside — `TypeError: this API expects a
  preamble group`, `AttributeError: 'Owned_OwnedRingParent_with_category' object has no
  attribute 'grading_monoid'` — naming nothing about what was wanted.  Annotate the
  parameter with the category its values range over; the family is then constructible as
  `C(D.an_object())`.
  `categories/group/groups.py`, `categories/group/predicate_subgroups.py`,
  `categories/modules/dg_modules.py`.

- [ ] **`DEV-11`: complete the owned `an_object()` implementations needed by each construction.**
  `OwnedCategory` declares the contract in `categories/abstract_categories/objects.py`.
  Each specimen must inhabit its stated category and use its own constructors and inherited operations.
  The remaining witness observations below identify candidates for this work.

- [ ] **`STY-49`: graded-commutative algebras hard-refuse every grading but `ZZ`.**
  `GradedCommutativeAlgebras(R, M)` and `StrictlyGradedCommutativeAlgebras(R, M)` compare
  `M` against `ZZ` by identity and raise `NotImplementedError: Koszul graded commutativity
  is currently represented for the integer grading` otherwise.  Koszul signs need a parity
  homomorphism to `ZZ/2`, not the integers: assert the hypothesis the mathematics actually
  has — `assert M in Monoids()`, then the parity map — instead of an identity test against
  one monoid.  `categories/algebras/graded_commutative_algebras.py`.

- [ ] **`OwnedCategoryOverBaseRing` is exported into the session but is not a category.**
  `from dzack_research.preamble.all import *` binds it, and building it raises
  `NotImplementedError: <abstract method super_categories>`.  An abstract base belongs to
  the implementation, not to the session surface.
  `categories/rings/ring_foundation.py`.

- [ ] **`LEX-01`: four form functors have no `_repr_`.**  `FreeBilinearFormFunctor`,
  `BilinearUnderlyingModuleFunctor`, `FreeQuadraticFormFunctor` and
  `QuadraticUnderlyingModuleFunctor` fall back to Python's default, so
  `BilinearFreeFormAdjunction` and `QuadraticFreeFormAdjunction` print their adjoints as
  `<... object at 0x...>`.  Every sibling in `categories/functors/` names itself.
  `categories/functors/free_forms.py`.

## Witnesses: what `an_object()` found

`OwnedCategory.an_object()` is the contract (`DEV-11`); 121 of 153 owned categories
answer it with an object verified on both counts — the object is **in** the category,
and it is **owned**, not a Sage object refined into place.  Each item below is a
category whose canonical object fails one of those.  The witness is left as the
mathematics names it: relaxing it to something that passes would delete the finding
and leave the defect.

- [ ] **An object is not a module or an algebra over itself.**  `ZZ` is in
  `Algebras(ZZ)`, but `QQ`, `RR` and `GF(2)` are not in `Algebras` of themselves, and
  **no** ring is in `CommutativeAlgebras` of itself.  The same gap one level up: a
  graded algebra `A` is not in `GradedAlgebraModules(A)`, and a differential graded
  algebra is not in `DifferentialGradedModules` of itself.  Consequences reach far —
  `KahlerDifferentials(R)` raises `Kähler calculus requires a commutative algebra`,
  `Spec` must be fed a polynomial ring instead of the base, an `R[x]`-connection
  cannot be built over most `R`, and `tests/algebras/test_augmented.py` — a committed
  test — is red for this reason alone.  The obligations sweep's row
  `a ring as an algebra over itself` passes only because its specimen is `ZZ`.
  `categories/algebras/algebras.py`.

- [ ] **The scheme layer returns Sage objects.**  `AffineSpace`, `ProjectiveSpace`,
  `Spec` and `scheme_product` all return `sage.schemes.*`, refined into owned
  categories rather than owned.  Fourteen scheme categories report it; the cause is
  one.  Every other part of the preamble owns its objects.
  `categories/schemes/schemes.py`.

- [ ] **`End_R(Free_R([2]))` is placed in none of the categories a matrix algebra
  belongs to.**  It is what a matrix algebra *is* here — `MatrixSpace(R, 2)` returns
  exactly that Hom — yet it is in neither `MatrixAlgebras(R)`, `LieAlgebras(R)` nor
  `CommutatorLieAlgebras(R)`, over any of `ZZ`, `QQ`, `RR`.  So the endomorphism
  algebra of a free module reaches no algebra placement at all.
  `categories/algebras/algebras.py`, `categories/modules/pure/modules.py`.

- [ ] **The form-module joins do not contain their own members.**  U is in
  `FormModules(R)` and in `FramedFreeModules(R)`, and `FreeFormModules(R)` declares
  exactly those two as its supercategories, yet U is not in it.  Same for
  `FormedModules`, `PairedModules`, `FinitelyGeneratedFormModules` and
  `FinitelyGeneratedFreeFormModules`.  `Lattices` does not refine any of them.
  `categories/modules/framed/formed/form_modules.py`.

- [ ] **A free module over a field is not in `VectorSpaces(K)`**, whose only
  supercategory is `Modules(K)`.  `categories/modules/pure/modules.py`.

- [ ] **`A^1` is not normal and nothing is a variety.**  `NormalSchemes`,
  `Varieties`, `Curves` and `Surfaces` do not contain affine or projective space of
  the matching dimension, which are the standard objects of each.
  `categories/schemes/schemes.py`, `categories/schemes/varieties.py`.

- [ ] **A fiber product of schemes cannot be built.**
  `A^1 \times_{Spec R} A^1` fails with `no represented pushout is owned by a common
  category of R, R[x], R[x]`, over `ZZ` and over `QQ` alike — although `Pushout` of
  two commutative algebras over the same base does build.  So the scheme layer is not
  reaching the owned algebra pushout.  `categories/schemes/schemes.py`.

- [ ] **`scheme_product` cannot square a projective space**: two copies of `P^1`
  raise `variable name 'x0' appears more than once`; the second factor's coordinates
  are not renamed.  `categories/schemes/schemes.py`.

- [ ] **`closed_subscheme` requires a field.**  Cutting a hypersurface out of `A^2`
  over `ZZ` reaches Singular syzygies, which refuse a non-field coefficient ring, so
  no closed subscheme over `ZZ` can be built at all.
  `categories/schemes/schemes.py`.

- [ ] **`OpenSubschemes` has no constructor.**  It is the one owned category with no
  witness, because nothing in the preamble builds an open subscheme: no route
  produces the complement of a closed subscheme, and the name appears at no
  construction site.  The distinguished open `D(x) \subset A^1` is the smallest thing
  missing.  `categories/schemes/schemes.py`.

- [ ] **A parameterized category does not declare what its parameter is.**  `GSets`
  takes a group, `PredicateSubgroups` a category, `ModulesWithConnection` an algebra,
  `LocalizedModules` a localization ring — and none of that is in a type, so nothing
  can compute the parameter's own `an_object()` to instantiate the family.  This is
  the `LEX-14` item above, measured: the witness audit has to carry a hand-written
  table of ten specimens for exactly these categories.

- [ ] **`Spec(A)` and `A.spectrum()` are different objects.**  One prints
  `Spectrum of R`, the other `Spec(R)`, and they are not identical.  So the
  session has two names for what should be one notion, and `Spec` cannot leave
  the global surface until they are reconciled -- `ARC-12` has no owned
  spelling to move it to.  `categories/rings/commutative_algebra.py`,
  `categories/schemes/schemes.py`.

- [ ] **Ring constructions are not interned.**  Two calls to `R.localization(f)`,
  `R.localize_at_prime(p)`, `R.quotient_ring(I)` or `R.ideal(g)` return distinct
  objects that are not `is`-identical, and the first three are not even equal.
  `R.fraction_field()`, `R.adic_completion(I)`, `f.kernel()` and `f.cokernel()`
  are interned, so the discipline exists and these four are outside it.  Every
  `is` check and every coercion between two "equal" localizations is affected.
  `categories/rings/commutative_algebra.py`.

- [ ] **A folded construction is not the construction over the index set.**
  `C.product(factors)` folds the category's binary construction, so three
  factors give `(M_0 x M_1) x M_2` rather than the object over the three-element
  index set.  Both satisfy the universal property, and they are not the same
  object; `Sets.product` already builds the n-ary one directly, so the other
  categories are the ones to bring up to it.
  `categories/abstract_categories/objects.py`.

- [ ] **`Schemes.ParentMethods.product(self, *others)` still takes an arity.**
  A construction is taken over an index set (`CON-14`), so this reads a family
  like the category methods do, or it is operator notation.
  `categories/schemes/schemes.py`.


- [ ] **A span is not yet an object.**  `C.pushout(left_leg, right_leg)` names
  the two legs because no span diagram is constructed; the diagram vocabulary
  can express one (`DiagramCategory` is `[J,C]`, and `ConeCategory(diagram)`
  already owns its cones), so the span should be built over the shape
  `. <- . -> .` and own its own colimit -- `span.pushout()`, with
  `C.pushout(span)` the category-side spelling.
  `categories/abstract_categories/products.py`.

- [ ] **Sage's `join` and `meet` on categories are inverted relative to the
  inclusion order, and 27 owned call sites use them directly.**  Measured:
  `Category.join([Modules(ZZ), FiniteSets()])` is below both, so it is the
  *meet* of the inclusion-ordered lattice, while `Category.meet(...)` returns
  `Sets`, which is above both.  Sage names it for joining the axioms.  Both are
  operations on categories reached with the categories in argument position, so
  they belong on `Cat` (`ARC-12`), which is also where the naming can stop
  being inverted.  24 `Category.join` and 3 `Category.meet` across the preamble.
