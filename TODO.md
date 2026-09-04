# Preamble remediation queue

## Collection and finiteness remediation

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

- [ ] **URGENT — `LEX-12`, `LEX-14`: annotate the preamble.**  Of 4931 public functions
  and methods under `src/dzack_research/preamble`, 2422 take an argument beyond `self`,
  and 52 of those — 2.1% — annotate every argument; 12.6% carry a return annotation.  The
  Sage QC tier reports 7142 mypy errors across 137 preamble files.  An annotation names
  the codomain and its reader is a mathematician (`LEX-12`), so an unannotated parameter
  is missing mathematics, not missing ceremony.  Annotate from the owned category graph,
  never from the framework's class tree (`LEX-14`), and never with `object` or `Any`.
  Everything below depends on this: a signature is the only place a tool can learn which
  category an operation takes and returns.

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

- [ ] **`DEV-11`: give every owned category an `an_object()`.**  `OwnedCategory` now
  declares it as an `abstract_method`; `OwnedGroups` and `OwnedRings` supply it, which is
  what makes `Subgroups(OwnedGroups().an_object())` and `Lattices(OwnedRings().an_object())`
  build.  Every other owned category still has none, so it cannot exhibit an inhabitant and
  nothing generic can construct over it.  Sage's inherited `Category.example` is not a
  substitute: it looks for a template under `sage.categories.examples` and returns the
  `NotImplemented` **singleton** when it finds none — silent where it must be loud, and
  answering for Sage's graph rather than the owned one.
  `categories/abstract_categories/objects.py`.

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

`OwnedCategory.an_object()` is the contract (`DEV-11`); 109 of 164 owned categories
answer it with an object verified to be both **in** the category and **owned**.  Each
item below is a category whose canonical object fails one of those two tests.  The
witness is left as the mathematics names it — relaxing it to something that passes
would delete the finding and leave the defect.

- [ ] **The scheme layer returns Sage objects.**  `AffineSpace`, `ProjectiveSpace`,
  `Spec` and `scheme_product` all return `sage.schemes.*`, refined into owned
  categories rather than owned.  Sixteen scheme categories report it; the cause is
  one.  Every other part of the preamble owns its objects.
  `categories/schemes/schemes.py`.

- [ ] **`R` is not in `CommutativeAlgebras(R)`**, though it is in `Algebras(R)`.  A
  commutative ring is a commutative algebra over itself.  The gap stops
  `KahlerDifferentials(R)`, which raises `Kähler calculus requires a commutative
  algebra`, and forces `Spec` to be fed a polynomial ring instead of the base.
  `categories/algebras/algebras.py`.

- [ ] **`MatrixAlgebras(R)` does not contain `End_R(Free_R([2]))`**, which is what a
  matrix algebra *is* in this preamble.  `MatrixSpace(R, 2)` is in it, so two routes
  to the same object disagree on placement.
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

- [ ] **`scheme_product` cannot square a projective space**: two copies of `P^1`
  raise `variable name 'x0' appears more than once`; the second factor's coordinates
  are not renamed.  `categories/schemes/schemes.py`.

- [ ] **`closed_subscheme` requires a field.**  Cutting a hypersurface out of `A^2`
  over `ZZ` reaches Singular syzygies, which refuse a non-field coefficient ring, so
  no closed subscheme over `ZZ` can be built at all.
  `categories/schemes/schemes.py`.

- [ ] **26 categories still have no witness.**  The chosen-structure ones
  (`AlgebrasWithChosenMultiplication`, `AlgebrasWithChosenFinitePresentation`,
  `AugmentedAlgebras`, `GradedAugmentedAlgebras`, the algebra coproducts and
  pushouts) need an object carrying the chosen datum, and no reachable constructor
  produces one; `LieAlgebras`, `CommutatorLieAlgebras`, `ModulesWithConnection`,
  `ModulesWithFlatConnection`, `GSets`, `FiniteGSets`, `PredicateSubgroups`,
  `RationalLattices`, `LocalizedModules`, `FractionFieldQuotients`,
  `RestrictedScalars*`, `FormalDivisorGroups`, `LebesgueGradedModules`,
  `GradedTensorProductModules`, `OpenSubschemes` and `FiberProductSchemes` are the
  rest.  `OwnedCategoryOverBaseRing` is on that list only because it is an abstract
  base exported as though it were a category.
