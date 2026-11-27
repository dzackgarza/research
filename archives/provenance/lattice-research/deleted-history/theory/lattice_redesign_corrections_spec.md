# Lattice Redesign Corrections Spec

This file is a durable preservation artifact for detailed user corrections that
must remain available even if chat context is compacted.

Canonical related sources:

- [theory/spec_backups/lattices_written_spec_backup.py](./spec_backups/lattices_written_spec_backup.py)
- [src/lattices/lattices.py](../src/lattices/lattices.py)

This file is not a replacement for the written lattice spec backup. It records
additional corrections and prohibitions stated after the initial redesign
attempts.

## Raw User Correction

Recorded on 2026-04-12. Preserved verbatim from the user message.

> You wrote insane helper functions that indirect simple one-liners. And NO, you can not throw away that code, you just spent hundreds of thousands of tokens generating it. You wrote helpers for dead simple sage code, like is_integral_matrix, which I already explained in comments is just checking "M in GL(n, ZZ)". Identity columns is fucking nonsense when identity_matrix exists. You used hasattr instead of properly typing your code. There are virtually no types at all. No mathematical assertions. No pydantic validation. zero_gram makes no sense when zero_matrix() exists. merge_orbit_constraints is absolutely braindead when ConditionSet supports unions and intersections directly. You imported and exposed sage-native constructs like signature_vector onto the public API, which preserves broken semantics that aren't in the new spec. You ignored all of my theory about bilinear modules being constructed from e.g. R^n and a gram matrix. This is completely general and well-defined, for any sage ring R and any symmetric element of GL_n(R). You used "pass" instead of defining simple ABCs. gens() is perfectly well-defined for any class here, it is literally a set of n symbols that behave as elements. You hard-coded ZZ at levels where general R is what the comments specify. You added inclusion_matrix when this is not even well-defined mathematically -- bilinear modules are NOT naturally embedded in ANY space. Only SPECIFIC subobjects have that. You have things returning None, completely undefined mathematically. projection_matrix is not in the spec at all. I specifically discussed how "contains" is a parent check: a vector v in ZZ^n DEFINES an element in L because it gives COORDINATES in the standard basis of L, but is NOT an element in L a priori. So v = vector(ZZ, [1,0]) is NOT an element of U. You have to use U.element_from(v) to identify v == e == 1*e + 0*f. scaled_element seems to make no sense, because if v is an element, 3*v is another perfectly valid element. These are free modules. submodule_from_rows doesn't make sense: submodules are defined by SETS of generators (or lists, tuples, etc), not the rows of a matrix. __add__ is braindead when identity_matrix() and block sums exist. you ignored my comments about L^n using sum, e.g. sum(n * [L]). You used the "native" terminiology, when there's no reason this should be on the public API whatsoever: there is a "sage-like" object. I explicitly discussed this in spec comments. lift_vector makes no sense: it is not just a random QQ-vector. It is an element of L^*. No object should REQUIRE a sage-like object in the constructor, they always STORE one by simple creating it internally and storing it, AND have a classmethod that takes a sage object and does the conversion internally. You allowed variable numbers of args (wrong), imported old sage-like constructs like modulus and modulus_qf. You left assertions in instead of using proper validation, discussed extensively in spec. You left in things I CLEARLY discussed as mathematically ill-defined, like p-rank, with a totally nonsensical algorithm that makes no sense in general. You put delta/coparity as invariants on A_L, when they are invariants of the LATTICES L. You left in SHIMS to old methods, like has_isomorphic_group_structure_to, the spec CLEARLY defined the correct names to migrate to. You made hom require images, which is semantically completely wrong, because that produces an ELEMENT of the hom space. Discussed at length already. You did not extend ANY sagemath constructs like homset or morphism like I required. You left out ALL of the hom and morphism methods I described. You used assert False to avoid creating proper objects: I explicitly described how e.g. cokernels need to CONSTRUCT the correct objects. It CAN be a lattice, or a torsion bilinear form. cokernel is completely wrong, and does not construct the cokernel correctly as discussed -- you construct an orthogonal complement, which is WILDLY wrong, and completely fails to construct A_L := coker(L -> L^*) correctly. projection_lattice is completely ill-defined in general: a lattice does not "project" onto a sublattice. There is no map. You forced dual lattices to only be quotientable by the original lattice, but this is wrong, they are rational lattices and can be quotiented by anything. This just defers to the cokernel of the inclusion. You expose and leak private data with methods that pipe into the underlying sage object, instead of forucing extracting the sage object if you want the "sage-native" objects, which should be almost NEVER. "outside_domain" is just is_p_elementary(2). methods like vec_to_list are braindead, there is NO reason to ever use this when you should be using lattice elements and manually extracting their coordinates when needed, and noting the fact that list(v.to_vector()) naturally works when v.to_vector() is a sage vector. Methods like _definite_orthogonal_group_generators are ill-placed, because the proper semantics is L.orthogonal_group().gens(). You are asserting matrix equations for isometries, which is totally wrong, you are supposed to do this in one place: the containment function for O(L). Stabilizers go on O(L), e.g. L.orthogonal_group().stabilizer(v), as do other related verbs.  You use isinstance and hasattr instead of properly typing and dispatching on inputs. You need to read the spec, the comments, the intended semantics and public API, start by stubbing out a subdir HIERARCHY with touched files for the various levels of the API, and then proceed to migrate the EXISTING code into the smaller organized hierarchy of files, then fix all of these issues

