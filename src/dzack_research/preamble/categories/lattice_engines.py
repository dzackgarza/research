r"""Private exact computational realizations for owned lattice constructions."""

from sage.libs.gap.libgap import libgap
from sage.matrix.constructor import matrix as engine_matrix
from sage.matrix.matrix0 import Matrix
from sage.quadratic_forms.binary_qf import BinaryQF
from sage.quadratic_forms.qfsolve import qfsolve
from sage.quadratic_forms.quadratic_form import QuadraticForm
from sage.rings.integer import Integer as SageInteger
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ

from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_element,
    _engine_ring,
    _owned_engine_element,
)
from dzack_research.preamble.categories.sets.set_categories import NN
from dzack_research.preamble.tensors.tensor import (
    Tensor,
    _engine_column_matrix_from_row_action,
    _engine_component_matrix,
    _engine_row_action_matrix,
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


def _rational_signed_direction(gram, sign):
    r"""Select a column of Sage's rational diagonalization with the requested sign.

    This is the shared diagonalization step of the port's positive-direction
    and negative-direction-in-span computations. A subspace supplies its own
    restricted Gram tensor through its formed subobject construction.
    """
    if not isinstance(gram, Tensor) or gram.tensor_valence() != (NN**2)((0, 2)):
        raise TypeError(f"cannot find a vector of positive square for {gram}: it must be the Gram tensor of a bilinear form, a tensor of type (0, 2)")
    engine_gram = _engine_component_matrix(gram).change_ring(SageQQ)
    diagonal, change = QuadraticForm(
        SageQQ,
        2 * engine_gram,
    ).rational_diagonal_form(return_matrix=True)
    diagonal_matrix = diagonal.matrix()
    index = next((
        index for index in range(diagonal_matrix.nrows())
        if sign * diagonal_matrix[index, index] > 0
    ), None)
    return None if index is None else change.column(index)


def _rational_positive_vector(gram):
    r"""Return one rational positive vector as a type-``(1,0)`` tensor."""
    column = _rational_signed_direction(gram, 1)
    if column is None:
        raise ValueError(f"the form with Gram tensor {gram} has no positive direction")
    rationals = gram.base_ring().fraction_field()
    return tensor.vector(
        rationals,
        tuple(_owned_engine_element(rationals, entry) for entry in column),
    )


def _raise_rational_lattice_vector(lattice, coordinates):
    r"""Raise a rational direction, primitively over ZZ, in its given lattice."""
    ring = lattice.base_ring()
    engine_ring = _engine_ring(ring)
    if engine_ring is SageZZ:
        coordinates = coordinates * coordinates.denominator()
    vector = lattice.linear_combination({
        label: _owned_engine_element(ring, engine_ring(coordinate))
        for label, coordinate in zip(lattice.module_generating_set(), coordinates, strict=True)
        if coordinate
    })
    return vector.primitive_part() if engine_ring is SageZZ else vector


def _signed_vector_witness(lattice, sign):
    r"""Realize a finite symmetric formed module's signed-vector operation.

    Private computation for ``BilinearFormModules.Symmetric.vector_of_sign``.
    The input retains its own form and selected framing; the raised vector
    belongs to that same module, including a represented formed submodule.
    Return None if the requested sign is absent.
    """
    ring = lattice.base_ring()
    assert _engine_ring(ring) is SageZZ or _engine_ring(ring) is SageQQ, (
        f"signed vector witnesses are computed over ZZ or QQ, not {ring}"
    )
    assert lattice.module_rank().is_finite(), (
        f"rational diagonalization requires finite rank, not {lattice.module_rank()}"
    )
    if lattice.module_rank() == 0:
        return None
    coordinates = _rational_signed_direction(lattice.gram_tensor(), sign)
    return None if coordinates is None else _raise_rational_lattice_vector(lattice, coordinates)


def _isotropic_vector_witness(lattice):
    r"""Raise PARI's rational isotropic vector into the given lattice.

    Migrated from ``sage-indefinite-port``'s ``find_hyperbolic_pair``.
    Sage's ``quadratic_forms.qfsolve.qfsolve`` returns an integer obstruction,
    a vector, or a matrix whose columns span the radical. Integral inputs
    receive a primitive integral vector after clearing denominators.
    """
    ring = lattice.base_ring()
    engine_ring = _engine_ring(ring)
    assert engine_ring is SageZZ or engine_ring is SageQQ, (
        f"isotropic witnesses are computed over ZZ or QQ, not {ring}"
    )
    assert lattice.module_rank().is_finite(), (
        f"PARI isotropic witnesses require finite rank, not {lattice.module_rank()}"
    )
    if lattice.module_rank() == 0:
        return None
    solution = qfsolve(_engine_component_matrix(lattice.gram_tensor()).change_ring(SageQQ))
    if isinstance(solution, SageInteger):
        return None
    if isinstance(solution, Matrix):
        solution = solution.column(0)
    return _raise_rational_lattice_vector(lattice, solution)


def _binary_form_discriminant(lattice):
    r"""Private binary-form datum for the lattice square-fibre operations."""
    if _engine_ring(lattice.base_ring()) is not SageZZ or lattice.module_rank() != 2:
        raise ValueError("binary square-fibre computation requires a rank-two ZZ-lattice")
    gram = _engine_component_matrix(lattice.gram_tensor())
    return gram[0, 1] ** 2 - gram[0, 0] * gram[1, 1]


def _split_binary_vectors_of_square(lattice, square):
    r"""All vectors of nonzero square for a split nondegenerate binary form.

    SymPy's BinaryQuadratic.solve handles the finite square-discriminant
    case by its maintained factor/divisor algorithm; unlike qfbsolve this
    returns the full fibre here. See sympy/solvers/diophantine/diophantine.py,
    BinaryQuadratic, case (3), and its Alpertron reference.
    """
    from sympy import symbols
    from sympy.solvers.diophantine.diophantine import BinaryQuadratic

    discriminant = _binary_form_discriminant(lattice)
    if not square or discriminant <= 0 or not discriminant.is_square():
        raise ValueError("a finite split binary square fibre requires nonzero square and positive square discriminant")
    gram = _engine_component_matrix(lattice.gram_tensor())
    x, y = symbols("x y", integer=True)
    polynomial = int(gram[0, 0]) * x*x + 2*int(gram[0, 1]) * x*y + int(gram[1, 1]) * y*y - int(square)
    solutions = BinaryQuadratic(polynomial, free_symbols=[x, y]).solve()
    labels = tuple(lattice.module_generating_set())
    ring = lattice.base_ring()
    return tuple(
        lattice.linear_combination({label: ring(int(coordinate)) for label, coordinate in zip(labels, solution, strict=True)})
        for solution in sorted(solutions)
    )


def _binary_primitive_isotropic_vectors(lattice):
    r"""Raise the primitive generators of the rational linear factors, with both signs."""
    from sympy import Poly, factor_list, symbols

    discriminant = _binary_form_discriminant(lattice)
    if not discriminant:
        raise ValueError("this finite null-line computation requires a nondegenerate binary form")
    if discriminant < 0 or not discriminant.is_square():
        return ()
    gram = _engine_component_matrix(lattice.gram_tensor())
    x, y = symbols("x y", integer=True)
    polynomial = int(gram[0, 0]) * x*x + 2*int(gram[0, 1]) * x*y + int(gram[1, 1]) * y*y
    labels = tuple(lattice.module_generating_set())
    ring = lattice.base_ring()
    points = []
    for factor, _multiplicity in factor_list(polynomial)[1]:
        line = Poly(factor, x, y)
        coefficients = (-int(line.coeff_monomial(y)), int(line.coeff_monomial(x)))
        vector = lattice.linear_combination(dict(zip(labels, (ring(c) for c in coefficients), strict=True))).primitive_part()
        points.extend((vector, -vector))
    return tuple(points)


def _rational_representation_witness(lattice, value):
    r"""Return a vector ``x`` of the nondegenerate ``QQ``-lattice with ``b(x, x) = value``, or ``None``.

    ``value`` is a nonzero element of the base ring, so ``b perp <-value>`` is
    nondegenerate and ``qfsolve`` returns either PARI's integer obstruction
    or one isotropic vector, never a matrix spanning a radical.  The space represents
    ``a != 0`` exactly when ``b perp <-a>`` represents 0 (Serre, *A Course
    in Arithmetic*, Ch. IV, 1.6, Cor. 1 of Prop. 3'), and PARI's
    ``qfsolve`` decides that isotropy (Hasse--Minkowski, Ch. IV, 3.2,
    Thm. 8).  A zero ``(x, z)`` with ``z != 0`` gives ``b(x/z, x/z) = a``.
    A zero with ``z = 0`` is a nonzero isotropic ``x`` of ``L``, and then
    every value is represented (Ch. IV, 1.3, Cor. of Prop. 3): with Gram
    matrix ``G``, ``y = G x`` has ``b(x, y) = (G x) . (G x) != 0``, and
    ``y + t x`` with ``t = (a - b(y, y)) / (2 b(x, y))`` has square ``a``.
    """
    assert _engine_ring(lattice.base_ring()) is SageQQ, (
        f"the rational representation witness is computed over QQ, not {lattice.base_ring()}"
    )
    gram = _engine_component_matrix(lattice.gram_tensor()).change_ring(SageQQ)
    rank = gram.nrows()
    augmented = gram.block_sum(engine_matrix(SageQQ, [[-SageQQ(_engine_element(lattice.base_ring(), value))]]))
    solution = qfsolve(augmented)
    if solution in SageZZ:
        return None
    last = solution[rank]
    isotropic = solution[:rank]
    if last:
        return _raise_rational_lattice_vector(lattice, isotropic / last)
    partner = gram * isotropic
    pairing = isotropic * gram * partner
    shift = (SageQQ(_engine_element(lattice.base_ring(), value)) - partner * gram * partner) / (2 * pairing)
    return _raise_rational_lattice_vector(lattice, partner + shift * isotropic)


def _binary_special_orthogonal_representatives(lattice, square):
    r"""Raise PARI representatives for a nonsplit indefinite binary form.

    PARI ``qfbsolve`` flag 3 includes imprimitive solutions and returns
    every class modulo the integral special orthogonal group:
    https://pari.math.u-bordeaux.fr/dochtml/html-stable/Arithmetic_functions.html#qfbsolve
    """
    ring = lattice.base_ring()
    if _engine_ring(ring) is not SageZZ or lattice.module_rank() != 2:
        raise ValueError("binary representation classes require a rank-two ZZ-lattice")
    gram = _engine_component_matrix(lattice.gram_tensor())
    form = BinaryQF((gram[0, 0], 2 * gram[0, 1], gram[1, 1]))
    discriminant = form.discriminant()
    if discriminant <= 0 or discriminant.is_square():
        raise ValueError("this binary representation computation requires positive nonsquare discriminant")
    if not square:
        return (lattice.zero(),)
    labels = tuple(lattice.module_generating_set())
    return tuple(
        lattice.linear_combination({label: _owned_engine_element(ring, SageZZ(coordinate)) for label, coordinate in zip(labels, solution, strict=True)})
        for solution in form.solve_integer(SageZZ(int(square)), _flag=3)
    )


def _binary_reduction_cycle(lattice, bound, start):
    r"""Realize the specified binary edgewalk cycle and raise its period map.

    The computation is the frozen provider in sage-indefinite-port commit
    709f81a, indefinite/edgewalk_rank2.py: canonical_companion, promised_step,
    shorter_pair, reduced_start_pair, and anisotropic_cycle. It is kept
    private here; its rows are raised through the lattice Mor constructor.
    """
    from sage.modules.free_module_element import vector

    discriminant = _binary_form_discriminant(lattice)
    if discriminant <= 0 or discriminant.is_square():
        raise ValueError("a binary reduction cycle requires a rationally anisotropic indefinite form")
    if start.parent() is not lattice or start.content() != lattice.base_ring().one() or start.q() <= 0:
        raise ValueError("the cycle start must be a primitive positive vector of the lattice")
    rational_bound = lattice.base_ring().fraction_field()(bound)
    bound = SageQQ(int(rational_bound.numerator())) / int(rational_bound.denominator())
    if bound <= 0:
        return None
    gram = _engine_component_matrix(lattice.gram_tensor())
    labels = tuple(lattice.module_generating_set())

    def pairing(left, right):
        return left * gram * right

    def square(point):
        return pairing(point, point)

    def companion(limit, right, left):
        rr, rl, ll = square(right), pairing(right, left), square(left)
        radicand = SageQQ(rl*rl - rr*(ll-limit))
        root = SageZZ(radicand.floor()).isqrt()
        multiple = SageZZ((SageQQ(-rl + root) / rr).floor())
        return left + multiple*right

    def step(limit, right, left):
        while True:
            middle = right + left
            if square(middle) <= limit or pairing(middle, right) < 0:
                left = middle
            elif square(left) >= 0 and pairing(right, left) > 0:
                return left, -right
            else:
                right = middle

    def characteristic(right, left):
        return square(right), pairing(right, left), square(left)

    def shorter(right, left):
        initial_square = square(right)
        initial = characteristic(right, left)
        while True:
            right, left = step(square(right), right, left)
            left = companion(square(right), right, left)
            if square(right) < initial_square:
                return right, left
            if characteristic(right, left) == initial:
                return None

    coordinates = start.to_vector()
    right = vector(SageZZ, [SageZZ(int(coordinates(label))) for label in labels])
    _gcd, s, t = right[0].xgcd(right[1])
    left = companion(bound, right, vector(SageZZ, [-t, s]))
    if square(right) <= bound:
        right, left = step(bound, right, left)
        left = companion(bound, right, left)
    else:
        while square(right) > bound:
            pair = shorter(right, left)
            if pair is None:
                return None
            right, left = pair
        left = companion(bound, right, left)

    initial = characteristic(right, left)
    frame = engine_matrix(SageQQ, [right, left])
    cycle = []
    while True:
        cycle.append(right)
        right, left = step(bound, right, left)
        left = companion(bound, right, left)
        if characteristic(right, left) == initial:
            period = (frame.inverse() * engine_matrix(SageQQ, [right, left])).change_ring(SageZZ)
            break

    ring = lattice.base_ring()

    def raise_vector(point):
        return lattice.linear_combination({label: ring(coordinate) for label, coordinate in zip(labels, point, strict=True)})

    automorphism = lattice.Isom(lattice)(tuple(raise_vector(row) for row in period.rows()))
    return automorphism, tuple(raise_vector(point) for point in cycle)


def _integer_engine_matrix(value):
    if not isinstance(value, Tensor) or value.tensor_order() != 2:
        raise TypeError(f"{value} cannot be passed to OSCAR as an integer matrix: it must be a tensor with two indices")
    return _engine_component_matrix(value).change_ring(SageZZ)


def _rational_engine_matrix(value):
    if not isinstance(value, Tensor) or value.tensor_order() != 2:
        raise TypeError(f"{value} cannot be passed to OSCAR as a rational matrix: it must be a tensor with two indices")
    return _engine_component_matrix(value).change_ring(SageQQ)


def _gap_rational_spinor_norm_class(gram, isometry):
    r"""Return a representative in \(\mathbb Q^\times\) of the spinor norm of ``isometry`` on \((\mathbb Q^n, b)\), ``gram`` the Gram tensor of \(b\).

    Private adapter for ``_rational_spinor_norm_representative`` in
    ``lattice_morphisms.py``.  For \(g\in O(V)\) let \(W=\operatorname{im}(1-g)\)
    and \([w, w']=2b(u, w')\) for \(w=u(1-g)\): the discriminant of this Wall
    form on \(W\) is the class \(b(v_1,v_1)\cdots b(v_m,v_m)\) for
    \(g=s_{v_1}\cdots s_{v_m}\) (Taylor, *The Geometry of the Classical
    Groups*, p. 163).  GAP's ``WallForm`` (``grp/classic.gi``) computes the
    Wall form over any field; both GAP and the lowered isometry act on rows.
    For \(g=1\), \(W=0\) and the class is \(1\).  The route and its
    measurement are the ``TRAPS.md`` row on the rational spinor norm.
    """
    row_action = _engine_row_action_matrix(isometry).change_ring(SageQQ)
    if row_action.is_one():
        return SageQQ.one()
    wall_form = libgap.WallForm(libgap(2 * _rational_engine_matrix(gram)), libgap(row_action))
    value = SageQQ(libgap.DeterminantMat(wall_form["form"]).sage())
    if value == 0:
        raise ArithmeticError(f"GAP computed a degenerate Wall form for the isometry {isometry} of the form {gram}, but the Wall form of an isometry of a nondegenerate space is nondegenerate")
    return value


def _owned_embedding_from_row_action(ring, row_action):
    r"""Raise an OSCAR embedding, which lists source generator images as rows, to an owned matrix Mor."""
    columns = _engine_column_matrix_from_row_action(row_action)
    return ring.matrix_space(columns.nrows(), columns.ncols()).from_rows(
        tuple(tuple(_owned_engine_element(ring, entry) for entry in row) for row in columns.rows())
    )


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


def _number_field_coefficient_rows(engine, field):
    r"""Write a Sage matrix over ``field`` as nested rational power-basis coefficients."""
    return [[list(_number_field_element_coefficients(field, engine[row, column])) for column in range(engine.ncols())] for row in range(engine.nrows())]


def _number_field_engine_matrix(value, field):
    r"""Lower a two-index tensor to nested rational power-basis coefficients."""
    if not isinstance(value, Tensor) or value.tensor_order() != 2:
        raise TypeError(f"{value} cannot be passed to OSCAR as a number-field matrix: it must be a tensor with two indices")
    return _number_field_coefficient_rows(_engine_component_matrix(value), field)


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

function integer_lattices_are_isometric(first_gram_entries, second_gram_entries)
    first = integer_lattice(; gram = change_base_ring(QQ, _zz_matrix(first_gram_entries)))
    second = integer_lattice(; gram = change_base_ring(QQ, _zz_matrix(second_gram_entries)))
    return is_isometric(first, second) ? 1 : 0
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
            _number_field_coefficient_rows(_engine_row_action_matrix(isometry), field),
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
            _engine_row_action_matrix(isometry).change_ring(SageZZ),
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

        embedding = _owned_embedding_from_row_action(ring, embedding_engine)
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
        embedding = _owned_embedding_from_row_action(ring, embedding_engine)
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
            embedding = _owned_embedding_from_row_action(ring, embedding_engine)
            validate_isometric_embedding((target_prime_gram, source_prime_gram, embedding), check=False)
            representatives.append((target_prime_gram, source_prime_gram, embedding))
        return tuple(representatives)

    def integer_lattices_are_isometric(self, first, second):
        r"""Decide whether ``(ZZ^n, first)`` and ``(ZZ^n, second)`` are isometric, by Hecke's ``is_isometric``.

        ``first`` and ``second`` are Sage integer Gram matrices of
        nondegenerate lattices ``L`` and ``M``.  For an indefinite genus of rank
        at least 3 Hecke (``_is_isometric_indef``) answers ``False`` when the
        genera differ and ``True`` when the genus has no improper spinor
        generators.  Otherwise it approximates an isometry ``f`` of the rational
        quadratic spaces with ``f(L_p) = M_p`` at every prime ``p`` dividing
        ``2 det L``, and answers whether the index ``r = [M : f(L) cap M]`` is
        improperly automorphous (Conway and Sloane, *Sphere Packings, Lattices
        and Groups*, chapter 15, Theorem 15, as Hecke's
        ``improper_spinor_generators`` cites it).
        """
        answer = SageZZ(
            self._bridge().call(
                "DzackResearchOscarLatticeAdapter.integer_lattices_are_isometric",
                first,
                second,
            )
        )
        if answer not in (0, 1):
            raise RuntimeError(f"Hecke answered {answer} for the isometry of the forms {first} and {second}, not 0 or 1")
        return answer == 1

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


_ROOTS_IN_ANNULUS = (
    "(form, majorant, inner, outer, lengths) -> my(found = List());"
    " forqfvec(v, majorant, outer, if(v~ * majorant * v > inner,"
    " my(square = v~ * form * v);"
    " if(square && setsearch(lengths, abs(square)) && content(2 * form * v) % square == 0, listput(found, v))));"
    " Vec(found)"
)
r"""PARI closure listing, one of each pair \(\pm v\), the roots \(v\) with ``inner < M(v) <= outer``.

``forqfvec`` visits the ball without storing it, so memory holds only the roots found.
"""


def _roots_generating_lattice(gram, lengths):
    r"""Return coordinate rows of roots that generate \(\mathbb Z^n\) under the integral form ``gram``.

    A root is a vector \(r\) with \(b(r,r)\ne 0\) dividing \(2b(r,x)\) for every
    \(x\); its \(|b(r,r)|\) lies in ``lengths``.  With
    \(T^{t}GT=D\) a rational diagonalization, \(T^{-t}|D|T^{-1}\) is a positive
    definite majorant \(M\) of \(G\), so each ball of \(M\) holds finitely many
    vectors.  The annuli between radii \(R\) and \(2R\) are searched in turn,
    and a root is kept when it enlarges the span of those kept.  The search
    returns once they span \(\mathbb Z^n\), and runs without end, in memory
    bounded by the roots found, when \(\mathbb Z\Phi(L)\ne L\).
    """
    from sage.arith.functions import lcm
    from sage.libs.pari import pari

    form = _engine_component_matrix(gram).change_ring(SageZZ)
    rank = form.nrows()
    diagonal, change = QuadraticForm(SageQQ, 2 * form).rational_diagonal_form(return_matrix=True)
    inverse = change.inverse()
    majorant = inverse.transpose() * diagonal.matrix().apply_map(abs) * inverse
    majorant = (lcm(entry.denominator() for entry in majorant.list()) * majorant).change_ring(SageZZ)
    roots_in_annulus = pari(_ROOTS_IN_ANNULUS)
    lengths = pari(sorted(int(length) for length in lengths))
    identity = engine_matrix.identity(SageZZ, rank)
    kept = []
    span = engine_matrix(SageZZ, 0, rank)
    inner, outer = 0, max(majorant.diagonal())
    while span != identity:
        for column in roots_in_annulus(pari(form), pari(majorant), inner, outer, lengths):
            vector = tuple(int(entry) for entry in column)
            enlarged = engine_matrix(SageZZ, [*span.rows(), vector]).echelon_form()
            enlarged = enlarged.matrix_from_rows([row for row in range(enlarged.nrows()) if not enlarged.row(row).is_zero()])
            if enlarged != span:
                kept.append(vector)
                span = enlarged
        inner, outer = outer, 2 * outer
    return tuple(kept)
