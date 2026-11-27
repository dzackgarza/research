r"""Subobject construction category for topological spaces."""

from __future__ import annotations

from ....cat import SubobjectsCategory


class _Subobjects(SubobjectsCategory):
    r"""Topological subspaces with the induced topology.

    Canonical chain: ``TopologicalSpaces().Subobjects()``.
    """

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...
