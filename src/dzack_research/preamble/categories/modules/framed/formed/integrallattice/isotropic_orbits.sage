r"""Orbits of isotropic subobjects under $O(L)$ and its subgroups containing
$\ker\varphi$.

The 0- and 1-cusps of a Baily--Borel boundary are $\Gamma$-orbits of
primitive totally isotropic sublattices of rank 1 and 2, so the objects here
are those sublattices and the flags of them, and the questions are orbit
enumeration and equivalence -- under the full $O(L)$, and under the
arithmetic subgroups the Enriques/Coble program names by characters
(determinant, real spinor norm) and by preimages under the discriminant
representation.

Naming, fixed once and used throughout.  A *line* is a rank-one primitive
totally isotropic sublattice $\mathbb Zv\subseteq L$ and a *plane* is a
rank-two one; both are sublattices of $L$ and neither is a subspace.  The
engine behind :mod:`engines` does work with subspaces -- it compares
$\mathbb Q$-spans, that is subspaces of $L\otimes\mathbb Q$ -- and the two
questions agree exactly because every representative here is primitive,
hence saturated.

:class:`OrthogonalPredicateSubgroups` is the home of every orbit question a
subgroup containing $\ker\varphi$ answers, so the *non*-isotropic vectors
are asked of it too; their own theory -- Nikulin's gluing over the
primitive extension a vector cuts out, and Dawes' algorithms over it --
lives in :mod:`vector_orbits`, and only the shared double-coset splitting
is here.

Two layers:

* **The $O(L)$ layer** -- $O(L)$-orbits and $O(L)$-equivalence, delegated to
  polyhedral_common behind :mod:`engines`, every representative and witness
  verified over $\mathbb Z$ against the owned lattice before it leaves.

* **The subgroup layer** -- a subgroup $\Gamma\le O(L)$ cut out by character
  data splits each $O(L)$-orbit into finitely many $\Gamma$-orbits, decided
  by double cosets in a finite quotient: assemble
  $\varphi=(\rho_L,\det,\operatorname{sn}_{\mathbb R})$ into a finite group,
  take the image of the $O(L)$-stabilizer and the image of $\Gamma$, and
  read the $\Gamma$-orbits inside one $O(L)$-orbit off
  $\operatorname{Stab}\backslash O(L)/\Gamma$ in that quotient (GAP's double
  cosets, behind libgap).  The construction is sound exactly because such a
  $\Gamma$ *is* the full preimage of its character data, so
  $\Gamma\supseteq\ker\varphi$ and everything descends.  The shape is the
  standard cusp computation (Dutour Sikirić--Hulek; the source corpus's
  isotropic-orbit backend ran it green for the degree-two Enriques group).

Convention: matrices act on coordinate rows on the right, the preamble's
morphism-matrix convention throughout.
"""

from typing import TYPE_CHECKING

from sage.matrix.constructor import matrix
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.group.predicate_subgroups import (
    PredicateSubgroups,
    predicate_subgroup_category,
)
from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.owned_category_bases import Category_singleton

if TYPE_CHECKING:
    from collections.abc import Callable

    from dzack_research.preamble.owned_category import ConstructionData

    from sage.libs.gap.element import GapElement
    from sage.rings.integer import Integer
    from sage.structure.parent import Parent

    from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
        FormModule,
    )
    from dzack_research.preamble.lexicon import Element, OrderedSet


# ---- owned validation of engine data ----


def _lattice_elements(lattice: "FormModule", rows: "list") -> tuple:
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.utilities import zipsum
    generators = tuple(lattice.module_generators())
    return tuple(
        zipsum(
            tuple(SageZZ(entry) for entry in row), generators, lattice.zero()
        )
        for row in rows
    )


def _element_rows(lattice: "FormModule", elements: "OrderedSet") -> list:
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _coordinate_vector
    held = tuple(
        element if element.parent() is lattice else lattice(element)
        for element in elements
    )
    return [[int(entry) for entry in _coordinate_vector(element)] for element in held]


