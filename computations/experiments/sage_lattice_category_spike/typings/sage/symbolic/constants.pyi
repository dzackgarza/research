# Repo-scoped stubs; see lexicon/README.md. At runtime these are Constant
# objects that coerce into Expression on first arithmetic use; the repo only
# ever uses them in expression arithmetic, so Expression is the honest type.
from sage.symbolic.expression import Expression

e: Expression
pi: Expression
