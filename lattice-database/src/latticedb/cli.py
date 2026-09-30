"""Command line of the lattice database: validate the corpus, build the site, deploy it."""

import sys
from pathlib import Path
from typing import Annotated
from urllib.request import Request, urlopen

from cyclopts import App, Parameter

from latticedb import corpus, site

SERVED = Path("/var/www/static-sites/lattice-database")
ADDRESS = "http://127.0.0.1/"
HOST = "lattice-database.localhost"

app = App(name="latticedb", help=__doc__)

Root = Annotated[Path, Parameter(help="Directory that holds `lattices/` and `pages/`.")]


@app.command
def check(root: Root = Path()) -> None:
    """Validate every record of the corpus. Prints each problem and exits with status 1 when a record is not well defined."""
    try:
        entries = corpus.load(root / "lattices")
    except corpus.CorpusInvalid as invalid:
        print("\n".join(invalid.problems), file=sys.stderr)
        print(f"{len(invalid.problems)} problems", file=sys.stderr)
        sys.exit(1)
    print(f"{len(entries)} lattices, all records valid")


@app.command
def build(root: Root = Path(), target: Annotated[Path, Parameter(help="Directory for the site. The command replaces it.")] = Path("_site")) -> None:
    """Build the site from the corpus."""
    count = site.build(root, target)
    print(f"{count} lattices -> {target}")


@app.command
def deploy(root: Root = Path()) -> None:
    """Build the site, link it into the directory that nginx serves, and check that nginx serves it."""
    target = (root / "_site").resolve()
    site.build(root, target)
    if not SERVED.is_symlink():
        SERVED.symlink_to(target)
    assert SERVED.resolve() == target, f"{SERVED} links to {SERVED.resolve()}, not to {target}"
    with urlopen(Request(ADDRESS, headers={"Host": HOST})) as response:
        assert response.status == 200, f"{ADDRESS} with host {HOST} returned {response.status}"
    print(f"http://{HOST}/")


@app.command
def next_tag(root: Root = Path()) -> None:
    """Print the tag for the next new record."""
    print(corpus.next_tag(corpus.load(root / "lattices")))
