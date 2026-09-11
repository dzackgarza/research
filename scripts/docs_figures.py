#!/usr/bin/env python3
"""Stage the figures the book's prose references.

The figures are authored and rendered in the shared pandoc-config repo, which this
machine reaches as ~/.pandoc and CI clones to $HOME/.pandoc. They are not copied into
this repo, so the book has to collect them at build time the same way it collects the
bibliography and the MathJax macros.

Every chapter is symlinked flat into writing/.book, so pandoc runs with its working
directory there for all of them and one `rendered/` beside the project file serves the
whole book. A page writes `![...](rendered/fig_x.svg)` and means that directory.

Only the referenced files are staged: the source tree is 52 MB of figures and PDFs for
every document on this machine, and the site should carry the thirty-odd this book
cites. A reference with no file is an error here rather than a broken image later.
"""
import os
import re
import shutil
import sys
from pathlib import Path

PROSE = Path("writing")
STAGE = PROSE / ".book" / "rendered"
SOURCE = Path(os.path.expanduser(os.environ.get("PANDOC_DIR", "~/.pandoc"))) / "figures" / "rendered"

if not SOURCE.is_dir():
    sys.exit(f"docs-figures: {SOURCE} is missing — is the pandoc-config clone in place?")

wanted = set()
for md in PROSE.rglob("*.md"):
    if "_site" in md.parts:
        continue
    wanted |= set(re.findall(r"\]\(rendered/([^)\s]+)", md.read_text(encoding="utf-8", errors="replace")))

missing = sorted(n for n in wanted if not (SOURCE / n).is_file())
if missing:
    sys.exit("docs-figures: the prose cites figures that do not exist in "
             f"{SOURCE}:\n" + "\n".join(f"  - {n}" for n in missing))

STAGE.mkdir(parents=True, exist_ok=True)
for name in sorted(wanted):
    shutil.copyfile(SOURCE / name, STAGE / name)
for stale in STAGE.iterdir():
    if stale.name not in wanted:
        stale.unlink()
print(f"docs-figures: staged {len(wanted)} figures into {STAGE}")
