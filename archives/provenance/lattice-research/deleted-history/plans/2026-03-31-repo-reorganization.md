# Repository Reorganization

## Goal

- Current state: The repo has ~125 files across 19 directories.
  Roughly half is substantive mathematical content (computations, proof sketches,
  literature notes). The other half is agent-generated process debris: changelogs,
  schedules, thrashing analyses, verification methodologies, state assessments, stale
  plans, and duplicative status documents.
  The audit/ directory alone has 22 markdown files, many of which document *agent
  process* rather than mathematics.
  The root has 7+ status/planning files.
  Multiple archive/ subdirectories exist but are under-used.

- Target state: A clean research repository with three clearly separated concerns:
  - `computations/` — Sage scripts, foundation library, tests, and output data
  - `notes/` — mathematical content: proof sketches, literature notes, claim analyses
  - `papers/` — acquired literature (unchanged)
  - Root: README, REFERENCES, GAPS, AGENTS, justfile, and build/env config only
  - Everything else archived or deleted

- Why this matters: The current structure makes it hard to find actual mathematical
  content. Agent process documents crowd out substance.
  A new contributor (or a future agent session) has to wade through changelogs,
  schedules, and audit reports to find the real work.
  The repo should look like a mathematician's working directory, not an agent's
  scratchpad.

## Constraints

- Required: All substantive mathematical content must be preserved.
  No mathematical results, proof sketches, or literature analysis may be deleted.
- Required: Git history must be preserved.
  Use `git rm` and `git mv`, not raw `rm`/`mv`.
- Required: All computation scripts must still run after reorganization.
- Required: Internal cross-references in surviving documents must be updated.
- Forbidden: Deleting any computation script or its output data.
- Forbidden: Changing any mathematical content during the move.

## What to keep at root

These files stay at root (some will be rewritten/consolidated):
- `README.md` — rewrite to reflect new structure
- `REFERENCES.md` — canonical literature list (keep as-is)
- `GAPS.md` — open mathematical problems (keep, trim process language)
- `GOAL.md` — consolidate into README or keep if still useful
- `AGENTS.md` — agent instructions (keep)
- `justfile` — build/run orchestrator (fix and keep)
- `.envrc`, `.gitignore`, `.python-version`, `pyproject.toml`, `uv.lock` — config (keep)

## What to archive or delete

### DELETE (no mathematical content, pure agent process):

- `CHANGELOG.md` — agent work log; git log serves this purpose
- `SCHEDULE.md` — fake hourly agent work rotation schedule
- `BUGS.md` — documents one fixed bug; belongs in git history
- `main.py` — empty placeholder (5 lines, does nothing)
- `task1_2_fixed_output.txt` — stray output file in root (duplicate of computations/)

### DELETE (agent process debris in audit/):

- `audit/thrashing_analysis_2026-03-30.md` — post-mortem of agent mistake
- `audit/verification_process.md` — agent methodology document (314 lines)
- `audit/project_state_assessment.md` — inventory duplicating README + GAPS
- `audit/arf_invariant_warning.md` — warning about a fixed error
- `audit/foundation_specification.md` — spec for already-built library
- `audit/lattice_construction_standards.md` — standards doc superseded by foundation
- `audit/literature_connection_audit.md` — audit log of subagent review

### ARCHIVE (historical value but not active):

- `audit/task5_1_lattice_audit_report.md` — 343-line audit of failed approach
- `audit/embedding_verification_report.md` — completed verification report
- `audit/software_research_orbit_computation.md` — tool research for task3_2
- `audit/task3_2_status.md` — status doc (content folded into GAPS.md already)
- `plans/2026-03-31-standardize-foundation.md` — completed plan
- `plans/2026-03-31-literature-integration.md` — completed plan
- `PLAN.md` — 496 lines of stale execution checklists

### MOVE to notes/ (substantive mathematical content currently in audit/):

- `audit/literature_claim_map.md` → `notes/literature_claim_map.md`
- `audit/task1_1_birationality_note.md` → `notes/task1_1_birationality_note.md`
- `audit/task1_1_exact_coordinate_note.md` → `notes/task1_1_exact_coordinate_note.md`
- `audit/task5_1_route_reset.md` → `notes/task5_1_route_reset.md`
- `audit/task5_1_exact_involution_note.md` → `notes/task5_1_exact_involution_note.md`
- `audit/moduli_dimension_claim.md` → `notes/moduli_dimension_claim.md`
- `audit/new_literature_connections.md` → `notes/literature_connections.md`
- `audit/task1_1_literature_search.md` → `notes/task1_1_literature_search.md`
- `audit/thas_vs_task1_1_comparison.md` → `notes/thas_vs_task1_1_comparison.md`
- `audit/carat_capability_audit.md` → `notes/carat_capabilities.md`
- `audit/gap_technical_issue_update.md` → `notes/task3_2_gap_difficulty.md`

