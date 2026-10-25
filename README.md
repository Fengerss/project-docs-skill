# Project Docs Plugin 草稿

一个用于新建、更新和审查项目文档的 Codex / Claude Code 插件。核心技能会先核对项目现状，帮助写出简洁、准确、易读的文档，并将当前状态与 ADR 决策历史分开。

本项目仍在修改阶段。英文技能入口位于 skills/project-docs/SKILL.md；中文对照稿在 docs/SKILL.zh-CN.md。

## Codex

在 Codex 插件界面 /plugins 添加 GitHub marketplace Fengerss/project-docs-skill，选择并安装 Project Docs，然后新开会话。

CLI：
codex plugin marketplace add Fengerss/project-docs-skill
codex plugin add project-docs@project-docs-marketplace

## Claude Code

claude plugin marketplace add Fengerss/project-docs-skill
claude plugin install project-docs@project-docs-marketplace

开发时也可从克隆目录临时加载：claude --plugin-dir .

技能命令：/project-docs:project-docs

## 仓库可见性

GitHub 仓库当前为私有。安装和更新的人都需要有该仓库的访问权限，并在对应客户端完成 GitHub 认证。
