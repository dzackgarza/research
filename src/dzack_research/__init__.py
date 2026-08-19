r"""The research package: the preamble is the codebase.

This is a *Sage* package, not a plain Python package. Its modules are
``.sage`` sources compiled to Python on import by the ``sageparse``
preparser (the ``tree-sitter-sage`` distribution, a hard runtime
dependency). Import it inside a Sage environment: ``src/sitecustomize.py``
installs the import hook into every process.

The exploratory spikes that preceded the preamble were fully absorbed into
it and deleted (2026-08-19); git history is their record.
"""
