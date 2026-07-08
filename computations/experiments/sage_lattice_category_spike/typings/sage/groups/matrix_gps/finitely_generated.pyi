# Repo-scoped stubs; see lexicon/README.md.
from typing import Any

from sage.groups.matrix_gps.finitely_generated_gap import (
    FinitelyGeneratedMatrixGroup_gap,
)

def MatrixGroup(*gens: Any, **kwds: Any) -> FinitelyGeneratedMatrixGroup_gap: ...
