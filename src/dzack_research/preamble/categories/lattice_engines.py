r"""Private exact computational realizations for owned lattice constructions."""

import shutil
from functools import partial
from importlib import import_module
from importlib.util import find_spec
from pathlib import Path

from sage.libs.gap.libgap import libgap
from sage.matrix.constructor import matrix as engine_matrix
from sage.quadratic_forms.quadratic_form import QuadraticForm
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ

from dzack_research.preamble.categories.rings.ring_foundation import _owned_engine_element
from dzack_research.preamble.categories.sets.set_categories import NN
from dzack_research.preamble.engine_capabilities import engine_capabilities
from dzack_research.preamble.tensors.tensor import (
    Tensor,
    _engine_component_matrix,
    tensor,
)
from py_polyhedral.binaries import (
    binary_available,
    indefinite_form_automorphism_group,
    indefinite_form_get_orbit_representative,
    indefinite_form_isotropic_k_stuff,
    indefinite_form_stabilizer_isotropic_subspace,
    indefinite_form_stabilizer_vector,
    indefinite_form_test_equivalence,
    indefinite_form_test_equivalence_isotropic_k_plane,
    indefinite_form_test_equivalence_vector,
    lorentzian_perfect_domain_traversal,
)


def _rational_positive_vector(gram):
    r"""Return one exact rational positive vector for signature ``(1,n)``.

    Sage supplies the rational diagonalization privately.  The returned value
    is immediately re-entered into the preamble as a type-``(1,0)`` tensor;
    the transformation matrix itself is never public API.
    """
    if not isinstance(gram, Tensor) or gram.tensor_valence() != (NN**2)((0, 2)):
        raise TypeError("a positive vector is computed from a bilinear-form tensor")
    engine_gram = _engine_component_matrix(gram).change_ring(SageQQ)
    diagonal, change = QuadraticForm(
        SageQQ,
        2 * engine_gram,
    ).rational_diagonal_form(return_matrix=True)
    diagonal_matrix = diagonal.matrix()
    positive = [
        index
        for index in range(diagonal_matrix.nrows())
        if diagonal_matrix[index, index] > 0
    ]
    if len(positive) != 1:
        raise ValueError(
            "a two-component positive cone requires exactly one positive direction"
        )
    column = change.column(positive[0])
    rationals = gram.base_ring().fraction_field()
    return tensor.vector(
        rationals,
        tuple(_owned_engine_element(rationals, entry) for entry in column),
    )


def _integer_engine_matrix(value, *, transpose=False):
    if not isinstance(value, Tensor) or value.tensor_order() != 2:
        raise TypeError("the lattice engine seam requires a two-index tensor")
    engine = _engine_component_matrix(value).change_ring(SageZZ)
    return engine.transpose() if transpose else engine


