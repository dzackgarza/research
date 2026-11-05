r"""Bind the variety-category abbreviations the tests in this directory use."""

import importlib.util
from pathlib import Path

from category_abbreviations import install

install()

# The expectation files here import the catalogue families from ``conftest``.  Inside
# this directory that name resolves to this file, so the shared definitions in the
# test-root conftest are re-exported here rather than duplicated or silently dropped.
_ROOT_CONFTEST = Path(__file__).resolve().parent.parent / "conftest.py"
_SPEC = importlib.util.spec_from_file_location("_research_root_conftest", _ROOT_CONFTEST)
_ROOT = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_ROOT)

for _name in ("COMMUTATIVE_RINGS", "FIELDS", "PRINCIPAL_IDEAL_DOMAINS", "specimen"):
    globals()[_name] = getattr(_ROOT, _name)
