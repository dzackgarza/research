from __future__ import annotations

import subprocess
import tempfile
import textwrap
from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from pathlib import Path

from sage.all import (
    QQ,
    ZZ,
    IntegralLattice,
    MatrixGroup,
    identity_matrix,
    lcm,
    matrix,
    vector,
)
from sage.structure.sequence import Sequence
from src.backends.external.py_polyhedral import (
    indefinite_form_get_orbit_representative,
    indefinite_form_stabilizer_vector,
    indefinite_form_test_equivalence_vector,
)


def find_vector_isometry_in_group(group, v1, v2):
    problem = _OrbitProblem.from_inputs(group, v1, v2)
    if problem is None:
        return None
    return _DawesOrbitBackend(problem).find_witness()


def vectors_are_equivalent_in_group(group, v1, v2) -> bool:
    return find_vector_isometry_in_group(group, v1, v2) is not None


def real_spinor_norm_sign(lattice, M) -> int:
    return _real_spinor_norm_signs(lattice, [M])[0]


def induced_discriminant_action(lattice, M):
    disc = lattice.discriminant_group()
    images = tuple(disc(M * generator.lift()._ambient_vector()) for generator in disc.gens())
    return _reduce_discriminant_action_matrix(lattice, _discriminant_images_to_matrix(images))


@dataclass(frozen=True)
class _SubgroupOrbitSpec:
    lattice: object
    determinant_kernel: bool
    positive_spinor_kernel: bool
    discriminant_preimages: tuple
    opaque: bool

    def allows_discriminant_action(self, discriminant_action):
        if not self.discriminant_preimages:
            return discriminant_action in self.lattice.discriminant_group().orthogonal_group()
        return all(discriminant_action in subgroup for subgroup in self.discriminant_preimages)

    def without_orientation_kernels(self):
        return _SubgroupOrbitSpec(
            lattice=self.lattice,
            determinant_kernel=False,
            positive_spinor_kernel=False,
            discriminant_preimages=self.discriminant_preimages,
            opaque=self.opaque,
        )


@dataclass(frozen=True)
class _OrbitProblem:
    group: object
    lattice: object
    spec: _SubgroupOrbitSpec
    w1: object
    w2: object
    norm: object
    scale: object

    @classmethod
    def from_inputs(cls, group, v1, v2):
        lattice = group.lattice
        normalized = _normalize_nonisotropic_pair(lattice, v1, v2)
        if normalized is None:
            return None
        w1, w2 = normalized
        return cls(
            group=group,
            lattice=lattice,
            spec=_compile_subgroup_spec(group),
            w1=w1,
            w2=w2,
            norm=_quadratic_norm(lattice, vector(QQ, w1)),
            scale=_minimal_positive_scale(vector(QQ, w1)),
        )


@dataclass(frozen=True)
class _ComplementDecomposition:
    vector: object
    line_lattice: object
    complement_lattice: object
    inclusion_matrix: object
    inverse_inclusion_matrix: object
    direct_sum_lattice: object
    direct_discriminant: object
    gluing_subgroup: object
    quotient_discriminant: object
    iota: object

    @property
    def line_discriminant(self):
        return self.line_lattice.discriminant_group()

    @property
    def complement_discriminant(self):
        return self.complement_lattice.discriminant_group()

    @property
    def complement_rank(self) -> int:
        return self.complement_lattice.rank()

    def direct_sum_discriminant_element(self, ambient_vector):
        coordinates = self.inverse_inclusion_matrix * vector(QQ, list(ambient_vector))
        return self.direct_discriminant(coordinates)

    def inject_line_discriminant(self, element):
        lift = vector(
            QQ,
            list(element.lift()._ambient_vector()) + [QQ.zero()] * self.complement_rank,
        )
        return self.direct_discriminant(lift)

    def inject_complement_discriminant(self, element):
        lift = vector(
            QQ,
            [QQ.zero()] + list(element.lift()._ambient_vector()),
        )
        return self.direct_discriminant(lift)


