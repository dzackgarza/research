from __future__ import annotations

import hashlib
import json
import logging
import os
from dataclasses import dataclass
from pathlib import Path

from sage.all import ZZ, MatrixGroup, matrix, vector
from sage.libs.gap.libgap import libgap
from src.backends.dawes_orbit_backend import (
    induced_discriminant_action,
    real_spinor_norm_sign,
)
from src.backends.external.py_polyhedral import (
    indefinite_form_test_equivalence_isotropic_k_plane,
    indefinite_form_test_equivalence_vector,
)

_LOGGER = logging.getLogger(__name__)
_CACHE_ENV_VAR = "COBLE_RESEARCH_CACHE_DIR"
_CACHE_NAMESPACE = "isotropic_gamma_orbit_backend"
_MEMORY_CACHE: dict[tuple[str, str], object] = {}


def isotropic_line_orbits_in_group(group):
    return _IsotropicOrbitBackend(group, "line").orbit_representatives()


def isotropic_plane_orbits_in_group(group):
    return _IsotropicOrbitBackend(group, "plane").orbit_representatives()


def isotropic_flag_orbits_in_group(group, k):
    return _IsotropicOrbitBackend(group, "flag", flag_depth=k).orbit_representatives()


def isotropic_lines_are_equivalent_in_group(group, v1, v2) -> bool:
    return _IsotropicOrbitBackend(group, "line").objects_are_equivalent(v1, v2)


def isotropic_planes_are_equivalent_in_group(group, basis1, basis2) -> bool:
    return _IsotropicOrbitBackend(group, "plane").objects_are_equivalent(
        tuple(basis1),
        tuple(basis2),
    )


@dataclass(frozen=True)
class _StructuredSubgroupSpec:
    lattice: object
    determinant_kernel: bool
    positive_spinor_kernel: bool
    discriminant_preimages: tuple
    opaque: bool


@dataclass
class _FiniteQuotientSpec:
    ambient_group: object
    source_group: object
    source_gap_group: object
    target_gap_group: object
    subgroup_image: object
    hom: object
    image_from_matrix: object

    def image(self, M):
        return self.image_from_matrix(matrix(ZZ, M))

    def image_subgroup(self, matrices):
        return _gap_subgroup(
            self.target_gap_group,
            [self.image(M) for M in matrices],
        )

    def lift(self, target_element):
        lifted = libgap.PreImagesRepresentative(self.hom, target_element)
        return matrix(ZZ, lifted)


