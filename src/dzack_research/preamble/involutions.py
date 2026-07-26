r"""Involutions of the K3 lattice $U^3 \oplus E_8^2$.

EXAMPLES::

    sage: from dzack_research.preamble.involutions import involution
    sage: I = involution("I_En")
    sage: I^2 == identity_matrix(ZZ, 22)
    True
"""

from __future__ import annotations

from typing import Any

from sage.matrix.constructor import matrix
from sage.matrix.special import identity_matrix
from sage.rings.integer_ring import ZZ

from . import catalogue
from .fixtures import INVOLUTION_IMAGES
from .fixtures import K3_BASIS_NAMES as BASIS_NAMES

__all__ = [
    "BASIS_NAMES",
    "anti_invariant_lattice",
    "invariant_lattice",
    "involution",
    "involutions",
]

_INDEX = {name: i for i, name in enumerate(BASIS_NAMES)}


def _images_to_matrix(images: tuple[tuple[str, int], ...]) -> Any:
    """Return the matrix with the signed basis images as columns."""
    size = len(BASIS_NAMES)
    assert len(images) == size, f"need {size} images, got {len(images)}"
    columns = []
    for name, sign in images:
        column = [0] * size
        column[_INDEX[name]] = sign
        columns.append(column)
    return matrix(ZZ, columns).transpose()


def involution(name: str) -> Any:
    """Return a named lattice involution.

    EXAMPLES::

        sage: from dzack_research.preamble.involutions import involution
        sage: involution("I_Nik").nrows()
        22
    """
    images = INVOLUTION_IMAGES
    assert name in images, f"unknown involution {name!r}; have {sorted(images)}"

    action = _images_to_matrix(images[name])
    size = action.nrows()

    assert action * action == identity_matrix(ZZ, size), (
        f"{name} is not an involution: I^2 != id"
    )
    gram = catalogue.LK3.gram_matrix()
    assert action.transpose() * gram * action == gram, (
        f"{name} is not an isometry: I^T G I != G"
    )
    return action


def involutions() -> dict[str, Any]:
    """Return all named involutions."""
    return {name: involution(name) for name in INVOLUTION_IMAGES}


def _eigenlattice(action: Any, sign: int) -> Any:
    r"""Return $\ker(I-\varepsilon\,\mathrm{id})$ with its induced form."""
    from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice

    size = action.nrows()
    kernel = (action - sign * identity_matrix(ZZ, size)).right_kernel().basis()
    if not kernel:
        return None
    gram = catalogue.LK3.gram_matrix()
    induced = matrix(ZZ, [[u * gram * v for v in kernel] for u in kernel])
    assert induced.is_symmetric(), "induced form on the eigenlattice is not symmetric"
    return IntegralLattice(induced)


def invariant_lattice(name: str) -> Any:
    r"""Return $L^{+}=\ker(I-\mathrm{id})$.

    EXAMPLES::

        sage: from dzack_research.preamble.involutions import invariant_lattice
        sage: invariant_lattice("I_En").rank()
        10
    """
    return _eigenlattice(involution(name), 1)


def anti_invariant_lattice(name: str) -> Any:
    r"""Return $L^{-}=\ker(I+\mathrm{id})$.

    EXAMPLES::

        sage: from dzack_research.preamble.involutions import anti_invariant_lattice
        sage: anti_invariant_lattice("I_En").rank()
        12
    """
    return _eigenlattice(involution(name), -1)