_OSCAR_LATTICE_ADAPTER_SOURCE = r"""
module DzackResearchOscarLatticeAdapter
using Oscar

function _zz_matrix(entries)
    rows, columns = size(entries)
    return matrix(
        ZZ,
        rows,
        columns,
        [ZZ(entries[i, j]) for i in 1:rows for j in 1:columns],
    )
end

function rational_spinor_norm_sign(gram_entries, isometry_entries)
    gram = _zz_matrix(gram_entries)
    lattice = integer_lattice(; gram = change_base_ring(QQ, gram))
    isometry = _zz_matrix(isometry_entries)
    lattice_with_isometry = integer_lattice_with_isometry(
        lattice,
        change_base_ring(QQ, isometry);
        check = true,
    )
    # Ask explicitly for the un-negated bilinear form.  Current OSCAR
    # defaults to b=-1, whereas the owned convention applies the sign
    # correction by the determinant at the category boundary.
    return rational_spinor_norm(lattice_with_isometry; b = 1)
end

function centralizer_discriminant_image(gram_entries, isometry_entries)
    gram = _zz_matrix(gram_entries)
    lattice = integer_lattice(; gram = change_base_ring(QQ, gram))
    isometry = _zz_matrix(isometry_entries)
    lattice_with_isometry = integer_lattice_with_isometry(
        lattice,
        change_base_ring(QQ, isometry);
        check = true,
    )
    invariant_rank = nrows(basis_matrix(invariant_lattice(lattice_with_isometry)))
    coinvariant_rank = nrows(basis_matrix(coinvariant_lattice(lattice_with_isometry)))
    image, _ = image_centralizer_in_Oq(lattice_with_isometry)
    generators = [matrix(generator) for generator in gens(image)]
    return [generators, order(image), invariant_rank, coinvariant_rank]
end

function even_unimodular_primitive_embedding(gram_entries, positive, negative)
    gram = _zz_matrix(gram_entries)
    source = integer_lattice(; gram = change_base_ring(QQ, gram))
    target, source_in_target, _ = embed_in_unimodular(
        source,
        Int(positive),
        Int(negative),
    )
    embedding = solve(
        basis_matrix(target),
        basis_matrix(source_in_target);
        side = :left,
    )
    return [
        change_base_ring(ZZ, gram_matrix(target)),
        change_base_ring(ZZ, embedding),
    ]
end

function target_primitive_embedding(source_gram_entries, target_gram_entries)
    source_gram = _zz_matrix(source_gram_entries)
    target_gram = _zz_matrix(target_gram_entries)
    source = integer_lattice(; gram = change_base_ring(QQ, source_gram))
    target = integer_lattice(; gram = change_base_ring(QQ, target_gram))
    exists, representatives = primitive_embeddings(
        genus(target),
        source;
        classification = :sub,
    )
    if !exists
        return [1, 0]
    end
    target_specific = filter(
        record -> is_isometric_with_isometry(record[1], target; ambient_representation = false)[1],
        representatives,
    )
    if isempty(target_specific)
        return [1, 0]
    end
    target_prime, source_prime, _complement = first(target_specific)
    inclusion = solve(
        basis_matrix(target_prime),
        basis_matrix(source_prime);
        side = :left,
    )
    return [
        1,
        1,
        change_base_ring(ZZ, gram_matrix(target_prime)),
        change_base_ring(ZZ, gram_matrix(source_prime)),
        change_base_ring(ZZ, inclusion),
    ]
end

function target_primitive_embedding_classes(
    source_gram_entries,
    target_gram_entries,
    classification_name,
)
    source_gram = _zz_matrix(source_gram_entries)
    target_gram = _zz_matrix(target_gram_entries)
    source = integer_lattice(; gram = change_base_ring(QQ, source_gram))
    target = integer_lattice(; gram = change_base_ring(QQ, target_gram))
    classification = Symbol(classification_name)
    @req classification in [:sub, :emb] "primitive embedding classes are :sub or :emb"
    exists, representatives = primitive_embeddings(
        genus(target),
        source;
        classification = classification,
    )
    if !exists
        return [1, 0, []]
    end
    result = []
    for (target_prime, source_prime, _complement) in representatives
        is_target, _target_witness = is_isometric_with_isometry(
            target_prime,
            target;
            ambient_representation = false,
        )
        if !is_target
            continue
        end
        inclusion = solve(
            basis_matrix(target_prime),
            basis_matrix(source_prime);
            side = :left,
        )
        push!(
            result,
            [
                change_base_ring(ZZ, gram_matrix(target_prime)),
                change_base_ring(ZZ, gram_matrix(source_prime)),
                change_base_ring(ZZ, inclusion),
            ],
        )
    end
    if isempty(result)
        return [1, 0, []]
    end
    return [1, 1, result]
end

function leech_gram_rows()
    lattice = leech_lattice()
    gram = change_base_ring(ZZ, gram_matrix(lattice))
    rows, columns = size(gram)
    return [[Int(gram[i, j]) for j in 1:columns] for i in 1:rows]
end

function integral_isometry_witness(source_gram_entries, target_gram_entries)
    source_gram = _zz_matrix(source_gram_entries)
    target_gram = _zz_matrix(target_gram_entries)
    source = integer_lattice(; gram = change_base_ring(QQ, source_gram))
    target = integer_lattice(; gram = change_base_ring(QQ, target_gram))
    isometric, isometry = is_isometric_with_isometry(
        source,
        target;
        ambient_representation = false,
    )
    if !isometric
        return [0]
    end
    integral = change_base_ring(ZZ, isometry)
    if integral * target_gram * transpose(integral) != source_gram
        error("OSCAR returned an isometry with the wrong Gram identity")
    end
    return [1, integral]
end
end
"""


