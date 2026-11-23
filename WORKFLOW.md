# 本地 + 云端练习流程

## 0. 一次性准备

1. 把本仓库推到 GitHub（见下方命令）
2. 打开 https://cursor.com/agents ，连接 GitHub，选中本仓库
3. （可选）在 Cloud Agents Secrets 里加以后需要的密钥

### 推到 GitHub（在本机终端）

```bash
cd ~/code/pythonProjects/cloud-local-demo
# 先在 github.com 新建空仓库 cloud-local-demo（不要勾选 README）
git add .
git commit -m "chore: scaffold for local+cloud practice"
git branch -M main
git remote add origin git@github.com:<你的用户名>/cloud-local-demo.git
git push -u origin main
```

## 1. 本地（Local）— 定方向

在 Cursor Agent 输入框选 **Local**，说：

> 阅读 README 的验收标准，帮我确认要实现哪些接口和测试文件结构。先不要写完整实现，只列计划和文件清单。

把计划记下来（或让本地 Agent 写进 `PLAN.md`），然后 commit + push 到 `main`。

## 2. 云端（Cloud）— 实现并开 PR

输入框改成 **Cloud**，对仓库说：

> 按 README 验收标准实现 FastAPI 待办 API + pytest。在新分支开发，测试通过后开 PR。不要改无关文件。

然后你可以离开；回来后在 GitHub 打开 PR，看 diff。

## 3. 本地（Local）— 验收打磨

```bash
git fetch
git checkout <云端开出的分支名>
```

本机跑服务、用浏览器或 curl 试接口。有问题继续用 **Local** 小改，再 push。

## 4. 云端收尾（可选）

```text
/in-cloud 根据当前分支补一段 README 使用说明，并加一个简单的 GitHub Action 跑 pytest
```

最后在 GitHub 点 **Merge** 合并 PR。

## 分工口诀

- 本地：想清楚、调体验、碰真实环境
- 云端：写实现、写测试、开 PR、修 CI
- 交接：靠分支 / PR，不靠口头复述
