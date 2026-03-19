from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Hello from FastAPI!",
        "env": os.getenv("APP_ENV")
    }
