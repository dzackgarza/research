"""The served docs site is not the render's working directory.

Quarto empties writing/.book/_site when a render starts. While nginx serves that
directory, every render -- a stopped one, a failed one, or a docs-lint of one page --
takes http://lattice-research.localhost/ down or replaces it with a partial site.
The deploy must publish a finished render to a separate directory and switch the
served link to it only after the gate passes.
"""

from __future__ import annotations

import os
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
RENDER_OUTPUT = REPO / "writing" / ".book" / "_site"
SERVED_LINK = Path("/var/www/static-sites/lattice-research")


def test_served_site_is_not_the_render_output():
    served = Path(os.path.realpath(SERVED_LINK))
    assert (served / "index.html").is_file(), f"{SERVED_LINK} -> {served} serves no index.html"
    assert served != RENDER_OUTPUT.resolve(), (
        f"{SERVED_LINK} points at the render output {RENDER_OUTPUT}; a render empties it")
