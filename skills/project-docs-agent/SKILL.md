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
- Focus the work record on the current task, last verified state, blockers, and next action. For time-sensitive progress, record the observation time and distinguish the snapshot from facts that must be rechecked when resuming.
- Make next actions and required checks concrete. For interrupted or running work, identify the first check and existing status sources or checkpoints; explain how the results determine whether to wait, resume, or stop within applicable authorization and limits. Check documented commands against available scripts and configuration; retain questions needing a human decision.
- Summarize only the verified work and validation results needed to resume. Distinguish what was implemented from what was validated. Place references needed for the next action beside that action.

Recheck references and commands, then report the changes and important unknowns.

## Example

Adapt this fictional handoff to the task.

```markdown
**Current task: fix large-file imports.**

- **Verified:** Small files import successfully; large files run out of memory.
- **Next action:** Measure peak memory use in the import path.
```