_OSCAR_PROVIDER = "oscar-via-sage-julia-bridge"
_OSCAR_PROVISIONING = (
    "clone github.com/dzackgarza/sage-julia-bridge and run `just setup` there: it "
    "installs the bridge into Sage's environment, instantiates the bridge's Julia "
    "project with its JSON and Oscar dependencies"
)


class _OscarLatticeAdapter:
    r"""One persistent OSCAR realization behind ``sage-julia-bridge``."""

    def available(self) -> bool:
        if find_spec("sage_julia_bridge") is None:
            return False
        juliaup = Path.home() / ".juliaup" / "bin" / "julia"
        return juliaup.exists() or shutil.which("julia") is not None

    def _bridge(self):
        from sage_julia_bridge import julia

        module_loaded = julia.sage(
            "isdefined(Main, :DzackResearchOscarLatticeAdapter)"
        )
        if not module_loaded:
            julia.eval(_OSCAR_LATTICE_ADAPTER_SOURCE)
        return julia

    def rational_spinor_norm_sign(self, gram, isometry):
        bridge = self._bridge()
        value = SageQQ(
            bridge.call(
                "DzackResearchOscarLatticeAdapter.rational_spinor_norm_sign",
                _integer_engine_matrix(gram),
                _integer_engine_matrix(isometry, transpose=True),
            )
        )
        if value == 0:
            raise ArithmeticError("the spinor norm of an isometry is a nonzero square class")
        return SageZZ.one() if value > 0 else -SageZZ.one()

    def centralizer_discriminant_image(self, gram, isometry):
        result = self._bridge().call(
            "DzackResearchOscarLatticeAdapter.centralizer_discriminant_image",
            _integer_engine_matrix(gram),
            _integer_engine_matrix(isometry, transpose=True),
        )
        if not isinstance(result, list) or len(result) != 4:
            raise RuntimeError("OSCAR returned malformed centralizer-image data")
        engine_generators, order, invariant_rank, coinvariant_rank = result
        generators = tuple(
            tensor.matrix(
                SageZZ,
                generator.nrows(),
                generator.ncols(),
                tuple(SageZZ(entry) for entry in generator.list()),
            )
            for generator in engine_generators
        )
        if any(
            generator.tensor_shape()[0] != generator.tensor_shape()[1]
            for generator in generators
        ):
            raise ArithmeticError("an OSCAR centralizer-image generator is not square")
        return (
            generators,
            SageZZ(order),
            SageZZ(invariant_rank),
            SageZZ(coinvariant_rank),
        )

    def even_unimodular_primitive_embedding(self, gram, positive, negative):
        result = self._bridge().call(
            "DzackResearchOscarLatticeAdapter.even_unimodular_primitive_embedding",
            _integer_engine_matrix(gram),
            int(positive),
            int(negative),
        )
        if not isinstance(result, list) or len(result) != 2:
            raise RuntimeError("OSCAR returned malformed primitive-embedding data")
        target_engine, embedding_engine = result
        ring = gram.base_ring()
        target_shape = (target_engine.nrows(), target_engine.ncols())
        target_gram = tensor(
            ring,
            (),
            target_shape,
            tuple(
                tuple(_owned_engine_element(ring, entry) for entry in row)
                for row in target_engine.rows()
            ),
        )

        # OSCAR emits source basis images as rows.  The live Mor matrix acts on
        # coordinate columns, so transpose those rows into target-by-source shape.
        embedding = ring.matrix_space(embedding_engine.ncols(), embedding_engine.nrows()).from_rows(
            tuple(
                tuple(
                    _owned_engine_element(ring, embedding_engine[source, target])
                    for source in range(embedding_engine.nrows())
                )
                for target in range(embedding_engine.ncols())
            )
        )
        if not target_gram.pullback(embedding).is_equal_tensor(gram):
            raise ArithmeticError(
                "OSCAR's primitive embedding does not pull back the target form"
            )
        if abs(target_gram.det()) != 1:
            raise ArithmeticError("OSCAR's primitive-embedding target is not unimodular")
        if any(target_gram[index, index] % 2 for index in range(target_shape[0])):
            raise ArithmeticError("OSCAR's primitive-embedding target is not even")
        return target_gram, embedding

    def target_primitive_embedding(self, source_gram, target_gram):
        result = self._bridge().call(
            "DzackResearchOscarLatticeAdapter.target_primitive_embedding",
            _integer_engine_matrix(source_gram),
            _integer_engine_matrix(target_gram),
        )
        if not isinstance(result, list) or not result:
            raise RuntimeError("OSCAR returned malformed target-embedding data")
        if int(result[0]) == 0:
            return None
        if len(result) < 2:
            raise RuntimeError("OSCAR omitted the target-embedding existence flag")
        if int(result[1]) == 0:
            return False
        if len(result) != 5:
            raise RuntimeError("OSCAR returned malformed target-embedding witness data")
        target_engine, source_engine, embedding_engine = result[2:]
        ring = source_gram.base_ring()

        def owned_gram(engine):
            return tensor(
                ring,
                (),
                (engine.nrows(), engine.ncols()),
                tuple(
                    tuple(_owned_engine_element(ring, entry) for entry in row)
                    for row in engine.rows()
                ),
            )

        target_prime_gram = owned_gram(target_engine)
        source_prime_gram = owned_gram(source_engine)
        embedding = ring.matrix_space(embedding_engine.ncols(), embedding_engine.nrows()).from_rows(
            tuple(
                tuple(
                    _owned_engine_element(ring, embedding_engine[source, target])
                    for source in range(embedding_engine.nrows())
                )
                for target in range(embedding_engine.ncols())
            )
        )
        if not target_prime_gram.pullback(embedding).is_equal_tensor(source_prime_gram):
            raise ArithmeticError(
                "OSCAR's target primitive embedding does not preserve the source-prime form"
            )
        return target_prime_gram, source_prime_gram, embedding

    def target_primitive_embedding_classes(
        self,
        source_gram,
        target_gram,
        classification,
    ):
        result = self._bridge().call(
            "DzackResearchOscarLatticeAdapter.target_primitive_embedding_classes",
            _integer_engine_matrix(source_gram),
            _integer_engine_matrix(target_gram),
            str(classification),
        )
        if not isinstance(result, list) or not result:
            raise RuntimeError("OSCAR returned malformed primitive-embedding class data")
        if int(result[0]) == 0:
            return None
        if len(result) != 3:
            raise RuntimeError("OSCAR returned malformed primitive-embedding class header")
        if int(result[1]) == 0:
            return ()
        representatives = []
        for record in result[2]:
            if not isinstance(record, list) or len(record) != 3:
                raise RuntimeError("OSCAR returned a malformed primitive-embedding class")
            target_engine, source_engine, embedding_engine = record
            ring = source_gram.base_ring()

            def owned_gram(engine):
                return tensor(
                    ring,
                    (),
                    (engine.nrows(), engine.ncols()),
                    tuple(
                        tuple(_owned_engine_element(ring, entry) for entry in row)
                        for row in engine.rows()
                    ),
                )

            target_prime_gram = owned_gram(target_engine)
            source_prime_gram = owned_gram(source_engine)
            embedding = ring.matrix_space(embedding_engine.ncols(), embedding_engine.nrows()).from_rows(
                tuple(
                    tuple(
                        _owned_engine_element(ring, embedding_engine[source, target])
                        for source in range(embedding_engine.nrows())
                    )
                    for target in range(embedding_engine.ncols())
                )
            )
            if not target_prime_gram.pullback(embedding).is_equal_tensor(source_prime_gram):
                raise ArithmeticError(
                    "an OSCAR primitive-embedding class does not preserve the source-prime form"
                )
            representatives.append((target_prime_gram, source_prime_gram, embedding))
        return tuple(representatives)

    def leech_gram_rows(self):
        rows = self._bridge().call(
            "DzackResearchOscarLatticeAdapter.leech_gram_rows"
        )
        if not isinstance(rows, list) or len(rows) != 24:
            raise RuntimeError("OSCAR returned malformed Leech Gram data")
        matrix_rows = tuple(tuple(SageZZ(entry) for entry in row) for row in rows)
        if any(len(row) != 24 for row in matrix_rows):
            raise RuntimeError("OSCAR returned a non-square Leech Gram matrix")
        gram = engine_matrix(SageZZ, matrix_rows)
        if not gram.is_symmetric():
            raise ArithmeticError("OSCAR returned a nonsymmetric Leech Gram matrix")
        if abs(gram.det()) != 1:
            raise ArithmeticError("OSCAR returned a non-unimodular Leech Gram matrix")
        if any(gram[index, index] % 2 for index in range(24)):
            raise ArithmeticError("OSCAR returned an odd Leech Gram matrix")
        return matrix_rows

    def integral_isometry_witness(self, source_gram, target_gram):
        result = self._bridge().call(
            "DzackResearchOscarLatticeAdapter.integral_isometry_witness",
            _integer_engine_matrix(source_gram),
            _integer_engine_matrix(target_gram),
        )
        if not isinstance(result, list) or not result:
            raise RuntimeError("OSCAR returned malformed lattice-isometry data")
        if int(result[0]) == 0:
            return None
        if len(result) != 2:
            raise RuntimeError("OSCAR returned malformed lattice-isometry witness data")
        witness = result[1]
        if witness.nrows() != witness.ncols():
            raise ArithmeticError("an OSCAR lattice isometry matrix is not square")
        source_engine = _integer_engine_matrix(source_gram)
        target_engine = _integer_engine_matrix(target_gram)
        if witness * target_engine * witness.transpose() != source_engine:
            raise ArithmeticError("an OSCAR lattice isometry does not preserve the Gram form")
        return tuple(
            tuple(SageZZ(entry) for entry in row)
            for row in witness.rows()
        )


