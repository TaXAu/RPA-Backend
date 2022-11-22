import json
from src.parser.parser import Parser
from src.types import TaskModel


def test_parser_hello():
    # read json files
    with open("src/tests/actions/hello.json", "r") as f:
        task_info = TaskModel(**json.load(f))
    p = Parser(task_info)
    while not p.end:
        p.run()
    assert p.end
    assert not p.fail
    assert p.step == len(task_info.program)
    assert p.vars["log"] == "Hello World!"
