# Repo-scoped stubs; see lexicon/README.md.
from typing import Any

class UniqueRepresentation:
    @staticmethod
    def __classcall__(cls: type, *args: Any, **kwds: Any) -> Any: ...

    @staticmethod
    def __classcall_private__(cls: type, *args: Any, **kwds: Any) -> Any: ...
