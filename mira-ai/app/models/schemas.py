from typing import Any, List

from pydantic import BaseModel, Field

class TaskRequest(BaseModel):
    input: str = Field(..., min_length=1, max_length=5000, description="User input containing one or more tasks")

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "input": "summarize this text and save it",
                },
                {
                    "input": "retrieve",
                },
            ]
        }

class TaskResponse(BaseModel):
    message: str
    input: str
    tasks: List[dict[str, Any]] = []

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "message": "Tasks executed successfully.",
                    "input": "summarize this text and save it",
                    "tasks": [
                        {
                            "intent": "summarize",
                            "text": "summarize this text",
                            "result": "<summary here>",
                        },
                        {
                            "intent": "save",
                            "text": "save it",
                            "result": "Saved successfully.",
                        },
                    ],
                }
            ]
        }