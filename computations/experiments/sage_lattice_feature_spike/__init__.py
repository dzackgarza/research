r"""Lattice feature spike — the fork carrying new mathematics beyond Sage.

Per the ruling "call the spike an import for all future work," this package
imports the base parity spike rather than re-implementing it. The base is the
drop-in Sage replacement substrate; engines added here (Nikulin primitive
embeddings, ZZ_p/QQ_p and Dedekind base-ring generalization, hyperbolic/Vinberg,
dual/functional machinery) build ON TOP of it.

No engine is added by an autonomous agent: each obeys the gap-ledger gating
(interactive session, cited source, reviewed test design, explicit user go) and
the freeze precondition on the base spike. See README.md.

The root research package re-exports this spike as `dzack_research.feature`.
"""

# The defining architectural property: the fork IS an import of the base parity
# spike. Loading it here also brings the base's sage_patches subtree live.
import sage_lattice_category_spike as base  # noqa: F401

__all__ = ["base"]
