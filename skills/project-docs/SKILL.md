---
name: project-docs
description: >-
  Organize, revise, and refactor project documentation: consolidate overlapping
  files and directories, maintain docs/README.md, repair references, and archive
  inactive records. Use for structure, lifecycle, and outdated-content cleanup;
  use the writing skills as needed for substantial revisions.
---

# Organize and Refactor Project Documentation

Read the [shared conventions](references/conventions.md).

1. Inspect the affected documents, directories, and references within the requested scope. Identify purpose, readers, status, authoritative sources, and unique content before merging or removing anything.
2. Compare directories with similar purposes by content and references. Present the differences and a recommended destination, then ask which directory to keep before merging unless the user has already chosen. Reuse useful topic-based organization and create directories only when needed.
3. Consolidate overlapping files into one maintained version, carrying over unique valid content. Revise outdated explanations and confusing structure against verified sources.
4. Move inactive documents worth retaining into the topic's archive. For mixed documents, archive useful obsolete sections and revise the remaining body. If a mostly obsolete document still serves a current purpose, archive its original before rewriting at the maintained path. Preserve enough context to understand archived material, reuse existing archive names, and record the date, reason, and replacement when applicable; apply the shared direction-change rules before retiring plans.
5. Maintain `docs/README.md` as a concise guide to current entry points, with purpose, readers, and status where useful. Group historical navigation behind existing topic or archive entry points. Link from the root README when appropriate; add local indexes only when navigation becomes difficult.
6. Repair incoming links and current work pointers, then remove emptied duplicate directories. Keep old-path redirects only where references cannot be updated; preserve references needed to trace historical decisions.

Use `project-docs-human` or `project-docs-agent` as appropriate to complete substantial revisions. A writing-only task does not require reorganizing the repository.

Verify changed claims and links, preservation of unique valid content, and consolidation of duplicate active versions. Confirm inactive records worth retaining are archived and current entry points lead to maintained documents. Report the changes and important unknowns.
