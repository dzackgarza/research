r"""The del Pezzo, Enriques and Nikulin involutions on $L_{K3} = U^3 \oplus E_8^2$.

Ported from old init.sage lines 183-224. The source wrote them as ``LK3.hom([...])``
over a named basis declared with Sage's ellipsis generator syntax::

    LK3.<v1, v2, u1, u2, up1, up2, e1, ..., e8, ep1, ..., ep8> = U**3 @ E8**2

so each involution is given as the list of images of the 22 basis vectors, in order.
They are built here as explicit matrices on coordinates, which avoids depending on
that syntax and makes the two defining properties checkable:

- $I^2 = \mathrm{id}$ (it is an involution), and
- $I^{T} G I = G$ (it is an isometry of the lattice).

Neither was asserted in the source. Both are asserted here, on all three, because a
single mistyped image in a 22-entry list would break one or the other.

The invariant and anti-invariant sublattices $L^{\pm} = \ker(I \mp \mathrm{id})$ are
the objects these involutions exist to produce -- for a nonsymplectic involution they
are the two-elementary lattices of the $(r, a, \delta)$ classification.
"""

from __future__ import annotations

from typing import Any

from sage.matrix.constructor import matrix
from sage.matrix.special import identity_matrix
from sage.rings.integer_ring import ZZ

from . import catalogue

__all__ = [
    "BASIS_NAMES",
    "anti_invariant_lattice",
    "involution",
    "invariant_lattice",
    "involutions",
]

#: The named basis of $L_{K3}$ in the source's order: three hyperbolic planes, then
#: two copies of $E_8$.
BASIS_NAMES: tuple[str, ...] = ("v1", "v2", "u1", "u2", "up1", "up2") + tuple(f"e{i}" for i in range(1, 9)) + tuple(f"ep{i}" for i in range(1, 9))

_INDEX = {name: i for i, name in enumerate(BASIS_NAMES)}


def _images_to_matrix(images: list[tuple[str, int]]) -> Any:
    """Build the matrix whose columns are the given signed basis images."""
    size = len(BASIS_NAMES)
    assert len(images) == size, f"need {size} images, got {len(images)}"
    columns = []
    for name, sign in images:
        column = [0] * size
        column[_INDEX[name]] = sign
        columns.append(column)
    return matrix(ZZ, columns).transpose()


def _involution_images() -> dict[str, list[tuple[str, int]]]:
    r"""The three image lists, transcribed from old lines 192-220."""
    e_names = [f"e{i}" for i in range(1, 9)]
    ep_names = [f"ep{i}" for i in range(1, 9)]

    return {
        # I_dP: v -> -v, the two u-planes swap, both E8 blocks negate.
        "I_dP": ([("v1", -1), ("v2", -1), ("up1", 1), ("up2", 1), ("u1", 1), ("u2", 1)] + [(n, -1) for n in e_names] + [(n, -1) for n in ep_names]),
        # I_En: v -> -v, the two u-planes swap, the two E8 blocks swap.
        "I_En": ([("v1", -1), ("v2", -1), ("up1", 1), ("up2", 1), ("u1", 1), ("u2", 1)] + [(n, 1) for n in ep_names] + [(n, 1) for n in e_names]),
        # I_Nik: all three hyperbolic planes fixed, the E8 blocks swap with a sign.
        "I_Nik": ([("v1", 1), ("v2", 1), ("u1", 1), ("u2", 1), ("up1", 1), ("up2", 1)] + [(n, -1) for n in ep_names] + [(n, -1) for n in e_names]),
    }


def involution(name: str) -> Any:
    """One of ``I_dP``, ``I_En``, ``I_Nik`` as a matrix, with both properties asserted."""
    images = _involution_images()
    assert name in images, f"unknown involution {name!r}; have {sorted(images)}"

    action = _images_to_matrix(images[name])
    size = action.nrows()

    assert action * action == identity_matrix(ZZ, size), f"{name} is not an involution: I^2 != id"
    gram = catalogue.LK3.gram_matrix()
    assert action.transpose() * gram * action == gram, f"{name} is not an isometry: I^T G I != G"
    return action


def involutions() -> dict[str, Any]:
    """All three, each validated."""
    return {name: involution(name) for name in _involution_images()}


def _eigenlattice(action: Any, sign: int) -> Any:
    r"""$\ker(I - \varepsilon\,\mathrm{id})$ as a lattice with the induced form."""
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
    r"""$L^{+} = \ker(I - \mathrm{id})$, the sublattice the involution fixes."""
    return _eigenlattice(involution(name), 1)


def anti_invariant_lattice(name: str) -> Any:
    r"""$L^{-} = \ker(I + \mathrm{id})$, on which the involution acts as $-1$."""
    return _eigenlattice(involution(name), -1)
