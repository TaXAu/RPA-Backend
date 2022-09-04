from typing import Optional
from src.types import TaskModel
from src.web.web_rpa import web_functions_easy as web

all_functions = web


class Parser(object):
    def __init__(self, task: Optional[TaskModel]):
        self.id = task.id
        self.name = task.name
        self.program = task.program

    def run(self):
        for step in self.program:
            func_name = step.name
            func_paras = step.paras
            if func_name in all_functions:
                all_functions[func_name](**func_paras)
            else:
                raise Exception(f"function '{func_name}' not found")
