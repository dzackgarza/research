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

The Vinberg invariant of two mirrors is the point
`[4 b(r,s)^2 : q(r) q(s)]` of `P^1`, and an `R`-point of `P^1_R` is a
morphism `Spec R -> P^1_R` (Vinberg, *Hyperbolic reflection groups*, 1985,
section 1). `VinbergInvariantMatrices.vinberg_invariant`
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

### Satake diagrams and real forms have no formalization

A Satake diagram is a Dynkin diagram with black nodes `X` and a diagram
involution `tau`, and it is one exactly when `(X, tau)` is admissible (Kolb,
*Quantum symmetric Kac-Moody pairs*, 2014, Definition 2.3; Araki 1962). The
preamble now presents the category (`categories/satake_diagrams.py`) with
admissibility as its validator, and lattice-db builds its Satake cards as its
objects. `rg -i 'satake|araki'` over `~/gitclones/lean-categories` found
neither the diagrams, the admissibility condition, nor real forms of a
semisimple Lie algebra on 2026-10-07.
**Dependency path:** Cartan matrix of a finite-type root basis -> its
automorphisms `Aut(A, X)` and the longest element `w_X` of a parabolic
subgroup -> admissible pairs -> the real form a Satake diagram presents.
**Consumers:** `SatakeDiagrams.is_admissible`; the lattice-db Satake cards;
the real-form functor of `satake-diagrams-present-real-forms` in TODO.
**Request:** `lean-categories` formalizes admissible pairs from Kolb,
Definition 2.3, and real forms of complex semisimple Lie algebras with Araki's
classification by Satake diagrams.

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

Add concrete observed workflow friction here under a descriptive heading, with the user action, expected behavior, actual result, owning boundary and example.
Use `DEV-59` for capture and resolution.
Foundational mathematical gaps belong above even when first noticed as an inconvenient method or notebook interaction.
