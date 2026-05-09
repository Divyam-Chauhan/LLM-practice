import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def language_translator(user_prompt):
  response = client.models.generate_content(model="gemini-2.5-flash", contents=user_prompt)
  return response

response = language_translator("Translate this to Hindi:'Welcome to the course Building LLm Applications'")

print(response.text)