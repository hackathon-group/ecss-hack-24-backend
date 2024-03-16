import requests
from PIL import Image
#from requests.auth
import io
import os


base_url = "https://api.dezgo.com/"

apiKey = "DEZGO-8DEA54D0009423549AE813CAFA6A37A3C606909DB4AD84013F645050051F4BDAA9E4154B"

headers = {
    "accept": "text/plain",
            "X-Dezgo-Key": apiKey # type: ignore
}

image2imageHeaders = {
    "accept": "*/*",
    #"Content-Type": "application/json",
    "X-Dezgo-Key": apiKey # type: ignore
}



def getAccountInfo():


    get_account_info = "account"

    

    #response = requests.get(base_url+get_account_info)
    response = requests.get(base_url+get_account_info, headers=headers)

    if (response.status_code == 200):
        print("Successful request")
        print("Data:")
        print(response.json())
    else:
        print("Error: Code " + str(response.status_code))


def generateImageFromText():
    getGeneratedImage = "text2image"

    prompt = "cat in a hat"

    model = "absolute_reality_1"

    data = {
        "prompt": prompt,
        "model": model
    }

    response = requests.post(base_url+getGeneratedImage, headers=headers, data=data)

    if (response.status_code == 200):
        print("Successful request")
        print("Data:")
        im = Image.open(io.BytesIO(response.content))
        im.show()
        im.save("image.jpg")
    else:
        print("Error: Code " + str(response.status_code))





def generateImageFromTextAndImage():
    getGenerateImageFromTextAndImage = "image2image"

    prompt = "add a fedora hat to this person"

    model = "absolute_reality_1"

    inputImageName = "Picture1.png"

    inputSplit = inputImageName.split('.')



    files = {
        "prompt": prompt,
        "init_image": (inputImageName, open(inputImageName, 'rb'), inputSplit[0]+'/'+inputSplit[1]),
        "model": model
    }


    response = requests.post(base_url+getGenerateImageFromTextAndImage, headers=image2imageHeaders, files=files)

    if (response.status_code == 200):
        print("Successful request")
        print("Data:")
        im = Image.open(io.BytesIO(response.content))
        im.show()
        im.save("imagefromtextandimage2.png")
    else:
        print("Error: Code " + str(response.status_code))













################################## Run Functions Below ############################
        
#getAccountInfo()
#generateImageFromText()
        
generateImageFromTextAndImage()

