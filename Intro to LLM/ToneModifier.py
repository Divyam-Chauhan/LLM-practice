import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def modify_tone(text):
    response = client.models.generate_content(model = "gemini-2.5-flash", contents = text)
    return response

response = modify_tone("Translate its tone to formal: 'Knowledge is power.'")
print(response.text)