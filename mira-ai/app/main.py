from fastapi import FastAPI
from app.routes.task_routes import router as task_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "MiraAI is running 🚀"}

# 🔥 Connect routes
app.include_router(task_router)