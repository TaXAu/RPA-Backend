from src.modules import BaseModule
from typing import TypedDict as D
from typing import Any


class TestModule1(BaseModule):
    def run(
        self, a: int, b: float, c: str, d: list, f
    ) -> D("hello", {"a": int, "b": float, "c": str, "d": list}):
        return {"a": a, "b": b, "c": c, "d": d}


def test_module():
    module = TestModule1()
    args = module.get_args()
    assert args == {"a": int, "b": float, "c": str, "d": list, "f": Any}