_oscar_lattices = _OscarLatticeAdapter()

engine_capabilities.register(
    "lattice.rational_spinor_norm_sign",
    _OSCAR_PROVIDER,
    _oscar_lattices.rational_spinor_norm_sign,
    available=_oscar_lattices.available,
    provisioning=_OSCAR_PROVISIONING,
)
engine_capabilities.register(
    "lattice.centralizer_discriminant_image",
    _OSCAR_PROVIDER,
    _oscar_lattices.centralizer_discriminant_image,
    available=_oscar_lattices.available,
    provisioning=_OSCAR_PROVISIONING,
)
engine_capabilities.register(
    "lattice.even_unimodular_primitive_embedding",
    _OSCAR_PROVIDER,
    _oscar_lattices.even_unimodular_primitive_embedding,
    available=_oscar_lattices.available,
    provisioning=_OSCAR_PROVISIONING,
)
engine_capabilities.register(
    "lattice.target_primitive_embedding",
    _OSCAR_PROVIDER,
    _oscar_lattices.target_primitive_embedding,
    available=_oscar_lattices.available,
    provisioning=_OSCAR_PROVISIONING,
)
engine_capabilities.register(
    "lattice.target_primitive_embedding_classes",
    _OSCAR_PROVIDER,
    _oscar_lattices.target_primitive_embedding_classes,
    available=_oscar_lattices.available,
    provisioning=_OSCAR_PROVISIONING,
)
engine_capabilities.register(
    "lattice.leech_gram_rows",
    _OSCAR_PROVIDER,
    _oscar_lattices.leech_gram_rows,
    available=_oscar_lattices.available,
    provisioning=_OSCAR_PROVISIONING,
)
engine_capabilities.register(
    "lattice.oscar_isometry_witness",
    _OSCAR_PROVIDER,
    _oscar_lattices.integral_isometry_witness,
    available=_oscar_lattices.available,
    provisioning=_OSCAR_PROVISIONING,
)


