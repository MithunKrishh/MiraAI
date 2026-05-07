from typing import Any, List

from pydantic import BaseModel

class TaskRequest(BaseModel):
    input: str

class TaskResponse(BaseModel):
    message: str
    input: str
    tasks: List[dict[str, Any]] = []