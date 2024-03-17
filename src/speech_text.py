import requests
import io
from openai import OpenAI
from fastapi import UploadFile, File


APIKEY = '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'
client = OpenAI(api_key=APIKEY)

audio_file = open("green_jumper.m4a", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file, 
  response_format="text"
)
print(transcription)

def speechFileToText(file: UploadFile):
  bytes = file.file.read()
  transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=bytes,
        response_format="text"
        )
  return transcription

def speech2text(audio_url):

    response = requests.get(audio_url)
    if response.status_code == 200:

        audio_file = io.BytesIO(response.content)
        
        transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file, 
        response_format="text"
        )
        return(transcription)
    else:
        return("Failed to download the file from the URL.")