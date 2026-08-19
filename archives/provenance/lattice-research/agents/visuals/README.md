# Visual artifacts

This directory holds optional human-facing windows into complex systems.

Visuals crystallize structure that is too hard to understand from code, cards, or kanban
alone. They help humans provide high-level organizational and directional input when
task details are too in-the-weeds to understand at a glance.

Visuals are supporting material only. The operative state remains in tracked markdown
files under `.agents` and in git history.

Use this directory for durable visuals such as:

- Mermaid diagrams for category inheritance, subcategory-spec organization, dependency
  graphs, sprint timelines, plan-to-task breakdowns, state machines, sequence diagrams,
  and constructor routing.
- Excalidraw diagrams for spatial architecture, decision trees, whiteboarding, and
  ambiguous organization.
- Data models for tracker metadata, plan/task/decision relationships, audit-state
  models, and category/spec object relationships.
- Mockups for cheap HTML windows into sprint dashboards, audit status, category
  inheritance, constructor-routing explorers, and review checklists.

Each visual should link to the plan, task, bug, feature, decision, or PR that owns it.
Do not use this directory as an outstanding-work inventory, status system, or
replacement for tracked cards.

Current visuals:

- `category-spec-workstreams.mmd`: high-level dependency graph for category-spec
  workstream triage.
- `category-spec-plan-hierarchy.mmd`: high-level dependency graph for the category-spec program plan tree.
