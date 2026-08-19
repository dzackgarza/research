# Stable homotopy theory over modules with a bilinear form

Fifteen documents, absorbed on 2026-08-20 from the Coxeter research corpus
(`research/explorations/connections/homotopy_theory/` and
`research/explorations/implementation-notes/homotopy-theory/`) under
PLAN-coxeter-deletion-audit-registry, reader H.
Each file keeps its own origin header, its preamble status, and the errors
recorded against it.
Nothing here is implemented in the preamble; this is a design corpus for a
research program, preserved as such.

## What the program proposes

Let $R$ be a commutative ring, $M$ an $R$-module, and $b: M \times M \to R$
a bilinear form.
The corpus writes $\mathrm{Bil}_R\text{-}\mathrm{Mod}$ for the category whose
objects are such pairs $(M, b)$ and whose morphisms are the maps preserving
the form.
It then proposes to transplant stable homotopy theory onto that category:

- a suspension endofunctor given by orthogonal sum with the hyperbolic plane;
- prespectra and the stabilization $\mathrm{Sp}(\mathrm{Bil}_R\text{-}\mathrm{Mod})$
  as the colimit of the suspension tower;
- a projective model structure on chain complexes, with cofibrant replacement
  by hyperbolic cells standing in for the free objects the category lacks;
- the Dold-Kan correspondence, giving simplicial methods;
- $\mathrm{Ext}$ and $\mathrm{Tor}$ computed by a bar-type construction with
  hyperbolic planes, with the form tracked through the computation;
- above all of that: ring spectra, $K$-theory, $L$-theory, $THH$, $TC$, the
  Dennis trace, Adams and Atiyah-Hirzebruch spectral sequences, $t$-structures
  and Bridgeland stability.

## The obstruction the corpus met and did not name

Every construction above needs additive homsets: a chain complex needs
$d^2 = 0$, normalization needs an intersection of kernels, a bar differential
needs an alternating sum, a triangulated structure needs a zero object, and
$\mathrm{Ext}$ needs a category in which short exact sequences make sense.

With form-preserving morphisms, $\mathrm{Hom}((M,b),(N,c))$ carries no addition.
If $f$ and $g$ both preserve the form then $f+g$ does not, and the zero map is
form-preserving only when $b$ is zero.
So the homsets are not groups, the category is not additive, and none of
$\mathrm{Ch}$, Dold-Kan, the projective model structure, the $t$-structure with
heart $\mathrm{Bil}_R\text{-}\mathrm{Mod}$, or $\mathrm{Ext}$ is defined as
written.
The corpus meets this obstruction empirically in
`program/computations/worked_example_ext.md`, where every form-preserving Hom
space in the complex is computed to vanish; the document reads that vanishing
as a defect in its own arithmetic and repairs it by substituting the classical
$\mathrm{Ext}$ of $\mathbb{Z}$-modules, which is the recorded error on that file.

A second, independent claim fails on its own terms.
`program/model-structures/bilr_mod_model_structure.md` asserts that every
object becomes free after enough suspensions, because suspension keeps adding
hyperbolic planes.
Over $\mathbb{Z}$ that is false: orthogonal sum with a hyperbolic plane leaves
the discriminant form unchanged up to isometry, so a lattice with nonzero
discriminant form is never hyperbolic after any number of suspensions.

## What survives, and where it already lives

The surviving kernel is not new mathematics but classical mathematics the
corpus was rediscovering.
Stabilization by hyperbolic planes, applied to forms over a ring, is the
construction of the Witt and Grothendieck-Witt groups; the reason it does not
trivialize everything is precisely that the Witt class is the invariant that
survives it.
Carried into homotopy theory, this is $L$-theory: Wall's surgery obstruction
groups and Ranicki's algebraic theory of surgery, together with Karoubi's
hermitian $K$-theory.
Those theories are all built on the *additive* category of $R$-modules,
with the form handled by a hyperbolic functor $\mathrm{Mod}_R \to
\mathrm{Bil}_R\text{-}\mathrm{Mod}$ and a forgetful functor back — exactly the
adjunction pattern that keeps the homological machinery on the side where it
is defined.
Any future version of this program should start there, and treat the
form-preserving category as the target of functors rather than as the place
where complexes and spectra are built.

