from src.modules.base import BaseModule, ModuleArgsException
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
    args = {"n": float}
    vars = {"log": str}

    def run(self):
        if "n" in self.args:
            sleep(float(self.args["n"]))
        else:
            raise ModuleArgsException("Missing argument `n`.")
        n = float(self.args["n"])
        rtn = f"Hello World! (delayed {n} seconds)"
        return ModuleResult(code=ModuleResultCode.SUCCESS, vars={"log": rtn})
