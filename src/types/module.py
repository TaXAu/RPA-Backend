from typing import Optional, Any
import enum
from pydantic import BaseModel


class ModuleResultCode(enum.Enum):
    SUCCESS = 0
    FAIL = 1


class ModuleResult(BaseModel):
    code: ModuleResultCode
    rtns: Any


class ModuleInfo(BaseModel):
    id: str
    name: str
    description: Optional[str]
    version: str
