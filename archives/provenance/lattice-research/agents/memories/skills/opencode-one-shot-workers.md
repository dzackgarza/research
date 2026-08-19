---
title: Opencode One-Shot Workers
status: active
date: 2026-05-29
---
# Opencode One-Shot Workers

Use this skill when a task is too large or independent to keep on the critical path, but
still small enough to hand to a single cheap worker in one shot.

## Source of truth

- `research-orchestration` still owns delegation contracts and artifact rules.
- `opencode-cli` still owns OpenCode CLI environment traps.
- This skill is the repo-local overlay for cheap parallel one-shot workers.

## Core policy

- Treat these workers as cheap parallel task executors, not as glorified shell aliases.
- Use them for one atomic leaf that can plausibly finish without another round of
  clarification from the main agent.
- Prefer narrow, opinionated worker agents with a clear job and a matching tool surface.
- Watch progress through PTY output instead of waiting blindly when the task matters to
  the current turn.
- Keep the main agent on orchestration, review, and integration work.
  Do not offload the whole problem.
- Massively parallel bounded work is fine and encouraged when the leaves are genuinely
  independent.

## Good use cases

- Attempt one tracker leaf that is already well-scoped and locally unblockable.
- Execute a contained refactor in a known file set.
- Implement one method family or one interface slice with clear acceptance criteria.
- Perform a bounded analysis pass whose output is a concise report or patch.

## Bad use cases

- Reading a few files for you.
- Mechanical line edits across many files when the main agent can do them directly.
- Tasks likely to require iterative clarification, user feedback, or strategy changes
  midway through execution.
- Overscoped cards hiding multiple distinct subtasks, major design decisions, or missing
  prerequisites.

## Git and acceptance hygiene

- Make a careful checkpoint before dispatching a large batch of workers.
- Review the resulting git diff carefully before accepting worker output.
- Treat worker output as provisional until the diff and evidence look right.
- If a worker produces noisy or mis-scoped changes, prefer discarding that run over
  rationalizing the output into acceptance.

## Worker selection

- Prefer cheaper and faster workers for lighter bounded leaves.
- If a worker needs a custom prompt or permission surface, define a dedicated primary
  agent in `~/ai/opencode/agents/*.md`.
- On this system, `command opencode` rereads config on each invocation, and agent
  markdown files in `~/ai/opencode/agents/` are picked up automatically.
- For one-shot CLI use, the agent must be `mode: primary`. `run --agent` will reject a
  `mode: subagent` agent and fall back.
- If you adapt a subagent-style prompt for CLI worker use, clone it as a separate
  `*-primary` agent instead of mutating the original subagent role.

## Contract requirements

Every one-shot worker prompt must include:

- The exact task statement.
- The file or directory scope.
- Allowed and forbidden actions.
- The expected output format.
- The exit condition or acceptance check.

Do not launch a worker with a vague "look into this" prompt when a concrete leaf was
available.

## Standard PTY pattern

In this harness, launch the worker in a PTY and poll it:

```text
functions.exec_command({
  "cmd": "command opencode run --agent <agent-primary> --format json --thinking '<task prompt>'",
  "workdir": "<repo>",
  "tty": true
})
```

Then poll with `functions.write_stdin` until completion.
`--format json` plus `--thinking` yields incremental JSON events on stdout, so PTY
polling can see real progress instead of only the final answer.

Expect events like:

- `step_start`
- `reasoning`
- `text`
- `step_finish`

## Repeated one-shots

- For atomic tasks, repeated clean one-shots are often better than trying to coach the
  same worker through several correction rounds.
- If the task is small enough and the contract was clear enough, use judgment: it can be
  more effective to discard the run, tighten the prompt, and relaunch.
- Do not do this reflexively for complex tasks that have already accumulated valuable
  local context.

## Prompt shape

Use prompts that force narrow execution:

- State the single task first.
- State the exact scope second.
- State explicit prohibitions third.
- State the required final artifact or answer shape last.

Example skeleton:

```text
Handle exactly this task: <task>.
Scope: <paths>.
Do not broaden scope, do not touch files outside scope, and stop on blockers.
Return: <patch/report/tests run/remaining blocker>.
```

## Environment traps

- Use `command opencode`, not a shell alias.
- Prefer non-attached `command opencode run` for specific agent one-shots.
- `--attach` plus `--agent` is a known broken path in local guidance.
- Do not use the shared user service for experiments when a repo-local server is
  required.

## Worktree policy

- For more complex delegated implementation tasks, consider putting the worker in a
  dedicated git worktree so the contribution can be reviewed as a unit.
- Once a worktree owns that task stream, it is fine to dispatch multiple worker runs
  back into the same worktree.
- Use good cleanup hygiene: remove stale worktrees when their task stream is truly
  complete or intentionally abandoned.

## Review rule

- Do not trust worker success claims without checking the artifact.
- Review the diff, report, or test evidence before integrating the result.
- If the worker drifted, produced theater, or solved a different problem, discard the
  result and tighten the contract instead of patching around the drift.
