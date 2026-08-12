# Repo-scoped stubs; see lexicon/README.md.
from abc import abstractmethod as abstract_method
from collections.abc import Callable

# The renaming import above is not an explicit re-export under
# --no-implicit-reexport (only ``X as X`` is), so name the public surface.
__all__ = ["AbstractMethod", "abstract_method", "abstract_methods_of_class"]

class AbstractMethod:
    r"""The descriptor Sage's ``@abstract_method`` leaves on a class.

    A category states an obligation by binding one of these; an object whose
    lookup still resolves to it has not implemented the obligation.  The
    obligations sweep reads exactly that, so the descriptor is part of the
    checked surface.
    """
    _f: Callable[..., object]
    def __call__(self, *args: object, **kwds: object) -> object: ...

# ``abstract_method`` is declared as a re-export of ``abc.abstractmethod``
# (see the import above): that IS its semantics — the decorated body is an
# obligation, not an implementation — and it is the one spelling mypy
# recognizes, so decorated docstring-only bodies stop reporting empty-body.
# The runtime decorator (which leaves an ``AbstractMethod`` descriptor, read
# by the obligations sweep) is untouched; only bare ``@abstract_method`` is
# used in this repo, so the ``optional=`` calling form is not declared.

def abstract_methods_of_class(cls: type) -> dict[str, list[str]]: ...
