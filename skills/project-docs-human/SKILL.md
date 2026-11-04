---
name: project-docs-human
description: >-
  Write, update, and review human-facing project explanations, guides, design,
  specifications, and status. Use when people need to understand the project,
  complete an operation, or assess a decision; AI can use the same documents.
---

# Write Project Documentation for People

Read the [shared conventions](../project-docs/references/conventions.md).

- Identify what the reader needs to understand or do. Ask only when missing information materially changes the result.
- Lead with a brief conclusion, outcome, key change, or action so readers can grasp the main point on a skim.
- Extract parallel findings, conditions, problems, or recommendations into scannable bullets. Choose the number of items to suit the content, without a fixed count. Each item should make one point, starting with a concise takeaway and adding only the explanation or evidence it needs. Use numbered lists for ordered steps.
- Add a short explanatory paragraph after the key points when it helps connect causes, relationships, or context. Keep each paragraph focused on one main point and add information rather than repeating the list.
- Use plain language, explain necessary terms, and connect technical details to their implications. Remove repetition and irrelevant background while preserving essential context, conditions, evidence, and limitations.
- When revising, simplify and reorganize the body itself; add an overview or reading guide only when navigation still needs one.
- Explain responsibilities, relationships, and reasons in design documents; provide usable steps and expected results in guides. Choose the structure for the reader rather than forcing a template.
- Summarize current status through verified milestones, outcomes, and meaningful blockers. Keep task execution detail in working records.

Check changed claims, examples, and links against their sources. Update the relevant entry point if navigation changes, and report important facts that remain unverified.

## Example

Fictional report section; adapt the structure and number of points to the content.

```markdown
**The trial improved matching accuracy, with slower responses.**

- **Accuracy:** Correct matches rose from 8/10 to 9/10 on the same test set.
- **Speed:** Average response time rose from one to two seconds.

The new flow performs an extra lookup, which explains the delay. Before adopting it, decide whether the accuracy gain justifies the extra wait.
```
