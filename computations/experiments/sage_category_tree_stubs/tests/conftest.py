"""Session hooks: keep the served SVG viewer in sync with the DOT."""

from __future__ import annotations

from sage_category_tree_stubs.viz import rebuild_viewer


def pytest_sessionstart(session: object) -> None:
    """Any pytest run regenerates category_parent_graph.svg from the DOT."""
    del session
    rebuild_viewer()