### MOVE proofs/solved/ → notes/proofs/:

- All 11 proof sketch files move from `proofs/solved/` to `notes/proofs/`
- The `proofs/` wrapper directory with its single `solved/` subdirectory is unnecessary
  nesting

### MOVE approaches/ → notes/:

- `approaches/task1_1_construction_families.md` →
  `notes/task1_1_construction_families.md`

### Flatten computations/:

- Keep all `.sage` scripts, `.txt` output files, foundation library, test file
- Keep `computations/archive/` as-is
- Delete `computations/FOUNDATION_DOCUMENTATION.md` (the foundation is self-documented
  with docstrings; the separate doc is a 137-line spec that duplicates what's in the
  code)
- The `.sage.py` files are gitignored build artifacts; leave them alone

## Target structure

```
research/
├── AGENTS.md
├── README.md              # rewritten: what this repo is, where to find things
├── REFERENCES.md          # canonical literature (unchanged)
├── GAPS.md                # open problems (trimmed)
├── justfile               # fixed: correct script names, all tasks, no inline envvars
├── .envrc / .gitignore / pyproject.toml / uv.lock / .python-version
├── computations/
│   ├── coble_geometry_foundation.sage    # canonical library
│   ├── coble_geometry.sage              # legacy (kept, not loaded by active scripts)
│   ├── test_foundation.sage             # 43 tests
│   ├── task*.sage                       # ~15 computation scripts
│   ├── compare_stabilizers.sage
│   ├── theta_matrix.sage                # generated data
│   ├── task3_1_generators.sage          # generated data
│   ├── *.txt                            # output data files
│   └── archive/                         # old scripts
├── notes/
│   ├── proofs/                          # proof sketches (from proofs/solved/)
│   │   ├── task1_1_sextic.md
│   │   ├── task1_2_gram_matrices.md
│   │   ├── ...
│   │   └── utilities_note.md
│   ├── literature_claim_map.md          # literature spine
│   ├── literature_connections.md        # paper ↔ computation connections
│   ├── task1_1_birationality_note.md
│   ├── task1_1_exact_coordinate_note.md
│   ├── task1_1_construction_families.md
│   ├── task1_1_literature_search.md
│   ├── thas_vs_task1_1_comparison.md
│   ├── task5_1_route_reset.md
│   ├── task5_1_exact_involution_note.md
│   ├── task3_2_gap_difficulty.md
│   ├── moduli_dimension_claim.md
│   └── carat_capabilities.md
├── papers/
│   ├── downloaded/
│   ├── extracted/
│   └── *.pdf
├── scripts/
│   └── gap_test.g
├── archive/                             # everything archived goes here
│   ├── audit/                           # old audit process docs
│   ├── plans/                           # completed plans
│   ├── logs/
│   └── verification_records/
├── coble_research_lean/                 # Lean project (future)
└── tests/
    └── test_task1_2_gram_properties.sage
```

## Phases

### Phase 1: Create target directories and move substantive math content

- Create `notes/` and `notes/proofs/`
- `git mv` all substantive audit files to notes/
- `git mv proofs/solved/*.md` to `notes/proofs/`
- `git mv approaches/task1_1_construction_families.md` to `notes/`

### Phase 2: Archive process debris

- Create `archive/audit/`, `archive/plans/`, `archive/logs/`,
  `archive/verification_records/`
- `git mv` archivable files (see lists above)
- `git mv` PLAN.md, completed plans to archive/
- Remove empty directories left behind

### Phase 3: Delete pure debris

- `git rm` files with no mathematical content (CHANGELOG, SCHEDULE, BUGS, main.py, stray
  root output file)
- `git rm` agent process docs from audit/ that are pure methodology/process

### Phase 4: Fix references and rewrite README

- Update cross-references in surviving notes/ files (grep for `audit/`,
  `proofs/solved/`)
- Rewrite README.md to reflect new structure
- Trim GAPS.md of process language
- Decide: keep GOAL.md separate or fold into README
- Fix justfile (correct script names, all tasks covered)

### Phase 5: Verify

- `just run-all` — all computation scripts still work
- `just test-foundation` — foundation tests pass
- Grep for broken internal references
- `git status` clean

## Risks / Rollback

- Risk: Cross-references in surviving documents point to old paths
- Mitigation: Grep-and-fix pass in Phase 4
- Rollback: Git history preserves everything; `git revert` any commit

## Stop Rules

- Do not delete any file containing mathematical results, proofs, or literature analysis
- Do not modify computation scripts during the reorganization
- If `just run-all` fails after reorganization, fix path issues before proceeding
