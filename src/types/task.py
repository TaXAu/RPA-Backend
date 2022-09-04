from pydantic import BaseModel
from typing import List, Dict, NewType
import enum


class ActionModel(BaseModel):
    name: str
    id: str
    paras: Dict


TaskID = NewType("TaskID", str)


class TaskModel(BaseModel):
    name: str
    id: TaskID
    program: List[ActionModel]


class TaskStatus(enum.Enum):
    INITIAL = ("initial",)
    INIT_ERROR = ("init_error",)
    READY = ("ready",)
    RUNNING = ("running",)
    PENDING = ("pending",)
    SUCCESS = ("success",)
    FAILED = ("failed",)