class _IsotropicOrbitBackend:
    def __init__(self, group, orbit_kind, *, flag_depth=None):
        self._group = group
        self._lattice = group.lattice
        self._orbit_kind = orbit_kind
        self._flag_depth = flag_depth
        self._spec = _compile_subgroup_spec(group)
        self._finite_quotient = _cached_finite_quotient_spec(group, self._spec)

    def orbit_representatives(self):
        key_payload = {
            "lattice": self._lattice._gram_rows(),
            "orbit_kind": self._orbit_kind,
            "flag_depth": self._flag_depth,
            "spec": _structured_spec_payload(self._spec),
        }
        return _cached_artifact(
            "subgroup_orbit_representatives",
            key_payload,
            compute_fn=self._compute_orbit_representatives,
            serialize_fn=lambda reps: [_serialize_isotropic_object(self._orbit_kind, rep) for rep in reps],
            deserialize_fn=lambda payload: [_normalize_isotropic_object(self._lattice, self._orbit_kind, rep) for rep in payload],
            validate_fn=lambda reps: _validate_orbit_representatives(
                self._lattice,
                self._orbit_kind,
                reps,
            ),
            label=(f"{self._orbit_kind} orbit representatives for {_structured_spec_label(self._spec)}"),
        )

    def objects_are_equivalent(self, left, right) -> bool:
        ambient_witness = _ambient_equivalence_witness(
            self._lattice,
            self._orbit_kind,
            left,
            right,
        )
        if ambient_witness is None:
            return False
        if ambient_witness in self._group:
            return True
        assert self._finite_quotient is not None, "Subgroup isotropic equivalence requires a computable finite quotient image"
        stabilizer_gens = _ambient_stabilizer_generators(
            self._lattice,
            self._orbit_kind,
            _normalize_isotropic_object(self._lattice, self._orbit_kind, right),
        )
        stabilizer_image = self._finite_quotient.image_subgroup(stabilizer_gens)
        identity_double_coset = libgap.DoubleCoset(
            stabilizer_image,
            libgap.One(self._finite_quotient.target_gap_group),
            self._finite_quotient.subgroup_image,
        )
        return self._finite_quotient.image(ambient_witness) in identity_double_coset

    def _compute_orbit_representatives(self):
        ambient_orbits = _ambient_isotropic_orbits(
            self._lattice,
            self._orbit_kind,
            flag_depth=self._flag_depth,
        )
        if self._finite_quotient is None:
            return list(ambient_orbits)
        orbit_reps = []
        for ambient_rep in ambient_orbits:
            stabilizer_gens = _ambient_stabilizer_generators(
                self._lattice,
                self._orbit_kind,
                ambient_rep,
            )
            stabilizer_image = self._finite_quotient.image_subgroup(stabilizer_gens)
            double_cosets = libgap.DoubleCosets(
                self._finite_quotient.target_gap_group,
                stabilizer_image,
                self._finite_quotient.subgroup_image,
            )
            for double_coset in double_cosets:
                representative = libgap.Representative(double_coset)
                lift = self._finite_quotient.lift(representative)
                orbit_reps.append(
                    _apply_ambient_isometry(
                        self._lattice,
                        self._orbit_kind,
                        ambient_rep,
                        lift,
                    )
                )
        return orbit_reps


def _compile_subgroup_spec(group):
    presentation = group._finite_quotient_presentation()
    if presentation is None:
        return _StructuredSubgroupSpec(
            lattice=group.lattice,
            determinant_kernel=False,
            positive_spinor_kernel=False,
            discriminant_preimages=(),
            opaque=True,
        )
    return _StructuredSubgroupSpec(
        lattice=group.lattice,
        determinant_kernel=presentation.determinant_kernel,
        positive_spinor_kernel=presentation.positive_spinor_kernel,
        discriminant_preimages=tuple(presentation.discriminant_preimages),
        opaque=False,
    )


def _cached_finite_quotient_spec(group, spec):
    cached = getattr(group, "_cached_isotropic_finite_quotient_spec", None)
    if cached is not None:
        return cached
    finite_quotient = _finite_quotient_spec(group, spec)
    group._cached_isotropic_finite_quotient_spec = finite_quotient
    return finite_quotient


def _cache_root() -> Path | None:
    cache_dir = os.environ.get(_CACHE_ENV_VAR)
    if not cache_dir:
        return None
    return Path(cache_dir) / _CACHE_NAMESPACE


def _cache_digest(payload) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _cache_path(kind: str, payload) -> Path | None:
    root = _cache_root()
    if root is None:
        return None
    return root / kind / f"{_cache_digest(payload)}.json"


def _cached_artifact(
    kind: str,
    key_payload,
    *,
    compute_fn,
    serialize_fn,
    deserialize_fn,
    validate_fn,
    label: str,
):
    digest = _cache_digest(key_payload)
    memory_key = (kind, digest)
    if memory_key in _MEMORY_CACHE:
        _LOGGER.warning("using in-memory cache for %s", label)
        return _MEMORY_CACHE[memory_key]
    path = _cache_path(kind, key_payload)
    if path is not None and path.exists():
        cached_payload = json.loads(path.read_text())
        assert cached_payload["kind"] == kind
        assert cached_payload["digest"] == digest
        value = deserialize_fn(cached_payload["value"])
        validate_fn(value)
        _MEMORY_CACHE[memory_key] = value
        _LOGGER.warning("using disk cache for %s from %s", label, path)
        return value
    value = compute_fn()
    validate_fn(value)
    _MEMORY_CACHE[memory_key] = value
    if path is not None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(
                {
                    "kind": kind,
                    "digest": digest,
                    "value": serialize_fn(value),
                },
                indent=2,
                sort_keys=True,
            )
            + "\n"
        )
    return value


