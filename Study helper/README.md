# 📚 AI Study Assistant (Study Helper)

Building your first LLM-powered application using Python! This project explains how to talk to an AI model using code instead of a chat interface.

### 🏠 Why use Python instead of a Chatbot?
While tools like ChatGPT are great, using Python gives you:
- **Flexibility**: You can connect it to anything (like a database or a website).
- **Control**: You define exactly how the AI should behave and what format it returns.
- **Automation**: You can process thousands of files automatically.

---

### 🍔 The "Burger" Analogy (The 3 Ingredients)
Building an AI app is like making a burger. You need three key ingredients:
1. **The Brain (The Meat)**: The AI model itself (we use `gemini-2.5-flash`).
2. **The Connector (The Bun)**: The link between your code and the AI. This is called an **SDK** (Software Development Kit).
3. **The Instructions (The Sauce)**: Your **Prompt**. This tells the AI exactly what to do.

---

### 🛠️ Setup Instructions

1.  **Install the SDK**: 
    Think of the SDK as the "Car" we use to drive to the AI's house. To install it, run:
    ```bash
    pip install -U google-genai
    ```
2.  **API Key**: 
    Get your free key from [Google AI Studio](https://aistudio.google.com/app/apikey).
3.  **The Secret File (`.env`)**:
    Create a file named `.env` in this folder and paste your key:
    ```env
    GEMINI_API_KEY="your_actual_key_here"
    ```

---

### 🔍 Code Breakdown (Line-by-Line)

Let's look at `app.py` and see what each part does:

#### **Lines 1-3: The Imports**
```python
import os
from dotenv import load_dotenv
from google import genai
```
- `os` & `dotenv`: These are for **security**. They allow us to load your API key from the `.env` file so you don't have to write it directly in your code (which is dangerous if you share your code!).
- `google.genai`: This is the official "Connector" (the Bun) that lets Python talk to Google's Gemini models.

#### **Lines 5-6: The Handshake**
```python
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
```
- `load_dotenv()`: This simply tells Python to go look at our `.env` file and grab the secrets.
- `genai.Client(...)`: This officially creates the connection. We call this the `client`. It is our "phone line" to the AI.

#### **Lines 8-11: The Brain Logic**
```python
def question_generator(text):
    user_prompt = "Generate questions from the following content:\n" + text
    response = client.models.generate_content(model="gemini-2.5-flash", contents=user_prompt)
    return response
```
- `question_generator(text)`: We wrapped the logic in a "Function" so we can reuse it easily.
- `client.models.generate_content(...)`: **This is the main event!** 
    - `model="gemini-2.5-flash"`: This tells the connector which "Brain" to use. Flash is fast and smart!
    - `contents=user_prompt`: This is our instruction (the "Sauce").
- `return response`: The AI doesn't just send text; it sends a big packet of data (including how many tokens it used). We return the whole thing.

#### **Lines 13-15: Seeing the Result**
```python
response = question_generator("Large Language Models...")
print(response.text)
```
- we call our function with some study text.
- `response.text`: Since the `response` is a big object, we only want to see the actual words the AI wrote. `.text` extracts only the words for us.

---

### 🎓 Learning Summary
In this project, we learned that:
1. An **SDK** is just a library that makes it easy to talk to an API.
2. We should **never hardcode API keys**—always use a `.env` file.
3. The `generate_content` method is the core command for getting a response from a model.

**Maintainer**: Divya Prakash Singh Chauhan 🚀
