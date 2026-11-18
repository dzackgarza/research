#!/usr/bin/env python3
"""Stage the figures the book's prose references.

The figures are authored and rendered in the shared pandoc-config repo, which this
machine reaches as ~/.pandoc and CI clones to $HOME/.pandoc. They are not copied into
this repo, so the book has to collect them at build time the same way it collects the
bibliography and the MathJax macros.

A page writes `![...](/rendered/fig_x.svg)`. The leading slash makes the path relative
to the project root, so one `rendered/` beside the project file serves every chapter,
whatever directory the chapter sits in.

Only the referenced files are staged: the source tree is 52 MB of figures and PDFs for
every document on this machine, and the site should carry the thirty-odd this book
cites. A reference with no file is an error here rather than a broken image later.
"""
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

PROSE = Path("writing")
STAGE = PROSE / ".book" / "rendered"
SOURCE = Path(os.path.expanduser(os.environ.get("PANDOC_DIR", "~/.pandoc"))) / "figures" / "rendered"
FIGURES = SOURCE.parent
DEPOSITED = PROSE / "coble" / "papers" / "AE22"

if not SOURCE.is_dir():
    sys.exit(f"docs-figures: {SOURCE} is missing — is the pandoc-config clone in place?")

wanted = set()
for md in PROSE.rglob("*.md"):
    if "_site" in md.parts:
        continue
    wanted |= set(re.findall(r"\]\(/rendered/([^)\s]+)", md.read_text(encoding="utf-8", errors="replace")))

def source_for(name):
    """Resolve exact authored assets, never similarly named substitutes."""
    for path in (SOURCE / name, FIGURES / "raster" / "dissertation" / name,
                 FIGURES / "raster" / name):
        if path.is_file():
            return path
    if name in {"fig-pumpkin.png", "fig-pumpkin2.png"}:
        path = DEPOSITED / (Path(name).stem + ".pdf")
        return path if path.is_file() else None
    return None


sources = {name: source_for(name) for name in wanted}
missing = sorted(name for name, path in sources.items() if path is None)
if missing:
    sys.exit("docs-figures: the prose cites figures that do not exist in "
             f"{SOURCE}:\n" + "\n".join(f"  - {n}" for n in missing))

STAGE.mkdir(parents=True, exist_ok=True)
for name in sorted(wanted):
    source = sources[name]
    if source.suffix == ".pdf" and name.endswith(".png"):
        subprocess.run(["pdftoppm", "-f", "1", "-singlefile", "-png", "-r", "150",
                        str(source), str((STAGE / name).with_suffix(""))], check=True)
    else:
        shutil.copyfile(source, STAGE / name)
for stale in STAGE.iterdir():
    if stale.name not in wanted:
        stale.unlink()
print(f"docs-figures: staged {len(wanted)} figures into {STAGE}")
