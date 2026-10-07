r"""Private exact computational realizations for owned lattice constructions."""

from sage.matrix.constructor import matrix as engine_matrix
from sage.quadratic_forms.quadratic_form import QuadraticForm
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ

from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_ring,
    _owned_engine_element,
)
from dzack_research.preamble.categories.sets.set_categories import NN
from dzack_research.preamble.tensors.tensor import (
    Tensor,
    _engine_component_matrix,
    tensor,
)
from dzack_research.preamble.validation import validator


@validator
def validate_isometric_embedding(embedding_datum):
    r"""Check that an engine's embedding ``A`` pulls the target Gram tensor ``G`` back to the source's: ``G(A-, A-) = G'``.

    ``embedding_datum`` is ``(target_gram, source_gram, embedding)`` as an
    engine returned it.  The engine's answer is untrusted; this law runs only
    when asked or under :data:`strict_checking`.
    """
    target_gram, source_gram, embedding = embedding_datum
    pulled_back = target_gram.pullback(embedding)
    if not pulled_back.is_equal_tensor(source_gram):
        raise ValueError(f"the embedding {embedding} into the form {target_gram} is not isometric: it pulls the target back to {pulled_back}, not {source_gram}")


@validator
def validate_even_unimodular_gram(gram):
    r"""Check that the Gram tensor ``gram`` is unimodular (``det = +-1``) and even (every ``G(e_i, e_i)`` is even)."""
    engine_gram = _engine_component_matrix(gram)
    if abs(engine_gram.determinant()) != 1:
        raise ValueError(f"the form {gram} is not unimodular: its determinant is {engine_gram.determinant()}")
    if any(entry % 2 for entry in engine_gram.diagonal()):
        raise ValueError(f"the form {gram} is not even: some diagonal entry is odd")


def _rational_positive_vector(gram):
    r"""Return one exact rational positive vector for signature ``(1,n)``.

    Sage supplies the rational diagonalization privately.  The returned value
    is immediately re-entered into the preamble as a type-``(1,0)`` tensor;
    the transformation matrix itself is never public API.
    """
    if not isinstance(gram, Tensor) or gram.tensor_valence() != (NN**2)((0, 2)):
        raise TypeError(f"cannot find a vector of positive square for {gram}: it must be the Gram tensor of a bilinear form, a tensor of type (0, 2)")
    engine_gram = _engine_component_matrix(gram).change_ring(SageQQ)
    diagonal, change = QuadraticForm(
        SageQQ,
        2 * engine_gram,
    ).rational_diagonal_form(return_matrix=True)
    diagonal_matrix = diagonal.matrix()
    positive = [index for index in range(diagonal_matrix.nrows()) if diagonal_matrix[index, index] > 0]
    if len(positive) != 1:
        raise ValueError(
            f"the form with Gram tensor {gram} has {len(positive)} positive directions, but its positive cone has two components only for signature (1, n), with exactly one"
        )
    column = change.column(positive[0])
    rationals = gram.base_ring().fraction_field()
    return tensor.vector(
        rationals,
        tuple(_owned_engine_element(rationals, entry) for entry in column),
    )


def _integer_engine_matrix(value, *, transpose=False):
    if not isinstance(value, Tensor) or value.tensor_order() != 2:
        raise TypeError(f"{value} cannot be passed to OSCAR as an integer matrix: it must be a tensor with two indices")
    engine = _engine_component_matrix(value).change_ring(SageZZ)
    return engine.transpose() if transpose else engine


def _rational_engine_matrix(value, *, transpose=False):
    if not isinstance(value, Tensor) or value.tensor_order() != 2:
        raise TypeError(f"{value} cannot be passed to OSCAR as a rational matrix: it must be a tensor with two indices")
    engine = _engine_component_matrix(value).change_ring(SageQQ)
    return engine.transpose() if transpose else engine


def _number_field_descriptor(field):
    r"""Return the selected absolute number field as rational power-basis data."""
    from sage.categories.number_fields import NumberFields as SageNumberFields

    engine = _engine_ring(field)
    assert engine in SageNumberFields() and engine is not SageQQ, f"the OSCAR number-field lattice adapter needs a nontrivial absolute number field, but got {field}"
    assert engine.is_absolute(), (
        f"the OSCAR number-field lattice adapter needs an absolute primitive-element presentation, but {field} is represented as a relative number field"
    )
    polynomial = engine.defining_polynomial()
    return tuple(SageQQ(coefficient) for coefficient in polynomial.list())


