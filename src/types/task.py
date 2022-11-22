from pydantic import BaseModel
from typing import List, Dict, NewType, Any
from enum import Enum


class ActionModel(BaseModel):
    id: str
    name: str
    paras: Dict[str, Any]


TaskID = NewType("TaskID", str)


class TaskModel(BaseModel):
    id: TaskID
    name: str
    program: List[ActionModel]


class TaskStatus(Enum):
    INITIAL = 0
    INIT_ERROR = 1
    READY = 2
    RUNNING = 3
    PENDING = 4
    SUCCESS = 5
    FAILED = 6
