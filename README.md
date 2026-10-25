# Project Docs

一个面向 Codex 和 Claude Code 的项目文档插件。它帮助新建、更新和审查项目说明、架构/设计文档、规则与术语表：先核对代码和现有资料，再写清晰、精简、准确的当前状态；需要保留的长期决策单独记录为 ADR。

## 包含内容

- `skills/project-docs/SKILL.md`：Codex 与 Claude Code 共用的技能入口。
- `docs/SKILL.zh-CN.md`：中文阅读稿。
- `.agents/plugins/marketplace.json`：Codex marketplace 清单。
- `.claude-plugin/plugin.json`、`.claude-plugin/marketplace.json`：Claude Code 插件和 marketplace 清单。

## 安装到 Codex

在 Codex 桌面插件页添加 GitHub 来源 `Fengerss/project-docs-skill` 并安装 **Project Docs**。Codex CLI 可运行：

```sh
codex plugin marketplace add Fengerss/project-docs-skill
codex plugin add project-docs@project-docs-marketplace
```

## 安装到 Claude Code

```sh
claude plugin marketplace add Fengerss/project-docs-skill
claude plugin install project-docs@project-docs-marketplace
```

开发时可以从克隆目录临时加载：

```sh
claude --plugin-dir .
```

Claude Code 中可通过 `/project-docs:project-docs` 显式调用。

## 许可

本项目采用 MIT License，详见 `LICENSE`。