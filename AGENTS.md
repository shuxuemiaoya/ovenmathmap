# MathMap Vault Security & Data Integrity Contract

本仓库是数学知识图谱核心金库（Master Vault）。所有在此目录或其子目录下操作的 Agent，必须无条件遵守以下数据安全契约：

## 1. 严格作用域边界与防误删红线 (Strict Scope Boundary)
- **禁止无作用域批量删除**：严禁在未获得用户明确书面授权的情况下，使用通配符（如 `rm -rf *`、`shutil.rmtree` 搭配全局 glob）批量删除既有章节或题库目录。
- **局部任务绝对隔离**：若当前任务仅指定了特定书籍、章节或专题，操作范围必须严格锁定在该白名单内，绝对禁止波及或清理未指定的其他分册/章节。
- **禁止静默粉碎**：任何对已有图谱目录的删除必须具备日志回溯与预检机制（`--dry-run`），严禁使用 `ignore_errors=True` 吞噬删除异常。

## 2. 变更后工作区自检门禁 (Post-Mutation Git Audit)
- 执行任何批量写入、重构或清理命令后，必须检查 `git status --porcelain`。
- 若发现非本次目标范围的文件出现意外的 `deleted` 状态，必须立即阻断后续动作并报警，绝不允许判定任务成功。

## 3. 手工编辑保护 (Preserve Manual Edits)
- 保护用户在 Obsidian 中手动添加的双链、标签、笔记批注以及 Canvas 节点排版布局，严禁无差别全量覆盖或抹除。
