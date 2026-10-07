#!/usr/bin/env python3
import subprocess
from pathlib import Path

from pandoc_config import expand_all

# Paths
DISS_ROOT = Path("/home/dzack/gitclones/diss")
COBLE_DIR = Path("/home/dzack/Coble-Paper")
BUILD_MD = DISS_ROOT / "build/dissertation.md"
STY_FILE = DISS_ROOT / "200-dev/thesis/src/latex_core/packages/DZG-Macros.sty"
BIB_FILE = DISS_ROOT / "200-dev/thesis/src/latex_core/Dissertation.bib"
OUT_FILE = COBLE_DIR / "references/thesis_standalone.md"


def main() -> None:
    print("1. Regenerating raw concatenated markdown...")
    subprocess.run(["python3", "200-dev/bin/build_diss.py"], cwd=str(DISS_ROOT))

    print("2. Expanding citations and macros...")
    with open(BUILD_MD) as f:
        text = f.read()

    text = expand_all(text, sty_file=STY_FILE, bib_file=BIB_FILE)

    print("3. Writing final output...")
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_FILE, "w") as f:
        f.write(text)

    print(f"Done! Created {OUT_FILE}")


if __name__ == "__main__":
    main()
