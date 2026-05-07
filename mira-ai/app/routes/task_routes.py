from fastapi import APIRouter, HTTPException, status

from app.models.schemas import TaskRequest, TaskResponse
from app.services.executor import execute_task
from app.services.parser import parse_tasks

router = APIRouter(
    prefix="/task",
    tags=["Task"]
)










@router.post(
    "/",
    response_model=TaskResponse,
    summary="Parse and execute tasks",
    description=(
        "Takes a single input string, splits it into simple tasks (using words like 'and' or 'then'), "
        "detects each task's intent (summarize/save/retrieve), executes them, and returns the results.\n\n"
        "Notes:\n"
        "- 'summarize' will attempt to summarize the provided text and store the result in memory.\n"
        "- 'save' stores the task text in memory.\n"
        "- 'retrieve' returns the last saved memory entry."
    ),
    response_description="Execution results for each parsed task.",
    responses={
        400: {
            "description": "Bad Request - parsing failed.",
            "content": {
                "application/json": {
                    "example": {"detail": "Failed to parse tasks from input."}
                }
            },
        },
        422: {
            "description": "Validation Error - empty input or no tasks found.",
            "content": {
                "application/json": {
                    "example": {"detail": "No tasks found in input."}
                }
            },
        },
    },
)
def handle_task(request: TaskRequest):
    # FastAPI/Pydantic handles most validation; keep some defensive checks to avoid crashes.
    if not request.input or not request.input.strip():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="'input' must be a non-empty string.",
        )

    try:
        parsed_tasks = parse_tasks(request.input)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to parse tasks from input.",
        )

    if not parsed_tasks:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="No tasks found in input.",
        )

    results = []
    for task in parsed_tasks:
        intent = (task.get("intent") or "unknown").strip()
        text = (task.get("text") or "").strip()

        if not text:
            continue

        try:
            result = execute_task(intent=intent, text=text)
        except Exception:
            # Don’t crash the whole request—return an item-level error for this task.
            result = "Task execution failed."

        results.append({"intent": intent, "text": text, "result": result})

    if not results:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="No valid tasks to execute.",
        )

    return {"message": "Tasks executed successfully.", "input": request.input, "tasks": results}