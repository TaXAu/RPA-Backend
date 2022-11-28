from src.task.task import TaskQueue
from src.tests.actions import actions
from src.types import TaskID, TaskStatus, TaskModel
from time import sleep

hello: TaskModel = actions["hello"]
delay_hello: TaskModel = actions["delay_hello"]


class TestTaskQueue:
    def test_add_task(self):
        queue = TaskQueue()
        for i in range(10):
            hello_i = hello.copy(deep=True)
            hello_i.id = f"hello_{i}"
            queue.add(hello_i)
        assert len(queue.task_info) == 10

    def test_run_task(self):
        queue = TaskQueue()
        for i in range(10):
            hello_i = hello.copy(deep=True)
            hello_i.id = TaskID(f"hello_{i}")
            queue.add(hello_i)
            assert queue.status(hello_i.id) == TaskStatus.READY
            queue.run(hello_i.id)
            sleep(0.1)
            assert queue.status(hello_i.id) == TaskStatus.SUCCESS
        assert len(queue.task_info) == 10

    def test_task_statue(self):
        queue = TaskQueue()
        assert queue.add(delay_hello)
        assert queue.status(delay_hello.id) == TaskStatus.READY
        assert queue.run(delay_hello.id)
        sleep(0.1)
        assert queue.status(delay_hello.id) == TaskStatus.RUNNING
        sleep(1)
        assert queue.status(delay_hello.id) == TaskStatus.SUCCESS
