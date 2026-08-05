r"""Sage global-symbol import resolution with a persistent cache.

External tools that operate on lowered Python — linters, jedi, an LSP —
need import statements for Sage globals so the names resolve outside a
Sage session.  Sage answers through
``sage.misc.dev_tools.import_statements``, which is slow, so answers
persist in sqlite across processes.  This subsumes sage-lsp's symbols
cache.
"""

from __future__ import annotations

import sqlite3
from collections.abc import Iterable
from pathlib import Path

import sage.all
from sage.misc.dev_tools import import_statements

_DEFAULT_CACHE = (
    Path.home() / ".cache" / "dzack-research-preamble" / "sage-symbols.sqlite"
)
_SCHEMA = (
    "CREATE TABLE IF NOT EXISTS symbols "
    "(name TEXT PRIMARY KEY, statement TEXT NOT NULL)"
)


def _connect(cache_path: Path) -> sqlite3.Connection:
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(cache_path)
    connection.execute(_SCHEMA)
    return connection


def import_statement_for(
    name: str, cache_path: Path = _DEFAULT_CACHE
) -> str | None:
    r"""The import statement binding ``name`` in plain Python, or ``None``.

    ``None`` means the name is not a Sage global (or not an identifier);
    the caller decides whether that is an undefined-name diagnostic.
    """
    if not name.isidentifier():
        return None
    with _connect(cache_path) as connection:
        row = connection.execute(
            "SELECT statement FROM symbols WHERE name = ?", (name,)
        ).fetchone()
        if row is not None:
            return str(row[0])
        if not hasattr(sage.all, name):
            return None
        statement = str(
            import_statements(name, answer_as_str=True, verbose=False)
        )
        connection.execute(
            "INSERT OR REPLACE INTO symbols VALUES (?, ?)", (name, statement)
        )
        return statement


def synthetic_imports(
    names: Iterable[str], cache_path: Path = _DEFAULT_CACHE
) -> str:
    r"""Import statements for every resolvable name, one per line.

    Prepending this block to lowered Python lets resolution-based tools
    (pyflakes, jedi) see Sage globals; the line count is the offset a
    position mapper must subtract.
    """
    statements = [
        import_statement_for(name, cache_path) for name in sorted(set(names))
    ]
    return "\n".join(
        statement for statement in statements if statement is not None
    )
