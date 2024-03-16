from typing import List, Union
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os
from fastapi import UploadFile, File

from src.vinted import VintedProduct, get_vinted_products

STORAGE_PATH = os.getenv('STORAGE_PATH', 'data')

app = FastAPI()
app.mount("/images", StaticFiles(directory=f"{STORAGE_PATH}"), name="images")

class Message(BaseModel):
    name: str

class ProductRequest(BaseModel):
    product_query: str

class ProductWithPortrait(BaseModel):
    product: VintedProduct
    portrait_url: str


# class Product(BaseModel):
#     name: str
#     price: str
#     size: str
#     image: str
#     url: str
    



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

@app.post("/get_products/{session_id}")
async def get_products(session_id: str, request: ProductRequest):
    file_path = os.path.join(STORAGE_PATH, session_id, 'portrait.jpg')
    product_query = request.product_query
    print(f'Processing product query: {product_query}...')

    products = get_vinted_products(product_query)

    # TODO Use GPT4V to get a detailed description of each product

    # TODO Use a (Text + Image -> Image) model to overlay each product on to the portrait
    
    result: List[ProductWithPortrait] = []

    return {
        'products': result
    }


if __name__ == "app.main":
    print('Starting FastAPI server...')
    