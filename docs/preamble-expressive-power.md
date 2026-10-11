# Preamble expressive power: objects, maps and compositions

The main weakness is incomplete composition between represented mathematical
objects. Many natural operations have names and some computational cases, but
their outputs do not always carry the structure needed by the next operation.

The general capabilities that need work are:

- Explicit group morphisms from chosen generators, with evaluation and descent
  through the defining relations.
- Images, inverse images, kernels and chosen preimages of those morphisms,
  across the supported group representations.
- Stabilizer subgroups of represented actions, with generating descriptions
  in cases where these can be computed.
- Products, equalizers and pullbacks with their universal maps.
- Class sets of groupoids, with class projections and selected representatives.
- Explicit isomorphisms and automorphism-group generators for represented
  mathematical objects.

These are operations at their general mathematical owners. A composite of
them inherits their meaning and computational limitations.

## Scope and evidence

This assessment is dated 2026-10-11. It inspects the research source based on
`050e51ab7e`, the local `lean-categories` checkout at `29ff4ad`, and the
local `sage-indefinite-port` checkout at `993029f`. It is a source audit;
execution and mathematical completeness of algorithms are unverified.

Mathematical meaning belongs to `lean-categories`. The preamble presents
that meaning. Computational realizations supply answers under the evidence
model in [INTENT.md](../INTENT.md).

This is a bounded survey of the group, action, category, set and lattice
owners. It establishes specific weaknesses below, rather than a completeness
claim about every mathematical domain in the preamble.

## Primitive operations and current coverage

Paths below are relative to `src/dzack_research/preamble/categories/`.

| General capability | Present source | Expressive or compositional boundary |
| --- | --- | --- |
| Groups with selected generators and a free-group augmentation | `group/groups.py:779-831,3235` | A selected epimorphism does not by itself supply relations or an algorithm to express an arbitrary group element as a word. |
| Explicit group morphisms, including generator images | `group/groups.py:2049-2128,2495` | Generator evaluation and relation validation use a private GAP presentation. An elementwise morphism can be evaluated but does not automatically acquire the same image and preimage operations. |
| Images, inverse images and kernels | `group/groups.py:2248-2299,4509`; `group/predicate_subgroups.py:544` | Inverse images and kernels can be represented by predicates. Computing generators or chosen preimages requires additional data; the computational routes are not uniform across the morphism representations. |
| Finite images with chosen preimages | `group/groups.py:3479-3563` | The algorithm uses source generators and an evaluable morphism, but returns a Python dictionary rather than the image subgroup, factorization and a selected section. |
| Represented group actions and restriction or transport of actions | `group/g_objects.py:795,911,925,1143` | The general functorial language exists. Its use still depends on the underlying construction supplying its action on morphisms. |
| Stabilizer subgroups | `group/g_objects.py:1115`; `group/predicate_subgroups.py:660` | The general action gives a predicate subgroup. A generating description is a separate operation, with finite and finite-index cases available through other routes. |
| Finite orbit sets and representatives | `group/g_sets.py:263,292`; `group/g_objects.py:1077,1097` | Finite actions can use generators of an infinite acting group. This capability is present; effective stabilizer generators do not follow merely from having orbit labels. |
| Products, equalizers and pullbacks of groups | `abstract_categories/cat.py:638,840`; `group/groups.py:2997` | The group product implementation accepts nonempty finite families of finite groups. The inspected group owners supply no equalizer realization. The general fiber-product method returns an equalizer rather than a selected pullback cone. |
| Category cores and class sets | `abstract_categories/arrow_categories.py:2035`; `lattices.py:1309,776` | Core is present. A general class projection and representative section were not established in the inspected category owners. Specialized finite partitions and representative lists do not supply those maps for an entire groupoid. |
| Explicit isomorphisms and automorphism groups | `lattices.py:2110,2726,2735`; `lattice_morphisms.py:2201,2505` | The lattice interfaces exist. General indefinite isometry witnesses and automorphism-group generators import a module absent from the inspected local port source. |
| Module kernels, images, quotients and intersections | `modules/module_morphisms/module_morphisms.py:1020,1204,1939,1964`; `modules/pure/modules.py:3105` | Inclusions and quotient projections are present. The intersection composes a biproduct, a kernel and an image. The inspected image route requires a finite selected generating set. |
| Genera, class enumeration and class numbers | `lattices.py:1350,3033,776,796,868` | Source algorithms exist. The presentation of a genus, its class set and the maps between them is incomplete; formal classification and finiteness coverage also has limits. |

