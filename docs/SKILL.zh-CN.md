# Project Docs 使用指南

本文件供人阅读，说明如何选择 skill。三个 skill 和[共用文档约定](../skills/project-docs/references/conventions.md)的执行版本均为英文；完整中文对照见下表，供阅读与审阅，执行以英文为准。

## 选择任务

| 你的需求 | 使用哪个 skill |
| --- | --- |
| 整理和归档项目文档，建立带守则的索引并接入代理指令 | [project-docs](../skills/project-docs/SKILL.md) |
| README、教程、架构、设计、规格或项目状态让人看得懂 | [project-docs-human](../skills/project-docs-human/SKILL.md) |
| AI 的执行计划、任务交接、工作记录和验证细节 | [project-docs-agent](../skills/project-docs-agent/SKILL.md) |

完成文档基建后，后续任务可从 `AGENTS.md` 或 `CLAUDE.md` 找到索引，按索引中的守则维护文档。需要撰写或大幅修订正文时，按受众选择写作技能。

## 中文对照

| 英文执行版 | 中文对照版 |
| --- | --- |
| [project-docs](../skills/project-docs/SKILL.md) | [项目文档基建](skills/project-docs.zh-CN.md) |
| [project-docs-human](../skills/project-docs-human/SKILL.md) | [写给人看](skills/project-docs-human.zh-CN.md) |
| [project-docs-agent](../skills/project-docs-agent/SKILL.md) | [写给 AI 看](skills/project-docs-agent.zh-CN.md) |
| [共用文档约定](../skills/project-docs/references/conventions.md) | [共用文档约定](skills/conventions.zh-CN.md) |

中文稿是英文规则的对照翻译，不单独扩展规则。修改执行规则时，在同一次修改中同步对应中文稿；三个技能仍只引用英文共用约定，避免同时加载两种语言的相同内容。

## 典型请求

- “用 `project-docs` 整理项目文档，归档失效计划，建立带整理守则的文档索引，再从项目的代理指令链接到索引。”
- “更新现有架构说明，让新成员理解模块职责和已确认的取舍；不复制数据契约。”
- “收敛 AI 工作记录，只留下已核实的完成情况、当前阻塞、下一步和必要资料入口。”
- “计划做了一半但方向变了，请区分实际完成、取消和仍需继续的事项，更新工作入口后归档旧计划。”

## 试用样例

[试用项目](../tests/fixtures/docs-cleanup/README.md) 保留了过时说明和工作记录，便于验证整理结果。将它复制到临时目录，再请 `project-docs` 按已接受的决策整理文档并建立文档基建。技能会先提出归档方案，待确认后再移动旧计划。

核对结果：说明应符合实际源码和配置；已接受的 ADR 与应用代码保持原样；被替代但未全部实施的旧计划应归档且不能标成全部完成；仍需完成的文档核对事项应保留在当前工作记录，相关链接应可用。

确认 `docs/README.md` 包含现行文档入口和整理守则，当前工具的项目指令文件指向该索引。