def _rational_spinor_norm_sign(gram, isometry):
    return engine_capabilities.compute(
        "lattice.rational_spinor_norm_sign",
        gram,
        isometry,
    )


def _centralizer_discriminant_image(gram, isometry):
    return engine_capabilities.compute(
        "lattice.centralizer_discriminant_image",
        gram,
        isometry,
    )


def _even_unimodular_primitive_embedding(gram, positive, negative):
    return engine_capabilities.compute(
        "lattice.even_unimodular_primitive_embedding",
        gram,
        positive,
        negative,
    )


def _target_primitive_embedding(source_gram, target_gram):
    return engine_capabilities.compute(
        "lattice.target_primitive_embedding",
        source_gram,
        target_gram,
    )


def _target_primitive_embedding_classes(source_gram, target_gram, classification):
    return engine_capabilities.compute(
        "lattice.target_primitive_embedding_classes",
        source_gram,
        target_gram,
        classification,
    )


def _leech_gram_rows():
    r"""Return Hecke's exact positive-definite Leech Gram rows privately."""
    return engine_capabilities.compute("lattice.leech_gram_rows")


def _integral_isometry_witness(source_gram, target_gram):
    return engine_capabilities.compute(
        "lattice.oscar_isometry_witness",
        source_gram,
        target_gram,
    )


