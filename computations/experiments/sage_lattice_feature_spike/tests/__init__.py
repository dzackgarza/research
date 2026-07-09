r"""Feature-spike test suite.

Kept as a subpackage (not flat like the base spike) so each FORK milestone's
tests land in their own module here as the milestone's interactive session
lands its engine: test_embeddings (M1), test_base_rings (M2),
test_hyperbolic (M3), test_duals (M4). Until then only the scaffold guard
(test_import_wiring) runs — no placeholder or skipped tests for unbuilt engines.
"""
