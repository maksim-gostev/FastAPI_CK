from fastapi import FastAPI
from task.router import tasks_router

app = FastAPI(
    title="Тестовое задание на FastAPI",
    description="Тестовое задание на FastAPI",
    version="0.1.0",
)


@app.get("/")
def read_root():
    return {"message": "Hello World"}


app.include_router(tasks_router)
