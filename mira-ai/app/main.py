from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "MiraAI is running successfully!"}