# Lattice Interface Complete Redesign Plan

This file is the execution plan for the complete lattice redesign. It
supersedes the earlier lightweight plan draft.

## Overview

Current state is not acceptable because the public lattice layer still carries
wrong semantics from an ambient embedded-module model, stale naming, thin
wrapper helpers, and incomplete morphism/group structure. The target state is a
clean semantic hierarchy of public nouns whose implementations delegate exact
computation to Sage and the existing backend code without leaking backend
concepts into the public API.

This is a complete redesign of the lattice interface, not a compatibility
cleanup. The current generated code is retained only as migration source
material. Any concept rejected in the canonical specs must be excised rather
than preserved behind shims or transitional wrappers.

## Canonical Sources

- `theory/spec_backups/lattices_written_spec_backup.py`
- `theory/lattice_redesign_corrections_spec.md`

These two files are the source of truth for architecture, naming, and semantic
requirements. Existing tests, current implementation details, and temporary
adapter code are not source-of-truth artifacts.

## Constraints

- No compatibility shims.
- No legacy import aliases beyond the final intended public export surface.
- No public `native` terminology.
- No public `to_sage`, `from_sage`, or equivalent Sage-object extraction or
  admission on the final public surface.
- No ambient embedding state on public lattice/module nouns.
- No helper wrappers for trivial one-line Sage operations.
- No new public methods that merely expose Sage-native semantics rejected by the
  specs.
- No `raise`, `try` / `except`, or `None`-sentinel control flow in final
  mathematical APIs.
- No hand-rolled public validation in constructors or conversion entry points;
  public-boundary validation must live in pydantic models.
- No optional arguments or optional public field types in the final API unless
  the user explicitly approves them.
- No `Any`, `object`, or similarly broad public type annotations.
- No manual matrix-equation checks duplicated across call sites when semantic
  containment on the relevant noun should own that check.
- No internal renaming of semantically obvious canonical objects.
- No further redesign work should add features to the current flat files except
  insofar as they are being migrated or deleted.
- Existing generated code must be migrated and reused where mathematically sound
  rather than discarded wholesale.
- General verbs must live on the highest semantically valid noun; do not push
  broadly meaningful operations down into lattice-only subclasses when they make
  sense for `BilinearModule`, its morphisms, or its hom spaces.
- Morphisms are hom-space elements, not containers or ambient subobjects.

## Preconditions

- The two canonical spec files above remain readable and tracked.
- The current generated lattice code remains available as extraction source
  until its logic has been migrated into the target hierarchy.
- Pydantic is the required public-boundary validation layer for constructor and
  coercion inputs.
- Mathematical preconditions inside proved algorithms remain assertions; object
  shape validation does not.
- The final public nouns must provide the standard method surface required by
  `CONTRIBUTING.md`: `__hash__`, `__repr__`, correct `__eq__`, and LaTeX
  printing hooks.

## Scope

In scope:

- Replacing the current lattice public API hierarchy.
- Replacing the current file layout with a real subdirectory hierarchy.
- Rebuilding morphisms, homspaces, dual/discriminant semantics, and orthogonal
  group semantics to match the written specs.
- Moving backend delegation behind the new semantic layer.
- Deleting rejected concepts and stale names from the public surface.

Out of scope during the redesign:

- Preserving the old API shape merely to keep stale tests passing.
- Expanding unrelated mathematical features.
- Full-suite stabilization before the new hierarchy is in place.

## Current Plan

This section is the active execution spec. It removes design freedom by fixing
the noun inventory and receiver placement before implementation begins. The
stages below exist to realize this inventory in dependency order, not to decide
it on the fly.

Throughout Stages 0-6, the spec files are read-only source material. Any
implementation/spec mismatch discovered during those stages must be recorded as
a Stage 7 review item rather than resolved by editing the spec.

### Stage entry packet for every stage

Before starting any stage:

- re-read `CONTRIBUTING.md`;
- re-read `theory/lattice_redesign_corrections_spec.md`;
- re-read the relevant block of
  `theory/spec_backups/lattices_written_spec_backup.py`;
- read the current contents of only the files named in the stage;
- record any newly discovered spec mismatch as a deferred Stage 7 review item;
- route executable verification through the repo `justfile`.

### Literal class inventory

Foundational scalar/codomain/module layer:

- `QuotientRing`
- `LocalizedRing`
- `CompletedRing`
- `FormCodomain`
- `QuotientFormCodomain`
- `FGPModuleWrapper`
- `Module`
- `ModuleElement`
- `FreeModule`
- `TorsionModule`
- `MixedModule`
- `ModuleHomSpace`
- `ModuleMorphism`

Bilinear/quadratic layer:

