from pathlib import Path
from openai import OpenAI

apiKey = "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"

speech_file_path = Path(__file__).parent / "speech.mp3"

client = OpenAI(api_key=apiKey)

text = "Today is a wonderful day to build something people love!"

response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input=text
)

with open(speech_file_path, "wb") as f:
    f.write(response.content)


def text2speech(text):

  response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=text
  )

  return(response.content)
