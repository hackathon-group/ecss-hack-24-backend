from pathlib import Path
from openai import OpenAI
import os

apiKey = "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"

#headers = {"Authorization": f"Bearer {apiKey}",
            #"Content-Type": "application/json"}

speech_file_path = Path(__file__).parent / "speech.mp3"

client = OpenAI(api_key=apiKey)

#openai.api_key = "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"
#default_headers = headers

response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Today is a wonderful day to build something people love!"
)

with open(speech_file_path, "wb") as f:
    f.write(response.content)