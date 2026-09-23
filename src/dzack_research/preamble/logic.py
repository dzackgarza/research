r"""Predicates whose truth can be asked without coercing uncertainty to false.

The preamble uses ordinary booleans when a proposition is already decided.
When a mathematical relation is not decided at construction time, it returns
a :class:`Predicate`.  ``ask(P)`` evaluates the predicate; if the available
exact/certified procedures still do not decide it, the answer is Sage's
``Unknown``.

A predicate here is a closed proposition ``R(x)``: the value
``chi_R(x)`` of the characteristic morphism ``chi_R : X -> Delta[1]`` of a
relation ``R`` on a set ``X`` at a point ``x``, whose computation is deferred.
``ask`` is the knowledge question about that value, so its codomain is
``True | False | Unknown`` (`DEF-06`).
"""

from sage.misc.abstract_method import abstract_method
from sage.misc.unknown import Unknown, UnknownClass
from sage.structure.element import parent as element_parent

from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.owned_category import _object_of


class _PropositionElement:
    r"""Private element realization for a represented closed proposition."""

    def __init__(self, parent=None) -> None:
        super().__init__(Propositions if parent is None else parent)

    @abstract_method
    def _ask_(self, *, max_prec: int = 4096) -> bool | UnknownClass:
        r"""Evaluate ``self`` as far as the predicate's algorithms permit.

        Protected contract (`OWN-05`).  Owner: :class:`Predicate`.  Implemented
        by each concrete proposition, which owns its decision algorithm; called
        only through the dispatcher :func:`ask`.  Returns ``True`` or
        ``False`` when the proposition is decided within the precision budget
        ``max_prec`` and ``Unknown`` otherwise; it never answers ``False`` for
        an undecided proposition.
        """
        ...

    def __bool__(self):
        raise TypeError("an undecided predicate has no truth value; use ask(...)")


class _PropositionSetEngine:
    r"""Private realization of the set of represented closed propositions."""

    def __init__(self, **rest) -> None:
        super().__init__(**rest)

    def __contains__(self, statement) -> bool:
        return element_parent(statement) is self

    is_parent_of = __contains__

    def _element_constructor_(self, statement):
        if element_parent(statement) is self:
            return statement
        raise TypeError("a represented proposition is constructed by its defining relation")

    def _repr_(self) -> str:
        return "Set of represented closed propositions"


Propositions = _object_of(
    Sets(),
    _engine=(Sets(), _PropositionSetEngine, _PropositionElement),
)
Predicate = Propositions.element_class


def ask(
    statement: bool | UnknownClass | Predicate,
    *,
    max_prec: int = 4096,
) -> bool | UnknownClass:
    r"""Return the truth value of ``statement``, or ``Unknown`` if undecided.

    ``True`` and ``False`` pass through unchanged.  Predicates own their
    evaluation algorithms.  ``Unknown`` also passes through, so callers can
    compose this with existing Sage three-valued predicates.
    """
    match statement:
        case _ if statement is True or statement is False or statement is Unknown:
            return statement
        case Predicate():
            answer = statement._ask_(max_prec=max_prec)
            assert answer is True or answer is False or answer is Unknown, (
                "a proposition's decision is True, False, or Unknown"
            )
            return answer
        case _:
            raise TypeError(f"ask(...) expects a boolean or Predicate, got {statement!r}")


__all__ = ["Predicate", "Propositions", "Unknown", "ask"]
