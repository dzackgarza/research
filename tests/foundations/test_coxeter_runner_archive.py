r"""Retire the archived Coxeter-specific pytest wrapper.

The old runner translated a private argparse vocabulary into ``python -m pytest``
and printed a hand-maintained test summary.  The live repository uses pytest
directly, with repository-wide diagnostics configured in ``pyproject.toml``;
Coxeter mathematics remains in ordinary collected tests.
"""

import tomllib
from pathlib import Path

ARCHIVE_RECONCILIATIONS = (
    {
        "archive_module": "preamble/tests/coxeter_tdd_specs/run_tests.py",
        "live_owner": "pyproject.toml",
        "disposition": "reconciled-live-owner",
    },
    {
        "archive_module": "preamble/tests/coxeter_tdd_specs/fixtures/__init__.py",
        "live_owner": "tests/lattices/test_coxeter_literature.py",
        "disposition": "reconciled-live-owner",
    },
    {
        "archive_module": "preamble/tests/coxeter_tdd_specs/test_index.py",
        "live_owner": "tests/lattices/test_coxeter_literature.py",
        "disposition": "reconciled-live-owner",
    },
    {
        "archive_module": "preamble/tests/coxeter_tdd_specs/literature/tools/webpage_to_markdown.py",
        "live_owner": "archives/preamble/tests/coxeter_tdd_specs/literature",
        "disposition": "reconciled-live-owner",
    },
)


def test_repository_pytest_policy_replaces_the_custom_coxeter_runner() -> None:
    config = tomllib.loads(Path("pyproject.toml").read_text())
    options = config["tool"]["pytest"]["ini_options"]
    addopts = options["addopts"]

    assert "--timeout=90" in addopts
    assert "--durations=0" in addopts
    assert "--junit-xml=tests/.report/junit.xml" in addopts
    assert "--report-log=tests/.report/run.jsonl" in addopts


def test_vendored_coxeter_web_captures_retain_source_revision_metadata() -> None:
    literature = Path("archives/preamble/tests/coxeter_tdd_specs/literature")
    captures = tuple(sorted((literature / "wikipedia").glob("*.md"))) + tuple(
        sorted((literature / "wikiwand").glob("*.md"))
    )

    assert captures
    for capture in captures:
        header = "\n".join(capture.read_text().splitlines()[:8])
        assert "**Source**:" in header, capture
        assert "**Retrieved**:" in header, capture
        assert "**Citation Key**:" in header, capture
        assert "**Revision**:" in header, capture
