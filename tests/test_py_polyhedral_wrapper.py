import os

import pytest

from py_polyhedral.binaries import binary_available, get_binary_path


def test_py_polyhedral_imports_without_any_compiled_backend() -> None:
    with pytest.raises(AssertionError, match="not available on PATH"):
        get_binary_path("DZACK_RESEARCH_TEST_POLYHEDRAL_BINARY_THAT_DOES_NOT_EXIST")


def test_py_polyhedral_resolves_backends_from_path(tmp_path, monkeypatch) -> None:
    executable = tmp_path / "INDEF_FORM_AutomorphismGroup"
    executable.write_text("#!/bin/sh\nexit 0\n")
    executable.chmod(0o755)
    monkeypatch.setenv("PATH", os.fspath(tmp_path))

    assert binary_available("INDEF_FORM_AutomorphismGroup")
    assert get_binary_path("INDEF_FORM_AutomorphismGroup") == os.fspath(executable)
