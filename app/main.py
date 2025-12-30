from fastapi import FastAPI
from app.api import auth, tasks

app = FastAPI(title="Technical Test Backend")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])

@app.get("/")
def root():
    return {"message": "API is running"}