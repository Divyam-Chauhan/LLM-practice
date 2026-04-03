# 📚 AI Study Assistant (Study Helper)

Building a custom LLM-powered application using Python. This project demonstrates how to interface directly with a generative model using a specialized software library (SDK).

### ⚙️ Why Python for LLM Integration?
Using a programming language like Python offers features that standard chat interfaces lack:
- **Custom logic**: You can preprocess input and post-process output for specific use cases.
- **Scalability**: Python scripts can be automated to handle large datasets.
- **Integration**: Easily connect your LLM to other APIs or local databases.

---

### 🧱 Technical Components
1. **The Model**: We use **`gemini-2.5-flash`**. This is the core logical engine that processes your input text and generates the response.
2. **The SDK**: We use **`google-genai`**. An SDK (Software Development Kit) is a set of pre-written code used to simplify communication with an external API. A google search on the architecture of SDKs would suffice for deeper understanding.
3. **The Prompt**: This is the literal string of instructions sent to the model's interface.

---

### 🛠️ Local Configuration

1.  **Dependency Installation**: 
    Install the necessary package using the following command (a google search on Python package management would suffice for details):
    ```bash
    pip install -U google-genai
    ```
2.  **API Key Generation**: 
    Generate a unique API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
3.  **Environment Configuration (`.env`)**:
    Store your secret API key safely in a `.env` file to separate configuration from code:
    ```env
    GEMINI_API_KEY="your_actual_key_here"
    ```

---

### 🔍 Code Execution Breakdown

The following is a line-by-line explanation of the logic in `app.py`:

#### **Imports**
- `import os`: This standard library module allows Python to interact with the operating system, specifically for retrieving environment variables.
- `from dotenv import load_dotenv`: This package reads key-value pairs from a `.env` file and adds them to the environment variables.
- `from google import genai`: This is the direct interface for Google's Generative AI services.

#### **Initialization & Authentication**
```python
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
```
- `load_dotenv()`: This call scans your directory for a `.env` file and loads its contents into memory.
- `genai.Client`: This instantiates a class used to authenticate your session and manage requests to the Gemini API. We refer to this instance as the `client`.

#### **Generation Function**
```python
def question_generator(text):
    user_prompt = "Generate questions from the following content:\n" + text
    response = client.models.generate_content(model="gemini-2.5-flash", contents=user_prompt)
    return response
```
- `user_prompt`: We concatenate a static instruction with the dynamic user text.
- `client.models.generate_content()`: This is the primary method used to send a request. It requires the `model` identifier and the `contents` (your prompt). 
- **Deep Dive**: `generate_content` is asynchronous-capable but here it runs synchronously, returning a complex `GenerateContentResponse` object. A google search on how API response objects work in Python would suffice for more detail.

#### **Output Handling**
```python
response = question_generator("Large Language Models...")
print(response.text)
```
- `response.text`: Because the response object contains metadata (like safety ratings and token counts), we access the `.text` attribute to display only the generated string.

---

### 📝 Final Note
The separation of code and API keys using `.env` is essential for secure software development. This foundation allows for more complex features like custom system instructions and temperature tuning.

**Maintainer**: Divya Prakash Singh Chauhan 🚀
