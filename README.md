# cloud-local-demo

用来练习 **本地 Agent + 云端 Agent** 协作开发的小项目（待办 API）。

## 目标功能（验收标准）

- [x] `GET /health` 返回 `{"status":"ok"}`
- [x] `POST /todos` 创建待办（title 必填）
- [x] `GET /todos` 列出全部待办
- [x] `PATCH /todos/{id}` 可标记完成
- [x] `DELETE /todos/{id}` 删除
- [x] 有基础测试（`pytest`）

## 本地 + 云端怎么练

见 [WORKFLOW.md](./WORKFLOW.md)。

## 本地快速启动

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

常用接口示例：

```bash
curl -s http://127.0.0.1:8000/health
curl -s -X POST http://127.0.0.1:8000/todos -H 'content-type: application/json' -d '{"title":"买牛奶"}'
curl -s http://127.0.0.1:8000/todos
```

跑测试：

```bash
pytest -q
```
