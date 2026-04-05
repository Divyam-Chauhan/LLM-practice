# 🔗 Introduction to LangChain

This is your entry point to understanding **LangChain** — what it is, why it exists, and how it works. The accompanying notebook (`Langchain 1.ipynb`) demonstrates LangChain's core functionality using Google Gemini on Google Colab.

---

### ⚙️ The Problem LangChain Solves

#### Manual Repetition in LLM Development
When building LLM applications directly with provider SDKs (like `google-genai` or `groq`), developers are required to manually:
- Format and structure prompts differently for each provider.
- Handle authentication flows that vary across providers.
- Parse response objects that have different schemas per provider.
- Rewrite tool-calling logic when switching models.

#### The Provider Problem
Consider an application built using Groq's SDK. If the requirement changes to use Google Gemini or OpenAI instead, the developer faces:
- **Different API structures**: Each provider has its own endpoint patterns and request formats.
- **Different response formats**: The shape of the returned data changes between providers.
- **Different message formatting**: How you structure system/user messages varies.

This means significant portions of the application code must be rewritten every time you switch providers.

#### Growing Complexity
As LLM applications evolve beyond simple question-answering, additional requirements increase complexity:
- Adding conversation memory.
- Integrating external tools (web search, calculators, databases).
- Handling errors and rate limits gracefully.

Building and maintaining all of this from scratch is time-consuming, error-prone, and difficult to scale.

---

### 🔧 What is LangChain?

LangChain is a framework that provides **standardized interfaces** and **pre-built modular components** to build LLM-powered applications. It abstracts away provider-specific differences so that your application logic is written once and works across any supported provider.

#### Why LangChain Specifically?
- **Adoption**: Over 120,000+ GitHub stars, used by thousands of companies.
- **Provider Support**: Integrations for 100+ LLM providers out of the box.
- **Documentation**: Extensive tutorials and active community support.
- **Modularity**: Use only what you need, extend when necessary.

#### Other Frameworks in This Space
LangChain is not the only option. Other frameworks include **LlamaIndex**, **Haystack**, **Semantic Kernel**, and **CrewAI** (a google search on LLM framework comparisons would suffice for exploring alternatives).

---

### 🧱 Core Components of LangChain

LangChain is organized into modular components. The ones used in this project are:

#### 1. Models
LangChain's `init_chat_model` is a universal model initializer. It accepts a provider-prefixed string (e.g., `"google_genai:gemini-2.5-flash"`) and returns a standardized chat model object. This is what makes provider-switching a one-line change.

#### 2. Messages
Messages are structured objects that represent conversation context. Each message has:
- **Role**: Identifies the message type (System, Human, or AI).
- **Content**: The actual text payload.

**Message types relevant here**:
- `SystemMessage`: Background instructions defining the model's behavior and personality. The model reads this first and follows it throughout the conversation.
- `HumanMessage`: The actual user input or question.
- `AIMessage`: The model's generated response (returned after invocation).

There are additional components in LangChain (like **Tools**, **Agents**, **Memory**) that are covered in later projects.

---

### 🛠️ Setup (Google Colab)

This project runs entirely on Google Colab — no local installation required.

1. Open the notebook in Colab (click the "Open in Colab" badge at the top of the `.ipynb` file).
2. Get a free Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
3. Store it in Colab Secrets: Click the 🔑 icon in the left sidebar → Add new secret → Name: `GEMINI_API_KEY` → Paste your key → Enable notebook access.

---

### 🔍 Code Execution Breakdown

The following is a line-by-line explanation of each cell in the notebook:

#### **Cell 1: Package Installation**
```python
!pip install -U langchain-google-genai
```
- `!`: Tells Colab to execute this as a shell command, not Python code.
- `pip install -U`: Installs or updates a Python package to the latest version (a google search on pip package management would suffice).
- `langchain-google-genai`: This is the LangChain integration package specifically for Google's Gemini models. Each LLM provider has its own LangChain package (e.g., `langchain-groq` for Groq, `langchain-openai` for OpenAI).

#### **Cell 2: Imports and API Key**
```python
from google.colab import userdata
api_key = userdata.get('GEMINI_API_KEY')
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, SystemMessage
```
- `google.colab.userdata`: A Colab-specific module that provides access to secrets stored in the Colab Secrets manager. This module only works inside Google Colab.
- `userdata.get('GEMINI_API_KEY')`: Retrieves the API key value stored under the name `GEMINI_API_KEY` from Colab Secrets.
- `init_chat_model`: LangChain's universal model initializer. It accepts a `provider:model-name` string and returns a ready-to-use chat model, regardless of the underlying provider.
- `HumanMessage`, `SystemMessage`: Structured message classes from LangChain that represent conversation roles. These are provider-agnostic — the same message objects work with Gemini, Groq, OpenAI, or any other supported provider.

#### **Cell 3: Message Construction**
```python
system_msg = SystemMessage("You are an ignorant maniac that doesn't want to follow orders.")
human_msg = HumanMessage("Hello, how are you?")
messages = [system_msg, human_msg]
```
- `SystemMessage(...)`: Defines the model's behavioral constraints. The model will follow these instructions for the entire request. Here we are giving the AI a deliberately rebellious personality to demonstrate how powerful system instructions are.
- `HumanMessage(...)`: The user's actual input that the model will respond to.
- `messages`: A Python list containing both messages in order. The model processes them sequentially — system instructions first, then the user query.

#### **Cell 4: Model Initialization**
```python
model = init_chat_model(
    "google_genai:gemini-2.5-flash",
    api_key = api_key,
)
```
- `"google_genai:gemini-2.5-flash"`: The format is `provider:model-name`. Here, `google_genai` is the provider and `gemini-2.5-flash` is the specific model.
- `api_key`: The authentication credential retrieved from Colab Secrets.
- The returned `model` object is a standardized LangChain chat model. To switch to a completely different provider, you would only change this string (e.g., `"groq:llama-3.3-70b-versatile"` or `"openai:gpt-4.1"`). The rest of the code remains identical.

#### **Cell 5: Invocation**
```python
response = model.invoke(messages)
```
- `model.invoke(messages)`: Sends the structured message list to the model and returns an `AIMessage` response object. The `invoke()` method is LangChain's standard way to call any model — it works the same regardless of provider.

#### **Cell 6: Output**
```python
print(response.content)
```
- `response.content`: The full response object contains metadata (token usage, model info, etc.). The `.content` attribute extracts only the generated text string.

---

### 🔭 What LangChain Can Do (Beyond This Project)

This project only scratches the surface. LangChain's full capabilities include:
- **Memory**: Maintaining conversation history across multiple exchanges so the AI remembers what was said earlier.
- **Tools**: Giving the AI the ability to execute real actions like searching the web, querying databases, or performing calculations.
- **Agents**: Autonomous systems that decide which tools to use and in what order, based on the user's request.
- **RAG (Retrieval-Augmented Generation)**: Connecting the AI to your own documents and data sources so it can answer questions about your specific content.
- **Chains**: Linking multiple LLM calls and operations together into structured workflows.
- **Callbacks**: Monitoring and logging model behavior in real-time for debugging and observability.

These concepts are explored in later projects within this repository.

**Maintainer**: Divya Prakash Singh Chauhan 🚀
