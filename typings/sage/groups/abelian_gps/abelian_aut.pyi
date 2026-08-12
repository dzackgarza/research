# Repo-scoped stubs; see lexicon/README.md.
#
# An automorphism of a finite abelian group, read as the matrix of its action
# on the group's generators -- the form the repo transposes to reach its own
# ``U^T G U = G`` convention.
from sage.structure.element import Matrix, MultiplicativeGroupElement

class AbelianGroupAutomorphism(MultiplicativeGroupElement):
    def matrix(self) -> Matrix: ...
