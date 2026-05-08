Building LLM Applications using Python | Part 1
Introduction
So far, we have understood what LLMs are and have explored their different capabilities using no-code tools like n8n, ChatGPT, Google Gemini, and Stable Diffusion. These tools are excellent for automating workflows without writing any code.

However, sometimes we require more flexibility, control, and the ability to build custom features. This is where programming languages like Python come in. This unit will introduce you to building your first LLM-powered application using Python.

Why Use a Programming Language?
While no-code tools are powerful, building applications with code provides:

More Flexibility: Integrate with any API or service you want.
More Control: Build custom User Interfaces (UIs) for your chatbots and add detailed logging for enhanced debugging.
n8n vs Code
When to use n8n
Quick prototypes needed in hours.
Simple, straightforward workflows.
Non-technical team members need to maintain it.
When to use Python
Custom logic is required.
Complex error handling is necessary.
You need to deploy at scale for customer-facing applications.
What We're Building: An AI Study Assistant
We will build an AI-powered Study Assistant that:

Explains complex topics in simple words.
Answers your questions in natural language.
Works anytime you need help.
How Applications Talk to LLMs
Connecting to a Large Language Model (LLM) involves three main methods:

Running LLMs locally on your machine.
Making direct HTTP requests to an LLM's API endpoint.
Using packages/libraries provided by the LLM provider.
We will be using the third method, as it's the most common and efficient approach used by developers.

Advantages of Using Libraries
Removes unnecessary manual steps like formatting raw HTTP calls.
Handles authentication and errors internally.
Allows us to focus on building the actual application.
The Three Essential Components
Building an LLM application is like making a burger. You need three key ingredients:

The Brain (LLM): The AI model that understands and generates text.
The Connector (API): The link between your application and the LLM.
Your Instructions (Prompt): The instructions for the LLM to perform a specific task.
Python Packages for LLMs
LLM providers typically offer official Python packages (SDKs) to make integration seamless. These packages handle things like authentication, request formatting, and error handling so you can focus on building.

Here are a few popular ones:

google-genai: For Google's Gemini family of models.
openai: For OpenAI's GPT models (e.g., GPT-4).
anthropic: For Claude models (e.g., Sonnet, Opus).
deepseek-ai: For DeepSeek models.
For our project, we will use the google-genai package because Gemini offers a generous free tier, allowing us to build and experiment without cost.

Note
Learning to use one of these packages makes it much easier to use others. Once you learn to drive one car, you can easily switch and drive another.
Let's Build our Study Assistant
We'll use Google Colab for this project and the google-genai package to interact with the Gemini LLM.

Step 1: Setting Up The Environment
Go to Google Colab
Create a new notebook and name it ai_powered_study_assistant.ipynb.
Install the Google Gemini package by running the following command in a cell:

PYTHON
1
!pip install -U google-genai
! tells Colab to execute this as a shell command.
pip is the Python Package Installer.
-U flag updates the package to the latest version if it's already installed.
Step 2: Get Your API Key
Go to Google AI Studio
Sign in and create a new API key.
Copy the key. We'll need it soon.
Step 3: Securely Store the API Key in Colab
To avoid pasting your API key directly in the code, we'll use Colab's "Secrets" feature.

Click the key icon in the left sidebar of your Colab notebook.
Click "Add new secret".
Enter the name as GEMINI_API_KEY.
Paste your copied API key into the "Value" field.
Make sure the "Allow notebook access" toggle is enabled.
Step 4: Write the Python Code
Now, let's write the code to connect to the Gemini API and build our study assistant.

Import Libraries and Access the API Key
PYTHON
12345678
import google.generativeai as genaifrom google.colab import userdata# Fetch the API key from Colab secretsapi_key = userdata.get("GEMINI_API_KEY")# Initialize the Gemini clientclient = genai.configure(api_key=api_key)
Create the Study Assistant Function
This function will take a user's prompt, send it to the Gemini model, and return the response.

PYTHON
1234567
def study_assistant(user_prompt):  """  Sends a prompt to the Gemini model and gets a response.  """  model = genai.GenerativeModel('gemini-2.5-flash')  response = model.generate_content(user_prompt)  return response.text
genai.GenerativeModel('gemini-2.5-flash'): Specifies which model to use.
model.generate_content(user_prompt): Sends the actual prompt to the LLM.
response.text: The response object contains more than just the text; we extract only the text part.
Call the Function and Print the Output
PYTHON
123456
# Ask the study assistant a questionuser_question = "Explain Generative AI in simple terms"output = study_assistant(user_question)# Print the resultprint(output)
Full Working Code -Using google-genai
Here is the complete code you can run in your Google Colab notebook.

PYTHON
1234567891011
from google import genaifrom google.colab import userdataclient = genai.Client(api_key=userdata.get("GEMINI_API_KEY"))def study_assistant(user_prompt):  response = client.models.generate_content(    model="gemini-2.5-flash",    contents=user_prompt  )  return response 
Expand
Full Working Code -Using groq

Similar to google-genai, groq is another package that allows you to make API calls to various models. Below is an example code snippet using groq.
To use Groq, you first need to install the Groq package. You can install groq using the following command:
1
pip install groq
PYTHON
1234567891011
from groq import Groqfrom google.colab import userdataclient = Groq(api_key=userdata.get("GROQ_API_KEY"))def study_assistant(user_prompt):    response = client.chat.completions.create(        model="llama-3.1-8b-instant",   # You can change with any Groq model        messages=[            {"role": "user", "content": user_prompt}        ] 
Expand
The Groq response object contains the model’s generated output along with useful metadata like token usage. You can access the final text message using response.choices[0].message.content.

You have built your first LLM-powered application using Python! This may be a simple version, but it’s the foundation for everything we will build next.