from pydantic import BaseModel
from typing import List, Dict


class ActionModel(BaseModel):
    name: str
    id: str
    paras: Dict


class ProgramModel(BaseModel):
    name: str
    id: str
    program: List[ActionModel]