class _DawesOrbitBackend:
    def __init__(self, problem: _OrbitProblem):
        self._problem = problem

    def find_witness(self):
        ambient_witness = _test_full_orthogonal_equivalence(
            self._problem.lattice,
            self._problem.w1,
            self._problem.w2,
        )
        if ambient_witness is None:
            return None
        if ambient_witness in self._problem.group:
            return ambient_witness

        if _complement_of_vector_is_definite(self._problem.lattice, self._problem.w1):
            return self._solve_algorithm_21()

        self._assert_algorithm_22_hypotheses()
        if not self._solve_algorithm_22():
            return None

        witness = _find_structured_witness(
            self._problem.group,
            self._problem.w2,
            ambient_witness,
            self._problem.spec,
        )
        if witness is None and (self._problem.spec.determinant_kernel or self._problem.spec.positive_spinor_kernel):
            base_witness = self._find_relaxed_structured_witness(ambient_witness)
            if base_witness is not None:
                witness = self._adjust_relaxed_witness_via_root_reflections(base_witness)
        assert witness is not None or self._problem.spec.determinant_kernel or self._problem.spec.positive_spinor_kernel, (
            "Algorithm 2.2 detected an admissible discriminant witness but witness recovery failed"
        )
        return witness

    def _find_relaxed_structured_witness(self, ambient_witness):
        return _find_structured_witness_with_spec(
            self._problem.lattice,
            self._problem.w2,
            ambient_witness,
            self._problem.spec.without_orientation_kernels(),
        )

    def _adjust_relaxed_witness_via_root_reflections(self, base_witness):
        target = _build_complement_decomposition(
            self._problem.lattice,
            self._problem.w2,
        )
        for adjustment in _complement_reflection_adjustments(
            self._problem.lattice,
            target,
        ):
            candidate = adjustment * base_witness
            if candidate in self._problem.group:
                return candidate
        return None

    def _solve_algorithm_21(self):
        _, left_complement = _orthogonal_complement_data(
            self._problem.lattice,
            self._problem.w1,
        )
        _, right_complement = _orthogonal_complement_data(
            self._problem.lattice,
            self._problem.w2,
        )
        if left_complement.rank() == 0 and right_complement.rank() == 0:
            return None
        left = _build_complement_decomposition(self._problem.lattice, self._problem.w1)
        right = _build_complement_decomposition(self._problem.lattice, self._problem.w2)
        for psi in _search_definite_complement_isometries(
            left.complement_lattice,
            right.complement_lattice,
        ):
            theta = _assemble_witness_from_complement_data(
                self._problem.lattice,
                left,
                right,
                psi,
            )
            if theta is None:
                continue
            if theta in self._problem.group:
                return theta
        return None

    def _solve_algorithm_22(self) -> bool:
        left = _build_complement_decomposition(self._problem.lattice, self._problem.w1)
        right = _build_complement_decomposition(self._problem.lattice, self._problem.w2)
        if not left.complement_lattice.is_isometric_to(right.complement_lattice):
            return False
        return self._solve_algorithm_23(left, right)

    def _solve_algorithm_23(self, left, right) -> bool:
        for line_isometry in _rank_one_discriminant_isometries(
            left.line_discriminant,
            right.line_discriminant,
        ):
            for complement_isometry in _search_discriminant_form_isometries(
                left.complement_discriminant,
                right.complement_discriminant,
            ):
                direct_sum_isometry = _combined_direct_sum_discriminant_isometry(
                    left,
                    right,
                    line_isometry,
                    complement_isometry,
                )
                if not _gluing_subgroups_match(left, right, direct_sum_isometry):
                    continue
                discriminant_action = _induced_discriminant_action_from_gluing(
                    left,
                    right,
                    direct_sum_isometry,
                )
                if self._problem.spec.allows_discriminant_action(discriminant_action):
                    return True
        return False

    def _assert_algorithm_22_hypotheses(self):
        assert not self._problem.spec.opaque, "Algorithms 2.2/2.3 require a structured subgroup, not an opaque predicate"
        assert not _complement_of_vector_is_definite(
            self._problem.lattice,
            self._problem.w1,
        ), "Algorithm 2.2/2.3 requires an indefinite orthogonal complement"
        assert _ambient_discriminant_action_is_surjective(self._problem.lattice), (
            "Algorithm 2.2/2.3 requires surjectivity O(L) -> O(D(L))"
        )


def _compile_subgroup_spec(group):
    presentation = group._finite_quotient_presentation()
    if presentation is None:
        return _SubgroupOrbitSpec(
            lattice=group.lattice,
            determinant_kernel=False,
            positive_spinor_kernel=False,
            discriminant_preimages=(),
            opaque=True,
        )
    return _SubgroupOrbitSpec(
        lattice=group.lattice,
        determinant_kernel=presentation.determinant_kernel,
        positive_spinor_kernel=presentation.positive_spinor_kernel,
        discriminant_preimages=tuple(presentation.discriminant_preimages),
        opaque=False,
    )


