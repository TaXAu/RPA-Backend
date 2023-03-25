from src.modules import BaseModule
from typing import Any


class Module1(BaseModule):
    def run(
        self, a: int, b: float, c: str, d: list, f
    ) -> tuple[int, float, str, list, Any]:
        return a, b, c, d, f


def test_module_args():
    module = Module1()
    args = module.get_args()
    assert args == {"a": int, "b": float, "c": str, "d": list, "f": Any}


def test_module_rtns():
    module = Module1()
    rtns = module.get_rtns()
    assert rtns == tuple[int, float, str, list, Any]
