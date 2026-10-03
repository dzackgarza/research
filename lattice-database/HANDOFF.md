# Lattice intake handoff

## State

| Item | Count |
| --- | ---: |
| Permanent lattice cards in `lattices/<TAG>.md` | 160,781 |
| Source rows still in `lattices/source/` | 0 |
| Nebe–Sloane archive cards without a parsed Gram tensor | 63 |

The 160,351 bulk source rows have permanent tags and root Markdown cards. The source
archives and normalized rows remain under `sources/`. Some archive entries state
invariants without an exact Gram tensor. Their cards keep the stated data and citation.

The card seeder uses its assigned tag and reads only the source row. It does not load
existing cards, compute invariants, or run checks. A full site corpus load with
`verify=False` read 160,781 cards successfully. A full site build has not run.

## Workflow contract

1. `seed` converts stored source rows into permanent cards.
2. `new` and direct Markdown edits author cards without a stored source row.
3. `enrich` computes additional card fields.
4. `verify` reports errors through independent modules in `src/latticedb/checks/`.

The site reads root cards for publication. Verification belongs in scheduled CI and
does not gate seeding, authoring, enrichment, or site publication.

## Work in progress

- The old intake commands and their batch modules have been removed from the CLI.
  `new` now writes without corpus loading or derivation. `next-tag` uses card
  filenames and retired tags. Morphism authoring reads only its own file.
- `enrich` now skips cards without a Gram tensor and saves derive certificates once
  per invocation. The full enrichment path and optional SageMath operations still
  need a focused run on small specimens.
- `checks/` has card, relation, and source modules. Some relation checks still live
  in `corpus.py`; move their ownership into the checks subtree. `corpus.load` still
  performs geometric relation checks even with `verify=False`.
- The scheduled workflow has been renamed to `lattice-database-verify.yml` and now
  runs the read-only `verify` command. Check its syntax and job behavior.
- Site rendering now handles missing basic invariants and uses a local Markdown
  renderer for bulk source prose. Render a sparse card and run a full build in a
  repository-owned scratch target before claiming publication works at this scale.
- Existing tests and some README passages still describe derivation and checks at
  card entry. Update them to the four workflows. Do not run a full verification
  suite as part of seeding or site building.

## Next actions

1. Run targeted checks of `new`, `next-tag`, `enrich --tag`, `verify` on a small
   fixture, and sparse card page rendering. Repair failures at their workflow owner.
2. Finish extracting relation checks from corpus loading. Ensure `verify` reports
   incomplete source cards and remains read-only.
3. Build the complete site in project-owned scratch space and inspect an archive
   card without a Gram tensor. Review memory and build time for 160,781 pages.
4. Reconcile README and targeted tests with the delivered commands. Commit and push
   the workflow changes on `main` without staging unrelated files under `writing/`.
