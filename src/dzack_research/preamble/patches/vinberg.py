r"""Attach ``vinberg_algorithm`` to Sage's integral-lattice class, via vendored vinal.

Ported from the old ``~/.sage/init.sage``, which did the same ``setattr`` at
startup after appending ``~/gitclones/vinal/src/sage`` to ``sys.path``. Two things
changed: the clone is vendored inside the repo (that ``gitclones`` path no longer
exists, so the original had been dead code), and applying the patch is now a
choice rather than a startup side effect.

Placement note, recorded rather than papered over: ``lexicon/INVENTORY.md`` names
``Cone``/``Fan`` as the *Vinberg workstream* in the lattice spike, still
undeclared. A root-enumeration algorithm's proper home is that workstream, on the
lattice object -- not bolted onto Sage's class from outside. This module is the
interim shim that keeps the old capability reachable; it is not the destination.
"""

from __future__ import annotations

import warnings
from typing import Any

from sage.rings.rational_field import QQ

from .. import vendor

#: The Sage class the old init.sage patched. A plain Python class, so it accepts
#: attribute assignment -- unlike the cython extension types the spike's
#: sage_patches subtree documents as unpatchable.
_TARGET_ATTR = "vinberg_algorithm"


def _lattice_class() -> type:
    from sage.modules.free_quadratic_module_integer_symmetric import (
        FreeQuadraticModule_integer_symmetric,
    )

    return FreeQuadraticModule_integer_symmetric


def assert_vinberg_applicable(lattice: Any) -> tuple[int, int]:
    """Reject input the algorithm cannot terminate on; return the signature pair.

    This does NOT decide whether the run will terminate. Vinberg's algorithm halts
    exactly when the reflection subgroup's fundamental polyhedron has finite volume,
    i.e. when the lattice is reflective, and it cannot report the negative case --
    it simply enumerates forever. vinal's own finite-covolume test
    (``src/sage/coxiter.py``, which asks CoxIter ``'Finite covolume'``) is that
    termination test, evaluated on the polyhedron accumulated so far, so it is not
    available in advance.

    What *is* cheap is the precondition, and it catches the failure that motivated
    this check -- calling the algorithm on ``U``:

    - **signature must be (n, 1)**: exactly one negative direction, matching vinal's
      requirement that ``<v0,v0> < 0`` with positive-definite orthogonal complement.
      vinal asserts this only after choosing ``v0``, and reports it as an opaque
      assertion rather than "this lattice is not hyperbolic".
    Rank 2 is deliberately NOT rejected. Signature (1,1) is hyperbolic 1-space,
    where the domain is a half-line and so has infinite volume, meaning the
    termination criterion can never fire -- but it has exactly ONE face, and that
    root is found immediately. Refusing the input would discard a real answer over
    an unreachable stopping condition. Bounded search plus a completeness flag is
    the honest treatment; see ``max_decompositions`` on :func:`vinberg_algorithm`.
    """
    from sage.quadratic_forms.quadratic_form import QuadraticForm

    gram = lattice.gram_matrix()
    positive, negative, zero = QuadraticForm(QQ, gram.change_ring(QQ)).signature_vector()

    assert zero == 0, f"lattice is degenerate: signature has {zero} zero direction(s)"
    assert negative == 1, (
        f"Vinberg's algorithm needs a hyperbolic lattice of signature (n, 1); "
        f"this one is ({positive}, {negative}). vinal's convention is one negative "
        f"direction with positive-definite orthogonal complement."
    )
    return positive, negative


