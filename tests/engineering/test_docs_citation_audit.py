"""The audit of citations that name no result, run by scripts/docs_citation_audit.py.

The script is run as `just docs-citation-audit` runs it, on a one-chapter fixture
project; the assertions read the Markdown report.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[2] / "scripts" / "docs_citation_audit.py"

CONFIG = "book:\n  chapters:\n    - one.md\n"

ONE = """\
Running prose summarizes [@Vin75], and @Nik80 classified the forms.

::: {.lemma #lem:a}
Every $a$ is $b$ ([@AEGS25], Definition 3.6).
:::

::: {.proof}
The reduction is [@Ale22, §3]. By [@AEGS25, Lem. 3.9] it ends.
:::
"""


def test_report_lists_each_loose_citation_with_its_place(tmp_path):
    (tmp_path / "_quarto.yml").write_text(CONFIG)
    (tmp_path / "one.md").write_text(ONE)
    out = tmp_path / "audit.md"
    subprocess.run(["uv", "run", "--script", str(SCRIPT), "--project", str(tmp_path),
                    "--out", str(out)], check=True, capture_output=True, timeout=300)
    report = out.read_text()
    # A result named after the brackets is a mechanical fix.
    assert ("`one.md:4` lemma lem:a (statement): `[@AEGS25]` then \"Definition 3.6\" "
            "→ `[@AEGS25, Definition 3.6]`") in report
    # Loose citations in a proof, in prose and in narrative form, each with its sentence.
    assert "- `one.md:8` proof of lemma lem:a: `[@Ale22, §3]`\n\n  > The reduction is [@Ale22, §3]." in report
    assert "- `one.md:1` prose: `[@Vin75]`" in report
    assert "- `one.md:1` prose: `[@Nik80]`" in report
    # A citation that names a result is not listed.
    assert "Lem. 3.9" not in report