def _normalize_nonisotropic_pair(lattice, v1, v2):
    qv1 = _qq_vector(v1)
    qv2 = _qq_vector(v2)
    norm1 = _quadratic_norm(lattice, qv1)
    norm2 = _quadratic_norm(lattice, qv2)
    assert not norm1.is_zero(), "This backend only handles non-isotropic vectors"
    assert not norm2.is_zero(), "This backend only handles non-isotropic vectors"
    scale1 = _minimal_positive_scale(qv1)
    scale2 = _minimal_positive_scale(qv2)
    if norm1 != norm2 or scale1 != scale2:
        return None
    w1 = vector(ZZ, [ZZ(scale1 * entry) for entry in qv1])
    w2 = vector(ZZ, [ZZ(scale2 * entry) for entry in qv2])
    return w1, w2


def _test_full_orthogonal_equivalence(lattice, w1, w2):
    raw_witness = indefinite_form_test_equivalence_vector(
        lattice._gram_rows(),
        [int(entry) for entry in w1],
        [int(entry) for entry in w2],
    )
    if raw_witness is None:
        return None
    return _normalize_raw_equivalence_witness(lattice, raw_witness, w1, w2)


def _build_complement_decomposition(lattice, w):
    line_lattice = type(lattice).Z().twist(int(_quadratic_norm(lattice, vector(QQ, w))))
    complement_basis, complement_lattice = _orthogonal_complement_data(lattice, w)
    inclusion_matrix = _column_matrix([vector(ZZ, list(w)), *complement_basis])
    inverse_inclusion_matrix = inclusion_matrix.inverse()
    direct_sum_gram = _block_diagonal_gram(
        line_lattice.inner_product_matrix(),
        complement_lattice.inner_product_matrix(),
    )
    direct_sum_lattice = type(lattice)._from_sage_like(IntegralLattice(direct_sum_gram))
    direct_discriminant = direct_sum_lattice.discriminant_group()
    data = _ComplementDecomposition(
        vector=vector(ZZ, list(w)),
        line_lattice=line_lattice,
        complement_lattice=complement_lattice,
        inclusion_matrix=inclusion_matrix,
        inverse_inclusion_matrix=inverse_inclusion_matrix,
        direct_sum_lattice=direct_sum_lattice,
        direct_discriminant=direct_discriminant,
        gluing_subgroup=None,
        quotient_discriminant=None,
        iota=None,
    )
    _assert_direct_sum_generator_split(data)
    gluing_generators = [data.direct_sum_discriminant_element(basis_vector) for basis_vector in lattice.basis()]
    gluing_subgroup = direct_discriminant.submodule(gluing_generators)
    gluing_orthogonal = direct_discriminant.orthogonal_submodule_to(gluing_subgroup)
    quotient_discriminant = gluing_orthogonal / gluing_subgroup
    lattice_discriminant = lattice.discriminant_group()
    iota_images = [
        quotient_discriminant(data.direct_sum_discriminant_element(generator.lift()._ambient_vector()))
        for generator in lattice_discriminant.gens()
    ]
    iota = lattice_discriminant.hom(quotient_discriminant).element_from_images(iota_images)
    assert iota.image().cardinality() == lattice_discriminant.cardinality()
    assert quotient_discriminant.cardinality() == lattice_discriminant.cardinality()
    return _ComplementDecomposition(
        vector=data.vector,
        line_lattice=data.line_lattice,
        complement_lattice=data.complement_lattice,
        inclusion_matrix=data.inclusion_matrix,
        inverse_inclusion_matrix=data.inverse_inclusion_matrix,
        direct_sum_lattice=data.direct_sum_lattice,
        direct_discriminant=data.direct_discriminant,
        gluing_subgroup=gluing_subgroup,
        quotient_discriminant=quotient_discriminant,
        iota=iota,
    )


def _assert_direct_sum_generator_split(data):
    return


