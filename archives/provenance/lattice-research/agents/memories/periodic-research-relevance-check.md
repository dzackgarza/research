---
title: Periodic Research Relevance Check
status: active
---
# Stop periodically and check whether the current work still advances research

Trigger this check:

- after 2-3 artifact edits;
- after 2-3 card/plan/status updates;
- after a correction from the user;
- after more than one round of classification without source changes;
- before detailed engineering work that does not directly expose mathematical
  vocabulary;
- whenever the agent feels tempted to create a plan, handoff, decision card, or memory
  instead of reading/fixing source.

Start with the mathematical checkpoint, not a route through project artifacts.
State which mathematical object, operation, theorem, construction, or interface is
advanced; which source file, proof note, spec method, backend bridge, or research
computation changes; which definitions, constructions, category obligations,
implementation witnesses, or proof obligations are established; which exact
mathematical claims remain unresolved; which unresolved claim is next and what source
or Sage/backend behavior controls it; and what mathematical claim becomes true if the
next task succeeds.

Do not answer this check with feature names, plan names, route labels, "work stack",
"stage", "gated", "executable work", or "useful guardrail" language before the
mathematical state is stated. If prior work did not change a definition, construction,
category/refinement membership, proof obligation, implementation witness, or
source-backed computation, call it paperwork, not mathematical progress.

If the checkpoint is vague, stop artifact work.
Read the source/math, fix the source-level issue, or retire the artifact.
