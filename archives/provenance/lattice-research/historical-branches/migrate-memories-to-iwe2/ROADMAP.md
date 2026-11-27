# Execution Roadmap

How this project gets from Sage-backed research to a spec-enforced, provably-correct
lattice DSL — and then to the Coble research results — without drifting into a paperwork
factory.

`GOAL.md` is the mathematical destination (the staged Coble program); this document is
the *execution methodology* and the *order of work*. It does not restate the mathematics
— read `GOAL.md` for that. Read this when planning a workstream, judging whether recent
work was worth it, or onboarding to "how we work and why."

## The corrected pipeline (the one canonical flow)

Every capability the research needs travels exactly this path. No research code is
written ahead of it.

1. **Research need.** A concrete research step (e.g. "compute $\Gamma_{Co}$-orbits of
   isotropic vectors in $T_{Co}$") names a capability it requires.
2. **Spec obligation.** That capability becomes an `@abstractmethod` on the *weakest*
   mathematical category that owns it. The spec declares the contract (operation,
   hypotheses, owner, return object); it never implements, never imports the
   implementation (`lattice-impl`), never carries a `NotImplementedError` body.
3. **Literature test.** A test asserts a *specific mathematical value* that a cited
   extraction guarantees. The ONLY acceptable citation is a registered Zotero key in
   `theory/references/references.bib` + its extraction file under
   `theory/references/literature/` + the specific line range that literally states the
   value (see the `What A Test Cites` memory). Vague citations ("SPLAG Ch. 4") are banned
   — agents fabricate them. The test asserts the mathematics (e.g. the discriminant group
   is $\mathbb{Z}/3$, the inclusion into the dual is/ is not an isomorphism), never a
   software property (raises, non-None, type, source-string). It first goes red because
   the backend does not yet compute the fact, then stays red until the implementation
   **recovers the cited value**. "Abstractly correct" and "it raised as expected" are
   never passing conditions; recovering the sourced value is.
4. **Implementation.** Written separately from the spec (impl may import Sage; spec may
   not). Its only job is to make the literature test green by computing the real value.
5. **Smoke = simple real computations.** Instantiate simple objects (e.g. the root
   lattices $A_2$, $E_8$) through category constructors and assert their literature-cited
   mathematical facts. Current Sage backends recover only a fraction of these correctly,
   so most smokes are **supposed to be red** — red means the backend does not yet compute
   the cited fact. A smoke goes green only when the backend genuinely recovers the cited
   value. Making a smoke green by weakening a spec, bypassing a constructor, or asserting
   a weaker fact than the source states is the cardinal sin.
6. **Promotion gate.** Only after 2–5 hold may the capability be used in research code.
   Research/agent code imports **categories, never Sage directly**; a method reaches the
   research layer only through this gate.

## Why this roadmap exists — the three defects it fixes

Grounded in the 2026-06-17 corpus audit (`reports/2026-06-16-memory-migration-ledger.md`
context; audit findings summarized here):

- **The gating tests are not mathematical.** The *run* obligation tests assert
  source-graph structure (`X is Y.ParentMethods`) and even silently pass unmet
  obligations — Python `abc.abstractmethod` does not enforce at call time through the Sage
  category MRO (observed 2026-06-18: a correctly-refined `A_2.inclusion_morphism()`
  returns `None` instead of computing $\iota: L \hookrightarrow L^\#$). They carry **zero
  literature citations**, while the genuinely cited artifacts (`tests/variety_spec/*.sage`,
  `tests/fixtures/coble_literature_fixtures.json`) are **not the gate** —
  `coble_literature_fixtures.json` is consumed by no test at all. So nothing forces the
  backend to recover real, sourced mathematics; agents feel green-at-all-costs pressure
  and weaken specs to relieve it. This is the engine of the thrashing.
- **No import discipline / promotion gate.** The implementation (`lattice-impl`, the
  Sage-backed dependency) imports Sage directly throughout; nothing forces capabilities
  through stages 2–5 first, so the DSL is not load-bearing.
- **Process doctrine is scar tissue.** The same anti-drift lesson is restated across 6+
  memories; operational gates (cards, triage, retirement, PR) never re-assert the
  mathematical-object gate, so an agent can satisfy every gate with zero math progress.

## Order of work

Each workstream is a self-limiting state machine with a hard DONE condition. A workstream
is not "done" when its cards are tidy — only when its DONE condition holds.

### WS-4 — This roadmap (current)
DONE when this file is reviewed and adopted as the program-of-record.

### WS-2 — Consolidate the process corpus
Stop the bog before adding new machinery.
- Collapse the 6+ duplicated anti-drift memories into one canonical memory; the rest
  become one-line pointers.
- Embed the single completion gate (ownership theorem / recovery formula /
  missing-category obligation / representation split) **directly into the task-card
  template and the retirement check**, so no gate is satisfiable without naming the math.
- Purge the worst dialect drift from governance docs: "descriptor binding" → "axiom $A$
  refines category $B$"; "surface" → name the actual structure; lead rule-docs with the
  mathematical contract, not the mypy/stub taxonomy.

DONE when: anti-drift doctrine has one canonical owner; the card template's acceptance
field IS the math-object gate; no *misleading* dialect ("descriptor binding" leading,
"surface" as a vague synonym) remains in governance docs or spec docstrings. (Not a mass
rename: acceptable uses like "method surface" stay; only misleading ones are fixed.)

### WS-1 — Fix the engine (prove via one vertical slice)
Per the chosen altitude, do **not** scaffold this broadly. Prove the corrected pipeline
end-to-end on **one** obligation, then generalize.

Proof slice (the first thing built):
- **Need:** the lattice→discriminant surface that the Coble orbits depend on.
- **Spec obligation:** `discriminant_group` / `inclusion_morphism` / `is_unimodular` on
  the integral lattice category (already abstract-declared in the `category-specs` repo,
  the abstract-DSL dependency).
- **Literature test:** assert the $A_2$ / $E_8$ facts, each cited to a specific
  extraction line per `What A Test Cites` — $A_2$ glue group (= discriminant group
  $L^\#/L$) is $C_3$ with glue-vector norm $2/3$ (`conway1999sphere.md:4655,4682`,
  `:4379`); $E_8$ even unimodular (`nikulin1979integral.md:120`). The test asserts the
  mathematics (the inclusion into the dual is an isomorphism iff the lattice is
  unimodular), never that a call raises or is non-None. Red while the backend does not
  compute the fact; green only on recovery.
  **Prerequisite (blocker):** register `conway1999sphere` and `nikulin1979integral` in
  `theory/references/references.bib` — those extractions exist but are unkeyed today.
- **Engine artifacts the slice forces into existence:** (a) a literature-sourced smoke
  that is red until the backend recovers the cited value (red simply means the math is
  not yet computed — there is no exception-disposition harness); (b) one such cited test
  replacing a `X is Y.ParentMethods` meta-assertion in the run set; (c) the
  import/promotion check, exercised on this one method.

Also addresses the observed non-enforcement defect: Python `abc.abstractmethod` does not
enforce at call time through the Sage MRO (unmet obligations silently return `None`).
Whether to fix by switching to Sage's `abstract_method` or another mechanism is decided
when this slice is built — but the *test* asserts the mathematics, and is red while the
fact is uncomputed regardless of the enforcement mechanism.

DONE when: the cited $A_2$/$E_8$ math test is red before impl and green only when the
backend recovers the cited values; it cites registered keys + specific extraction lines;
the meta-assertion it replaces is deleted; an import-discipline check exists and passes
for this method. Generalize across obligations only after this.

### WS-3 — Coble keystone surfaces
The research payoff. Build these 5 method-families through the corrected pipeline (each
its own slice). The biggest mathematical hole is keystone (1).
1. **Lattice→discriminant lifting** — `O(L)→O(A_L,q_L)` (`stable_subgroup`,
   `discriminant_action`, abstract at `lattices/homsets.py` in the `category-specs`
   repo) **+ the
   Nikulin/Eichler lifting theorem** converting finite discriminant-orbit equality into
   primitive isotropic-vector orbit equality. *No named theorem/backend exists today —
   logged unresolved in `SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES`. This is the keystone.*
2. **`primitive_embedding` / `primitive_extension` constructors** — absent today (only
   `is_primitive` + gluing exist); needed to build $S_{Co}\subset\Lambda_{K3}$,
   $T_{Co}=S_{Co}^\perp$, and the gluing anti-isometry.
3. **Typed subgroup stabilizer / centralizer** — realize
   $\Gamma_{Co}=\mathrm{Stab}(\tilde h_{Co})\cap Z(\theta)$ as a typed $O(T_{Co})$
   subgroup with verified generators.
4. **Indefinite isotropic-plane orbit binding** — bind the (complete) Indefinite.jl
   `INDEF_FORM_GetOrbit_IsotropicKplane` backend to a Coble-callable spec method.
5. **Morphism-from-generators + matrix extraction** — `hom(images)` / `to_matrix()` as
   the substrate so $\theta$, $\gamma_{Co}$, pullbacks are defined on generators and
   matrices are *extracted*, never hand-written.

DONE when: $\Gamma_{Co}$-orbits of isotropic vectors in $T_{Co}$ are computed through
typed DSL methods (no hand-written matrices), each step backed by a literature test.

## Self-healing audit (kill authority)

On a fixed cadence (every ~N substantive commits, or on context handoff), a high-level
audit runs and is **empowered to halt a workstream**:

- **The value question:** "Did the last batch of commits move at least one literature
  test from red→green, add a real spec obligation, or implement a recovery — or did it
  only rearrange cards, statuses, ledgers, and prose?" If the latter, the batch is drift.
- **The dialect question:** did any engineering jargon re-enter spec docstrings or new
  governance prose?
- **The gate question:** did any `enforced-and-unmet` smoke get turned green by weakening
  a spec rather than implementing the math?
- **Verdict:** `healthy` | `drifting` (course-correct, name the next literature test) |
  `paperclip-factory` (stop the workstream, escalate to the user). The audit reports the
  verdict and the one next mathematical action — not a status matrix.

Detailed per-workstream sub-workflows (state diagrams) are authored **just-in-time when a
workstream starts**, not all upfront — authoring them all now would itself be the bog
this roadmap exists to prevent.