def _search_definite_complement_isometries(left, right):
    if left.rank() == 0:
        yield matrix(ZZ, 0, 0, [])
        return
    left_positive = _positive_definite_copy(left)
    right_positive = _positive_definite_copy(right)
    standard_isometry = left_positive.quadratic_form().is_globally_equivalent_to(
        right_positive.quadratic_form(),
        return_matrix=True,
    )
    if standard_isometry is False:
        return
    # Sage returns the equivalence matrix in the opposite orientation from the
    # column-action convention used by the ambient lattice API, so invert here.
    base_isometry = matrix(ZZ, standard_isometry).inverse()
    automorphism_generators = [
        matrix(ZZ, generator.matrix().transpose()) for generator in left_positive.orthogonal_group().gens()
    ]
    if not automorphism_generators:
        yield base_isometry
        return
    for automorphism in MatrixGroup(automorphism_generators):
        yield base_isometry * matrix(ZZ, automorphism.matrix())


def _assemble_witness_from_complement_data(lattice, left, right, complement_isometry):
    block_matrix = _block_diagonal_with_scalar_one(complement_isometry)
    candidate = right.inclusion_matrix * block_matrix * left.inverse_inclusion_matrix
    if not all(entry in ZZ for entry in candidate.list()):
        return None
    witness = matrix(ZZ, candidate)
    gram = lattice.inner_product_matrix()
    assert witness.transpose() * gram * witness == gram
    assert witness * left.vector == right.vector
    return witness


def _search_discriminant_form_isometries(domain, codomain):
    assert domain.is_isometric_to(codomain)
    domain_gens = tuple(domain.smith_form_gens())
    codomain_elements = tuple(codomain)
    candidate_lists = []
    for generator in domain_gens:
        generator_order = generator.additive_order()
        candidate_lists.append([element for element in codomain_elements if element.additive_order() == generator_order])
    seen = set()
    for image_tuple in product(*candidate_lists):
        hom = domain._hom_from_smith(Sequence(image_tuple, universe=codomain))
        if hom.image().cardinality() != domain.cardinality():
            continue
        if not _is_discriminant_form_isometry(domain_gens, hom):
            continue
        key = tuple(tuple(int(entry) for entry in image.vector()) for image in image_tuple)
        if key in seen:
            continue
        seen.add(key)
        yield hom


def _rank_one_discriminant_isometries(domain, codomain):
    generator = codomain.gens()[0]
    for sign in (1, -1):
        yield domain.hom(codomain).element_from_images([sign * generator])


def _combined_direct_sum_discriminant_isometry(
    left,
    right,
    line_isometry,
    complement_isometry,
):
    images = [right.inject_line_discriminant(line_isometry(generator)) for generator in left.line_discriminant.gens()]
    images.extend(
        right.inject_complement_discriminant(complement_isometry(generator)) for generator in left.complement_discriminant.gens()
    )
    return left.direct_discriminant.hom(right.direct_discriminant).element_from_images(images)


def _gluing_subgroups_match(left, right, direct_sum_isometry):
    image_generators = [direct_sum_isometry(generator) for generator in left.gluing_subgroup.gens()]
    image_subgroup = right.direct_discriminant.submodule(image_generators)
    return image_subgroup.cardinality() == right.gluing_subgroup.cardinality() and all(
        generator in right.gluing_subgroup for generator in image_generators
    )


def _induced_discriminant_action_from_gluing(left, right, direct_sum_isometry):
    images = []
    for generator in left.iota.domain().gens():
        quotient_element = left.iota(generator)
        representative = left.direct_discriminant(quotient_element.lift())
        transported = direct_sum_isometry(representative)
        quotient_image = right.quotient_discriminant(transported)
        images.append(right.iota.lift(quotient_image))
    return _reduce_discriminant_action_matrix_for_group(
        left.iota.domain(),
        _discriminant_images_to_matrix(images),
    )


def _find_structured_witness(group, w2, ambient_witness, spec):
    witness = _find_structured_witness_with_spec(
        group.lattice,
        w2,
        ambient_witness,
        spec,
    )
    if witness is not None:
        assert witness in group
    return witness


