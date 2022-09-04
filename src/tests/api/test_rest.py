from fastapi.testclient import TestClient
from src.api.rest import app, tasks

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
