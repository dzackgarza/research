r"""Record how long the suite spends, and on what, every time it runs.

The suite's cost is not where a test list suggests.  Loading the preamble
takes minutes and each test process pays it once, so a per-test table alone
reads as "one test is slow" when the truth is "importing the module is
slow".  Both numbers are recorded here: module collection, which is where
``load(install.sage)`` lands, and the call phase of each test, which is the
mathematics.

Written to ``tests/timings.jsonl``, one JSON object per run, appended.  It
is a log rather than a source file -- committing a new line per run would
bury real diffs -- so it is ignored by git and read by comparing runs.
"""

from __future__ import annotations

import json
import os
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

import pytest

_LOG = Path(__file__).resolve().parent / "timings.jsonl"

_collections: dict[str, float] = {}
_collection_started: dict[str, float] = {}
_tests: dict[str, float] = {}
_started = time.time()


def _commit() -> str:
    r"""Return the commit the timings belong to, so runs stay comparable."""
    try:
        return subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=Path(__file__).resolve().parent,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
    except (subprocess.CalledProcessError, OSError):
        return "unknown"


def pytest_collectstart(collector: pytest.Collector) -> None:
    _collection_started[collector.nodeid] = time.time()


@pytest.hookimpl(trylast=True)
def pytest_collectreport(report: pytest.CollectReport) -> None:
    r"""Record module collection: importing a .sage test loads the preamble.

    Timed here rather than read off the report, which carries no duration
    for collection.
    """
    start = _collection_started.pop(report.nodeid, None)
    if start is not None:
        _collections[report.nodeid or "<session>"] = time.time() - start


@pytest.hookimpl(trylast=True)
def pytest_runtest_logreport(report: pytest.TestReport) -> None:
    if report.when == "call":
        _tests[report.nodeid] = report.duration


def pytest_sessionfinish(session: pytest.Session, exitstatus: int) -> None:
    record = {
        "at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "commit": _commit(),
        "exitstatus": int(exitstatus),
        "wall_seconds": round(time.time() - _started, 2),
        "collection_seconds": {
            name: round(seconds, 2)
            for name, seconds in sorted(
                _collections.items(), key=lambda item: -item[1]
            )
            if seconds >= 0.5
        },
        "test_seconds": {
            name: round(seconds, 2)
            for name, seconds in sorted(_tests.items(), key=lambda item: -item[1])
            if seconds >= 0.5
        },
        "tests_run": len(_tests),
    }
    with _LOG.open("a", encoding="utf-8") as log:
        log.write(json.dumps(record) + "\n")

    terminal = session.config.pluginmanager.get_plugin("terminalreporter")
    if terminal is not None and not os.environ.get("PYTEST_XDIST_WORKER"):
        collected = sum(record["collection_seconds"].values())
        ran = sum(record["test_seconds"].values())
        terminal.write_line(
            f"timings: {record['wall_seconds']}s wall, {collected}s importing "
            f"test modules, {ran}s in tests -> {_LOG.name}"
        )