## Additional Raw Corrections

Recorded on 2026-04-13. Preserved verbatim from the user messages.

> And morphisms can not "contain" anything...

> Note that a morphism can not have a "perp" either

> You also have most methods too far down the hierarchy: almost everything makes sense for objects in BilinearModules, their morphisms, hom spaces, etc

> That's not right. BilinearModules is a new category. It has its own elements and morphisms. It is the category of pairs (M, \beta) where M is an finitely generated R-module, R is a PID, and \beta is a bilinear form on M. So you might as well hook a new category properly, emulating https://github.com/sagemath/sage/blob/develop/src/sage/categories/modules.py

## Framing Corrections

Recorded on 2026-04-13. Preserved verbatim from the user messages.

> Wait, what the fuck do you mean "aspirational"? That is the SPEC

> What do you mean "the spec *can* be ahead of the implementation"? Do you not understand what "spec" means?

> Wait, what do you mean when you say these are "blockers"...? This is the spec. You aren't finished implementing it. You keep stopping midway, as I keep pointing out. Nothing is "blocked"

> Make sure the plan and documents are clear about everything I've corrected you on in the last few turns

## Normalized Design Directives

The following are implementation directives distilled from the raw correction.
These are not new ideas; they restate the user's correction in structured form.

### Public mathematical model

- A bilinear module is presented by canonical generators of `R^n` together with
  a Gram matrix.
- `BilinearModules(R)` is a genuine new Sage category of pairs `(M, \beta)`,
  not merely an informal wrapper convention around existing module parents.
- This must be defined generally over a Sage ring `R`, not hard-coded to `ZZ`
  except where a class specifically models integral lattices.
- Public lattice/module nouns are not naturally embedded in ambient spaces.
- Public nouns must not carry `inclusion_matrix`, `projection_matrix`,
  `projection_lattice`, or similar ambient-embedding state.
- Specific embeddings and subobjects must be represented separately, not baked
  into the core noun.
- `gens()` is semantically well-defined throughout the hierarchy and should not
  be omitted.
- Membership is a parent check: coordinate vectors are not automatically
  elements of a lattice.
- `L.element_from(v)` is the semantic conversion from coordinates to an element.

### Spec authority and execution discipline

- The lattice spec is authoritative.
  If a behavior appears in the normative spec files, it is required target
  behavior until the user explicitly revises that status.
- Do not describe unmet spec surface as "aspirational", "optional",
  "migration-only", or otherwise outside the redesign gate merely because the
  implementation does not satisfy it yet.
- Do not describe unfinished required implementation as a "blocker".
  It is remaining required work on the spec itself.
- Do not treat completion of a local redesign slice as completion of the task.
  The task ends only when the required spec surface is actually implemented.
- The redesign plan is a signoff artifact and must stay truthful.
  It must not claim architectural completion while required spec work remains.

### API hierarchy and file organization

- The redesign must use a real hierarchy of files under a subdirectory
  structure, not a monolithic public file.
- The existing generated code should be migrated into the organized hierarchy,
  not discarded and restarted from scratch.
- Public API terminology should be semantic and stable; do not preserve stale
  names from older designs.

### Typing, validation, and dispatch

- Do not use `hasattr` or ad hoc runtime probing where proper typing and
  dispatch are intended.
- Add real type annotations throughout the hierarchy.
- Use Pydantic validation rather than loose assertions for public-object
  validation.
