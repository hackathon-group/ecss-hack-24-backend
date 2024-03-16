from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import os
from fastapi import UploadFile, File

STORAGE_PATH = os.getenv('STORAGE_PATH', 'data')

app = FastAPI()

class Message(BaseModel):
    name: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/hello")
def hello_world(message):
    return {"result": f'Hello, {message.name}!'}

@app.post("/upload_portrait/{session_id}")
async def upload_portrait(session_id: str, portrait: UploadFile = File(...)):
    file_path = os.path.join(STORAGE_PATH, session_id, 'portrait.jpg')
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "wb") as buffer:
        buffer.write(portrait.file.read())
    return {
        'success': True
    }

if __name__ == "app.main":
    print('Starting FastAPI server...')
    