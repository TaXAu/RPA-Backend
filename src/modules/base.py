import inspect
from src.types.module import ModuleResult, ModuleResultCode
from typing import Dict, Any, Optional


class BaseModule(object):
    """Base class for all modules.

    This class is responsible for loading the module's configuration and
    providing a common interface for all modules.

    """

    id: str = "base_module"
    name: str = "Base Module"
    description: str = "Base module for all modules."
    version: str = "0.1.0"

    def __init__(self, args: Optional[Dict[str, Any]] = None):
        self.args = None

    def set_args(self, args: Optional[Dict[str, Any]] = None):
        self.args = args

    def run(self, **kwargs) -> ModuleResult:
        """
        Run the module.
        """
        raise NotImplementedError()

    def module_run(self) -> ModuleResult:
        """
        Run the module.
        """
        try:
            return self.run(**self.args)
        except ModuleException:
            return ModuleResult(code=ModuleResultCode.FAIL)

    def get_args(self):
        """
        获取函数形参的类型标注，不包括 self，未进行标注的处理为 Any
        """
        args = inspect.getfullargspec(self.run).args
        annotations = inspect.getfullargspec(self.run).annotations
        rtn = {}
        for k in args:
            if k == "self":
                continue
            elif k in annotations:
                rtn[k] = annotations[k]
            else:
                rtn[k] = Any
        return rtn

    def get_rtn(self):
        """
        Get the return type of the module.
        """
        return inspect.getfullargspec(self.run).annotations.get("return", Any)


class ModuleException(Exception):
    """Base class for all module exceptions."""

    pass


class ModuleArgsException(ModuleException):
    """Exception for module arguments."""

    pass
