from typing import List
import importlib
import inspect
import os
from src.modules.base import BaseModule, ModuleException, ModuleArgsException
from src.types import ModuleInfo


def get_modules(path):
    """Get all files in a directory."""
    result = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            if file == "__init__.py":
                # ignore when file name is `__init__.py`
                pass
            elif file.startswith("_") or not file.endswith(".py"):
                pass
            else:
                result.append(f"src.modules.{file[:-3]}")
    return result


modules = {}
for module in get_modules(os.path.dirname(__file__)):
    module = importlib.import_module(module, package="src.modules")
    classes = inspect.getmembers(module, inspect.isclass)
    for name, cls in classes:
        if issubclass(cls, BaseModule):
            if cls.id != "base_module" and cls.id not in modules:
                modules[cls.id] = cls

modules_info: List[ModuleInfo] = []
for _, module in modules.items():
    modules_info.append(
        ModuleInfo(
            id=module.id,
            name=module.name,
            description=module.description,
            version=module.version,
            args={k: str(v) for k, v in module().get_args().items()},
            rtns=str(module().get_rtns()),
        )
    )

__all__ = [
    "BaseModule",
    "modules",
    "modules_info",
    "ModuleException",
    "ModuleArgsException",
]