- `BilinearForm`
- `QuadraticForm`
- `BilinearModule`
- `BilinearModuleElement`
- `QuadraticModule`
- `QuadraticModuleElement`
- `FreeBilinearModule`
- `FreeBilinearModuleElement`
- `FreeQuadraticModule`
- `FreeQuadraticModuleElement`
- `TorsionBilinearModule`
- `TorsionBilinearModuleElement`
- `TorsionQuadraticModule`
- `TorsionQuadraticModuleElement`
- `BilinearModuleHomSpace`
- `BilinearModuleMorphism`
- `FreeBilinearModuleHomSpace`
- `FreeBilinearModuleMorphism`
- `TorsionBilinearModuleHomSpace`
- `TorsionBilinearModuleMorphism`
- `QuadraticModuleHomSpace`
- `QuadraticModuleMorphism`
- `FreeQuadraticModuleHomSpace`
- `FreeQuadraticModuleMorphism`
- `TorsionQuadraticModuleHomSpace`
- `TorsionQuadraticModuleMorphism`

Lattice/discriminant layer:

- `RationalLattice`
- `RationalLatticeElement`
- `Lattice`
- `LatticeElement`
- `DualLattice`
- `DualLatticeElement`
- `DiscriminantForm`
- `DiscriminantGroup`
- `DiscriminantGroupElement`
- `RationalLatticeHomSpace`
- `RationalLatticeMorphism`
- `LatticeHomSpace`
- `LatticeMorphism`
- `DiscriminantGroupHomSpace`
- `DiscriminantGroupMorphism`

Group layer:

- `LatticeOrthogonalGroup`
- `LatticeOrthogonalSubgroup`
- `DiscriminantOrthogonalGroup`
- `DiscriminantOrthogonalSubgroup`
- `WeylGroup`
- `CoxeterDiagram`
- `EichlerGroup`

### Literal method-to-class attachment inventory

The methods below are the canonical receivers. If a method can live higher in
the hierarchy without losing meaning, it belongs on the higher noun.

`Module`:

- `gens`
- `element_from`
- `base_ring`
- `rank`
- `free_part`
- `torsion_part`
- `submodule`
- `quotient`
- `tensor`
- `base_change`
- `localize`
- `complete`
- `Hom`
- `End`
- `Aut`

`ModuleElement`:

- `to_coordinates`
- `parent`

`ModuleHomSpace`:

- inherits the `Module` structure over the same base ring
- `element_from_dict`
- `element_from_matrix`
- `identity`
- `natural_map`

`ModuleMorphism`:

- `image`
- `kernel`
- `cokernel`
- `is_injective`
- `is_surjective`
- `is_isomorphism`
- `is_primitive`

`FormCodomain`:

- `base_ring`
- `fraction_field`
- `contains`
- `quotient`

`BilinearForm`:

- `domain`
- `codomain`
- `gram_matrix`
- `tensor_map`
- `evaluate`

`QuadraticForm`:

- `domain`
- `codomain`
- `gram_matrix`
- `evaluate`

`BilinearModule`:

- `gram_matrix`
- `bilinear_form`
- `quadratic_form`
- `codomain`
- `is_R_valued`
- `is_K_valued`
- `dual`
- `direct_sum`
- `twist`
- `span`
- `orthogonal_complement`
- `Hom`
- `End`
- `Aut`

`QuadraticModule`:

- `quadratic_form`
- `polar_form`
- `codomain`
- `is_R_valued`
- `is_K_valued`
- `Hom`
- `End`
- `Aut`

`BilinearModuleElement`:

- `bilinear_product_with`
- `q`
- `norm`
- `is_isotropic`
- `perp`
- `to_vector`
- `to_coordinates`

`BilinearModuleHomSpace`:

- `element_from_dict`
- `element_from_matrix`
- `natural_map`

`FreeBilinearModuleHomSpace`, `TorsionBilinearModuleHomSpace`,
`QuadraticModuleHomSpace`, `FreeQuadraticModuleHomSpace`,
`TorsionQuadraticModuleHomSpace`:

- inherit the highest valid hom-space structure
- add only the specialization-specific constructors and validation needed by
  their layer

`BilinearModuleMorphism`:

- `image`
- `kernel`
- `cokernel`
- `is_isometry`
- `is_injective`
- `is_surjective`
- `is_isomorphism`
- `is_primitive`
- `direct_sum`

`FreeBilinearModuleMorphism`, `TorsionBilinearModuleMorphism`,
`QuadraticModuleMorphism`, `FreeQuadraticModuleMorphism`,
`TorsionQuadraticModuleMorphism`:

- inherit the highest valid morphism structure
- override only the computations that genuinely specialize to their layer

`RationalLattice`:

- `from_gram`
- `codomain`
- `is_integral`
- `dual_lattice`
- `discriminant_group`

`Lattice`:

- named constructors such as `U`, `A1`, `E8`, and the other canonical examples
- `dual_lattice`
- `discriminant_group`
- `orthogonal_group`
- `roots`
- `root_sublattice`
- `weyl_group`
- `coxeter_diagram`
- `eichler_group`
- `delta`
- `coparity`

`DiscriminantGroup`:

- `quadratic_form`
- `bilinear_form`
- `orthogonal_group`
- `isotropic_subgroup`
- `value_map`
- `norm_classes`

`RationalLatticeHomSpace`, `LatticeHomSpace`, `DiscriminantGroupHomSpace`:

- `element_from_dict`
- `element_from_matrix`
- `natural_map`

`RationalLatticeMorphism`, `LatticeMorphism`, `DiscriminantGroupMorphism`:

