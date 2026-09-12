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
)


def test_repository_pytest_policy_replaces_the_custom_coxeter_runner() -> None:
    config = tomllib.loads(Path("pyproject.toml").read_text())
    options = config["tool"]["pytest"]["ini_options"]
    addopts = options["addopts"]

    assert "--timeout=90" in addopts
    assert "--durations=0" in addopts
    assert "--junit-xml=tests/.report/junit.xml" in addopts
    assert "--report-log=tests/.report/run.jsonl" in addopts
