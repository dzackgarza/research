"""Owned runtime names emitted by the research Sage dialect.

The parser may run on top of Sage, but lowered public preamble source resolves
these names into preamble objects.  Backend constructors are used only inside
the functions below and every backend value is crossed back before return.
"""

from __future__ import annotations
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedRings,
    _own_ring,
)
from dzack_research.preamble.categories.sets.set_categories import (
    ConditionSet as owned_condition_set,
    ImageSet as owned_image_set,
    Set as owned_set,
)
from dzack_research.preamble.rings.real import (
    RR,
    RealApproximation as owned,
)


def Integer(value=0):
    from sage.rings.integer_ring import ZZ as SageZZ

    return _own_ring(SageZZ)(value)


def RealNumber(value):

    return RR(value)


def RealApproximation(value):

    return owned(value)


def ComplexNumber(real, imag=None):
    from sage.rings.complex_mpfr import create_ComplexNumber

    backend = (
        create_ComplexNumber(real)
        if imag is None
        else create_ComplexNumber(real, imag)
    )
    parent = _own_ring(backend.parent())
    return parent._from_engine_element(backend)


def matrix(rows):
    r"""Construct the owned matrix-Hom represented by a rectangular row family."""
    rows = tuple(tuple(row) for row in rows)
    if rows:
        width = len(rows[0])
        if any(len(row) != width for row in rows):
            raise ValueError("matrix rows must have one common length")
    else:
        width = 0

    from sage.rings.integer_ring import ZZ as SageZZ

    ring = None
    for row in rows:
        for entry in row:
            parent = getattr(entry, "parent", lambda: None)()
            if parent in OwnedRings():
                ring = parent
                break
        if ring is not None:
            break
    if ring is None:
        ring = _own_ring(SageZZ)
    matrix_space = __import__(
        "dzack_research.preamble.categories.modules.module_morphisms.module_morphisms",
        fromlist=["MatrixSpace"],
    ).MatrixSpace(ring, len(rows), width)
    return matrix_space.from_rows(rows)


def Set(iterable):

    return owned_set(iterable)


def ImageSet(function, domain):

    return owned_image_set(function, domain)


def ConditionSet(domain, predicate):

    return owned_condition_set(domain, predicate)


def factorial(value):
    integer = Integer(value)
    from math import factorial as python_factorial

    return integer.parent()(python_factorial(int(integer)))


def ellipsis_range(*args):
    from sage.arith.srange import ellipsis_range as backend_ellipsis_range

    converted = [int(Integer(value)) if value is not Ellipsis else value for value in args]
    return [Integer(value) for value in backend_ellipsis_range(*converted)]


def ellipsis_iter(*args):
    return iter(ellipsis_range(*args))


def var(*_args, **_kwargs):
    raise NotImplementedError(
        "the preamble has no owned generic symbolic-variable parent yet"
    )


def symbolic_expression(*_args, **_kwargs):
    raise NotImplementedError(
        "the preamble has no owned generic symbolic-expression parent yet"
    )


_RUNTIME = {
    "Integer": Integer,
    "RealNumber": RealNumber,
    "ComplexNumber": ComplexNumber,
    "RealApproximation": RealApproximation,
    "ellipsis_range": ellipsis_range,
    "ellipsis_iter": ellipsis_iter,
    "var": var,
    "symbolic_expression": symbolic_expression,
    "factorial": factorial,
    "matrix": matrix,
    "Set": Set,
    "ImageSet": ImageSet,
    "ConditionSet": ConditionSet,
}
_IMPORTS = {
    name: f"from dzack_research.preamble.language_runtime import {name}"
    for name in _RUNTIME
}
_EXTENSION = {}


def install() -> None:
    from sageparse.preparser import register_extension

    register_extension(_EXTENSION, runtime=_RUNTIME, imports=_IMPORTS)


__all__ = tuple(_RUNTIME) + ("install",)
