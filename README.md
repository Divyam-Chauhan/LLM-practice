# 🚀 LLM Practice & Learning Journey

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Langchain](https://img.shields.io/badge/Langchain-0.3-orange?logo=python&logoColor=white)
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

### 1. `Langchain 1`
* **Format**: Google Colab Notebook
* **What it does**: A very basic introduction to setting up a chat model and giving the AI a custom "persona" (we make it act like an ignorant maniac!).
* **What you learn**: How to use Langchain to structure an AI's behavior using `SystemMessage` (the instructions you secretly give the AI) and `HumanMessage` (what the user types). It runs perfectly in the cloud on Google Colab, so there's no complex local setup needed.

### 2. `Study helper`
* **Format**: Pure Python Script
* **What it does**: You provide it a paragraph of text, and it automatically generates test questions based on that text.
* **What you learn**: How to use the official, native `google-genai` SDK directly. This project doesn't use the Langchain wrapper; it's just you and the raw Google API talking to each other.

### 3. `Langchain Travel Guide`
* **Format**: Python Script
* **What it does**: A simple local application where the AI is instructed to act as a focused travel assistant.
* **What you learn**: How to set up Langchain *locally* on your machine and how to safely store your secret API keys in a `.env` file instead of hardcoding them into your scripts.

### 4. `Langchain Tutor Assistant`
* **Format**: Python Script
* **What it does**: An AI tutor that explains Python programming concepts (like dictionaries) with code examples.
* **What you learn**: You will learn how easy it is to **swap brains**! Instead of Google's Gemini, this project uses Langchain to connect to a massive open-source model (`Llama-3.3-70b-versatile`) hosted on Groq, demonstrating how flexible standard frameworks can be.

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
