from fastapi import APIRouter

from app.models.schemas import TaskRequest, TaskResponse
from app.services.executor import execute_task
from app.services.parser import parse_tasks

router = APIRouter(
    prefix="/task",
    tags=["Task"]
)

@router.post("/", response_model=TaskResponse)
def handle_task(request: TaskRequest):
    parsed_tasks = parse_tasks(request.input)

    results = []
    for task in parsed_tasks:
        intent = task.get("intent")
        text = task.get("text")
        result = execute_task(intent=intent, text=text)
        results.append({"intent": intent, "text": text, "result": result})

    return {
        "message": "Tasks executed successfully.",
        "input": request.input,
        "tasks": results,
    }