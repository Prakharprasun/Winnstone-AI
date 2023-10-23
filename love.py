import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant"},
    {"role": "user", "content": "Compose a poem that explains the concept of love"}
  ]
)

print(completion.choices[0].message)