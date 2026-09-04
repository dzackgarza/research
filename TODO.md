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

## Errors surfaced by the live preamble survey (2026-09-05)

`just preamble-megadoc` builds every owned category from a running session and reports
what refuses to build.  These are its findings, each to be fixed in the preamble, not
worked around in the survey.

- [ ] **The preamble is essentially unannotated.**  Of 4931 public functions and methods
  under `src/dzack_research/preamble`, 2422 take an argument beyond `self`, and 52 of
  those — 2.1% — annotate every argument.  Only 12.6% carry a return annotation at all.
  The Sage QC tier reports 7142 mypy errors across 137 preamble files as a consequence.
  Signatures are where a reader learns which category an operation is about, so an
  unannotated parameter is missing mathematics, not missing ceremony.  Annotate with the
  owned mathematical types (`Parent`, the owned category types, the element types), never
  with `object` or `Any`.

- [ ] **`OwnedParameterizedCategory` erases what its parameter is.**  `Subgroups`,
  `PredicateSubgroups`, `DifferentialGradedModules` and `GradedAlgebraModules` all
  declare `(parameter)`, so neither a reader nor a tool can tell that the first two want
  a group, the third a DGA and the fourth a graded algebra.  Building any of them with a
  ring fails deep inside — `TypeError: this API expects a preamble group`, or
  `AttributeError: 'Owned_OwnedRingParent_with_category' object has no attribute
  'grading_monoid'` — rather than at the signature.  Name each parameter for the
  structure it is (`supergroup`, `dga`, `graded_algebra`), the way
  `OwnedCategoryOverBaseRing` names `base_ring`.
  `src/dzack_research/preamble/categories/group/groups.py:1826`,
  `categories/group/predicate_subgroups.py:40`,
  `categories/modules/dg_modules.py:10` and `:36`.

- [ ] **Graded-commutative algebras exist only over the integer grading.**
  `GradedCommutativeAlgebras(R, M)` and `StrictlyGradedCommutativeAlgebras(R, M)` raise
  `NotImplementedError: Koszul graded commutativity is currently represented for the
  integer grading` for every `M` other than `ZZ`, including `NN`.  Koszul signs are
  defined for any grading monoid with a parity homomorphism to `ZZ/2`; represent that
  instead of hard-refusing.
  `src/dzack_research/preamble/categories/algebras/graded_commutative_algebras.py:21`
  and `:50`.

- [ ] **`OwnedCategoryOverBaseRing` is exported into the session but is not a category.**
  `from dzack_research.preamble.all import *` binds it, and building it raises
  `NotImplementedError: <abstract method super_categories>`.  An abstract base belongs to
  the implementation, not to the session namespace: drop it from the export surface.
  `src/dzack_research/preamble/categories/rings/ring_foundation.py:668`.

- [ ] **Four form functors have no `_repr_`.**  `FreeBilinearFormFunctor`,
  `BilinearUnderlyingModuleFunctor`, `FreeQuadraticFormFunctor` and
  `QuadraticUnderlyingModuleFunctor` fall back to Python's default, so
  `BilinearFreeFormAdjunction` and `QuadraticFreeFormAdjunction` print their adjoints as
  `<... object at 0x...>` — every sibling functor in `categories/functors/` names itself.
  `src/dzack_research/preamble/categories/functors/free_forms.py`.
