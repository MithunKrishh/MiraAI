from typing import Any, List

from pydantic import BaseModel, Field

class TaskRequest(BaseModel):
    input: str = Field(..., min_length=1, max_length=5000, description="User input containing one or more tasks")

class TaskResponse(BaseModel):
    message: str
    input: str
    tasks: List[dict[str, Any]] = []