def _tqdm_progress(total: int | None) -> tuple[Any, Any]:
    """Build a ``progress(decompositions, roots)`` callback and its closer.

    ``tqdm.auto`` is the notebook-aware entry point: it renders an ipywidgets bar
    inside a Jupyter kernel and a terminal bar outside, so one call site covers
    both. ipywidgets ships with this Sage.

    With ``total=None`` the display is a *counter*, not a bar -- deliberately. An
    unbounded search has no denominator, so a percentage would be invented. Pass
    ``max_decompositions`` and there is a real denominator, so a real bar.
    """
    from tqdm.auto import tqdm

    # Coerce at the boundary: Sage preparses integer literals to Integer, and tqdm
    # computes rates from them, producing Rationals it cannot format. tqdm is a
    # plain-Python consumer, so plain ints are what cross into it -- once, here.
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
    """Enumerate the roots of this lattice with vinal's Vinberg algorithm.

    Signature preserved from the old init.sage, including ``use_coxiter``, which
    routes vinal to the external CoxIter binary. ``max_roots`` and
    ``max_decompositions`` bound the search (fork-only parameters).

    The roots are returned either way. When the fundamental polyhedron did not
    close -- because a bound stopped the search, or because the criterion is
    unreachable for this lattice -- a warning says so, naming what is and is not
    established. The roots found are still genuine roots; what is unproven is that
    they are *all* of them.
    """
    assert_vinberg_applicable(self)

    vendor.activate_clone("vinal", "src", "sage")
    from vinal import VinAl

    # output is passed through untouched: vinal treats None as quiet, which is how
    # its own tests call it. The old init.sage substituted sys.stdout for None,
    # which made the method unsilenceably noisy.
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
    r"""Enumerate roots, twisting to the convention vinal needs, and label them.

    Ported from old lines 943-960. **The source had a typo that disabled half of it:**
    it set ``do_twist = True`` but tested ``if doTwist:`` -- two different names, with
    ``doTwist`` initialised ``False`` and never reassigned. So the negation branch
    could never run, and a lattice that *was* twisted came back with un-negated roots.
    Fixed here; one name is used throughout.

    Returns a copy of the lattice carrying ``.roots`` and, when names are assigned,
    ``.root_names``.
    """
    from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice

    twisted = lattice.signature_pair()[0] == 1
    source = lattice.twist(-1) if twisted else lattice
    roots = vinberg_algorithm(source, **kwargs)

    result = IntegralLattice(lattice.gram_matrix())
    result.roots = [-1 * root for root in roots] if twisted else list(roots)
    try:
        result._assign_names(lattice.variable_names())
        result.root_names = [result.to_lin_comb_generators(root) for root in result.roots]
    except ValueError, AttributeError:
        # No names on the input lattice, or lattice_methods not installed: the roots
        # are still returned, just unlabelled.
        result.root_names = None
    return result


def get_isotrop_type(lattice: Any, isotropic_vector: Any) -> str:
    r"""Classify an isotropic vector by the isometry type of $e^{\perp}/e$'s complement.

    Ported from old lines 111-121 with one change forced by types. The source wrote::

        S_bar = L.e_perp_mod_e(v)
        compl = L.orthogonal_complement(S_bar)

    but ``e_perp_mod_e`` returns a *quotient*, which is not a sublattice of ``L``, so
    ``orthogonal_complement`` cannot take it -- that composition is ill-typed and the
    function could never have run. The classification it wants is of $e^{\perp}/e$
    itself, against the three cases the source lists, so that is what is compared.
    """
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
    """Attach the method. Asserts the class really took it."""
    target = _lattice_class()
    setattr(target, _TARGET_ATTR, vinberg_algorithm)
    assert hasattr(target, _TARGET_ATTR), f"{target.__name__} did not accept the {_TARGET_ATTR} attribute"
    assert getattr(target, _TARGET_ATTR) is vinberg_algorithm, f"{target.__name__}.{_TARGET_ATTR} is not the function just installed"


def uninstall() -> None:
    """Detach the method, leaving the class as Sage shipped it."""
    target = _lattice_class()
    if hasattr(target, _TARGET_ATTR):
        delattr(target, _TARGET_ATTR)
    assert not hasattr(target, _TARGET_ATTR), f"{_TARGET_ATTR} survived removal from {target.__name__}"
