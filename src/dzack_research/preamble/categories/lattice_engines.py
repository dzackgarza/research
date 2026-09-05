r"""Private exact computational realizations for owned lattice constructions."""

from importlib.util import find_spec
from pathlib import Path
import shutil

from sage.quadratic_forms.quadratic_form import QuadraticForm
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ

from dzack_research.preamble.engine_capabilities import (
    EngineAbsence,
    EngineCapabilityUnavailable,
    engine_capabilities,
)
from dzack_research.preamble.tensors.tensor import (
    Tensor,
    tensor,
)
from dzack_research.preamble.tensors.tensor import _engine_component_matrix
from dzack_research.preamble.categories.sets.set_categories import NN
from dzack_research.preamble.categories.modules.framed.framed_free_modules import MatrixSpace


def rational_positive_vector(gram):
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
        tuple(rationals._from_engine_element(entry) for entry in column),
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
    return (generators, order(image), invariant_rank, coinvariant_rank)
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
    return (
        change_base_ring(ZZ, gram_matrix(target)),
        change_base_ring(ZZ, embedding),
    )
end
end
[
    DzackResearchOscarLatticeAdapter.rational_spinor_norm_sign,
    DzackResearchOscarLatticeAdapter.centralizer_discriminant_image,
    DzackResearchOscarLatticeAdapter.even_unimodular_primitive_embedding,
]
"""


_OSCAR_PROVIDER = "oscar-via-sage-julia-bridge"
_OSCAR_PROVISIONING = (
    "clone github.com/dzackgarza/sage-julia-bridge and run `just setup` there: it "
    "installs the bridge into Sage's environment, instantiates the bridge's Julia "
    "project with its JSON dependency, and loads Oscar from the Julia depot"
)


class _OscarLatticeAdapter:
    r"""One retained-callable OSCAR realization behind ``sage-julia-bridge``."""

    def __init__(self) -> None:
        self._functions = None

    def available(self) -> bool:
        if find_spec("sage_julia_bridge") is None:
            return False
        juliaup = Path.home() / ".juliaup" / "bin" / "julia"
        return juliaup.exists() or shutil.which("julia") is not None

    def _load_functions(self):
        if self._functions is not None:
            try:
                for function in self._functions:
                    function.identity_key()
                return self._functions
            except Exception as error:
                # Only a stale/released bridge handle should invalidate this
                # cache.  Import lazily so absence of Julia never prevents
                # construction of an owned lattice.
                from sage_julia_bridge import (
                    JuliaReleasedObjectError,
                    JuliaStaleObjectError,
                )

                if not isinstance(error, (JuliaReleasedObjectError, JuliaStaleObjectError)):
                    raise
                self._functions = None

        try:
            from sage_julia_bridge import JuliaError, JuliaHandle, julia

            functions = julia.sage(_OSCAR_LATTICE_ADAPTER_SOURCE)
        except Exception as error:
            try:
                from sage_julia_bridge import JuliaError
            except Exception:
                JuliaError = ()
            if JuliaError and isinstance(error, JuliaError):
                raise EngineCapabilityUnavailable(
                    "lattice.oscar-adapter",
                    (EngineAbsence(_OSCAR_PROVIDER, _OSCAR_PROVISIONING),),
                ) from error
            raise
        if (
            not isinstance(functions, list)
            or len(functions) != 3
            or any(not isinstance(function, JuliaHandle) for function in functions)
        ):
            raise RuntimeError("sage-julia-bridge did not retain the OSCAR lattice callables")
        self._functions = tuple(functions)
        return self._functions

    def rational_spinor_norm_sign(self, gram, isometry):
        function = self._load_functions()[0]
        value = SageQQ(
            function(
                _integer_engine_matrix(gram),
                _integer_engine_matrix(isometry, transpose=True),
            )
        )
        if value == 0:
            raise ArithmeticError("the spinor norm of an isometry is a nonzero square class")
        return SageZZ.one() if value > 0 else -SageZZ.one()

    def centralizer_discriminant_image(self, gram, isometry):
        function = self._load_functions()[1]
        result = function(
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
        function = self._load_functions()[2]
        result = function(
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
                tuple(ring._from_engine_element(entry) for entry in row)
                for row in target_engine.rows()
            ),
        )

        # OSCAR emits source basis images as rows.  The live Hom matrix acts on
        # coordinate columns, so transpose those rows into target-by-source shape.
        embedding = MatrixSpace(
            ring,
            embedding_engine.ncols(),
            embedding_engine.nrows(),
        ).from_rows(
            tuple(
                tuple(
                    ring._from_engine_element(embedding_engine[source, target])
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


def rational_spinor_norm_sign(gram, isometry):
    return engine_capabilities.compute(
        "lattice.rational_spinor_norm_sign",
        gram,
        isometry,
    )


def centralizer_discriminant_image(gram, isometry):
    return engine_capabilities.compute(
        "lattice.centralizer_discriminant_image",
        gram,
        isometry,
    )


def even_unimodular_primitive_embedding(gram, positive, negative):
    return engine_capabilities.compute(
        "lattice.even_unimodular_primitive_embedding",
        gram,
        positive,
        negative,
    )


__all__ = [
    "centralizer_discriminant_image",
    "even_unimodular_primitive_embedding",
    "rational_positive_vector",
    "rational_spinor_norm_sign",
]
