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

### The quotient of a group by a non-normal subgroup has no owned coset construction

For a subgroup \(H\le G\) the left cosets \(G/H\) form a transitive
\(G\)-set pointed at \(H\), with the projection \(G\to G/H\); it is a group,
and the projection a group morphism, exactly when \(H\) is normal. A group
morphism \(f\colon G\to G'\) then has the exact sequence of pointed sets
\(1\to\ker f\to G\to G'\to G'/f(G)\to *\), which is an exact sequence of
groups only when \(f(G)\) is normal. The discriminant reduction sequence
\(1\to\tilde O(L)\to O(L)\to O(A_L)\to C_L\to 1\) is the consumer: its
cokernel \(C_L=O(A_L)/f(O(L))\) is this coset set.

Observed in source: `SubgroupInclusion.cokernel()` and `GroupMorphism.cokernel()`
(`categories/group/groups.py`) quotient by the normal closure of the image,
the categorical cokernel in groups, and `left_cosets` returns the engine's
cosets as a tuple (`_engine_cosets`), not an object of `FiniteGSets(G)` with
its projection. `DiscriminantReductionSequence.cokernel_projection`
(`categories/lattices.py`) therefore asserts that \(f(O(L))\) is normal.
Specimen, derived and not executed: for \(L=A_2\oplus A_2\oplus E_6\),
\(A_L\cong(\mathbb Z/3)^3\) with a nondegenerate form, so
\(O(q_L)\cong O_3(\mathbb F_3)\cong C_2\times S_4\) of order 48; \(O(L)\)
maps onto \(\{\pm1\}^3\rtimes\langle(12)\rangle\), a Sylow 2-subgroup of order
16, which is not normal. \(C_L\) has three points, while the normal-closure
quotient is trivial.

**Dependency path:** finite \(G\)-sets (`FiniteGSets(G)`) -> the coset
\(G\)-set \(G/H\) with its projection -> exact sequences of pointed sets ->
the discriminant reduction cokernel.
**Consumers:** `Lattices.discriminant_reduction_sequence`; counting
overlattices and primitive embeddings through double cosets of \(O(A_L)\).
**Coverage boundary:** the group cokernels and coset listing in `groups.py`
were read; `g_sets.py` was searched for a coset construction and none was
found. Repair: `coset-spaces-of-finite-groups` in [TODO.md](TODO.md).

### The image of the spinor norm of an anisotropic binary or unary space is not computed

The cokernel \(C_{\mathrm{sn}_K}=(K^\times/(K^\times)^2)/\mathrm{sn}_K(O(V))\)
of the spinor norm of a quadratic space \(V\) over \(K=\mathbb Q\) needs the
image. It is generated by the spinor norms of rotations and the classes
\([c\,(v,v)]\) of reflections (O'Meara, *Introduction to Quadratic Forms*,
§55). When \(V\) is isotropic, or has dimension at least 3, the rotations
give all of \(K^\times\) or its positive classes (O'Meara 55:2a, 101:8), and
`SpinorNormSequence.cokernel_projection` (`categories/lattices.py`) answers
from those theorems. For an anisotropic \(V\) of dimension 1 or 2 the image
is the subgroup generated by products of values of \(V\) (O'Meara 55:2),
the cokernel is an infinite quotient of \(\mathbb Q^\times/(\mathbb Q^\times)^2\),
and the square-class group has no owned quotient by a subgroup given by
generators or by a decidable predicate. The same method asserts there.
Specimen, derived and not executed: for \(V=\langle 6\rangle\),
\(\mathrm{sn}_{\mathbb Q}(O(V))=\{[1],[-3]\}\) and \(C\) is
\(\mathbb Q^\times/(\mathbb Q^\times)^2\) modulo \([-3]\).

**Dependency path:** quotients of abelian groups by subgroups with a
membership decision -> the square-class group -> the value set \(Q(V)\) of a
binary space, decided by Hasse--Minkowski (Hecke's `represents` on isometry
classes) -> \(C_{\mathrm{sn}_K}\).
**Consumers:** `SpinorNormSequence.cokernel` for lattices of rank one or two
with anisotropic rational space, such as \(A_2\).
**Coverage boundary:** the owned group quotients in `groups.py` (GAP, finite
groups only) were read. Repair: `spinor-norm-images` in [TODO.md](TODO.md).

### The spinor norm and Witt index are computed only over the rationals

\(\mathrm{sn}_K\) and the Witt index are defined for a quadratic space over
any field of characteristic not 2, and a lattice over an order \(R\) of a
number field \(K\) asks for them over \(K\). The adapters
(`categories/lattice_engines.py`) call OSCAR's `rational_spinor_norm`, which
takes quadratic spaces over \(\mathbb Q\), and Hecke's isometry classes of
rational spaces. OSCAR's exported `witt_index` takes a `SesquilinearForm` or
`QuadraticForm` of its matrix-group code and calls GAP's `WittIndex`
(`Oscar/src/Groups/matrices/forms.jl`); it has no method for a Hecke
`QuadSpace`. Unresolved capability question: `Oscar.spin`, the
reflection factorization behind `rational_spinor_norm`, is written for a
diagonal Gram matrix over any field, and Hecke's `QuadSpaceCls` covers number
fields; whether the bridge carries number-field matrices has not been
checked.

**Dependency path:** quadratic spaces over number fields -> their isometry
classes and reflection factorizations -> \(\mathrm{sn}_K\), the Witt index.
**Consumers:** `Lattices.spinor_norm`, `spinor_norm_sequence`, `witt_index`
for lattices over rings of integers. Repair: `orthogonal-reduction-sequences`
in [TODO.md](TODO.md).

### Scalar extension of an infinite-rank lattice is not a lattice

\(L\otimes_R S\) along \(R\to S\) is a free \(S\)-module with the
\(S\)-bilinear extension of the form, an object of `Lattices(S)` at every
rank. `Lattices.base_change` (`categories/lattices.py`) builds it from the
Gram matrix, so it asserts finite rank; an infinite-rank lattice's Gram is a
pairing rule (`_PairingGram` in `categories/_lattice.py`), and no rule
transports a pairing along a ring map. The formed-module base change
(`_formed_module_base_change`) handles pairing rules but lands in
`FormModules(S)`, outside `Lattices(S)`.

**Dependency path:** pairing-rule Gram tensors -> their image along a ring
map -> `Lattices(S)` on that rule.
**Consumers:** `vector_space`, `spinor_norm`, `witt_index` of infinite-rank
lattices; none observed in the tree. Repair:
`infinite-rank-lattice-base-change` in [TODO.md](TODO.md).

## Workflow Papercuts

Add concrete observed workflow friction here under a descriptive heading, with the user action, expected behavior, actual result, owning boundary and example.
Use `DEV-59` for capture and resolution.
Foundational mathematical gaps belong above even when first noticed as an inconvenient method or notebook interaction.
