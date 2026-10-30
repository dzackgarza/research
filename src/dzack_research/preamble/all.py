r"""The research session: ``from dzack_research.preamble.all import *``.

The session namespace and its parser runtime belong to ``sage_extensions.all``.
This module re-exports it under the name the research notebooks and scripts
import, and registers that name so the parser treats its star import as the
complete session.
"""

from sage_extensions import language_runtime as _language_runtime
from sage_extensions.all import *  # noqa: F401,F403
from sage_extensions.categories.group.groups import OwnedGroups as Groups

_language_runtime.register_session_module(__name__)
