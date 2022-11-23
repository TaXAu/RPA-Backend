import os
import json
from src.types import TaskModel

# read all json files as actions
actions = {}
for file in os.listdir(os.path.dirname(__file__)):
    if file.endswith(".json"):
        with open(os.path.join(os.path.dirname(__file__), file), "r") as f:
            info = TaskModel(**json.load(f))
            actions[info.id] = info
