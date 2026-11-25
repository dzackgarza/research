# Issue-tree and milestone policy (research repo)

## Execution order

Minimize the work needed to complete the full required programme, including
implementation, verification and rework. Rank work by its mathematical consequence
and the later work it removes before sorting dependencies. The default
priority is: shared wrong answers and failed constructions; reusable operations
that unblock named computations; required mathematical capability; broad audits,
interface normalization, typing and cleanup; then optional extensions. State the
concrete consumer or repeated implementation avoided when promoting a refactor.
An architectural label, scanner score, issue count or small task size is not a
payoff. A historical report requires current-source confirmation at selection.

Before selecting a repair, inspect the scheduled changes to its owner and callers.
If a later construction or refactor replaces that code or changes the required
interface, advance that shared change and its prerequisites. Implement the repair
on the resulting owner. Record the affected issue numbers, source paths and work
saved in the owning issue. A smaller immediate patch earns priority only when it
is needed to perform the shared change or has an independent result that survives it.

After a shared change, compare each affected issue's full requirements with the
delivered result. Work already discharged becomes a closure check; retain and
schedule any remaining requirements. Preserve the original acceptance obligations.
Reassess this order when source or dependencies change. Observed workflow costs
that recur across required tasks can justify early repair on the same basis.

Split a concrete correctness repair out of a whole-repository survey when the
survey would delay it. Preserve both contracts and make the survey depend on
the repair. Performance work moves forward only for a measured obstruction to
a named computation. A constructor that cannot produce its mathematical object
is a correctness failure, distinct from a general construction-cost survey.

Global API freeze and aggregate acceptance do not supply mathematical inputs to
independent feature computations. Keep the actual construction dependencies;
retain every owner-local assertion and the full final acceptance obligations.
The native order at issue #46 records the current payoff assessment. Milestone
numbers identify scopes and do not impose a numerical execution order.

Native sub-issue order is the execution priority. `itree next` selects the
first ready work unit in depth-first order; it does not propagate a consumer's
priority to its prerequisites. When adding or moving a task, place each open
prerequisite before its consumer. For a grouping issue, place its prerequisites
before the whole subtree. A grouping issue must never block on a descendant.
Move a prerequisite branch earlier when necessary; do not add dependency edges
merely to express priority.

Required repairs precede optional extensions. A construction consumed by required
work is required too: preserve its full contract and place it in the required
milestone. Acceptance issues depend on all required branches they claim to
accept. Construction and loading defects precede the acceptance that exercises
them. Shared primitives retain their own acceptance; a port consumer does not
gate their closure.

Validate both the dependency graph and the native traversal order. A clean
`itree doctor` establishes structural consistency, not agreement with these
priorities. Check that every open blocker precedes its consumer, no ancestor
blocks on its descendant, required tasks have no optional prerequisites, and
each acceptance issue reaches all work in its stated scope, including required
tasks moved to another milestone for execution. An acceptance task can follow
its inputs in a later milestone without losing any of those obligations.

## Milestone scope

This is a research repository with a much longer work horizon, more detailed planning, and more human check-ins than a typical software project.
Naive software-geared structural rules (e.g. itree's W040 native-milestone mirror) are less applicable here: treat such findings as a flag to investigate whether *some* consolidation is warranted, never as a mandate — and never collapse the tree or milestones by an order of magnitude to satisfy one.
The itree issue tree is authoritative; native GitHub milestones are capability-level human-review checkpoints created just-in-time (user ruling 2026-07-11; W040 = 46 is accepted as-is).

The `needs-research` label is the parking state — work parked pending investigation or upstream capability — not a register of decisions awaiting the user.
Do not enumerate labeled issues as "open human decisions"; genuine decisions are extracted through decision-register sweeps (see #97) and recorded as rulings on the issues, the gap ledger, and plan cards.

## Where in-progress ideas live

Ideas are not all issues yet.
An agent that searches only the issue tree will miss live thinking and re-derive it badly.

- **GitHub Discussions** hold ideas still **in flux**: competing framings, pasted prompt responses to be reconciled, designs whose scope has not settled.
  A discussion is a thinking surface, not a decision — nothing in one is authoritative, and implementation requires a scoped issue.
  Live example: #217 (*Bridging Lean to computational backends*, Ideas category).

- **Issues** hold ideas that have a scope, carrying the label that names their state: `draft` (the scope itself is provisional; expect the body to change), `research` (empirical research or evaluation required before implementation), `needs-research` (parked — above), `needs-planning` (scope known; decomposition or an executable plan required before implementation).

The pipeline is one-directional: **a discussion is crystallized into an issue once its scope stops moving**, and everything downstream — implementation research, decomposition into work units, proof obligations, completion claims — is carried out on the issue tree, never in the discussion.
Link the discussion from the issue and leave it in place as the rationale trail; the development of an idea, including its retractions, is the record of why the scope is what it is.
Do not delete it or summarize it away.

Practical consequences: when picking up a topic, search discussions as well as issues.
When a discussion has stabilized, the next action is to file the issue, not to keep commenting.
When a discussion is still moving, do not manufacture an issue to make it look tracked.