- Do not use `pass` where simple ABCs should be defined.
- Do not use `assert False` in places where mathematically meaningful objects
  must be constructed.

### Anti-wrapper / anti-slop rules

- Do not introduce helper functions that merely wrap obvious one-line Sage
  functionality.
- Do not create helpers like `zero_gram` when `zero_matrix()` already exists.
- Do not create helpers like identity-column builders when `identity_matrix()`
  already exists.
- Do not create row-oriented constructor helpers when the semantics are really
  about generators or standard objects already available in Sage.

### Terminology and interop

- Do not expose `native` terminology on the public API.
- If Sage interop must exist, use explicit "sage-like" extraction, not leaked
  wrapper passthroughs.
- Constructors should build and store their internal Sage object themselves.
- Separate class methods may accept Sage objects and convert them internally.
- No public object should require a Sage object as its constructor input.

### Semantics explicitly rejected

- `signature_vector` on the public API.
- `merge_orbit_constraints` or parallel subgroup-constraint bookkeeping when
  `ConditionSet` should express subgroup restrictions directly.
- `scaled_element` as a semantic public operation on free-module elements.
- `submodule_from_rows`; submodules are defined by generators, not matrix rows
  as a public noun.
- `projection_lattice`; lattices do not canonically project onto sublattices.
- `lift_vector`; lifts in this context are elements of `L^*`, not bare vectors.
- `vec_to_list` style shims.
- old shim names like `has_isomorphic_group_structure_to`.
- ill-defined invariants or algorithms such as the cited `p-rank` method.

### Morphisms and categorical semantics

- `hom()` should construct a hom-space, not require images directly.
- Elements of a hom-space are the morphisms.
- Bilinear-module objects need category-owned elements and morphisms, not plain
  Python wrappers carrying Sage objects on the side.
- The category should be hooked properly through Sage parent/category
  machinery, modeled on `sage.categories.modules`, with its own parent methods,
  element methods, and homset category.
- The actual Sage hook for custom homset construction is `_Hom_`; redefining
  `Hom` alone is not sufficient.
- Wrapped elements must be real Sage elements (`Element` /
  `ElementWrapper`-based), not plain Python wrappers carrying Sage objects on
  the side, or Sage morphisms will not compose through `Map.__call__`.
- The implementation should extend or properly model Sage morphism/homset
  semantics where specified.
- Morphisms are not containers; no morphism class should define semantic
  containment for arbitrary values.
- `perp` / orthogonal-complement verbs do not belong on morphisms; those belong
  on the relevant subobject or ambient bilinear-module noun.
- General verbs should live as high in the hierarchy as their semantics allow:
  on `BilinearModule`, `BilinearModuleMorphism`, `BilinearModuleHomSpace`, and
  only specialize lower when extra structure genuinely appears.
- The omitted morphism and hom-space methods described in the written spec must
  be implemented.
- Cokernels must construct the correct mathematical object, which may be a
  lattice, torsion bilinear module, discriminant form, or another appropriate
  object depending on the context.
- `A_L := coker(L -> L^*)` must be modeled correctly.
- On discriminant/torsion backends, hom construction should defer to Sage's
  Smith-form hom constructor where that is the backend's exact interface.
- Dual lattices are rational lattices and may be quotiented by more than the
  original lattice.

### Invariants and theory placement

- `delta` / `coparity` are invariants of lattices `L`, not of discriminant
  groups `A_L`.
- `outside_domain` should not be a separate ad hoc notion when the meaningful
  predicate is `is_p_elementary(2)`.
- Isometry verification belongs in the containment semantics of `O(L)`, not
  scattered matrix-equation assertions.

### Group semantics

- Orthogonal-group semantics live on `L.orthogonal_group()`.
- Stabilizers and related verbs belong on orthogonal groups, e.g.
  `L.orthogonal_group().stabilizer(v)`.
- Implementation details like `_definite_orthogonal_group_generators` are not
  the public semantic surface.

## Non-Negotiable Preservation Rule

The generated redesign code must be reorganized and corrected, not discarded
wholesale. The correct procedure is:

- stub the intended hierarchy,
- migrate the existing generated code into the smaller hierarchy,
- then repair the semantics, validation, typing, and mathematical design
  defects listed above.

## Source of Truth Rule

When future work is done on the lattice redesign, consult this file and
`theory/spec_backups/lattices_written_spec_backup.py` before changing the public
interface.
