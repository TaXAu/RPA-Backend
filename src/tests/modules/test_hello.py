from src.modules import modules
from src.types import ModuleResultCode


def test_hello_module():
    module = modules["hello"]()
    result = module.module_run()
    assert result.code == ModuleResultCode.SUCCESS
