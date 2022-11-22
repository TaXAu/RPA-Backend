from src.types.module import ModuleResult
from typing import Dict, Optional, Any


class BaseModule(object):
    """Base class for all modules.

    This class is responsible for loading the module's configuration and
    providing a common interface for all modules.

    """

    id: str = "base_module"
    name: str = "Base Module"
    description: str = "Base module for all modules."
    version: str = "0.1.0"
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None

    def __init__(self, config: Optional[Dict[str, str]] = None) -> None:
        """
        :param config: The module's configuration.
        """
        self.config = config

    def run(self) -> ModuleResult:
        """
        Run the module.
        """
        raise NotImplementedError()
