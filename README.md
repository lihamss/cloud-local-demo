# cloud-local-demo

用来练习 **本地 Agent + 云端 Agent** 协作开发的小项目（待办 API）。

## 目标功能（验收标准）

- [ ] `GET /health` 返回 `{"status":"ok"}`
- [ ] `POST /todos` 创建待办（title 必填）
- [ ] `GET /todos` 列出全部待办
- [ ] `PATCH /todos/{id}` 可标记完成
- [ ] `DELETE /todos/{id}` 删除
- [ ] 有基础测试（`pytest`）

## 本地 + 云端怎么练

见 [WORKFLOW.md](./WORKFLOW.md)。

## 本地快速启动（实现完成后）

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
