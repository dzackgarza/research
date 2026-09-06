# The preamble, surveyed from a live session

This is the reference for what a session can build on: which categories
exist, what sits above and below each one, which operations an object of
each category answers to and where each operation is defined, which
functors move between categories, and which named specimens are on hand.

Everything here was read from a running session, not from the source text.
`super_categories` is a method, the base ring is an argument, and the
operations an object carries are assembled by Sage from the category graph
at runtime -- so a category's place and its methods are facts only a live
object can report.

```python
from dzack_research.preamble.all import *
```

## How to read an entry

A category parameterized by a ring is written `C(R)` and was probed at
`R = ZZ`; the relations hold for the parameter generally, and the
**probed as** line shows the object the survey actually held.

**Above** and **below** are the direct edges of the poset: `super_categories`
and its inverse. **Refines** is the transitive closure upward.

**Operations introduced here** are the ones this category *defines*.  Every
operation is written out once, at the category that owns it; a descendant
lists it under **inherited** with a link, because that is where placement
lives.  So an object of `C` answers to the union of the operations
introduced by `C` and by everything in its ancestry.

Operations are split by what they act on: **objects** of the category,
**elements** of those objects, and **morphisms** between them.

A category the survey could not build, or an operation whose signature
would not resolve, is recorded with the error rather than dropped.

The same survey is serialized to `docs/preamble-graph.json`, which carries
every operation name, so a question this prose cannot index is a `jq` away:

```bash
# which category owns discriminant_group?
jq -r '.categories | to_entries[]
      | select(.value.operations.objects[]?.name == "discriminant_group")
      | .key' docs/preamble-graph.json
```

The poset is drawn in `docs/preamble-graph.html` (pan and zoom), from
`docs/preamble-graph.dot`.

| | |
| :--- | ---: |
| categories in the poset | 278 |
| of those, built and interrogated | 196 |
| operations, each written once at its owner | 1125 |
| functors | 69, 11 of them with a domain and codomain resolved here |
| adjunctions | 21 |

## The category poset

An edge points from a category to a category it refines.  In the drawing the
arrow runs leftward and the chapters are boxed, so reading left is forgetting
structure and reading right is adding it; a dashed node is a category Sage
provides rather than one the preamble owns.

The top of the poset, refining nothing further: [`Objects`](#cat-objects).

The whole graph at once is [`preamble-graph.html`](preamble-graph.html); the diagrams below are its restriction to one chapter, together with any immediate supercategory that lies outside it.

## Getting from one category to another

Every functor the survey could build, indexed by where it starts.  This is
the table to read when the object you have and the object you want are in
different categories.

| from | functor | to |
| :--- | :--- | :--- |
| Category of abelian groups | [`AbelianGroupInclusionFunctor`](#fun-abeliangroupinclusionfunctor) | Category of groups |
| Category of discrete categories | [`ObjectSetFunctor`](#fun-objectsetfunctor) | Category of sets |
| Category of groups | [`AbelianizationFunctor`](#fun-abelianizationfunctor) | Category of abelian groups |
| Category of groups | [`GroupUnderlyingSetFunctor`](#fun-groupunderlyingsetfunctor) | Category of sets |
| Category of number fields | [`RingOfIntegersFunctor`](#fun-ringofintegersfunctor) | Category of owned orders |
| Category of owned orders | [`FractionFieldFunctor`](#fun-fractionfieldfunctor) | Category of number fields |
| Category of sets | [`FinitePowerSetFunctor`](#fun-finitepowersetfunctor) | Category of sets |
| Category of sets | [`FreeGroupFunctor`](#fun-freegroupfunctor) | Category of groups |
| Core of Category of sets | [`CardinalityFunctor`](#fun-cardinalityfunctor) | Category of cardinalities |
| Opposite of Category of sets | [`InverseImagePowerSetFunctor`](#fun-inverseimagepowersetfunctor) | Category of sets |
| Product of Opposite of Category of sets and Category of sets | [`ExponentialFunctor`](#fun-exponentialfunctor) | Category of sets |

### Adjunctions

| adjunction | left adjoint | | right adjoint |
| :--- | :--- | :---: | :--- |
| [`AbelianizationAdjunction`](#fun-abelianizationadjunction) | Abelianization functor | ⊣ | Inclusion of abelian groups into groups |
| [`FreeGroupUnderlyingSetAdjunction`](#fun-freegroupunderlyingsetadjunction) | Free-group functor | ⊣ | Underlying-set functor on groups |
| [`OrderNumberFieldAdjunction`](#fun-ordernumberfieldadjunction) | Fraction-field functor | ⊣ | Ring-of-integers functor |

76 further functors take data the survey does not choose for you (a ring map, a group, a subgroup pair); they are written out in their chapters with the arguments they want.

## Named specimens

Objects the catalogue has already built, with the invariants the survey could compute from them.

### `Embeddings` {#embeddings}

`src/dzack_research/preamble/catalogue.py:918`

| name | is | domain | codomain | category |
| :--- | :--- | :--- | :--- | :--- |
| `Embeddings.E8_2_into_TdP` | Generic morphism:
  From: Integral lattice of rank 8 and signature (0, 8)
  To:   Integral lattice of rank 20 and signature (2, 18) | Integral lattice of rank 8 and signature (0, 8) | Integral lattice of rank 20 and signature (2, 18) | Category of homsets of sets |
| `Embeddings.TCo_into_TEn` | Generic morphism:
  From: Integral lattice of rank 11 and signature (2, 9)
  To:   Integral lattice of rank 12 and signature (2, 10) | Integral lattice of rank 11 and signature (2, 9) | Integral lattice of rank 12 and signature (2, 10) | Category of homsets of sets |
| `Embeddings.TEn_into_TdP` | Generic morphism:
  From: Integral lattice of rank 12 and signature (2, 10)
  To:   Integral lattice of rank 20 and signature (2, 18) | Integral lattice of rank 12 and signature (2, 10) | Integral lattice of rank 20 and signature (2, 18) | Category of homsets of sets |
| `Embeddings.TdP_into_LK3` | Generic morphism:
  From: Integral lattice of rank 20 and signature (2, 18)
  To:   Integral lattice of rank 22 and signature (3, 19) | Integral lattice of rank 20 and signature (2, 18) | Integral lattice of rank 22 and signature (3, 19) | Category of homsets of sets |
| `Embeddings.TEn_into_LK3` | Generic morphism:
  From: Integral lattice of rank 12 and signature (2, 10)
  To:   Integral lattice of rank 22 and signature (3, 19) | Integral lattice of rank 12 and signature (2, 10) | Integral lattice of rank 22 and signature (3, 19) | Category of homsets of sets |
| `Embeddings.U_E8_2_into_TEn` | Generic morphism:
  From: Integral lattice of rank 10 and signature (1, 9)
  To:   Integral lattice of rank 12 and signature (2, 10) | Integral lattice of rank 10 and signature (1, 9) | Integral lattice of rank 12 and signature (2, 10) | Category of homsets of sets |

### `Involutions` {#involutions}

Named involutions of the K3 lattice in its displayed block framing.

`src/dzack_research/preamble/catalogue.py:889`

| name | is | domain | codomain | category |
| :--- | :--- | :--- | :--- | :--- |
| `Involutions.I_dP` | Generic endomorphism of Integral lattice of rank 22 and signature (3, 19) | Integral lattice of rank 22 and signature (3, 19) | Integral lattice of rank 22 and signature (3, 19) | Join of Category of groups and Category of endsets and Category of homsets of sets |
| `Involutions.I_En` | Generic endomorphism of Integral lattice of rank 22 and signature (3, 19) | Integral lattice of rank 22 and signature (3, 19) | Integral lattice of rank 22 and signature (3, 19) | Join of Category of groups and Category of endsets and Category of homsets of sets |
| `Involutions.I_Nik` | Generic endomorphism of Integral lattice of rank 22 and signature (3, 19) | Integral lattice of rank 22 and signature (3, 19) | Integral lattice of rank 22 and signature (3, 19) | Join of Category of groups and Category of endsets and Category of homsets of sets |

### `NamedLattices` {#namedlattices}

`src/dzack_research/preamble/catalogue.py:74`

| name | is | rank | signature_pair | discriminant | category |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `NamedLattices.Zero` | Integral lattice of rank 0 and signature (0, 0) | 0 | (0, 0) | 1 | Join of Category of even lattices and Category of nondegenerate lattices and Category of finite-rank lattices |
| `NamedLattices.Z` | Integral lattice of rank 1 and signature (1, 0) | 1 | (1, 0) | 1 | Join of Category of nondegenerate lattices and Category of finite-rank lattices |
| `NamedLattices.Z_2` | Integral lattice of rank 1 and signature (1, 0) | 1 | (1, 0) | 2 | Join of Category of even lattices and Category of nondegenerate lattices and Category of finite-rank lattices |
| `NamedLattices.U` | Integral lattice of rank 2 and signature (1, 1) | 2 | (1, 1) | 1 | Join of Category of even lattices and Category of nondegenerate lattices and Category of finite-rank lattices |
| `NamedLattices.H` | Integral lattice of rank 2 and signature (1, 1) | 2 | (1, 1) | 1 | Join of Category of even lattices and Category of nondegenerate lattices and Category of finite-rank lattices |
| `NamedLattices.U_2` | Integral lattice of rank 2 and signature (1, 1) | 2 | (1, 1) | 4 | Join of Category of even lattices and Category of nondegenerate lattices and Category of finite-rank lattices |
| `NamedLattices.H_2` | Integral lattice of rank 2 and signature (1, 1) | 2 | (1, 1) | 4 | Join of Category of even lattices and Category of nondegenerate lattices and Category of finite-rank lattices |
| `NamedLattices.E8` | Integral lattice of rank 8 and signature (0, 8) | 8 | (0, 8) | 1 | Category of root lattices |
| `NamedLattices.E8_2` | Integral lattice of rank 8 and signature (0, 8) | 8 | (0, 8) | 256 | Join of Category of even lattices and Category of nondegenerate lattices and Category of finite-rank lattices |
| `NamedLattices.E10` | Integral lattice of rank 10 and signature (1, 9) | 10 | (1, 9) | 1 | Join of Category of even lattices and Category of nondegenerate lattices and Category of finite-rank lattices and Category of direct sum objects |
| `NamedLattices.E10_2` | Integral lattice of rank 10 and signature (1, 9) | 10 | (1, 9) | 1024 | Join of Category of even lattices and Category of nondegenerate lattices and Category of finite-rank lattices and Category of direct sum objects |
| `NamedLattices.Sdp` | Integral lattice of rank 2 and signature (1, 1) | 2 | (1, 1) | 4 | Join of Category of even lattices and Category of nondegenerate lattices and Category of finite-rank lattices |
| `NamedLattices.SEn` | Integral lattice of rank 10 and signature (1, 9) | 10 | (1, 9) | 1024 | Join of Category of even lattices and Category of nondegenerate lattices and Category of finite-rank lattices and Category of direct sum objects |
| `NamedLattices.Tco` | Integral lattice of rank 11 and signature (2, 9) | 11 | (2, 9) | 2048 | Join of Category of even lattices and Category of nondegenerate lattices and Category of finite-rank lattices |
| `NamedLattices.Sco` | Integral lattice of rank 11 and signature (1, 10) | 11 | (1, 10) | -2048 | Join of Category of even lattices and Category of nondegenerate lattices and Category of finite-rank lattices |
| `NamedLattices.TEn` | Integral lattice of rank 12 and signature (2, 10) | 12 | (2, 10) | 1024 | Join of Category of even lattices and Category of nondegenerate lattices and Category of finite-rank lattices |
| `NamedLattices.TdP` | Integral lattice of rank 20 and signature (2, 18) | 20 | (2, 18) | 4 | Join of Category of even lattices and Category of nondegenerate lattices and Category of finite-rank lattices |
| `NamedLattices.L_20_2_0` | Integral lattice of rank 20 and signature (2, 18) | 20 | (2, 18) | 4 | Join of Category of even lattices and Category of nondegenerate lattices and Category of finite-rank lattices |
| `NamedLattices.LK3` | Integral lattice of rank 22 and signature (3, 19) | 22 | (3, 19) | 1 | Join of Category of even lattices and Category of nondegenerate lattices and Category of finite-rank lattices |
| `NamedLattices.LK3_2` | Integral lattice of rank 21 and signature (2, 19) | 21 | (2, 19) | -2 | Join of Category of even lattices and Category of nondegenerate lattices and Category of finite-rank lattices |
| `NamedLattices.LK3_4` | Integral lattice of rank 21 and signature (2, 19) | 21 | (2, 19) | -4 | Join of Category of even lattices and Category of nondegenerate lattices and Category of finite-rank lattices |
| `NamedLattices.LpNik` | Integral lattice of rank 14 and signature (3, 11) | 14 | (3, 11) | 256 | Join of Category of even lattices and Category of nondegenerate lattices and Category of finite-rank lattices |
| `NamedLattices.LmNik` | Integral lattice of rank 8 and signature (0, 8) | 8 | (0, 8) | 256 | Join of Category of even lattices and Category of nondegenerate lattices and Category of finite-rank lattices |
| `NamedLattices.Mukai` | Integral lattice of rank 24 and signature (4, 20) | 24 | (4, 20) | 1 | Join of Category of even lattices and Category of nondegenerate lattices and Category of finite-rank lattices |
| `NamedLattices.MukaiExtended` | Integral lattice of rank 26 and signature (5, 21) | 26 | (5, 21) | 1 | Join of Category of even lattices and Category of nondegenerate lattices and Category of finite-rank lattices |
| `NamedLattices.MukaiAbelian` | Integral lattice of rank 8 and signature (4, 4) | 8 | (4, 4) | 1 | Join of Category of even lattices and Category of nondegenerate lattices and Category of finite-rank lattices |
| `NamedLattices.MukaiAbelianExtended` | Integral lattice of rank 10 and signature (5, 5) | 10 | (5, 5) | 1 | Join of Category of even lattices and Category of nondegenerate lattices and Category of finite-rank lattices |
| `NamedLattices.U_E8_2` | Integral lattice of rank 10 and signature (1, 9) | 10 | (1, 9) | 256 | Join of Category of even lattices and Category of nondegenerate lattices and Category of finite-rank lattices and Category of direct sum objects |
| `NamedLattices.BogachevKolpakovNonReflective` | Integral lattice of rank 3 and signature (1, 2) | 3 | (1, 2) | -2401 | Join of Category of nondegenerate lattices and Category of finite-rank lattices |
| `NamedLattices.BogachevKolpakovWithoutRoots` | Integral lattice of rank 3 and signature (1, 2) | 3 | (1, 2) | -117649 | Join of Category of nondegenerate lattices and Category of finite-rank lattices |
| `NamedLattices.A1` | Integral lattice of rank 1 and signature (0, 1) | 1 | (0, 1) | -2 | Category of root lattices |
| `NamedLattices.D4` | Integral lattice of rank 4 and signature (0, 4) | 4 | (0, 4) | 4 | Category of root lattices |
| `NamedLattices.D6` | Integral lattice of rank 6 and signature (0, 6) | 6 | (0, 6) | -4 | Category of root lattices |
| `NamedLattices.D8` | Integral lattice of rank 8 and signature (0, 8) | 8 | (0, 8) | 4 | Category of root lattices |
| `NamedLattices.E7` | Integral lattice of rank 7 and signature (0, 7) | 7 | (0, 7) | 2 | Category of root lattices |
| `NamedLattices.Z_m2` | Integral lattice of rank 1 and signature (0, 1) | 1 | (0, 1) | -2 | Join of Category of even lattices and Category of nondegenerate lattices and Category of finite-rank lattices |

## Abstract Category Theory & Universal Constructions

> Category of categories (Cat), Arrow and Slice categories, Limits, Colimits, Biproducts, Subobjects, and Diagram categories.

```mermaid
graph RL
  Cat["Cat"]
  CoxeterDiagrams["CoxeterDiagrams"]
  DirectSumObjects["DirectSumObjects"]
  DiscreteCategories["DiscreteCategories"]
  HomCategories["HomCategories"]
  Objects["Objects"]
  RationalLattices["RationalLattices(R)"]
  FinitelyGeneratedFreeFormModules("FinitelyGeneratedFreeFormModules(R)")
  Sets("Sets")
  SymmetricBilinearFormModules("SymmetricBilinearFormModules(R)")
  Cat --> Objects
  CoxeterDiagrams --> Sets
  DirectSumObjects --> Objects
  DiscreteCategories --> Objects
  HomCategories --> Objects
  RationalLattices --> FinitelyGeneratedFreeFormModules
  RationalLattices --> SymmetricBilinearFormModules
  classDef outside stroke-dasharray:6 4,fill:#f8fafc;
  class FinitelyGeneratedFreeFormModules,Sets,SymmetricBilinearFormModules outside;
```

### Categories

Ordered by depth: the least structured first.

#### `Objects` {#cat-objects}

The root of the owned mathematical category graph.

```text
This category carries no mathematical supercategory. Sage's own
``Objects``/``Sets`` categories remain runtime substrate only and are not
semantic ancestors of owned categories.
```

- **not exported**: reachable only as a supercategory
- **probed as** `Category of represented mathematical objects`
- **below** [`Cardinalities`](#cat-cardinalities), [`Cat`](#cat-cat), [`DirectSumObjects`](#cat-directsumobjects), [`DiscreteCategories`](#cat-discretecategories), [`HomCategories`](#cat-homcategories), [`OrdinalSemirings`](#cat-ordinalsemirings), [`Sets`](#cat-sets), [`SetsWithPartialMaps`](#cat-setswithpartialmaps)
- **build an object** `Objects(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - The root of the owned mathematical category graph.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |

#### `Cat` {#cat-cat}

The represented category of categories.

```text
``Cat`` deliberately does not take the owned base that makes a category an
object of ``Cat``.  Applying it here would assert a self-membership
statement and would make ``Cat().Mor(Cat(), Cat())`` an apparent
1-categorical construction; that higher level is not modelled.  Every
other owned category is such an object.
```

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/cat.py:98`
- **probed as** `Category of categories`
- **above** [`Objects`](#cat-objects)
- **refines**, transitively, in Sage's linearization order: [`Objects`](#cat-objects)
- **build an object** `Cat(x, *args, **opts)`

**Operations introduced here** (11 on objects)

*on objects*

- `ArrowCategory()`
  - Return \(\mathrm{Ar}(C)=\mathrm{Fun}([1],C)\).
- `Core()`
  - Return the maximal groupoid inside this category.
- `CosliceUnder(base_object)`
  - Return the coslice \(X/C\).
- `ElementType()` <sub>read as an attribute</sub>
  - Return the complete implementation type for their elements.
- `ObjectType()` <sub>read as an attribute</sub>
  - Return the complete implementation type for objects of this category.
- `SliceOver(base_object)`
  - Return the slice \(C/X\).
- `SubobjectCategory(base_object)`
  - Return the category of subobjects of ``base_object`` here.
- `SuperobjectCategory(base_object)`
  - Return the category of superobjects of ``base_object`` here.
- `fiber_product(left_leg, right_leg)`
  - Return the fiber product of the cospan these two legs form.
- `opposite()`
  - Return \(C^{op}\).
- `pushout(left_leg, right_leg)`
  - Return the pushout of the span these two legs form.

#### `DirectSumObjects` {#cat-directsumobjects}

Objects carrying a selected ordered family of direct summands.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/direct_sum_objects.py:11`
- **probed as** `Category of direct sum objects`
- **above** [`Objects`](#cat-objects)
- **below** [`BiproductModules(R)`](#cat-biproductmodules)
- **refines**, transitively, in Sage's linearization order: [`Objects`](#cat-objects)
- **build an object** `DirectSumObjects(x, *args, **opts)`
- **specimens** `NamedLattices.E10`, `NamedLattices.E10_2`, `NamedLattices.SEn`, `NamedLattices.U_E8_2`

**Operations introduced here** (5 on objects)

*on objects*

- `ElementType()`
  - Objects carrying a selected ordered family of direct summands.
- `number_of_summands()`
- `summand(label)`
- `summand_index_set()`
- `summands()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `DiscreteCategories` {#cat-discretecategories}

The category of represented discrete categories.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/functors.py:279`
- **probed as** `Category of discrete categories`
- **above** [`Objects`](#cat-objects)
- **refines**, transitively, in Sage's linearization order: [`Objects`](#cat-objects)
- **build an object** `DiscreteCategories(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `HomCategories` {#cat-homcategories}

The category of represented fixed-endpoint Hom categories.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/hom_categories.py:713`
- **probed as** `Category of hom categories`
- **above** [`Objects`](#cat-objects)
- **refines**, transitively, in Sage's linearization order: [`Objects`](#cat-objects)
- **build an object** `HomCategories(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `CoxeterDiagrams` {#cat-coxeterdiagrams}

Finite Coxeter diagrams: a symmetric matrix of vertex angles.

- **defined at** `src/dzack_research/preamble/categories/coxeter_diagrams.py:43`
- **probed as** `Category of Coxeter diagrams`
- **above** [`Sets`](#cat-sets)
- **refines**, transitively, in Sage's linearization order: [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `CoxeterDiagrams(x, *args, **opts)`

**Operations introduced here** (23 on objects)

*on objects*

- `ElementType()`
  - Finite Coxeter diagrams: a symmetric matrix of vertex angles.
- `cardinality()`
- `connected_components()`
- `coxeter_entry(left, right)`
- `coxeter_matrix()`
- `elliptic_subdiagrams(*, connected=False)`
- `graph()`
- `index_set()`
- `induced_subdiagram(vertices)`
- `is_connected() -> bool`
- `is_elliptic() -> bool`
- `is_hyperbolic() -> bool`
- `is_parabolic() -> bool`
- `is_rooted() -> bool`
- `negative_inertia_index()`
  - Return \(n_-\), the negative index of inertia of the Schlaefli form.
- `parabolic_subdiagrams(*, connected=False)`
- `positive_inertia_index()`
  - Return \(n_+\), the positive index of inertia of the Schlaefli form.
- `preferred_positions()`
  - Return stored presentation coordinates, or a computed graph layout.
- `root_gram_tensor()`
- `roots()`
- `schlafli_tensor()`
  - Return the normalized reflection Gram tensor ``S_ii=1``.
- `vertex_names()`
- `zero_inertia_index()`
  - Return \(n_0\), the dimension of the radical of the Schlaefli form.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `RationalLattices(R)` {#cat-rationallattices}

Nondegenerate finite free `R`-modules with `Frac(R)`-valued form.

- **defined at** `src/dzack_research/preamble/categories/rational_lattices.py:26`
- **probed as** `Category of rational lattices`
- **above** [`FinitelyGeneratedFreeFormModules(R)`](#cat-finitelygeneratedfreeformmodules), [`SymmetricBilinearFormModules(R)`](#cat-symmetricbilinearformmodules)
- **refines**, transitively, in Sage's linearization order: [`FinitelyGeneratedFreeFormModules(R)`](#cat-finitelygeneratedfreeformmodules) · [`FinitelyGeneratedFormModules(R)`](#cat-finitelygeneratedformmodules) · [`FreeFormModules(R)`](#cat-freeformmodules) · [`FinitelyGeneratedFreeModules(R)`](#cat-finitelygeneratedfreemodules) · [`ModulesWithChosenFinitePresentation(R)`](#cat-moduleswithchosenfinitepresentation) · [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) · [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) · [`SymmetricBilinearFormModules(R)`](#cat-symmetricbilinearformmodules) · [`FramedFreeModules(R)`](#cat-framedfreemodules) · [`BilinearFormModules(R)`](#cat-bilinearformmodules) · [`FormModules(R)`](#cat-formmodules) · [`FramedModules(R)`](#cat-framedmodules) · [`FreeModules(R)`](#cat-freemodules) · [`ProjectiveModules(R)`](#cat-projectivemodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `RationalLattices(R)(x, *args, **opts)`

**Operations introduced here** (4 on objects)

*on objects*

- `ElementType()`
  - Nondegenerate finite free ``R``-modules with ``Frac(R)``-valued form.
- `determinant()`
- `fraction_field()`
- `is_nondegenerate() -> bool`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| [`FormModules(R)`](#cat-formmodules) | 17 | 2 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FramedFreeModules(R)`](#cat-framedfreemodules) | 13 |  |  |
| [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) | 10 |  |  |
| [`FramedModules(R)`](#cat-framedmodules) | 10 |  |  |
| [`FinitelyGeneratedFreeFormModules(R)`](#cat-finitelygeneratedfreeformmodules) | 8 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`SymmetricBilinearFormModules(R)`](#cat-symmetricbilinearformmodules) | 7 |  |  |
| [`FinitelyGeneratedFreeModules(R)`](#cat-finitelygeneratedfreemodules) | 3 |  |  |
| [`FreeFormModules(R)`](#cat-freeformmodules) | 3 |  |  |
| [`ProjectiveModules(R)`](#cat-projectivemodules) | 3 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) | 2 |  |  |
| [`FreeModules(R)`](#cat-freemodules) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`BilinearFormModules(R)`](#cat-bilinearformmodules) | 1 |  |  |
| [`FinitelyGeneratedFormModules(R)`](#cat-finitelygeneratedformmodules) | 1 |  |  |
| [`ModulesWithChosenFinitePresentation(R)`](#cat-moduleswithchosenfinitepresentation) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `ArrowCategory` {#cat-arrowcategory}

The category `Arr(C)=Fun([1],C)`.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py:103`
- **not placed**: `ArrowCategory(base_category)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

**Operations introduced here** (4 on objects)

*on objects*

- `arrow()`
- `arrow_category()`
- `source_object()`
- `target_object()`

#### `AutCategoryConstruction` {#cat-autcategoryconstruction}

The family `A |-> Aut_C(A)`.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/hom_categories.py:1107`
- **not placed**: `AutCategoryConstruction(base_category)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `AutCategoryOf` {#cat-autcategoryof}

The family `A |-> Aut_C(A)`.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/hom_categories.py:1049`
- **not placed**: `AutCategoryOf(base_category)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `AutomorphismArrowCategory` {#cat-automorphismarrowcategory}

The full subcategory of the arrow category on automorphisms.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py:332`
- **not placed**: `AutomorphismArrowCategory(base_category)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `BiproductCategory` {#cat-biproductcategory}

Objects equipped with the selected finite biproduct structure.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/products.py:336`
- **not placed**: `BiproductCategory(factors)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `CoconeCategory` {#cat-coconecategory}

The category of cocones under one represented diagram.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/products.py:216`
- **not placed**: `CoconeCategory(diagram)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

**Operations introduced here** (6 on objects)

*on objects*

- `apex()`
- `cocone_category()`
- `costructure_morphism(index)`
- `costructure_morphisms()`
- `diagram()`
- `transformation()`

#### `ColimitsOfCategory` {#cat-colimitsofcategory}

The base class for modeling mathematical categories, like for example:

```text
- ``Groups()`` -- the category of groups
- ``EuclideanDomains()`` -- the category of euclidean rings
- ``VectorSpaces(QQ)`` -- the category of vector spaces over the field of
  rationals

See :mod:`sage.categories.primer` for an introduction to
categories in Sage, their relevance, purpose, and usage. The
documentation below will focus on their implementation.

Technically, a category is an instance of the class
:class:`Category` or some of its subclasses. Some categories, like
:class:`VectorSpaces`, are parametrized: ``VectorSpaces(QQ)`` is one of
many instances of the class :class:`VectorSpaces`. On the other
hand, ``EuclideanDomains()`` is the single instance of the class
:class:`EuclideanDomains`.

Recall that an algebraic structure (say, the ring `\QQ[x]`) is
modelled in Sage by an object which is called a parent. This
object belongs to certain categories (here ``EuclideanDomains()`` and
``Algebras()``). The elements of the ring are themselves objects.

The class of a category (say :class:`EuclideanDomains`) can define simultaneously:

- Operations on the category itself (what is its super categories?
  its category of morphisms? its dual category?).
- Generic operations on parents in this category, like the ring `\QQ[x]`.
- Generic operations on elements of such parents (e. g., the
  Euclidean algorithm for computing gcds).
- Generic operations on morphisms of this category.

This is achieved as follows::

    sage: from sage.categories.category import Category
    sage: class EuclideanDomains(Category):
    ....:     # operations on the category itself
    ....:     def super_categories(self):
    ....:         [Rings()]
    ....:
    ....:     def dummy(self): # TODO: find some good examples
    ....:          pass
    ....:
    ....:     class ParentMethods: # holds the generic operations on parents
    ....:          # TODO: find a good example of an operation
    ....:          pass
    ....:
    ....:     class ElementMethods:# holds the generic operations on elements
    ....:          def gcd(x, y):
    ....:              # Euclid algorithms
    ....:              pass
    ....:
    ....:     class MorphismMethods: # holds the generic operations on morphisms
    ....:          # TODO: find a good example of an operation
    ....:          pass
    ....:

Note that the nested class ``ParentMethods`` is merely a container
of operations, and does not inherit from anything. Instead, the
hierarchy relation is defined once at the level of the categories,
and the actual hierarchy of classes is built in parallel from all
the ``ParentMethods`` nested classes, and stored in the attributes
``parent_class``. Then, a parent in a category ``C`` receives the
appropriate operations from all the super categories by usual
class inheritance from ``C.parent_class``.

Similarly, two other hierarchies of classes, for elements and
morphisms respectively, are built from all the ``ElementMethods``
and ``MorphismMethods`` nested classes.

EXAMPLES:

We define a hierarchy of four categories ``As()``, ``Bs()``,
``Cs()``, ``Ds()`` with a diamond inheritance. Think for example:

- ``As()`` -- the category of sets
- ``Bs()`` -- the category of additive groups
- ``Cs()`` -- the category of multiplicative monoids
- ``Ds()`` -- the category of rings

::

    sage: from sage.categories.category import Category
    sage: from sage.misc.lazy_attribute import lazy_attribute
    sage: class As (Category):
    ....:     def super_categories(self):
    ....:         return []
    ....:
    ....:     class ParentMethods:
    ....:         def fA(self):
    ....:             return "A"
    ....:         f = fA

    sage: class Bs (Category):
    ....:     def super_categories(self):
    ....:         return [As()]
    ....:
    ....:     class ParentMethods:
    ....:         def fB(self):
    ....:             return "B"

    sage: class Cs (Category):
    ....:     def super_categories(self):
    ....:         return [As()]
    ....:
    ....:     class ParentMethods:
    ....:         def fC(self):
    ....:             return "C"
    ....:         f = fC

    sage: class Ds (Category):
    ....:     def super_categories(self):
    ....:         return [Bs(),Cs()]
    ....:
    ....:     class ParentMethods:
    ....:         def fD(self):
    ....:             return "D"

Categories should always have unique representation; by :issue:`12215`,
this means that it will be kept in cache, but only
if there is still some strong reference to it.

We check this before proceeding::

    sage: import gc
    sage: idAs = id(As())
    sage: _ = gc.collect()
    sage: n == id(As())
    False
    sage: a = As()
    sage: id(As()) == id(As())
    True
    sage: As().parent_class == As().parent_class
    True

We construct a parent in the category ``Ds()`` (that, is an instance
of ``Ds().parent_class``), and check that it has access to all the
methods provided by all the categories, with the appropriate
inheritance order::

    sage: D = Ds().parent_class()
    sage: [ D.fA(), D.fB(), D.fC(), D.fD() ]
    ['A', 'B', 'C', 'D']
    sage: D.f()
    'C'

::

    sage: C = Cs().parent_class()
    sage: [ C.fA(), C.fC() ]
    ['A', 'C']
    sage: C.f()
    'C'

Here is the parallel hierarchy of classes which has been built
automatically, together with the method resolution order (``.mro()``)::

    sage: As().parent_class
    <class '__main__.As.parent_class'>
    sage: As().parent_class.__bases__
    (<... 'object'>,)
    sage: As().parent_class.mro()
    [<class '__main__.As.parent_class'>, <... 'object'>]

::

    sage: Bs().parent_class
    <class '__main__.Bs.parent_class'>
    sage: Bs().parent_class.__bases__
    (<class '__main__.As.parent_class'>,)
    sage: Bs().parent_class.mro()
    [<class '__main__.Bs.parent_class'>, <class '__main__.As.parent_class'>, <... 'object'>]

::

    sage: Cs().parent_class
    <class '__main__.Cs.parent_class'>
    sage: Cs().parent_class.__bases__
    (<class '__main__.As.parent_class'>,)
    sage: Cs().parent_class.__mro__
    (<class '__main__.Cs.parent_class'>, <class '__main__.As.parent_class'>, <... 'object'>)

::

    sage: Ds().parent_class
    <class '__main__.Ds.parent_class'>
    sage: Ds().parent_class.__bases__
    (<class '__main__.Cs.parent_class'>, <class '__main__.Bs.parent_class'>)
    sage: Ds().parent_class.mro()
    [<class '__main__.Ds.parent_class'>, <class '__main__.Cs.parent_class'>,
     <class '__main__.Bs.parent_class'>, <class '__main__.As.parent_class'>, <... 'object'>]

Note that two categories in the same class need not have the
same ``super_categories``. For example, ``Algebras(QQ)`` has
``VectorSpaces(QQ)`` as super category, whereas ``Algebras(ZZ)``
only has ``Modules(ZZ)`` as super category. In particular, the
constructed parent class and element class will differ (inheriting,
or not, methods specific for vector spaces)::

    sage: Algebras(QQ).parent_class is Algebras(ZZ).parent_class
    False
    sage: issubclass(Algebras(QQ).parent_class, VectorSpaces(QQ).parent_class)
    True

On the other hand, identical hierarchies of classes are,
preferably, built only once (e.g. for categories over a base ring)::

    sage: Algebras(GF(5)).parent_class is Algebras(GF(7)).parent_class
    True
    sage: F = FractionField(ZZ['t'])
    sage: Coalgebras(F).parent_class is Coalgebras(FractionField(F['x'])).parent_class
    True

We now construct a parent in the usual way::

    sage: class myparent(Parent):
    ....:     def __init__(self):
    ....:         Parent.__init__(self, category=Ds())
    ....:     def g(self):
    ....:         return "myparent"
    ....:     class Element():
    ....:         pass
    sage: D = myparent()
    sage: D.__class__
    <class '__main__.myparent_with_category'>
    sage: D.__class__.__bases__
    (<class '__main__.myparent'>, <class '__main__.Ds.parent_class'>)
    sage: D.__class__.mro()
    [<class '__main__.myparent_with_category'>,
    <class '__main__.myparent'>,
    <class 'sage.structure.parent.Parent'>,
    <class 'sage.structure.category_object.CategoryObject'>,
    <class 'sage.structure.sage_object.SageObject'>,
    <class '__main__.Ds.parent_class'>,
    <class '__main__.Cs.parent_class'>,
    <class '__main__.Bs.parent_class'>,
    <class '__main__.As.parent_class'>,
    <... 'object'>]
    sage: D.fA()
    'A'
    sage: D.fB()
    'B'
    sage: D.fC()
    'C'
    sage: D.fD()
    'D'
    sage: D.f()
    'C'
    sage: D.g()
    'myparent'

::

    sage: D.element_class
    <class '__main__.myparent_with_category.element_class'>
    sage: D.element_class.mro()
    [<class '__main__.myparent_with_category.element_class'>,
    <class ...__main__....Element...>,
    <class '__main__.Ds.element_class'>,
    <class '__main__.Cs.element_class'>,
    <class '__main__.Bs.element_class'>,
    <class '__main__.As.element_class'>,
    <... 'object'>]


TESTS::

    sage: import __main__
    sage: __main__.myparent = myparent
    sage: __main__.As = As
    sage: __main__.Bs = Bs
    sage: __main__.Cs = Cs
    sage: __main__.Ds = Ds
    sage: loads(dumps(Ds)) is Ds
    True
    sage: loads(dumps(Ds())) is Ds()
    True
    sage: loads(dumps(Ds().element_class)) is Ds().element_class
    True

.. automethod:: Category._super_categories
.. automethod:: Category._super_categories_for_classes
.. automethod:: Category._all_super_categories
.. automethod:: Category._all_super_categories_proper
.. automethod:: Category._set_of_super_categories
.. automethod:: Category._make_named_class
.. automethod:: Category._repr_
.. automethod:: Category._repr_object_names
.. automethod:: Category._test_category
.. automethod:: Category._with_axiom
.. automethod:: Category._with_axiom_as_tuple
.. automethod:: Category._without_axioms
.. automethod:: Category._sort
.. automethod:: Category._sort_uniq
.. automethod:: Category.__classcall__
.. automethod:: Category.__init__
```

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/products.py:308`
- **not placed**: `ColimitsOfCategory(index_category, target_category)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `ConeCategory` {#cat-conecategory}

The category of cones over one represented diagram.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/products.py:145`
- **not placed**: `ConeCategory(diagram)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

**Operations introduced here** (6 on objects)

*on objects*

- `apex()`
- `cone_category()`
- `diagram()`
- `structure_morphism(index)`
- `structure_morphisms()`
- `transformation()`

#### `CoproductCoconeCategory` {#cat-coproductcoconecategory}

Selected coproduct cocones under one finite discrete diagram.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/products.py:291`
- **not placed**: `CoproductCoconeCategory(diagram)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `CoproductsOfCategory` {#cat-coproductsofcategory}

The base class for modeling mathematical categories, like for example:

```text
- ``Groups()`` -- the category of groups
- ``EuclideanDomains()`` -- the category of euclidean rings
- ``VectorSpaces(QQ)`` -- the category of vector spaces over the field of
  rationals

See :mod:`sage.categories.primer` for an introduction to
categories in Sage, their relevance, purpose, and usage. The
documentation below will focus on their implementation.

Technically, a category is an instance of the class
:class:`Category` or some of its subclasses. Some categories, like
:class:`VectorSpaces`, are parametrized: ``VectorSpaces(QQ)`` is one of
many instances of the class :class:`VectorSpaces`. On the other
hand, ``EuclideanDomains()`` is the single instance of the class
:class:`EuclideanDomains`.

Recall that an algebraic structure (say, the ring `\QQ[x]`) is
modelled in Sage by an object which is called a parent. This
object belongs to certain categories (here ``EuclideanDomains()`` and
``Algebras()``). The elements of the ring are themselves objects.

The class of a category (say :class:`EuclideanDomains`) can define simultaneously:

- Operations on the category itself (what is its super categories?
  its category of morphisms? its dual category?).
- Generic operations on parents in this category, like the ring `\QQ[x]`.
- Generic operations on elements of such parents (e. g., the
  Euclidean algorithm for computing gcds).
- Generic operations on morphisms of this category.

This is achieved as follows::

    sage: from sage.categories.category import Category
    sage: class EuclideanDomains(Category):
    ....:     # operations on the category itself
    ....:     def super_categories(self):
    ....:         [Rings()]
    ....:
    ....:     def dummy(self): # TODO: find some good examples
    ....:          pass
    ....:
    ....:     class ParentMethods: # holds the generic operations on parents
    ....:          # TODO: find a good example of an operation
    ....:          pass
    ....:
    ....:     class ElementMethods:# holds the generic operations on elements
    ....:          def gcd(x, y):
    ....:              # Euclid algorithms
    ....:              pass
    ....:
    ....:     class MorphismMethods: # holds the generic operations on morphisms
    ....:          # TODO: find a good example of an operation
    ....:          pass
    ....:

Note that the nested class ``ParentMethods`` is merely a container
of operations, and does not inherit from anything. Instead, the
hierarchy relation is defined once at the level of the categories,
and the actual hierarchy of classes is built in parallel from all
the ``ParentMethods`` nested classes, and stored in the attributes
``parent_class``. Then, a parent in a category ``C`` receives the
appropriate operations from all the super categories by usual
class inheritance from ``C.parent_class``.

Similarly, two other hierarchies of classes, for elements and
morphisms respectively, are built from all the ``ElementMethods``
and ``MorphismMethods`` nested classes.

EXAMPLES:

We define a hierarchy of four categories ``As()``, ``Bs()``,
``Cs()``, ``Ds()`` with a diamond inheritance. Think for example:

- ``As()`` -- the category of sets
- ``Bs()`` -- the category of additive groups
- ``Cs()`` -- the category of multiplicative monoids
- ``Ds()`` -- the category of rings

::

    sage: from sage.categories.category import Category
    sage: from sage.misc.lazy_attribute import lazy_attribute
    sage: class As (Category):
    ....:     def super_categories(self):
    ....:         return []
    ....:
    ....:     class ParentMethods:
    ....:         def fA(self):
    ....:             return "A"
    ....:         f = fA

    sage: class Bs (Category):
    ....:     def super_categories(self):
    ....:         return [As()]
    ....:
    ....:     class ParentMethods:
    ....:         def fB(self):
    ....:             return "B"

    sage: class Cs (Category):
    ....:     def super_categories(self):
    ....:         return [As()]
    ....:
    ....:     class ParentMethods:
    ....:         def fC(self):
    ....:             return "C"
    ....:         f = fC

    sage: class Ds (Category):
    ....:     def super_categories(self):
    ....:         return [Bs(),Cs()]
    ....:
    ....:     class ParentMethods:
    ....:         def fD(self):
    ....:             return "D"

Categories should always have unique representation; by :issue:`12215`,
this means that it will be kept in cache, but only
if there is still some strong reference to it.

We check this before proceeding::

    sage: import gc
    sage: idAs = id(As())
    sage: _ = gc.collect()
    sage: n == id(As())
    False
    sage: a = As()
    sage: id(As()) == id(As())
    True
    sage: As().parent_class == As().parent_class
    True

We construct a parent in the category ``Ds()`` (that, is an instance
of ``Ds().parent_class``), and check that it has access to all the
methods provided by all the categories, with the appropriate
inheritance order::

    sage: D = Ds().parent_class()
    sage: [ D.fA(), D.fB(), D.fC(), D.fD() ]
    ['A', 'B', 'C', 'D']
    sage: D.f()
    'C'

::

    sage: C = Cs().parent_class()
    sage: [ C.fA(), C.fC() ]
    ['A', 'C']
    sage: C.f()
    'C'

Here is the parallel hierarchy of classes which has been built
automatically, together with the method resolution order (``.mro()``)::

    sage: As().parent_class
    <class '__main__.As.parent_class'>
    sage: As().parent_class.__bases__
    (<... 'object'>,)
    sage: As().parent_class.mro()
    [<class '__main__.As.parent_class'>, <... 'object'>]

::

    sage: Bs().parent_class
    <class '__main__.Bs.parent_class'>
    sage: Bs().parent_class.__bases__
    (<class '__main__.As.parent_class'>,)
    sage: Bs().parent_class.mro()
    [<class '__main__.Bs.parent_class'>, <class '__main__.As.parent_class'>, <... 'object'>]

::

    sage: Cs().parent_class
    <class '__main__.Cs.parent_class'>
    sage: Cs().parent_class.__bases__
    (<class '__main__.As.parent_class'>,)
    sage: Cs().parent_class.__mro__
    (<class '__main__.Cs.parent_class'>, <class '__main__.As.parent_class'>, <... 'object'>)

::

    sage: Ds().parent_class
    <class '__main__.Ds.parent_class'>
    sage: Ds().parent_class.__bases__
    (<class '__main__.Cs.parent_class'>, <class '__main__.Bs.parent_class'>)
    sage: Ds().parent_class.mro()
    [<class '__main__.Ds.parent_class'>, <class '__main__.Cs.parent_class'>,
     <class '__main__.Bs.parent_class'>, <class '__main__.As.parent_class'>, <... 'object'>]

Note that two categories in the same class need not have the
same ``super_categories``. For example, ``Algebras(QQ)`` has
``VectorSpaces(QQ)`` as super category, whereas ``Algebras(ZZ)``
only has ``Modules(ZZ)`` as super category. In particular, the
constructed parent class and element class will differ (inheriting,
or not, methods specific for vector spaces)::

    sage: Algebras(QQ).parent_class is Algebras(ZZ).parent_class
    False
    sage: issubclass(Algebras(QQ).parent_class, VectorSpaces(QQ).parent_class)
    True

On the other hand, identical hierarchies of classes are,
preferably, built only once (e.g. for categories over a base ring)::

    sage: Algebras(GF(5)).parent_class is Algebras(GF(7)).parent_class
    True
    sage: F = FractionField(ZZ['t'])
    sage: Coalgebras(F).parent_class is Coalgebras(FractionField(F['x'])).parent_class
    True

We now construct a parent in the usual way::

    sage: class myparent(Parent):
    ....:     def __init__(self):
    ....:         Parent.__init__(self, category=Ds())
    ....:     def g(self):
    ....:         return "myparent"
    ....:     class Element():
    ....:         pass
    sage: D = myparent()
    sage: D.__class__
    <class '__main__.myparent_with_category'>
    sage: D.__class__.__bases__
    (<class '__main__.myparent'>, <class '__main__.Ds.parent_class'>)
    sage: D.__class__.mro()
    [<class '__main__.myparent_with_category'>,
    <class '__main__.myparent'>,
    <class 'sage.structure.parent.Parent'>,
    <class 'sage.structure.category_object.CategoryObject'>,
    <class 'sage.structure.sage_object.SageObject'>,
    <class '__main__.Ds.parent_class'>,
    <class '__main__.Cs.parent_class'>,
    <class '__main__.Bs.parent_class'>,
    <class '__main__.As.parent_class'>,
    <... 'object'>]
    sage: D.fA()
    'A'
    sage: D.fB()
    'B'
    sage: D.fC()
    'C'
    sage: D.fD()
    'D'
    sage: D.f()
    'C'
    sage: D.g()
    'myparent'

::

    sage: D.element_class
    <class '__main__.myparent_with_category.element_class'>
    sage: D.element_class.mro()
    [<class '__main__.myparent_with_category.element_class'>,
    <class ...__main__....Element...>,
    <class '__main__.Ds.element_class'>,
    <class '__main__.Cs.element_class'>,
    <class '__main__.Bs.element_class'>,
    <class '__main__.As.element_class'>,
    <... 'object'>]


TESTS::

    sage: import __main__
    sage: __main__.myparent = myparent
    sage: __main__.As = As
    sage: __main__.Bs = Bs
    sage: __main__.Cs = Cs
    sage: __main__.Ds = Ds
    sage: loads(dumps(Ds)) is Ds
    True
    sage: loads(dumps(Ds())) is Ds()
    True
    sage: loads(dumps(Ds().element_class)) is Ds().element_class
    True

.. automethod:: Category._super_categories
.. automethod:: Category._super_categories_for_classes
.. automethod:: Category._all_super_categories
.. automethod:: Category._all_super_categories_proper
.. automethod:: Category._set_of_super_categories
.. automethod:: Category._make_named_class
.. automethod:: Category._repr_
.. automethod:: Category._repr_object_names
.. automethod:: Category._test_category
.. automethod:: Category._with_axiom
.. automethod:: Category._with_axiom_as_tuple
.. automethod:: Category._without_axioms
.. automethod:: Category._sort
.. automethod:: Category._sort_uniq
.. automethod:: Category.__classcall__
.. automethod:: Category.__init__
```

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/products.py:316`
- **not placed**: `CoproductsOfCategory(index_category, target_category)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `CoreCategory` {#cat-corecategory}

The maximal subgroupoid (core) of a represented category.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py:621`
- **not placed**: `CoreCategory(base_category)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `CosliceCategory` {#cat-coslicecategory}

The coslice category \(X/C\).

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py:272`
- **not placed**: `CosliceCategory(base_category, base_object)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `DiagramCategory` {#cat-diagramcategory}

The functor category `[J,C]` of diagrams of one shape.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/products.py:27`
- **not placed**: `DiagramCategory(index_category, target_category)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `DirectSumCategory` {#cat-directsumcategory}

Objects equipped with the selected finite biproduct structure.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/products.py:336`
- **not placed**: `DirectSumCategory(factors)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `DirectedSystem` {#cat-directedsystem}

A diagram category whose index category represents a directed order.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/products.py:40`
- **not placed**: `DirectedSystem(index_category, target_category)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `DiscreteCategory` {#cat-discretecategory}

The discrete category on one set.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/functors.py:204`
- **not placed**: `DiscreteCategory(object_set)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

**Operations introduced here** (2 on objects)

*on objects*

- `discrete_category()`
- `value()`

#### `EndArrowCategory` {#cat-endarrowcategory}

The full subcategory of `Arr(C)` on endomorphisms.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py:314`
- **not placed**: `EndArrowCategory(base_category)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `EndCategoryConstruction` {#cat-endcategoryconstruction}

The family `A |-> End_C(A)`.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/hom_categories.py:1091`
- **not placed**: `EndCategoryConstruction(base_category)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `EndCategoryOf` {#cat-endcategoryof}

The family `A |-> End_C(A)`.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/hom_categories.py:952`
- **not placed**: `EndCategoryOf(base_category)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `EpiCategoryConstruction` {#cat-epicategoryconstruction}

A family of fixed-endpoint subcategories of an existing `Mor`.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/hom_categories.py:1099`
- **not placed**: `EpiCategoryConstruction(base_category)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `EpiCategoryOf` {#cat-epicategoryof}

A family of fixed-endpoint subcategories of an existing `Mor`.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/hom_categories.py:1014`
- **not placed**: `EpiCategoryOf(base_category)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `EpimorphismArrowCategory` {#cat-epimorphismarrowcategory}

The full subcategory of the arrow category on represented epimorphisms.

```text
As for monomorphisms, the base category's declared epi family answers.
```

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py:360`
- **not placed**: `EpimorphismArrowCategory(base_category)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `FunctorCategory` {#cat-functorcategory}

The category `[C,D]` of represented functors and natural transformations.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/cat.py:373`
- **not placed**: `FunctorCategory(category_of_categories, domain, codomain)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `HomCategoryConstruction` {#cat-homcategoryconstruction}

The family `(A,B) |-> Hom_C(A,B)` attached to one category `C`.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/hom_categories.py:1087`
- **not placed**: `HomCategoryConstruction(base_category)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `HomCategoryOf` {#cat-homcategoryof}

The family `(A,B) |-> Hom_C(A,B)` attached to one category `C`.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/hom_categories.py:821`
- **not placed**: `HomCategoryOf(base_category)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `InverseSystem` {#cat-inversesystem}

A diagram category read contravariantly as an inverse system.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/products.py:44`
- **not placed**: `InverseSystem(index_category, target_category)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `IsoArrowCategory` {#cat-isoarrowcategory}

The full subcategory of `Arr(C)` on explicitly represented isomorphisms.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py:323`
- **not placed**: `IsoArrowCategory(base_category)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `IsoCategoryConstruction` {#cat-isocategoryconstruction}

The family `(A,B) |-> Hom_C(A,B)` attached to one category `C`.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/hom_categories.py:1103`
- **not placed**: `IsoCategoryConstruction(base_category)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `IsoCategoryOf` {#cat-isocategoryof}

The family `(A,B) |-> Hom_C(A,B)` attached to one category `C`.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/hom_categories.py:1027`
- **not placed**: `IsoCategoryOf(base_category)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `LatticeHomset` {#cat-latticehomset}

A represented Hom object which is both a Sage Homset and a category.

```text
This is the live counterpart of the archived owned Hom-category base.  It
keeps Sage's hard requirement that every ``Morphism`` be parented by an
actual ``Homset``, while also making that same parent the discrete category
``Hom_C(A,B)``.  Concrete categories subclass this and add enrichment to
the *same object*.
```

- **defined at** `src/dzack_research/preamble/categories/lattice_morphisms.py:563`
- **not placed**: `LatticeHomset(hom_family, domain, codomain)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `LimitsOfCategory` {#cat-limitsofcategory}

The base class for modeling mathematical categories, like for example:

```text
- ``Groups()`` -- the category of groups
- ``EuclideanDomains()`` -- the category of euclidean rings
- ``VectorSpaces(QQ)`` -- the category of vector spaces over the field of
  rationals

See :mod:`sage.categories.primer` for an introduction to
categories in Sage, their relevance, purpose, and usage. The
documentation below will focus on their implementation.

Technically, a category is an instance of the class
:class:`Category` or some of its subclasses. Some categories, like
:class:`VectorSpaces`, are parametrized: ``VectorSpaces(QQ)`` is one of
many instances of the class :class:`VectorSpaces`. On the other
hand, ``EuclideanDomains()`` is the single instance of the class
:class:`EuclideanDomains`.

Recall that an algebraic structure (say, the ring `\QQ[x]`) is
modelled in Sage by an object which is called a parent. This
object belongs to certain categories (here ``EuclideanDomains()`` and
``Algebras()``). The elements of the ring are themselves objects.

The class of a category (say :class:`EuclideanDomains`) can define simultaneously:

- Operations on the category itself (what is its super categories?
  its category of morphisms? its dual category?).
- Generic operations on parents in this category, like the ring `\QQ[x]`.
- Generic operations on elements of such parents (e. g., the
  Euclidean algorithm for computing gcds).
- Generic operations on morphisms of this category.

This is achieved as follows::

    sage: from sage.categories.category import Category
    sage: class EuclideanDomains(Category):
    ....:     # operations on the category itself
    ....:     def super_categories(self):
    ....:         [Rings()]
    ....:
    ....:     def dummy(self): # TODO: find some good examples
    ....:          pass
    ....:
    ....:     class ParentMethods: # holds the generic operations on parents
    ....:          # TODO: find a good example of an operation
    ....:          pass
    ....:
    ....:     class ElementMethods:# holds the generic operations on elements
    ....:          def gcd(x, y):
    ....:              # Euclid algorithms
    ....:              pass
    ....:
    ....:     class MorphismMethods: # holds the generic operations on morphisms
    ....:          # TODO: find a good example of an operation
    ....:          pass
    ....:

Note that the nested class ``ParentMethods`` is merely a container
of operations, and does not inherit from anything. Instead, the
hierarchy relation is defined once at the level of the categories,
and the actual hierarchy of classes is built in parallel from all
the ``ParentMethods`` nested classes, and stored in the attributes
``parent_class``. Then, a parent in a category ``C`` receives the
appropriate operations from all the super categories by usual
class inheritance from ``C.parent_class``.

Similarly, two other hierarchies of classes, for elements and
morphisms respectively, are built from all the ``ElementMethods``
and ``MorphismMethods`` nested classes.

EXAMPLES:

We define a hierarchy of four categories ``As()``, ``Bs()``,
``Cs()``, ``Ds()`` with a diamond inheritance. Think for example:

- ``As()`` -- the category of sets
- ``Bs()`` -- the category of additive groups
- ``Cs()`` -- the category of multiplicative monoids
- ``Ds()`` -- the category of rings

::

    sage: from sage.categories.category import Category
    sage: from sage.misc.lazy_attribute import lazy_attribute
    sage: class As (Category):
    ....:     def super_categories(self):
    ....:         return []
    ....:
    ....:     class ParentMethods:
    ....:         def fA(self):
    ....:             return "A"
    ....:         f = fA

    sage: class Bs (Category):
    ....:     def super_categories(self):
    ....:         return [As()]
    ....:
    ....:     class ParentMethods:
    ....:         def fB(self):
    ....:             return "B"

    sage: class Cs (Category):
    ....:     def super_categories(self):
    ....:         return [As()]
    ....:
    ....:     class ParentMethods:
    ....:         def fC(self):
    ....:             return "C"
    ....:         f = fC

    sage: class Ds (Category):
    ....:     def super_categories(self):
    ....:         return [Bs(),Cs()]
    ....:
    ....:     class ParentMethods:
    ....:         def fD(self):
    ....:             return "D"

Categories should always have unique representation; by :issue:`12215`,
this means that it will be kept in cache, but only
if there is still some strong reference to it.

We check this before proceeding::

    sage: import gc
    sage: idAs = id(As())
    sage: _ = gc.collect()
    sage: n == id(As())
    False
    sage: a = As()
    sage: id(As()) == id(As())
    True
    sage: As().parent_class == As().parent_class
    True

We construct a parent in the category ``Ds()`` (that, is an instance
of ``Ds().parent_class``), and check that it has access to all the
methods provided by all the categories, with the appropriate
inheritance order::

    sage: D = Ds().parent_class()
    sage: [ D.fA(), D.fB(), D.fC(), D.fD() ]
    ['A', 'B', 'C', 'D']
    sage: D.f()
    'C'

::

    sage: C = Cs().parent_class()
    sage: [ C.fA(), C.fC() ]
    ['A', 'C']
    sage: C.f()
    'C'

Here is the parallel hierarchy of classes which has been built
automatically, together with the method resolution order (``.mro()``)::

    sage: As().parent_class
    <class '__main__.As.parent_class'>
    sage: As().parent_class.__bases__
    (<... 'object'>,)
    sage: As().parent_class.mro()
    [<class '__main__.As.parent_class'>, <... 'object'>]

::

    sage: Bs().parent_class
    <class '__main__.Bs.parent_class'>
    sage: Bs().parent_class.__bases__
    (<class '__main__.As.parent_class'>,)
    sage: Bs().parent_class.mro()
    [<class '__main__.Bs.parent_class'>, <class '__main__.As.parent_class'>, <... 'object'>]

::

    sage: Cs().parent_class
    <class '__main__.Cs.parent_class'>
    sage: Cs().parent_class.__bases__
    (<class '__main__.As.parent_class'>,)
    sage: Cs().parent_class.__mro__
    (<class '__main__.Cs.parent_class'>, <class '__main__.As.parent_class'>, <... 'object'>)

::

    sage: Ds().parent_class
    <class '__main__.Ds.parent_class'>
    sage: Ds().parent_class.__bases__
    (<class '__main__.Cs.parent_class'>, <class '__main__.Bs.parent_class'>)
    sage: Ds().parent_class.mro()
    [<class '__main__.Ds.parent_class'>, <class '__main__.Cs.parent_class'>,
     <class '__main__.Bs.parent_class'>, <class '__main__.As.parent_class'>, <... 'object'>]

Note that two categories in the same class need not have the
same ``super_categories``. For example, ``Algebras(QQ)`` has
``VectorSpaces(QQ)`` as super category, whereas ``Algebras(ZZ)``
only has ``Modules(ZZ)`` as super category. In particular, the
constructed parent class and element class will differ (inheriting,
or not, methods specific for vector spaces)::

    sage: Algebras(QQ).parent_class is Algebras(ZZ).parent_class
    False
    sage: issubclass(Algebras(QQ).parent_class, VectorSpaces(QQ).parent_class)
    True

On the other hand, identical hierarchies of classes are,
preferably, built only once (e.g. for categories over a base ring)::

    sage: Algebras(GF(5)).parent_class is Algebras(GF(7)).parent_class
    True
    sage: F = FractionField(ZZ['t'])
    sage: Coalgebras(F).parent_class is Coalgebras(FractionField(F['x'])).parent_class
    True

We now construct a parent in the usual way::

    sage: class myparent(Parent):
    ....:     def __init__(self):
    ....:         Parent.__init__(self, category=Ds())
    ....:     def g(self):
    ....:         return "myparent"
    ....:     class Element():
    ....:         pass
    sage: D = myparent()
    sage: D.__class__
    <class '__main__.myparent_with_category'>
    sage: D.__class__.__bases__
    (<class '__main__.myparent'>, <class '__main__.Ds.parent_class'>)
    sage: D.__class__.mro()
    [<class '__main__.myparent_with_category'>,
    <class '__main__.myparent'>,
    <class 'sage.structure.parent.Parent'>,
    <class 'sage.structure.category_object.CategoryObject'>,
    <class 'sage.structure.sage_object.SageObject'>,
    <class '__main__.Ds.parent_class'>,
    <class '__main__.Cs.parent_class'>,
    <class '__main__.Bs.parent_class'>,
    <class '__main__.As.parent_class'>,
    <... 'object'>]
    sage: D.fA()
    'A'
    sage: D.fB()
    'B'
    sage: D.fC()
    'C'
    sage: D.fD()
    'D'
    sage: D.f()
    'C'
    sage: D.g()
    'myparent'

::

    sage: D.element_class
    <class '__main__.myparent_with_category.element_class'>
    sage: D.element_class.mro()
    [<class '__main__.myparent_with_category.element_class'>,
    <class ...__main__....Element...>,
    <class '__main__.Ds.element_class'>,
    <class '__main__.Cs.element_class'>,
    <class '__main__.Bs.element_class'>,
    <class '__main__.As.element_class'>,
    <... 'object'>]


TESTS::

    sage: import __main__
    sage: __main__.myparent = myparent
    sage: __main__.As = As
    sage: __main__.Bs = Bs
    sage: __main__.Cs = Cs
    sage: __main__.Ds = Ds
    sage: loads(dumps(Ds)) is Ds
    True
    sage: loads(dumps(Ds())) is Ds()
    True
    sage: loads(dumps(Ds().element_class)) is Ds().element_class
    True

.. automethod:: Category._super_categories
.. automethod:: Category._super_categories_for_classes
.. automethod:: Category._all_super_categories
.. automethod:: Category._all_super_categories_proper
.. automethod:: Category._set_of_super_categories
.. automethod:: Category._make_named_class
.. automethod:: Category._repr_
.. automethod:: Category._repr_object_names
.. automethod:: Category._test_category
.. automethod:: Category._with_axiom
.. automethod:: Category._with_axiom_as_tuple
.. automethod:: Category._without_axioms
.. automethod:: Category._sort
.. automethod:: Category._sort_uniq
.. automethod:: Category.__classcall__
.. automethod:: Category.__init__
```

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/products.py:295`
- **not placed**: `LimitsOfCategory(index_category, target_category)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `MonoCategoryConstruction` {#cat-monocategoryconstruction}

A family of fixed-endpoint subcategories of an existing `Mor`.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/hom_categories.py:1095`
- **not placed**: `MonoCategoryConstruction(base_category)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `MonoCategoryOf` {#cat-monocategoryof}

A family of fixed-endpoint subcategories of an existing `Mor`.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/hom_categories.py:1001`
- **not placed**: `MonoCategoryOf(base_category)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `MonomorphismArrowCategory` {#cat-monomorphismarrowcategory}

The full subcategory of the arrow category on represented monomorphisms.

```text
Which arrows are monic is the base category's own question, so this asks
the mono family that category declares.  Injectivity is the answer in sets
and modules and is the declared default there; it is neither necessary nor
sufficient in every category, so it is not the definition used here.
```

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py:341`
- **not placed**: `MonomorphismArrowCategory(base_category)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `ProductConeCategory` {#cat-productconecategory}

Selected product cones over one finite discrete diagram.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/products.py:287`
- **not placed**: `ProductConeCategory(diagram)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `ProductsOfCategory` {#cat-productsofcategory}

The base class for modeling mathematical categories, like for example:

```text
- ``Groups()`` -- the category of groups
- ``EuclideanDomains()`` -- the category of euclidean rings
- ``VectorSpaces(QQ)`` -- the category of vector spaces over the field of
  rationals

See :mod:`sage.categories.primer` for an introduction to
categories in Sage, their relevance, purpose, and usage. The
documentation below will focus on their implementation.

Technically, a category is an instance of the class
:class:`Category` or some of its subclasses. Some categories, like
:class:`VectorSpaces`, are parametrized: ``VectorSpaces(QQ)`` is one of
many instances of the class :class:`VectorSpaces`. On the other
hand, ``EuclideanDomains()`` is the single instance of the class
:class:`EuclideanDomains`.

Recall that an algebraic structure (say, the ring `\QQ[x]`) is
modelled in Sage by an object which is called a parent. This
object belongs to certain categories (here ``EuclideanDomains()`` and
``Algebras()``). The elements of the ring are themselves objects.

The class of a category (say :class:`EuclideanDomains`) can define simultaneously:

- Operations on the category itself (what is its super categories?
  its category of morphisms? its dual category?).
- Generic operations on parents in this category, like the ring `\QQ[x]`.
- Generic operations on elements of such parents (e. g., the
  Euclidean algorithm for computing gcds).
- Generic operations on morphisms of this category.

This is achieved as follows::

    sage: from sage.categories.category import Category
    sage: class EuclideanDomains(Category):
    ....:     # operations on the category itself
    ....:     def super_categories(self):
    ....:         [Rings()]
    ....:
    ....:     def dummy(self): # TODO: find some good examples
    ....:          pass
    ....:
    ....:     class ParentMethods: # holds the generic operations on parents
    ....:          # TODO: find a good example of an operation
    ....:          pass
    ....:
    ....:     class ElementMethods:# holds the generic operations on elements
    ....:          def gcd(x, y):
    ....:              # Euclid algorithms
    ....:              pass
    ....:
    ....:     class MorphismMethods: # holds the generic operations on morphisms
    ....:          # TODO: find a good example of an operation
    ....:          pass
    ....:

Note that the nested class ``ParentMethods`` is merely a container
of operations, and does not inherit from anything. Instead, the
hierarchy relation is defined once at the level of the categories,
and the actual hierarchy of classes is built in parallel from all
the ``ParentMethods`` nested classes, and stored in the attributes
``parent_class``. Then, a parent in a category ``C`` receives the
appropriate operations from all the super categories by usual
class inheritance from ``C.parent_class``.

Similarly, two other hierarchies of classes, for elements and
morphisms respectively, are built from all the ``ElementMethods``
and ``MorphismMethods`` nested classes.

EXAMPLES:

We define a hierarchy of four categories ``As()``, ``Bs()``,
``Cs()``, ``Ds()`` with a diamond inheritance. Think for example:

- ``As()`` -- the category of sets
- ``Bs()`` -- the category of additive groups
- ``Cs()`` -- the category of multiplicative monoids
- ``Ds()`` -- the category of rings

::

    sage: from sage.categories.category import Category
    sage: from sage.misc.lazy_attribute import lazy_attribute
    sage: class As (Category):
    ....:     def super_categories(self):
    ....:         return []
    ....:
    ....:     class ParentMethods:
    ....:         def fA(self):
    ....:             return "A"
    ....:         f = fA

    sage: class Bs (Category):
    ....:     def super_categories(self):
    ....:         return [As()]
    ....:
    ....:     class ParentMethods:
    ....:         def fB(self):
    ....:             return "B"

    sage: class Cs (Category):
    ....:     def super_categories(self):
    ....:         return [As()]
    ....:
    ....:     class ParentMethods:
    ....:         def fC(self):
    ....:             return "C"
    ....:         f = fC

    sage: class Ds (Category):
    ....:     def super_categories(self):
    ....:         return [Bs(),Cs()]
    ....:
    ....:     class ParentMethods:
    ....:         def fD(self):
    ....:             return "D"

Categories should always have unique representation; by :issue:`12215`,
this means that it will be kept in cache, but only
if there is still some strong reference to it.

We check this before proceeding::

    sage: import gc
    sage: idAs = id(As())
    sage: _ = gc.collect()
    sage: n == id(As())
    False
    sage: a = As()
    sage: id(As()) == id(As())
    True
    sage: As().parent_class == As().parent_class
    True

We construct a parent in the category ``Ds()`` (that, is an instance
of ``Ds().parent_class``), and check that it has access to all the
methods provided by all the categories, with the appropriate
inheritance order::

    sage: D = Ds().parent_class()
    sage: [ D.fA(), D.fB(), D.fC(), D.fD() ]
    ['A', 'B', 'C', 'D']
    sage: D.f()
    'C'

::

    sage: C = Cs().parent_class()
    sage: [ C.fA(), C.fC() ]
    ['A', 'C']
    sage: C.f()
    'C'

Here is the parallel hierarchy of classes which has been built
automatically, together with the method resolution order (``.mro()``)::

    sage: As().parent_class
    <class '__main__.As.parent_class'>
    sage: As().parent_class.__bases__
    (<... 'object'>,)
    sage: As().parent_class.mro()
    [<class '__main__.As.parent_class'>, <... 'object'>]

::

    sage: Bs().parent_class
    <class '__main__.Bs.parent_class'>
    sage: Bs().parent_class.__bases__
    (<class '__main__.As.parent_class'>,)
    sage: Bs().parent_class.mro()
    [<class '__main__.Bs.parent_class'>, <class '__main__.As.parent_class'>, <... 'object'>]

::

    sage: Cs().parent_class
    <class '__main__.Cs.parent_class'>
    sage: Cs().parent_class.__bases__
    (<class '__main__.As.parent_class'>,)
    sage: Cs().parent_class.__mro__
    (<class '__main__.Cs.parent_class'>, <class '__main__.As.parent_class'>, <... 'object'>)

::

    sage: Ds().parent_class
    <class '__main__.Ds.parent_class'>
    sage: Ds().parent_class.__bases__
    (<class '__main__.Cs.parent_class'>, <class '__main__.Bs.parent_class'>)
    sage: Ds().parent_class.mro()
    [<class '__main__.Ds.parent_class'>, <class '__main__.Cs.parent_class'>,
     <class '__main__.Bs.parent_class'>, <class '__main__.As.parent_class'>, <... 'object'>]

Note that two categories in the same class need not have the
same ``super_categories``. For example, ``Algebras(QQ)`` has
``VectorSpaces(QQ)`` as super category, whereas ``Algebras(ZZ)``
only has ``Modules(ZZ)`` as super category. In particular, the
constructed parent class and element class will differ (inheriting,
or not, methods specific for vector spaces)::

    sage: Algebras(QQ).parent_class is Algebras(ZZ).parent_class
    False
    sage: issubclass(Algebras(QQ).parent_class, VectorSpaces(QQ).parent_class)
    True

On the other hand, identical hierarchies of classes are,
preferably, built only once (e.g. for categories over a base ring)::

    sage: Algebras(GF(5)).parent_class is Algebras(GF(7)).parent_class
    True
    sage: F = FractionField(ZZ['t'])
    sage: Coalgebras(F).parent_class is Coalgebras(FractionField(F['x'])).parent_class
    True

We now construct a parent in the usual way::

    sage: class myparent(Parent):
    ....:     def __init__(self):
    ....:         Parent.__init__(self, category=Ds())
    ....:     def g(self):
    ....:         return "myparent"
    ....:     class Element():
    ....:         pass
    sage: D = myparent()
    sage: D.__class__
    <class '__main__.myparent_with_category'>
    sage: D.__class__.__bases__
    (<class '__main__.myparent'>, <class '__main__.Ds.parent_class'>)
    sage: D.__class__.mro()
    [<class '__main__.myparent_with_category'>,
    <class '__main__.myparent'>,
    <class 'sage.structure.parent.Parent'>,
    <class 'sage.structure.category_object.CategoryObject'>,
    <class 'sage.structure.sage_object.SageObject'>,
    <class '__main__.Ds.parent_class'>,
    <class '__main__.Cs.parent_class'>,
    <class '__main__.Bs.parent_class'>,
    <class '__main__.As.parent_class'>,
    <... 'object'>]
    sage: D.fA()
    'A'
    sage: D.fB()
    'B'
    sage: D.fC()
    'C'
    sage: D.fD()
    'D'
    sage: D.f()
    'C'
    sage: D.g()
    'myparent'

::

    sage: D.element_class
    <class '__main__.myparent_with_category.element_class'>
    sage: D.element_class.mro()
    [<class '__main__.myparent_with_category.element_class'>,
    <class ...__main__....Element...>,
    <class '__main__.Ds.element_class'>,
    <class '__main__.Cs.element_class'>,
    <class '__main__.Bs.element_class'>,
    <class '__main__.As.element_class'>,
    <... 'object'>]


TESTS::

    sage: import __main__
    sage: __main__.myparent = myparent
    sage: __main__.As = As
    sage: __main__.Bs = Bs
    sage: __main__.Cs = Cs
    sage: __main__.Ds = Ds
    sage: loads(dumps(Ds)) is Ds
    True
    sage: loads(dumps(Ds())) is Ds()
    True
    sage: loads(dumps(Ds().element_class)) is Ds().element_class
    True

.. automethod:: Category._super_categories
.. automethod:: Category._super_categories_for_classes
.. automethod:: Category._all_super_categories
.. automethod:: Category._all_super_categories_proper
.. automethod:: Category._set_of_super_categories
.. automethod:: Category._make_named_class
.. automethod:: Category._repr_
.. automethod:: Category._repr_object_names
.. automethod:: Category._test_category
.. automethod:: Category._with_axiom
.. automethod:: Category._with_axiom_as_tuple
.. automethod:: Category._without_axioms
.. automethod:: Category._sort
.. automethod:: Category._sort_uniq
.. automethod:: Category.__classcall__
.. automethod:: Category.__init__
```

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/products.py:312`
- **not placed**: `ProductsOfCategory(index_category, target_category)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `SliceCategory` {#cat-slicecategory}

The slice category \(C/X\).

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py:223`
- **not placed**: `SliceCategory(base_category, base_object)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `SubobjectCategory` {#cat-subobjectcategory}

The category of represented subobjects of one fixed object.

```text
An object is an object ``A`` of the base category equipped with its chosen
monomorphism ``A.inclusion(): A -> X``.  Morphisms are the commuting
triangles between those inclusions.
```

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py:449`
- **not placed**: `SubobjectCategory(base_category, base_object)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `SubobjectHomset` {#cat-subobjecthomset}

A represented Hom object which is both a Sage Homset and a category.

```text
This is the live counterpart of the archived owned Hom-category base.  It
keeps Sage's hard requirement that every ``Morphism`` be parented by an
actual ``Homset``, while also making that same parent the discrete category
``Hom_C(A,B)``.  Concrete categories subclass this and add enrichment to
the *same object*.
```

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py:413`
- **not placed**: `SubobjectHomset(subobject_category, domain, codomain)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `SuperobjectCategory` {#cat-superobjectcategory}

The category of represented quotient/superobjects of one object.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py:532`
- **not placed**: `SuperobjectCategory(base_category, base_object)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `TensorProductCategory` {#cat-tensorproductcategory}

Objects equipped with a chosen tensor-product universal bilinear map.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/products.py:362`
- **not placed**: `TensorProductCategory(factors)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `WideSubcategory` {#cat-widesubcategory}

A category with the same objects as `C` and a selected class of arrows.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py:545`
- **not placed**: `WideSubcategory(base_category, arrow_category)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

### Functors and adjunctions

#### `Bifunctor` {#fun-bifunctor}

A functor `C x D -> E` with a two-argument convenience API.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/functors.py:89`
- **built by** `Bifunctor(left_domain, right_domain, codomain)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `left_domain()`
- `morphism_image(left_morphism, right_morphism=None)`
- `object_image(left, right=None)`
- `right_domain()`

#### `CodomainFunctor` {#fun-codomainfunctor}

The codomain functor `Arr(C) -> C`.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/functors.py:151`
- **built by** `CodomainFunctor(category)`
- **not resolved here**: parameterized by data the survey does not choose for you

#### `ConstantDiagram` {#fun-constantdiagram}

The constant functor from an index category at one object.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/functors.py:352`
- **built by** `ConstantDiagram(index_category, codomain, value)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `constant_value()`

#### `ContravariantFunctor` {#fun-contravariantfunctor}

A functor `C^op -> D` with convenience calls on arrows of `C`.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/functors.py:42`
- **built by** `ContravariantFunctor(domain, codomain)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `adopt_object_image(preimage, image)`
  - Use a provenance-validated exact image object for ``preimage``.
- `base_domain()`
- `chosen_preimage(image)`
  - Return the unique source object recorded for this exact functor image.
- `morphism_image(morphism)`
- `object_image(obj)`

#### `DiscreteDiagram` {#fun-discretediagram}

A functor from a discrete category, specified on its objects.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/functors.py:332`
- **built by** `DiscreteDiagram(index_category, codomain, values)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `diagram_objects()`

#### `DiscreteFunctor` {#fun-discretefunctor}

A functor between discrete categories induced by a map of object sets.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/functors.py:292`
- **built by** `DiscreteFunctor(domain, codomain, object_map)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `object_map()`

#### `DomainFunctor` {#fun-domainfunctor}

The domain functor `Arr(C) -> C`.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/functors.py:138`
- **built by** `DomainFunctor(category)`
- **not resolved here**: parameterized by data the survey does not choose for you

#### `ObjectSetFunctor` {#fun-objectsetfunctor}

Take the object set of a represented discrete category.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/functors.py:316`
- **acts** Category of discrete categories → Category of sets
- **built by** `ObjectSetFunctor()`

### Objects

#### `CategoryObject` <sub>OBJECT</sub>

A Sage category regarded as an object of `Cat`.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/cat.py:26`
- **built by** `CategoryObject(category_of_categories, represented_category)`

**Operations**

- `category_of_categories()`
- `represented_category()`

### Morphisms and homsets

#### `CategoricalIsomorphism` <sub>MORPHISM</sub>

An isomorphism represented by mutually inverse arrows.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/hom_categories.py:574`
- **built by** `CategoricalIsomorphism(parent, forward, inverse, *, verify=True)`

**Operations**

- `forward()`
- `inverse()`

#### `CategoryFunctorMorphism` <sub>MORPHISM</sub>

A live functor regarded as a morphism in `Cat`.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/cat.py:44`
- **built by** `CategoryFunctorMorphism(parent, functor)`

**Operations**

- `functor()`

#### `CommutativeSquare` <sub>MORPHISM</sub>

A morphism between two arrow objects, i.e. a commuting square.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py:18`
- **built by** `CommutativeSquare(parent, left, right)`

**Operations**

- `components()`
- `left()`
- `right()`

#### `LatticeEmbedding` <sub>MORPHISM</sub>

A form-preserving monomorphism of lattices.

- **defined at** `src/dzack_research/preamble/categories/lattice_morphisms.py:104`
- **built by** `LatticeEmbedding(parent, images, *, verify_injective=True)`

**Operations**

- `discriminant_inclusion()`
  - Return ``A_S -> A_L`` for an orthogonal direct-summand embedding.
- `factor_through(target_embedding)`
  - Factor this lattice embedding through a module embedding when possible.
- `is_injective() -> bool`
  - Return whether ``ker(self)=0`` when the kernel is computable.
- `isotropic_reduction()`
  - Return ``S^perp/S`` for this isotropic embedding ``S -> L``.

#### `LatticeIsometry` <sub>MORPHISM</sub>

An invertible lattice morphism.

- **defined at** `src/dzack_research/preamble/categories/lattice_morphisms.py:300`
- **built by** `LatticeIsometry(parent, images)`

**Operations**

- `centralizer_discriminant_image()` <sub>cached</sub>
  - Return ``rho_L(Z_{O(L)}(self)) <= O(A_L)`` when OSCAR computes it.
- `cyclic_subgroup()`
  - Return the literal subgroup ``<self> <= O(L)``.
- `determinant()`
  - Return the determinant of this automorphism/isometry tensor.
- `discriminant_isometry()` <sub>cached</sub>
  - Return the induced isometry ``Disc(self): A_L -> A_M``.
- `discriminant_morphism()` <sub>cached</sub>
  - Return ``Disc(self)`` parented by ``O(A_L)`` for an automorphism.
- `formed_coinvariants()` <sub>cached</sub>
  - Return ``(L^self)^perp`` as a formed subobject of ``L``.
- `invariant_lattice()` <sub>cached</sub>
  - Return ``ker(self-id)`` as a formed subobject of the lattice.
- `inverse()`
  - Return the inverse isometry.
- `is_surjective() -> bool`
  - Return whether ``coker(self)=0`` when the cokernel is computable.
- `preserves_positive_cone() -> bool`
  - Return whether an isometry preserves a component of the positive cone.
- `real_spinor_norm_sign()` <sub>cached</sub>
  - Return the sign of the real spinor norm in Dawes' convention.

#### `LatticeMorphism` <sub>MORPHISM</sub>

A module morphism preserving the lattice form.

- **defined at** `src/dzack_research/preamble/categories/lattice_morphisms.py:80`
- **built by** `LatticeMorphism(parent, images, *, elementwise=False)`

#### `NaturalTransformationMorphism` <sub>MORPHISM</sub>

A natural transformation as a morphism in a functor category.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/cat.py:300`
- **built by** `NaturalTransformationMorphism(parent, transformation)`

**Operations**

- `component(obj)`
- `naturality_square(morphism)`
- `transformation()`

#### `OppositeMorphism` <sub>MORPHISM</sub>

An arrow of `C^op` represented by the reverse arrow in `C`.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/category_constructions.py:17`
- **built by** `OppositeMorphism(parent, underlying_arrow)`

**Operations**

- `underlying_arrow()`

#### `ProductMorphism` <sub>MORPHISM</sub>

A pair of morphisms in a product category.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/category_constructions.py:130`
- **built by** `ProductMorphism(parent, first, second)`

**Operations**

- `first()`
- `second()`

#### `SubobjectMorphism` <sub>MORPHISM</sub>

The unique commuting-triangle map between two represented subobjects.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py:381`
- **built by** `SubobjectMorphism(parent, factor_morphism)`

**Operations**

- `factor_morphism()`

### Supporting classes

#### `CategoryPacket` <sub>CLASS</sub>

The coordinated `C / Hom_C / End_C / Iso_C / Aut_C` packet.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/hom_categories.py:723`
- **built by** `CategoryPacket(category)`

**Operations**

- `Auts()`
- `C()`
  - SageObject.category(self)
- `Ends()`
- `Epis()`
- `Homs()`
- `Isos()`
- `Monos()`
- `category()`
  - SageObject.category(self)
- `super_packets()`

#### `IsotropicFlag` <sub>CLASS</sub>

A primitive totally isotropic flag, recorded by its nested lattice subobjects.

- **defined at** `src/dzack_research/preamble/categories/isotropic_orbits.py:27`
- **built by** `IsotropicFlag(lattice, basis)`

**Operations**

- `basis()`
- `lattice()`
- `rank()`
- `terms()`
- `top()`

#### `VectorPrimitiveExtension` <sub>CLASS</sub>

Nikulin's primitive extension cut out by one anisotropic primitive vector.

```text
For ``w in L`` this records

``M = Zw ⊥ w^perp -> L``

together with its finite index, the two discriminant inclusions into
``A_M``, the gluing subgroup ``H=L/M <= A_M``, and representatives of
``A_L`` in ``H^perp``.
```

- **defined at** `src/dzack_research/preamble/categories/vector_orbits.py:16`
- **built by** `VectorPrimitiveExtension(lattice, element)`

**Operations**

- `class_of_representative(element)`
  - Return the class of ``A_L`` represented by an element of ``H^perp``.
- `complement_is_definite() -> bool`
  - Return whether the orthogonal complement is definite.
- `representative_of(discriminant_class)`
  - Return the selected representative in ``A_M`` of a class of ``A_L``.

### Functions

#### `Cocone` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/products.py:396`
- **built by** `Cocone(diagram, apex, components)`

#### `Cone` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/products.py:392`
- **built by** `Cone(diagram, apex, components)`

#### `DirectSumDecomposition` <sub>FUNCTION</sub>

Verify the constructor-owned decomposition `underlying_object = ⊕ M_i`.

```text
Direct-sum data is construction data, so this accessor never equips an
already existing parent.  It only verifies that the stated family agrees
with the decomposition selected by that parent's constructor.
```

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/direct_sum_objects.py:86`
- **built by** `DirectSumDecomposition(underlying_object, summands, summand_index_set=None)`

#### `Isomorphism` <sub>FUNCTION</sub>

Return the isomorphism represented by mutually inverse arrows.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py:692`
- **built by** `Isomorphism(forward, inverse)`

#### `NaturalTransformations` <sub>FUNCTION</sub>

Return the represented type of natural transformations between parallel functors.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/functors.py:417`
- **built by** `NaturalTransformations(source, target)`

#### `category_packet` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/hom_categories.py:816`
- **built by** `category_packet(category) -> dzack_research.preamble.categories.abstract_categories.hom_categories.CategoryPacket`

#### `common_category` <sub>FUNCTION</sub>

Return the greatest Sage category common to the stated objects.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/arrow_categories.py:307`
- **built by** `common_category(*objects)`

#### `compose_functors` <sub>FUNCTION</sub>

Return `second ∘ first` in the current functor core.

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/functors.py:372`
- **built by** `compose_functors(second, first)`

#### `coproduct_cocone_category` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/products.py:414`
- **built by** `coproduct_cocone_category(factors, target_category=None)`

#### `definite_complement_extensions` <sub>FUNCTION</sub>

Return every `g in O(L)` carrying `left` to `right` when complements are definite.

```text
This is Dawes' definite-complement route.  An isometry of the two
complements, together with ``left -> right``, defines an isometry
``C:M_left -> M_right`` on the orthogonal sums.  With the finite-index
inclusions ``A_i:M_i -> L``, its rational ambient extension is

``A_right * C * A_left^{-1}``.

Exactly the rational ambient morphisms preserving the integral lattice
belong to ``O(L)``.  Since the complement isometry homset is a finite
torsor in this regime, the returned tuple is exhaustive.
```

- **defined at** `src/dzack_research/preamble/categories/vector_orbits.py:212`
- **built by** `definite_complement_extensions(lattice, left, right)`

#### `diagonal_gram` <sub>FUNCTION</sub>

The diagonal type-$(0,2)$ tensor on `module`.

```text
``exceptions`` is the indexed family of diagonal values that differ
from ``default``.  The Lorentz form on \(R^{\mathbb N}\) is
``diagonal_gram(R^NN, {0: -1}, default=1)``.

EXAMPLES::

    sage: from dzack_research.preamble.categories.lattices import Lattices, diagonal_gram
    sage: G = diagonal_gram(ZZ^NN, {0: -1})
    sage: G
    [-1] ⊕ I_∞ ∈ (ZZ^NN ⊗ ZZ^NN)*
    sage: latex(G)
    [-1]\oplus I_{\infty}
    sage: G.parent()
    (ZZ^NN ⊗ ZZ^NN)*
    sage: Lattices(ZZ)(G)
    Integral lattice of rank +Infinity and signature (+Infinity, 1)
```

- **defined at** `src/dzack_research/preamble/categories/_lattice.py:882`
- **built by** `diagonal_gram(module, exceptions, default=1)`

#### `gluing_route_discriminant_classes` <sub>FUNCTION</sub>

Return the finite discriminant classes compatible with `left -> right`.

```text
For the primitive extensions ``M_i=Zw_i perp w_i^perp`` this enumerates
the full finite-form isometry torsors of the line and complement factors,
retains exactly the assembled maps ``A_{M_1}->A_{M_2}`` carrying
``H_1=L/M_1`` onto ``H_2=L/M_2``, and descends them to
``H_1^perp/H_1 -> H_2^perp/H_2 = A_L``.

These are the admissible classes in ``O(A_L)``.  Lifting such a class to
an actual element of ``O(L)`` is deliberately separate: it is governed by
the image of the discriminant representation and is not assumed here.
```

- **defined at** `src/dzack_research/preamble/categories/vector_orbits.py:347`
- **built by** `gluing_route_discriminant_classes(lattice, left, right)`

#### `product_cone_category` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/abstract_categories/products.py:410`
- **built by** `product_cone_category(factors, target_category=None)`

#### `signature_pair` <sub>FUNCTION</sub>

Return \((p,q)\) as an object of :func:`signature_pairs`.

- **defined at** `src/dzack_research/preamble/categories/_lattice.py:1003`
- **built by** `signature_pair(positive, negative)`

#### `signature_pairs` <sub>FUNCTION</sub>

Return \(\mathbf{Card}\times\mathbf{Card}\), where a signature pair lives.

```text
An index of inertia can be infinite -- \(\mathbb Z^{(\mathbb N)}\) with
its standard form has \((p,q)=(\aleph_0,0)\) -- so each entry is a
cardinal and the pair is an object of the product category.
```

- **defined at** `src/dzack_research/preamble/categories/_lattice.py:992`
- **built by** `signature_pairs()`

## Functors & Adjunctions

> Functorial constructions, Adjunctions, Base change, Free/Forgetful, Cohomology, De Rham, Group actions, and Induction.

### Functors and adjunctions

#### `AbelianGroupInclusionFunctor` {#fun-abeliangroupinclusionfunctor}

The full inclusion `Ab -> Grp`.

- **defined at** `src/dzack_research/preamble/categories/functors/abelianization.py:98`
- **acts** Category of abelian groups → Category of groups
- **built by** `AbelianGroupInclusionFunctor()`

#### `AbelianizationAdjunction` {#fun-abelianizationadjunction}

`(-)^ab ⊣ i`.

- **defined at** `src/dzack_research/preamble/categories/functors/abelianization.py:114`
- **adjunction** Abelianization functor ⊣ Inclusion of abelian groups into groups
- **built by** `AbelianizationAdjunction()`

**Operations**

- `counit(abelian_group)`
- `unit(group)`

#### `AbelianizationFunctor` {#fun-abelianizationfunctor}

`G -> G/[G,G] : Grp -> Ab`.

- **defined at** `src/dzack_research/preamble/categories/functors/abelianization.py:29`
- **acts** Category of groups → Category of abelian groups
- **built by** `AbelianizationFunctor()`

**Operations**

- `quotient_projection(group)`
- `quotient_projection_from_image(abelianization)`

#### `Adjunction` {#fun-adjunction}

An adjunction `F ⊣ U` with its unit, counit, and Hom-set bijection.

- **defined at** `src/dzack_research/preamble/categories/functors/core.py:258`
- **built by** `Adjunction(left_adjoint: dzack_research.preamble.categories.functors.core.Functor, right_adjoint: dzack_research.preamble.categories.functors.core.Functor)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `counit(obj)`
- `counit_transformation() -> dzack_research.preamble.categories.functors.core.NaturalTransformation`
- `hom_set_isomorphism_forward(morphism, source=None)`
  - Transpose ``f:F(A)->B`` to ``U(f) after eta_A``.
- `hom_set_isomorphism_inverse(morphism, codomain=None)`
  - Transpose ``g:A->U(B)`` to ``epsilon_B after F(g)``.
- `left_adjoint() -> dzack_research.preamble.categories.functors.core.Functor`
- `right_adjoint() -> dzack_research.preamble.categories.functors.core.Functor`
- `unit(obj)`
- `unit_transformation() -> dzack_research.preamble.categories.functors.core.NaturalTransformation`

#### `AlgebraBaseChangeAdjunction` {#fun-algebrabasechangeadjunction}

The represented algebra adjunction `S tensor_R - ⊣ Res_f`.

- **defined at** `src/dzack_research/preamble/categories/functors/algebra_scalar_change.py:162`
- **built by** `AlgebraBaseChangeAdjunction(ring_map)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `counit(algebra)`
- `unit(algebra)`

#### `AlgebraRestrictionOfScalarsFunctor` {#fun-algebrarestrictionofscalarsfunctor}

`Res_f : Alg_S -> Alg_R` along `f : R -> S`.

- **defined at** `src/dzack_research/preamble/categories/functors/algebra_scalar_change.py:117`
- **built by** `AlgebraRestrictionOfScalarsFunctor(ring_map)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `ring_map()`

#### `AlgebraScalarExtensionFunctor` {#fun-algebrascalarextensionfunctor}

`S tensor_R - : Alg_R -> Alg_S` along `f : R -> S`.

```text
The functor is mathematical on all algebras.  The live object adapter is
deliberately narrower: it materializes chosen finite polynomial
presentations and refuses to advertise an unavailable general tensor
algebra backend as though it had been constructed.
```

- **defined at** `src/dzack_research/preamble/categories/functors/algebra_scalar_change.py:74`
- **built by** `AlgebraScalarExtensionFunctor(ring_map)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `ring_map()`

#### `AlgebraUnderlyingModuleFunctor` {#fun-algebraunderlyingmodulefunctor}

\(U\colon\mathbf{Alg}_R\to\mathbf{Mod}_R\).

- **defined at** `src/dzack_research/preamble/categories/functors/algebra_modules.py:248`
- **built by** `AlgebraUnderlyingModuleFunctor(base_ring, algebra_category=None)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `base_ring()`

#### `AlternatingAlgebraFunctor` {#fun-alternatingalgebrafunctor}

Exterior-algebra functor on represented modules.

```text
No ordinary free/forgetful adjunction is asserted for this construction.
```

- **defined at** `src/dzack_research/preamble/categories/functors/free_algebras.py:96`
- **built by** `AlternatingAlgebraFunctor(base_ring)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `base_ring()`

#### `BaseChangeAdjunction` {#fun-basechangeadjunction}

`S tensor_R - ⊣ Res_f`.

- **defined at** `src/dzack_research/preamble/categories/functors/scalar_change.py:246`
- **built by** `BaseChangeAdjunction(ring_map)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `counit(module)`
- `unit(module)`

#### `BilinearFreeFormAdjunction` {#fun-bilinearfreeformadjunction}

The tautological bilinear-form classifier adjunction.

- **defined at** `src/dzack_research/preamble/categories/functors/free_forms.py:182`
- **built by** `BilinearFreeFormAdjunction(base_ring)`
- **not resolved here**: parameterized by data the survey does not choose for you

#### `BilinearUnderlyingModuleFunctor` {#fun-bilinearunderlyingmodulefunctor}

Forget the selected form while retaining the module object itself.

- **defined at** `src/dzack_research/preamble/categories/functors/free_forms.py:60`
- **built by** `BilinearUnderlyingModuleFunctor(base_ring)`
- **not resolved here**: parameterized by data the survey does not choose for you

#### `BiproductBifunctor` {#fun-biproductbifunctor}

The direct-sum/biproduct bifunctor on finitely presented modules.

- **defined at** `src/dzack_research/preamble/categories/functors/linear_constructions.py:63`
- **built by** `BiproductBifunctor(base_ring)`
- **not resolved here**: parameterized by data the survey does not choose for you

#### `CardinalityFunctor` {#fun-cardinalityfunctor}

Send a set to its cardinal and a set isomorphism to the unique order arrow.

- **defined at** `src/dzack_research/preamble/categories/functors/cardinality.py:13`
- **acts** Core of Category of sets → Category of cardinalities
- **built by** `CardinalityFunctor()`

#### `CategoryInclusionFunctor` {#fun-categoryinclusionfunctor}

The canonical functor along a declared subcategory inclusion.

```text
If ``C`` is a subcategory of ``D``, every object and morphism of ``C`` is
already an object and morphism of ``D``.  The functor therefore changes
only the category in which the same mathematical data is read.
```

- **defined at** `src/dzack_research/preamble/categories/functors/core.py:156`
- **built by** `CategoryInclusionFunctor(subcategory, supercategory)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `chosen_preimage(image)`
  - Return the unique source object recorded for this exact functor image.

#### `CochainUnderlyingGradedModuleFunctor` {#fun-cochainunderlyinggradedmodulefunctor}

Forget the differential while retaining the same graded module.

- **defined at** `src/dzack_research/preamble/categories/functors/cochain_complexes.py:11`
- **built by** `CochainUnderlyingGradedModuleFunctor(base_ring)`
- **not resolved here**: parameterized by data the survey does not choose for you

#### `CoextensionOfScalarsFunctor` {#fun-coextensionofscalarsfunctor}

`Hom_R(S, -) : Mod_R -> Mod_S` along `f: R -> S`, the right adjoint of `Res_f`.

```text
``S`` acts on ``Hom_R(S, M)`` through its right regular action,
``(s . phi)(t) = phi(t s)``.  The Hom is represented when ``S`` is a
finitely framed ``R``-module; ``Hom_ZZ(ZZ[x], M)`` is a countable product
the module layer does not build, and is refused.
```

- **defined at** `src/dzack_research/preamble/categories/functors/scalar_change.py:147`
- **built by** `CoextensionOfScalarsFunctor(ring_map)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `ring_map()`
- `scalars_as_module()`
  - ``S`` as an ``R``-module, the domain of every ``Hom_R(S, M)``.

#### `CohomologyAlgebraFunctor` {#fun-cohomologyalgebrafunctor}

The graded cohomology-algebra functor `H^*` on strict CDGAs.

- **defined at** `src/dzack_research/preamble/categories/functors/cohomology.py:100`
- **built by** `CohomologyAlgebraFunctor(base_ring)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `base_ring()`

#### `CohomologyFunctor` {#fun-cohomologyfunctor}

The degree-`p` cohomology functor `H^p : Coch_R -> Mod_R`.

- **defined at** `src/dzack_research/preamble/categories/functors/cohomology.py:26`
- **built by** `CohomologyFunctor(base_ring, degree)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `base_ring()`
- `degree()`

#### `CoinductionFunctor` {#fun-coinductionfunctor}

`Coind_H^G : Modules(R[H]) -> Modules(R[G])`, coextension along `R[H] -> R[G]`.

- **defined at** `src/dzack_research/preamble/categories/functors/group_induction.py:298`
- **built by** `CoinductionFunctor(ring_map)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `element_from_values(coinduced, value_function)`
- `identity_representative()`
- `inclusion()`
- `representatives()`
- `subgroup()`
- `supergroup()`
- `value_at(coinduced, vector, representative)`

#### `CoinvariantsFunctor` {#fun-coinvariantsfunctor}

`(-)_G : Modules(R[G]) -> Modules(R)`, scalar extension along the augmentation.

- **defined at** `src/dzack_research/preamble/categories/functors/group_actions.py:135`
- **built by** `CoinvariantsFunctor(ring_map)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `group()`

#### `CoinvariantsTrivialAdjunction` {#fun-coinvariantstrivialadjunction}

`(-)_G ⊣ Triv_G`, base change along the augmentation.

- **defined at** `src/dzack_research/preamble/categories/functors/group_actions.py:193`
- **built by** `CoinvariantsTrivialAdjunction(ring_map)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `counit(module)`
- `unit(group_module)`

#### `CokernelArrowFunctor` {#fun-cokernelarrowfunctor}

The cokernel functor from the finite-free module arrow category.

- **defined at** `src/dzack_research/preamble/categories/functors/linear_constructions.py:115`
- **built by** `CokernelArrowFunctor(base_ring)`
- **not resolved here**: parameterized by data the survey does not choose for you

#### `ComposedFunctor` {#fun-composedfunctor}

The composite `second ∘ first`.

- **defined at** `src/dzack_research/preamble/categories/functors/core.py:191`
- **built by** `ComposedFunctor(first: dzack_research.preamble.categories.functors.core.Functor, second: dzack_research.preamble.categories.functors.core.Functor)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `adopt_object_image(preimage, image)`
  - Use a provenance-validated exact image object for ``preimage``.
- `chosen_preimage(image)`
  - Return the unique source object recorded for this exact functor image.
- `factors()`
- `is_faithful() -> bool`

#### `CompositeAdjunction` {#fun-compositeadjunction}

The composite of `F ⊣ U` and `G ⊣ V` as `GF ⊣ UV`.

- **defined at** `src/dzack_research/preamble/categories/functors/core.py:310`
- **built by** `CompositeAdjunction(first: dzack_research.preamble.categories.functors.core.Adjunction, second: dzack_research.preamble.categories.functors.core.Adjunction)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `counit(obj)`
- `first() -> dzack_research.preamble.categories.functors.core.Adjunction`
- `second() -> dzack_research.preamble.categories.functors.core.Adjunction`
- `unit(obj)`

#### `CompositeFunctor` {#fun-compositefunctor}

The composite `second ∘ first`.

- **defined at** `src/dzack_research/preamble/categories/functors/core.py:191`
- **built by** `CompositeFunctor(first: dzack_research.preamble.categories.functors.core.Functor, second: dzack_research.preamble.categories.functors.core.Functor)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `adopt_object_image(preimage, image)`
  - Use a provenance-validated exact image object for ``preimage``.
- `chosen_preimage(image)`
  - Return the unique source object recorded for this exact functor image.
- `factors()`
- `is_faithful() -> bool`

#### `DeRhamAdjunction` {#fun-derhamadjunction}

The adjunction `DR_R ⊣ (-)^0`.

```text
On the represented algebras the Hom-set bijection is the universal
extension of an algebra map ``A -> B^0`` by ``da |-> d_B(a)``.
```

- **defined at** `src/dzack_research/preamble/categories/functors/de_rham.py:137`
- **built by** `DeRhamAdjunction(base_ring)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `base_ring()`
- `counit(dga)`
- `unit(algebra)`

#### `DeRhamCohomologyAlgebraFunctor` {#fun-derhamcohomologyalgebrafunctor}

The composite `H^* ∘ DR_R`.

- **defined at** `src/dzack_research/preamble/categories/functors/cohomology.py:129`
- **built by** `DeRhamCohomologyAlgebraFunctor(base_ring)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `base_ring()`

#### `DeRhamCohomologyFunctor` {#fun-derhamcohomologyfunctor}

The literal composite `H^p ∘ U_Coch ∘ DR_R`.

- **defined at** `src/dzack_research/preamble/categories/functors/cohomology.py:72`
- **built by** `DeRhamCohomologyFunctor(base_ring, degree)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `base_ring()`
- `degree()`

#### `DeRhamFunctor` {#fun-derhamfunctor}

`DR_R : CAlg_R -> SCDGA_R^{>=0}` on represented affine algebras.

- **defined at** `src/dzack_research/preamble/categories/functors/de_rham.py:71`
- **built by** `DeRhamFunctor(base_ring)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `base_ring()`

#### `DegreeZeroDGAFunctor` {#fun-degreezerodgafunctor}

Degree zero `(-)^0 : SCDGA_R^{>=0} -> CAlg_R`.

- **defined at** `src/dzack_research/preamble/categories/functors/de_rham.py:96`
- **built by** `DegreeZeroDGAFunctor(base_ring)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `base_ring()`

#### `DirectImageSubobjectFunctor` {#fun-directimagesubobjectfunctor}

The monotone map `f_* : Sub(M) -> Sub(N)`.

- **defined at** `src/dzack_research/preamble/categories/functors/subobject_images.py:19`
- **built by** `DirectImageSubobjectFunctor(morphism)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `morphism()`

#### `DualizationFunctor` {#fun-dualizationfunctor}

Finite-free duality `(-)^* : C^op -> C`.

- **defined at** `src/dzack_research/preamble/categories/functors/linear_constructions.py:23`
- **built by** `DualizationFunctor(base_ring)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `double_dual_morphism(module)`
  - Return the canonical finite-free biduality map ``M -> M**``.

#### `ExponentialFunctor` {#fun-exponentialfunctor}

The internal-Hom functor `Set^op x Set -> Set`.

- **defined at** `src/dzack_research/preamble/categories/functors/set_constructions.py:26`
- **acts** Product of Opposite of Category of sets and Category of sets → Category of sets
- **built by** `ExponentialFunctor()`

**Operations**

- `morphism(precompose, postcompose)`
  - Return the product-category morphism induced by ``precompose`` and ``postcompose``.
- `opposite_sets()`
- `pair(exponent, codomain)`

#### `FinitePowerSetFunctor` {#fun-finitepowersetfunctor}

The covariant finite-power-set functor under direct image.

- **defined at** `src/dzack_research/preamble/categories/functors/set_constructions.py:87`
- **acts** Category of sets → Category of sets
- **built by** `FinitePowerSetFunctor()`

#### `FixedCardinalitySubsetFunctor` {#fun-fixedcardinalitysubsetfunctor}

Direct image on `k`-element subsets, defined on injective set maps.

- **defined at** `src/dzack_research/preamble/categories/functors/set_constructions.py:105`
- **built by** `FixedCardinalitySubsetFunctor(subset_cardinality)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `subset_cardinality()`

#### `FractionFieldFunctor` {#fun-fractionfieldfunctor}

`Frac : Orders -> NumberFields`.

- **defined at** `src/dzack_research/preamble/categories/functors/orders_number_fields.py:26`
- **acts** Category of owned orders → Category of number fields
- **built by** `FractionFieldFunctor()`

#### `FreeBilinearFormFunctor` {#fun-freebilinearformfunctor}

Send `M` to `(M, M tensor M, universal pure tensor)`.

- **defined at** `src/dzack_research/preamble/categories/functors/free_forms.py:78`
- **built by** `FreeBilinearFormFunctor(base_ring)`
- **not resolved here**: parameterized by data the survey does not choose for you

#### `FreeForgetfulAdjunction` {#fun-freeforgetfuladjunction}

`F_R ⊣ U` between sets and `R`-modules.

- **defined at** `src/dzack_research/preamble/categories/functors/free_forgetful.py:58`
- **built by** `FreeForgetfulAdjunction(base_ring)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `counit(module)`
- `unit(set_object)`

#### `FreeGroupFunctor` {#fun-freegroupfunctor}

`F : Set -> Grp`.

- **defined at** `src/dzack_research/preamble/categories/functors/free_groups.py:21`
- **acts** Category of sets → Category of groups
- **built by** `FreeGroupFunctor()`

#### `FreeGroupUnderlyingSetAdjunction` {#fun-freegroupunderlyingsetadjunction}

The adjunction `F : Set <-> Grp : U`.

- **defined at** `src/dzack_research/preamble/categories/functors/free_groups.py:65`
- **adjunction** Free-group functor ⊣ Underlying-set functor on groups
- **built by** `FreeGroupUnderlyingSetAdjunction()`

**Operations**

- `counit(group)`
- `unit(set_object)`

#### `FreeModuleFunctor` {#fun-freemodulefunctor}

`F_R : Set -> Mod_R`.

- **defined at** `src/dzack_research/preamble/categories/functors/free_forgetful.py:14`
- **built by** `FreeModuleFunctor(base_ring)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `base_ring()`

#### `FreeQuadraticFormFunctor` {#fun-freequadraticformfunctor}

Send `M` to `(M, Gamma^2(M), gamma_2)`.

- **defined at** `src/dzack_research/preamble/categories/functors/free_forms.py:116`
- **built by** `FreeQuadraticFormFunctor(base_ring)`
- **not resolved here**: parameterized by data the survey does not choose for you

#### `Functor` {#fun-functor}

A functor with explicit actions on objects and morphisms.

- **defined at** `src/dzack_research/preamble/categories/functors/core.py:13`
- **built by** `Functor(domain, codomain)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `adopt_object_image(preimage, image)`
  - Use a provenance-validated exact image object for ``preimage``.
- `chosen_preimage(image)`
  - Return the unique source object recorded for this exact functor image.
- `codomain()`
- `domain()`
- `factors()`
- `is_faithful() -> bool`
- `morphism_image(morphism)`
- `object_image(obj)`
- `on_morphism(morphism)`
- `on_object(obj)`
- `then(other)`
  - Return ``other ∘ self``.

#### `GroupModuleBaseChangeAdjunction` {#fun-groupmodulebasechangeadjunction}

`S tensor_R - ⊣ Res_f` on modules carrying a fixed `G`-action.

- **defined at** `src/dzack_research/preamble/categories/functors/group_scalar_change.py:176`
- **built by** `GroupModuleBaseChangeAdjunction(ring_map, group)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `counit(group_module)`
- `unit(group_module)`

#### `GroupModuleRestrictionOfScalarsFunctor` {#fun-groupmodulerestrictionofscalarsfunctor}

`Res_f : S[G]-Mod -> R[G]-Mod`.

- **defined at** `src/dzack_research/preamble/categories/functors/group_scalar_change.py:106`
- **built by** `GroupModuleRestrictionOfScalarsFunctor(ring_map, group)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `group()`
- `ring_map()`

#### `GroupModuleScalarExtensionFunctor` {#fun-groupmodulescalarextensionfunctor}

`S tensor_R - : R[G]-Mod -> S[G]-Mod` along one scalar map.

- **defined at** `src/dzack_research/preamble/categories/functors/group_scalar_change.py:55`
- **built by** `GroupModuleScalarExtensionFunctor(ring_map, group)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `group()`
- `ring_map()`

#### `GroupUnderlyingSetFunctor` {#fun-groupunderlyingsetfunctor}

`U : Grp -> Set`.

- **defined at** `src/dzack_research/preamble/categories/functors/free_groups.py:44`
- **acts** Category of groups → Category of sets
- **built by** `GroupUnderlyingSetFunctor()`

#### `IdentityFunctor` {#fun-identityfunctor}

A functor with explicit actions on objects and morphisms.

- **defined at** `src/dzack_research/preamble/categories/functors/core.py:131`
- **built by** `IdentityFunctor(category)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `chosen_preimage(image)`
  - Return the unique source object recorded for this exact functor image.
- `factors()`
- `is_faithful() -> bool`

#### `InducedAutFunctor` {#fun-inducedautfunctor}

The functor `Aut_C(A) -> Aut_D(F(A))` induced by `F`.

- **defined at** `src/dzack_research/preamble/categories/functors/hom_packets.py:108`
- **built by** `InducedAutFunctor(functor, obj)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `base_functor()`
- `morphism_image(morphism)`
- `object_image(arrow_object)`

#### `InducedEndFunctor` {#fun-inducedendfunctor}

The functor `End_C(A) -> End_D(F(A))` induced by `F`.

- **defined at** `src/dzack_research/preamble/categories/functors/hom_packets.py:69`
- **built by** `InducedEndFunctor(functor, obj)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `base_functor()`
- `morphism_image(morphism)`
- `object_image(arrow_object)`

#### `InducedHomFunctor` {#fun-inducedhomfunctor}

The functor `Hom_C(A,B) -> Hom_D(F(A),F(B))` induced by `F`.

- **defined at** `src/dzack_research/preamble/categories/functors/hom_packets.py:15`
- **built by** `InducedHomFunctor(functor, domain_object, codomain_object)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `base_functor()`
- `morphism_image(morphism)`
- `object_image(arrow_object)`

#### `InductionFunctor` {#fun-inductionfunctor}

`Ind_H^G : Modules(R[H]) -> Modules(R[G])`, scalar extension along `R[H] -> R[G]`.

- **defined at** `src/dzack_research/preamble/categories/functors/group_induction.py:197`
- **built by** `InductionFunctor(ring_map)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `identity_representative()`
- `inclusion()`
- `representatives()`
- `subgroup()`
- `supergroup()`

#### `InductionRestrictionAdjunction` {#fun-inductionrestrictionadjunction}

`Ind_H^G ⊣ Res_H^G`, the base-change adjunction along `R[H] -> R[G]`.

- **defined at** `src/dzack_research/preamble/categories/functors/group_induction.py:438`
- **built by** `InductionRestrictionAdjunction(ring_map)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `counit(group_module)`
- `unit(group_module)`

#### `InternalHomFromFunctor` {#fun-internalhomfromfunctor}

The endofunctor `Hom_R(M,-)` represented by internal Hom modules.

- **defined at** `src/dzack_research/preamble/categories/functors/tensor_hom.py:52`
- **built by** `InternalHomFromFunctor(fixed_source)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `fixed_source()`

#### `InvariantsFunctor` {#fun-invariantsfunctor}

`(-)^G : Modules(R[G]) -> Modules(R)`, coextension along the augmentation.

- **defined at** `src/dzack_research/preamble/categories/functors/group_actions.py:100`
- **built by** `InvariantsFunctor(ring_map)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `group()`

#### `InverseImagePowerSetFunctor` {#fun-inverseimagepowersetfunctor}

The contravariant power-set functor on the opposite of Set.

- **defined at** `src/dzack_research/preamble/categories/functors/set_constructions.py:63`
- **acts** Opposite of Category of sets → Category of sets
- **built by** `InverseImagePowerSetFunctor()`

**Operations**

- `opposite_morphism(morphism)`
- `opposite_sets()`

#### `InverseImageSubobjectFunctor` {#fun-inverseimagesubobjectfunctor}

The monotone map `f^{-1} : Sub(N) -> Sub(M)`.

- **defined at** `src/dzack_research/preamble/categories/functors/subobject_images.py:39`
- **built by** `InverseImageSubobjectFunctor(morphism)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `morphism()`

#### `KernelArrowFunctor` {#fun-kernelarrowfunctor}

The kernel functor from the finite-free module arrow category.

- **defined at** `src/dzack_research/preamble/categories/functors/linear_constructions.py:89`
- **built by** `KernelArrowFunctor(base_ring)`
- **not resolved here**: parameterized by data the survey does not choose for you

#### `ModuleLocalizationFunctor` {#fun-modulelocalizationfunctor}

The functor `S^{-1}R tensor_R - : Mod_R -> Mod_{S^{-1}R}`.

- **defined at** `src/dzack_research/preamble/categories/functors/module_localization.py:25`
- **built by** `ModuleLocalizationFunctor(localization_ring)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `cokernel_comparison(morphism)`
  - Return ``S^{-1}coker(f) ~= coker(S^{-1}f)`` in represented regimes.
- `is_exact() -> bool`
  - Localization of modules is exact.
- `kernel_comparison(morphism)`
  - Return ``S^{-1}ker(f) ~= ker(S^{-1}f)``.
- `localization_ring()`
- `localization_submonoid()`
- `unit(module, *, localized=None)`
  - Return ``M -> Res_R(S^{-1}M)``, the localization unit.

#### `OrderNumberFieldAdjunction` {#fun-ordernumberfieldadjunction}

`Frac ⊣ O`.

- **defined at** `src/dzack_research/preamble/categories/functors/orders_number_fields.py:64`
- **adjunction** Fraction-field functor ⊣ Ring-of-integers functor
- **built by** `OrderNumberFieldAdjunction()`

**Operations**

- `counit(field)`
- `unit(order)`

#### `OrthogonalDirectSumBifunctor` {#fun-orthogonaldirectsumbifunctor}

The orthogonal-direct-sum bifunctor on finite-rank lattices.

- **defined at** `src/dzack_research/preamble/categories/functors/linear_constructions.py:142`
- **built by** `OrthogonalDirectSumBifunctor(base_ring)`
- **not resolved here**: parameterized by data the survey does not choose for you

#### `QuadraticFreeFormAdjunction` {#fun-quadraticfreeformadjunction}

The divided-square quadratic-form classifier adjunction.

- **defined at** `src/dzack_research/preamble/categories/functors/free_forms.py:210`
- **built by** `QuadraticFreeFormAdjunction(base_ring)`
- **not resolved here**: parameterized by data the survey does not choose for you

#### `QuadraticUnderlyingModuleFunctor` {#fun-quadraticunderlyingmodulefunctor}

Forget the selected form while retaining the module object itself.

- **defined at** `src/dzack_research/preamble/categories/functors/free_forms.py:69`
- **built by** `QuadraticUnderlyingModuleFunctor(base_ring)`
- **not resolved here**: parameterized by data the survey does not choose for you

#### `RestrictionCoextensionAdjunction` {#fun-restrictioncoextensionadjunction}

`Res_f ⊣ Hom_R(S, -)`.

```text
The unit sends ``n`` to ``s |-> s n`` and the counit evaluates at ``1``.
```

- **defined at** `src/dzack_research/preamble/categories/functors/scalar_change.py:282`
- **built by** `RestrictionCoextensionAdjunction(ring_map)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `counit(module)`
- `unit(module)`

#### `RestrictionCoinductionAdjunction` {#fun-restrictioncoinductionadjunction}

`Res_H^G ⊣ Coind_H^G`, the restriction/coextension adjunction along `R[H] -> R[G]`.

- **defined at** `src/dzack_research/preamble/categories/functors/group_induction.py:473`
- **built by** `RestrictionCoinductionAdjunction(ring_map)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `counit(group_module)`
- `unit(group_module)`

#### `RestrictionOfActingGroupFunctor` {#fun-restrictionofactinggroupfunctor}

`Res_H^G : Modules(R[G]) -> Modules(R[H])`, restriction along `R[H] -> R[G]`.

- **defined at** `src/dzack_research/preamble/categories/functors/group_induction.py:153`
- **built by** `RestrictionOfActingGroupFunctor(ring_map)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `inclusion()`
- `subgroup()`
- `supergroup()`

#### `RestrictionOfScalarsFunctor` {#fun-restrictionofscalarsfunctor}

`Res_f : Mod_S -> Mod_R` along `f:R -> S`.

- **defined at** `src/dzack_research/preamble/categories/functors/scalar_change.py:91`
- **built by** `RestrictionOfScalarsFunctor(ring_map)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `ring_map()`

#### `RingOfIntegersFunctor` {#fun-ringofintegersfunctor}

`K -> O_K : NumberFields -> Orders`.

- **defined at** `src/dzack_research/preamble/categories/functors/orders_number_fields.py:46`
- **acts** Category of number fields → Category of owned orders
- **built by** `RingOfIntegersFunctor()`

#### `ScalarExtensionFunctor` {#fun-scalarextensionfunctor}

`S tensor_R - : Mod_R -> Mod_S` along `f:R -> S`.

```text
The mathematical functor is defined on every module.  The live computation
presently materializes the represented framed/free/presented cases for
which the module layer has an exact constructor.
```

- **defined at** `src/dzack_research/preamble/categories/functors/scalar_change.py:38`
- **built by** `ScalarExtensionFunctor(ring_map)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `ring_map()`

#### `SubobjectImageAdjunction` {#fun-subobjectimageadjunction}

The Galois connection `f_* ⊣ f^{-1}` on fixed-ambient subobjects.

- **defined at** `src/dzack_research/preamble/categories/functors/subobject_images.py:59`
- **built by** `SubobjectImageAdjunction(morphism)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `counit(subobject)`
- `unit(subobject)`

#### `SymmetricAlgebraAdjunction` {#fun-symmetricalgebraadjunction}

The adjunction \(\operatorname{Sym}_R\dashv U\) for commutative algebras.

- **defined at** `src/dzack_research/preamble/categories/functors/free_algebras.py:214`
- **built by** `SymmetricAlgebraAdjunction(base_ring)`
- **not resolved here**: parameterized by data the survey does not choose for you

#### `SymmetricAlgebraFunctor` {#fun-symmetricalgebrafunctor}

The functor \(\operatorname{Sym}_R:\mathbf{Mod}_R\to\mathbf{CAlg}_R\).

- **defined at** `src/dzack_research/preamble/categories/functors/free_algebras.py:88`
- **built by** `SymmetricAlgebraFunctor(base_ring)`
- **not resolved here**: parameterized by data the survey does not choose for you

#### `TensorAlgebraAdjunction` {#fun-tensoralgebraadjunction}

The adjunction \(T_R\dashv U:\mathbf{Mod}_R\leftrightarrows\mathbf{Alg}_R\).

- **defined at** `src/dzack_research/preamble/categories/functors/free_algebras.py:207`
- **built by** `TensorAlgebraAdjunction(base_ring)`
- **not resolved here**: parameterized by data the survey does not choose for you

#### `TensorAlgebraFunctor` {#fun-tensoralgebrafunctor}

The functor \(T_R:\mathbf{Mod}_R\to\mathbf{Alg}_R\).

- **defined at** `src/dzack_research/preamble/categories/functors/free_algebras.py:80`
- **built by** `TensorAlgebraFunctor(base_ring)`
- **not resolved here**: parameterized by data the survey does not choose for you

#### `TensorByFunctor` {#fun-tensorbyfunctor}

The endofunctor `- tensor_R M` on chosen finite presentations.

- **defined at** `src/dzack_research/preamble/categories/functors/tensor_hom.py:20`
- **built by** `TensorByFunctor(fixed_module)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `fixed_module()`

#### `TensorHomAdjunction` {#fun-tensorhomadjunction}

The adjunction `- tensor_R M ⊣ Hom_R(M,-)`.

- **defined at** `src/dzack_research/preamble/categories/functors/tensor_hom.py:84`
- **built by** `TensorHomAdjunction(fixed_module)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `counit(module)`
- `fixed_module()`
- `unit(module)`

#### `TrivialActionFunctor` {#fun-trivialactionfunctor}

`Triv_G : Modules(R) -> Modules(R[G])`, restriction along the augmentation.

- **defined at** `src/dzack_research/preamble/categories/functors/group_actions.py:74`
- **built by** `TrivialActionFunctor(ring_map)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `group()`

#### `TrivialInvariantsAdjunction` {#fun-trivialinvariantsadjunction}

`Triv_G ⊣ (-)^G`, restriction/coextension along the augmentation.

- **defined at** `src/dzack_research/preamble/categories/functors/group_actions.py:166`
- **built by** `TrivialInvariantsAdjunction(ring_map)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `counit(group_module)`
- `unit(module)`

#### `UnderlyingSetFunctor` {#fun-underlyingsetfunctor}

`U : Mod_R -> Set`; a module is already a set object.

- **defined at** `src/dzack_research/preamble/categories/functors/free_forgetful.py:38`
- **built by** `UnderlyingSetFunctor(base_ring)`
- **not resolved here**: parameterized by data the survey does not choose for you

### Supporting classes

#### `NaturalTransformation` <sub>CLASS</sub>

A natural transformation `source => target` given by its components.

- **defined at** `src/dzack_research/preamble/categories/functors/core.py:227`
- **built by** `NaturalTransformation(source: dzack_research.preamble.categories.functors.core.Functor, target: dzack_research.preamble.categories.functors.core.Functor, component)`

**Operations**

- `component(obj)`
- `naturality_square(morphism)`
  - Return the two composites that naturality asserts are equal.
- `source() -> dzack_research.preamble.categories.functors.core.Functor`
- `target() -> dzack_research.preamble.categories.functors.core.Functor`

### Functions

#### `abelianization_adjunction` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/abelianization.py:150`
- **built by** `abelianization_adjunction() -> dzack_research.preamble.categories.functors.abelianization.AbelianizationAdjunction`

#### `algebra_base_change_adjunction` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/algebra_scalar_change.py:191`
- **built by** `algebra_base_change_adjunction(ring_map) -> dzack_research.preamble.categories.functors.algebra_scalar_change.AlgebraBaseChangeAdjunction`

#### `algebra_underlying_module_functor` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/algebra_modules.py:296`
- **built by** `algebra_underlying_module_functor(base_ring, algebra_category=None) -> dzack_research.preamble.categories.functors.algebra_modules.AlgebraUnderlyingModuleFunctor`

#### `alternating_algebra_functor` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/free_algebras.py:221`
- **built by** `alternating_algebra_functor(base_ring) -> dzack_research.preamble.categories.functors.free_algebras.AlternatingAlgebraFunctor`

#### `base_change_adjunction` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/scalar_change.py:335`
- **built by** `base_change_adjunction(ring_map) -> dzack_research.preamble.categories.functors.scalar_change.BaseChangeAdjunction`

#### `bilinear_free_form_adjunction` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/free_forms.py:236`
- **built by** `bilinear_free_form_adjunction(base_ring) -> dzack_research.preamble.categories.functors.free_forms.BilinearFreeFormAdjunction`

#### `cardinality_functor` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/cardinality.py:33`
- **built by** `cardinality_functor() -> dzack_research.preamble.categories.functors.cardinality.CardinalityFunctor`

#### `category_inclusion` <sub>FUNCTION</sub>

Return the canonical functor attached to `subcategory <= supercategory`.

- **defined at** `src/dzack_research/preamble/categories/functors/core.py:186`
- **built by** `category_inclusion(subcategory, supercategory) -> dzack_research.preamble.categories.functors.core.CategoryInclusionFunctor`

#### `cochain_underlying_graded_module_functor` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/cochain_complexes.py:25`
- **built by** `cochain_underlying_graded_module_functor(base_ring)`

#### `cohomology_algebra_functor` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/cohomology.py:157`
- **built by** `cohomology_algebra_functor(base_ring) -> dzack_research.preamble.categories.functors.cohomology.CohomologyAlgebraFunctor`

#### `cohomology_functor` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/cohomology.py:147`
- **built by** `cohomology_functor(base_ring, degree) -> dzack_research.preamble.categories.functors.cohomology.CohomologyFunctor`

#### `compose_adjunctions` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/core.py:340`
- **built by** `compose_adjunctions(first: dzack_research.preamble.categories.functors.core.Adjunction, second: dzack_research.preamble.categories.functors.core.Adjunction) -> dzack_research.preamble.categories.functors.core.CompositeAdjunction`

#### `de_rham_adjunction` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/de_rham.py:178`
- **built by** `de_rham_adjunction(base_ring) -> dzack_research.preamble.categories.functors.de_rham.DeRhamAdjunction`

#### `de_rham_cohomology_algebra_functor` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/cohomology.py:162`
- **built by** `de_rham_cohomology_algebra_functor(base_ring) -> dzack_research.preamble.categories.functors.cohomology.DeRhamCohomologyAlgebraFunctor`

#### `de_rham_cohomology_functor` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/cohomology.py:152`
- **built by** `de_rham_cohomology_functor(base_ring, degree) -> dzack_research.preamble.categories.functors.cohomology.DeRhamCohomologyFunctor`

#### `de_rham_functor` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/de_rham.py:168`
- **built by** `de_rham_functor(base_ring) -> dzack_research.preamble.categories.functors.de_rham.DeRhamFunctor`

#### `degree_zero_dga_functor` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/de_rham.py:173`
- **built by** `degree_zero_dga_functor(base_ring) -> dzack_research.preamble.categories.functors.de_rham.DegreeZeroDGAFunctor`

#### `exponential_functor` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/set_constructions.py:134`
- **built by** `exponential_functor() -> dzack_research.preamble.categories.functors.set_constructions.ExponentialFunctor`

#### `finite_power_set_functor` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/set_constructions.py:144`
- **built by** `finite_power_set_functor() -> dzack_research.preamble.categories.functors.set_constructions.FinitePowerSetFunctor`

#### `fixed_cardinality_subset_functor` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/set_constructions.py:149`
- **built by** `fixed_cardinality_subset_functor(subset_cardinality) -> dzack_research.preamble.categories.functors.set_constructions.FixedCardinalitySubsetFunctor`

#### `free_forgetful_adjunction` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/free_forgetful.py:84`
- **built by** `free_forgetful_adjunction(base_ring) -> dzack_research.preamble.categories.functors.free_forgetful.FreeForgetfulAdjunction`

#### `free_group_underlying_set_adjunction` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/free_groups.py:86`
- **built by** `free_group_underlying_set_adjunction() -> dzack_research.preamble.categories.functors.free_groups.FreeGroupUnderlyingSetAdjunction`

#### `group_module_base_change_adjunction` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/group_scalar_change.py:238`
- **built by** `group_module_base_change_adjunction(ring_map, group) -> dzack_research.preamble.categories.functors.group_scalar_change.GroupModuleBaseChangeAdjunction`

#### `induced_aut_functor` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/hom_packets.py:158`
- **built by** `induced_aut_functor(functor, obj) -> dzack_research.preamble.categories.functors.hom_packets.InducedAutFunctor`

#### `induced_end_functor` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/hom_packets.py:154`
- **built by** `induced_end_functor(functor, obj) -> dzack_research.preamble.categories.functors.hom_packets.InducedEndFunctor`

#### `induced_hom_functor` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/hom_packets.py:150`
- **built by** `induced_hom_functor(functor, domain_object, codomain_object) -> dzack_research.preamble.categories.functors.hom_packets.InducedHomFunctor`

#### `inverse_image_power_set_functor` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/set_constructions.py:139`
- **built by** `inverse_image_power_set_functor() -> dzack_research.preamble.categories.functors.set_constructions.InverseImagePowerSetFunctor`

#### `module_localization_functor` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/module_localization.py:314`
- **built by** `module_localization_functor(localization_ring)`

#### `order_number_field_adjunction` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/orders_number_fields.py:97`
- **built by** `order_number_field_adjunction() -> dzack_research.preamble.categories.functors.orders_number_fields.OrderNumberFieldAdjunction`

#### `quadratic_free_form_adjunction` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/free_forms.py:241`
- **built by** `quadratic_free_form_adjunction(base_ring) -> dzack_research.preamble.categories.functors.free_forms.QuadraticFreeFormAdjunction`

#### `restriction_coextension_adjunction` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/scalar_change.py:340`
- **built by** `restriction_coextension_adjunction(ring_map) -> dzack_research.preamble.categories.functors.scalar_change.RestrictionCoextensionAdjunction`

#### `subobject_image_adjunction` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/subobject_images.py:79`
- **built by** `subobject_image_adjunction(morphism) -> dzack_research.preamble.categories.functors.subobject_images.SubobjectImageAdjunction`

#### `symmetric_algebra_adjunction` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/free_algebras.py:236`
- **built by** `symmetric_algebra_adjunction(base_ring) -> dzack_research.preamble.categories.functors.free_algebras.SymmetricAlgebraAdjunction`

#### `symmetric_algebra_functor` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/free_algebras.py:154`
- **built by** `symmetric_algebra_functor(base_ring) -> dzack_research.preamble.categories.functors.free_algebras.SymmetricAlgebraFunctor`

#### `tensor_algebra_adjunction` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/free_algebras.py:231`
- **built by** `tensor_algebra_adjunction(base_ring) -> dzack_research.preamble.categories.functors.free_algebras.TensorAlgebraAdjunction`

#### `tensor_algebra_functor` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/free_algebras.py:149`
- **built by** `tensor_algebra_functor(base_ring) -> dzack_research.preamble.categories.functors.free_algebras.TensorAlgebraFunctor`

#### `tensor_hom_adjunction` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/functors/tensor_hom.py:127`
- **built by** `tensor_hom_adjunction(fixed_module) -> dzack_research.preamble.categories.functors.tensor_hom.TensorHomAdjunction`

## Lattices, Quadratic Forms & Invariants

> Free modules with quadratic forms, Genus, Definite/Root/Rational lattices, Isometries, Embeddings, Orbits, and Diagrams.

```mermaid
graph RL
  EvenLattices["EvenLattices(R)"]
  FiniteRankLattices["FiniteRankLattices(R)"]
  Lattices["Lattices(R)"]
  NondegenerateLattices["NondegenerateLattices(R)"]
  RootLattices["RootLattices"]
  FinitelyGeneratedFreeModules("FinitelyGeneratedFreeModules(R)")
  FramedFreeModules("FramedFreeModules(R)")
  SymmetricBilinearFormModules("SymmetricBilinearFormModules(R)")
  EvenLattices --> Lattices
  FiniteRankLattices --> FinitelyGeneratedFreeModules
  FiniteRankLattices --> Lattices
  Lattices --> FramedFreeModules
  Lattices --> SymmetricBilinearFormModules
  NondegenerateLattices --> Lattices
  RootLattices --> EvenLattices
  RootLattices --> FiniteRankLattices
  RootLattices --> NondegenerateLattices
  classDef outside stroke-dasharray:6 4,fill:#f8fafc;
  class FinitelyGeneratedFreeModules,FramedFreeModules,SymmetricBilinearFormModules outside;
```

### Categories

Ordered by depth: the least structured first.

#### `Lattices(R)` {#cat-lattices}

The category of lattices over a base ring, and the constructor for its objects.

```text
Sage's ``IntegralLattice`` factory constructs finite nondegenerate
integral forms but does not provide the mathematical category used here.
``Lattices(R)`` owns the broader category of free `R`-modules with an
`R`-valued symmetric form; finite rank and nondegeneracy are refinements,
not hidden constructor assumptions.      Named descriptors (``U``, a finite
simply-laced Cartan type, a Euclidean rank) are owned Gram tensors.

Sage's meet/join lattices are :class:`LatticePosets`, a different
mathematical object.

EXAMPLES::

    sage: from dzack_research.preamble.categories.lattices import Lattices
    sage: Lattices(ZZ)
    Lattices(ZZ)
    sage: Lattices(ZZ).super_categories()
    [Category of framed free modules]

    sage: C = Lattices(ZZ)
    sage: L = C("U")
    sage: L
    Integral lattice of rank 2 and signature (1, 1)
    sage: L in C
    True
    sage: C("A2")
    Integral lattice of rank 2 and signature (0, 2)
    sage: latex(L)
    \begin{gathered}
    L \in \mathrm{Lattices}(\mathbb{Z}), \quad \mathrm{rk}(L) = 2, \quad \mathrm{sig}(L) = (1, 1), \quad \mathrm{disc}(L) = 1 \\
    L = U \\
    G_L = \left(\begin{array}{rr}
    \cdot & 1 \\
    1 & \cdot
    \end{array}\right) \\
    \end{gathered}
    sage: latex(Lattices(ZZ))
    \mathrm{Lattices}(\mathbb{Z}) \in \mathrm{Cat}
```

- **defined at** `src/dzack_research/preamble/categories/lattices.py:535`
- **probed as** `Lattices(ZZ)`
- **above** [`FramedFreeModules(R)`](#cat-framedfreemodules), [`SymmetricBilinearFormModules(R)`](#cat-symmetricbilinearformmodules)
- **below** [`EvenLattices(R)`](#cat-evenlattices), [`FiniteRankLattices(R)`](#cat-finiteranklattices), [`NondegenerateLattices(R)`](#cat-nondegeneratelattices)
- **refines**, transitively, in Sage's linearization order: [`SymmetricBilinearFormModules(R)`](#cat-symmetricbilinearformmodules) · [`FramedFreeModules(R)`](#cat-framedfreemodules) · [`BilinearFormModules(R)`](#cat-bilinearformmodules) · [`FormModules(R)`](#cat-formmodules) · [`FramedModules(R)`](#cat-framedmodules) · [`FreeModules(R)`](#cat-freemodules) · [`ProjectiveModules(R)`](#cat-projectivemodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `Lattices(R)(data: object, *args: object, **options: object) -> 'Lattices.ParentMethods'`

**Operations introduced here** (123 on objects, 11 on elements)

*on objects*

- `ElementType()`
  - Operations generic to every lattice element.
- `Aut()`
  - Return ``Isom(L,L)``, the orthogonal automorphism homset.
- `BKZ(block_size=20)`
  - Return the same formed lattice in a BKZ-reduced framing.
- `Emb(codomain)`
  - Return the set of form-preserving embeddings into ``codomain``.
- `HKZ()`
  - Return the full-block BKZ (HKZ) reframing.
- `Isom(codomain)`
  - Return the set of isometries to ``codomain``.
- `LLL()`
  - Return the same formed lattice in an LLL-reduced framing.
- `Mor(codomain, category=None)`
- `O()`
  - Return ``O(L,b)=Aut(L,b)`` as the owned isometry group.
- `SO()` <sub>cached</sub>
  - Return ``SO(L)=ker(det:O(L)->{+-1})`` as a predicate subgroup.
- `approximate_closest_vector(target)`
- `b(left, right)`
  - Return the bilinear pairing \(b(v,w)\).
- `babai(target)`
- `bilinear_orthogonal_group()`
  - Return ``O(L,b)``; explicit name for the lattice pairing.
- `biproduct_factors()` <sub>cached</sub>
  - Return the indexed family of factors when this lattice was built by ``+``.
- `bkz_reduction(block_size=20)`
- `center_density()`
- `closest_vector(target)`
- `contact_polytope()`
- `correlation()`
- `correlation_morphism()` <sub>cached</sub>
  - Return ``L -> L^#``, ``v |-> b(v,-)``, whose selected-basis matrix is ``G``.
- `covering_radius()`
- `decomposition()` <sub>cached</sub>
  - Return the represented direct-sum decomposition, if present.
- `decomposition_names()`
  - Return the registered name of each indecomposable summand.
- `definite_complement_extensions(left, right)`
  - Return all isometries ``g`` with ``g(left)=right`` in the definite-complement regime.
- `delta()`
  - Return Nikulin's ``delta`` for an even 2-elementary lattice.
- `determinant()`
  - Return the determinant of a finite-rank lattice form.
- `discriminant()`
  - Return $d_\pm(b)=(-1)^{n(n-1)/2}\det G$, the signed determinant.
- `discriminant_bilinear_form()` <sub>cached</sub>
  - Return ``A_L`` with its descended ``K/R``-valued bilinear form.
- `discriminant_class(dual_lattice_element)`
  - Project an element of ``L^#`` to its discriminant class.
- `discriminant_group()`
  - Return the ``ZZ`` discriminant group with every form supported by ``L``.
- `discriminant_image()` <sub>cached</sub>
  - Return the computed image of ``rho_L`` when ``O(L)`` generators are known.
- `discriminant_length()`
  - Return the minimal number of generators of ``A_L`` over ``ZZ``.
- `discriminant_module()` <sub>cached</sub>
  - Return ``A_L = coker(L -> L^#)`` with the selected dual-basis presentation.
- `discriminant_projection()`
  - Return the quotient morphism ``L^# -> A_L``.
- `discriminant_quadratic_form()`
  - Return ``A_L`` with its ``K/2R``-valued quadratic form when ``L`` is even.
- `discriminant_representation()` <sub>cached</sub>
  - Return ``rho_L:O(L)->O(A_L)`` by functoriality of discriminants.
- `discriminant_representation_is_surjective() -> bool` <sub>cached</sub>
  - Return whether the computed discriminant image equals ``O(A_L)``.
- `div(element)`
  - Return the divisibility ``gcd{b(element,x): x in L}`` over ``ZZ``.
- `divided_discriminant_class(element)`
  - Return the class represented by ``correlation(element)/div(element)``.
- `dual_basis()`
  - Return the selected basis of ``L^#`` dual to the selected basis of ``L``.
- `dual_lattice()` <sub>cached</sub>
  - Return the metric dual ``L^#`` on the algebraic dual module.
- `dual_module()` <sub>cached</sub>
  - Return the algebraic dual module ``Hom_R(L,R)`` in the dual framing.
- `embed_in_even_unimodular(positive, negative)`
  - Return one primitive embedding into an even unimodular lattice.
- `embeds_in_even_unimodular(positive, negative) -> bool`
  - Decide primitive embeddability into an even unimodular ``II_{p,q}``.
- `equip_form_morphism()` <sub>cached</sub>
- `even_overlattice_inclusions()`
  - Return all even overlattice inclusions ``L -> L'``.
- `forget_form_morphism()` <sub>cached</sub>
- `form()` <sub>cached</sub>
  - Return the existing lattice pairing as a bilinear-form morphism.
- `gaussian_heuristic(*, exact_form=False)`
- `genus()` <sub>cached</sub>
  - Return the genus from signature and discriminant quadratic form.
- `glue_map(first, second)`
  - Return the Nikulin glue anti-isometry for a primitive extension.
- `gluing_route_discriminant_classes(left, right)`
  - Return admissible ``O(A_L)`` classes from the primitive-extension gluing route.
- `gram_tensor()`
  - Return the Gram tensor of the form: type $(0,2)$, not a matrix.
- `hadamard_ratio()`
- `hermite_invariant()`
- `hkz_reduction()`
- `identity_morphism()`
  - Return ``id_L`` in the lattice endomorphism homset.
- `indecomposable_name()`
- `indecomposable_summands()`
  - Return the family of indecomposable summands, in order.
- `is_decomposable()`
- `is_definite() -> bool`
- `is_even() -> bool`
  - Return whether ``b(x,x)`` lies in ``2R`` for every lattice vector.
- `is_finite_rank() -> bool`
  - Return whether this lattice is free of finite rank.
- `is_isometric(other)`
  - Return whether ``self`` and ``other`` are isometric when decidable.
- `is_locally_isometric(other, prime) -> bool`
  - Return whether ``self`` and ``other`` are isometric over ``ZZ_p``.
- `is_negative_definite() -> bool`
- `is_nondegenerate() -> bool`
  - Return whether the correlation map has zero radical.
- `is_p_elementary(prime) -> bool`
  - Return whether ``A_L`` is an elementary abelian ``prime``-group.
- `is_positive_definite() -> bool`
- `is_similar(other, scale)`
  - Return whether a similarity of the stated scale exists.
- `is_unimodular() -> bool`
  - Return whether the correlation ``L -> L^#`` is an isomorphism.
- `isotropic_flag(*basis)`
- `isotropic_flag_orbit_representatives(rank=2)`
- `isotropic_line_orbit_representatives()`
- `isotropic_plane_orbit_representatives()`
- `isotropic_reduction()`
  - Return ``S^perp/S`` when this lattice is represented as a subobject.
- `kissing_number()`
- `lattice_category()`
  - Return the base-ring lattice category owning this object.
- `level()`
  - Return the level of a finite nondegenerate integral lattice.
- `lll_reduction()`
- `local_modification(prime, *discriminant_classes)`
  - Return the isotropic ``p``-primary overlattice modification.
- `metric_dual()`
  - Return the metric dual ``L^#``; explicit synonym for ``dual_lattice``.
- `minimum()`
- `module_generating_set()`
  - Return the labels of the distinguished free-module framing.
- `module_generator(index)`
  - Return the module generator indexed by ``index``.
- `module_generators()` <sub>cached</sub>
- `orthogonal_group()`
  - Return ``O(L,b)=Aut(L,b)`` as the owned isometry group.
- `overlattice(*discriminant_classes)`
  - Return the inclusion ``L -> L'`` generated by discriminant classes.
- `packing_density()`
- `packing_radius()`
- `positive_cone_subgroup()`
  - Return the positive-cone-preserving subgroup in signature ``(1,n)``.
- `primitive_isotropic_subobject(*basis)`
- `q(vector)`
  - Return the quadratic form \(q(v)=b(v,v)\).
- `quadratic_orthogonal_group()`
  - Return ``O(L,q)`` for ``q(x)=b(x,x)``.
- `radical()`
  - Return ``rad(L)=id_L(L)^perp`` as a subobject of ``L``.
- `radical_quotient()`
  - Return the nondegenerate quotient ``L/rad(L)``.
- `rank()`
  - Return the rank of this lattice as a free module.
- `reflection(root)`
  - Return the integral orthogonal reflection in ``root``.
- `root_sublattice()`
- `roots()`
- `roots_of_square(square)`
- `shortest_vectors()`
- `signature_pair()`
  - Return $(p,q)$: the positive and negative indices of inertia.
- `similarity(scale, images=None, codomain=None)`
  - Return an explicit similarity as an isometry from ``L(scale)``.
- `similarity_homset(other, scale)`
  - Return similarities of scale ``scale`` as ``Isom(L(scale),other)``.
- `special_orthogonal_group()` <sub>cached</sub>
  - Return ``SO(L)=ker(det:O(L)->{+-1})`` as a predicate subgroup.
- `spinor_kernel_subgroup()`
  - Return the kernel of the real spinor-norm sign on ``O(L)``.
- `stable_complement_root_reflections(element)`
  - Return stable reflections in root-orbit representatives of ``element^perp``.
- `stable_orthogonal_group()` <sub>cached</sub>
  - Return ``ker(rho_L)`` as the stable orthogonal subgroup.
- `subobject_on(module_generating_set)`
  - Return the span with the restricted lattice form.
- `successive_minima()`
- `summands()`
- `theta_series(precision=20, variable='q')`
- `twist(scalar)`
  - Keep the module and rescale its form by ``scalar``.
- `two_elementary_invariants()`
  - Return Nikulin's \((r,a,\delta)\) for an even 2-elementary lattice.
- `unformed_module()`
  - Read this same parent at its weaker module level.
- `value_module()`
- `vector_primitive_extension(element)`
  - Return the primitive-extension/gluing datum cut out by ``element``.
- `vectors_of_square(square)`
- `vectors_of_square_and_divisibility(square, divisibility)`
- `voronoi_cell(bound=None)`
- `voronoi_relevant_vectors()`

*on elements*

- `b(other)`
  - Return \(b(v,w)\) by contracting the Gram tensor on \(v\) and \(w\).
- `div()`
  - Return the positive integer generator of ``b(v,L)`` over ``ZZ``.
- `divided_discriminant_class()`
- `divisibility_ideal()`
- `is_root() -> bool`
  - Return whether the orthogonal reflection in this vector is integral.
- `monomial_coefficients()`
- `norm()`
  - Return the form norm ``b(v,v)``.
- `q()`
  - Return \(q(v)=b(v,v)\).
- `to_list()`
  - Return the coordinates of this element as a Python list.
- `to_tuple()`
  - Return the coordinates of this element as a Python tuple.
- `to_vector()`
  - Return the coordinates of this element as a vector tensor of type $(1,0)$.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| [`FormModules(R)`](#cat-formmodules) | 17 | 2 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FramedFreeModules(R)`](#cat-framedfreemodules) | 13 |  |  |
| [`FramedModules(R)`](#cat-framedmodules) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`SymmetricBilinearFormModules(R)`](#cat-symmetricbilinearformmodules) | 7 |  |  |
| [`ProjectiveModules(R)`](#cat-projectivemodules) | 3 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`FreeModules(R)`](#cat-freemodules) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`BilinearFormModules(R)`](#cat-bilinearformmodules) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `EvenLattices(R)` {#cat-evenlattices}

Lattices satisfying `b(x,x) in 2R` for every lattice vector `x`.

- **defined at** `src/dzack_research/preamble/categories/lattices.py:2499`
- **probed as** `Category of even lattices`
- **above** [`Lattices(R)`](#cat-lattices)
- **below** [`RootLattices`](#cat-rootlattices)
- **refines**, transitively, in Sage's linearization order: [`Lattices(R)`](#cat-lattices) · [`SymmetricBilinearFormModules(R)`](#cat-symmetricbilinearformmodules) · [`FramedFreeModules(R)`](#cat-framedfreemodules) · [`BilinearFormModules(R)`](#cat-bilinearformmodules) · [`FormModules(R)`](#cat-formmodules) · [`FramedModules(R)`](#cat-framedmodules) · [`FreeModules(R)`](#cat-freemodules) · [`ProjectiveModules(R)`](#cat-projectivemodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `EvenLattices(R)(x, *args, **opts)`
- **specimens** `NamedLattices.Zero`, `NamedLattices.Z_2`, `NamedLattices.U`, `NamedLattices.H`, `NamedLattices.U_2`, `NamedLattices.H_2`, `NamedLattices.E8_2`, `NamedLattices.E10`, `NamedLattices.E10_2`, `NamedLattices.Sdp`, `NamedLattices.SEn`, `NamedLattices.Tco`, and 15 more

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Lattices satisfying ``b(x,x) in 2R`` for every lattice vector ``x``.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Lattices(R)`](#cat-lattices) | 123 | 11 |  |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| [`FormModules(R)`](#cat-formmodules) | 17 | 2 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FramedFreeModules(R)`](#cat-framedfreemodules) | 13 |  |  |
| [`FramedModules(R)`](#cat-framedmodules) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`SymmetricBilinearFormModules(R)`](#cat-symmetricbilinearformmodules) | 7 |  |  |
| [`ProjectiveModules(R)`](#cat-projectivemodules) | 3 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`FreeModules(R)`](#cat-freemodules) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`BilinearFormModules(R)`](#cat-bilinearformmodules) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `NondegenerateLattices(R)` {#cat-nondegeneratelattices}

Lattices whose correlation map has zero kernel.

- **defined at** `src/dzack_research/preamble/categories/lattices.py:2482`
- **probed as** `Category of nondegenerate lattices`
- **above** [`Lattices(R)`](#cat-lattices)
- **below** [`RootLattices`](#cat-rootlattices)
- **refines**, transitively, in Sage's linearization order: [`Lattices(R)`](#cat-lattices) · [`SymmetricBilinearFormModules(R)`](#cat-symmetricbilinearformmodules) · [`FramedFreeModules(R)`](#cat-framedfreemodules) · [`BilinearFormModules(R)`](#cat-bilinearformmodules) · [`FormModules(R)`](#cat-formmodules) · [`FramedModules(R)`](#cat-framedmodules) · [`FreeModules(R)`](#cat-freemodules) · [`ProjectiveModules(R)`](#cat-projectivemodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `NondegenerateLattices(R)(x, *args, **opts)`
- **specimens** `NamedLattices.Zero`, `NamedLattices.Z`, `NamedLattices.Z_2`, `NamedLattices.U`, `NamedLattices.H`, `NamedLattices.U_2`, `NamedLattices.H_2`, `NamedLattices.E8_2`, `NamedLattices.E10`, `NamedLattices.E10_2`, `NamedLattices.Sdp`, `NamedLattices.SEn`, and 18 more

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Lattices whose correlation map has zero kernel.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Lattices(R)`](#cat-lattices) | 123 | 11 |  |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| [`FormModules(R)`](#cat-formmodules) | 17 | 2 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FramedFreeModules(R)`](#cat-framedfreemodules) | 13 |  |  |
| [`FramedModules(R)`](#cat-framedmodules) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`SymmetricBilinearFormModules(R)`](#cat-symmetricbilinearformmodules) | 7 |  |  |
| [`ProjectiveModules(R)`](#cat-projectivemodules) | 3 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`FreeModules(R)`](#cat-freemodules) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`BilinearFormModules(R)`](#cat-bilinearformmodules) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `FiniteRankLattices(R)` {#cat-finiteranklattices}

Lattices whose underlying free module has finite rank.

- **defined at** `src/dzack_research/preamble/categories/lattices.py:2454`
- **probed as** `Category of finite-rank lattices`
- **above** [`FinitelyGeneratedFreeModules(R)`](#cat-finitelygeneratedfreemodules), [`Lattices(R)`](#cat-lattices)
- **below** [`RootLattices`](#cat-rootlattices)
- **refines**, transitively, in Sage's linearization order: [`Lattices(R)`](#cat-lattices) · [`FinitelyGeneratedFreeModules(R)`](#cat-finitelygeneratedfreemodules) · [`ModulesWithChosenFinitePresentation(R)`](#cat-moduleswithchosenfinitepresentation) · [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) · [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) · [`SymmetricBilinearFormModules(R)`](#cat-symmetricbilinearformmodules) · [`FramedFreeModules(R)`](#cat-framedfreemodules) · [`BilinearFormModules(R)`](#cat-bilinearformmodules) · [`FormModules(R)`](#cat-formmodules) · [`FramedModules(R)`](#cat-framedmodules) · [`FreeModules(R)`](#cat-freemodules) · [`ProjectiveModules(R)`](#cat-projectivemodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `FiniteRankLattices(R)(x, *args, **opts)`
- **specimens** `NamedLattices.Zero`, `NamedLattices.Z`, `NamedLattices.Z_2`, `NamedLattices.U`, `NamedLattices.H`, `NamedLattices.U_2`, `NamedLattices.H_2`, `NamedLattices.E8_2`, `NamedLattices.E10`, `NamedLattices.E10_2`, `NamedLattices.Sdp`, `NamedLattices.SEn`, and 18 more

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - Lattices whose underlying free module has finite rank.
- `is_finite_rank() -> bool`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Lattices(R)`](#cat-lattices) | 123 | 11 |  |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| [`FormModules(R)`](#cat-formmodules) | 17 | 2 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FramedFreeModules(R)`](#cat-framedfreemodules) | 13 |  |  |
| [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) | 10 |  |  |
| [`FramedModules(R)`](#cat-framedmodules) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`SymmetricBilinearFormModules(R)`](#cat-symmetricbilinearformmodules) | 7 |  |  |
| [`FinitelyGeneratedFreeModules(R)`](#cat-finitelygeneratedfreemodules) | 3 |  |  |
| [`ProjectiveModules(R)`](#cat-projectivemodules) | 3 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) | 2 |  |  |
| [`FreeModules(R)`](#cat-freemodules) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`BilinearFormModules(R)`](#cat-bilinearformmodules) | 1 |  |  |
| [`ModulesWithChosenFinitePresentation(R)`](#cat-moduleswithchosenfinitepresentation) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `RootLattices` {#cat-rootlattices}

Negative-definite ADE root lattices with a chosen simple-root framing.

- **defined at** `src/dzack_research/preamble/categories/lattices.py:2516`
- **probed as** `Category of root lattices`
- **above** [`EvenLattices(R)`](#cat-evenlattices), [`FiniteRankLattices(R)`](#cat-finiteranklattices), [`NondegenerateLattices(R)`](#cat-nondegeneratelattices)
- **refines**, transitively, in Sage's linearization order: [`EvenLattices(R)`](#cat-evenlattices) · [`NondegenerateLattices(R)`](#cat-nondegeneratelattices) · [`FiniteRankLattices(R)`](#cat-finiteranklattices) · [`Lattices(R)`](#cat-lattices) · [`FinitelyGeneratedFreeModules(R)`](#cat-finitelygeneratedfreemodules) · [`ModulesWithChosenFinitePresentation(R)`](#cat-moduleswithchosenfinitepresentation) · [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) · [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) · [`SymmetricBilinearFormModules(R)`](#cat-symmetricbilinearformmodules) · [`FramedFreeModules(R)`](#cat-framedfreemodules) · [`BilinearFormModules(R)`](#cat-bilinearformmodules) · [`FormModules(R)`](#cat-formmodules) · [`FramedModules(R)`](#cat-framedmodules) · [`FreeModules(R)`](#cat-freemodules) · [`ProjectiveModules(R)`](#cat-projectivemodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `RootLattices(x, *args, **opts)`
- **specimens** `NamedLattices.E8`, `NamedLattices.A1`, `NamedLattices.D4`, `NamedLattices.D6`, `NamedLattices.D8`, `NamedLattices.E7`

**Operations introduced here** (6 on objects, 4 on elements)

*on objects*

- `cartan_type()`
- `coxeter_number()`
- `fundamental_weights()`
  - Return the weights dual to the simple coroots.
- `highest_root()`
  - Return the highest root in the selected simple-root framing.
- `simple_reflections()`
- `simple_roots()`
  - Return the selected framing, which is the chosen simple system.

*on elements*

- `coroot()`
  - Return ``alpha^vee = 2*b(alpha,-)/b(alpha,alpha)`` in ``L^#``.
- `height()`
- `is_negative_root() -> bool`
- `is_positive_root() -> bool`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Lattices(R)`](#cat-lattices) | 123 | 11 |  |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| [`FormModules(R)`](#cat-formmodules) | 17 | 2 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FramedFreeModules(R)`](#cat-framedfreemodules) | 13 |  |  |
| [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) | 10 |  |  |
| [`FramedModules(R)`](#cat-framedmodules) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`SymmetricBilinearFormModules(R)`](#cat-symmetricbilinearformmodules) | 7 |  |  |
| [`FinitelyGeneratedFreeModules(R)`](#cat-finitelygeneratedfreemodules) | 3 |  |  |
| [`ProjectiveModules(R)`](#cat-projectivemodules) | 3 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`FiniteRankLattices(R)`](#cat-finiteranklattices) | 2 |  |  |
| [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) | 2 |  |  |
| [`FreeModules(R)`](#cat-freemodules) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`BilinearFormModules(R)`](#cat-bilinearformmodules) | 1 |  |  |
| [`EvenLattices(R)`](#cat-evenlattices) | 1 |  |  |
| [`ModulesWithChosenFinitePresentation(R)`](#cat-moduleswithchosenfinitepresentation) | 1 |  |  |
| [`NondegenerateLattices(R)`](#cat-nondegeneratelattices) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

### Supporting classes

#### `Genus` <sub>CLASS</sub>

The genus determined by signature and discriminant quadratic form.

- **defined at** `src/dzack_research/preamble/categories/lattices.py:362`
- **built by** `Genus(signature_pair, discriminant_quadratic_form)`

**Operations**

- `class_number()`
- `determinant()`
  - Return the determinant of a representative of this genus.
- `discriminant_form()`
  - Return the finite discriminant quadratic form component.
- `excess(prime)`
- `exists() -> bool`
  - Return whether the signature/discriminant-form datum is realizable.
- `level(prime)`
- `local_symbol(prime)`
  - Return the owned exact ``ZZ_p`` genus symbol at ``prime``.
- `mass()`
  - Return the Smith--Minkowski--Siegel mass for a definite genus.
- `representative()`
  - Return one owned integral lattice representing this genus.
- `representatives()`
  - Return the owned representatives enumerated by the exact backend.
- `signature_pair()`
  - Return the archimedean signature component ``(t_+,t_-)``.

### Functions

#### `nikulin_invariants` <sub>FUNCTION</sub>

Return \((r,a,\delta)\) as a point of \(\mathbb N^3\).

- **defined at** `src/dzack_research/preamble/categories/lattices.py:144`
- **built by** `nikulin_invariants(rank, discriminant_length, delta)`

## Modules, Complexes & Homological Algebra

> Framed free modules, Finitely presented modules, Formed modules, Group modules, Cochain complexes, Connections, and DG modules.

This chapter holds 43 categories, too many to draw legibly here; see [the interactive graph](preamble-graph.html).

### Categories

Ordered by depth: the least structured first.

#### `Modules(R)` {#cat-modules}

Modules over a ring, on the owned additive and scalar spines.

- **defined at** `src/dzack_research/preamble/categories/modules/pure/modules.py:125`
- **probed as** `Category of modules`
- **above** [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative)
- **below** [`AssociativeAlgebras(R)`](#cat-associativealgebras), [`BiproductModules(R)`](#cat-biproductmodules), [`CommutativeIdeals(R)`](#cat-commutativeideals), [`DividedPowerModules`](#cat-dividedpowermodules), [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules), [`FormModules(R)`](#cat-formmodules), [`FractionalIdeals(R)`](#cat-fractionalideals), [`FramedModules(R)`](#cat-framedmodules), [`FreeModules(R)`](#cat-freemodules), [`GradedTensorProductModules(R)`](#cat-gradedtensorproductmodules), [`LebesgueGradedModules(R)`](#cat-lebesguegradedmodules), [`LieAlgebras(R)`](#cat-liealgebras), [`LinearHomModules(R)`](#cat-linearhommodules), [`LocalizedModules(R)`](#cat-localizedmodules), [`ModuleSubobjects(R)`](#cat-modulesubobjects), [`ProjectiveModules(R)`](#cat-projectivemodules), [`RestrictedScalarsModules(R)`](#cat-restrictedscalarsmodules), [`TensorProductModules(R)`](#cat-tensorproductmodules), [`TorsionModules(R)`](#cat-torsionmodules), [`VectorSpaces(R)`](#cat-vectorspaces)
- **refines**, transitively, in Sage's linearization order: [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `Modules(R)(x, *args, **opts)`

**Operations introduced here** (20 on objects)

*on objects*

- `ElementType()`
  - Additive groups whose addition is commutative.
- `Mor(codomain, category=None)`
- `annihilator()`
  - Return ``Ann_R(M)=ker(R -> End_R(M))``.
- `base_change(ring_map)`
- `base_ring()`
- `is_finite()`
- `is_finitely_generated() -> bool`
- `is_flat() -> bool`
  - Decide flatness in the represented field/PID regimes.
- `is_framed() -> bool`
- `is_free() -> bool`
- `is_module() -> bool`
- `localization(*datum)`
  - Return ``S^{-1}M`` by scalar extension to ``S^{-1}R``.
- `localization_at_prime(prime)`
  - Return the localized module ``M_p`` at a represented prime.
- `localize(*datum)`
  - Return ``S^{-1}M`` by scalar extension to ``S^{-1}R``.
- `localize_at_prime(prime)`
  - Return the localized module ``M_p`` at a represented prime.
- `module_category()`
- `restrict_scalars(ring_map)`
  - Read this module over the domain of ``ring_map``.
- `scalar_action()`
- `scalar_multiple(scalar, element)`
  - Return ``r*m = rho_M(r)(m)``.
- `twist_scalar_action(ring_endomorphism)`
  - Twist this module's scalar action along a base-ring endomorphism.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `DividedPowerModules` {#cat-dividedpowermodules}

- **not exported**: reachable only as a supercategory
- **probed as** `Category of divided powers of modules`
- **above** [`Modules(R)`](#cat-modules)
- **below** [`DividedSquareModules(R)`](#cat-dividedsquaremodules)
- **refines**, transitively, in Sage's linearization order: [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `DividedPowerModules(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Additive groups whose addition is commutative.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `FinitelyGeneratedModules(R)` {#cat-finitelygeneratedmodules}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/modules/pure/modules.py:885`
- **probed as** `Category of finitely generated modules`
- **above** [`Modules(R)`](#cat-modules)
- **below** [`FinitelyGeneratedFormModules(R)`](#cat-finitelygeneratedformmodules), [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules)
- **refines**, transitively, in Sage's linearization order: [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `FinitelyGeneratedModules(R)(x, *args, **opts)`

**Operations introduced here** (10 on objects)

*on objects*

- `ElementType()`
  - Additive groups whose addition is commutative.
- `fiber(point)` <sub>cached</sub>
  - Return ``M(p)=M tensor_R kappa(p)`` at ``p in Spec(R)``.
- `fiber_dimension(point)`
  - Return ``dim_{kappa(p)} M(p)`` when the finite fiber is represented.
- `generic_rank()`
  - Return ``dim_K(M tensor_R K)`` for an integral-domain base ``R``.
- `is_finitely_generated() -> bool`
- `local_minimal_generators(point)`
  - Return a selected minimal generating set of ``M_p`` when represented.
- `local_number_of_generators(point)`
  - Return the minimal number of generators of ``M_p`` by Nakayama.
- `minimal_number_of_generators()`
  - Return ``dim_k(M/mM)`` for a finite module over a local ring.
- `rank_at(point)`
  - Return the local fiber rank ``dim_{kappa(p)} M(p)``.
- `residue_module()`
  - Return ``M/mM = M tensor_R k`` for a represented local base ring.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `FormModules(R)` {#cat-formmodules}

Modules over `R` equipped with a form.

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py:737`
- **probed as** `Category of form modules`
- **above** [`Modules(R)`](#cat-modules)
- **below** [`BilinearFormModules(R)`](#cat-bilinearformmodules), [`FinitelyGeneratedFormModules(R)`](#cat-finitelygeneratedformmodules), [`FinitelyPresentedFormModules(R)`](#cat-finitelypresentedformmodules), [`FreeFormModules(R)`](#cat-freeformmodules), [`QuadraticFormModules(R)`](#cat-quadraticformmodules)
- **refines**, transitively, in Sage's linearization order: [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `FormModules(R)(x, *args, **opts)`

**Operations introduced here** (17 on objects, 2 on elements)

*on objects*

- `ElementType()`
  - Additive groups whose addition is commutative.
- `Mor(codomain, category=None)`
- `b(left, right)`
  - Evaluate the (polar) bilinear form on two elements of this module.
- `base_change(ring_map)`
  - Base-change a scalar-valued finite free form along ``R -> S``.
- `equip_form_morphism()` <sub>cached</sub>
  - Return the inverse canonical module identification into the formed copy.
- `fibered_formed_hom(codomain, ring_map, module_morphism, value_morphism)`
  - Construct a formed morphism over a coefficient-ring map.
- `forget_form_morphism()` <sub>cached</sub>
  - Return the canonical module identification from the formed copy.
- `form()` <sub>cached</sub>
- `formed_hom(module_morphism, value_morphism)`
  - Construct the general fixed-fiber formed morphism ``(f,h)``.
- `gram_tensor()`
  - Return the scalar Gram as its intrinsic type-``(0,2)`` tensor.
- `left_module()`
- `norm(element)`
  - Return ``q(x)`` for a quadratic form, else ``b(x, x)``.
- `pairing(left, right)`
- `right_module()`
- `twist(scalar)`
- `unformed_module()`
  - Return the module used to equip this represented formed object.
- `value_module()`

*on elements*

- `b(other)`
  - Return the polar bilinear value ``b(self, other)``.
- `q()`
  - Return the represented quadratic/norm value of this element.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `FramedModules(R)` {#cat-framedmodules}

Modules carrying a specified generating map from a set.

- **defined at** `src/dzack_research/preamble/categories/modules/pure/modules.py:1165`
- **probed as** `Category of framed modules`
- **above** [`Modules(R)`](#cat-modules)
- **below** [`CartierDivisorGroups`](#cat-cartierdivisorgroups), [`ClassGroups`](#cat-classgroups), [`FractionFieldQuotients(R)`](#cat-fractionfieldquotients), [`FramedFreeModules(R)`](#cat-framedfreemodules), [`KahlerDifferentialModules(R)`](#cat-kahlerdifferentialmodules), [`ModulesWithChosenFinitePresentation(R)`](#cat-moduleswithchosenfinitepresentation), [`PicardGroups`](#cat-picardgroups)
- **refines**, transitively, in Sage's linearization order: [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `FramedModules(R)(x, *args, **opts)`

**Operations introduced here** (10 on objects)

*on objects*

- `ElementType()`
  - Modules carrying a specified generating map from a set.
- `framing_morphism()`
  - Return the presentation \(F(S) \twoheadrightarrow M\) of the framing.
- `inject_variables(scope=None, verbose=True)`
- `is_framed() -> bool`
- `linear_combination(coefficients, factor_on_left=True)`
- `module_generating_set()`
- `module_generator(label)`
- `module_generator_morphism()`
- `module_generators()` <sub>cached</sub>
- `number_of_module_generators()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `LinearHomModules(R)` {#cat-linearhommodules}

Represented Hom parents closed under pointwise `R`-linear operations.

- **defined at** `src/dzack_research/preamble/categories/modules/pure/modules.py:634`
- **probed as** `Category of linear Hom modules`
- **above** [`Modules(R)`](#cat-modules)
- **below** [`InternalHomModules(R)`](#cat-internalhommodules)
- **refines**, transitively, in Sage's linearization order: [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `LinearHomModules(R)(x, *args, **opts)`

**Operations introduced here** (7 on objects)

*on objects*

- `ElementType()`
  - Represented Hom parents closed under pointwise ``R``-linear operations.
- `as_morphism(element)`
- `evaluation(map_element, source_element)`
- `from_morphism(morphism)`
- `scalar_multiple(scalar, morphism)`
- `source_module()`
- `target_module()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `LocalizedModules(R)` {#cat-localizedmodules}

Modules represented as `S^{-1}M` for a chosen localization `S^{-1}R`.

- **defined at** `src/dzack_research/preamble/categories/modules/localizations.py:35`
- **probed as** `Category of localized modules`
- **above** [`Modules(R)`](#cat-modules)
- **refines**, transitively, in Sage's linearization order: [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `LocalizedModules(R)(x, *args, **opts)`

**Operations introduced here** (14 on objects, 3 on elements)

*on objects*

- `ElementType(parent, numerator, denominator) -> None`
  - A represented fraction ``m/s`` in ``S^{-1}M``.
- `base()`
- `base_ring()`
- `fraction(numerator, denominator=None, *, _trusted_denominator=False)`
- `is_finite()`
- `is_zero()`
  - Decide whether this localization is zero from finite generators or a finite source.
- `localization_functor()`
- `localization_prime_point()`
- `localization_ring()`
- `localization_source_module()`
- `localization_submonoid()`
- `localization_unit()`
- `source_ring()`
- `zero()`

*on elements*

- `denominator()`
- `equality_status(other)`
  - Return ``True``, ``False``, or ``Unknown`` for fraction equality.
- `numerator()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `SageObject` | 8 | 8 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `Element` |  | 9 |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| `ModuleElement` |  | 2 |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `ModuleSubobjects(R)` {#cat-modulesubobjects}

Modules carrying a chosen monomorphism into another module.

- **defined at** `src/dzack_research/preamble/categories/modules/pure/modules.py:709`
- **probed as** `Category of module subobjects`
- **above** [`Modules(R)`](#cat-modules)
- **below** [`FractionalIdeals(R)`](#cat-fractionalideals)
- **refines**, transitively, in Sage's linearization order: [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `ModuleSubobjects(R)(x, *args, **opts)`

**Operations introduced here** (11 on objects)

*on objects*

- `ElementType()`
  - Modules carrying a chosen monomorphism into another module.
- `ambient_module()`
  - Return the ambient module, i.e. the codomain of the inclusion.
- `embedded_module_generators()`
  - Return the indexed family of selected generator images.
- `inclusion()` <sub>cached</sub>
  - Return the chosen monomorphism represented by constructor data.
- `index()`
- `intersection(other)`
  - Return the meet as the image of the kernel of ``(i,-j)``.
- `is_primitive() -> bool`
- `is_saturated() -> bool`
- `orthogonal_complement()`
  - Return the orthogonal complement by deferring to the inclusion.
- `saturation()`
  - Return the primitive closure by deferring to the inclusion.
- `sum(other)`
  - Return the join of two subobjects of the same codomain.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `ProjectiveModules(R)` {#cat-projectivemodules}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/modules/pure/modules.py:1137`
- **probed as** `Category of projective modules`
- **above** [`Modules(R)`](#cat-modules)
- **below** [`FinitelyGeneratedFreeModules(R)`](#cat-finitelygeneratedfreemodules), [`FreeModules(R)`](#cat-freemodules)
- **refines**, transitively, in Sage's linearization order: [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `ProjectiveModules(R)(x, *args, **opts)`

**Operations introduced here** (3 on objects)

*on objects*

- `ElementType()`
  - Additive groups whose addition is commutative.
- `is_projective() -> bool`
- `projective_rank(point)`
  - Return the local free rank of a finite projective module at ``point``.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `RestrictedScalarsModules(R)` {#cat-restrictedscalarsmodules}

Modules obtained by reading an `S`-module over `R` along `R -> S`.

- **defined at** `src/dzack_research/preamble/categories/modules/pure/modules.py:1277`
- **probed as** `Category of restricted-scalars modules`
- **above** [`Modules(R)`](#cat-modules)
- **refines**, transitively, in Sage's linearization order: [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `RestrictedScalarsModules(R)(x, *args, **opts)`

**Operations introduced here** (5 on objects)

*on objects*

- `ElementType()`
  - Modules obtained by reading an ``S``-module over ``R`` along ``R -> S``.
- `extension_ring()`
- `module_over_extension()`
  - Return the original ``S``-module before restriction of scalars.
- `ring_map()`
  - Return the selected scalar map ``R -> S``.
- `scalar_multiple(scalar, element)`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `TensorProductModules(R)` {#cat-tensorproductmodules}

Modules carrying a selected tensor-product universal object.

- **defined at** `src/dzack_research/preamble/categories/modules/pure/modules.py:1704`
- **probed as** `Category of chosen tensor-product modules`
- **above** [`Modules(R)`](#cat-modules)
- **refines**, transitively, in Sage's linearization order: [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `TensorProductModules(R)(x, *args, **opts)`

**Operations introduced here** (6 on objects)

*on objects*

- `ElementType()`
  - Modules carrying a selected tensor-product universal object.
- `from_bilinear(bilinear)`
- `pure_tensor(left_element, right_element)`
  - Return the universal pure tensor of two elements.
- `tensor_factor(index)`
- `tensor_factors()`
  - Return the family of factors, indexed by the product's own index set.
- `universal_bilinear_map()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `TorsionModules(R)` {#cat-torsionmodules}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/modules/pure/torsion_modules.py:28`
- **probed as** `Category of torsion modules`
- **above** [`Modules(R)`](#cat-modules)
- **below** [`FinitelyPresentedTorsionModules(R)`](#cat-finitelypresentedtorsionmodules)
- **refines**, transitively, in Sage's linearization order: [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `TorsionModules(R)(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - Additive groups whose addition is commutative.
- `is_torsion() -> bool`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `VectorSpaces(R)` {#cat-vectorspaces}

Vector spaces over a field.

- **defined at** `src/dzack_research/preamble/categories/modules/pure/modules.py:828`
- **probed as** `Category of vector spaces`
- **above** [`Modules(R)`](#cat-modules)
- **refines**, transitively, in Sage's linearization order: [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `VectorSpaces(R)(x, *args, **opts)`

**Operations introduced here** (3 on objects)

*on objects*

- `ElementType()`
  - Vector spaces over a field.
- `basis_generator_labels()`
  - Return selected framing labels whose classes form a basis.
- `dimension()`
  - Return the dimension from this vector space's represented backend.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `BilinearFormModules(R)` {#cat-bilinearformmodules}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py:978`
- **probed as** `Category of modules with a bilinear form`
- **above** [`FormModules(R)`](#cat-formmodules)
- **below** [`FinitelyPresentedBilinearFormModules(R)`](#cat-finitelypresentedbilinearformmodules), [`SymmetricBilinearFormModules(R)`](#cat-symmetricbilinearformmodules)
- **refines**, transitively, in Sage's linearization order: [`FormModules(R)`](#cat-formmodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `BilinearFormModules(R)(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Additive groups whose addition is commutative.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| [`FormModules(R)`](#cat-formmodules) | 17 | 2 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `BiproductModules(R)` {#cat-biproductmodules}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/modules/pure/modules.py:1876`
- **probed as** `Category of chosen module biproducts`
- **above** [`DirectSumObjects`](#cat-directsumobjects), [`Modules(R)`](#cat-modules)
- **refines**, transitively, in Sage's linearization order: [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`DirectSumObjects`](#cat-directsumobjects) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `BiproductModules(R)(x, *args, **opts)`

**Operations introduced here** (11 on objects)

*on objects*

- `ElementType()`
  - Additive groups whose addition is commutative.
- `biproduct_factor(index)`
- `biproduct_factors()`
- `from_summands(left_map, right_map)`
  - Return the unique map ``self -> X`` extending both summand maps.
- `left_inclusion()`
- `left_injection()`
  - Return \(\iota_0 : M_0 \to M_0 \oplus M_1\).
- `left_projection()`
- `right_inclusion()`
- `right_injection()`
  - Return \(\iota_1 : M_1 \to M_0 \oplus M_1\).
- `right_projection()`
- `to_product(left_map, right_map)`
  - Return the unique map ``X -> self`` with the specified projections.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`DirectSumObjects`](#cat-directsumobjects) | 5 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `CochainComplexes(R)` {#cat-cochaincomplexes}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/modules/cochain_complexes.py:39`
- **probed as** `Category of cochain complexes`
- **above** [`GradedModules`](#cat-gradedmodules)
- **below** [`DifferentialGradedAlgebras(R)`](#cat-differentialgradedalgebras)
- **refines**, transitively, in Sage's linearization order: [`GradedModules`](#cat-gradedmodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `CochainComplexes(R)(x, *args, **opts)`

**Operations introduced here** (4 on objects)

*on objects*

- `ElementType()`
  - Modules graded by a monoid.
- `cohomology(degree)`
- `d(element)`
- `differential()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`GradedModules`](#cat-gradedmodules) | 4 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `DividedSquareModules(R)` {#cat-dividedsquaremodules}

Degree-two divided powers, classifying quadratic maps.

- **defined at** `src/dzack_research/preamble/categories/modules/powers.py:309`
- **probed as** `Category of divided-square modules`
- **above** [`DividedPowerModules`](#cat-dividedpowermodules)
- **refines**, transitively, in Sage's linearization order: [`DividedPowerModules`](#cat-dividedpowermodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `DividedSquareModules(R)(x, *args, **opts)`

**Operations introduced here** (5 on objects)

*on objects*

- `ElementType()`
  - Degree-two divided powers, classifying quadratic maps.
- `divided_square_source()`
- `from_quadratic(quadratic, codomain)`
  - Factor a quadratic map uniquely through the divided square.
- `polar(left, right)`
  - Return ``gamma_2(x+y)-gamma_2(x)-gamma_2(y)``.
- `quadratic(element)`
  - Return the universal quadratic value ``gamma_2(element)``.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`DividedPowerModules`](#cat-dividedpowermodules) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `FinitelyPresentedModules(R)` {#cat-finitelypresentedmodules}

Modules admitting a finite presentation.

- **defined at** `src/dzack_research/preamble/categories/modules/pure/modules.py:963`
- **probed as** `Category of finitely presented modules`
- **above** [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules)
- **below** [`CohomologyModules(R)`](#cat-cohomologymodules), [`FinitelyPresentedFormModules(R)`](#cat-finitelypresentedformmodules), [`FinitelyPresentedTorsionModules(R)`](#cat-finitelypresentedtorsionmodules), [`KahlerDifferentialModules(R)`](#cat-kahlerdifferentialmodules), [`ModulesWithChosenFinitePresentation(R)`](#cat-moduleswithchosenfinitepresentation)
- **refines**, transitively, in Sage's linearization order: [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `FinitelyPresentedModules(R)(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - Modules admitting a finite presentation.
- `is_finitely_presented() -> bool`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `FractionFieldQuotients(R)` {#cat-fractionfieldquotients}

Modules `Frac(R) / a` for a fractional ideal `a` of `R`.

```text
The active computation engine specializes this construction to
``R = ZZ``, where Sage's :class:`QmodnZ` computes ``QQ / n ZZ``.
```

- **defined at** `src/dzack_research/preamble/categories/modules/framed/fraction_field_quotients.py:38`
- **probed as** `Category of fraction-field quotients`
- **above** [`FramedModules(R)`](#cat-framedmodules)
- **refines**, transitively, in Sage's linearization order: [`FramedModules(R)`](#cat-framedmodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `FractionFieldQuotients(R)(x, *args, **opts)`

**Operations introduced here** (9 on objects, 2 on elements)

*on objects*

- `ElementType(parent, backend_element) -> None`
  - What a class in \(\operatorname{Frac}(R)/R\) is.
- `an_element()`
- `base_ring()`
- `divisibility_chain(index)`
  - Return the chosen cofinal divisibility chain element ``d_index``.
- `fraction_field()`
- `lift(element)`
  - Return the selected representative of ``element`` in the fraction field.
- `modulus()`
  - Return a generator of the fractional ideal being quotiented out.
- `projection_from_fraction_field()`
  - Return the quotient map ``Frac(R) -> Frac(R) / a`` as an owned set map.
- `zero()`

*on elements*

- `additive_order()`
- `lift()`
  - Return this class's representative in \(K\) under the chosen section.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `SageObject` | 8 | 8 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FramedModules(R)`](#cat-framedmodules) | 10 |  |  |
| `Element` |  | 9 |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `FractionalIdeals(R)` {#cat-fractionalideals}

Fractional ideals of an integral domain, as modules in its fraction field.

- **defined at** `src/dzack_research/preamble/categories/modules/fractional_ideals.py:58`
- **probed as** `Category of fractional ideals`
- **above** [`ModuleSubobjects(R)`](#cat-modulesubobjects), [`Modules(R)`](#cat-modules)
- **below** [`Ideals(R)`](#cat-ideals)
- **refines**, transitively, in Sage's linearization order: [`ModuleSubobjects(R)`](#cat-modulesubobjects) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `FractionalIdeals(R)(x, *args, **opts)`

**Operations introduced here** (12 on objects)

*on objects*

- `ElementType(parent, value) -> None`
  - File: /home/dzack/gitclones/sage-dev-allopts/src/sage/structure/element.pyx (starting at line 2367)
- `an_element()`
- `fraction_field()`
- `intersection(other)`
  - Return ``I intersect J`` inside the common fraction field.
- `inverse()`
  - Return ``I^{-1}={x in K : xI subseteq R}`` for an invertible ideal.
- `is_principal() -> bool`
- `is_projective() -> bool`
- `module_generators()` <sub>cached</sub>
- `principal_generator()`
  - Return ``a`` with ``I=aR`` when this ideal is principal.
- `scalar_multiple(scalar, element)`
- `sum(other)`
  - Return ``I+J`` inside the common fraction field.
- `zero()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `SageObject` | 8 | 8 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`ModuleSubobjects(R)`](#cat-modulesubobjects) | 11 |  |  |
| `Element` |  | 9 |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| `ModuleElement` |  | 2 |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `FreeModules(R)` {#cat-freemodules}

Modules admitting a basis.

- **defined at** `src/dzack_research/preamble/categories/modules/pure/modules.py:860`
- **probed as** `Category of free modules`
- **above** [`Modules(R)`](#cat-modules), [`ProjectiveModules(R)`](#cat-projectivemodules)
- **below** [`FramedFreeModules(R)`](#cat-framedfreemodules)
- **refines**, transitively, in Sage's linearization order: [`ProjectiveModules(R)`](#cat-projectivemodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `FreeModules(R)(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - Modules admitting a basis.
- `is_free() -> bool`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`ProjectiveModules(R)`](#cat-projectivemodules) | 3 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `InternalHomModules(R)` {#cat-internalhommodules}

The canonical full enriched Hom modules `Hom_R(M,N)`.

- **defined at** `src/dzack_research/preamble/categories/modules/pure/modules.py:681`
- **probed as** `Category of internal Hom modules`
- **above** [`LinearHomModules(R)`](#cat-linearhommodules)
- **below** [`MatrixSpaces(R)`](#cat-matrixspaces)
- **refines**, transitively, in Sage's linearization order: [`LinearHomModules(R)`](#cat-linearhommodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `InternalHomModules(R)(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - The canonical full enriched Hom modules ``Hom_R(M,N)``.
- `inclusion_into_generator_maps()`
  - The inclusion of the presented model of ``Hom(M, N)`` into ``N^{gens(M)}``.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`LinearHomModules(R)`](#cat-linearhommodules) | 7 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `QuadraticFormModules(R)` {#cat-quadraticformmodules}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py:1037`
- **probed as** `Category of modules with a quadratic form`
- **above** [`FormModules(R)`](#cat-formmodules)
- **below** [`FinitelyPresentedQuadraticFormModules(R)`](#cat-finitelypresentedquadraticformmodules)
- **refines**, transitively, in Sage's linearization order: [`FormModules(R)`](#cat-formmodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `QuadraticFormModules(R)(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - Additive groups whose addition is commutative.
- `q(element)`
  - Evaluate the equipped quadratic form on ``element``.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| [`FormModules(R)`](#cat-formmodules) | 17 | 2 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `CohomologyModules(R)` {#cat-cohomologymodules}

Cohomology modules retaining their represented cycle quotient.

- **defined at** `src/dzack_research/preamble/categories/modules/cochain_complexes.py:70`
- **probed as** `Category of cohomology modules`
- **above** [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules)
- **refines**, transitively, in Sage's linearization order: [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) · [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `CohomologyModules(R)(x, *args, **opts)`

**Operations introduced here** (6 on objects)

*on objects*

- `ElementType()`
  - Cohomology modules retaining their represented cycle quotient.
- `class_of_cycle(cycle)`
  - Return the cohomology class of a closed element of ``C^p``.
- `cochain_complex()`
- `cohomological_degree()`
- `cycle_representative(cohomology_class)`
  - Return the selected closed representative in ``C^p``.
- `degree()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `FinitelyGeneratedFormModules(R)` {#cat-finitelygeneratedformmodules}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py:1141`
- **probed as** `Category of finitely generated form modules`
- **above** [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules), [`FormModules(R)`](#cat-formmodules)
- **below** [`FinitelyGeneratedFreeFormModules(R)`](#cat-finitelygeneratedfreeformmodules)
- **refines**, transitively, in Sage's linearization order: [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) · [`FormModules(R)`](#cat-formmodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `FinitelyGeneratedFormModules(R)(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Additive groups whose addition is commutative.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| [`FormModules(R)`](#cat-formmodules) | 17 | 2 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `SymmetricBilinearFormModules(R)` {#cat-symmetricbilinearformmodules}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py:995`
- **probed as** `Category of modules with a symmetric bilinear form`
- **above** [`BilinearFormModules(R)`](#cat-bilinearformmodules)
- **below** [`Lattices(R)`](#cat-lattices), [`RationalLattices(R)`](#cat-rationallattices)
- **refines**, transitively, in Sage's linearization order: [`BilinearFormModules(R)`](#cat-bilinearformmodules) · [`FormModules(R)`](#cat-formmodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `SymmetricBilinearFormModules(R)(x, *args, **opts)`

**Operations introduced here** (7 on objects)

*on objects*

- `ElementType()`
  - Additive groups whose addition is commutative.
- `algebraic_correlation_morphism()`
- `correlation_isomorphism()`
- `hodge_discriminant(volume)`
- `hodge_star(volume, degree)`
- `hodge_star_over_fraction_field(volume, degree)`
- `multivector_hodge_star(volume, degree)`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| [`FormModules(R)`](#cat-formmodules) | 17 | 2 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`BilinearFormModules(R)`](#cat-bilinearformmodules) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `FinitelyPresentedFormModules(R)` {#cat-finitelypresentedformmodules}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py:1061`
- **probed as** `Category of finitely presented form modules`
- **above** [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules), [`FormModules(R)`](#cat-formmodules)
- **below** [`FinitelyPresentedBilinearFormModules(R)`](#cat-finitelypresentedbilinearformmodules), [`FinitelyPresentedQuadraticFormModules(R)`](#cat-finitelypresentedquadraticformmodules)
- **refines**, transitively, in Sage's linearization order: [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) · [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) · [`FormModules(R)`](#cat-formmodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `FinitelyPresentedFormModules(R)(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - Modules admitting a finite presentation.
- `base_change(ring_map)`
  - Base-change a scalar-valued finite free form along ``R -> S``.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| [`FormModules(R)`](#cat-formmodules) | 17 | 2 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `FinitelyPresentedTorsionModules(R)` {#cat-finitelypresentedtorsionmodules}

Finitely presented torsion modules over a PID.

- **defined at** `src/dzack_research/preamble/categories/modules/pure/torsion_modules.py:50`
- **probed as** `Category of finitely presented torsion modules`
- **above** [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules), [`TorsionModules(R)`](#cat-torsionmodules)
- **below** [`DiscriminantModules(R)`](#cat-discriminantmodules), [`TorsionBilinearFormModules(R)`](#cat-torsionbilinearformmodules), [`TorsionQuadraticFormModules(R)`](#cat-torsionquadraticformmodules)
- **refines**, transitively, in Sage's linearization order: [`TorsionModules(R)`](#cat-torsionmodules) · [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) · [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `FinitelyPresentedTorsionModules(R)(x, *args, **opts)`

**Operations introduced here** (3 on objects)

*on objects*

- `ElementType()`
  - Finitely presented torsion modules over a PID.
- `elements()` <sub>cached</sub>
  - Return all elements through the private finite Smith workspace.
- `is_torsion() -> bool`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) | 2 |  |  |
| [`TorsionModules(R)`](#cat-torsionmodules) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `FramedFreeModules(R)` {#cat-framedfreemodules}

Free modules equipped with the canonical basis map.

- **defined at** `src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py:274`
- **probed as** `Category of framed free modules`
- **above** [`FramedModules(R)`](#cat-framedmodules), [`FreeModules(R)`](#cat-freemodules)
- **below** [`DivisorGroups`](#cat-divisorgroups), [`FinitelyGeneratedFreeModules(R)`](#cat-finitelygeneratedfreemodules), [`FormalDivisorGroups(R)`](#cat-formaldivisorgroups), [`FreeFormModules(R)`](#cat-freeformmodules), [`Lattices(R)`](#cat-lattices)
- **refines**, transitively, in Sage's linearization order: [`FramedModules(R)`](#cat-framedmodules) · [`FreeModules(R)`](#cat-freemodules) · [`ProjectiveModules(R)`](#cat-projectivemodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `FramedFreeModules(R)(x, *args, **opts)`

**Operations introduced here** (13 on objects)

*on objects*

- `ElementType()`
  - Free modules equipped with the canonical basis map.
- `base_change(ring_map)`
  - Return ``S tensor_R M`` along the specified ring map ``R -> S``.
- `base_ring()`
- `cardinality()`
  - Return ``|R^(S)|``: ``|R|^|S|`` for finite ``S``, else ``max(|R|, |S|)`` by finite support.
- `framing_morphism()`
- `is_finite() -> bool`
  - Return whether the underlying free module is finite.
- `is_finite_rank() -> bool`
- `is_torsion_free() -> bool`
- `module_generating_set()`
- `module_generator(label)`
- `module_generators()` <sub>cached</sub>
- `rank()`
  - Return the cardinality of the module generating set.
- `subobject_on(module_generating_set)`
  - Return the submodule spanned by the specified elements.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FramedModules(R)`](#cat-framedmodules) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`ProjectiveModules(R)`](#cat-projectivemodules) | 3 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`FreeModules(R)`](#cat-freemodules) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `Ideals(R)` {#cat-ideals}

Integral ideals `I <= R`.

- **defined at** `src/dzack_research/preamble/categories/modules/fractional_ideals.py:367`
- **probed as** `Category of ideals`
- **above** [`CommutativeIdeals(R)`](#cat-commutativeideals), [`FractionalIdeals(R)`](#cat-fractionalideals)
- **refines**, transitively, in Sage's linearization order: [`FractionalIdeals(R)`](#cat-fractionalideals) · [`CommutativeIdeals(R)`](#cat-commutativeideals) · [`ModuleSubobjects(R)`](#cat-modulesubobjects) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `Ideals(R)(x, *args, **opts)`

**Operations introduced here** (3 on objects)

*on objects*

- `ElementType(parent, value) -> None`
  - Integral ideals ``I <= R``.
- `ideal_generators()`
- `ring()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`CommutativeIdeals(R)`](#cat-commutativeideals) | 22 |  |  |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `SageObject` | 8 | 8 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FractionalIdeals(R)`](#cat-fractionalideals) | 12 |  |  |
| [`ModuleSubobjects(R)`](#cat-modulesubobjects) | 11 |  |  |
| `Element` |  | 9 |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| `ModuleElement` |  | 2 |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `ModulesWithChosenFinitePresentation(R)` {#cat-moduleswithchosenfinitepresentation}

Finitely presented modules carrying one selected finite presentation.

- **defined at** `src/dzack_research/preamble/categories/modules/pure/modules.py:985`
- **probed as** `Category of modules with a chosen finite presentation`
- **above** [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules), [`FramedModules(R)`](#cat-framedmodules)
- **below** [`FinitelyGeneratedFreeModules(R)`](#cat-finitelygeneratedfreemodules)
- **refines**, transitively, in Sage's linearization order: [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) · [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) · [`FramedModules(R)`](#cat-framedmodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `ModulesWithChosenFinitePresentation(R)(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Finitely presented modules carrying one selected finite presentation.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) | 10 |  |  |
| [`FramedModules(R)`](#cat-framedmodules) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `DiscriminantModules(R)` {#cat-discriminantmodules}

Cokernels `A_L = coker(L -> L^#)` of nondegenerate finite lattices.

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/discriminant_modules.py:52`
- **probed as** `Category of discriminant modules`
- **above** [`FinitelyPresentedTorsionModules(R)`](#cat-finitelypresentedtorsionmodules)
- **below** [`DiscriminantBilinearModules(R)`](#cat-discriminantbilinearmodules)
- **refines**, transitively, in Sage's linearization order: [`FinitelyPresentedTorsionModules(R)`](#cat-finitelypresentedtorsionmodules) · [`TorsionModules(R)`](#cat-torsionmodules) · [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) · [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `DiscriminantModules(R)(x, *args, **opts)`

**Operations introduced here** (9 on objects)

*on objects*

- `ElementType()`
  - Cokernels ``A_L = coker(L -> L^#)`` of nondegenerate finite lattices.
- `discriminant_class(dual_lattice_element)`
  - Return the class of an element of ``L^#`` in ``A_L``.
- `dual_lattice()`
  - Return the selected metric dual ``L^#`` covering this quotient.
- `dual_lattice_lift(element)`
  - Return a representative of ``element`` in the selected metric dual ``L^#``.
- `primary_components()`
  - Return the family \(p\mapsto A_p\) over the primes dividing \(|A|\).
- `projection()` <sub>cached</sub>
  - Return the quotient map ``L^# -> A_L`` on the selected dual basis.
- `source_lattice()`
- `subgroup_on(generators)`
  - Return the finite subgroup generated by ``generators`` with its inclusion.
- `subgroups()` <sub>cached</sub>
  - Return all finite subgroups, exhaustively, for the represented finite module.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`FinitelyPresentedTorsionModules(R)`](#cat-finitelypresentedtorsionmodules) | 3 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) | 2 |  |  |
| [`TorsionModules(R)`](#cat-torsionmodules) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `FinitelyPresentedBilinearFormModules(R)` {#cat-finitelypresentedbilinearformmodules}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py:1080`
- **probed as** `Category of finitely presented modules with a bilinear form`
- **above** [`BilinearFormModules(R)`](#cat-bilinearformmodules), [`FinitelyPresentedFormModules(R)`](#cat-finitelypresentedformmodules)
- **below** [`TorsionBilinearFormModules(R)`](#cat-torsionbilinearformmodules)
- **refines**, transitively, in Sage's linearization order: [`FinitelyPresentedFormModules(R)`](#cat-finitelypresentedformmodules) · [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) · [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) · [`BilinearFormModules(R)`](#cat-bilinearformmodules) · [`FormModules(R)`](#cat-formmodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `FinitelyPresentedBilinearFormModules(R)(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Modules admitting a finite presentation.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| [`FormModules(R)`](#cat-formmodules) | 17 | 2 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`FinitelyPresentedFormModules(R)`](#cat-finitelypresentedformmodules) | 2 |  |  |
| [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`BilinearFormModules(R)`](#cat-bilinearformmodules) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `FinitelyPresentedQuadraticFormModules(R)` {#cat-finitelypresentedquadraticformmodules}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py:1098`
- **probed as** `Category of finitely presented modules with a quadratic form`
- **above** [`FinitelyPresentedFormModules(R)`](#cat-finitelypresentedformmodules), [`QuadraticFormModules(R)`](#cat-quadraticformmodules)
- **below** [`TorsionQuadraticFormModules(R)`](#cat-torsionquadraticformmodules)
- **refines**, transitively, in Sage's linearization order: [`QuadraticFormModules(R)`](#cat-quadraticformmodules) · [`FinitelyPresentedFormModules(R)`](#cat-finitelypresentedformmodules) · [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) · [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) · [`FormModules(R)`](#cat-formmodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `FinitelyPresentedQuadraticFormModules(R)(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Modules admitting a finite presentation.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| [`FormModules(R)`](#cat-formmodules) | 17 | 2 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`FinitelyPresentedFormModules(R)`](#cat-finitelypresentedformmodules) | 2 |  |  |
| [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) | 2 |  |  |
| [`QuadraticFormModules(R)`](#cat-quadraticformmodules) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `FreeFormModules(R)` {#cat-freeformmodules}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py:1116`
- **probed as** `Category of free form modules`
- **above** [`FormModules(R)`](#cat-formmodules), [`FramedFreeModules(R)`](#cat-framedfreemodules)
- **below** [`FinitelyGeneratedFreeFormModules(R)`](#cat-finitelygeneratedfreeformmodules)
- **refines**, transitively, in Sage's linearization order: [`FramedFreeModules(R)`](#cat-framedfreemodules) · [`FormModules(R)`](#cat-formmodules) · [`FramedModules(R)`](#cat-framedmodules) · [`FreeModules(R)`](#cat-freemodules) · [`ProjectiveModules(R)`](#cat-projectivemodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `FreeFormModules(R)(x, *args, **opts)`

**Operations introduced here** (3 on objects)

*on objects*

- `ElementType()`
  - Free modules equipped with the canonical basis map.
- `base_change(ring_map)`
  - Base-change a scalar-valued finite free form along ``R -> S``.
- `subobject_on(module_generating_set)`
  - Return the span equipped with the pulled-back form.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| [`FormModules(R)`](#cat-formmodules) | 17 | 2 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FramedFreeModules(R)`](#cat-framedfreemodules) | 13 |  |  |
| [`FramedModules(R)`](#cat-framedmodules) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`ProjectiveModules(R)`](#cat-projectivemodules) | 3 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`FreeModules(R)`](#cat-freemodules) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `FinitelyGeneratedFreeModules(R)` {#cat-finitelygeneratedfreemodules}

Finite-rank free modules with a chosen ordered basis.

- **defined at** `src/dzack_research/preamble/categories/modules/pure/modules.py:1058`
- **probed as** `Category of finitely generated free modules`
- **above** [`FramedFreeModules(R)`](#cat-framedfreemodules), [`ModulesWithChosenFinitePresentation(R)`](#cat-moduleswithchosenfinitepresentation), [`ProjectiveModules(R)`](#cat-projectivemodules)
- **below** [`FiniteRankLattices(R)`](#cat-finiteranklattices), [`FinitelyGeneratedFreeFormModules(R)`](#cat-finitelygeneratedfreeformmodules), [`MatrixSpaces(R)`](#cat-matrixspaces)
- **refines**, transitively, in Sage's linearization order: [`ModulesWithChosenFinitePresentation(R)`](#cat-moduleswithchosenfinitepresentation) · [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) · [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) · [`FramedFreeModules(R)`](#cat-framedfreemodules) · [`FramedModules(R)`](#cat-framedmodules) · [`FreeModules(R)`](#cat-freemodules) · [`ProjectiveModules(R)`](#cat-projectivemodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `FinitelyGeneratedFreeModules(R)(x, *args, **opts)`

**Operations introduced here** (3 on objects)

*on objects*

- `ElementType()`
  - Finite-rank free modules with a chosen ordered basis.
- `dual_module()`
- `free_resolution()` <sub>cached</sub>

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FramedFreeModules(R)`](#cat-framedfreemodules) | 13 |  |  |
| [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) | 10 |  |  |
| [`FramedModules(R)`](#cat-framedmodules) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`ProjectiveModules(R)`](#cat-projectivemodules) | 3 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) | 2 |  |  |
| [`FreeModules(R)`](#cat-freemodules) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`ModulesWithChosenFinitePresentation(R)`](#cat-moduleswithchosenfinitepresentation) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `TorsionBilinearFormModules(R)` {#cat-torsionbilinearformmodules}

Finitely presented torsion modules with a bilinear form.

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/torsion_form_modules.py:1161`
- **probed as** `Category of finitely presented torsion modules with a bilinear form`
- **above** [`FinitelyPresentedBilinearFormModules(R)`](#cat-finitelypresentedbilinearformmodules), [`FinitelyPresentedTorsionModules(R)`](#cat-finitelypresentedtorsionmodules)
- **below** [`DiscriminantBilinearModules(R)`](#cat-discriminantbilinearmodules)
- **refines**, transitively, in Sage's linearization order: [`FinitelyPresentedBilinearFormModules(R)`](#cat-finitelypresentedbilinearformmodules) · [`FinitelyPresentedFormModules(R)`](#cat-finitelypresentedformmodules) · [`FinitelyPresentedTorsionModules(R)`](#cat-finitelypresentedtorsionmodules) · [`TorsionModules(R)`](#cat-torsionmodules) · [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) · [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) · [`BilinearFormModules(R)`](#cat-bilinearformmodules) · [`FormModules(R)`](#cat-formmodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `TorsionBilinearFormModules(R)(x, *args, **opts)`

**Operations introduced here** (15 on objects)

*on objects*

- `ElementType()`
  - Finitely presented torsion modules with a bilinear form.
- `O()`
- `automorphism_group()` <sub>cached</sub>
  - Return ``O(A,b)`` as a finite owned group of live automorphisms.
- `form_vanishes_on(elements) -> bool`
- `invariant_factor_form()` <sub>cached</sub>
  - Return the form-preserving isomorphism to invariant-factor framing.
- `is_anti_isometric(other) -> bool`
  - Return whether ``(self,b)`` is isometric to ``(other,-b)``.
- `is_isometric_to(other) -> bool`
  - Decide isometry of represented finite symmetric bilinear forms.
- `is_isomorphic(other) -> bool`
  - Decide isometry of represented finite symmetric bilinear forms.
- `normal_form()`
  - Return the explicit isometry to this form in Jordan framing.
- `orthogonal_group()`
- `p_adic_jordan_decomposition()`
  - Return the chosen Jordan generators indexed by their prime.
- `p_adic_jordan_form()`
  - Return the explicit isometry to this form in Jordan framing.
- `p_adic_jordan_module_generators()`
  - Return the chosen prime-by-prime Jordan generating family.
- `pontryagin_dual_identification()`
  - Return ``A -> Hom(A,K/R)``, ``x |-> b(x,-)``, for perfect ``b``.
- `twist(scalar)`
  - Return the same finite module equipped with ``scalar*b``.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| [`FormModules(R)`](#cat-formmodules) | 17 | 2 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`FinitelyPresentedTorsionModules(R)`](#cat-finitelypresentedtorsionmodules) | 3 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`FinitelyPresentedFormModules(R)`](#cat-finitelypresentedformmodules) | 2 |  |  |
| [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) | 2 |  |  |
| [`TorsionModules(R)`](#cat-torsionmodules) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`BilinearFormModules(R)`](#cat-bilinearformmodules) | 1 |  |  |
| [`FinitelyPresentedBilinearFormModules(R)`](#cat-finitelypresentedbilinearformmodules) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `TorsionQuadraticFormModules(R)` {#cat-torsionquadraticformmodules}

Finitely presented torsion modules with a quadratic form.

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/torsion_form_modules.py:1308`
- **probed as** `Category of finitely presented torsion modules with a quadratic form`
- **above** [`FinitelyPresentedQuadraticFormModules(R)`](#cat-finitelypresentedquadraticformmodules), [`FinitelyPresentedTorsionModules(R)`](#cat-finitelypresentedtorsionmodules)
- **below** [`DiscriminantQuadraticModules(R)`](#cat-discriminantquadraticmodules)
- **refines**, transitively, in Sage's linearization order: [`FinitelyPresentedQuadraticFormModules(R)`](#cat-finitelypresentedquadraticformmodules) · [`QuadraticFormModules(R)`](#cat-quadraticformmodules) · [`FinitelyPresentedFormModules(R)`](#cat-finitelypresentedformmodules) · [`FinitelyPresentedTorsionModules(R)`](#cat-finitelypresentedtorsionmodules) · [`TorsionModules(R)`](#cat-torsionmodules) · [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) · [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) · [`FormModules(R)`](#cat-formmodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `TorsionQuadraticFormModules(R)(x, *args, **opts)`

**Operations introduced here** (15 on objects)

*on objects*

- `ElementType()`
  - Finitely presented torsion modules with a quadratic form.
- `O()`
- `associated_bilinear_form()`
  - Polarize ``q:A->QQ/2ZZ`` to ``b_q:A^2->QQ/ZZ``.
- `automorphism_group()` <sub>cached</sub>
  - Return ``O(A,q)`` as a finite owned group of live automorphisms.
- `form_vanishes_on(elements) -> bool`
- `invariant_factor_form()` <sub>cached</sub>
  - Return the quadratic-form isomorphism to invariant-factor framing.
- `is_anti_isometric(other) -> bool`
  - Return whether ``(self,q)`` is isometric to ``(other,-q)``.
- `is_isometric_to(other) -> bool`
  - Decide isometry of represented finite quadratic forms.
- `is_isomorphic(other) -> bool`
  - Decide isometry of represented finite quadratic forms.
- `normal_form()`
  - Return the explicit isometry to this quadratic form in Jordan framing.
- `orthogonal_group()`
- `p_adic_jordan_decomposition()`
  - Return the chosen quadratic Jordan generators indexed by prime.
- `p_adic_jordan_form()`
  - Return the explicit isometry to this quadratic form in Jordan framing.
- `p_adic_jordan_module_generators()`
  - Return the chosen prime-by-prime quadratic Jordan generators.
- `twist(scalar)`
  - Return the same finite module equipped with ``scalar*q``.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| [`FormModules(R)`](#cat-formmodules) | 17 | 2 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`FinitelyPresentedTorsionModules(R)`](#cat-finitelypresentedtorsionmodules) | 3 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`FinitelyPresentedFormModules(R)`](#cat-finitelypresentedformmodules) | 2 |  |  |
| [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) | 2 |  |  |
| [`QuadraticFormModules(R)`](#cat-quadraticformmodules) | 2 |  |  |
| [`TorsionModules(R)`](#cat-torsionmodules) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`FinitelyPresentedQuadraticFormModules(R)`](#cat-finitelypresentedquadraticformmodules) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `DiscriminantBilinearModules(R)` {#cat-discriminantbilinearmodules}

Discriminant modules with `K/R`-valued bilinear form.

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/discriminant_modules.py:147`
- **probed as** `Category of discriminant bilinear modules`
- **above** [`DiscriminantModules(R)`](#cat-discriminantmodules), [`TorsionBilinearFormModules(R)`](#cat-torsionbilinearformmodules)
- **below** [`DiscriminantQuadraticModules(R)`](#cat-discriminantquadraticmodules)
- **refines**, transitively, in Sage's linearization order: [`TorsionBilinearFormModules(R)`](#cat-torsionbilinearformmodules) · [`DiscriminantModules(R)`](#cat-discriminantmodules) · [`FinitelyPresentedBilinearFormModules(R)`](#cat-finitelypresentedbilinearformmodules) · [`FinitelyPresentedFormModules(R)`](#cat-finitelypresentedformmodules) · [`FinitelyPresentedTorsionModules(R)`](#cat-finitelypresentedtorsionmodules) · [`TorsionModules(R)`](#cat-torsionmodules) · [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) · [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) · [`BilinearFormModules(R)`](#cat-bilinearformmodules) · [`FormModules(R)`](#cat-formmodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `DiscriminantBilinearModules(R)(x, *args, **opts)`

**Operations introduced here** (26 on objects)

*on objects*

- `ElementType()`
  - Discriminant modules with ``K/R``-valued bilinear form.
- `O()`
- `automorphism_group()` <sub>cached</sub>
  - Return ``O(A,b)`` as live form automorphisms.
- `b(left, right)`
- `bilinear_value_module()`
- `discriminant_form_of_overlattice(subgroup)`
  - Return the Nikulin subquotient ``H^perp/H`` for the glued lattice.
- `equip_form_morphism()` <sub>cached</sub>
- `forget_form_morphism()` <sub>cached</sub>
- `form()` <sub>cached</sub>
- `form_vanishes_on(elements) -> bool`
  - Return whether the bilinear form vanishes on all pairs.
- `invariant_factor_form()` <sub>cached</sub>
  - Return the bilinear isometry to a normalized framed torsion form.
- `is_anti_isometric(other) -> bool`
- `is_isometric_to(other) -> bool`
- `is_isomorphic(other) -> bool`
- `normal_form()`
- `orthogonal_group()`
- `orthogonal_quotient(subgroup)`
  - Return ``H^perp/H`` with its descended bilinear form.
- `orthogonal_subgroup(subgroup)`
  - Return ``H^perp`` for a subgroup ``H <= A``.
- `overlattice_from_isotropic_subobject(subgroup)`
  - Return ``L -> L'`` for bilinear-isotropic glue ``H <= A_L``.
- `p_adic_jordan_decomposition()`
- `p_adic_jordan_form()`
- `p_adic_jordan_module_generators()`
- `pontryagin_dual_identification()`
  - Return ``A -> Hom(A,QQ/ZZ)``, ``x |-> b(x,-)``.
- `twist(scalar)`
- `unformed_module()`
- `value_module()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| [`FormModules(R)`](#cat-formmodules) | 17 | 2 |  |
| `Parent` | 15 |  |  |
| [`TorsionBilinearFormModules(R)`](#cat-torsionbilinearformmodules) | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) | 10 |  |  |
| [`DiscriminantModules(R)`](#cat-discriminantmodules) | 9 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`FinitelyPresentedTorsionModules(R)`](#cat-finitelypresentedtorsionmodules) | 3 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`FinitelyPresentedFormModules(R)`](#cat-finitelypresentedformmodules) | 2 |  |  |
| [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) | 2 |  |  |
| [`TorsionModules(R)`](#cat-torsionmodules) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`BilinearFormModules(R)`](#cat-bilinearformmodules) | 1 |  |  |
| [`FinitelyPresentedBilinearFormModules(R)`](#cat-finitelypresentedbilinearformmodules) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `MatrixSpaces(R)` {#cat-matrixspaces}

Hom objects between finitely generated framed free `R`-modules.

- **defined at** `src/dzack_research/preamble/categories/modules/pure/modules.py:2035`
- **probed as** `Category of matrix Hom objects`
- **above** [`FinitelyGeneratedFreeModules(R)`](#cat-finitelygeneratedfreemodules), [`InternalHomModules(R)`](#cat-internalhommodules)
- **below** [`MatrixEndomorphismSpaces(R)`](#cat-matrixendomorphismspaces)
- **refines**, transitively, in Sage's linearization order: [`InternalHomModules(R)`](#cat-internalhommodules) · [`LinearHomModules(R)`](#cat-linearhommodules) · [`FinitelyGeneratedFreeModules(R)`](#cat-finitelygeneratedfreemodules) · [`ModulesWithChosenFinitePresentation(R)`](#cat-moduleswithchosenfinitepresentation) · [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) · [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) · [`FramedFreeModules(R)`](#cat-framedfreemodules) · [`FramedModules(R)`](#cat-framedmodules) · [`FreeModules(R)`](#cat-freemodules) · [`ProjectiveModules(R)`](#cat-projectivemodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `MatrixSpaces(R)(x, *args, **opts)`

**Operations introduced here** (14 on objects, 19 on elements)

*on objects*

- `ElementType()`
  - The canonical full enriched Hom modules ``Hom_R(M,N)``.
- `column_index_set()`
- `from_flat_entries(entries)`
- `from_rows(rows)`
  - Construct the matrix morphism with the stated row entries.
- `from_tensor(coordinate_tensor)`
  - Read a compatible type-``(1,1)`` tensor as this linear map.
- `matrix_shape()`
- `matrix_unit(row_label, column_label)`
- `module_generating_set()`
- `module_generator(label)`
- `module_generators()` <sub>cached</sub>
- `ncols()`
- `nrows()`
- `number_of_module_generators()`
- `row_index_set()`

*on elements*

- `T()`
- `column(column_label)`
- `columns()`
- `det()`
- `determinant()`
- `invariant_factors()`
- `inverse()`
  - Return the inverse matrix morphism with reversed endpoints.
- `list()`
- `matrix_entry(row_label, column_label)`
- `matrix_rank()`
- `matrix_shape()`
- `ncols()`
- `nrows()`
- `row(row_label)`
- `rows()`
- `smith_form()`
  - Return ``(D,U,V)`` from invariant-factor presentation normalization.
- `smith_normal_form()`
- `solve_right(target)`
  - Return ``x`` in the domain with ``self(x)=target``.
- `transpose()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FramedFreeModules(R)`](#cat-framedfreemodules) | 13 |  |  |
| [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) | 10 |  |  |
| [`FramedModules(R)`](#cat-framedmodules) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`LinearHomModules(R)`](#cat-linearhommodules) | 7 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`FinitelyGeneratedFreeModules(R)`](#cat-finitelygeneratedfreemodules) | 3 |  |  |
| [`ProjectiveModules(R)`](#cat-projectivemodules) | 3 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) | 2 |  |  |
| [`FreeModules(R)`](#cat-freemodules) | 2 |  |  |
| [`InternalHomModules(R)`](#cat-internalhommodules) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`ModulesWithChosenFinitePresentation(R)`](#cat-moduleswithchosenfinitepresentation) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `FinitelyGeneratedFreeFormModules(R)` {#cat-finitelygeneratedfreeformmodules}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py:1157`
- **probed as** `Category of finitely generated free form modules`
- **above** [`FinitelyGeneratedFormModules(R)`](#cat-finitelygeneratedformmodules), [`FinitelyGeneratedFreeModules(R)`](#cat-finitelygeneratedfreemodules), [`FreeFormModules(R)`](#cat-freeformmodules)
- **below** [`RationalLattices(R)`](#cat-rationallattices)
- **refines**, transitively, in Sage's linearization order: [`FinitelyGeneratedFormModules(R)`](#cat-finitelygeneratedformmodules) · [`FreeFormModules(R)`](#cat-freeformmodules) · [`FinitelyGeneratedFreeModules(R)`](#cat-finitelygeneratedfreemodules) · [`ModulesWithChosenFinitePresentation(R)`](#cat-moduleswithchosenfinitepresentation) · [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) · [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) · [`FramedFreeModules(R)`](#cat-framedfreemodules) · [`FormModules(R)`](#cat-formmodules) · [`FramedModules(R)`](#cat-framedmodules) · [`FreeModules(R)`](#cat-freemodules) · [`ProjectiveModules(R)`](#cat-projectivemodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `FinitelyGeneratedFreeFormModules(R)(x, *args, **opts)`

**Operations introduced here** (8 on objects)

*on objects*

- `ElementType()`
  - Finite-rank free modules with a chosen ordered basis.
- `base_change(ring_map)`
  - Base-change a scalar-valued finite free form along ``R -> S``.
- `correlation_morphism()` <sub>cached</sub>
- `determinant()`
  - Return the determinant of the selected scalar-valued form.
- `dual_module()` <sub>cached</sub>
- `is_nondegenerate() -> bool`
- `is_unimodular() -> bool`
  - Return whether the correlation morphism is an isomorphism.
- `scale_submodule()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| [`FormModules(R)`](#cat-formmodules) | 17 | 2 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FramedFreeModules(R)`](#cat-framedfreemodules) | 13 |  |  |
| [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) | 10 |  |  |
| [`FramedModules(R)`](#cat-framedmodules) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`FinitelyGeneratedFreeModules(R)`](#cat-finitelygeneratedfreemodules) | 3 |  |  |
| [`FreeFormModules(R)`](#cat-freeformmodules) | 3 |  |  |
| [`ProjectiveModules(R)`](#cat-projectivemodules) | 3 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) | 2 |  |  |
| [`FreeModules(R)`](#cat-freemodules) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`FinitelyGeneratedFormModules(R)`](#cat-finitelygeneratedformmodules) | 1 |  |  |
| [`ModulesWithChosenFinitePresentation(R)`](#cat-moduleswithchosenfinitepresentation) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `DiscriminantQuadraticModules(R)` {#cat-discriminantquadraticmodules}

Even-lattice discriminant modules with quadratic form in `K/2R`.

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/discriminant_modules.py:366`
- **probed as** `Category of discriminant quadratic modules`
- **above** [`DiscriminantBilinearModules(R)`](#cat-discriminantbilinearmodules), [`TorsionQuadraticFormModules(R)`](#cat-torsionquadraticformmodules)
- **refines**, transitively, in Sage's linearization order: [`TorsionQuadraticFormModules(R)`](#cat-torsionquadraticformmodules) · [`DiscriminantBilinearModules(R)`](#cat-discriminantbilinearmodules) · [`FinitelyPresentedQuadraticFormModules(R)`](#cat-finitelypresentedquadraticformmodules) · [`QuadraticFormModules(R)`](#cat-quadraticformmodules) · [`TorsionBilinearFormModules(R)`](#cat-torsionbilinearformmodules) · [`DiscriminantModules(R)`](#cat-discriminantmodules) · [`FinitelyPresentedBilinearFormModules(R)`](#cat-finitelypresentedbilinearformmodules) · [`FinitelyPresentedFormModules(R)`](#cat-finitelypresentedformmodules) · [`FinitelyPresentedTorsionModules(R)`](#cat-finitelypresentedtorsionmodules) · [`TorsionModules(R)`](#cat-torsionmodules) · [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) · [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) · [`BilinearFormModules(R)`](#cat-bilinearformmodules) · [`FormModules(R)`](#cat-formmodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `DiscriminantQuadraticModules(R)(x, *args, **opts)`

**Operations introduced here** (28 on objects)

*on objects*

- `ElementType()`
  - Even-lattice discriminant modules with quadratic form in ``K/2R``.
- `O()`
- `associated_bilinear_form()`
  - Return the ``QQ/ZZ``-valued polarization as a distinct object.
- `automorphism_group()` <sub>cached</sub>
  - Return ``O(A,q)`` as live quadratic-form automorphisms.
- `brown_invariant()` <sub>cached</sub>
  - Return the Brown invariant in ``ZZ/8ZZ`` from the exact Gauss sum.
- `discriminant_form_of_overlattice(subgroup)`
  - Return ``H^perp/H``, the discriminant form of the glued overlattice.
- `form()` <sub>cached</sub>
- `form_vanishes_on(elements) -> bool`
  - Return whether ``q`` vanishes on every supplied element.
- `invariant_factor_form()` <sub>cached</sub>
  - Return the quadratic isometry to invariant-factor framing.
- `is_anisotropic() -> bool`
- `is_anti_isometric(other) -> bool`
- `is_isometric_to(other) -> bool`
- `is_isomorphic(other) -> bool`
- `is_metabolic() -> bool`
- `isotropic_elements()` <sub>cached</sub>
  - Return the classes on which the quadratic form vanishes.
- `isotropic_subgroups()` <sub>cached</sub>
  - Return all subgroups on which ``q`` vanishes identically.
- `lagrangian_subgroups()` <sub>cached</sub>
  - Return isotropic ``H`` with ``|H|^2=|A|``.
- `normal_form()`
- `orthogonal_group()`
- `orthogonal_quotient(subgroup)`
  - Return ``H^perp/H`` with its descended quadratic form.
- `overlattice_from_isotropic_subobject(subgroup)`
  - Return ``L -> L'`` for q-isotropic glue ``H <= A_L``.
- `p_adic_jordan_decomposition()`
- `p_adic_jordan_form()`
- `p_adic_jordan_module_generators()`
- `q(element)`
- `quadratic_value_module()`
- `twist(scalar)`
- `value_module()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`DiscriminantBilinearModules(R)`](#cat-discriminantbilinearmodules) | 26 |  |  |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| [`FormModules(R)`](#cat-formmodules) | 17 | 2 |  |
| `Parent` | 15 |  |  |
| [`TorsionBilinearFormModules(R)`](#cat-torsionbilinearformmodules) | 15 |  |  |
| [`TorsionQuadraticFormModules(R)`](#cat-torsionquadraticformmodules) | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) | 10 |  |  |
| [`DiscriminantModules(R)`](#cat-discriminantmodules) | 9 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`FinitelyPresentedTorsionModules(R)`](#cat-finitelypresentedtorsionmodules) | 3 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`FinitelyPresentedFormModules(R)`](#cat-finitelypresentedformmodules) | 2 |  |  |
| [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) | 2 |  |  |
| [`QuadraticFormModules(R)`](#cat-quadraticformmodules) | 2 |  |  |
| [`TorsionModules(R)`](#cat-torsionmodules) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`BilinearFormModules(R)`](#cat-bilinearformmodules) | 1 |  |  |
| [`FinitelyPresentedBilinearFormModules(R)`](#cat-finitelypresentedbilinearformmodules) | 1 |  |  |
| [`FinitelyPresentedQuadraticFormModules(R)`](#cat-finitelypresentedquadraticformmodules) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `MatrixEndomorphismSpaces(R)` {#cat-matrixendomorphismspaces}

The matrix realization of `End_R(F)` for a finite framed free module `F`.

- **defined at** `src/dzack_research/preamble/categories/modules/pure/modules.py:2317`
- **probed as** `Category of matrix endomorphism objects`
- **above** [`MatrixSpaces(R)`](#cat-matrixspaces), [`OwnedRings`](#cat-ownedrings)
- **below** [`MatrixAlgebras(R)`](#cat-matrixalgebras)
- **refines**, transitively, in Sage's linearization order: [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`MatrixSpaces(R)`](#cat-matrixspaces) · [`InternalHomModules(R)`](#cat-internalhommodules) · [`LinearHomModules(R)`](#cat-linearhommodules) · [`FinitelyGeneratedFreeModules(R)`](#cat-finitelygeneratedfreemodules) · [`ModulesWithChosenFinitePresentation(R)`](#cat-moduleswithchosenfinitepresentation) · [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) · [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) · [`FramedFreeModules(R)`](#cat-framedfreemodules) · [`FramedModules(R)`](#cat-framedmodules) · [`FreeModules(R)`](#cat-freemodules) · [`ProjectiveModules(R)`](#cat-projectivemodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `MatrixEndomorphismSpaces(R)(x, *args, **opts)`

**Operations introduced here** (3 on objects, 1 on elements)

*on objects*

- `ElementType()`
  - Unital rings whose notebook-facing ring interface is owned here.
- `diagonal(entries)`
- `identity_matrix()`

*on elements*

- `trace()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`MatrixSpaces(R)`](#cat-matrixspaces) | 14 | 19 |  |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FramedFreeModules(R)`](#cat-framedfreemodules) | 13 |  |  |
| [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) | 10 |  |  |
| [`FramedModules(R)`](#cat-framedmodules) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`LinearHomModules(R)`](#cat-linearhommodules) | 7 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 7 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`FinitelyGeneratedFreeModules(R)`](#cat-finitelygeneratedfreemodules) | 3 |  |  |
| [`ProjectiveModules(R)`](#cat-projectivemodules) | 3 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) | 2 |  |  |
| [`FreeModules(R)`](#cat-freemodules) | 2 |  |  |
| [`InternalHomModules(R)`](#cat-internalhommodules) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`ModulesWithChosenFinitePresentation(R)`](#cat-moduleswithchosenfinitepresentation) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `CochainHomset` {#cat-cochainhomset}

A represented Hom object which is both a Sage Homset and a category.

```text
This is the live counterpart of the archived owned Hom-category base.  It
keeps Sage's hard requirement that every ``Morphism`` be parented by an
actual ``Homset``, while also making that same parent the discrete category
``Hom_C(A,B)``.  Concrete categories subclass this and add enrichment to
the *same object*.
```

- **defined at** `src/dzack_research/preamble/categories/modules/cochain_complexes.py:315`
- **not placed**: `CochainHomset(hom_family, domain, codomain)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `ConnectionHomset` {#cat-connectionhomset}

A restricted Hom category that also carries independent enrichment.

```text
Its elements may be structured witnesses (for example derivations) whose
actual categorical arrows live in :meth:`arrow_set`.  Unlike
:class:`CategoricalHomset`, this parent is therefore not itself a Homset
and cannot become a second Homset for the same fixed endpoints.
```

- **defined at** `src/dzack_research/preamble/categories/modules/connections.py:529`
- **not placed**: `ConnectionHomset(family, domain, codomain)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `ConnectionSpace` {#cat-connectionspace}

A restricted Hom category that also carries independent enrichment.

```text
Its elements may be structured witnesses (for example derivations) whose
actual categorical arrows live in :meth:`arrow_set`.  Unlike
:class:`CategoricalHomset`, this parent is therefore not itself a Homset
and cannot become a second Homset for the same fixed endpoints.
```

- **defined at** `src/dzack_research/preamble/categories/modules/connections.py:357`
- **not placed**: `ConnectionSpace(family, restricted_source, restricted_target)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `DifferentialGradedModules` {#cat-differentialgradedmodules}

Right differential graded modules over one selected DGA `(A,d)`.

- **defined at** `src/dzack_research/preamble/categories/modules/dg_modules.py:44`
- **not placed**: `DifferentialGradedModules(parameter)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

**Operations introduced here** (2 on objects)

*on objects*

- `dga()`
- `is_differential_graded_module() -> bool`

#### `FiberedFormedModuleHomset` {#cat-fiberedformedmodulehomset}

A represented Hom object which is both a Sage Homset and a category.

```text
This is the live counterpart of the archived owned Hom-category base.  It
keeps Sage's hard requirement that every ``Morphism`` be parented by an
actual ``Homset``, while also making that same parent the discrete category
``Hom_C(A,B)``.  Concrete categories subclass this and add enrichment to
the *same object*.
```

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py:584`
- **not placed**: `FiberedFormedModuleHomset(domain, codomain, ring_map)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `FormedModuleHomset` {#cat-formedmodulehomset}

A represented Hom object which is both a Sage Homset and a category.

```text
This is the live counterpart of the archived owned Hom-category base.  It
keeps Sage's hard requirement that every ``Morphism`` be parented by an
actual ``Homset``, while also making that same parent the discrete category
``Hom_C(A,B)``.  Concrete categories subclass this and add enrichment to
the *same object*.
```

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py:350`
- **not placed**: `FormedModuleHomset(hom_family, domain, codomain)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `FormedModules` {#cat-formedmodules}

Modules equipped with a bilinear form \(M\otimes_R M\to W\).

```text
This is the diagonal of :class:`PairedModules`: a pairing of a module
with itself.
```

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py:694`
- **not placed**: `FormedModules(parameter)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

**Operations introduced here** (2 on objects, 2 on elements)

*on objects*

- `b(left, right)`
- `q(element)`

*on elements*

- `b(other)`
  - Return the bilinear value ``b(self, other)``.
- `q()`
  - Return the quadratic value ``q(self)=b(self,self)``.

#### `GradedAlgebraModules` {#cat-gradedalgebramodules}

Right graded modules over one selected graded algebra `A`.

- **defined at** `src/dzack_research/preamble/categories/modules/dg_modules.py:9`
- **not placed**: `GradedAlgebraModules(parameter)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

**Operations introduced here** (3 on objects)

*on objects*

- `act(module_element, algebra_element)`
- `graded_algebra()`
- `right_action()`

#### `GradedModules` {#cat-gradedmodules}

Modules graded by a monoid.

```text
Let \(M\) be a monoid and \(R\) a ring. An \(M\)-graded \(R\)-module is
an \(R\)-module \(N\) together with a direct-sum decomposition
\(N = \bigoplus_{m \in M} N_m\). This is the nLab graded module over an
ungraded ring (an \(M\)-graded object of \(\mathbf{Mod}_R\)).

The default monoid is \(\mathbb{Z}\) (additive), which is Sage's graded
module axiom. An \(M\)-graded algebra is an \(M\)-graded module whose
product sends \(N_m \times N_{m'}\) into \(N_{mm'}\).
```

- **defined at** `src/dzack_research/preamble/categories/modules/graded_modules.py:108`
- **not placed**: `GradedModules(base_ring, grading_monoid: sage.structure.parent.Parent)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)
- **below** [`CochainComplexes(R)`](#cat-cochaincomplexes)
- **specimens** `LebesgueConvolutionAlgebra`

**Operations introduced here** (3 on objects)

*on objects*

- `combine_degrees(left, right)`
  - The monoid product of two degrees.
- `grading_monoid()`
- `is_graded() -> bool`

#### `GroupModuleHomset` {#cat-groupmodulehomset}

Python implementation shared by module-enriched Hom parents.

```text
This is not a mathematical Hom category.  Concrete Hom parents remain
distinct categories and use this class only to share ordinary module-Hom
operations.
```

- **defined at** `src/dzack_research/preamble/categories/modules/group_modules/group_modules.py:628`
- **not placed**: `GroupModuleHomset(hom_family, domain, codomain)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `ModulesWithConnection` {#cat-moduleswithconnection}

Modules over `A` equipped with an `A/R`-connection.

- **defined at** `src/dzack_research/preamble/categories/modules/connections.py:44`
- **not placed**: `ModulesWithConnection(parameter)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

**Operations introduced here** (1 on objects)

*on objects*

- `connection()` <sub>cached</sub>

#### `ModulesWithFlatConnection` {#cat-moduleswithflatconnection}

Modules whose selected connection has zero curvature.

- **defined at** `src/dzack_research/preamble/categories/modules/connections.py:105`
- **not placed**: `ModulesWithFlatConnection(parameter)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

**Operations introduced here** (1 on objects)

*on objects*

- `is_flat_connection() -> bool`

#### `PairedModules` {#cat-pairedmodules}

Pairings \(X\otimes_R Y\to W\).

```text
An object is classified by an element of
\(\operatorname{Hom}_R(X\otimes_R Y,W)\).  The diagonal \(X=Y\) is
:class:`FormedModules`.
```

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py:642`
- **not placed**: `PairedModules(parameter)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

**Operations introduced here** (4 on objects)

*on objects*

- `left_module()`
- `pairing(left, right)`
  - Evaluate the pairing on a pair of elements.
- `right_module()`
- `value_module()`

### Objects

#### `CochainComplexObject` <sub>OBJECT</sub>

A nonnegative represented cochain complex with selected finite pieces.

- **defined at** `src/dzack_research/preamble/categories/modules/cochain_complexes.py:182`
- **built by** `CochainComplexObject(base_ring, pieces, differentials, name=None)`

**Operations**

- `Element(parent, components) -> None`
  - A finite family of homogeneous components.
- `differential_component(degree)`
- `selected_degrees()`

#### `GeneralModuleParent` <sub>OBJECT</sub>

A general `R`-module carried by a represented set.

```text
The defining data are additive operations on the underlying set and a scalar
action.  After construction the action is stored as the actual morphism
``rho : R -> End_R(M)``; it is not merely a callback attached to the
parent.
```

- **defined at** `src/dzack_research/preamble/categories/modules/general_modules.py:74`
- **built by** `GeneralModuleParent(ring, underlying_set, *, addition, zero, negation, scalar_action=None, rho=None, verify=True)`

**Operations**

- `Element(parent, value) -> None`
  - One element of a module presented on an arbitrary underlying set.
- `base()`
  - CategoryObject.base(self)
- `base_ring()`
  - CategoryObject.base_ring(self)
- `cardinality()`
- `is_finite()`
- `scalar_action_input()`
  - Return the supplied ``rho`` when one was given explicitly.
- `underlying_set()`
- `zero()`

#### `RestrictedScalarsModuleView` <sub>OBJECT</sub>

A distinct parent for the same additive group with a restricted scalar action.

- **defined at** `src/dzack_research/preamble/categories/modules/pure/modules.py:1324`
- **built by** `RestrictedScalarsModuleView(module, ring_map, *, subobject_ambient=None, subobject_generator_images=None, subobject_lift=None, subobject_inclusion_factory=None, subobject_verify_linearity=True)`

**Operations**

- `Element(parent, underlying_element) -> None`
  - File: /home/dzack/gitclones/sage-dev-allopts/src/sage/structure/element.pyx (starting at line 2367)
- `an_element()`
  - Parent.an_element(self)
- `framing_morphism()`
- `module_generating_set()`
- `module_generator(label)`
- `module_generators()` <sub>cached</sub>
- `wrap(underlying_element)`
  - Read an element of the extension module in this restricted module.
- `zero()`

### Elements

#### `CochainComplexElement` <sub>ELEMENT</sub>

A finite family of homogeneous components.

- **defined at** `src/dzack_research/preamble/categories/modules/cochain_complexes.py:178`
- **built by** `CochainComplexElement(parent, components)`

#### `Connection` <sub>ELEMENT</sub>

An `R`-connection `E -> E tensor_A Omega^1_{A/R}`.

- **defined at** `src/dzack_research/preamble/categories/modules/connections.py:138`
- **built by** `Connection(parent, generator_images)`

**Operations**

- `algebra()`
- `as_morphism()`
- `curvature_on_generator(label)`
- `curvature_target()`
- `de_rham_module()`
  - Return the DG-module de Rham complex attached to this flat connection.
- `generator_image(label)`
- `is_flat() -> bool`
- `module()`
- `one_forms()`
- `target_module()`
- `underlying_linear_morphism()`

#### `ConnectionMorphism` <sub>ELEMENT</sub>

An `A`-linear map horizontal for the selected connections.

- **defined at** `src/dzack_research/preamble/categories/modules/connections.py:473`
- **built by** `ConnectionMorphism(parent, images, *, verify_horizontality=True)`

**Operations**

- `as_morphism()`
- `codomain()`
- `domain()`
- `underlying_linear_morphism()`

#### `GeneralModuleElement` <sub>ELEMENT</sub>

One element of a module presented on an arbitrary underlying set.

- **defined at** `src/dzack_research/preamble/categories/modules/general_modules.py:27`
- **built by** `GeneralModuleElement(parent, value)`

**Operations**

- `underlying_element()`
- `value()`

### Morphisms and homsets

#### `BilinearFormMorphism` <sub>MORPHISM</sub>

A linear map out of a chosen tensor product, hence a bilinear map.

- **defined at** `src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py:1206`
- **built by** `BilinearFormMorphism(parent, images, *, elementwise=False, verify_linearity=True)`

**Operations**

- `coordinate_values()`
- `left_module()`
- `module()`
- `norm(element)`
- `polar_form()`
- `pullback(morphism)`
- `right_module()`

#### `CochainMorphism` <sub>MORPHISM</sub>

A degree-zero morphism commuting with the selected differentials.

- **defined at** `src/dzack_research/preamble/categories/modules/cochain_complexes.py:245`
- **built by** `CochainMorphism(parent, components)`

**Operations**

- `component(degree)`

#### `FiberedFormedModuleMorphism` <sub>MORPHISM</sub>

A formed-module morphism over a coefficient-ring map `g:S1 -> S2`.

```text
The actual linear data live in the target fiber, exactly as required by
the Grothendieck/fibered-category formulation:

``module_morphism : S2 tensor_S1 L1 -> L2`` and
``value_morphism  : S2 tensor_S1 W1 -> W2``.

The active scalar-extension backend currently materializes this for the
scalar-valued finite-free formed objects supported by ``FormModule``'s
``base_change`` method.  Unsupported scalar extensions fail at object
construction rather than being represented by a semilinear fiction.
```

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py:441`
- **built by** `FiberedFormedModuleMorphism(parent, module_morphism, value_morphism)`

**Operations**

- `base_changed_domain()`
- `map_value(value)`
- `module_morphism()`
- `ring_map()`
- `value_morphism()`

#### `FormEmbedding` <sub>MORPHISM</sub>

A form-preserving morphism whose module map is a monomorphism.

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py:310`
- **built by** `FormEmbedding(parent, module_morphism, value_morphism, *, quadratic: bool)`

**Operations**

- `is_quadratic() -> bool`

#### `FormedModuleMorphism` <sub>MORPHISM</sub>

A morphism of formed modules in one coefficient-ring fiber.

```text
The datum is a pair ``(f,h)`` with a module map on the underlying modules
and a module map on the value objects, satisfying the form square.  The
form is preserved exactly, and the morphism is an isometry onto its image,
exactly when ``h`` is the identity; :func:`is_form_morphism` asks that.
```

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py:167`
- **built by** `FormedModuleMorphism(parent, module_morphism, value_morphism)`

**Operations**

- `is_injective() -> bool`
  - Return whether the underlying module map is injective.
- `map_value(value)`
- `module_morphism()`
- `value_morphism()`

#### `GroupModuleMorphism` <sub>MORPHISM</sub>

An `R`-linear map commuting with the chosen `G`-actions.

- **defined at** `src/dzack_research/preamble/categories/modules/group_modules/group_modules.py:595`
- **built by** `GroupModuleMorphism(parent, images, *, elementwise=False, verify_linearity=True, verify_equivariance=True)`

#### `ModuleEmbedding` <sub>MORPHISM</sub>

A module morphism declared to be a monomorphism.

- **defined at** `src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py:791`
- **built by** `ModuleEmbedding(parent, images, *, elementwise=False, verify_linearity=True)`

**Operations**

- `factor_through(target_embedding)`
  - Return the unique factor through ``target_embedding`` when it exists.
- `is_injective() -> bool`
  - Return whether ``ker(self)=0`` when the kernel is computable.

#### `PairingMorphism` <sub>MORPHISM</sub>

A linear map out of a chosen tensor product, hence a bilinear map.

- **defined at** `src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py:1206`
- **built by** `PairingMorphism(parent, images, *, elementwise=False, verify_linearity=True)`

**Operations**

- `coordinate_values()`
- `left_module()`
- `module()`
- `norm(element)`
- `polar_form()`
- `pullback(morphism)`
- `right_module()`

#### `QuadraticFormMorphism` <sub>MORPHISM</sub>

A classifier `Gamma^2(M) -> W`, read as the quadratic map `M -> W`.

- **defined at** `src/dzack_research/preamble/categories/modules/powers.py:108`
- **built by** `QuadraticFormMorphism(parent, images, *, elementwise=False, verify_linearity=True)`

**Operations**

- `b(left, right)`
- `classifying_morphism()`
- `gram_tensor()`
- `lift_coordinate_values()`
- `lift_pairing(left, right)`
- `module()`
- `polar_coordinate_values()`
- `polar_form()`
- `pullback(morphism)`

#### `TorsionFormIsometry` <sub>MORPHISM</sub>

An explicit isomorphism of finite framed torsion modules preserving a form.

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/torsion_form_modules.py:167`
- **built by** `TorsionFormIsometry(parent, forward, inverse, *, quadratic: bool)`

**Operations**

- `is_quadratic() -> bool`

### Supporting classes

#### `BilinearMap` <sub>CLASS</sub>

A bilinear map specified on the selected product framing.

- **defined at** `src/dzack_research/preamble/categories/modules/pure/modules.py:1601`
- **built by** `BilinearMap(left, right, codomain, generator_images)`

**Operations**

- `codomain()`
- `generator_image(left_label, right_label)`
- `generator_index_set()`
- `left_factor()`
- `right_factor()`

#### `CochainDifferential` <sub>CLASS</sub>

The degree-`+1` differential of a represented cochain complex.

- **defined at** `src/dzack_research/preamble/categories/modules/cochain_complexes.py:151`
- **built by** `CochainDifferential(complex_)`

**Operations**

- `complex()`
- `component(degree)`
- `degree_shift()`

#### `ConnectionDeRhamDifferential` <sub>CLASS</sub>

The covariant differential on `E tensor_A Omega^*_{A/R}`.

- **defined at** `src/dzack_research/preamble/categories/modules/connections.py:611`
- **built by** `ConnectionDeRhamDifferential(module)`

**Operations**

- `degree_shift()`
- `module()`

#### `ConnectionDeRhamModule` <sub>CLASS</sub>

Factory namespace for a flat connection's de Rham DG-module.

- **defined at** `src/dzack_research/preamble/categories/modules/connections.py:634`
- **built by** `ConnectionDeRhamModule(connection)`

#### `FreeResolution` <sub>CLASS</sub>

The exact resolution `0 -> F_1 -> F_0 -> M -> 0` over a PID.

- **defined at** `src/dzack_research/preamble/categories/modules/pure/modules.py:1005`
- **built by** `FreeResolution(_module: object, _degree_zero: object, _degree_one: object, _differential_one: object, _augmentation: object, _zero_term: object)`

**Operations**

- `augmentation()`
- `differential(degree)`
- `is_exact()`
- `length()`
- `module()`
- `term(degree)`

### Functions

#### `AlgebraicCorrelationMorphism` <sub>FUNCTION</sub>

Return `g^flat : M -> M^vee` for a scalar-valued bilinear metric.

- **defined at** `src/dzack_research/preamble/categories/modules/hodge.py:201`
- **built by** `AlgebraicCorrelationMorphism(metric)`

#### `BasedFreeModule` <sub>FUNCTION</sub>

Return the selected based free module on a rank or explicit labels.

- **defined at** `src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py:840`
- **built by** `BasedFreeModule(base_ring, rank_or_labels)`

#### `BilinearForm` <sub>FUNCTION</sub>

Return `module` equipped with the stated bilinear form.

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py:1329`
- **built by** `BilinearForm(module, value_module, datum)`

#### `Boundaries` <sub>FUNCTION</sub>

Return `im(d^(degree-1))` as a subobject of `C^degree`.

- **defined at** `src/dzack_research/preamble/categories/modules/cochain_complexes.py:424`
- **built by** `Boundaries(complex_, degree)`

#### `CochainComplex` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/modules/cochain_complexes.py:415`
- **built by** `CochainComplex(base_ring, pieces, differentials, name=None)`

#### `Cohomology` <sub>FUNCTION</sub>

Return `H^degree = ker(d^degree) / im(d^(degree-1))`.

- **defined at** `src/dzack_research/preamble/categories/modules/cochain_complexes.py:432`
- **built by** `Cohomology(complex_, degree)`

#### `Connections` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/modules/connections.py:455`
- **built by** `Connections(module) -> dzack_research.preamble.categories.modules.connections.ConnectionSpace`

#### `CorrelationIsomorphism` <sub>FUNCTION</sub>

Return the perfect correlation `M ~= M^vee` for a unimodular form.

- **defined at** `src/dzack_research/preamble/categories/modules/hodge.py:230`
- **built by** `CorrelationIsomorphism(metric)`

#### `Cycles` <sub>FUNCTION</sub>

Return `ker(d^degree)` as a subobject of `C^degree`.

- **defined at** `src/dzack_research/preamble/categories/modules/cochain_complexes.py:419`
- **built by** `Cycles(complex_, degree)`

#### `DeterminantLine` <sub>FUNCTION</sub>

Return `det(module) = Lambda^rank(module) module`.

- **defined at** `src/dzack_research/preamble/categories/modules/hodge.py:55`
- **built by** `DeterminantLine(module)`

#### `DiscriminantModule` <sub>FUNCTION</sub>

Return the literal cokernel of `L -> L^#` with descended forms when supported.

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/discriminant_modules.py:822`
- **built by** `DiscriminantModule(lattice)`

#### `DividedSquare` <sub>FUNCTION</sub>

Return `Gamma^2_R(M)`, the universal target for quadratic maps.

- **defined at** `src/dzack_research/preamble/categories/modules/powers.py:620`
- **built by** `DividedSquare(module)`

#### `Ext` <sub>FUNCTION</sub>

Return `Ext^degree(module, other)`, the cohomology of `Hom(F_•, other)`.

- **defined at** `src/dzack_research/preamble/categories/modules/derived_functors.py:69`
- **built by** `Ext(degree, module, other)`

#### `ExteriorForms` <sub>FUNCTION</sub>

Return `Lambda^degree(module^vee)`.

- **defined at** `src/dzack_research/preamble/categories/modules/hodge.py:62`
- **built by** `ExteriorForms(module, degree)`

#### `FinitelyPresentedModule` <sub>FUNCTION</sub>

Return `coker(presentation)` in `R-Mod` with its selected module presentation.

- **defined at** `src/dzack_research/preamble/categories/modules/framed/finitely_generated/finitely_presented_modules.py:1722`
- **built by** `FinitelyPresentedModule(presentation, *, _cokernel_morphism=None, _extra_categories=(), _extra_construction_data=None, _subobject_ambient=None, _subobject_generator_images=None, _subobject_lift=None, _subobject_inclusion_factory=None, _subobject_verify_linearity=True, _biproduct_factors=None)`

#### `FormModule` <sub>FUNCTION</sub>

Return the same represented module construction equipped with `form`.

```text
The result remains a module object; it is not a wrapper around an
``underlying`` module.  A distinct represented parent is used so that two
different selected forms on isomorphic modules remain distinct structured
objects.
```

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py:1230`
- **built by** `FormModule(form, *, _extra_categories=(), _subobject_ambient=None, _subobject_generator_images=None, _subobject_lift=None, _subobject_inclusion_factory=None, _subobject_verify_linearity=True)`

#### `FractionFieldQuotient` <sub>FUNCTION</sub>

Return `Frac(base_ring) / modulus*base_ring` when natively supported.

- **defined at** `src/dzack_research/preamble/categories/modules/framed/fraction_field_quotients.py:267`
- **built by** `FractionFieldQuotient(base_ring, modulus=1)`

#### `FractionalIdeal` <sub>FUNCTION</sub>

Return the fractional ideal of `R` spanned by the stated elements of `Frac(R)`.

- **defined at** `src/dzack_research/preamble/categories/modules/fractional_ideals.py:745`
- **built by** `FractionalIdeal(base_ring, module_generating_set)`

#### `FramingVolumeTrivialization` <sub>FUNCTION</sub>

Explicitly trivialize `det(M)` using the selected framing.

```text
This is deliberately opt-in: a chosen module framing is not silently
treated as orientation data.  ``unit`` rescales the selected top wedge and
must be a unit of the coefficient ring.
```

- **defined at** `src/dzack_research/preamble/categories/modules/hodge.py:91`
- **built by** `FramingVolumeTrivialization(module, unit=None)`

#### `FreeModule` <sub>FUNCTION</sub>

Return the free module on a finite rank or an arbitrary index set.

- **defined at** `src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py:745`
- **built by** `FreeModule(base_ring, rank_or_index_set)`

#### `FreeModuleOn` <sub>FUNCTION</sub>

Return \(F_R(S)\), retaining the actual labels in `S`.

- **defined at** `src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py:791`
- **built by** `FreeModuleOn(base_ring, module_generating_set)`

#### `GeneralModule` <sub>FUNCTION</sub>

Construct a general represented `R`-module from its structure data.

- **defined at** `src/dzack_research/preamble/categories/modules/general_modules.py:321`
- **built by** `GeneralModule(ring, underlying_set, *, addition, zero, negation, scalar_action=None, rho=None, verify=True)`

#### `HodgeDiscriminant` <sub>FUNCTION</sub>

Return `Delta_(g,eps) = det(g) / eps(e_1 wedge ... wedge e_n)^2`.

- **defined at** `src/dzack_research/preamble/categories/modules/hodge.py:251`
- **built by** `HodgeDiscriminant(metric, volume)`

#### `HodgeStar` <sub>FUNCTION</sub>

Return the Hodge isomorphism on covariant `degree`-forms.

```text
For a perfect metric this is the categorical composite

``Lambda^k M^vee --Lambda^k(g^sharp)--> Lambda^k M --PD--> Lambda^(n-k) M^vee``.
```

- **defined at** `src/dzack_research/preamble/categories/modules/hodge.py:258`
- **built by** `HodgeStar(metric, volume, degree)`

#### `HodgeStarOverFractionField` <sub>FUNCTION</sub>

Return the covariant-form Hodge isomorphism after `R -> Frac(R)`.

```text
This is the explicit scalar-extension path for a nondegenerate but
non-unimodular metric.  The returned isomorphism lives over the fraction
field; it is never reported as an integral Hodge star on ``metric``.
```

- **defined at** `src/dzack_research/preamble/categories/modules/hodge.py:307`
- **built by** `HodgeStarOverFractionField(metric, volume, degree)`

#### `InternalHom` <sub>FUNCTION</sub>

Return the canonical enriched Hom object `source.Hom(target)`.

- **defined at** `src/dzack_research/preamble/categories/modules/internal_hom.py:166`
- **built by** `InternalHom(source, target)`

#### `ModuleWithConnection` <sub>FUNCTION</sub>

Return a fresh finite-free module carrying the selected connection.

- **defined at** `src/dzack_research/preamble/categories/modules/connections.py:591`
- **built by** `ModuleWithConnection(connection)`

#### `MultivectorHodgeStar` <sub>FUNCTION</sub>

Return the integral multivector Hodge map `Lambda^k M -> Lambda^(n-k) M`.

```text
Unlike the covariant-form Hodge star, this direction uses ``g^flat`` and
therefore does not require the metric to be perfect over the coefficient
ring.  It need not be an isomorphism for a non-unimodular metric.
```

- **defined at** `src/dzack_research/preamble/categories/modules/hodge.py:284`
- **built by** `MultivectorHodgeStar(metric, volume, degree)`

#### `PoincareDuality` <sub>FUNCTION</sub>

Return `Lambda^k M ~= Lambda^(n-k) M^vee` from `volume`.

- **defined at** `src/dzack_research/preamble/categories/modules/hodge.py:134`
- **built by** `PoincareDuality(module, volume, degree)`

#### `QuadraticForm` <sub>FUNCTION</sub>

Return `module` equipped with the stated quadratic form.

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py:1335`
- **built by** `QuadraticForm(module, value_module, datum)`

#### `QuadraticSquare` <sub>FUNCTION</sub>

Return `Gamma^2_R(M)`, the universal target for quadratic maps.

- **defined at** `src/dzack_research/preamble/categories/modules/powers.py:620`
- **built by** `QuadraticSquare(module)`

#### `Tor` <sub>FUNCTION</sub>

Return `Tor_degree(module, other)`, the homology of `F_• ⊗ other`.

- **defined at** `src/dzack_research/preamble/categories/modules/derived_functors.py:60`
- **built by** `Tor(degree, module, other)`

#### `TorsionModule` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/modules/pure/torsion_modules.py:182`
- **built by** `TorsionModule(presentation)`

#### `VolumeTrivialization` <sub>FUNCTION</sub>

Return the stated isomorphism `det(module) ~= R`.

```text
No orientation or volume is inferred from a framing.  This constructor
merely verifies two already represented mutually inverse module maps.
```

- **defined at** `src/dzack_research/preamble/categories/modules/hodge.py:72`
- **built by** `VolumeTrivialization(module, forward, inverse)`

#### `biproduct_morphism` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/modules/pure/modules.py:2015`
- **built by** `biproduct_morphism(left_morphism, right_morphism, source=None, target=None)`

#### `cochain_homset` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/modules/cochain_complexes.py:405`
- **built by** `cochain_homset(domain, codomain)`

#### `connection_homset` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/modules/connections.py:582`
- **built by** `connection_homset(domain, codomain)`

#### `divided_square_morphism` <sub>FUNCTION</sub>

Return `Gamma^2(f)` for a module morphism `f`.

- **defined at** `src/dzack_research/preamble/categories/modules/powers.py:635`
- **built by** `divided_square_morphism(morphism, source=None, target=None)`

#### `fibered_formed_module_homset` <sub>FUNCTION</sub>

Return formed morphisms `domain -> codomain` lying over `ring_map`.

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py:637`
- **built by** `fibered_formed_module_homset(domain, codomain, ring_map) -> dzack_research.preamble.categories.modules.framed.formed.form_modules.FiberedFormedModuleHomset`

#### `form_embedding` <sub>FUNCTION</sub>

Construct a form-preserving monomorphism on a chosen framing.

```text
The underlying module homset checks linearity and the selected relations.
The form square is checked by :class:`FormedModuleMorphism`, whose value
map is the identity here.  This works for both represented
:class:`FormModule` objects and discriminant-form objects, which
intentionally have their own structured-category realization rather than
being wrappers around one.
```

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py:321`
- **built by** `form_embedding(domain, codomain, images, *, quadratic: bool | None = None) -> dzack_research.preamble.categories.modules.framed.formed.form_modules.FormEmbedding`

#### `formed_module_homset` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/modules/framed/formed/form_modules.py:413`
- **built by** `formed_module_homset(domain, codomain) -> dzack_research.preamble.categories.modules.framed.formed.form_modules.FormedModuleHomset`

#### `free_resolution` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/modules/pure/modules.py:1054`
- **built by** `free_resolution(module)`

#### `internal_hom_morphism` <sub>FUNCTION</sub>

Return the map on internal Homs induced by pre- and postcomposition.

```text
``source_map`` runs from the new source to the old source and
``target_map`` from the old target to the new target, so the result is
``h |-> target_map * h * source_map``.
```

- **defined at** `src/dzack_research/preamble/categories/modules/internal_hom.py:174`
- **built by** `internal_hom_morphism(source_internal_hom, target_internal_hom, source_map, target_map)`

#### `module_embedding` <sub>FUNCTION</sub>

Construct a declared module monomorphism on a chosen framing.

- **defined at** `src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py:1191`
- **built by** `module_embedding(domain, codomain, images, *, verify_linearity=True) -> dzack_research.preamble.categories.modules.module_morphisms.module_morphisms.ModuleEmbedding`

#### `module_from_action` <sub>FUNCTION</sub>

Construct a general represented `R`-module from its structure data.

- **defined at** `src/dzack_research/preamble/categories/modules/general_modules.py:321`
- **built by** `module_from_action(ring, underlying_set, *, addition, zero, negation, scalar_action=None, rho=None, verify=True)`

#### `module_homset` <sub>FUNCTION</sub>

`Hom_R(domain, codomain)` for `R` the base of `domain`; both must be placed over `R`.

- **defined at** `src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py:1180`
- **built by** `module_homset(domain, codomain) -> dzack_research.preamble.categories.modules.module_morphisms.module_morphisms.ModuleHomset`

#### `regular_dg_module` <sub>FUNCTION</sub>

Read a DGA as its canonical right DG-module over itself.

- **defined at** `src/dzack_research/preamble/categories/modules/dg_modules.py:83`
- **built by** `regular_dg_module(dga)`

#### `restrict_scalars` <sub>FUNCTION</sub>

Return `Res_R^S(module)` along the specified morphism `R -> S`.

- **defined at** `src/dzack_research/preamble/categories/modules/pure/modules.py:1549`
- **built by** `restrict_scalars(module, ring_map, *, _subobject_ambient=None, _subobject_generator_images=None, _subobject_lift=None, _subobject_inclusion_factory=None, _subobject_verify_linearity=True)`

#### `ring_as_module` <sub>FUNCTION</sub>

Return the canonical free rank-one module of a ring over itself.

- **defined at** `src/dzack_research/preamble/categories/modules/framed/framed_free_modules.py:845`
- **built by** `ring_as_module(ring)`

#### `tensor_product_morphism` <sub>FUNCTION</sub>

Return `f tensor g` on the chosen tensor products.

- **defined at** `src/dzack_research/preamble/categories/modules/tensor_products.py:56`
- **built by** `tensor_product_morphism(left_morphism, right_morphism, source=None, target=None)`

#### `twist_scalar_action` <sub>FUNCTION</sub>

Twist the scalar action of an `R`-module along `R -> R`.

```text
This is restriction of scalars along an endomorphism of the scalar ring;
it is unrelated to ``L.twist(a)``, which rescales a lattice form while
leaving its scalar action unchanged.
```

- **defined at** `src/dzack_research/preamble/categories/modules/pure/modules.py:1573`
- **built by** `twist_scalar_action(module, ring_endomorphism)`

## Algebras & Differential Graded Algebras

> Associative/Commutative algebras, DGAs, Cohomology algebras, De Rham algebras, Derivations, and Graded algebras.

```mermaid
graph RL
  Algebras["Algebras(R)"]
  Algebras.Commutative["Algebras.Commutative"]
  AlgebrasWithChosenFinitePresentation["AlgebrasWithChosenFinitePresentation(R)"]
  AlgebrasWithChosenMultiplication["AlgebrasWithChosenMultiplication(R)"]
  AlternatingAlgebras["AlternatingAlgebras(R)"]
  AssociativeAlgebras["AssociativeAlgebras(R)"]
  AssociativeAlgebrasWithChosenMultiplication["AssociativeAlgebrasWithChosenMultiplication(R)"]
  AugmentedAlgebras["AugmentedAlgebras(R)"]
  CohomologyAlgebras["CohomologyAlgebras(R)"]
  CommutativeAlgebraCoproducts["CommutativeAlgebraCoproducts(R)"]
  CommutativeAlgebraPushouts["CommutativeAlgebraPushouts(R)"]
  CommutativeDifferentialGradedAlgebras["CommutativeDifferentialGradedAlgebras(R)"]
  CommutatorLieAlgebras["CommutatorLieAlgebras(R)"]
  DeRhamAlgebras["DeRhamAlgebras(R)"]
  DifferentialGradedAlgebras["DifferentialGradedAlgebras(R)"]
  FinitelyPresentedAlgebras["FinitelyPresentedAlgebras(R)"]
  FramedAlgebras["FramedAlgebras(R)"]
  FreeAlgebras["FreeAlgebras(R)"]
  GradedFreeAlgebras["GradedFreeAlgebras(R)"]
  GroupAlgebras["GroupAlgebras(R)"]
  KahlerDifferentialModules["KahlerDifferentialModules(R)"]
  LieAlgebras["LieAlgebras(R)"]
  MatrixAlgebras["MatrixAlgebras(R)"]
  OwnedAlgebras["OwnedAlgebras(R)"]
  RestrictedScalarsAlgebras["RestrictedScalarsAlgebras(R)"]
  StrictlyCommutativeDifferentialGradedAlgebras["StrictlyCommutativeDifferentialGradedAlgebras(R)"]
  SymmetricAlgebras["SymmetricAlgebras(R)"]
  TensorAlgebras["TensorAlgebras(R)"]
  CochainComplexes("CochainComplexes(R)")
  FinitelyPresentedModules("FinitelyPresentedModules(R)")
  FramedModules("FramedModules(R)")
  GradedAlgebras("GradedAlgebras")
  GradedCommutativeAlgebras("GradedCommutativeAlgebras")
  MatrixEndomorphismSpaces("MatrixEndomorphismSpaces(R)")
  Modules("Modules(R)")
  OwnedRings("OwnedRings")
  OwnedRings.Commutative("OwnedRings.Commutative")
  StrictlyGradedCommutativeAlgebras("StrictlyGradedCommutativeAlgebras")
  Algebras --> AssociativeAlgebras
  Algebras --> OwnedRings
  Algebras.Commutative --> Algebras
  Algebras.Commutative --> OwnedRings.Commutative
  AlgebrasWithChosenFinitePresentation --> FinitelyPresentedAlgebras
  AlgebrasWithChosenFinitePresentation --> FramedAlgebras
  AlgebrasWithChosenMultiplication --> Algebras
  AlgebrasWithChosenMultiplication --> AssociativeAlgebrasWithChosenMultiplication
  AlternatingAlgebras --> StrictlyGradedCommutativeAlgebras
  AssociativeAlgebras --> Modules
  AssociativeAlgebrasWithChosenMultiplication --> AssociativeAlgebras
  AugmentedAlgebras --> Algebras
  CohomologyAlgebras --> StrictlyGradedCommutativeAlgebras
  CommutativeAlgebraCoproducts --> Algebras.Commutative
  CommutativeAlgebraPushouts --> Algebras.Commutative
  CommutativeDifferentialGradedAlgebras --> DifferentialGradedAlgebras
  CommutativeDifferentialGradedAlgebras --> GradedCommutativeAlgebras
  CommutatorLieAlgebras --> AssociativeAlgebras
  CommutatorLieAlgebras --> LieAlgebras
  DeRhamAlgebras --> StrictlyCommutativeDifferentialGradedAlgebras
  DifferentialGradedAlgebras --> CochainComplexes
  DifferentialGradedAlgebras --> GradedAlgebras
  FinitelyPresentedAlgebras --> Algebras
  FramedAlgebras --> Algebras
  FreeAlgebras --> Algebras
  GradedFreeAlgebras --> FreeAlgebras
  GradedFreeAlgebras --> GradedAlgebras
  GroupAlgebras --> AlgebrasWithChosenMultiplication
  GroupAlgebras --> AugmentedAlgebras
  KahlerDifferentialModules --> FinitelyPresentedModules
  KahlerDifferentialModules --> FramedModules
  LieAlgebras --> Modules
  MatrixAlgebras --> Algebras
  MatrixAlgebras --> FramedAlgebras
  MatrixAlgebras --> MatrixEndomorphismSpaces
  OwnedAlgebras --> Algebras
  RestrictedScalarsAlgebras --> Algebras
  StrictlyCommutativeDifferentialGradedAlgebras --> CommutativeDifferentialGradedAlgebras
  StrictlyCommutativeDifferentialGradedAlgebras --> StrictlyGradedCommutativeAlgebras
  SymmetricAlgebras --> Algebras.Commutative
  SymmetricAlgebras --> GradedAlgebras
  TensorAlgebras --> GradedAlgebras
  classDef outside stroke-dasharray:6 4,fill:#f8fafc;
  class CochainComplexes,FinitelyPresentedModules,FramedModules,GradedAlgebras,GradedCommutativeAlgebras,MatrixEndomorphismSpaces,Modules,OwnedRings,OwnedRings.Commutative,StrictlyGradedCommutativeAlgebras outside;
```

### Categories

Ordered by depth: the least structured first.

#### `AssociativeAlgebras(R)` {#cat-associativealgebras}

Associative \(R\)-algebras, not necessarily unital.

```text
An associative algebra is an \(R\)-module with an associative bilinear
product. A unit is extra structure: the owned unital category is
:class:`Algebras`. Convolution \(L^1(\mathbb R)\) is the standard
non-unital example.
```

- **defined at** `src/dzack_research/preamble/categories/algebras/algebras.py:56`
- **probed as** `Category of associative algebras`
- **above** [`Modules(R)`](#cat-modules)
- **below** [`Algebras(R)`](#cat-algebras), [`AssociativeAlgebrasWithChosenMultiplication(R)`](#cat-associativealgebraswithchosenmultiplication), [`CommutatorLieAlgebras(R)`](#cat-commutatorliealgebras)
- **refines**, transitively, in Sage's linearization order: [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `AssociativeAlgebras(R)(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Associative \(R\)-algebras, not necessarily unital.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `LieAlgebras(R)` {#cat-liealgebras}

Lie algebras over a commutative owned base ring.

- **defined at** `src/dzack_research/preamble/categories/algebras/lie_algebras.py:11`
- **probed as** `Category of Lie algebras`
- **above** [`Modules(R)`](#cat-modules)
- **below** [`CommutatorLieAlgebras(R)`](#cat-commutatorliealgebras)
- **refines**, transitively, in Sage's linearization order: [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `LieAlgebras(R)(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - Lie algebras over a commutative owned base ring.
- `bracket(left, right)`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `AssociativeAlgebrasWithChosenMultiplication(R)` {#cat-associativealgebraswithchosenmultiplication}

Associative algebras interned on a chosen morphism \(A\otimes_R A\to A\).

- **defined at** `src/dzack_research/preamble/categories/algebras/algebras.py:84`
- **probed as** `Category of associative algebras with chosen multiplication`
- **above** [`AssociativeAlgebras(R)`](#cat-associativealgebras)
- **below** [`AlgebrasWithChosenMultiplication(R)`](#cat-algebraswithchosenmultiplication)
- **refines**, transitively, in Sage's linearization order: [`AssociativeAlgebras(R)`](#cat-associativealgebras) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `AssociativeAlgebrasWithChosenMultiplication(R)(x, *args, **opts)`
- **specimens** `LebesgueConvolutionAlgebra`

**Operations introduced here** (3 on objects)

*on objects*

- `ElementType()`
  - Associative \(R\)-algebras, not necessarily unital.
- `is_commutative() -> bool`
  - Whether the chosen multiplication commutes, decided at construction.
- `multiplication_morphism()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`AssociativeAlgebras(R)`](#cat-associativealgebras) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `CommutatorLieAlgebras(R)` {#cat-commutatorliealgebras}

Associative algebras with bracket `[x,y]=xy-yx`.

- **defined at** `src/dzack_research/preamble/categories/algebras/lie_algebras.py:35`
- **probed as** `Category of commutator Lie algebras`
- **above** [`AssociativeAlgebras(R)`](#cat-associativealgebras), [`LieAlgebras(R)`](#cat-liealgebras)
- **refines**, transitively, in Sage's linearization order: [`LieAlgebras(R)`](#cat-liealgebras) · [`AssociativeAlgebras(R)`](#cat-associativealgebras) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `CommutatorLieAlgebras(R)(x, *args, **opts)`

**Operations introduced here** (1 on objects, 1 on elements)

*on objects*

- `ElementType()`
  - Lie algebras over a commutative owned base ring.

*on elements*

- `bracket(other)`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`LieAlgebras(R)`](#cat-liealgebras) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`AssociativeAlgebras(R)`](#cat-associativealgebras) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `KahlerDifferentialModules(R)` {#cat-kahlerdifferentialmodules}

Selected modules `Omega^1_{A/R}` for the coefficient algebra `A`.

- **defined at** `src/dzack_research/preamble/categories/algebras/kahler_differentials.py:40`
- **probed as** `Category of Kähler differential modules`
- **above** [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules), [`FramedModules(R)`](#cat-framedmodules)
- **refines**, transitively, in Sage's linearization order: [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) · [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) · [`FramedModules(R)`](#cat-framedmodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `KahlerDifferentialModules(R)(x, *args, **opts)`

**Operations introduced here** (15 on objects)

*on objects*

- `ElementType()`
  - Selected modules ``Omega^1_{A/R}`` for the coefficient algebra ``A``.
- `ambient_differentials()`
  - Return ``Omega^1_{P/R} tensor_P A`` in the selected conormal sequence.
- `conormal_module()`
  - Return ``A tensor_P I ~= I/I^2`` for the selected quotient ``P -> A``.
- `conormal_morphism()`
  - Return ``I/I^2 -> Omega^1_{P/R} tensor_P A``, ``f |-> df``.
- `conormal_morphism_at(point)`
  - Base-change the selected conormal map to ``kappa(point)``.
- `cotangent_space(point)` <sub>cached</sub>
  - Return ``Omega^1_{A/R} tensor_A kappa(point)``.
- `derivation_classifier_isomorphism(target_module)`
  - Return ``Hom_A(Omega^1_{A/R},M) ~= Der_R(A,M)`` as an ``A``-module isomorphism.
- `differential_generator(algebra_generator_label)`
- `differential_projection()`
  - Return the quotient map onto ``Omega^1_{A/R}`` in the conormal sequence.
- `from_derivation(derivation)`
- `representing_isomorphism(target_module)`
  - Return ``Hom_A(Omega^1_{A/R},M) ~= Der_R(A,M)`` as an ``A``-module isomorphism.
- `source_algebra()`
- `tangent_dimension(point)`
  - Return the dimension of the relative Zariski tangent space.
- `tangent_space(point)` <sub>cached</sub>
  - Return the relative Zariski tangent space dual to ``cotangent_space(point)``.
- `universal_derivation()` <sub>cached</sub>

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) | 10 |  |  |
| [`FramedModules(R)`](#cat-framedmodules) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `Algebras(R)` {#cat-algebras}

Associative unital algebras over `R`.

```text
The structure morphism is \(\eta\colon R\to Z(A)\).  The forgetful
functor \(U\colon\mathbf{Alg}_R\to\mathbf{Mod}_R\) is
:func:`~dzack_research.preamble.categories.functors.algebra_modules.algebra_underlying_module_functor`.
Multiplication is the \(R\)-module morphism
\(m\colon A\otimes_R A\to A\).
```

- **defined at** `src/dzack_research/preamble/categories/algebras/algebras.py:192`
- **probed as** `Category of algebras`
- **above** [`AssociativeAlgebras(R)`](#cat-associativealgebras), [`OwnedRings`](#cat-ownedrings)
- **below** [`Algebras.Commutative`](#cat-algebras-commutative), [`AlgebrasWithChosenMultiplication(R)`](#cat-algebraswithchosenmultiplication), [`AugmentedAlgebras(R)`](#cat-augmentedalgebras), [`FinitelyPresentedAlgebras(R)`](#cat-finitelypresentedalgebras), [`FramedAlgebras(R)`](#cat-framedalgebras), [`FreeAlgebras(R)`](#cat-freealgebras), [`MatrixAlgebras(R)`](#cat-matrixalgebras), [`OwnedAlgebras(R)`](#cat-ownedalgebras), [`RestrictedScalarsAlgebras(R)`](#cat-restrictedscalarsalgebras)
- **refines**, transitively, in Sage's linearization order: [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AssociativeAlgebras(R)`](#cat-associativealgebras) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `Algebras(R)(x, *args, **opts)`

**Operations introduced here** (10 on objects)

*on objects*

- `ElementType()`
  - Associative unital algebras over ``R``.
- `Mor(codomain, category=None)`
- `algebra_base_ring()`
- `algebra_homset(hom_family, codomain)`
  - Return the fixed-endpoint homset selected by this algebra category.
- `algebra_structure_morphism()` <sub>cached</sub>
  - The structure morphism \(\eta\colon R\to Z(A)\) of this \(R\)-algebra.
- `base_ring()`
- `center()` <sub>cached</sub>
  - The centre \(Z(A)=\{z : za = az \text{ for all } a\}\) as a submodule of \(A\).
- `is_algebra() -> bool`
- `multiplication_morphism()` <sub>cached</sub>
  - The multiplication \(m\colon A\otimes_R A\to A\) as an \(R\)-module morphism.
- `scalar_multiple(scalar, element)`
  - ``a x`` for ``a`` in the algebra is the product, the regular module; a base scalar acts through the structure map.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 7 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`AssociativeAlgebras(R)`](#cat-associativealgebras) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `AugmentedAlgebras(R)` {#cat-augmentedalgebras}

Associative unital \(R\)-algebras equipped with an augmentation.

```text
An \(R\)-algebra is a ring \(A\) together with a ring homomorphism
\(R\to A\). If it is further equipped with an \(R\)-algebra homomorphism
the other way,
\[
\varepsilon\colon A\to R,
\]
then it is an *augmented* \(R\)-algebra. The kernel of \(\varepsilon\) is
the augmentation ideal. This is the nLab definition of an augmented
algebra (Cartan–Eilenberg: a supplemented algebra).
```

- **defined at** `src/dzack_research/preamble/categories/algebras/augmented_algebras.py:28`
- **probed as** `Category of augmented algebras`
- **above** [`Algebras(R)`](#cat-algebras)
- **below** [`GroupAlgebras(R)`](#cat-groupalgebras)
- **refines**, transitively, in Sage's linearization order: [`Algebras(R)`](#cat-algebras) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AssociativeAlgebras(R)`](#cat-associativealgebras) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `AugmentedAlgebras(R)(x, *args, **opts)`

**Operations introduced here** (3 on objects)

*on objects*

- `ElementType()`
  - Associative unital \(R\)-algebras equipped with an augmentation.
- `augmentation()` <sub>cached</sub>
- `is_augmented() -> bool`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Algebras(R)`](#cat-algebras) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 7 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`AssociativeAlgebras(R)`](#cat-associativealgebras) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `FinitelyPresentedAlgebras(R)` {#cat-finitelypresentedalgebras}

Algebras that admit a finite algebra presentation.

- **defined at** `src/dzack_research/preamble/categories/algebras/algebras.py:629`
- **probed as** `Category of finitely presented algebras`
- **above** [`Algebras(R)`](#cat-algebras)
- **below** [`AlgebrasWithChosenFinitePresentation(R)`](#cat-algebraswithchosenfinitepresentation)
- **refines**, transitively, in Sage's linearization order: [`Algebras(R)`](#cat-algebras) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AssociativeAlgebras(R)`](#cat-associativealgebras) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `FinitelyPresentedAlgebras(R)(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - Algebras that admit a finite algebra presentation.
- `is_finitely_presented() -> bool`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Algebras(R)`](#cat-algebras) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 7 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`AssociativeAlgebras(R)`](#cat-associativealgebras) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `FramedAlgebras(R)` {#cat-framedalgebras}

Algebras carrying a chosen algebra generating set.

- **defined at** `src/dzack_research/preamble/categories/algebras/algebras.py:507`
- **probed as** `Category of framed algebras`
- **above** [`Algebras(R)`](#cat-algebras)
- **below** [`AlgebrasWithChosenFinitePresentation(R)`](#cat-algebraswithchosenfinitepresentation), [`MatrixAlgebras(R)`](#cat-matrixalgebras)
- **refines**, transitively, in Sage's linearization order: [`Algebras(R)`](#cat-algebras) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AssociativeAlgebras(R)`](#cat-associativealgebras) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `FramedAlgebras(R)(x, *args, **opts)`

**Operations introduced here** (8 on objects)

*on objects*

- `ElementType()`
  - Algebras carrying a chosen algebra generating set.
- `algebra_generating_set()`
- `algebra_generator(label)`
- `algebra_generators()` <sub>cached</sub>
- `cardinality()`
- `is_central(element)`
  - Decide centrality from the selected algebra generating family.
- `number_of_algebra_generators()`
- `product_on_algebra_generators(left, right)`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Algebras(R)`](#cat-algebras) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 7 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`AssociativeAlgebras(R)`](#cat-associativealgebras) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `FreeAlgebras(R)` {#cat-freealgebras}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/algebras/free_algebras.py:499`
- **probed as** `Category of free algebras`
- **above** [`Algebras(R)`](#cat-algebras)
- **below** [`GradedFreeAlgebras(R)`](#cat-gradedfreealgebras)
- **refines**, transitively, in Sage's linearization order: [`Algebras(R)`](#cat-algebras) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AssociativeAlgebras(R)`](#cat-associativealgebras) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `FreeAlgebras(R)(x, *args, **opts)`

**Operations introduced here** (3 on objects)

*on objects*

- `ElementType()`
  - Associative unital algebras over ``R``.
- `algebra_homset(hom_family, codomain)`
- `is_free() -> bool`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Algebras(R)`](#cat-algebras) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 7 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`AssociativeAlgebras(R)`](#cat-associativealgebras) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `OwnedAlgebras(R)` {#cat-ownedalgebras}

Algebras carrying their chosen structure map `R -> Z(A)`.

- **defined at** `src/dzack_research/preamble/categories/algebras/algebras.py:1357`
- **probed as** `Category of owned algebras`
- **above** [`Algebras(R)`](#cat-algebras)
- **refines**, transitively, in Sage's linearization order: [`Algebras(R)`](#cat-algebras) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AssociativeAlgebras(R)`](#cat-associativealgebras) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `OwnedAlgebras(R)(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Algebras carrying their chosen structure map ``R -> Z(A)``.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Algebras(R)`](#cat-algebras) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 7 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`AssociativeAlgebras(R)`](#cat-associativealgebras) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `RestrictedScalarsAlgebras(R)` {#cat-restrictedscalarsalgebras}

`R`-algebras obtained by restricting an algebra along `R -> S`.

- **defined at** `src/dzack_research/preamble/categories/algebras/restricted_scalars.py:41`
- **probed as** `Category of restricted-scalars algebras`
- **above** [`Algebras(R)`](#cat-algebras)
- **refines**, transitively, in Sage's linearization order: [`Algebras(R)`](#cat-algebras) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AssociativeAlgebras(R)`](#cat-associativealgebras) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `RestrictedScalarsAlgebras(R)(x, *args, **opts)`

**Operations introduced here** (6 on objects)

*on objects*

- `ElementType()`
  - ``R``-algebras obtained by restricting an algebra along ``R -> S``.
- `algebra_over_extension()`
  - Return the original ``S``-algebra before scalar restriction.
- `extension_ring()`
- `restricted_algebra_generator_labels()`
- `restricted_scalar_generator_labels()`
- `ring_map()`
  - Return the selected scalar map ``R -> S``.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Algebras(R)`](#cat-algebras) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 7 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`AssociativeAlgebras(R)`](#cat-associativealgebras) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `Algebras.Commutative` {#cat-algebras-commutative}

Commutative associative unital algebras over `R`.

- **not exported**: reachable only as a supercategory
- **probed as** `Category of commutative algebras`
- **above** [`Algebras(R)`](#cat-algebras), [`OwnedRings.Commutative`](#cat-ownedrings-commutative)
- **below** [`CommutativeAlgebraCoproducts(R)`](#cat-commutativealgebracoproducts), [`CommutativeAlgebraPushouts(R)`](#cat-commutativealgebrapushouts), [`FormalPowerSeriesRings(R)`](#cat-formalpowerseriesrings), [`SymmetricAlgebras(R)`](#cat-symmetricalgebras)
- **refines**, transitively, in Sage's linearization order: [`Algebras(R)`](#cat-algebras) · [`OwnedRings.Commutative`](#cat-ownedrings-commutative) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AssociativeAlgebras(R)`](#cat-associativealgebras) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `Algebras.Commutative(x, *args, **opts)`
- **specimens** `AA`, `CC`, `CDF`, `GradedLebesgueAlgebra`, `QQ`, `QQbar`, `RDF`, `RR`, `ZZ`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 17 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Algebras(R)`](#cat-algebras) | 12 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`AssociativeAlgebras(R)`](#cat-associativealgebras) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `AlgebrasWithChosenMultiplication(R)` {#cat-algebraswithchosenmultiplication}

Unital algebras interned on a chosen morphism \(A\otimes_R A\to A\).

- **defined at** `src/dzack_research/preamble/categories/algebras/algebras.py:439`
- **probed as** `Category of algebras with chosen multiplication`
- **above** [`Algebras(R)`](#cat-algebras), [`AssociativeAlgebrasWithChosenMultiplication(R)`](#cat-associativealgebraswithchosenmultiplication)
- **below** [`GroupAlgebras(R)`](#cat-groupalgebras)
- **refines**, transitively, in Sage's linearization order: [`Algebras(R)`](#cat-algebras) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AssociativeAlgebrasWithChosenMultiplication(R)`](#cat-associativealgebraswithchosenmultiplication) · [`AssociativeAlgebras(R)`](#cat-associativealgebras) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `AlgebrasWithChosenMultiplication(R)(x, *args, **opts)`
- **specimens** `GradedLebesgueAlgebra`

**Operations introduced here** (3 on objects)

*on objects*

- `ElementType()`
  - Unital algebras interned on a chosen morphism \(A\otimes_R A\to A\).
- `multiplication_morphism()`
- `one()` <sub>cached</sub>

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Algebras(R)`](#cat-algebras) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 7 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AssociativeAlgebrasWithChosenMultiplication(R)`](#cat-associativealgebraswithchosenmultiplication) | 3 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`AssociativeAlgebras(R)`](#cat-associativealgebras) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `AlgebrasWithChosenFinitePresentation(R)` {#cat-algebraswithchosenfinitepresentation}

Finitely presented algebras carrying one selected finite presentation.

- **defined at** `src/dzack_research/preamble/categories/algebras/algebras.py:652`
- **probed as** `Category of algebras with a chosen finite presentation`
- **above** [`FinitelyPresentedAlgebras(R)`](#cat-finitelypresentedalgebras), [`FramedAlgebras(R)`](#cat-framedalgebras)
- **refines**, transitively, in Sage's linearization order: [`FinitelyPresentedAlgebras(R)`](#cat-finitelypresentedalgebras) · [`FramedAlgebras(R)`](#cat-framedalgebras) · [`Algebras(R)`](#cat-algebras) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AssociativeAlgebras(R)`](#cat-associativealgebras) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `AlgebrasWithChosenFinitePresentation(R)(x, *args, **opts)`

**Operations introduced here** (10 on objects)

*on objects*

- `ElementType()`
  - Finitely presented algebras carrying one selected finite presentation.
- `algebra_homset(hom_family, codomain)`
- `algebra_presentation_morphism()`
- `base_change(ring_map)`
- `is_torsion_free() -> bool`
  - Decide torsion-freeness in the supported integral PID-algebra regime.
- `lift_to_presentation(element)`
- `presentation()`
- `presentation_ideal()`
- `presentation_ring()`
- `relations()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Algebras(R)`](#cat-algebras) | 10 |  |  |
| [`FramedAlgebras(R)`](#cat-framedalgebras) | 8 |  |  |
| `SageObject` | 8 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 7 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`FinitelyPresentedAlgebras(R)`](#cat-finitelypresentedalgebras) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`AssociativeAlgebras(R)`](#cat-associativealgebras) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `CommutativeAlgebraCoproducts(R)` {#cat-commutativealgebracoproducts}

Commutative `R`-algebras equipped as selected binary coproducts.

- **defined at** `src/dzack_research/preamble/categories/algebras/algebras.py:858`
- **probed as** `Category of commutative algebra coproducts`
- **above** [`Algebras.Commutative`](#cat-algebras-commutative)
- **refines**, transitively, in Sage's linearization order: [`Algebras.Commutative`](#cat-algebras-commutative) · [`Algebras(R)`](#cat-algebras) · [`OwnedRings.Commutative`](#cat-ownedrings-commutative) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AssociativeAlgebras(R)`](#cat-associativealgebras) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `CommutativeAlgebraCoproducts(R)(x, *args, **opts)`

**Operations introduced here** (9 on objects)

*on objects*

- `ElementType()`
  - Commutative ``R``-algebras equipped as selected binary coproducts.
- `coproduct_factors()`
  - Return the family of factors, indexed by the product's own index set.
- `coproduct_injection(index)` <sub>cached</sub>
- `coproduct_injections()`
- `from_cocone(left_map, right_map)`
- `left_coproduct_map()`
- `right_coproduct_map()`
- `tensor_factors()`
  - Return the family of factors, indexed by the product's own index set.
- `tensor_map(left_map, right_map)`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 17 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Algebras(R)`](#cat-algebras) | 12 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`AssociativeAlgebras(R)`](#cat-associativealgebras) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `CommutativeAlgebraPushouts(R)` {#cat-commutativealgebrapushouts}

Commutative `R`-algebras equipped as selected pushouts of one span.

- **defined at** `src/dzack_research/preamble/categories/algebras/algebras.py:914`
- **probed as** `Category of commutative algebra pushouts`
- **above** [`Algebras.Commutative`](#cat-algebras-commutative)
- **refines**, transitively, in Sage's linearization order: [`Algebras.Commutative`](#cat-algebras-commutative) · [`Algebras(R)`](#cat-algebras) · [`OwnedRings.Commutative`](#cat-ownedrings-commutative) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AssociativeAlgebras(R)`](#cat-associativealgebras) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `CommutativeAlgebraPushouts(R)(x, *args, **opts)`

**Operations introduced here** (6 on objects)

*on objects*

- `ElementType()`
  - Commutative ``R``-algebras equipped as selected pushouts of one span.
- `from_pushout_cocone(left_map, right_map)`
- `left_pushout_map()`
- `pushout_maps()` <sub>cached</sub>
- `pushout_span()`
- `right_pushout_map()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 17 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Algebras(R)`](#cat-algebras) | 12 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`AssociativeAlgebras(R)`](#cat-associativealgebras) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `TensorAlgebras(R)` {#cat-tensoralgebras}

Tensor algebras of represented modules.

- **defined at** `src/dzack_research/preamble/categories/algebras/free_algebras.py:596`
- **probed as** `Category of tensor algebras`
- **above** [`GradedAlgebras`](#cat-gradedalgebras)
- **refines**, transitively, in Sage's linearization order: [`GradedAlgebras`](#cat-gradedalgebras) · [`Algebras(R)`](#cat-algebras) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`GradedModules`](#cat-gradedmodules) · [`AssociativeAlgebras(R)`](#cat-associativealgebras) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `TensorAlgebras(R)(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - Tensor algebras of represented modules.
- `free_source_module()`
  - Return the module whose tensor algebra this object represents.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Algebras(R)`](#cat-algebras) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 7 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`GradedAlgebras`](#cat-gradedalgebras) | 2 | 2 |  |
| [`GradedModules`](#cat-gradedmodules) | 4 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`AssociativeAlgebras(R)`](#cat-associativealgebras) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `DifferentialGradedAlgebras(R)` {#cat-differentialgradedalgebras}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py:83`
- **probed as** `Category of differential graded algebras`
- **above** [`CochainComplexes(R)`](#cat-cochaincomplexes), [`GradedAlgebras`](#cat-gradedalgebras)
- **below** [`CommutativeDifferentialGradedAlgebras(R)`](#cat-commutativedifferentialgradedalgebras)
- **refines**, transitively, in Sage's linearization order: [`GradedAlgebras`](#cat-gradedalgebras) · [`Algebras(R)`](#cat-algebras) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`CochainComplexes(R)`](#cat-cochaincomplexes) · [`GradedModules`](#cat-gradedmodules) · [`AssociativeAlgebras(R)`](#cat-associativealgebras) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `DifferentialGradedAlgebras(R)(x, *args, **opts)`

**Operations introduced here** (9 on objects)

*on objects*

- `ElementType()`
  - Associative unital algebras over ``R``.
- `act(module_element, algebra_element)`
- `d(element)`
- `dga()`
- `differential()`
- `differential_component(degree)`
- `graded_algebra()`
- `is_differential_graded_module() -> bool`
- `right_action()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Algebras(R)`](#cat-algebras) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 7 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`CochainComplexes(R)`](#cat-cochaincomplexes) | 4 |  |  |
| [`GradedAlgebras`](#cat-gradedalgebras) | 2 | 2 |  |
| [`GradedModules`](#cat-gradedmodules) | 4 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`AssociativeAlgebras(R)`](#cat-associativealgebras) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `GradedFreeAlgebras(R)` {#cat-gradedfreealgebras}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/algebras/free_algebras.py:523`
- **probed as** `Category of graded free algebras`
- **above** [`FreeAlgebras(R)`](#cat-freealgebras), [`GradedAlgebras`](#cat-gradedalgebras)
- **refines**, transitively, in Sage's linearization order: [`GradedAlgebras`](#cat-gradedalgebras) · [`FreeAlgebras(R)`](#cat-freealgebras) · [`Algebras(R)`](#cat-algebras) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`GradedModules`](#cat-gradedmodules) · [`AssociativeAlgebras(R)`](#cat-associativealgebras) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `GradedFreeAlgebras(R)(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - Associative unital algebras over ``R``.
- `graded_piece(degree)`
  - Return the canonical degree piece of this free construction.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Algebras(R)`](#cat-algebras) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 7 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`GradedAlgebras`](#cat-gradedalgebras) | 2 | 2 |  |
| [`GradedModules`](#cat-gradedmodules) | 4 |  |  |
| [`FreeAlgebras(R)`](#cat-freealgebras) | 3 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`AssociativeAlgebras(R)`](#cat-associativealgebras) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `GroupAlgebras(R)` {#cat-groupalgebras}

Algebras of the form \(R[G]\), interned on their group.

```text
A data subcategory of \(R\)-algebras: an object is \(R[G]\) together with
the group \(G\) framing it.  The multiplication is the chosen morphism
\(R[G]\otimes_R R[G]\to R[G]\) extending the group law, and the augmentation
is determined by the datum, so this refines both chosen-multiplication
algebras and augmented algebras.
```

- **defined at** `src/dzack_research/preamble/categories/algebras/group_algebras.py:45`
- **probed as** `Category of group algebras`
- **above** [`AlgebrasWithChosenMultiplication(R)`](#cat-algebraswithchosenmultiplication), [`AugmentedAlgebras(R)`](#cat-augmentedalgebras)
- **refines**, transitively, in Sage's linearization order: [`AugmentedAlgebras(R)`](#cat-augmentedalgebras) · [`AlgebrasWithChosenMultiplication(R)`](#cat-algebraswithchosenmultiplication) · [`Algebras(R)`](#cat-algebras) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AssociativeAlgebrasWithChosenMultiplication(R)`](#cat-associativealgebraswithchosenmultiplication) · [`AssociativeAlgebras(R)`](#cat-associativealgebras) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `GroupAlgebras(R)(x, *args, **opts)`

**Operations introduced here** (7 on objects)

*on objects*

- `ElementType()`
  - Algebras of the form \(R[G]\), interned on their group.
- `augmentation()` <sub>cached</sub>
  - The algebra morphism \(\varepsilon\colon R[G]\to R\), \(g\mapsto 1\).
- `center()` <sub>cached</sub>
  - The centre \(Z(R[G])\), free on the conjugacy-class sums.
- `group()`
  - The group \(G\) this algebra is \(R[G]\) of.
- `group_inclusion()` <sub>cached</sub>
  - The monoid morphism \(G\to R[G]\), \(g\mapsto g\).
- `is_semisimple() -> bool`
  - Maschke's theorem in its ring form (Lam, FC, Theorem 6.1).
- `regular_representation()` <sub>cached</sub>
  - ``R[G]`` as a module over itself by left multiplication.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Algebras(R)`](#cat-algebras) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 7 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AlgebrasWithChosenMultiplication(R)`](#cat-algebraswithchosenmultiplication) | 3 |  |  |
| [`AssociativeAlgebrasWithChosenMultiplication(R)`](#cat-associativealgebraswithchosenmultiplication) | 3 |  |  |
| [`AugmentedAlgebras(R)`](#cat-augmentedalgebras) | 3 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`AssociativeAlgebras(R)`](#cat-associativealgebras) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `AlternatingAlgebras(R)` {#cat-alternatingalgebras}

Exterior/alternating algebras.

- **defined at** `src/dzack_research/preamble/categories/algebras/free_algebras.py:656`
- **probed as** `Category of alternating algebras`
- **above** [`StrictlyGradedCommutativeAlgebras`](#cat-strictlygradedcommutativealgebras)
- **refines**, transitively, in Sage's linearization order: [`StrictlyGradedCommutativeAlgebras`](#cat-strictlygradedcommutativealgebras) · [`GradedCommutativeAlgebras`](#cat-gradedcommutativealgebras) · [`GradedAlgebras`](#cat-gradedalgebras) · [`Algebras(R)`](#cat-algebras) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`GradedModules`](#cat-gradedmodules) · [`AssociativeAlgebras(R)`](#cat-associativealgebras) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `AlternatingAlgebras(R)(x, *args, **opts)`

**Operations introduced here** (4 on objects)

*on objects*

- `ElementType()`
  - Exterior/alternating algebras.
- `Mor(codomain, category=None)`
- `free_source_module()`
- `graded_piece(degree)`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Algebras(R)`](#cat-algebras) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 7 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`GradedAlgebras`](#cat-gradedalgebras) | 2 | 2 |  |
| [`GradedModules`](#cat-gradedmodules) | 4 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`AssociativeAlgebras(R)`](#cat-associativealgebras) | 1 |  |  |
| [`GradedCommutativeAlgebras`](#cat-gradedcommutativealgebras) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |
| [`StrictlyGradedCommutativeAlgebras`](#cat-strictlygradedcommutativealgebras) | 1 |  |  |

#### `CohomologyAlgebras(R)` {#cat-cohomologyalgebras}

Graded algebras `H^*(B)` represented from a DGA `B`.

- **defined at** `src/dzack_research/preamble/categories/algebras/cohomology_algebras.py:27`
- **probed as** `Category of cohomology algebras`
- **above** [`StrictlyGradedCommutativeAlgebras`](#cat-strictlygradedcommutativealgebras)
- **refines**, transitively, in Sage's linearization order: [`StrictlyGradedCommutativeAlgebras`](#cat-strictlygradedcommutativealgebras) · [`GradedCommutativeAlgebras`](#cat-gradedcommutativealgebras) · [`GradedAlgebras`](#cat-gradedalgebras) · [`Algebras(R)`](#cat-algebras) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`GradedModules`](#cat-gradedmodules) · [`AssociativeAlgebras(R)`](#cat-associativealgebras) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `CohomologyAlgebras(R)(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - Graded algebras ``H^*(B)`` represented from a DGA ``B``.
- `source_dga()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Algebras(R)`](#cat-algebras) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 7 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`GradedAlgebras`](#cat-gradedalgebras) | 2 | 2 |  |
| [`GradedModules`](#cat-gradedmodules) | 4 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`AssociativeAlgebras(R)`](#cat-associativealgebras) | 1 |  |  |
| [`GradedCommutativeAlgebras`](#cat-gradedcommutativealgebras) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |
| [`StrictlyGradedCommutativeAlgebras`](#cat-strictlygradedcommutativealgebras) | 1 |  |  |

#### `SymmetricAlgebras(R)` {#cat-symmetricalgebras}

Symmetric algebras of represented modules.

- **defined at** `src/dzack_research/preamble/categories/algebras/free_algebras.py:620`
- **probed as** `Category of symmetric algebras`
- **above** [`Algebras.Commutative`](#cat-algebras-commutative), [`GradedAlgebras`](#cat-gradedalgebras)
- **refines**, transitively, in Sage's linearization order: [`GradedAlgebras`](#cat-gradedalgebras) · [`Algebras.Commutative`](#cat-algebras-commutative) · [`Algebras(R)`](#cat-algebras) · [`OwnedRings.Commutative`](#cat-ownedrings-commutative) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`GradedModules`](#cat-gradedmodules) · [`AssociativeAlgebras(R)`](#cat-associativealgebras) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `SymmetricAlgebras(R)(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - Symmetric algebras of represented modules.
- `free_source_module()`
  - Return the module whose symmetric algebra this object represents.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 17 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Algebras(R)`](#cat-algebras) | 12 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`GradedAlgebras`](#cat-gradedalgebras) | 2 | 2 |  |
| [`GradedModules`](#cat-gradedmodules) | 4 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`AssociativeAlgebras(R)`](#cat-associativealgebras) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `CommutativeDifferentialGradedAlgebras(R)` {#cat-commutativedifferentialgradedalgebras}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py:152`
- **probed as** `Category of commutative differential graded algebras`
- **above** [`DifferentialGradedAlgebras(R)`](#cat-differentialgradedalgebras), [`GradedCommutativeAlgebras`](#cat-gradedcommutativealgebras)
- **below** [`StrictlyCommutativeDifferentialGradedAlgebras(R)`](#cat-strictlycommutativedifferentialgradedalgebras)
- **refines**, transitively, in Sage's linearization order: [`DifferentialGradedAlgebras(R)`](#cat-differentialgradedalgebras) · [`GradedCommutativeAlgebras`](#cat-gradedcommutativealgebras) · [`GradedAlgebras`](#cat-gradedalgebras) · [`Algebras(R)`](#cat-algebras) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`CochainComplexes(R)`](#cat-cochaincomplexes) · [`GradedModules`](#cat-gradedmodules) · [`AssociativeAlgebras(R)`](#cat-associativealgebras) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `CommutativeDifferentialGradedAlgebras(R)(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Associative unital algebras over ``R``.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Algebras(R)`](#cat-algebras) | 10 |  |  |
| [`DifferentialGradedAlgebras(R)`](#cat-differentialgradedalgebras) | 9 |  |  |
| `SageObject` | 8 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 7 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`CochainComplexes(R)`](#cat-cochaincomplexes) | 4 |  |  |
| [`GradedAlgebras`](#cat-gradedalgebras) | 2 | 2 |  |
| [`GradedModules`](#cat-gradedmodules) | 4 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`AssociativeAlgebras(R)`](#cat-associativealgebras) | 1 |  |  |
| [`GradedCommutativeAlgebras`](#cat-gradedcommutativealgebras) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `StrictlyCommutativeDifferentialGradedAlgebras(R)` {#cat-strictlycommutativedifferentialgradedalgebras}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py:173`
- **probed as** `Category of strictly commutative differential graded algebras`
- **above** [`CommutativeDifferentialGradedAlgebras(R)`](#cat-commutativedifferentialgradedalgebras), [`StrictlyGradedCommutativeAlgebras`](#cat-strictlygradedcommutativealgebras)
- **below** [`DeRhamAlgebras(R)`](#cat-derhamalgebras)
- **refines**, transitively, in Sage's linearization order: [`CommutativeDifferentialGradedAlgebras(R)`](#cat-commutativedifferentialgradedalgebras) · [`DifferentialGradedAlgebras(R)`](#cat-differentialgradedalgebras) · [`StrictlyGradedCommutativeAlgebras`](#cat-strictlygradedcommutativealgebras) · [`GradedCommutativeAlgebras`](#cat-gradedcommutativealgebras) · [`GradedAlgebras`](#cat-gradedalgebras) · [`Algebras(R)`](#cat-algebras) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`CochainComplexes(R)`](#cat-cochaincomplexes) · [`GradedModules`](#cat-gradedmodules) · [`AssociativeAlgebras(R)`](#cat-associativealgebras) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `StrictlyCommutativeDifferentialGradedAlgebras(R)(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Associative unital algebras over ``R``.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Algebras(R)`](#cat-algebras) | 10 |  |  |
| [`DifferentialGradedAlgebras(R)`](#cat-differentialgradedalgebras) | 9 |  |  |
| `SageObject` | 8 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 7 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`CochainComplexes(R)`](#cat-cochaincomplexes) | 4 |  |  |
| [`GradedAlgebras`](#cat-gradedalgebras) | 2 | 2 |  |
| [`GradedModules`](#cat-gradedmodules) | 4 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`AssociativeAlgebras(R)`](#cat-associativealgebras) | 1 |  |  |
| [`CommutativeDifferentialGradedAlgebras(R)`](#cat-commutativedifferentialgradedalgebras) | 1 |  |  |
| [`GradedCommutativeAlgebras`](#cat-gradedcommutativealgebras) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |
| [`StrictlyGradedCommutativeAlgebras`](#cat-strictlygradedcommutativealgebras) | 1 |  |  |

#### `DeRhamAlgebras(R)` {#cat-derhamalgebras}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/algebras/de_rham_algebras.py:22`
- **probed as** `Category of algebraic de Rham algebras`
- **above** [`StrictlyCommutativeDifferentialGradedAlgebras(R)`](#cat-strictlycommutativedifferentialgradedalgebras)
- **refines**, transitively, in Sage's linearization order: [`StrictlyCommutativeDifferentialGradedAlgebras(R)`](#cat-strictlycommutativedifferentialgradedalgebras) · [`CommutativeDifferentialGradedAlgebras(R)`](#cat-commutativedifferentialgradedalgebras) · [`DifferentialGradedAlgebras(R)`](#cat-differentialgradedalgebras) · [`StrictlyGradedCommutativeAlgebras`](#cat-strictlygradedcommutativealgebras) · [`GradedCommutativeAlgebras`](#cat-gradedcommutativealgebras) · [`GradedAlgebras`](#cat-gradedalgebras) · [`Algebras(R)`](#cat-algebras) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`CochainComplexes(R)`](#cat-cochaincomplexes) · [`GradedModules`](#cat-gradedmodules) · [`AssociativeAlgebras(R)`](#cat-associativealgebras) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `DeRhamAlgebras(R)(x, *args, **opts)`

**Operations introduced here** (3 on objects)

*on objects*

- `ElementType()`
  - Associative unital algebras over ``R``.
- `de_rham_source_algebra()`
- `kahler_differentials()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Algebras(R)`](#cat-algebras) | 10 |  |  |
| [`DifferentialGradedAlgebras(R)`](#cat-differentialgradedalgebras) | 9 |  |  |
| `SageObject` | 8 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 7 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`CochainComplexes(R)`](#cat-cochaincomplexes) | 4 |  |  |
| [`GradedAlgebras`](#cat-gradedalgebras) | 2 | 2 |  |
| [`GradedModules`](#cat-gradedmodules) | 4 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`AssociativeAlgebras(R)`](#cat-associativealgebras) | 1 |  |  |
| [`CommutativeDifferentialGradedAlgebras(R)`](#cat-commutativedifferentialgradedalgebras) | 1 |  |  |
| [`GradedCommutativeAlgebras`](#cat-gradedcommutativealgebras) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |
| [`StrictlyCommutativeDifferentialGradedAlgebras(R)`](#cat-strictlycommutativedifferentialgradedalgebras) | 1 |  |  |
| [`StrictlyGradedCommutativeAlgebras`](#cat-strictlygradedcommutativealgebras) | 1 |  |  |

#### `MatrixAlgebras(R)` {#cat-matrixalgebras}

Finite matrix endomorphism Hom objects with their canonical algebra structure.

- **defined at** `src/dzack_research/preamble/categories/algebras/algebras.py:565`
- **probed as** `Category of matrix algebras`
- **above** [`Algebras(R)`](#cat-algebras), [`FramedAlgebras(R)`](#cat-framedalgebras), [`MatrixEndomorphismSpaces(R)`](#cat-matrixendomorphismspaces)
- **refines**, transitively, in Sage's linearization order: [`FramedAlgebras(R)`](#cat-framedalgebras) · [`MatrixEndomorphismSpaces(R)`](#cat-matrixendomorphismspaces) · [`Algebras(R)`](#cat-algebras) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`MatrixSpaces(R)`](#cat-matrixspaces) · [`InternalHomModules(R)`](#cat-internalhommodules) · [`LinearHomModules(R)`](#cat-linearhommodules) · [`FinitelyGeneratedFreeModules(R)`](#cat-finitelygeneratedfreemodules) · [`ModulesWithChosenFinitePresentation(R)`](#cat-moduleswithchosenfinitepresentation) · [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) · [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) · [`FramedFreeModules(R)`](#cat-framedfreemodules) · [`FramedModules(R)`](#cat-framedmodules) · [`FreeModules(R)`](#cat-freemodules) · [`ProjectiveModules(R)`](#cat-projectivemodules) · [`AssociativeAlgebras(R)`](#cat-associativealgebras) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `MatrixAlgebras(R)(x, *args, **opts)`

**Operations introduced here** (4 on objects)

*on objects*

- `ElementType()`
  - Finite matrix endomorphism Hom objects with their canonical algebra structure.
- `algebra_base_ring()`
- `algebra_generating_set()`
- `algebra_generator(label)`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`MatrixSpaces(R)`](#cat-matrixspaces) | 14 | 19 |  |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FramedFreeModules(R)`](#cat-framedfreemodules) | 13 |  |  |
| [`Algebras(R)`](#cat-algebras) | 10 |  |  |
| [`FinitelyGeneratedModules(R)`](#cat-finitelygeneratedmodules) | 10 |  |  |
| [`FramedModules(R)`](#cat-framedmodules) | 10 |  |  |
| [`FramedAlgebras(R)`](#cat-framedalgebras) | 8 |  |  |
| `SageObject` | 8 |  |  |
| [`LinearHomModules(R)`](#cat-linearhommodules) | 7 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 7 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`MatrixEndomorphismSpaces(R)`](#cat-matrixendomorphismspaces) | 3 | 1 |  |
| [`FinitelyGeneratedFreeModules(R)`](#cat-finitelygeneratedfreemodules) | 3 |  |  |
| [`ProjectiveModules(R)`](#cat-projectivemodules) | 3 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`FinitelyPresentedModules(R)`](#cat-finitelypresentedmodules) | 2 |  |  |
| [`FreeModules(R)`](#cat-freemodules) | 2 |  |  |
| [`InternalHomModules(R)`](#cat-internalhommodules) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`AssociativeAlgebras(R)`](#cat-associativealgebras) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`ModulesWithChosenFinitePresentation(R)`](#cat-moduleswithchosenfinitepresentation) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `AlgebraHomset` {#cat-algebrahomset}

Shared equality protocol for represented algebra Hom parents.

- **defined at** `src/dzack_research/preamble/categories/algebras/algebras.py:1316`
- **not placed**: `AlgebraHomset(hom_family, domain, codomain)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `CohomologyAlgebraHomset` {#cat-cohomologyalgebrahomset}

A represented Hom object which is both a Sage Homset and a category.

```text
This is the live counterpart of the archived owned Hom-category base.  It
keeps Sage's hard requirement that every ``Morphism`` be parented by an
actual ``Homset``, while also making that same parent the discrete category
``Hom_C(A,B)``.  Concrete categories subclass this and add enrichment to
the *same object*.
```

- **defined at** `src/dzack_research/preamble/categories/algebras/cohomology_algebras.py:169`
- **not placed**: `CohomologyAlgebraHomset(hom_family, domain, codomain)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `DGAHomset` {#cat-dgahomset}

A represented Hom object which is both a Sage Homset and a category.

```text
This is the live counterpart of the archived owned Hom-category base.  It
keeps Sage's hard requirement that every ``Morphism`` be parented by an
actual ``Homset``, while also making that same parent the discrete category
``Hom_C(A,B)``.  Concrete categories subclass this and add enrichment to
the *same object*.
```

- **defined at** `src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py:271`
- **not placed**: `DGAHomset(hom_family, domain, codomain)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `DerivationSpace` {#cat-derivationspace}

The `A`-module `Der_R(A,M)` with its restricted Hom inclusion.

```text
The actual subobject of ``Hom_R(A,Res_R M)`` is
``Res_R Der_R(A,M)``.  Keeping these two scalar structures distinct is
essential: the derivation module is canonically an ``A``-module, whereas
its inclusion into the existing ``R``-linear Hom is only ``R``-linear.
```

- **defined at** `src/dzack_research/preamble/categories/algebras/derivations.py:313`
- **not placed**: `DerivationSpace(family, algebra, restricted_target)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `GradedAlgebraHomset` {#cat-gradedalgebrahomset}

A represented Hom object which is both a Sage Homset and a category.

```text
This is the live counterpart of the archived owned Hom-category base.  It
keeps Sage's hard requirement that every ``Morphism`` be parented by an
actual ``Homset``, while also making that same parent the discrete category
``Hom_C(A,B)``.  Concrete categories subclass this and add enrichment to
the *same object*.
```

- **defined at** `src/dzack_research/preamble/categories/algebras/graded_algebras.py:102`
- **not placed**: `GradedAlgebraHomset(hom_family, domain, codomain)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `GradedAlgebras` {#cat-gradedalgebras}

Associative unital algebras graded by a monoid.

```text
Let \(M\) be a monoid. An \(M\)-graded \(R\)-algebra is an associative
unital \(R\)-algebra \(A\) together with a direct-sum decomposition
\(A = \bigoplus_{m \in M} A_m\) of the underlying module such that the
product sends \(A_m \times A_{m'}\) into \(A_{mm'}\).

The default monoid is \(\mathbb{Z}\) (additive), which is Sage's graded
algebra axiom. The additive monoid \(\mathbb{N}\) is the nonnegative
case. This is the nLab definition of a graded algebra; Stacks Project
tag 00JL is the special case \(M = \mathbb{N}\).
```

- **defined at** `src/dzack_research/preamble/categories/algebras/graded_algebras.py:156`
- **not placed**: `GradedAlgebras(base_ring, grading_monoid: sage.structure.parent.Parent)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)
- **below** [`DifferentialGradedAlgebras(R)`](#cat-differentialgradedalgebras), [`GradedFreeAlgebras(R)`](#cat-gradedfreealgebras), [`SymmetricAlgebras(R)`](#cat-symmetricalgebras), [`TensorAlgebras(R)`](#cat-tensoralgebras)
- **specimens** `GradedLebesgueAlgebra`

**Operations introduced here** (1 on objects, 2 on elements)

*on objects*

- `homogeneous_degree(element)`
  - Return the selected degree of one nonzero homogeneous element.

*on elements*

- `degree()`
- `is_homogeneous()`

#### `GradedAugmentedAlgebras` {#cat-gradedaugmentedalgebras}

Graded algebras over an augmented \(R\)-algebra.

```text
Let \(B\) be an augmented \(R\)-algebra and let \(A\) be a graded
\(B\)-algebra that is itself augmented over \(B\). The composite of
the two augmentations is an augmentation of \(A\) over \(R\):
\[
A \to B \to R.
\]
For a connected grading, \(B = A_u = R\) and the second map is the
identity. This is the nLab graded-plus-augmented situation
(Cartan–Eilenberg: a supplemented graded algebra).
```

- **defined at** `src/dzack_research/preamble/categories/algebras/augmented_algebras.py:77`
- **not placed**: `GradedAugmentedAlgebras(base_ring, grading_monoid)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

**Operations introduced here** (1 on objects)

*on objects*

- `ground_ring_augmentation()`
  - The composite augmentation \(A\to A_u\to R\).

#### `GradedCommutativeAlgebras` {#cat-gradedcommutativealgebras}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/algebras/graded_commutative_algebras.py:21`
- **not placed**: `GradedCommutativeAlgebras(base_ring, grading_monoid)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)
- **below** [`CommutativeDifferentialGradedAlgebras(R)`](#cat-commutativedifferentialgradedalgebras)

#### `GradedDerivationSpace` {#cat-gradedderivationspace}

The `R`-submodule of degree-`r` graded derivations in `Hom_R`.

- **defined at** `src/dzack_research/preamble/categories/algebras/derivations.py:631`
- **not placed**: `GradedDerivationSpace(family, algebra, target)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `StrictlyGradedCommutativeAlgebras` {#cat-strictlygradedcommutativealgebras}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/algebras/graded_commutative_algebras.py:56`
- **not placed**: `StrictlyGradedCommutativeAlgebras(base_ring, grading_monoid)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)
- **below** [`AlternatingAlgebras(R)`](#cat-alternatingalgebras), [`CohomologyAlgebras(R)`](#cat-cohomologyalgebras), [`StrictlyCommutativeDifferentialGradedAlgebras(R)`](#cat-strictlycommutativedifferentialgradedalgebras)

### Functors and adjunctions

#### `GroupAlgebraFunctor` {#fun-groupalgebrafunctor}

\(R[-]\colon \mathbf{Grp}\to \mathbf{Alg}_R\).

```text
On a group morphism \(f\colon H\to G\) it is the algebra morphism
\(R[H]\to R[G]\) extending \(f\) \(R\)-linearly; for a subgroup
inclusion this is the ring morphism \(R[H]\to R[G]\).
```

- **defined at** `src/dzack_research/preamble/categories/algebras/group_algebras.py:176`
- **built by** `GroupAlgebraFunctor(base_ring)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `base_ring()`

### Objects

#### `RestrictedGradedAlgebra` <sub>OBJECT</sub>

The same graded ring read over the constants of its degree-zero algebra.

- **defined at** `src/dzack_research/preamble/categories/algebras/restricted_graded_algebras.py:32`
- **built by** `RestrictedGradedAlgebra(extension_algebra, ring_map, *, extra_categories=())`

**Operations**

- `Element(parent, components) -> None`
  - A finite family of homogeneous components.
- `algebra_base_ring()`
- `algebra_generating_set()`
- `algebra_generator(label)`
  - Return the generator at a point of the coproduct framing.
- `algebra_structure_morphism()`
- `degree_zero_algebra()`
- `degree_zero_element(element)`
- `extension_algebra()`
- `from_degree_zero(element)`
- `is_commutative()`
  - The same multiplication read over fewer scalars commutes exactly when it did.
- `multiply(left, right)`
- `one()`
- `realize(element)`
  - Return the same finite homogeneous sum in the extension algebra.
- `ring_map()`

### Elements

#### `CohomologyAlgebraElement` <sub>ELEMENT</sub>

A finite family of homogeneous components.

- **defined at** `src/dzack_research/preamble/categories/algebras/cohomology_algebras.py:52`
- **built by** `CohomologyAlgebraElement(parent, components)`

#### `Derivation` <sub>ELEMENT</sub>

An actual `R`-linear arrow `A -> Res_R(M)` satisfying Leibniz.

```text
The public codomain of a derivation remains the original ``A``-module
``M``.  :meth:`underlying_linear_morphism` is the corresponding element of
the canonical ``Hom_R(A, Res_R(M))`` containing this derivation subobject.
```

- **defined at** `src/dzack_research/preamble/categories/algebras/derivations.py:90`
- **built by** `Derivation(parent, generator_images)`

**Operations**

- `as_morphism()`
- `codomain()`
- `domain()`
- `generator_image(label)`
- `restricted_codomain()`
- `underlying_linear_morphism()`

#### `Differential` <sub>ELEMENT</sub>

A represented degree-one square-zero graded derivation.

- **defined at** `src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py:194`
- **built by** `Differential(algebra, function)`

#### `GradedDerivation` <sub>ELEMENT</sub>

A homogeneous graded derivation of a represented graded algebra.

```text
For shift ``r`` this represents a map ``D : A^p -> M^(p+r)`` satisfying
``D(ab) = D(a)b + (-1)^(r p) a D(b)`` on homogeneous ``a``.  It is an
actual ``R``-linear morphism, lying in a represented submodule of
``Hom_R(A,M)``.
```

- **defined at** `src/dzack_research/preamble/categories/algebras/derivations.py:530`
- **built by** `GradedDerivation(parent, function)`

**Operations**

- `algebra()`
- `as_morphism()`
- `check_on_generators() -> bool`
  - Check degree and graded Leibniz on a selected finite algebra framing.
- `degree_shift()`
- `target()`
- `underlying_linear_morphism()`

#### `RestrictedGradedAlgebraElement` <sub>ELEMENT</sub>

A finite family of homogeneous components.

- **defined at** `src/dzack_research/preamble/categories/algebras/restricted_graded_algebras.py:27`
- **built by** `RestrictedGradedAlgebraElement(parent, components)`

### Morphisms and homsets

#### `AlgebraMorphism` <sub>MORPHISM</sub>

An `R`-algebra morphism specified by the images of algebra generators.

- **defined at** `src/dzack_research/preamble/categories/algebras/algebras.py:975`
- **built by** `AlgebraMorphism(parent, images)`

**Operations**

- `algebra_generator_images()`
- `algebra_generator_morphism()`

#### `CohomologyAlgebraMorphism` <sub>MORPHISM</sub>

The graded algebra morphism induced on cohomology by a DGA morphism.

- **defined at** `src/dzack_research/preamble/categories/algebras/cohomology_algebras.py:127`
- **built by** `CohomologyAlgebraMorphism(parent, dga_morphism)`

**Operations**

- `underlying_dga_morphism()`

#### `DGAMorphism` <sub>MORPHISM</sub>

Map(parent, codomain=None)

```text
File: /home/dzack/gitclones/sage-dev-allopts/src/sage/categories/map.pyx (starting at line 83)

Basic class for all maps.

.. NOTE::

    The call method is of course not implemented in this base class. This must
    be done in the sub classes, by overloading ``_call_`` and possibly also
    ``_call_with_args``.

EXAMPLES:

Usually, instances of this class will not be constructed directly, but
for example like this::

    sage: from sage.categories.morphism import SetMorphism
    sage: X.<x> = ZZ[]
    sage: Y = ZZ
    sage: phi = SetMorphism(Hom(X, Y, Rings()), lambda p: p[0])
    sage: phi(x^2+2*x-1)
    -1
    sage: R.<x,y> = QQ[]
    sage: f = R.hom([x+y, x-y], R)
    sage: f(x^2+2*x-1)
    x^2 + 2*x*y + y^2 + 2*x + 2*y - 1
```

- **defined at** `src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py:209`
- **built by** `DGAMorphism(parent, function)`

**Operations**

- `component(degree)`
  - Return the degree-``degree`` linear component of this DGA map.

#### `DegreewiseLinearMorphism` <sub>MORPHISM</sub>

An `R`-linear map between two represented homogeneous pieces.

```text
This is deliberately independent of a selected finite framing. When the
source and target pieces admit the finite module-morphism backend,
:meth:`represented_module_morphism` exposes it and therefore enables the
usual kernel/image algorithms; otherwise the component remains a genuine
morphism with exact evaluation but no fabricated finite presentation.
```

- **defined at** `src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py:25`
- **built by** `DegreewiseLinearMorphism(domain, codomain, function)`

**Operations**

- `image()`
- `kernel()`
- `represented_module_morphism()`

#### `DifferentialComponentMorphism` <sub>MORPHISM</sub>

A degreewise component of a represented DGA differential.

- **defined at** `src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py:79`
- **built by** `DifferentialComponentMorphism(domain, codomain, function)`

#### `GradedAlgebraMorphism` <sub>MORPHISM</sub>

An algebra morphism preserving the selected grading.

- **defined at** `src/dzack_research/preamble/categories/algebras/graded_algebras.py:39`
- **built by** `GradedAlgebraMorphism(parent, images, *, check_degrees=True)`

**Operations**

- `underlying_algebra_morphism()`

### Functions

#### `AlternatingAlgebraOf` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/algebras/framed_free_algebras.py:162`
- **built by** `AlternatingAlgebraOf(module)`

#### `AlternatingAlgebraOn` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/algebras/framed_free_algebras.py:49`
- **built by** `AlternatingAlgebraOn(base_ring, algebra_generating_set)`

#### `CohomologyAlgebra` <sub>FUNCTION</sub>

Return the graded algebra `H^*(dga)` with descended multiplication.

- **defined at** `src/dzack_research/preamble/categories/algebras/cohomology_algebras.py:193`
- **built by** `CohomologyAlgebra(dga)`

#### `CommutativeAlgebras` <sub>FUNCTION</sub>

The category of commutative `R`-algebras.

```text
The session name for ``Algebras(R).Commutative()``: commutativity is an
axiom on the multiplication, and this is the category it cuts out.
```

- **defined at** `src/dzack_research/preamble/categories/algebras/algebras.py:1803`
- **built by** `CommutativeAlgebras(base_ring)`

#### `DeRhamAlgebra` <sub>FUNCTION</sub>

Return the strictly commutative DGA `Omega^*_{A/R}`.

```text
The exterior algebra itself is the existing authoritative
``AlternatingAlgebraOf(Omega^1_{A/R})``.  The public DGA is its restriction
from the degree-zero coefficient algebra ``A`` to the differential
constants ``R`` along the selected algebra structure morphism.
```

- **defined at** `src/dzack_research/preamble/categories/algebras/de_rham_algebras.py:101`
- **built by** `DeRhamAlgebra(algebra)`

#### `Derivations` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/algebras/derivations.py:515`
- **built by** `Derivations(algebra, target_module) -> dzack_research.preamble.categories.algebras.derivations.DerivationSpace`

#### `FinitelyPresentedAlgebra` <sub>FUNCTION</sub>

Return the selected quotient `R[S] / (relations)`.

- **defined at** `src/dzack_research/preamble/categories/algebras/free_algebras.py:422`
- **built by** `FinitelyPresentedAlgebra(presentation_ring, relations, *, _extra_categories=(), _extra_construction_data=None, _free_source_module=None)`

#### `FinitelyPresentedAlgebraOn` <sub>FUNCTION</sub>

Construct `R[S] / (relations)` with the displayed finite presentation.

- **defined at** `src/dzack_research/preamble/categories/algebras/finitely_presented_algebras.py:225`
- **built by** `FinitelyPresentedAlgebraOn(base_ring, algebra_generating_set, relations)`

#### `FreeAlgebraOn` <sub>FUNCTION</sub>

Return the free commutative algebra `R[S] = Sym(F_R(S))`.

- **defined at** `src/dzack_research/preamble/categories/algebras/free_algebras.py:93`
- **built by** `FreeAlgebraOn(base_ring, algebra_generating_set)`

#### `GradedCommutator` <sub>FUNCTION</sub>

Return the graded commutator of endo-derivations.

```text
For homogeneous derivations of shifts ``p`` and ``q`` this is
``D E - (-1)^(pq) E D`` and has shift ``p+q``.
```

- **defined at** `src/dzack_research/preamble/categories/algebras/cartan_calculus.py:58`
- **built by** `GradedCommutator(left, right)`

#### `GradedDerivations` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/algebras/derivations.py:758`
- **built by** `GradedDerivations(algebra, target=None, shift=0) -> dzack_research.preamble.categories.algebras.derivations.GradedDerivationSpace`

#### `GroupAlgebra` <sub>FUNCTION</sub>

The group algebra \(R[G]\): the free \(R\)-module on \(G\), multiplied by the group law.

- **defined at** `src/dzack_research/preamble/categories/algebras/group_algebras.py:149`
- **built by** `GroupAlgebra(base_ring, group)`

#### `InteriorProduct` <sub>FUNCTION</sub>

Return contraction `i_X` as a degree `-1` derivation of `DR(A)`.

- **defined at** `src/dzack_research/preamble/categories/algebras/cartan_calculus.py:101`
- **built by** `InteriorProduct(vector_field)`

#### `KahlerDifferentials` <sub>FUNCTION</sub>

Return `Omega^1_{A/R}` with its universal `R`-derivation.

- **defined at** `src/dzack_research/preamble/categories/algebras/kahler_differentials.py:236`
- **built by** `KahlerDifferentials(algebra)`

#### `LieBracket` <sub>FUNCTION</sub>

Return the commutator `[left,right]` of two vector fields.

- **defined at** `src/dzack_research/preamble/categories/algebras/cartan_calculus.py:39`
- **built by** `LieBracket(left, right)`

#### `LieDerivative` <sub>FUNCTION</sub>

Return `L_X = [d,i_X]` as a degree-zero derivation of `DR(A)`.

- **defined at** `src/dzack_research/preamble/categories/algebras/cartan_calculus.py:156`
- **built by** `LieDerivative(vector_field)`

#### `SymmetricAlgebraOf` <sub>FUNCTION</sub>

Return \(\operatorname{Sym}_R(M)\) with `M`'s linear relations.

- **defined at** `src/dzack_research/preamble/categories/algebras/framed_free_algebras.py:91`
- **built by** `SymmetricAlgebraOf(module)`

#### `SymmetricAlgebraOn` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/algebras/free_algebras.py:125`
- **built by** `SymmetricAlgebraOn(base_ring, algebra_generating_set)`

#### `TensorAlgebraOf` <sub>FUNCTION</sub>

Return \(T_R(M)\), including the linear relations of `M`.

- **defined at** `src/dzack_research/preamble/categories/algebras/framed_free_algebras.py:77`
- **built by** `TensorAlgebraOf(module)`

#### `TensorAlgebraOn` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/algebras/free_algebras.py:140`
- **built by** `TensorAlgebraOn(base_ring, algebra_generating_set)`

#### `VectorFields` <sub>FUNCTION</sub>

Return `Der_R(A,A)` as the existing derivation module.

- **defined at** `src/dzack_research/preamble/categories/algebras/cartan_calculus.py:22`
- **built by** `VectorFields(algebra)`

#### `algebra_from_multiplication` <sub>FUNCTION</sub>

Return the algebra presented by an \(R\)-module morphism \(A\otimes_R A\to A\).

```text
``unit`` and ``commutative`` state what the caller already knows about
the multiplication.  When ``unit`` is ``None`` the two-sided unit is
solved for on the module generating set; when ``commutative`` is
``None`` commutativity is decided there.
```

- **defined at** `src/dzack_research/preamble/categories/algebras/algebras.py:1619`
- **built by** `algebra_from_multiplication(multiplication, base_ring=None, unital=True, *, extra_categories=(), extra_construction_data=None, unit=None, commutative=None)`

#### `algebra_homset` <sub>FUNCTION</sub>

`Hom_{R-Alg}(domain, codomain)` for `R` the base of `domain`; both must be placed over `R`.

- **defined at** `src/dzack_research/preamble/categories/algebras/algebras.py:1334`
- **built by** `algebra_homset(domain, codomain) -> dzack_research.preamble.categories.algebras.algebras.AlgebraHomset`

#### `augmented_algebra` <sub>FUNCTION</sub>

Return the domain of `augmentation`, as an augmented algebra.

```text
An augmentation of an \(R\)-algebra is an algebra morphism \(A\to R\).
When \(A\) is graded, the unit-degree piece \(A_u\) is a subalgebra, and
\(A\) is an \(A_u\)-algebra; an augmentation of that algebra is a map
\(A\to A_u\).
```

- **defined at** `src/dzack_research/preamble/categories/algebras/augmented_algebras.py:199`
- **built by** `augmented_algebra(augmentation)`

#### `cohomology_algebra_homset` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/algebras/cohomology_algebras.py:186`
- **built by** `cohomology_algebra_homset(domain, codomain)`

#### `commutative_algebra_coproduct` <sub>FUNCTION</sub>

Return `left tensor_R right`, the coproduct in commutative algebras.

- **defined at** `src/dzack_research/preamble/categories/algebras/algebras.py:1339`
- **built by** `commutative_algebra_coproduct(left, right)`

#### `commutative_algebra_pushout` <sub>FUNCTION</sub>

Return the pushout of two commutative-algebra maps with common domain.

- **defined at** `src/dzack_research/preamble/categories/algebras/algebras.py:1348`
- **built by** `commutative_algebra_pushout(left_map, right_map)`

#### `dga_homset` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/algebras/differential_graded_algebras.py:301`
- **built by** `dga_homset(domain, codomain)`

#### `graded_algebra_homset` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/algebras/graded_algebras.py:143`
- **built by** `graded_algebra_homset(domain, codomain) -> dzack_research.preamble.categories.algebras.graded_algebras.GradedAlgebraHomset`

#### `own_algebra` <sub>FUNCTION</sub>

Return the algebra object presented by the supplied ring map.

- **defined at** `src/dzack_research/preamble/categories/algebras/algebras.py:1678`
- **built by** `own_algebra(structure_map)`

#### `restrict_algebra_scalars` <sub>FUNCTION</sub>

Return `Res_f(B)` for `f : R -> S` and an `S`-algebra `B`.

```text
Scalar restriction itself is global: the returned algebra always retains
the exact underlying computation ring of ``B`` and composes its structure
map with ``f``.  The stronger chosen finite presentation is retained only
when it can be constructed from chosen presentations of both ``S/R`` and
``B/S`` along the selected structure map of ``S``.
```

- **defined at** `src/dzack_research/preamble/categories/algebras/restricted_scalars.py:325`
- **built by** `restrict_algebra_scalars(algebra, ring_map)`

#### `restrict_graded_algebra_scalars` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/algebras/restricted_graded_algebras.py:175`
- **built by** `restrict_graded_algebra_scalars(algebra, ring_map)`

## Groups, Profinite Groups & Galois Theory

> Groups, Finitely presented groups, G-Sets, Actions, Profinite groups, Absolute Galois groups, Characters, and Inertia.

```mermaid
graph RL
  AbsoluteGaloisGroups["AbsoluteGaloisGroups"]
  AbsoluteGaloisGroupsOfFiniteFields["AbsoluteGaloisGroupsOfFiniteFields"]
  AdditiveGroups["AdditiveGroups"]
  AdditiveGroups.AdditiveCommutative["AdditiveGroups.AdditiveCommutative"]
  AdditiveMagmas["AdditiveMagmas"]
  AdditiveMonoids["AdditiveMonoids"]
  AdditiveSemigroups["AdditiveSemigroups"]
  CyclicGroups["CyclicGroups"]
  FinitelyGeneratedGroups["FinitelyGeneratedGroups"]
  FinitelyPresentedGroups["FinitelyPresentedGroups"]
  Groups["Groups"]
  GroupsWithChosenFiniteGeneratingSet["GroupsWithChosenFiniteGeneratingSet"]
  GroupsWithChosenFinitePresentation["GroupsWithChosenFinitePresentation"]
  Magmas["Magmas"]
  Monoids["Monoids"]
  OpenAbsoluteGaloisSubgroups["OpenAbsoluteGaloisSubgroups"]
  OrbitSets["OrbitSets"]
  OwnedFinitelyGeneratedGroups["OwnedFinitelyGeneratedGroups"]
  OwnedFinitelyPresentedGroups["OwnedFinitelyPresentedGroups"]
  OwnedGroups["OwnedGroups"]
  OwnedGroups.Commutative["OwnedGroups.Commutative"]
  ProfiniteGroups["ProfiniteGroups"]
  Semigroups["Semigroups"]
  TopologicalGroups["TopologicalGroups"]
  groups["groups"]
  Sets("Sets")
  Sets.Finite("Sets.Finite")
  AbsoluteGaloisGroups --> ProfiniteGroups
  AbsoluteGaloisGroupsOfFiniteFields --> AbsoluteGaloisGroups
  AbsoluteGaloisGroupsOfFiniteFields --> OwnedGroups.Commutative
  AdditiveGroups --> AdditiveMonoids
  AdditiveGroups.AdditiveCommutative --> AdditiveGroups
  AdditiveMagmas --> Sets
  AdditiveMonoids --> AdditiveSemigroups
  AdditiveSemigroups --> AdditiveMagmas
  CyclicGroups --> GroupsWithChosenFiniteGeneratingSet
  CyclicGroups --> OwnedGroups.Commutative
  FinitelyGeneratedGroups --> OwnedGroups
  FinitelyPresentedGroups --> OwnedFinitelyGeneratedGroups
  Groups --> Monoids
  GroupsWithChosenFiniteGeneratingSet --> OwnedFinitelyGeneratedGroups
  GroupsWithChosenFinitePresentation --> GroupsWithChosenFiniteGeneratingSet
  GroupsWithChosenFinitePresentation --> OwnedFinitelyPresentedGroups
  Magmas --> Sets
  Monoids --> Semigroups
  OpenAbsoluteGaloisSubgroups --> AbsoluteGaloisGroups
  OrbitSets --> Sets.Finite
  OwnedFinitelyGeneratedGroups --> OwnedGroups
  OwnedFinitelyPresentedGroups --> OwnedFinitelyGeneratedGroups
  OwnedGroups --> Monoids
  OwnedGroups.Commutative --> OwnedGroups
  ProfiniteGroups --> TopologicalGroups
  Semigroups --> Magmas
  TopologicalGroups --> OwnedGroups
  groups --> Monoids
  classDef outside stroke-dasharray:6 4,fill:#f8fafc;
  class Sets,Sets.Finite outside;
```

### Categories

Ordered by depth: the least structured first.

#### `AdditiveMagmas` {#cat-additivemagmas}

- **not exported**: reachable only as a supercategory
- **probed as** `Category of additive magmas`
- **above** [`Sets`](#cat-sets)
- **below** [`AdditiveSemigroups`](#cat-additivesemigroups)
- **refines**, transitively, in Sage's linearization order: [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `AdditiveMagmas(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - The owned category of sets.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `Magmas` {#cat-magmas}

- **not exported**: reachable only as a supercategory
- **probed as** `Category of magmas`
- **above** [`Sets`](#cat-sets)
- **below** [`Semigroups`](#cat-semigroups)
- **refines**, transitively, in Sage's linearization order: [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `Magmas(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - The owned category of sets.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `AdditiveSemigroups` {#cat-additivesemigroups}

- **not exported**: reachable only as a supercategory
- **probed as** `Category of additive semigroups`
- **above** [`AdditiveMagmas`](#cat-additivemagmas)
- **below** [`AdditiveMonoids`](#cat-additivemonoids)
- **refines**, transitively, in Sage's linearization order: [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `AdditiveSemigroups(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - The owned category of sets.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `OrbitSets` {#cat-orbitsets}

The finite orbit quotients \(X/G\) of a finite \(G\)-set.

- **defined at** `src/dzack_research/preamble/categories/group/g_sets.py:254`
- **probed as** `Category of orbit sets`
- **above** [`Sets.Finite`](#cat-sets-finite)
- **refines**, transitively, in Sage's linearization order: [`Sets.Finite`](#cat-sets-finite) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `OrbitSets(x, *args, **opts)`

**Operations introduced here** (9 on objects, 2 on elements)

*on objects*

- `ElementType(parent, index) -> None`
  - What an orbit is.
- `cardinality()`
- `g_set()`
- `index(orbit)`
- `orbit_of(point)`
- `orbit_points(orbit)`
- `position(orbit)`
- `rank(orbit)`
- `unrank(position)`

*on elements*

- `points()`
- `representative()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `SageObject` | 8 | 8 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `Element` |  | 9 |  |
| [`Sets`](#cat-sets) | 8 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `Semigroups` {#cat-semigroups}

- **not exported**: reachable only as a supercategory
- **probed as** `Category of semigroups`
- **above** [`Magmas`](#cat-magmas)
- **below** [`Monoids`](#cat-monoids), [`OwnedRngs`](#cat-ownedrngs)
- **refines**, transitively, in Sage's linearization order: [`Magmas`](#cat-magmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `Semigroups(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - The owned category of sets.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `AdditiveMonoids` {#cat-additivemonoids}

- **not exported**: reachable only as a supercategory
- **probed as** `Category of additive monoids`
- **above** [`AdditiveSemigroups`](#cat-additivesemigroups)
- **below** [`AdditiveGroups`](#cat-additivegroups), [`OwnedSemirings`](#cat-ownedsemirings)
- **refines**, transitively, in Sage's linearization order: [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `AdditiveMonoids(x, *args, **opts)`
- **specimens** `NonNegativeReals`

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - The owned category of sets.
- `monoidal_unit()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `Monoids` {#cat-monoids}

- **not exported**: reachable only as a supercategory
- **probed as** `Category of monoids`
- **above** [`Semigroups`](#cat-semigroups)
- **below** [`Groups`](#cat-groups), [`OwnedGroups`](#cat-ownedgroups), [`OwnedSemirings`](#cat-ownedsemirings), [`groups`](#cat-groups)
- **refines**, transitively, in Sage's linearization order: [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `Monoids(x, *args, **opts)`
- **specimens** `UnitInterval`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - The owned category of sets.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `AdditiveGroups` {#cat-additivegroups}

- **not exported**: reachable only as a supercategory
- **probed as** `Category of additive groups`
- **above** [`AdditiveMonoids`](#cat-additivemonoids)
- **below** [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative), [`OwnedRngs`](#cat-ownedrngs)
- **refines**, transitively, in Sage's linearization order: [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `AdditiveGroups(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - The owned category of sets.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `Groups` {#cat-groups}

Groups whose notebook-facing group interface is owned by the preamble.

- **defined at** `src/dzack_research/preamble/categories/group/groups.py:1453`
- **probed as** `Category of groups`
- **above** [`Monoids`](#cat-monoids)
- **refines**, transitively, in Sage's linearization order: [`Monoids`](#cat-monoids) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `Groups(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedGroups`](#cat-ownedgroups) | 15 | 1 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `OwnedGroups` {#cat-ownedgroups}

Groups whose notebook-facing group interface is owned by the preamble.

- **defined at** `src/dzack_research/preamble/categories/group/groups.py:1453`
- **probed as** `Category of groups`
- **above** [`Monoids`](#cat-monoids)
- **below** [`FinitelyGeneratedGroups`](#cat-finitelygeneratedgroups), [`OwnedFinitelyGeneratedGroups`](#cat-ownedfinitelygeneratedgroups), [`OwnedGroups.Commutative`](#cat-ownedgroups-commutative), [`TopologicalGroups`](#cat-topologicalgroups)
- **refines**, transitively, in Sage's linearization order: [`Monoids`](#cat-monoids) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `OwnedGroups(x, *args, **opts)`
- **specimens** `Involutions.I_dP`, `Involutions.I_En`, `Involutions.I_Nik`

**Operations introduced here** (15 on objects, 1 on elements)

*on objects*

- `ElementType()`
  - The owned category of sets.
- `Aut()` <sub>cached</sub>
- `End()`
- `Mor(codomain, category=None)`
- `cardinality()`
- `inclusion()`
- `is_abelian()`
- `is_arithmetic_group()`
- `is_finite()`
- `is_finitely_generated()`
- `is_finitely_presented()`
- `is_isomorphic_to(other)`
- `order()`
  - Return the group order as an integer when finite, else its cardinality.
- `subgroup(generators)`
- `supergroup()`

*on elements*

- `inverse()`
  - Return the group inverse.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `groups` {#cat-groups}

Groups whose notebook-facing group interface is owned by the preamble.

- **defined at** `src/dzack_research/preamble/categories/group/groups.py:1453`
- **probed as** `Category of groups`
- **above** [`Monoids`](#cat-monoids)
- **refines**, transitively, in Sage's linearization order: [`Monoids`](#cat-monoids) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `groups(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedGroups`](#cat-ownedgroups) | 15 | 1 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `AdditiveGroups.AdditiveCommutative` {#cat-additivegroups-additivecommutative}

Additive groups whose addition is commutative.

- **not exported**: reachable only as a supercategory
- **probed as** `Category of commutative additive groups`
- **above** [`AdditiveGroups`](#cat-additivegroups)
- **below** [`Modules(R)`](#cat-modules)
- **refines**, transitively, in Sage's linearization order: [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `AdditiveGroups.AdditiveCommutative(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `FinitelyGeneratedGroups` {#cat-finitelygeneratedgroups}

Groups admitting some finite generating set.

- **defined at** `src/dzack_research/preamble/categories/group/groups.py:1848`
- **probed as** `Category of finitely generated groups`
- **above** [`OwnedGroups`](#cat-ownedgroups)
- **refines**, transitively, in Sage's linearization order: [`OwnedGroups`](#cat-ownedgroups) · [`Monoids`](#cat-monoids) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `FinitelyGeneratedGroups(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedGroups`](#cat-ownedgroups) | 15 | 1 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`OwnedFinitelyGeneratedGroups`](#cat-ownedfinitelygeneratedgroups) | 2 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `OwnedFinitelyGeneratedGroups` {#cat-ownedfinitelygeneratedgroups}

Groups admitting some finite generating set.

- **defined at** `src/dzack_research/preamble/categories/group/groups.py:1848`
- **probed as** `Category of finitely generated groups`
- **above** [`OwnedGroups`](#cat-ownedgroups)
- **below** [`FinitelyPresentedGroups`](#cat-finitelypresentedgroups), [`GroupsWithChosenFiniteGeneratingSet`](#cat-groupswithchosenfinitegeneratingset), [`OwnedFinitelyPresentedGroups`](#cat-ownedfinitelypresentedgroups)
- **refines**, transitively, in Sage's linearization order: [`OwnedGroups`](#cat-ownedgroups) · [`Monoids`](#cat-monoids) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `OwnedFinitelyGeneratedGroups(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - Groups admitting some finite generating set.
- `is_finitely_generated()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedGroups`](#cat-ownedgroups) | 15 | 1 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `OwnedGroups.Commutative` {#cat-ownedgroups-commutative}

- **not exported**: reachable only as a supercategory
- **probed as** `Category of abelian groups`
- **above** [`OwnedGroups`](#cat-ownedgroups)
- **below** [`AbsoluteGaloisGroupsOfFiniteFields`](#cat-absolutegaloisgroupsoffinitefields), [`CyclicGroups`](#cat-cyclicgroups)
- **refines**, transitively, in Sage's linearization order: [`OwnedGroups`](#cat-ownedgroups) · [`Monoids`](#cat-monoids) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `OwnedGroups.Commutative(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedGroups`](#cat-ownedgroups) | 20 | 1 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `TopologicalGroups` {#cat-topologicalgroups}

Owned groups equipped with a represented compatible topology.

- **not exported**: reachable only as a supercategory
- **probed as** `Category of topological groups`
- **above** [`OwnedGroups`](#cat-ownedgroups)
- **below** [`ProfiniteGroups`](#cat-profinitegroups)
- **refines**, transitively, in Sage's linearization order: [`OwnedGroups`](#cat-ownedgroups) · [`Monoids`](#cat-monoids) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `TopologicalGroups(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - Owned groups equipped with a represented compatible topology.
- `is_topological_group() -> bool`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedGroups`](#cat-ownedgroups) | 15 | 1 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `FinitelyPresentedGroups` {#cat-finitelypresentedgroups}

Finitely presented groups, as a property of the group.

- **defined at** `src/dzack_research/preamble/categories/group/groups.py:1971`
- **probed as** `Category of finitely presented groups`
- **above** [`OwnedFinitelyGeneratedGroups`](#cat-ownedfinitelygeneratedgroups)
- **refines**, transitively, in Sage's linearization order: [`OwnedFinitelyGeneratedGroups`](#cat-ownedfinitelygeneratedgroups) · [`OwnedGroups`](#cat-ownedgroups) · [`Monoids`](#cat-monoids) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `FinitelyPresentedGroups(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedGroups`](#cat-ownedgroups) | 15 | 1 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`OwnedFinitelyGeneratedGroups`](#cat-ownedfinitelygeneratedgroups) | 2 |  |  |
| [`OwnedFinitelyPresentedGroups`](#cat-ownedfinitelypresentedgroups) | 2 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `GroupsWithChosenFiniteGeneratingSet` {#cat-groupswithchosenfinitegeneratingset}

Finitely generated groups carrying a chosen finite generating set.

- **defined at** `src/dzack_research/preamble/categories/group/groups.py:1867`
- **probed as** `Category of groups with chosen finite generating set`
- **above** [`OwnedFinitelyGeneratedGroups`](#cat-ownedfinitelygeneratedgroups)
- **below** [`CyclicGroups`](#cat-cyclicgroups), [`GroupsWithChosenFinitePresentation`](#cat-groupswithchosenfinitepresentation)
- **refines**, transitively, in Sage's linearization order: [`OwnedFinitelyGeneratedGroups`](#cat-ownedfinitelygeneratedgroups) · [`OwnedGroups`](#cat-ownedgroups) · [`Monoids`](#cat-monoids) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `GroupsWithChosenFiniteGeneratingSet(x, *args, **opts)`

**Operations introduced here** (4 on objects)

*on objects*

- `ElementType()`
  - Finitely generated groups carrying a chosen finite generating set.
- `conjugation_morphism()`
- `group_generators()` <sub>cached</sub>
- `number_of_group_generators()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedGroups`](#cat-ownedgroups) | 15 | 1 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`OwnedFinitelyGeneratedGroups`](#cat-ownedfinitelygeneratedgroups) | 2 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `OwnedFinitelyPresentedGroups` {#cat-ownedfinitelypresentedgroups}

Finitely presented groups, as a property of the group.

- **defined at** `src/dzack_research/preamble/categories/group/groups.py:1971`
- **probed as** `Category of finitely presented groups`
- **above** [`OwnedFinitelyGeneratedGroups`](#cat-ownedfinitelygeneratedgroups)
- **below** [`GroupsWithChosenFinitePresentation`](#cat-groupswithchosenfinitepresentation)
- **refines**, transitively, in Sage's linearization order: [`OwnedFinitelyGeneratedGroups`](#cat-ownedfinitelygeneratedgroups) · [`OwnedGroups`](#cat-ownedgroups) · [`Monoids`](#cat-monoids) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `OwnedFinitelyPresentedGroups(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - Finitely presented groups, as a property of the group.
- `is_finitely_presented()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedGroups`](#cat-ownedgroups) | 15 | 1 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`OwnedFinitelyGeneratedGroups`](#cat-ownedfinitelygeneratedgroups) | 2 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `ProfiniteGroups` {#cat-profinitegroups}

File: /home/dzack/gitclones/sage-dev-allopts/src/sage/categories/category_singleton.pyx (starting at line 85)

```text
A base class for implementing singleton category.

A *singleton* category is a category whose class takes no
parameters like ``Fields()`` or ``Rings()``. See also the
:wikipedia:`Singleton design pattern <Singleton_pattern>`.

This is a subclass of :class:`Category`, with a couple
optimizations for singleton categories.

The main purpose is to make the idioms::

    sage: QQ in Fields()
    True
    sage: ZZ in Fields()
    False

as fast as possible, and in particular competitive to calling a
constant Python method, in order to foster its systematic use
throughout the Sage library. Such tests are time critical, in
particular when creating a lot of polynomial rings over small
fields like in the elliptic curve code.

EXAMPLES::

    sage: from sage.categories.category_singleton import Category_singleton
    sage: class MyRings(Category):
    ....:     def super_categories(self): return Rings().super_categories()
    sage: class MyRingsSingleton(Category_singleton):
    ....:     def super_categories(self): return Rings().super_categories()

We create three rings. One of them is contained in the usual category of
rings, one in the category of "my rings" and the third in the category of
"my rings singleton"::

    sage: R = QQ['x,y']
    sage: R1 = Parent(category = MyRings())
    sage: R2 = Parent(category = MyRingsSingleton())
    sage: R in MyRings()
    False
    sage: R1 in MyRings()
    True
    sage: R1 in MyRingsSingleton()
    False
    sage: R2 in MyRings()
    False
    sage: R2 in MyRingsSingleton()
    True

One sees that containment tests for the singleton class is a lot faster
than for a usual class::

    sage: # not tested
    sage: timeit("R in MyRings()", number=10000)
    10000 loops, best of 3: 7.12 µs per loop
    sage: timeit("R1 in MyRings()", number=10000)
    10000 loops, best of 3: 6.98 µs per loop
    sage: timeit("R in MyRingsSingleton()", number=10000)
    10000 loops, best of 3: 3.08 µs per loop
    sage: timeit("R2 in MyRingsSingleton()", number=10000)
    10000 loops, best of 3: 2.99 µs per loop

So this is an improvement, but not yet competitive with a pure
Cython method::

    sage: timeit("R.is_ring()", number=10000)                     # not tested
    10000 loops, best of 3: 383 ns per loop

However, it is competitive with a Python method. Actually it is faster,
if one stores the category in a variable::

    sage: _Rings = Rings()
    sage: R3 = Parent(category = _Rings)
    sage: R3.is_ring.__module__
    'sage.categories.rings'
    sage: timeit("R3.is_ring()", number=10000)                    # not tested
    10000 loops, best of 3: 2.64 µs per loop
    sage: timeit("R3 in Rings()", number=10000)                   # not tested
    10000 loops, best of 3: 3.01 µs per loop
    sage: timeit("R3 in _Rings", number=10000)                    # not tested
    10000 loops, best of 3: 652 ns per loop

This might not be easy to further optimize, since the time is
consumed in many different spots::

    sage: timeit("MyRingsSingleton.__classcall__()", number=10000)# not tested
    10000 loops, best of 3: 306 ns per loop

    sage: X = MyRingsSingleton()
    sage: timeit("R in X  ", number=10000)                        # not tested
    10000 loops, best of 3: 699 ns per loop

    sage: c = MyRingsSingleton().__contains__
    sage: timeit("c(R)", number = 10000)                          # not tested
    10000 loops, best of 3: 661 ns per loop

.. WARNING::

    A singleton concrete class `A` should not have a subclass `B`
    (necessarily concrete). Otherwise, creating an instance `a` of
    `A` and an instance `b` of `B` would break the singleton
    principle: `A` would have two instances `a` and `b`.

    With the current implementation only direct subclasses of
    :class:`Category_singleton` are supported::

        sage: class MyRingsSingleton(Category_singleton):
        ....:     def super_categories(self): return Rings().super_categories()
        sage: class Disaster(MyRingsSingleton): pass
        sage: Disaster()
        Traceback (most recent call last):
        ...
        AssertionError: <class '__main__.Disaster'> is not a direct subclass of <class 'sage.categories.category_singleton.Category_singleton'>

    However, it is acceptable for a direct subclass `R` of
    :class:`Category_singleton` to create its unique instance as
    an instance of a subclass of itself (in which case, its the
    subclass of `R` which is concrete, not `R` itself). This is
    used for example to plug in extra category code via a dynamic
    subclass::

        sage: from sage.categories.category_singleton import Category_singleton
        sage: class R(Category_singleton):
        ....:     def super_categories(self): return [Sets()]
        sage: R()
        Category of r
        sage: R().__class__
        <class '__main__.R_with_category'>
        sage: R().__class__.mro()
        [<class '__main__.R_with_category'>,
         <class '__main__.R'>,
         <class 'sage.categories.category_singleton.Category_singleton'>,
         <class 'sage.categories.category.Category'>,
         <class 'sage.structure.unique_representation.UniqueRepresentation'>,
         <class 'sage.misc.fast_methods.WithEqualityById'>,
         <class 'sage.structure.unique_representation.CachedRepresentation'>,
         <class 'sage.structure.unique_representation.WithPicklingByInitArgs'>,
         <class 'sage.structure.sage_object.SageObject'>,
         <class '__main__.R.subcategory_class'>,
         <class 'sage.categories.sets_cat.Sets.subcategory_class'>,
         <class 'sage.categories.sets_with_partial_maps.SetsWithPartialMaps.subcategory_class'>,
         <class 'sage.categories.objects.Objects.subcategory_class'>,
         <class 'object'>]
        sage: R() is R()
        True
        sage: R() is R().__class__()
        True

    In that case, ``R`` is an abstract class and has a single
    concrete subclass, so this does not break the Singleton design
    pattern.

    .. SEEALSO:: :meth:`Category.__classcall__`, :meth:`Category.__init__`

TESTS::

    sage: import __main__
    sage: __main__.MyRings = MyRings
    sage: __main__.MyRingsSingleton = MyRingsSingleton
    sage: TestSuite(MyRingsSingleton()).run(skip=["_test_category"])

.. NOTE::

    The ``_test_category`` test is failing because
    ``MyRingsSingleton()`` is not a subcategory of the join of its
    super categories::

        sage: C = MyRingsSingleton()
        sage: C.super_categories()
        [Category of rngs, Category of semirings]
        sage: Rngs() & Semirings()
        Category of rings
        sage: C.is_subcategory(Rings())
        False

    Oh well; it's not really relevant for those tests.
```

- **defined at** `src/dzack_research/preamble/categories/group/profinite/profinite_groups.py:9`
- **probed as** `Category of profinite groups`
- **above** [`TopologicalGroups`](#cat-topologicalgroups)
- **below** [`AbsoluteGaloisGroups`](#cat-absolutegaloisgroups)
- **refines**, transitively, in Sage's linearization order: [`TopologicalGroups`](#cat-topologicalgroups) · [`OwnedGroups`](#cat-ownedgroups) · [`Monoids`](#cat-monoids) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `ProfiniteGroups(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `is_profinite()`
- `topological_group_generators()` <sub>abstract, a contract on implementations</sub>

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedGroups`](#cat-ownedgroups) | 15 | 1 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`TopologicalGroups`](#cat-topologicalgroups) | 2 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `AbsoluteGaloisGroups` {#cat-absolutegaloisgroups}

Groups (G_K=\operatorname{Aut}_K(\bar K)) with a chosen base point.

- **defined at** `src/dzack_research/preamble/categories/group/profinite/absolute_galois_groups.py:14`
- **probed as** `Category of absolute Galois groups`
- **above** [`ProfiniteGroups`](#cat-profinitegroups)
- **below** [`AbsoluteGaloisGroupsOfFiniteFields`](#cat-absolutegaloisgroupsoffinitefields), [`OpenAbsoluteGaloisSubgroups`](#cat-openabsolutegaloissubgroups)
- **refines**, transitively, in Sage's linearization order: [`ProfiniteGroups`](#cat-profinitegroups) · [`TopologicalGroups`](#cat-topologicalgroups) · [`OwnedGroups`](#cat-ownedgroups) · [`Monoids`](#cat-monoids) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `AbsoluteGaloisGroups(x, *args, **opts)`

**Operations introduced here** (3 on objects)

*on objects*

- `characteristic()`
- `is_abelian()`
- `is_profinite() -> bool`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedGroups`](#cat-ownedgroups) | 15 | 1 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`ProfiniteGroups`](#cat-profinitegroups) | 2 |  |  |
| [`TopologicalGroups`](#cat-topologicalgroups) | 2 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `CyclicGroups` {#cat-cyclicgroups}

Groups generated by one chosen element.

```text
The generator is the datum: a cyclic group is one for which such an element
exists, and an object of this category has selected one.  Everything below
is computed by walking that generator.
```

- **defined at** `src/dzack_research/preamble/categories/group/cyclic_subgroups.py:47`
- **probed as** `Category of cyclic groups`
- **above** [`GroupsWithChosenFiniteGeneratingSet`](#cat-groupswithchosenfinitegeneratingset), [`OwnedGroups.Commutative`](#cat-ownedgroups-commutative)
- **refines**, transitively, in Sage's linearization order: [`GroupsWithChosenFiniteGeneratingSet`](#cat-groupswithchosenfinitegeneratingset) · [`OwnedFinitelyGeneratedGroups`](#cat-ownedfinitelygeneratedgroups) · [`OwnedGroups.Commutative`](#cat-ownedgroups-commutative) · [`OwnedGroups`](#cat-ownedgroups) · [`Monoids`](#cat-monoids) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `CyclicGroups(x, *args, **opts)`

**Operations introduced here** (9 on objects)

*on objects*

- `ElementType()`
  - Groups generated by one chosen element.
- `cardinality()`
- `generator()`
  - Return the element this group is generated by.
- `group_generators()` <sub>cached</sub>
- `is_abelian()`
- `is_finite()`
- `number_of_group_generators()`
- `one()`
- `order()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedGroups`](#cat-ownedgroups) | 20 | 1 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`GroupsWithChosenFiniteGeneratingSet`](#cat-groupswithchosenfinitegeneratingset) | 4 |  |  |
| [`OwnedFinitelyGeneratedGroups`](#cat-ownedfinitelygeneratedgroups) | 2 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `GroupsWithChosenFinitePresentation` {#cat-groupswithchosenfinitepresentation}

Groups carrying a chosen finite presentation.

- **defined at** `src/dzack_research/preamble/categories/group/groups.py:1990`
- **probed as** `Category of groups with chosen finite presentation`
- **above** [`GroupsWithChosenFiniteGeneratingSet`](#cat-groupswithchosenfinitegeneratingset), [`OwnedFinitelyPresentedGroups`](#cat-ownedfinitelypresentedgroups)
- **refines**, transitively, in Sage's linearization order: [`OwnedFinitelyPresentedGroups`](#cat-ownedfinitelypresentedgroups) · [`GroupsWithChosenFiniteGeneratingSet`](#cat-groupswithchosenfinitegeneratingset) · [`OwnedFinitelyGeneratedGroups`](#cat-ownedfinitelygeneratedgroups) · [`OwnedGroups`](#cat-ownedgroups) · [`Monoids`](#cat-monoids) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `GroupsWithChosenFinitePresentation(x, *args, **opts)`

**Operations introduced here** (4 on objects)

*on objects*

- `ElementType()`
  - Groups carrying a chosen finite presentation.
- `defining_relations()` <sub>cached</sub>
  - The chosen relators, as elements of the presenting free group.
- `presenting_free_group()`
- `quotient_by_relators(relators)`
  - Return ``G / <<relators>>``, the quotient by the normal closure of ``relators``.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedGroups`](#cat-ownedgroups) | 15 | 1 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`GroupsWithChosenFiniteGeneratingSet`](#cat-groupswithchosenfinitegeneratingset) | 4 |  |  |
| [`OwnedFinitelyGeneratedGroups`](#cat-ownedfinitelygeneratedgroups) | 2 |  |  |
| [`OwnedFinitelyPresentedGroups`](#cat-ownedfinitelypresentedgroups) | 2 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `OpenAbsoluteGaloisSubgroups` {#cat-openabsolutegaloissubgroups}

Open subgroups (G_E\subseteq G_K) carrying the embedding (E\to\bar K).

- **defined at** `src/dzack_research/preamble/categories/group/profinite/absolute_galois_groups.py:67`
- **probed as** `Category of open subgroups of absolute Galois groups`
- **above** [`AbsoluteGaloisGroups`](#cat-absolutegaloisgroups)
- **refines**, transitively, in Sage's linearization order: [`AbsoluteGaloisGroups`](#cat-absolutegaloisgroups) · [`ProfiniteGroups`](#cat-profinitegroups) · [`TopologicalGroups`](#cat-topologicalgroups) · [`OwnedGroups`](#cat-ownedgroups) · [`Monoids`](#cat-monoids) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `OpenAbsoluteGaloisSubgroups(x, *args, **opts)`

**Operations introduced here** (6 on objects)

*on objects*

- `embedding()`
- `fixed_extension()`
- `fixed_field()`
- `inclusion()`
- `index()`
- `supergroup()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedGroups`](#cat-ownedgroups) | 15 | 1 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AbsoluteGaloisGroups`](#cat-absolutegaloisgroups) | 3 |  |  |
| [`ProfiniteGroups`](#cat-profinitegroups) | 2 |  |  |
| [`TopologicalGroups`](#cat-topologicalgroups) | 2 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `AbsoluteGaloisGroupsOfFiniteFields` {#cat-absolutegaloisgroupsoffinitefields}

The procyclic absolute Galois groups of finite fields.

- **defined at** `src/dzack_research/preamble/categories/group/profinite/absolute_galois_groups.py:35`
- **probed as** `Category of absolute Galois groups of finite fields`
- **above** [`AbsoluteGaloisGroups`](#cat-absolutegaloisgroups), [`OwnedGroups.Commutative`](#cat-ownedgroups-commutative)
- **refines**, transitively, in Sage's linearization order: [`OwnedGroups.Commutative`](#cat-ownedgroups-commutative) · [`AbsoluteGaloisGroups`](#cat-absolutegaloisgroups) · [`ProfiniteGroups`](#cat-profinitegroups) · [`TopologicalGroups`](#cat-topologicalgroups) · [`OwnedGroups`](#cat-ownedgroups) · [`Monoids`](#cat-monoids) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `AbsoluteGaloisGroupsOfFiniteFields(x, *args, **opts)`

**Operations introduced here** (6 on objects)

*on objects*

- `cardinality()`
- `is_abelian() -> bool`
- `is_finite() -> bool`
- `is_finitely_generated() -> bool`
- `order()`
- `topological_group_generators()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedGroups`](#cat-ownedgroups) | 20 | 1 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AbsoluteGaloisGroups`](#cat-absolutegaloisgroups) | 3 |  |  |
| [`ProfiniteGroups`](#cat-profinitegroups) | 2 |  |  |
| [`TopologicalGroups`](#cat-topologicalgroups) | 2 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `AbsoluteGaloisGroup` {#cat-absolutegaloisgroup}

The automorphism group of one exact extension object (K\to\bar K).

```text
The extension is an object of the coslice category (K/\mathbf{Fields}),
equivalently an object of the slice of affine schemes over
(\operatorname{Spec}K).  Elements are precisely closure automorphisms
commuting with that structure map.
```

- **defined at** `src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py:390`
- **not placed**: `AbsoluteGaloisGroup(field, *, closure=None, embedding=None, extra_categories=())` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `ExactFieldHomset` {#cat-exactfieldhomset}

A represented Hom object which is both a Sage Homset and a category.

```text
This is the live counterpart of the archived owned Hom-category base.  It
keeps Sage's hard requirement that every ``Morphism`` be parented by an
actual ``Homset``, while also making that same parent the discrete category
``Hom_C(A,B)``.  Concrete categories subclass this and add enrichment to
the *same object*.
```

- **defined at** `src/dzack_research/preamble/categories/group/profinite/field_morphisms.py:149`
- **not placed**: `ExactFieldHomset(domain, codomain)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `FiniteGSets` {#cat-finitegsets}

The represented finite objects of `GSets(G)`.

- **defined at** `src/dzack_research/preamble/categories/group/g_sets.py:65`
- **not placed**: `FiniteGSets(group)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

**Operations introduced here** (8 on objects)

*on objects*

- `cardinality()`
- `fixed_points()`
  - The fixed-point set ``X^G``.
- `is_parent_of(point) -> bool`
- `orbits()`
  - The orbit set ``X / G``.
- `permutation_representation()`
  - Return the chosen action as the group morphism ``G -> Sym(X)``.
- `point_set()`
  - Return the finite set used to present the points of this ``G``-set.
- `rank(point)`
- `unrank(position)`

#### `GObjectHomset` {#cat-gobjecthomset}

The represented `Mor_G(X, Y)`: the equivariant morphisms of `C`.

```text
Equivariance is decided on the chosen generators of the acting group,
since the morphisms commuting with a group element form a subgroup.
```

- **defined at** `src/dzack_research/preamble/categories/group/g_objects.py:102`
- **not placed**: `GObjectHomset(hom_family, domain, codomain)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `GObjects` {#cat-gobjects}

The category of objects of `C` with a chosen `G`-action.

- **defined at** `src/dzack_research/preamble/categories/group/g_objects.py:158`
- **not placed**: `GObjects(group, category)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

**Operations introduced here** (6 on objects)

*on objects*

- `act(group_element, element)`
  - Return ``group_element . element``.
- `acting_group()`
- `action()` <sub>cached</sub>
  - Return the chosen action as the set morphism ``G -> Mor_C(X, X)``.
- `action_of(group_element)` <sub>cached</sub>
  - Return the automorphism of ``X`` in ``C`` induced by ``group_element``.
- `is_invariant(element)`
  - Decide ``g . element = element`` for all ``g``, on the chosen generators.
- `underlying_category()`
  - Return the category in which this object is acted on.

#### `GSetHomset` {#cat-gsethomset}

The equivariant Mor category between represented finite `G`-sets.

- **defined at** `src/dzack_research/preamble/categories/group/g_sets.py:241`
- **not placed**: `GSetHomset(hom_family, domain, codomain)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `GroupAutomorphismGroup` {#cat-groupautomorphismgroup}

The canonical owned homset Hom(G,H).

- **defined at** `src/dzack_research/preamble/categories/group/groups.py:1329`
- **not placed**: `GroupAutomorphismGroup(hom_family, group, engine_subgroup=None)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `GroupHomset` {#cat-grouphomset}

The canonical owned homset Hom(G,H).

- **defined at** `src/dzack_research/preamble/categories/group/groups.py:1164`
- **not placed**: `GroupHomset(hom_family, domain, codomain, *, category=None)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `IndexedFreeGroupHomset` {#cat-indexedfreegrouphomset}

The canonical Hom-set out of the free group on a chosen set.

- **defined at** `src/dzack_research/preamble/categories/group/groups.py:1085`
- **not placed**: `IndexedFreeGroupHomset(hom_family, domain, codomain)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `OpenAbsoluteGaloisSubgroup` {#cat-openabsolutegaloissubgroup}

The actual subgroup fixing one embedded finite extension (E/K).

- **defined at** `src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py:798`
- **not placed**: `OpenAbsoluteGaloisSubgroup(supergroup, extension: dzack_research.preamble.categories.group.profinite.galois_quotient.FiniteGaloisExtension)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

#### `PredicateSubgroups` {#cat-predicatesubgroups}

An owned category parameterized by one arbitrary mathematical object.

```text
The parameter is stored verbatim; this base performs no Sage-category
membership test. Subclasses normalize their own parameters when needed.
```

- **defined at** `src/dzack_research/preamble/categories/group/predicate_subgroups.py:21`
- **not placed**: `PredicateSubgroups(parameter)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

**Operations introduced here** (13 on objects)

*on objects*

- `cardinality()`
- `character_data()`
- `contains_character_kernel() -> bool`
- `defining_predicate()`
- `finite_character_quotient()`
- `inclusion()`
- `intersection(other)`
- `isotropic_are_equivalent(left, right, *, flag=False) -> bool`
- `isotropic_orbit_representatives(rank, *, flag=False)`
- `one()`
- `supergroup()`
- `vector_orbit_representatives(square)`
- `vectors_are_equivalent(left, right) -> bool`

#### `Subgroups` {#cat-subgroups}

Groups represented as a specified subgroup of one ambient owned group.

- **defined at** `src/dzack_research/preamble/categories/group/groups.py:2094`
- **not placed**: `Subgroups(parameter)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

**Operations introduced here** (2 on objects)

*on objects*

- `inclusion()`
- `supergroup()`

#### `Torsors` {#cat-torsors}

The base class for modeling mathematical categories, like for example:

```text
- ``Groups()`` -- the category of groups
- ``EuclideanDomains()`` -- the category of euclidean rings
- ``VectorSpaces(QQ)`` -- the category of vector spaces over the field of
  rationals

See :mod:`sage.categories.primer` for an introduction to
categories in Sage, their relevance, purpose, and usage. The
documentation below will focus on their implementation.

Technically, a category is an instance of the class
:class:`Category` or some of its subclasses. Some categories, like
:class:`VectorSpaces`, are parametrized: ``VectorSpaces(QQ)`` is one of
many instances of the class :class:`VectorSpaces`. On the other
hand, ``EuclideanDomains()`` is the single instance of the class
:class:`EuclideanDomains`.

Recall that an algebraic structure (say, the ring `\QQ[x]`) is
modelled in Sage by an object which is called a parent. This
object belongs to certain categories (here ``EuclideanDomains()`` and
``Algebras()``). The elements of the ring are themselves objects.

The class of a category (say :class:`EuclideanDomains`) can define simultaneously:

- Operations on the category itself (what is its super categories?
  its category of morphisms? its dual category?).
- Generic operations on parents in this category, like the ring `\QQ[x]`.
- Generic operations on elements of such parents (e. g., the
  Euclidean algorithm for computing gcds).
- Generic operations on morphisms of this category.

This is achieved as follows::

    sage: from sage.categories.category import Category
    sage: class EuclideanDomains(Category):
    ....:     # operations on the category itself
    ....:     def super_categories(self):
    ....:         [Rings()]
    ....:
    ....:     def dummy(self): # TODO: find some good examples
    ....:          pass
    ....:
    ....:     class ParentMethods: # holds the generic operations on parents
    ....:          # TODO: find a good example of an operation
    ....:          pass
    ....:
    ....:     class ElementMethods:# holds the generic operations on elements
    ....:          def gcd(x, y):
    ....:              # Euclid algorithms
    ....:              pass
    ....:
    ....:     class MorphismMethods: # holds the generic operations on morphisms
    ....:          # TODO: find a good example of an operation
    ....:          pass
    ....:

Note that the nested class ``ParentMethods`` is merely a container
of operations, and does not inherit from anything. Instead, the
hierarchy relation is defined once at the level of the categories,
and the actual hierarchy of classes is built in parallel from all
the ``ParentMethods`` nested classes, and stored in the attributes
``parent_class``. Then, a parent in a category ``C`` receives the
appropriate operations from all the super categories by usual
class inheritance from ``C.parent_class``.

Similarly, two other hierarchies of classes, for elements and
morphisms respectively, are built from all the ``ElementMethods``
and ``MorphismMethods`` nested classes.

EXAMPLES:

We define a hierarchy of four categories ``As()``, ``Bs()``,
``Cs()``, ``Ds()`` with a diamond inheritance. Think for example:

- ``As()`` -- the category of sets
- ``Bs()`` -- the category of additive groups
- ``Cs()`` -- the category of multiplicative monoids
- ``Ds()`` -- the category of rings

::

    sage: from sage.categories.category import Category
    sage: from sage.misc.lazy_attribute import lazy_attribute
    sage: class As (Category):
    ....:     def super_categories(self):
    ....:         return []
    ....:
    ....:     class ParentMethods:
    ....:         def fA(self):
    ....:             return "A"
    ....:         f = fA

    sage: class Bs (Category):
    ....:     def super_categories(self):
    ....:         return [As()]
    ....:
    ....:     class ParentMethods:
    ....:         def fB(self):
    ....:             return "B"

    sage: class Cs (Category):
    ....:     def super_categories(self):
    ....:         return [As()]
    ....:
    ....:     class ParentMethods:
    ....:         def fC(self):
    ....:             return "C"
    ....:         f = fC

    sage: class Ds (Category):
    ....:     def super_categories(self):
    ....:         return [Bs(),Cs()]
    ....:
    ....:     class ParentMethods:
    ....:         def fD(self):
    ....:             return "D"

Categories should always have unique representation; by :issue:`12215`,
this means that it will be kept in cache, but only
if there is still some strong reference to it.

We check this before proceeding::

    sage: import gc
    sage: idAs = id(As())
    sage: _ = gc.collect()
    sage: n == id(As())
    False
    sage: a = As()
    sage: id(As()) == id(As())
    True
    sage: As().parent_class == As().parent_class
    True

We construct a parent in the category ``Ds()`` (that, is an instance
of ``Ds().parent_class``), and check that it has access to all the
methods provided by all the categories, with the appropriate
inheritance order::

    sage: D = Ds().parent_class()
    sage: [ D.fA(), D.fB(), D.fC(), D.fD() ]
    ['A', 'B', 'C', 'D']
    sage: D.f()
    'C'

::

    sage: C = Cs().parent_class()
    sage: [ C.fA(), C.fC() ]
    ['A', 'C']
    sage: C.f()
    'C'

Here is the parallel hierarchy of classes which has been built
automatically, together with the method resolution order (``.mro()``)::

    sage: As().parent_class
    <class '__main__.As.parent_class'>
    sage: As().parent_class.__bases__
    (<... 'object'>,)
    sage: As().parent_class.mro()
    [<class '__main__.As.parent_class'>, <... 'object'>]

::

    sage: Bs().parent_class
    <class '__main__.Bs.parent_class'>
    sage: Bs().parent_class.__bases__
    (<class '__main__.As.parent_class'>,)
    sage: Bs().parent_class.mro()
    [<class '__main__.Bs.parent_class'>, <class '__main__.As.parent_class'>, <... 'object'>]

::

    sage: Cs().parent_class
    <class '__main__.Cs.parent_class'>
    sage: Cs().parent_class.__bases__
    (<class '__main__.As.parent_class'>,)
    sage: Cs().parent_class.__mro__
    (<class '__main__.Cs.parent_class'>, <class '__main__.As.parent_class'>, <... 'object'>)

::

    sage: Ds().parent_class
    <class '__main__.Ds.parent_class'>
    sage: Ds().parent_class.__bases__
    (<class '__main__.Cs.parent_class'>, <class '__main__.Bs.parent_class'>)
    sage: Ds().parent_class.mro()
    [<class '__main__.Ds.parent_class'>, <class '__main__.Cs.parent_class'>,
     <class '__main__.Bs.parent_class'>, <class '__main__.As.parent_class'>, <... 'object'>]

Note that two categories in the same class need not have the
same ``super_categories``. For example, ``Algebras(QQ)`` has
``VectorSpaces(QQ)`` as super category, whereas ``Algebras(ZZ)``
only has ``Modules(ZZ)`` as super category. In particular, the
constructed parent class and element class will differ (inheriting,
or not, methods specific for vector spaces)::

    sage: Algebras(QQ).parent_class is Algebras(ZZ).parent_class
    False
    sage: issubclass(Algebras(QQ).parent_class, VectorSpaces(QQ).parent_class)
    True

On the other hand, identical hierarchies of classes are,
preferably, built only once (e.g. for categories over a base ring)::

    sage: Algebras(GF(5)).parent_class is Algebras(GF(7)).parent_class
    True
    sage: F = FractionField(ZZ['t'])
    sage: Coalgebras(F).parent_class is Coalgebras(FractionField(F['x'])).parent_class
    True

We now construct a parent in the usual way::

    sage: class myparent(Parent):
    ....:     def __init__(self):
    ....:         Parent.__init__(self, category=Ds())
    ....:     def g(self):
    ....:         return "myparent"
    ....:     class Element():
    ....:         pass
    sage: D = myparent()
    sage: D.__class__
    <class '__main__.myparent_with_category'>
    sage: D.__class__.__bases__
    (<class '__main__.myparent'>, <class '__main__.Ds.parent_class'>)
    sage: D.__class__.mro()
    [<class '__main__.myparent_with_category'>,
    <class '__main__.myparent'>,
    <class 'sage.structure.parent.Parent'>,
    <class 'sage.structure.category_object.CategoryObject'>,
    <class 'sage.structure.sage_object.SageObject'>,
    <class '__main__.Ds.parent_class'>,
    <class '__main__.Cs.parent_class'>,
    <class '__main__.Bs.parent_class'>,
    <class '__main__.As.parent_class'>,
    <... 'object'>]
    sage: D.fA()
    'A'
    sage: D.fB()
    'B'
    sage: D.fC()
    'C'
    sage: D.fD()
    'D'
    sage: D.f()
    'C'
    sage: D.g()
    'myparent'

::

    sage: D.element_class
    <class '__main__.myparent_with_category.element_class'>
    sage: D.element_class.mro()
    [<class '__main__.myparent_with_category.element_class'>,
    <class ...__main__....Element...>,
    <class '__main__.Ds.element_class'>,
    <class '__main__.Cs.element_class'>,
    <class '__main__.Bs.element_class'>,
    <class '__main__.As.element_class'>,
    <... 'object'>]


TESTS::

    sage: import __main__
    sage: __main__.myparent = myparent
    sage: __main__.As = As
    sage: __main__.Bs = Bs
    sage: __main__.Cs = Cs
    sage: __main__.Ds = Ds
    sage: loads(dumps(Ds)) is Ds
    True
    sage: loads(dumps(Ds())) is Ds()
    True
    sage: loads(dumps(Ds().element_class)) is Ds().element_class
    True

.. automethod:: Category._super_categories
.. automethod:: Category._super_categories_for_classes
.. automethod:: Category._all_super_categories
.. automethod:: Category._all_super_categories_proper
.. automethod:: Category._set_of_super_categories
.. automethod:: Category._make_named_class
.. automethod:: Category._repr_
.. automethod:: Category._repr_object_names
.. automethod:: Category._test_category
.. automethod:: Category._with_axiom
.. automethod:: Category._with_axiom_as_tuple
.. automethod:: Category._without_axioms
.. automethod:: Category._sort
.. automethod:: Category._sort_uniq
.. automethod:: Category.__classcall__
.. automethod:: Category.__init__
```

- **defined at** `src/dzack_research/preamble/categories/group/g_sets.py:490`
- **not placed**: `Torsors(group)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

**Operations introduced here** (2 on objects)

*on objects*

- `an_element()` <sub>abstract, a contract on implementations</sub>
  - Return the chosen point trivializing this torsor.
- `transporter(source, target)`
  - Return the unique group element carrying ``source`` to ``target`` when computable.

### Objects

#### `ContinuousGroupHomset` <sub>OBJECT</sub>

The class for collections of morphisms in a category.

```text
EXAMPLES::

    sage: H = Hom(QQ^2, QQ^3)                                                       # needs sage.modules
    sage: loads(H.dumps()) is H                                                     # needs sage.modules
    True

Homsets of unique parents are unique as well::

    sage: H = End(AffineSpace(2, names='x,y'))
    sage: loads(dumps(AffineSpace(2, names='x,y'))) is AffineSpace(2, names='x,y')
    True
    sage: loads(dumps(H)) is H
    True

Conversely, homsets of non-unique parents are non-unique::

    sage: P11 = ProductProjectiveSpaces(QQ, [1, 1])
    sage: H = End(P11)
    sage: loads(dumps(P11)) is ProductProjectiveSpaces(QQ, [1, 1])
    False
    sage: loads(dumps(P11)) == ProductProjectiveSpaces(QQ, [1, 1])
    True
    sage: loads(dumps(H)) is H
    False
    sage: loads(dumps(H)) == H
    True
```

- **defined at** `src/dzack_research/preamble/categories/group/profinite/galois_quotient.py:352`
- **built by** `ContinuousGroupHomset(domain, codomain)`

#### `FiniteGaloisQuotient` <sub>OBJECT</sub>

The finite quotient (\operatorname{Gal}(L/K)) as exact field maps.

- **defined at** `src/dzack_research/preamble/categories/group/profinite/galois_quotient.py:232`
- **built by** `FiniteGaloisQuotient(extension: dzack_research.preamble.categories.group.profinite.galois_quotient.FiniteGaloisExtension)`

**Operations**

- `Element(parent, index: int) -> None`
  - An exact (K)-automorphism of a represented finite extension (L/K).
- `automorphisms() -> tuple[dzack_research.preamble.categories.group.profinite.field_morphisms.ExactFieldMorphism, ...]`
- `base_field()`
- `cardinality()`
- `compose(left, right)`
- `extension_data() -> dzack_research.preamble.categories.group.profinite.galois_quotient.FiniteGaloisExtension`
- `group_generators()`
- `inverse(element)`
- `is_abelian() -> bool`
- `one()`
- `order()`
- `top_field()`

#### `FiniteGaloisSubgroup` <sub>OBJECT</sub>

A literal finite subgroup represented by selected quotient elements.

- **defined at** `src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py:98`
- **built by** `FiniteGaloisSubgroup(supergroup, elements, description)`

**Operations**

- `cardinality()`
- `group_generators()`
- `one()`
- `order()`
- `supergroup()`

### Elements

#### `AbsoluteGaloisGroupElement` <sub>ELEMENT</sub>

A coherent, progressively realized automorphism of the chosen closure.

```text
A global exact map may be supplied directly.  A lift from a finite
quotient instead starts with one exact finite coordinate; additional
coordinates can be installed only after their compatibility is checked.
```

- **defined at** `src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py:63`
- **built by** `AbsoluteGaloisGroupElement(parent, *, exact_action: dzack_research.preamble.categories.group.profinite.field_morphisms.ExactFieldMorphism | None = None, coordinates=(), frobenius_exponent=None)`

**Operations**

- `as_morphism()`
- `codomain()`
- `conjugacy_class()`
- `domain()`
- `exact_action()`
- `extend_coordinate(restriction_map, coordinate) -> None`
  - Install a higher finite coordinate after checking compatibility.
- `fixes_base_field() -> bool`
- `frobenius_exponent()`
- `inverse()`
- `is_globally_evaluable() -> bool`
- `realized_stages() -> tuple`
- `restrict(stage)`
- `restriction_coordinate(stage)`
- `underlying_field_morphism()`

#### `FiniteGaloisAutomorphism` <sub>ELEMENT</sub>

An exact (K)-automorphism of a represented finite extension (L/K).

- **defined at** `src/dzack_research/preamble/categories/group/profinite/galois_quotient.py:162`
- **built by** `FiniteGaloisAutomorphism(parent, index: int)`

**Operations**

- `action() -> dzack_research.preamble.categories.group.profinite.field_morphisms.ExactFieldMorphism`
- `as_morphism() -> dzack_research.preamble.categories.group.profinite.field_morphisms.ExactFieldMorphism`
- `inverse()`
- `multiplicative_order()`

#### `FrobeniusElement` <sub>ELEMENT</sub>

An integral power of the canonical (q)-Frobenius.

- **defined at** `src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py:246`
- **built by** `FrobeniusElement(parent, exponent=1)`

### Morphisms and homsets

#### `AbsoluteGaloisSliceAutomorphism` <sub>MORPHISM</sub>

The commuting square in (K/\mathbf{Fields}) defined by an element of (G_K).

- **defined at** `src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py:310`
- **built by** `AbsoluteGaloisSliceAutomorphism(parent, element)`

**Operations**

- `components()`
- `inverse()`
- `left()`
- `right()`

#### `CyclotomicCharacter` <sub>MORPHISM</sub>

The continuous character (\chi_n:G_K\to(\mathbb Z/n)^{\times}).

- **defined at** `src/dzack_research/preamble/categories/group/profinite/galois_characters.py:87`
- **built by** `CyclotomicCharacter(domain, n)`

**Operations**

- `modulus()`
- `primitive_root()`

#### `EquivariantMorphism` <sub>MORPHISM</sub>

A morphism of `C` between two `G`-objects that commutes with the actions.

- **defined at** `src/dzack_research/preamble/categories/group/g_objects.py:63`
- **built by** `EquivariantMorphism(parent, arrow)`

**Operations**

- `underlying_arrow()`
  - Return the same morphism read in the underlying category.

#### `ExactFieldMorphism` <sub>MORPHISM</sub>

A field morphism with owned endpoints and an exact Sage map backend.

- **defined at** `src/dzack_research/preamble/categories/group/profinite/field_morphisms.py:50`
- **built by** `ExactFieldMorphism(parent, engine_morphism: sage.categories.map.Map)`

**Operations**

- `agrees_on_field(other) -> bool`
- `is_injective() -> bool`

#### `FiniteGroupClassFunction` <sub>MORPHISM</sub>

A class function `G -> A` stored on chosen conjugacy representatives.

- **defined at** `src/dzack_research/preamble/categories/group/class_functions.py:11`
- **built by** `FiniteGroupClassFunction(group, codomain, representatives, values)`

**Operations**

- `conjugacy_class_representatives()`
- `degree()`
  - The value at the identity: for a character, the dimension of its representation.
- `values()`

#### `GSetMorphism` <sub>MORPHISM</sub>

A set map checked to commute with the represented group actions.

- **defined at** `src/dzack_research/preamble/categories/group/g_sets.py:213`
- **built by** `GSetMorphism(parent, function)`

**Operations**

- `is_injective() -> bool`
- `is_surjective() -> bool`
  - Map.is_surjective(self)

#### `GaloisRestrictionMap` <sub>MORPHISM</sub>

The continuous quotient map (G_K\to\operatorname{Gal}(L/K)).

- **defined at** `src/dzack_research/preamble/categories/group/profinite/galois_quotient.py:361`
- **built by** `GaloisRestrictionMap(domain, codomain: dzack_research.preamble.categories.group.profinite.galois_quotient.FiniteGaloisQuotient)`

**Operations**

- `extension() -> dzack_research.preamble.categories.group.profinite.galois_quotient.FiniteGaloisExtension`
- `is_continuous() -> bool`
- `is_surjective() -> bool`
  - Map.is_surjective(self)
- `kernel()`

#### `IndexedFreeGroupHomomorphism` <sub>MORPHISM</sub>

A morphism out of the free group on a chosen set.

```text
The free group on an arbitrary set has no elementwise GAP model.  Its
universal morphisms are therefore evaluated directly on reduced words
instead of forcing this object through the unrelated libGAP path.
```

- **defined at** `src/dzack_research/preamble/categories/group/groups.py:1021`
- **built by** `IndexedFreeGroupHomomorphism(parent, images)`

**Operations**

- `generator_morphism()`
- `postcompose(morphism)`

#### `OpenSubgroupInclusion` <sub>MORPHISM</sub>

The literal inclusion of a realized open subgroup into its supergroup group.

- **defined at** `src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py:770`
- **built by** `OpenSubgroupInclusion(subgroup)`

**Operations**

- `is_continuous() -> bool`
- `is_injective() -> bool`

#### `ProfiniteCharacter` <sub>MORPHISM</sub>

A character factoring through one represented finite Galois quotient.

- **defined at** `src/dzack_research/preamble/categories/group/profinite/galois_characters.py:49`
- **built by** `ProfiniteCharacter(domain, codomain, extension: dzack_research.preamble.categories.group.profinite.galois_quotient.FiniteGaloisExtension)`

**Operations**

- `factor_extension() -> dzack_research.preamble.categories.group.profinite.galois_quotient.FiniteGaloisExtension`
- `factorization()`
- `is_continuous() -> bool`
- `kernel()`
- `restrict(subgroup)`

#### `QuadraticCharacter` <sub>MORPHISM</sub>

The character attached to (K(\sqrt a)/K) in characteristic not two.

- **defined at** `src/dzack_research/preamble/categories/group/profinite/galois_characters.py:165`
- **built by** `QuadraticCharacter(domain, a)`

**Operations**

- `square_class()`
- `square_root()`

#### `RestrictedProfiniteCharacter` <sub>MORPHISM</sub>

Map(parent, codomain=None)

```text
File: /home/dzack/gitclones/sage-dev-allopts/src/sage/categories/map.pyx (starting at line 83)

Basic class for all maps.

.. NOTE::

    The call method is of course not implemented in this base class. This must
    be done in the sub classes, by overloading ``_call_`` and possibly also
    ``_call_with_args``.

EXAMPLES:

Usually, instances of this class will not be constructed directly, but
for example like this::

    sage: from sage.categories.morphism import SetMorphism
    sage: X.<x> = ZZ[]
    sage: Y = ZZ
    sage: phi = SetMorphism(Hom(X, Y, Rings()), lambda p: p[0])
    sage: phi(x^2+2*x-1)
    -1
    sage: R.<x,y> = QQ[]
    sage: f = R.hom([x+y, x-y], R)
    sage: f(x^2+2*x-1)
    x^2 + 2*x*y + y^2 + 2*x + 2*y - 1
```

- **defined at** `src/dzack_research/preamble/categories/group/profinite/galois_characters.py:32`
- **built by** `RestrictedProfiniteCharacter(character, subgroup)`

**Operations**

- `is_continuous() -> bool`

### Supporting classes

#### `AbsoluteDecompositionGroup` <sub>CLASS</sub>

File: /home/dzack/gitclones/sage-dev-allopts/src/sage/structure/sage_object.pyx (starting at line 35)

```text
Base class for all (user-visible) objects in Sage

Every object that can end up being returned to the user should
inherit from :class:`SageObject`.

.. automethod:: _ascii_art_
.. automethod:: _cache_key
```

- **defined at** `src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py:247`
- **built by** `AbsoluteDecompositionGroup(supergroup, prime, prolongation: dzack_research.preamble.categories.group.profinite.galois_decomposition.PrimeProlongation)`

**Operations**

- `conjugacy_class()`
- `image(quotient)`
- `prime()`
- `prolongation()`
- `supergroup()`

#### `AbsoluteInertiaGroup` <sub>CLASS</sub>

File: /home/dzack/gitclones/sage-dev-allopts/src/sage/structure/sage_object.pyx (starting at line 35)

```text
Base class for all (user-visible) objects in Sage

Every object that can end up being returned to the user should
inherit from :class:`SageObject`.

.. automethod:: _ascii_art_
.. automethod:: _cache_key
```

- **defined at** `src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py:281`
- **built by** `AbsoluteInertiaGroup(supergroup, prime, prolongation: dzack_research.preamble.categories.group.profinite.galois_decomposition.PrimeProlongation)`

**Operations**

- `conjugacy_class()`
- `image(quotient)`
- `prime()`
- `prolongation()`
- `supergroup()`

#### `DecompositionGroupConjugacyClass` <sub>CLASS</sub>

File: /home/dzack/gitclones/sage-dev-allopts/src/sage/structure/sage_object.pyx (starting at line 35)

```text
Base class for all (user-visible) objects in Sage

Every object that can end up being returned to the user should
inherit from :class:`SageObject`.

.. automethod:: _ascii_art_
.. automethod:: _cache_key
```

- **defined at** `src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py:315`
- **built by** `DecompositionGroupConjugacyClass(supergroup, prime)`

**Operations**

- `prime()`
- `representative(prolongation)`
- `supergroup()`

#### `ElementConjugacyClass` <sub>CLASS</sub>

The conjugacy class of a represented global automorphism.

- **defined at** `src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py:253`
- **built by** `ElementConjugacyClass(supergroup, representative)`

**Operations**

- `representative()`
- `supergroup()`

#### `FiniteElementConjugacyClass` <sub>CLASS</sub>

The actual conjugacy orbit of an element in a finite quotient.

- **defined at** `src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py:154`
- **built by** `FiniteElementConjugacyClass(supergroup, representative)`

**Operations**

- `elements() -> tuple`
- `representative()`
- `supergroup()`

#### `FiniteGaloisExtension` <sub>CLASS</sub>

A finite Galois field (L/K\subset\bar K) with both exact embeddings.

- **defined at** `src/dzack_research/preamble/categories/group/profinite/galois_quotient.py:63`
- **built by** `FiniteGaloisExtension(base_field, field, base_embedding: dzack_research.preamble.categories.group.profinite.field_morphisms.ExactFieldMorphism, closure, closure_embedding: dzack_research.preamble.categories.group.profinite.field_morphisms.ExactFieldMorphism)`

**Operations**

- `algebraic_closure()`
- `automorphisms() -> tuple[dzack_research.preamble.categories.group.profinite.field_morphisms.ExactFieldMorphism, ...]`
- `base_embedding() -> dzack_research.preamble.categories.group.profinite.field_morphisms.ExactFieldMorphism`
- `base_field()`
- `degree()`
- `embedding() -> dzack_research.preamble.categories.group.profinite.field_morphisms.ExactFieldMorphism`
- `field()`
- `is_galois() -> bool`

#### `FrobeniusConjugacyClass` <sub>CLASS</sub>

The canonical global Frobenius class at an unramified base prime.

- **defined at** `src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py:377`
- **built by** `FrobeniusConjugacyClass(supergroup, prime)`

**Operations**

- `conjugacy_class()`
- `image(quotient, prime_above)`
- `prime()`
- `supergroup()`

#### `InertiaGroupConjugacyClass` <sub>CLASS</sub>

File: /home/dzack/gitclones/sage-dev-allopts/src/sage/structure/sage_object.pyx (starting at line 35)

```text
Base class for all (user-visible) objects in Sage

Every object that can end up being returned to the user should
inherit from :class:`SageObject`.

.. automethod:: _ascii_art_
.. automethod:: _cache_key
```

- **defined at** `src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py:346`
- **built by** `InertiaGroupConjugacyClass(supergroup, prime)`

**Operations**

- `prime()`
- `representative(prolongation)`
- `supergroup()`

#### `LiftCoset` <sub>CLASS</sub>

The coset of all global extensions of one finite-level automorphism.

- **defined at** `src/dzack_research/preamble/categories/group/profinite/galois_quotient.py:404`
- **built by** `LiftCoset(restriction_map: dzack_research.preamble.categories.group.profinite.galois_quotient.GaloisRestrictionMap, element)`

**Operations**

- `extension() -> dzack_research.preamble.categories.group.profinite.galois_quotient.FiniteGaloisExtension`
- `finite_automorphism()`
- `kernel()`
- `representative(candidate=None)`
  - Return a supplied representative, or the canonical finite-field one.
- `supergroup()`

#### `OpenGaloisSubgroupConjugacyClass` <sub>CLASS</sub>

The conjugacy class obtained by forgetting (E\hookrightarrow\bar K).

- **defined at** `src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py:960`
- **built by** `OpenGaloisSubgroupConjugacyClass(supergroup, extension_field)`

**Operations**

- `base_embedding()`
- `fixed_field()`
- `index()`
- `representative(embedding=None)`
- `supergroup()`

#### `PrimeProlongation` <sub>CLASS</sub>

A coherent finite-stage oracle for a chosen prolongation (\bar v).

- **defined at** `src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py:14`
- **built by** `PrimeProlongation(base_prime, at_stage)`

**Operations**

- `at(extension)`
- `base_prime()`

### Functions

#### `AbelianGroups` <sub>FUNCTION</sub>

The category of abelian groups.

- **defined at** `src/dzack_research/preamble/categories/group/groups.py:2158`
- **built by** `AbelianGroups()`

#### `FiniteAbelianGroups` <sub>FUNCTION</sub>

The category of finite abelian groups.

```text
One category cut out by two axioms, not a third class beside them.
```

- **defined at** `src/dzack_research/preamble/categories/group/groups.py:2163`
- **built by** `FiniteAbelianGroups()`

#### `FiniteGroups` <sub>FUNCTION</sub>

The category of finite groups.

- **defined at** `src/dzack_research/preamble/categories/group/groups.py:2148`
- **built by** `FiniteGroups()`

#### `GSets` <sub>FUNCTION</sub>

Return the category of `group`-sets: objects of `Sets()` with a chosen action.

- **defined at** `src/dzack_research/preamble/categories/group/g_sets.py:55`
- **built by** `GSets(group)`

#### `OwnedAbelianGroups` <sub>FUNCTION</sub>

The category of abelian groups.

- **defined at** `src/dzack_research/preamble/categories/group/groups.py:2158`
- **built by** `OwnedAbelianGroups()`

#### `OwnedFiniteAbelianGroups` <sub>FUNCTION</sub>

The category of finite abelian groups.

```text
One category cut out by two axioms, not a third class beside them.
```

- **defined at** `src/dzack_research/preamble/categories/group/groups.py:2163`
- **built by** `OwnedFiniteAbelianGroups()`

#### `OwnedFiniteGroups` <sub>FUNCTION</sub>

The category of finite groups.

- **defined at** `src/dzack_research/preamble/categories/group/groups.py:2148`
- **built by** `OwnedFiniteGroups()`

#### `Submonoids` <sub>FUNCTION</sub>

Return the generic subobject category of submonoids of `ambient_monoid`.

- **defined at** `src/dzack_research/preamble/categories/group/submonoids.py:135`
- **built by** `Submonoids(ambient_monoid)`

#### `absolute_galois_group_category` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/group/profinite/absolute_galois_groups.py:97`
- **built by** `absolute_galois_group_category(field)`

#### `centralizer` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/group/predicate_subgroups.py:192`
- **built by** `centralizer(containing_group, element)`

#### `continuous_group_homset` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/group/profinite/galois_quotient.py:357`
- **built by** `continuous_group_homset(domain, codomain)`

#### `cyclic_subgroup` <sub>FUNCTION</sub>

Return the literal cyclic subgroup `<g> <= G` generated by `g`.

```text
A facade of ``G``: its elements are the actual elements of the ambient
group, not parallel residue classes in an abstract ``C_n``.  Finiteness is
inherited when the ambient group is known finite; a cyclic subgroup of an
undecided group makes no finite-order claim.
```

- **defined at** `src/dzack_research/preamble/categories/group/cyclic_subgroups.py:25`
- **built by** `cyclic_subgroup(generator)`

#### `exact_embeddings` <sub>FUNCTION</sub>

Return all exact embeddings of `domain` into `codomain`.

- **defined at** `src/dzack_research/preamble/categories/group/profinite/field_morphisms.py:186`
- **built by** `exact_embeddings(domain, codomain) -> tuple[dzack_research.preamble.categories.group.profinite.field_morphisms.ExactFieldMorphism, ...]`

#### `exact_field_homset` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/group/profinite/field_morphisms.py:174`
- **built by** `exact_field_homset(domain, codomain) -> dzack_research.preamble.categories.group.profinite.field_morphisms.ExactFieldHomset`

#### `extensions_along` <sub>FUNCTION</sub>

Return exactly the candidate automorphisms satisfying (\sigma j=j\tau).

- **defined at** `src/dzack_research/preamble/categories/group/profinite/galois_quotient.py:471`
- **built by** `extensions_along(automorphism, embedding, candidates)`

#### `field_generators` <sub>FUNCTION</sub>

Return exact elements which determine a unital map out of `field`.

- **defined at** `src/dzack_research/preamble/categories/group/profinite/field_morphisms.py:26`
- **built by** `field_generators(field) -> tuple`

#### `finite_decomposition_group` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py:190`
- **built by** `finite_decomposition_group(quotient, prime_above) -> dzack_research.preamble.categories.group.profinite.galois_decomposition.FiniteGaloisSubgroup`

#### `finite_frobenius_class` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py:218`
- **built by** `finite_frobenius_class(quotient, base_prime, prime_above) -> dzack_research.preamble.categories.group.profinite.galois_decomposition.FiniteElementConjugacyClass`

#### `finite_g_set` <sub>FUNCTION</sub>

Return the finite owned `G`-set defined by `action(g,x)`.

- **defined at** `src/dzack_research/preamble/categories/group/g_sets.py:471`
- **built by** `finite_g_set(point_set, group, action)`

#### `finite_inertia_group` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/group/profinite/galois_decomposition.py:204`
- **built by** `finite_inertia_group(quotient, prime_above) -> dzack_research.preamble.categories.group.profinite.galois_decomposition.FiniteGaloisSubgroup`

#### `first_exact_embedding` <sub>FUNCTION</sub>

Choose the first exact Sage embedding in its deterministic ordering.

- **defined at** `src/dzack_research/preamble/categories/group/profinite/field_morphisms.py:203`
- **built by** `first_exact_embedding(domain, codomain) -> dzack_research.preamble.categories.group.profinite.field_morphisms.ExactFieldMorphism`

#### `fixed_point_set` <sub>FUNCTION</sub>

Return the finite fixed-point set `X^G`.

- **defined at** `src/dzack_research/preamble/categories/group/g_sets.py:481`
- **built by** `fixed_point_set(g_set)`

#### `g_set_homset` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/group/g_sets.py:399`
- **built by** `g_set_homset(domain, codomain) -> dzack_research.preamble.categories.group.g_sets.GSetHomset`

#### `generated_submonoid` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/group/submonoids.py:140`
- **built by** `generated_submonoid(ambient, generators, *, description=None, structure_data=None)`

#### `group_homset` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/group/groups.py:1256`
- **built by** `group_homset(domain, codomain)`

#### `open_absolute_galois_subgroup` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/group/profinite/absolute_galois_group.py:1046`
- **built by** `open_absolute_galois_subgroup(supergroup, extension, embedding=None)`

#### `predicate_subgroup` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/group/predicate_subgroups.py:166`
- **built by** `predicate_subgroup(containing_group, predicate, description, *, character_data=None)`

#### `predicate_submonoid` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/group/submonoids.py:150`
- **built by** `predicate_submonoid(ambient, predicate, description, *, structure_data=None)`

#### `restrict_along` <sub>FUNCTION</sub>

Solve (j\tau=\sigma j) for the exact restriction `tau`.

- **defined at** `src/dzack_research/preamble/categories/group/profinite/galois_quotient.py:450`
- **built by** `restrict_along(automorphism: dzack_research.preamble.categories.group.profinite.field_morphisms.ExactFieldMorphism, embedding: dzack_research.preamble.categories.group.profinite.field_morphisms.ExactFieldMorphism) -> dzack_research.preamble.categories.group.profinite.field_morphisms.ExactFieldMorphism`

#### `trivial_g_set` <sub>FUNCTION</sub>

Equip a finite set with the trivial `group`-action.

- **defined at** `src/dzack_research/preamble/categories/group/g_sets.py:476`
- **built by** `trivial_g_set(point_set, group)`

## Rings, Fields & Commutative Algebra

> Owned rings, Fields, Number fields, Prime spectrum, Completions, Localizations, Exact real field, and Predicate subrings.

```mermaid
graph RL
  AdicallyCompleteRings["AdicallyCompleteRings"]
  ArtinianRings["ArtinianRings"]
  CommutativeIdeals["CommutativeIdeals(R)"]
  CompleteLocalRings["CompleteLocalRings"]
  DivisionRings["DivisionRings"]
  Fields["Fields"]
  FormalPowerSeriesRings["FormalPowerSeriesRings(R)"]
  IntegralDomains["IntegralDomains"]
  LocalRings["LocalRings"]
  NoetherianRings["NoetherianRings"]
  NumberFieldsWithChosenPrimitiveElement["NumberFieldsWithChosenPrimitiveElement"]
  OrderedRings["OrderedRings"]
  OwnedAdicallyCompleteRings["OwnedAdicallyCompleteRings"]
  OwnedArtinianRings["OwnedArtinianRings"]
  OwnedCompleteLocalRings["OwnedCompleteLocalRings"]
  OwnedDivisionRings["OwnedDivisionRings"]
  OwnedFields["OwnedFields"]
  OwnedIntegralDomains["OwnedIntegralDomains"]
  OwnedLocalRings["OwnedLocalRings"]
  OwnedNoetherianRings["OwnedNoetherianRings"]
  OwnedNumberFields["OwnedNumberFields"]
  OwnedOrderedRings["OwnedOrderedRings"]
  OwnedOrders["OwnedOrders"]
  OwnedPrincipalIdealDomains["OwnedPrincipalIdealDomains"]
  OwnedRings["OwnedRings"]
  OwnedRings.Commutative["OwnedRings.Commutative"]
  OwnedRngs["OwnedRngs"]
  OwnedSemirings["OwnedSemirings"]
  PredicateSubrings["PredicateSubrings"]
  PrimeFields["PrimeFields"]
  PrimeSpectra["PrimeSpectra"]
  PrincipalIdealDomains["PrincipalIdealDomains"]
  Rings["Rings"]
  AdditiveGroups("AdditiveGroups")
  AdditiveMonoids("AdditiveMonoids")
  Algebras.Commutative("Algebras.Commutative")
  Modules("Modules(R)")
  Monoids("Monoids")
  PartiallyOrderedSets("PartiallyOrderedSets")
  Semigroups("Semigroups")
  AdicallyCompleteRings --> OwnedRings.Commutative
  ArtinianRings --> OwnedNoetherianRings
  CommutativeIdeals --> Modules
  CompleteLocalRings --> OwnedAdicallyCompleteRings
  CompleteLocalRings --> OwnedLocalRings
  DivisionRings --> OwnedRings
  Fields --> OwnedArtinianRings
  Fields --> OwnedDivisionRings
  Fields --> OwnedIntegralDomains
  Fields --> OwnedLocalRings
  Fields --> OwnedNoetherianRings
  Fields --> OwnedPrincipalIdealDomains
  FormalPowerSeriesRings --> Algebras.Commutative
  FormalPowerSeriesRings --> OwnedAdicallyCompleteRings
  IntegralDomains --> OwnedRings.Commutative
  LocalRings --> OwnedRings.Commutative
  NoetherianRings --> OwnedRings.Commutative
  NumberFieldsWithChosenPrimitiveElement --> OwnedNumberFields
  OrderedRings --> OwnedRings
  OwnedAdicallyCompleteRings --> OwnedRings.Commutative
  OwnedArtinianRings --> OwnedNoetherianRings
  OwnedCompleteLocalRings --> OwnedAdicallyCompleteRings
  OwnedCompleteLocalRings --> OwnedLocalRings
  OwnedDivisionRings --> OwnedRings
  OwnedFields --> OwnedArtinianRings
  OwnedFields --> OwnedDivisionRings
  OwnedFields --> OwnedIntegralDomains
  OwnedFields --> OwnedLocalRings
  OwnedFields --> OwnedNoetherianRings
  OwnedFields --> OwnedPrincipalIdealDomains
  OwnedIntegralDomains --> OwnedRings.Commutative
  OwnedLocalRings --> OwnedRings.Commutative
  OwnedNoetherianRings --> OwnedRings.Commutative
  OwnedNumberFields --> OwnedFields
  OwnedOrderedRings --> OwnedRings
  OwnedOrders --> OwnedIntegralDomains
  OwnedOrders --> OwnedNoetherianRings
  OwnedPrincipalIdealDomains --> OwnedIntegralDomains
  OwnedPrincipalIdealDomains --> OwnedNoetherianRings
  OwnedRings --> OwnedRngs
  OwnedRings --> OwnedSemirings
  OwnedRings.Commutative --> OwnedRings
  OwnedRngs --> AdditiveGroups
  OwnedRngs --> Semigroups
  OwnedSemirings --> AdditiveMonoids
  OwnedSemirings --> Monoids
  PredicateSubrings --> OwnedRings
  PrimeFields --> OwnedFields
  PrimeSpectra --> PartiallyOrderedSets
  PrincipalIdealDomains --> OwnedIntegralDomains
  PrincipalIdealDomains --> OwnedNoetherianRings
  Rings --> OwnedRngs
  Rings --> OwnedSemirings
  classDef outside stroke-dasharray:6 4,fill:#f8fafc;
  class AdditiveGroups,AdditiveMonoids,Algebras.Commutative,Modules,Monoids,PartiallyOrderedSets,Semigroups outside;
```

### Categories

Ordered by depth: the least structured first.

#### `PrimeSpectra` {#cat-primespectra}

The prime spectra \(\operatorname{Spec}R\), ordered by inclusion.

- **defined at** `src/dzack_research/preamble/categories/rings/commutative_algebra.py:70`
- **probed as** `Category of prime spectra`
- **above** [`PartiallyOrderedSets`](#cat-partiallyorderedsets)
- **refines**, transitively, in Sage's linearization order: [`PartiallyOrderedSets`](#cat-partiallyorderedsets) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `PrimeSpectra(x, *args, **opts)`

**Operations introduced here** (9 on objects, 7 on elements)

*on objects*

- `ElementType(parent, ideal) -> None`
  - What a prime point is.
- `D(function)`
- `V(ideal)`
- `closed_set(ideal)`
- `coordinate_ring()`
- `distinguished_open(function)`
- `generic_point()`
- `le(left, right) -> bool`
- `ring()`

*on elements*

- `ideal()`
- `local_ring()` <sub>cached</sub>
- `prime_ideal()`
- `residue_field()` <sub>cached</sub>
- `residue_map()` <sub>cached</sub>
  - Return the canonical map ``R -> kappa(p)`` attached to this point.
- `specializes_to(other) -> bool`
- `stalk()` <sub>cached</sub>

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `SageObject` | 8 | 8 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `Element` |  | 9 |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`PartiallyOrderedSets`](#cat-partiallyorderedsets) | 1 |  |  |

#### `CommutativeIdeals(R)` {#cat-commutativeideals}

Ideals of `R`: subobjects of the rank-one `R`-module `R`.

- **defined at** `src/dzack_research/preamble/categories/rings/commutative_ideals.py:83`
- **probed as** `Category of commutative ideals`
- **above** [`Modules(R)`](#cat-modules)
- **below** [`Ideals(R)`](#cat-ideals)
- **refines**, transitively, in Sage's linearization order: [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `CommutativeIdeals(R)(x, *args, **opts)`

**Operations introduced here** (22 on objects)

*on objects*

- `ElementType()`
  - Ideals of ``R``: subobjects of the rank-one ``R``-module ``R``.
- `associated_primes()`
- `colon(other)`
  - Return the ideal quotient ``(self : other)`` when the backend supports it.
- `contains_ambient_element(element) -> bool`
  - Return whether an ambient ring element lies in this ideal.
- `contraction()`
  - Contract this selected localized extension back to its source ring.
- `contraction_from_localization()`
  - Contract this selected localized extension back to its source ring.
- `extension(localization_ring)`
  - Return the represented localization ``S^{-1}I <= S^{-1}R``.
- `extension_to_localization(localization_ring)`
  - Return the represented localization ``S^{-1}I <= S^{-1}R``.
- `ideal_generators()`
- `ideal_quotient(other)`
  - Return the ideal quotient ``(self : other)`` when the backend supports it.
- `intersection(other)`
- `is_maximal()`
- `is_prime()`
- `power(exponent)`
- `primary_decomposition()`
- `product(other)`
- `quotient_ring()`
- `radical()`
- `ring()`
- `saturation(other)`
  - Return ``(self : other^infinity)`` when the backend supports it.
- `sum(other)`
- `syzygy_matrix()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `OwnedRngs` {#cat-ownedrngs}

Rngs on the owned operation spine.

- **defined at** `src/dzack_research/preamble/categories/rings/ring_foundation.py:692`
- **probed as** `Category of owned rngs`
- **above** [`AdditiveGroups`](#cat-additivegroups), [`Semigroups`](#cat-semigroups)
- **below** [`OwnedRings`](#cat-ownedrings), [`Rings`](#cat-rings)
- **refines**, transitively, in Sage's linearization order: [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `OwnedRngs(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Rngs on the owned operation spine.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 1 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `OwnedSemirings` {#cat-ownedsemirings}

Semirings on the owned operation spine.

- **defined at** `src/dzack_research/preamble/categories/rings/ring_foundation.py:681`
- **probed as** `Category of owned semirings`
- **above** [`AdditiveMonoids`](#cat-additivemonoids), [`Monoids`](#cat-monoids)
- **below** [`OwnedRings`](#cat-ownedrings), [`Rings`](#cat-rings)
- **refines**, transitively, in Sage's linearization order: [`Monoids`](#cat-monoids) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `OwnedSemirings(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Semirings on the owned operation spine.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `OwnedRings` {#cat-ownedrings}

Unital rings whose notebook-facing ring interface is owned here.

- **defined at** `src/dzack_research/preamble/categories/rings/ring_foundation.py:703`
- **probed as** `Category of owned rings`
- **above** [`OwnedRngs`](#cat-ownedrngs), [`OwnedSemirings`](#cat-ownedsemirings)
- **below** [`Algebras(R)`](#cat-algebras), [`DivisionRings`](#cat-divisionrings), [`MatrixEndomorphismSpaces(R)`](#cat-matrixendomorphismspaces), [`OrderedRings`](#cat-orderedrings), [`OwnedDivisionRings`](#cat-owneddivisionrings), [`OwnedOrderedRings`](#cat-ownedorderedrings), [`OwnedRings.Commutative`](#cat-ownedrings-commutative), [`PredicateSubrings`](#cat-predicatesubrings)
- **refines**, transitively, in Sage's linearization order: [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `OwnedRings(x, *args, **opts)`

**Operations introduced here** (7 on objects)

*on objects*

- `ElementType()`
  - Unital rings whose notebook-facing ring interface is owned here.
- `Mor(codomain, category=None)`
- `algebra_structure_morphism()`
  - The structure morphism of this ring as an algebra over itself.
- `cardinality()`
  - Return the exact represented cardinal of the underlying set.
- `fraction_field()`
  - Return the fraction field through the computation ring.
- `is_central(element)`
  - Return whether ``element`` is central in the foundational ring regimes.
- `ring_center()` <sub>cached</sub>
  - Return the centre ``Z(R)`` as a predicate-defined subring.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 1 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `Rings` {#cat-rings}

Unital rings whose notebook-facing ring interface is owned here.

- **defined at** `src/dzack_research/preamble/categories/rings/ring_foundation.py:703`
- **probed as** `Category of owned rings`
- **above** [`OwnedRngs`](#cat-ownedrngs), [`OwnedSemirings`](#cat-ownedsemirings)
- **refines**, transitively, in Sage's linearization order: [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `Rings(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 7 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 1 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `DivisionRings` {#cat-divisionrings}

Base class for categories belonging to the owned mathematical graph.

```text
Over :class:`owned_category_bases.Category`, which ties this category's
``ParentMethods`` / ``ElementMethods`` / ``MorphismMethods`` into the
named classes as real bases.  Sage's own builder passes
``prepend_cls_bases=False``, so only a copy of the container's
``__dict__`` reaches the MRO -- a copy carries no bases, so it cannot
carry ``Parent``, so it cannot carry fields or a constructor.  That, and
nothing else, is why a level would otherwise need a hand-written parent
class beside its category.
```

- **defined at** `src/dzack_research/preamble/categories/rings/ring_foundation.py:1134`
- **probed as** `Category of owned division rings`
- **above** [`OwnedRings`](#cat-ownedrings)
- **refines**, transitively, in Sage's linearization order: [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `DivisionRings(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 7 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 1 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedDivisionRings`](#cat-owneddivisionrings) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `OrderedRings` {#cat-orderedrings}

Totally ordered rings in the owned scalar hierarchy.

- **defined at** `src/dzack_research/preamble/categories/rings/ring_foundation.py:974`
- **probed as** `Category of owned ordered rings`
- **above** [`OwnedRings`](#cat-ownedrings)
- **refines**, transitively, in Sage's linearization order: [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `OrderedRings(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 7 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 1 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedOrderedRings`](#cat-ownedorderedrings) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `OwnedDivisionRings` {#cat-owneddivisionrings}

Base class for categories belonging to the owned mathematical graph.

```text
Over :class:`owned_category_bases.Category`, which ties this category's
``ParentMethods`` / ``ElementMethods`` / ``MorphismMethods`` into the
named classes as real bases.  Sage's own builder passes
``prepend_cls_bases=False``, so only a copy of the container's
``__dict__`` reaches the MRO -- a copy carries no bases, so it cannot
carry ``Parent``, so it cannot carry fields or a constructor.  That, and
nothing else, is why a level would otherwise need a hand-written parent
class beside its category.
```

- **defined at** `src/dzack_research/preamble/categories/rings/ring_foundation.py:1134`
- **probed as** `Category of owned division rings`
- **above** [`OwnedRings`](#cat-ownedrings)
- **below** [`Fields`](#cat-fields), [`OwnedFields`](#cat-ownedfields)
- **refines**, transitively, in Sage's linearization order: [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `OwnedDivisionRings(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Unital rings whose notebook-facing ring interface is owned here.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 7 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 1 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `OwnedOrderedRings` {#cat-ownedorderedrings}

Totally ordered rings in the owned scalar hierarchy.

- **not exported**: reachable only as a supercategory
- **probed as** `Category of owned ordered rings`
- **above** [`OwnedRings`](#cat-ownedrings)
- **refines**, transitively, in Sage's linearization order: [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `OwnedOrderedRings(x, *args, **opts)`
- **specimens** `QQ`, `ZZ`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Unital rings whose notebook-facing ring interface is owned here.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 7 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 1 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `OwnedRings.Commutative` {#cat-ownedrings-commutative}

Commutative unital rings in the owned mathematical graph.

- **not exported**: reachable only as a supercategory
- **probed as** `Category of commutative rings`
- **above** [`OwnedRings`](#cat-ownedrings)
- **below** [`AdicallyCompleteRings`](#cat-adicallycompleterings), [`Algebras.Commutative`](#cat-algebras-commutative), [`IntegralDomains`](#cat-integraldomains), [`LocalRings`](#cat-localrings), [`NoetherianRings`](#cat-noetherianrings), [`OwnedAdicallyCompleteRings`](#cat-ownedadicallycompleterings), [`OwnedIntegralDomains`](#cat-ownedintegraldomains), [`OwnedLocalRings`](#cat-ownedlocalrings), [`OwnedNoetherianRings`](#cat-ownednoetherianrings)
- **refines**, transitively, in Sage's linearization order: [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `OwnedRings.Commutative(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedRings`](#cat-ownedrings) | 17 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 1 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `PredicateSubrings` {#cat-predicatesubrings}

Base class for categories belonging to the owned mathematical graph.

```text
Over :class:`owned_category_bases.Category`, which ties this category's
``ParentMethods`` / ``ElementMethods`` / ``MorphismMethods`` into the
named classes as real bases.  Sage's own builder passes
``prepend_cls_bases=False``, so only a copy of the container's
``__dict__`` reaches the MRO -- a copy carries no bases, so it cannot
carry ``Parent``, so it cannot carry fields or a constructor.  That, and
nothing else, is why a level would otherwise need a hand-written parent
class beside its category.
```

- **defined at** `src/dzack_research/preamble/categories/rings/ring_foundation.py:221`
- **probed as** `Category of predicate subrings`
- **above** [`OwnedRings`](#cat-ownedrings)
- **refines**, transitively, in Sage's linearization order: [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `PredicateSubrings(x, *args, **opts)`

**Operations introduced here** (6 on objects)

*on objects*

- `ElementType()`
  - Unital rings whose notebook-facing ring interface is owned here.
- `ambient_ring()`
- `defining_predicate()`
- `inclusion()`
- `one()`
- `zero()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 7 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 1 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `AdicallyCompleteRings` {#cat-adicallycompleterings}

Commutative rings represented as complete for a chosen adic topology.

- **defined at** `src/dzack_research/preamble/categories/rings/ring_foundation.py:1101`
- **probed as** `Category of owned adically complete rings`
- **above** [`OwnedRings.Commutative`](#cat-ownedrings-commutative)
- **refines**, transitively, in Sage's linearization order: [`OwnedRings.Commutative`](#cat-ownedrings-commutative) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `AdicallyCompleteRings(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedRings`](#cat-ownedrings) | 17 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`OwnedAdicallyCompleteRings`](#cat-ownedadicallycompleterings) | 3 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 1 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `IntegralDomains` {#cat-integraldomains}

Commutative rings without zero divisors.

- **defined at** `src/dzack_research/preamble/categories/rings/ring_foundation.py:990`
- **probed as** `Category of owned integral domains`
- **above** [`OwnedRings.Commutative`](#cat-ownedrings-commutative)
- **refines**, transitively, in Sage's linearization order: [`OwnedRings.Commutative`](#cat-ownedrings-commutative) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `IntegralDomains(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedRings`](#cat-ownedrings) | 17 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`OwnedIntegralDomains`](#cat-ownedintegraldomains) | 2 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 1 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `LocalRings` {#cat-localrings}

Commutative rings equipped with their unique maximal ideal.

- **defined at** `src/dzack_research/preamble/categories/rings/ring_foundation.py:1063`
- **probed as** `Category of owned local rings`
- **above** [`OwnedRings.Commutative`](#cat-ownedrings-commutative)
- **refines**, transitively, in Sage's linearization order: [`OwnedRings.Commutative`](#cat-ownedrings-commutative) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `LocalRings(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedRings`](#cat-ownedrings) | 17 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`OwnedLocalRings`](#cat-ownedlocalrings) | 6 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 1 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `NoetherianRings` {#cat-noetherianrings}

Noetherian commutative rings.

- **defined at** `src/dzack_research/preamble/categories/rings/ring_foundation.py:1030`
- **probed as** `Category of owned noetherian rings`
- **above** [`OwnedRings.Commutative`](#cat-ownedrings-commutative)
- **refines**, transitively, in Sage's linearization order: [`OwnedRings.Commutative`](#cat-ownedrings-commutative) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `NoetherianRings(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedRings`](#cat-ownedrings) | 17 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`OwnedNoetherianRings`](#cat-ownednoetherianrings) | 3 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 1 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `OwnedAdicallyCompleteRings` {#cat-ownedadicallycompleterings}

Commutative rings represented as complete for a chosen adic topology.

- **not exported**: reachable only as a supercategory
- **probed as** `Category of owned adically complete rings`
- **above** [`OwnedRings.Commutative`](#cat-ownedrings-commutative)
- **below** [`CompleteLocalRings`](#cat-completelocalrings), [`FormalPowerSeriesRings(R)`](#cat-formalpowerseriesrings), [`OwnedCompleteLocalRings`](#cat-ownedcompletelocalrings)
- **refines**, transitively, in Sage's linearization order: [`OwnedRings.Commutative`](#cat-ownedrings-commutative) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `OwnedAdicallyCompleteRings(x, *args, **opts)`

**Operations introduced here** (3 on objects)

*on objects*

- `ElementType()`
  - Commutative rings represented as complete for a chosen adic topology.
- `ideal_of_definition()`
- `is_adically_complete()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedRings`](#cat-ownedrings) | 17 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 1 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `OwnedIntegralDomains` {#cat-ownedintegraldomains}

Commutative rings without zero divisors.

- **not exported**: reachable only as a supercategory
- **probed as** `Category of owned integral domains`
- **above** [`OwnedRings.Commutative`](#cat-ownedrings-commutative)
- **below** [`Fields`](#cat-fields), [`OwnedFields`](#cat-ownedfields), [`OwnedOrders`](#cat-ownedorders), [`OwnedPrincipalIdealDomains`](#cat-ownedprincipalidealdomains), [`PrincipalIdealDomains`](#cat-principalidealdomains)
- **refines**, transitively, in Sage's linearization order: [`OwnedRings.Commutative`](#cat-ownedrings-commutative) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `OwnedIntegralDomains(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - Commutative rings without zero divisors.
- `is_integral_domain(*args, **kwargs)`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedRings`](#cat-ownedrings) | 17 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 1 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `OwnedLocalRings` {#cat-ownedlocalrings}

Commutative rings equipped with their unique maximal ideal.

- **not exported**: reachable only as a supercategory
- **probed as** `Category of owned local rings`
- **above** [`OwnedRings.Commutative`](#cat-ownedrings-commutative)
- **below** [`CompleteLocalRings`](#cat-completelocalrings), [`Fields`](#cat-fields), [`OwnedCompleteLocalRings`](#cat-ownedcompletelocalrings), [`OwnedFields`](#cat-ownedfields)
- **refines**, transitively, in Sage's linearization order: [`OwnedRings.Commutative`](#cat-ownedrings-commutative) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `OwnedLocalRings(x, *args, **opts)`

**Operations introduced here** (6 on objects)

*on objects*

- `ElementType()`
  - Commutative rings equipped with their unique maximal ideal.
- `fraction_field()`
- `is_local()`
- `maximal_ideal()`
- `residue_field()`
- `residue_map()`
  - Return the represented local quotient map ``R -> kappa(m)``.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedRings`](#cat-ownedrings) | 17 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 1 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `OwnedNoetherianRings` {#cat-ownednoetherianrings}

Noetherian commutative rings.

- **not exported**: reachable only as a supercategory
- **probed as** `Category of owned noetherian rings`
- **above** [`OwnedRings.Commutative`](#cat-ownedrings-commutative)
- **below** [`ArtinianRings`](#cat-artinianrings), [`Fields`](#cat-fields), [`OwnedArtinianRings`](#cat-ownedartinianrings), [`OwnedFields`](#cat-ownedfields), [`OwnedOrders`](#cat-ownedorders), [`OwnedPrincipalIdealDomains`](#cat-ownedprincipalidealdomains), [`PrincipalIdealDomains`](#cat-principalidealdomains)
- **refines**, transitively, in Sage's linearization order: [`OwnedRings.Commutative`](#cat-ownedrings-commutative) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `OwnedNoetherianRings(x, *args, **opts)`

**Operations introduced here** (3 on objects)

*on objects*

- `ElementType()`
  - Noetherian commutative rings.
- `is_noetherian()`
- `krull_dimension()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedRings`](#cat-ownedrings) | 17 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 1 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `ArtinianRings` {#cat-artinianrings}

Artinian commutative rings.

- **defined at** `src/dzack_research/preamble/categories/rings/ring_foundation.py:1048`
- **probed as** `Category of owned artinian rings`
- **above** [`OwnedNoetherianRings`](#cat-ownednoetherianrings)
- **refines**, transitively, in Sage's linearization order: [`OwnedNoetherianRings`](#cat-ownednoetherianrings) · [`OwnedRings.Commutative`](#cat-ownedrings-commutative) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `ArtinianRings(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedRings`](#cat-ownedrings) | 17 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`OwnedNoetherianRings`](#cat-ownednoetherianrings) | 3 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`OwnedArtinianRings`](#cat-ownedartinianrings) | 2 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 1 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `OwnedArtinianRings` {#cat-ownedartinianrings}

Artinian commutative rings.

- **not exported**: reachable only as a supercategory
- **probed as** `Category of owned artinian rings`
- **above** [`OwnedNoetherianRings`](#cat-ownednoetherianrings)
- **below** [`Fields`](#cat-fields), [`OwnedFields`](#cat-ownedfields)
- **refines**, transitively, in Sage's linearization order: [`OwnedNoetherianRings`](#cat-ownednoetherianrings) · [`OwnedRings.Commutative`](#cat-ownedrings-commutative) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `OwnedArtinianRings(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - Artinian commutative rings.
- `is_artinian()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedRings`](#cat-ownedrings) | 17 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`OwnedNoetherianRings`](#cat-ownednoetherianrings) | 3 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 1 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `CompleteLocalRings` {#cat-completelocalrings}

Local rings complete for the represented maximal-ideal/adic topology.

- **defined at** `src/dzack_research/preamble/categories/rings/ring_foundation.py:1121`
- **probed as** `Category of owned complete local rings`
- **above** [`OwnedAdicallyCompleteRings`](#cat-ownedadicallycompleterings), [`OwnedLocalRings`](#cat-ownedlocalrings)
- **refines**, transitively, in Sage's linearization order: [`OwnedAdicallyCompleteRings`](#cat-ownedadicallycompleterings) · [`OwnedLocalRings`](#cat-ownedlocalrings) · [`OwnedRings.Commutative`](#cat-ownedrings-commutative) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `CompleteLocalRings(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedRings`](#cat-ownedrings) | 17 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`OwnedLocalRings`](#cat-ownedlocalrings) | 6 |  |  |
| [`OwnedAdicallyCompleteRings`](#cat-ownedadicallycompleterings) | 3 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 1 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedCompleteLocalRings`](#cat-ownedcompletelocalrings) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `OwnedCompleteLocalRings` {#cat-ownedcompletelocalrings}

Local rings complete for the represented maximal-ideal/adic topology.

- **not exported**: reachable only as a supercategory
- **probed as** `Category of owned complete local rings`
- **above** [`OwnedAdicallyCompleteRings`](#cat-ownedadicallycompleterings), [`OwnedLocalRings`](#cat-ownedlocalrings)
- **refines**, transitively, in Sage's linearization order: [`OwnedAdicallyCompleteRings`](#cat-ownedadicallycompleterings) · [`OwnedLocalRings`](#cat-ownedlocalrings) · [`OwnedRings.Commutative`](#cat-ownedrings-commutative) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `OwnedCompleteLocalRings(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Local rings complete for the represented maximal-ideal/adic topology.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedRings`](#cat-ownedrings) | 17 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`OwnedLocalRings`](#cat-ownedlocalrings) | 6 |  |  |
| [`OwnedAdicallyCompleteRings`](#cat-ownedadicallycompleterings) | 3 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 1 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `OwnedOrders` {#cat-ownedorders}

Orders in number fields as a ring-theoretic property category.

- **defined at** `src/dzack_research/preamble/categories/rings/ring_foundation.py:1169`
- **probed as** `Category of owned orders`
- **above** [`OwnedIntegralDomains`](#cat-ownedintegraldomains), [`OwnedNoetherianRings`](#cat-ownednoetherianrings)
- **refines**, transitively, in Sage's linearization order: [`OwnedNoetherianRings`](#cat-ownednoetherianrings) · [`OwnedIntegralDomains`](#cat-ownedintegraldomains) · [`OwnedRings.Commutative`](#cat-ownedrings-commutative) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `OwnedOrders(x, *args, **opts)`

**Operations introduced here** (3 on objects)

*on objects*

- `ElementType()`
  - Orders in number fields as a ring-theoretic property category.
- `cardinality()`
- `is_maximal() -> bool`
  - Return whether this is the maximal order of its fraction field.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedRings`](#cat-ownedrings) | 17 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`OwnedNoetherianRings`](#cat-ownednoetherianrings) | 3 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`OwnedIntegralDomains`](#cat-ownedintegraldomains) | 2 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 1 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `OwnedPrincipalIdealDomains` {#cat-ownedprincipalidealdomains}

Principal ideal domains in the owned ring hierarchy.

- **not exported**: reachable only as a supercategory
- **probed as** `Category of owned principal ideal domains`
- **above** [`OwnedIntegralDomains`](#cat-ownedintegraldomains), [`OwnedNoetherianRings`](#cat-ownednoetherianrings)
- **below** [`Fields`](#cat-fields), [`OwnedFields`](#cat-ownedfields)
- **refines**, transitively, in Sage's linearization order: [`OwnedNoetherianRings`](#cat-ownednoetherianrings) · [`OwnedIntegralDomains`](#cat-ownedintegraldomains) · [`OwnedRings.Commutative`](#cat-ownedrings-commutative) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `OwnedPrincipalIdealDomains(x, *args, **opts)`
- **specimens** `ZZ`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Principal ideal domains in the owned ring hierarchy.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedRings`](#cat-ownedrings) | 17 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`OwnedNoetherianRings`](#cat-ownednoetherianrings) | 3 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`OwnedIntegralDomains`](#cat-ownedintegraldomains) | 2 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 1 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `PrincipalIdealDomains` {#cat-principalidealdomains}

Principal ideal domains in the owned ring hierarchy.

- **defined at** `src/dzack_research/preamble/categories/rings/ring_foundation.py:1005`
- **probed as** `Category of owned principal ideal domains`
- **above** [`OwnedIntegralDomains`](#cat-ownedintegraldomains), [`OwnedNoetherianRings`](#cat-ownednoetherianrings)
- **refines**, transitively, in Sage's linearization order: [`OwnedNoetherianRings`](#cat-ownednoetherianrings) · [`OwnedIntegralDomains`](#cat-ownedintegraldomains) · [`OwnedRings.Commutative`](#cat-ownedrings-commutative) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `PrincipalIdealDomains(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedRings`](#cat-ownedrings) | 17 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`OwnedNoetherianRings`](#cat-ownednoetherianrings) | 3 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`OwnedIntegralDomains`](#cat-ownedintegraldomains) | 2 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 1 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedPrincipalIdealDomains`](#cat-ownedprincipalidealdomains) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `Fields` {#cat-fields}

Base class for categories belonging to the owned mathematical graph.

```text
Over :class:`owned_category_bases.Category`, which ties this category's
``ParentMethods`` / ``ElementMethods`` / ``MorphismMethods`` into the
named classes as real bases.  Sage's own builder passes
``prepend_cls_bases=False``, so only a copy of the container's
``__dict__`` reaches the MRO -- a copy carries no bases, so it cannot
carry ``Parent``, so it cannot carry fields or a constructor.  That, and
nothing else, is why a level would otherwise need a hand-written parent
class beside its category.
```

- **defined at** `src/dzack_research/preamble/categories/rings/ring_foundation.py:1143`
- **probed as** `Category of owned fields`
- **above** [`OwnedArtinianRings`](#cat-ownedartinianrings), [`OwnedDivisionRings`](#cat-owneddivisionrings), [`OwnedIntegralDomains`](#cat-ownedintegraldomains), [`OwnedLocalRings`](#cat-ownedlocalrings), [`OwnedNoetherianRings`](#cat-ownednoetherianrings), [`OwnedPrincipalIdealDomains`](#cat-ownedprincipalidealdomains)
- **refines**, transitively, in Sage's linearization order: [`OwnedLocalRings`](#cat-ownedlocalrings) · [`OwnedArtinianRings`](#cat-ownedartinianrings) · [`OwnedPrincipalIdealDomains`](#cat-ownedprincipalidealdomains) · [`OwnedDivisionRings`](#cat-owneddivisionrings) · [`OwnedNoetherianRings`](#cat-ownednoetherianrings) · [`OwnedIntegralDomains`](#cat-ownedintegraldomains) · [`OwnedRings.Commutative`](#cat-ownedrings-commutative) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `Fields(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedRings`](#cat-ownedrings) | 17 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`OwnedLocalRings`](#cat-ownedlocalrings) | 6 |  |  |
| [`OwnedFields`](#cat-ownedfields) | 4 |  |  |
| [`OwnedNoetherianRings`](#cat-ownednoetherianrings) | 3 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`OwnedArtinianRings`](#cat-ownedartinianrings) | 2 |  |  |
| [`OwnedIntegralDomains`](#cat-ownedintegraldomains) | 2 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 1 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedDivisionRings`](#cat-owneddivisionrings) | 1 |  |  |
| [`OwnedPrincipalIdealDomains`](#cat-ownedprincipalidealdomains) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `FormalPowerSeriesRings(R)` {#cat-formalpowerseriesrings}

Formal power-series rings `R[[t]]` over the owned ring `R`.

- **defined at** `src/dzack_research/preamble/categories/rings/commutative_algebra.py:1191`
- **probed as** `Category of formal power-series rings`
- **above** [`Algebras.Commutative`](#cat-algebras-commutative), [`OwnedAdicallyCompleteRings`](#cat-ownedadicallycompleterings)
- **refines**, transitively, in Sage's linearization order: [`OwnedAdicallyCompleteRings`](#cat-ownedadicallycompleterings) · [`Algebras.Commutative`](#cat-algebras-commutative) · [`Algebras(R)`](#cat-algebras) · [`OwnedRings.Commutative`](#cat-ownedrings-commutative) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AssociativeAlgebras(R)`](#cat-associativealgebras) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `FormalPowerSeriesRings(R)(x, *args, **opts)`

**Operations introduced here** (2 on objects, 1 on elements)

*on objects*

- `ElementType()`
  - Commutative rings represented as complete for a chosen adic topology.
- `power_series_variable()`

*on elements*

- `coefficient(degree)`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 17 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Algebras(R)`](#cat-algebras) | 12 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`OwnedAdicallyCompleteRings`](#cat-ownedadicallycompleterings) | 3 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`AssociativeAlgebras(R)`](#cat-associativealgebras) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `OwnedFields` {#cat-ownedfields}

Base class for categories belonging to the owned mathematical graph.

```text
Over :class:`owned_category_bases.Category`, which ties this category's
``ParentMethods`` / ``ElementMethods`` / ``MorphismMethods`` into the
named classes as real bases.  Sage's own builder passes
``prepend_cls_bases=False``, so only a copy of the container's
``__dict__`` reaches the MRO -- a copy carries no bases, so it cannot
carry ``Parent``, so it cannot carry fields or a constructor.  That, and
nothing else, is why a level would otherwise need a hand-written parent
class beside its category.
```

- **defined at** `src/dzack_research/preamble/categories/rings/ring_foundation.py:1143`
- **probed as** `Category of owned fields`
- **above** [`OwnedArtinianRings`](#cat-ownedartinianrings), [`OwnedDivisionRings`](#cat-owneddivisionrings), [`OwnedIntegralDomains`](#cat-ownedintegraldomains), [`OwnedLocalRings`](#cat-ownedlocalrings), [`OwnedNoetherianRings`](#cat-ownednoetherianrings), [`OwnedPrincipalIdealDomains`](#cat-ownedprincipalidealdomains)
- **below** [`OwnedNumberFields`](#cat-ownednumberfields), [`PrimeFields`](#cat-primefields)
- **refines**, transitively, in Sage's linearization order: [`OwnedLocalRings`](#cat-ownedlocalrings) · [`OwnedArtinianRings`](#cat-ownedartinianrings) · [`OwnedPrincipalIdealDomains`](#cat-ownedprincipalidealdomains) · [`OwnedDivisionRings`](#cat-owneddivisionrings) · [`OwnedNoetherianRings`](#cat-ownednoetherianrings) · [`OwnedIntegralDomains`](#cat-ownedintegraldomains) · [`OwnedRings.Commutative`](#cat-ownedrings-commutative) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `OwnedFields(x, *args, **opts)`
- **specimens** `AA`, `CC`, `CDF`, `QQbar`, `RDF`, `RR`

**Operations introduced here** (4 on objects)

*on objects*

- `ElementType()`
  - Commutative rings equipped with their unique maximal ideal.
- `maximal_ideal()`
- `residue_field()`
- `residue_map()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedRings`](#cat-ownedrings) | 17 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`OwnedLocalRings`](#cat-ownedlocalrings) | 6 |  |  |
| [`OwnedNoetherianRings`](#cat-ownednoetherianrings) | 3 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`OwnedArtinianRings`](#cat-ownedartinianrings) | 2 |  |  |
| [`OwnedIntegralDomains`](#cat-ownedintegraldomains) | 2 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 1 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedDivisionRings`](#cat-owneddivisionrings) | 1 |  |  |
| [`OwnedPrincipalIdealDomains`](#cat-ownedprincipalidealdomains) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `OwnedNumberFields` {#cat-ownednumberfields}

Finite extensions of `QQ`.

- **defined at** `src/dzack_research/preamble/categories/rings/number_fields.py:83`
- **probed as** `Category of number fields`
- **above** [`OwnedFields`](#cat-ownedfields)
- **below** [`NumberFieldsWithChosenPrimitiveElement`](#cat-numberfieldswithchosenprimitiveelement)
- **refines**, transitively, in Sage's linearization order: [`OwnedFields`](#cat-ownedfields) · [`OwnedLocalRings`](#cat-ownedlocalrings) · [`OwnedArtinianRings`](#cat-ownedartinianrings) · [`OwnedPrincipalIdealDomains`](#cat-ownedprincipalidealdomains) · [`OwnedDivisionRings`](#cat-owneddivisionrings) · [`OwnedNoetherianRings`](#cat-ownednoetherianrings) · [`OwnedIntegralDomains`](#cat-ownedintegraldomains) · [`OwnedRings.Commutative`](#cat-ownedrings-commutative) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `OwnedNumberFields(x, *args, **opts)`
- **specimens** `QQ`

**Operations introduced here** (17 on objects)

*on objects*

- `Mor(codomain, category=None)`
- `as_algebra()`
  - Return this field with its selected finite ``QQ``-algebra presentation.
- `class_number()`
  - Return the class number of the ring of integers.
- `degree()`
  - Return ``[K:QQ]`` as an owned integer.
- `discriminant()`
  - Return the discriminant of the ring of integers of ``K``.
- `embeddings(target)`
  - Return the exact owned field embeddings ``K -> target``.
- `extension(polynomial, name='a')`
  - Return the finite extension defined by an owned polynomial over ``self``.
- `galois_group()`
  - Return ``Gal(K/QQ)``; this name is reserved for Galois ``K``.
- `is_galois() -> bool`
  - Return whether ``K/QQ`` is Galois.
- `maximal_order()`
  - Return the maximal order ``O_K`` as an owned ring.
- `normal_closure()`
  - Return a chosen normal closure of ``K/QQ``.
- `normal_closure_galois_group()`
  - Return the Galois group of a chosen normal closure of ``K``.
- `order_generated_by(*generators)`
  - Return the order ``ZZ[generators]`` inside this number field.
- `primes_above(prime)`
  - Return the prime ideals of ``O_K`` above a rational prime.
- `ramified_primes()`
  - Return the rational primes ramified in ``K``.
- `ring_of_integers()`
  - Return the maximal order ``O_K`` as an owned ring.
- `signature()`
  - Return the signature pair ``(r_1,r_2)`` with ``r_1+2r_2=[K:QQ]``.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedRings`](#cat-ownedrings) | 17 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`OwnedLocalRings`](#cat-ownedlocalrings) | 6 |  |  |
| [`OwnedFields`](#cat-ownedfields) | 4 |  |  |
| [`OwnedNoetherianRings`](#cat-ownednoetherianrings) | 3 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`OwnedArtinianRings`](#cat-ownedartinianrings) | 2 |  |  |
| [`OwnedIntegralDomains`](#cat-ownedintegraldomains) | 2 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 1 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedDivisionRings`](#cat-owneddivisionrings) | 1 |  |  |
| [`OwnedPrincipalIdealDomains`](#cat-ownedprincipalidealdomains) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `PrimeFields` {#cat-primefields}

Prime fields \(\mathbf F_p\).

- **defined at** `src/dzack_research/preamble/categories/rings/ring_foundation.py:1197`
- **probed as** `Category of prime fields`
- **above** [`OwnedFields`](#cat-ownedfields)
- **refines**, transitively, in Sage's linearization order: [`OwnedFields`](#cat-ownedfields) · [`OwnedLocalRings`](#cat-ownedlocalrings) · [`OwnedArtinianRings`](#cat-ownedartinianrings) · [`OwnedPrincipalIdealDomains`](#cat-ownedprincipalidealdomains) · [`OwnedDivisionRings`](#cat-owneddivisionrings) · [`OwnedNoetherianRings`](#cat-ownednoetherianrings) · [`OwnedIntegralDomains`](#cat-ownedintegraldomains) · [`OwnedRings.Commutative`](#cat-ownedrings-commutative) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `PrimeFields(x, *args, **opts)`
- **specimens** `QQ`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Prime fields \(\mathbf F_p\).

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedRings`](#cat-ownedrings) | 17 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`OwnedLocalRings`](#cat-ownedlocalrings) | 6 |  |  |
| [`OwnedFields`](#cat-ownedfields) | 4 |  |  |
| [`OwnedNoetherianRings`](#cat-ownednoetherianrings) | 3 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`OwnedArtinianRings`](#cat-ownedartinianrings) | 2 |  |  |
| [`OwnedIntegralDomains`](#cat-ownedintegraldomains) | 2 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 1 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedDivisionRings`](#cat-owneddivisionrings) | 1 |  |  |
| [`OwnedPrincipalIdealDomains`](#cat-ownedprincipalidealdomains) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `NumberFieldsWithChosenPrimitiveElement` {#cat-numberfieldswithchosenprimitiveelement}

Number fields carrying the primitive element selected by their presentation.

- **defined at** `src/dzack_research/preamble/categories/rings/number_fields.py:293`
- **probed as** `Category of number fields with a chosen primitive element`
- **above** [`OwnedNumberFields`](#cat-ownednumberfields)
- **refines**, transitively, in Sage's linearization order: [`OwnedNumberFields`](#cat-ownednumberfields) · [`OwnedFields`](#cat-ownedfields) · [`OwnedLocalRings`](#cat-ownedlocalrings) · [`OwnedArtinianRings`](#cat-ownedartinianrings) · [`OwnedPrincipalIdealDomains`](#cat-ownedprincipalidealdomains) · [`OwnedDivisionRings`](#cat-owneddivisionrings) · [`OwnedNoetherianRings`](#cat-ownednoetherianrings) · [`OwnedIntegralDomains`](#cat-ownedintegraldomains) · [`OwnedRings.Commutative`](#cat-ownedrings-commutative) · [`OwnedRings`](#cat-ownedrings) · [`OwnedSemirings`](#cat-ownedsemirings) · [`Monoids`](#cat-monoids) · [`OwnedRngs`](#cat-ownedrngs) · [`Semigroups`](#cat-semigroups) · [`Magmas`](#cat-magmas) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `NumberFieldsWithChosenPrimitiveElement(x, *args, **opts)`

**Operations introduced here** (5 on objects)

*on objects*

- `algebra_generating_set()`
- `algebra_generator(label)`
- `defining_polynomial()`
  - Return the owned defining polynomial of the selected primitive element.
- `embedding_images(target)`
  - Return the images of the selected primitive element under ``K -> target``.
- `primitive_element()`
  - Return the selected primitive element ``alpha``.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`OwnedNumberFields`](#cat-ownednumberfields) | 17 |  |  |
| [`OwnedRings`](#cat-ownedrings) | 17 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`OwnedLocalRings`](#cat-ownedlocalrings) | 6 |  |  |
| [`OwnedFields`](#cat-ownedfields) | 4 |  |  |
| [`OwnedNoetherianRings`](#cat-ownednoetherianrings) | 3 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`OwnedArtinianRings`](#cat-ownedartinianrings) | 2 |  |  |
| [`OwnedIntegralDomains`](#cat-ownedintegraldomains) | 2 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 1 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Magmas`](#cat-magmas) | 1 |  |  |
| [`Monoids`](#cat-monoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`OwnedDivisionRings`](#cat-owneddivisionrings) | 1 |  |  |
| [`OwnedPrincipalIdealDomains`](#cat-ownedprincipalidealdomains) | 1 |  |  |
| [`OwnedRngs`](#cat-ownedrngs) | 1 |  |  |
| [`OwnedSemirings`](#cat-ownedsemirings) | 1 |  |  |
| [`Semigroups`](#cat-semigroups) | 1 |  |  |

#### `OwnedCategoryOverBaseRing(R)` {#cat-ownedcategoryoverbasering}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/rings/ring_foundation.py:1208`
- **could not be built**: NotImplementedError: <abstract method super_categories at 0x7f8532351a60>

### Objects

#### `ExactRealField` <sub>OBJECT</sub>

The exact field of real numbers represented by closed exact expressions.

- **defined at** `src/dzack_research/preamble/rings/real.py:441`
- **built by** `ExactRealField()`

**Operations**

- `Element(parent: 'ExactRealField', expression: sage.symbolic.expression.Expression) -> None`
  - An exact, explicitly real number.
- `cardinality()`
- `characteristic()`
- `e() -> dzack_research.preamble.rings.real.ExactRealNumber`
- `fraction_field()`
- `is_exact() -> bool`
  - Parent.is_exact(self) -> bool
- `is_finite() -> bool`
- `one() -> dzack_research.preamble.rings.real.ExactRealNumber`
  - Ring.one(self)
- `pi() -> dzack_research.preamble.rings.real.ExactRealNumber`
- `relation(left: dzack_research.preamble.rings.real.ExactRealNumber, right: dzack_research.preamble.rings.real.ExactRealNumber, relation)`
  - Return a decided Boolean or an exact real relation predicate.
- `zero() -> dzack_research.preamble.rings.real.ExactRealNumber`
  - Ring.zero(self)

### Elements

#### `ExactRealNumber` <sub>ELEMENT</sub>

An exact, explicitly real number.

- **defined at** `src/dzack_research/preamble/rings/real.py:260`
- **built by** `ExactRealNumber(parent: 'ExactRealField', expression: sage.symbolic.expression.Expression)`

**Operations**

- `cos()`
- `exp()`
- `expression() -> sage.symbolic.expression.Expression`
  - Return the exact symbolic expression representing this real.
- `is_negative()`
- `is_one()`
  - RingElement.is_one(self)
- `is_positive()`
- `is_real() -> bool`
- `is_zero()`
  - Element.is_zero(self)
- `log(base=None)`
- `n(prec: int = 53, digits: int | None = None, **kwds)`
  - Return an explicit floating-point approximation of ``self``.
- `numerical_approx(prec: int = 53, digits: int | None = None, **kwds)`
  - Return an explicit floating-point approximation of ``self``.
- `sin()`
- `sqrt()`
- `tan()`

### Morphisms and homsets

#### `DistinguishedOpenSubobject` <sub>MORPHISM</sub>

The distinguished open subobject `D(f) -> Spec(R)`.

- **defined at** `src/dzack_research/preamble/categories/rings/commutative_algebra.py:329`
- **built by** `DistinguishedOpenSubobject(spectrum, function)`

**Operations**

- `coordinate_ring()`
- `function()`

#### `ZariskiClosedSubobject` <sub>MORPHISM</sub>

The closed subobject `V(I) -> Spec(R)`.

- **defined at** `src/dzack_research/preamble/categories/rings/commutative_algebra.py:295`
- **built by** `ZariskiClosedSubobject(spectrum, ideal)`

**Operations**

- `defining_ideal()`

### Objects the session already holds

#### `AA` <sub>LIVE OBJECT</sub>

An owned ring parent with one private computational realization.

- **is** Algebraic Real Field
- **in** Join of Category of commutative algebras and Category of owned fields

#### `CC` <sub>LIVE OBJECT</sub>

An owned ring parent with one private computational realization.

- **is** Complex Field with 53 bits of precision
- **in** Join of Category of commutative algebras and Category of owned fields and Category of uncountable sets

#### `CDF` <sub>LIVE OBJECT</sub>

An owned ring parent with one private computational realization.

- **is** Complex Double Field
- **in** Join of Category of commutative algebras and Category of owned fields and Category of uncountable sets

#### `NonNegativeReals` <sub>LIVE OBJECT</sub>

The additive monoid \(([0,\infty],+)\).

- **is** Nonnegative extended real numbers
- **in** Join of Category of additive monoids and Category of commutative additive monoids and Category of infinite sets and Category of infinite sets

#### `QQ` <sub>LIVE OBJECT</sub>

An owned ring parent with one private computational realization.

- **is** Rational Field
- **in** Join of Category of number fields and Category of commutative algebras and Category of prime fields and Category of owned ordered rings and Category of countably infinite sets

#### `QQbar` <sub>LIVE OBJECT</sub>

An owned ring parent with one private computational realization.

- **is** Algebraic Field
- **in** Join of Category of commutative algebras and Category of owned fields and Category of countably infinite sets

#### `RDF` <sub>LIVE OBJECT</sub>

An owned ring parent with one private computational realization.

- **is** Real Double Field
- **in** Join of Category of commutative algebras and Category of owned fields and Category of uncountable sets

#### `RR` <sub>LIVE OBJECT</sub>

The exact field of real numbers represented by closed exact expressions.

- **is** Real Field
- **in** Join of Category of commutative algebras and Category of owned fields and Category of uncountable sets

#### `UnitInterval` <sub>LIVE OBJECT</sub>

The monoid \(([0,1],\oplus)\) with \(s\oplus t=s+t-1\) and identity \(1\).

- **is** unit interval under s⊕t = s+t-1
- **in** Join of Category of monoids and Category of commutative monoids and Category of infinite sets and Category of infinite sets

#### `ZZ` <sub>LIVE OBJECT</sub>

An owned ring parent with one private computational realization.

- **is** Integer Ring
- **in** Join of Category of orders with a chosen integral basis and Category of commutative algebras and Category of owned ordered rings and Category of owned principal ideal domains and Category of countably infinite sets

### Functions

#### `CommutativeIdeal` <sub>FUNCTION</sub>

Return `(generators) <= R` with its selected module inclusion.

- **defined at** `src/dzack_research/preamble/categories/rings/commutative_ideals.py:582`
- **built by** `CommutativeIdeal(ring, *generators)`

#### `CommutativeRings` <sub>FUNCTION</sub>

The category of commutative unital rings.

```text
The session name for ``OwnedRings().Commutative()``: commutativity is an
axiom on the operation, and this is the category it cuts out.
```

- **defined at** `src/dzack_research/preamble/categories/rings/ring_foundation.py:1871`
- **built by** `CommutativeRings()`

#### `ComplexField` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/rings/__init__.py:139`
- **built by** `ComplexField(*args, **kwargs)`

#### `CyclotomicField` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/rings/__init__.py:143`
- **built by** `CyclotomicField(*args, **kwargs)`

#### `DualNumbers` <sub>FUNCTION</sub>

Return the dual-number algebra `R[epsilon]/(epsilon^2)`.

- **defined at** `src/dzack_research/preamble/categories/rings/commutative_algebra.py:1318`
- **built by** `DualNumbers(base_ring, name='epsilon')`

#### `FiniteField` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/rings/__init__.py:112`
- **built by** `FiniteField(*args, **kwargs)`

#### `GF` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/rings/__init__.py:112`
- **built by** `GF(*args, **kwargs)`

#### `IntegerModRing` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/rings/__init__.py:123`
- **built by** `IntegerModRing(*args, **kwargs)`

#### `Integers` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/rings/__init__.py:123`
- **built by** `Integers(*args, **kwargs)`

#### `LaurentPolynomialRing` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/rings/__init__.py:159`
- **built by** `LaurentPolynomialRing(base_ring, *args, **kwargs)`

#### `MatrixSpace` <sub>FUNCTION</sub>

Return the public finite matrix Hom, with algebra structure when square.

- **defined at** `src/dzack_research/preamble/rings/__init__.py:170`
- **built by** `MatrixSpace(base_ring, nrows, ncols=None)`

#### `NumberField` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/rings/__init__.py:151`
- **built by** `NumberField(polynomial, *args, **kwargs)`

#### `PolynomialRing` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/rings/__init__.py:155`
- **built by** `PolynomialRing(base_ring, *args, **kwargs)`

#### `PowerSeriesRing` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/rings/commutative_algebra.py:1276`
- **built by** `PowerSeriesRing(base_ring, *args, **kwargs)`

#### `PrimeField` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/rings/__init__.py:119`
- **built by** `PrimeField(characteristic)`

#### `Qp` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/rings/__init__.py:131`
- **built by** `Qp(*args, **kwargs)`

#### `QuadraticField` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/rings/__init__.py:147`
- **built by** `QuadraticField(*args, **kwargs)`

#### `RealApproximation` <sub>FUNCTION</sub>

Return the owned finite-precision real represented by `value`.

- **defined at** `src/dzack_research/preamble/rings/real.py:53`
- **built by** `RealApproximation(value)`

#### `RealField` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/rings/__init__.py:135`
- **built by** `RealField(*args, **kwargs)`

#### `ResidueField` <sub>FUNCTION</sub>

Return `R/m` for a maximal ideal, or the represented local residue field.

- **defined at** `src/dzack_research/preamble/categories/rings/commutative_algebra.py:1092`
- **built by** `ResidueField(ring, ideal=None)`

#### `Zmod` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/rings/__init__.py:123`
- **built by** `Zmod(*args, **kwargs)`

#### `Zp` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/rings/commutative_algebra.py:1263`
- **built by** `Zp(*args, **kwargs)`

#### `predicate_subring` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/rings/ring_foundation.py:669`
- **built by** `predicate_subring(ambient_ring, predicate, description, category=None)`

## Schemes & Algebraic Geometry

> Schemes, Affine/Projective schemes, Subschemes, Varieties, Curves, Surfaces, Polytopes, and Structure sheaves.

```mermaid
graph RL
  AffineSchemes["AffineSchemes(R)"]
  AffineSpaces["AffineSpaces(R)"]
  ConvexPolygons["ConvexPolygons"]
  ConvexPolytopes["ConvexPolytopes"]
  Curves["Curves(R)"]
  FiberProductSchemes["FiberProductSchemes(R)"]
  FiniteTypeSchemes["FiniteTypeSchemes(R)"]
  IntegralSchemes["IntegralSchemes(R)"]
  LatticePolygons["LatticePolygons"]
  LatticePolytopes["LatticePolytopes"]
  LocallyRingedSpaces["LocallyRingedSpaces"]
  NormalSchemes["NormalSchemes(R)"]
  ProductProjectiveSpaces["ProductProjectiveSpaces(R)"]
  ProductSchemes["ProductSchemes(R)"]
  ProjectiveSchemes["ProjectiveSchemes(R)"]
  ProjectiveSpaces["ProjectiveSpaces(R)"]
  QuasiAffineSchemes["QuasiAffineSchemes(R)"]
  QuasiProjectiveSchemes["QuasiProjectiveSchemes(R)"]
  RingedSpaces["RingedSpaces"]
  Schemes["Schemes(R)"]
  SeparatedSchemes["SeparatedSchemes(R)"]
  SmoothSchemes["SmoothSchemes(R)"]
  Surfaces["Surfaces(R)"]
  Varieties["Varieties(R)"]
  Sets("Sets")
  AffineSchemes --> QuasiAffineSchemes
  AffineSchemes --> Schemes
  AffineSchemes --> SeparatedSchemes
  AffineSpaces --> AffineSchemes
  AffineSpaces --> FiniteTypeSchemes
  AffineSpaces --> SmoothSchemes
  ConvexPolygons --> ConvexPolytopes
  ConvexPolytopes --> Sets
  Curves --> Varieties
  FiberProductSchemes --> AffineSchemes
  FiniteTypeSchemes --> Schemes
  IntegralSchemes --> Schemes
  LatticePolygons --> ConvexPolygons
  LatticePolygons --> LatticePolytopes
  LatticePolytopes --> ConvexPolytopes
  LocallyRingedSpaces --> RingedSpaces
  NormalSchemes --> Schemes
  ProductProjectiveSpaces --> ProductSchemes
  ProductProjectiveSpaces --> ProjectiveSchemes
  ProductProjectiveSpaces --> SmoothSchemes
  ProductSchemes --> Schemes
  ProjectiveSchemes --> FiniteTypeSchemes
  ProjectiveSchemes --> QuasiProjectiveSchemes
  ProjectiveSchemes --> Schemes
  ProjectiveSchemes --> SeparatedSchemes
  ProjectiveSpaces --> ProjectiveSchemes
  ProjectiveSpaces --> SmoothSchemes
  QuasiAffineSchemes --> Schemes
  QuasiAffineSchemes --> SeparatedSchemes
  QuasiProjectiveSchemes --> Schemes
  QuasiProjectiveSchemes --> SeparatedSchemes
  RingedSpaces --> Sets
  Schemes --> LocallyRingedSpaces
  SeparatedSchemes --> Schemes
  SmoothSchemes --> Schemes
  Surfaces --> Varieties
  Varieties --> FiniteTypeSchemes
  Varieties --> IntegralSchemes
  Varieties --> Schemes
  Varieties --> SeparatedSchemes
  classDef outside stroke-dasharray:6 4,fill:#f8fafc;
  class Sets outside;
```

### Categories

Ordered by depth: the least structured first.

#### `ConvexPolytopes` {#cat-convexpolytopes}

Rational convex polytopes in a chosen coordinate lattice.

```text
Public coordinate data live in the owned modules ``ZZ^n`` and ``QQ^n``.
Sage's exact ``Polyhedron`` is retained only as the private polyhedral
computation engine.
```

- **defined at** `src/dzack_research/preamble/categories/schemes/polytopes.py:25`
- **probed as** `Category of convex polytopes`
- **above** [`Sets`](#cat-sets)
- **below** [`ConvexPolygons`](#cat-convexpolygons), [`LatticePolytopes`](#cat-latticepolytopes)
- **refines**, transitively, in Sage's linearization order: [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `ConvexPolytopes(x, *args, **opts)`

**Operations introduced here** (24 on objects)

*on objects*

- `ElementType()`
  - Rational convex polytopes in a chosen coordinate lattice.
- `ambient_lattice()`
  - Return the owned coordinate lattice ``ZZ^n``.
- `ambient_space()`
  - Return the owned rational coordinate module ``QQ^n``.
- `boundary_integral_points()`
- `contains_point(point) -> bool`
- `dimension()`
- `ehrhart_polynomial(variable='t')`
  - Return the exact owned Ehrhart polynomial by interpolation.
- `facets()`
  - Return the codimension-one faces as owned polytopes.
- `h_star_vector()`
  - Return the owned Ehrhart ``h*`` vector ``(h*_0,...,h*_d)``.
- `integral_points()`
- `interior_contains_point(point) -> bool`
- `interior_integral_points()`
- `is_compact() -> bool`
- `is_lattice_polytope() -> bool`
- `is_reflexive() -> bool`
- `is_smooth() -> bool`
- `n_boundary_points()`
- `n_integral_points()`
- `n_interior_points()`
- `n_vertices()`
- `normalized_volume()`
- `polar_dual()`
- `vertices()`
- `volume()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `RingedSpaces` {#cat-ringedspaces}

Ringed spaces `(X,O_X)`.

- **defined at** `src/dzack_research/preamble/categories/schemes/ringed_spaces.py:420`
- **probed as** `Category of ringed spaces`
- **above** [`Sets`](#cat-sets)
- **below** [`LocallyRingedSpaces`](#cat-locallyringedspaces)
- **refines**, transitively, in Sage's linearization order: [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `RingedSpaces(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `structure_sheaf()` <sub>cached</sub>
- `underlying_space()` <sub>cached</sub>

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `ConvexPolygons` {#cat-convexpolygons}

Convex polytopes of affine dimension two.

- **defined at** `src/dzack_research/preamble/categories/schemes/polytopes.py:376`
- **probed as** `Category of convex polygons`
- **above** [`ConvexPolytopes`](#cat-convexpolytopes)
- **below** [`LatticePolygons`](#cat-latticepolygons)
- **refines**, transitively, in Sage's linearization order: [`ConvexPolytopes`](#cat-convexpolytopes) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `ConvexPolygons(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Convex polytopes of affine dimension two.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`ConvexPolytopes`](#cat-convexpolytopes) | 24 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `LatticePolytopes` {#cat-latticepolytopes}

Convex polytopes all of whose vertices are lattice points.

- **defined at** `src/dzack_research/preamble/categories/schemes/polytopes.py:360`
- **probed as** `Category of lattice polytopes`
- **above** [`ConvexPolytopes`](#cat-convexpolytopes)
- **below** [`LatticePolygons`](#cat-latticepolygons)
- **refines**, transitively, in Sage's linearization order: [`ConvexPolytopes`](#cat-convexpolytopes) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `LatticePolytopes(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Convex polytopes all of whose vertices are lattice points.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`ConvexPolytopes`](#cat-convexpolytopes) | 24 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `LocallyRingedSpaces` {#cat-locallyringedspaces}

Ringed spaces whose stalks are local rings.

- **defined at** `src/dzack_research/preamble/categories/schemes/ringed_spaces.py:449`
- **probed as** `Category of locally ringed spaces`
- **above** [`RingedSpaces`](#cat-ringedspaces)
- **below** [`Schemes(R)`](#cat-schemes)
- **refines**, transitively, in Sage's linearization order: [`RingedSpaces`](#cat-ringedspaces) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `LocallyRingedSpaces(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `stalk(point)`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`RingedSpaces`](#cat-ringedspaces) | 2 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `Schemes(R)` {#cat-schemes}

Schemes over `Spec(R)` for the represented base ring `R`.

- **defined at** `src/dzack_research/preamble/categories/schemes/schemes.py:447`
- **probed as** `Category of schemes over Integer Ring`
- **above** [`LocallyRingedSpaces`](#cat-locallyringedspaces)
- **below** [`AffineSchemes(R)`](#cat-affineschemes), [`FiniteTypeSchemes(R)`](#cat-finitetypeschemes), [`IntegralSchemes(R)`](#cat-integralschemes), [`NormalSchemes(R)`](#cat-normalschemes), [`ProductSchemes(R)`](#cat-productschemes), [`ProjectiveSchemes(R)`](#cat-projectiveschemes), [`QuasiAffineSchemes(R)`](#cat-quasiaffineschemes), [`QuasiProjectiveSchemes(R)`](#cat-quasiprojectiveschemes), [`SeparatedSchemes(R)`](#cat-separatedschemes), [`SmoothSchemes(R)`](#cat-smoothschemes), [`Varieties(R)`](#cat-varieties)
- **refines**, transitively, in Sage's linearization order: [`LocallyRingedSpaces`](#cat-locallyringedspaces) · [`RingedSpaces`](#cat-ringedspaces) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `Schemes(R)(x, *args, **opts)`

**Operations introduced here** (13 on objects)

*on objects*

- `ElementType()`
  - Schemes over ``Spec(R)`` for the represented base ring ``R``.
- `Mor(codomain, category=None)`
- `as_slice_object()`
- `base_scheme()`
- `categorical_identity_morphism()`
- `point_count(extension_degree=1)`
  - Return ``#X(F_{q^n})`` for the stated extension degree ``n``.
- `point_counts(extension_degree)`
  - Return ``(#X(F_q),...,#X(F_{q^n}))`` for a finite base field.
- `point_morphism(coordinates)`
- `product(*others)`
- `relative_dimension()`
- `scheme_base_ring()`
- `scheme_category()`
- `structure_morphism()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`RingedSpaces`](#cat-ringedspaces) | 2 |  |  |
| [`LocallyRingedSpaces`](#cat-locallyringedspaces) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `FiniteTypeSchemes(R)` {#cat-finitetypeschemes}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/schemes/schemes.py:829`
- **probed as** `Category of finite-type schemes over Integer Ring`
- **above** [`Schemes(R)`](#cat-schemes)
- **below** [`AffineSpaces(R)`](#cat-affinespaces), [`ProjectiveSchemes(R)`](#cat-projectiveschemes), [`Varieties(R)`](#cat-varieties)
- **refines**, transitively, in Sage's linearization order: [`Schemes(R)`](#cat-schemes) · [`LocallyRingedSpaces`](#cat-locallyringedspaces) · [`RingedSpaces`](#cat-ringedspaces) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `FiniteTypeSchemes(R)(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - Schemes over ``Spec(R)`` for the represented base ring ``R``.
- `is_finite_type()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Schemes(R)`](#cat-schemes) | 13 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`RingedSpaces`](#cat-ringedspaces) | 2 |  |  |
| [`LocallyRingedSpaces`](#cat-locallyringedspaces) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `IntegralSchemes(R)` {#cat-integralschemes}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/schemes/schemes.py:845`
- **probed as** `Category of integral schemes over Integer Ring`
- **above** [`Schemes(R)`](#cat-schemes)
- **below** [`Varieties(R)`](#cat-varieties)
- **refines**, transitively, in Sage's linearization order: [`Schemes(R)`](#cat-schemes) · [`LocallyRingedSpaces`](#cat-locallyringedspaces) · [`RingedSpaces`](#cat-ringedspaces) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `IntegralSchemes(R)(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - Schemes over ``Spec(R)`` for the represented base ring ``R``.
- `is_integral()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Schemes(R)`](#cat-schemes) | 13 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`RingedSpaces`](#cat-ringedspaces) | 2 |  |  |
| [`LocallyRingedSpaces`](#cat-locallyringedspaces) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `LatticePolygons` {#cat-latticepolygons}

Lattice polytopes of affine dimension two.

- **defined at** `src/dzack_research/preamble/categories/schemes/polytopes.py:394`
- **probed as** `Category of lattice polygons`
- **above** [`ConvexPolygons`](#cat-convexpolygons), [`LatticePolytopes`](#cat-latticepolytopes)
- **refines**, transitively, in Sage's linearization order: [`LatticePolytopes`](#cat-latticepolytopes) · [`ConvexPolygons`](#cat-convexpolygons) · [`ConvexPolytopes`](#cat-convexpolytopes) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `LatticePolygons(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Lattice polytopes of affine dimension two.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`ConvexPolytopes`](#cat-convexpolytopes) | 24 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`ConvexPolygons`](#cat-convexpolygons) | 1 |  |  |
| [`LatticePolytopes`](#cat-latticepolytopes) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `NormalSchemes(R)` {#cat-normalschemes}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/schemes/schemes.py:861`
- **probed as** `Category of normal schemes over Integer Ring`
- **above** [`Schemes(R)`](#cat-schemes)
- **refines**, transitively, in Sage's linearization order: [`Schemes(R)`](#cat-schemes) · [`LocallyRingedSpaces`](#cat-locallyringedspaces) · [`RingedSpaces`](#cat-ringedspaces) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `NormalSchemes(R)(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - Schemes over ``Spec(R)`` for the represented base ring ``R``.
- `is_normal()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Schemes(R)`](#cat-schemes) | 13 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`RingedSpaces`](#cat-ringedspaces) | 2 |  |  |
| [`LocallyRingedSpaces`](#cat-locallyringedspaces) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `ProductSchemes(R)` {#cat-productschemes}

Scheme products equipped with their stated factors and projections.

- **defined at** `src/dzack_research/preamble/categories/schemes/schemes.py:1518`
- **probed as** `Category of scheme products over Integer Ring`
- **above** [`Schemes(R)`](#cat-schemes)
- **below** [`ProductProjectiveSpaces(R)`](#cat-productprojectivespaces)
- **refines**, transitively, in Sage's linearization order: [`Schemes(R)`](#cat-schemes) · [`LocallyRingedSpaces`](#cat-locallyringedspaces) · [`RingedSpaces`](#cat-ringedspaces) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `ProductSchemes(R)(x, *args, **opts)`

**Operations introduced here** (5 on objects)

*on objects*

- `ElementType()`
  - Scheme products equipped with their stated factors and projections.
- `factors()`
  - Return the family of factors, indexed by the product's own index set.
- `number_of_factors()`
- `projection(index)`
- `projections()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Schemes(R)`](#cat-schemes) | 13 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`RingedSpaces`](#cat-ringedspaces) | 2 |  |  |
| [`LocallyRingedSpaces`](#cat-locallyringedspaces) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `SeparatedSchemes(R)` {#cat-separatedschemes}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/schemes/schemes.py:815`
- **probed as** `Category of separated schemes over Integer Ring`
- **above** [`Schemes(R)`](#cat-schemes)
- **below** [`AffineSchemes(R)`](#cat-affineschemes), [`ProjectiveSchemes(R)`](#cat-projectiveschemes), [`QuasiAffineSchemes(R)`](#cat-quasiaffineschemes), [`QuasiProjectiveSchemes(R)`](#cat-quasiprojectiveschemes), [`Varieties(R)`](#cat-varieties)
- **refines**, transitively, in Sage's linearization order: [`Schemes(R)`](#cat-schemes) · [`LocallyRingedSpaces`](#cat-locallyringedspaces) · [`RingedSpaces`](#cat-ringedspaces) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `SeparatedSchemes(R)(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - Schemes over ``Spec(R)`` for the represented base ring ``R``.
- `is_separated()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Schemes(R)`](#cat-schemes) | 13 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`RingedSpaces`](#cat-ringedspaces) | 2 |  |  |
| [`LocallyRingedSpaces`](#cat-locallyringedspaces) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `SmoothSchemes(R)` {#cat-smoothschemes}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/schemes/schemes.py:875`
- **probed as** `Category of smooth schemes over Integer Ring`
- **above** [`Schemes(R)`](#cat-schemes)
- **below** [`AffineSpaces(R)`](#cat-affinespaces), [`ProductProjectiveSpaces(R)`](#cat-productprojectivespaces), [`ProjectiveSpaces(R)`](#cat-projectivespaces)
- **refines**, transitively, in Sage's linearization order: [`Schemes(R)`](#cat-schemes) · [`LocallyRingedSpaces`](#cat-locallyringedspaces) · [`RingedSpaces`](#cat-ringedspaces) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `SmoothSchemes(R)(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - Schemes over ``Spec(R)`` for the represented base ring ``R``.
- `is_smooth()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Schemes(R)`](#cat-schemes) | 13 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`RingedSpaces`](#cat-ringedspaces) | 2 |  |  |
| [`LocallyRingedSpaces`](#cat-locallyringedspaces) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `QuasiAffineSchemes(R)` {#cat-quasiaffineschemes}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/schemes/schemes.py:1368`
- **probed as** `Category of quasi-affine schemes over Integer Ring`
- **above** [`Schemes(R)`](#cat-schemes), [`SeparatedSchemes(R)`](#cat-separatedschemes)
- **below** [`AffineSchemes(R)`](#cat-affineschemes)
- **refines**, transitively, in Sage's linearization order: [`SeparatedSchemes(R)`](#cat-separatedschemes) · [`Schemes(R)`](#cat-schemes) · [`LocallyRingedSpaces`](#cat-locallyringedspaces) · [`RingedSpaces`](#cat-ringedspaces) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `QuasiAffineSchemes(R)(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - Schemes over ``Spec(R)`` for the represented base ring ``R``.
- `is_quasi_affine()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Schemes(R)`](#cat-schemes) | 13 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`RingedSpaces`](#cat-ringedspaces) | 2 |  |  |
| [`SeparatedSchemes(R)`](#cat-separatedschemes) | 2 |  |  |
| [`LocallyRingedSpaces`](#cat-locallyringedspaces) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `QuasiProjectiveSchemes(R)` {#cat-quasiprojectiveschemes}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/schemes/schemes.py:1387`
- **probed as** `Category of quasi-projective schemes over Integer Ring`
- **above** [`Schemes(R)`](#cat-schemes), [`SeparatedSchemes(R)`](#cat-separatedschemes)
- **below** [`ProjectiveSchemes(R)`](#cat-projectiveschemes)
- **refines**, transitively, in Sage's linearization order: [`SeparatedSchemes(R)`](#cat-separatedschemes) · [`Schemes(R)`](#cat-schemes) · [`LocallyRingedSpaces`](#cat-locallyringedspaces) · [`RingedSpaces`](#cat-ringedspaces) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `QuasiProjectiveSchemes(R)(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - Schemes over ``Spec(R)`` for the represented base ring ``R``.
- `is_quasi_projective()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Schemes(R)`](#cat-schemes) | 13 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`RingedSpaces`](#cat-ringedspaces) | 2 |  |  |
| [`SeparatedSchemes(R)`](#cat-separatedschemes) | 2 |  |  |
| [`LocallyRingedSpaces`](#cat-locallyringedspaces) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `AffineSchemes(R)` {#cat-affineschemes}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/schemes/schemes.py:889`
- **probed as** `Category of affine schemes over Integer Ring`
- **above** [`QuasiAffineSchemes(R)`](#cat-quasiaffineschemes), [`Schemes(R)`](#cat-schemes), [`SeparatedSchemes(R)`](#cat-separatedschemes)
- **below** [`AffineSpaces(R)`](#cat-affinespaces), [`FiberProductSchemes(R)`](#cat-fiberproductschemes)
- **refines**, transitively, in Sage's linearization order: [`QuasiAffineSchemes(R)`](#cat-quasiaffineschemes) · [`SeparatedSchemes(R)`](#cat-separatedschemes) · [`Schemes(R)`](#cat-schemes) · [`LocallyRingedSpaces`](#cat-locallyringedspaces) · [`RingedSpaces`](#cat-ringedspaces) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `AffineSchemes(R)(x, *args, **opts)`

**Operations introduced here** (13 on objects)

*on objects*

- `ElementType()`
  - Schemes over ``Spec(R)`` for the represented base ring ``R``.
- `associated_module_sheaf(module)`
  - Return ``M~`` on the represented distinguished-open basis of this affine scheme.
- `closed_subscheme(*equations)`
- `coordinate_algebra()`
- `coordinate_ring()`
  - Return the owned coordinate ring/algebra of this affine scheme.
- `differential_rank_drop_subscheme(rank)`
  - Return the closed Fitting stratum ``V(Fitt_rank(Omega^1_{X/S}))``.
- `distinguished_open(element)`
  - Return \(D(f)\subseteq X\), the open locus where ``element`` is a unit.
- `distinguished_open_cover(*elements)`
  - Return the finite cover by ``D(f_i)`` when the ``f_i`` generate the unit ideal.
- `is_affine()`
- `is_flat() -> bool`
  - Return whether this represented affine scheme is flat over its base.
- `relative_differentials()` <sub>cached</sub>
  - Return the affine module of relative Kähler differentials.
- `relative_nonsmooth_subscheme()`
  - Return the relative nonsmooth locus in the supported flat hypersurface regime.
- `singular_subscheme()`
  - Return the nonsmooth closed subscheme in the supported equidimensional field case.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Schemes(R)`](#cat-schemes) | 13 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`QuasiAffineSchemes(R)`](#cat-quasiaffineschemes) | 2 |  |  |
| [`RingedSpaces`](#cat-ringedspaces) | 2 |  |  |
| [`SeparatedSchemes(R)`](#cat-separatedschemes) | 2 |  |  |
| [`LocallyRingedSpaces`](#cat-locallyringedspaces) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `FiberProductSchemes(R)` {#cat-fiberproductschemes}

Affine schemes equipped as selected pullbacks of one cospan.

- **defined at** `src/dzack_research/preamble/categories/schemes/schemes.py:2306`
- **probed as** `Category of fiber product schemes`
- **above** [`AffineSchemes(R)`](#cat-affineschemes)
- **refines**, transitively, in Sage's linearization order: [`AffineSchemes(R)`](#cat-affineschemes) · [`QuasiAffineSchemes(R)`](#cat-quasiaffineschemes) · [`SeparatedSchemes(R)`](#cat-separatedschemes) · [`Schemes(R)`](#cat-schemes) · [`LocallyRingedSpaces`](#cat-locallyringedspaces) · [`RingedSpaces`](#cat-ringedspaces) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `FiberProductSchemes(R)(x, *args, **opts)`

**Operations introduced here** (7 on objects)

*on objects*

- `ElementType()`
  - Affine schemes equipped as selected pullbacks of one cospan.
- `fiber_product_base()`
- `fiber_product_cospan()`
- `fiber_product_projections()`
- `from_pullback_cone(left_map, right_map)`
  - Return the unique represented map into this affine fiber product.
- `left_projection()`
- `right_projection()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`AffineSchemes(R)`](#cat-affineschemes) | 13 |  |  |
| [`Schemes(R)`](#cat-schemes) | 13 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`QuasiAffineSchemes(R)`](#cat-quasiaffineschemes) | 2 |  |  |
| [`RingedSpaces`](#cat-ringedspaces) | 2 |  |  |
| [`SeparatedSchemes(R)`](#cat-separatedschemes) | 2 |  |  |
| [`LocallyRingedSpaces`](#cat-locallyringedspaces) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `ProjectiveSchemes(R)` {#cat-projectiveschemes}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/schemes/schemes.py:1404`
- **probed as** `Category of projective schemes over Integer Ring`
- **above** [`FiniteTypeSchemes(R)`](#cat-finitetypeschemes), [`QuasiProjectiveSchemes(R)`](#cat-quasiprojectiveschemes), [`Schemes(R)`](#cat-schemes), [`SeparatedSchemes(R)`](#cat-separatedschemes)
- **below** [`ProductProjectiveSpaces(R)`](#cat-productprojectivespaces), [`ProjectiveSpaces(R)`](#cat-projectivespaces)
- **refines**, transitively, in Sage's linearization order: [`QuasiProjectiveSchemes(R)`](#cat-quasiprojectiveschemes) · [`FiniteTypeSchemes(R)`](#cat-finitetypeschemes) · [`SeparatedSchemes(R)`](#cat-separatedschemes) · [`Schemes(R)`](#cat-schemes) · [`LocallyRingedSpaces`](#cat-locallyringedspaces) · [`RingedSpaces`](#cat-ringedspaces) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `ProjectiveSchemes(R)(x, *args, **opts)`

**Operations introduced here** (3 on objects)

*on objects*

- `ElementType()`
  - Schemes over ``Spec(R)`` for the represented base ring ``R``.
- `closed_subscheme(*equations)`
- `is_projective()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Schemes(R)`](#cat-schemes) | 13 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`FiniteTypeSchemes(R)`](#cat-finitetypeschemes) | 2 |  |  |
| [`QuasiProjectiveSchemes(R)`](#cat-quasiprojectiveschemes) | 2 |  |  |
| [`RingedSpaces`](#cat-ringedspaces) | 2 |  |  |
| [`SeparatedSchemes(R)`](#cat-separatedschemes) | 2 |  |  |
| [`LocallyRingedSpaces`](#cat-locallyringedspaces) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `Varieties(R)` {#cat-varieties}

Integral separated schemes of finite type over the stated base.

- **defined at** `src/dzack_research/preamble/categories/schemes/varieties.py:12`
- **probed as** `Category of varieties over Integer Ring`
- **above** [`FiniteTypeSchemes(R)`](#cat-finitetypeschemes), [`IntegralSchemes(R)`](#cat-integralschemes), [`Schemes(R)`](#cat-schemes), [`SeparatedSchemes(R)`](#cat-separatedschemes)
- **below** [`Curves(R)`](#cat-curves), [`Surfaces(R)`](#cat-surfaces)
- **refines**, transitively, in Sage's linearization order: [`IntegralSchemes(R)`](#cat-integralschemes) · [`FiniteTypeSchemes(R)`](#cat-finitetypeschemes) · [`SeparatedSchemes(R)`](#cat-separatedschemes) · [`Schemes(R)`](#cat-schemes) · [`LocallyRingedSpaces`](#cat-locallyringedspaces) · [`RingedSpaces`](#cat-ringedspaces) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `Varieties(R)(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Integral separated schemes of finite type over the stated base.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Schemes(R)`](#cat-schemes) | 13 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`FiniteTypeSchemes(R)`](#cat-finitetypeschemes) | 2 |  |  |
| [`IntegralSchemes(R)`](#cat-integralschemes) | 2 |  |  |
| [`RingedSpaces`](#cat-ringedspaces) | 2 |  |  |
| [`SeparatedSchemes(R)`](#cat-separatedschemes) | 2 |  |  |
| [`LocallyRingedSpaces`](#cat-locallyringedspaces) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `Curves(R)` {#cat-curves}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/schemes/varieties.py:33`
- **probed as** `Category of curves over Integer Ring`
- **above** [`Varieties(R)`](#cat-varieties)
- **refines**, transitively, in Sage's linearization order: [`Varieties(R)`](#cat-varieties) · [`IntegralSchemes(R)`](#cat-integralschemes) · [`FiniteTypeSchemes(R)`](#cat-finitetypeschemes) · [`SeparatedSchemes(R)`](#cat-separatedschemes) · [`Schemes(R)`](#cat-schemes) · [`LocallyRingedSpaces`](#cat-locallyringedspaces) · [`RingedSpaces`](#cat-ringedspaces) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `Curves(R)(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - Integral separated schemes of finite type over the stated base.
- `dimension()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Schemes(R)`](#cat-schemes) | 13 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`FiniteTypeSchemes(R)`](#cat-finitetypeschemes) | 2 |  |  |
| [`IntegralSchemes(R)`](#cat-integralschemes) | 2 |  |  |
| [`RingedSpaces`](#cat-ringedspaces) | 2 |  |  |
| [`SeparatedSchemes(R)`](#cat-separatedschemes) | 2 |  |  |
| [`LocallyRingedSpaces`](#cat-locallyringedspaces) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`Varieties(R)`](#cat-varieties) | 1 |  |  |

#### `Surfaces(R)` {#cat-surfaces}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/schemes/varieties.py:51`
- **probed as** `Category of surfaces over Integer Ring`
- **above** [`Varieties(R)`](#cat-varieties)
- **refines**, transitively, in Sage's linearization order: [`Varieties(R)`](#cat-varieties) · [`IntegralSchemes(R)`](#cat-integralschemes) · [`FiniteTypeSchemes(R)`](#cat-finitetypeschemes) · [`SeparatedSchemes(R)`](#cat-separatedschemes) · [`Schemes(R)`](#cat-schemes) · [`LocallyRingedSpaces`](#cat-locallyringedspaces) · [`RingedSpaces`](#cat-ringedspaces) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `Surfaces(R)(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - Integral separated schemes of finite type over the stated base.
- `dimension()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Schemes(R)`](#cat-schemes) | 13 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`FiniteTypeSchemes(R)`](#cat-finitetypeschemes) | 2 |  |  |
| [`IntegralSchemes(R)`](#cat-integralschemes) | 2 |  |  |
| [`RingedSpaces`](#cat-ringedspaces) | 2 |  |  |
| [`SeparatedSchemes(R)`](#cat-separatedschemes) | 2 |  |  |
| [`LocallyRingedSpaces`](#cat-locallyringedspaces) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`Varieties(R)`](#cat-varieties) | 1 |  |  |

#### `AffineSpaces(R)` {#cat-affinespaces}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/schemes/schemes.py:1434`
- **probed as** `Category of affine spaces over Integer Ring`
- **above** [`AffineSchemes(R)`](#cat-affineschemes), [`FiniteTypeSchemes(R)`](#cat-finitetypeschemes), [`SmoothSchemes(R)`](#cat-smoothschemes)
- **refines**, transitively, in Sage's linearization order: [`SmoothSchemes(R)`](#cat-smoothschemes) · [`FiniteTypeSchemes(R)`](#cat-finitetypeschemes) · [`AffineSchemes(R)`](#cat-affineschemes) · [`QuasiAffineSchemes(R)`](#cat-quasiaffineschemes) · [`SeparatedSchemes(R)`](#cat-separatedschemes) · [`Schemes(R)`](#cat-schemes) · [`LocallyRingedSpaces`](#cat-locallyringedspaces) · [`RingedSpaces`](#cat-ringedspaces) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `AffineSpaces(R)(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - Schemes over ``Spec(R)`` for the represented base ring ``R``.
- `zeta_function()`
  - Return ``Z(A^d/F_q,T)=1/(1-q^d T)``.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`AffineSchemes(R)`](#cat-affineschemes) | 13 |  |  |
| [`Schemes(R)`](#cat-schemes) | 13 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`FiniteTypeSchemes(R)`](#cat-finitetypeschemes) | 2 |  |  |
| [`QuasiAffineSchemes(R)`](#cat-quasiaffineschemes) | 2 |  |  |
| [`RingedSpaces`](#cat-ringedspaces) | 2 |  |  |
| [`SeparatedSchemes(R)`](#cat-separatedschemes) | 2 |  |  |
| [`SmoothSchemes(R)`](#cat-smoothschemes) | 2 |  |  |
| [`LocallyRingedSpaces`](#cat-locallyringedspaces) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `ProjectiveSpaces(R)` {#cat-projectivespaces}

A category over a ring, normalized to the session's owned ring.

- **defined at** `src/dzack_research/preamble/categories/schemes/schemes.py:1476`
- **probed as** `Category of projective spaces over Integer Ring`
- **above** [`ProjectiveSchemes(R)`](#cat-projectiveschemes), [`SmoothSchemes(R)`](#cat-smoothschemes)
- **refines**, transitively, in Sage's linearization order: [`ProjectiveSchemes(R)`](#cat-projectiveschemes) · [`QuasiProjectiveSchemes(R)`](#cat-quasiprojectiveschemes) · [`SmoothSchemes(R)`](#cat-smoothschemes) · [`FiniteTypeSchemes(R)`](#cat-finitetypeschemes) · [`SeparatedSchemes(R)`](#cat-separatedschemes) · [`Schemes(R)`](#cat-schemes) · [`LocallyRingedSpaces`](#cat-locallyringedspaces) · [`RingedSpaces`](#cat-ringedspaces) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `ProjectiveSpaces(R)(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `ElementType()`
  - Schemes over ``Spec(R)`` for the represented base ring ``R``.
- `zeta_function()`
  - Return ``Z(P^d/F_q,T)=prod_{i=0}^d(1-q^i T)^(-1)``.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Schemes(R)`](#cat-schemes) | 13 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`ProjectiveSchemes(R)`](#cat-projectiveschemes) | 3 |  |  |
| [`FiniteTypeSchemes(R)`](#cat-finitetypeschemes) | 2 |  |  |
| [`QuasiProjectiveSchemes(R)`](#cat-quasiprojectiveschemes) | 2 |  |  |
| [`RingedSpaces`](#cat-ringedspaces) | 2 |  |  |
| [`SeparatedSchemes(R)`](#cat-separatedschemes) | 2 |  |  |
| [`SmoothSchemes(R)`](#cat-smoothschemes) | 2 |  |  |
| [`LocallyRingedSpaces`](#cat-locallyringedspaces) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `ProductProjectiveSpaces(R)` {#cat-productprojectivespaces}

Finite products of projective spaces over one base ring.

- **defined at** `src/dzack_research/preamble/categories/schemes/schemes.py:1558`
- **probed as** `Category of products of projective spaces over Integer Ring`
- **above** [`ProductSchemes(R)`](#cat-productschemes), [`ProjectiveSchemes(R)`](#cat-projectiveschemes), [`SmoothSchemes(R)`](#cat-smoothschemes)
- **refines**, transitively, in Sage's linearization order: [`ProjectiveSchemes(R)`](#cat-projectiveschemes) · [`ProductSchemes(R)`](#cat-productschemes) · [`QuasiProjectiveSchemes(R)`](#cat-quasiprojectiveschemes) · [`SmoothSchemes(R)`](#cat-smoothschemes) · [`FiniteTypeSchemes(R)`](#cat-finitetypeschemes) · [`SeparatedSchemes(R)`](#cat-separatedschemes) · [`Schemes(R)`](#cat-schemes) · [`LocallyRingedSpaces`](#cat-locallyringedspaces) · [`RingedSpaces`](#cat-ringedspaces) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `ProductProjectiveSpaces(R)(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Finite products of projective spaces over one base ring.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`Schemes(R)`](#cat-schemes) | 13 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`ProductSchemes(R)`](#cat-productschemes) | 5 |  |  |
| [`ProjectiveSchemes(R)`](#cat-projectiveschemes) | 3 |  |  |
| [`FiniteTypeSchemes(R)`](#cat-finitetypeschemes) | 2 |  |  |
| [`QuasiProjectiveSchemes(R)`](#cat-quasiprojectiveschemes) | 2 |  |  |
| [`RingedSpaces`](#cat-ringedspaces) | 2 |  |  |
| [`SeparatedSchemes(R)`](#cat-separatedschemes) | 2 |  |  |
| [`SmoothSchemes(R)`](#cat-smoothschemes) | 2 |  |  |
| [`LocallyRingedSpaces`](#cat-locallyringedspaces) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `ClosedEmbeddings` {#cat-closedembeddings}

Subobjects of `X` whose inclusion is a closed immersion.

```text
For affine \(X=\operatorname{Spec}A\) this is
\(\operatorname{Spec}(A/I)\hookrightarrow X\), induced by the quotient
\(A\twoheadrightarrow A/I\).  Every closed subscheme of \(X\) arises this
way from a unique ideal \(I\), so no further subclass exists to name; a
chosen finite generating set of \(I\) presents the coordinate algebra and
is stated on that algebra.
```

- **defined at** `src/dzack_research/preamble/categories/schemes/schemes.py:2515`
- **not placed**: `ClosedEmbeddings(parameter)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

**Operations introduced here** (3 on objects)

*on objects*

- `codimension()`
- `defining_equations()`
  - Return the family of equations that cut this subscheme out.
- `defining_ideal_owned()`

#### `OpenImmersions` {#cat-openimmersions}

Subobjects of `X` whose inclusion is an open immersion.

```text
The standard affine specimen is the distinguished open
\(D(f)=\operatorname{Spec}A[1/f]\subseteq\operatorname{Spec}A\), whose
inclusion is induced by the localization map \(A\to A[1/f]\).
```

- **defined at** `src/dzack_research/preamble/categories/schemes/schemes.py:2568`
- **not placed**: `OpenImmersions(parameter)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

**Operations introduced here** (2 on objects)

*on objects*

- `distinguished_open_element()`
- `is_distinguished_open()`

#### `SchemeMonomorphisms` {#cat-schememonomorphisms}

Monomorphisms of schemes.

```text
A closed immersion and an open immersion are monomorphisms.  Which of the
two an inclusion is, is declared where it is constructed, and this reads
that declaration.  Injectivity on points is neither necessary nor
sufficient for a scheme monomorphism, so the inherited test does not apply.
```

- **defined at** `src/dzack_research/preamble/categories/schemes/schemes.py:2594`
- **not placed**: `SchemeMonomorphisms(base_category)` annotates no parameter, so the survey has nothing to construct it from (`LEX-12`)

### Functors and adjunctions

#### `AffineSpecFunctor` {#fun-affinespecfunctor}

The contravariant functor `Spec_R: CAlg_R -> AffSch_R`.

- **defined at** `src/dzack_research/preamble/categories/schemes/affine_spec.py:15`
- **built by** `AffineSpecFunctor(base_ring)`
- **not resolved here**: parameterized by data the survey does not choose for you

**Operations**

- `base_ring()`

### Morphisms and homsets

#### `SchemeMorphism` <sub>MORPHISM</sub>

Categorical wrapper around one native Sage scheme morphism.

- **defined at** `src/dzack_research/preamble/categories/schemes/schemes.py:80`
- **built by** `SchemeMorphism(native_morphism, *, domain=None, codomain=None, homset=None, pullback=None)`

**Operations**

- `codomain()`
  - codomain: object
- `compose(before)`
- `coordinate_algebra_morphism()`
- `domain()`
  - domain: object
- `evaluate_at(point)`
- `native_morphism()`
- `pullback_on_coordinate_algebras()`
- `then(after)`

### Supporting classes

#### `SchemeUnderlyingSpace` <sub>CLASS</sub>

The underlying topological space of a represented ringed space.

```text
Sage's scheme parents do not expose a separate topological-space parent.
The owned API nevertheless keeps the mathematical structure explicit: this
object remembers the represented scheme and is the space on which open
and closed-subspace structure can later be attached.
```

- **defined at** `src/dzack_research/preamble/categories/schemes/ringed_spaces.py:13`
- **built by** `SchemeUnderlyingSpace(ringed_space)`

**Operations**

- `ringed_space()`
- `scheme()`

#### `StructureSheaf` <sub>CLASS</sub>

The represented structure sheaf `O_X` of a ringed space `X`.

- **defined at** `src/dzack_research/preamble/categories/schemes/ringed_spaces.py:34`
- **built by** `StructureSheaf(ringed_space)`

**Operations**

- `associated_module_sheaf(module)`
  - Return the represented affine sheaf ``M~`` on the distinguished-open basis.
- `global_sections()`
  - Return ``Gamma(X,O_X)`` in the exact cases represented live.
- `restriction_map(source_open, target_open)`
  - Return the represented restriction ``O(source_open) -> O(target_open)``.
- `ringed_space()`
- `scheme()`
- `sections()`
  - Return ``Gamma(X,O_X)`` in the exact cases represented live.
- `sections_on_distinguished_open(distinguished_open)`
  - Return ``O_X(D(f)) = Gamma(X,O_X)_f`` for an affine scheme.
- `stalk(point)`
  - Return ``O_{X,p}`` for a represented affine prime point.

### Functions

#### `AffineSpace` <sub>FUNCTION</sub>

Return the owned affine space `A^n_R`.

- **defined at** `src/dzack_research/preamble/categories/schemes/schemes.py:2107`
- **built by** `AffineSpace(dimension, base_ring, names=None)`

#### `ConvexPolygon` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/schemes/polytopes.py:450`
- **built by** `ConvexPolygon(vertices, lattice=None)`

#### `ConvexPolytope` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/schemes/polytopes.py:446`
- **built by** `ConvexPolytope(vertices, lattice=None)`

#### `LatticePolygon` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/schemes/polytopes.py:461`
- **built by** `LatticePolygon(vertices, lattice=None)`

#### `LatticePolytope` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/schemes/polytopes.py:457`
- **built by** `LatticePolytope(vertices, lattice=None)`

#### `ProjectiveSpace` <sub>FUNCTION</sub>

Return the owned projective space `P^n_R`.

- **defined at** `src/dzack_research/preamble/categories/schemes/schemes.py:2165`
- **built by** `ProjectiveSpace(dimension, base_ring, names=None)`

#### `Spec` <sub>FUNCTION</sub>

Return the affine scheme `Spec(A)` over the represented scalar base.

```text
If ``A`` is an owned commutative ``R``-algebra, the returned object lies in
``Schemes(R)`` and its structure morphism is induced contravariantly by
``R -> A``.  A bare commutative ring ``R`` is read as an ``R``-algebra over
itself when it is supplied as the explicit ``base_ring``, so
``Spec(R, base_ring=R)`` is the terminal affine ``R``-scheme.  Omitting the
base retains the coordinate algebra's represented scalar base.
```

- **defined at** `src/dzack_research/preamble/categories/schemes/schemes.py:1673`
- **built by** `Spec(ring_or_algebra, base_ring=None)`

#### `SpecFunctor` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/schemes/affine_spec.py:40`
- **built by** `SpecFunctor(base_ring)`

#### `affine_spec_functor` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/schemes/affine_spec.py:40`
- **built by** `affine_spec_functor(base_ring)`

#### `scheme_fiber_product` <sub>FUNCTION</sub>

Return `X x_S Y` for two represented affine scheme maps to `S`.

- **defined at** `src/dzack_research/preamble/categories/schemes/schemes.py:2438`
- **built by** `scheme_fiber_product(left_map, right_map)`

#### `scheme_product` <sub>FUNCTION</sub>

Return the categorical product in the currently supported scheme regimes.

```text
Affine spaces use ``A^m x A^n = A^{m+n}``; products of projective spaces
use Sage's genuine multiprojective scheme backend.  In both cases the
returned scheme retains the stated factors and actual projection
morphisms.  General affine schemes and mixed products belong to the same
surface but require the coordinate-algebra tensor-product/fiber-product
layer and are not silently represented as products of underlying sets.
```

- **defined at** `src/dzack_research/preamble/categories/schemes/schemes.py:2210`
- **built by** `scheme_product(*schemes)`

## Divisors & Picard Theory

> Divisor groups, Cartier divisors, Weil divisors, Picard groups, Class groups, and Formal divisors.

```mermaid
graph RL
  CartierDivisorGroups["CartierDivisorGroups"]
  ClassGroups["ClassGroups"]
  DivisorGroups["DivisorGroups"]
  FormalDivisorGroups["FormalDivisorGroups(R)"]
  PicardGroups["PicardGroups"]
  WeilDivisorGroups["WeilDivisorGroups"]
  FramedFreeModules("FramedFreeModules(R)")
  FramedModules("FramedModules(R)")
  CartierDivisorGroups --> FramedModules
  ClassGroups --> FramedModules
  DivisorGroups --> FramedFreeModules
  FormalDivisorGroups --> FramedFreeModules
  PicardGroups --> FramedModules
  WeilDivisorGroups --> DivisorGroups
  classDef outside stroke-dasharray:6 4,fill:#f8fafc;
  class FramedFreeModules,FramedModules outside;
```

### Categories

Ordered by depth: the least structured first.

#### `CartierDivisorGroups` {#cat-cartierdivisorgroups}

The base class for modeling mathematical categories, like for example:

```text
- ``Groups()`` -- the category of groups
- ``EuclideanDomains()`` -- the category of euclidean rings
- ``VectorSpaces(QQ)`` -- the category of vector spaces over the field of
  rationals

See :mod:`sage.categories.primer` for an introduction to
categories in Sage, their relevance, purpose, and usage. The
documentation below will focus on their implementation.

Technically, a category is an instance of the class
:class:`Category` or some of its subclasses. Some categories, like
:class:`VectorSpaces`, are parametrized: ``VectorSpaces(QQ)`` is one of
many instances of the class :class:`VectorSpaces`. On the other
hand, ``EuclideanDomains()`` is the single instance of the class
:class:`EuclideanDomains`.

Recall that an algebraic structure (say, the ring `\QQ[x]`) is
modelled in Sage by an object which is called a parent. This
object belongs to certain categories (here ``EuclideanDomains()`` and
``Algebras()``). The elements of the ring are themselves objects.

The class of a category (say :class:`EuclideanDomains`) can define simultaneously:

- Operations on the category itself (what is its super categories?
  its category of morphisms? its dual category?).
- Generic operations on parents in this category, like the ring `\QQ[x]`.
- Generic operations on elements of such parents (e. g., the
  Euclidean algorithm for computing gcds).
- Generic operations on morphisms of this category.

This is achieved as follows::

    sage: from sage.categories.category import Category
    sage: class EuclideanDomains(Category):
    ....:     # operations on the category itself
    ....:     def super_categories(self):
    ....:         [Rings()]
    ....:
    ....:     def dummy(self): # TODO: find some good examples
    ....:          pass
    ....:
    ....:     class ParentMethods: # holds the generic operations on parents
    ....:          # TODO: find a good example of an operation
    ....:          pass
    ....:
    ....:     class ElementMethods:# holds the generic operations on elements
    ....:          def gcd(x, y):
    ....:              # Euclid algorithms
    ....:              pass
    ....:
    ....:     class MorphismMethods: # holds the generic operations on morphisms
    ....:          # TODO: find a good example of an operation
    ....:          pass
    ....:

Note that the nested class ``ParentMethods`` is merely a container
of operations, and does not inherit from anything. Instead, the
hierarchy relation is defined once at the level of the categories,
and the actual hierarchy of classes is built in parallel from all
the ``ParentMethods`` nested classes, and stored in the attributes
``parent_class``. Then, a parent in a category ``C`` receives the
appropriate operations from all the super categories by usual
class inheritance from ``C.parent_class``.

Similarly, two other hierarchies of classes, for elements and
morphisms respectively, are built from all the ``ElementMethods``
and ``MorphismMethods`` nested classes.

EXAMPLES:

We define a hierarchy of four categories ``As()``, ``Bs()``,
``Cs()``, ``Ds()`` with a diamond inheritance. Think for example:

- ``As()`` -- the category of sets
- ``Bs()`` -- the category of additive groups
- ``Cs()`` -- the category of multiplicative monoids
- ``Ds()`` -- the category of rings

::

    sage: from sage.categories.category import Category
    sage: from sage.misc.lazy_attribute import lazy_attribute
    sage: class As (Category):
    ....:     def super_categories(self):
    ....:         return []
    ....:
    ....:     class ParentMethods:
    ....:         def fA(self):
    ....:             return "A"
    ....:         f = fA

    sage: class Bs (Category):
    ....:     def super_categories(self):
    ....:         return [As()]
    ....:
    ....:     class ParentMethods:
    ....:         def fB(self):
    ....:             return "B"

    sage: class Cs (Category):
    ....:     def super_categories(self):
    ....:         return [As()]
    ....:
    ....:     class ParentMethods:
    ....:         def fC(self):
    ....:             return "C"
    ....:         f = fC

    sage: class Ds (Category):
    ....:     def super_categories(self):
    ....:         return [Bs(),Cs()]
    ....:
    ....:     class ParentMethods:
    ....:         def fD(self):
    ....:             return "D"

Categories should always have unique representation; by :issue:`12215`,
this means that it will be kept in cache, but only
if there is still some strong reference to it.

We check this before proceeding::

    sage: import gc
    sage: idAs = id(As())
    sage: _ = gc.collect()
    sage: n == id(As())
    False
    sage: a = As()
    sage: id(As()) == id(As())
    True
    sage: As().parent_class == As().parent_class
    True

We construct a parent in the category ``Ds()`` (that, is an instance
of ``Ds().parent_class``), and check that it has access to all the
methods provided by all the categories, with the appropriate
inheritance order::

    sage: D = Ds().parent_class()
    sage: [ D.fA(), D.fB(), D.fC(), D.fD() ]
    ['A', 'B', 'C', 'D']
    sage: D.f()
    'C'

::

    sage: C = Cs().parent_class()
    sage: [ C.fA(), C.fC() ]
    ['A', 'C']
    sage: C.f()
    'C'

Here is the parallel hierarchy of classes which has been built
automatically, together with the method resolution order (``.mro()``)::

    sage: As().parent_class
    <class '__main__.As.parent_class'>
    sage: As().parent_class.__bases__
    (<... 'object'>,)
    sage: As().parent_class.mro()
    [<class '__main__.As.parent_class'>, <... 'object'>]

::

    sage: Bs().parent_class
    <class '__main__.Bs.parent_class'>
    sage: Bs().parent_class.__bases__
    (<class '__main__.As.parent_class'>,)
    sage: Bs().parent_class.mro()
    [<class '__main__.Bs.parent_class'>, <class '__main__.As.parent_class'>, <... 'object'>]

::

    sage: Cs().parent_class
    <class '__main__.Cs.parent_class'>
    sage: Cs().parent_class.__bases__
    (<class '__main__.As.parent_class'>,)
    sage: Cs().parent_class.__mro__
    (<class '__main__.Cs.parent_class'>, <class '__main__.As.parent_class'>, <... 'object'>)

::

    sage: Ds().parent_class
    <class '__main__.Ds.parent_class'>
    sage: Ds().parent_class.__bases__
    (<class '__main__.Cs.parent_class'>, <class '__main__.Bs.parent_class'>)
    sage: Ds().parent_class.mro()
    [<class '__main__.Ds.parent_class'>, <class '__main__.Cs.parent_class'>,
     <class '__main__.Bs.parent_class'>, <class '__main__.As.parent_class'>, <... 'object'>]

Note that two categories in the same class need not have the
same ``super_categories``. For example, ``Algebras(QQ)`` has
``VectorSpaces(QQ)`` as super category, whereas ``Algebras(ZZ)``
only has ``Modules(ZZ)`` as super category. In particular, the
constructed parent class and element class will differ (inheriting,
or not, methods specific for vector spaces)::

    sage: Algebras(QQ).parent_class is Algebras(ZZ).parent_class
    False
    sage: issubclass(Algebras(QQ).parent_class, VectorSpaces(QQ).parent_class)
    True

On the other hand, identical hierarchies of classes are,
preferably, built only once (e.g. for categories over a base ring)::

    sage: Algebras(GF(5)).parent_class is Algebras(GF(7)).parent_class
    True
    sage: F = FractionField(ZZ['t'])
    sage: Coalgebras(F).parent_class is Coalgebras(FractionField(F['x'])).parent_class
    True

We now construct a parent in the usual way::

    sage: class myparent(Parent):
    ....:     def __init__(self):
    ....:         Parent.__init__(self, category=Ds())
    ....:     def g(self):
    ....:         return "myparent"
    ....:     class Element():
    ....:         pass
    sage: D = myparent()
    sage: D.__class__
    <class '__main__.myparent_with_category'>
    sage: D.__class__.__bases__
    (<class '__main__.myparent'>, <class '__main__.Ds.parent_class'>)
    sage: D.__class__.mro()
    [<class '__main__.myparent_with_category'>,
    <class '__main__.myparent'>,
    <class 'sage.structure.parent.Parent'>,
    <class 'sage.structure.category_object.CategoryObject'>,
    <class 'sage.structure.sage_object.SageObject'>,
    <class '__main__.Ds.parent_class'>,
    <class '__main__.Cs.parent_class'>,
    <class '__main__.Bs.parent_class'>,
    <class '__main__.As.parent_class'>,
    <... 'object'>]
    sage: D.fA()
    'A'
    sage: D.fB()
    'B'
    sage: D.fC()
    'C'
    sage: D.fD()
    'D'
    sage: D.f()
    'C'
    sage: D.g()
    'myparent'

::

    sage: D.element_class
    <class '__main__.myparent_with_category.element_class'>
    sage: D.element_class.mro()
    [<class '__main__.myparent_with_category.element_class'>,
    <class ...__main__....Element...>,
    <class '__main__.Ds.element_class'>,
    <class '__main__.Cs.element_class'>,
    <class '__main__.Bs.element_class'>,
    <class '__main__.As.element_class'>,
    <... 'object'>]


TESTS::

    sage: import __main__
    sage: __main__.myparent = myparent
    sage: __main__.As = As
    sage: __main__.Bs = Bs
    sage: __main__.Cs = Cs
    sage: __main__.Ds = Ds
    sage: loads(dumps(Ds)) is Ds
    True
    sage: loads(dumps(Ds())) is Ds()
    True
    sage: loads(dumps(Ds().element_class)) is Ds().element_class
    True

.. automethod:: Category._super_categories
.. automethod:: Category._super_categories_for_classes
.. automethod:: Category._all_super_categories
.. automethod:: Category._all_super_categories_proper
.. automethod:: Category._set_of_super_categories
.. automethod:: Category._make_named_class
.. automethod:: Category._repr_
.. automethod:: Category._repr_object_names
.. automethod:: Category._test_category
.. automethod:: Category._with_axiom
.. automethod:: Category._with_axiom_as_tuple
.. automethod:: Category._without_axioms
.. automethod:: Category._sort
.. automethod:: Category._sort_uniq
.. automethod:: Category.__classcall__
.. automethod:: Category.__init__
```

- **defined at** `src/dzack_research/preamble/categories/divisors/cartier_divisor_groups.py:10`
- **probed as** `Category of Cartier divisor groups`
- **above** [`FramedModules(R)`](#cat-framedmodules)
- **refines**, transitively, in Sage's linearization order: [`FramedModules(R)`](#cat-framedmodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `CartierDivisorGroups(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FramedModules(R)`](#cat-framedmodules) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `ClassGroups` {#cat-classgroups}

The base class for modeling mathematical categories, like for example:

```text
- ``Groups()`` -- the category of groups
- ``EuclideanDomains()`` -- the category of euclidean rings
- ``VectorSpaces(QQ)`` -- the category of vector spaces over the field of
  rationals

See :mod:`sage.categories.primer` for an introduction to
categories in Sage, their relevance, purpose, and usage. The
documentation below will focus on their implementation.

Technically, a category is an instance of the class
:class:`Category` or some of its subclasses. Some categories, like
:class:`VectorSpaces`, are parametrized: ``VectorSpaces(QQ)`` is one of
many instances of the class :class:`VectorSpaces`. On the other
hand, ``EuclideanDomains()`` is the single instance of the class
:class:`EuclideanDomains`.

Recall that an algebraic structure (say, the ring `\QQ[x]`) is
modelled in Sage by an object which is called a parent. This
object belongs to certain categories (here ``EuclideanDomains()`` and
``Algebras()``). The elements of the ring are themselves objects.

The class of a category (say :class:`EuclideanDomains`) can define simultaneously:

- Operations on the category itself (what is its super categories?
  its category of morphisms? its dual category?).
- Generic operations on parents in this category, like the ring `\QQ[x]`.
- Generic operations on elements of such parents (e. g., the
  Euclidean algorithm for computing gcds).
- Generic operations on morphisms of this category.

This is achieved as follows::

    sage: from sage.categories.category import Category
    sage: class EuclideanDomains(Category):
    ....:     # operations on the category itself
    ....:     def super_categories(self):
    ....:         [Rings()]
    ....:
    ....:     def dummy(self): # TODO: find some good examples
    ....:          pass
    ....:
    ....:     class ParentMethods: # holds the generic operations on parents
    ....:          # TODO: find a good example of an operation
    ....:          pass
    ....:
    ....:     class ElementMethods:# holds the generic operations on elements
    ....:          def gcd(x, y):
    ....:              # Euclid algorithms
    ....:              pass
    ....:
    ....:     class MorphismMethods: # holds the generic operations on morphisms
    ....:          # TODO: find a good example of an operation
    ....:          pass
    ....:

Note that the nested class ``ParentMethods`` is merely a container
of operations, and does not inherit from anything. Instead, the
hierarchy relation is defined once at the level of the categories,
and the actual hierarchy of classes is built in parallel from all
the ``ParentMethods`` nested classes, and stored in the attributes
``parent_class``. Then, a parent in a category ``C`` receives the
appropriate operations from all the super categories by usual
class inheritance from ``C.parent_class``.

Similarly, two other hierarchies of classes, for elements and
morphisms respectively, are built from all the ``ElementMethods``
and ``MorphismMethods`` nested classes.

EXAMPLES:

We define a hierarchy of four categories ``As()``, ``Bs()``,
``Cs()``, ``Ds()`` with a diamond inheritance. Think for example:

- ``As()`` -- the category of sets
- ``Bs()`` -- the category of additive groups
- ``Cs()`` -- the category of multiplicative monoids
- ``Ds()`` -- the category of rings

::

    sage: from sage.categories.category import Category
    sage: from sage.misc.lazy_attribute import lazy_attribute
    sage: class As (Category):
    ....:     def super_categories(self):
    ....:         return []
    ....:
    ....:     class ParentMethods:
    ....:         def fA(self):
    ....:             return "A"
    ....:         f = fA

    sage: class Bs (Category):
    ....:     def super_categories(self):
    ....:         return [As()]
    ....:
    ....:     class ParentMethods:
    ....:         def fB(self):
    ....:             return "B"

    sage: class Cs (Category):
    ....:     def super_categories(self):
    ....:         return [As()]
    ....:
    ....:     class ParentMethods:
    ....:         def fC(self):
    ....:             return "C"
    ....:         f = fC

    sage: class Ds (Category):
    ....:     def super_categories(self):
    ....:         return [Bs(),Cs()]
    ....:
    ....:     class ParentMethods:
    ....:         def fD(self):
    ....:             return "D"

Categories should always have unique representation; by :issue:`12215`,
this means that it will be kept in cache, but only
if there is still some strong reference to it.

We check this before proceeding::

    sage: import gc
    sage: idAs = id(As())
    sage: _ = gc.collect()
    sage: n == id(As())
    False
    sage: a = As()
    sage: id(As()) == id(As())
    True
    sage: As().parent_class == As().parent_class
    True

We construct a parent in the category ``Ds()`` (that, is an instance
of ``Ds().parent_class``), and check that it has access to all the
methods provided by all the categories, with the appropriate
inheritance order::

    sage: D = Ds().parent_class()
    sage: [ D.fA(), D.fB(), D.fC(), D.fD() ]
    ['A', 'B', 'C', 'D']
    sage: D.f()
    'C'

::

    sage: C = Cs().parent_class()
    sage: [ C.fA(), C.fC() ]
    ['A', 'C']
    sage: C.f()
    'C'

Here is the parallel hierarchy of classes which has been built
automatically, together with the method resolution order (``.mro()``)::

    sage: As().parent_class
    <class '__main__.As.parent_class'>
    sage: As().parent_class.__bases__
    (<... 'object'>,)
    sage: As().parent_class.mro()
    [<class '__main__.As.parent_class'>, <... 'object'>]

::

    sage: Bs().parent_class
    <class '__main__.Bs.parent_class'>
    sage: Bs().parent_class.__bases__
    (<class '__main__.As.parent_class'>,)
    sage: Bs().parent_class.mro()
    [<class '__main__.Bs.parent_class'>, <class '__main__.As.parent_class'>, <... 'object'>]

::

    sage: Cs().parent_class
    <class '__main__.Cs.parent_class'>
    sage: Cs().parent_class.__bases__
    (<class '__main__.As.parent_class'>,)
    sage: Cs().parent_class.__mro__
    (<class '__main__.Cs.parent_class'>, <class '__main__.As.parent_class'>, <... 'object'>)

::

    sage: Ds().parent_class
    <class '__main__.Ds.parent_class'>
    sage: Ds().parent_class.__bases__
    (<class '__main__.Cs.parent_class'>, <class '__main__.Bs.parent_class'>)
    sage: Ds().parent_class.mro()
    [<class '__main__.Ds.parent_class'>, <class '__main__.Cs.parent_class'>,
     <class '__main__.Bs.parent_class'>, <class '__main__.As.parent_class'>, <... 'object'>]

Note that two categories in the same class need not have the
same ``super_categories``. For example, ``Algebras(QQ)`` has
``VectorSpaces(QQ)`` as super category, whereas ``Algebras(ZZ)``
only has ``Modules(ZZ)`` as super category. In particular, the
constructed parent class and element class will differ (inheriting,
or not, methods specific for vector spaces)::

    sage: Algebras(QQ).parent_class is Algebras(ZZ).parent_class
    False
    sage: issubclass(Algebras(QQ).parent_class, VectorSpaces(QQ).parent_class)
    True

On the other hand, identical hierarchies of classes are,
preferably, built only once (e.g. for categories over a base ring)::

    sage: Algebras(GF(5)).parent_class is Algebras(GF(7)).parent_class
    True
    sage: F = FractionField(ZZ['t'])
    sage: Coalgebras(F).parent_class is Coalgebras(FractionField(F['x'])).parent_class
    True

We now construct a parent in the usual way::

    sage: class myparent(Parent):
    ....:     def __init__(self):
    ....:         Parent.__init__(self, category=Ds())
    ....:     def g(self):
    ....:         return "myparent"
    ....:     class Element():
    ....:         pass
    sage: D = myparent()
    sage: D.__class__
    <class '__main__.myparent_with_category'>
    sage: D.__class__.__bases__
    (<class '__main__.myparent'>, <class '__main__.Ds.parent_class'>)
    sage: D.__class__.mro()
    [<class '__main__.myparent_with_category'>,
    <class '__main__.myparent'>,
    <class 'sage.structure.parent.Parent'>,
    <class 'sage.structure.category_object.CategoryObject'>,
    <class 'sage.structure.sage_object.SageObject'>,
    <class '__main__.Ds.parent_class'>,
    <class '__main__.Cs.parent_class'>,
    <class '__main__.Bs.parent_class'>,
    <class '__main__.As.parent_class'>,
    <... 'object'>]
    sage: D.fA()
    'A'
    sage: D.fB()
    'B'
    sage: D.fC()
    'C'
    sage: D.fD()
    'D'
    sage: D.f()
    'C'
    sage: D.g()
    'myparent'

::

    sage: D.element_class
    <class '__main__.myparent_with_category.element_class'>
    sage: D.element_class.mro()
    [<class '__main__.myparent_with_category.element_class'>,
    <class ...__main__....Element...>,
    <class '__main__.Ds.element_class'>,
    <class '__main__.Cs.element_class'>,
    <class '__main__.Bs.element_class'>,
    <class '__main__.As.element_class'>,
    <... 'object'>]


TESTS::

    sage: import __main__
    sage: __main__.myparent = myparent
    sage: __main__.As = As
    sage: __main__.Bs = Bs
    sage: __main__.Cs = Cs
    sage: __main__.Ds = Ds
    sage: loads(dumps(Ds)) is Ds
    True
    sage: loads(dumps(Ds())) is Ds()
    True
    sage: loads(dumps(Ds().element_class)) is Ds().element_class
    True

.. automethod:: Category._super_categories
.. automethod:: Category._super_categories_for_classes
.. automethod:: Category._all_super_categories
.. automethod:: Category._all_super_categories_proper
.. automethod:: Category._set_of_super_categories
.. automethod:: Category._make_named_class
.. automethod:: Category._repr_
.. automethod:: Category._repr_object_names
.. automethod:: Category._test_category
.. automethod:: Category._with_axiom
.. automethod:: Category._with_axiom_as_tuple
.. automethod:: Category._without_axioms
.. automethod:: Category._sort
.. automethod:: Category._sort_uniq
.. automethod:: Category.__classcall__
.. automethod:: Category.__init__
```

- **defined at** `src/dzack_research/preamble/categories/divisors/class_groups.py:10`
- **probed as** `Category of class groups`
- **above** [`FramedModules(R)`](#cat-framedmodules)
- **refines**, transitively, in Sage's linearization order: [`FramedModules(R)`](#cat-framedmodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `ClassGroups(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FramedModules(R)`](#cat-framedmodules) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `PicardGroups` {#cat-picardgroups}

The base class for modeling mathematical categories, like for example:

```text
- ``Groups()`` -- the category of groups
- ``EuclideanDomains()`` -- the category of euclidean rings
- ``VectorSpaces(QQ)`` -- the category of vector spaces over the field of
  rationals

See :mod:`sage.categories.primer` for an introduction to
categories in Sage, their relevance, purpose, and usage. The
documentation below will focus on their implementation.

Technically, a category is an instance of the class
:class:`Category` or some of its subclasses. Some categories, like
:class:`VectorSpaces`, are parametrized: ``VectorSpaces(QQ)`` is one of
many instances of the class :class:`VectorSpaces`. On the other
hand, ``EuclideanDomains()`` is the single instance of the class
:class:`EuclideanDomains`.

Recall that an algebraic structure (say, the ring `\QQ[x]`) is
modelled in Sage by an object which is called a parent. This
object belongs to certain categories (here ``EuclideanDomains()`` and
``Algebras()``). The elements of the ring are themselves objects.

The class of a category (say :class:`EuclideanDomains`) can define simultaneously:

- Operations on the category itself (what is its super categories?
  its category of morphisms? its dual category?).
- Generic operations on parents in this category, like the ring `\QQ[x]`.
- Generic operations on elements of such parents (e. g., the
  Euclidean algorithm for computing gcds).
- Generic operations on morphisms of this category.

This is achieved as follows::

    sage: from sage.categories.category import Category
    sage: class EuclideanDomains(Category):
    ....:     # operations on the category itself
    ....:     def super_categories(self):
    ....:         [Rings()]
    ....:
    ....:     def dummy(self): # TODO: find some good examples
    ....:          pass
    ....:
    ....:     class ParentMethods: # holds the generic operations on parents
    ....:          # TODO: find a good example of an operation
    ....:          pass
    ....:
    ....:     class ElementMethods:# holds the generic operations on elements
    ....:          def gcd(x, y):
    ....:              # Euclid algorithms
    ....:              pass
    ....:
    ....:     class MorphismMethods: # holds the generic operations on morphisms
    ....:          # TODO: find a good example of an operation
    ....:          pass
    ....:

Note that the nested class ``ParentMethods`` is merely a container
of operations, and does not inherit from anything. Instead, the
hierarchy relation is defined once at the level of the categories,
and the actual hierarchy of classes is built in parallel from all
the ``ParentMethods`` nested classes, and stored in the attributes
``parent_class``. Then, a parent in a category ``C`` receives the
appropriate operations from all the super categories by usual
class inheritance from ``C.parent_class``.

Similarly, two other hierarchies of classes, for elements and
morphisms respectively, are built from all the ``ElementMethods``
and ``MorphismMethods`` nested classes.

EXAMPLES:

We define a hierarchy of four categories ``As()``, ``Bs()``,
``Cs()``, ``Ds()`` with a diamond inheritance. Think for example:

- ``As()`` -- the category of sets
- ``Bs()`` -- the category of additive groups
- ``Cs()`` -- the category of multiplicative monoids
- ``Ds()`` -- the category of rings

::

    sage: from sage.categories.category import Category
    sage: from sage.misc.lazy_attribute import lazy_attribute
    sage: class As (Category):
    ....:     def super_categories(self):
    ....:         return []
    ....:
    ....:     class ParentMethods:
    ....:         def fA(self):
    ....:             return "A"
    ....:         f = fA

    sage: class Bs (Category):
    ....:     def super_categories(self):
    ....:         return [As()]
    ....:
    ....:     class ParentMethods:
    ....:         def fB(self):
    ....:             return "B"

    sage: class Cs (Category):
    ....:     def super_categories(self):
    ....:         return [As()]
    ....:
    ....:     class ParentMethods:
    ....:         def fC(self):
    ....:             return "C"
    ....:         f = fC

    sage: class Ds (Category):
    ....:     def super_categories(self):
    ....:         return [Bs(),Cs()]
    ....:
    ....:     class ParentMethods:
    ....:         def fD(self):
    ....:             return "D"

Categories should always have unique representation; by :issue:`12215`,
this means that it will be kept in cache, but only
if there is still some strong reference to it.

We check this before proceeding::

    sage: import gc
    sage: idAs = id(As())
    sage: _ = gc.collect()
    sage: n == id(As())
    False
    sage: a = As()
    sage: id(As()) == id(As())
    True
    sage: As().parent_class == As().parent_class
    True

We construct a parent in the category ``Ds()`` (that, is an instance
of ``Ds().parent_class``), and check that it has access to all the
methods provided by all the categories, with the appropriate
inheritance order::

    sage: D = Ds().parent_class()
    sage: [ D.fA(), D.fB(), D.fC(), D.fD() ]
    ['A', 'B', 'C', 'D']
    sage: D.f()
    'C'

::

    sage: C = Cs().parent_class()
    sage: [ C.fA(), C.fC() ]
    ['A', 'C']
    sage: C.f()
    'C'

Here is the parallel hierarchy of classes which has been built
automatically, together with the method resolution order (``.mro()``)::

    sage: As().parent_class
    <class '__main__.As.parent_class'>
    sage: As().parent_class.__bases__
    (<... 'object'>,)
    sage: As().parent_class.mro()
    [<class '__main__.As.parent_class'>, <... 'object'>]

::

    sage: Bs().parent_class
    <class '__main__.Bs.parent_class'>
    sage: Bs().parent_class.__bases__
    (<class '__main__.As.parent_class'>,)
    sage: Bs().parent_class.mro()
    [<class '__main__.Bs.parent_class'>, <class '__main__.As.parent_class'>, <... 'object'>]

::

    sage: Cs().parent_class
    <class '__main__.Cs.parent_class'>
    sage: Cs().parent_class.__bases__
    (<class '__main__.As.parent_class'>,)
    sage: Cs().parent_class.__mro__
    (<class '__main__.Cs.parent_class'>, <class '__main__.As.parent_class'>, <... 'object'>)

::

    sage: Ds().parent_class
    <class '__main__.Ds.parent_class'>
    sage: Ds().parent_class.__bases__
    (<class '__main__.Cs.parent_class'>, <class '__main__.Bs.parent_class'>)
    sage: Ds().parent_class.mro()
    [<class '__main__.Ds.parent_class'>, <class '__main__.Cs.parent_class'>,
     <class '__main__.Bs.parent_class'>, <class '__main__.As.parent_class'>, <... 'object'>]

Note that two categories in the same class need not have the
same ``super_categories``. For example, ``Algebras(QQ)`` has
``VectorSpaces(QQ)`` as super category, whereas ``Algebras(ZZ)``
only has ``Modules(ZZ)`` as super category. In particular, the
constructed parent class and element class will differ (inheriting,
or not, methods specific for vector spaces)::

    sage: Algebras(QQ).parent_class is Algebras(ZZ).parent_class
    False
    sage: issubclass(Algebras(QQ).parent_class, VectorSpaces(QQ).parent_class)
    True

On the other hand, identical hierarchies of classes are,
preferably, built only once (e.g. for categories over a base ring)::

    sage: Algebras(GF(5)).parent_class is Algebras(GF(7)).parent_class
    True
    sage: F = FractionField(ZZ['t'])
    sage: Coalgebras(F).parent_class is Coalgebras(FractionField(F['x'])).parent_class
    True

We now construct a parent in the usual way::

    sage: class myparent(Parent):
    ....:     def __init__(self):
    ....:         Parent.__init__(self, category=Ds())
    ....:     def g(self):
    ....:         return "myparent"
    ....:     class Element():
    ....:         pass
    sage: D = myparent()
    sage: D.__class__
    <class '__main__.myparent_with_category'>
    sage: D.__class__.__bases__
    (<class '__main__.myparent'>, <class '__main__.Ds.parent_class'>)
    sage: D.__class__.mro()
    [<class '__main__.myparent_with_category'>,
    <class '__main__.myparent'>,
    <class 'sage.structure.parent.Parent'>,
    <class 'sage.structure.category_object.CategoryObject'>,
    <class 'sage.structure.sage_object.SageObject'>,
    <class '__main__.Ds.parent_class'>,
    <class '__main__.Cs.parent_class'>,
    <class '__main__.Bs.parent_class'>,
    <class '__main__.As.parent_class'>,
    <... 'object'>]
    sage: D.fA()
    'A'
    sage: D.fB()
    'B'
    sage: D.fC()
    'C'
    sage: D.fD()
    'D'
    sage: D.f()
    'C'
    sage: D.g()
    'myparent'

::

    sage: D.element_class
    <class '__main__.myparent_with_category.element_class'>
    sage: D.element_class.mro()
    [<class '__main__.myparent_with_category.element_class'>,
    <class ...__main__....Element...>,
    <class '__main__.Ds.element_class'>,
    <class '__main__.Cs.element_class'>,
    <class '__main__.Bs.element_class'>,
    <class '__main__.As.element_class'>,
    <... 'object'>]


TESTS::

    sage: import __main__
    sage: __main__.myparent = myparent
    sage: __main__.As = As
    sage: __main__.Bs = Bs
    sage: __main__.Cs = Cs
    sage: __main__.Ds = Ds
    sage: loads(dumps(Ds)) is Ds
    True
    sage: loads(dumps(Ds())) is Ds()
    True
    sage: loads(dumps(Ds().element_class)) is Ds().element_class
    True

.. automethod:: Category._super_categories
.. automethod:: Category._super_categories_for_classes
.. automethod:: Category._all_super_categories
.. automethod:: Category._all_super_categories_proper
.. automethod:: Category._set_of_super_categories
.. automethod:: Category._make_named_class
.. automethod:: Category._repr_
.. automethod:: Category._repr_object_names
.. automethod:: Category._test_category
.. automethod:: Category._with_axiom
.. automethod:: Category._with_axiom_as_tuple
.. automethod:: Category._without_axioms
.. automethod:: Category._sort
.. automethod:: Category._sort_uniq
.. automethod:: Category.__classcall__
.. automethod:: Category.__init__
```

- **defined at** `src/dzack_research/preamble/categories/divisors/picard_groups.py:10`
- **probed as** `Category of Picard groups`
- **above** [`FramedModules(R)`](#cat-framedmodules)
- **refines**, transitively, in Sage's linearization order: [`FramedModules(R)`](#cat-framedmodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `PicardGroups(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FramedModules(R)`](#cat-framedmodules) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `DivisorGroups` {#cat-divisorgroups}

Free abelian groups on specified prime divisors.

- **defined at** `src/dzack_research/preamble/categories/divisors/divisor_groups.py:33`
- **probed as** `Category of divisor groups`
- **above** [`FramedFreeModules(R)`](#cat-framedfreemodules)
- **below** [`WeilDivisorGroups`](#cat-weildivisorgroups)
- **refines**, transitively, in Sage's linearization order: [`FramedFreeModules(R)`](#cat-framedfreemodules) · [`FramedModules(R)`](#cat-framedmodules) · [`FreeModules(R)`](#cat-freemodules) · [`ProjectiveModules(R)`](#cat-projectivemodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `DivisorGroups(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FramedFreeModules(R)`](#cat-framedfreemodules) | 13 |  |  |
| [`FramedModules(R)`](#cat-framedmodules) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`ProjectiveModules(R)`](#cat-projectivemodules) | 3 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`FreeModules(R)`](#cat-freemodules) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `FormalDivisorGroups(R)` {#cat-formaldivisorgroups}

Formal divisors with coefficients in a specified ring.

- **defined at** `src/dzack_research/preamble/categories/divisors/divisor_groups.py:58`
- **probed as** `Category of formal divisor groups`
- **above** [`FramedFreeModules(R)`](#cat-framedfreemodules)
- **refines**, transitively, in Sage's linearization order: [`FramedFreeModules(R)`](#cat-framedfreemodules) · [`FramedModules(R)`](#cat-framedmodules) · [`FreeModules(R)`](#cat-freemodules) · [`ProjectiveModules(R)`](#cat-projectivemodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `FormalDivisorGroups(R)(x, *args, **opts)`

**Operations introduced here** (5 on objects)

*on objects*

- `ElementType()`
  - Formal divisors with coefficients in a specified ring.
- `components(divisor)`
- `divisor_latex(divisor) -> str`
- `divisor_repr(divisor) -> str`
- `terms(divisor)`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FramedFreeModules(R)`](#cat-framedfreemodules) | 13 |  |  |
| [`FramedModules(R)`](#cat-framedmodules) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`ProjectiveModules(R)`](#cat-projectivemodules) | 3 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`FreeModules(R)`](#cat-freemodules) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `WeilDivisorGroups` {#cat-weildivisorgroups}

The base class for modeling mathematical categories, like for example:

```text
- ``Groups()`` -- the category of groups
- ``EuclideanDomains()`` -- the category of euclidean rings
- ``VectorSpaces(QQ)`` -- the category of vector spaces over the field of
  rationals

See :mod:`sage.categories.primer` for an introduction to
categories in Sage, their relevance, purpose, and usage. The
documentation below will focus on their implementation.

Technically, a category is an instance of the class
:class:`Category` or some of its subclasses. Some categories, like
:class:`VectorSpaces`, are parametrized: ``VectorSpaces(QQ)`` is one of
many instances of the class :class:`VectorSpaces`. On the other
hand, ``EuclideanDomains()`` is the single instance of the class
:class:`EuclideanDomains`.

Recall that an algebraic structure (say, the ring `\QQ[x]`) is
modelled in Sage by an object which is called a parent. This
object belongs to certain categories (here ``EuclideanDomains()`` and
``Algebras()``). The elements of the ring are themselves objects.

The class of a category (say :class:`EuclideanDomains`) can define simultaneously:

- Operations on the category itself (what is its super categories?
  its category of morphisms? its dual category?).
- Generic operations on parents in this category, like the ring `\QQ[x]`.
- Generic operations on elements of such parents (e. g., the
  Euclidean algorithm for computing gcds).
- Generic operations on morphisms of this category.

This is achieved as follows::

    sage: from sage.categories.category import Category
    sage: class EuclideanDomains(Category):
    ....:     # operations on the category itself
    ....:     def super_categories(self):
    ....:         [Rings()]
    ....:
    ....:     def dummy(self): # TODO: find some good examples
    ....:          pass
    ....:
    ....:     class ParentMethods: # holds the generic operations on parents
    ....:          # TODO: find a good example of an operation
    ....:          pass
    ....:
    ....:     class ElementMethods:# holds the generic operations on elements
    ....:          def gcd(x, y):
    ....:              # Euclid algorithms
    ....:              pass
    ....:
    ....:     class MorphismMethods: # holds the generic operations on morphisms
    ....:          # TODO: find a good example of an operation
    ....:          pass
    ....:

Note that the nested class ``ParentMethods`` is merely a container
of operations, and does not inherit from anything. Instead, the
hierarchy relation is defined once at the level of the categories,
and the actual hierarchy of classes is built in parallel from all
the ``ParentMethods`` nested classes, and stored in the attributes
``parent_class``. Then, a parent in a category ``C`` receives the
appropriate operations from all the super categories by usual
class inheritance from ``C.parent_class``.

Similarly, two other hierarchies of classes, for elements and
morphisms respectively, are built from all the ``ElementMethods``
and ``MorphismMethods`` nested classes.

EXAMPLES:

We define a hierarchy of four categories ``As()``, ``Bs()``,
``Cs()``, ``Ds()`` with a diamond inheritance. Think for example:

- ``As()`` -- the category of sets
- ``Bs()`` -- the category of additive groups
- ``Cs()`` -- the category of multiplicative monoids
- ``Ds()`` -- the category of rings

::

    sage: from sage.categories.category import Category
    sage: from sage.misc.lazy_attribute import lazy_attribute
    sage: class As (Category):
    ....:     def super_categories(self):
    ....:         return []
    ....:
    ....:     class ParentMethods:
    ....:         def fA(self):
    ....:             return "A"
    ....:         f = fA

    sage: class Bs (Category):
    ....:     def super_categories(self):
    ....:         return [As()]
    ....:
    ....:     class ParentMethods:
    ....:         def fB(self):
    ....:             return "B"

    sage: class Cs (Category):
    ....:     def super_categories(self):
    ....:         return [As()]
    ....:
    ....:     class ParentMethods:
    ....:         def fC(self):
    ....:             return "C"
    ....:         f = fC

    sage: class Ds (Category):
    ....:     def super_categories(self):
    ....:         return [Bs(),Cs()]
    ....:
    ....:     class ParentMethods:
    ....:         def fD(self):
    ....:             return "D"

Categories should always have unique representation; by :issue:`12215`,
this means that it will be kept in cache, but only
if there is still some strong reference to it.

We check this before proceeding::

    sage: import gc
    sage: idAs = id(As())
    sage: _ = gc.collect()
    sage: n == id(As())
    False
    sage: a = As()
    sage: id(As()) == id(As())
    True
    sage: As().parent_class == As().parent_class
    True

We construct a parent in the category ``Ds()`` (that, is an instance
of ``Ds().parent_class``), and check that it has access to all the
methods provided by all the categories, with the appropriate
inheritance order::

    sage: D = Ds().parent_class()
    sage: [ D.fA(), D.fB(), D.fC(), D.fD() ]
    ['A', 'B', 'C', 'D']
    sage: D.f()
    'C'

::

    sage: C = Cs().parent_class()
    sage: [ C.fA(), C.fC() ]
    ['A', 'C']
    sage: C.f()
    'C'

Here is the parallel hierarchy of classes which has been built
automatically, together with the method resolution order (``.mro()``)::

    sage: As().parent_class
    <class '__main__.As.parent_class'>
    sage: As().parent_class.__bases__
    (<... 'object'>,)
    sage: As().parent_class.mro()
    [<class '__main__.As.parent_class'>, <... 'object'>]

::

    sage: Bs().parent_class
    <class '__main__.Bs.parent_class'>
    sage: Bs().parent_class.__bases__
    (<class '__main__.As.parent_class'>,)
    sage: Bs().parent_class.mro()
    [<class '__main__.Bs.parent_class'>, <class '__main__.As.parent_class'>, <... 'object'>]

::

    sage: Cs().parent_class
    <class '__main__.Cs.parent_class'>
    sage: Cs().parent_class.__bases__
    (<class '__main__.As.parent_class'>,)
    sage: Cs().parent_class.__mro__
    (<class '__main__.Cs.parent_class'>, <class '__main__.As.parent_class'>, <... 'object'>)

::

    sage: Ds().parent_class
    <class '__main__.Ds.parent_class'>
    sage: Ds().parent_class.__bases__
    (<class '__main__.Cs.parent_class'>, <class '__main__.Bs.parent_class'>)
    sage: Ds().parent_class.mro()
    [<class '__main__.Ds.parent_class'>, <class '__main__.Cs.parent_class'>,
     <class '__main__.Bs.parent_class'>, <class '__main__.As.parent_class'>, <... 'object'>]

Note that two categories in the same class need not have the
same ``super_categories``. For example, ``Algebras(QQ)`` has
``VectorSpaces(QQ)`` as super category, whereas ``Algebras(ZZ)``
only has ``Modules(ZZ)`` as super category. In particular, the
constructed parent class and element class will differ (inheriting,
or not, methods specific for vector spaces)::

    sage: Algebras(QQ).parent_class is Algebras(ZZ).parent_class
    False
    sage: issubclass(Algebras(QQ).parent_class, VectorSpaces(QQ).parent_class)
    True

On the other hand, identical hierarchies of classes are,
preferably, built only once (e.g. for categories over a base ring)::

    sage: Algebras(GF(5)).parent_class is Algebras(GF(7)).parent_class
    True
    sage: F = FractionField(ZZ['t'])
    sage: Coalgebras(F).parent_class is Coalgebras(FractionField(F['x'])).parent_class
    True

We now construct a parent in the usual way::

    sage: class myparent(Parent):
    ....:     def __init__(self):
    ....:         Parent.__init__(self, category=Ds())
    ....:     def g(self):
    ....:         return "myparent"
    ....:     class Element():
    ....:         pass
    sage: D = myparent()
    sage: D.__class__
    <class '__main__.myparent_with_category'>
    sage: D.__class__.__bases__
    (<class '__main__.myparent'>, <class '__main__.Ds.parent_class'>)
    sage: D.__class__.mro()
    [<class '__main__.myparent_with_category'>,
    <class '__main__.myparent'>,
    <class 'sage.structure.parent.Parent'>,
    <class 'sage.structure.category_object.CategoryObject'>,
    <class 'sage.structure.sage_object.SageObject'>,
    <class '__main__.Ds.parent_class'>,
    <class '__main__.Cs.parent_class'>,
    <class '__main__.Bs.parent_class'>,
    <class '__main__.As.parent_class'>,
    <... 'object'>]
    sage: D.fA()
    'A'
    sage: D.fB()
    'B'
    sage: D.fC()
    'C'
    sage: D.fD()
    'D'
    sage: D.f()
    'C'
    sage: D.g()
    'myparent'

::

    sage: D.element_class
    <class '__main__.myparent_with_category.element_class'>
    sage: D.element_class.mro()
    [<class '__main__.myparent_with_category.element_class'>,
    <class ...__main__....Element...>,
    <class '__main__.Ds.element_class'>,
    <class '__main__.Cs.element_class'>,
    <class '__main__.Bs.element_class'>,
    <class '__main__.As.element_class'>,
    <... 'object'>]


TESTS::

    sage: import __main__
    sage: __main__.myparent = myparent
    sage: __main__.As = As
    sage: __main__.Bs = Bs
    sage: __main__.Cs = Cs
    sage: __main__.Ds = Ds
    sage: loads(dumps(Ds)) is Ds
    True
    sage: loads(dumps(Ds())) is Ds()
    True
    sage: loads(dumps(Ds().element_class)) is Ds().element_class
    True

.. automethod:: Category._super_categories
.. automethod:: Category._super_categories_for_classes
.. automethod:: Category._all_super_categories
.. automethod:: Category._all_super_categories_proper
.. automethod:: Category._set_of_super_categories
.. automethod:: Category._make_named_class
.. automethod:: Category._repr_
.. automethod:: Category._repr_object_names
.. automethod:: Category._test_category
.. automethod:: Category._with_axiom
.. automethod:: Category._with_axiom_as_tuple
.. automethod:: Category._without_axioms
.. automethod:: Category._sort
.. automethod:: Category._sort_uniq
.. automethod:: Category.__classcall__
.. automethod:: Category.__init__
```

- **defined at** `src/dzack_research/preamble/categories/divisors/weil_divisor_groups.py:13`
- **probed as** `Category of Weil divisor groups`
- **above** [`DivisorGroups`](#cat-divisorgroups)
- **refines**, transitively, in Sage's linearization order: [`DivisorGroups`](#cat-divisorgroups) · [`FramedFreeModules(R)`](#cat-framedfreemodules) · [`FramedModules(R)`](#cat-framedmodules) · [`FreeModules(R)`](#cat-freemodules) · [`ProjectiveModules(R)`](#cat-projectivemodules) · [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `WeilDivisorGroups(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`FramedFreeModules(R)`](#cat-framedfreemodules) | 13 |  |  |
| [`FramedModules(R)`](#cat-framedmodules) | 10 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`ProjectiveModules(R)`](#cat-projectivemodules) | 3 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`FreeModules(R)`](#cat-freemodules) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

### Supporting classes

#### `InvertibleSheaf` <sub>CLASS</sub>

A line bundle represented by rank-one free descent on one affine cover.

- **defined at** `src/dzack_research/preamble/categories/divisors/invertible_sheaves.py:44`
- **built by** `InvertibleSheaf(gluing_datum)`

**Operations**

- `cover()`
- `dual()`
  - Return the dual line bundle, with transition units ``u_ij^{-1}``.
- `global_sections()`
- `gluing_datum()`
- `local_module(index)`
- `local_trivialization(index)`
  - Return the literal rank-one free chart module trivializing this sheaf.
- `morphism_to(target, local_maps)`
  - Return the descent morphism represented by the supplied chart maps.
- `ringed_space()`
- `scheme()`
- `sections()`
- `sheaf()`
- `tensor_power(exponent)`
  - Return ``self^tensor exponent`` using powers of the transition units.
- `tensor_product(other)`
  - Tensor two line bundles by multiplying their transition units.
- `transition_unit(source_index, target_index)`
  - Return the unit ``u_ij`` with ``e_i |-> u_ij e_j`` on the overlap.

### Functions

#### `CartierDivisorGroup` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/divisors/cartier_divisor_groups.py:21`
- **built by** `CartierDivisorGroup(module)`

#### `ClassGroup` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/divisors/class_groups.py:21`
- **built by** `ClassGroup(module)`

#### `DivisorGroup` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/divisors/divisor_groups.py:46`
- **built by** `DivisorGroup(module)`

#### `FormalDivisor` <sub>FUNCTION</sub>

Return the formal linear combination of the stated prime divisors.

```text
The divisor is an element of ``FormalDivisorGroup(R, S)`` for ``S`` the
prime divisors in ``terms``, in order of first appearance; that group
answers ``terms``, ``components`` and printing for it.
```

- **defined at** `src/dzack_research/preamble/categories/divisors/divisor_groups.py:116`
- **built by** `FormalDivisor(coefficient_ring, terms)`

#### `PicardGroup` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/divisors/picard_groups.py:21`
- **built by** `PicardGroup(module)`

#### `TrivialInvertibleSheaf` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/divisors/invertible_sheaves.py:201`
- **built by** `TrivialInvertibleSheaf(cover)`

#### `WeilDivisorGroup` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/divisors/weil_divisor_groups.py:22`
- **built by** `WeilDivisorGroup(module)`

## Bilinear Forms, Quadratic Forms & Pairings

> Bilinear/Quadratic forms, Pairings, Gram matrices, and Form spaces.

### Functions

#### `BilinearForms` <sub>FUNCTION</sub>

Return `Hom_R(M tensor_R M,W)` whenever that universal object exists.

- **defined at** `src/dzack_research/preamble/categories/forms/forms.py:387`
- **built by** `BilinearForms(module, value_module)`

#### `Pairings` <sub>FUNCTION</sub>

Return `Hom_R(X tensor_R Y,W)` whenever that universal object exists.

- **defined at** `src/dzack_research/preamble/categories/forms/forms.py:372`
- **built by** `Pairings(left_module, right_module, value_module)`

#### `QuadraticForms` <sub>FUNCTION</sub>

Return `Hom_R(Gamma^2(M),W)` whenever the divided square is represented.

- **defined at** `src/dzack_research/preamble/categories/forms/forms.py:400`
- **built by** `QuadraticForms(module, value_module)`

#### `gram_tensor_from_graph` <sub>FUNCTION</sub>

Recover the type-`(0,2)` Gram tensor presented by a weighted graph.

- **defined at** `src/dzack_research/preamble/categories/forms/gram_matrices.py:29`
- **built by** `gram_tensor_from_graph(graph, base_ring)`

#### `gram_tensor_graph` <sub>FUNCTION</sub>

Return the weighted undirected graph presented by a symmetric Gram tensor.

- **defined at** `src/dzack_research/preamble/categories/forms/gram_matrices.py:11`
- **built by** `gram_tensor_graph(gram)`

#### `tensor_connected_component_cuts` <sub>FUNCTION</sub>

Return cuts between consecutive connected diagonal blocks.

- **defined at** `src/dzack_research/preamble/categories/forms/gram_matrices.py:45`
- **built by** `tensor_connected_component_cuts(gram) -> list[int]`

## Function Spaces & Analysis

> Lebesgue modules, Lp, ell, C(X), Graded Lebesgue algebras, and Convolution algebras.

```mermaid
graph RL
  GradedTensorProductModules["GradedTensorProductModules(R)"]
  LebesgueGradedModules["LebesgueGradedModules(R)"]
  Modules("Modules(R)")
  GradedTensorProductModules --> Modules
  LebesgueGradedModules --> Modules
  classDef outside stroke-dasharray:6 4,fill:#f8fafc;
  class Modules outside;
```

### Categories

Ordered by depth: the least structured first.

#### `GradedTensorProductModules(R)` {#cat-gradedtensorproductmodules}

Tensor squares of Lebesgue graded modules.

```text
Elements are finite sums of homogeneous pure tensors. This is not the
finitely presented tensor product: the summands \(L^{1/s}\) are not
finitely presented \(\mathbb R\)-modules.
```

- **defined at** `src/dzack_research/preamble/categories/functions/lebesgue_graded.py:204`
- **probed as** `Category of graded tensor products of Lebesgue modules`
- **above** [`Modules(R)`](#cat-modules)
- **refines**, transitively, in Sage's linearization order: [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `GradedTensorProductModules(R)(x, *args, **opts)`

**Operations introduced here** (4 on objects)

*on objects*

- `ElementType()`
  - Tensor squares of Lebesgue graded modules.
- `pure_tensor(left_element, right_element)`
  - Return the image of \((left, right)\) under \(\otimes\).
- `tensor_factor(index)`
- `tensor_factors()`
  - Return the family of factors, indexed by the product's own index set.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `LebesgueGradedModules(R)` {#cat-lebesguegradedmodules}

Graded modules whose homogeneous pieces are Lebesgue spaces \(L^{1/s}\).

- **defined at** `src/dzack_research/preamble/categories/functions/lebesgue_graded.py:111`
- **probed as** `Category of Lebesgue graded modules`
- **above** [`Modules(R)`](#cat-modules)
- **refines**, transitively, in Sage's linearization order: [`Modules(R)`](#cat-modules) · [`AdditiveGroups.AdditiveCommutative`](#cat-additivegroups-additivecommutative) · [`AdditiveGroups`](#cat-additivegroups) · [`AdditiveMonoids`](#cat-additivemonoids) · [`AdditiveSemigroups`](#cat-additivesemigroups) · [`AdditiveMagmas`](#cat-additivemagmas) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `LebesgueGradedModules(R)(x, *args, **opts)`
- **specimens** `GradedLebesgueAlgebra`, `LebesgueConvolutionAlgebra`

**Operations introduced here** (8 on objects)

*on objects*

- `ElementType()`
  - Graded modules whose homogeneous pieces are Lebesgue spaces \(L^{1/s}\).
- `algebra_from_multiplication(multiplication, *, unital=True)`
  - Equip this graded Lebesgue module with its represented product.
- `degree_projection(degree)`
  - The projection \(\pi_s\colon N\to L^{1/s}\) onto a homogeneous piece.
- `integral_form()`
  - The linear form \(\varepsilon=\iota\circ\pi_1\colon N\to\mathbb R\).
- `integral_pairing()`
  - The pairing \(B\) as an element of \(\operatorname{Hom}(A\otimes A,\mathbb R)\).
- `integral_pairing_morphism()`
  - The pairing \(B=\varepsilon\circ m\colon A\otimes_{\mathbb R}A\to\mathbb R\).
- `integration_of_degree_one()`
  - Integration \(\iota\colon L^1\to\mathbb R\) of the degree-\(1\) piece.
- `unit_piece_projection()`
  - The graded augmentation \(A\to A_u\), for a unital graded algebra.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Modules(R)`](#cat-modules) | 20 |  |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`AdditiveGroups`](#cat-additivegroups) | 2 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 2 |  |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 1 |  |  |
| [`AdditiveSemigroups`](#cat-additivesemigroups) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

### Objects

#### `GradedLebesgueModule` <sub>OBJECT</sub>

The \(M\)-graded module \(\bigoplus_{s\in M} L^{1/s}\).

```text
The monoid \(M\) supplies the index of Hölder degrees. The full
family uses \(([0,\infty],+)\); convolution uses \(([0,1],\oplus)\).
```

- **defined at** `src/dzack_research/preamble/categories/functions/lebesgue_graded.py:565`
- **built by** `GradedLebesgueModule(grading_monoid)`

**Operations**

- `Element(parent, components) -> None`
  - A finitely supported family of homogeneous Lebesgue classes.
- `graded_piece(degree)`
  - The homogeneous summand \(L^{1/s}\) in Hölder degree \(s\).
- `zero()`

#### `GradedTensorSquare` <sub>OBJECT</sub>

The tensor square \(N\otimes_{\mathbb R} N\) of a Lebesgue graded module.

- **defined at** `src/dzack_research/preamble/categories/functions/lebesgue_graded.py:410`
- **built by** `GradedTensorSquare(module)`

**Operations**

- `Element(parent, summands) -> None`
  - A finite sum of homogeneous pure tensors.
- `zero()`

#### `Lp` <sub>OBJECT</sub>

The \(\mathbb R\)-module \(L^p(\mathbb R)\), represented by functions.

```text
\(L^2(\mathbb R)\) is a module with the symmetric bilinear form
\(b(f,g)=\int_{\mathbb R}fg\).  A general \(L^p\) is not: Hölder pairs it
with \(L^{p'}\) as \(L^p * L^{p'}\).

EXAMPLES::

    sage: from dzack_research.preamble.all import (
    ....:     C, FormModules, FormedModules, Lp, PairedModules, RR,
    ....:     SymmetricBilinearFormModules, VectorSpaces, exp,
    ....: )
    sage: L = Lp(2)
    sage: L
    L^2(RR)
    sage: L in VectorSpaces(RR)
    True
    sage: L in SymmetricBilinearFormModules(RR)
    True
    sage: L in FormedModules(RR)
    True
    sage: L in PairedModules(RR)
    True
    sage: Lp(1) in FormModules(RR)
    False
    sage: Maps = C(Infinity, RR)
    sage: gaussian = Maps(exp(-Maps.indeterminate() ** 2))
    sage: L(gaussian)(0)
    1
    sage: L.b(L(gaussian), L(gaussian))
    1/2*sqrt(2)*sqrt(pi)
    sage: L.q(L(gaussian))
    1/2*sqrt(2)*sqrt(pi)
    sage: L.pairing_module() is L
    True
    sage: Lp(1) * Lp(Infinity) in PairedModules(RR)
    True
    sage: Lp(1) * Lp(Infinity) in FormedModules(RR)
    False
```

- **defined at** `src/dzack_research/preamble/categories/functions/real_functions.py:775`
- **built by** `Lp(p)`

**Operations**

- `conjugate_lebesgue_space()`
  - The space \(L^{p'}\) with \(1/p+1/p'=1\).
- `differentiability()`
  - Lebesgue classes are not a \(C^k\) mapping space.
- `integrability_exponent()`
- `pairing_module()` <sub>cached</sub>
  - The Hölder pairing module \(L^p\otimes L^{p'}\to\mathbb R\).

### Objects the session already holds

#### `GradedLebesgueAlgebra` <sub>LIVE OBJECT</sub>

A Lebesgue graded module interned on a chosen multiplication morphism.

- **is** graded Lebesgue algebra
- **in** Join of Category of algebras graded by Nonnegative extended real numbers over Real Field and Category of commutative algebras and Category of algebras with chosen multiplication and Category of Lebesgue graded modules

#### `LebesgueConvolutionAlgebra` <sub>LIVE OBJECT</sub>

A Lebesgue graded module interned on a chosen multiplication morphism.

- **is** Lebesgue convolution algebra
- **in** Join of Category of modules graded by unit interval under s⊕t = s+t-1 over Real Field and Category of associative algebras with chosen multiplication and Category of Lebesgue graded modules

### Functions

#### `C` <sub>FUNCTION</sub>

The constructor \(C\).  \(C^k(X,Y)\) is the mapping space of class \(k\).

```text
``C(k, X, Y)`` and ``C^k(X, Y)`` are the same space.  ``C(k, X)`` and
``C^k(X)`` are \(C^k(X,X)\).

EXAMPLES::

    sage: from dzack_research.preamble.all import Algebras, C, RR, VectorSpaces, exp
    sage: (C^Infinity)(RR) is C(Infinity, RR, RR)
    True
    sage: (C^2)(RR, RR) is C(2, RR)
    True
    sage: (C^Infinity)(RR)
    C(Infinity, RR)
    sage: (C^Infinity)(RR) in VectorSpaces(RR)
    True
    sage: (C^Infinity)(RR) in Algebras(RR)
    True
    sage: x = (C^Infinity)(RR).coordinate()
    sage: x(3)
    3
    sage: f = (C^Infinity)(RR)(exp)
    sage: f(0)
    1
    sage: (f * x)(0)
    0
    sage: f(x * x)(0)
    1
    sage: (C^Infinity)(RR).integral(x, 0)(2)
    2
```

- **defined at** `src/dzack_research/preamble/categories/functions/real_functions.py:724`
- **built by** `C(k, domain, codomain=None)`

#### `ell` <sub>FUNCTION</sub>

The constructor \(\ell\).  \(\ell^p(\mathbb R)\) is \(p\)-summable real sequences.

```text
``ell(p)``, ``ell(p, RR)``, and ``ell^p(RR)`` are the same space.

EXAMPLES::

    sage: from dzack_research.preamble.all import (
    ....:     FormedModules, PairedModules, QQ, RR, VectorSpaces, ell,
    ....: )
    sage: from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing
    sage: ell(2) is ell(2, RR)
    True
    sage: ell(2) in VectorSpaces(RR)
    True
    sage: ell(2) in FormedModules(RR)
    True
    sage: ell(1) in FormedModules(RR)
    False
    sage: n = ell(2).indeterminate()
    sage: geometric = ell(2)(2 ** (-n))
    sage: geometric(3)
    1/8
    sage: ell(2).b(geometric, geometric)
    4/3
    sage: t = PolynomialRing(QQ, "t").gen()
    sage: truncated = ell(2)(1 + t + t**2)
    sage: truncated(3)
    0
    sage: ell(2).b(truncated, truncated)
    3
    sage: ell(2) * ell(2) is ell(2)
    True
    sage: ell(1) * ell(Infinity) in PairedModules(RR)
    True
    sage: ell(1) * ell(Infinity) in FormedModules(RR)
    False
```

- **defined at** `src/dzack_research/preamble/categories/functions/real_functions.py:954`
- **built by** `ell(p, values=None)`

#### `graded_lebesgue_algebra` <sub>FUNCTION</sub>

The pointwise algebra \(\bigoplus_s L^{1/s}\), interned from its product.

- **defined at** `src/dzack_research/preamble/categories/functions/lebesgue_graded.py:628`
- **built by** `graded_lebesgue_algebra()`

#### `lebesgue_convolution_algebra` <sub>FUNCTION</sub>

The convolution algebra \(\bigoplus_{s\in[0,1]} L^{1/s}\), interned from its product.

- **defined at** `src/dzack_research/preamble/categories/functions/lebesgue_graded.py:638`
- **built by** `lebesgue_convolution_algebra()`

## Sets, Cardinals & Ordinals

> Sets, Cardinalities, Ordinals, Enumerated sets, Fourier characters, Hermite polynomials, and Power sets.

```mermaid
graph RL
  Cardinalities["Cardinalities"]
  CartesianProductsOfSets["CartesianProductsOfSets"]
  CoproductsOfSets["CoproductsOfSets"]
  CountableSets["CountableSets"]
  CountablyInfiniteSets["CountablyInfiniteSets"]
  DisjointUnionsOfSets["DisjointUnionsOfSets"]
  EnumeratedByIntegers["EnumeratedByIntegers"]
  EnumeratedByNaturals["EnumeratedByNaturals"]
  EnumeratedSets["EnumeratedSets"]
  FinitePowerSets["FinitePowerSets"]
  FinitelySupportedFunctionSets["FinitelySupportedFunctionSets"]
  FunctionEnumeratedSets["FunctionEnumeratedSets"]
  InfiniteEnumeratedSets["InfiniteEnumeratedSets"]
  OrdinalSemirings["OrdinalSemirings"]
  PartiallyOrderedSets["PartiallyOrderedSets"]
  PowerSets["PowerSets"]
  Sets["Sets"]
  Sets.Finite["Sets.Finite"]
  Sets.Infinite["Sets.Infinite"]
  TotallyOrderedSets["TotallyOrderedSets"]
  UncountableSets["UncountableSets"]
  Objects("Objects")
  Cardinalities --> Objects
  CartesianProductsOfSets --> Sets
  CoproductsOfSets --> Sets
  CountableSets --> Sets
  CountablyInfiniteSets --> CountableSets
  CountablyInfiniteSets --> Sets.Infinite
  DisjointUnionsOfSets --> Sets
  EnumeratedByIntegers --> InfiniteEnumeratedSets
  EnumeratedByNaturals --> InfiniteEnumeratedSets
  EnumeratedSets --> Sets
  FinitePowerSets --> Sets
  FinitelySupportedFunctionSets --> Sets
  FunctionEnumeratedSets --> EnumeratedSets
  InfiniteEnumeratedSets --> EnumeratedSets
  OrdinalSemirings --> Objects
  PartiallyOrderedSets --> Sets
  PowerSets --> Sets
  Sets --> Objects
  Sets.Finite --> Sets
  Sets.Infinite --> Sets
  TotallyOrderedSets --> PartiallyOrderedSets
  UncountableSets --> Sets.Infinite
  classDef outside stroke-dasharray:6 4,fill:#f8fafc;
  class Objects outside;
```

### Categories

Ordered by depth: the least structured first.

#### `Cardinalities` {#cat-cardinalities}

The thin category associated to the represented cardinal order.

- **defined at** `src/dzack_research/preamble/categories/sets/cardinals.py:118`
- **probed as** `Category of cardinalities`
- **above** [`Objects`](#cat-objects)
- **refines**, transitively, in Sage's linearization order: [`Objects`](#cat-objects)
- **build an object** `Cardinalities(x, *args, **opts)`
- **specimens** `aleph0`, `continuum`

**Operations introduced here** (16 on objects)

*on objects*

- `ElementType()`
  - The thin category associated to the represented cardinal order.
- `Mor(codomain, category=None)`
- `aleph_index()`
- `cardinality()`
- `expression()`
- `finite_value()`
  - Return the ordinary nonnegative integer representing this finite cardinal.
- `initial_ordinal()`
- `is_aleph() -> 'bool'`
- `is_continuum() -> 'bool'`
- `is_countable() -> 'bool'`
- `is_countably_infinite() -> 'bool'`
- `is_finite() -> 'bool'`
- `is_infinite() -> 'bool'`
- `is_uncountable() -> 'bool'`
- `is_uncountably_infinite() -> 'bool'`
- `sort_key() -> 'tuple[int, str]'`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `OrdinalSemirings` {#cat-ordinalsemirings}

The category containing the ordinal semiring under natural operations.

- **defined at** `src/dzack_research/preamble/categories/sets/cardinals.py:601`
- **probed as** `Category of ordinal semirings`
- **above** [`Objects`](#cat-objects)
- **refines**, transitively, in Sage's linearization order: [`Objects`](#cat-objects)
- **build an object** `OrdinalSemirings(x, *args, **opts)`

**Operations introduced here** (9 on objects, 7 on elements)

*on objects*

- `ElementType(parent, expression) -> 'None'`
  - What an ordinal is.
- `Mor(codomain, category=None)`
- `from_expression(expression) -> 'Ordinal'`
- `initial(index) -> 'Ordinal'`
- `natural_product(*factors) -> 'Ordinal'`
- `natural_sum(*summands) -> 'Ordinal'`
- `one() -> 'Ordinal'`
- `proves_le(left, right) -> 'bool'`
- `zero() -> 'Ordinal'`

*on elements*

- `cardinality()`
- `expression()`
- `initial_index()`
- `is_initial() -> 'bool'`
- `ordinal_power(exponent)`
- `ordinal_product(other)`
- `ordinal_sum(other)`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `SageObject` | 8 | 8 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `Element` |  | 9 |  |
| [`Semigroups`](#cat-semigroups) | 8 |  |  |
| [`Sets`](#cat-sets) | 7 | 1 |  |
| [`Magmas`](#cat-magmas) | 6 | 1 |  |
| [`Monoids`](#cat-monoids) | 3 | 3 |  |
| [`AdditiveMagmas`](#cat-additivemagmas) | 5 |  |  |
| [`AdditiveMonoids`](#cat-additivemonoids) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `Sets` {#cat-sets}

The owned category of sets.

```text
All Sage set objects are admitted.  The category owns the mathematical
constructions the preamble adds; Sage remains the implementation of
ordinary set maps.

Sage remains an implementation substrate for concrete parent and coercion
behavior, but the mathematical supercategory edge is entirely owned.
```

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:298`
- **probed as** `Category of sets`
- **above** [`Objects`](#cat-objects)
- **below** [`AdditiveMagmas`](#cat-additivemagmas), [`CartesianProductsOfSets`](#cat-cartesianproductsofsets), [`ConvexPolytopes`](#cat-convexpolytopes), [`CoproductsOfSets`](#cat-coproductsofsets), [`CountableSets`](#cat-countablesets), [`CoxeterDiagrams`](#cat-coxeterdiagrams), [`DisjointUnionsOfSets`](#cat-disjointunionsofsets), [`EnumeratedSets`](#cat-enumeratedsets), [`FinitePowerSets`](#cat-finitepowersets), [`FinitelySupportedFunctionSets`](#cat-finitelysupportedfunctionsets), [`Magmas`](#cat-magmas), [`PartiallyOrderedSets`](#cat-partiallyorderedsets), [`PowerSets`](#cat-powersets), [`RingedSpaces`](#cat-ringedspaces), [`Sets.Finite`](#cat-sets-finite), [`Sets.Infinite`](#cat-sets-infinite)
- **refines**, transitively, in Sage's linearization order: [`Objects`](#cat-objects)
- **build an object** `Sets(x, *args, **opts)`

**Operations introduced here** (7 on objects)

*on objects*

- `ElementType()`
  - The owned category of sets.
- `Mor(codomain, category=None)`
- `exponential(exponent)`
- `finite_subsets()`
- `power_set()`
- `product_with(other)`
  - Return $X \times Y$, the product asked of the objects.
- `subsets_of_size(size)`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `CartesianProductsOfSets` {#cat-cartesianproductsofsets}

Dependent products of families of sets.

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:1118`
- **probed as** `Category of cartesian products of sets`
- **above** [`Sets`](#cat-sets)
- **refines**, transitively, in Sage's linearization order: [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `CartesianProductsOfSets(x, *args, **opts)`

**Operations introduced here** (10 on objects, 1 on elements)

*on objects*

- `ElementType(parent, components) -> None`
  - What an element of a product of a family is.
- `cardinality()`
- `factor(index)`
- `family()`
- `from_maps(source, maps)`
  - Return the unique map into the product with the stated components.
- `has_finite_index_set() -> bool`
- `index_set()`
- `projection(index)`
- `rank(section)`
  - Return the mixed-radix position of a finite product section.
- `unrank(position)`
  - Return the finite product section in mixed-radix order.

*on elements*

- `component(index)`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `SageObject` | 8 | 8 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `Element` |  | 9 |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `CoproductsOfSets` {#cat-coproductsofsets}

Dependent coproducts (disjoint unions) of families of sets.

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:1347`
- **probed as** `Category of coproducts of sets`
- **above** [`Sets`](#cat-sets)
- **refines**, transitively, in Sage's linearization order: [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `CoproductsOfSets(x, *args, **opts)`

**Operations introduced here** (12 on objects, 2 on elements)

*on objects*

- `ElementType(parent, index, value) -> None`
  - What an element of a coproduct of a family is.
- `cardinality()`
- `cofactor(index)`
- `family()`
- `from_maps(target, maps)`
  - Return the unique map out of the coproduct extending the stated maps.
- `index(element)`
  - Return the lazy enumeration rank of one coproduct element.
- `index_set()`
- `injection(index)`
- `is_parent_of(element) -> bool`
- `position(element)`
  - Return the lazy enumeration rank of one coproduct element.
- `rank(element)`
  - Return the lazy enumeration rank of one coproduct element.
- `unrank(position)`
  - Return a coproduct element in lazy rank-layer/diagonal order.

*on elements*

- `summand_element()`
- `summand_index()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `SageObject` | 8 | 8 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `Element` |  | 9 |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `CountableSets` {#cat-countablesets}

Sets equipped with a countable enumeration.

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:1796`
- **probed as** `Category of countable sets`
- **above** [`Sets`](#cat-sets)
- **below** [`CountablyInfiniteSets`](#cat-countablyinfinitesets)
- **refines**, transitively, in Sage's linearization order: [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `CountableSets(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Sets equipped with a countable enumeration.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `DisjointUnionsOfSets` {#cat-disjointunionsofsets}

Dependent coproducts (disjoint unions) of families of sets.

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:1347`
- **probed as** `Category of coproducts of sets`
- **above** [`Sets`](#cat-sets)
- **refines**, transitively, in Sage's linearization order: [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `DisjointUnionsOfSets(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `SageObject` | 8 | 8 |  |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| [`CoproductsOfSets`](#cat-coproductsofsets) | 12 | 2 |  |
| `Element` |  | 9 |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `EnumeratedSets` {#cat-enumeratedsets}

Sets equipped with a represented ranking/enumeration.

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:40`
- **probed as** `Category of enumerated sets`
- **above** [`Sets`](#cat-sets)
- **below** [`FunctionEnumeratedSets`](#cat-functionenumeratedsets), [`InfiniteEnumeratedSets`](#cat-infiniteenumeratedsets)
- **refines**, transitively, in Sage's linearization order: [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `EnumeratedSets(x, *args, **opts)`

**Operations introduced here** (3 on objects)

*on objects*

- `ElementType()`
  - Sets equipped with a represented ranking/enumeration.
- `rank(element)`
- `unrank(position)`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `FinitePowerSets` {#cat-finitepowersets}

Finite power objects \(P_{fin}(X)\), the finite subsets of \(X\).

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:1035`
- **probed as** `Category of finite power sets`
- **above** [`Sets`](#cat-sets)
- **refines**, transitively, in Sage's linearization order: [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `FinitePowerSets(x, *args, **opts)`

**Operations introduced here** (4 on objects)

*on objects*

- `ElementType()`
  - Finite power objects \(P_{fin}(X)\), the finite subsets of \(X\).
- `cardinality()`
- `power_set()`
- `source()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `FinitelySupportedFunctionSets` {#cat-finitelysupportedfunctionsets}

Function sets whose elements have finite support.

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:1882`
- **probed as** `Category of finitely supported function sets`
- **above** [`Sets`](#cat-sets)
- **refines**, transitively, in Sage's linearization order: [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `FinitelySupportedFunctionSets(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Function sets whose elements have finite support.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `PartiallyOrderedSets` {#cat-partiallyorderedsets}

Sets equipped with a partial order.

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:1853`
- **probed as** `Category of partially ordered sets`
- **above** [`Sets`](#cat-sets)
- **below** [`PrimeSpectra`](#cat-primespectra), [`TotallyOrderedSets`](#cat-totallyorderedsets)
- **refines**, transitively, in Sage's linearization order: [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `PartiallyOrderedSets(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Sets equipped with a partial order.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `PowerSets` {#cat-powersets}

The power object \(P(X)\), represented by subobjects of `X`.

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:736`
- **probed as** `Category of power sets`
- **above** [`Sets`](#cat-sets)
- **refines**, transitively, in Sage's linearization order: [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `PowerSets(x, *args, **opts)`

**Operations introduced here** (13 on objects)

*on objects*

- `ElementType()`
  - The power object \(P(X)\), represented by subobjects of ``X``.
- `base_set()`
- `bottom()`
- `cardinality()`
- `cardinality_comparison()`
- `characteristic_hom_category()`
- `characteristic_homset()`
- `direct_image_morphism(morphism)`
- `from_characteristic_morphism(characteristic_morphism)`
- `from_predicate(predicate: collections.abc.Callable)`
- `inverse_image_morphism(morphism)`
- `top()`
- `truth_values()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `Sets.Finite` {#cat-sets-finite}

Sets whose cardinality is finite.

- **not exported**: reachable only as a supercategory
- **probed as** `Category of finite sets`
- **above** [`Sets`](#cat-sets)
- **below** [`OrbitSets`](#cat-orbitsets)
- **refines**, transitively, in Sage's linearization order: [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `Sets.Finite(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 8 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `Sets.Infinite` {#cat-sets-infinite}

Sets whose cardinality is infinite.

- **not exported**: reachable only as a supercategory
- **probed as** `Category of infinite sets`
- **above** [`Sets`](#cat-sets)
- **below** [`CountablyInfiniteSets`](#cat-countablyinfinitesets), [`UncountableSets`](#cat-uncountablesets)
- **refines**, transitively, in Sage's linearization order: [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `Sets.Infinite(x, *args, **opts)`
- **specimens** `NonNegativeReals`, `UnitInterval`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 8 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `FunctionEnumeratedSets` {#cat-functionenumeratedsets}

Enumerated sets whose elements stand for functions.

- **defined at** `src/dzack_research/preamble/categories/sets/enumerated/function_sets.py:83`
- **probed as** `Category of function enumerated sets`
- **above** [`EnumeratedSets`](#cat-enumeratedsets)
- **refines**, transitively, in Sage's linearization order: [`EnumeratedSets`](#cat-enumeratedsets) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `FunctionEnumeratedSets(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`EnumeratedSets`](#cat-enumeratedsets) | 3 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `InfiniteEnumeratedSets` {#cat-infiniteenumeratedsets}

Countably infinite enumerated sets.

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:60`
- **probed as** `Category of infinite enumerated sets`
- **above** [`EnumeratedSets`](#cat-enumeratedsets)
- **below** [`EnumeratedByIntegers`](#cat-enumeratedbyintegers), [`EnumeratedByNaturals`](#cat-enumeratedbynaturals)
- **refines**, transitively, in Sage's linearization order: [`EnumeratedSets`](#cat-enumeratedsets) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `InfiniteEnumeratedSets(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Countably infinite enumerated sets.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`EnumeratedSets`](#cat-enumeratedsets) | 3 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `TotallyOrderedSets` {#cat-totallyorderedsets}

Sets equipped with a total order.

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:1864`
- **probed as** `Category of totally ordered sets`
- **above** [`PartiallyOrderedSets`](#cat-partiallyorderedsets)
- **refines**, transitively, in Sage's linearization order: [`PartiallyOrderedSets`](#cat-partiallyorderedsets) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `TotallyOrderedSets(x, *args, **opts)`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Sets equipped with a total order.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |
| [`PartiallyOrderedSets`](#cat-partiallyorderedsets) | 1 |  |  |

#### `UncountableSets` {#cat-uncountablesets}

Sets whose represented cardinal is provably uncountable.

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:1834`
- **probed as** `Category of uncountable sets`
- **above** [`Sets.Infinite`](#cat-sets-infinite)
- **refines**, transitively, in Sage's linearization order: [`Sets.Infinite`](#cat-sets-infinite) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `UncountableSets(x, *args, **opts)`
- **specimens** `CC`, `CDF`, `RDF`, `RR`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Sets whose represented cardinal is provably uncountable.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 8 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `CountablyInfiniteSets` {#cat-countablyinfinitesets}

Countably infinite sets.

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:1815`
- **probed as** `Category of countably infinite sets`
- **above** [`CountableSets`](#cat-countablesets), [`Sets.Infinite`](#cat-sets-infinite)
- **refines**, transitively, in Sage's linearization order: [`Sets.Infinite`](#cat-sets-infinite) · [`CountableSets`](#cat-countablesets) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `CountablyInfiniteSets(x, *args, **opts)`
- **specimens** `QQ`, `QQbar`, `ZZ`

**Operations introduced here** (1 on objects)

*on objects*

- `ElementType()`
  - Countably infinite sets.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 8 |  |  |
| [`CountableSets`](#cat-countablesets) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `EnumeratedByIntegers` {#cat-enumeratedbyintegers}

Infinite enumerated sets whose functions are indexed by \(\mathbb Z\).

```text
Sage's ranking still runs through \(\mathbb N\); :meth:`function` takes the
integer index, and :meth:`unrank` takes the corresponding natural number.
```

- **defined at** `src/dzack_research/preamble/categories/sets/enumerated/function_sets.py:110`
- **probed as** `Category of enumerated by integers`
- **above** [`InfiniteEnumeratedSets`](#cat-infiniteenumeratedsets)
- **refines**, transitively, in Sage's linearization order: [`InfiniteEnumeratedSets`](#cat-infiniteenumeratedsets) · [`EnumeratedSets`](#cat-enumeratedsets) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `EnumeratedByIntegers(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `function(index)`
- `index_set()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`EnumeratedSets`](#cat-enumeratedsets) | 3 |  |  |
| [`InfiniteEnumeratedSets`](#cat-infiniteenumeratedsets) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

#### `EnumeratedByNaturals` {#cat-enumeratedbynaturals}

Infinite enumerated sets ranked by \(\mathbb N\).

- **defined at** `src/dzack_research/preamble/categories/sets/enumerated/function_sets.py:90`
- **probed as** `Category of enumerated by naturals`
- **above** [`InfiniteEnumeratedSets`](#cat-infiniteenumeratedsets)
- **refines**, transitively, in Sage's linearization order: [`InfiniteEnumeratedSets`](#cat-infiniteenumeratedsets) · [`EnumeratedSets`](#cat-enumeratedsets) · [`Sets`](#cat-sets) · [`Objects`](#cat-objects)
- **build an object** `EnumeratedByNaturals(x, *args, **opts)`

**Operations introduced here** (2 on objects)

*on objects*

- `function(index)`
- `index_set()`

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| `Parent` | 15 |  |  |
| `CategoryObject` | 14 |  |  |
| `SageObject` | 8 |  |  |
| [`Sets`](#cat-sets) | 7 |  |  |
| [`EnumeratedSets`](#cat-enumeratedsets) | 3 |  |  |
| [`InfiniteEnumeratedSets`](#cat-infiniteenumeratedsets) | 1 |  |  |
| [`Objects`](#cat-objects) | 1 |  |  |

### Objects

#### `FourierCharacters` <sub>OBJECT</sub>

The enumerated set \(\{e^{i n x} : n\in\mathbb Z\}\) as symbols \(F_n\in\mathrm{SR}\).

```text
Each character is the formal symbol \(F_n\), not an evaluated
exponential, so \(F_0\) does not collapse to \(1\).
```

- **defined at** `src/dzack_research/preamble/categories/sets/enumerated/fourier_characters.py:9`
- **built by** `FourierCharacters()`

#### `HermitePolynomials` <sub>OBJECT</sub>

The enumerated set \(\{H_n : n\in\mathbb N\}\subset\mathrm{SR}\).

- **defined at** `src/dzack_research/preamble/categories/sets/enumerated/hermite_polynomials.py:13`
- **built by** `HermitePolynomials()`

#### `LaurentMonomials` <sub>OBJECT</sub>

The enumerated set \(\{z^n : n\in\mathbb Z\}\subset\mathrm{SR}\).

- **defined at** `src/dzack_research/preamble/categories/sets/enumerated/laurent_monomials.py:13`
- **built by** `LaurentMonomials()`

#### `SincTranslates` <sub>OBJECT</sub>

The enumerated set \(\{\operatorname{sinc}(\,\cdot\,-n):n\in\mathbb Z\}\subset\mathrm{SR}\).

```text
Each translate is the formal symbol \(\mathrm{sinc}_n\), not Sage's
evaluated \(\operatorname{sinc}\).
```

- **defined at** `src/dzack_research/preamble/categories/sets/enumerated/sinc_translates.py:13`
- **built by** `SincTranslates()`

### Morphisms and homsets

#### `SetInclusion` <sub>MORPHISM</sub>

A represented subobject inclusion \(A\hookrightarrow X\).

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:603`
- **built by** `SetInclusion(domain, codomain, characteristic_morphism=None, finite_members=None)`

**Operations**

- `cardinality()`
- `characteristic_morphism()`
- `complement()`
- `difference(other)`
- `factor_through(target_inclusion)`
  - Return the canonical map of subset objects when this subset is contained.
- `inclusion()`
- `intersection(other)`
- `is_injective() -> bool`
  - Decide ``f(x) = f(y) => x = y`` by counting the image.
- `symmetric_difference(other)`
- `underlying_set()`
- `union(other)`

#### `SetInjection` <sub>MORPHISM</sub>

A set morphism supplied with the assertion that it is injective.

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:581`
- **built by** `SetInjection(...)`

**Operations**

- `is_injective() -> bool`
  - Decide ``f(x) = f(y) => x = y`` by counting the image.

#### `SetSurjection` <sub>MORPHISM</sub>

A set morphism supplied with the assertion that it is surjective.

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:588`
- **built by** `SetSurjection(...)`

**Operations**

- `is_surjective() -> bool`
  - Decide that every point of the codomain is a value.

### Objects the session already holds

#### `NN` <sub>LIVE OBJECT</sub>

- **is** Natural numbers
- **in** Category of natural number sets

#### `aleph0` <sub>LIVE OBJECT</sub>

- **is** ℵ_0
- **in** Category of cardinalities

#### `continuum` <sub>LIVE OBJECT</sub>

- **is** (2)^(ℵ_0)
- **in** Category of cardinalities

### Supporting classes

#### `CardinalComparison` <sub>CLASS</sub>

Create a collection of name/value pairs.

```text
Example enumeration:

>>> class Color(Enum):
...     RED = 1
...     BLUE = 2
...     GREEN = 3

Access them by:

- attribute access:

  >>> Color.RED
  <Color.RED: 1>

- value lookup:

  >>> Color(1)
  <Color.RED: 1>

- name lookup:

  >>> Color['RED']
  <Color.RED: 1>

Enumerations can be iterated over, and know how many members they have:

>>> len(Color)
3

>>> list(Color)
[<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

Methods can be added to enumerations, and members can have their own
attributes -- see the documentation for details.
```

- **defined at** `src/dzack_research/preamble/categories/sets/cardinals.py:62`
- **built by** `CardinalComparison(*values)`

### Functions

#### `CartesianProductMorphism` <sub>FUNCTION</sub>

Return the componentwise map between two dependent products.

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:1614`
- **built by** `CartesianProductMorphism(source, target, component_morphisms)`

#### `CartesianProductOfFamily` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:1594`
- **built by** `CartesianProductOfFamily(index_set, family)`

#### `CartesianProductOfSets` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:1606`
- **built by** `CartesianProductOfSets(*factors)`

#### `ConditionSet` <sub>FUNCTION</sub>

Return the subset of `universe` cut out by `predicate`.

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:557`
- **built by** `ConditionSet(universe, predicate)`

#### `CoproductMorphism` <sub>FUNCTION</sub>

Return the componentwise map between two dependent coproducts.

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:1646`
- **built by** `CoproductMorphism(source, target, component_morphisms)`

#### `CoproductOfFamily` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:1630`
- **built by** `CoproductOfFamily(index_set, family)`

#### `CoproductOfSets` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:1642`
- **built by** `CoproductOfSets(*cofactors)`

#### `ExponentialOfSets` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:951`
- **built by** `ExponentialOfSets(codomain, exponent)`

#### `FiniteSets` <sub>FUNCTION</sub>

The category of finite sets.

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:536`
- **built by** `FiniteSets()`

#### `FiniteSubsets` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:1089`
- **built by** `FiniteSubsets(source)`

#### `ImageSet` <sub>FUNCTION</sub>

Return the represented image of `domain_subset` under `map_`.

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:562`
- **built by** `ImageSet(map_, domain_subset, *, category=None, is_injective=None, inverse=None)`

#### `InfiniteSets` <sub>FUNCTION</sub>

The category of infinite sets.

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:541`
- **built by** `InfiniteSets()`

#### `Ordinals` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/sets/cardinals.py:880`
- **built by** `Ordinals() -> 'OrdinalSemiring'`

#### `PowerSet` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:879`
- **built by** `PowerSet(base_set)`

#### `Set` <sub>FUNCTION</sub>

Return `source` as an owned set whenever this constructor creates it.

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:548`
- **built by** `Set(source)`

#### `SubsetsOfSize` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:1026`
- **built by** `SubsetsOfSize(source, subset_cardinality)`

#### `aleph` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/sets/cardinals.py:920`
- **built by** `aleph(index) -> "'Cardinalities.ObjectType'"`

#### `cardinal` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/sets/cardinals.py:901`
- **built by** `cardinal(value) -> "'Cardinalities.ObjectType'"`

#### `cartesian_product_of` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:1610`
- **built by** `cartesian_product_of(factors)`

#### `omega` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/sets/cardinals.py:889`
- **built by** `omega(index) -> 'Ordinal'`

#### `ordinal` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/sets/cardinals.py:885`
- **built by** `ordinal(value) -> 'Ordinal'`

#### `set_injection` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:595`
- **built by** `set_injection(domain, codomain, function)`

#### `set_surjection` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/categories/sets/set_categories.py:599`
- **built by** `set_surjection(domain, codomain, function)`

## Named Catalogue & Classification Tables

> Named integral lattices (U, E8, LK3, Mukai, etc.), 2-elementary tables, Nikulin involutions, and Primitive embeddings.

### Functions

#### `signature_orthogonal_sums` <sub>FUNCTION</sub>

Enumerate multisets of the supplied blocks with the target signature.

- **defined at** `src/dzack_research/preamble/catalogue.py:843`
- **built by** `signature_orthogonal_sums(target_signature, blocks)`

#### `two_elementary_orthogonal_sums` <sub>FUNCTION</sub>

Return block-orthogonal realizations of the stated 2-elementary invariants.

- **defined at** `src/dzack_research/preamble/catalogue.py:788`
- **built by** `two_elementary_orthogonal_sums(target_signature, a, delta)`

#### `validate_negative_def_two_elementary_table` <sub>FUNCTION</sub>

Validate the signature and discriminant invariants of every listed class.

- **defined at** `src/dzack_research/preamble/catalogue.py:717`
- **built by** `validate_negative_def_two_elementary_table()`

#### `validate_two_elementary_table` <sub>FUNCTION</sub>

Validate every row against its signature and Nikulin invariants.

- **defined at** `src/dzack_research/preamble/catalogue.py:744`
- **built by** `validate_two_elementary_table()`

## Tensor Calculus

> Multilinear tensors, Tensor modules, Tensor shapes, and Tensor products.

### Objects

#### `TensorModule` <sub>OBJECT</sub>

The module of type-$(p,q)$ tensors with the given index ranks.

```text
If every contravariant index is a copy of \(M=R^n\) and every covariant
index is a copy of \(M\), this is
\(M^{\otimes p}\otimes(M^*)^{\otimes q}\).  A type-$(0,q)$ tensor
at infinite rank is an element of \((M^{\otimes q})^*\), not of
\((M^*)^{\otimes q}\).

EXAMPLES::

    sage: from dzack_research.preamble.tensors import tensor
    sage: G = tensor(ZZ, (), (2, 2), [[0, 1], [1, 0]])
    sage: G.parent()
    ((ZZ^2)*)^{⊗2}
    sage: G.tensor_type()
    (0, 2)
    sage: latex(G.parent())
    ((\mathbb{Z}^{2})^{*})^{\otimes 2}
```

- **defined at** `src/dzack_research/preamble/tensors/tensor.py:1162`
- **built by** `TensorModule(base_ring: sage.structure.parent.Parent, upper_ranks: tuple[int, ...], lower_ranks: tuple[int, ...])`

**Operations**

- `Element(parent: sage.structure.parent.Parent, entries: tuple) -> None`
  - A coordinate tensor that is not Sage's vector or matrix specialization.
- `construction()`
  - Return no functorial construction.
- `index_modules()`
  - Return the contravariant and covariant index modules \(R^{n_i}\).
- `tensor_indices()`
  - Return the standard generating set of each finite index module.
- `tensor_shape()`
  - Return the family assigning each index slot the rank of its module.
- `tensor_type() -> Any`
  - Return the type $(p, q)$ as a point of $\mathbb N^2$ (`CON-15`).
- `tensor_valence() -> Any`
- `zero() -> dzack_research.preamble.tensors.tensor._CoordinateTensor`

### Supporting classes

#### `Tensor` <sub>CLASS</sub>

A tensor of type $(p,q)$.

```text
A type-$(p,q)$ tensor on a module \(M\) is an element of
\(M^{\otimes p}\otimes(M^*)^{\otimes q}\).  When the index modules
differ, it is an element of the corresponding mixed tensor product.
At infinite rank a type-$(0,2)$ pairing lives in
\((M\otimes M)^*\), not in \((M^*)^{\otimes 2}\).

This class carries no storage.  Every tensor, of every valence, is an
element of a :class:`TensorModule` over the owned base ring.
```

- **defined at** `src/dzack_research/preamble/tensors/tensor.py:293`
- **built by** `Tensor()`

**Operations**

- `change_ring(ring)`
  - Change coefficients without changing tensor variance.
- `components()`
  - Return the finite rectangular component array of this tensor.
- `contract(*vectors)`
  - Fully contract a purely covariant tensor with contravariant vectors.
- `dual_tensor()`
  - Dualize a nondegenerate pairing or copairing.
- `index_modules()`
  - Return the contravariant and covariant index modules.
- `is_equal_tensor(other) -> bool`
  - Return whether ``other`` is the same tensor mathematically.
- `is_symmetric() -> bool`
  - Return whether a square two-index tensor is symmetric in its slots.
- `list()`
  - Return flattened finite components in tensor-index order.
- `pullback(morphism)`
  - Pull this covariant tensor back along an owned linear morphism.
- `tensor_indices()`
  - Return the generating set of each index module.
- `tensor_order()`
  - Return the cardinal number of tensor indices.
- `tensor_shape()`
  - Return the family assigning each index slot the rank of its module.
- `tensor_space()`
  - Return the module of which this tensor is an element.
- `tensor_type() -> Any`
  - Return $(p,q)$: $p$ contravariant indices and $q$ covariant indices.
- `tensor_valence() -> Any`
  - Return the type $(p,q)$; synonym of :meth:`tensor_type`.

### Functions

#### `tensor` <sub>FUNCTION</sub>

General tensor constructor with variance encoded in the rank vectors.

```text
``tensor.vector(R, data)``, ``tensor.covector(R, data)``, and
``tensor.matrix(R, data)`` are small typed conveniences over the main
``tensor(R, ps, qs, data)`` call.  They accept owned rings and mathematical
component data only; Sage constructor/storage compatibility is not public
API.

The main call is ``tensor(R, ps, qs, data)``.  ``ps`` lists upper-index
dimensions and ``qs`` lower-index dimensions.  Hence vectors and covectors
are different constructor calls even though both have one index.
```

- **defined at** `src/dzack_research/preamble/tensors/tensor.py:1372`
- **built by** `tensor(base_ring: sage.structure.parent.Parent, upper_ranks, lower_ranks, components=None, **kwds) -> dzack_research.preamble.tensors.tensor.Tensor`

## Logic & Predicates

> Three-valued logic predicates, queries, and certainty propagation.

### Supporting classes

#### `Predicate` <sub>CLASS</sub>

An unevaluated mathematical proposition.

- **defined at** `src/dzack_research/preamble/logic.py:14`
- **built by** `Predicate(...)`

### Functions

#### `ask` <sub>FUNCTION</sub>

Return the truth value of `statement`, or `Unknown` if undecided.

```text
``True`` and ``False`` pass through unchanged.  Predicates own their
evaluation algorithms.  ``Unknown`` also passes through, so callers can
compose this with existing Sage three-valued predicates.
```

- **defined at** `src/dzack_research/preamble/logic.py:27`
- **built by** `ask(statement, *, max_prec: int = 4096)`

## Specialized Geometries (Coble & Sterk)

> Coble surfaces, Sterk invariant theory, and Automorphic forms.

### Supporting classes

#### `Coble` <sub>CLASS</sub>

- **defined at** `src/dzack_research/preamble/coble.py:11`
- **built by** `Coble()`

**Operations**

- `isotropic_vectors()`
- `isotropic_vectors_in_TEn()`
- `isotropic_vectors_in_TdP()`
- `rank_ten_coxeter_roots()`
- `rank_ten_diagram()`

#### `Sterk` <sub>CLASS</sub>

- **defined at** `src/dzack_research/preamble/sterk.py:87`
- **built by** `Sterk()`

**Operations**

- `diagram_layouts()`
  - Return copies of the optional exact presentation coordinates.
- `diagrams()`
- `isotropic_vectors()`
- `roots_18_0_0()`
- `roots_18_2_0()`
- `selected_isotropic_vectors()`
- `sterk5_in_U_E8_2()`
  - Return Sterk 5's fourteen roots in ``U + E8(2)`` coordinates.
- `sterk_roots()`
- `sterks_in_TEn()`
  - Return the alternative Sterk 1--3 roots in ``TEn`` coordinates.

## Preamble Entrypoints & Utilities

> Top-level session loaders, environment initializers, and refinement helpers.

```mermaid
graph RL
  ObjectSetsOfDiscreteCategories["ObjectSetsOfDiscreteCategories"]
  SetsWithPartialMaps["SetsWithPartialMaps"]
  Objects("Objects")
  ObjectSetsOfDiscreteCategories --> SetsWithPartialMaps
  SetsWithPartialMaps --> Objects
  classDef outside stroke-dasharray:6 4,fill:#f8fafc;
  class Objects outside;
```

### Categories

Ordered by depth: the least structured first.

#### `SetsWithPartialMaps` {#cat-setswithpartialmaps}

The category whose objects are sets and whose morphisms are maps that are allowed to raise a :exc:`ValueError` on some inputs.

```text
This category is equivalent to the category of pointed sets,
via the equivalence sending an object X to X union {error},
a morphism f to the morphism of pointed sets that sends x
to f(x) if f does not raise an error on x, or to error if it
does.

EXAMPLES::

    sage: SetsWithPartialMaps()
    Category of sets with partial maps

    sage: SetsWithPartialMaps().super_categories()
    [Category of objects]

TESTS::

    sage: TestSuite(SetsWithPartialMaps()).run()
```

- **not exported**: reachable only as a supercategory
- **probed as** `Category of sets with partial maps`
- **above** [`Objects`](#cat-objects)
- **below** [`ObjectSetsOfDiscreteCategories`](#cat-objectsetsofdiscretecategories)
- **refines**, transitively, in Sage's linearization order: [`Objects`](#cat-objects)
- **build an object** `SetsWithPartialMaps(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

#### `ObjectSetsOfDiscreteCategories` {#cat-objectsetsofdiscretecategories}

The category of sets.

```text
The base category for collections of elements with = (equality).

This is also the category whose objects are all parents.

EXAMPLES::

    sage: Sets()
    Category of sets
    sage: Sets().super_categories()
    [Category of sets with partial maps]
    sage: Sets().all_super_categories()
    [Category of sets, Category of sets with partial maps, Category of objects]

Let us consider an example of set::

    sage: P = Sets().example("inherits")
    sage: P
    Set of prime numbers

See ``P??`` for the code.


P is in the category of sets::

    sage: P.category()
    Category of sets

and therefore gets its methods from the following classes::

    sage: for cl in P.__class__.mro(): print(cl)
    <class 'sage.categories.examples.sets_cat.PrimeNumbers_Inherits_with_category'>
    <class 'sage.categories.examples.sets_cat.PrimeNumbers_Inherits'>
    <class 'sage.categories.examples.sets_cat.PrimeNumbers_Abstract'>
    <class 'sage.structure.unique_representation.UniqueRepresentation'>
    <class 'sage.misc.fast_methods.WithEqualityById'>
    <class 'sage.structure.unique_representation.CachedRepresentation'>
    <class 'sage.structure.unique_representation.WithPicklingByInitArgs'>
    <class 'sage.structure.parent.Parent'>
    <class 'sage.structure.category_object.CategoryObject'>
    <class 'sage.structure.sage_object.SageObject'>
    <class 'sage.categories.sets_cat.Sets.parent_class'>
    <class 'sage.categories.sets_with_partial_maps.SetsWithPartialMaps.parent_class'>
    <class 'sage.categories.objects.Objects.parent_class'>
    <class 'object'>

We run some generic checks on P::

    sage: TestSuite(P).run(verbose=True)                                            # needs sage.libs.pari
    running ._test_an_element() . . . pass
    running ._test_cardinality() . . . pass
    running ._test_category() . . . pass
    running ._test_construction() . . . pass
    running ._test_elements() . . .
      Running the test suite of self.an_element()
      running ._test_category() . . . pass
      running ._test_eq() . . . pass
      running ._test_new() . . . pass
      running ._test_not_implemented_methods() . . . pass
      running ._test_pickling() . . . pass
      pass
    running ._test_elements_eq_reflexive() . . . pass
    running ._test_elements_eq_symmetric() . . . pass
    running ._test_elements_eq_transitive() . . . pass
    running ._test_elements_neq() . . . pass
    running ._test_eq() . . . pass
    running ._test_new() . . . pass
    running ._test_not_implemented_methods() . . . pass
    running ._test_pickling() . . . pass
    running ._test_some_elements() . . . pass

Now, we manipulate some elements of P::

    sage: P.an_element()
    47
    sage: x = P(3)
    sage: x.parent()
    Set of prime numbers
    sage: x in P, 4 in P
    (True, False)
    sage: x.is_prime()
    True

They get their methods from the following classes::

    sage: for cl in x.__class__.mro(): print(cl)
    <class 'sage.categories.examples.sets_cat.PrimeNumbers_Inherits_with_category.element_class'>
    <class 'sage.categories.examples.sets_cat.PrimeNumbers_Inherits.Element'>
    <class 'sage.rings.integer.IntegerWrapper'>
    <class 'sage.rings.integer.Integer'>
    <class 'sage.structure.element.EuclideanDomainElement'>
    <class 'sage.structure.element.PrincipalIdealDomainElement'>
    <class 'sage.structure.element.DedekindDomainElement'>
    <class 'sage.structure.element.IntegralDomainElement'>
    <class 'sage.structure.element.CommutativeRingElement'>
    <class 'sage.structure.element.RingElement'>
    <class 'sage.structure.element.ModuleElement'>
    <class 'sage.categories.examples.sets_cat.PrimeNumbers_Abstract.Element'>
    <class 'sage.structure.element.Element'>
    <class 'sage.structure.sage_object.SageObject'>
    <class 'sage.categories.sets_cat.Sets.element_class'>
    <class 'sage.categories.sets_with_partial_maps.SetsWithPartialMaps.element_class'>
    <class 'sage.categories.objects.Objects.element_class'>
    <... 'object'>

FIXME: Objects.element_class is not very meaningful ...


TESTS::

      sage: TestSuite(Sets()).run()
```

- **defined at** `/home/dzack/gitclones/sage-dev-allopts/.venv/lib/python3.14/site-packages/sage/categories/sets_cat.py:102`
- **probed as** `Category of sets`
- **above** [`SetsWithPartialMaps`](#cat-setswithpartialmaps)
- **refines**, transitively, in Sage's linearization order: [`SetsWithPartialMaps`](#cat-setswithpartialmaps) · [`Objects`](#cat-objects)
- **build an object** `ObjectSetsOfDiscreteCategories(x, *args, **opts)`

Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.

**Inherited operations**, defined where they are owned:

| from | objects | elements | morphisms |
| :--- | ---: | ---: | ---: |
| [`Sets`](#cat-sets) | 7 | 1 | 2 |

### Functions

#### `ComplexNumber` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/language_runtime.py:40`
- **built by** `ComplexNumber(real, imag=None)`

#### `Integer` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/language_runtime.py:24`
- **built by** `Integer(value=0)`

#### `RealNumber` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/language_runtime.py:30`
- **built by** `RealNumber(value)`

#### `ellipsis_iter` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/language_runtime.py:111`
- **built by** `ellipsis_iter(*args)`

#### `ellipsis_range` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/language_runtime.py:104`
- **built by** `ellipsis_range(*args)`

#### `factorial` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/language_runtime.py:97`
- **built by** `factorial(value)`

#### `lmap` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/utilities.py:11`
- **built by** `lmap(function: collections.abc.Callable[[T], U], values: collections.abc.Iterable[T]) -> list[U]`

#### `load` <sub>FUNCTION</sub>

Load a Sage file and restore this session's owned scalar vocabulary.

- **defined at** `src/dzack_research/preamble/all.py:793`
- **built by** `load(filename: str, globals: dict | None = None, attach: bool = False) -> None`

#### `lzip` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/utilities.py:15`
- **built by** `lzip(*iterables: collections.abc.Iterable[T]) -> list[tuple[T, ...]]`

#### `matrix` <sub>FUNCTION</sub>

Construct the owned matrix-Hom represented by a rectangular row family.

- **defined at** `src/dzack_research/preamble/language_runtime.py:52`
- **built by** `matrix(rows)`

#### `symbolic_expression` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/language_runtime.py:121`
- **built by** `symbolic_expression(*_args, **_kwargs)`

#### `to_var_names` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/utilities.py:19`
- **built by** `to_var_names(names: str) -> list[str]`

#### `var` <sub>FUNCTION</sub>

- **defined at** `src/dzack_research/preamble/language_runtime.py:115`
- **built by** `var(*_args, **_kwargs)`

#### `zipsum` <sub>FUNCTION</sub>

Return the sum of pairwise terms from two equally sized iterables.

- **defined at** `src/dzack_research/preamble/utilities.py:23`
- **built by** `zipsum(coefficients: collections.abc.Iterable[C], elements: collections.abc.Iterable[G], zero: T, *, term: collections.abc.Callable[[C, G], T] | None = None) -> T`

## Every exported name

| name | kind | chapter |
| :--- | :--- | :--- |
| `AA` | live object | Rings, Fields & Commutative Algebra |
| [`AbelianGroupInclusionFunctor`](#fun-abeliangroupinclusionfunctor) | functor | Functors & Adjunctions |
| `AbelianGroups` | function | Groups, Profinite Groups & Galois Theory |
| [`AbelianizationAdjunction`](#fun-abelianizationadjunction) | adjunction | Functors & Adjunctions |
| [`AbelianizationFunctor`](#fun-abelianizationfunctor) | functor | Functors & Adjunctions |
| `AbsoluteDecompositionGroup` | class | Groups, Profinite Groups & Galois Theory |
| [`AbsoluteGaloisGroup`](#cat-absolutegaloisgroup) | category | Groups, Profinite Groups & Galois Theory |
| `AbsoluteGaloisGroupElement` | element | Groups, Profinite Groups & Galois Theory |
| [`AbsoluteGaloisGroups`](#cat-absolutegaloisgroups) | category | Groups, Profinite Groups & Galois Theory |
| [`AbsoluteGaloisGroupsOfFiniteFields`](#cat-absolutegaloisgroupsoffinitefields) | category | Groups, Profinite Groups & Galois Theory |
| `AbsoluteGaloisSliceAutomorphism` | morphism | Groups, Profinite Groups & Galois Theory |
| `AbsoluteInertiaGroup` | class | Groups, Profinite Groups & Galois Theory |
| [`AdicallyCompleteRings`](#cat-adicallycompleterings) | category | Rings, Fields & Commutative Algebra |
| [`Adjunction`](#fun-adjunction) | adjunction | Functors & Adjunctions |
| [`AffineSchemes`](#cat-affineschemes) | category | Schemes & Algebraic Geometry |
| `AffineSpace` | function | Schemes & Algebraic Geometry |
| [`AffineSpaces`](#cat-affinespaces) | category | Schemes & Algebraic Geometry |
| [`AffineSpecFunctor`](#fun-affinespecfunctor) | functor | Schemes & Algebraic Geometry |
| [`AlgebraBaseChangeAdjunction`](#fun-algebrabasechangeadjunction) | adjunction | Functors & Adjunctions |
| [`AlgebraHomset`](#cat-algebrahomset) | category | Algebras & Differential Graded Algebras |
| `AlgebraMorphism` | morphism | Algebras & Differential Graded Algebras |
| [`AlgebraRestrictionOfScalarsFunctor`](#fun-algebrarestrictionofscalarsfunctor) | functor | Functors & Adjunctions |
| [`AlgebraScalarExtensionFunctor`](#fun-algebrascalarextensionfunctor) | functor | Functors & Adjunctions |
| [`AlgebraUnderlyingModuleFunctor`](#fun-algebraunderlyingmodulefunctor) | functor | Functors & Adjunctions |
| `AlgebraicCorrelationMorphism` | function | Modules, Complexes & Homological Algebra |
| [`Algebras`](#cat-algebras) | category | Algebras & Differential Graded Algebras |
| [`AlgebrasWithChosenFinitePresentation`](#cat-algebraswithchosenfinitepresentation) | category | Algebras & Differential Graded Algebras |
| [`AlgebrasWithChosenMultiplication`](#cat-algebraswithchosenmultiplication) | category | Algebras & Differential Graded Algebras |
| [`AlternatingAlgebraFunctor`](#fun-alternatingalgebrafunctor) | functor | Functors & Adjunctions |
| `AlternatingAlgebraOf` | function | Algebras & Differential Graded Algebras |
| `AlternatingAlgebraOn` | function | Algebras & Differential Graded Algebras |
| [`AlternatingAlgebras`](#cat-alternatingalgebras) | category | Algebras & Differential Graded Algebras |
| [`ArrowCategory`](#cat-arrowcategory) | category | Abstract Category Theory & Universal Constructions |
| [`ArtinianRings`](#cat-artinianrings) | category | Rings, Fields & Commutative Algebra |
| [`AssociativeAlgebras`](#cat-associativealgebras) | category | Algebras & Differential Graded Algebras |
| [`AssociativeAlgebrasWithChosenMultiplication`](#cat-associativealgebraswithchosenmultiplication) | category | Algebras & Differential Graded Algebras |
| [`AugmentedAlgebras`](#cat-augmentedalgebras) | category | Algebras & Differential Graded Algebras |
| [`AutCategoryConstruction`](#cat-autcategoryconstruction) | category | Abstract Category Theory & Universal Constructions |
| [`AutCategoryOf`](#cat-autcategoryof) | category | Abstract Category Theory & Universal Constructions |
| [`AutomorphismArrowCategory`](#cat-automorphismarrowcategory) | category | Abstract Category Theory & Universal Constructions |
| [`BaseChangeAdjunction`](#fun-basechangeadjunction) | adjunction | Functors & Adjunctions |
| `BasedFreeModule` | function | Modules, Complexes & Homological Algebra |
| [`Bifunctor`](#fun-bifunctor) | functor | Abstract Category Theory & Universal Constructions |
| `BilinearForm` | function | Modules, Complexes & Homological Algebra |
| [`BilinearFormModules`](#cat-bilinearformmodules) | category | Modules, Complexes & Homological Algebra |
| `BilinearFormMorphism` | morphism | Modules, Complexes & Homological Algebra |
| `BilinearForms` | function | Bilinear Forms, Quadratic Forms & Pairings |
| [`BilinearFreeFormAdjunction`](#fun-bilinearfreeformadjunction) | adjunction | Functors & Adjunctions |
| `BilinearMap` | class | Modules, Complexes & Homological Algebra |
| [`BilinearUnderlyingModuleFunctor`](#fun-bilinearunderlyingmodulefunctor) | functor | Functors & Adjunctions |
| [`BiproductBifunctor`](#fun-biproductbifunctor) | functor | Functors & Adjunctions |
| [`BiproductCategory`](#cat-biproductcategory) | category | Abstract Category Theory & Universal Constructions |
| [`BiproductModules`](#cat-biproductmodules) | category | Modules, Complexes & Homological Algebra |
| `Boundaries` | function | Modules, Complexes & Homological Algebra |
| `C` | function | Function Spaces & Analysis |
| `CC` | live object | Rings, Fields & Commutative Algebra |
| `CDF` | live object | Rings, Fields & Commutative Algebra |
| `CardinalComparison` | class | Sets, Cardinals & Ordinals |
| [`Cardinalities`](#cat-cardinalities) | category | Sets, Cardinals & Ordinals |
| [`CardinalityFunctor`](#fun-cardinalityfunctor) | functor | Functors & Adjunctions |
| `CartesianProductMorphism` | function | Sets, Cardinals & Ordinals |
| `CartesianProductOfFamily` | function | Sets, Cardinals & Ordinals |
| `CartesianProductOfSets` | function | Sets, Cardinals & Ordinals |
| [`CartesianProductsOfSets`](#cat-cartesianproductsofsets) | category | Sets, Cardinals & Ordinals |
| `CartierDivisorGroup` | function | Divisors & Picard Theory |
| [`CartierDivisorGroups`](#cat-cartierdivisorgroups) | category | Divisors & Picard Theory |
| [`Cat`](#cat-cat) | category | Abstract Category Theory & Universal Constructions |
| `CategoricalIsomorphism` | morphism | Abstract Category Theory & Universal Constructions |
| `CategoryFunctorMorphism` | morphism | Abstract Category Theory & Universal Constructions |
| [`CategoryInclusionFunctor`](#fun-categoryinclusionfunctor) | functor | Functors & Adjunctions |
| `CategoryObject` | object | Abstract Category Theory & Universal Constructions |
| `CategoryPacket` | class | Abstract Category Theory & Universal Constructions |
| `ClassGroup` | function | Divisors & Picard Theory |
| [`ClassGroups`](#cat-classgroups) | category | Divisors & Picard Theory |
| [`ClosedEmbeddings`](#cat-closedembeddings) | category | Schemes & Algebraic Geometry |
| `Coble` | class | Specialized Geometries (Coble & Sterk) |
| `CochainComplex` | function | Modules, Complexes & Homological Algebra |
| `CochainComplexElement` | element | Modules, Complexes & Homological Algebra |
| `CochainComplexObject` | object | Modules, Complexes & Homological Algebra |
| [`CochainComplexes`](#cat-cochaincomplexes) | category | Modules, Complexes & Homological Algebra |
| `CochainDifferential` | class | Modules, Complexes & Homological Algebra |
| [`CochainHomset`](#cat-cochainhomset) | category | Modules, Complexes & Homological Algebra |
| `CochainMorphism` | morphism | Modules, Complexes & Homological Algebra |
| [`CochainUnderlyingGradedModuleFunctor`](#fun-cochainunderlyinggradedmodulefunctor) | functor | Functors & Adjunctions |
| `Cocone` | function | Abstract Category Theory & Universal Constructions |
| [`CoconeCategory`](#cat-coconecategory) | category | Abstract Category Theory & Universal Constructions |
| [`CodomainFunctor`](#fun-codomainfunctor) | functor | Abstract Category Theory & Universal Constructions |
| [`CoextensionOfScalarsFunctor`](#fun-coextensionofscalarsfunctor) | functor | Functors & Adjunctions |
| `Cohomology` | function | Modules, Complexes & Homological Algebra |
| `CohomologyAlgebra` | function | Algebras & Differential Graded Algebras |
| `CohomologyAlgebraElement` | element | Algebras & Differential Graded Algebras |
| [`CohomologyAlgebraFunctor`](#fun-cohomologyalgebrafunctor) | functor | Functors & Adjunctions |
| [`CohomologyAlgebraHomset`](#cat-cohomologyalgebrahomset) | category | Algebras & Differential Graded Algebras |
| `CohomologyAlgebraMorphism` | morphism | Algebras & Differential Graded Algebras |
| [`CohomologyAlgebras`](#cat-cohomologyalgebras) | category | Algebras & Differential Graded Algebras |
| [`CohomologyFunctor`](#fun-cohomologyfunctor) | functor | Functors & Adjunctions |
| [`CohomologyModules`](#cat-cohomologymodules) | category | Modules, Complexes & Homological Algebra |
| [`CoinductionFunctor`](#fun-coinductionfunctor) | functor | Functors & Adjunctions |
| [`CoinvariantsFunctor`](#fun-coinvariantsfunctor) | functor | Functors & Adjunctions |
| [`CoinvariantsTrivialAdjunction`](#fun-coinvariantstrivialadjunction) | adjunction | Functors & Adjunctions |
| [`CokernelArrowFunctor`](#fun-cokernelarrowfunctor) | functor | Functors & Adjunctions |
| [`ColimitsOfCategory`](#cat-colimitsofcategory) | category | Abstract Category Theory & Universal Constructions |
| [`CommutativeAlgebraCoproducts`](#cat-commutativealgebracoproducts) | category | Algebras & Differential Graded Algebras |
| [`CommutativeAlgebraPushouts`](#cat-commutativealgebrapushouts) | category | Algebras & Differential Graded Algebras |
| `CommutativeAlgebras` | function | Algebras & Differential Graded Algebras |
| [`CommutativeDifferentialGradedAlgebras`](#cat-commutativedifferentialgradedalgebras) | category | Algebras & Differential Graded Algebras |
| `CommutativeIdeal` | function | Rings, Fields & Commutative Algebra |
| [`CommutativeIdeals`](#cat-commutativeideals) | category | Rings, Fields & Commutative Algebra |
| `CommutativeRings` | function | Rings, Fields & Commutative Algebra |
| `CommutativeSquare` | morphism | Abstract Category Theory & Universal Constructions |
| [`CommutatorLieAlgebras`](#cat-commutatorliealgebras) | category | Algebras & Differential Graded Algebras |
| [`CompleteLocalRings`](#cat-completelocalrings) | category | Rings, Fields & Commutative Algebra |
| `ComplexField` | function | Rings, Fields & Commutative Algebra |
| `ComplexNumber` | function | Preamble Entrypoints & Utilities |
| [`ComposedFunctor`](#fun-composedfunctor) | functor | Functors & Adjunctions |
| [`CompositeAdjunction`](#fun-compositeadjunction) | adjunction | Functors & Adjunctions |
| [`CompositeFunctor`](#fun-compositefunctor) | functor | Functors & Adjunctions |
| `ConditionSet` | function | Sets, Cardinals & Ordinals |
| `Cone` | function | Abstract Category Theory & Universal Constructions |
| [`ConeCategory`](#cat-conecategory) | category | Abstract Category Theory & Universal Constructions |
| `Connection` | element | Modules, Complexes & Homological Algebra |
| `ConnectionDeRhamDifferential` | class | Modules, Complexes & Homological Algebra |
| `ConnectionDeRhamModule` | class | Modules, Complexes & Homological Algebra |
| [`ConnectionHomset`](#cat-connectionhomset) | category | Modules, Complexes & Homological Algebra |
| `ConnectionMorphism` | element | Modules, Complexes & Homological Algebra |
| [`ConnectionSpace`](#cat-connectionspace) | category | Modules, Complexes & Homological Algebra |
| `Connections` | function | Modules, Complexes & Homological Algebra |
| [`ConstantDiagram`](#fun-constantdiagram) | functor | Abstract Category Theory & Universal Constructions |
| `ContinuousGroupHomset` | object | Groups, Profinite Groups & Galois Theory |
| [`ContravariantFunctor`](#fun-contravariantfunctor) | functor | Abstract Category Theory & Universal Constructions |
| `ConvexPolygon` | function | Schemes & Algebraic Geometry |
| [`ConvexPolygons`](#cat-convexpolygons) | category | Schemes & Algebraic Geometry |
| `ConvexPolytope` | function | Schemes & Algebraic Geometry |
| [`ConvexPolytopes`](#cat-convexpolytopes) | category | Schemes & Algebraic Geometry |
| [`CoproductCoconeCategory`](#cat-coproductcoconecategory) | category | Abstract Category Theory & Universal Constructions |
| `CoproductMorphism` | function | Sets, Cardinals & Ordinals |
| `CoproductOfFamily` | function | Sets, Cardinals & Ordinals |
| `CoproductOfSets` | function | Sets, Cardinals & Ordinals |
| [`CoproductsOfCategory`](#cat-coproductsofcategory) | category | Abstract Category Theory & Universal Constructions |
| [`CoproductsOfSets`](#cat-coproductsofsets) | category | Sets, Cardinals & Ordinals |
| [`CoreCategory`](#cat-corecategory) | category | Abstract Category Theory & Universal Constructions |
| `CorrelationIsomorphism` | function | Modules, Complexes & Homological Algebra |
| [`CosliceCategory`](#cat-coslicecategory) | category | Abstract Category Theory & Universal Constructions |
| [`CountableSets`](#cat-countablesets) | category | Sets, Cardinals & Ordinals |
| [`CountablyInfiniteSets`](#cat-countablyinfinitesets) | category | Sets, Cardinals & Ordinals |
| [`CoxeterDiagrams`](#cat-coxeterdiagrams) | category | Abstract Category Theory & Universal Constructions |
| [`Curves`](#cat-curves) | category | Schemes & Algebraic Geometry |
| `Cycles` | function | Modules, Complexes & Homological Algebra |
| [`CyclicGroups`](#cat-cyclicgroups) | category | Groups, Profinite Groups & Galois Theory |
| `CyclotomicCharacter` | morphism | Groups, Profinite Groups & Galois Theory |
| `CyclotomicField` | function | Rings, Fields & Commutative Algebra |
| [`DGAHomset`](#cat-dgahomset) | category | Algebras & Differential Graded Algebras |
| `DGAMorphism` | morphism | Algebras & Differential Graded Algebras |
| [`DeRhamAdjunction`](#fun-derhamadjunction) | adjunction | Functors & Adjunctions |
| `DeRhamAlgebra` | function | Algebras & Differential Graded Algebras |
| [`DeRhamAlgebras`](#cat-derhamalgebras) | category | Algebras & Differential Graded Algebras |
| [`DeRhamCohomologyAlgebraFunctor`](#fun-derhamcohomologyalgebrafunctor) | functor | Functors & Adjunctions |
| [`DeRhamCohomologyFunctor`](#fun-derhamcohomologyfunctor) | functor | Functors & Adjunctions |
| [`DeRhamFunctor`](#fun-derhamfunctor) | functor | Functors & Adjunctions |
| `DecompositionGroupConjugacyClass` | class | Groups, Profinite Groups & Galois Theory |
| [`DegreeZeroDGAFunctor`](#fun-degreezerodgafunctor) | functor | Functors & Adjunctions |
| `DegreewiseLinearMorphism` | morphism | Algebras & Differential Graded Algebras |
| `Derivation` | element | Algebras & Differential Graded Algebras |
| [`DerivationSpace`](#cat-derivationspace) | category | Algebras & Differential Graded Algebras |
| `Derivations` | function | Algebras & Differential Graded Algebras |
| `DeterminantLine` | function | Modules, Complexes & Homological Algebra |
| [`DiagramCategory`](#cat-diagramcategory) | category | Abstract Category Theory & Universal Constructions |
| `Differential` | element | Algebras & Differential Graded Algebras |
| `DifferentialComponentMorphism` | morphism | Algebras & Differential Graded Algebras |
| [`DifferentialGradedAlgebras`](#cat-differentialgradedalgebras) | category | Algebras & Differential Graded Algebras |
| [`DifferentialGradedModules`](#cat-differentialgradedmodules) | category | Modules, Complexes & Homological Algebra |
| [`DirectImageSubobjectFunctor`](#fun-directimagesubobjectfunctor) | functor | Functors & Adjunctions |
| [`DirectSumCategory`](#cat-directsumcategory) | category | Abstract Category Theory & Universal Constructions |
| `DirectSumDecomposition` | function | Abstract Category Theory & Universal Constructions |
| [`DirectSumObjects`](#cat-directsumobjects) | category | Abstract Category Theory & Universal Constructions |
| [`DirectedSystem`](#cat-directedsystem) | category | Abstract Category Theory & Universal Constructions |
| [`DiscreteCategories`](#cat-discretecategories) | category | Abstract Category Theory & Universal Constructions |
| [`DiscreteCategory`](#cat-discretecategory) | category | Abstract Category Theory & Universal Constructions |
| [`DiscreteDiagram`](#fun-discretediagram) | functor | Abstract Category Theory & Universal Constructions |
| [`DiscreteFunctor`](#fun-discretefunctor) | functor | Abstract Category Theory & Universal Constructions |
| [`DiscriminantBilinearModules`](#cat-discriminantbilinearmodules) | category | Modules, Complexes & Homological Algebra |
| `DiscriminantModule` | function | Modules, Complexes & Homological Algebra |
| [`DiscriminantModules`](#cat-discriminantmodules) | category | Modules, Complexes & Homological Algebra |
| [`DiscriminantQuadraticModules`](#cat-discriminantquadraticmodules) | category | Modules, Complexes & Homological Algebra |
| [`DisjointUnionsOfSets`](#cat-disjointunionsofsets) | category | Sets, Cardinals & Ordinals |
| `DistinguishedOpenSubobject` | morphism | Rings, Fields & Commutative Algebra |
| `DividedSquare` | function | Modules, Complexes & Homological Algebra |
| [`DividedSquareModules`](#cat-dividedsquaremodules) | category | Modules, Complexes & Homological Algebra |
| [`DivisionRings`](#cat-divisionrings) | category | Rings, Fields & Commutative Algebra |
| `DivisorGroup` | function | Divisors & Picard Theory |
| [`DivisorGroups`](#cat-divisorgroups) | category | Divisors & Picard Theory |
| [`DomainFunctor`](#fun-domainfunctor) | functor | Abstract Category Theory & Universal Constructions |
| `DualNumbers` | function | Rings, Fields & Commutative Algebra |
| [`DualizationFunctor`](#fun-dualizationfunctor) | functor | Functors & Adjunctions |
| `ElementConjugacyClass` | class | Groups, Profinite Groups & Galois Theory |
| [`Embeddings`](#embeddings) | catalogue | Named Catalogue & Classification Tables |
| [`EndArrowCategory`](#cat-endarrowcategory) | category | Abstract Category Theory & Universal Constructions |
| [`EndCategoryConstruction`](#cat-endcategoryconstruction) | category | Abstract Category Theory & Universal Constructions |
| [`EndCategoryOf`](#cat-endcategoryof) | category | Abstract Category Theory & Universal Constructions |
| [`EnumeratedByIntegers`](#cat-enumeratedbyintegers) | category | Sets, Cardinals & Ordinals |
| [`EnumeratedByNaturals`](#cat-enumeratedbynaturals) | category | Sets, Cardinals & Ordinals |
| [`EnumeratedSets`](#cat-enumeratedsets) | category | Sets, Cardinals & Ordinals |
| [`EpiCategoryConstruction`](#cat-epicategoryconstruction) | category | Abstract Category Theory & Universal Constructions |
| [`EpiCategoryOf`](#cat-epicategoryof) | category | Abstract Category Theory & Universal Constructions |
| [`EpimorphismArrowCategory`](#cat-epimorphismarrowcategory) | category | Abstract Category Theory & Universal Constructions |
| `EquivariantMorphism` | morphism | Groups, Profinite Groups & Galois Theory |
| [`EvenLattices`](#cat-evenlattices) | category | Lattices, Quadratic Forms & Invariants |
| [`ExactFieldHomset`](#cat-exactfieldhomset) | category | Groups, Profinite Groups & Galois Theory |
| `ExactFieldMorphism` | morphism | Groups, Profinite Groups & Galois Theory |
| `ExactRealField` | object | Rings, Fields & Commutative Algebra |
| `ExactRealNumber` | element | Rings, Fields & Commutative Algebra |
| [`ExponentialFunctor`](#fun-exponentialfunctor) | functor | Functors & Adjunctions |
| `ExponentialOfSets` | function | Sets, Cardinals & Ordinals |
| `Ext` | function | Modules, Complexes & Homological Algebra |
| `ExteriorForms` | function | Modules, Complexes & Homological Algebra |
| [`FiberProductSchemes`](#cat-fiberproductschemes) | category | Schemes & Algebraic Geometry |
| [`FiberedFormedModuleHomset`](#cat-fiberedformedmodulehomset) | category | Modules, Complexes & Homological Algebra |
| `FiberedFormedModuleMorphism` | morphism | Modules, Complexes & Homological Algebra |
| [`Fields`](#cat-fields) | category | Rings, Fields & Commutative Algebra |
| `FiniteAbelianGroups` | function | Groups, Profinite Groups & Galois Theory |
| `FiniteElementConjugacyClass` | class | Groups, Profinite Groups & Galois Theory |
| `FiniteField` | function | Rings, Fields & Commutative Algebra |
| [`FiniteGSets`](#cat-finitegsets) | category | Groups, Profinite Groups & Galois Theory |
| `FiniteGaloisAutomorphism` | element | Groups, Profinite Groups & Galois Theory |
| `FiniteGaloisExtension` | class | Groups, Profinite Groups & Galois Theory |
| `FiniteGaloisQuotient` | object | Groups, Profinite Groups & Galois Theory |
| `FiniteGaloisSubgroup` | object | Groups, Profinite Groups & Galois Theory |
| `FiniteGroupClassFunction` | morphism | Groups, Profinite Groups & Galois Theory |
| `FiniteGroups` | function | Groups, Profinite Groups & Galois Theory |
| [`FinitePowerSetFunctor`](#fun-finitepowersetfunctor) | functor | Functors & Adjunctions |
| [`FinitePowerSets`](#cat-finitepowersets) | category | Sets, Cardinals & Ordinals |
| [`FiniteRankLattices`](#cat-finiteranklattices) | category | Lattices, Quadratic Forms & Invariants |
| `FiniteSets` | function | Sets, Cardinals & Ordinals |
| `FiniteSubsets` | function | Sets, Cardinals & Ordinals |
| [`FiniteTypeSchemes`](#cat-finitetypeschemes) | category | Schemes & Algebraic Geometry |
| [`FinitelyGeneratedFormModules`](#cat-finitelygeneratedformmodules) | category | Modules, Complexes & Homological Algebra |
| [`FinitelyGeneratedFreeFormModules`](#cat-finitelygeneratedfreeformmodules) | category | Modules, Complexes & Homological Algebra |
| [`FinitelyGeneratedFreeModules`](#cat-finitelygeneratedfreemodules) | category | Modules, Complexes & Homological Algebra |
| [`FinitelyGeneratedGroups`](#cat-finitelygeneratedgroups) | category | Groups, Profinite Groups & Galois Theory |
| [`FinitelyGeneratedModules`](#cat-finitelygeneratedmodules) | category | Modules, Complexes & Homological Algebra |
| `FinitelyPresentedAlgebra` | function | Algebras & Differential Graded Algebras |
| `FinitelyPresentedAlgebraOn` | function | Algebras & Differential Graded Algebras |
| [`FinitelyPresentedAlgebras`](#cat-finitelypresentedalgebras) | category | Algebras & Differential Graded Algebras |
| [`FinitelyPresentedBilinearFormModules`](#cat-finitelypresentedbilinearformmodules) | category | Modules, Complexes & Homological Algebra |
| [`FinitelyPresentedFormModules`](#cat-finitelypresentedformmodules) | category | Modules, Complexes & Homological Algebra |
| [`FinitelyPresentedGroups`](#cat-finitelypresentedgroups) | category | Groups, Profinite Groups & Galois Theory |
| `FinitelyPresentedModule` | function | Modules, Complexes & Homological Algebra |
| [`FinitelyPresentedModules`](#cat-finitelypresentedmodules) | category | Modules, Complexes & Homological Algebra |
| [`FinitelyPresentedQuadraticFormModules`](#cat-finitelypresentedquadraticformmodules) | category | Modules, Complexes & Homological Algebra |
| [`FinitelyPresentedTorsionModules`](#cat-finitelypresentedtorsionmodules) | category | Modules, Complexes & Homological Algebra |
| [`FinitelySupportedFunctionSets`](#cat-finitelysupportedfunctionsets) | category | Sets, Cardinals & Ordinals |
| [`FixedCardinalitySubsetFunctor`](#fun-fixedcardinalitysubsetfunctor) | functor | Functors & Adjunctions |
| `FormEmbedding` | morphism | Modules, Complexes & Homological Algebra |
| `FormModule` | function | Modules, Complexes & Homological Algebra |
| [`FormModules`](#cat-formmodules) | category | Modules, Complexes & Homological Algebra |
| `FormalDivisor` | function | Divisors & Picard Theory |
| [`FormalDivisorGroups`](#cat-formaldivisorgroups) | category | Divisors & Picard Theory |
| [`FormalPowerSeriesRings`](#cat-formalpowerseriesrings) | category | Rings, Fields & Commutative Algebra |
| [`FormedModuleHomset`](#cat-formedmodulehomset) | category | Modules, Complexes & Homological Algebra |
| `FormedModuleMorphism` | morphism | Modules, Complexes & Homological Algebra |
| [`FormedModules`](#cat-formedmodules) | category | Modules, Complexes & Homological Algebra |
| `FourierCharacters` | object | Sets, Cardinals & Ordinals |
| [`FractionFieldFunctor`](#fun-fractionfieldfunctor) | functor | Functors & Adjunctions |
| `FractionFieldQuotient` | function | Modules, Complexes & Homological Algebra |
| [`FractionFieldQuotients`](#cat-fractionfieldquotients) | category | Modules, Complexes & Homological Algebra |
| `FractionalIdeal` | function | Modules, Complexes & Homological Algebra |
| [`FractionalIdeals`](#cat-fractionalideals) | category | Modules, Complexes & Homological Algebra |
| [`FramedAlgebras`](#cat-framedalgebras) | category | Algebras & Differential Graded Algebras |
| [`FramedFreeModules`](#cat-framedfreemodules) | category | Modules, Complexes & Homological Algebra |
| [`FramedModules`](#cat-framedmodules) | category | Modules, Complexes & Homological Algebra |
| `FramingVolumeTrivialization` | function | Modules, Complexes & Homological Algebra |
| `FreeAlgebraOn` | function | Algebras & Differential Graded Algebras |
| [`FreeAlgebras`](#cat-freealgebras) | category | Algebras & Differential Graded Algebras |
| [`FreeBilinearFormFunctor`](#fun-freebilinearformfunctor) | functor | Functors & Adjunctions |
| [`FreeForgetfulAdjunction`](#fun-freeforgetfuladjunction) | adjunction | Functors & Adjunctions |
| [`FreeFormModules`](#cat-freeformmodules) | category | Modules, Complexes & Homological Algebra |
| [`FreeGroupFunctor`](#fun-freegroupfunctor) | functor | Functors & Adjunctions |
| [`FreeGroupUnderlyingSetAdjunction`](#fun-freegroupunderlyingsetadjunction) | adjunction | Functors & Adjunctions |
| `FreeModule` | function | Modules, Complexes & Homological Algebra |
| [`FreeModuleFunctor`](#fun-freemodulefunctor) | functor | Functors & Adjunctions |
| `FreeModuleOn` | function | Modules, Complexes & Homological Algebra |
| [`FreeModules`](#cat-freemodules) | category | Modules, Complexes & Homological Algebra |
| [`FreeQuadraticFormFunctor`](#fun-freequadraticformfunctor) | functor | Functors & Adjunctions |
| `FreeResolution` | class | Modules, Complexes & Homological Algebra |
| `FrobeniusConjugacyClass` | class | Groups, Profinite Groups & Galois Theory |
| `FrobeniusElement` | element | Groups, Profinite Groups & Galois Theory |
| [`FunctionEnumeratedSets`](#cat-functionenumeratedsets) | category | Sets, Cardinals & Ordinals |
| [`Functor`](#fun-functor) | functor | Functors & Adjunctions |
| [`FunctorCategory`](#cat-functorcategory) | category | Abstract Category Theory & Universal Constructions |
| `GF` | function | Rings, Fields & Commutative Algebra |
| [`GObjectHomset`](#cat-gobjecthomset) | category | Groups, Profinite Groups & Galois Theory |
| [`GObjects`](#cat-gobjects) | category | Groups, Profinite Groups & Galois Theory |
| [`GSetHomset`](#cat-gsethomset) | category | Groups, Profinite Groups & Galois Theory |
| `GSetMorphism` | morphism | Groups, Profinite Groups & Galois Theory |
| `GSets` | function | Groups, Profinite Groups & Galois Theory |
| `GaloisRestrictionMap` | morphism | Groups, Profinite Groups & Galois Theory |
| `GeneralModule` | function | Modules, Complexes & Homological Algebra |
| `GeneralModuleElement` | element | Modules, Complexes & Homological Algebra |
| `GeneralModuleParent` | object | Modules, Complexes & Homological Algebra |
| `Genus` | class | Lattices, Quadratic Forms & Invariants |
| [`GradedAlgebraHomset`](#cat-gradedalgebrahomset) | category | Algebras & Differential Graded Algebras |
| [`GradedAlgebraModules`](#cat-gradedalgebramodules) | category | Modules, Complexes & Homological Algebra |
| `GradedAlgebraMorphism` | morphism | Algebras & Differential Graded Algebras |
| [`GradedAlgebras`](#cat-gradedalgebras) | category | Algebras & Differential Graded Algebras |
| [`GradedAugmentedAlgebras`](#cat-gradedaugmentedalgebras) | category | Algebras & Differential Graded Algebras |
| [`GradedCommutativeAlgebras`](#cat-gradedcommutativealgebras) | category | Algebras & Differential Graded Algebras |
| `GradedCommutator` | function | Algebras & Differential Graded Algebras |
| `GradedDerivation` | element | Algebras & Differential Graded Algebras |
| [`GradedDerivationSpace`](#cat-gradedderivationspace) | category | Algebras & Differential Graded Algebras |
| `GradedDerivations` | function | Algebras & Differential Graded Algebras |
| [`GradedFreeAlgebras`](#cat-gradedfreealgebras) | category | Algebras & Differential Graded Algebras |
| `GradedLebesgueAlgebra` | live object | Function Spaces & Analysis |
| `GradedLebesgueModule` | object | Function Spaces & Analysis |
| [`GradedModules`](#cat-gradedmodules) | category | Modules, Complexes & Homological Algebra |
| [`GradedTensorProductModules`](#cat-gradedtensorproductmodules) | category | Function Spaces & Analysis |
| `GradedTensorSquare` | object | Function Spaces & Analysis |
| `GroupAlgebra` | function | Algebras & Differential Graded Algebras |
| [`GroupAlgebraFunctor`](#fun-groupalgebrafunctor) | functor | Algebras & Differential Graded Algebras |
| [`GroupAlgebras`](#cat-groupalgebras) | category | Algebras & Differential Graded Algebras |
| [`GroupAutomorphismGroup`](#cat-groupautomorphismgroup) | category | Groups, Profinite Groups & Galois Theory |
| [`GroupHomset`](#cat-grouphomset) | category | Groups, Profinite Groups & Galois Theory |
| [`GroupModuleBaseChangeAdjunction`](#fun-groupmodulebasechangeadjunction) | adjunction | Functors & Adjunctions |
| [`GroupModuleHomset`](#cat-groupmodulehomset) | category | Modules, Complexes & Homological Algebra |
| `GroupModuleMorphism` | morphism | Modules, Complexes & Homological Algebra |
| [`GroupModuleRestrictionOfScalarsFunctor`](#fun-groupmodulerestrictionofscalarsfunctor) | functor | Functors & Adjunctions |
| [`GroupModuleScalarExtensionFunctor`](#fun-groupmodulescalarextensionfunctor) | functor | Functors & Adjunctions |
| [`GroupUnderlyingSetFunctor`](#fun-groupunderlyingsetfunctor) | functor | Functors & Adjunctions |
| [`Groups`](#cat-groups) | category | Groups, Profinite Groups & Galois Theory |
| [`GroupsWithChosenFiniteGeneratingSet`](#cat-groupswithchosenfinitegeneratingset) | category | Groups, Profinite Groups & Galois Theory |
| [`GroupsWithChosenFinitePresentation`](#cat-groupswithchosenfinitepresentation) | category | Groups, Profinite Groups & Galois Theory |
| `HermitePolynomials` | object | Sets, Cardinals & Ordinals |
| `HodgeDiscriminant` | function | Modules, Complexes & Homological Algebra |
| `HodgeStar` | function | Modules, Complexes & Homological Algebra |
| `HodgeStarOverFractionField` | function | Modules, Complexes & Homological Algebra |
| [`HomCategories`](#cat-homcategories) | category | Abstract Category Theory & Universal Constructions |
| [`HomCategoryConstruction`](#cat-homcategoryconstruction) | category | Abstract Category Theory & Universal Constructions |
| [`HomCategoryOf`](#cat-homcategoryof) | category | Abstract Category Theory & Universal Constructions |
| [`Ideals`](#cat-ideals) | category | Modules, Complexes & Homological Algebra |
| [`IdentityFunctor`](#fun-identityfunctor) | functor | Functors & Adjunctions |
| `ImageSet` | function | Sets, Cardinals & Ordinals |
| `IndexedFreeGroupHomomorphism` | morphism | Groups, Profinite Groups & Galois Theory |
| [`IndexedFreeGroupHomset`](#cat-indexedfreegrouphomset) | category | Groups, Profinite Groups & Galois Theory |
| [`InducedAutFunctor`](#fun-inducedautfunctor) | functor | Functors & Adjunctions |
| [`InducedEndFunctor`](#fun-inducedendfunctor) | functor | Functors & Adjunctions |
| [`InducedHomFunctor`](#fun-inducedhomfunctor) | functor | Functors & Adjunctions |
| [`InductionFunctor`](#fun-inductionfunctor) | functor | Functors & Adjunctions |
| [`InductionRestrictionAdjunction`](#fun-inductionrestrictionadjunction) | adjunction | Functors & Adjunctions |
| `InertiaGroupConjugacyClass` | class | Groups, Profinite Groups & Galois Theory |
| [`InfiniteEnumeratedSets`](#cat-infiniteenumeratedsets) | category | Sets, Cardinals & Ordinals |
| `InfiniteSets` | function | Sets, Cardinals & Ordinals |
| `Integer` | function | Preamble Entrypoints & Utilities |
| `IntegerModRing` | function | Rings, Fields & Commutative Algebra |
| `Integers` | function | Rings, Fields & Commutative Algebra |
| [`IntegralDomains`](#cat-integraldomains) | category | Rings, Fields & Commutative Algebra |
| [`IntegralSchemes`](#cat-integralschemes) | category | Schemes & Algebraic Geometry |
| `InteriorProduct` | function | Algebras & Differential Graded Algebras |
| `InternalHom` | function | Modules, Complexes & Homological Algebra |
| [`InternalHomFromFunctor`](#fun-internalhomfromfunctor) | functor | Functors & Adjunctions |
| [`InternalHomModules`](#cat-internalhommodules) | category | Modules, Complexes & Homological Algebra |
| [`InvariantsFunctor`](#fun-invariantsfunctor) | functor | Functors & Adjunctions |
| [`InverseImagePowerSetFunctor`](#fun-inverseimagepowersetfunctor) | functor | Functors & Adjunctions |
| [`InverseImageSubobjectFunctor`](#fun-inverseimagesubobjectfunctor) | functor | Functors & Adjunctions |
| [`InverseSystem`](#cat-inversesystem) | category | Abstract Category Theory & Universal Constructions |
| `InvertibleSheaf` | class | Divisors & Picard Theory |
| [`Involutions`](#involutions) | catalogue | Named Catalogue & Classification Tables |
| [`IsoArrowCategory`](#cat-isoarrowcategory) | category | Abstract Category Theory & Universal Constructions |
| [`IsoCategoryConstruction`](#cat-isocategoryconstruction) | category | Abstract Category Theory & Universal Constructions |
| [`IsoCategoryOf`](#cat-isocategoryof) | category | Abstract Category Theory & Universal Constructions |
| `Isomorphism` | function | Abstract Category Theory & Universal Constructions |
| `IsotropicFlag` | class | Abstract Category Theory & Universal Constructions |
| [`KahlerDifferentialModules`](#cat-kahlerdifferentialmodules) | category | Algebras & Differential Graded Algebras |
| `KahlerDifferentials` | function | Algebras & Differential Graded Algebras |
| [`KernelArrowFunctor`](#fun-kernelarrowfunctor) | functor | Functors & Adjunctions |
| `LatticeEmbedding` | morphism | Abstract Category Theory & Universal Constructions |
| [`LatticeHomset`](#cat-latticehomset) | category | Abstract Category Theory & Universal Constructions |
| `LatticeIsometry` | morphism | Abstract Category Theory & Universal Constructions |
| `LatticeMorphism` | morphism | Abstract Category Theory & Universal Constructions |
| `LatticePolygon` | function | Schemes & Algebraic Geometry |
| [`LatticePolygons`](#cat-latticepolygons) | category | Schemes & Algebraic Geometry |
| `LatticePolytope` | function | Schemes & Algebraic Geometry |
| [`LatticePolytopes`](#cat-latticepolytopes) | category | Schemes & Algebraic Geometry |
| [`Lattices`](#cat-lattices) | category | Lattices, Quadratic Forms & Invariants |
| `LaurentMonomials` | object | Sets, Cardinals & Ordinals |
| `LaurentPolynomialRing` | function | Rings, Fields & Commutative Algebra |
| `LebesgueConvolutionAlgebra` | live object | Function Spaces & Analysis |
| [`LebesgueGradedModules`](#cat-lebesguegradedmodules) | category | Function Spaces & Analysis |
| [`LieAlgebras`](#cat-liealgebras) | category | Algebras & Differential Graded Algebras |
| `LieBracket` | function | Algebras & Differential Graded Algebras |
| `LieDerivative` | function | Algebras & Differential Graded Algebras |
| `LiftCoset` | class | Groups, Profinite Groups & Galois Theory |
| [`LimitsOfCategory`](#cat-limitsofcategory) | category | Abstract Category Theory & Universal Constructions |
| [`LinearHomModules`](#cat-linearhommodules) | category | Modules, Complexes & Homological Algebra |
| [`LocalRings`](#cat-localrings) | category | Rings, Fields & Commutative Algebra |
| [`LocalizedModules`](#cat-localizedmodules) | category | Modules, Complexes & Homological Algebra |
| [`LocallyRingedSpaces`](#cat-locallyringedspaces) | category | Schemes & Algebraic Geometry |
| `Lp` | object | Function Spaces & Analysis |
| [`MatrixAlgebras`](#cat-matrixalgebras) | category | Algebras & Differential Graded Algebras |
| [`MatrixEndomorphismSpaces`](#cat-matrixendomorphismspaces) | category | Modules, Complexes & Homological Algebra |
| `MatrixSpace` | function | Rings, Fields & Commutative Algebra |
| [`MatrixSpaces`](#cat-matrixspaces) | category | Modules, Complexes & Homological Algebra |
| `ModuleEmbedding` | morphism | Modules, Complexes & Homological Algebra |
| [`ModuleLocalizationFunctor`](#fun-modulelocalizationfunctor) | functor | Functors & Adjunctions |
| [`ModuleSubobjects`](#cat-modulesubobjects) | category | Modules, Complexes & Homological Algebra |
| `ModuleWithConnection` | function | Modules, Complexes & Homological Algebra |
| [`Modules`](#cat-modules) | category | Modules, Complexes & Homological Algebra |
| [`ModulesWithChosenFinitePresentation`](#cat-moduleswithchosenfinitepresentation) | category | Modules, Complexes & Homological Algebra |
| [`ModulesWithConnection`](#cat-moduleswithconnection) | category | Modules, Complexes & Homological Algebra |
| [`ModulesWithFlatConnection`](#cat-moduleswithflatconnection) | category | Modules, Complexes & Homological Algebra |
| [`MonoCategoryConstruction`](#cat-monocategoryconstruction) | category | Abstract Category Theory & Universal Constructions |
| [`MonoCategoryOf`](#cat-monocategoryof) | category | Abstract Category Theory & Universal Constructions |
| [`MonomorphismArrowCategory`](#cat-monomorphismarrowcategory) | category | Abstract Category Theory & Universal Constructions |
| `MultivectorHodgeStar` | function | Modules, Complexes & Homological Algebra |
| `NN` | live object | Sets, Cardinals & Ordinals |
| [`NamedLattices`](#namedlattices) | catalogue | Named Catalogue & Classification Tables |
| `NaturalTransformation` | class | Functors & Adjunctions |
| `NaturalTransformationMorphism` | morphism | Abstract Category Theory & Universal Constructions |
| `NaturalTransformations` | function | Abstract Category Theory & Universal Constructions |
| [`NoetherianRings`](#cat-noetherianrings) | category | Rings, Fields & Commutative Algebra |
| `NonNegativeReals` | live object | Rings, Fields & Commutative Algebra |
| [`NondegenerateLattices`](#cat-nondegeneratelattices) | category | Lattices, Quadratic Forms & Invariants |
| [`NormalSchemes`](#cat-normalschemes) | category | Schemes & Algebraic Geometry |
| `NumberField` | function | Rings, Fields & Commutative Algebra |
| [`NumberFieldsWithChosenPrimitiveElement`](#cat-numberfieldswithchosenprimitiveelement) | category | Rings, Fields & Commutative Algebra |
| [`ObjectSetFunctor`](#fun-objectsetfunctor) | functor | Abstract Category Theory & Universal Constructions |
| [`ObjectSetsOfDiscreteCategories`](#cat-objectsetsofdiscretecategories) | category | Preamble Entrypoints & Utilities |
| [`OpenAbsoluteGaloisSubgroup`](#cat-openabsolutegaloissubgroup) | category | Groups, Profinite Groups & Galois Theory |
| [`OpenAbsoluteGaloisSubgroups`](#cat-openabsolutegaloissubgroups) | category | Groups, Profinite Groups & Galois Theory |
| `OpenGaloisSubgroupConjugacyClass` | class | Groups, Profinite Groups & Galois Theory |
| [`OpenImmersions`](#cat-openimmersions) | category | Schemes & Algebraic Geometry |
| `OpenSubgroupInclusion` | morphism | Groups, Profinite Groups & Galois Theory |
| `OppositeMorphism` | morphism | Abstract Category Theory & Universal Constructions |
| [`OrbitSets`](#cat-orbitsets) | category | Groups, Profinite Groups & Galois Theory |
| [`OrderNumberFieldAdjunction`](#fun-ordernumberfieldadjunction) | adjunction | Functors & Adjunctions |
| [`OrderedRings`](#cat-orderedrings) | category | Rings, Fields & Commutative Algebra |
| [`OrdinalSemirings`](#cat-ordinalsemirings) | category | Sets, Cardinals & Ordinals |
| `Ordinals` | function | Sets, Cardinals & Ordinals |
| [`OrthogonalDirectSumBifunctor`](#fun-orthogonaldirectsumbifunctor) | functor | Functors & Adjunctions |
| `OwnedAbelianGroups` | function | Groups, Profinite Groups & Galois Theory |
| [`OwnedAlgebras`](#cat-ownedalgebras) | category | Algebras & Differential Graded Algebras |
| [`OwnedCategoryOverBaseRing`](#cat-ownedcategoryoverbasering) | category | Rings, Fields & Commutative Algebra |
| [`OwnedDivisionRings`](#cat-owneddivisionrings) | category | Rings, Fields & Commutative Algebra |
| [`OwnedFields`](#cat-ownedfields) | category | Rings, Fields & Commutative Algebra |
| `OwnedFiniteAbelianGroups` | function | Groups, Profinite Groups & Galois Theory |
| `OwnedFiniteGroups` | function | Groups, Profinite Groups & Galois Theory |
| [`OwnedFinitelyGeneratedGroups`](#cat-ownedfinitelygeneratedgroups) | category | Groups, Profinite Groups & Galois Theory |
| [`OwnedFinitelyPresentedGroups`](#cat-ownedfinitelypresentedgroups) | category | Groups, Profinite Groups & Galois Theory |
| [`OwnedGroups`](#cat-ownedgroups) | category | Groups, Profinite Groups & Galois Theory |
| [`OwnedNumberFields`](#cat-ownednumberfields) | category | Rings, Fields & Commutative Algebra |
| [`OwnedOrders`](#cat-ownedorders) | category | Rings, Fields & Commutative Algebra |
| [`OwnedRings`](#cat-ownedrings) | category | Rings, Fields & Commutative Algebra |
| [`OwnedRngs`](#cat-ownedrngs) | category | Rings, Fields & Commutative Algebra |
| [`OwnedSemirings`](#cat-ownedsemirings) | category | Rings, Fields & Commutative Algebra |
| [`PairedModules`](#cat-pairedmodules) | category | Modules, Complexes & Homological Algebra |
| `PairingMorphism` | morphism | Modules, Complexes & Homological Algebra |
| `Pairings` | function | Bilinear Forms, Quadratic Forms & Pairings |
| [`PartiallyOrderedSets`](#cat-partiallyorderedsets) | category | Sets, Cardinals & Ordinals |
| `PicardGroup` | function | Divisors & Picard Theory |
| [`PicardGroups`](#cat-picardgroups) | category | Divisors & Picard Theory |
| `PoincareDuality` | function | Modules, Complexes & Homological Algebra |
| `PolynomialRing` | function | Rings, Fields & Commutative Algebra |
| `PowerSeriesRing` | function | Rings, Fields & Commutative Algebra |
| `PowerSet` | function | Sets, Cardinals & Ordinals |
| [`PowerSets`](#cat-powersets) | category | Sets, Cardinals & Ordinals |
| `Predicate` | class | Logic & Predicates |
| [`PredicateSubgroups`](#cat-predicatesubgroups) | category | Groups, Profinite Groups & Galois Theory |
| [`PredicateSubrings`](#cat-predicatesubrings) | category | Rings, Fields & Commutative Algebra |
| `PrimeField` | function | Rings, Fields & Commutative Algebra |
| [`PrimeFields`](#cat-primefields) | category | Rings, Fields & Commutative Algebra |
| `PrimeProlongation` | class | Groups, Profinite Groups & Galois Theory |
| [`PrimeSpectra`](#cat-primespectra) | category | Rings, Fields & Commutative Algebra |
| [`PrincipalIdealDomains`](#cat-principalidealdomains) | category | Rings, Fields & Commutative Algebra |
| [`ProductConeCategory`](#cat-productconecategory) | category | Abstract Category Theory & Universal Constructions |
| `ProductMorphism` | morphism | Abstract Category Theory & Universal Constructions |
| [`ProductProjectiveSpaces`](#cat-productprojectivespaces) | category | Schemes & Algebraic Geometry |
| [`ProductSchemes`](#cat-productschemes) | category | Schemes & Algebraic Geometry |
| [`ProductsOfCategory`](#cat-productsofcategory) | category | Abstract Category Theory & Universal Constructions |
| `ProfiniteCharacter` | morphism | Groups, Profinite Groups & Galois Theory |
| [`ProfiniteGroups`](#cat-profinitegroups) | category | Groups, Profinite Groups & Galois Theory |
| [`ProjectiveModules`](#cat-projectivemodules) | category | Modules, Complexes & Homological Algebra |
| [`ProjectiveSchemes`](#cat-projectiveschemes) | category | Schemes & Algebraic Geometry |
| `ProjectiveSpace` | function | Schemes & Algebraic Geometry |
| [`ProjectiveSpaces`](#cat-projectivespaces) | category | Schemes & Algebraic Geometry |
| `QQ` | live object | Rings, Fields & Commutative Algebra |
| `QQbar` | live object | Rings, Fields & Commutative Algebra |
| `Qp` | function | Rings, Fields & Commutative Algebra |
| `QuadraticCharacter` | morphism | Groups, Profinite Groups & Galois Theory |
| `QuadraticField` | function | Rings, Fields & Commutative Algebra |
| `QuadraticForm` | function | Modules, Complexes & Homological Algebra |
| [`QuadraticFormModules`](#cat-quadraticformmodules) | category | Modules, Complexes & Homological Algebra |
| `QuadraticFormMorphism` | morphism | Modules, Complexes & Homological Algebra |
| `QuadraticForms` | function | Bilinear Forms, Quadratic Forms & Pairings |
| [`QuadraticFreeFormAdjunction`](#fun-quadraticfreeformadjunction) | adjunction | Functors & Adjunctions |
| `QuadraticSquare` | function | Modules, Complexes & Homological Algebra |
| [`QuadraticUnderlyingModuleFunctor`](#fun-quadraticunderlyingmodulefunctor) | functor | Functors & Adjunctions |
| [`QuasiAffineSchemes`](#cat-quasiaffineschemes) | category | Schemes & Algebraic Geometry |
| [`QuasiProjectiveSchemes`](#cat-quasiprojectiveschemes) | category | Schemes & Algebraic Geometry |
| `RDF` | live object | Rings, Fields & Commutative Algebra |
| `RR` | live object | Rings, Fields & Commutative Algebra |
| [`RationalLattices`](#cat-rationallattices) | category | Abstract Category Theory & Universal Constructions |
| `RealApproximation` | function | Rings, Fields & Commutative Algebra |
| `RealField` | function | Rings, Fields & Commutative Algebra |
| `RealNumber` | function | Preamble Entrypoints & Utilities |
| `ResidueField` | function | Rings, Fields & Commutative Algebra |
| `RestrictedGradedAlgebra` | object | Algebras & Differential Graded Algebras |
| `RestrictedGradedAlgebraElement` | element | Algebras & Differential Graded Algebras |
| `RestrictedProfiniteCharacter` | morphism | Groups, Profinite Groups & Galois Theory |
| [`RestrictedScalarsAlgebras`](#cat-restrictedscalarsalgebras) | category | Algebras & Differential Graded Algebras |
| `RestrictedScalarsModuleView` | object | Modules, Complexes & Homological Algebra |
| [`RestrictedScalarsModules`](#cat-restrictedscalarsmodules) | category | Modules, Complexes & Homological Algebra |
| [`RestrictionCoextensionAdjunction`](#fun-restrictioncoextensionadjunction) | adjunction | Functors & Adjunctions |
| [`RestrictionCoinductionAdjunction`](#fun-restrictioncoinductionadjunction) | adjunction | Functors & Adjunctions |
| [`RestrictionOfActingGroupFunctor`](#fun-restrictionofactinggroupfunctor) | functor | Functors & Adjunctions |
| [`RestrictionOfScalarsFunctor`](#fun-restrictionofscalarsfunctor) | functor | Functors & Adjunctions |
| [`RingOfIntegersFunctor`](#fun-ringofintegersfunctor) | functor | Functors & Adjunctions |
| [`RingedSpaces`](#cat-ringedspaces) | category | Schemes & Algebraic Geometry |
| [`Rings`](#cat-rings) | category | Rings, Fields & Commutative Algebra |
| [`RootLattices`](#cat-rootlattices) | category | Lattices, Quadratic Forms & Invariants |
| [`ScalarExtensionFunctor`](#fun-scalarextensionfunctor) | functor | Functors & Adjunctions |
| [`SchemeMonomorphisms`](#cat-schememonomorphisms) | category | Schemes & Algebraic Geometry |
| `SchemeMorphism` | morphism | Schemes & Algebraic Geometry |
| `SchemeUnderlyingSpace` | class | Schemes & Algebraic Geometry |
| [`Schemes`](#cat-schemes) | category | Schemes & Algebraic Geometry |
| [`SeparatedSchemes`](#cat-separatedschemes) | category | Schemes & Algebraic Geometry |
| `Set` | function | Sets, Cardinals & Ordinals |
| `SetInclusion` | morphism | Sets, Cardinals & Ordinals |
| `SetInjection` | morphism | Sets, Cardinals & Ordinals |
| `SetSurjection` | morphism | Sets, Cardinals & Ordinals |
| [`Sets`](#cat-sets) | category | Sets, Cardinals & Ordinals |
| `SincTranslates` | object | Sets, Cardinals & Ordinals |
| [`SliceCategory`](#cat-slicecategory) | category | Abstract Category Theory & Universal Constructions |
| [`SmoothSchemes`](#cat-smoothschemes) | category | Schemes & Algebraic Geometry |
| `Spec` | function | Schemes & Algebraic Geometry |
| `SpecFunctor` | function | Schemes & Algebraic Geometry |
| `Sterk` | class | Specialized Geometries (Coble & Sterk) |
| [`StrictlyCommutativeDifferentialGradedAlgebras`](#cat-strictlycommutativedifferentialgradedalgebras) | category | Algebras & Differential Graded Algebras |
| [`StrictlyGradedCommutativeAlgebras`](#cat-strictlygradedcommutativealgebras) | category | Algebras & Differential Graded Algebras |
| `StructureSheaf` | class | Schemes & Algebraic Geometry |
| [`Subgroups`](#cat-subgroups) | category | Groups, Profinite Groups & Galois Theory |
| `Submonoids` | function | Groups, Profinite Groups & Galois Theory |
| [`SubobjectCategory`](#cat-subobjectcategory) | category | Abstract Category Theory & Universal Constructions |
| [`SubobjectHomset`](#cat-subobjecthomset) | category | Abstract Category Theory & Universal Constructions |
| [`SubobjectImageAdjunction`](#fun-subobjectimageadjunction) | adjunction | Functors & Adjunctions |
| `SubobjectMorphism` | morphism | Abstract Category Theory & Universal Constructions |
| `SubsetsOfSize` | function | Sets, Cardinals & Ordinals |
| [`SuperobjectCategory`](#cat-superobjectcategory) | category | Abstract Category Theory & Universal Constructions |
| [`Surfaces`](#cat-surfaces) | category | Schemes & Algebraic Geometry |
| [`SymmetricAlgebraAdjunction`](#fun-symmetricalgebraadjunction) | adjunction | Functors & Adjunctions |
| [`SymmetricAlgebraFunctor`](#fun-symmetricalgebrafunctor) | functor | Functors & Adjunctions |
| `SymmetricAlgebraOf` | function | Algebras & Differential Graded Algebras |
| `SymmetricAlgebraOn` | function | Algebras & Differential Graded Algebras |
| [`SymmetricAlgebras`](#cat-symmetricalgebras) | category | Algebras & Differential Graded Algebras |
| [`SymmetricBilinearFormModules`](#cat-symmetricbilinearformmodules) | category | Modules, Complexes & Homological Algebra |
| `Tensor` | class | Tensor Calculus |
| [`TensorAlgebraAdjunction`](#fun-tensoralgebraadjunction) | adjunction | Functors & Adjunctions |
| [`TensorAlgebraFunctor`](#fun-tensoralgebrafunctor) | functor | Functors & Adjunctions |
| `TensorAlgebraOf` | function | Algebras & Differential Graded Algebras |
| `TensorAlgebraOn` | function | Algebras & Differential Graded Algebras |
| [`TensorAlgebras`](#cat-tensoralgebras) | category | Algebras & Differential Graded Algebras |
| [`TensorByFunctor`](#fun-tensorbyfunctor) | functor | Functors & Adjunctions |
| [`TensorHomAdjunction`](#fun-tensorhomadjunction) | adjunction | Functors & Adjunctions |
| `TensorModule` | object | Tensor Calculus |
| [`TensorProductCategory`](#cat-tensorproductcategory) | category | Abstract Category Theory & Universal Constructions |
| [`TensorProductModules`](#cat-tensorproductmodules) | category | Modules, Complexes & Homological Algebra |
| `Tor` | function | Modules, Complexes & Homological Algebra |
| [`TorsionBilinearFormModules`](#cat-torsionbilinearformmodules) | category | Modules, Complexes & Homological Algebra |
| `TorsionFormIsometry` | morphism | Modules, Complexes & Homological Algebra |
| `TorsionModule` | function | Modules, Complexes & Homological Algebra |
| [`TorsionModules`](#cat-torsionmodules) | category | Modules, Complexes & Homological Algebra |
| [`TorsionQuadraticFormModules`](#cat-torsionquadraticformmodules) | category | Modules, Complexes & Homological Algebra |
| [`Torsors`](#cat-torsors) | category | Groups, Profinite Groups & Galois Theory |
| [`TotallyOrderedSets`](#cat-totallyorderedsets) | category | Sets, Cardinals & Ordinals |
| [`TrivialActionFunctor`](#fun-trivialactionfunctor) | functor | Functors & Adjunctions |
| [`TrivialInvariantsAdjunction`](#fun-trivialinvariantsadjunction) | adjunction | Functors & Adjunctions |
| `TrivialInvertibleSheaf` | function | Divisors & Picard Theory |
| [`UncountableSets`](#cat-uncountablesets) | category | Sets, Cardinals & Ordinals |
| [`UnderlyingSetFunctor`](#fun-underlyingsetfunctor) | functor | Functors & Adjunctions |
| `UnitInterval` | live object | Rings, Fields & Commutative Algebra |
| [`Varieties`](#cat-varieties) | category | Schemes & Algebraic Geometry |
| `VectorFields` | function | Algebras & Differential Graded Algebras |
| `VectorPrimitiveExtension` | class | Abstract Category Theory & Universal Constructions |
| [`VectorSpaces`](#cat-vectorspaces) | category | Modules, Complexes & Homological Algebra |
| `VolumeTrivialization` | function | Modules, Complexes & Homological Algebra |
| `WeilDivisorGroup` | function | Divisors & Picard Theory |
| [`WeilDivisorGroups`](#cat-weildivisorgroups) | category | Divisors & Picard Theory |
| [`WideSubcategory`](#cat-widesubcategory) | category | Abstract Category Theory & Universal Constructions |
| `ZZ` | live object | Rings, Fields & Commutative Algebra |
| `ZariskiClosedSubobject` | morphism | Rings, Fields & Commutative Algebra |
| `Zmod` | function | Rings, Fields & Commutative Algebra |
| `Zp` | function | Rings, Fields & Commutative Algebra |
| `abelianization_adjunction` | function | Functors & Adjunctions |
| `absolute_galois_group_category` | function | Groups, Profinite Groups & Galois Theory |
| `affine_spec_functor` | function | Schemes & Algebraic Geometry |
| `aleph` | function | Sets, Cardinals & Ordinals |
| `aleph0` | live object | Sets, Cardinals & Ordinals |
| `algebra_base_change_adjunction` | function | Functors & Adjunctions |
| `algebra_from_multiplication` | function | Algebras & Differential Graded Algebras |
| `algebra_homset` | function | Algebras & Differential Graded Algebras |
| `algebra_underlying_module_functor` | function | Functors & Adjunctions |
| `alternating_algebra_functor` | function | Functors & Adjunctions |
| `ask` | function | Logic & Predicates |
| `augmented_algebra` | function | Algebras & Differential Graded Algebras |
| `base_change_adjunction` | function | Functors & Adjunctions |
| `bilinear_free_form_adjunction` | function | Functors & Adjunctions |
| `biproduct_morphism` | function | Modules, Complexes & Homological Algebra |
| `cardinal` | function | Sets, Cardinals & Ordinals |
| `cardinality_functor` | function | Functors & Adjunctions |
| `cartesian_product_of` | function | Sets, Cardinals & Ordinals |
| `category_inclusion` | function | Functors & Adjunctions |
| `category_packet` | function | Abstract Category Theory & Universal Constructions |
| `centralizer` | function | Groups, Profinite Groups & Galois Theory |
| `cochain_homset` | function | Modules, Complexes & Homological Algebra |
| `cochain_underlying_graded_module_functor` | function | Functors & Adjunctions |
| `cohomology_algebra_functor` | function | Functors & Adjunctions |
| `cohomology_algebra_homset` | function | Algebras & Differential Graded Algebras |
| `cohomology_functor` | function | Functors & Adjunctions |
| `common_category` | function | Abstract Category Theory & Universal Constructions |
| `commutative_algebra_coproduct` | function | Algebras & Differential Graded Algebras |
| `commutative_algebra_pushout` | function | Algebras & Differential Graded Algebras |
| `compose_adjunctions` | function | Functors & Adjunctions |
| `compose_functors` | function | Abstract Category Theory & Universal Constructions |
| `connection_homset` | function | Modules, Complexes & Homological Algebra |
| `continuous_group_homset` | function | Groups, Profinite Groups & Galois Theory |
| `continuum` | live object | Sets, Cardinals & Ordinals |
| `coproduct_cocone_category` | function | Abstract Category Theory & Universal Constructions |
| `cyclic_subgroup` | function | Groups, Profinite Groups & Galois Theory |
| `de_rham_adjunction` | function | Functors & Adjunctions |
| `de_rham_cohomology_algebra_functor` | function | Functors & Adjunctions |
| `de_rham_cohomology_functor` | function | Functors & Adjunctions |
| `de_rham_functor` | function | Functors & Adjunctions |
| `definite_complement_extensions` | function | Abstract Category Theory & Universal Constructions |
| `degree_zero_dga_functor` | function | Functors & Adjunctions |
| `dga_homset` | function | Algebras & Differential Graded Algebras |
| `diagonal_gram` | function | Abstract Category Theory & Universal Constructions |
| `divided_square_morphism` | function | Modules, Complexes & Homological Algebra |
| `ell` | function | Function Spaces & Analysis |
| `ellipsis_iter` | function | Preamble Entrypoints & Utilities |
| `ellipsis_range` | function | Preamble Entrypoints & Utilities |
| `exact_embeddings` | function | Groups, Profinite Groups & Galois Theory |
| `exact_field_homset` | function | Groups, Profinite Groups & Galois Theory |
| `exponential_functor` | function | Functors & Adjunctions |
| `extensions_along` | function | Groups, Profinite Groups & Galois Theory |
| `factorial` | function | Preamble Entrypoints & Utilities |
| `fibered_formed_module_homset` | function | Modules, Complexes & Homological Algebra |
| `field_generators` | function | Groups, Profinite Groups & Galois Theory |
| `finite_decomposition_group` | function | Groups, Profinite Groups & Galois Theory |
| `finite_frobenius_class` | function | Groups, Profinite Groups & Galois Theory |
| `finite_g_set` | function | Groups, Profinite Groups & Galois Theory |
| `finite_inertia_group` | function | Groups, Profinite Groups & Galois Theory |
| `finite_power_set_functor` | function | Functors & Adjunctions |
| `first_exact_embedding` | function | Groups, Profinite Groups & Galois Theory |
| `fixed_cardinality_subset_functor` | function | Functors & Adjunctions |
| `fixed_point_set` | function | Groups, Profinite Groups & Galois Theory |
| `form_embedding` | function | Modules, Complexes & Homological Algebra |
| `formed_module_homset` | function | Modules, Complexes & Homological Algebra |
| `free_forgetful_adjunction` | function | Functors & Adjunctions |
| `free_group_underlying_set_adjunction` | function | Functors & Adjunctions |
| `free_resolution` | function | Modules, Complexes & Homological Algebra |
| `g_set_homset` | function | Groups, Profinite Groups & Galois Theory |
| `generated_submonoid` | function | Groups, Profinite Groups & Galois Theory |
| `gluing_route_discriminant_classes` | function | Abstract Category Theory & Universal Constructions |
| `graded_algebra_homset` | function | Algebras & Differential Graded Algebras |
| `graded_lebesgue_algebra` | function | Function Spaces & Analysis |
| `gram_tensor_from_graph` | function | Bilinear Forms, Quadratic Forms & Pairings |
| `gram_tensor_graph` | function | Bilinear Forms, Quadratic Forms & Pairings |
| `group_homset` | function | Groups, Profinite Groups & Galois Theory |
| `group_module_base_change_adjunction` | function | Functors & Adjunctions |
| [`groups`](#cat-groups) | category | Groups, Profinite Groups & Galois Theory |
| `induced_aut_functor` | function | Functors & Adjunctions |
| `induced_end_functor` | function | Functors & Adjunctions |
| `induced_hom_functor` | function | Functors & Adjunctions |
| `internal_hom_morphism` | function | Modules, Complexes & Homological Algebra |
| `inverse_image_power_set_functor` | function | Functors & Adjunctions |
| `lebesgue_convolution_algebra` | function | Function Spaces & Analysis |
| `lmap` | function | Preamble Entrypoints & Utilities |
| `load` | function | Preamble Entrypoints & Utilities |
| `lzip` | function | Preamble Entrypoints & Utilities |
| `matrix` | function | Preamble Entrypoints & Utilities |
| `module_embedding` | function | Modules, Complexes & Homological Algebra |
| `module_from_action` | function | Modules, Complexes & Homological Algebra |
| `module_homset` | function | Modules, Complexes & Homological Algebra |
| `module_localization_functor` | function | Functors & Adjunctions |
| `nikulin_invariants` | function | Lattices, Quadratic Forms & Invariants |
| `omega` | function | Sets, Cardinals & Ordinals |
| `open_absolute_galois_subgroup` | function | Groups, Profinite Groups & Galois Theory |
| `order_number_field_adjunction` | function | Functors & Adjunctions |
| `ordinal` | function | Sets, Cardinals & Ordinals |
| `own_algebra` | function | Algebras & Differential Graded Algebras |
| `predicate_subgroup` | function | Groups, Profinite Groups & Galois Theory |
| `predicate_submonoid` | function | Groups, Profinite Groups & Galois Theory |
| `predicate_subring` | function | Rings, Fields & Commutative Algebra |
| `product_cone_category` | function | Abstract Category Theory & Universal Constructions |
| `quadratic_free_form_adjunction` | function | Functors & Adjunctions |
| `regular_dg_module` | function | Modules, Complexes & Homological Algebra |
| `restrict_algebra_scalars` | function | Algebras & Differential Graded Algebras |
| `restrict_along` | function | Groups, Profinite Groups & Galois Theory |
| `restrict_graded_algebra_scalars` | function | Algebras & Differential Graded Algebras |
| `restrict_scalars` | function | Modules, Complexes & Homological Algebra |
| `restriction_coextension_adjunction` | function | Functors & Adjunctions |
| `ring_as_module` | function | Modules, Complexes & Homological Algebra |
| `scheme_fiber_product` | function | Schemes & Algebraic Geometry |
| `scheme_product` | function | Schemes & Algebraic Geometry |
| `set_injection` | function | Sets, Cardinals & Ordinals |
| `set_surjection` | function | Sets, Cardinals & Ordinals |
| `signature_orthogonal_sums` | function | Named Catalogue & Classification Tables |
| `signature_pair` | function | Abstract Category Theory & Universal Constructions |
| `signature_pairs` | function | Abstract Category Theory & Universal Constructions |
| `subobject_image_adjunction` | function | Functors & Adjunctions |
| `symbolic_expression` | function | Preamble Entrypoints & Utilities |
| `symmetric_algebra_adjunction` | function | Functors & Adjunctions |
| `symmetric_algebra_functor` | function | Functors & Adjunctions |
| `tensor` | function | Tensor Calculus |
| `tensor_algebra_adjunction` | function | Functors & Adjunctions |
| `tensor_algebra_functor` | function | Functors & Adjunctions |
| `tensor_connected_component_cuts` | function | Bilinear Forms, Quadratic Forms & Pairings |
| `tensor_hom_adjunction` | function | Functors & Adjunctions |
| `tensor_product_morphism` | function | Modules, Complexes & Homological Algebra |
| `to_var_names` | function | Preamble Entrypoints & Utilities |
| `trivial_g_set` | function | Groups, Profinite Groups & Galois Theory |
| `twist_scalar_action` | function | Modules, Complexes & Homological Algebra |
| `two_elementary_orthogonal_sums` | function | Named Catalogue & Classification Tables |
| `validate_negative_def_two_elementary_table` | function | Named Catalogue & Classification Tables |
| `validate_two_elementary_table` | function | Named Catalogue & Classification Tables |
| `var` | function | Preamble Entrypoints & Utilities |
| `zipsum` | function | Preamble Entrypoints & Utilities |
