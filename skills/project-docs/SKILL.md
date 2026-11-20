---
name: project-docs
description: >-
  Set up or reorganize project documentation. Consolidate and archive existing
  docs, establish a README index with maintenance rules, and link it from
  AGENTS.md or CLAUDE.md for future tasks.
---

# Set Up Project Documentation

Read the [shared conventions](references/conventions.md). Follow any maintenance rules in the project's existing documentation index.

Organize the documents, then set up the index and its entry points in the project's agent instructions. For an index-only request, inspect the existing documents and limit edits to [setting up the index](#set-up-the-documentation-index).

1. Inspect the affected documents, directories, and references within the requested scope, including consumers in code, tests, scripts, configuration, and sealed artifacts. Identify purpose, readers, status, authoritative sources, and unique content before merging, moving, or removing anything.
2. Compare overlapping documents or directories by content and references. Reuse the existing topic structure where it fits. Before merging, moving, renaming, archiving, or removing existing documents or directories, present the proposed changes together. Explain what to keep, where content would go, and which references would change. Ask the user to confirm and wait for approval before applying those changes. Proceed directly with any specific changes the user has already approved.
3. Consolidate overlapping files into one maintained version, carrying over unique valid content. Revise outdated explanations and confusing structure against verified sources.
4. Move inactive documents worth retaining into the topic's archive, unless fixed-path consumers or sealed references require keeping them in place; identify such retained historical material in navigation. For mixed documents, preserve valid definitions, archive useful obsolete sections, and replace outdated action instructions in the body itself with current guidance and links to history. If a mostly obsolete document still serves a current purpose, archive its original before rewriting at the maintained path. Preserve enough context to understand archived material, reuse existing archive names, and record the date, reason, and replacement when applicable; apply the shared direction-change rules before retiring plans.
5. Update history links in the owning maintained documents. Repair incoming links, affected file consumers, and current work pointers, then remove emptied duplicate directories. Keep old-path redirects only where references cannot be updated. Preserve references needed to trace historical decisions.
6. [Set up the documentation index](#set-up-the-documentation-index), then [link it from agent instructions](#link-the-index-from-agent-instructions). Link to the index from the root README when appropriate.

Use `project-docs-human` or `project-docs-agent` as appropriate to complete substantial revisions. A writing-only task does not require reorganizing the repository.

Verify changed claims and links, affected file consumers, preservation of unique valid content, and consolidation of duplicate active versions. Confirm current documents have no duplicate or superseded action sections, and inactive records worth retaining are archived or explicitly retained in place. Follow the reader's intended routes from current entry points and confirm they reach authoritative, maintained information, with historical instructions clearly separated from current work. Report the changes and important unknowns.

## Set up the documentation index

Reuse the project's documentation index or create `docs/README.md`. Include a short title, links to key documents, and the maintenance rules. Keep detailed explanations and task updates in the linked documents.

- Add a direct link when it helps readers complete a common task, resume active work, or find an authoritative reference they regularly need. Combine entries that serve the same purpose. Link supporting material such as drafts, evidence, and individual historical records from the relevant maintained document or an existing topic index.
- Use relative links to maintained documents and put the most useful entries first. Choose link labels by what readers need to find. Add a short description if the label alone is unclear.
- When grouping entries makes the index easier to scan, give each group a heading and a table. Choose columns based on what readers need to find the right document in that group.
- For cleanup limited to a topic, update the affected entries in the existing index.

For an example of grouped tables and the rules block, see the [bundled documentation index example](references/index-example.md). Adapt the layout and links to the target project.

Keep the project's existing maintenance rules. If the index lacks them, add the [rules below](#documentation-maintenance-rules) in the project's documentation language, with the heading and list in one Markdown blockquote. Follow the affected links from the index and confirm that they reach the intended maintained documents.

> ### Documentation maintenance rules
>
> - **Update docs before closing the task.** When project behavior, an accepted decision, or plan status changes, check the documents affected by the work. Use verified information to update outdated instructions, status, or next steps in place.
> - **Keep documentation concise and useful.** Update a suitable existing document and create a new one only when it serves a distinct purpose. Keep the facts, constraints, and steps readers need. Maintain each fact in one place and link to that source where readers need it.
> - **Archive inactive records.** When a record stops guiding current work, carry valid conclusions into the maintained docs and unfinished work that still applies into the current work record. Archive historical material worth keeping under its topic. Record the date and reason, and link to the replacement if one exists. If a record must stay at its original path, mark it as historical there.
> - **Keep the index focused.** Link directly to the documents readers need for common tasks, active work, or frequently consulted guidance. Put supporting links in the relevant document. After merging, moving, or archiving a document, update or remove its index entry, repair affected references, and check where they lead.

## Link the index from agent instructions

Update each existing project-level `AGENTS.md` and `CLAUDE.md`. If the current tool's project instruction file is missing, create it at the project root using `AGENTS.md` for Codex or `CLAUDE.md` for Claude Code.

Add a short “Project documentation guide” section in the project's language, or update its existing documentation pointer in place. Link to the index with a relative Markdown link.

## Example

A mixed `docs/research/findings.md` contains applicable conclusions and past trials. Keep the conclusions in place, move historical detail into the topic's archive, and add a brief history entry at the end of `findings.md`. Reuse existing paths and archive names; this structure is illustrative.

```text
docs/
├── README.md                  # Document entry points
├── todo/
│   ├── progress.md            # Current task and its history index
│   └── archive/
│       └── past-work.md       # Historical task records
└── research/
    ├── findings.md            # Applicable conclusions and their history index
    └── archive/
        └── past-experiments.md # Past trials and superseded approaches
```
