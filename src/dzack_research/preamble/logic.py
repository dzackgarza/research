r"""Predicates whose truth can be asked without coercing uncertainty to false.

The preamble uses ordinary booleans when a proposition is already decided.
When a mathematical relation is not decided at construction time, it returns
a :class:`Predicate`.  ``ask(P)`` evaluates the predicate; if the available
exact/certified procedures still do not decide it, the answer is Sage's
``Unknown``.
"""

from sage.misc.unknown import Unknown
from sage.structure.sage_object import SageObject


class Predicate(SageObject):
    r"""An unevaluated mathematical proposition."""

    __slots__ = ()

    def _ask_(self, *, max_prec: int = 4096):
        r"""Evaluate ``self`` as far as the predicate's algorithms permit."""
        raise NotImplementedError

    def __bool__(self):
        raise TypeError("an undecided predicate has no truth value; use ask(...)")


def ask(statement, *, max_prec: int = 4096):
    r"""Return the truth value of ``statement``, or ``Unknown`` if undecided.

    ``True`` and ``False`` pass through unchanged.  Predicates own their
    evaluation algorithms.  ``Unknown`` also passes through, so callers can
    compose this with existing Sage three-valued predicates.
    """
    if statement is True or statement is False or statement is Unknown:
        return statement
    if isinstance(statement, Predicate):
        return statement._ask_(max_prec=max_prec)
    raise TypeError(f"ask(...) expects a boolean or Predicate, got {statement!r}")


__all__ = ["Predicate", "Unknown", "ask"]