def _number_field_element_coefficients(field, value):
    r"""Return ``value`` in the selected power basis of the Sage realization of ``field``."""
    engine = _engine_ring(field)
    element = engine(value)
    coefficients = list(element.list())
    coefficients.extend([SageQQ.zero()] * (engine.degree() - len(coefficients)))
    return tuple(SageQQ(coefficient) for coefficient in coefficients)


def _number_field_engine_matrix(value, field, *, transpose=False):
    r"""Lower a represented matrix to nested rational power-basis coefficients."""
    if not isinstance(value, Tensor) or value.tensor_order() != 2:
        raise TypeError(f"{value} cannot be passed to OSCAR as a number-field matrix: it must be a tensor with two indices")
    engine = _engine_component_matrix(value)
    if transpose:
        engine = engine.transpose()
    return [[list(_number_field_element_coefficients(field, engine[row, column])) for column in range(engine.ncols())] for row in range(engine.nrows())]


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

function _qq_matrix(entries)
    rows, columns = size(entries)
    return matrix(
        QQ,
        rows,
        columns,
        [QQ(entries[i, j]) for i in 1:rows for j in 1:columns],
    )
end

function _number_field(defining_coefficients)
    QQx, x = polynomial_ring(QQ, "a")
    polynomial = sum(
        QQ(defining_coefficients[i]) * x^(i - 1)
        for i in eachindex(defining_coefficients)
    )
    return number_field(polynomial, "a")
end

function _number_field_element(K, a, coefficients)
    return sum(
        K(QQ(coefficients[i])) * a^(i - 1)
        for i in eachindex(coefficients)
    )
end

function _number_field_matrix(K, a, entries)
    rows = length(entries)
    columns = rows == 0 ? 0 : length(entries[1])
    return matrix(
        K,
        rows,
        columns,
        [
            _number_field_element(K, a, entries[i][j])
            for i in 1:rows for j in 1:columns
        ],
    )
end

function rational_spinor_norm_class(gram_entries, isometry_entries)
    space = quadratic_space(QQ, _qq_matrix(gram_entries))
    space_with_isometry = quadratic_space_with_isometry(
        space,
        _qq_matrix(isometry_entries);
        check = true,
    )
    # Ask explicitly for the untwisted form b: OSCAR decomposes the isometry
    # into reflections s_{v_1} ... s_{v_m} over a diagonalized Gram matrix and
    # returns b(v_1, v_1) ... b(v_m, v_m), a representative of the whole square
    # class (Oscar.spin).  Its default is b = -1; the owned spinor norm applies
    # its own multiplier at the owning morphism.
    return rational_spinor_norm(space_with_isometry; b = 1)
end

function rational_witt_index(gram_entries)
    gram = _qq_matrix(gram_entries)
    _anisotropic, hyperbolic, radical = Oscar.Hecke._quadratic_form_decomposition(gram)
    nrows(radical) == 0 || error("Witt index requires a nondegenerate quadratic space")
    iseven(nrows(hyperbolic)) || error("Hecke returned an odd-dimensional hyperbolic summand")
    return div(nrows(hyperbolic), 2)
end

function number_field_spinor_norm_class(defining_coefficients, gram_entries, isometry_entries)
    K, a = _number_field(defining_coefficients)
    gram = _number_field_matrix(K, a, gram_entries)
    isometry = _number_field_matrix(K, a, isometry_entries)
    D, U = Oscar.Hecke._gram_schmidt(gram, K)
    transformed = U * isometry * inv(U)
    value = Oscar.spin(D, transformed)
    return [QQ(coeff(value, i)) for i in 0:(degree(K) - 1)]
end

