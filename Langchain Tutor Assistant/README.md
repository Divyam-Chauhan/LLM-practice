# 🔗 Langchain Tutor Assistant

A Python application demonstrating how **LangChain** standardizes LLM integration, allowing you to swap between model providers (Google, Groq, OpenAI) with minimal code changes. This project specifically uses a **Groq-hosted open-source model** (`llama-3.3-70b-versatile`) as the backend.

---

### ⚙️ Why LangChain?

#### The Provider Problem
When building LLM applications directly with provider SDKs (like `google-genai` or `groq`), every provider has:
- Different API structures and authentication flows.
- Different response formats and object schemas.
- Different message formatting requirements.
- Different ways to handle tool calling.

If you build an application using raw Groq SDK and later want to switch to Google Gemini or OpenAI, you would need to rewrite significant portions of your code.

#### What LangChain Solves
LangChain provides a **standardized interface** that abstracts away provider-specific differences. You write your application logic once, and switching providers becomes a one-line change (literally just changing the model string). It also provides pre-built, modular components for common tasks like message structuring, memory management, and tool integration.

#### Other Frameworks in This Space
LangChain is not the only framework available. Others include **LlamaIndex**, **Haystack**, **Semantic Kernel**, and **CrewAI**. LangChain is used here because of its wide adoption (120,000+ GitHub stars), integration support for 100+ providers, and extensive documentation.

---

### 🧱 Core Components Used

#### 1. Models (`init_chat_model`)
LangChain's `init_chat_model` is a universal model initializer. It accepts a provider-prefixed model string (e.g., `"groq:llama-3.3-70b-versatile"` or `"google_genai:gemini-2.5-flash"`) and returns a standardized chat model object. This is what makes provider-switching trivial.

#### 2. Messages (`SystemMessage`, `HumanMessage`)
Messages are structured objects that represent the conversation context sent to the model. Each message contains:
- **Role**: Identifies the message type (system, human, or AI).
- **Content**: The actual text payload.

**Message Types used here**:
- `SystemMessage`: Background instructions that define the model's behavior and role before the user speaks. The model reads this first and follows it throughout the conversation.
- `HumanMessage`: The actual user input or question that the model processes.

---

### 🛠️ Local Configuration

1.  **Dependency Installation**:
    The `langchain-groq` package is required to enable LangChain to communicate with LLMs hosted on Groq. Install dependencies using:
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

The following is a line-by-line explanation of the logic in `app.py`:

#### **Imports**
```python
import os
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
```
- `os`: Standard library module used to read environment variables from the system.
- `init_chat_model`: LangChain's universal model initializer. It accepts a provider-prefixed string and returns a ready-to-use chat model, regardless of the underlying provider.
- `HumanMessage`, `SystemMessage`: Structured message classes from LangChain that represent conversation roles. These are provider-agnostic — the same message objects work with Groq, Gemini, OpenAI, or any other supported provider.
- `load_dotenv`: Reads key-value pairs from your `.env` file and loads them into the process environment. A google search on python-dotenv would suffice for more detail.

#### **Environment Setup**
```python
load_dotenv()
api_key = os.getenv('GROQ_API_KEY')
```
- `load_dotenv()`: Scans the current directory for a `.env` file and loads its contents into memory.
- `os.getenv('GROQ_API_KEY')`: Retrieves the value of `GROQ_API_KEY` from the loaded environment variables.

#### **Message Construction**
```python
system_msg = SystemMessage("You are a Python tutor who explains concepts with simple code examples.")
human_msg = HumanMessage("Explain what a dictionary is in Python with an example.")
messages = [system_msg, human_msg]
```
- `SystemMessage(...)`: Defines the model's role and behavioral constraints. The model will adhere to this instruction for the entire request.
- `HumanMessage(...)`: The actual question being asked.
- `messages`: A Python list containing both messages in order. The model processes them sequentially — system instructions first, then the user query.

#### **Model Initialization**
```python
model = init_chat_model(
    "groq:llama-3.3-70b-versatile",
    api_key = api_key,
)
```
- `"groq:llama-3.3-70b-versatile"`: The format is `provider:model-name`. Here, `groq` is the provider and `llama-3.3-70b-versatile` is Meta's open-source Llama 3.3 model (70 billion parameters) hosted on Groq's infrastructure.
- To switch to a different provider, you would only change this string. For example: `"google_genai:gemini-2.5-flash"` for Gemini, or `"openai:gpt-4.1"` for OpenAI. The rest of the code remains identical.

#### **Invocation & Output**
```python
response = model.invoke(messages)
print(response.content)
```
- `model.invoke(messages)`: Sends the structured message list to the model and returns an `AIMessage` response object.
- `response.content`: Extracts only the text string from the response object. The full response object also contains metadata such as token usage and model information, but `.content` gives us the generated text directly.

---

### 📝 Key Takeaway
The entire point of this project is **portability**. The same `SystemMessage`, `HumanMessage`, `invoke()`, and `.content` pattern works identically whether you are talking to Groq, Google Gemini, or OpenAI. LangChain handles the translation layer between your code and each provider's API internally.

**Maintainer**: Divya Prakash Singh Chauhan 🚀
