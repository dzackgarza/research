r"""Retire the archived framework scenario manifest as planning metadata.

The manifest grouped a proposed projective-scheme certification corpus by topic.
It was never an executable mathematical owner.  The live repository tracks
implementation work in ``TODO.md`` and records archive reconciliation per module
in the generated denominator, so individual framework scenarios remain pending
or reconciled independently of this retired grouping table.
"""

from pathlib import Path

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/tests/framework/scenario_manifest.sage",
    "live_owner": "TODO.md",
    "disposition": "reconciled-live-owner",
}


def test_live_plan_owns_archive_reconciliation_instead_of_a_scenario_table() -> None:
    plan = Path("TODO.md").read_text()

    assert "Reconcile every archived mathematical construction" in plan
    assert "archive_reconciliation_inventory.tsv" in plan
