# Repo-scoped stubs; see lexicon/README.md.
#
# The preparser prepends ``from sage.all_cmdline import *`` to every compiled
# .sage module and rewrites integer/real literals through the two names below
# (``_sage_const_0 = Integer(0)``). Without this stub the star-import made the
# whole module's constant pool ``Any`` — every ``xs[0]`` subscript silently
# erased its element type. Only the preparser's own names are exported:
# modules must import everything else explicitly (repo style), and an honest
# short list keeps accidental star-reliance visible.
from sage.rings.integer import Integer as Integer
from sage.rings.real_mpfr import RealNumber as _RealElement

# The preparser's real-literal spelling calls create_RealNumber, the factory
# that accepts the literal as a string; the element class is its return.
def RealNumber(x: str | float | int | _RealElement, base: int | Integer = ...) -> _RealElement: ...