def _validated_isotropic_basis(
    lattice: "FormModule", elements: tuple
) -> tuple:
    r"""Assert what an isotropic representative is; return it unchanged.

    Every vector isotropic, all pairings zero, the vectors independent, and
    -- for a single vector -- primitive.  This is the owned check every
    engine representative passes before it is one of ours.
    """
    for left in elements:
        assert left.q() == 0, f"{left} is not isotropic"
        for right in elements:
            assert left.b(right) == 0, (
                f"{left} and {right} do not span a totally isotropic subobject"
            )
    rows = matrix(SageZZ, _element_rows(lattice, elements))
    assert rows.rank() == len(elements), "the representative rows are dependent"
    if len(elements) == 1:
        assert elements[0].is_primitive(), (
            f"{elements[0]} is not primitive; the generator of a rank-one "
            "isotropic sublattice is"
        )
    return elements


def orthogonal_group_isotropic_orbit_representatives(
    lattice: "FormModule", rank: "Integer", isotropic_object: str
) -> tuple:
    r"""Return one validated basis tuple per $O(L)$-orbit (engine behind the seam)."""
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.engines import isotropic_sublattice_orbit_representative_rows
    representatives = tuple(
        _validated_isotropic_basis(
            lattice, _lattice_elements(lattice, block)
        )
        for block in isotropic_sublattice_orbit_representative_rows(
            matrix(SageZZ, lattice.gram_matrix()), int(rank), isotropic_object
        )
    )
    return representatives


def orthogonal_group_line_equivalence_witness(
    lattice: "FormModule", left: "Element", right: "Element"
) -> "Morphism | None":
    r"""Return $g\in O(L)$ with $g(\mathbb Z v)=\mathbb Z w$, or ``None``.

    A rank-one isotropic sublattice $\mathbb Zv$ is a primitive vector up to
    sign, so the engine's vector equivalence is asked at both signs of the
    target; the returned matrix crosses back as a
    morphism of $O(L)$, whose constructor re-asserts form preservation.
    """
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.engines import vector_equivalence_witness
    source = _validated_isotropic_basis(
        lattice, tuple(_held_elements(lattice, (left,)))
    )[0]
    target = _validated_isotropic_basis(
        lattice, tuple(_held_elements(lattice, (right,)))
    )[0]
    gram = matrix(SageZZ, lattice.gram_matrix())
    (source_row,) = _element_rows(lattice, (source,))
    for signed_target in (target, -target):
        (target_row,) = _element_rows(lattice, (signed_target,))
        witness = vector_equivalence_witness(
            gram, source_row, target_row
        )
        if witness is not None:
            return lattice.Aut()._isometry_on_rows(witness.rows())
    return None


def orthogonal_group_sublattice_equivalence_witness(
    lattice: "FormModule",
    left: "OrderedSet",
    right: "OrderedSet",
    isotropic_object: str,
) -> "Morphism | None":
    r"""Return $g\in O(L)$ carrying one isotropic sublattice or flag to another.

    For a flag the witness is checked term by term at the seam -- equality
    of every initial-segment span, the flag relation itself, not the
    coarser total-span comparison the source corpus's flag branch decided
    (a recorded error corrected here).
    """
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.engines import isotropic_sublattice_equivalence_witness
    source = _validated_isotropic_basis(
        lattice, tuple(_held_elements(lattice, left))
    )
    target = _validated_isotropic_basis(
        lattice, tuple(_held_elements(lattice, right))
    )
    assert len(source) == len(target), (
        "sublattices of different rank are never equivalent; nothing to ask"
    )
    witness = isotropic_sublattice_equivalence_witness(
        matrix(SageZZ, lattice.gram_matrix()),
        _element_rows(lattice, source),
        _element_rows(lattice, target),
        isotropic_object,
    )
    if witness is None:
        return None
    return lattice.Aut()._isometry_on_rows(witness.rows())