- `image`
- `kernel`
- `cokernel`
- `is_isometry`
- `is_primitive`

`LatticeOrthogonalGroup`:

- `gens`
- `stabilizer`
- `centralizer`
- `discriminant_kernel`
- `reflection`

`DiscriminantOrthogonalGroup`:

- `gens`
- `stabilizer`

`WeylGroup`:

- `gens`
- `simple_reflections`

`CoxeterDiagram`:

- diagram construction and inspection methods only

`EichlerGroup`:

- `gens`
- `stabilizer`

### Stage 0: Public boundary and file ownership

Goal:

- settle the package boundary and permanent file ownership before deeper code
  movement begins.

Fixed design decisions:

- The normative direct import target is `src.lattices.lattices`, because the
  spec and test artifacts import that module directly.
- `src/lattices/lattices.py` must not remain a pure re-export file.
- `src/lattices/__init__.py` must not remain a competing second public export
  surface.
- `src/lattices/lattices.py` owns `Lattice`, its named constructors, and the
  direct public boundary used by the lattice specs.
- General bilinear-module, discriminant, morphism, and group machinery stays in
  the split hierarchy under `core/`, `morphisms/`, `groups/`, and
  `categories/`.

Primary files:

- `src/lattices/lattices.py`
- `src/lattices/__init__.py`
- this plan file

Completion:

- the noun inventory above has a permanent file home;
- `src/lattices/lattices.py` contains substantive code rather than only imports;
- `src/lattices/__init__.py` no longer acts as a second export hub.

### Stage 1: Foundational rings, fields, and finitely generated modules

Goal:

- build the scalar/module layer required by `tests/sage_spec/misc.sage`.

Primary files:

- `src/lattices/core/codomains.py`
- `src/lattices/core/fgp.py`
- `src/lattices/core/rings.py`
- `src/lattices/core/modules.py`
- `src/lattices/validation/presentations.py`

Implementation target:

- implement the foundational class inventory through `MixedModule`;
- wrap Sage FGP modules over the relevant general rings `R` instead of only the
  free `ZZ` case;
- make `ModuleHomSpace` itself an `R`-module rather than only a set of maps;
- make mixed modules such as `ZZ/2` and `ZZ^3 + ZZ/2` first-class cases;
- attach the module-level verbs listed above to the module nouns rather than to
  lattices;
- make free, torsion, and mixed cases one shared layer using internally stored
  Sage objects for delegation;
- keep public inputs/outputs semantic rather than raw Sage objects.

Completion:

- the module/ring layer can express the contracts in `tests/sage_spec/misc.sage`
  without lattice-specific hacks;
- the class and method inventory above is real at the module layer.

### Stage 2: Bilinear and quadratic modules

Goal:

- build the bilinear/quadratic layer on top of Stage 1 instead of hard-coding
  lattice semantics early.

Primary files:

- `src/lattices/core/forms.py`
- `src/lattices/core/abstract.py`
- `src/lattices/core/elements.py`
- `src/lattices/core/free.py`
- `src/lattices/core/torsion.py`
- `src/lattices/categories/bilinear_modules.py`

Implementation target:

- make `BilinearModules(R)` a real Sage category of pairs `(M, \beta)`;
- realize `BilinearForm` and `QuadraticForm` as explicit objects rather than
  implicit matrices attached to parents;
- allow the form codomain to be any specified subring of the fraction field or
  quotient codomain required by the specs, including `QQ/ZZ` and `QQ/2ZZ`;
- treat a bilinear form as an actual map `M \otimes_R M -> C`, where `C` is the
  chosen codomain object, while still storing exact Sage data internally for
  computation;
- handle the `R`-valued versus `K`-valued distinction at the general
  `BilinearModule` and `QuadraticModule` levels rather than first introducing
  it at the lattice layer;
- realize the bilinear/quadratic class inventory above with real parent and
  element types;
- realize the free, torsion, and quadratic specializations as actual inherited
  layers with their own elements, hom spaces, and morphisms, not as flags on a
  single parent;
- allow free bilinear and free quadratic modules to remain possibly degenerate;
- attach the bilinear-module verbs to `BilinearModule`,
  `BilinearModuleElement`, `BilinearModuleHomSpace`, and
  `BilinearModuleMorphism` exactly as listed above;
- keep `__call__` a thin router to explicit element constructors.

Completion:

- the bilinear-module layer works over the rings the spec requires, not only
  over `ZZ`;
- bilinear forms over quotient codomains such as `QQ/ZZ` and `QQ/2ZZ` are
  natively representable;
- the `R`-valued versus `K`-valued distinction is available already on the
  general bilinear/quadratic module layer;
- public containment is parent-based;
- the bilinear/quadratic inventory above exists with the listed receivers.

### Stage 3: Rational lattices, lattices, duals, and discriminants

Goal:

- realize the lattice/discriminant layer as a specialization of Stage 2.

Primary files:

- `src/lattices/lattices.py`
- `src/lattices/core/rational.py`
- `src/lattices/core/discriminant.py`
- `src/lattices/core/elements.py`

Implementation target:

