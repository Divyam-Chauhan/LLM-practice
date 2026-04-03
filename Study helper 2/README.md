# 🎓 Smart Study Assistant (Study Helper 2)

An enhanced version of the Study Assistant that introduces **System Instructions** and **Generation Tuning** to control the AI's behavior and response style.

### 🧠 Core Concepts

#### **1. Chat Model Roles**
Conversational AI models use three distinct roles to structure logic:
- **System**: Background instructions that define the model's personality, tone, and rules before the user even speaks.
- **User**: The actual input or question from the human.
- **Assistant**: The model's response based on the system instructions and user input.

#### **2. System Instructions**
This project uses a dictionary of personalities (Friendly vs. Academic). By passing a `system_instruction` to the model, we can force it to behave like a specific character without including those instructions in every single user prompt.

#### **3. Generation Tuning (`GenerateContentConfig`)**
We can control the technical behavior of the model using two primary parameters:
- **Temperature**: Controls the randomness of the output. 
    - `0.0` is deterministic (best for facts/code).
    - `0.4 - 0.7` is balanced (best for general study).
    - `1.0+` is creative (best for brainstorming).
- **Max Output Tokens**: Limits the technical length of the response to manage both costs and conciseness. A google search on how LLM tokens are calculated would suffice for more detail.

---

### 🔍 Code Execution Breakdown

#### **Imports**
```python
from google.genai import types
```
- `types`: This module provides access to structured data classes like `GenerateContentConfig`, which we use to pass configuration settings to the model.

#### **The Personalities Dictionary**
We store our system instructions in a standard Python dictionary. This allows the application to switch between roles (e.g., a "Friendly Assistant" that uses simple terms or an "Academic Professor" that uses formal terminology) by simply changing a key.

#### **Advanced Generation Call**
```python
response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction=system_prompt,
        temperature=0.4,
        max_output_tokens=1000
    ),
    contents=question
)
```
- `system_instruction`: We pass the selected persona here. This is legally binding for the AI's behavior for the duration of the request.
- `config`: Instead of a simple prompt, we pass a `GenerateContentConfig` object containing our tuning parameters.

---

### 🛠️ Execution Guide

1.  **Dependencies**:
    Ensure you have the required packages (a google search on managing virtual environments is recommended for local development):
    ```bash
    pip install -r requirements.txt
    ```
2.  **Run the Script**:
    ```bash
    python app.py
    ```

**Maintainer**: Divya Prakash Singh Chauhan 🚀
