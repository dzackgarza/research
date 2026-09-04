# Two separate installations.
#
# ``research`` is the dialect: it registers the lowering rules and turns
# implicit multiplication on, which is what a session's ``preparse`` uses.
# ``importer`` is the meta-path finder that makes ``.sage`` an importable
# source format.  Importing the dialect does not install the finder.
#
# Guard: this file rides sys.path into EVERY interpreter (the editable
# install's .pth and the repo .envrc both expose src/), including plain
# CPython tools that never load Sage.  The hook is meaningful exactly where
# ``sage`` is importable: there, a missing ``sageparse`` must stay loud;
# elsewhere the hook is vacuous and erroring on every unrelated python
# process is pure noise.
import importlib
import importlib.util

if importlib.util.find_spec("sage") is not None:
    importlib.import_module("sageparse.preparser.importer")
    importlib.import_module("sageparse.preparser.research")
