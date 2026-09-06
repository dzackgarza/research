r"""Every category name the session publishes builds a category.

A name reached from the session import is mathematics a reader can use.  An
abstract base is not: it declares no supercategories, so building it reports
an unimplemented abstract method rather than a category.  Such a base is
reached from the module that defines it, by the implementation that needs it,
and this asks the whole published surface with no name excused.
"""

import inspect

import pytest
from sage.categories.category import Category

import dzack_research.preamble.all as session


def _nullary_category_names():
    r"""The session's category names that take no argument to build."""
    for name, candidate in sorted(vars(session).items()):
        if name.startswith("_") or not inspect.isclass(candidate):
            continue
        if not issubclass(candidate, Category):
            continue
        required = [
            parameter
            for parameter in inspect.signature(candidate.__init__).parameters.values()
            if parameter.name != "self"
            and parameter.kind not in (parameter.VAR_POSITIONAL, parameter.VAR_KEYWORD)
            and parameter.default is parameter.empty
        ]
        if not required:
            yield name


@pytest.mark.parametrize("name", sorted(_nullary_category_names()))
def test_a_published_nullary_category_name_builds_a_category(name) -> None:
    built = getattr(session, name)()

    assert isinstance(built, Category)
    assert all(
        isinstance(super_category, Category)
        for super_category in built.super_categories()
    )
