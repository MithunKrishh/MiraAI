from fastapi import APIRouter
from app.models.schemas import TaskRequest, TaskResponse
from app.services.parser import parse_tasks
from app.services.executor import execute_pipeline

router = APIRouter(
    prefix="/task",
    tags=["Task"]
)

@router.post("/", response_model=TaskResponse)
def handle_task(request: TaskRequest):
    tasks = parse_tasks(request.input)
    result = execute_pipeline(tasks)

    return {
        "message": result,
        "input": request.input
    }