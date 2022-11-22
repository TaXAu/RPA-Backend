import logging
from typing import Optional
from src.types import TaskModel, ModuleResultCode
from src.modules import modules


class Parser(object):
    def __init__(self, task: Optional[TaskModel]):
        self.task = task
        self.vars = {}
        self.step = 0
        self.fail = False

    @property
    def end(self) -> bool:
        return self.step >= len(self.task.program)

    def run(self):
        if not self.end and not self.fail:
            try:
                step_info = self.task.program[self.step]
                if step_info.id in modules:
                    module = modules[step_info.id](param=step_info.param)
                    result = module.run()
                    if result.code == ModuleResultCode.SUCCESS:
                        self.vars.update(result.vars)
                        self.step += 1
                    else:
                        logging.error(
                            f"Module {step_info.id} failed "
                            f"because of fail result '{result.vars}'."
                        )
                        Exception("Module failed.")

            except Exception as e:
                self.fail = True
                raise e
