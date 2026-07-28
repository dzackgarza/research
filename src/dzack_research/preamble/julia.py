r"""Call Julia and Oscar from Sage.

EXAMPLES::

    sage: from dzack_research.preamble.julia import BONDS, oscar_call
    sage: oscar_call("rank", BONDS["bond1"])
    2
"""

from __future__ import annotations

from typing import Any

from sage_julia_bridge import JuliaHandle, julia

from .fixtures import BONDS

__all__ = ["BONDS", "JuliaHandle", "julia", "oscar_call"]


def oscar_call(function: str, *args: object, **kwargs: object) -> Any:
    """Call ``function`` in Oscar after converting the arguments.

    EXAMPLES::

        sage: from dzack_research.preamble.julia import BONDS, oscar_call
        sage: oscar_call("nrows", BONDS["bond2"])
        2
    """
    julia.eval("using Oscar")
    return julia.call(function, *args, **kwargs)
