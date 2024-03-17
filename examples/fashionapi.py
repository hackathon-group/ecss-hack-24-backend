import requests
import json
from PIL import Image
import io
import json

url = "https://modelslab.com/api/v6/image_editing/fashion"


inputImageName = "Picture2.png"

inputSplit = inputImageName.split('.')

payload = json.dumps({
  "key": "qg5Wa8DsHDs4Whc23kE9Al90UhhyEJPkcnLgQQsPRuFJAw3ShmOIBnkTEy1Y",
  "prompt": "A realistic photo of a model wearing a football shirt.",
  "negative_prompt": "Low quality, unrealistic, bad cloth, warped cloth",
  "init_image": "https://i2-prod.mirror.co.uk/incoming/article27248367.ece/ALTERNATES/n615/0_Screenshot-2022-06-09-at-093256.jpg",
  "cloth_image": "https://m.media-amazon.com/images/I/61A9pfQot5L._AC_SX569_.jpg",
  "cloth_type": "upper-body",
  "height": 615,
  "width": 345,
  "guidance_scale": 8,
  "num_inference_steps": 20,
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
    
    response = response.json()

    print(response)

    imageResponse = requests.get(response['output'][0])

    print(imageResponse)

    img = Image.open(io.BytesIO(imageResponse.content))


    img.save("imagefromtextandimage3.png")
else:
    print("Error: Code " + str(response.status_code))

