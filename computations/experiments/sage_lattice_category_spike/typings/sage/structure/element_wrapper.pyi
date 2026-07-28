from sage.structure.element import Element
from sage.structure.parent import Parent

class ElementWrapper(Element):
    value: object
    wrapped_class: type[object]

    def __init__(self, parent: Parent, value: object) -> None: ...
