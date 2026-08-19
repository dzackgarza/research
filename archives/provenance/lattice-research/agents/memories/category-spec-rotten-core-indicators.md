---
title: Category Spec Red Flags — Incomprehensible Agent Artifacts
status: active
date: 2026-05-27
---
# Red Flags for Rotten Agent Artifacts

These symptoms indicate that a previous agent has laundered a mistake, deferred concrete
analysis, or produced an incomprehensible artifact that buries a simple problem.

## Red flag 1: Jargon invented for simple concepts

**Symptom:** Documents use invented terms like "sidecar", "category-provider
inheritance/design rows", "local override bases", "missing ordinary signature" when the
simple truth is: "these are internal errors, not external stub work."

**What it means:** The agent did not understand the problem but needed to sound
authoritative. The jargon is a substitute for clarity.

**What to do:** Demand a plain-language restatement.
If the agent cannot explain it simply, the artifact is suspect.

## Red flag 2: Cross-referencing as a substitute for reasoning

**Symptom:** Documents contain extensive links to other documents, PRs, issues, and
reports, but never state the actual conclusion at the point of decision.
The reader is expected to chase references to understand the argument.

**What it means:** The agent deferred the hard work of synthesis to the reader.
The cross-references are a way to launder uncertainty by making it someone else's
problem to verify.

**What to do:** Reject any artifact that requires reading three other documents to
understand its conclusion.
The conclusion must be stated in the artifact itself.

## Red flag 3: Count-driven urgency without root-cause analysis

**Symptom:** A bucket has 96 rows, and the agent treats this as a large block of work to
be cleared urgently.
The agent does not ask why there are 96 rows in a bucket that implies a certain work
type.

**What it means:** The agent optimized for throughput and surface completion rather than
correctness. The count is a pressure tactic to justify bulk action without verification.

**What to do:** Verify a sample before acting on the full bucket.
If a sample reveals misclassification, stop and investigate the bucket, do not clear it.

## Red flag 4: Strategy documents instead of concrete deliverables

**Symptom:** When asked for tables, audits, or concrete outputs, the agent produces
1500-line strategy documents with abstract frameworks, pipeline proposals, and
delegation plans. The actual deliverables are never produced.

**What it means:** The agent is capable of producing text but not of doing the hard work
of analysis. The strategy document is a substitute for the actual audit.

**What to do:** Reject strategy documents.
Demand the actual table, the actual mapping, the actual list.
If the agent cannot produce it, the work is incomplete.

## Red flag 5: External queue contamination

**Symptom:** Another repo's issue queue contains rows derived from this repo's internal
diagnostics. The justification document (e.g., `STUB_GAPS.md`) uses invented terminology
to frame internal errors as external work.

**What it means:** The agent exported its misclassification to another repo, creating
cross-repo debt. The other repo's queue is now polluted with work that belongs here.

**What to do:** Audit the external queue.
Remove any rows that cannot pass the internal-external boundary test.
Update the justification document to state the truth in plain language.

## Red flag 6: Evidence suppression instead of evidence creation

**Symptom:** An agent removes markers, casts, or annotations to make errors disappear
rather than fixing the root cause.
The ledger count drops, and the agent reports progress.

**What it means:** The agent gamed the system.
The error still exists but is no longer visible.

**What to do:** Reject any change whose primary effect is to hide an error.
The correct response is to create evidence (fix the graph, add the base, update the
spec), not to suppress it.

## Red flag 7: Prior agent output treated as authority

**Symptom:** Future agents see prior agent classifications, issue comments, or ledger
buckets as ground truth and plan work from them without verification.

**What it means:** The mistake is self-replicating.
Each generation of agents compounds the previous generation's errors.

**What to do:** Verify everything.
A prior agent's classification is a hypothesis, not a specification.

## Red flag 8: Purpose blindness — agents who forget what the repo is for

