r"""Orbits of isotropic subobjects under $O(L)$ and its structured subgroups.

The 0- and 1-cusps of a Baily--Borel boundary are $\Gamma$-orbits of
primitive totally isotropic sublattices of rank 1 and 2, so the objects here
are primitive isotropic vectors, planes, and flags, and the questions are
orbit enumeration and equivalence -- under the full $O(L)$, and under the
arithmetic subgroups the Enriques/Coble program names by characters
(determinant, real spinor norm) and by preimages under the discriminant
representation.

Two layers:

* **Ambient layer** -- $O(L)$-orbits and $O(L)$-equivalence, delegated to
  polyhedral_common behind :mod:`engines`, every representative and witness
  verified over $\mathbb Z$ against the owned lattice before it leaves.

* **Subgroup layer** -- a subgroup $\Gamma\le O(L)$ cut out by character
  data splits each ambient orbit into finitely many $\Gamma$-orbits, decided
  by double cosets in a finite quotient: assemble
  $\varphi=(\rho_L,\det,\operatorname{sn}_{\mathbb R})$ into a finite group,
  take the image of the ambient stabilizer and the image of $\Gamma$, and
  read the $\Gamma$-orbits inside one $O(L)$-orbit off
  $\operatorname{Stab}\backslash O(L)/\Gamma$ in that quotient (GAP's double
  cosets, behind libgap).  The construction is sound exactly because a
  structured $\Gamma$ *is* the full preimage of its character data, so
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
    PredicateSubgroup,
)

if TYPE_CHECKING:
    from collections.abc import Callable

    from sage.libs.gap.element import GapElement
    from sage.rings.integer import Integer
    from sage.structure.parent import Parent

    from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
        FormModule,
        FormMorphism,
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
            f"{elements[0]} is not primitive; a line representative is"
        )
    return elements


def ambient_isotropic_orbit_representatives(
    lattice: "FormModule", depth: "Integer", nature: str
) -> tuple:
    r"""Return one validated basis tuple per $O(L)$-orbit (engine behind the seam)."""
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.engines import isotropic_subspace_orbit_representative_rows
    representatives = tuple(
        _validated_isotropic_basis(
            lattice, _lattice_elements(lattice, block)
        )
        for block in isotropic_subspace_orbit_representative_rows(
            matrix(SageZZ, lattice.gram_matrix()), int(depth), nature
        )
    )
    return representatives


def ambient_line_equivalence_witness(
    lattice: "FormModule", left: "Element", right: "Element"
) -> "FormMorphism | None":
    r"""Return $g\in O(L)$ with $g(\mathbb Z v)=\mathbb Z w$, or ``None``.

    A line is a vector up to sign, so the engine's vector equivalence is
    asked at both signs of the target; the returned matrix crosses back as a
    morphism of $O(L)$, whose constructor re-asserts form preservation.
    """
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.engines import isotropic_vector_equivalence_witness
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
        witness = isotropic_vector_equivalence_witness(
            gram, source_row, target_row
        )
        if witness is not None:
            return lattice.Aut()._isometry_on_rows(witness.rows())
    return None


def ambient_subspace_equivalence_witness(
    lattice: "FormModule",
    left: "OrderedSet",
    right: "OrderedSet",
    nature: str,
) -> "FormMorphism | None":
    r"""Return $g\in O(L)$ carrying one isotropic plane or flag to another.

    For a flag the witness is checked stratum by stratum at the seam --
    equality of every initial-segment span, the flag relation itself, not
    the coarser total-span comparison the source corpus's flag branch
    decided (a recorded error corrected here).
    """
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.engines import isotropic_subspace_equivalence_witness
    source = _validated_isotropic_basis(
        lattice, tuple(_held_elements(lattice, left))
    )
    target = _validated_isotropic_basis(
        lattice, tuple(_held_elements(lattice, right))
    )
    assert len(source) == len(target), (
        "subspaces of different rank are never equivalent; nothing to ask"
    )
    witness = isotropic_subspace_equivalence_witness(
        matrix(SageZZ, lattice.gram_matrix()),
        _element_rows(lattice, source),
        _element_rows(lattice, target),
        nature,
    )
    if witness is None:
        return None
    return lattice.Aut()._isometry_on_rows(witness.rows())


def ambient_isotropic_stabilizer_generators(
    lattice: "FormModule", elements: "OrderedSet", nature: str
) -> tuple:
    r"""Return generators of $\operatorname{Stab}_{O(L)}$ of a plane or flag.

    Engine generators crossed back as morphisms; each is verified to
    preserve every stratum's *saturation* (the engine stabilizes primitive
    subspaces, i.e. saturated subobjects, where $\mathbb Q$-span
    preservation and subobject preservation agree).
    """
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.engines import isotropic_subspace_stabilizer_generator_matrices
    basis = _validated_isotropic_basis(
        lattice, tuple(_held_elements(lattice, elements))
    )
    strata = tuple(
        lattice.subobject_on(basis[: depth + 1]).saturation()
        for depth in range(len(basis))
    )
    checked = strata if nature == "flag" else strata[-1:]
    generators = tuple(
        lattice.Aut()._isometry_on_rows(generator.rows())
        for generator in isotropic_subspace_stabilizer_generator_matrices(
            matrix(SageZZ, lattice.gram_matrix()),
            _element_rows(lattice, basis),
            nature,
        )
    )
    assert all(
        generator.preserves(stratum)
        for generator in generators
        for stratum in checked
    ), "an engine stabilizer generator moves a stratum it must preserve"
    return generators


def _held_elements(lattice: "FormModule", elements: "OrderedSet") -> tuple:
    return tuple(
        element if element.parent() is lattice else lattice(element)
        for element in elements
    )


# ---- the finite quotient and the structured subgroups ----


def _engine_element_of_discriminant_morphism(
    automorphism_group: "Parent", morphism: "FormMorphism"
) -> "Element":
    r"""Return the engine-group element of an owned $O(A_L)$ morphism.

    The engine's smith-form generators are lifted to the cover, whose basis
    corresponds one to one to the owned module generators (the
    :func:`torsion_modules_with_form._engine_torsion_module` contract); each
    lift crosses to an owned element, is moved by the morphism, and crosses
    back, giving the matrix of the morphism on the smith generators -- which
    is what the engine's orthogonal group constructs elements from.
    """
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.modules.framed.formed.torsionform.torsion_modules_with_form import _coordinates_in_module_generators
    from dzack_research.preamble.utilities import zipsum
    engine_module = automorphism_group._engine_module
    engine_group = automorphism_group._engine_group
    form = automorphism_group.domain()
    cover = engine_module.V()
    cover_basis = tuple(cover.basis())
    owned_generators = tuple(form.module_generators())
    generating_set = form.module_generating_set()
    rows = []
    for smith_generator in engine_module.smith_form_gens():
        coordinates = cover.coordinates(smith_generator.lift())
        owned = zipsum(
            tuple(SageZZ(coordinate) for coordinate in coordinates),
            owned_generators,
            form.zero(),
        )
        image = morphism(owned)
        image_coordinates = _coordinates_in_module_generators(
            image, generating_set
        )
        engine_image = engine_module(
            sum(
                SageZZ(coordinate) * basis_vector
                for coordinate, basis_vector in zip(
                    image_coordinates, cover_basis
                )
            )
        )
        rows.append([SageZZ(entry) for entry in engine_image.vector()])
    return engine_group(matrix(SageZZ, rows))


class _FiniteQuotient:
    r"""$\varphi: O(L)\to Q$ assembled from the characters a subgroup is cut by.

    $Q$ is the (finite) direct product of the factors the subgroup's data
    names -- the engine's $O(A_L)$ for discriminant preimages, one $C_2$
    per $\pm1$ character -- held as GAP groups behind libgap; the
    homomorphism is defined on the ambient generators (functoriality of the
    discriminant construction and multiplicativity of the characters make
    it one, so GAP is not asked to re-check).  ``lift`` inverts through
    GAP's preimage representative.
    """

    def __init__(self, subgroup: "OrthogonalPredicateSubgroup") -> None:
        from sage.libs.gap.libgap import libgap

        ambient = subgroup.supergroup()
        lattice = ambient.domain()
        assert ambient is lattice.Aut(), (
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
                        libgap(
                            _engine_element_of_discriminant_morphism(
                                automorphism_group, generator
                            )
                        )
                        for generator in preimage_target.group_generators()
                    ],
                )
                allowed = libgap.Intersection(allowed, target_gap)

            def _discriminant_image(
                isometry: "FormMorphism",
                _automorphism_group: "Parent" = automorphism_group,
            ) -> "GapElement":
                return libgap(
                    _engine_element_of_discriminant_morphism(
                        _automorphism_group, isometry.discriminant_morphism()
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
            "an opaque subgroup has no finite quotient; the splitting is "
            "stated for subgroups cut by determinant, spinor, or "
            "discriminant-image data"
        )
        ambient_generators = tuple(ambient.group_generators())
        source_matrix_group = _gap_matrix_group(ambient_generators)
        if len(factors) == 1:
            product, allowed_group, image_of = factors[0]

            def _image(isometry: "FormMorphism") -> "GapElement":
                return image_of(isometry)

        else:
            product = libgap.DirectProduct(*[factor[0] for factor in factors])
            embeddings = [
                libgap.Embedding(product, index + 1)
                for index in range(len(factors))
            ]

            def _image(isometry: "FormMorphism") -> "GapElement":
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
        generator_images = [_image(generator) for generator in ambient_generators]
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
        self._ambient = ambient

    def image(self, isometry: "FormMorphism") -> "GapElement":
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

    def lift(self, target_element: "GapElement") -> "FormMorphism":
        from sage.libs.gap.libgap import libgap

        lifted = libgap.PreImagesRepresentative(
            self._homomorphism, target_element
        )
        return self._ambient._isometry_on_rows(
            matrix(SageZZ, lifted).rows()
        )


def _sign_character_factor(character: "Callable") -> tuple:
    from sage.libs.gap.libgap import libgap

    cyclic = libgap.CyclicGroup(2)
    generator = cyclic.GeneratorsOfGroup()[0]

    def _image(isometry: "FormMorphism") -> "GapElement":
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


class OrthogonalPredicateSubgroup(PredicateSubgroup):
    r"""A subgroup of $O(L)$ cut out by a membership predicate, with its cut data.

    The predicate is the always-available operation
    (:mod:`predicate_subgroups`); what this refinement adds is the record of
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

    def __init__(
        self,
        isometry_group: "Parent",
        predicate: "Callable",
        description: str,
        *,
        determinant_kernel: bool = False,
        spinor_kernel: bool = False,
        discriminant_preimages: tuple = (),
    ) -> None:
        PredicateSubgroup.__init__(self, isometry_group, predicate, description)
        self._determinant_kernel = bool(determinant_kernel)
        self._spinor_kernel = bool(spinor_kernel)
        self._discriminant_preimages = tuple(discriminant_preimages)

    def domain(self) -> "FormModule":
        r"""Return $L$: a subgroup of $O(L)$ acts where $O(L)$ does."""
        return self.supergroup().domain()

    def is_structured(self) -> bool:
        r"""Return whether character data cuts this subgroup out."""
        return bool(
            self._determinant_kernel
            or self._spinor_kernel
            or self._discriminant_preimages
        )

    def intersection(
        self, other: "OrthogonalPredicateSubgroup"
    ) -> "OrthogonalPredicateSubgroup":
        r"""Return $\Gamma_1\cap\Gamma_2$: predicates conjoin, cut data unions.

        The degree-two Enriques group is the model:
        $\rho^{-1}(\operatorname{Stab}(h/2))\cap O^+(L)$.
        """
        assert (
            isinstance(other, OrthogonalPredicateSubgroup)
            and other.supergroup() is self.supergroup()
        ), "an intersection of subgroups happens inside one group"
        left_predicate = self.defining_predicate()
        right_predicate = other.defining_predicate()
        return OrthogonalPredicateSubgroup(
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
        assert self.is_structured(), (
            f"{self} carries no determinant, spinor, or discriminant-image "
            "data, so no finite quotient decides its orbits"
        )
        cached = self.__dict__.get("_finite_quotient_cache")
        if cached is None:
            cached = _FiniteQuotient(self)
            self._finite_quotient_cache = cached
        return cached

    # ---- orbit splitting by double cosets ----

    def _split_ambient_orbits(self, depth: "Integer", nature: str) -> tuple:
        r"""Split each $O(L)$-orbit into $\Gamma$-orbits.

        $O(L)/\operatorname{Stab}(x)\to O(L)\cdot x$ is the orbit map (right
        action on rows), so $\Gamma$-orbits inside one ambient orbit are the
        double cosets
        $\operatorname{Stab}(x)\backslash O(L)/\Gamma$, computed in the
        finite quotient -- sound because $\Gamma\supseteq\ker\varphi$ -- and
        each coset representative is lifted through the quotient and applied
        to the ambient representative.
        """
        from sage.libs.gap.libgap import libgap

        lattice = self.domain()
        quotient = self._finite_quotient()
        representatives = []
        for ambient_representative in ambient_isotropic_orbit_representatives(
            lattice, depth, nature
        ):
            stabilizer_image = quotient.image_subgroup(
                ambient_isotropic_stabilizer_generators(
                    lattice, ambient_representative, nature
                )
            )
            double_cosets = libgap.DoubleCosets(
                quotient.image_group(),
                stabilizer_image,
                quotient.subgroup_image(),
            )
            for double_coset in double_cosets:
                witness = quotient.lift(libgap.Representative(double_coset))
                representatives.append(
                    tuple(
                        witness(element) for element in ambient_representative
                    )
                )
        return tuple(representatives)

    def isotropic_line_orbit_representatives(self) -> tuple:
        r"""Return one primitive isotropic vector per $\Gamma$-orbit of lines."""
        return tuple(flag[0] for flag in self._split_ambient_orbits(1, "plane"))

    def isotropic_plane_orbit_representatives(self) -> tuple:
        r"""Return one basis pair per $\Gamma$-orbit of totally isotropic planes."""
        return self._split_ambient_orbits(2, "plane")

    def isotropic_flag_orbit_representatives(self, depth: "Integer") -> tuple:
        r"""Return one ordered basis per $\Gamma$-orbit of isotropic flags."""
        return self._split_ambient_orbits(depth, "flag")

    # ---- equivalence by double-coset membership ----

    def _objects_are_equivalent(
        self, left: "OrderedSet", right: "OrderedSet", nature: str
    ) -> bool:
        r"""Decide $\Gamma$-equivalence through one ambient witness.

        With $x\cdot W\sim y$ an ambient witness, the isometries carrying
        $x$ to $y$ are $\operatorname{Stab}(x)\cdot W=W\cdot
        \operatorname{Stab}(y)$, so one meets $\Gamma$ exactly when
        $\varphi(W)\in\varphi(\Gamma)\cdot\varphi(\operatorname{Stab}(y))$
        -- membership of the image in one double coset.  (The right-action
        order of the factors is forced by the row convention; the source
        corpus's column-action code had them mirrored.)
        """
        from sage.libs.gap.libgap import libgap

        lattice = self.domain()
        if len(tuple(left)) == 1 and nature == "plane":
            witness = ambient_line_equivalence_witness(
                lattice, tuple(left)[0], tuple(right)[0]
            )
        else:
            witness = ambient_subspace_equivalence_witness(
                lattice, left, right, nature
            )
        if witness is None:
            return False
        if witness in self:
            return True
        quotient = self._finite_quotient()
        stabilizer_image = quotient.image_subgroup(
            ambient_isotropic_stabilizer_generators(
                lattice, _held_elements(lattice, right), nature
            )
        )
        identity_double_coset = libgap.DoubleCoset(
            quotient.subgroup_image(),
            libgap.One(quotient.image_group()),
            stabilizer_image,
        )
        return bool(quotient.image(witness) in identity_double_coset)

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
