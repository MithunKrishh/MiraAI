from fastapi import APIRouter
from app.models.schemas import TaskRequest, TaskResponse
from app.services.parser import parse_tasks

router = APIRouter(
    prefix="/task",
    tags=["Task"]
)

@router.post("/", response_model=TaskResponse)
def handle_task(request: TaskRequest):
    parsed_tasks = parse_tasks(request.input)

    return {
        "message": f"Parsed tasks: {parsed_tasks}",
        "input": request.input
    }