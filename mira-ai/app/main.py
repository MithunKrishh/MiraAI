from fastapi import FastAPI
from app.routes.task_routes import router as task_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=(
        "A beginner-friendly FastAPI project that can parse simple user instructions "
        "into tasks, execute them, and store results in a small JSON memory file."
    ),
    openapi_tags=[
        {
            "name": "Health",
            "description": "Basic endpoints to verify the API is running.",
        },
        {
            "name": "Task",
            "description": "Parse and execute tasks from user input (summarize/save/retrieve).",
        },
    ],
)

@app.get(
    "/",
    tags=["Health"],
    summary="Health check",
    description="Simple endpoint to confirm the API is up and running.",
    response_description="A small status message.",
)
def root():
    return {"message": f"{settings.PROJECT_NAME} is running 🚀"}

app.include_router(task_router)