"""Source-backed typing surface for dot2tex.dotparsing in dot2tex 2.11.3."""

from collections.abc import Iterable, Iterator


class DotNode:
    name: str
    fillcolor: str
    pos: str
    texlbl: str
    xlp: str


class DotEdge:
    def get_source(self) -> str: ...
    def get_destination(self) -> str: ...


class DotGraph:
    attr: dict[str, str]
    allnodes: Iterable[DotNode]
    alledges: Iterable[DotEdge]
    allgraphs: Iterator[DotGraph]


class DotDataParser:
    def parse_dot_data(self, data: bytes) -> DotGraph: ...
