from typing import List, Union
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os
from fastapi import UploadFile, File
import uuid
from src.gpt_description import gpt_query
from src.image_fusion import image_fusion_replicate
from src.speech_text import speech2text, speechFileToText
from src.vinted import VintedProduct, get_vinted_products
from fastapi.middleware.cors import CORSMiddleware


STORAGE_PATH = os.getenv('STORAGE_PATH', 'data')

app = FastAPI()
app.mount("/images", StaticFiles(directory=f"{STORAGE_PATH}"), name="images")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False, # Must be False when allow_origins is ["*"]
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    name: str

class ProductRequest(BaseModel):
    product_query: str

class ProductWithPortrait(BaseModel):
    product: VintedProduct
    portrait_url: str
    description: str

class ProductWithDescription(BaseModel):
    product: VintedProduct
    description: str


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
async def upload_portrait(session_id: str, transcript: UploadFile = File(...)):
    file_path = os.path.join(STORAGE_PATH, session_id, 'transcript.mp3')
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "wb") as buffer:
        buffer.write(transcript.file.read())
    return {
        'success': True,
        'transcript': await speechFileToText(transcript)
    }

async def get_product_description(product: VintedProduct) -> str:
    # TODO Use GPT4V to get a detailed description of each product
    description = gpt_query(product.name, product.image)
    return description


# ProductWithDescription -> ProductWithPortrait
async def get_product_with_portrait(session_id: str, product: ProductWithDescription) -> ProductWithPortrait:
    return ProductWithPortrait(
        product=product.product,
        portrait_url='',
        description=product.description
    ) 


    # Write the image to STORAGE_PATH/session_id/<random_uuid>.jpg 
    # The public facing URL will be /images/session_id/<random_uuid>.jpg
    rand_uuid = uuid.uuid4()
    file_path = os.path.join(STORAGE_PATH, session_id, f'{rand_uuid}.jpg')
    portrait_url = f'/images/{session_id}/{rand_uuid}.jpg'

    description = product.description
    portrait = open(os.path.join(STORAGE_PATH, session_id, 'portrait.jpg'), 'rb').read()
    root = 'https://ecss-hack-24-backend.onrender.com'
    final_url = image_fusion_replicate(
        root + portrait_url, 
        product.product.image
    )
    
    result = portrait # will be the result of the model
    with open(file_path, 'wb') as temp_: 
        temp_.write(result)

    return ProductWithPortrait(
        product=product.product,
        portrait_url=final_url,
        description=product.description
    )

@app.get("/get_products/{session_id}/")
async def get_products(session_id: str, product_query: str):
    print(f'Processing product query: {product_query}...')

    products = get_vinted_products(product_query)
    # Limit to first 5 products
    products = products[:5]

    products_with_description: List[ProductWithDescription] = []
    for product in products:
        description = ''
        try:
            description = await get_product_description(product)
        except Exception as e:
            print(f'Error getting product description for {product.name}: {e}')
            description = product.name
        products_with_description.append(ProductWithDescription(product=product, description=description))

    result: List[ProductWithPortrait] = []
    for product_with_description in products_with_description:
        try:
            product_with_portrait = await get_product_with_portrait(session_id, product_with_description)
            result.append(product_with_portrait)
        except Exception as e:
            print(f'Error getting product portrait for {product_with_description.product.name}: {e}')

    return {
        'products': result
    }


if __name__ == "app.main":
    print('Starting FastAPI server...')
    