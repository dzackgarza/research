"""Load helpers for `Projective_Scheme_Framework.ipynb` in pytest.

The projective framework is developed inside a notebook, so tests cannot import it
as a normal Python module. This loader executes the notebook code into an isolated
namespace once per test session.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

_SKIP_REGRESSIONS_ENV = "PROJECTIVE_SCHEME_FRAMEWORK_SKIP_REGRESSIONS"
_FRAMEWORK_NOTEBOOK_RELATIVE = Path("computations/notebooks/Projective_Scheme_Framework.ipynb")

NotebookNamespace = dict[str, Any]
"""The namespace produced by executing notebook cells; cell outputs are
arbitrary Sage objects, so the value type is genuinely unconstrained — the
ambiguity is quarantined to this one alias."""

_loaded_namespace: NotebookNamespace | None = None


def _repo_root() -> Path:
    for candidate in [Path(__file__).resolve(), *Path(__file__).resolve().parents]:
        if candidate.name == "research":
            return candidate
    raise RuntimeError("Could not locate repository root from test-framework loader path.")


def _framework_notebook_path() -> Path:
    path = _repo_root() / _FRAMEWORK_NOTEBOOK_RELATIVE
    if not path.is_file():
        raise FileNotFoundError(f"Projective framework notebook not found: {path}")
    return path


def load_projective_framework(*, run_regressions: bool = False, force_reload: bool = False) -> NotebookNamespace:
    """Load framework extensions into an executable namespace.

    Parameters
    ----------
    run_regressions:
        When False, keep the framework's built-in regression probes skipped.
    force_reload:
        Re-run notebook cells even if already loaded in this process.
    """

    global _loaded_namespace
    if _loaded_namespace is not None and not force_reload:
        return _loaded_namespace

    notebook_path = _framework_notebook_path()
    notebook_payload = json.loads(notebook_path.read_text(encoding="utf-8"))

    previous_skip = os.environ.get(_SKIP_REGRESSIONS_ENV)
    if run_regressions:
        os.environ.pop(_SKIP_REGRESSIONS_ENV, None)
    else:
        os.environ[_SKIP_REGRESSIONS_ENV] = "1"

    namespace: NotebookNamespace = {"__name__": "__main__", "__file__": str(notebook_path)}
    try:
        for idx, cell in enumerate(notebook_payload.get("cells", [])):
            if cell.get("cell_type") != "code":
                continue
            source = "".join(cell.get("source", []))
            if not source.strip():
                continue
            code = compile(source, f"{notebook_path}:{idx}", "exec")
            exec(code, namespace, namespace)
    finally:
        if previous_skip is None:
            os.environ.pop(_SKIP_REGRESSIONS_ENV, None)
        else:
            os.environ[_SKIP_REGRESSIONS_ENV] = previous_skip

    _loaded_namespace = namespace
    return namespace
