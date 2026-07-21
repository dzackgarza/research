# Namespace package used to force-load Sage category modules.
from typing import Any

def __getattr__(name: str) -> Any: ...