- make `RationalLattice.from_gram(...)` the unique promotion site;
- make `A_L := coker(L -> L^*)` literal architecture;
- keep lattice as the `R = ZZ` specialization and track the codomain
  distinction between `K`-valued rational lattices and `R`-valued integral
  lattices explicitly rather than by ad hoc predicates;
- keep the lattice layer thin wherever possible:
  once the general bilinear/quadratic module machinery is correct, the main
  lattice-specific work should be `ZZ`-specific algorithms and shortcuts such as
  isometry and orthogonal-group computations;
- attach the lattice/discriminant verbs to the receivers listed above, with
  named constructors on `Lattice` and not on ad hoc helper functions;
- keep dual lifts semantic as `DualLatticeElement` objects.

Completion:

- rational, integral, dual, and discriminant objects come from one coherent
  module-plus-cokernel design;
- `delta` and `coparity` live on `Lattice`;
- the lattice/discriminant inventory above exists with the listed receivers.

### Stage 4: Morphisms, hom spaces, subobjects, and orthogonal groups

Goal:

- put maps and subobjects on the correct nouns instead of on matrix helpers or
  ambient-space hacks.

Primary files:

- `src/lattices/morphisms/homspaces.py`
- `src/lattices/morphisms/lattice.py`
- `src/lattices/morphisms/discriminant.py`
- `src/lattices/groups/orthogonal.py`

Implementation target:

- make `hom()` return hom spaces and morphisms their elements;
- attach image/kernel/cokernel/primitivity/isometry verbs to morphism nouns;
- represent subobjects by inclusion morphisms and quotients by cokernel
  objects;
- attach stabilizer/centralizer/discriminant-kernel semantics to the
  orthogonal-group nouns.

Completion:

- no morphism class owns `__contains__` or `perp`;
- the hom-space/morphism/group inventory above exists with the listed
  receivers.

### Stage 5: Root, Weyl, Coxeter, and Eichler surface

Goal:

- finish the higher lattice-theoretic surface only after the underlying nouns
  already exist canonically.

Primary files:

- `src/lattices/groups/weyl.py`
- `src/lattices/groups/coxeter.py`
- `src/lattices/groups/orthogonal.py`
- lattice-layer files that own root data

Implementation target:

- realize the `WeylGroup`, `CoxeterDiagram`, and `EichlerGroup` classes from
  the inventory above;
- attach their listed verbs to those nouns and keep root/reflection semantics
  on the lattice/group layer rather than backend helpers.

Completion:

- the higher group inventory above exists with the listed receivers;
- the root/Weyl/Coxeter/Eichler surface composes with Stage 4 instead of
  bypassing it.

### Stage 6: General indefinite-isometry completion

Goal:

- remove the remaining places where the spec still has to drop to raw Sage
  setup because the noun layer is incomplete.

Primary files:

- `src/backends/isometry_backend.py`
- `src/backends/dawes_orbit_backend.py`
- `src/backends/isotropic_gamma_orbit_backend.py`
- whichever noun-layer files still need missing exact constructors

Implementation target:

- add the remaining canonical constructors and exact transforms needed by the
  indefinite-isometry specs;
- keep the backend layer delegation-only.

Completion:

- the remaining indefinite-isometry spec cases are expressed through noun-layer
  constructors and morphisms rather than raw `IntegralLattice` or
  `ambient_module()` setup.

### Stage 7: Human-in-the-loop spec review

Goal:

- review implementation/spec mismatches only after the implementation target
  above is actually built.

Implementation target:

- review the deferred mismatch list with the user;
- revise specs only where the user explicitly directs and reviews the change.

Completion:

- implementation-side redesign work is finished;
- any actual spec edit is human-directed and explicit.

### Migration strategy across all stages

- Reuse the existing generated code where it is mathematically sound.
- Prefer extraction and refactoring from the current `src/lattices/` hierarchy
  over restart-from-zero rewrites.
- Preserve the two Sage-integration lessons already recovered in this repo:
  `_Hom_` is the correct homset hook, and wrapped elements must be genuine Sage
  elements.

## Target Hierarchy

The public package should end in this form:

- `src/lattices/__init__.py`: package marker/documentation only, not a second
  public export hub
- `src/lattices/lattices.py`: `Lattice`, named constructors, and the direct
  public import boundary used by the specs
- `src/lattices/core/codomains.py`: form-codomain objects, including quotient
  codomains such as `QQ/ZZ` and `QQ/2ZZ`
- `src/lattices/core/fgp.py`: enriched wrappers around Sage FGP-module objects
  over the relevant general rings `R`
- `src/lattices/core/rings.py`: quotient/localized/completed scalar objects
- `src/lattices/core/modules.py`: `Module`, `FreeModule`, `TorsionModule`,
  `MixedModule`, and `ModuleHomSpace` as an `R`-module
- `src/lattices/core/forms.py`: `BilinearForm`, `QuadraticForm`, and the
  tensor-map interpretation of Gram data
- `src/lattices/core/abstract.py`: concrete `BilinearModule` /
  `QuadraticModule` parents built from module objects plus form objects
