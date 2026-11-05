# Shared Documentation Conventions

These conventions apply to project documentation and working records.

## Shared principles

- Keep the smallest useful document set. Update an appropriate existing document before creating one with a genuinely separate purpose.
- Write for the intended reader. Human-facing documents also guide AI work; execution notes add task context without creating a third collaboration version.
- Maintain one authoritative source per fact. Link to detailed definitions and actual configuration instead of copying them; retain only the summary a reader needs.
- Distinguish verified behavior, accepted goals, proposals, and unknowns. Resolve or flag conflicting sources rather than silently overwriting one.
- Revise current documents in place, preserving valid facts, requirements, decisions, and constraints. Merge repeated content and replace superseded status and next actions in the affected sections rather than appending another dated update.
- Working records become historical when they stop guiding current work, regardless of age or whether every original task was completed. Archive inactive records and useful superseded sections; retain only the information needed to find them in current navigation. Reuse existing reports or records for details instead of duplicating them.
- Keep a brief history index at the end of the maintained document whose content was archived: enough identifying information, a status or conclusion, and a record link. Keep `docs/README.md` focused on document entry points; leave individual history entries in their owning documents. Topic and archive directories need no additional README files.
- Report routine maintenance checks in the response. Persist validation details only when needed for subsequent work or explicitly requested.

## Changes of direction

- If the goal remains the same, update the existing plan and briefly explain material changes while preserving completed-work facts.
- If the goal or core approach changes, mark the old plan as terminated or superseded. Record the reason, actual completed work, cancelled work, and the destination of anything still relevant. Carry continuing work into its current record before retiring the old plan; link a replacement when one exists, without inventing follow-up work.
