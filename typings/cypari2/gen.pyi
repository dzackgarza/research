# Repo-scoped stubs; see lexicon/README.md.
#
# The PARI object handle. Declared with the surface the preamble consumes:
# qfminim's (count, largest, coordinate-matrix) result is indexed and
# tuple-unpacked, and results convert into Sage parents via Parent.__call__.
from collections.abc import Iterator

from sage.rings.integer import Integer

class Gen:
    def qfminim(self, bound: object = ..., flag: object = ..., **kwds: object) -> Gen: ...
    def __getitem__(self, i: int | Integer) -> Gen: ...
    def __iter__(self) -> Iterator[Gen]: ...
