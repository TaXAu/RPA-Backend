import json
from src.web.web_rpa import web_functions_easy as web

all_functions = web


def load_json(file_path):
    """
    Loads a json file and returns a dictionary.
    """
    with open(file_path, "r") as f:
        data = json.load(f)
    return data


def load_program(json_data):
    """
    Loads a program from a dictionary.
    """
    program = json_data["program"]
    return program


def run_program(program):
    """
    Runs a program.
    """
    for step in program:
        func_name = step["name"]
        func_args = step["paras"]
        if func_name in all_functions:
            all_functions[func_name](**func_args)

def run_program_from_file(file_path):
    """
    Runs a program from a json file.
    """
    json_data = load_json(file_path)
    print("[Program loaded]", json_data["name"])
    program = load_program(json_data)
    run_program(program)

# class RpaProgram:
#     def __init__(self):
#         self.program = []
#         self.name = ""
#
#     def load_json(self, file_path):
#         with open(file_path, "r") as f:
#             data = json.load(f)
#         self.program = data["program"]
#
#     def run(self):
#         for step in self.program:
#


if __name__ == "__main__":
    print("This is a module for parsing json files and running the steps in it.")
    data = load_json("../test/sample.json")
    program = load_program(data)
    run_program(program)
