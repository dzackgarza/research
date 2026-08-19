# Research Orchestration Reference

## Delegation contract completeness

Subagents do not know what a tracker key, task ID, plan label, or chat-local name means unless that meaning is provided in the delegation contract or recoverable from an explicitly named artifact they are told to read.

Before delegating, provide the exact task statement or tracker/card body, concrete files or directories in scope, allowed and forbidden actions, expected output format, and exit condition.

Do not assume a subagent can infer hidden intent from the current chat, a tracker key, or the orchestrator's private context. If the task definition matters, quote it or attach the durable artifact containing it.

## Worktree policy

At most one worktree is active at any time. Do not create a second worktree while one exists. Check with `git worktree list` before creating.

Every worktree branches cleanly off the current tip of `main` with `git worktree add .worktrees/<name> -b <name> main`.

When the task is done, merged, or abandoned, remove the worktree immediately with `git worktree remove .worktrees/<name> && git branch -d <name>`.

Never leave a stale worktree behind. If a worktree exists at session startup with no active task, remove it.

## Durable artifact rule

If you are an orchestrating agent, commit outputs to permanent artifacts: memories, files, and git commits when authorized. Do not report artifacts and findings only in chat because chat summaries are lossy.

## Poisoned work policy

Never repair code that violates audits. Repairing poisoned code creates polishing and whittling behavior. Delete poisoned code after reading it into context, preserve recoverability through git when required, and delegate a ground-up rewrite of the poisoned parts.

Motto: excise and rewrite, never iterate on poisoned code.

## Project lens

The goal is substantive mathematical work with trustworthy independent verification, not maximum visible activity. Apply delegation through the lens of mathematical value: real uncertainty reduced, real claims checked, and real downstream trust improved.

If a task is blocked because the semantic base lacks the right noun, method, morphism, coercion, or interop bridge, load `research-state-machine` and treat that as a task-boundary failure. Surface the need for a base card plus a redesigned dependent card; do not patch around it locally.
