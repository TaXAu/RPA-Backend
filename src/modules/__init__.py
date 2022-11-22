__all__ = ["BaseModule", "modules"]

from src.modules.base import BaseModule
import importlib
import inspect
import os


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