def _finite_quotient_spec(group, spec):
    if _is_full_ambient_group(group):
        return None
    assert not spec.opaque, "Subgroup isotropic splitting requires structured subgroup constraints"
    factors = []
    if spec.discriminant_preimages:
        ambient_disc_group = spec.lattice.discriminant_group().orthogonal_group()
        sage_disc_group = ambient_disc_group._require_sage_group()
        disc_gap_group = libgap(sage_disc_group)
        allowed_disc_group = disc_gap_group
        for subgroup in spec.discriminant_preimages:
            allowed_disc_group = libgap.Intersection(allowed_disc_group, libgap(subgroup._sage_subgroup))

        def _disc_image(M, _lattice=spec.lattice, _sage_disc_group=sage_disc_group):
            return libgap(_sage_disc_group(induced_discriminant_action(_lattice, M)))

        factors.append(
            (
                disc_gap_group,
                allowed_disc_group,
                _disc_image,
            )
        )
    if spec.determinant_kernel:
        c2_det = libgap.CyclicGroup(2)
        det_gen = c2_det.GeneratorsOfGroup()[0]

        def _det_image(M, _det_gen=det_gen, _c2_det=c2_det):
            return libgap.One(_c2_det) if ZZ(M.det()) == 1 else _det_gen

        factors.append(
            (
                c2_det,
                _gap_subgroup(c2_det, []),
                _det_image,
            )
        )
    if spec.positive_spinor_kernel:
        c2_spin = libgap.CyclicGroup(2)
        spin_gen = c2_spin.GeneratorsOfGroup()[0]

        def _spin_image(M, _spin_gen=spin_gen, _c2_spin=c2_spin, _lattice=spec.lattice):
            return libgap.One(_c2_spin) if real_spinor_norm_sign(_lattice, M) == 1 else _spin_gen

        factors.append(
            (
                c2_spin,
                _gap_subgroup(c2_spin, []),
                _spin_image,
            )
        )
    assert factors, "Subgroup isotropic splitting requires determinant, spinor, or discriminant-image data"
    ambient_group = spec.lattice.orthogonal_group()
    ambient_generators = [matrix(ZZ, generator) for generator in ambient_group.gens()]
    source_group = MatrixGroup(ambient_generators)
    source_gap_group = libgap(source_group)

    if len(factors) == 1:
        target_gap_group, allowed_group, image_fn = factors[0]
        target_images = [image_fn(generator) for generator in ambient_generators]

        def _image_from_matrix(M, _image_fn=image_fn):
            return _image_fn(M)

    else:
        target_gap_group = libgap.DirectProduct(*[factor[0] for factor in factors])
        embeddings = [libgap.Embedding(target_gap_group, index + 1) for index in range(len(factors))]
        target_images = []
        for generator in ambient_generators:
            product_image = libgap.One(target_gap_group)
            for embedding, (_, _, image_fn) in zip(embeddings, factors, strict=True):
                product_image *= libgap.Image(embedding, image_fn(generator))
            target_images.append(product_image)
        allowed_gens = []
        for embedding, (_, allowed_factor, _) in zip(embeddings, factors, strict=True):
            allowed_gens.extend(libgap.Image(embedding, gen) for gen in allowed_factor.GeneratorsOfGroup())
        allowed_group = _gap_subgroup(target_gap_group, allowed_gens)

        def _image_from_matrix(M, _embeddings=embeddings, _factors=factors, _target=target_gap_group):
            product_image = libgap.One(_target)
            for embedding, (_, _, image_fn) in zip(_embeddings, _factors, strict=True):
                product_image *= libgap.Image(embedding, image_fn(M))
            return product_image

    target_image_group = _gap_subgroup(target_gap_group, target_images)
    subgroup_image = libgap.Intersection(target_image_group, allowed_group)
    hom = libgap.GroupHomomorphismByImagesNC(
        source_gap_group,
        target_gap_group,
        source_gap_group.GeneratorsOfGroup(),
        target_images,
    )
    return _FiniteQuotientSpec(
        ambient_group=ambient_group,
        source_group=source_group,
        source_gap_group=source_gap_group,
        target_gap_group=target_image_group,
        subgroup_image=subgroup_image,
        hom=hom,
        image_from_matrix=_image_from_matrix,
    )


