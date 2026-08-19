from __future__ import annotations

from pathlib import Path
import re


# The specification and the conformance corpus were separated when this material
# was migrated into the research repository. The specification lives here; the
# engine conformance suites live under computations/scripts/conformance_lattice_engines/.
SPECIFICATION_DIR = Path(__file__).resolve().parent
REPO_ROOT = SPECIFICATION_DIR.parents[2]
CONFORMANCE_DIR = REPO_ROOT / "computations" / "scripts" / "conformance_lattice_engines"

MARKER_PATTERN = re.compile(
    r"(?m)^\s*(?:@pytest\.mark\.tdd_red|pytestmark\s*=\s*pytest\.mark\.tdd_red)\s*$"
)


def test_tdd_red_marker_scope_is_the_specification_only():
    """
    Policy contract:
    the tdd_red marker states that a test asserts an interface the repository
    does not yet provide. It is reserved for the specification in this
    directory and must never appear in a conformance suite, where a passing
    test is a fact about an engine rather than an unmet obligation.
    """
    offenders: list[str] = []
    for pyfile in sorted(CONFORMANCE_DIR.rglob("*.py")):
        if MARKER_PATTERN.search(pyfile.read_text(encoding="utf-8")) is None:
            continue
        offenders.append(str(pyfile.relative_to(REPO_ROOT)))

    assert not offenders, (
        "tdd_red marker is out of allowed scope. "
        f"Allowed scope: {SPECIFICATION_DIR.relative_to(REPO_ROOT)}\n"
        f"Found in: {offenders}"
    )


def test_the_specification_actually_carries_red_phase_markers():
    """A scope guard that ranges over an empty marker set asserts nothing."""
    marked = [
        pyfile.name
        for pyfile in sorted(SPECIFICATION_DIR.glob("test_*.py"))
        if MARKER_PATTERN.search(pyfile.read_text(encoding="utf-8")) is not None
    ]
    assert len(marked) >= 10, marked