# ---------------------------------------------------------------------------
# The indefinite-lattice algorithms, in the order the layer offers them.
#
# ``sage-indefinite-port`` is where these algorithms are going: it ports the
# ``INDEF_FORM_*`` kernels onto the owned formed-lattice category, so a ported
# operation computes in the session instead of through a file protocol.  It is
# the first provider of every capability below.
#
# ``polyhedral_common``, reached through the ``py_polyhedral`` wrapper, is the
# realization being replaced, and it is what computes today.  The wrapper owns
# that boundary: it writes the matrix files the programs read and resolves each
# program from ``PATH`` at call time, so nothing here names a build directory
# or an absolute executable.
#
# The second entry is not a fallback.  It is the realization the layer reaches
# while the port of that operation is outstanding, and when neither provider is
# available the refusal carries both absences with both remedies.
#
# The port depends on this package, so it is imported lazily, inside the
# availability predicate, the same way the OSCAR adapter reaches the Julia
# bridge.  A capability the port does not expose yet names its own module and
# attribute as ``None``; filling those in is what turns the port on for that
# operation.
# ---------------------------------------------------------------------------

_PORT_PROVIDER = "sage-indefinite-port"
_PORT_PACKAGE = "sage_indefinite_port"
_PORT_INSTALL = (
    "sage -pip install --no-deps -e /home/dzack/gitclones/sage-indefinite-port"
)


def _port_provisioning(kernel, ported):
    r"""State how ``kernel`` becomes available from the port."""
    if ported:
        return f"install the port into Sage's environment with `{_PORT_INSTALL}`"
    return (
        f"install the port into Sage's environment with `{_PORT_INSTALL}`; the "
        f"operation itself arrives with sage-indefinite-port's port of {kernel}"
    )


