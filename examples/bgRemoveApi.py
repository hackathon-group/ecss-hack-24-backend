import io
from PIL import Image
import requests

def removebgCall():
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        data={
            'image_url': 'https://ecss-hack-24-backend.onrender.com/images/2d74f900-f500-4fdf-b412-57a5b243fca3/portrait.jpg',
            'size': 'auto'
        },
        headers={'X-Api-Key': '5h3V6uE6AMPT9sGFSTmAX4D2'},
    )
    if response.status_code == requests.codes.ok:
        img = Image.open(io.BytesIO(response.content))
        img.save("imagefromtextandimage34.png")

    else:
        print("Error:", response.status_code, response.text)
        
print(removebgCall())
    
    
    
    