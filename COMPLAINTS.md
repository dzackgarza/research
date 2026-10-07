# Foundational Gaps and Papercuts

Record unresolved issues observed anywhere in research or contribution work.
The primary subject is general mathematical machinery that should be available but is missing, incomplete, or bypassed in the owned language.
Concrete workflow papercuts also belong here.
This is neither a retrospective work log nor a list of hypothetical defects.

Use the [mathematical tracing method](CONTRIBUTING.md#mathematical-dependency-tracing) and the capture/lifecycle rule [`DEV-59`](CONTRIBUTING.md#dev-59-record-observed-foundational-gaps-and-papercuts).
State the mathematics before its implementation symptoms.
Extend an existing entry when another consumer exposes the same foundation.
Link execution details in [TODO.md](TODO.md); it owns implementation ordering under the single-worker `DEV-61` rule.
Remove resolved entries with evidence in the commit, retaining only unfinished needs and any required terminal verification.
Durable definitions and decisions belong at their mathematical declarations or in CONTRIBUTING, not solely here.

## Foundational Mathematics

### Backing-core constructor narrowing and colimit lifting block integration specimens

The backing core must preserve the constructor of a fixed-endpoint Mor under
property restriction and must use a selected forgetful functor's supplied
coequalizer lifting. These are prerequisites for owned subset inclusions and
presented modules, respectively.

Fresh Sage execution on rack at sage-categories `5867543f` demonstrates two
failures. `Mor(Sets)(X,X).Monomorphisms().construction_owner()` returns the
unfixed Mor family, so supplying a map raises a missing-`codomain` error.
`SetSubobjects.from_predicate` reaches that route. Separately, the existing
presented-module consumer over M2(F2) registers the required colimit lift but
`FullSubcategory.colimit_construction` delegates to its ambient without
consulting selected-functor liftings; the coequalizer construction fails.

The inspected core already implements nested group construction, composite
structure transport, exact-category implementation installation and lifted
universal maps, with passing consumers in this assessment. The gap is the
shared constructor/dispatch route, not a claim that those foundations are
absent. The source owners, minimal reproduction, runtime and exact coverage
boundary are in [the execution assessment](docs/sage-categories-readiness.md).
The backing-core repair belongs to sage-categories; its research consumers
are `constructor-discovery` and `optional-sage-categories-property-layer` in
TODO. Later module factorization assertions remain unverified until quotient
construction succeeds.

### Fixed Mor categories with discrete 2-Morphisms do not realize their discrete universal constructions

For an ordinary represented fixed Mor category `Mor_C(A,B)` whose selected
2-Mor family is discrete, the objects are the represented arrows `A -> B` and
there is only an identity 2-morphism on each object.  Its finite universal
constructions are therefore exactly those of the discrete category on that
arrow set.  In particular `Mor_Set(*,*)` for a singleton set has one object and
is the terminal category, so every represented finite diagram into it has the
unique arrow object as both limit and colimit.  This statement does not apply
to special fixed Mor categories that declare a non-discrete 2-Mor, such as
functor categories with natural transformations.

Observed during `category-method-coverage-sweep` on 2026-09-25:
`FixedMorCategory`/`CategoricalMor`
(`categories/abstract_categories/mor_categories.py`) select
`_DiscreteTwoMorCategoryOf` for their ordinary 2-Mor, but source search finds no
`_categorical_product`, `_categorical_coproduct`, `_categorical_equalizer`,
`_categorical_coequalizer`, or family realization on that discrete fixed-Mor
route.  Consequently even the one-object `End_Set(*)` cannot answer the
universal operations inherited from `Cat`.  `_FunctorCategory` is explicitly
excluded: it overrides the 2-Mor with natural transformations and therefore is
not evidence that `MorCategories()` as a whole is discrete.  This is source
evidence; pre-T execution remains suspended by `DEV-58`.

**Dependency path:** fixed Mor with `_DiscreteTwoMorCategoryOf` -> discrete
category on represented arrows -> selected universal construction with forced
identity 2-morphisms -> the inherited `Cat` product/(co)equalizer and
`Limits`/`Colimits` operations.
**Consumers:** `test_mor_categories_construct.sage`, induced functors between
ordinary fixed Mor categories, and any construction using such a Mor category
as a diagram target.
**Coverage boundary:** the ordinary discrete fixed-Mor route and the singleton
set specimen were inspected; no claim is made about non-discrete specializations.
Repair: `discrete-fixed-mor-universal-constructions` in [TODO.md](TODO.md).

### Discrete categories do not realize universal constructions that exist

The discrete category on one object is the terminal category.  Every diagram
into it has exactly one cone and one cocone, hence its limit and colimit are the
unique object.  More generally, a finite product, coproduct, equalizer or
coequalizer in a represented discrete category exists exactly when the
corresponding universal cone/cocone exists; when it exists its structure maps
are forced identities.  Nonexistence for other discrete diagrams is part of
the mathematics and should be reported as such, not conflated with an absent
implementation.

Observed during `category-method-coverage-sweep` on 2026-09-25:
`DiscreteCategory` (`categories/abstract_categories/functors.py`) represents
objects and their identity-only Mor correctly, but defines none of the
`_categorical_product`, `_categorical_coproduct`, `_categorical_equalizer`,
`_categorical_coequalizer`, or family construction hooks inherited from
`Cat.ParentMethods`.  Thus even `Disc({*})` cannot realize the finite universal
constructions that are mathematically forced.  The same omission prevents the
generic selected `Limits`/`Colimits` reduction from reaching its valid answer.
This is source evidence; pre-T execution remains suspended by `DEV-58`.

**Dependency path:** represented discrete category -> existence criterion for
the relevant universal cone/cocone -> selected universal construction with its
identity structure maps -> generic product/(co)equalizer reduction ->
`Limits`/`Colimits` and their functors.
**Consumers:** `test_discrete_categories_construct.sage`, finite diagram
constructions, and every consumer using a discrete target as an actual
category rather than merely as an indexing shape.
**Coverage boundary:** the one-object case and the missing construction hooks
were inspected. Repair: `discrete-category-universal-constructions` in
[TODO.md](TODO.md).

### Set-theoretic behaviour is re-implemented instead of wired to a set engine

A set is determined by its membership condition. A finite set of listed points
decides membership by the points' identity; a set given by a predicate decides
it by the predicate; the image of a map decides it by an inverse or an inverse
image. An enumeration is a further chosen datum -- a bijection from an ordinal
onto the set -- which supplies order and rank and never decides membership.
Maintained engines already implement each of these: Sage's `Set` (a hashed
`frozenset`), `ConditionSet`, `ImageSubobject`, `cartesian_product`,
`DisjointUnionEnumeratedSets`, `Subsets`, `FiniteSetMaps`, `IntegerRange`,
`NonNegativeIntegers`; SymPy's `FiniteSet`, `ConditionSet`, `ImageSet`; GAP's
collections.

