"""待办 API：内存存储的 CRUD。"""

from __future__ import annotations

from itertools import count
from typing import Annotated

from fastapi import FastAPI, HTTPException, Path, status
from pydantic import BaseModel, Field

app = FastAPI(title="cloud-local-demo", version="0.1.0")

_id_seq = count(1)
_todos: dict[int, "Todo"] = {}


class TodoCreate(BaseModel):
    title: str = Field(min_length=1, description="待办标题，必填")


class TodoUpdate(BaseModel):
    completed: bool | None = None
    title: str | None = Field(default=None, min_length=1)


class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/todos", response_model=Todo, status_code=status.HTTP_201_CREATED)
def create_todo(payload: TodoCreate) -> Todo:
    todo_id = next(_id_seq)
    todo = Todo(id=todo_id, title=payload.title.strip(), completed=False)
    if not todo.title:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="title must not be blank",
        )
    _todos[todo_id] = todo
    return todo


@app.get("/todos", response_model=list[Todo])
def list_todos() -> list[Todo]:
    return sorted(_todos.values(), key=lambda t: t.id)


@app.patch("/todos/{todo_id}", response_model=Todo)
def update_todo(
    todo_id: Annotated[int, Path(ge=1)],
    payload: TodoUpdate,
) -> Todo:
    todo = _todos.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="todo not found")

    data = payload.model_dump(exclude_unset=True)
    if "title" in data:
        title = data["title"].strip()
        if not title:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="title must not be blank",
            )
        data["title"] = title

    updated = todo.model_copy(update=data)
    _todos[todo_id] = updated
    return updated


@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: Annotated[int, Path(ge=1)]) -> None:
    if todo_id not in _todos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="todo not found")
    del _todos[todo_id]


def reset_store() -> None:
    """测试用：清空内存数据并重置 id 序列。"""
    global _id_seq
    _todos.clear()
    _id_seq = count(1)
