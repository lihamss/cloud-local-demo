"""待办 API 入口。

当前只有占位健康检查。完整 CRUD 留给云端 Agent 在 PR 里实现。
"""

from fastapi import FastAPI

app = FastAPI(title="cloud-local-demo", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
