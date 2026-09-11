"""Source-level regressions for the archive reconciliation denominator."""

from pathlib import Path
import runpy


def _inventory_module():
    return runpy.run_path("computations/scripts/archive_reconciliation_inventory.py")


def test_multiline_function_parameters_are_not_module_public_bindings(tmp_path: Path) -> None:
    archive_root = tmp_path / "archives" / "preamble"
    archive_root.mkdir(parents=True)
    module = archive_root / "sample.py"
    module.write_text(
        """def combine[T](\n"
        "    values: list[T],\n"
        "    *,\n"
        "    term: T | None = None,\n"
        "):\n"
        "    local = term\n"
        "    return values, local\n"
        """
    )

    scan_module = _inventory_module()["scan_module"]
    notions = scan_module(module, archive_root)
    names = tuple(notion.qualified_name for notion in notions)

    assert names == ("<module>", "combine")


def test_one_line_suite_does_not_nest_later_public_declarations(tmp_path: Path) -> None:
    archive_root = tmp_path / "archives" / "preamble"
    archive_root.mkdir(parents=True)
    module = archive_root / "sample.py"
    module.write_text(
        "def first(): return 1\n"
        "def second():\n"
        "    return 2\n"
        "class Third:\n"
        "    def method(self):\n"
        "        return 3\n"
    )

    scan_module = _inventory_module()["scan_module"]
    notions = scan_module(module, archive_root)
    names = tuple(notion.qualified_name for notion in notions)

    assert names == ("<module>", "first", "second", "Third", "Third.method")
