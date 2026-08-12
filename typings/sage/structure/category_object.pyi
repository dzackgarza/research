# Repo-scoped stubs; see lexicon/README.md.
#
# The base of Sage's parent hierarchy that carries category and base data
# (category_object.pyx). Only the surface the preamble consumes is declared.
from sage.rings.integer import Integer
from sage.structure.parent import Parent

# category_object.pyx: validates/expands generator names — 'x' with n=3
# becomes ('x0','x1','x2'); a sequence is checked and passed through.
def normalize_names(ngens: int | Integer, names: object) -> tuple[str, ...]: ...

class CategoryObject:
    def base(self) -> Parent: ...
