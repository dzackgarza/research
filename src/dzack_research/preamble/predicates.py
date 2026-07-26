r"""Predicates and quotients for integral lattices.

EXAMPLES::

    sage: from dzack_research.preamble import catalogue, predicates
    sage: predicates.is_elliptic(catalogue.E8)
    True
    sage: predicates.delta(catalogue.E8)
    0
"""

from __future__ import annotations

from typing import Any

from sage.arith.misc import gcd
from sage.rings.infinity import Infinity

__all__ = [
    "delta",
    "e_perp_mod_e",
    "is_coeven",
    "is_coodd",
    "is_elliptic",
    "is_parabolic",
]


def is_coeven(lattice: Any) -> bool:
    r"""Return whether the discriminant form is integer-valued.

    This is Nikulin's condition $\delta=0$.

    EXAMPLES::

        sage: from dzack_research.preamble import catalogue, predicates
        sage: predicates.is_coeven(catalogue.E8)
        True
    """
    from sage.rings.rational_field import QQ

    disc = lattice.discriminant_group()
    assert disc.cardinality() < Infinity, (
        "discriminant group is infinite; the lattice must be nondegenerate"
    )
    return all(QQ(element.q()).denominator() == 1 for element in disc)


def is_coodd(lattice: Any) -> bool:
    """Return the negation of :func:`is_coeven`."""
    return not is_coeven(lattice)


def delta(lattice: Any) -> int:
    r"""Return Nikulin's invariant $\delta\in\{0,1\}$."""
    return 0 if is_coeven(lattice) else 1


def is_elliptic(lattice: Any) -> bool:
    """Return whether the lattice is negative definite."""
    return bool((-lattice.gram_matrix()).is_positive_definite())


def is_parabolic(lattice: Any) -> bool:
    """Return whether the lattice is negative semidefinite."""
    return bool((-lattice.gram_matrix()).is_positive_semidefinite())


def e_perp_mod_e(lattice: Any, isotropic_vector: Any) -> Any:
    r"""Return $e^\perp/\langle e\rangle$ for a primitive isotropic vector.

    EXAMPLES::

        sage: from dzack_research.preamble import catalogue, predicates
        sage: e = catalogue.U.gens()[0]
        sage: predicates.e_perp_mod_e(catalogue.U, e)
        []
    """
    from sage.matrix.constructor import matrix
    from sage.modules.free_module import FreeModule
    from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice
    from sage.rings.integer_ring import ZZ

    norm = isotropic_vector.inner_product(isotropic_vector)
    assert norm == 0, (
        f"e_perp_mod_e needs an isotropic vector; this one has norm {norm}"
    )

    gram = lattice.gram_matrix()
    coords = lattice.coordinate_vector(isotropic_vector).change_ring(ZZ)
    assert gcd(coords) == 1, (
        f"isotropic vector must be primitive; its coordinates {coords} have common divisor {gcd(coords)}, so <e> is not saturated and the quotient would carry spurious torsion"
    )

    free_module = FreeModule(ZZ, lattice.rank())
    perp = free_module.submodule(matrix(ZZ, [gram * coords]).right_kernel().basis())
    quotient = perp / free_module.submodule([coords])

    lifts = [generator.lift() for generator in quotient.gens()]
    induced = matrix(
        ZZ,
        [[(u * gram * v) for v in lifts] for u in lifts],
    )
    assert induced.is_symmetric(), "induced form is not symmetric"
    if induced.nrows() == 0:
        return induced  # rank 0: U itself, where the quotient is the zero lattice
    return IntegralLattice(induced)