None of the standard references were checked out while writing this note, so
no citation keys are recorded; the four bodies of work are named above by
author so a reader can resolve them against the library before use.

## Preamble coverage

Owned, and relevant:

| notion | owner |
| --- | --- |
| modules with a bilinear or quadratic form, with element-level evaluation | `src/dzack_research/preamble/categories/modules/framed/formed/form_modules.sage` |
| homsets and morphisms of formed modules as first-class parents | `form_modules.sage` (`FormHomset`, `FormMorphism`) |
| isometries and inclusions of integral lattices | `categories/modules/framed/formed/integrallattice/lattice_isometries.sage`, `lattice_homomorphisms.sage`, `subobjects.sage` |
| the hyperbolic plane as a named specimen | `catalogue.sage` (`Lattices.U`, `Lattices.H`) |
| orthogonal sum, and direct sums as objects | `catalogue.sage` (`direct_sum`), `categories/abstract_categories/direct_sum_objects.sage` |
| free-forgetful and base-change adjunctions as functor objects | `categories/functors/free_forgetful_adjunction.sage`, `base_change_adjunction.sage` |

Absent, and needed before any of this corpus can be built: chain complexes and
their homology, simplicial objects, spectra, and a settled answer to which
category the homological machinery is to run over.

## File map

| file | content |
| --- | --- |
| `program/README.md` | program overview: stabilize by hyperbolic suspension, recover Ext and Tor as homotopy groups |
| `program/suspension/suspension_functor.md` | the suspension endofunctor, prespectra, stabilization, the stable category interface |
| `program/spectra/bilinear_module_spectra.md` | spectrum objects, wedge, smash, function spectra, homotopy groups, Adams and chromatic filtrations, K-theory, L-theory, THH |
| `program/infinity-categories/bilinear_infinity_category.md` | mapping spaces, homotopy limits, presentability, monoidal structure, model presentation, t-structures, Bridgeland stability |
| `program/model-structures/bilr_mod_model_structure.md` | projective model structure sketch; cofibrant replacement by hyperbolic cells as a substitute for freeness |
| `program/dold-kan/dold_kan_bilinear.md` | normalization and denormalization, simplicial formed modules, Kan complexes, bar resolution, Eilenberg-MacLane objects |
| `program/computations/derived_functor_computations.md` | bar-type construction with hyperbolic planes; Ext and Tor with the form tracked; periodicity and Kunneth shortcuts |
| `program/computations/worked_example_ext.md` | the one fully worked computation; its vanishing Hom spaces are the corpus's own evidence for the obstruction above |
| `implementation-notes/functors.md` | suspension and loop functors, K-theory, THH, Dennis trace, smash and internal hom, base change, Dold-Kan; plus an unrelated root-system test block |
| `implementation-notes/stable-category/sp_bilr_mod.md` | the stable category: symmetric monoidal structure, triangulated structure, spectral enrichment, limits, homotopy and homology |
| `implementation-notes/stable-category/sp_bilr_mod_objects.md` | suspension spectra, Eilenberg-MacLane spectra, the sphere spectrum, K-theory spectra, finite spectra |
| `implementation-notes/stable-category/sp_bilr_mod_morphisms.md` | level maps, suspension maps, structure maps, mapping spectra, stable homotopy classes |
| `implementation-notes/ring-spectra/ring_spectra_category.md` | E-infinity and A-infinity ring spectra, matrix ring spectra, module spectra, K-theory of a ring spectrum |
| `implementation-notes/ring-spectra/ring_spectrum_objects.md` | sphere and Eilenberg-MacLane ring spectra, group ring spectra, THH and K-theory spectra, localization |
| `implementation-notes/ring-spectra/ring_spectrum_morphisms.md` | ring maps, localization and completion, inclusions and quotients, base change, transfers, induced K-theory and THH maps |