## Where the language and computation fail to compose

### Explicit group morphisms are not uniformly effective

A finite generating set, a presentation, and an algorithm for lifting an
element to a generator word are distinct data. The public language needs to
retain each when supplied. A map on generators descends to a group morphism
only when the source relations are respected.

`GroupMorphism` accepts generator images, an elementwise rule, or a GAP map.
Its generator-word evaluator uses a private generating epimorphism and
`PreImagesRepresentative` (`groups.py:2088-2128`). Its ordinary
`image()` and element-preimage route instead call
`_gap_morphism_crossing()` (`:2167,2248,2291`), which requires generator
images or an existing GAP realization. An evaluable elementwise morphism
therefore need not support the same operations.

There is a stronger computational case already available:
`finite_image_lifts` can compute a finite image from source generators and
evaluation alone. The ordinary image operation does not use that route.

**Required general improvement:** let the image operation use the
mathematical data available on the morphism and its endpoints. Retain the
image inclusion, the factorization through the image, and a selected
preimage operation where computable. A caller should not have to rebuild
the image because it constructed the same mathematical map in another
supported form.

### Computed finite images lack composable result maps

`finite_image_lifts` returns a dictionary of image elements and source
witnesses. It contains enough data for its present consumers, including the
finite-index Schreier method, but it exposes no image subgroup or
factorization as part of its result.

For a morphism `f: G -> H`, the structural output is an image subgroup
`I -> H` and a surjection `G -> I`. A choice of preimages is a set map
`I -> G`; it need not be a group homomorphism. These maps allow subgroup
images, inverse images, action restriction and subsequent compositions to
use one result.

**Required general improvement:** present the computed image and choices
through these existing mathematical constructions. The dictionary is
computation data, not the public image object.

### Stabilizers exist, but generating descriptions do not propagate

A represented action supplies the stabilizer of a point. The preamble's
general stabilizer method constructs that subgroup by its defining
predicate and retains the point. This is genuine expressive coverage.

For finite actions, the permutation action and its stabilizers can be
computed. For represented finite-index subgroups, Schreier methods can
compute generators from ambient generators and coset data. The inspected
general stabilizer method does not connect these cases into a generating
description of its returned subgroup. A caller must assemble the extra
maps and computations.

**Required general improvement:** compute generators at the subgroup owner
when its retained action, index or presentation supports that computation.
The result remains the same subgroup with its inclusion.

Finite generation of an ambient group does not imply finite generation of
every subgroup. Nor does it make arbitrary word, membership or stabilizer
problems decidable. The representation must state which computations its
data support. Unsupported computation does not change the mathematical
definition of the subgroup.

### Group limits are incomplete as constructions

`Cat.fiber_product` expresses a pullback through a product and an equalizer.
The inspected group product route supports only finite groups and rejects
an empty family. The inspected group files supply no equalizer realization.

There is also a structural boundary at the general owner: the method returns
the equalizer result. It does not return a selected pullback with both legs
and the universal factorization operation, although selected product and
equalizer interfaces exist separately.

**Required general improvement:** supply products and equalizers on the
supported group representations and expose the resulting pullback cone.
A predicate-defined subgroup of a product can express the pullback before
a generating algorithm is available. The universal maps belong to its
construction, not to later caller code.

The existing `pullbacks-in-every-category` node owns this work.

### Class sets need a general quotient interface

For a groupoid `C`, its class set is the quotient of its objects by
isomorphism. The class projection and a selected representative section are
separate maps. A chosen representative is not itself an equivalence class;
a chosen isomorphism between representatives is additional data.

