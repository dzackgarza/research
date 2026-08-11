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
import sageparse.preparser.importer  # noqa: F401
import sageparse.preparser.research  # noqa: F401