The preamble's set layer (`categories/sets/set_categories.py`,
`categories/sets/finite_ordered_sets.py`) instead builds every finite set as an
index set plus position/point lambdas and derived membership by comparing a
candidate with every point. Observed on 2026-09-23: framing labels are SR
symbols, each comparison is a symbolic proof attempt, and the star import took
460 s (a rank-8 lattice took 3.3 s, growing cubically). `from_indexed` now
defaults to Sage's hashed `Set` and a hash map for positions (`77b05adb`), and
product points keep their components (`cfc27a51`); the rest of the layer still
hand-rolls what the engines above compute:

| Owned construction | Membership now | Engine that computes it |
| --- | --- | --- |
| `_ImageSet` | inverse, or `Set` of the values for a finite source | `ImageSubobject(map, domain, inverse=...)` |
| `CartesianProductsOfSets` | category default; points rebuilt through factor constructors | `cartesian_product` |
| `CoproductsOfSets` | parent identity | `DisjointUnionEnumeratedSets` |
| `PowerSets`, `FixedCardinalitySubsetSets`, `FinitePowerSets` | hand-written through subobject placement (iteration already uses `Subsets`) | `Subsets(X)`, `Subsets(X, k)` |
| `FunctionSets` | membership in the owned Mor | `FiniteSetMaps(X, Y)` |
| `_ConditionSet` | the predicate (correct in shape) | `ConditionSet(universe, predicate)` |
| `AugmentedSimplexCategory`, `NN` | bounds checks (correct in shape) | `IntegerRange(n)`, `NonNegativeIntegers()` |

