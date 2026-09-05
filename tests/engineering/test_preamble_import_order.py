import os
from pathlib import Path
import shutil
import subprocess

import pytest


_REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
_IMPORT_PREFIXES = (
    "",
    "import dzack_research.preamble.categories.group.magmas; ",
    "import dzack_research.preamble.categories.abstract_categories.products; ",
    "import dzack_research.preamble.categories.modules.framed.framed_free_modules; ",
    "import dzack_research.preamble.categories.rings.number_fields; ",
)


@pytest.mark.parametrize("prefix", _IMPORT_PREFIXES)
def test_natural_numbers_additive_structure_is_import_order_independent(prefix) -> None:
    sage = os.environ.get("SAGE_BIN") or shutil.which("sage")
    assert sage is not None
    sage = os.path.realpath(sage)

    environment = os.environ.copy()
    source = os.fspath(_REPOSITORY_ROOT / "src")
    environment["PYTHONPATH"] = os.pathsep.join(
        part
        for part in (source, environment.get("PYTHONPATH", ""))
        if part
    )
    program = prefix + (
        "from dzack_research.preamble.categories.sets.set_categories import NN; "
        "from dzack_research.preamble.categories.group.magmas import AdditiveMonoids; "
        "assert NN in AdditiveMonoids(); "
        "assert NN.zero() + NN(int(2)) == NN(int(2))"
    )

    subprocess.run(
        [sage, "-c", program],
        check=True,
        env=environment,
        cwd=_REPOSITORY_ROOT,
    )