- `src/lattices/core/elements.py`: element nouns and shared element behavior
- `src/lattices/core/free.py`: free bilinear-module semantics over general `R`
- `src/lattices/core/torsion.py`: pure-torsion specialization of the general
  bilinear-module noun
- `src/lattices/core/rational.py`: `RationalLattice`, `DualLattice`
- `src/lattices/core/discriminant.py`: `DiscriminantForm`,
  `DiscriminantGroup`, discriminant elements
- `src/lattices/morphisms/homspaces.py`: homspace nouns
- `src/lattices/morphisms/lattice.py`: rational/integral lattice morphisms
- `src/lattices/morphisms/discriminant.py`: discriminant morphisms
- `src/lattices/groups/orthogonal.py`: orthogonal-group nouns and subgroup
  semantics
- `src/lattices/groups/weyl.py`: `WeylGroup`
- `src/lattices/groups/coxeter.py`: `CoxeterDiagram`
- `src/lattices/validation/presentations.py`: constructor validation only

Backend delegation should end in this form:

- `src/backends/isometry_backend.py`: isometry delegation only
- `src/backends/dawes_orbit_backend.py`: orbit/stabilizer delegation only
- `src/backends/isotropic_gamma_orbit_backend.py`: isotropic-orbit delegation
  only

Flat files such as the current `src/lattices/modules.py`,
`src/lattices/morphisms.py`, `src/lattices/groups.py`, and
`src/lattices/orthogonal.py` are temporary migration waypoints and should be
deleted once their contents have been moved into the target hierarchy.

## Phases

### Phase A: Containment and skeleton

- Create the target subdirectory hierarchy and stub only the intended files.
- Freeze the public noun vocabulary and file ownership.
- Mark current flat lattice files as migration-source files, not destinations.
- Completion:
  - every target file exists,
  - every public noun has a declared home,
  - no new work lands in the wrong file class.
- Verification:
  - file inventory inspection,
  - import graph inspection,
  - diff review confirming no new compatibility shims were added.

### Phase B: Core noun migration

- Replace the current abstract-shell top layer with a real semantic carrier:
  `BilinearModule` must wrap a finitely generated module presented as an FGP
  module together with a bilinear form matrix in a fixed generator order.
- `FreeBilinearModule` and `TorsionBilinearModule` are specializations of that
  general noun when the torsion part or free part vanishes, respectively.
- Keep bilinear and quadratic public semantics distinct even when a class stores
  multiple Sage backend objects for delegation.
- Move shared element semantics, free-module semantics, and
  rational/integral lattice semantics into the target `core/` files.
- Replace hard-coded `ZZ` where the written spec requires general `R`.
- Remove rejected public state:
  `ambient_parent`, `inclusion_matrix`, `projection_lattice`,
  `projection_matrix`, `scaled_element`, `lift_vector`, and any public
  `native`-style methods.
- Lift general module verbs upward so they live on `BilinearModule` unless they
  truly require lattice-specific structure: `gens`, `element_from`, direct
  sums, twists, submodule generation, quotient construction, bilinear-form
  access, and related parent-level operations.
- Remove public Sage leakage:
  `to_sage`, `from_sage`, direct Sage-object constructor admission, and
  analogous passthroughs that let callers bypass the semantic layer.
- Remove optional-argument constructor shapes from the public nouns and split
  the cases into explicit constructors or class methods.
- Completion:
  - `BilinearModule(...)` is a concrete mixed free-plus-torsion noun backed by
    an FGP module and a bilinear form matrix,
  - `FreeBilinearModule` and `TorsionBilinearModule` are genuine special cases
    of that noun rather than disjoint presentation systems,
  - public module/lattice nouns are presented only by generators and Gram data,
  - membership is parent-based,
  - no ambient embedding state remains on the public nouns,
  - no public Sage leakage remains on the noun surface.
- Verification:
  - direct inspection of public constructors and fields,
  - import compile of the moved files,
  - spec-review against the canonical sources,
  - grep confirming that public `src/lattices/core/` APIs no longer expose
    `to_sage`, `from_sage`, `ambient_parent`, or `inclusion_matrix`.

### Phase C: Validation and typing pass

- Replace hand-written public validation with explicit pydantic models at the
  public boundary.
- Add complete type annotations on constructors, element conversions, morphism
  constructors, and group entry points.
- Replace `hasattr`/`isinstance` abuse with typed or semantic dispatch.
- Remove `raise`-style validation from public constructors and coercions.
- Remove optional public types and `Any`-typed surfaces from the final lattice
  package.
- Add explicit `@override` markers wherever the codebase/runtime supports them.
- Completion:
  - public constructors and coercions validate through pydantic models,
  - abstract classes have real abstract methods,
  - public methods no longer return `None` for mathematically undefined cases,
  - public mathematical APIs use assertions only for true mathematical domain
    obligations rather than input-shape checking,
  - public signatures avoid `Any` and optional variants.
- Verification:
  - static inspection of signatures,
  - direct inspection of validation ownership in `src/lattices/validation/`,
  - import compile,
  - grep confirming no new `raise`, `try`, or `except` in the public lattice
    layer,
  - grep confirming no `Any`, `object`, `| None`, or `Optional` in the public
    lattice signatures.

