import logging
from src.types.module import ModuleResult
from typing import Dict, Optional


class BaseModule(object):
    """Base class for all modules.

    This class is responsible for loading the module's configuration and
    providing a common interface for all modules.

    """

    id: str = "base_module"
    name: str = "Base Module"
    description: str = "Base module for all modules."
    version: str = "0.1.0"
    args: Dict[str, type] = {}
    vars: Dict[str, type] = {}

    def __init__(
        self,
        config: Optional[Dict[str, str]] = None,
        param: Optional[Dict[str, str]] = None,
    ) -> None:
        """
        :param config: The module's configuration.
        """
        self.config = config
        self.param = param
        logging.debug(f"Module {self.id} initialized.")
        logging.debug(f"Module {self.id} configuration: {self.config}")
        logging.debug(f"Module {self.id} parameters: {self.param}")

    def run(self) -> ModuleResult:
        """
        Run the module.
        """
        raise NotImplementedError()


class ModuleException(Exception):
    """Base class for all module exceptions."""

    pass


class ModuleArgsException(ModuleException):
    """Exception for module arguments."""

    pass
