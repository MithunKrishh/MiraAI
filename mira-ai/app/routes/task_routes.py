from fastapi import APIRouter
from app.models.schemas import TaskRequest, TaskResponse
from app.services.intent_service import detect_intent

router = APIRouter(
    prefix="/task",
    tags=["Task"]
)

@router.post("/", response_model=TaskResponse)
def handle_task(request: TaskRequest):
    intent = detect_intent(request.input)

    return {
        "message": f"Detected intent: {intent}",
        "input": request.input
    }