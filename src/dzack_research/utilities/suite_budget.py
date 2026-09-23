"""The test suite's time gates.

Loaded as a pytest plugin (``-p dzack_research.utilities.suite_budget`` in
``pyproject.toml``).  Three limits, each a red run when exceeded:

- **Star import.**  ``from dzack_research.preamble.all import *`` has
  ``STAR_IMPORT_CEILING`` seconds.  Sage's own ``sage.all`` is imported first
  and not counted, so the ceiling measures what the preamble adds.  Timed
  before the conftests load, since ``tests/conftest.py`` performs the import.
- **Collection.**  Collecting the tests has ``COLLECTION_CEILING`` seconds.
- **Execution.**  The session deadline of pytest-timeout is set to
  ``PER_TEST_BUDGET`` times the number of selected tests, counted from the end
  of collection; pytest-timeout checks it after every test.

A run over any limit is a defect in the code or the tests, never a wait:
find the cost, do not raise the limit.
"""

import time

import pytest
from pytest_timeout import SESSION_EXPIRE_KEY, SESSION_TIMEOUT_KEY

STAR_IMPORT_CEILING = 2.0
COLLECTION_CEILING = 30.0
PER_TEST_BUDGET = 0.1

_STAR_IMPORT_SECONDS = pytest.StashKey[float]()
_COLLECTION_START = pytest.StashKey[float]()


@pytest.hookimpl(tryfirst=True)
def pytest_load_initial_conftests(early_config: pytest.Config) -> None:
    import sage.all  # noqa: F401  (Sage's own load, which the ceiling excludes)

    start = time.perf_counter()
    import dzack_research.preamble.all  # noqa: F401

    early_config.stash[_STAR_IMPORT_SECONDS] = time.perf_counter() - start


def pytest_sessionstart(session: pytest.Session) -> None:
    star_import = session.config.stash[_STAR_IMPORT_SECONDS]
    if star_import > STAR_IMPORT_CEILING:
        pytest.exit(
            f"preamble star import took {star_import:.2f} s; the ceiling is {STAR_IMPORT_CEILING:.0f} s",
            returncode=pytest.ExitCode.TESTS_FAILED,
        )
    session.config.stash[_COLLECTION_START] = time.perf_counter()


@pytest.hookimpl(trylast=True)
def pytest_collection_finish(session: pytest.Session) -> None:
    collection = time.perf_counter() - session.config.stash[_COLLECTION_START]
    if collection > COLLECTION_CEILING:
        pytest.exit(
            f"collection took {collection:.1f} s; the ceiling is {COLLECTION_CEILING:.0f} s",
            returncode=pytest.ExitCode.TESTS_FAILED,
        )
    budget = PER_TEST_BUDGET * len(session.items)
    session.config.stash[SESSION_TIMEOUT_KEY] = budget
    session.config.stash[SESSION_EXPIRE_KEY] = time.time() + budget


def pytest_report_header(config: pytest.Config) -> str:
    return (
        f"time gates: star import {config.stash[_STAR_IMPORT_SECONDS]:.2f} s "
        f"(ceiling {STAR_IMPORT_CEILING:.0f} s), collection ceiling {COLLECTION_CEILING:.0f} s, "
        f"{PER_TEST_BUDGET * 1000:.0f} ms per selected test"
    )
