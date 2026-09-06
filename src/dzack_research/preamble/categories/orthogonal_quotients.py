r"""Finite character quotients controlling arithmetic-subgroup orbit splitting."""
from dzack_research.preamble.categories.isotropic_orbits import transport_isotropic_object


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
        self.supergroup = subgroup.supergroup()
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
        if self._has_discriminant:
            self._discriminant_group = self.lattice.discriminant_group().O()
            for target in self.discriminant_preimages:
                ambient = (
                    target
                    if target is self._discriminant_group
                    else getattr(target, "supergroup", lambda: None)()
                )
                if ambient is not self._discriminant_group:
                    raise ValueError("a discriminant preimage must lie in O(A_L)")
        self._witnesses = self._enumerate_image()

    def image(self, isometry):
        components = []
        if self._has_discriminant:
            components.append(isometry.discriminant_morphism())
        if self.determinant_kernel:
            components.append(int(isometry.determinant()))
        if self.spinor_kernel:
            components.append(int(isometry.real_spinor_norm_sign()))
        return tuple(components)

    def _multiply(self, left, right):
        result = []
        position = 0
        if self._has_discriminant:
            result.append(left[position] * right[position])
            position += 1
        if self.determinant_kernel:
            result.append(left[position] * right[position])
            position += 1
        if self.spinor_kernel:
            result.append(left[position] * right[position])
        return tuple(result)

    def _inverse(self, value):
        result = []
        position = 0
        if self._has_discriminant:
            result.append(~value[position])
            position += 1
        if self.determinant_kernel:
            result.append(value[position])
            position += 1
        if self.spinor_kernel:
            result.append(value[position])
        return tuple(result)

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
        identity = self.supergroup.one()
        identity_key = self.image(identity)
        witnesses = {identity_key: identity}
        steps = []
        for generator in self.supergroup.group_generators():
            steps.append((self.image(generator), generator))
            inverse = ~generator
            steps.append((self.image(inverse), inverse))
        frontier = [identity_key]
        while frontier:
            current_key = frontier.pop()
            current_witness = witnesses[current_key]
            for step_key, step_witness in steps:
                candidate_key = self._multiply(step_key, current_key)
                if candidate_key in witnesses:
                    continue
                witnesses[candidate_key] = step_witness * current_witness
                frontier.append(candidate_key)
                if len(witnesses) > self._ambient_bound():
                    raise ArithmeticError(
                        "the generated character image exceeds its finite ambient product"
                    )
        return witnesses

    def _allowed(self, key) -> bool:
        position = 0
        if self._has_discriminant:
            discriminant_image = key[position]
            position += 1
            if any(
                discriminant_image not in target
                for target in self.discriminant_preimages
            ):
                return False
        if self.determinant_kernel:
            if key[position] != 1:
                return False
            position += 1
        if self.spinor_kernel and key[position] != 1:
            return False
        return True

    def image_keys(self):
        return frozenset(self._witnesses)

    def subgroup_image_keys(self):
        return frozenset(key for key in self._witnesses if self._allowed(key))

    def _generated_keys(self, generators):
        identity = self.image(self.supergroup.one())
        supplied = tuple(generators)
        steps = supplied + tuple(self._inverse(generator) for generator in supplied)
        known = {identity}
        frontier = [identity]
        while frontier:
            current = frontier.pop()
            for step in steps:
                candidate = self._multiply(step, current)
                if candidate not in known:
                    known.add(candidate)
                    frontier.append(candidate)
        return frozenset(known)

    def stabilizer_image_keys(self, stabilizer_generators):
        return self._generated_keys(
            tuple(self.image(generator) for generator in stabilizer_generators)
        )

    def splitting_isometries(self, stabilizer_generators):
        r"""Return one lift per ``Stab\image(O(L))/Gamma`` double coset."""
        stabilizer = self.stabilizer_image_keys(stabilizer_generators)
        subgroup = self.subgroup_image_keys()
        remaining = set(self.image_keys())
        representatives = []
        while remaining:
            representative = next(iter(remaining))
            representatives.append(self._witnesses[representative])
            double_coset = {
                self._multiply(self._multiply(left, representative), right)
                for left in stabilizer
                for right in subgroup
            }
            remaining.difference_update(double_coset)
        return tuple(representatives)

    def witness_meets_subgroup(self, witness, stabilizer_generators) -> bool:
        if witness in self.subgroup:
            return True
        target = self.image(witness)
        stabilizer = self.stabilizer_image_keys(stabilizer_generators)
        subgroup = self.subgroup_image_keys()
        return any(
            self._multiply(left, right) == target
            for left in subgroup
            for right in stabilizer
        )


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
    elements = _finite_supergroup_elements(subgroup)
    lattice = subgroup.supergroup().domain()
    remaining = {
        tuple(vector.to_tuple()): vector
        for vector in lattice.vectors_of_square(square)
    }
    representatives = []
    while remaining:
        _coordinates, representative = next(iter(remaining.items()))
        representatives.append(representative)
        for automorphism in elements:
            remaining.pop(tuple(automorphism(representative).to_tuple()), None)
    return tuple(representatives)


def subgroup_vector_orbit_representatives(subgroup, square):
    if not subgroup.contains_character_kernel():
        return _finite_subgroup_vector_orbit_representatives(subgroup, square)
    quotient = OrthogonalCharacterQuotient(subgroup)
    orthogonal_group = subgroup.supergroup()
    representatives = []
    seen = set()
    for representative in orthogonal_group.vector_orbit_representatives(square):
        stabilizer = orthogonal_group.vector_stabilizer_generators(representative)
        for splitting in quotient.splitting_isometries(stabilizer):
            image = splitting(representative)
            key = tuple(image.to_tuple())
            if key not in seen:
                seen.add(key)
                representatives.append(image)
    return tuple(representatives)


def subgroup_vectors_are_equivalent(subgroup, left, right) -> bool:
    orthogonal_group = subgroup.supergroup()
    if not subgroup.contains_character_kernel():
        lattice = orthogonal_group.domain()
        source, target = lattice(left), lattice(right)
        return any(
            automorphism(source) == target
            for automorphism in _finite_supergroup_elements(subgroup)
        )
    witness = orthogonal_group.vector_equivalence_witness(left, right)
    if witness is None:
        return False
    stabilizer = orthogonal_group.vector_stabilizer_generators(right)
    return OrthogonalCharacterQuotient(subgroup).witness_meets_subgroup(
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


def subgroup_isotropic_orbit_representatives(subgroup, rank, *, flag=False):
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
            transport_isotropic_object(splitting, representative)
            for splitting in quotient.splitting_isometries(stabilizer)
        )
    return tuple(representatives)


def subgroup_isotropic_are_equivalent(subgroup, left, right, *, flag=False) -> bool:
    _assert_isotropic_splitting_has_character_data(subgroup)
    orthogonal_group = subgroup.supergroup()
    witness = orthogonal_group.isotropic_equivalence_witness(
        left, right, flag=flag
    )
    if witness is None:
        return False
    stabilizer = orthogonal_group.isotropic_stabilizer_generators(
        right, flag=flag
    )
    return OrthogonalCharacterQuotient(subgroup).witness_meets_subgroup(
        witness, stabilizer
    )


__all__ = [
    "OrthogonalCharacterQuotient",
    "subgroup_isotropic_are_equivalent",
    "subgroup_isotropic_orbit_representatives",
    "subgroup_vector_orbit_representatives",
    "subgroup_vectors_are_equivalent",
]
