r"""Install the vendored Vinberg root-enumeration method.

EXAMPLES::

    sage: from dzack_research.preamble import patches
    sage: patches.install("vinberg")
    sage: "vinberg" in patches.installed()
    True
    sage: patches.uninstall("vinberg")
"""

from __future__ import annotations

import warnings
from typing import Any

from sage.rings.rational_field import QQ

from .. import vendor

_TARGET_ATTR = "vinberg_algorithm"


def _lattice_class() -> type:
    from sage.modules.free_quadratic_module_integer_symmetric import (
        FreeQuadraticModule_integer_symmetric,
    )

    return FreeQuadraticModule_integer_symmetric


def assert_vinberg_applicable(lattice: Any) -> tuple[int, int]:
    """Return the signature after checking that it is ``(n, 1)``.

    EXAMPLES::

        sage: from dzack_research.preamble import catalogue
        sage: from dzack_research.preamble.patches.vinberg import assert_vinberg_applicable
        sage: assert_vinberg_applicable(catalogue.U)
        (1, 1)
    """
    from sage.quadratic_forms.quadratic_form import QuadraticForm

    gram = lattice.gram_matrix()
    positive, negative, zero = QuadraticForm(
        QQ, gram.change_ring(QQ)
    ).signature_vector()

    assert zero == 0, f"lattice is degenerate: signature has {zero} zero direction(s)"
    assert negative == 1, (
        f"Vinberg's algorithm needs a hyperbolic lattice of signature (n, 1); "
        f"this one is ({positive}, {negative}). vinal's convention is one negative "
        f"direction with positive-definite orthogonal complement."
    )
    return positive, negative


def _tqdm_progress(total: int | None) -> tuple[Any, Any]:
    """Return a progress callback and its ``tqdm`` object."""
    from tqdm.auto import tqdm

    bar = tqdm(
        total=None if total is None else int(total),
        unit=" decomp",
        desc="Vinberg search",
        postfix={"roots": 0},
        leave=True,
    )

    def report(decompositions: int, roots: int) -> None:
        bar.n = int(decompositions)
        bar.set_postfix(roots=int(roots), refresh=False)
        bar.refresh()

    return report, bar


def vinberg_algorithm(
    self: Any,
    v0: Any = None,
    use_coxiter: bool = False,
    output: Any = None,
    max_roots: int | None = None,
    max_decompositions: int | None = None,
    verbose: bool = False,
) -> Any:
    """Enumerate roots with the vendored Vinberg algorithm.

    Set ``max_roots`` or ``max_decompositions`` to bound the search.
    """
    assert_vinberg_applicable(self)

    vendor.activate_clone("vinal", "src", "sage")
    from vinal import VinAl

    algorithm = VinAl(self.gram_matrix(), v0, use_coxiter, output)

    report, bar = _tqdm_progress(max_decompositions) if verbose else (None, None)
    try:
        complete = algorithm.FindRoots(
            max_roots=max_roots,
            max_decompositions=max_decompositions,
            progress=report,
        )
    finally:
        if bar is not None:
            bar.close()

    if not complete:
        warnings.warn(
            f"Vinberg search did not establish the fundamental polyhedron: "
            f"{len(algorithm.roots)} root(s) found, but finite covolume was never "
            f"confirmed. These are roots; that they are all of them is unproven. "
            f"For signature (n, 1) with n = 1 the criterion is unreachable in "
            f"principle (half-line in H^1, infinite volume, one face).",
            RuntimeWarning,
            stacklevel=2,
        )
    return algorithm.roots


def run_vin(lattice: Any, **kwargs: Any) -> Any:
    r"""Return a copy of ``lattice`` with enumerated roots and optional labels."""
    from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice

    twisted = lattice.signature_pair()[0] == 1
    source = lattice.twist(-1) if twisted else lattice
    roots = vinberg_algorithm(source, **kwargs)

    result = IntegralLattice(lattice.gram_matrix())
    result.roots = [-1 * root for root in roots] if twisted else list(roots)
    try:
        result._assign_names(lattice.variable_names())
        result.root_names = [
            result.to_lin_comb_generators(root) for root in result.roots
        ]
    except ValueError, AttributeError:
        result.root_names = None
    return result


def get_isotrop_type(lattice: Any, isotropic_vector: Any) -> str:
    r"""Classify an isotropic vector using the isometry type of $e^\perp/e$."""
    from .. import catalogue

    quotient = lattice.e_perp_mod_e(isotropic_vector)
    if quotient.is_isometric(catalogue.U):
        return "Odd"
    if quotient.is_isometric(catalogue.U_2):
        return "Even ordinary"
    if quotient.is_isometric(catalogue.IPQ(1, 1).twist(2)):
        return "Even characteristic"
    return "Not found."


def install() -> None:
    """Install ``vinberg_algorithm`` on Sage integral lattices."""
    target = _lattice_class()
    setattr(target, _TARGET_ATTR, vinberg_algorithm)
    assert hasattr(target, _TARGET_ATTR), (
        f"{target.__name__} did not accept the {_TARGET_ATTR} attribute"
    )
    assert getattr(target, _TARGET_ATTR) is vinberg_algorithm, (
        f"{target.__name__}.{_TARGET_ATTR} is not the function just installed"
    )


def uninstall() -> None:
    """Remove ``vinberg_algorithm`` from Sage integral lattices."""
    target = _lattice_class()
    if hasattr(target, _TARGET_ATTR):
        delattr(target, _TARGET_ATTR)
    assert not hasattr(target, _TARGET_ATTR), (
        f"{_TARGET_ATTR} survived removal from {target.__name__}"
    )
