r"""Finite character quotients controlling arithmetic-subgroup orbit splitting."""
from sage.libs.gap.libgap import libgap

from dzack_research.preamble.categories.group.g_sets import FiniteGSets
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.indexed_families import finite_indexed_family
from dzack_research.preamble.categories.sets.set_categories import Set, Sets


class OrthogonalCharacterQuotient:
    r"""The finite image of ``O(L)`` under the characters defining a subgroup.

    Components are the discriminant representation and optional determinant /
    real-spinor signs.  The finite image is generated from live ``O(L)``
    generators, retaining one live lattice isometry above every quotient
    element.  This avoids introducing a parallel matrix-group model of the
    infinite arithmetic group.
    """

    def __init__(self, subgroup) -> None:
        self.subgroup = subgroup
        if not subgroup.character_data_is_complete():
            raise ValueError(
                "the retained finite characters do not define this whole subgroup"
            )
        # This finite-image algorithm is explicitly generator-driven.  Selecting
        # the exact represented O(L) framing is therefore part of constructing
        # this quotient; merely knowing O(L) is finitely generated would not be.
        self.supergroup = subgroup.supergroup().framing()
        self.lattice = self.supergroup.domain()
        data = subgroup.character_data()
        self.discriminant_preimages = tuple(data.get("discriminant_preimages", ()))
        self.determinant_kernel = bool(data.get("determinant_kernel", False))
        self.spinor_kernel = bool(data.get("spinor_kernel", False))
        if not (
            self.discriminant_preimages
            or self.determinant_kernel
            or self.spinor_kernel
        ):
            raise ValueError(
                "a finite orthogonal-character quotient requires discriminant, determinant, or spinor data"
            )
        self._has_discriminant = bool(self.discriminant_preimages)
        factors = {}
        labels = []
        if self._has_discriminant:
            self._discriminant_group = self.lattice.discriminant_group().O()
            labels.append("discriminant")
            factors["discriminant"] = self._discriminant_group
            for target in self.discriminant_preimages:
                ambient = (
                    target
                    if target is self._discriminant_group
                    else getattr(target, "supergroup", lambda: None)()
                )
                if ambient is not self._discriminant_group:
                    raise ValueError("a discriminant preimage must lie in O(A_L)")
        signs = finite_ordered_set(
            (self.lattice.base_ring()(-1), self.lattice.base_ring()(1))
        )
        if self.determinant_kernel:
            labels.append("determinant")
            factors["determinant"] = signs
        if self.spinor_kernel:
            labels.append("spinor")
            factors["spinor"] = signs
        self._image_labels = finite_ordered_set(tuple(labels))
        self._image_space = Sets().product(
            finite_indexed_family(
                self._image_labels,
                factors.__getitem__,
                name="Orthogonal character quotient factors",
            )
        )
        self._witnesses = self._enumerate_image()

    def image_space(self):
        r"""Return the owned product in which all character images live."""
        return self._image_space

    def image(self, isometry):
        components = {}
        if self._has_discriminant:
            components["discriminant"] = isometry.discriminant_morphism()
        if self.determinant_kernel:
            components["determinant"] = self.lattice.base_ring()(isometry.determinant())
        if self.spinor_kernel:
            components["spinor"] = self.lattice.base_ring()(
                isometry.real_spinor_norm_sign()
            )
        return self.image_space()(components.__getitem__)

    def _multiply(self, left, right):
        result = {}
        if self._has_discriminant:
            result["discriminant"] = left["discriminant"] * right["discriminant"]
        if self.determinant_kernel:
            result["determinant"] = left["determinant"] * right["determinant"]
        if self.spinor_kernel:
            result["spinor"] = left["spinor"] * right["spinor"]
        return self.image_space()(result.__getitem__)

    def _ambient_bound(self):
        bound = 1
        if self._has_discriminant:
            bound *= int(self._discriminant_group.order())
        if self.determinant_kernel:
            bound *= 2
        if self.spinor_kernel:
            bound *= 2
        return bound

    def _enumerate_image(self):
        return self.supergroup.finite_image_lifts(
            self.image,
            multiply=self._multiply,
            image_bound=self._ambient_bound(),
        )

    def _allowed(self, key) -> bool:
        if self._has_discriminant:
            discriminant_image = key["discriminant"]
            if any(
                discriminant_image not in target
                for target in self.discriminant_preimages
            ):
                return False
        if self.determinant_kernel:
            if key["determinant"] != 1:
                return False
        if self.spinor_kernel and key["spinor"] != 1:
            return False
        return True

    def image_keys(self):
        return Set(tuple(self._witnesses))

    def subgroup_image_keys(self):
        return Set(
            tuple(key for key in self._witnesses if self._allowed(key))
        )

    def stabilizer_image_keys(self, stabilizer_generators):
        return frozenset(self.stabilizer_image_witnesses(stabilizer_generators))

    def stabilizer_image_witnesses(self, stabilizer_generators):
        r"""Return one live stabilizer element above every generated character image."""
        return self.supergroup.finite_image_lifts(
            self.image,
            generators=tuple(stabilizer_generators),
            multiply=self._multiply,
            image_bound=self._ambient_bound(),
        )

    def _gap_regular_model(self):
        r"""Return the right-regular libGAP model of the finite character image.

        The quotient keys remain the owned public representation.  GAP sees
        only their right-regular permutations, so its finite-group algorithms
        can compute subgroup and double-coset combinatorics without becoming
        part of the mathematical API.
        """
        keys = tuple(self.image_keys())
        positions = {key: position + 1 for position, key in enumerate(keys)}
        permutations = {}
        for key in keys:
            images = [
                positions[self._multiply(source, key)]
                for source in keys
            ]
            permutations[key] = libgap.PermList(images)
        group = libgap.Group(list(permutations.values()))
        if int(group.Size()) != len(keys):
            raise ArithmeticError(
                "the libGAP right-regular model does not have the character-image order"
            )
        return keys, permutations, group

    def right_coset_transversal(self):
        r"""Return one live lift for every right coset ``H r`` in the image.

        Here ``Q = rho(O(L))`` is the represented finite character image and
        ``H = rho(Gamma)`` is the image of the selected arithmetic subgroup.
        A right coset is therefore the subset ``H r = {h r : h in H}`` of
        ``Q``.  GAP computes representatives in the private regular-action
        model; before crossing them back, this method reconstructs those
        subsets with :meth:`_multiply` and verifies that they are disjoint and
        cover all of ``Q``.  The public result consists only of live lattice
        isometries lifting the chosen quotient representatives.
        """
        subgroup = self.subgroup_image_keys()
        keys, permutations, group = self._gap_regular_model()
        gap_subgroup = libgap.Subgroup(
            group,
            [permutations[key] for key in subgroup],
        )
        quotient_representatives = []
        for right_coset in libgap.RightCosets(group, gap_subgroup):
            gap_representative = right_coset.Representative()
            quotient_representative = next(
                (
                    key
                    for key in keys
                    if permutations[key] == gap_representative
                ),
                None,
            )
            if quotient_representative is None:
                raise ArithmeticError(
                    "a libGAP right-coset representative did not cross back to the character image"
                )
            quotient_representatives.append(quotient_representative)

        owned_cosets = tuple(
            frozenset(
                self._multiply(subgroup_element, representative)
                for subgroup_element in subgroup
            )
            for representative in quotient_representatives
        )
        if len(set(owned_cosets)) != len(owned_cosets):
            raise ArithmeticError(
                "the selected right-coset representatives repeat a character-image coset"
            )
        covered = frozenset().union(*owned_cosets) if owned_cosets else frozenset()
        if Set(covered) != self.image_keys():
            raise ArithmeticError(
                "the selected right cosets do not cover the full character image"
            )
        return finite_ordered_set(
            tuple(
                self._witnesses[representative]
                for representative in quotient_representatives
            )
        )

    def splitting_isometries(self, stabilizer_generators):
        r"""Return one lift per ``Stab\image(O(L))/Gamma`` double coset."""
        stabilizer = self.stabilizer_image_keys(stabilizer_generators)
        subgroup = self.subgroup_image_keys()
        keys, permutations, group = self._gap_regular_model()
        left = libgap.Subgroup(
            group,
            [permutations[key] for key in stabilizer],
        )
        right = libgap.Subgroup(
            group,
            [permutations[key] for key in subgroup],
        )
        representatives = []
        for double_coset in libgap.DoubleCosets(group, left, right):
            gap_representative = double_coset.Representative()
            quotient_representative = next(
                (
                    key
                    for key in keys
                    if permutations[key] == gap_representative
                ),
                None,
            )
            if quotient_representative is None:
                raise ArithmeticError(
                    "a libGAP double-coset representative did not cross back to the character image"
                )
            representatives.append(self._witnesses[quotient_representative])
        return finite_ordered_set(tuple(representatives))

    def witness_meets_subgroup(self, witness, stabilizer_generators) -> bool:
        return self.adjust_witness_into_subgroup(witness, stabilizer_generators) is not None

    def adjust_witness_into_subgroup(self, witness, target_stabilizer_generators):
        r"""Left-adjust ``witness`` by the target stabilizer until it lies in the subgroup.

        If ``witness(x)=y`` and ``t`` stabilizes ``y``, then ``t*witness`` still
        carries ``x`` to ``y``.  Thus the relevant finite-character condition
        is ``rho(t) rho(witness) in rho(Gamma)``.  Right multiplication by a
        target stabilizer would instead act on the source and is not the same
        transporter problem.
        """
        if witness in self.subgroup:
            return witness
        subgroup_keys = self.subgroup_image_keys()
        for stabilizer_key, stabilizer_witness in self.stabilizer_image_witnesses(
            target_stabilizer_generators
        ).items():
            candidate_key = self._multiply(stabilizer_key, self.image(witness))
            if candidate_key not in subgroup_keys:
                continue
            candidate = stabilizer_witness * witness
            if candidate not in self.subgroup:
                raise ArithmeticError(
                    "complete finite-character data accepted a transporter excluded by its subgroup predicate"
                )
            return candidate
        return None


