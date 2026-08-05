r"""Behavioral proofs for the Sage symbol-import resolver."""

import sqlite3
from pathlib import Path

from dzack_research.preamble.symbols import import_statement_for, synthetic_imports


def test_known_symbols_resolve_to_their_defining_modules(tmp_path: Path) -> None:
    cache = tmp_path / "symbols.sqlite"

    assert (
        import_statement_for("QQ", cache)
        == "from sage.rings.rational_field import QQ"
    )
    assert (
        import_statement_for("PolynomialRing", cache)
        == "from sage.rings.polynomial.polynomial_ring_constructor"
        " import PolynomialRing"
    )
    assert (
        import_statement_for("matrix", cache)
        == "from sage.matrix.constructor import matrix"
    )


def test_non_sage_names_resolve_to_none(tmp_path: Path) -> None:
    cache = tmp_path / "symbols.sqlite"

    assert import_statement_for("definitely_not_a_sage_global", cache) is None
    assert import_statement_for("not an identifier", cache) is None


def test_cache_is_the_source_of_truth_on_a_hit(tmp_path: Path) -> None:
    cache = tmp_path / "symbols.sqlite"
    live = import_statement_for("QQ", cache)
    assert live == "from sage.rings.rational_field import QQ"

    # Overwrite the stored row; a repeated lookup must serve the stored
    # value, proving the second call never re-derives from Sage.
    sentinel = "from sentinel.module import QQ"
    with sqlite3.connect(cache) as connection:
        connection.execute(
            "UPDATE symbols SET statement = ? WHERE name = 'QQ'", (sentinel,)
        )

    assert import_statement_for("QQ", cache) == sentinel


def test_synthetic_imports_joins_resolvable_names_and_skips_the_rest(
    tmp_path: Path,
) -> None:
    cache = tmp_path / "symbols.sqlite"

    block = synthetic_imports(["matrix", "no_such_sage_name", "QQ"], cache)

    assert block == (
        "from sage.rings.rational_field import QQ\n"
        "from sage.matrix.constructor import matrix"
    )