function number_field_witt_index(defining_coefficients, gram_entries)
    K, a = _number_field(defining_coefficients)
    gram = _number_field_matrix(K, a, gram_entries)
    _anisotropic, hyperbolic, radical = Oscar.Hecke._quadratic_form_decomposition(gram)
    nrows(radical) == 0 || error("Witt index requires a nondegenerate quadratic space")
    iseven(nrows(hyperbolic)) || error("Hecke returned an odd-dimensional hyperbolic summand")
    return div(nrows(hyperbolic), 2)
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
end
"""


class _OscarLatticeAdapter:
    r"""One persistent OSCAR realization behind ``sage-julia-bridge``."""

    def _bridge(self):
        from sage_julia_bridge import julia

        module_loaded = julia.sage("isdefined(Main, :DzackResearchOscarLatticeAdapter)")
        if not module_loaded:
            julia.eval(_OSCAR_LATTICE_ADAPTER_SOURCE)
        return julia

    def rational_spinor_norm_class(self, gram, isometry):
        r"""Return ``b(v_1,v_1)...b(v_m,v_m)`` for ``isometry = s_{v_1}...s_{v_m}`` of ``(QQ^n, gram)``."""
        bridge = self._bridge()
        value = SageQQ(
            bridge.call(
                "DzackResearchOscarLatticeAdapter.rational_spinor_norm_class",
                _rational_engine_matrix(gram),
                _rational_engine_matrix(isometry, transpose=True),
            )
        )
        if value == 0:
            raise ArithmeticError(f"OSCAR computed spinor norm 0 for the isometry {isometry} of the form {gram}, but a spinor norm is a nonzero square class")
        return value

    def rational_witt_index(self, gram):
        r"""Return the Witt index of the quadratic space ``(QQ^n, gram)``."""
        engine_gram = _rational_engine_matrix(gram)
        index = SageZZ(
            self._bridge().call(
                "DzackResearchOscarLatticeAdapter.rational_witt_index",
                engine_gram,
            )
        )
        if not 0 <= 2 * index <= engine_gram.nrows():
            raise ArithmeticError(f"OSCAR computed Witt index {index} for the form {gram}, but a Witt index r satisfies 0 <= 2r <= the dimension")
        return index

    def number_field_spinor_norm_class(self, field, gram, isometry):
        r"""Return an untwisted spinor-norm representative over the absolute number field ``field``."""
        coefficients = self._bridge().call(
            "DzackResearchOscarLatticeAdapter.number_field_spinor_norm_class",
            list(_number_field_descriptor(field)),
            _number_field_engine_matrix(gram, field),
            _number_field_engine_matrix(isometry, field, transpose=True),
        )
        engine = _engine_ring(field)
        generator = engine.gen()
        value = engine.zero()
        for exponent, coefficient in enumerate(coefficients):
            value += SageQQ(coefficient) * generator**exponent
        if value == 0:
            raise ArithmeticError(f"OSCAR computed spinor norm 0 for the isometry {isometry} of the form {gram} over {field}, but a spinor norm is a nonzero square class")
        return _owned_engine_element(field, value)

    def number_field_witt_index(self, field, gram):
        r"""Return the Witt index of a nondegenerate quadratic space over ``field``."""
        engine_gram = _engine_component_matrix(gram)
        index = SageZZ(
            self._bridge().call(
                "DzackResearchOscarLatticeAdapter.number_field_witt_index",
                list(_number_field_descriptor(field)),
                _number_field_engine_matrix(gram, field),
            )
        )
        if not 0 <= 2 * index <= engine_gram.nrows():
            raise ArithmeticError(f"Hecke computed Witt index {index} for the form {gram} over {field}, but a Witt index r satisfies 0 <= 2r <= the dimension")
        return index

    def centralizer_discriminant_image(self, gram, isometry):
        result = self._bridge().call(
            "DzackResearchOscarLatticeAdapter.centralizer_discriminant_image",
            _integer_engine_matrix(gram),
            _integer_engine_matrix(isometry, transpose=True),
        )
        if not isinstance(result, list) or len(result) != 4:
            raise RuntimeError(f"the image of the centralizer of {isometry} in O(A_L) for the form {gram} came back from OSCAR as {result!r}, not a list of four entries")
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
        if any(generator.tensor_shape()[0] != generator.tensor_shape()[1] for generator in generators):
            raise ArithmeticError(f"OSCAR returned generators {generators} for the image of the centralizer of {isometry} in O(A_L), and some are not square matrices")
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
            raise RuntimeError(
                f"the primitive embedding of the form {gram} into an even unimodular lattice of "
                f"signature ({positive}, {negative}) came back from OSCAR as {result!r}, not a "
                f"list of two entries"
            )
        target_engine, embedding_engine = result
        ring = gram.base_ring()
        target_shape = (target_engine.nrows(), target_engine.ncols())
        target_gram = tensor(
            ring,
            (),
            target_shape,
            tuple(tuple(_owned_engine_element(ring, entry) for entry in row) for row in target_engine.rows()),
        )

        # OSCAR emits source basis images as rows.  The live Mor matrix acts on
        # coordinate columns, so transpose those rows into target-by-source shape.
        embedding = ring.matrix_space(embedding_engine.ncols(), embedding_engine.nrows()).from_rows(
            tuple(
                tuple(_owned_engine_element(ring, embedding_engine[source, target]) for source in range(embedding_engine.nrows())) for target in range(embedding_engine.ncols())
            )
        )
        validate_isometric_embedding((target_gram, gram, embedding), check=False)
        validate_even_unimodular_gram(target_gram, check=False)
        return target_gram, embedding

    def target_primitive_embedding(self, source_gram, target_gram):
        result = self._bridge().call(
            "DzackResearchOscarLatticeAdapter.target_primitive_embedding",
            _integer_engine_matrix(source_gram),
            _integer_engine_matrix(target_gram),
        )
        if not isinstance(result, list) or not result:
            raise RuntimeError(f"the primitive embedding of the form {source_gram} into {target_gram} came back from OSCAR as {result!r}, not a nonempty list")
        if int(result[0]) == 0:
            return None
        if len(result) < 2:
            raise RuntimeError(
                f"the primitive embedding of the form {source_gram} into {target_gram} came back from OSCAR as {result!r}, without the entry saying whether one exists"
            )
        if int(result[1]) == 0:
            return False
        if len(result) != 5:
            raise RuntimeError(f"the primitive embedding of the form {source_gram} into {target_gram} came back from OSCAR as {result!r}, not a list of five entries")
        target_engine, source_engine, embedding_engine = result[2:]
        ring = source_gram.base_ring()

        def owned_gram(engine):
            return tensor(
                ring,
                (),
                (engine.nrows(), engine.ncols()),
                tuple(tuple(_owned_engine_element(ring, entry) for entry in row) for row in engine.rows()),
            )

        target_prime_gram = owned_gram(target_engine)
        source_prime_gram = owned_gram(source_engine)
        embedding = ring.matrix_space(embedding_engine.ncols(), embedding_engine.nrows()).from_rows(
            tuple(
                tuple(_owned_engine_element(ring, embedding_engine[source, target]) for source in range(embedding_engine.nrows())) for target in range(embedding_engine.ncols())
            )
        )
        validate_isometric_embedding((target_prime_gram, source_prime_gram, embedding), check=False)
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
            raise RuntimeError(f"the classes of primitive embeddings of {source_gram} into {target_gram} came back from OSCAR as {result!r}, not a nonempty list")
        if int(result[0]) == 0:
            return None
        if len(result) != 3:
            raise RuntimeError(f"the classes of primitive embeddings of {source_gram} into {target_gram} came back from OSCAR as {result!r}, not a list of three entries")
        if int(result[1]) == 0:
            return ()
        representatives = []
        for record in result[2]:
            if not isinstance(record, list) or len(record) != 3:
                raise RuntimeError(f"a class of primitive embeddings of {source_gram} into {target_gram} came back from OSCAR as {record!r}, not a list of three entries")
            target_engine, source_engine, embedding_engine = record
            ring = source_gram.base_ring()

            def owned_gram(engine):
                return tensor(
                    ring,
                    (),
                    (engine.nrows(), engine.ncols()),
                    tuple(tuple(_owned_engine_element(ring, entry) for entry in row) for row in engine.rows()),
                )

            target_prime_gram = owned_gram(target_engine)
            source_prime_gram = owned_gram(source_engine)
            embedding = ring.matrix_space(embedding_engine.ncols(), embedding_engine.nrows()).from_rows(
                tuple(
                    tuple(_owned_engine_element(ring, embedding_engine[source, target]) for source in range(embedding_engine.nrows()))
                    for target in range(embedding_engine.ncols())
                )
            )
            validate_isometric_embedding((target_prime_gram, source_prime_gram, embedding), check=False)
            representatives.append((target_prime_gram, source_prime_gram, embedding))
        return tuple(representatives)

    def leech_gram_rows(self):
        rows = self._bridge().call("DzackResearchOscarLatticeAdapter.leech_gram_rows")
        if not isinstance(rows, list) or len(rows) != 24:
            raise RuntimeError(f"the Gram matrix of the Leech lattice came back from OSCAR as {rows!r}, not a list of 24 rows")
        matrix_rows = tuple(tuple(SageZZ(entry) for entry in row) for row in rows)
        if any(len(row) != 24 for row in matrix_rows):
            raise RuntimeError(f"the Gram matrix of the Leech lattice from OSCAR has row lengths {tuple(len(row) for row in matrix_rows)}, not 24 each")
        gram = engine_matrix(SageZZ, matrix_rows)
        if not gram.is_symmetric():
            raise ArithmeticError(f"the Gram matrix of the Leech lattice from OSCAR is not symmetric:\n{gram}")
        if abs(gram.det()) != 1:
            raise ArithmeticError(f"the Gram matrix of the Leech lattice from OSCAR is not unimodular: its determinant is {gram.det()}")
        if any(gram[index, index] % 2 for index in range(24)):
            raise ArithmeticError("the Gram matrix of the Leech lattice from OSCAR is not even: some diagonal entry is odd")
        return matrix_rows


_oscar_lattices = _OscarLatticeAdapter()

__all__: list[str] = []
