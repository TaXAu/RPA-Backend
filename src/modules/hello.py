from typing import Union
from src.modules.base import BaseModule
from time import sleep


class HelloModule(BaseModule):
    id = "hello"
    name = "Hello World Module"
    version = "0.0.1"

    def run(self) -> str:
        return "hello"


class DelayHelloModule(BaseModule):
    id = "delay_hello"
    name = "Delay Hello World Module"
    version = "0.0.1"

    def run(self) -> str:
        sleep(1)
        return "hello"


class DelayNSecHelloModule(BaseModule):
    id = "delay_n_sec_hello"
    name = "Delay N Sec Hello World Module"
    version = "0.0.1"

    def run(self, n: Union[int, float, str], msg: str = "Hello World!") -> str:
        n = float(n)
        sleep(n)
        return "hello"
