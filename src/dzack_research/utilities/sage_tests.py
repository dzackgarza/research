r"""Collect ``test_*.sage`` files as Sage sessions.

A test is Sage code, written as a notebook cell is written: Sage literals,
Sage syntax, the research dialect, and a namespace holding what a Sage kernel
starts with (``sage.all_cmdline``) together with the preamble session. It is not
a Python module.

Loaded as a pytest plugin (``-p dzack_research.utilities.sage_tests`` in
``pyproject.toml``). Collection uses pytest's own ``Module`` for the file. Only
the import is replaced: the file is lowered by the owned
``sageparse.preparser.importer.SageLoader``, which applies the dialect that
``dzack_research.preamble.all`` installs and keeps the file's line numbers in
tracebacks. The module is then executed in the session namespace. Sage's
``sage-preparse`` gives a ``.sage`` script ``from sage.all_cmdline import *``
in the same way, which is the convention followed here.
"""

import ast
import builtins
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from types import ModuleType

import pytest

SUFFIX = ".sage"


def _session_namespace() -> dict[str, object]:
    import sage.all_cmdline

    import dzack_research.preamble.all as preamble

    names = {name: value for name, value in vars(sage.all_cmdline).items() if not name.startswith("_")}
    names.update({name: value for name, value in vars(preamble).items() if not name.startswith("_")})
    return names


def _session_loader(config: pytest.Config) -> type:
    from _pytest.assertion.rewrite import rewrite_asserts
    from sageparse import lower
    from sageparse.preparser.importer import SageLoader

    class SessionLoader(SageLoader):
        r"""A ``.sage`` file executed as a session, not as a library module.

        The lowered tree gets pytest's assertion rewriting, as a ``.py`` test
        module would through pytest's import hook, so a failing assertion
        reports its operands.
        """

        def source_to_code(self, data, path="<string>", *, _optimize=-1):
            source = data if isinstance(data, str) else bytes(data).decode("utf-8")
            lowered = lower(source).python
            tree = ast.parse(lowered, filename=str(path))
            rewrite_asserts(tree, lowered.encode("utf-8"), str(path), config)
            return compile(tree, str(path), "exec", dont_inherit=True, optimize=_optimize)

        def exec_module(self, module: ModuleType) -> None:
            # The session names resolve the way builtins do: after the file's
            # own bindings, and invisibly to pytest, which would otherwise
            # collect Sage's ``TestSuite`` from the module namespace.
            scope = dict(vars(builtins))
            scope.update(_session_namespace())
            module.__dict__["__builtins__"] = scope
            super().exec_module(module)

    return SessionLoader


class SageSession(pytest.Module):
    r"""A ``test_*.sage`` file, imported through ``SessionLoader``."""

    def _getobj(self) -> ModuleType:
        # As pytest's default ``prepend`` import mode does for a test module
        # outside a package: its directory goes first on ``sys.path``, so the
        # helper modules beside it import.
        directory = str(self.path.parent)
        if directory not in sys.path:
            sys.path.insert(0, directory)
        name = ".".join(self.path.relative_to(self.config.rootpath).with_suffix("").parts)
        loader = _session_loader(self.config)(name, str(self.path))
        spec = spec_from_file_location(name, self.path, loader=loader)
        module = module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        self.config.pluginmanager.consider_module(module)
        return module


def pytest_collect_file(file_path: Path, parent: pytest.Collector) -> pytest.Module | None:
    if file_path.suffix == SUFFIX and file_path.name.startswith("test_"):
        return SageSession.from_parent(parent, path=file_path)
    return None
