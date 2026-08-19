# Mathematical Source Report Memories

Trigger: mathematical research, source-mining, theorem lookup, background investigation,
or claim analysis that relies on external/web sources and is intended to inform later
repo work.

Rule: if mathematical research uses external or web sources, do not leave the result
only in chat. Record it in a durable mathematical report memory with direct source
links so later agents can recover the claim, scope, and provenance after transcript
compaction or session loss.

Required contents for the report memory:

- the mathematical question or claim investigated;
- the conclusion or current best synthesis, labeled clearly if it remains tentative;
- the exact source links or stable source identifiers used;
- any key theorem/definition pointers or sections needed to resume work;
- the boundary between sourced facts, repo-specific inference, and remaining gaps.

Scope rule: this is for research findings, not bare bibliography. Keep
`theory/references/` as the canonical literature store, but also preserve the
research-level takeaway in memory when the result came from active source investigation.

Audit rule: research that depends on external sources but is not preserved in a durable
report memory is not reusable audit input. A later agent should not need to reread old
chat logs to recover why a cited source mattered.

Verification: a future agent resuming the topic should be able to open the memory,
follow the source links, and recover both the sourced claim and the exact research
question without searching transcript history.
