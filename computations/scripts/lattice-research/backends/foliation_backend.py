from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from ore_algebra import OreAlgebra
from ore_algebra.differential_operator_1_1 import (
    UnivariateDifferentialOperatorOverUnivariateRing,
)
from sage.all import (
    SR,
    ZZ,
    I,
    PolynomialRing,
    QQbar,
    companion_matrix,
    diagonal_matrix,
    exp,
    factorial,
    identity_matrix,
    matrix,
    pi,
)
from sage.interfaces.singular import singular

_FOLIATION_LIB_PATH = Path(__file__).resolve().parent.parent / "external" / "foliation.lib"
_FOLIATION_LIB_LOADED = False


@dataclass(frozen=True)
class MonodromyJordanBlock:
    exponent: object
    eigenvalue: object
    size: int


@dataclass(frozen=True)
class HodgeTheoreticMonodromy:
    milnor_number: int
    picard_fuchs_operator: UnivariateDifferentialOperatorOverUnivariateRing
    indicial_polynomial: object
    log_monodromy_jordan_form: object
    semisimple_log_monodromy: object
    nilpotent_log_monodromy: object
    nilpotent_monodromy_matrix: object
    semisimple_monodromy_matrix: object
    unipotent_monodromy_matrix: object
    monodromy_matrix: object
    monodromy_jordan_form: object
    jordan_blocks: tuple[MonodromyJordanBlock, ...]


@dataclass(frozen=True)
class _NormalizedHypersurfaceFamily:
    polynomial: object
    parameter: object
    spatial_variables: tuple
    spatial_weights: tuple[int, ...] | None


def hodge_theoretic_monodromy_of_family(family) -> HodgeTheoreticMonodromy:
    normalized = _normalize_one_parameter_hypersurface_family(family)
    milnor_number, coefficients = _singular_picard_fuchs_data(normalized)
    operator = _picard_fuchs_operator(normalized.parameter, coefficients)
    indicial_polynomial = _indicial_polynomial_at_zero(operator)
    log_jordan = _log_monodromy_jordan_form(indicial_polynomial, milnor_number)
    semisimple_log = _diagonal_part(log_jordan)
    nilpotent_log = log_jordan - semisimple_log
    blocks = _jordan_blocks(log_jordan)
    nilpotent_monodromy = _nilpotent_monodromy_matrix(nilpotent_log)
    semisimple_monodromy = _semisimple_monodromy_matrix(blocks)
    unipotent_monodromy = _unipotent_monodromy_matrix(nilpotent_log)
    return HodgeTheoreticMonodromy(
        milnor_number=milnor_number,
        picard_fuchs_operator=operator,
        indicial_polynomial=indicial_polynomial,
        log_monodromy_jordan_form=log_jordan,
        semisimple_log_monodromy=semisimple_log,
        nilpotent_log_monodromy=nilpotent_log,
        nilpotent_monodromy_matrix=nilpotent_monodromy,
        semisimple_monodromy_matrix=semisimple_monodromy,
        unipotent_monodromy_matrix=unipotent_monodromy,
        monodromy_matrix=semisimple_monodromy * unipotent_monodromy,
        monodromy_jordan_form=_standard_monodromy_jordan_form(blocks),
        jordan_blocks=blocks,
    )


def _normalize_one_parameter_hypersurface_family(family) -> _NormalizedHypersurfaceFamily:
    equation = family.hypersurface_family_equation()
    ring = equation.parent()
    assert ring.base_ring().characteristic() == 0
    generators = ring.gens()
    assert len(generators) >= 2
    normalized_names = tuple(f"x{i}" for i in range(len(generators) - 1)) + ("t",)
    normalized_ring = PolynomialRing(
        ring.base_ring(),
        names=normalized_names,
        order=ring.term_order(),
    )
    normalized_equation = ring.hom(normalized_ring.gens(), normalized_ring)(equation)
    term_order = normalized_ring.term_order()
    weights = getattr(term_order, "weights", lambda: None)()
    if weights is None:
        spatial_weights = None
    else:
        assert len(weights) == len(normalized_ring.gens())
        spatial_weights = tuple(ZZ(weight) for weight in weights[:-1])
    return _NormalizedHypersurfaceFamily(
        polynomial=normalized_equation,
        parameter=normalized_ring.gens()[-1],
        spatial_variables=normalized_ring.gens()[:-1],
        spatial_weights=spatial_weights,
    )