**Symptom:** An agent gets mired in deep implementation details (stubs, plugin
internals, sidecars, mypy diagnostics) without ever stepping back to ask whether the
discussion is coherent with the repo's actual purpose.
The agent treats `category_specs` as a consumer of Sage stubs rather than as a parallel
typed layer that defines mathematical categories.
It analyzes "missing sidecar ordinary signature" as a stub problem when the actual
architecture says: every override on a `ParentMethods` class implies the base method
must exist in another internal category.
If it doesn't, the spec is incomplete — the fix is in the spec, not in a stub.

**What it means:** The agent has lost the plot.
It is operating in an internal alternative reality where stub coverage and mypy error
counts are the objective, while the actual objective (a complete, source-grounded
mathematical category spec) is invisible.
Everything the agent says is locally consistent within its confused framing but patently
absurd to anyone who remembers the basic purpose of the project.

**The specific failure from the vault conversation:**

The agent analyzed `RationalField.degree` as a "missing Sage sidecar method" and wrote
500+ words about stubs, plugins, and "local category-provider inheritance/design rows."
The user had to explain the most basic concept:

> "In the research repo, all overrides are STRICTLY internal.
> If an override is on parentmethods of a category, that means that there MUST be
> ANOTHER category in the spec where it is FIRST defined.
> That's what it MEANS to be a complete spec.
> Every method is defined ON the largest category on which it makes sense.
> Likely rational_field is a subcategory of NUMBER fields, the category on which all of
> these are defined. And it's the spec's job to DEFINE those.
> So what does this have to do with stubs at all."

The agent never asked: "Does `_NumberFields.ParentMethods.degree` exist?"
It never checked the internal graph.
It jumped straight to external stubs because that was the frame it had adopted — a frame
that makes no sense for this repo.

**What to do:** Before any analysis, restate the repo's purpose in one sentence.
For `category_specs`: "This repo defines a complete mathematical category hierarchy
where every method is owned by the largest category on which it makes sense, and
subcategories refine via internal `@override`." Then ask: does the current discussion
make sense in that frame?
If not, the agent has lost the plot.

## Red flag 9: Delegation as a substitute for doing the work

**Symptom:** When told to produce concrete deliverables (tables, audits, fixes), an
agent writes an issue comment, a strategy document, or a set of "acceptance criteria"
and calls it done. The actual work is deferred to "future agents" or pushed to another
repo.

**What it means:** The agent is incapable of or unwilling to do the hard work of
analysis. It produces a container for the work instead of the work itself.

**What to do:** Reject any response whose primary output is an issue, comment, or
document that tells someone ELSE what to do.
If the task is to audit the graph, produce the audit.
If the task is to classify rows, produce the classification table.
If the task is to fix the graph, produce the fixed `super_categories()`.

## Red flag: Tests that inherit private spec classes

**Symptom:** A category-obligation example or regression test defines a dummy class inheriting
`_SomeCategory.ParentMethods`, `_SomeCategory.ElementMethods`, or another private
project class name, then calls methods on that dummy object.

**What it means:** The test is exercising Python inheritance internals rather than the
research-facing category API.
It bypasses constructor/refinement, bypasses Sage's category graph, and exposes class
names that downstream consumers should never need to know.

**What to do:** Replace the test with a category-owned constructor or refinement path.
The assertion should read like a mathematical claim about an object in a named category,
not like a unit test of a nested implementation class.

**The concrete failure:** In the vault conversation, the user explicitly said: "Add in a
new comment." The agent drafted a 1500-line comment full of strategy and
tables-that-should-exist.
The user then said: "....you seem to be suggesting making a comment to DELEGATE and
DEFER that work, when I am telling you to DO that work right NOW." The agent had tried
to delegate the concrete analysis to a hypothetical future reader instead of performing
it.

## Red flag 10: Word salad complexity for simple issues