The category core implementation retains the objects and invertible arrows.
The inspected category owners did not establish a general operation
presenting the component quotient with these maps. The lattice owner has a
finite-family isometry partition and a genus representative enumeration.
The genus facade also accepts arbitrary lattices of the genus, while its
iteration yields selected representatives. This leaves membership in a
genus and membership in its class set without separate public projections.

**Required general improvement:** present class sets through the general
quotient construction, with their projections and selected representatives.
Enumeration and class numbers then operate on that set. The relevant
finiteness hypotheses and isomorphism decision procedures remain explicit.

`lean-categories` already defines `GenusCat`, `genusClassSet`,
`GenusClass` and `classNumber` in `LocalGlobal.lean:244` and
`Mass.lean:92-104`. The local `Mass.lean:111` and
`ReducedBasis.lean:458` establish positive-definite genus finiteness.
Further formal classification and finiteness coverage belongs to the
existing `genera-present-their-formalization` node.

### Module images have a finite-generation boundary

The module owner demonstrates useful composition: its intersection method
constructs a difference map on a biproduct, takes its kernel, composes the
inclusions and takes the image. It uses mathematical objects and maps
throughout (`modules/pure/modules.py:3105`).

The inspected `ModuleMorphism.image` route requires the domain's selected
generating set to be finite (`module_morphisms.py:1204`). This is an algorithm
for an image, not a hypothesis in the definition of an image. That route
cannot present images of maps with infinite selected generating sets, even
when another representation could describe the image.

**Required general improvement:** retain images as subobjects at their full
formal domain, and route computation through the represented map and its
endpoints. A finite spanning algorithm is one computational case. This is the
same distinction needed for group images and predicate subgroups.

### Isomorphism witnesses and automorphism generators have limited coverage

The existence of an isomorphism, a decision of isomorphism, and a selected
isomorphism are distinct operations. Likewise, an automorphism group exists
as a mathematical object before a generating family has been computed.

The lattice owner has public isometry and automorphism interfaces. Its
general indefinite witness and generator branches import
`sage_indefinite_port.indefinite.recursive`. That module is absent from
the inspected local port `src/` tree. This is an observed computational
coverage gap at the existing owners.

**Required general improvement:** supply effective isomorphism witnesses
and automorphism-group generating data for the advertised representations.
These outputs must feed the general morphism, subgroup and action operations.
More interfaces with specialized names would not repair this boundary.

## Composites supported by the existing language

Finite double cosets can be expressed as orbits of the left and right
action of `H x K` on a group or a stable subset:
`(h,k).g = h g k^-1`. Finite group products and finite action orbit sets
already support this composition. GAP also supplies
[DoubleCosets](https://gap-system.github.io/gap/doc/ref/chap39_mj.html).

Similarly, the image of a stabilizer is a composition of a subgroup
inclusion and an image operation. A subgroup inverse image is a pullback
along its inclusion. Restriction of an action is precomposition with a
group morphism; transport of an action is postcomposition with a functor.
The latter two already have general owners in `GObjects`.

These expressions test whether the primitives return compatible objects
and maps. Their usefulness depends on the boundaries identified above.

## Assessment

The inspected preamble has substantial vocabulary and several effective
algorithms. The strongest observed weaknesses are:

- Different representations of a group morphism do not receive uniform
  image and preimage operations.
- Computed images and chosen lifts do not consistently return their
  mathematical objects and maps.
- Stabilizer predicates do not generally connect to available generator
  computations.
- Group products, equalizers and pullbacks have incomplete representation
  coverage and incomplete universal-map output.
- Class enumeration is not consistently presented through a class quotient
  and its maps.
- The inspected module image route requires finite selected generators,
  rather than presenting the image independently of that algorithm.
- Explicit isometry witnesses and automorphism generators have an unmet
  indefinite computation dependency.

The next work belongs to these general owners. Its acceptance should concern
the primitives and their compositions across representations, using
independent mathematical assertions.