def _find_structured_witness_with_spec(
    lattice,
    w2,
    ambient_witness,
    spec,
):
    stabilizer_generators = _stabilizer_generators(lattice, w2)
    spinor_images = None
    if spec.positive_spinor_kernel:
        spinor_images = _real_spinor_norm_signs(
            lattice,
            [*stabilizer_generators, ambient_witness],
        )
    product_image_generators = [
        _structured_image(
            lattice,
            generator,
            spec,
            precomputed_spinor=(None if spinor_images is None else spinor_images[index]),
        )
        for index, generator in enumerate(stabilizer_generators)
    ]
    ambient_image = _structured_image(
        lattice,
        ambient_witness,
        spec,
        precomputed_spinor=(None if spinor_images is None else spinor_images[-1]),
    )
    identity_witness = identity_matrix(ZZ, lattice.rank())
    identity_image = _structured_identity(lattice, spec)

    queue = deque([(identity_image, identity_witness)])
    seen = {_structured_key(identity_image)}

    while queue:
        current_image, current_witness = queue.popleft()
        candidate = current_witness * ambient_witness
        if _candidate_satisfies_constraints(
            lattice,
            candidate,
            current_image,
            ambient_image,
            spec,
        ):
            return candidate
        for generator, generator_image in zip(
            stabilizer_generators,
            product_image_generators,
            strict=True,
        ):
            next_image = _multiply_structured_images(
                lattice,
                current_image,
                generator_image,
                spec,
            )
            key = _structured_key(next_image)
            if key in seen:
                continue
            seen.add(key)
            queue.append((next_image, current_witness * generator))
    return None


def _complement_reflection_adjustments(lattice, decomposition):
    rank = lattice.rank()
    identity = identity_matrix(ZZ, rank)
    seen = {_matrix_key(identity)}
    yield identity

    positive_reflections = _stable_complement_reflections(lattice, decomposition, 2)
    negative_reflections = _stable_complement_reflections(lattice, decomposition, -2)

    for reflection in positive_reflections + negative_reflections:
        key = _matrix_key(reflection)
        if key in seen:
            continue
        seen.add(key)
        yield reflection

    for positive in positive_reflections:
        for negative in negative_reflections:
            for adjustment in (positive * negative, negative * positive):
                key = _matrix_key(adjustment)
                if key in seen:
                    continue
                seen.add(key)
                yield adjustment


def _stable_complement_reflections(lattice, decomposition, norm):
    reflection_extensions = []
    discriminant_rank = len(lattice.discriminant_group().gens())
    identity_discriminant = identity_matrix(ZZ, discriminant_rank)
    for root_vector in _candidate_root_vectors(decomposition.complement_lattice, norm):
        reflection = _reflection_matrix(
            decomposition.complement_lattice.inner_product_matrix(),
            root_vector,
        )
        extension = _assemble_witness_from_complement_data(
            lattice,
            decomposition,
            decomposition,
            reflection,
        )
        if extension is None:
            continue
        if induced_discriminant_action(lattice, extension) != identity_discriminant:
            continue
        reflection_extensions.append(extension)
    return reflection_extensions


def _candidate_root_vectors(lattice, norm):
    seen = set()
    candidates = []
    raw_candidates = indefinite_form_get_orbit_representative(
        lattice._gram_rows(),
        norm,
    )
    for raw_candidate in raw_candidates:
        candidate = vector(ZZ, raw_candidate)
        key = tuple(int(entry) for entry in candidate)
        if key in seen:
            continue
        seen.add(key)
        candidates.append(candidate)
    fallback_candidate = _search_integer_vector_of_norm(lattice, norm)
    if fallback_candidate is not None:
        key = tuple(int(entry) for entry in fallback_candidate)
        if key not in seen:
            candidates.append(fallback_candidate)
    return candidates


def _search_integer_vector_of_norm(lattice, norm, *, max_abs=6):
    rank = lattice.rank()
    for bound in range(1, max_abs + 1):
        for coefficients in product(range(-bound, bound + 1), repeat=rank):
            if all(coefficient == 0 for coefficient in coefficients):
                continue
            candidate = vector(ZZ, coefficients)
            if _quadratic_norm(lattice, candidate) == norm:
                return candidate
    return None


def _find_finite_black_box_witness(group, w2, ambient_witness):
    lattice = group.lattice
    stabilizer_generators = _stabilizer_generators(lattice, w2)
    if not stabilizer_generators:
        return None
    stabilizer_group = MatrixGroup(stabilizer_generators)
    assert stabilizer_group.is_finite()
    for stabilizer_element in stabilizer_group:
        candidate = matrix(ZZ, stabilizer_element.matrix()) * ambient_witness
        if candidate in group:
            return candidate
    return None


