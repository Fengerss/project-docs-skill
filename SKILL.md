---
name: project-docs
description: >-
  Create, update, and review repository documentation, especially project guides,
  architecture and design docs, rules, and glossaries. Use when documentation must
  reflect verified project facts and stay readable and concise.
---

# Project Docs

Help people and future contributors understand the project through a small, accurate set of documents. Follow repository-specific conventions when they exist.

## Establish the facts

- Read relevant project guidance and existing documentation first; inspect source code, configuration, tests, or other authoritative materials to verify claims.
- Identify the intended reader and what they need to learn or do. If that is unclear and changes the content materially, ask; otherwise make a reasonable choice and state it briefly.
- Describe current, verified behavior and structure. Mark unresolved details as unverified instead of filling gaps with guesses.

## Write for people

- Lead with the purpose and practical information. Prefer clear language, explain necessary terms, and include only the architecture or implementation detail needed by the reader.
- Create the smallest useful document set. Use the README as a concise entry point when the project has one; link to focused pages only when they add value.
- Keep each fact in one authoritative place. Avoid duplicated explanations, task diaries, speculative plans, and lengthy lists of prohibitions or caveats.

## Keep current state separate from history

- Keep active project guides and architecture docs focused on how the project works now. Do not turn them into change logs or preserve superseded approaches as if they were current.
- When a lasting decision or its trade-offs need preserving, record it separately as an ADR or in the repository's existing decision-history format, then link to it only where useful. Do not create a decision record for every routine change.

## Review and maintain

- Compare existing documentation with the verified project state. Correct stale claims and broken links; consolidate clear duplication without rewriting unrelated material.
- For project overviews, architecture/design docs, rules, or glossaries, choose a structure that serves the reader rather than forcing every document into one template.
- After editing, recheck changed claims and links against their sources. Report the files changed and any material facts that remain unverified.