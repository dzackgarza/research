r"""Isometries of integral lattices."""

from sage.matrix.constructor import matrix
from sage.rings.integer_ring import ZZ as SageZZ
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Iterable
    from sage.structure.parent import MembershipInput

from dzack_research.preamble.categories.modules.module_morphisms.morphism_matrices import MorphismMatrix
if TYPE_CHECKING:
    from dzack_research.preamble.lexicon import Element
    from dzack_research.preamble.lexicon import RingElement
    from sage.categories.groups import Group
    from sage.rings.integer import Integer
    from sage.structure.parent import Parent
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModule

if TYPE_CHECKING:
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormMorphism
    from sage.groups.matrix_gps.finitely_generated_gap import (
        FinitelyGeneratedMatrixGroup_gap,
    )
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleAutomorphism
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleAutomorphismGroup
    from sage.categories.morphism import Morphism
    from dzack_research.preamble.categories.sets.sets import Set

from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormAutomorphismGroup
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import AutomorphismSubgroup
from typing import Protocol, TYPE_CHECKING

from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.sets.cardinals import Cardinal
from dzack_research.preamble.categories.modules.module_morphisms.morphism_matrices import matrix_group
from dzack_research.preamble.owned_category_bases import Category
from sage.categories.groups import Groups as SageGroups
from sage.quadratic_forms.quadratic_form import QuadraticForm as SageQuadraticForm
from sage.sets.totally_ordered_finite_set import TotallyOrderedFiniteSet

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import OrderedSet

    from collections.abc import Iterator

    from sage.libs.gap.element import GapElement

    class IsometryGroupParent(Protocol):
        r"""What $O(L)$ and its subgroups offer.

        A homset whose elements are the isometries, so the lattice it acts on
        is read off the arrow: ``domain()``.
        """

        _group_generators: TotallyOrderedFiniteSet
        _finite_presentation_relations: tuple

        def domain(self) -> "FormModule": ...
        def is_finite(self) -> bool: ...
        def is_countable(self) -> bool: ...
        def one(self) -> "FormMorphism": ...
        def cardinality(self) -> "Cardinal": ...
        def group_generators(self) -> TotallyOrderedFiniteSet["FormMorphism"]: ...
        def subgroup_on(self, group_generators: "Set") -> "LatticeIsometrySubgroup": ...
        def presenting_free_group(self) -> "Group": ...
        def _isometry_on_rows(self, rows: "Iterable") -> "FormMorphism": ...
        def _matrix_group(self) -> "FinitelyGeneratedMatrixGroup_gap": ...
        def _defining_matrix_group(self) -> "FinitelyGeneratedMatrixGroup_gap": ...
        def __call__(self, images: "dict | FormMorphism") -> "FormMorphism": ...
        def __contains__(self, candidate: "MembershipInput") -> bool: ...

    class IsometryMorphism(Protocol):
        r"""What one isometry offers."""

        def parent(self) -> "IsometryGroupParent": ...
        def domain(self) -> "FormModule": ...
        def matrix(self) -> "MorphismMatrix": ...
        def is_identity(self) -> bool: ...
        def __mul__(self, other: "IsometryMorphism") -> "FormMorphism": ...
        def __call__(self, element: "Element") -> "Element": ...


def _definite_isometry_group_generator_matrices(lattice: "FormModule") -> tuple:
    r"""Return matrices generating \(O(L)\), for a definite \(L\).

    \(O(L)=\{M:MGM^t=G\}\) is a condition on the Gram matrix and on nothing
    else, so this is a call to the engine's algorithm with a matrix -- the way
    :meth:`IntegralLattices.ParentMethods.genus` is -- and not a passage into
    the engine's lattice objects.  The algorithm is Plesken--Souvignier, which
    the engine reaches through the quadratic form \(2G\); the doubling is the
    passage from the bilinear form to the quadratic one, and the sign is the
    lattice's, since \(O(L)=O(L(-1))\) and the algorithm wants the positive
    definite representative.

    A row of each matrix is the image of a framing label, which is the
    convention the whole preamble reads a morphism matrix in.  The engine's
    quadratic forms act on columns, hence the transpose -- and nothing rests
    on getting that right silently: a morphism is built from these matrices
    below, and its constructor rejects a map that does not preserve the form.

    Definite is the hypothesis and not a preference: Plesken--Souvignier is a
    definite-forms algorithm.  The indefinite regime has its own engine --
    polyhedral_common's ``INDEF_FORM_AutomorphismGroup`` behind
    :mod:`engines`, routed by :func:`_isometry_group_generator_matrices` --
    and when that engine is unprovisioned no generating set is in hand:
    :mod:`predicate_subgroups` exists because computing one by search for a
    common indefinite lattice runs for days.  That \(O(L)\) is nevertheless
    finitely generated is Borel and Harish-Chandra's theorem, which is why
    the group is placed in the category of finitely generated groups without
    being asked to exhibit anything.
    """
    positive, negative = lattice.signature_pair()
    assert positive + negative == lattice.rank() and 0 in (positive, negative), (
        f"{lattice} is not definite, so no generating set of O(L) is in hand. "
        "Name a subgroup by its generators, or cut one out by a membership "
        "predicate"
    )
    gram = matrix(SageZZ, lattice.gram_matrix())
    quadratic_form = SageQuadraticForm(SageZZ, -2 * gram if positive == 0 else 2 * gram)
    # Over the integers, which the engine's quadratic forms do not say: an
    # isometry of an integral lattice permutes the lattice, so its matrix in
    # an integral framing has integral entries, and reading it over the
    # rationals would make the images rational combinations of generators.
    return tuple(
        generator.matrix().transpose().change_ring(SageZZ)
        for generator in quadratic_form.automorphism_group().gens()
    )