The set layer is one instance. The same afternoon found an owned matrix
algebra, with its tensor-algebra framing, built for every lattice in order to
take one determinant (now Sage's matrix determinant, `_gram_determinant`), a
real-number relation decided by Maxima's `simplify_full` before `AA` or Arb
were tried (`rings/real.py`), and each Gram entry re-derived by building and
expanding a pure tensor. The general need is that owned objects keep public
mathematics owned and route computation through a maintained engine
privately (`OWN-06`); where the preamble re-rolls an engine's behaviour, the
owned code is a second, slower, less correct implementation.

**Consumers:** every framed module (framing labels), tensor products (pair
labels), lattices and forms (Gram entries), catalogues, and every membership
test in construction admission.
**Coverage boundary:** the set layer's constructions were read; other layers
were found only where profiling of the star import led. The audit of the
whole preamble for engine behaviour re-implemented locally is the TODO node
`engine-wiring-audit`.

### Chosen generators are encoded as a global axiom instead of a resolution

A chosen generating epimorphism, a chosen presentation and a chosen syzygy
tower are truncations of one datum, a resolution of the object by free (or
`P`-projective) objects, and they belong to a category of resolutions over
`C` (`CAT-29`). The tree encodes the first of them as a global `Framed`
axiom on `Objects`, with `FramedModules(R)` and `FramedAlgebras(R)` as its
specializations, and decides membership by whether a framing was stored on
the object. Every object is resolvable -- the counit `F(UX) ->> X` starts the
canonical comonadic resolution -- so the axiom names no property, and Sage's
joins, which close under axioms, propagate it across branches as if it were
one.

Observed on 2026-09-25: the meet of `ZZ.category()` and `RR.category()`
contains `Algebras(ZZ).Associative().Unital().Framed()`, `ZZ` is not placed
there, and `RR.coerce_map_from(ZZ)` raises `ValueError`, so `4 / pi**2`
fails. Placing `ZZ` with its empty algebra framing moves the failure to
`QQ.coerce_map_from(ZZ)`: the meet then carries `Framed` on `Modules(ZZ)`.
Rack's separation of algebra framing from module framing (`09215fd7e`) made
framings relative to their category, which the global axiom cannot express.

**Dependency path:** resolutions over `C` (`lean-categories` `FOUNDATIONS.md`
§76-77 for the additive case, extension filed as dzackgarza/lean-categories#62;
simplicial objects over a projective class in
general) -> truncations and finiteness properties -> chosen generators and
presentations -> coercion and every consumer of chosen generators.
**Consumers:** coercion of session integers into `QQ` and `RR`; algebra
generators, presentation display, module generators, the matrix-unit algebra
structure of `End_R(F)`; the `tests/functions` Lebesgue tests and the D4
Gaussian heuristic.
**Coverage boundary:** the `Framed` population was counted by the `rg` in the
`framed-axiom-retired` node; the coercion was observed for `ZZ` into `QQ` and
`RR` only. Repair: `categories-of-resolutions`, `framed-axiom-retired`,
`integers-coerce-into-rationals-and-reals` in [TODO.md](TODO.md).

### Indefinite integral lattices of rank at least three have no exact represented-value witness backend

For an integral lattice `L` and integer `n`, `representation_vector(n)` must
return an integral vector `v in L` with `q(v)=n`, or establish that none
exists. Rational solvability of `q(v)=n` is a different problem. The current
tree has exact maintained routes for the two lower-complexity regimes:
definite lattices enumerate exact vectors through PARI `qfminim`, and Sage's
`BinaryQF.solve_integer` delegates binary integral equations to PARI
`qfbsolve`. Installed Sage/Hecke/OSCAR source was searched for the higher-rank
integral operation. Hecke supplies rational quadratic-space isotropy,
isometry-class representation and hyperbolic decomposition, but no complete
integral lattice witness for a prescribed norm; OSCAR exposes the same
quadratic-space layer here. Thus `QuadraticForm.solve`/Hecke `represents`
cannot be used to justify the requested integral result.

**Dependency path:** exact local integral representability -> strong
approximation/Kneser construction in indefinite rank at least four; in rank
three, local conditions plus the spinor-exceptional square classes -> exact
integral witness or exact nonrepresentation.
**Consumers:** `Lattices(ZZ).representation_vector(n)` and `represents(n)`;
the distinguishing specimens are `U+U` at `n=0` and
`-(x^2+y^2+z^2)` at `n=-7`.
**Coverage boundary:** Sage's quadratic-form and binary-form sources, the
installed Hecke/Oscar quadratic-form sources, and the repository's current
lattice engine capability map were inspected. No complete maintained exact
rank-at-least-three integral witness route was found. Repair requires the
`higher-rank-representation-engine-ruling` and then
`higher-rank-integral-lattice-representation` nodes in [TODO.md](TODO.md).

### The genus of an odd integral lattice has no owned object

Two integral lattices are in one genus when they are equivalent over `RR`
and over `ZZ_p` for every prime `p` [CS10, Ch. 15, §7]. The owned
`Lattices(ZZ).genus()` asserts `is_even()` and returns a `Genus` built from
the signature and the discriminant quadratic form, so an odd lattice has no
genus in the session, and two genera have no equality to group by.
`Lattices(ZZ).isometry_classes` must split a family of even and odd cards by
genus before it decides isometry, so it keys each card in private on Sage's
canonical `p`-adic symbols [CS10, Ch. 15, §7.6] together with the signature.
Sage's `GenusSymbol_global_ring.__eq__` compares the local symbols only and
never the signature, and the class has no `__hash__`, so the key is a tuple
of `(p, canonical_symbol)` pairs beside the signature.

**Dependency path:** local integral equivalence classes at every prime and
at the real place -> the genus of an integral lattice, even or odd -> the
genus as the finite set of isometry classes it contains -> grouping a family
by genus.
**Consumers:** `Lattices(ZZ).isometry_classes`; lattice-db duplicate
detection (`latticedb.records.definite_isometry_problems`).
**Coverage boundary:** the owned `genus()` and `Genus` in
`categories/lattices.py` and Sage's `sage/quadratic_forms/genera/genus.py`
were inspected. Repair is the `genera-are-finite-sets-of-isometry-classes`
node in [TODO.md](TODO.md).

### Arithmetic reflection subgroups outside the definite and Vinberg regimes have no exact backend

For a nondegenerate integral lattice `L`, `W(L)` is generated by every
integral reflection. The current tree has exact finite enumeration in the
definite case and a Vinberg chamber algorithm in signature `(1,n)`/`(n,1)`.
For indefinite signature with both inertia indices at least two, roots of an
admissible norm need not form a finite set and no chamber algorithm in the
current engine population certifies that a finite search found every
reflection generator. A bounded search therefore constructs only a subgroup,
not `W(L)`.

There is a second, distinct gap even in the hyperbolic case. For a proper norm
set `S`, `W_S(L)` is generated by all reflections in roots of norms in `S`.
Filtering the simple roots of a Vinberg chamber is not equivalent to this:
other `S`-roots can lie in the full `W(L)`-orbit structure and need not be
simple for the full chamber. Magma and standard Coxeter software construct
reflection subgroups from supplied roots/root data, but the inspected APIs do
not construct this infinite norm-defined root family from the lattice itself.

**Dependency path:** integral root criterion and finite admissible norm set ->
complete root-orbit/reflection-subgroup enumeration -> owned subgroup of
`O(L)`; in the hyperbolic restricted case, a complete norm-defined reflection
subgroup/chamber construction.
**Consumers:** `Lattices.reflection_group(S)`, the Coxeter-system structure of
reflection groups, and later abelianization/growth computations.
**Coverage boundary:** current Sage/OSCAR/Hecke/project reflection machinery and
Magma's documented real-reflection/reflection-subgroup APIs were inspected.
No exact backend was found for either missing construction. Repair requires
the two reflection-engine ruling nodes in [TODO.md](TODO.md).

### A Vinberg invariant is not yet a point of the projective line

The invariant of two mirrors is the point `[4 b(r,s)^2 : q(r) q(s)]` of
`P^1`; for normals of positive square it dehomogenizes to `4 g^2`, where `g`
is the entry of the Gram matrix of the unit normals (Vinberg, *Hyperbolic
reflection groups*, 1985, section 1). An `R`-point of `P^1_R` is a morphism
`Spec R -> P^1_R`. `VinbergInvariantMatrices.vinberg_invariant`
(`categories/vinberg_invariants.py`) asks the owned scheme
`ProjectiveSpaces(R)(1)` to accept the pair `[numerator, denominator]`, and
that scheme has no element constructor: the call raises `AttributeError`
for `_element_constructor_`. So `vinberg_invariant`, `vertex_label`,
`edge_label` and `weighted_graph` fail on every invariant matrix, while
`vinberg_ratio` (the dehomogenized value) works.
**Dependency path:** owned `ProjectiveSpaces(R)(n)` -> its `R`-points as
`Mor(Spec R, P^n_R)` -> the Vinberg invariant -> the labelled graph of
mirrors. `Schemes(R).projective_morphism_from_coordinates` builds such a
morphism from a basepoint-free coordinate family; over `ZZ` the pair
`(4 b^2, q(r) q(s))` need not generate the unit ideal (`(4, 4)` for two
roots of square `-2` with product `1`), so the point is that of the
primitive pair, which exists because `P^1(ZZ) = P^1(QQ)`.
**Consumers:** `VinbergInvariantMatrices.vinberg_invariant`, its graph
labels and `weighted_graph`; the lattice-db graph cards that read them.
**Coverage boundary:** the scheme route was not executed on 2026-10-07:
`Spec ZZ.projective_morphism_from_coordinates` failed earlier, in
`_restriction_to_base`, with `RngMorphism.__init__() got an unexpected
keyword argument 'evaluator'` from the module-morphism construction.
Repair: `vinberg-invariants-are-points-of-the-projective-line` in TODO.

### Products of equal families of sets are different sets

The product \(\prod_{i\in I}X_i\) is determined by the family
\(i\mapsto X_i\): two equal families have one product. `Sets().product`
(`categories/sets/set_categories.py`) interns a finite product by
`_finite_family_key`, the identity of the index set and of each factor
object, and the product objects compare by identity. Finite ordered sets
compare extensionally, so `V = finite_ordered_set((0, 1))` and
`W = finite_ordered_set((0, 1))` satisfy `V == W`, but `V**2 == W**2` is
`False`, and an element of `V**2` is refused by `W**2` with
`ValueError: (0, 0) is an element of Product of the family over {0,...,1},
not of the product Product of the family over {0,...,1}` (observed
2026-10-07).
**Dependency path:** equality of finite sets -> equality of their
products -> extensional equality of functions on a product, as
`IndexedFamily.__eq__` first compares index sets.
**Consumers:** the Coxeter matrix `m: V x V -> Card` of a Coxeter diagram
and of a Vinberg invariant matrix. Two diagrams built separately on the
vertex set `{0, 1}` have unequal Coxeter matrices even with equal entries:
`tests/lattices/test_coxeter.sage`, `test_vinberg_invariants.sage` and
`test_coxeter_subdiagrams.sage` (parallel and divergent mirrors),
`test_coxeter_diagrams_of_root_configurations.sage` (the diagram of
type `B_3`) and `tests/schemes/test_regular_polytope_symmetry.sage` assert
equalities that are true and answer `False`.
Repair: `products-of-equal-families-are-equal` in TODO.

### Coxeter diagrams answer subdiagram orders and drawings as Sage objects

The induced subdiagrams of a Coxeter diagram, ordered by inclusion of
their vertex sets, form a finite partially ordered set, and so do the
`Aut`-orbits of subdiagrams under the order that inclusion induces on orbits. `CoxeterDiagrams`
(`categories/coxeter_diagrams.py`) returns both as Sage `Poset` objects
through `_subdiagram_poset_on` and `_subdiagram_orbit_poset_on`: the six
public methods `subdiagram_poset`, `elliptic_subdiagram_poset`,
`parabolic_subdiagram_poset`, `subdiagram_orbit_poset`,
`elliptic_subdiagram_orbit_poset` and `parabolic_subdiagram_orbit_poset`
put a raw engine object on the public surface (`OWN-03`). The owned
`PartiallyOrderedSets()` (`categories/sets/set_categories.py`) has no
constructor of a finite poset from its underlying set and its order
relation, so no owned object can be returned today. `plot()` returns a
Sage `Graphics`.
The same category still admits engine input: `from_coxeter_matrix`
accepts a Sage `CoxeterMatrix`, `from_cartan_type` a Sage `CartanType`,
and `Groups.Coxeter` (`categories/group/groups.py`) passes any argument
other than the owned Coxeter matrix to Sage's `CoxeterGroup` unchanged
(`OWN-04`). `lexicon/geometry.py` exports Sage's `CoxeterMatrix`.
**Dependency path:** finite posets in `PartiallyOrderedSets()` from
`(X, <=)` -> inclusion of subdiagrams and the order it induces on
`Aut`-orbits -> the public poset methods.
**Partial capability:** the Coxeter matrix is the owned function
`m: V x V -> Card` (`coxeter_matrix()`), and the Coxeter graph and the root
intersection graph are objects of `LabelledGraphs()`.
**Consumers:** the six poset methods, their callers in
`tests/lattices/test_coxeter_subdiagrams.sage`, and the expectation files
under `tests/constructions/` that ask for their cardinalities.
Repair: `coxeter-diagram-orders-are-owned-posets` in TODO.

**Observed 2026-10-07:** `Groups.Coxeter(["A", 2])` and
`Groups.Coxeter(D.coxeter_matrix())` both raise `NotImplementedError`.
`_own_group` places the raised group at construction, and
`_owned_group_category` calls `_is_abelian_witness`, which calls
`is_abelian()` on Sage's `CoxeterMatrixGroup`; Sage's `Group.is_abelian`
raises for that class. Deciding commutativity is a computation done at
construction (`OWN-22`). Repair: `construction-is-instant` in TODO.

### Satake diagrams and real forms have no formalization

A Satake diagram is a Dynkin diagram with black nodes `X` and a diagram
involution `tau`, and it is one exactly when `(X, tau)` is admissible (Kolb,
*Quantum symmetric Kac-Moody pairs*, 2014, Definition 2.3; Araki 1962). The
preamble now presents the category (`categories/satake_diagrams.py`) with
admissibility as its validator, and lattice-db builds its Satake cards as its
objects. A GitHub code search of `dzackgarza/lean-categories` for `Satake`
and `real form` on 2026-10-07 found only the Baily-Borel/Satake
compactification row FC11-C19-U035 and quadratic-form uses of "real form":
neither the diagrams, the admissibility condition, nor real forms of a
semisimple Lie algebra. This host has no local checkout.
**Dependency path:** Cartan matrix of a finite-type root basis -> its
automorphisms `Aut(A, X)` and the longest element `w_X` of a parabolic
subgroup -> admissible pairs -> the real form a Satake diagram presents.
**Consumers:** `SatakeDiagrams.is_admissible`; the lattice-db Satake cards;
the real-form functor of `satake-diagrams-present-real-forms` in TODO.
**Request:** `lean-categories` formalizes admissible pairs from Kolb,
Definition 2.3, and real forms of complex semisimple Lie algebras with Araki's
classification by Satake diagrams. Filed as dzackgarza/lean-categories#86.

### Complex realization acts only on objects, and analytification exists only on affine spaces

For a field `k` of characteristic 0 and an embedding `sigma: k -> CC`, the
complex realization `X -> X(CC)_sigma` is a functor from schemes of finite type
over `k` to topological spaces, and the comparison theorem (Freitag-Kiehl
[FK88] Ch. I Thm 11.6) identifies the l-adic Betti numbers of `X_{kbar}` with
the Betti numbers of `X(CC)_sigma`. `Schemes(k).FiniteType.complex_realization`
(`categories/schemes/schemes.py`) acts on objects only: no morphism `f: X -> Y`
has an image `f(CC)`, so no induced map `H^k(Y(CC); ZZ) -> H^k(X(CC); ZZ)`
exists. Analytification exists only as `AffineSpaces(k).analytification`
(`schemes.py`, `analytic_families.py`), on affine spaces and polynomial maps.
The realization computes integral cohomology for projective space, smooth
complete toric varieties and smooth projective complete intersections only, and
the embedding `sigma` is constructed only for `k = QQ`.

**Dependency path:** analytification of a scheme of finite type -> its action on
morphisms -> complex realization as a functor -> induced maps on singular
cohomology; separately, the embeddings of a number field into `CC`.
**Consumers:** `Schemes(k).FiniteType.betti_number` and `euler_characteristic`
on schemes that are neither toric nor complete intersections, including the
branched double covers of `P^1 x P^1` in
`tests/schemes/test_horikawa_k3_family.sage` and
`tests/schemes/test_horikawa_enriques_family.sage` (`chi = 24`); every
pullback on cohomology.
**Coverage boundary:** the realization owner in `geometric_cohomology.py`, the
analytification owner in `analytic_families.py` and the scheme categories in
`schemes.py` were inspected. Repair is the `complex-realization-is-a-functor`
node in [TODO.md](TODO.md).

### The Hodge structure of a smooth complete intersection is present only for the quartic surface

A smooth complete intersection `X` of multidegree `(d_1, ..., d_r)` in `P^n`
over a field of characteristic 0 has Hodge numbers determined by `n` and the
`d_i`; outside the middle degree they are those of projective space. The tree's
`ProjectiveCompleteIntersections(k).hodge_structure()`
(`categories/schemes/complete_intersections.py`) builds `_QuarticK3HodgeData`
only, so every other multidegree has no Hodge numbers.

**Dependency path:** smooth projective complete intersection -> Lefschetz
hyperplane theorem outside the middle degree -> generating function of the
middle-degree Hodge numbers -> `hodge_number(p, q)`.
**Consumers:** `Schemes(k).Proper().Smooth().hodge_number` on complete
intersections; the `hodge_poincare` series stored on lattice-database
geometric cards.
**Coverage boundary:** the Zotero library was searched for a source stating the
general formula. The item labelled SGA 7 II (`CMV4MC6A`, LNM 340) holds an
extraction of SGA 7 I; the item labelled SGA 4 volume 305 (`ZXUPYTKS`) holds
tome 1, Exposés I to IV; SGA 4½ (`HRUVM374`) holds a table of contents only;
Hirzebruch, *Topological Methods in Algebraic Geometry*, is absent. Dimca
[Dim92] (B34) states the Steenbrink formula for quasismooth weighted
hypersurfaces only. Repair is the `complete-intersection-hodge-sources` and
`complete-intersection-hodge-structure` nodes in [TODO.md](TODO.md).

### Geometric lattice-database cards store no Betti numbers

Of the 37 cards in `lattice-database/geometric-objects/`, only
`k3-surface.md` stores `betti_numbers`. The others store a Hodge series, a
linked cohomology lattice or neither, so no card-level Betti number or Euler
characteristic exists to compare with `Schemes(k).FiniteType.betti_number`.

**Dependency path:** a cited source or a constructed preamble object ->
`b_k` and `chi` on the card.
**Consumers:** the lattice-database geometric-object pages and every
comparison of a card with the preamble's realization.
**Coverage boundary:** the frontmatter of every card under
`lattice-database/geometric-objects/` was read. Repair is the
`geometric-cards-store-betti-numbers` node in [TODO.md](TODO.md).

## Workflow Papercuts

### Finite cyclic subgroup membership is decided by enumerating powers

`CyclicGroups.__contains__` in
`categories/group/cyclic_subgroups.py` currently answers membership in a
finite cyclic subgroup by constructing `_finite_elements()` and comparing the
candidate against every power of the selected generator. Membership in the
represented subgroup is a group-engine question when the ambient realization
supports subgroup membership; enumeration is a separate chosen presentation
of the finite set and should not be the decision procedure.

**Dependency path:** selected cyclic generator -> represented subgroup in the
ambient group engine -> engine membership decision -> owned subgroup
membership. Infinite cyclic membership retains its explicit discrete-log
computability boundary when no maintained route applies.
**Consumer:** `CyclicGroups.__contains__`; iteration may continue to enumerate
finite cyclic groups, but membership must not depend on that enumeration.
**Repair:** `engine-wiring-audit` in [TODO.md](TODO.md).

### Zettlr all-workspace lint conflates component `id=` properties with Pandoc `#` identifiers

Running the Zettlr linter across the configured writing and site workspaces
should lint valid component attribute blocks without aborting.  The site
component contract uses key-value attributes such as
`{.component type="video" provider="youtube" id="E_Ly2NWX1g8"}`; the same
form is used by multiple site documents.

Observed on 2026-09-29: all-workspace lint aborts with
`Inconsistent attribute block: id "E_Ly2NWX1g8" not found ...`.
`extract-references.ts::locateAttribute` in the Zettlr/Pandoc integration
calls `parsePandocAttributes`, sees `attributes.id`, and then requires that
value to occur as an authored `#<id>` token.  A component's ordinary
key-value `id=...` property therefore reaches the identifier-token branch and
throws even though the authored attribute block is valid for the component
renderer.  Linting the `/research/writing` workspace alone is clean through
warning severity; adding the site workspace exposes the failure.

**Expected behavior:** a generic key-value `id=...` property remains component
data and is not treated as a Pandoc reference identifier unless an authored
`#...` identifier token is present.  Explicit `#...` reference identifiers
must continue to be located with their exact source range.
**Owning boundary:** Zettlr/Pandoc attribute parsing and reference extraction,
not the research documents or the site component syntax.
**Examples:** the Benson Farb video block above, together with established site
video blocks using `id="3IjAy0gHRyY"` and `id="zRPa-VAvl6Q"`.
**Coverage boundary:** the concrete all-workspace failure, the identifier
locator source, and these three site video-component uses were inspected.  No
claim is made about other key-value `id=` consumers.

### Flowmark Unicode-math lint scans inert comments and literal code

Running Flowmark's `math/unicode-symbol` rule on authored Markdown should
inspect mathematical prose, not text Pandoc treats as inert or literal.  The
rule currently reports Unicode-math warnings inside both HTML comments and
inline code spans.

Observed on 2026-09-29 with minimal stdin specimens: a comment containing
`F\u2082d` and `\u0393\u2082d` reports warnings for those Unicode math code
points, while an inline code span containing `AltBil\u2286SkewBil` and
`\u03b3` reports the same rule.  The same first
failure accounts for the remaining `math/unicode-symbol` diagnostics in
commented archival notes in
`writing/dissertation/sections/1-part-combinatorial/3-chapter-enriques-k3/450-scattone.md`
and
`writing/dissertation/sections/3-part-main-theorem/6-chapter/600-finite-coarsening.md`;
the inline-code failure appears in literal bad/good authoring examples in
`writing/CONTRIBUTING.md`.

**Expected behavior:** HTML comments and code spans are excluded from
`math/unicode-symbol`; Unicode mathematical notation in rendered prose remains
diagnosed.
**Owning boundary:** Flowmark's Markdown token scoping for the
`math/unicode-symbol` rule, not the dissertation comments or literal examples.
**Coverage boundary:** the two minimal stdin specimens and the current
repository occurrences above were reproduced.  No claim is made about other
math lint rules or other Markdown literal-node kinds.

### Source category-graph slices collapse parameterized fibres into self-edges

The source-only category graph is an inspection tool for the M1 placement
audit, so selecting a category must remain usable while execution is suspended.
On 2026-09-29,
`just category-graph slice --select PermutationGroups --direction up` aborted
before producing the requested slice with
`Self-declarations cannot define a strict category order:
['DistinguishedAffineCovers']`.

The triggering declaration is
`DistinguishedAffineCovers(X).super_categories()`, whose parameterized fibre
lists the unparameterized catalogue `DistinguishedAffineCovers()` together
with `CoveringFamilies(AffSch_R/X)`.  The source graph records category classes
but not this parameter distinction, so the fibre-to-catalogue inclusion is
collapsed to an apparent class self-edge and blocks inspection of unrelated
categories.

**Expected behavior:** a source slice for an unrelated category does not abort
because a parameterized category and its catalogue share one implementation
class.  The graph either represents their parameters sufficiently to retain
the strict relation or records that relation outside its class-level strict
poset.
**Owning boundary:** `dzack_research.utilities.category_graph`'s source model of
parameterized category declarations, not the `PermutationGroups` placement
pass and not, by this observation alone, the mathematics of distinguished
affine covers.
**Coverage boundary:** the failing slice command and the declaration at
`categories/schemes/ringed_spaces.py::DistinguishedAffineCovers.super_categories`
were inspected.  No claim is made here about other same-class parameterized
relations.

### Module-subobject joins and meets do not transport canonical ideal structure

The placement audit found that `CommutativeIdeals(R)` is a strict subcategory
of `ModuleSubobjects(R)`, but it reimplements both `sum` and `intersection`
with raw ideal-engine operations.  Mathematically these are the same join and
meet of the two submodules of the regular module `R`: the sum of ideals is the
module sum and the intersection of ideals is the module-subobject pullback.

The general owner already implements both constructions in
`categories/modules/pure/modules.py::ModuleSubobjects.ParentMethods`, but its
results are constructed only as module subobjects.  Simply deleting the ideal
overrides would therefore discard the canonical fact that the result is again
an ideal, together with the selected ideal-generator/engine data required by
the current `CommutativeIdeals` representation.  The ideal overrides in
`categories/rings/commutative_ideals.py` preserve that structure only by
maintaining a second computation path.

**Expected behavior:** the module-subobject sum/meet construction has one
authority and transports any structural category whose closure under the
selected construction is part of its declared contract.  In particular,
intersections and sums of commutative ideals return `CommutativeIdeals(R)`
without a second public `sum`/`intersection` implementation at the ideal leaf.
**Dependency path:** selected module subobjects and their inclusions -> general
subobject join/pullback -> structure-preservation datum for commutative ideals
-> one result carrying both `ModuleSubobjects(R)` and `CommutativeIdeals(R)`.
**Consumers:** `CommutativeIdeals.sum`, `CommutativeIdeals.intersection`, and
all callers that subsequently require ideal operations on those results.
**Coverage boundary:** the live module-subobject implementations at
`modules/pure/modules.py` and the two ideal implementations at
`rings/commutative_ideals.py` were inspected during `placement-audit`.  No
claim is made here about preservation of arbitrary additional subobject
categories; each such closure law requires its own mathematical justification.

### Toric scalar base change drops the toric construction data

Scalar base change of a toric scheme should retain the fan that defines the
toric variety.  On 2026-09-29 the construction-chain review for projective
surface method placement found that `_SchemeBaseChangeFunctor._apply_object`
routes every scheme presented by a finite affine gluing through
`_glued_object` before inspecting any toric specialization.  `ToricSchemes`
are built by exactly such a gluing.  `_glued_object` then reconstructs only a
generic glued scheme in `FiberProductSchemes(R')`; it does not retain
`ToricSchemes(R')`, the fan, or the optional polarizing polytope.

**Expected behavior:** for a scalar map `R -> R'`, the base change of
`X_Sigma` remains the toric scheme `X_Sigma` over `R'`, carrying the same fan
and any selected polarization together with the fibre-product projections.
Properties determined by the fan, such as smoothness and (for complete toric
surfaces over a field) projective-surface placement, are then inherited from
that same retained datum rather than re-guessed after gluing.
**Dependency path:** `ToricSchemes(R)` and its defining fan -> affine-atlas
gluing -> scheme scalar base change -> fibre-product gluing over `R'` ->
retained toric construction data and category placement.
**Owning boundary:** the scheme base-change constructor together with the
toric-scheme constructor, not the individual toric operations that disappear
after the base change.
**Coverage boundary:** `_SchemeBaseChangeFunctor._apply_object` and
`_glued_object`, and the toric construction in `_toric_variety`, were inspected
as source.  No runtime execution was performed under the current M1 execution
suspension, and no claim is made here about other specialized affine-gluing
families that may also need structure-preserving base change.

Add concrete observed workflow friction here under a descriptive heading, with the user action, expected behavior, actual result, owning boundary and example.
Use `DEV-59` for capture and resolution.
Foundational mathematical gaps belong above even when first noticed as an inconvenient method or notebook interaction.
