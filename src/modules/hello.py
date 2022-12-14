from typing import Union
from src.modules.base import BaseModule
from src.types import ModuleResult, ModuleResultCode
from time import sleep


class HelloModule(BaseModule):
    id = "hello"
    name = "Hello World Module"
    version = "0.0.1"

    def run(self):
        return ModuleResult(code=ModuleResultCode.SUCCESS, vars={"log": "Hello World!"})


class DelayHelloModule(BaseModule):
    id = "delay_hello"
    name = "Delay Hello World Module"
    version = "0.0.1"

    def run(self):
        sleep(1)
        return ModuleResult(code=ModuleResultCode.SUCCESS, vars={"log": "Hello World!"})


class DelayNSecHelloModule(BaseModule):
    id = "delay_n_sec_hello"
    name = "Delay N Sec Hello World Module"
    version = "0.0.1"

    def run(self, n: Union[int, float, str], msg: str = "Hello World!"):
        n = float(n)
        sleep(n)
        return ModuleResult(code=ModuleResultCode.SUCCESS, vars={"msg": msg})