def _stabilizer_generators(lattice, w):
    raw_generators = indefinite_form_stabilizer_vector(
        lattice._gram_rows(),
        [int(entry) for entry in w],
    )
    return lattice._matrices_from_raw(raw_generators)


def _normalize_raw_equivalence_witness(lattice, raw_matrix, source, target):
    gram = lattice.inner_product_matrix()
    raw = matrix(ZZ, raw_matrix)
    candidate = raw.inverse().transpose()
    assert candidate.transpose() * gram * candidate == gram
    assert candidate * source == target
    return candidate


def _candidate_satisfies_constraints(
    lattice,
    candidate,
    stabilizer_image,
    ambient_image,
    spec,
):
    if spec.determinant_kernel:
        if stabilizer_image["determinant"] * ambient_image["determinant"] != 1:
            return False
    if spec.positive_spinor_kernel:
        if stabilizer_image["spinor"] * ambient_image["spinor"] != 1:
            return False
    if spec.discriminant_preimages:
        combined = _compose_discriminant_actions(
            lattice,
            stabilizer_image["discriminant"],
            ambient_image["discriminant"],
        )
        if not spec.allows_discriminant_action(combined):
            return False
    return True


def _structured_identity(lattice, spec):
    image = {}
    if spec.discriminant_preimages:
        discriminant_rank = len(lattice.discriminant_group().gens())
        image["discriminant"] = identity_matrix(ZZ, discriminant_rank)
    if spec.determinant_kernel:
        image["determinant"] = 1
    if spec.positive_spinor_kernel:
        image["spinor"] = 1
    return image


def _structured_image(lattice, M, spec, *, precomputed_spinor=None):
    image = {}
    if spec.discriminant_preimages:
        image["discriminant"] = induced_discriminant_action(lattice, M)
    if spec.determinant_kernel:
        image["determinant"] = _determinant_sign(M)
    if spec.positive_spinor_kernel:
        image["spinor"] = precomputed_spinor if precomputed_spinor is not None else real_spinor_norm_sign(lattice, M)
    return image


def _multiply_structured_images(lattice, left, right, spec):
    image = {}
    if spec.discriminant_preimages:
        image["discriminant"] = _compose_discriminant_actions(
            lattice,
            left["discriminant"],
            right["discriminant"],
        )
    if spec.determinant_kernel:
        image["determinant"] = left["determinant"] * right["determinant"]
    if spec.positive_spinor_kernel:
        image["spinor"] = left["spinor"] * right["spinor"]
    return image


def _structured_key(image):
    key = []
    if "discriminant" in image:
        key.append(("discriminant", _matrix_key(image["discriminant"])))
    if "determinant" in image:
        key.append(("determinant", int(image["determinant"])))
    if "spinor" in image:
        key.append(("spinor", int(image["spinor"])))
    return tuple(key)


def _ambient_discriminant_action_is_surjective(lattice) -> bool:
    key = _gram_key(lattice)
    cache = _ambient_discriminant_action_is_surjective.__dict__.setdefault(
        "_cache",
        {},
    )
    if key in cache:
        return cache[key]
    target_group = lattice.discriminant_group().orthogonal_group()
    image_group = target_group.subgroup(
        [induced_discriminant_action(lattice, generator) for generator in lattice.orthogonal_group().gens()]
    )
    cache[key] = all(generator in image_group for generator in target_group.gens())
    return cache[key]


def _is_discriminant_form_isometry(domain_gens, hom) -> bool:
    for left_generator in domain_gens:
        image_left = hom(left_generator)
        if image_left.q() != left_generator.q():
            return False
        for right_generator in domain_gens:
            image_right = hom(right_generator)
            if image_left.b(image_right) != left_generator.b(right_generator):
                return False
    return True


def _complement_of_vector_is_definite(lattice, w) -> bool:
    _, complement = _orthogonal_complement_data(lattice, w)
    positive_rank, negative_rank = complement.signature_pair()
    return positive_rank == 0 or negative_rank == 0


def _orthogonal_complement_data(lattice, w):
    primitive = vector(ZZ, [ZZ(entry) for entry in w])
    right_transform = _dawes_right_smith_transform(lattice, primitive)
    complement_basis = [vector(ZZ, list(right_transform.column(column))) for column in range(1, right_transform.ncols())]
    for basis_vector in complement_basis:
        assert (primitive * lattice.inner_product_matrix() * basis_vector.column())[0] == 0
    complement_gram = _gram_on_embedded_basis(
        lattice.inner_product_matrix(),
        complement_basis,
    )
    complement_lattice = type(lattice)._from_sage_like(IntegralLattice(complement_gram))
    return complement_basis, complement_lattice


