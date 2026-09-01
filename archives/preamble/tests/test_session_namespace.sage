r"""The session's names mean the owned objects, and go on meaning them.

``dzack_research.preamble.all`` is the preamble's ``sage.all``: importing it
is what makes a scope a session.  What that has to be worth is that
:math:`\ZZ` in such a scope is the ring the preamble builds over, so
``ZZ^3`` is the owned free module -- and that it stays so, which is the part
a caller used to have to maintain by hand.
"""

import pytest

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.rings.rings import engine_ring


@pytest.fixture
def session() -> dict:
    r"""A scope with the one import a session makes, and nothing else."""
    scope: dict = {}
    exec("from dzack_research.preamble.all import *", scope)
    return scope


def test_a_session_ring_is_the_ring_and_not_the_engine(session: dict) -> None:
    r"""``ZZ^n`` is the owned free module, so ``ZZ`` is the owned ring.

    Asserted on what the name *does*, not on what it is: the engine's
    :math:`\ZZ` answers ``ZZ^3`` with Sage's free module, and the whole point
    of the owned view is that a session's does not.  The engine is still
    reachable underneath, which is what ``engine_ring`` is for -- a matrix
    built over the wrapper would be a generic one.
    """
    ring = session["ZZ"]

    assert engine_ring(ring) is SageZZ, "the owned ring is a view of the engine's"
    assert ring is not SageZZ, "a session's ZZ is the view, not the engine"

    module = ring ** 3
    assert module.base_ring() is ring
    assert module.module_generating_set().cardinality() == 3
    assert module is not SageZZ ** 3, (
        "ZZ^3 in a session is the preamble's free module, not Sage's"
    )


def test_a_lattice_from_the_session_namespace_answers_for_itself(
    session: dict,
) -> None:
    r"""$A_2$ built through the session's names has its form and its category."""
    lattice = session["Lattices"]("A", 2)
    generators = tuple(lattice.module_generators())

    assert lattice.rank() == 2
    assert lattice.base_ring() is session["ZZ"]
    assert lattice.is_even() and lattice.is_nondegenerate()
    assert lattice.gram_matrix().determinant() == 3
    assert abs(generators[0].b(generators[1])) == 1


def test_loading_a_script_leaves_the_session_rings_owned(
    session: dict, tmp_path
) -> None:
    r"""A ``load()`` does not put the engine's rings back under the session's names.

    Sage's own ``load`` runs the script in the scope it is given, and a script
    that imports Sage's namespace rebinds ``ZZ`` there -- so ``ZZ^3`` would
    mean the preamble's free module before that line and Sage's after it.
    The ``load`` this session holds is the one that closes that: the property
    is the module, not the name.
    """
    script = tmp_path / "imports_sage.sage"
    script.write_text("from sage.all import *\nran = 1\n")
    before = session["ZZ"] ** 3

    session["load"](str(script), session)

    assert session["ran"] == 1, "the script has to actually run"
    assert session["ZZ"] ** 3 is before, "ZZ^3 means the same module after the load"
    assert engine_ring(session["ZZ"]) is SageZZ
