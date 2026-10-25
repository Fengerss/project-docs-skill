---
name: project-docs
description: >-
  Organize project documentation: consolidate duplicates, maintain docs/README.md,
  repair references, and archive inactive working records. Use for documentation
  structure and lifecycle maintenance; use the writing skills for substantial
  content changes.
---

# Organize Project Documentation

Read the [shared conventions](references/conventions.md).

1. Inspect the affected documents and their references. Identify purpose, readers, status, authoritative sources, and any unique content before merging or removing files.
2. Keep useful topic-based organization and existing names. Create directories only when needed; apply the shared principles to decide what to retain, consolidate, or retire.
3. Maintain `docs/README.md` as a curated set of current entry points with purpose, readers, and status where useful. Link it from the root README when appropriate; add local indexes only when navigation becomes difficult.
4. Move useful inactive records into the relevant topic's archive, reusing its existing naming convention. Record the archive date, reason, and replacement when applicable; apply the shared direction-change rules before retiring plans.
5. Repair incoming links and current work pointers after moves or replacements. Preserve references needed to trace historical decisions.

Use `project-docs-human` for substantial human-facing writing and `project-docs-agent` for AI working documents. A writing-only task does not require reorganizing the repository.

Verify changed claims and references, then report the changes and important unknowns. Keep changes within the requested documentation scope.
