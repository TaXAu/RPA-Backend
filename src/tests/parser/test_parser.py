from src.parser.parser import Parser
from src.tests.actions import actions


def test_parser_hello():
    p = Parser(actions["hello"])
    while not p.end:
        p.run()
    assert p.end
    assert not p.fail
    assert p.step == len(actions["hello"].program)
    assert p.vars["log"] == "Hello World!"


def test_n_hello_module():
    p = Parser(actions["delay_n_sec_hello"])
    while not p.end:
        p.run()
    assert p.end
    assert not p.fail
    assert p.step == len(actions["hello"].program)
    assert p.vars["msg"] == actions["delay_n_sec_hello"].program[0].args["msg"]
