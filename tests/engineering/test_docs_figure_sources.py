"""The book's figure staging must use actual source bytes, never placeholders."""

import os
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
STAGER = ROOT / "scripts" / "docs_figures.py"


def test_deposited_pdf_and_shared_raster_are_staged(tmp_path):
    prose = tmp_path / "writing"
    deposit = prose / "coble" / "papers" / "AE22"
    deposit.mkdir(parents=True)
    (prose / ".book").mkdir()
    shutil.copyfile(ROOT / "writing/coble/papers/AE22/fig-pumpkin.pdf",
                    deposit / "fig-pumpkin.pdf")
    shared = tmp_path / "pandoc" / "figures" / "raster" / "dissertation"
    shared.mkdir(parents=True)
    (shared.parent.parent / "rendered").mkdir()
    source = ROOT / "writing" / "coble" / "papers" / "AE22" / "fig-pumpkin.pdf"
    assert source.read_bytes().startswith(b"%PDF-")
    (shared / "exact.jpg").write_bytes(b"\xff\xd8\xff\xd9")
    (prose / "page.md").write_text(
        "![](/rendered/fig-pumpkin.png)\n![](/rendered/exact.jpg)\n"
    )
    run = subprocess.run(
        [sys.executable, str(STAGER)], cwd=tmp_path,
        env={**os.environ, "PANDOC_DIR": str(tmp_path / "pandoc")},
        capture_output=True, text=True, check=True,
    )
    assert "staged 2 figures" in run.stdout
    assert (prose / ".book/rendered/fig-pumpkin.png").read_bytes().startswith(
        b"\x89PNG\r\n\x1a\n"
    )
    assert (prose / ".book/rendered/exact.jpg").read_bytes() == b"\xff\xd8\xff\xd9"


def test_lfs_pointer_is_not_staged_as_an_image(tmp_path):
    prose = tmp_path / "writing"
    prose.mkdir()
    (prose / "page.md").write_text("![](/rendered/missing.png)\n")
    shared = tmp_path / "pandoc" / "figures" / "rendered"
    shared.mkdir(parents=True)
    (shared / "missing.png").write_text(
        "version https://git-lfs.github.com/spec/v1\n"
        "oid sha256:" + "0" * 64 + "\nsize 100\n"
    )
    run = subprocess.run(
        [sys.executable, str(STAGER)], cwd=tmp_path,
        env={**os.environ, "PANDOC_DIR": str(tmp_path / "pandoc")},
        capture_output=True, text=True,
    )
    assert run.returncode != 0
    assert "unresolved Git LFS pointer" in run.stderr
    assert not (prose / ".book/rendered/missing.png").exists()