def orthogonal_group_isotropic_stabilizer_generators(
    lattice: "FormModule", elements: "OrderedSet", isotropic_object: str
) -> tuple:
    r"""Return generators of $\operatorname{Stab}_{O(L)}$ of a sublattice or flag.

    Engine generators crossed back as morphisms; each is verified to
    preserve the *saturation* of every flag term (the engine stabilizes
    primitive sublattices, i.e. saturated subobjects, where
    $\mathbb Q$-span preservation and subobject preservation agree).
    """
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.engines import isotropic_sublattice_stabilizer_generator_matrices
    basis = _validated_isotropic_basis(
        lattice, tuple(_held_elements(lattice, elements))
    )
    terms = tuple(
        lattice.subobject_on(basis[: position + 1]).saturation()
        for position in range(len(basis))
    )
    checked = terms if isotropic_object == "flag" else terms[-1:]
    generators = tuple(
        lattice.Aut()._isometry_on_rows(generator.rows())
        for generator in isotropic_sublattice_stabilizer_generator_matrices(
            matrix(SageZZ, lattice.gram_matrix()),
            _element_rows(lattice, basis),
            isotropic_object,
        )
    )
    assert all(
        generator.preserves(term)
        for generator in generators
        for term in checked
    ), "an engine stabilizer generator moves a flag term it must preserve"
    return generators


def _held_elements(lattice: "FormModule", elements: "OrderedSet") -> tuple:
    return tuple(
        element if element.parent() is lattice else lattice(element)
        for element in elements
    )


# ---- the finite quotient and the subgroups containing ker(phi) ----


class _FiniteQuotient:
    r"""$\varphi: O(L)\to Q$ assembled from the characters a subgroup is cut by.

    $Q$ is the (finite) direct product of the factors the subgroup's data
    names -- the engine's $O(A_L)$ for discriminant preimages, one $C_2$
    per $\pm1$ character -- held as GAP groups behind libgap; the
    homomorphism is defined on generators of $O(L)$ (functoriality of the
    discriminant construction and multiplicativity of the characters make
    it one, so GAP is not asked to re-check).  ``lift`` inverts through
    GAP's preimage representative.
    """

    def __init__(self, subgroup: "Parent") -> None:
        from sage.libs.gap.libgap import libgap

        supergroup = subgroup.supergroup()
        lattice = supergroup.domain()
        assert supergroup is lattice.Aut(), (
            "the finite-quotient splitting is stated for subgroups of the "
            "full O(L)"
        )
        factors: list = []
        if subgroup._discriminant_preimages:
            automorphism_group = lattice.discriminant_group().automorphism_group()
            engine_group = automorphism_group._engine_group
            gap_group = libgap(engine_group)
            allowed = gap_group
            for preimage_target in subgroup._discriminant_preimages:
                target_gap = _gap_subgroup(
                    gap_group,
                    [
                        libgap(automorphism_group._to_engine(generator))
                        for generator in preimage_target.group_generators()
                    ],
                )
                allowed = libgap.Intersection(allowed, target_gap)

            def _discriminant_image(
                isometry: "Morphism",
                _automorphism_group: "Parent" = automorphism_group,
            ) -> "GapElement":
                return libgap(
                    _automorphism_group._to_engine(
                        isometry.discriminant_morphism()
                    )
                )

            factors.append((gap_group, allowed, _discriminant_image))
        if subgroup._determinant_kernel:
            factors.append(_sign_character_factor(lambda isometry: isometry.determinant()))
        if subgroup._spinor_kernel:
            factors.append(
                _sign_character_factor(
                    lambda isometry: isometry.real_spinor_norm_sign()
                )
            )
        assert factors, (
            "a subgroup given only by its membership predicate has no "
            "finite quotient; the splitting is stated for subgroups cut by "
            "determinant, spinor, or discriminant-image data"
        )
        supergroup_generators = tuple(supergroup.group_generators())
        source_matrix_group = _gap_matrix_group(supergroup_generators)
        if len(factors) == 1:
            product, allowed_group, image_of = factors[0]

            def _image(isometry: "Morphism") -> "GapElement":
                return image_of(isometry)

        else:
            product = libgap.DirectProduct(*[factor[0] for factor in factors])
            embeddings = [
                libgap.Embedding(product, index + 1)
                for index in range(len(factors))
            ]

            def _image(isometry: "Morphism") -> "GapElement":
                composite = libgap.One(product)
                for embedding, (_, _, image_of) in zip(embeddings, factors):
                    composite = composite * libgap.Image(
                        embedding, image_of(isometry)
                    )
                return composite

            allowed_generators: list = []
            for embedding, (_, allowed_factor, _) in zip(embeddings, factors):
                allowed_generators.extend(
                    libgap.Image(embedding, generator)
                    for generator in allowed_factor.GeneratorsOfGroup()
                )
            allowed_group = _gap_subgroup(product, allowed_generators)
        generator_images = [_image(generator) for generator in supergroup_generators]
        self._image_of = _image
        self._image_group = _gap_subgroup(product, generator_images)
        self._subgroup_image = libgap.Intersection(
            self._image_group, allowed_group
        )
        # Functoriality of Disc and multiplicativity of the characters make
        # this a homomorphism; NC because GAP cannot cheaply verify it on an
        # infinite matrix source.
        self._homomorphism = libgap.GroupHomomorphismByImagesNC(
            source_matrix_group,
            product,
            source_matrix_group.GeneratorsOfGroup(),
            generator_images,
        )
        self._supergroup = supergroup

    def image(self, isometry: "Morphism") -> "GapElement":
        return self._image_of(isometry)

    def image_subgroup(self, isometries: "OrderedSet") -> "GapElement":
        return _gap_subgroup(
            self._image_group,
            [self.image(isometry) for isometry in isometries],
        )

    def subgroup_image(self) -> "GapElement":
        r"""Return $\varphi(\Gamma)=\varphi(O(L))\cap(\text{allowed})$."""
        return self._subgroup_image

    def image_group(self) -> "GapElement":
        r"""Return $\varphi(O(L))$, where every double coset lives."""
        return self._image_group

    def lift(self, target_element: "GapElement") -> "Morphism":
        from sage.libs.gap.libgap import libgap

        lifted = libgap.PreImagesRepresentative(
            self._homomorphism, target_element
        )
        return self._supergroup._isometry_on_rows(
            matrix(SageZZ, lifted).rows()
        )


