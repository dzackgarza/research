# research#606 — issue wording vs the stated intent (review only, no action taken)

## What #606's wording asserts (verbatim snippets)

- "Research's notebooks and consumers use those public operations and no longer use a
  second public Python set category."
- "Replace the old set-layer provider path only as the corresponding formal and kernel
  routes become available..."
- "...the Lean kernel replaces the dynamic-inheritance core." — backed in the issue by
  `INTENT.md`, `lean-categories/TODO.md` and `lean-cas-dsl/specs/computational-core.md §3`.

## What the stated intent now requires

- Research consumes maintained public interfaces (it imports `sage_extensions.all` via
  `src/dzack_research/preamble/all.py`).
- Abstraction and runtime implementation belong to their upstream owners; this session
  does not implement upstream set-layer migration in research, and does not treat #606's
  prose as an independently established mandate.

## Where the repository's own text sits

`INTENT.md:1-4` — "This is the grounding reference for `lean-categories`, `lean-cas-dsl`,
`lean-cas-dsl-leaf-contracts`, `lean-cas-dsl-leaves`, `sage-categories` and `research`."

So the citation in the issue is not invented: there is a recorded architectural split in
repo files. But it is a *record of an architecture*, not an instruction to this agent.
The instruction "research consumes maintained public interfaces; implementation belongs
upstream" governs this session and takes precedence over both #606's phrasing and my own
earlier echoes of it.

## The conflict, stated narrowly

Both directions agree on ownership: the formal and kernel pieces live upstream
(`lean-categories`, `lean-cas-dsl`). They differ on research's role:

- #606's wording frames research as the place whose consumers get *moved onto* the
  Lean-kernel catalogue-derived operations, implying active rearchitecture of this repo's
  surface by whoever executes the issue.
- The stated intent confines this repo to *consuming maintained public interfaces* — i.e.
  `sage_extensions.all` today — and leaves any re-surfacing to be delivered and adopted by
  its owners.

Earlier passes of this session repeated the issue phrasing ("consumers must be moved onto
the catalogue-derived language") as if settled. Recorded here as an error of framing only:
**nothing implementing it was ever written** — the survey files measured existing
behavior, and the inventory file treats the needed surface as external. No code executed
any migration.

## Evidenced present state (unchanged by this review)

- research's public set surface is the star-reexport of `sage_extensions.all`
  (`preamble.all:9-11`) into `sage_extensions/categories/sets/*`.
- no file in this repo enacts the Lean-side migration described in #606's text; the only
  artifacts are read-measure evidence files and two prepared upstream patches awaiting an
  owner route.

## Explicitly not done

- no `lean-categories` checkout, editing or authoring (held since the boundary was set);
- no edit to the consumer surface, `preamble.all`, or `archives/`;
- no implementation inferred from issue prose; no rearchitecture;
- no files deleted; no issue written or reordered;
- #219 remains measured and passing (23/23), closure still outside this connection.

## Dependencies that stay external regardless of reading

`lean-categories#97` then `#96`; the `lean-cas-dsl` catalogue-derived surface;
`sage-extensions#234/#498` (`DEV-58`); research-issue writes (read-only here); and the
`lean-categories` publication route for the two prepared patches.
