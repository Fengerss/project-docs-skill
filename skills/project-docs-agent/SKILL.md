---
name: project-docs-agent
description: >-
  Write, update, and review AI-facing execution plans, task handoffs, and working
  notes. Use when an agent needs concrete next steps, validation details, or
  enough current context to resume project work.
---

# Write AI Working Documents

Read the [shared conventions](../project-docs/references/conventions.md).

- Read the existing task context and link the project documents that govern the work. State the objective, scope, and completion conditions.
- Reuse the current work record and keep it focused on the current task, last verified state, blockers, and next action. For time-sensitive progress, record the observation time and distinguish the snapshot from facts that must be rechecked when resuming.
- Make next actions and required checks concrete. For interrupted or running work, identify the first check and existing status sources or checkpoints; explain how the results determine whether to wait, resume, or stop within applicable authorization and limits. Check documented commands against available scripts and configuration; retain questions needing a human decision.
- Summarize only verified work and validation results needed to resume. Keep conclusions that still govern current actions; refer to the history index or source records for past task details. Place references needed for the next action beside that action.
- Update the record when work materially changes. Distinguish implementation from validation, replace stale next steps, and apply the shared direction-change rules rather than appending an interaction diary.

Recheck references and commands, then report the changes and important unknowns.

## Example

Fictional current handoff after archiving a completed comparison; adapt the fields and number of points to the task.

```markdown
**Current task: fix large-file imports.**

- **Verified:** Small files import successfully; large files run out of memory.
- **Next action:** Measure peak memory use in the import path.

## History index

- Import-format comparison | Completed; existing format retained | archive/past-work.md
```
