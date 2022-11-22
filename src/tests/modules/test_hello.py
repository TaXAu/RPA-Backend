from src.modules import modules
from src.types import ModuleResultCode


def test_hello_module():
    module = modules["hello"]()
    result = module.run()
    assert result.code == ModuleResultCode.SUCCESS
    assert result.result == {"log": "Hello World!"}
