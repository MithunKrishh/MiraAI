from fastapi import APIRouter

router = APIRouter(
    prefix="/task",
    tags=["Task"]
)

@router.get("/test")
def test_route():
    return {"message": "Task route working ✅"}