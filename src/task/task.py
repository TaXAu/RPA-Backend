from typing import Optional, List, Tuple
from multiprocessing import Process
from src.types import TaskModel
from src.types import TaskStatus
from src.types import TaskID
from src.parser import Parser


class Task(object):
    def __init__(self, task_info: Optional[TaskModel] = None):
        self._task_process = None
        self.info: Optional[TaskModel] = task_info
        self.id: TaskID = task_info.id
        self.status: TaskStatus = TaskStatus.INITIAL
        if task_info is None:
            self.status = TaskStatus.INIT_ERROR

    def is_started(self) -> bool:
        """Judge whether the task is running.

        Returns:
            bool:
                True if the task is running or pending,
                False otherwise.
        """
        return self.status == TaskStatus.RUNNING or TaskStatus.PENDING

    def is_over(self) -> bool:
        """Judge whether the task is finished.

        Returns:
            bool:
                True if the task is either success or failed,
                False otherwise.
        """
        return self.status == TaskStatus.SUCCESS or TaskStatus.FAILED

    def __child_process_entry(self):
        """Entry point of the child process of the task."""
        Parser(self.info).run()

    def exec(self):
        """Execute the task thread."""
        if self.status == TaskStatus.READY:
            self._task_process = Process(target=self.__child_process_entry)
            self._task_process.start()

    def stop(self):
        """Stop the task thread."""
        pass


class TaskQueue(object):
    def __init__(self):
        self._tasks: List[Task] = []

    def __find_task(self, id: TaskID) -> Optional[Task]:
        for task in self._tasks:
            if task.id == id:
                return task
        return None

    @property
    def task_info(self) -> List[TaskModel]:
        return list(map(lambda task: task.info, self._tasks))

    @property
    def task_status(self) -> List[Tuple[TaskID, TaskStatus]]:
        return list(map(lambda task: (task.id, task.status), self._tasks))

    def add(self, program: TaskModel) -> bool:
        self._tasks.append(Task(program))
        return True

    def exec(self, id: TaskID) -> bool:
        task = self.__find_task(id)
        if task is None:
            return False
        elif task.status == TaskStatus.READY:
            task.exec()
            return True
        else:
            return False

    def stop(self, id: TaskID) -> bool:
        task = self.__find_task(id)
        if task is None:
            return False
        elif task.is_started():
            task.stop()
            return True
        else:
            return False

    def status(self, id: TaskID) -> Optional[TaskStatus]:
        task = self.__find_task(id)
        if task is None:
            return None
        else:
            return task.status

    def remove(self, id: TaskID) -> bool:
        task = self.__find_task(id)
        if task is None:
            return False
        elif task.is_started():
            return False
        else:
            self._tasks.remove(task)
            return True

    def __del__(self):
        """
        manually terminate all the child processes
        """
        for task in self._tasks:
            if task.is_started():
                task.stop()
