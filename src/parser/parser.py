from typing import Optional
from src.types import TaskModel


class Parser(object):
    def __init__(self, task: Optional[TaskModel], toml_file: str, json_file: str):
        self.id = task.id
        self.name = task.name
        self.program = task.program
        self.vars = {}

    def step(self):
        pass

    def run(self):
        pass
