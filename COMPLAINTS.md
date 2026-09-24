# Foundational Gaps and Papercuts

Record unresolved issues observed anywhere in research or contribution work.
The primary subject is general mathematical machinery that should be available but is missing, incomplete, or bypassed in the owned language.
Concrete workflow papercuts also belong here.
This is neither a retrospective work log nor a list of hypothetical defects.

Use the [mathematical tracing method](CONTRIBUTING.md#mathematical-dependency-tracing) and the capture/lifecycle rule [`DEV-59`](CONTRIBUTING.md#dev-59-record-observed-foundational-gaps-and-papercuts).
State the mathematics before its implementation symptoms.
Extend an existing entry when another consumer exposes the same foundation.
Link execution details in [TODO.md](TODO.md); it owns implementation ordering under the single-worker `DEV-61` rule.
Remove resolved entries with evidence in the commit, retaining only unfinished needs and any required terminal verification.
Durable definitions and decisions belong at their mathematical declarations or in CONTRIBUTING, not solely here.

## Foundational Mathematics

## Workflow Papercuts

Add concrete observed workflow friction here under a descriptive heading, with the user action, expected behavior, actual result, owning boundary and example.
Use `DEV-59` for capture and resolution.
Foundational mathematical gaps belong above even when first noticed as an inconvenient method or notebook interaction.

### Intended research Sage runtime needs terminal verification

- **User action:** run the repository's mandatory commit gate or regenerate the live preamble megadoc using the `SAGE_BIN` exported by the tracked `.envrc`.

- **Expected:** the tracked `.envrc` selects the intended stable research-Sage runtime and its declared dependencies; the normal just recipes can preparse and import the public session.

- **Observed:** on 2026-09-15 the source-checkout `sage`/`sage-preparse`
  launcher resolved into `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src` and
  failed with `ModuleNotFoundError: No module named 'sage'`. Current `.envrc`
  instead defaults to `/home/dzack/gitclones/sage-dev-allopts/.venv/bin/sage`.
  Source inspection confirms that changed launch path, not its successful runtime
  behavior. `research-sage-runtime` in TODO owns the terminal verification and
  any reproduced repair; the historical launcher failure alone does not justify
  another installation or reverting this path.

- **Owner:** research-Sage runtime/environment provisioning and the tracked `.envrc` contract.

- **Example:** observed when banking the resumed architecture-remediation DAG on 2026-09-15; the commit gate reached `_sage-syntax` and then failed inside the stub-tree `sage-preparse`.
