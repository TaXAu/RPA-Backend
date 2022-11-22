from pydantic import BaseModel
from typing import List, Dict, NewType
from enum import Enum


class ActionModel(BaseModel):
    name: str
    id: str
    paras: Dict


TaskID = NewType("TaskID", str)


class TaskModel(BaseModel):
    name: str
    id: TaskID
    program: List[ActionModel]


class TaskStatus(Enum):
    INITIAL = 0
    INIT_ERROR = 1
    READY = 2
    RUNNING = 3
    PENDING = 4
    SUCCESS = 5
    FAILED = 6
