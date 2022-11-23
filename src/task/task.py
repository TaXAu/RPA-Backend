from typing import Optional, List, Tuple
from src.types import TaskModel
from src.types import TaskStatus
from src.types import TaskID
from src.parser import Parser
from threading import Thread
from typing import Dict
import logging


class Task(object):
    def __init__(self, task_info: Optional[TaskModel] = None):
        self.info = task_info
        self.step = False  # if step mode
        self.step_flag = False  # if stepped
        self.stop_flag = False  # if force to stop
        self.thread = None
        logging.debug(f"Task {self.info.id} created. " f"Step Mode: {self.step}.")
        if task_info is None:
            self.status = TaskStatus.INIT_ERROR
            logging.error(f"Task {self.info.id} init error.")
        else:
            self.status: TaskStatus = TaskStatus.INITIAL
            logging.debug(f"Task {self.info.id} init success.")
        self.parser = Parser(task_info)
        self.status = TaskStatus.READY
        logging.info(f"Task {self.info.id} ready.")

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

    def _thread_entry(self):
        """
        Execute one step of the task.
        """
        if self.status == TaskStatus.READY:
            self.status = TaskStatus.RUNNING
            logging.info(f"Task {self.info.id} started.")
            while (
                self.status != TaskStatus.SUCCESS and self.status != TaskStatus.FAILED
            ):
                if not self.step:
                    self.parser.run()
                elif self.step_flag:
                    self.parser.run()
                    self.step_flag = False
                else:
                    self.status = TaskStatus.PENDING
                    logging.info(f"Task {self.info.id} pending.")

                if self.parser.fail:
                    self.status = TaskStatus.FAILED
                    logging.error(f"Task {self.info.id} failed.")
                elif self.parser.end:
                    self.status = TaskStatus.SUCCESS
                    logging.info(f"Task {self.info.id} success.")
                elif self.status != TaskStatus.PENDING:
                    self.status = TaskStatus.RUNNING

                if self.stop_flag and self.status != TaskStatus.SUCCESS:
                    self.status = TaskStatus.FAILED
                    logging.error(f"Task {self.info.id} force to stop, task failed.")
                    break

    def run(self):
        """Execute the task."""
        self.thread = Thread(target=self._thread_entry)
        self.thread.start()

    def stop(self):
        """Stop the task."""
        self.stop_flag = True


class TaskQueue(object):
    def __init__(self):
        self._tasks: Dict[TaskID, Task] = {}

    # def _find_task(self, id: TaskID) -> Optional[Task]:
    #     for task in self._tasks:
    #         if task.info.id == id:
    #             return task
    #     return None

    @property
    def task_info(self) -> List[TaskModel]:
        return [task.info for _, task in self._tasks.items()]

    @property
    def task_status(self) -> List[Tuple[TaskID, TaskStatus]]:
        return [(task.info.id, task.status) for _, task in self._tasks.items()]

    def add(self, program: TaskModel) -> bool:
        if program.id in self._tasks:
            return False
        else:
            self._tasks[program.id] = Task(program)
            return True

    def run(self, id: TaskID) -> bool:
        if id not in self._tasks:
            return False
        elif self._tasks[id].status == TaskStatus.READY:
            self._tasks[id].run()
            return True
        else:
            return False

    def stop(self, id: TaskID) -> bool:
        if id not in self._tasks:
            return False
        elif self._tasks[id].is_started():
            self._tasks[id].stop()
            return True
        else:
            return False

    def status(self, id: TaskID) -> Optional[TaskStatus]:
        if id not in self._tasks:
            return None
        else:
            return self._tasks[id].status

    def remove(self, id: TaskID) -> bool:
        if id not in self._tasks:
            return False
        elif self._tasks[id].is_started():
            return False
        else:
            del self._tasks[id]
            return True
