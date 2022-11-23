from src.modules.base import BaseModule
from src.types import ModuleResult, ModuleResultCode
from time import sleep


class HelloModule(BaseModule):
    id = "hello"
    name = "Hello World Module"
    version = "0.0.1"

    def run(self):
        print("Hello World!")
        return ModuleResult(code=ModuleResultCode.SUCCESS, vars={"log": "Hello World!"})


class DelayHelloModule(BaseModule):
    id = "delay_hello"
    name = "Delay Hello World Module"
    version = "0.0.1"

    def run(self):
        sleep(1)
        print("Hello World!")
        return ModuleResult(code=ModuleResultCode.SUCCESS, vars={"log": "Hello World!"})