def _isometry_group_generator_matrices(lattice: "FormModule") -> tuple:
    r"""Return matrices generating \(O(L)\), routed by signature.

    One question, two engines: Plesken--Souvignier (PARI, through Sage's
    quadratic forms) on the definite regime,
    polyhedral_common's ``INDEF_FORM_AutomorphismGroup`` (behind
    :mod:`engines`) on the indefinite one.  Either engine's output is
    row-convention generator matrices verified against the Gram matrix
    before an isometry is built from them.
    """
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.engines import (
        indefinite_orthogonal_group_generator_matrices,
        polyhedral_engine,
    )
    positive, negative = lattice.signature_pair()
    if 0 in (positive, negative):
        return _definite_isometry_group_generator_matrices(lattice)
    assert polyhedral_engine() is not None, (
        f"O({lattice}) is indefinite; its generating set is the "
        "polyhedral_common engine's (INDEF_FORM_AutomorphismGroup), which is "
        "not provisioned -- see engines.sage.  Name a subgroup by its "
        "generators, or cut one out by a membership predicate"
    )
    return indefinite_orthogonal_group_generator_matrices(
        matrix(SageZZ, lattice.gram_matrix())
    )


class LatticeIsometries(Category):
    r"""Invertible lattice homomorphisms.

    A group, as an object: the parents here are \(O(L)\) and its subgroups.
    Composition of lattice automorphisms is the group law.  Thus the owned
    group category is a super category rather than a
    declaration made again at each construction, and the words a group
    answers -- ``number_of_group_generators``, ``is_finitely_generated`` --
    reach these objects because they are groups and not because anything was
    written on them here.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "lattice isometries"

    def super_categories(self) -> list:
        r"""Return the homomorphism and finitely generated group categories.

        Finitely generated and not merely a group: every object here has a
        finite generating set.  A subgroup was named by one, and \(O(L)\) has
        one by Borel and Harish-Chandra.  Not finitely *presented*, which
        \(O(L)\) itself carries and its subgroups do not: a finitely generated
        subgroup of a finitely presented group need not be finitely presented.

        Stating it here is also what orders the methods.  The finitely
        category of finitely generated groups answers ``group_generators`` by reading Sage's
        ``gens``, which these groups do not have -- they compute their
        generators from the Gram matrix -- and a category that this one
        declares as a super category is a category this one's methods
        precede.
        """
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.framed.formed.integrallattice.lattice_homomorphisms import LatticeHomomorphisms
        from dzack_research.preamble.categories.group.groups import OwnedFinitelyGeneratedGroups
        return [LatticeHomomorphisms(), OwnedFinitelyGeneratedGroups()]

    class ParentMethods:
        def is_countable(self: "IsometryGroupParent") -> bool:
            r"""Whether the isometries admit an enumeration.  Always.

            $O(L)$ is a subgroup of $\mathrm{GL}_n(\mathbb Z)$, which is a
            countable set (integer matrices are tuples of integers), so
            every isometry group here is countable -- finite or not.
            """
            return True

        def is_uncountable(self: "IsometryGroupParent") -> bool:
            r"""Whether the isometries are beyond every enumeration."""
            return not self.is_countable()

        def structure_description(self: "IsometryGroupParent") -> str:
            r"""Return GAP's structure description of a finite isometry group.

            A human-readable isomorphism type (``"C2 x S5"``), computed by
            GAP behind the matrix-group boundary.  Descriptive, not
            canonical: GAP documents that non-isomorphic groups can share a
            description, so this is a label for the mathematician, never a
            datum an equality is decided on.
            """
            assert self.is_finite(), (
                "GAP's StructureDescription is finite-group vocabulary"
            )
            return str(self._matrix_group().structure_description())

        def __call__(self: "IsometryGroupParent", images: "dict | FormMorphism") -> "Morphism":
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormMorphism
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.lattice_homomorphisms import LatticeHomomorphisms
            from dzack_research.preamble.refine import refine
            if isinstance(images, FormMorphism):
                # A homset is a parent and its morphisms are its elements, so
                # being handed one is a parent constructing an element it
                # already has.  Coercion discovery and ``an_element`` both ask
                # for exactly this; declaring it again through framing labels
                # would only rebuild what was passed in.
                assert images.domain() is self.domain(), (
                    f"{images} is not an isometry of {self.domain()}"
                )
                held: "Morphism" = images
                return held
            morphism = LatticeHomomorphisms.ParentMethods.__call__(
                self,
                images,
            )
            determinant = morphism.matrix().det()
            assert determinant in (1, -1), (
                f"an integral isometry has unit determinant, got {determinant}"
            )
            isometry: "Morphism" = refine(morphism, LatticeIsometries())
            return isometry

        def one(self: "IsometryGroupParent") -> "ModuleAutomorphism":
            return self(
                {
                    label: self.domain().module_generator(label)
                    for label in self.domain().module_generating_set()
                }
            )

        def an_element(self: "IsometryGroupParent") -> "ModuleAutomorphism":
            r"""Return the identity.

            Sage's generic ``_an_element_`` probes with ``self(0)``,
            ``self(1)`` and so on, which for an isometry group means
            declaring a lattice morphism from an integer.  A group has a
            distinguished element and this is it.
            """
            identity: "ModuleAutomorphism" = self.one()
            return identity

        def subgroup_on(self: "IsometryGroupParent", group_generators: "Set") -> "LatticeIsometrySubgroup":
            r"""Return the subgroup generated by a *set* of isometries."""
            assert all(generator in self for generator in group_generators), (
                "each subgroup generator must belong to this isometry group"
            )
            return LatticeIsometrySubgroup(self, group_generators)

        def discriminant_image(self: "IsometryGroupParent") -> "Parent":
            r"""Return $\rho_L(G)\le O(A_L)$: this group's image on the discriminant form.

            The image of the discriminant representation
            (:meth:`IntegralLattices.ParentMethods.discriminant_representation`;
            FOUNDATIONS Defs 26.1/26.3; Nik80 §§3°–4°, Zotero TTY9FFJS)
            restricted to this group: the subgroup of the finite $O(A_L)$
            generated by the group generators' induced automorphisms.  A
            homomorphic image is generated by the images of the generators,
            so the answer is grounded exactly where ``group_generators`` is
            -- on the full $O(L)$ that is the engine's definite regime, on a
            generated subgroup always.
            """
            form = self.domain().discriminant_group()
            return form.automorphism_group().subgroup_on(
                tuple(
                    generator.discriminant_morphism()
                    for generator in self.group_generators()
                )
            )

        # ---- characters' kernels and stabilizers, as predicate subgroups ----
        #
        # A subgroup of O(L) for an indefinite L cannot be handed over by
        # generators, so each of these is the predicate that decides
        # membership (predicate_subgroups.sage), together with the character
        # data the finite-quotient orbit machinery consumes
        # (isotropic_orbits.sage).

        def special_orthogonal_subgroup(self: "IsometryGroupParent") -> "Parent":
            r"""Return $SO(L)=\ker(\det: O(L)\to\{\pm1\})$.

            The special orthogonal group: the index-2 subgroup of isometries
            of determinant $+1$ (Dawes 2021 §1.2, via the migrated glossary).
            Cut out by the determinant character on
            :meth:`MorphismMethods.determinant`.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.isotropic_orbits import OrthogonalPredicateSubgroup
            return OrthogonalPredicateSubgroup(
                self,
                lambda isometry: isometry.determinant() == 1,
                "det(g) = 1",
                determinant_kernel=True,
            )

        def spinor_kernel_subgroup(self: "IsometryGroupParent") -> "Parent":
            r"""Return $O^+(L)$: the kernel of the real spinor norm.

            $O^+(L\otimes\mathbb R)$ is the kernel of the spinor norm on
            $O(L\otimes\mathbb R)$, and for a hyperbolic lattice it is the
            index-2 subgroup preserving the positive cone (Dawes 2021 §1.2,
            via the migrated glossary); $O^+(L)$ is its intersection with
            $O(L)$.  Cut out by
            :meth:`MorphismMethods.real_spinor_norm_sign`, whose docstring
            states the convention and its relation to
            :meth:`MorphismMethods.preserves_positive_cone`.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.isotropic_orbits import OrthogonalPredicateSubgroup
            return OrthogonalPredicateSubgroup(
                self,
                lambda isometry: isometry.real_spinor_norm_sign() == 1,
                "the real spinor norm of g is positive",
                spinor_kernel=True,
            )

        def discriminant_preimage(
            self: "IsometryGroupParent", subgroup: "Parent"
        ) -> "Parent":
            r"""Return $\rho_L^{-1}(H)$ for $H\le O(A_L)$, as a predicate subgroup.

            The preimage under the discriminant representation -- the shape
            of every arithmetic group in the Enriques/Coble program (the
            degree-two Enriques group is
            $\rho^{-1}(\operatorname{Stab}(h/2))\cap O^+$).  Membership is
            $\rho_L(g)\in H$, decided on the finite $O(A_L)$; no generating
            set of the preimage is needed, or claimed.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.isotropic_orbits import OrthogonalPredicateSubgroup
            from dzack_research.preamble.categories.modules.framed.formed.torsionform.torsion_modules_with_form import (
                TorsionFormAutomorphismGroup,
                TorsionFormAutomorphismSubgroup,
            )
            assert isinstance(
                subgroup,
                (TorsionFormAutomorphismGroup, TorsionFormAutomorphismSubgroup),
            ), "the preimage is taken of a subgroup of O(A_L)"
            assert subgroup.domain() is self.domain().discriminant_group(), (
                "the subgroup must live on this lattice's discriminant form"
            )
            return OrthogonalPredicateSubgroup(
                self,
                lambda isometry: isometry.discriminant_morphism() in subgroup,
                f"rho(g) lies in {subgroup}",
                discriminant_preimages=(subgroup,),
            )

        def stabilizer_of_vector(
            self: "IsometryGroupParent", element: "Element"
        ) -> "Parent":
            r"""Return $\{g: g(v)=v\}$, the pointwise stabilizer of a vector."""
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.isotropic_orbits import OrthogonalPredicateSubgroup
            lattice = self.domain()
            vector = element if element.parent() is lattice else lattice(element)
            return OrthogonalPredicateSubgroup(
                self,
                lambda isometry: isometry(vector) == vector,
                f"g fixes {vector}",
            )

        def stabilizer_of_isotropic_line(
            self: "IsometryGroupParent", element: "Element"
        ) -> "Parent":
            r"""Return the setwise stabilizer of the isotropic line $\mathbb Zv$.

            A 0-cusp datum: the lines are the rank-1 primitive totally
            isotropic sublattices.  $g$ preserving $\mathbb Zv$ sends $v$ to
            $\pm v$ ($v$ primitive; the units of $\mathbb Z$).
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.isotropic_orbits import OrthogonalPredicateSubgroup
            lattice = self.domain()
            vector = element if element.parent() is lattice else lattice(element)
            assert vector.q() == 0, (
                f"{vector} is not isotropic; this stabilizer is 0-cusp vocabulary"
            )
            return OrthogonalPredicateSubgroup(
                self,
                lambda isometry: isometry(vector) in (vector, -vector),
                f"g preserves the line through {vector}",
            )

        def stabilizer_of_isotropic_plane(
            self: "IsometryGroupParent", elements: "OrderedSet"
        ) -> "Parent":
            r"""Return the setwise stabilizer of a totally isotropic plane.

            A 1-cusp datum.  The plane is the subobject the two vectors
            span; $g$ stabilizes it exactly when $g$ maps the subobject into
            itself -- into suffices, since $g(S)\subseteq S$ for invertible
            $g$ forces $g(S)=S$ (the chain $f^{-n}S$ ascends in the finite-
            index saturation, so the index is 1).
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.isotropic_orbits import OrthogonalPredicateSubgroup
            lattice = self.domain()
            vectors = tuple(
                element if element.parent() is lattice else lattice(element)
                for element in elements
            )
            assert len(vectors) == 2, "a plane is spanned by two vectors"
            plane = lattice.subobject_on(vectors)
            assert all(
                left.b(right) == 0 for left in vectors for right in vectors
            ), "the plane is not totally isotropic"
            return OrthogonalPredicateSubgroup(
                self,
                lambda isometry: isometry.preserves(plane),
                f"g preserves the plane on {vectors}",
            )

        def stabilizer_of_isotropic_flag(
            self: "IsometryGroupParent", elements: "OrderedSet"
        ) -> "Parent":
            r"""Return the stabilizer of the full isotropic flag the vectors generate.

            The flag is the chain $S_1\subset S_2\subset\cdots$ of subobjects
            spanned by the initial segments; the stabilizer preserves *every*
            term, which is strictly finer than preserving the total span
            (the source corpus's flag validation compared total spans only, a
            recorded error corrected here).
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.isotropic_orbits import OrthogonalPredicateSubgroup
            lattice = self.domain()
            vectors = tuple(
                element if element.parent() is lattice else lattice(element)
                for element in elements
            )
            assert vectors, "a flag has at least one term"
            assert all(
                left.b(right) == 0 for left in vectors for right in vectors
            ), "the flag is not totally isotropic"
            terms = tuple(
                lattice.subobject_on(vectors[: depth + 1])
                for depth in range(len(vectors))
            )
            return OrthogonalPredicateSubgroup(
                self,
                lambda isometry: all(
                    isometry.preserves(term) for term in terms
                ),
                f"g preserves every term of the flag on {vectors}",
            )

        # ---- orbits of isotropic subobjects, engine behind the seam ----

        def vector_orbit_representatives(
            self: "IsometryGroupParent", square: "RingElement"
        ) -> tuple:
            r"""Return one lattice element per $O(L)$-orbit of vectors of the
            given square, as the engine enumerates them.

            Finitely many for an indefinite lattice (the migrated finiteness
            note is ``notes/topics/coble-enriques-lattice-theory/``
            ``finiteness-orbits-indefinite-lattices.md``); each
            representative's square is verified at the seam
            (:func:`engines.indefinite_vector_orbit_representative_rows`).
            Orbits of *vectors*, not of lines: $v$ and $-v$ may or may not
            share an orbit, and :meth:`isotropic_line_orbit_representatives`
            is the line-level question at square $0$.  Implemented on the
            full $O(L)$; a subgroup containing $\ker\varphi$ splits these
            $O(L)$-orbits by double cosets in its finite quotient.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.engines import indefinite_vector_orbit_representative_rows
            assert self is self.domain().Aut(), (
                "orbit enumeration is O(L)'s; ask a subgroup containing "
                "ker(phi) for its own splitting"
            )
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.utilities import zipsum
            lattice = self.domain()
            return tuple(
                zipsum(row, lattice.module_generators(), lattice.zero())
                for row in indefinite_vector_orbit_representative_rows(
                    lattice.gram_matrix(), square
                )
            )

        def isotropic_line_orbit_representatives(
            self: "IsometryGroupParent",
        ) -> tuple:
            r"""Return one primitive isotropic vector per $O(L)$-orbit of lines.

            The 0-cusps of the Baily--Borel boundary for this group.  The
            engine's representatives are validated against the owned lattice
            (isotropy, primitivity) before they leave
            (:func:`isotropic_orbits.orthogonal_group_isotropic_orbit_representatives`).
            Implemented on the full $O(L)$; a subgroup containing
            $\ker\varphi$ splits these $O(L)$-orbits by double cosets in its
            finite quotient, and a subgroup given only by its membership
            predicate states the absence.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.isotropic_orbits import orthogonal_group_isotropic_orbit_representatives
            assert self is self.domain().Aut(), (
                "orbit enumeration is O(L)'s; ask a subgroup containing "
                "ker(phi) for its own splitting"
            )
            return tuple(
                flag[0]
                for flag in orthogonal_group_isotropic_orbit_representatives(
                    self.domain(), 1, "plane"
                )
            )

        def isotropic_plane_orbit_representatives(
            self: "IsometryGroupParent",
        ) -> tuple:
            r"""Return one basis pair per $O(L)$-orbit of totally isotropic planes.

            The 1-cusps.  Each representative is a pair of lattice elements
            spanning the plane, validated at the seam.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.isotropic_orbits import orthogonal_group_isotropic_orbit_representatives
            assert self is self.domain().Aut(), (
                "orbit enumeration is O(L)'s; ask a subgroup containing "
                "ker(phi) for its own splitting"
            )
            return orthogonal_group_isotropic_orbit_representatives(
                self.domain(), 2, "plane"
            )

        def isotropic_flag_orbit_representatives(
            self: "IsometryGroupParent", depth: "Integer"
        ) -> tuple:
            r"""Return one ordered basis per $O(L)$-orbit of isotropic ``depth``-flags."""
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.isotropic_orbits import orthogonal_group_isotropic_orbit_representatives
            assert self is self.domain().Aut(), (
                "orbit enumeration is O(L)'s; ask a subgroup containing "
                "ker(phi) for its own splitting"
            )
            return orthogonal_group_isotropic_orbit_representatives(
                self.domain(), depth, "flag"
            )

        def isotropic_lines_are_equivalent(
            self: "IsometryGroupParent", left: "Element", right: "Element"
        ) -> bool:
            r"""Decide whether two primitive isotropic lines lie in one $O(L)$-orbit."""
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.isotropic_orbits import orthogonal_group_line_equivalence_witness
            assert self is self.domain().Aut(), (
                "orbit equivalence is O(L)'s; ask a subgroup containing "
                "ker(phi) for the double-coset decision"
            )
            return (
                orthogonal_group_line_equivalence_witness(self.domain(), left, right)
                is not None
            )

        def isotropic_planes_are_equivalent(
            self: "IsometryGroupParent",
            left: "OrderedSet",
            right: "OrderedSet",
        ) -> bool:
            r"""Decide whether two totally isotropic planes lie in one $O(L)$-orbit."""
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.isotropic_orbits import orthogonal_group_sublattice_equivalence_witness
            assert self is self.domain().Aut(), (
                "orbit equivalence is O(L)'s; ask a subgroup containing "
                "ker(phi) for the double-coset decision"
            )
            return (
                orthogonal_group_sublattice_equivalence_witness(
                    self.domain(), left, right, "plane"
                )
                is not None
            )

        def isotropic_flags_are_equivalent(
            self: "IsometryGroupParent",
            left: "OrderedSet",
            right: "OrderedSet",
        ) -> bool:
            r"""Decide whether two isotropic flags lie in one $O(L)$-orbit.

            Flag equivalence, not total-span equivalence: the witness must
            send every term of the flag to its counterpart, which the seam
            checks term by term.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.isotropic_orbits import orthogonal_group_sublattice_equivalence_witness
            assert self is self.domain().Aut(), (
                "orbit equivalence is O(L)'s; ask a subgroup containing "
                "ker(phi) for the double-coset decision"
            )
            return (
                orthogonal_group_sublattice_equivalence_witness(
                    self.domain(), left, right, "flag"
                )
                is not None
            )

        def _isometry_on_rows(self: "IsometryGroupParent", rows: "Iterable") -> "FormMorphism":
            r"""Return the isometry sending each framing label to a row's combination.

            The one place a matrix becomes an element of this group.  A row is
            read against the module generators, so what crosses back from the
            engine is a morphism of this lattice and never a matrix a caller
            would have to interpret.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.utilities import zipsum
            lattice = self.domain()
            return self(
                {
                    label: zipsum(row, lattice.module_generators(), lattice.zero())
                    for label, row in zip(lattice.module_generating_set(), rows)
                }
            )

        def group_generators(
            self: "IsometryGroupParent",
        ) -> TotallyOrderedFiniteSet["FormMorphism"]:
            r"""Return \(S\) with \(\langle S\rangle\) this group.

            One question with two sources and one answer.  A subgroup was
            named by its generators and holds them; the full \(O(L)\) was not,
            so its generators are the ones the engine computes from the Gram
            matrix -- and once computed they are held the same way, which is
            what makes ``has_computed_group_generators`` true of both.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.sets.sets import finite_ordered_set
            stored: TotallyOrderedFiniteSet["FormMorphism"] | None = (
                self.__dict__.get("_group_generators")
            )
            if stored is None:
                stored = finite_ordered_set(
                    tuple(
                        self._isometry_on_rows(entries.rows())
                        for entries in
                        _isometry_group_generator_matrices(self.domain())
                    )
                )
                self._group_generators = stored
            return stored

        @cached_method
        def _matrix_group(
            self: "IsometryGroupParent",
        ) -> "FinitelyGeneratedMatrixGroup_gap":
            r"""Return this group as a GAP-backed matrix group.  The private model.

            \(O(L)\) is cut out of \(GL_n(R)\) by \(MGM^t=G\), so it and every
            subgroup of it is a matrix group on its generators' matrices.
            Deciding order, finiteness and enumeration from generators is
            Schreier--Sims and coset enumeration -- mature algorithms this
            repo calls and never restates.  Every method below defers here and
            translates the answers back into this group's own elements.
            """
            gap_group: "FinitelyGeneratedMatrixGroup_gap" = matrix_group(
                generator.matrix() for generator in self.group_generators()
            )
            return gap_group

        def _defining_matrix_group(
            self: "IsometryGroupParent",
        ) -> "FinitelyGeneratedMatrixGroup_gap":
            r"""Return the GAP model ``_libgap_`` converts through.

            On the full \(O(L)\) this is the matrix model itself, admissible
            exactly where the group is finite -- GAP's character machinery is
            finite-group vocabulary.  ``LatticeIsometrySubgroup`` inherits a
            finer version from ``AutomorphismSubgroup``, which precedes this
            one in the MRO.
            """
            assert self.is_finite(), (
                "the GAP model backing _libgap_ is finite-group vocabulary; "
                f"{self} is not known finite"
            )
            return self._matrix_group()

        @cached_method
        def presenting_free_group(self: "IsometryGroupParent") -> "Group":
            r"""Return the free group in a computed presentation of this group.

            A presentation is what coset enumeration produces, and the
            algorithm wants a permutation action to enumerate over, so the
            matrix group is realised as one first.  Both steps are the
            engine's.  Producing one at all needs the group enumerated, which
            is the definite case -- the same hypothesis
            :func:`_definite_isometry_group_generator_matrices` states, and
            for the same reason.  That \(O(L)\) *has* a finite presentation
            regardless is Borel and Harish-Chandra's theorem.

            The temporary Sage quotient supplies data only.  This object
            remains the isometry group and receives the free group and
            relators directly.
            """
            presented = (
                self._matrix_group()
                .as_permutation_group()
                .as_finitely_presented_group()
            )
            self._finite_presentation_relations = tuple(presented.relations())
            return presented.free_group()

        @cached_method
        def defining_relations(self: "IsometryGroupParent") -> "OrderedSet":
            r"""Return the relators in :meth:`presenting_free_group`."""
            from dzack_research.preamble.categories.sets.sets import finite_ordered_set

            self.presenting_free_group()
            return finite_ordered_set(self._finite_presentation_relations)

        def is_finite(self: "IsometryGroupParent") -> bool:
            r"""Return whether this group is finite, as decided by GAP."""
            return bool(self._matrix_group().is_finite())

        def cardinality(self: "IsometryGroupParent") -> "Cardinal":
            r"""Return \(|G|\), as computed by GAP."""
            return Cardinal(self._matrix_group().order())

        def order(self: "IsometryGroupParent") -> "Cardinal":
            r"""Return \(|G|\).  The order of a group is its cardinality."""
            return self.cardinality()

        def __iter__(self: "IsometryGroupParent") -> "Iterator[FormMorphism]":
            r"""Enumerate this group's elements, which a finite group has."""
            assert self.is_finite(), (
                f"{self} is infinite, so it cannot be enumerated"
            )
            for element in self._matrix_group():
                yield self._isometry_on_rows(element.matrix().rows())

    class MorphismMethods:
        def to_matrix(self: "IsometryMorphism") -> "MorphismMatrix":
            return self.matrix()

        def is_identity(self: "IsometryMorphism") -> bool:
            identity: bool = self.matrix().is_one()
            return identity

        def is_involution(self: "IsometryMorphism") -> bool:
            involution: bool = (self * self).is_identity()
            return involution

        def determinant(self: "IsometryMorphism") -> "Integer":
            r"""Return $\det(g)\in\{\pm1\}$: the determinant character.

            A character $O(L)\to\{\pm1\}$ whose kernel is the special
            orthogonal group $SO(L)$
            (:meth:`ParentMethods.special_orthogonal_subgroup`).  An
            integral isometry has unit determinant, asserted at
            construction, so the value is $\pm1$ by membership.
            """
            value: "Integer" = SageZZ(self.matrix().det())
            return value

        def real_spinor_norm_sign(self: "IsometryMorphism") -> "Integer":
            r"""Return the sign of the real spinor norm of this isometry.

            Writing $g=\sigma_{w_1}\cdots\sigma_{w_m}$ as a product of
            reflections over $\mathbb R$, the real spinor norm is
            $\prod_i[-(w_i,w_i)/2]\in\mathbb R^*/(\mathbb R^*)^2$,
            well-defined independently of the decomposition (Dawes 2021
            §1.2, transcribed in the migrated glossary).  Its kernel is
            $O^+(L)$, and for a hyperbolic lattice that kernel is exactly
            the positive-cone-preserving subgroup -- so for signature
            $(1,n)$ this character and
            :meth:`preserves_positive_cone` agree, a theorem and not a
            shared implementation.

            Computed through the OSCAR seam
            (:func:`engines.oscar_rational_spinor_norm_sign`), whose
            ``rational_spinor_norm`` values $\sigma_w$ at $[(w,w)]$ instead
            -- the two conventions differ by the determinant character
            (on $U$: $\sigma_{e+f}$ has $(w,w)=2$, OSCAR sign $+1$, and
            reverses the cone; $\sigma_{e-f}$ has $(w,w)=-2$, OSCAR sign
            $-1$, and preserves it) -- so the seam's sign is multiplied by
            $\det(g)$ here.  The source corpus computed the two characters
            in two branches of one function under one name, a recorded
            error this separation corrects.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.engines import oscar_rational_spinor_norm_sign
            lattice = self.domain()
            oscar_sign = oscar_rational_spinor_norm_sign(
                matrix(SageZZ, lattice.gram_matrix()),
                matrix(SageZZ, self.matrix()),
            )
            sign: "Integer" = SageZZ(oscar_sign) * self.determinant()
            return sign

        def preserves_positive_cone(self: "IsometryMorphism") -> bool:
            r"""Return whether this isometry preserves the positive cone.

            For signature $(1,n)$ the set $\{v\in L\otimes\mathbb R:
            (v,v)>0\}$ has two connected components (the two cones), and an
            isometry either preserves each or swaps them, decided by the
            sign of $(v, g(v))$ for any one positive-norm $v$: the pairing
            cannot vanish there, and its sign is constant on the component.
            The subgroup this character cuts out is $O^+(L)$, equal to the
            kernel of :meth:`real_spinor_norm_sign` -- computed
            independently, so the equality stays falsifiable.  For
            $p\ge 2$ the positivity domain is connected and there is no
            cone character, which is why the hypothesis is asserted rather
            than widened.
            """
            from sage.rings.rational_field import QQ as SageQQ
            from sage.quadratic_forms.quadratic_form import QuadraticForm

            lattice = self.domain()
            positive, negative = lattice.signature_pair()
            assert positive == 1 and negative >= 1, (
                "the positive cone has two components exactly for signature "
                f"(1, n); {lattice} has signature {(positive, negative)}"
            )
            gram = matrix(SageQQ, lattice.gram_matrix())
            _diagonal_form, change = QuadraticForm(
                SageQQ, 2 * gram
            ).rational_diagonal_form(return_matrix=True)
            positive_columns = [
                index
                for index in range(gram.nrows())
                if (
                    change.column(index) * gram * change.column(index)
                ) > 0
            ]
            assert len(positive_columns) == 1, (
                "rational diagonalization must exhibit exactly one positive "
                "direction for signature (1, n)"
            )
            cone_vector = change.column(positive_columns[0])
            image = cone_vector * matrix(SageQQ, self.matrix())
            pairing = cone_vector * gram * image
            assert pairing != 0, (
                "the pairing of a positive-norm vector with its image never "
                "vanishes for an isometry"
            )
            return bool(pairing > 0)

        def then(self: "IsometryMorphism", other: "FormMorphism") -> "FormMorphism":
            r"""Return $g\circ f$, sited by what the two factors are.

            A composite of isometries is an isometry: it preserves the form
            because both factors do, and it is invertible because both
            factors are.  So $g\circ f$ belongs to
            $\operatorname{Isom}(L, N)$ and answers the vocabulary of an
            isometry -- ``is_identity``, ``inverse``, ``determinant`` --
            which the general composition, siting every composite in
            $\operatorname{Hom}(L, N)$, leaves out of reach.

            The other factor need not be an isometry, and then neither is
            the composite: $f$ followed by an inclusion of finite index is
            an inclusion of finite index, and $f$ followed by a projection
            onto a discriminant group leaves the lattices altogether.  Both
            are read off the composite, which is the arrow being sited.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormMorphism
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.integral_lattices import IntegralLattices
            composite: "FormMorphism" = FormMorphism.then(self, other)
            codomain = composite.codomain()
            if codomain in IntegralLattices() and composite.matrix().is_invertible():
                admitted: "FormMorphism" = composite.domain().Isom(codomain)(composite)
                return admitted
            return composite

        def __mul__(self: "IsometryMorphism", other: "Element") -> "Element":
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormMorphism
            assert (
                isinstance(other, FormMorphism)
                and other.parent() is self.parent()
            ), "composition is internal to one isometry group"
            return self.parent()(
                {
                    label: self(other(other.domain().module_generator(label)))
                    for label in other.domain().module_generating_set()
                }
            )

        def inverse(self: "IsometryMorphism") -> "ModuleAutomorphism":
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.utilities import zipsum
            inverse_matrix = self.matrix().inverse().change_ring(SageZZ)
            return self.parent()(
                {
                    label: zipsum(
            row,
            self.domain().module_generators(),
            self.domain().zero(),
        )
                    for label, row in zip(
                        self.domain().module_generating_set(),
                        inverse_matrix.rows(),
                    )
                }
            )

        def discriminant_morphism(self: "IsometryMorphism") -> "FormMorphism":
            r"""Return $\operatorname{Disc}(f)$: the induced automorphism of $A_L$.

            The discriminant construction is a functor on cores (FOUNDATIONS
            Def 26.1; Nik80 §§3°–4°, Zotero TTY9FFJS), so it acts on
            isometries, and its value on this one is a morphism of the
            torsion-form category -- an element of $O(A_L)$, constructed in
            that group.

            The functor's value on a morphism is
            :meth:`~LatticeHomomorphisms.MorphismMethods.discriminant_isometry`,
            which is where the formula lives and where the receiving homset
            checks that the result preserves the form.  What this adds is the
            *parent*: at $L=M$ the value is an element of $O(A_L)$, which is
            what lets :meth:`ParentMethods.discriminant_image` generate a
            subgroup of $O(A_L)$ from it.
            """
            form = self.domain().discriminant_group()
            induced = self.discriminant_isometry()
            return form.automorphism_group()(
                {
                    label: induced(form.module_generator(label))
                    for label in form.module_generating_set()
                }
            )

        def centralizer_discriminant_image(self: "IsometryMorphism") -> "Parent":
            r"""Return $\rho_L\bigl(Z_{O(L)}(f)\bigr)\le O(A_L)$.

            The centralizer $Z_{O(L)}(f)$ itself is
            ``predicate_subgroups.centralizer(L.Aut(), f)``: a membership
            predicate, because an arithmetic group carries no generating set
            on offer.  Its *image* under the discriminant representation is
            nevertheless computable, and not by generating the centralizer:
            hermitian Miranda--Morrison theory computes it directly, which is
            what Hecke's ``image_centralizer_in_Oq`` runs (behind
            :func:`engines.oscar_centralizer_discriminant_image`).  Even
            lattices only -- the theory's own hypothesis.

            The subgroup is what this returns, and four things are checked at
            the boundary before it does: every crossed-back generator is an
            isometry of the owned $A_L$ (the engine's element constructor
            says so, or fails); every one commutes with $\rho_L(f)$, which
            it must, the image of a centralizer lying in the centralizer of
            the image; the generated subgroup has the order the engine
            reports; and the engine's own invariant and coinvariant ranks
            agree with the owned $L^{\langle f\rangle}$ and its orthogonal
            complement, computed here natively.

            Stated residual: the crossing identifies the engine's smith
            generators of $A_L$ with the owned ones in order.  The four
            checks above are what stands behind that identification --
            together they pin the subgroup up to an isometry of $A_L$
            commuting with $\rho_L(f)$ -- and they do not by themselves
            prove the two presentations are the same one.  A caller needing
            that certainty compares $\rho_L$-images of concrete isometries.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.engines import oscar_centralizer_discriminant_image
            from dzack_research.preamble.categories.sets.cardinals import Cardinal
            lattice = self.domain()
            assert lattice.is_even(), (
                "the image of a centralizer in O(A_L) is computed by "
                f"hermitian Miranda-Morrison theory, which needs L even; "
                f"{lattice} is odd, a stated absence"
            )
            form = lattice.discriminant_group()
            automorphism_group = form.automorphism_group()
            (
                generator_matrices,
                order,
                invariant_rank,
                coinvariant_rank,
            ) = oscar_centralizer_discriminant_image(
                matrix(SageZZ, lattice.gram_matrix()),
                matrix(SageZZ, self.matrix()),
            )
            action = self.cyclic_subgroup().inclusion()
            assert lattice.invariant_lattice(action).rank() == invariant_rank, (
                "the engine's invariant lattice and the owned L^<f> differ in "
                "rank"
            )
            assert (
                lattice.coinvariant_lattice(action).rank() == coinvariant_rank
            ), (
                "the engine's coinvariant lattice and the owned "
                "(L^<f>)-perp differ in rank"
            )
            generators = tuple(
                automorphism_group._from_engine(
                    automorphism_group._engine_group(generator_matrix)
                )
                for generator_matrix in generator_matrices
            )
            induced = self.discriminant_morphism()
            assert all(
                generator * induced == induced * generator
                for generator in generators
            ), (
                "an engine generator of the centralizer's image does not "
                "commute with rho_L(f)"
            )
            image = automorphism_group.subgroup_on(generators)
            assert image.cardinality() == Cardinal(order), (
                "the crossed-back generators do not generate a group of the "
                "order the engine reports"
            )
            return image

        def cyclic_subgroup(self: "IsometryMorphism") -> "Group":
            r"""Return \(\langle f\rangle\le O(L)\), the subgroup this generates.

            A group in its own right, and the \(G\) of the construction that
            names elements and takes what they generate; the action of that
            \(G\) on \(L\) is its own ``inclusion()``.  It is not the abstract \(C_n\):
            a caller who means an abstract group and a possibly unfaithful
            \(\rho\) constructs both, and hands \(\rho\) to ``with_action``.
            """
            return self.parent().subgroup_on({self})

        def _libgap_(self: "IsometryMorphism") -> "GapElement":
            r"""Return this isometry inside its group's GAP model.

            A character is a function on a group, and when that group is a
            literal subgroup of \(O(L)\) its elements are these isometries;
            declaring where they sit in GAP is what makes GAP's characters
            functions on them rather than on a parallel set of matrices a
            caller would have to translate for.  This is the conversion
            protocol ``ClassFunction`` evaluates through.
            """
            return self.parent()._defining_matrix_group()(self.matrix()).gap()

        gap = _libgap_


class LatticeIsometrySubgroup(
    AutomorphismSubgroup,
    FormAutomorphismGroup,
):
    r"""The subgroup of \(O(L)\) generated by a set of isometries.

    Generated, not finite.  An isometry of an indefinite lattice can have
    infinite order, and finite-order isometries can generate an infinite
    group -- two reflections whose product has infinite order generate an
    infinite dihedral group.  So the generating set is what this object
    knows, finite generation is what it carries, and finiteness is a
    question put to GAP, never a constructor invariant.
    """

    def __init__(self, supergroup: "Group", group_generators: "Set") -> None:
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.framed.formed.integrallattice.lattice_homomorphisms import LatticeHomomorphisms
        from dzack_research.preamble.categories.sets.sets import finite_ordered_set
        from dzack_research.preamble.refine import refine
        lattice = supergroup.domain()
        assert supergroup.codomain() is lattice, (
            "an isometry group is an endomorphism homset"
        )
        FormAutomorphismGroup.__init__(self, lattice)
        # A subgroup of \(O(L)\) is a group, and that is the whole placement.
        # Not ``Groups().Finite()``: refining into the finite subcategory
        # asserts a theorem, and one that is generally hard -- it needs
        # \(O(L)\) computed, or a definiteness hypothesis.  Cardinality is
        # not a reason to reach for it, being total on sets already.
        #
        # Finitely generated is the one axiom the constructor does witness:
        # the generating set is the argument.  The isometry node carries the
        # group vocabulary and the engine's own node carries the axiom, so
        # the placement is what makes this object answer as a group.
        refine(
            self,
            [
                LatticeHomomorphisms(),
                LatticeIsometries(),
                SageGroups().FinitelyGenerated(),
                SageGroups().Subobjects(),
            ],
        )
        assert group_generators, "a generated subgroup needs a generator"
        assert all(
            generator in supergroup for generator in group_generators
        ), "each subgroup generator must belong to the stated isometry group"
        self._group_generators = finite_ordered_set(
            [
                self(
                    {
                        label: generator(lattice.module_generator(label))
                        for label in lattice.module_generating_set()
                    }
                )
                for generator in group_generators
            ]
        )
        self._supergroup = supergroup

    def __contains__(self, element: "Element") -> bool:
        r"""Return whether ``element`` lies in this subgroup.

        Membership is the one operation always available on a group carved
        out of \(GL_n(R)\) by a condition, so it is decided directly rather
        than by searching an enumeration.
        """
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormMorphism
        return (
            isinstance(element, FormMorphism)
            and element.domain() is self.domain()
            # ``matrix`` converts through ``MorphismMatrix._matrix_``, the
            # owned protocol.  Asking the group directly would let Sage's
            # containment swallow the failed conversion and answer False for
            # an element that is present.
            and matrix(element.matrix()) in self._matrix_group()
        )

    def _repr_(self) -> str:
        return (
            f"Subgroup of O({self.domain()}) generated by "
            f"{self._group_generators.cardinality()} isometries"
        )