def _dawes_right_smith_transform(lattice, w):
    pairing_row = matrix(
        ZZ,
        1,
        lattice.rank(),
        list(w * lattice.inner_product_matrix()),
    )
    _, _, right_transform = pairing_row.smith_form()
    return matrix(ZZ, right_transform)


def _positive_definite_copy(lattice):
    positive_rank, negative_rank = lattice.signature_pair()
    assert positive_rank == 0 or negative_rank == 0
    return lattice._sage_like() if not negative_rank else IntegralLattice(-lattice.inner_product_matrix())


def _block_diagonal_with_scalar_one(M):
    size = M.nrows()
    result = matrix(ZZ, size + 1, size + 1, 0)
    result[0, 0] = 1
    for i in range(size):
        for j in range(size):
            result[i + 1, j + 1] = M[i, j]
    return result


def _column_matrix(columns):
    if not columns:
        return matrix(ZZ, 0, 0, [])
    return matrix(QQ, len(columns[0]), len(columns), lambda i, j: QQ(columns[j][i]))


def _block_diagonal_gram(left, right):
    left_rank = left.nrows()
    right_rank = right.nrows()
    result = matrix(ZZ, left_rank + right_rank, left_rank + right_rank, 0)
    for i in range(left_rank):
        for j in range(left_rank):
            result[i, j] = ZZ(left[i, j])
    for i in range(right_rank):
        for j in range(right_rank):
            result[left_rank + i, left_rank + j] = ZZ(right[i, j])
    return result


def _gram_on_embedded_basis(ambient_gram, basis_vectors):
    if not basis_vectors:
        return matrix(ZZ, 0, 0, [])
    basis_matrix = matrix(ZZ, [list(basis_vector) for basis_vector in basis_vectors])
    return basis_matrix * ambient_gram * basis_matrix.transpose()


def _determinant_sign(M) -> int:
    determinant = ZZ(M.det())
    assert determinant in (ZZ.one(), -ZZ.one())
    return int(determinant)


def _discriminant_images_to_matrix(images):
    size = len(images)
    return matrix(ZZ, size, size, lambda i, j: ZZ(images[j].vector()[i]))


def _reduce_discriminant_action_matrix(lattice, action):
    return _reduce_discriminant_action_matrix_for_group(
        lattice.discriminant_group(),
        action,
    )


def _reduce_discriminant_action_matrix_for_group(discriminant_group, action):
    invariants = tuple(int(invariant) for invariant in discriminant_group.invariants())
    if not invariants:
        return matrix(ZZ, 0, 0, [])
    assert action.nrows() == len(invariants)
    return matrix(
        ZZ,
        action.nrows(),
        action.ncols(),
        lambda i, j: ZZ(action[i, j]) % invariants[i],
    )


def _compose_discriminant_actions(lattice, left, right):
    return _reduce_discriminant_action_matrix(lattice, left * right)


def _reflection_matrix(gram, root_vector):
    root = vector(QQ, list(root_vector))
    root_norm = (root * gram * root.column())[0]
    assert root_norm in (QQ(2), QQ(-2))
    pairing_row = matrix(QQ, 1, gram.nrows(), list(root * gram))
    reflection = identity_matrix(QQ, gram.nrows()) - (QQ(2) / root_norm) * root.column() * pairing_row
    assert all(entry in ZZ for entry in reflection.list())
    return matrix(ZZ, reflection)


def _compute_real_spinor_norm_sign(lattice, M) -> int:
    return _compute_real_spinor_norm_signs(lattice, [M])[0]


def _real_spinor_norm_signs(lattice, matrices):
    if _is_lorentzian_positive_cone_case(lattice):
        return [_lorentzian_positive_cone_sign(lattice, M) for M in matrices]
    gram_key = _gram_key(lattice)
    cache = real_spinor_norm_sign.__dict__.setdefault("_cache", {})
    keys = [(gram_key, _matrix_key(M)) for M in matrices]
    missing = [(key, M) for key, M in zip(keys, matrices, strict=True) if key not in cache]
    if missing:
        missing_signs = _compute_real_spinor_norm_signs(
            lattice,
            [M for _, M in missing],
        )
        for (key, _), sign in zip(missing, missing_signs, strict=True):
            cache[key] = sign
    return [cache[key] for key in keys]


