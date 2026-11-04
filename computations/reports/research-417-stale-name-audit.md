# Stale session names in the expectation files: resolved against the provider's exports

Checked against `.scratch/se-provider-6ad7a5ea/src/sage_extensions/all.py` (the consumer
pin) and the provider source. No test was edited: renaming without a verified target would
invent an API, and deleting the assertions would drop obligations.

| name used by the test | where | provider reality | classification |
| --- | --- | --- | --- |
| `NumberFields()` | `test_functors_construct.sage:112,114` | exports are `OwnedNumberFields` and `NumberFieldsWithChosenPrimitiveElement`; **neither** exposes `ring_of_integers` as a category constructor (`number_fields.py:481` is an element-level `def`) | stale name **and** missing construction → provider |
| `AbelianGroups()` | `test_properties_construct.sage:75` | the provider's own name is `OwnedAbelianGroups` (used at `groups.py:1187`), and `all.py` does **not** export it | stale name with an existing but unexported counterpart → provider export |
| `FinitelyPresentedTorsionModules(ZZ)` | `test_properties_construct.sage:109` | no such class; the method it calls, `direct_sum_of_cyclics`, is defined at `modules/pure/modules.py:520` on a different parent | stale name with no category-level counterpart → provider |

## Why no repair was made here

Each of the three would need one of: an exported provider name, or a construction that does
not exist. Neither is in this repository's gift. What *is* ours is that the expectations
must keep stating the mathematics — so they stay as written and remain visible failures,
exactly as the functor population now records its blocked entries with causes rather than
dropping them.

## What this settles and what it leaves

- Settled: the three names are stale in research, and the reason is the provider's export
  surface, not the mathematics. `FractionFieldQuotients` — repaired upstream — is the proof
  that this class of blocker resolves by export, not by renaming in the consumer.
- Left open: `OwnedAbelianGroups` export; a category-level `ring_of_integers` and
  torsion-module constructor. These join the already-queued provider findings.

Coverage unchanged: two of 754 construction files run under the harness, a third collects,
and `#417` remains unaccepted.
