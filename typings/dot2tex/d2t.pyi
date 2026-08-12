"""Source-backed typing surface for dot2tex.dot2tex in dot2tex 2.11.3."""

def create_xdot(
    dotdata: str,
    prog: str = "dot",
    options: str = "",
) -> bytes: ...