def _port_available(module_name, attribute) -> bool:
    r"""Return whether the port exposes this operation in this session."""
    if module_name is None or find_spec(_PORT_PACKAGE) is None:
        return False
    return attribute in vars(import_module(module_name))


def _port_operation(module_name, attribute, /, *args, **kwargs):
    return vars(import_module(module_name))[attribute](*args, **kwargs)


# Capability, the kernel the port carries it under, module, attribute.  The
# kernel names are the ones declared in `src_indefinite/CombinedAlgorithms.h`,
# except INDEF_FORM_Invariant, which is in `src_indefinite/IndefiniteFormFundamental.h`.
# They are not the driver names: the driver INDEF_FORM_TestEquivalenceVector
# calls the kernel INDEF_FORM_EquivalenceVector, and INDEF_FORM_StabilizerIsotropicPlane
# calls INDEF_FORM_Stabilizer_IsotropicKplane.
_PORT_REALIZATIONS = (
    (
        "lattice.indefinite_isometry_prefilter",
        "INDEF_FORM_Invariant",
        "sage_indefinite_port.invariants",
        "lattice_prefilter",
    ),
    (
        "lattice.indefinite_automorphism_group",
        "INDEF_FORM_AutomorphismGroup",
        None,
        None,
    ),
    ("lattice.indefinite_isometry_witness", "INDEF_FORM_TestEquivalence", None, None),
    (
        "lattice.indefinite_vector_isometry_witness",
        "INDEF_FORM_EquivalenceVector",
        None,
        None,
    ),
    (
        "lattice.indefinite_orbit_representative",
        "INDEF_FORM_GetOrbitRepresentative",
        None,
        None,
    ),
    (
        "lattice.indefinite_isotropic_subspace_orbits",
        "INDEF_FORM_GetOrbit_IsotropicKplane",
        None,
        None,
    ),
    (
        "lattice.indefinite_isotropic_subspace_stabilizer",
        "INDEF_FORM_Stabilizer_IsotropicKplane",
        None,
        None,
    ),
    ("lattice.indefinite_vector_stabilizer", "INDEF_FORM_StabilizerVector", None, None),
    (
        "lattice.indefinite_isotropic_subspace_isometry_witness",
        "INDEF_FORM_Equivalence_IsotropicKplane",
        None,
        None,
    ),
    (
        "lattice.rational_integral_structure",
        "MatrixIntegral_* / GroupAction.g",
        "sage_indefinite_port.groups.integral_structures",
        "integral_structure_action_for_group",
    ),
)

for _capability, _kernel, _module, _attribute in _PORT_REALIZATIONS:
    engine_capabilities.register(
        _capability,
        _PORT_PROVIDER,
        partial(_port_operation, _module, _attribute),
        available=partial(_port_available, _module, _attribute),
        provisioning=_port_provisioning(_kernel, _module is not None),
    )


_POLYHEDRAL_PROVIDER = "polyhedral-common-via-py-polyhedral"

_POLYHEDRAL_BUILD = (
    "clone github.com/MathieuDutSik/polyhedral_common, build the indefinite-form "
    "programs with `make -C src_indefinite`, and link them into a directory on PATH"
)

_POLYHEDRAL_LORENTZIAN_BUILD = (
    "clone github.com/MathieuDutSik/polyhedral_common, build "
    "LORENTZ_MPI_PerfectLorentzian from src_lorentzian, and expose the binary on PATH"
)