def _sign_character_factor(character: "Callable") -> tuple:
    from sage.libs.gap.libgap import libgap

    cyclic = libgap.CyclicGroup(2)
    generator = cyclic.GeneratorsOfGroup()[0]

    def _image(isometry: "Morphism") -> "GapElement":
        value = character(isometry)
        assert value in (1, -1), f"a sign character returned {value}"
        return libgap.One(cyclic) if value == 1 else generator

    return (cyclic, _gap_subgroup(cyclic, []), _image)


def _gap_subgroup(parent_group: "GapElement", generators: list) -> "GapElement":
    from sage.libs.gap.libgap import libgap

    generators = list(generators)
    if generators:
        return libgap.Subgroup(parent_group, generators)
    return libgap.TrivialSubgroup(parent_group)


def _gap_matrix_group(generators: tuple) -> "GapElement":
    from sage.groups.matrix_gps.matrix_group import MatrixGroup
    from sage.libs.gap.libgap import libgap

    return libgap(
        MatrixGroup([matrix(SageZZ, generator.matrix()) for generator in generators])
    )


class OrthogonalPredicateSubgroups(Category_singleton):
    r"""A subgroup of $O(L)$ cut out by a membership predicate, with its
    defining character data.

    The predicate is the always-available operation
    (:mod:`predicate_subgroups`); what this level adds is the record of
    *which characters* cut the subgroup out -- the determinant kernel, the
    real-spinor-norm kernel, preimages of subgroups of $O(A_L)$ -- because
    that data is exactly what makes orbit questions decidable by double
    cosets in a finite quotient.  Standing hypothesis, guaranteed by the
    named constructors on ``LatticeIsometries.ParentMethods`` and preserved
    by :meth:`intersection`: the subgroup *is* the full preimage of its
    character data, so it contains $\ker\varphi$ and the quotient decides
    faithfully.  A subgroup carrying no character data still answers
    membership; its orbit questions are a stated absence.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "predicate subgroups of an orthogonal group"

    def super_categories(self) -> list:
        return [PredicateSubgroups()]

    class ParentMethods:
        def __init__(
            self,
            determinant_kernel: bool = False,
            spinor_kernel: bool = False,
            discriminant_preimages: tuple = (),
            **rest: "ConstructionData",
        ) -> None:
            self._determinant_kernel = bool(determinant_kernel)
            self._spinor_kernel = bool(spinor_kernel)
            self._discriminant_preimages = tuple(discriminant_preimages)
            super().__init__(**rest)

        def domain(self) -> "FormModule":
            r"""Return $L$: a subgroup of $O(L)$ acts where $O(L)$ does."""
            return self.supergroup().domain()

        def contains_character_kernel(self) -> bool:
            r"""Return whether $\Gamma\supseteq\ker\varphi$.

            Equivalently, whether character data cuts this subgroup out: a
            subgroup so cut *is* the full preimage of that data, which is the
            standing hypothesis every orbit method below needs.
            """
            return bool(
                self._determinant_kernel
                or self._spinor_kernel
                or self._discriminant_preimages
            )

        def intersection(self, other: "Parent") -> "Parent":
            r"""Return $\Gamma_1\cap\Gamma_2$: predicates conjoin, the defining
            characters union.

            The degree-two Enriques group is the model:
            $\rho^{-1}(\operatorname{Stab}(h/2))\cap O^+(L)$.
            """
            assert (
                other in OrthogonalPredicateSubgroups()
                and other.supergroup() is self.supergroup()
            ), "an intersection of subgroups happens inside one group"
            left_predicate = self.defining_predicate()
            right_predicate = other.defining_predicate()
            return orthogonal_predicate_subgroup(
                self.supergroup(),
                lambda isometry: left_predicate(isometry)
                and right_predicate(isometry),
                f"({self._description}) and ({other._description})",
                determinant_kernel=self._determinant_kernel
                or other._determinant_kernel,
                spinor_kernel=self._spinor_kernel or other._spinor_kernel,
                discriminant_preimages=self._discriminant_preimages
                + other._discriminant_preimages,
            )

        def _finite_quotient(self) -> _FiniteQuotient:
            assert self.contains_character_kernel(), (
                f"{self} carries no determinant, spinor, or discriminant-image "
                "data, so no finite quotient decides its orbits"
            )
            cached = self.__dict__.get("_finite_quotient_cache")
            if cached is None:
                cached = _FiniteQuotient(self)
                self._finite_quotient_cache = cached
            return cached

        # ---- orbit splitting by double cosets ----

        def _splitting_isometries(self, stabilizer_generators: "OrderedSet") -> tuple:
            r"""Return one isometry per $\Gamma$-orbit inside one $O(L)$-orbit.

            $O(L)/\operatorname{Stab}(x)\to O(L)\cdot x$ is the orbit map (right
            action on rows), so the $\Gamma$-orbits inside one $O(L)$-orbit are
            the double cosets $\operatorname{Stab}(x)\backslash O(L)/\Gamma$,
            computed in the finite quotient -- sound because
            $\Gamma\supseteq\ker\varphi$ -- and each coset representative is
            lifted back through the quotient.  Applying them to the
            $O(L)$-representative is the caller's step, because what an isometry
            is applied *to* differs by the kind of object.
            """
            from sage.libs.gap.libgap import libgap

            quotient = self._finite_quotient()
            stabilizer_image = quotient.image_subgroup(stabilizer_generators)
            return tuple(
                quotient.lift(libgap.Representative(double_coset))
                for double_coset in libgap.DoubleCosets(
                    quotient.image_group(),
                    stabilizer_image,
                    quotient.subgroup_image(),
                )
            )

        def _witness_meets_subgroup(
            self, witness: "Morphism", stabilizer_generators: "OrderedSet"
        ) -> bool:
            r"""Decide whether $\Gamma$ meets $W\cdot\operatorname{Stab}(y)$.

            With $W$ an $O(L)$-witness carrying $x$ to $y$, the isometries
            carrying $x$ to $y$ are exactly $W\cdot\operatorname{Stab}(y)$, so
            one of them lies in $\Gamma$ exactly when
            $\varphi(W)\in\varphi(\Gamma)\cdot\varphi(\operatorname{Stab}(y))$ --
            membership of the image in one double coset.  (The right-action order
            of the factors is forced by the row convention; the source corpus's
            column-action code had them mirrored.)  Every character cutting such
            a subgroup out factors through $\varphi$, so this is a decision and
            never a bounded search.
            """
            from sage.libs.gap.libgap import libgap

            if witness in self:
                return True
            quotient = self._finite_quotient()
            stabilizer_image = quotient.image_subgroup(stabilizer_generators)
            identity_double_coset = libgap.DoubleCoset(
                quotient.subgroup_image(),
                libgap.One(quotient.image_group()),
                stabilizer_image,
            )
            return bool(quotient.image(witness) in identity_double_coset)

        def _split_orthogonal_group_orbits(
            self, rank: "Integer", isotropic_object: str
        ) -> tuple:
            r"""Split each $O(L)$-orbit of isotropic subobjects into $\Gamma$-orbits."""
            lattice = self.domain()
            representatives = []
            for representative in orthogonal_group_isotropic_orbit_representatives(
                lattice, rank, isotropic_object
            ):
                for witness in self._splitting_isometries(
                    orthogonal_group_isotropic_stabilizer_generators(
                        lattice, representative, isotropic_object
                    )
                ):
                    representatives.append(
                        tuple(witness(element) for element in representative)
                    )
            return tuple(representatives)

        def isotropic_line_orbit_representatives(self) -> tuple:
            r"""Return one primitive isotropic vector per $\Gamma$-orbit of lines."""
            return tuple(
                flag[0] for flag in self._split_orthogonal_group_orbits(1, "plane")
            )

        def isotropic_plane_orbit_representatives(self) -> tuple:
            r"""Return one basis pair per $\Gamma$-orbit of totally isotropic planes."""
            return self._split_orthogonal_group_orbits(2, "plane")

        def isotropic_flag_orbit_representatives(self, length: "Integer") -> tuple:
            r"""Return one ordered basis per $\Gamma$-orbit of isotropic flags."""
            return self._split_orthogonal_group_orbits(length, "flag")

        # ---- equivalence by double-coset membership ----

        def _objects_are_equivalent(
            self, left: "OrderedSet", right: "OrderedSet", isotropic_object: str
        ) -> bool:
            r"""Decide $\Gamma$-equivalence of two isotropic subobjects."""
            lattice = self.domain()
            if len(tuple(left)) == 1 and isotropic_object == "plane":
                witness = orthogonal_group_line_equivalence_witness(
                    lattice, tuple(left)[0], tuple(right)[0]
                )
            else:
                witness = orthogonal_group_sublattice_equivalence_witness(
                    lattice, left, right, isotropic_object
                )
            if witness is None:
                return False
            return self._witness_meets_subgroup(
                witness,
                orthogonal_group_isotropic_stabilizer_generators(
                    lattice, _held_elements(lattice, right), isotropic_object
                ),
            )

        def isotropic_lines_are_equivalent(
            self, left: "Element", right: "Element"
        ) -> bool:
            r"""Decide whether two primitive isotropic lines lie in one $\Gamma$-orbit."""
            return self._objects_are_equivalent((left,), (right,), "plane")

        def isotropic_planes_are_equivalent(
            self, left: "OrderedSet", right: "OrderedSet"
        ) -> bool:
            r"""Decide whether two totally isotropic planes lie in one $\Gamma$-orbit."""
            return self._objects_are_equivalent(left, right, "plane")

        def isotropic_flags_are_equivalent(
            self, left: "OrderedSet", right: "OrderedSet"
        ) -> bool:
            r"""Decide whether two isotropic flags lie in one $\Gamma$-orbit."""
            return self._objects_are_equivalent(left, right, "flag")

        # ---- orbits of non-isotropic vectors ----
        #
        # The theory is Nikulin's gluing over the primitive extension a vector
        # cuts out, and it lives in ``vector_orbits``; what belongs here is the
        # same double-coset splitting, asked of a vector's pointwise stabilizer.

        def vector_orbit_representatives(self, square: "Integer") -> tuple:
            r"""Return one vector per $\Gamma$-orbit of vectors of this square.

            The $O(L)$-orbits of vectors $v$ with $q(v)$ equal to
            ``square`` are finitely many for an indefinite lattice and the engine
            enumerates them
            (:meth:`LatticeIsometries.ParentMethods.vector_orbit_representatives`);
            each splits into the double cosets of $\Gamma$ against the vector's
            pointwise stabilizer.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.vector_orbits import orthogonal_group_vector_stabilizer_generators
            lattice = self.domain()
            representatives = []
            for representative in lattice.Aut().vector_orbit_representatives(
                square
            ):
                for witness in self._splitting_isometries(
                    orthogonal_group_vector_stabilizer_generators(
                        lattice, representative
                    )
                ):
                    representatives.append(witness(representative))
            return tuple(representatives)

        def vectors_are_equivalent(self, left: "Element", right: "Element") -> bool:
            r"""Decide whether two vectors lie in one $\Gamma$-orbit.

            Complete, and a decision rather than a search: the isometries
            carrying $v$ to $w$ are one coset of $\operatorname{Stab}_{O(L)}(w)$,
            every character cutting $\Gamma$ out factors through the finite
            quotient, and the coset meets $\Gamma$ exactly when the
            $O(L)$-witness's image lies in the identity double coset.  (The source
            corpus decided this by a search bounded twice over -- a fixed
            coefficient box and products of at most two reflections -- and
            reported "not equivalent" when that search came up empty; neither
            bound was a theorem.  That route is not reproduced.)
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.vector_orbits import (
                orthogonal_group_vector_equivalence_witness,
                orthogonal_group_vector_stabilizer_generators,
            )
            lattice = self.domain()
            witness = orthogonal_group_vector_equivalence_witness(lattice, left, right)
            if witness is None:
                return False
            return self._witness_meets_subgroup(
                witness, orthogonal_group_vector_stabilizer_generators(lattice, right)
            )

        def vector_equivalence_witness(
            self, left: "Element", right: "Element"
        ) -> "Morphism | None":
            r"""Return an element of $\Gamma$ carrying one vector to another.

            ``None`` is the absence of such an element, and it is grounded:
            either no isometry of $L$ at all carries $v$ to $w$, or
            :meth:`vectors_are_equivalent` decides that none of them lies in
            $\Gamma$.

            Two routes produce the element itself.  The $O(L)$-witness may
            already lie in $\Gamma$.  Otherwise, when $w^{\perp}$ is definite,
            Dawes' Algorithm 2.1 constructs every isometry carrying $v$ to $w$
            and the first one in $\Gamma$ is returned
            (:func:`vector_orbits.definite_complement_extensions`).

            Stated gap, for an indefinite complement with the $O(L)$-witness
            outside $\Gamma$: the decision is available and is asserted here,
            but *exhibiting* the element needs a preimage in
            $\operatorname{Stab}_{O(L)}(w)$ of a named element of the finite
            quotient, which this surface does not compute -- $\varphi$ is
            presented on generators of $O(L)$, not of the stabilizer.  The
            assertion below is that absence by name, never a ``None`` standing
            in for it.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.vector_orbits import (
                orthogonal_group_vector_equivalence_witness,
                definite_complement_extensions,
                vector_primitive_extension,
            )
            lattice = self.domain()
            witness = orthogonal_group_vector_equivalence_witness(lattice, left, right)
            if witness is None:
                return None
            if witness in self:
                return witness
            if not self.vectors_are_equivalent(left, right):
                return None
            assert vector_primitive_extension(
                lattice, right
            ).complement_is_definite(), (
                f"{left} and {right} are equivalent under {self}, and exhibiting "
                "the isometry for an indefinite complement needs a preimage in "
                "Stab(w) of an element of the finite quotient; that computation "
                "is not sited here"
            )
            for extension in definite_complement_extensions(lattice, left, right):
                if extension in self:
                    return extension
            assert False, (
                "the double-coset decision and Algorithm 2.1 disagree: one says "
                "an isometry in this subgroup exists and the other enumerated "
                "them all without finding it"
            )


def orthogonal_predicate_subgroup(
    isometry_group: "Parent",
    predicate: "Callable",
    description: str,
    *,
    determinant_kernel: bool = False,
    spinor_kernel: bool = False,
    discriminant_preimages: tuple = (),
) -> "Parent":
    r"""Return $\Gamma\le O(L)$, with the character data that cuts it out."""
    from sage.categories.category import Category

    return object_of(
        Category.join(
            (OrthogonalPredicateSubgroups(), predicate_subgroup_category())
        ),
        containing_group=isometry_group,
        predicate=predicate,
        description=description,
        determinant_kernel=determinant_kernel,
        spinor_kernel=spinor_kernel,
        discriminant_preimages=discriminant_preimages,
    )
