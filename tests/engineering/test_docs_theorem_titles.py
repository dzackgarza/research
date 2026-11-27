"""Every numbered block title must parse as inline Markdown."""

import json
import re
import subprocess
from pathlib import Path


PAGE = Path(__file__).resolve().parents[2] / "writing/coble/compactifications/toroidal-and-semitoroidal.md"


def test_numbered_block_titles_parse_as_inlines():
    for line_number, line in enumerate(PAGE.read_text().splitlines(), 1):
        match = re.search(r'title="(.*)"\}', line)
        if match is None:
            continue
        document = subprocess.run(
            ["pandoc", "--from=markdown", "--to=json"],
            input=match.group(1),
            text=True,
            capture_output=True,
            check=True,
        )
        blocks = json.loads(document.stdout)["blocks"]
        assert len(blocks) == 1 and blocks[0]["t"] in {"Para", "Plain"}, line_number
