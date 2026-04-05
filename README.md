# 🚀 LLM Practice & Learning Journey

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Langchain](https://img.shields.io/badge/Langchain-1.2+-orange?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)


Welcome to my repository!

This is a clean, organized collection of my learnings as I dive into the world of Large Language Models (LLMs). I believe the best way to understand complex AI concepts is to break them down into simple, working examples—no BS, no unnecessary jargon, just the essentials.

I will be actively maintaining and growing this directory throughout my journey. Whether you're an absolute beginner or just looking for simple reference templates, **you are very welcome to learn along with me!**

---

## 🛠️ Prerequisites (What you need before you start)

Before you dive into any of the folders, make sure you have the following ready on your computer:

1. **Python**: You'll need Python installed (version 3.10 or higher is recommended).
2. **Git**: Basic Git knowledge to clone this repository to your local machine.
3. **API Keys**: Since we are talking to AI models hosted on the internet, we need a "key" to unlock access to them. Don't worry, they are free for learning!
   - **Google Gemini API Key**: Used in most of our projects. [Get it here for free.](https://aistudio.google.com/app/apikey)
   - **Groq API Key**: Groq is a super-fast platform for running open-source models like Llama. [Get it here for free.](https://console.groq.com/keys)

---

## 📂 Repository Map & What You'll Learn here

Every folder in this repository is a standalone mini-project tailored to teach a specific concept. 

### 1. `Intro to LLM` ⭐ Start Here
* **Format**: Pure Python Script
* **What it does**: Takes a paragraph of text and automatically generates study questions from it using Google Gemini.
* **What you learn**: **This is your starting point.** It covers what an LLM is, how applications communicate with one, what an SDK is, why we use `google-genai`, how to securely manage API keys with `.env` files, and a complete line-by-line code breakdown of the `generate_content` method.

### 2. `Study helper 2`
* **Format**: Pure Python Script
* **What it does**: An enhanced version of the Study Assistant with switchable AI personalities (Friendly vs. Academic) and output tuning.
* **What you learn**: How **System Instructions** work via `GenerateContentConfig`, and how to control output using **Temperature** (randomness) and **Max Output Tokens** (length). The README explains Chat Model Roles (System, User, Assistant) in detail.

### 3. `Intro to Langchain`
* **Format**: Google Colab Notebook
* **What it does**: Sets up a chat model and gives the AI a custom persona using LangChain directly in the browser.
* **What you learn**: This is where **LangChain is fully introduced** — the Provider Problem (why switching between AI providers is painful without a framework), what LangChain solves, its core components (Models, Messages), and a detailed line-by-line breakdown of the notebook code. The README ends with an overview of LangChain's broader capabilities (Memory, Tools, Agents, RAG).

### 4. `Langchain Travel Guide`
* **Format**: Python Script
* **What it does**: A local application where the AI acts as a focused travel recommendation assistant using LangChain and Google Gemini.
* **What you learn**: How to set up LangChain locally on your machine using `init_chat_model`, and how to safely manage API keys using `.env` files.

### 5. `Langchain Tutor Assistant`
* **Format**: Python Script
* **What it does**: An AI tutor that explains Python programming concepts with code examples, powered by Meta's open-source Llama 3.3 model hosted on Groq.
* **What you learn**: How to **swap providers** in LangChain — switching from Google Gemini to Groq (Llama 3.3) with a single line change. Demonstrates that `SystemMessage`, `HumanMessage`, `invoke()`, and `.content` work identically across any supported backend.

---

## 🚀 How to Run These Projects on Your Computer

1. **Clone the repository:**
   Download the code to your local machine using your terminal:
   ```bash
   git clone https://github.com/Divyam-Chauhan/LLM-practice.git
   cd LLM-practice
   ```

2. **Navigate to the project you want to learn:**
   ```bash
   cd "Langchain Travel Guide" # Or any other folder
   ```

3. **Install the Requirements:**
   Each script folder has strict, minimal dependencies. Install them using:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Your Secrets (`.env` file):**
   Never put your secret API keys directly in the code! Instead, create a file named `.env` in the folder you are working in. 
   
   If you are doing a Gemini project, your `.env` file should look like this:
   ```env
   GEMINI_API_KEY="your_actual_key_here"
   ```
   If you are doing a Groq project, it should look like this:
   ```env
   GROQ_API_KEY="your_actual_key_here"
   ```

5. **Run the Code!**
   ```bash
   python app.py
   ```

---

## 🔮 What's Next? (Roadmap)
I'll be consistently updating this repository. In the future, look forward to new folders exploring concepts like:
- **RAG (Retrieval-Augmented Generation)**: Teaching the AI to read our own documents.
- **Memory**: Giving the AI the ability to remember past conversations.
- **Agents**: AI that can use tools (like searching the web or calculating math).

Happy learning! 💡
