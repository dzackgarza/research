# Repo-scoped stubs; see lexicon/README.md.
from typing import TypeVar

from sage.structure.parent import ElementConstructorInput

_Unique = TypeVar("_Unique", bound=UniqueRepresentation)

class UniqueRepresentation:
    # CachedRepresentation with equality by identity: calling the class with
    # the same constructor arguments returns the identical instance.
    @classmethod
    def __classcall__(
        cls: type[_Unique],
        *args: ElementConstructorInput,
        **kwds: ElementConstructorInput,
    ) -> _Unique: ...
