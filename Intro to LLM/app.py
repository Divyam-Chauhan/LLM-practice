import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def question_generator(text):
    user_prompt = "Generate questions from the following content:\n" +text
    response = client.models.generate_content(model="gemini-2.5-flash", contents=user_prompt)
    return response

response = question_generator ( "Large Language Models(LLMs) are AI systems trained on massive text data.They can understand, generate, and summarize human language.")

print(response.text)