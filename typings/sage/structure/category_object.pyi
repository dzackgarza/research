# Repo-scoped stubs; see lexicon/README.md.
#
# The base of Sage's parent hierarchy that carries category and base data
# (category_object.pyx). Only the surface the preamble consumes is declared.
from sage.structure.parent import Parent

class CategoryObject:
    def base(self) -> Parent: ...
