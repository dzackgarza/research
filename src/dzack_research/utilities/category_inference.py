r"""The category of what each category's methods return, inferred from the returned value's class.

Implementation classes are exactly a category's ``ParentMethods``, ``ElementMethods`` and
``MorphismMethods``, so the class of a returned value names the category it lies in. For every
exported category the session can build, each method the category defines that takes no
arguments is called on the category's example object (or an element of it), and the category
read off the returned value's class is recorded. The result is JSON consumed by
``category_graph --format constructions --inferred FILE``. Nothing here judges a placement.
"""

from __future__ import annotations

import argparse
import inspect
import json
import signal
from types import FrameType

from sage.categories.category import Category
from sage.structure.element import Element
from sage.structure.parent import Parent

from dzack_research.utilities.megadoc import Survey, stable_runtime_text

CALL_SECONDS = 10
SLOTS = (("parent_class", "ParentMethods"), ("element_class", "ElementMethods"))


class CallTimedOut(Exception):
    r"""A call ran past ``CALL_SECONDS``."""


def _on_alarm(_signum: int, _frame: FrameType | None) -> None:
    raise CallTimedOut


def _value(thunk: object) -> tuple[bool, object]:
    signal.alarm(CALL_SECONDS)
    try:
        return True, thunk()  # type: ignore[operator]
    except Exception:  # noqa: BLE001 - a value that cannot be produced has no class to read
        return False, None
    finally:
        signal.alarm(0)


def _category_of_class(value: object) -> str | None:
    r"""The category named by the class of ``value``: an object's, or an element's parent's."""
    match value:
        case Parent():
            return stable_runtime_text(repr(value.category()))
        case Element():
            return "an element of an object of " + stable_runtime_text(repr(value.parent().category()))
        case bool():
            return "a truth value, not an object"
    return None


def _required(method: object) -> bool:
    try:
        signature = inspect.signature(method)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return False
    return any(
        p.default is inspect.Parameter.empty
        and p.kind in {inspect.Parameter.POSITIONAL_ONLY, inspect.Parameter.POSITIONAL_OR_KEYWORD, inspect.Parameter.KEYWORD_ONLY}
        for p in signature.parameters.values()
    )


def _own_names(instance: Category, slot: str, owner: str) -> list[str]:
    dynamic = getattr(instance, slot, None)
    if dynamic is None:
        return []
    names: dict[str, None] = {}
    for klass in dynamic.__mro__:
        if klass.__qualname__.split(".")[0] == owner:
            for member in Survey.members(klass):
                if not isinstance(getattr(klass, member.name, None), type):
                    names[member.name] = None
    return list(names)


def infer() -> dict[str, dict[str, dict[str, str]]]:
    survey = Survey()
    signal.signal(signal.SIGALRM, _on_alarm)
    inferred: dict[str, dict[str, dict[str, str]]] = {}
    for name in survey.names:
        klass = getattr(survey.session, name)
        if not (inspect.isclass(klass) and issubclass(klass, Category)):
            continue
        probe = survey.probe_arguments(klass)
        if probe is None or probe[1] == "abstract":
            continue
        instance = survey.build(klass, probe[0])
        if isinstance(instance, str):
            continue
        built, subject = _value(lambda: instance.an_object())
        if not built:
            continue
        subjects = {"ParentMethods": subject}
        got, element = _value(lambda: subject.an_element())
        if got:
            subjects["ElementMethods"] = element
        for slot, container in SLOTS:
            if container not in subjects:
                continue
            for method_name in _own_names(instance, slot, name):
                got, bound = _value(lambda: getattr(subjects[container], method_name))
                if not got:
                    continue
                if callable(bound):
                    if _required(bound):
                        continue
                    got, bound = _value(bound)
                    if not got:
                        continue
                category = _category_of_class(bound)
                if category is not None:
                    inferred.setdefault(name, {}).setdefault(container, {})[method_name] = category
    return inferred


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("-o", "--output", required=True)
    arguments = parser.parse_args(argv)
    inferred = infer()
    with open(arguments.output, "w", encoding="utf-8") as handle:
        json.dump(inferred, handle, indent=1, sort_keys=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
