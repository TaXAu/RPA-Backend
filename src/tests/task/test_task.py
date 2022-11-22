import json
from src.task.task import Task
from src.types import TaskModel, TaskStatus


def test_task_hello():
    # read json files
    with open("src/tests/actions/hello.json", "r") as f:
        task_info = TaskModel(**json.load(f))
    t = Task(task_info=task_info)
    t.run()
    assert t.status == TaskStatus.SUCCESS
    assert t.parser.end
    assert not t.parser.fail
    assert t.parser.step == len(task_info.program)
    assert t.parser.vars["log"] == "Hello World!"
