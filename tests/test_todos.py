from fastapi.testclient import TestClient

from app.main import app, reset_store

client = TestClient(app)


def setup_function() -> None:
    reset_store()


def test_create_todo_requires_title() -> None:
    response = client.post("/todos", json={})
    assert response.status_code == 422


def test_create_and_list_todos() -> None:
    created = client.post("/todos", json={"title": "买牛奶"})
    assert created.status_code == 201
    body = created.json()
    assert body["id"] == 1
    assert body["title"] == "买牛奶"
    assert body["completed"] is False

    listed = client.get("/todos")
    assert listed.status_code == 200
    assert listed.json() == [body]


def test_patch_marks_completed() -> None:
    created = client.post("/todos", json={"title": "写测试"})
    todo_id = created.json()["id"]

    patched = client.patch(f"/todos/{todo_id}", json={"completed": True})
    assert patched.status_code == 200
    assert patched.json()["completed"] is True
    assert patched.json()["title"] == "写测试"


def test_patch_missing_todo_returns_404() -> None:
    response = client.patch("/todos/999", json={"completed": True})
    assert response.status_code == 404


def test_delete_todo() -> None:
    created = client.post("/todos", json={"title": "临时任务"})
    todo_id = created.json()["id"]

    deleted = client.delete(f"/todos/{todo_id}")
    assert deleted.status_code == 204

    listed = client.get("/todos")
    assert listed.json() == []


def test_delete_missing_todo_returns_404() -> None:
    response = client.delete("/todos/999")
    assert response.status_code == 404
