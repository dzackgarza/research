# Replay Contract

## Exact replay route

- The implementation task must provide a single just recipe named
  `t0011-foundation-replay`.
- That recipe must replay only the frozen candidate surface from
  `tasks/T-0011/admission_target.md`.
- The recipe must use a task-local harness at
  `tasks/T-0011/computations/foundation_replay.sage`.

## Required emitted certificate

- Replay must emit a task-local certificate at
  `tasks/T-0011/outcomes/foundation_replay_certificate.md`.
- The certificate must enumerate the admitted primitives actually replayed, the exact
  backend operation named in `tasks/T-0011/dependencies.md` for each primitive, and the
  exact invariant/cross-check outputs relied on.
- The certificate must contain one explicit entry per admitted symbol; family-level or
  grouped replay claims are not sufficient.
- The certificate may not certify any blocked or ambiguous symbol from
  `tasks/T-0011/admission_target.md`.
- The certificate may not rely on implicit action models, implicit domain encodings, or
  implicit wrapper semantics not already frozen in the task artifacts.
- In the current pre-audit package, replay obligations are limited to the still-admitted
  constructor and extractor symbols only; no blocked constructor-family wrapper,
  predicate wrapper, transform wrapper, or action wrapper may appear in the certificate.

## Stop rule

- If exact replay of the frozen candidate surface cannot be expressed through this
  single task-local harness and just recipe without broadening scope, the task returns
  to `REPLAN_REQUIRED` rather than improvising additional shared harnesses.
