from pydantic import BaseModel
from typing import List, Dict


class ActionModel(BaseModel):
    name: str
    id: str
    paras: Dict


class TaskModel(BaseModel):
    name: str
    id: str
    program: List[ActionModel]
