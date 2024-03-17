from openai import OpenAI

APIKEY = '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'
client = OpenAI(api_key=APIKEY)

audio_file = open("green_jumper.m4a", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file, 
  response_format="text"
)
print(transcription)

