from src.modules.base import BaseModule
from time import sleep


class Delay(BaseModule):
    id = "delay"
    name = "Delay Module"
    version = "0.0.1"
    description = "提供一段时间的延时"

    def run(self, ms: str):
        n = float(ms) / 1000
        sleep(n)
