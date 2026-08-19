from __future__ import annotations

import os
from pathlib import Path

import pytest


# Julia runtime for juliacall must come from juliaup.
_HOME = Path("/tmp/sage-home")
_PROJECT = _HOME / "julia_env"
_DEPOT = _HOME / ".julia"
_JULIAUP_JULIA = Path("/home/codespace/.julia/juliaup/julia-1.11.9+0.x64.linux.gnu/bin/julia")

_HOME.mkdir(parents=True, exist_ok=True)
_PROJECT.mkdir(parents=True, exist_ok=True)
_DEPOT.mkdir(parents=True, exist_ok=True)

os.environ["HOME"] = str(_HOME)
os.environ["PYTHON_JULIAPKG_PROJECT"] = str(_PROJECT)
os.environ["JULIA_DEPOT_PATH"] = str(_DEPOT)
os.environ["PYTHON_JULIAPKG_EXE"] = str(_JULIAUP_JULIA)
os.environ["JULIAUP_CHANNEL"] = "1.11"
os.environ["JULIA_PKG_SERVER"] = ""

if not _JULIAUP_JULIA.exists():
    raise RuntimeError(
        "juliaup Julia runtime not found at "
        f"{_JULIAUP_JULIA}. Install juliaup first."
    )

from juliacall import Main as jl


@pytest.fixture(scope="session", autouse=True)
def _init_julia_oscar_runtime() -> None:
    jl.seval("using Pkg")
    jl.seval('Pkg.activate("tests/julia_doc")')
    jl.seval("using Nemo")
    jl.seval("using Hecke")
    jl.seval("using Oscar")
    jl.seval("using Test")