### Phase D: Morphisms and homspaces

- Rebuild homspace nouns first, then morphism elements as elements of those
  spaces, wrapping Sage homsets and morphisms rather than hand-rolling matrix
  carriers.
- Use Sage's real parent hook: custom hom construction belongs on `_Hom_`,
  not on ad hoc `Hom` forwarding methods.
- Custom homsets must be initialized with the bilinear-module category itself;
  passing the homset category in directly produces the wrong Sage construction
  path.
- Wrapped module/lattice/discriminant elements must be genuine Sage
  `Element`/`ElementWrapper` instances; plain Python wrappers break
  `Map.__call__`, coercion, and category-owned morphism behavior.
- Implement the missing constructor families and migration of existing matrix
  and generator-image logic.
- Replace the current bogus cokernel logic with actual bilinear-module quotient
  construction driven by the FGP module cokernel.
- On torsion/discriminant backends, build homomorphisms through the backend's
  own Smith-form constructor (`_hom_from_smith`) when that is the exact Sage
  interface, rather than reassembling maps through ad hoc image routing.
- Move matrix-isometry checking to the semantic containment boundary of the
  relevant hom-space or orthogonal-group noun instead of repeating matrix
  equations in ad hoc methods.
- Delete wrong-noun APIs from morphisms: no morphism `__contains__`, no
  morphism `perp`, and no ambient-subobject semantics on morphism elements.
- Lift general morphism verbs upward so they live on
  `BilinearModuleMorphism` unless they genuinely require integral/rational
  specialization: `image`, `kernel`, `cokernel`, `is_primitive`, and the
  standard constructors through hom-space parents.
- Completion:
  - `hom()` returns homspaces,
  - morphisms own `image`, `kernel`, `cokernel`, `is_primitive`, and related
    verbs,
  - `A_L := coker(L -> L^*)` is modeled through the correct construction path,
  - equality on hom spaces and morphisms matches the `CONTRIBUTING.md`
    semantics.
- Verification:
  - API inspection,
  - dedicated spec tests once the hierarchy is stable,
  - review against the morphism block in the written spec backup.

### Phase E: Discriminant and dual semantics

- Rebuild `DualLattice` and discriminant objects without fake projection state.
- Ensure dual-lattice elements, not ad hoc vectors, are the relevant lift
  objects.
- Move lattice invariants such as `delta` and `coparity` to the lattice layer.
- Completion:
  - discriminant class semantics come from the dual/discriminant architecture,
    not from remembered ambient state,
  - discriminant-group API does not own lattice-only invariants.
- Verification:
  - public API inspection,
  - direct comparison against the preserved correction spec.

### Phase F: Orthogonal groups and backend boundary

- Move orthogonal-group nouns into `src/lattices/groups/orthogonal.py`.
- Remove constraint-merge bookkeeping from the public group layer and express
  subgroup semantics through the proper `ConditionSet` boundary.
- Keep backend files delegation-only; they may compute generators/orbits, but
  they must not define the public semantics.
- Completion:
  - `L.orthogonal_group()` is the semantic home,
  - stabilizers live on the orthogonal-group nouns,
  - backend files no longer dictate public API structure.
- Verification:
  - call-site inspection,
  - import compile,
  - spec-check against the orthogonal-group corrections.

### Phase G: Debris deletion

- Delete temporary flat files and any remaining stale names once all migrated
  logic has a final home.
- Delete rejected helper functions and old shim names.
- Delete internal renamings of canonical objects where direct construction is
  the intended name.
- Completion:
  - the repo has exactly one intended public lattice hierarchy,
  - no duplicate or transitional lattice files remain.
- Verification:
  - file inventory,
  - grep for banned names and rejected fields.

## Current Status Snapshot

This section records the actual redesign state after the `_Hom_` /
`ElementWrapper` migration slice and after comparison against
`CONTRIBUTING.md`, the lattice spec tests, and the durable lattice memories.
It is the current signoff surface for what remains architecturally unresolved.

### What is materially in place

- The target subdirectory hierarchy from Phase A exists.
- The intended canonical public module remains `src/lattices/lattices.py`, but
  it currently exists as a pure re-export file, which violates
  `CONTRIBUTING.md`.
  `src/lattices/__init__.py` is also still acting as a second export surface,
  so the package boundary is currently wrong even though the module exists.
- The bilinear-module category now uses Sage's real `_Hom_` hook rather than
  ad hoc `Hom` forwarding.
- Bilinear-module and discriminant elements are now real Sage
  `ElementWrapper`-based elements, which fixes the previous `Map.__call__`
  failure mode.
- Bilinear homsets/morphisms and discriminant homsets/morphisms now wrap Sage
  hom objects instead of pretending plain Python wrappers are sufficient.
- Homspace selection is now stratified by semantic layer rather than always
  collapsing to the generic bilinear homspace:
  - lattice-to-lattice homs produce lattice morphisms;
  - rational-lattice homs produce rational-lattice morphisms;
  - discriminant-group homs use their own discriminant homspace.
- Direct sums now install their canonical summands and embedding morphisms on
  the ambient result instead of throwing away that decomposition immediately.