_MISSING_ARITHMETIC_GENERATING_SET = (
    "Over an indefinite lattice O(L) is an infinite arithmetic group and this "
    "subgroup has no owned generating set.  The missing operation is a "
    "generating set for an arithmetic subgroup of O(L), owned by lattice_engines"
)


def _finite_supergroup_elements(subgroup):
    r"""Return the elements of a subgroup whose supergroup is a finite ``O(L)``.

    A predicate subgroup with no character data has no finite quotient of
    ``O(L)`` describing it, so the only thing that describes it is the group
    itself.  Listing it is a finite computation exactly when ``O(L)`` is
    finite, which for a lattice is definiteness.
    """
    supergroup = subgroup.supergroup()
    lattice = supergroup.domain()
    assert lattice.is_definite(), (
        f"{subgroup} is cut out by a predicate that is not a character kernel, "
        "so it is described by acting with the subgroup itself.  That is a "
        "finite computation only for a definite lattice.  "
        + _MISSING_ARITHMETIC_GENERATING_SET
    )
    return tuple(
        automorphism for automorphism in supergroup if automorphism in subgroup
    )


def _finite_subgroup_vector_orbit_representatives(subgroup, square):
    r"""Return one representative of each orbit of a listable subgroup."""
    lattice = subgroup.supergroup().domain()
    action = FiniteGSets(subgroup)(
        lattice.vectors_of_square(square),
        lambda automorphism, vector: automorphism(vector),
    )
    return finite_ordered_set(
        tuple(orbit.representative() for orbit in action.orbits())
    )


