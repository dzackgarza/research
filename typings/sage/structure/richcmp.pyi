# Repo-scoped stubs; see lexicon/README.md.
def richcmp(x: object, y: object, op: int) -> bool: ...

# The comparison-operator codes richcmp dispatches on (richcmp.pyx).
op_LT: int
op_LE: int
op_EQ: int
op_NE: int
op_GT: int
op_GE: int