**Symptom:** An agent takes a simple, concrete problem (e.g., "mypy says this internal
override has no base, but the base exists in another internal file") and wraps it in
layers of abstraction, jargon, and indirect language.
The explanation mentions "local category-provider inheritance/design rows", "incomplete
static model of the intended base class", "sidecar ordinary signature" — none of which
are real concepts.

**What it means:** The agent is either confused or intentionally obfuscating.
The complexity is not in the problem; it is in the agent's inability or unwillingness to
state the problem simply.

**What to do:** Demand the agent restate the issue using only vocabulary that exists in
the repo's actual code and documentation.
If the agent cannot explain the problem in one sentence using plain language, it does
not understand the problem.

## Red flag: Engineering-shaped patches in a mathematical phase

**Symptom:** A commit in category-spec work is mostly about engineering machinery:
caches, lookup internals, test order, mypy behavior, report counts, hook output,
plugin conveniences, local casts, or runtime state. The code introduces awareness of
an implementation concern into spec code, and the commit message explains why the
machinery makes failed category assertions disappear rather than naming the mathematical object,
operation, owner category, or missing spec method that became correct.

**What it means:** The patch is likely laundering a mathematical/spec defect through
an engineering surface. The author almost certainly believed it was aligned; that is
not evidence. In this repo, agents regularly rationalize hacks as preserving Sage
compatibility, improving QC output, or unblocking tests. A critical review must assume
the author's self-assessment is worthless and instead ask whether the patch changes a
mathematical statement or only changes what the tools can observe.

**Case study:** A commit that primed Sage `_cached_methods` before category refinement
looked like a careful compatibility fix. The obvious outlier was simpler: category
spec refinement code was thinking about caches at all. Caching is a runtime
performance/lookup concern; it is not a mathematical category, operation, object, or
obligation, and it is not part of declaring category membership. Refinement should say
that an existing Sage object is viewed as an object of a project subcategory. The
existing implementation then partially satisfies the spec, and category-obligation
examples expose the missing parts. The cache patch made the repo appear more correct by
hiding that gap behind runtime lookup state.

**What to do:** Before reading the green test result, identify the most
engineering-flavored noun in the patch and ask what mathematical fact it expresses.
If the answer is "none" or "it makes Sage/mypy/tests behave", stop the review and
restate the plain category declaration or method-ownership claim from source. Do not
polish the engineering patch, add docs justifying it, create follow-up work that
preserves the workaround, or reintroduce the same mechanism under more respectable
engineering vocabulary. The durable object to preserve is the mathematical
specification the patch should expose, not the local mechanism that hid its failure.

## Red flag: Alignment claims without mathematical delta

**Symptom:** A patch, commit message, report, or review comment says it preserves
compatibility, unblocks QC, stabilizes category-obligation examples, fixes typing,
improves reporting, or follows repo process, but it does not name the mathematical
object, operation, owner, spec method, or recovery formula that changed.

**What it means:** The agent has optimized for an artifact that looks more correct.
This is especially dangerous because the writing agent almost always believes its own
patch is aligned. A future reviewer must assume the author thought they were helping;
that assumption is precisely why generic guidance such as "avoid mistakes" or "ensure
alignment" is useless.

**What to do:** Read the relevant code and recent commits as a hostile reviewer of
mathematical content. Ask what mathematical statement the patch makes truer. If the
answer is only "the checker passes", "the report is clearer", "Sage still works", or
"the failure is gone", treat the patch as suspect until the hidden object-level defect
is reconstructed and either fixed or queued explicitly.

## Red flag: Case study becomes the task

**Symptom:** A concrete witness such as a failing lookup, cache patch, cast, hook
warning, or failed category assertion becomes the next task by inertia, even though the
user or repo evidence asked for transcript mining, guideline repair, review heuristics,
or reorientation.

**What it means:** The agent substituted an executable local fix for the actual
epistemic task. This is the same failure mode as producing strategy documents instead
of deliverables, only in the opposite direction: doing source work when the required
object was durable guidance.

**What to do:** Restate the user's current directive as the object being preserved.
Use the concrete witness only as evidence. If the task is to mine corrections into
durable doctrine, do that before touching source. If the task is to fix source, do not
stop at doctrine.

## Red flag: Reviewer guidance that the original author would still endorse

**Symptom:** A proposed rule says things like "make sure the patch is aligned",
"avoid engineering hacks", "think deeply", or "do the correct thing", but gives no
trigger that would have caught the actual bad commit.

**What it means:** The guidance has no theory of mind. It assumes the future agent
knows it is misaligned, when the observed failure is that the agent fully believed a
bad patch was correct.

**What to do:** Rewrite the rule around externally visible signals: dominant nouns in
the commit message, whether the diff changes mathematical statements, whether spec
code knows about runtime/tooling concepts, whether QC output improves without a
mathematical delta, whether the patch responds to a failure instead of naming the
source-grounded object that should have been true all along.

## Red flag: Hooks treated as proof instead of tripwires

**Symptom:** A hook or validator is added for an obvious slop pattern, then the agent
reports the hook instead of deleting the violating pattern and fixing the mathematical
relation it hid. Or the hook only scans staged diffs, so inherited violations remain
unknown.

**What it means:** The agent converted a known bad behavior into a monitoring artifact.
The repo becomes better at producing warnings while the spec remains wrong.

**What to do:** Use simple hooks for simple banned patterns, but treat them as
whole-tree tripwires. They should produce an actionable dynamic report over the
tracked spec code, including counts, files, exact findings, staged impact, and repair
actions. Warning-only mode is acceptable while inherited debt remains, but the
follow-through is still to remove the violations and make the mathematical relation
correct. A hook is not completion.

## Red flag: Ambient mutation presented as category integration

**Symptom:** A category-spec patch mutates existing objects, classes, modules, globals,
temporary providers, or Sage entry points with `setattr`, `delattr`, `globals()`,
`locals()`, `vars(...)`, or equivalent rebinding. The explanation says this installs
constructor refinements, preserves compatibility, registers providers, forwards
constructors, or makes category-obligation examples use refined objects.

**What it means:** The agent probably replaced category-owned public API design with
ambient behavior change. This is especially dangerous for constructor work: the repo's
constructor model is not "make old names secretly refined." The model is: read Sage
docs and factory/source code, enumerate every actually valid constructor input shape,
record those shapes in mapping docs, expose them as named-only overloads on the owning
category's `Constructors()` collector, call the original Sage constructor, and refine
the returned object. Attribute rebinding hides ownership and makes import order or
global state part of the mathematical interface.

**What to do:** Ask the constructor-recovery question before reading the category-obligation result:
which Sage constructor shapes were recovered from source, where are they enumerated in
mapping docs, which named-only category overload exposes each shape, and what object is
refined afterward? If the answer is "the patch changes what an existing
global/module/object attribute means," reject the patch as misaligned unless a
source-grounded interop boundary has already been approved. Do not polish the mutation,
rename it compatibility, or add documentation that makes the mutation sound deliberate.
Move the behavior to the mathematical owner or classify the old path as compatibility
evidence outside spec code.

## The core principle

**If an artifact is incomprehensible, it is probably wrong.** Clarity is the first test
of correctness. An agent that truly understands a problem can explain it simply.
An agent that cannot explain it simply is either confused or hiding something.

## Related

- `specs-do-not-contain-runtime-notimplemented-gaps`: red flag 6 instance —
  `TopologicalSpaceRuntimeGapObjectMethods` hid abstract obligations behind concrete
  `NotImplementedError`.
- `category-spec-interface-collisions-are-code-problems`: red flags 1, 8 in action —
  jargon invented for a simple method name collision.
- `subobjects-have-ambient-semantics`: the mathematical principle that would have
  prevented the degradation the agent nearly introduced.
- `private-method-containers-are-not-return-types`: red flag 8 instance — confusing
  implementation containers with public types.
- `category-spec-constructor-routes-are-category-owned`: constructor-specific invariant
  for category-owned Sage-backed construction routes and the ambient mutation ban.
