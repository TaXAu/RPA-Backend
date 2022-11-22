from typing import Dict, Optional
import enum
from pydantic import BaseModel


class ModuleResultCode(enum.Enum):
    SUCCESS = 0
    FAIL = 1


class ModuleResult(BaseModel):
    code: ModuleResultCode
    result: Optional[Dict[str, str]]