def _subgroup_vector_orbit_representatives(subgroup, square):
    if not subgroup.contains_character_kernel():
        return _finite_subgroup_vector_orbit_representatives(subgroup, square)
    quotient = OrthogonalCharacterQuotient(subgroup)
    orthogonal_group = subgroup.supergroup()
    def split_representatives():
        for representative in orthogonal_group.vector_orbit_representatives(square):
            stabilizer = orthogonal_group.vector_stabilizer_generators(representative)
            for splitting in quotient.splitting_isometries(stabilizer):
                yield splitting(representative)

    return finite_ordered_set(split_representatives())


def _subgroup_vector_equivalence_witness(subgroup, left, right):
    orthogonal_group = subgroup.supergroup()
    if not subgroup.contains_character_kernel():
        lattice = orthogonal_group.domain()
        source, target = lattice(left), lattice(right)
        return next(
            (
                automorphism
                for automorphism in _finite_supergroup_elements(subgroup)
                if automorphism(source) == target
            ),
            None,
        )
    witness = orthogonal_group.vector_equivalence_witness(left, right)
    if witness is None:
        return None
    stabilizer = orthogonal_group.vector_stabilizer_generators(right)
    return OrthogonalCharacterQuotient(subgroup).adjust_witness_into_subgroup(
        witness, stabilizer
    )


def _assert_isotropic_splitting_has_character_data(subgroup) -> None:
    r"""Assert that a subgroup splitting isotropic orbits carries character data.

    A primitive isotropic subobject of positive rank exists only in an
    indefinite lattice, so the route that reads a predicate subgroup by listing
    it inside a finite ``O(L)`` is never available here: that listing is finite
    only for a definite lattice, and a definite lattice has no isotropic
    vector.  Character data is therefore the only description of a subgroup
    that splits an isotropic orbit.
    """
    assert subgroup.contains_character_kernel(), (
        f"{subgroup} is cut out by a predicate that is not a character kernel, "
        "so no finite character quotient describes it, and the subgroup itself "
        "cannot be listed instead: that listing is finite only for a definite "
        "lattice, which has no isotropic vector.  "
        + _MISSING_ARITHMETIC_GENERATING_SET
    )


def _subgroup_isotropic_orbit_representatives(subgroup, rank, *, flag=False):
    _assert_isotropic_splitting_has_character_data(subgroup)
    quotient = OrthogonalCharacterQuotient(subgroup)
    orthogonal_group = subgroup.supergroup()
    representatives = []
    for representative in orthogonal_group.isotropic_orbit_representatives(
        rank, flag=flag
    ):
        stabilizer = orthogonal_group.isotropic_stabilizer_generators(
            representative, flag=flag
        )
        representatives.extend(
            splitting.transport_isotropic_object(representative)
            for splitting in quotient.splitting_isometries(stabilizer)
        )
    return finite_ordered_set(tuple(representatives))


def _subgroup_isotropic_equivalence_witness(subgroup, left, right, *, flag=False):
    _assert_isotropic_splitting_has_character_data(subgroup)
    orthogonal_group = subgroup.supergroup()
    witness = orthogonal_group.isotropic_equivalence_witness(
        left, right, flag=flag
    )
    if witness is None:
        return None
    stabilizer = orthogonal_group.isotropic_stabilizer_generators(
        right, flag=flag
    )
    return OrthogonalCharacterQuotient(subgroup).adjust_witness_into_subgroup(
        witness, stabilizer
    )


__all__ = ["OrthogonalCharacterQuotient"]
