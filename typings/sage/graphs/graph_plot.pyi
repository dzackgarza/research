from typing import Any

from sage.plot.graphics import Graphics


class GraphPlot:
    def plot(self, **kwds: Any) -> Graphics: ...
