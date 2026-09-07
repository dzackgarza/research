# Task complexity and model selection

Calibration date: 2026-09-07.

This guide assigns work a score from 0 to 100.
The score measures the judgment needed to preserve mathematical structure and long-term maintainability.
It increases with uncertain ownership, unresolved contracts, and errors that propagate into later contributions.
File count, output length, repetition, and execution cost do not determine the score.

The [TODO workstream DAG](TODO.md#remaining-workstreams-as-a-dependency-graph) determines which work is ready.
This guide determines the reasoning capability appropriate to that work.
The [construction and inheritance design](references/preamble-architecture.md) supplies the preamble's architectural context.

## Assigning a score

Score the actual responsibility assigned to the worker, including discovery and integration.
First identify the mathematical owner, the unsettled decision, and the downstream constructions that depend on it.
Then choose the highest applicable band below.
Use its lower end when the contracts and correctness criteria are explicit.
Use its upper end when competing interpretations remain or errors can propagate unnoticed.

Keep architectural consequences visible when assessing uncertainty.
A short change to category refinement can affect every object constructed afterward.
A long implementation of a specified algorithm can remain local and easy to assess.
An average across these factors would conceal the first task's risk.

Scores are ordinal routing judgments, not probabilities, time estimates, or measured model capability.
Prefer multiples of five; use a finer score only when it changes the assignment.
If uncertainty crosses bands, state the interval and route using its upper endpoint.

| Score | Character of the work | Typical responsibility |
| --- | --- | --- |
| `0 <= s < 5` | Mechanical execution; use deterministic tools | Apply a settled symbol rename, rewrite a known AST pattern, regenerate derived files, or classify records by an executable rule. |
| `5 <= s < 20` | Bounded interpretation and evidence collection | Find the relevant source, classify cases that need contextual judgment, select codemod inputs, or apply an established policy to actual code. |
| `20 <= s < 35` | Extension at an established owner | Implement a referenced algorithm, add a backend operation through an existing bridge, write a notebook, or build a bounded spike. |
| `35 <= s < 50` | Integration through established contracts | Add a category that inherits several existing structures; implement its maps and structural functors through their known owners. |
| `50 <= s < 70` | Coherent composition across category families | Combine algebraic, action, and topological structures when their basic definitions are settled but their interactions need development. |
| `70 <= s < 85` | Design, planning, organization, and orchestration | Choose decomposition and dependency order; organize contributions; discover new violation families; resolve uncertain ownership across subtrees. |
| `85 <= s < 95` | Shared foundations and enforcement | Change Cat-level operations, category refinement, construction contracts, generic Hom behavior, import direction, or enforcement of contribution policies. |
| `95 <= s <= 100` | Open-ended foundational direction | Resolve competing mathematical architectures, establish the core contracts for a broad rebuild, or direct research with unresolved foundations. |

The agent interval is `[5, 100]`.
The interval `[0, 5)` is the **waste-of-tokens tier** for agent execution.
Its exclusion applies equally to inexpensive and frontier models.

### Deterministic work and the intelligent task around it

Once the replacement rule and target symbols are settled, an LSP rename or codemod should perform the edits.
Three hundred call sites do not make that operation harder than three.
The intelligent task is establishing the rule, finding its full domain, and resolving semantic exceptions.

The same distinction applies to classification.
Assigning labels to prepared records by a fixed rule belongs in a query or script.
Finding the evidence, deciding which cases belong together, and interpreting ambiguous cases can justify an agent.
Give that agent the whole evidence question and access to its sources.
Having another capable agent prepare every input can consume the reasoning the assignment was meant to obtain.

For repeated work, inspect one operation and its dependencies.
Independent repetitions change execution volume.
Repeated use of an unresolved shared design preserves that design's higher score.
Use symbolic tools for the mechanical part after the design is settled.

### Consequences that raise the score

- **Shared meaning:** the change determines what an object, morphism, functor, or category membership means.
- **Construction authority:** later constructors depend on its required data or validation boundary.
- **Propagation:** a mistaken convention can be inherited, copied, or treated as policy by later contributors.
- **Uncertain ownership:** the task must decide where a mathematical concept first belongs.
- **Unsettled mathematics:** the work requires a new argument, algorithm, or decision about its computational domain.
- **Coordination authority:** the worker chooses scope, interfaces, dependency order, or how other workers divide responsibility.

Shared semantic or enforcement design normally starts at 85.
Planning, organizing, and orchestrating work normally starts at 70, even when the output is a short document.
Transcribing an already decided schedule is mechanical work.
Applying a known policy is bounded inspection; deciding what policy to enforce has broader consequences.

An isolated research problem can also score highly through mathematical uncertainty.
Conversely, sophisticated mathematical notation does not raise the score when a precise reference settles the construction.
Use the applicable correctness boundary: an arbitrary equality problem does not become decidable because a worker needs a check.

## Preamble examples

These scores assume the conditions stated in each row.
They describe assignments, not permanent scores attached to files or workstreams.

| Assignment | Score | Reason |
| --- | --- | --- |
| Apply an approved symbol rename at all references with the language server | 2 | The tool has the semantic target and the replacement rule. |
| Find which call sites satisfy the mathematical hypotheses for an approved replacement | 15 | Evidence selection and exceptional cases require judgment. |
| Inspect source for violations of an established naming or ownership rule | 15 | The criterion is known; source interpretation remains necessary. |
| Reproduce a specified calculation in a notebook using released preamble objects | 20 | The construction and its owner already exist. |
| Implement a paper's algorithm with explicit hypotheses and a suitable existing interface | 25 | The reference supplies the method and correctness argument. |
| Add a GAP, Julia, Macaulay2, or Singular operation through an established backend interface | 25 | The bridge and mathematical return objects are settled. |
| Add a scheme subcategory defined by existing finite-type, smoothness, properness, and base-field refinements | 30 | Placement and inherited contracts are already determined. |
| Add a category combining established module and group-action interfaces | 45 | The maps and forgetful functors must agree across owners. |
| Develop topological algebras with continuous group actions through settled algebra, action, and topology foundations | 60 | Continuity and structure preservation interact across several category families. |
| Determine a previously unrecognized family of ownership violations | 80 | The task must discover the criterion and distinguish defects from valid constructions. |
| Organize the preamble backlog into mathematical workstreams and dependency releases | 85 | Incorrect dependencies direct later work toward duplication or incompatible foundations. |
| Design the shared backend boundary used by every algebraic engine | 85 | Each later adapter will depend on its object and morphism contracts. |
| Repair generic module construction so every constructor establishes the same defining action | 90 | Specialized modules inherit the consequences of this shared construction. |
| Design category-wide enforcement of defining data and inherited method contracts | 90 | A mistaken rule can admit invalid objects or reject valid mathematical constructions throughout the preamble. |
| Redesign Cat-level construction and refinement while reconciling module, algebra, and action foundations | 100 | The task must settle the architecture that constrains all subsequent extensions. |

The topological-algebra example rises into the foundational bands if it must first redefine generic actions or internal modules.
A leaf assignment becomes lower complexity only after its required structures have clear owners and usable contracts.
The [DAG](TODO.md#remaining-workstreams-as-a-dependency-graph) records those dependencies.

## Reading the model tables

Each cell gives an inclusive recommended score interval for that model and effort combination.
These are initial repository routing recommendations, based on the risk bands above and the documented model roles.
They are not vendor benchmarks or measured success thresholds on this repository.
The sources establish model identity and effort support; the numerical intervals are local judgments.

An interval's lower endpoint indicates when that combination becomes a reasonable use of resources.
Its upper endpoint indicates when to prefer a stronger combination for independent responsibility.
Overlaps allow choices based on relevant task experience, tool access, and context continuity.
A stronger model can do easier work, but that alone does not justify assigning it there.

Select a combination whose interval contains the task score.
Within the overlap, prefer the least costly combination that has demonstrated the required semantic judgment on comparable work.
Retain a worker's useful context when reassignment would require reconstructing the difficult part of the task.
Higher effort can support deeper reasoning; it does not replace missing mathematical sources or shared contracts.

Score orchestration separately from the tasks it coordinates.
A high-complexity owner can assign a settled leaf to a lower-complexity worker.
If the leaf worker must decide a shared interface, that decision belongs in its score.
Splitting a foundational problem into small edits does not lower the responsibility for its architecture.

### Anthropic: Claude

The current versions are [Claude Opus 5](https://platform.claude.com/docs/en/models/opus-5/overview)
and [Claude Fable 5.1](https://platform.claude.com/docs/en/models/fable-5-1/overview).
Both support `low`, `medium`, `high`, `xhigh`, and `max`; both default to `high`.
These are values of `output_config.effort`.
See Anthropic's [effort documentation](https://platform.claude.com/docs/en/build-with-claude/effort).

| Model | `low` | `medium` | `high` | `xhigh` | `max` |
| --- | --- | --- | --- | --- | --- |
| Opus 5 — `claude-opus-5` | [5, 30] | [20, 50] | [40, 70] | [60, 85] | [75, 95] |
| Fable 5.1 — `claude-fable-5-1` | [20, 45] | [35, 65] | [55, 85] | [75, 95] | [85, 100] |

Use Opus for bounded delivery and integration through known contracts.
Reserve Fable's upper settings for foundational judgment and unresolved architectural work.
This allocation follows Anthropic's recommendation to use Fable for demanding reasoning beyond what higher-effort Opus handles adequately.
See the [Fable model guidance](https://platform.claude.com/docs/en/models/fable-5-1/overview).

### OpenAI: Codex

The table uses the Codex model IDs and selectable effort names.
OpenAI describes Astra as the choice for its hardest complete workflows, Sol for complex work, Terra for everyday work, and Luna for clear tasks.
Spark targets rapid coding iteration.
See the current [Codex model guide](https://learn.chatgpt.com/docs/models)
and [Astra guidance](https://developers.openai.com/api/docs/guides/latest-model).

| Model | `low` | `medium` | `high` | `xhigh` | `max` | `ultra` |
| --- | --- | --- | --- | --- | --- | --- |
| Codex Spark — `gpt-5.3-codex-spark` | [5, 15] | [10, 25] | [15, 30] | [20, 35] | — | — |
| Luna — `gpt-5.6-luna` | [5, 25] | [15, 35] | [25, 45] | [35, 50] | [40, 55] | — |
| Terra — `gpt-5.6-terra` | [15, 35] | [25, 50] | [40, 65] | [50, 75] | [60, 80] | [75, 80] |
| Sol — `gpt-5.6-sol` | [25, 50] | [40, 65] | [55, 80] | [65, 90] | [75, 95] | [75, 95] |
| Astra — `gpt-6-astra` | [35, 60] | [50, 75] | [65, 90] | [75, 95] | [85, 100] | [85, 100] |

Effort support was checked against the local Codex model catalogue, fetched on 2026-09-07.
Its source is `~/.codex/models_cache.json`, fields `slug` and `supported_reasoning_levels`.
A dash means the catalogue does not offer that combination.
This is a Codex client table; API parameter support must be checked for the specific endpoint.

`ultra` uses parallel subagents; it is not simply a deeper single-worker setting.
Use its interval only when the work contains independently assignable parts and delegation is authorized.
Use `max` for a difficult problem whose reasoning remains tightly coupled.
OpenAI documents this distinction in [Max and Ultra guidance](https://learn.chatgpt.com/docs/models#know-when-to-use-max-or-ultra).

### Coverage and calibration

Each provider independently covers the entire agent interval:

| Provider | Union of its table intervals | Lower boundary | Upper boundary |
| --- | --- | --- | --- |
| Anthropic | [5, 100] | Opus 5, `low` | Fable 5.1, `max` |
| OpenAI | [5, 100] | Spark or Luna, `low` | Astra, `max` |

The OpenAI union remains `[5, 100]` using single-worker settings alone.
Provider coverage describes the routing table; actual model access depends on the account and client.
Use another available combination covering the score when a listed combination is unavailable.

Revise a range when comparable work shows that it misprices the required judgment.
Use concrete evidence: preserved structure, correct ownership, coherent morphisms, and whether later extensions reuse the result cleanly.
Long answers, large patches, and successful mechanical checks do not establish that judgment.
Record a task-specific reason alongside the score when assigning work; the existing task or work claim is sufficient.
Refresh the model versions and effort support when offerings change, while retaining the risk-based meaning of the scale.
