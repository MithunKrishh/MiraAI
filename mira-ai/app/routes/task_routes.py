from fastapi import APIRouter
from app.models.schemas import TaskRequest, TaskResponse

router = APIRouter(
    prefix="/task",
    tags=["Task"]
)

@router.get("/test")
def test_route():
    return {"message": "Task route working ✅"}


# 🔥 NEW ENDPOINT
@router.post("/", response_model=TaskResponse)
def handle_task(request: TaskRequest):
    return {
        "message": "Task received successfully",
        "input": request.input
    }