from time import sleep

from fastapi.testclient import TestClient
from src.api.rest import app, tasks
from src.tests.actions import actions
from src.types import TaskStatus

client = TestClient(app)


def test_add_task():
    response = client.post(
        "/api/tasks/add",
        json={"name": "test-add-task", "id": "test-add-task", "program": []},
    )
    assert response.status_code == 200
    assert response.json() is True
    assert len(tasks.task_info) == 1
    assert tasks.task_info[0].name == "test-add-task"
    assert tasks.task_info[0].id == "test-add-task"
    assert tasks.task_info[0].program == []


def test_delay_hello_task():
    hello = actions["delay_hello"].copy(deep=True)
    hello.id = "eaf55da7-1d64-4c91-9d28-6df798c66c0a"
    response = client.post("/api/tasks/add", json=hello.dict())
    assert response.status_code == 200
    assert response.json() is True

    response = client.get("/api/tasks/info", params={"id": hello.id})
    assert response.status_code == 200
    assert response.json() is not None
    assert response.json()[0] == hello.dict()

    response = client.get("/api/tasks/status", params={"id": hello.id})
    assert response.status_code == 200
    assert response.json() is not None
    assert response.json()[0][0] == hello.id
    assert response.json()[0][1] == TaskStatus.READY.value

    response = client.get("/api/tasks/run", params={"id": hello.id})
    assert response.status_code == 200
    assert response.json() is True

    sleep(1)

    response = client.get("/api/tasks/status", params={"id": hello.id})
    assert response.status_code == 200
    assert response.json() is not None
    assert response.json()[0][0] == hello.id
    assert response.json()[0][1] == TaskStatus.SUCCESS.value
