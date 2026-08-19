import json
import os
import time
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, cast

import pytest

_TIMING_ENV_VAR = "COBLE_RESEARCH_TEST_TIMING_DIR"
_SESSION_STARTED_AT = 0.0
_SESSION_REPORTS: dict[str, dict[str, Any]] = {}
_SESSION_DESELECTED = 0
_SESSION_COLLECTED = 0
_SESSION_SELECTED = 0


def _timing_root() -> Path:
    configured = os.environ.get(_TIMING_ENV_VAR)
    if configured:
        return Path(configured)
    return Path(__file__).resolve().parents[1] / ".cache" / "test_timings"


def _utc_timestamp(epoch_seconds: float) -> str:
    return (
        datetime.fromtimestamp(epoch_seconds, tz=UTC)
        .isoformat(timespec="seconds")
        .replace("+00:00", "Z")
    )


def _append_jsonl(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        json.dump(payload, handle, sort_keys=True)
        handle.write("\n")


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--run-slow", action="store_true", default=False, help="run slow tests (>2 min)"
    )


def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line(
        "markers", "slow: marks tests that take more than 2 minutes"
    )


def pytest_sessionstart(session: pytest.Session) -> None:
    global _SESSION_STARTED_AT, _SESSION_REPORTS, _SESSION_DESELECTED
    global _SESSION_COLLECTED, _SESSION_SELECTED
    _SESSION_STARTED_AT = time.time()
    _SESSION_REPORTS = {}
    _SESSION_DESELECTED = 0
    _SESSION_COLLECTED = 0
    _SESSION_SELECTED = 0


def pytest_collection_finish(session: pytest.Session) -> None:
    global _SESSION_COLLECTED, _SESSION_SELECTED
    _SESSION_COLLECTED = session.testscollected
    _SESSION_SELECTED = len(session.items)


def pytest_deselected(items: list[pytest.Item]) -> None:
    global _SESSION_DESELECTED
    _SESSION_DESELECTED += len(items)


def pytest_collection_modifyitems(
    config: pytest.Config, items: list[pytest.Item]
) -> None:
    if config.getoption("--run-slow"):
        return
    skip_slow = pytest.mark.skip(reason="skipped by default; use --run-slow to enable")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)


def pytest_runtest_logreport(report: pytest.TestReport) -> None:
    node_report = _SESSION_REPORTS.setdefault(report.nodeid, {"nodeid": report.nodeid})
    node_report[f"{report.when}_seconds"] = report.duration
    phase_outcomes = node_report.setdefault("phase_outcomes", {})
    phase_outcomes[report.when] = report.outcome
    if report.outcome == "failed":
        node_report["outcome"] = "failed"
    elif report.outcome == "skipped" and "outcome" not in node_report:
        node_report["outcome"] = "skipped"
    elif report.when == "call" and "outcome" not in node_report:
        node_report["outcome"] = report.outcome


def pytest_sessionfinish(session: pytest.Session, exitstatus: int) -> None:
    finished_at = time.time()
    records: list[dict[str, Any]] = []
    for report in _SESSION_REPORTS.values():
        setup_seconds = float(report.get("setup_seconds", 0.0))
        call_seconds = float(report.get("call_seconds", 0.0))
        teardown_seconds = float(report.get("teardown_seconds", 0.0))
        records.append(
            {
                "nodeid": report["nodeid"],
                "outcome": report.get("outcome", "passed"),
                "phase_outcomes": report.get("phase_outcomes", {}),
                "setup_seconds": setup_seconds,
                "call_seconds": call_seconds,
                "teardown_seconds": teardown_seconds,
                "total_seconds": setup_seconds + call_seconds + teardown_seconds,
            }
        )
    records.sort(key=lambda record: (-record["total_seconds"], record["nodeid"]))
    timing_root = _timing_root()
    session_dir = timing_root / "pytest_sessions"
    session_dir.mkdir(parents=True, exist_ok=True)
    session_stamp = (
        _utc_timestamp(_SESSION_STARTED_AT)
        .replace(":", "")
        .replace(
            "-",
            "",
        )
    )
    session_path = session_dir / f"{session_stamp}_{os.getpid()}.json"
    session_payload = {
        "started_at": _utc_timestamp(_SESSION_STARTED_AT),
        "finished_at": _utc_timestamp(finished_at),
        "wall_seconds": finished_at - _SESSION_STARTED_AT,
        "exitstatus": exitstatus,
        "args": list(session.config.invocation_params.args),
        "collected_count": _SESSION_COLLECTED,
        "selected_count": _SESSION_SELECTED,
        "deselected_count": _SESSION_DESELECTED,
        "slow_enabled": bool(session.config.getoption("--run-slow")),
        "records": records,
    }
    session_path.write_text(
        json.dumps(session_payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    latest_path = timing_root / "latest.json"
    latest_path.write_text(
        json.dumps(session_payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    history_entry = {
        "started_at": session_payload["started_at"],
        "finished_at": session_payload["finished_at"],
        "wall_seconds": session_payload["wall_seconds"],
        "exitstatus": exitstatus,
        "args": session_payload["args"],
        "collected_count": _SESSION_COLLECTED,
        "selected_count": _SESSION_SELECTED,
        "deselected_count": _SESSION_DESELECTED,
        "slow_enabled": session_payload["slow_enabled"],
        "session_file": str(session_path),
        "slowest": [
            {"nodeid": record["nodeid"], "total_seconds": record["total_seconds"]}
            for record in records[:20]
        ],
    }
    history_path = timing_root / "history.jsonl"
    _append_jsonl(history_path, history_entry)
    config_storage = cast(Any, session.config)
    config_storage._timing_session_path = session_path
    config_storage._timing_history_path = history_path


def pytest_terminal_summary(
    terminalreporter: pytest.TerminalReporter, exitstatus: int, config: pytest.Config
) -> None:
    config_storage = cast(Any, config)
    session_path = getattr(config_storage, "_timing_session_path", None)
    history_path = getattr(config_storage, "_timing_history_path", None)
    if session_path is not None and history_path is not None:
        terminalreporter.write_sep(
            "-",
            f"timing log: session={session_path} history={history_path}",
        )
