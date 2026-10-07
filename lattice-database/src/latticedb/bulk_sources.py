"""Store the catalogue's published tables of individual quadratic forms."""

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import urlopen

CATALOGUE = "https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES"

NIPP_QUATERNARY = ("d4to457.html", *(f"d{end}.html" for end in (641, 777, 893, 992, 1080, 1161, 1236, 1308, 1373, 1433, 1492, 1549, 1604, 1656, 1705, 1732)))
NIPP_QUINARY = tuple(f"tbl.{end}.html" for end in (256, 270, 300, 322, 345, 400, 440, 480, 500, 513))
SOURCE_FILES = (
    *((f"nipp/{name}", name) for name in (*NIPP_QUATERNARY, *NIPP_QUINARY)),
    ("brandt_intrau/Brandt_1.html", "Brandt_1.html"),
    ("brandt_intrau/Brandt_2.html", "Brandt_2.html"),
    ("watson/watson.txt", "Classi/watson"),
)


def _fetch(root: Path, local: str, remote: str) -> str:
    path = root / "sources" / local
    if path.exists():
        return local
    with urlopen(f"{CATALOGUE}/{remote}", timeout=60) as response:
        content = response.read()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
    return local


def fetch(root: Path) -> list[str]:
    """Store each published bulk source file under its source-specific directory."""
    with ThreadPoolExecutor(max_workers=6) as pool:
        return list(pool.map(lambda item: _fetch(root, *item), SOURCE_FILES))