def _is_full_ambient_group(group) -> bool:
    presentation = group._finite_quotient_presentation()
    if presentation is None:
        return False
    return group.__class__.__name__ == "LatticeOrthogonalGroup" and presentation.is_ambient()


def _gap_subgroup(parent_group, generators):
    generators = list(generators)
    if generators:
        return libgap.Subgroup(parent_group, generators)
    return libgap.TrivialSubgroup(parent_group)


def _ambient_isotropic_orbits(lattice, orbit_kind, *, flag_depth=None):
    key_payload = {
        "lattice": lattice._gram_rows(),
        "orbit_kind": orbit_kind,
        "flag_depth": flag_depth,
    }
    return tuple(
        _cached_artifact(
            "ambient_isotropic_orbits",
            key_payload,
            compute_fn=lambda: _compute_ambient_isotropic_orbits(
                lattice,
                orbit_kind,
                flag_depth=flag_depth,
            ),
            serialize_fn=lambda reps: [_serialize_isotropic_object(orbit_kind, rep) for rep in reps],
            deserialize_fn=lambda payload: tuple(_normalize_isotropic_object(lattice, orbit_kind, rep) for rep in payload),
            validate_fn=lambda reps: _validate_orbit_representatives(
                lattice,
                orbit_kind,
                reps,
            ),
            label=f"ambient {orbit_kind} orbits for lattice of rank {lattice.rank()}",
        )
    )


def _ambient_stabilizer_generators(lattice, orbit_kind, isotropic_object):
    normalized = _normalize_isotropic_object(lattice, orbit_kind, isotropic_object)
    key_payload = {
        "lattice": lattice._gram_rows(),
        "orbit_kind": orbit_kind,
        "object": _serialize_isotropic_object(orbit_kind, normalized),
    }
    return list(
        _cached_artifact(
            "ambient_stabilizer_generators",
            key_payload,
            compute_fn=lambda: _compute_ambient_stabilizer_generators(
                lattice,
                orbit_kind,
                normalized,
            ),
            serialize_fn=lambda gens: [_matrix_rows(generator) for generator in gens],
            deserialize_fn=lambda payload: [matrix(ZZ, rows) for rows in payload],
            validate_fn=lambda gens: _validate_stabilizer_generators(
                lattice,
                orbit_kind,
                normalized,
                gens,
            ),
            label=f"ambient stabilizer for {orbit_kind} object",
        )
    )


