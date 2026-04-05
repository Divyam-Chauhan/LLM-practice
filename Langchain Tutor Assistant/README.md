# 🔗 Langchain Tutor Assistant

A Python application demonstrating **provider portability** in LangChain. This project uses a **Groq-hosted open-source model** (`llama-3.3-70b-versatile`) instead of Google Gemini, proving that switching providers in LangChain is a one-line change.

> If you haven't read the LangChain introduction yet, refer to the `Intro to Langchain` folder first.

---

### ⚙️ What This Project Demonstrates

The `Intro to Langchain` and `Langchain Travel Guide` projects both use Google Gemini as the backend. This project switches to **Groq** — a cloud platform that hosts open-source models like Meta's Llama 3.3.

The key takeaway: the only thing that changes in the code is the model initialization string. Everything else — `SystemMessage`, `HumanMessage`, `invoke()`, `.content` — stays exactly the same.

#### What is Groq?
Groq is an inference platform that runs open-source LLMs at high speed. It provides free API access for development and testing (a google search on Groq's inference architecture would suffice for more detail).

#### What is Llama 3.3?
`llama-3.3-70b-versatile` is Meta's open-source large language model with 70 billion parameters. It is hosted on Groq's infrastructure and accessible via their API (a google search on Meta's Llama model family would suffice for more detail).

---

### 🛠️ Local Configuration

1.  **Dependency Installation**:
    The `langchain-groq` package is required to enable LangChain to communicate with models hosted on Groq:
    ```bash
    pip install -r requirements.txt
    ```
2.  **API Key**:
    Generate a free Groq API key from [Groq Console](https://console.groq.com/keys).
3.  **Environment Configuration (`.env`)**:
    Place your key in the `.env` file:
    ```env
    GROQ_API_KEY="your_actual_key_here"
    ```

---

### 🔍 Code Execution Breakdown

#### **Imports**
```python
import os
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
```
- `os`: Standard library module used to read environment variables.
- `init_chat_model`: LangChain's universal model initializer. Same function used in the Gemini projects — it works identically here with Groq.
- `HumanMessage`, `SystemMessage`: Provider-agnostic message classes. These are the same objects used in the Travel Guide and Intro projects.
- `load_dotenv`: Reads key-value pairs from the `.env` file and loads them into the process environment (a google search on python-dotenv would suffice).

#### **Environment Setup**
```python
load_dotenv()
api_key = os.getenv('GROQ_API_KEY')
```
- `load_dotenv()`: Scans the current directory for a `.env` file and loads its contents into memory.
- `os.getenv('GROQ_API_KEY')`: Retrieves the Groq API key from the loaded environment variables. Note that this is `GROQ_API_KEY` instead of `GEMINI_API_KEY` — the only environment-level difference.

#### **Message Construction**
```python
system_msg = SystemMessage("You are a Python tutor who explains concepts with simple code examples.")
human_msg = HumanMessage("Explain what a dictionary is in Python with an example.")
messages = [system_msg, human_msg]
```
- This is identical in structure to the Gemini projects. The same `SystemMessage` and `HumanMessage` objects work regardless of the backend provider.

#### **Model Initialization (The One-Line Swap)**
```python
model = init_chat_model(
    "groq:llama-3.3-70b-versatile",
    api_key = api_key,
)
```
- `"groq:llama-3.3-70b-versatile"`: The format is `provider:model-name`. In the Travel Guide project, this was `"google_genai:gemini-2.5-flash"`. Here it is `"groq:llama-3.3-70b-versatile"`. This single string is the **only functional difference** between the two projects.
- LangChain internally routes this to the `langchain-groq` package for communication with Groq's API.

#### **Invocation & Output**
```python
response = model.invoke(messages)
print(response.content)
```
- `model.invoke(messages)`: Sends the structured message list to the Llama model and returns an `AIMessage` response object. Same method, same behavior, different backend.
- `response.content`: Extracts the generated text string from the response object.

---

### 📝 Key Takeaway
The entire point of this project is **portability**. The same `SystemMessage`, `HumanMessage`, `invoke()`, and `.content` pattern works identically whether you are talking to Groq, Google Gemini, or OpenAI. LangChain handles the translation layer internally.

**Maintainer**: Divya Prakash Singh Chauhan 🚀