def _compute_real_spinor_norm_signs(lattice, matrices):
    if not matrices:
        return []
    with tempfile.TemporaryDirectory() as tmp:
        gram_path = Path(tmp) / "gram.txt"
        _write_integer_matrix(gram_path, lattice._gram_rows())
        isometry_paths = []
        for index, M in enumerate(matrices):
            isometry_path = Path(tmp) / f"isometry_{index}.txt"
            _write_integer_matrix(isometry_path, _oscar_ambient_rows(M))
            isometry_paths.append(isometry_path)
        julia_program = textwrap.dedent(
            """
            using Oscar

            function read_int_matrix(path)
                rows = Vector{Vector{Int}}()
                open(path) do io
                    for line in eachline(io)
                        line = strip(line)
                        isempty(line) && continue
                        push!(rows, parse.(Int, split(line)))
                    end
                end
                n = length(rows)
                m = length(rows[1])
                return matrix(ZZ, n, m, reduce(vcat, rows))
            end

            gram = read_int_matrix(ARGS[1])
            lattice = integer_lattice(; gram = change_base_ring(QQ, gram))
            for path in ARGS[2:end]
                isometry = read_int_matrix(path)
                lattice_with_isometry = integer_lattice_with_isometry(
                    lattice,
                    change_base_ring(QQ, isometry);
                    check = true,
                )
                println(rational_spinor_norm(lattice_with_isometry))
            end
            """
        )
        result = subprocess.run(
            [
                "julia",
                "--startup-file=no",
                "-e",
                julia_program,
                str(gram_path),
                *(str(path) for path in isometry_paths),
            ],
            capture_output=True,
            text=True,
        )
    assert result.returncode == 0, result.stderr
    spinor_lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    assert len(spinor_lines) == len(matrices)
    spinors = [Fraction(line.replace("//", "/")) for line in spinor_lines]
    return [1 if spinor > 0 else -1 for spinor in spinors]


def _write_integer_matrix(path: Path, rows) -> None:
    with open(path, "w") as handle:
        for row in rows:
            handle.write(" ".join(str(int(entry)) for entry in row) + "\n")


def _matrix_rows(M):
    return [[int(entry) for entry in row] for row in M.rows()]


def _oscar_ambient_rows(M):
    return _matrix_rows(M.transpose())


def _gram_key(lattice):
    return tuple(tuple(int(entry) for entry in row) for row in lattice.inner_product_matrix().rows())


def _matrix_key(M):
    return tuple(tuple(int(entry) for entry in row) for row in M.rows())


def _is_lorentzian_positive_cone_case(lattice) -> bool:
    positive_rank, negative_rank = lattice.signature_pair()
    return positive_rank == 1 and negative_rank >= 1


def _lorentzian_positive_cone_sign(lattice, M) -> int:
    positive_vector = _lorentzian_positive_cone_vector(lattice)
    image_vector = M * positive_vector
    pairing = _inner_product(lattice, positive_vector, image_vector)
    assert pairing != 0
    return 1 if pairing > 0 else -1


def _lorentzian_positive_cone_vector(lattice):
    key = _gram_key(lattice)
    cache = _lorentzian_positive_cone_vector.__dict__.setdefault("_cache", {})
    if key not in cache:
        diagonal_form, change_of_basis = lattice.quadratic_form().rational_diagonal_form(return_matrix=True)
        diagonal_entries = diagonal_form.matrix().diagonal()
        positive_indices = [index for index, entry in enumerate(diagonal_entries) if entry > 0]
        assert len(positive_indices) == 1
        positive_vector = vector(QQ, list(change_of_basis.column(positive_indices[0])))
        assert _quadratic_norm(lattice, positive_vector) > 0
        cache[key] = positive_vector
    return cache[key]


def _minimal_positive_scale(v):
    denominators = [QQ(entry).denominator() for entry in v]
    scale = lcm(denominators) if denominators else ZZ.one()
    assert scale > 0
    return QQ(scale)


def _quadratic_norm(lattice, v):
    return _inner_product(lattice, v, v)


def _inner_product(lattice, left, right):
    return (left * lattice.inner_product_matrix() * right.column())[0]


def _qq_vector(v):
    return vector(QQ, list(v))
