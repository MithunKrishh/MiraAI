from fastapi import FastAPI
from app.routes.task_routes import router as task_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

@app.get("/")
def root():
    return {"message": f"{settings.PROJECT_NAME} is running 🚀"}

app.include_router(task_router)