def _singular_picard_fuchs_data(
    normalized: _NormalizedHypersurfaceFamily,
) -> tuple[int, tuple]:
    _ensure_foliation_lib_loaded()
    ring_order = _singular_ring_order(normalized)
    spatial_variables = ",".join(str(v) for v in normalized.spatial_variables)
    singular.eval(f"ring foliation_r = (0,t),({spatial_variables}),{ring_order};")
    singular.eval(f"poly f = {normalized.polynomial};")
    singular.eval("ideal J = jacob(f);")
    singular.eval("ideal B = okbase(std(J));")
    singular.eval("int mu = size(B);")
    singular.eval("poly gen_p = 0;")
    singular.eval("int ii;")
    singular.eval("for (ii = 1; ii <= mu; ii++) { gen_p = gen_p + B[ii]; }")
    singular.eval("poly dy_c = diff(f, var(nvars(basering)));")
    singular.eval("poly P_form = (-1)^(nvars(basering)-1) * (dy_c / var(nvars(basering))) * gen_p;")
    singular.eval("vector ve = [1];")
    singular.eval("matrix PF = PFequ(f, P_form, ve);")
    milnor_number = int(singular.eval("mu"))
    pf_matrix = singular("PF").sage()
    coefficients = tuple(_extract_parameter_polynomial(entry) for entry in pf_matrix.rows()[0])
    assert len(coefficients) == milnor_number + 1
    return milnor_number, coefficients


def _extract_parameter_polynomial(entry):
    assert all(degree == 0 for degree in entry.degrees())
    constant = entry.constant_coefficient()
    assert constant.denominator() == 1
    return constant.numerator()


def _picard_fuchs_operator(
    parameter,
    coefficients,
) -> UnivariateDifferentialOperatorOverUnivariateRing:
    parameter_ring = coefficients[0].parent()
    differential_algebra = OreAlgebra(parameter_ring, names=(f"D{parameter}",))
    differential_operator = differential_algebra.gen()
    return sum(
        (coefficient * differential_operator**degree for degree, coefficient in enumerate(coefficients)),
        differential_algebra.zero(),
    )


def _indicial_polynomial_at_zero(operator):
    # ore_algebra built-in: roots are the indicial exponents at t=0.
    return operator.indicial_polynomial(operator.base_ring().gen())


def _log_monodromy_jordan_form(indicial_polynomial, milnor_number: int):
    assert indicial_polynomial.degree() == milnor_number, (
        "Degree of indicial polynomial must equal Milnor number (regular singular point assumption)"
    )
    jordan, _ = companion_matrix(indicial_polynomial.monic()).change_ring(QQbar).jordan_form(transformation=True)
    return jordan


def _diagonal_part(jordan_matrix):
    diagonal = [jordan_matrix[index, index] for index in range(jordan_matrix.nrows())]
    return diagonal_matrix(jordan_matrix.base_ring(), diagonal)


def _nilpotent_monodromy_matrix(nilpotent_log):
    return (2 * pi * I) * nilpotent_log.change_ring(SR)


def _unipotent_monodromy_matrix(nilpotent_log):
    nilpotent_sr = nilpotent_log.change_ring(SR)
    size = nilpotent_sr.nrows()
    scalar = 2 * pi * I
    result = identity_matrix(SR, size)
    power = identity_matrix(SR, size)
    for exponent in range(1, size):
        power *= nilpotent_sr
        if power.is_zero():
            break
        result += (scalar**exponent / factorial(exponent)) * power
    return result


def _jordan_blocks(jordan_matrix) -> tuple[MonodromyJordanBlock, ...]:
    blocks = []
    index = 0
    size = jordan_matrix.nrows()
    while index < size:
        exponent = jordan_matrix[index, index]
        block_size = 1
        while (
            index + block_size < size
            and jordan_matrix[index + block_size - 1, index + block_size] != 0
            and jordan_matrix[index + block_size, index + block_size] == exponent
        ):
            block_size += 1
        blocks.append(
            MonodromyJordanBlock(
                exponent=exponent,
                eigenvalue=_monodromy_eigenvalue(exponent),
                size=block_size,
            )
        )
        index += block_size
    return tuple(blocks)


def _semisimple_monodromy_matrix(blocks: tuple[MonodromyJordanBlock, ...]):
    diagonal = [block.eigenvalue for block in blocks for _ in range(block.size)]
    return diagonal_matrix(SR, diagonal)


def _standard_monodromy_jordan_form(blocks: tuple[MonodromyJordanBlock, ...]):
    size = sum(block.size for block in blocks)
    result = matrix(SR, size, size, 0)
    offset = 0
    for block in blocks:
        for index in range(block.size):
            result[offset + index, offset + index] = block.eigenvalue
        for index in range(block.size - 1):
            result[offset + index, offset + index + 1] = 1
        offset += block.size
    return result


def _monodromy_eigenvalue(exponent):
    return SR(exp(2 * pi * I * SR(exponent)))


def _singular_ring_order(normalized: _NormalizedHypersurfaceFamily) -> str:
    if normalized.spatial_weights is None:
        return "dp"
    weights = ",".join(str(weight) for weight in normalized.spatial_weights)
    return f"wp({weights})"


def _ensure_foliation_lib_loaded():
    global _FOLIATION_LIB_LOADED
    assert _FOLIATION_LIB_PATH.exists()
    if _FOLIATION_LIB_LOADED:
        return
    singular.eval(f'LIB "{_FOLIATION_LIB_PATH}";')
    _FOLIATION_LIB_LOADED = True


__all__ = [
    "HodgeTheoreticMonodromy",
    "MonodromyJordanBlock",
    "hodge_theoretic_monodromy_of_family",
]