- Free torsionfree bilinear modules now use explicit Sage `FGP_Module`
  backends, which makes mixed-ring hom construction behave predictably instead
  of collapsing onto quotient-vector-space edge cases.
- `DualLattice` is now modeled as a free `ZZ`-module with `QQ`-valued form,
  rather than as a raw `QQ`-vector-space lattice.
  This restores the intended semantics of the inclusion
  `\iota_L : L \to L^*`:
  - unimodular inclusions are surjective,
  - non-unimodular inclusions have torsion cokernel,
  - `coker(\iota_L)` can now be promoted to `DiscriminantGroup`.
- The discriminant-hom path now handles both nontrivial Smith-form data and the
  trivial discriminant-group endomorphism case without falling back to the
  wrong Sage homset category.
- Morphisms now expose the missing spec-facing verbs needed by the redesign
  slice:
  - `is_injective`, `is_surjective`, `is_bijective`, `is_isomorphism`,
    `is_isometry`,
  - `direct_sum`,
  - `perp` on subobject embeddings.
- A manual runtime sweep of the current written-feedback spec surface now
  passes end to end without running the global QC/lint stack.
- The correction artifacts already record the two critical Sage-integration
  lessons from this slice:
  - custom hom construction belongs on `_Hom_`;
  - wrapped elements must be genuine Sage elements.

### Framing corrections carried into this plan

The user corrected the execution framing in April 2026, and this plan must
preserve those corrections explicitly:

- The spec is the contract for this redesign.
  Files under `tests/lattice_spec/` and the relevant lattice/module files under
  `tests/sage_spec/` are normative until the user says otherwise.
- Unimplemented spec surface is remaining required work.
  It is not "aspirational", not optional migration material, and not an
  external obstacle category separate from the work itself.
- Intermediate redesign slices are not task completion.
  This plan must not declare success while required spec surface remains
  unimplemented.

### Current remaining required work

The redesign stop condition is not yet met because required spec work remains.
The items below are unfinished implementation, not polish:

- `CONTRIBUTING.md` still forbids optional/default public APIs, but the live
  lattice surface still exposes them in files such as
  `src/lattices/core/free.py`,
  `src/lattices/core/rational.py`,
  `src/lattices/core/integral.py`,
  `src/lattices/core/discriminant.py`,
  `src/lattices/groups/orthogonal.py`,
  `src/lattices/morphisms/discriminant.py`,
  `src/lattices/morphisms/homspaces.py`, and
  `src/lattices/categories/bilinear_modules.py`.
  These are not style nits; they violate the stated public API contract.
- The canonical export surface is currently broken.
  `src/lattices/lattices.py` is a pure re-export file and
  `src/lattices/__init__.py` is still a competing export surface, so the
  package boundary must be repaired before the redesign can claim to have a
  stable public surface.
- The lower bilinear-module support stack is still underbuilt.
  The redesign still lacks explicit form-codomain objects, enriched FGP-module
  wrappers over general `R`, and a module-hom layer that treats
  `Hom_R(M, N)` as an `R`-module.
  Without those layers, the stated goal of a fully general
  `BilinearModule(R)` architecture is not yet satisfied.
- Backend encapsulation is still incomplete.
  Public-path lattice/discriminant/group code still depends on
  `_sage_like` / `_from_sage_like`, and discriminant comparison still reaches
  into Sage-private data such as `_modulus` / `_modulus_qf`.
  That remains architectural leakage under `CONTRIBUTING.md`.
- The foundational module-theory surface required by `tests/sage_spec/misc.sage`
  remains to be implemented and is an upstream dependency of the rest of the
  redesign:
  free/torsion decomposition, tensor/base-change/localization/completion,
  richer `Hom`/`End`/`Aut` support, kernels/cokernels/projections/natural maps,
  and the stated `Tor`/`Ext`-adjacent module semantics.
- The root/Weyl/Coxeter/Eichler surface required by
  `tests/lattice_spec/interface_extensions.sage` and
  `tests/sage_spec/coxeter.sage` remains to be implemented:
  root systems, root sublattices, Weyl groups, Coxeter diagrams, reflections,
  reflection decompositions, Eichler groups, and the associated diagram/group
  morphism surface.
- The discriminant and subobject enrichment required by
  `tests/lattice_spec/interface_extensions.sage` and
  `tests/lattice_spec/more_specs.sage` remains to be implemented:
  isotropic-element enumerators, norm-class partitions, value maps,
  saturated-image/submodule semantics, and the richer quotient/cokernel
  behavior required by the written spec.
- The witness/functionals and dual-surface API required by
  `tests/lattice_spec/more_specs.sage` remains to be implemented:
  witness-returning isometry checks, the exact functional/homspace constructor
  surface, and the remaining dual/discriminant lift behavior.
- The canonical-construction gap is still open.
  `tests/lattice_spec/interface_semantics.sage` and
  `tests/lattice_spec/todo_general_indefinite_isometry_spec.py` still need raw
  `IntegralLattice`, `ambient_module()`, and basis-surgery constructions for
  some cases, which means the noun surface is still missing required canonical
  constructors or exact transforms.
