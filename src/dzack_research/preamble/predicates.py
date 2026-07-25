r"""Lattice predicates from the old init.sage.

**Placement warning, recorded rather than hidden.** These are free functions taking
a lattice, and the lattice spike sites exactly this kind of question as *methods on
the lattice object* (``algebra/domain_algebra.py`` declares ``is_definite``,
``discriminant_form``, ``discriminant_group``, ``isotropic_vectors``, ``twist``,
``direct_sum``, ...). Porting them in this shape re-declares locally what the
category provides, which the repo's own doctrine forbids. They are here because the
port was asked for; the destination for each is a siting decision against
``lexicon/INVENTORY.md``, not this module.

The old file defined ``is_coeven``/``is_coodd`` **twice**. The first pair (line 103)
read ``L.delta``, an attribute nothing in the file ever set, and ``delta_comp``
derived ``delta`` *from* ``is_coeven`` -- so those definitions were circular as well
as dead. Python's later binding won, so the working definitions are the ones at
line 985, ported below. The circular pair is deliberately not reproduced.
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
    r"""Whether $q_L$ is integer-valued on the discriminant group: Nikulin's $\delta = 0$.

    **Neither** of the old file's two definitions ran. The first (line 103) read
    ``L.delta``, which nothing set, and was circular with ``delta_comp``. The second
    (line 985) was ``L.dual_lattice().twist(2).is_even()``, and ``dual_lattice()``
    returns a ``FreeQuadraticModule_submodule_pid`` -- which has no ``twist``, so that
    call raised AttributeError too. There was no working implementation to port.

    Written from the definition instead, preserving the second one's evident intent.
    ``L^*(2)`` even means $2x^2 \in 2\mathbb{Z}$, i.e. $x^2 \in \mathbb{Z}$ for every
    $x \in L^*$, and that is exactly the condition that the discriminant form
    $q_L : A_L \to \mathbb{Q}/2\mathbb{Z}$ takes values in $\mathbb{Z}/2\mathbb{Z}$.

    Every element is tested, not just generators: $q$ is quadratic, not additive
    ($q(x+y) = q(x) + q(y) + 2b(x,y)$), so integrality on generators does not
    propagate to sums.
    """
    from sage.rings.rational_field import QQ

    disc = lattice.discriminant_group()
    assert disc.cardinality() < Infinity, "discriminant group is infinite; the lattice must be nondegenerate"
    return all(QQ(element.q()).denominator() == 1 for element in disc)


def is_coodd(lattice: Any) -> bool:
    """Negation of :func:`is_coeven`.

    The old file wrote this as a separate ``L.delta == 1`` test; stating it as the
    negation removes the possibility of the two disagreeing.
    """
    return not is_coeven(lattice)


def delta(lattice: Any) -> int:
    r"""The invariant $\delta \in \{0, 1\}$: 0 when co-even, 1 when co-odd.

    ``delta_comp`` in the old file. This is the direction the definitions actually
    run -- $\delta$ is *computed from* co-evenness, not assumed as an attribute.
    """
    return 0 if is_coeven(lattice) else 1


def is_elliptic(lattice: Any) -> bool:
    r"""Whether the lattice is negative definite.

    The old file tested this on a *matrix* as ``(-1 * M).is_positive_definite()``.
    Stated on the lattice here: definiteness is a property of the form, and the spike
    already declares ``is_definite`` on the lattice object.

    "Elliptic" is the Coxeter-theoretic name for the spherical case. Note this repo's
    terminology rule: lattices are described by signature and definiteness, and
    "finite type" is not a property a lattice has.
    """
    return bool((-lattice.gram_matrix()).is_positive_definite())


def is_parabolic(lattice: Any) -> bool:
    """Whether the lattice is negative semi-definite (the euclidean/affine case)."""
    return bool((-lattice.gram_matrix()).is_positive_semidefinite())


def e_perp_mod_e(lattice: Any, isotropic_vector: Any) -> Any:
    r"""The lattice $(e^\perp / \langle e\rangle)$ for an isotropic $e$.

    Reconstructed, not ported: the old file *called* ``L.e_perp_mod_e(v)`` in
    ``get_isotrop_type`` and in the Sterk section, but no definition exists anywhere
    in it -- the method had been attached to Sage's class by something no longer
    present, so every one of those call sites raised AttributeError.

    Asserts isotropy first: the quotient is only a lattice when $e^2 = 0$, and
    passing a non-isotropic vector would otherwise return a form that silently is
    not the intended one.

    Taken at module level, not via ``orthogonal_complement``. Because $e$ is
    isotropic it lies in $e^\perp$, so $e^\perp$ is *always* a degenerate lattice and
    Sage refuses to construct it ("lattices must be nondegenerate"). Only the
    quotient is nondegenerate, so the quotient is formed on the underlying modules
    and the form is attached to the result.
    """
    from sage.matrix.constructor import matrix
    from sage.modules.free_module import FreeModule
    from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice
    from sage.rings.integer_ring import ZZ

    norm = isotropic_vector.inner_product(isotropic_vector)
    assert norm == 0, f"e_perp_mod_e needs an isotropic vector; this one has norm {norm}"

    gram = lattice.gram_matrix()
    coords = lattice.coordinate_vector(isotropic_vector).change_ring(ZZ)
    assert gcd(coords) == 1, (
        f"isotropic vector must be primitive; its coordinates {coords} have common divisor {gcd(coords)}, so <e> is not saturated and the quotient would carry spurious torsion"
    )

    ambient = FreeModule(ZZ, lattice.rank())
    perp = ambient.submodule(matrix(ZZ, [gram * coords]).right_kernel().basis())
    quotient = perp / ambient.submodule([coords])

    lifts = [generator.lift() for generator in quotient.gens()]
    induced = matrix(
        ZZ,
        [[(u * gram * v) for v in lifts] for u in lifts],
    )
    assert induced.is_symmetric(), "induced form is not symmetric"
    if induced.nrows() == 0:
        return induced  # rank 0: U itself, where the quotient is the zero lattice
    return IntegralLattice(induced)
