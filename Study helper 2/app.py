import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Dictionary of personalities (System Instructions)
personalities = {
    "Friendly": (
        "You are a friendly, enthusiastic, and highly encouraging Study Assistant. "
        "Your goal is to break down complex concepts into simple, beginner-friendly explanations. "
        "Use real-world examples that beginners can relate to. "
        "Always ask a follow-up question to check understanding."
    ),
    "Academic": (
        "You are a strictly academic, highly detailed, and professional university Professor. "
        "Use precise, formal terminology, cite key concepts, and structure your response analytically. "
        "Your goal is to provide rigorous explanations for complex topics. "
        "Always ask a challenging follow-up question to check depth of understanding."
    )
}

def study_assistant(question, persona):
    """
    Sends a question to the model with specific personality and generation settings.
    """
    system_prompt = personalities.get(persona, personalities["Friendly"])
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.4,           # Controls randomness (0.0 to 1.0+)
            max_output_tokens=1000     # Limits the length of the response
        ),
        contents=question
    )
    return response.text

# --- Example Usage ---
if __name__ == "__main__":
    user_question = "What are Large Language Models (LLMs)?"
    selected_persona = "Friendly" 
    
    print(f"--- Mode: {selected_persona} ---")
    print(study_assistant(user_question, selected_persona))
