import logging
from typing import Optional, Dict, Any
from src.types import TaskModel, ModuleResultCode
from src.modules import modules, ModuleException, ModuleArgsException

logger = logging.getLogger("rpa.parser")


class Parser(object):
    def __init__(self, task: Optional[TaskModel]):
        self.task = task
        self.vars: Dict[str, Any] = {}
        self.step = 0
        self.fail = False

    @property
    def end(self) -> bool:
        return self.step >= len(self.task.program)

    def run(self):
        if not self.end and not self.fail:
            try:
                # get param and args from json data
                step_info = self.task.program[self.step]  # get each step info
                # `{}` is to avoid none got from json data
                _param = step_info.param or {}
                _args = step_info.args or {}

                # get args
                # because of args are strings, so we only need to
                # add all args from json to the module args dict
                args = {**_args}  # all args for a module instance to run

                # get params
                for k, v in _param.items():
                    # because of params are refs to vars in the parser,
                    # we need firstly judge if the given param name is in vars,
                    # (and we do a type check here to make sure
                    #   all the keys for vars are string)
                    # if not, we will raise an error(ModuleArgsException)
                    if isinstance(v, str) and v in self.vars:
                        args[k] = self.vars.get(v, v)
                    else:
                        raise ModuleArgsException(f"Invalid argument: {k}={v}")

                # run modules
                if step_info.id in modules:  # judge if id in all module
                    module = modules[step_info.id]()

                    # judge if args from json is more than required args
                    if set(module.get_args().keys()).issubset(args.keys()):
                        module.set_args(args)
                        result = module.module_run()
                    else:
                        raise ModuleArgsException(f"Invalid arguments: {args.keys()}")

                    # judge task result
                    if result.code == ModuleResultCode.SUCCESS:
                        rtns = result.rtns  # 返回值
                        rtn_vars = step_info.rtns  # 返回值的变量名称，list 或 str
                        if isinstance(rtn_vars, list):  # 如果给定了多个变量名，执行解构语法
                            for i, var in enumerate(rtn_vars):
                                if var == "_":
                                    continue
                                else:
                                    self.vars[var] = rtns[i]  # 这里如果访问元素出错会直接捕获转任务失败
                        elif isinstance(rtn_vars, str):  # 给定的是一个字符串，直接将变量赋值进该变量名
                            self.vars[rtn_vars] = rtns
                        self.step += 1
                    else:
                        raise ModuleException("Module failed.")

            except Exception as e:
                self.fail = True
                logger.error(e)
