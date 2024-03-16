import requests
import json
from PIL import Image
import io
import json

url = "https://stablediffusionapi.com/api/v5/fashion"


inputImageName = "Picture2.png"

inputSplit = inputImageName.split('.')


payload = json.dumps({
   "key": "qg5Wa8DsHDs4Whc23kE9Al90UhhyEJPkcnLgQQsPRuFJAw3ShmOIBnkTEy1Y",
   "prompt": "A realistic photo of a model wearing a beautiful white top.",
   "negative_prompt": "Low quality, unrealistic, bad cloth, warped cloth",
   "init_image": "https://ecss-hack-24-backend.onrender.com/images/2d74f900-f500-4fdf-b412-57a5b243fca3/portrait.jpg",
   "cloth_image": "https://thumbs.dreamstime.com/b/plain-hollow-female-tank-top-shirt-isolated-white-background-30020169.jpg",
   "cloth_type": "upper-body", #upper-body, lower-body
   "height": 512,
   "width": 384,
   "guidance_scale": 15.0,
   "num_inference_steps": 33,
   "seed": 128915590,
   "temp": "no",
   "webhook": None,
   "track_id": None 
})

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

if (response.status_code == 200):
    print("Successful request")
    print("Data:")
    
    #im = Image.open(io.BytesIO(response.content))
    #im.show()
    response = response.json()

    print(response)

    imageResponse = requests.get(response['output'][0])

    print(imageResponse)

    img = Image.open(io.BytesIO(imageResponse.content))


    img.save("imagefromtextandimage3.png")
else:
    print("Error: Code " + str(response.status_code))