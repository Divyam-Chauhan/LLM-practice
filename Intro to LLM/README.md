# 🧠 Introduction to LLM (Your Starting Point)

This is where your LLM journey begins. Before diving into frameworks or advanced features, this project teaches you the absolute fundamentals: **what an LLM is, how your code talks to one, and how to build your first working application.**

---

### 📖 What is a Large Language Model (LLM)?

A Large Language Model is an AI system trained on massive amounts of text data. It can understand, generate, and manipulate human language. When you type a question into ChatGPT, Google Gemini, or Claude — you are interacting with an LLM.

These models are served over the internet through APIs. Your code sends a request (a prompt) to the model, and the model sends back a generated response.

---

### ⚙️ How Applications Talk to LLMs

There are three main ways to connect your code to an LLM:

1. **Running LLMs locally on your machine** — requires powerful hardware (a google search on local LLM inference would suffice).
2. **Making direct HTTP requests** to the provider's API endpoint — requires manually formatting headers, authentication, and parsing raw JSON responses.
3. **Using the provider's official SDK (Software Development Kit)** — a pre-built Python package that handles all the complexity for you.

We use the **third method** because it is the most practical and widely used approach.

#### What is an SDK?
An SDK (Software Development Kit) is a set of pre-written code provided by a company to simplify communication with their services. Instead of manually constructing HTTP requests, formatting headers, and parsing JSON, you call clean Python methods. The SDK handles authentication, request formatting, error handling, and response parsing internally.

#### Available LLM SDKs
Each major LLM provider offers an official Python SDK:
- **`google-genai`** — For Google's Gemini models.
- **`openai`** — For OpenAI's GPT models.
- **`anthropic`** — For Anthropic's Claude models.
- **`groq`** — For models hosted on Groq (like Llama).

We use **`google-genai`** in this project because Gemini offers a generous free tier for learning and experimentation.

> Once you learn to use one SDK, switching to another is straightforward — the patterns are very similar across providers.

---

### ⚙️ Why Python?
Using a programming language like Python instead of a chat interface gives you:
- **Custom logic**: Preprocess input and post-process output for specific use cases.
- **Scalability**: Automate processing across large datasets.
- **Integration**: Connect the LLM to databases, APIs, or other services.

---

### 🧱 The Three Essential Components

Every LLM application requires three things:

1. **The Model**: The AI engine that processes text. We use **`gemini-2.5-flash`**.
2. **The Connector (SDK)**: The Python package that communicates with the model's API. We use **`google-genai`**.
3. **The Prompt**: The literal string of instructions you send to the model.

---

### 🛠️ Local Configuration

1.  **Dependency Installation**:
    Install the official Google GenAI SDK:
    ```bash
    pip install -r requirements.txt
    ```
2.  **API Key Generation**:
    Generate a free API key from [Google AI Studio](https://aistudio.google.com/app/apikey). This key authenticates your application with Google's servers.
3.  **Environment Configuration (`.env`)**:
    Store your API key in a `.env` file to keep it separate from your code:
    ```env
    GEMINI_API_KEY="your_actual_key_here"
    ```

---

### 🔍 Code Execution Breakdown

The following is a line-by-line explanation of the logic in `app.py`:

#### **Imports**
```python
import os
from dotenv import load_dotenv
from google import genai
```
- `import os`: A standard Python library module that allows interaction with the operating system. Here it is used specifically to retrieve environment variables.
- `from dotenv import load_dotenv`: This package reads key-value pairs from a `.env` file and loads them into the system's environment variables. This is how we avoid hardcoding secret keys into our source code.
- `from google import genai`: The official Google Generative AI SDK. This is the direct interface through which Python communicates with Google's Gemini models.

#### **Initialization & Authentication**
```python
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
```
- `load_dotenv()`: Scans the current directory for a `.env` file and loads its contents into memory.
- `os.getenv("GEMINI_API_KEY")`: Retrieves the API key value from the environment variables.
- `genai.Client(...)`: Creates an authenticated client instance. This `client` is the active connection to Google's API — all subsequent requests go through it.

#### **The Generation Function**
```python
def question_generator(text):
    user_prompt = "Generate questions from the following content:\n" + text
    response = client.models.generate_content(model="gemini-2.5-flash", contents=user_prompt)
    return response
```
- `question_generator(text)`: A reusable function that takes any text and generates study questions from it.
- `user_prompt`: Concatenates a static instruction (`"Generate questions from..."`) with the dynamic user input. This combined string is what the model receives.
- `client.models.generate_content()`: **This is the core method.** It sends the prompt to the specified model and returns a `GenerateContentResponse` object.
  - `model="gemini-2.5-flash"`: Identifies which model to use. Flash is optimized for speed.
  - `contents=user_prompt`: The actual text the model will process.
- `return response`: Returns the full response object (which contains the generated text plus metadata like token usage and safety ratings).

#### **Output Handling**
```python
response = question_generator("Large Language Models(LLMs) are AI systems trained on massive text data...")
print(response.text)
```
- We call the function with sample study text.
- `response.text`: The response object contains much more than just the generated words (it includes token counts, safety ratings, etc.). The `.text` attribute extracts only the generated string for display.

---

### 📝 What You've Learned
After working through this project, you now understand:
1. What an LLM is and how applications communicate with one.
2. What an SDK is and why we use `google-genai` instead of raw HTTP requests.
3. How to securely manage API keys using `.env` files.
4. The `generate_content` method — the fundamental building block for all LLM interactions.

This foundation is used in every subsequent project in this repository.

**Maintainer**: Divya Prakash Singh Chauhan
