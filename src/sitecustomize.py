# Two separate installations, and the preamble needs both.
#
# ``research`` is the dialect: it registers the lowering rules and turns
# implicit multiplication on, which is what a session's ``preparse`` uses.
# ``importer`` is the meta-path finder that makes ``.sage`` an importable
# source format.  Importing the dialect does not install the finder.
#
# ``init.sage`` -- Sage's startup file, which every REPL and Jupyter kernel
# runs -- imports ``dzack_research.preamble.catalogue`` on its second line,
# and that is a ``.sage`` module.  Without the finder here it raises
# ModuleNotFoundError before the preamble exists, so every session and every
# notebook comes up bare.
#
# Guard: this file rides sys.path into EVERY interpreter (the editable
# install's .pth and the repo .envrc both expose src/), including plain
# CPython tools that can never load the preamble.  The hook is meaningful
# exactly where ``sage`` is importable: there, a missing ``sageparse`` must
# stay loud (a bare kernel is the failure this file exists to prevent);
# elsewhere the hook is vacuous and erroring on every unrelated python
# process is pure noise.
import importlib
import importlib.util

if importlib.util.find_spec("sage") is not None:
    importlib.import_module("sageparse.preparser.importer")
    importlib.import_module("sageparse.preparser.research")
