"""Source-level regressions for the archive reconciliation denominator."""

import runpy
from pathlib import Path


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


def test_multiline_docstring_text_is_not_a_public_definition(tmp_path: Path) -> None:
    archive_root = tmp_path / "archives" / "preamble"
    archive_root.mkdir(parents=True)
    module = archive_root / "sample.py"
    module.write_text(
        'r"""Notes.\n'
        "\n"
        "A category may describe its class graph by hand.\n"
        '"""\n'
        "class Actual:\n"
        "    pass\n"
    )

    scan_module = _inventory_module()["scan_module"]
    notions = scan_module(module, archive_root)
    names = tuple(notion.qualified_name for notion in notions)

    assert names == ("<module>", "Actual")


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


def test_reconciliation_metadata_accepts_one_or_many_archive_modules(tmp_path: Path) -> None:
    tests = tmp_path / "tests"
    tests.mkdir()
    (tests / "test_single.py").write_text(
        "ARCHIVE_RECONCILIATION = {\n"
        "    'archive_module': 'preamble/single.sage',\n"
        "    'live_owner': 'src/single.py',\n"
        "    'disposition': 'reconciled-live-owner',\n"
        "}\n"
    )
    (tests / "test_many.py").write_text(
        "ARCHIVE_RECONCILIATIONS = (\n"
        "    {\n"
        "        'archive_module': 'preamble/first.sage',\n"
        "        'live_owner': 'src/first.py',\n"
        "        'disposition': 'reconciled-live-owner',\n"
        "    },\n"
        "    {\n"
        "        'archive_module': 'preamble/second.sage',\n"
        "        'live_owner': 'src/second.py',\n"
        "        'disposition': 'reconciled-live-owner',\n"
        "    },\n"
        ")\n"
    )

    metadata = _inventory_module()["reconciliation_metadata"](tests)

    assert set(metadata) == {
        "preamble/single.sage",
        "preamble/first.sage",
        "preamble/second.sage",
    }
    assert metadata["preamble/first.sage"]["live_owner"] == "src/first.py"
