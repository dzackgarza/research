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

### Matrix endomorphism objects over a noncommutative base have no declared morphism owner

For a finite free module whose represented endomorphisms form a matrix ring,
the endomorphism object has ring multiplication by composition.  When the
selected coefficient ring `R` is commutative, the same object is an
associative unital `R`-algebra and algebra morphisms give the corresponding
fixed-Mor theory.  For noncommutative `R`, that `R`-algebra structure is not
available merely from the endomorphism-ring construction; the category must
instead state the morphisms preserving the structures it actually declares.

Observed during `placement-audit` on 2026-09-28:
`MatrixEndomorphismSpaces(R)` unconditionally selected
`AssociativeAlgebraMorCategoryConstruction`, while its former
`super_categories()` also unconditionally selected
`AdditiveEndomorphismRings(R)`.  The latter category explicitly requires
`R in OwnedRings().Commutative()` and asserts otherwise.  The current source
repair makes the object graph conditional: over a commutative base it retains
the additive-endomorphism algebra owner, while over a noncommutative base it
uses `OwnedRings()` for the multiplicative structure.  The fixed Mor owner is
still unconditional.  Source search found separate ring, module and
associative-algebra Mor constructions, but no declared fixed-Mor construction
for this noncommutative-base matrix-endomorphism intersection.  This is source
evidence; execution remains deferred by `DEV-58`.

**Dependency path:** finite free module -> represented matrix endomorphism
object -> composition ring -> intersection with the represented matrix/module
structure -> fixed Mor preserving that declared structure.
**Consumers:** `MatrixEndomorphismSpaces(R)`, matrix-ring category membership,
and any functor or construction asking for morphisms between such objects over
a noncommutative `R`.
**Coverage boundary:** the matrix-endomorphism declaration and the repository's
ring, module and associative-algebra Mor constructors were inspected.  No
claim is made that a more general structured-Mor intersection mechanism is
absent outside those searched owners.  The finding arose inside
`placement-audit`; no separate repair node is currently selected.

## Workflow Papercuts

Add concrete observed workflow friction here under a descriptive heading, with the user action, expected behavior, actual result, owning boundary and example.
Use `DEV-59` for capture and resolution.
Foundational mathematical gaps belong above even when first noticed as an inconvenient method or notebook interaction.
