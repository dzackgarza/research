"""Pytest configuration for SageMath tests."""

import os
import re
import textwrap

import pytest
from sage.all import *  # noqa: F403
from sage.all import ZZ, Genus, Matrix


# Make SageMath globals available to all tests
@pytest.fixture(autouse=True)
def sage_globals(request):
    """Inject sage.all exports into test module globals."""
    import sage.all as sg

    target_dict = request.node.obj.__globals__
    for name in dir(sg):
        if not name.startswith("_"):
            target_dict[name] = getattr(sg, name)


def pytest_collection_modifyitems(config, items):
    """Collect tested methods from docstrings during collection."""
    config._tested_methods = {}

    for item in items:
        target = getattr(item.module, "TEST_TARGET", None)
        if target:
            key = (str(item.fspath), target)
            config._tested_methods.setdefault(key, set())
            doc = getattr(item.obj, "__doc__", "")
            if doc:
                # Match "Tests .method()" or "Tests method()"
                match = re.search(r"Tests \.?([a-zA-Z0-9_]+)\(\)", doc)
                if match:
                    config._tested_methods[key].add(match.group(1))


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """Print untested mathematical methods for each class."""
    tested_map = getattr(config, "_tested_methods", {})
    if not tested_map:
        return

    terminalreporter.section("Mathematical Method Coverage Analysis")

    # boilerplate methods common to Sage objects
    # ONLY truly non-mathematical system/Python boilerplate should be here.
    # Methods like 'base_ring', 'hom', 'parent', 'category' are PURPOSELY OMITTED
    # from this blacklist because they ARE mathematically significant to test.
    boilerplate = {
        "copy",
        "deepcopy",
        "dump",
        "dumps",
        "get_custom_name",
        "is_immutable",
        "is_mutable",
        "list_external_initializations",
        "register_action",
        "register_coercion",
        "register_conversion",
        "register_embedding",
        "rename",
        "reset_name",
        "save",
        "set_immutable",
        "version",
        "trait_names",
        "static_attributes",
        "firstlineno",
        "pyx_vtable",
    }

    for (file_path, target), tested_methods in tested_map.items():
        # Try to get methods from an instance if possible, fallback to class
        try:
            # We try common construction patterns to get an instance
            if target.__name__ == "IntegerLattice":
                obj = target([[1, 0], [0, 1]])
            elif target.__name__ == "IntegralLattice":
                obj = target("A1")
            elif target.__name__ == "BinaryQF":
                obj = target(1, 0, 1)
            elif target.__name__ == "QuadraticForm":
                obj = target(ZZ, 1, [1])
            elif target.__name__ == "TernaryQF":
                obj = target([1, 1, 1, 0, 0, 0])
            elif target.__name__ == "GenusSymbol_global_ring":
                obj = Genus(Matrix(ZZ, 1, 1, [2]))
            else:
                obj = target
        except Exception:
            obj = target

        all_attrs = dir(obj)
        math_methods = {
            m
            for m in all_attrs
            if not m.startswith("_")
            and not m.startswith("test")
            and m not in boilerplate
            and callable(getattr(obj, m))
        }

        untested = sorted(math_methods - tested_methods)
        rel_path = os.path.relpath(file_path)

        terminalreporter.write_line(f"\n{rel_path} (Target: {target.__name__})")
        if untested:
            terminalreporter.write_line(f"Untested ({len(untested)}):")
            msg = ", ".join(untested)
            terminalreporter.write_line(
                textwrap.fill(msg, initial_indent="  ", subsequent_indent="  ")
            )
        else:
            terminalreporter.write_line("  All mathematical methods are tested!")
