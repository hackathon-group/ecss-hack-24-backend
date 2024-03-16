from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    name: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/hello")
def hello_world(message):
    return {"result": f'Hello, {message.name}!'}

if __name__ == "app.main":
    print('Starting FastAPI server...')
    