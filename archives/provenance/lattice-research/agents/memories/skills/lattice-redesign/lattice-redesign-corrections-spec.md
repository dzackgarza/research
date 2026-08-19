# Lattice Redesign Corrections Spec

This file is a durable preservation artifact for detailed user corrections that
must remain available even if chat context is compacted. The normalized design
directives distilled from these corrections now live in
`lattice-interface-style-guide.md` and `category-abc-spec.md`.

Canonical related sources:

- [src.bak/spec-backups/lattices_written_spec_backup.py](../../../../src.bak/spec-backups/lattices_written_spec_backup.py)
- [src.bak/lattices/lattices.py](../../../../src.bak/lattices/lattices.py)
- [lattice-interface-style-guide.md](./lattice-interface-style-guide.md) (distilled public API and audit rules)
- [category-abc-spec.md](./category-abc-spec.md) (category contract and discriminant descent rules)

## Raw User Correction

Recorded on 2026-04-12. Preserved verbatim from the user message.

> You wrote insane helper functions that indirect simple one-liners. And NO, you can not throw away that code, you just spent hundreds of thousands of tokens generating it. You wrote helpers for dead simple sage code, like is_integral_matrix, which I already explained in comments is just checking "M in GL(n, ZZ)". Identity columns is fucking nonsense when identity_matrix exists. You used hasattr instead of properly typing your code. There are virtually no types at all. No mathematical assertions. No pydantic validation. zero_gram makes no sense when zero_matrix() exists. merge_orbit_constraints is absolutely braindead when ConditionSet supports unions and intersections directly. You imported and exposed sage-native constructs like signature_vector onto the public API, which preserves broken semantics that aren't in the new spec. You ignored all of my theory about bilinear modules being constructed from e.g. R^n and a gram matrix. This is completely general and well-defined, for any sage ring R and any symmetric element of GL_n(R). You used "pass" instead of defining simple ABCs. gens() is perfectly well-defined for any class here, it is literally a set of n symbols that behave as elements. You hard-coded ZZ at levels where general R is what the comments specify. You added inclusion_matrix when this is not even well-defined mathematically -- bilinear modules are NOT naturally embedded in ANY space. Only SPECIFIC subobjects have that. You have things returning None, completely undefined mathematically. projection_matrix is not in the spec at all. I specifically discussed how "contains" is a parent check: a vector v in ZZ^n DEFINES an element in L because it gives COORDINATES in the standard basis of L, but is NOT an element in L a priori. So v = vector(ZZ, [1,0]) is NOT an element of U. You have to use U.element_from(v) to identify v == e == 1*e + 0*f. scaled_element seems to make no sense, because if v is an element, 3*v is another perfectly valid element. These are free modules. submodule_from_rows doesn't make sense: submodules are defined by SETS of generators (or lists, tuples, etc), not the rows of a matrix. __add__ is braindead when identity_matrix() and block sums exist. you ignored my comments about L^n using sum, e.g. sum(n * [L]). You used the "native" terminiology, when there's no reason this should be on the public API whatsoever: there is a "sage-like" object. I explicitly discussed this in spec comments. lift_vector makes no sense: it is not just a random QQ-vector. It is an element of L^*. No object should REQUIRE a sage-like object in the constructor, they always STORE one by simple creating it internally and storing it, AND have a classmethod that takes a sage object and does the conversion internally. You allowed variable numbers of args (wrong), imported old sage-like constructs like modulus and modulus_qf. You left assertions in instead of using proper validation, discussed extensively in spec. You left in things I CLEARLY discussed as mathematically ill-defined, like p-rank, with a totally nonsensical algorithm that makes no sense in general. You put delta/coparity as invariants on A_L, when they are invariants of the LATTICES L. You left in SHIMS to old methods, like has_isomorphic_group_structure_to, the spec CLEARLY defined the correct names to migrate to. You made hom require images, which is semantically completely wrong, because that produces an ELEMENT of the hom space. Discussed at length already. You did not extend ANY sagemath constructs like homset or morphism like I required. You left out ALL of the hom and morphism methods I described. You used assert False to avoid creating proper objects: I explicitly described how e.g. cokernels need to CONSTRUCT the correct objects. It CAN be a lattice, or a torsion bilinear form. cokernel is completely wrong, and does not construct the cokernel correctly as discussed -- you construct an orthogonal complement, which is WILDLY wrong, and completely fails to construct A_L := coker(L -> L^*) correctly. projection_lattice is completely ill-defined in general: a lattice does not "project" onto a sublattice. There is no map. You forced dual lattices to only be quotientable by the original lattice, but this is wrong, they are rational lattices and can be quotiented by anything. This just defers to the cokernel of the inclusion. You expose and leak private data with methods that pipe into the underlying sage object, instead of forucing extracting the sage object if you want the "sage-native" objects, which should be almost NEVER. "outside_domain" is just is_p_elementary(2). methods like vec_to_list are braindead, there is NO reason to ever use this when you should be using lattice elements and manually extracting their coordinates when needed, and noting the fact that list(v.to_vector()) naturally works when v.to_vector() is a sage vector. Methods like _definite_orthogonal_group_generators are ill-placed, because the proper semantics is L.orthogonal_group().gens(). You are asserting matrix equations for isometries, which is totally wrong, you are supposed to do this in one place: the containment function for O(L). Stabilizers go on O(L), e.g. L.orthogonal_group().stabilizer(v), as do other related verbs.  You use isinstance and hasattr instead of properly typing and dispatching on inputs. You need to read the spec, the comments, the intended semantics and public API, start by stubbing out a subdir HIERARCHY with touched files for the various levels of the API, and then proceed to migrate the EXISTING code into the smaller organized hierarchy of files, then fix all of these issues

## Additional Raw Corrections

Recorded on 2026-04-13. Preserved verbatim from the user messages.

> And morphisms can not "contain" anything...

> a morphism can not have a "perp" either

> You also have most methods too far down the hierarchy: almost everything makes sense for objects in BilinearModules, their morphisms, hom spaces, etc

> That's not right. BilinearModules is a new category. It has its own elements and morphisms. It is the category of pairs (M, \beta) where M is an finitely generated R-module, R is a PID, and \beta is a bilinear form on M. So you might as well hook a new category properly, emulating https://github.com/sagemath/sage/blob/develop/src/sage/categories/modules.py

## Framing Corrections

Recorded on 2026-04-13. Preserved verbatim from the user messages.

> Wait, what the fuck do you mean "aspirational"? That is the SPEC

> What do you mean "the spec *can* be ahead of the implementation"? Do you not understand what "spec" means?

> Wait, what do you mean when you say these are "blockers"...? This is the spec. You aren't finished implementing it. You keep stopping midway, as I keep pointing out. Nothing is "blocked"

> Make sure the plan and documents are clear about everything I've corrected you on in the last few turns

## Non-Negotiable Preservation Rule

The generated redesign code must be reorganized and corrected, not discarded
wholesale. The correct procedure is:

- stub the intended hierarchy,
- migrate the existing generated code into the smaller hierarchy,
- then repair the semantics, validation, typing, and mathematical design
  defects listed above.

## Source of Truth Rule

When future work is done on the lattice redesign, consult
`lattice-interface-style-guide.md`, `category-abc-spec.md`, and
`src.bak/spec-backups/lattices_written_spec_backup.py` before changing the
public interface.