def _lorentzian_perfect_domain_records(gram, option="total"):
    r"""Cross polyhedral_common's GAP traversal records to plain exact data."""
    output = lorentzian_perfect_domain_traversal(gram, option)
    expression = output.strip()
    if expression.startswith("return "):
        expression = expression[len("return ") :]
    if expression.endswith(";"):
        expression = expression[:-1]
    records = libgap.eval(expression)
    result = []
    for record in records:
        obj = record["x"]
        ext = obj["EXT"].sage()
        group = obj["GRP"]
        degree = len(ext)
        permutations = []
        for generator in group.GeneratorsOfGroup():
            permutations.append(
                [
                    int(libgap.OnPoints(point, generator).sage()) - 1
                    for point in range(1, degree + 1)
                ]
            )
        adjacencies = []
        for adjacency in record["ListAdj"]:
            data = adjacency["x"]
            selected_face_positions = {
                int(position) for position in data["eInc"].sage()
            }
            adjacencies.append(
                {
                    "x": {
                        "eInc": [
                            int(position in selected_face_positions)
                            for position in range(1, degree + 1)
                        ],
                        "eBigMat": data["eBigMat"].sage(),
                    },
                    "iOrb": int(adjacency["iOrb"].sage()),
                }
            )
        result.append(
            {
                "x": {"EXT": ext, "GRP": permutations},
                "ListAdj": adjacencies,
            }
        )
    return tuple(result)


def _polyhedral_no_program(kernel):
    r"""State that this operation has no program, and where it comes from instead.

    ``src_indefinite/Makefile`` lists the drivers polyhedral_common compiles and
    these are not among them, so no build or install produces them.  The kernel
    exists in ``src_indefinite/CombinedAlgorithms.h``, and the operation reaches
    the session through the port of that kernel.
    """
    return (
        "polyhedral_common builds no program of this name, so the operation "
        f"arrives with sage-indefinite-port's port of {kernel}"
    )


_POLYHEDRAL_REALIZATIONS = (
    (
        "lattice.indefinite_automorphism_group",
        "INDEF_FORM_AutomorphismGroup",
        indefinite_form_automorphism_group,
        _POLYHEDRAL_BUILD,
    ),
    (
        "lattice.indefinite_isometry_witness",
        "INDEF_FORM_TestEquivalence",
        indefinite_form_test_equivalence,
        _POLYHEDRAL_BUILD,
    ),
    (
        "lattice.indefinite_vector_isometry_witness",
        "INDEF_FORM_TestEquivalenceVector",
        indefinite_form_test_equivalence_vector,
        _POLYHEDRAL_BUILD,
    ),
    (
        "lattice.indefinite_orbit_representative",
        "INDEF_FORM_GetOrbitRepresentative",
        indefinite_form_get_orbit_representative,
        _POLYHEDRAL_BUILD,
    ),
    (
        "lattice.indefinite_isotropic_subspace_orbits",
        "INDEF_FORM_GetOrbit_IsotropicKplane",
        indefinite_form_isotropic_k_stuff,
        _POLYHEDRAL_BUILD,
    ),
    (
        "lattice.indefinite_isotropic_subspace_stabilizer",
        "INDEF_FORM_StabilizerIsotropicPlane",
        indefinite_form_stabilizer_isotropic_subspace,
        _POLYHEDRAL_BUILD,
    ),
    (
        "lattice.indefinite_vector_stabilizer",
        "INDEF_FORM_StabilizerVector",
        indefinite_form_stabilizer_vector,
        _polyhedral_no_program("INDEF_FORM_StabilizerVector"),
    ),
    (
        "lattice.indefinite_isotropic_subspace_isometry_witness",
        "INDEF_FORM_TestEquivalenceIsotropicKplane",
        indefinite_form_test_equivalence_isotropic_k_plane,
        _polyhedral_no_program("INDEF_FORM_Equivalence_IsotropicKplane"),
    ),
    (
        "lattice.lorentzian_perfect_domain_traversal",
        "LORENTZ_MPI_PerfectLorentzian",
        _lorentzian_perfect_domain_records,
        _POLYHEDRAL_LORENTZIAN_BUILD,
    ),
)

for _capability, _binary, _operation, _provisioning in _POLYHEDRAL_REALIZATIONS:
    engine_capabilities.register(
        _capability,
        _POLYHEDRAL_PROVIDER,
        _operation,
        available=partial(binary_available, _binary),
        provisioning=_provisioning,
    )


__all__: list[str] = []