def _normalize_primitive_line(v):
    primitive = vector(ZZ, list(v))
    gcd_value = ZZ.zero()
    for entry in primitive:
        gcd_value = gcd_value.gcd(ZZ(entry))
    assert gcd_value > 0
    primitive = vector(ZZ, [ZZ(entry) // gcd_value for entry in primitive])
    for entry in primitive:
        if entry:
            return -primitive if entry < 0 else primitive
    assert False, "Primitive isotropic line representative must be nonzero"


def _normalize_isotropic_object(lattice, orbit_kind, isotropic_object):
    if orbit_kind == "line":
        return lattice(_normalize_primitive_line(isotropic_object))
    if orbit_kind == "plane":
        return tuple(lattice(vector(ZZ, list(row))) for row in isotropic_object)
    assert orbit_kind == "flag"
    return tuple(lattice(vector(ZZ, list(row))) for row in isotropic_object)


def _apply_ambient_isometry(lattice, orbit_kind, isotropic_object, M):
    if orbit_kind == "line":
        image = lattice(M * vector(ZZ, list(isotropic_object)))
        return lattice(_normalize_primitive_line(image))
    images = tuple(lattice(M * vector(ZZ, list(row))) for row in isotropic_object)
    return images


def _ambient_equivalence_witness(lattice, orbit_kind, left, right):
    normalized_left = _normalize_isotropic_object(lattice, orbit_kind, left)
    normalized_right = _normalize_isotropic_object(lattice, orbit_kind, right)
    key_payload = {
        "lattice": lattice._gram_rows(),
        "orbit_kind": orbit_kind,
        "left": _serialize_isotropic_object(orbit_kind, normalized_left),
        "right": _serialize_isotropic_object(orbit_kind, normalized_right),
    }
    return _cached_artifact(
        "ambient_equivalence_witness",
        key_payload,
        compute_fn=lambda: _compute_ambient_equivalence_witness(
            lattice,
            orbit_kind,
            normalized_left,
            normalized_right,
        ),
        serialize_fn=lambda witness: None if witness is None else _matrix_rows(witness),
        deserialize_fn=lambda payload: None if payload is None else matrix(ZZ, payload),
        validate_fn=lambda witness: _validate_equivalence_witness(
            lattice,
            orbit_kind,
            normalized_left,
            normalized_right,
            witness,
        ),
        label=f"ambient equivalence witness for {orbit_kind} objects",
    )


def _compute_ambient_isotropic_orbits(lattice, orbit_kind, *, flag_depth=None):
    if orbit_kind == "line":
        return tuple(lattice(_normalize_primitive_line(v)) for v in lattice.isotropic_line_orbits())
    if orbit_kind == "plane":
        return tuple(tuple(lattice(v) for v in pair) for pair in lattice.isotropic_plane_orbits())
    assert orbit_kind == "flag"
    assert flag_depth is not None and flag_depth >= 1
    return tuple(tuple(lattice(v) for v in flag) for flag in lattice.isotropic_flag_orbits(flag_depth))


def _compute_ambient_stabilizer_generators(lattice, orbit_kind, isotropic_object):
    ambient_group = lattice.orthogonal_group()
    if orbit_kind == "line":
        return ambient_group.stabilizer_of_isotropic_line(isotropic_object).gens()
    if orbit_kind == "plane":
        return ambient_group.stabilizer_of_isotropic_plane(*isotropic_object).gens()
    assert orbit_kind == "flag"
    return ambient_group.stabilizer_of_isotropic_flag(list(isotropic_object)).gens()


def _compute_ambient_equivalence_witness(lattice, orbit_kind, left, right):
    if orbit_kind == "line":
        left_vec = vector(ZZ, list(_normalize_primitive_line(left)))
        right_vec = vector(ZZ, list(_normalize_primitive_line(right)))
        for target in (right_vec, -right_vec):
            raw = indefinite_form_test_equivalence_vector(
                lattice._gram_rows(),
                [int(entry) for entry in left_vec],
                [int(entry) for entry in target],
            )
            if raw is None:
                continue
            return _normalize_vector_witness(lattice, raw, left_vec, target)
        return None
    left_rows = _object_basis_rows(left)
    right_rows = _object_basis_rows(right)
    raw = indefinite_form_test_equivalence_isotropic_k_plane(
        lattice._gram_rows(),
        left_rows,
        right_rows,
        choice="plane",
    )
    if raw is None:
        return None
    return _normalize_subspace_witness(
        lattice,
        raw,
        left_rows,
        right_rows,
    )


def _object_basis_rows(isotropic_object):
    return [[int(entry) for entry in row] for row in isotropic_object]


def _serialize_isotropic_object(orbit_kind, isotropic_object):
    if orbit_kind == "line":
        return [int(entry) for entry in isotropic_object]
    return _object_basis_rows(isotropic_object)


def _matrix_rows(M):
    return [[int(entry) for entry in row] for row in matrix(ZZ, M).rows()]


def _normalize_vector_witness(lattice, raw_matrix, source, target):
    gram = lattice.inner_product_matrix()
    raw = matrix(ZZ, raw_matrix)
    candidate = raw.inverse().transpose()
    assert candidate.transpose() * gram * candidate == gram
    assert candidate * source == target
    return candidate


def _normalize_subspace_witness(lattice, raw_matrix, source_rows, target_rows):
    gram = lattice.inner_product_matrix()
    raw = matrix(ZZ, raw_matrix)
    candidate = raw.inverse().transpose()
    assert candidate.transpose() * gram * candidate == gram
    source_basis = matrix(ZZ, source_rows)
    target_basis = matrix(ZZ, target_rows)
    source_image = source_basis * raw
    assert source_image.row_module() == target_basis.row_module()
    return candidate


def _structured_spec_payload(spec):
    return {
        "determinant_kernel": spec.determinant_kernel,
        "positive_spinor_kernel": spec.positive_spinor_kernel,
        "opaque": spec.opaque,
        "discriminant_preimages": [_discriminant_subgroup_payload(subgroup) for subgroup in spec.discriminant_preimages],
    }


def _structured_spec_label(spec):
    parts = []
    if spec.determinant_kernel:
        parts.append("det-kernel")
    if spec.positive_spinor_kernel:
        parts.append("spin-kernel")
    if spec.discriminant_preimages:
        parts.append("disc-preimage")
    if not parts:
        parts.append("ambient-group")
    return ",".join(parts)


def _discriminant_subgroup_payload(subgroup):
    if subgroup is None:
        return None
    generator_rows = sorted(
        (_matrix_rows(generator) for generator in subgroup.gens()),
        key=lambda rows: json.dumps(rows, separators=(",", ":")),
    )
    return {
        "invariants": [int(entry) for entry in subgroup.discriminant_group.invariants()],
        "generators": generator_rows,
    }


def _validate_orbit_representatives(lattice, orbit_kind, orbit_representatives):
    for representative in orbit_representatives:
        _validate_isotropic_object(lattice, orbit_kind, representative)


def _validate_isotropic_object(lattice, orbit_kind, isotropic_object):
    if orbit_kind == "line":
        primitive = lattice(_normalize_primitive_line(isotropic_object))
        assert primitive.is_isotropic()
        gcd_value = ZZ.zero()
        for entry in primitive:
            gcd_value = gcd_value.gcd(ZZ(entry))
        assert gcd_value == 1
        return
    basis = tuple(lattice(vector(ZZ, list(row))) for row in isotropic_object)
    assert basis
    for vector_i in basis:
        assert vector_i.is_isotropic()
    for left_index, left in enumerate(basis):
        for right in basis[left_index + 1 :]:
            assert left.inner_product(right).is_zero()
    rank = matrix(ZZ, _object_basis_rows(basis)).rank()
    assert rank == len(basis)


def _validate_stabilizer_generators(lattice, orbit_kind, isotropic_object, generators):
    normalized_object = _normalize_isotropic_object(lattice, orbit_kind, isotropic_object)
    gram = lattice.inner_product_matrix()
    if orbit_kind == "line":
        line_vector = vector(ZZ, list(normalized_object))
        line_span = lattice.ambient_module().span([line_vector])
    else:
        basis = [vector(ZZ, list(row)) for row in normalized_object]
        target_span = lattice.ambient_module().span(basis)
    for generator in generators:
        generator = matrix(ZZ, generator)
        assert generator.transpose() * gram * generator == gram
        if orbit_kind == "line":
            assert generator * line_vector in line_span
            continue
        for basis_vector in basis:
            assert generator * basis_vector in target_span


def _validate_equivalence_witness(lattice, orbit_kind, left, right, witness):
    _validate_isotropic_object(lattice, orbit_kind, left)
    _validate_isotropic_object(lattice, orbit_kind, right)
    if witness is None:
        return
    witness = matrix(ZZ, witness)
    gram = lattice.inner_product_matrix()
    assert witness.transpose() * gram * witness == gram
    right_object = _normalize_isotropic_object(lattice, orbit_kind, right)
    if orbit_kind == "line":
        left_image = _apply_ambient_isometry(lattice, orbit_kind, left, witness)
        assert left_image == right_object
        return
    image_rows = matrix(
        ZZ,
        _object_basis_rows(
            _apply_ambient_isometry(
                lattice,
                orbit_kind,
                left,
                witness,
            )
        ),
    )
    right_rows = matrix(ZZ, _object_basis_rows(right_object))
    assert image_rows.row_module() == right_rows.row_module()
