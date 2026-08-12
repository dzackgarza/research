r"""The research package: the preamble is the codebase.

This is a *Sage* package, not a plain Python package. Its modules are
``.sage`` sources compiled to Python on import by the ``sageparse``
preparser (the ``tree-sitter-sage`` distribution, a hard runtime
dependency). Import it inside a Sage environment: ``src/sitecustomize.py``
installs the import hook into every process.

The exploratory spikes that once re-exported here are archived reference
material under ``computations/archives/`` — importable in a session for
reference, imported by nothing.
"""
