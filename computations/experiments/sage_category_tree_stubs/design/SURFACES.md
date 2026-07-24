# Four separately reviewable surfaces (decision record 3 §2)

The Sage bridge is one PR but **four independently reviewable surfaces**. DR3 §2: complete
independent interfaces merge independently — the monolith made mathematical review harder,
not more rigorous. This file is the review-boundary contract; it partitions the existing
modules and artifacts (LAYOUT contracts 1–4) into the four surfaces and fixes their
dependency direction.

Dependency direction (one-way): **(a) → (b) → (c)**, with **(d)** consuming **(b)** and
referencing **(c)**. No lower surface reads a higher one.

## (a) Pinned Sage observation & extraction  — LAYOUT contract 1
- **Interface:** what pinned Sage reports — classes, parameters, immediate
  supercategories, axioms, constructions, aliases. No math corrections, no
  property/structure/stuff classification, no parent "fixes".
- **Modules:** `runtime_probe.py`, `observed_build.py`, `observed_diff.py`, `sage_embed.py`,
  `sage_category_graph/` inventory sources.
- **Artifacts:** `design/sage/runtime_probe.json`, `design/sage/observed.json`,
  `design/sage/observed_parents.dot`.
- **Depends on:** nothing (root). Pinned to a Sage version label.

## (b) Correspondence ledger  — LAYOUT contract 3
- **Interface:** the hand-authored/reviewed Sage → normalized correspondence, mechanically
  validated against (a) and the normalized SSOT (`semantic_seed/`). Every row is a DR3 §6.3
  **bridge record** — `comparison_status`, `lean_semantic_category`, `proof_obligation_id`,
  `backend_capabilities`, `pinned_sage_version`. The finite-limit constructibility verdict
  (`relation`) is a *diagnostic* here, never semantic evidence (DR3 §3).
- **Modules:** `authored_mapping.py`, `mapping_build.py`, `seed_authored_sync.py`,
  `requirement_manifest.py`, `constructibility.py` (diagnostic), `naming.py`.
- **Artifacts:** `design/sage/mapping.yaml`, `design/sage/authored/*.json` (ledger +
  `lean_requirement_manifest.json`), `design/sage/correspondence.dot` (a view, not truth).
- **Depends on:** (a) and the normalized SSOT.

## (c) Pinned-release consumer  — BLOCKED on lean-lattices#4
- **Interface:** consume a **pinned lean-lattices release** and populate the realized side —
  `lean_semantic_category` and the `exact-Mathlib` / `exact-constructed` /
  `proven-presentation-equivalence` comparison statuses, plus the proof-carrying alternative
  to `ObservedTransport`. Until the release lands, every bridge record is
  `observed-Sage-approximation` / `not-yet-realized` with `lean_semantic_category: null`.
- **Current state:** the local `lean_category_dsl_spike/` copy, which DR3 §1 directs be
  **dropped** in favour of the pinned release (its empty in-tree lakefile is consistent with
  that). This surface is a **stub** until #4 releases — deliberately empty, never fabricated.
- **Depends on:** (b) and the pinned lean-lattices release. **Blocked.**

## (d) DSL / backend capability routing  — LAYOUT contract 4
- **Interface:** which implementations *provide* algorithms for a constructible category
  (the fiber/capability map), and execution routing `op.* → Sage receivers`, versioned
  separately from category meaning. Backend statuses: kernel-verified / Lean-checked
  certificate / experimental (never promotable without a certificate).
- **Modules:** `capability.py`, `factory.py` (stub instantiation), `routes/`.
- **Artifacts:** `routes/routes.yaml`, the capability manifest.
- **Depends on:** (b); references (c) backend capabilities.

---

*Scope note.* This file establishes the review boundaries and dependency contract. A literal
split of PR #278 into four separately-merged PRs is a follow-up git operation gated on the
same lean-lattices#4 release that surface (c) needs; it is not performed here.