- The plan artifact itself was previously corrupted by a false completion
  declaration.
  Until this list is kept in sync with the real code/spec state, this
  file is not a reliable signoff surface.

### Immediate redesign order

The next implementation slices should proceed in this order:

- repair the package boundary by making `src/lattices/lattices.py`
  substantive and reducing `src/lattices/__init__.py` to a non-competing
  package file;
- implement the foundational codomain/ring/FGP/module layer required by
  `tests/sage_spec/misc.sage`, including quotient codomains, mixed modules,
  and `Hom_R(M, N)` as an `R`-module;
- rebuild `BilinearModules(R)`, `BilinearForm`, `QuadraticForm`, and the
  concrete general `BilinearModule` carrier over that shared module layer;
- realize the free/torsion/quadratic specializations as real inherited layers
  with their own elements, hom spaces, and morphisms;
- migrate lattice/rational/dual/discriminant semantics onto the general
  bilinear-module and cokernel machinery, with explicit codomain control for
  `R`-valued versus `K`-valued forms and for quotient codomains such as
  `QQ/ZZ` and `QQ/2ZZ`;
- finish morphism, subobject, and orthogonal-group semantics against
  `tests/lattice_spec/interface_semantics.sage`,
  `tests/lattice_spec/test_lattices_written_feedback_spec.py`,
  `tests/lattice_spec/more_specs.sage`, and `tests/sage_spec/lattice_methods.sage`;
- implement the root/Weyl/Coxeter/Eichler surface required by
  `tests/lattice_spec/interface_extensions.sage` and
  `tests/sage_spec/coxeter.sage`;
- extend the noun surface so the remaining spec cases no longer require new raw
  `IntegralLattice`, `ambient_module()`, or basis-surgery workarounds in the
  implementation path, and then finish the general indefinite-isometry backend;
- document any spec revision candidates discovered along the way for the final
  human-in-the-loop review stage;
- only after these required surfaces are in place may this file grow a
  completion section again.

### Stop condition

The redesign is complete only when all of the following are true:

- the public noun surface no longer violates the `CONTRIBUTING.md` rules on
  optional/default public APIs;
- public lattice/discriminant/group methods no longer rely on raw Sage-object
  admission or Sage-private invariants as part of their external contract;
- the class inventory and method-to-class attachment inventory in this plan has
  been realized, with `BilinearModule(R)` working over general `R` rather than
  only over `ZZ`;
- the remaining required surface in `tests/lattice_spec/` and the relevant
  lattice/module specs in `tests/sage_spec/` is implemented rather than being
  downgraded, deferred, or described as optional;
- the live spec gate is canonical and noun-based rather than mixed with raw
  `IntegralLattice` construction patterns;
- this plan file accurately reflects remaining required work instead of
  declaring completion early.

## Task-Level Stop Rules

- Stop if a public noun requires ambient embedding state to function.
- Stop if a phase attempts to preserve a rejected name or helper for convenience.
- Stop if backend code begins defining public semantics rather than delegated
  computation.
- Stop if an operation cannot be expressed without inventing a new ad hoc
  helper instead of using an existing Sage or backend primitive.
- Stop if public-object validation is drifting back into ad hoc asserts or
  exception plumbing instead of the pydantic boundary layer.
- Stop if a public API patch introduces optional args/types, `Any`, or public
  Sage-object passthroughs.
- Stop if downstream consumer rewiring begins before the upstream noun/morphism
  interfaces are stable.

## System-Level Validation

- During the architecture migration, use file-layout inspection, import
  compilation, grep checks for banned names, and spec conformance review.
- During validation migration, explicitly grep for `raise`, `try`, `except`,
  `hasattr`, and `None`-sentinel returns in `src/lattices/`.
- During style migration, explicitly grep for `Any`, `object`, `| None`,
  `Optional`, public `to_sage`/`from_sage`, and missing standard methods on the
  public nouns.
- After the hierarchy stabilizes, add or update dedicated spec tests that prove
  the mathematical interface rather than preserve stale implementation details.
- Do not treat the legacy suite as the architecture gate.

## Risks and Rollback

Main risks:

- Carrying over wrong ambient or wrapper semantics into the new hierarchy.
- Splitting files without actually changing the semantic model.
- Letting backend convenience concerns dictate the public API.

Mitigation:

- Treat the canonical spec files as hard gate documents for every phase.
- Use the current generated files only as extraction sources.
- Delete migrated source files as soon as their logic has a stable final home.

Rollback / fallback:

- The rollback point is the current staged flat hierarchy.
- If a migration step corrupts the target hierarchy, restore from the staged
  checkpoint and redo that phase without preserving the rejected abstraction.

## Expected End State

At completion, the lattice subsystem is a clean semantic package with:

- a real subdirectory hierarchy,
- no compatibility cruft,
- no ambient-embedding state on public nouns,
- no public Sage leakage,
- no optional public API surface and no `Any`-typed public signatures,
- typed constructors with pydantic-backed public validation,
- correct homspace/morphism/discriminant semantics,
- backend delegation kept behind the public mathematical layer.
