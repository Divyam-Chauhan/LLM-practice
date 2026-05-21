# Tool Use & Function Calling in LLMs

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Divyam-Chauhan/LLM-practice/blob/main/Tool%20Use%20%26%20Function%20Calling/Tool%20use%20and%20function%20calling.ipynb)

This project introduces **Tool Use**, also called **Function Calling**. It shows how an LLM can decide when external information is needed, request a function call with structured arguments, and then use the returned data to generate a final answer.

The notebook (`Tool use and function calling.ipynb`) builds a real-time weather assistant using **Groq**, **Llama 3.3**, and the **OpenWeatherMap API**.

---

### What Problem Tool Calling Solves

LLMs are trained on large amounts of text data, but their knowledge is not live. A model can answer many general questions from its training, but it cannot automatically know current information unless your application connects it to an external source.

Examples of data that normally requires external access:
- Current weather conditions.
- Live stock prices.
- Latest news headlines.
- Real-time sports scores.
- Calendar events or private user data.

If a user asks for current weather and the model has no tool, it may guess, refuse, or provide outdated information. Tool calling solves this by letting the application expose specific functions that the model can request.

---

### What is Tool Calling?

Tool calling is a model capability where the LLM receives a list of available tools and decides whether one of them is needed to answer the user.

Important: the LLM does **not** execute the Python function by itself.

The model only returns a structured tool call, such as:
- which function should be used,
- what arguments should be passed,
- and why the function is relevant based on the user request.

Your Python code must then:
1. Read the tool call returned by the model.
2. Execute the real function locally.
3. Send the function result back to the model.
4. Ask the model to produce the final natural-language answer.

This project uses a weather function as the example tool, but the same pattern can be used for email sending, spreadsheet updates, calendar scheduling, database queries, calculations, web search, or any external API.

---

### Why Groq and Llama Are Used Here

This project uses **Groq** as the model provider and **`llama-3.3-70b-versatile`** as the model.

Groq is a hosted inference platform that can run open-source models through an API. In this notebook, Groq accepts the chat messages, the tool definition, and the tool-choice setting. If the model decides that the weather tool is needed, Groq returns a structured `tool_calls` response.

`llama-3.3-70b-versatile` is the model name passed into the Groq chat completion request. A google search on Meta's Llama model family would suffice for deeper background.

---

### Prerequisites

This notebook is designed for **Google Colab**.

You need:
1. A **Groq API key** for model access.
2. An **OpenWeatherMap API key** for real-time weather data.
3. The `groq` package installed in the notebook.
4. The `requests` package available for HTTP API calls.

In Colab, keys are stored using **Colab Secrets** through `google.colab.userdata`.

Expected secret names in the notebook:
```text
GROQ_API_KEY
openweather_API_KEY
```

The OpenWeatherMap endpoint used in this project is:
```text
http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}
```

The `{location}` value is replaced with the city name, and `{api_key}` is replaced with your OpenWeatherMap API key.

---

### Code Execution Breakdown

The following is a line-by-line explanation of the notebook logic.

#### **Cell 1: Install Groq**
```python
!pip install groq
```
- `!`: In Google Colab, this tells the notebook to run a shell command instead of normal Python code.
- `pip install groq`: Installs the official Groq Python SDK so the notebook can send requests to Groq-hosted models.

---

#### **Cell 2: Import Colab Secrets**
```python
from google.colab import userdata
```
- `google.colab`: A Colab-specific package that provides notebook utilities.
- `userdata`: Gives Python access to secrets stored in the Colab sidebar. This is how API keys are loaded without writing the actual key directly in the notebook.

---

#### **Cell 3: Import the Groq Client**
```python
from groq import Groq
```
- `Groq`: The client class from the Groq SDK. It creates an authenticated connection to Groq's API.

---

#### **Cell 4: Create the Groq Client**
```python
client = Groq(
    api_key=userdata.get("GROQ_API_KEY"),
)
```
- `userdata.get("GROQ_API_KEY")`: Reads the Groq API key from Colab Secrets.
- `Groq(...)`: Creates the API client using that key.
- `client`: The object used later to call `client.chat.completions.create(...)`.

---

#### **Cell 5: Import JSON**
```python
import json
```
- `json`: A standard Python library for converting between Python objects and JSON strings.
- It is used here because tool-call arguments come back as JSON text, and tool results are sent back in a JSON-compatible format.

---

#### **Cell 6: Import Requests and Pretty Print**
```python
import requests
from pprint import pprint
```
- `requests`: A Python package used to make HTTP requests. Here it sends a request to the OpenWeatherMap API.
- `pprint`: Pretty-prints Python objects in a readable format. The notebook imports it for debugging and inspection, even though the main flow does not depend on it.

---

### The Weather Function

#### **Cell 7: Define `get_weather`**
```python
def get_weather(location):
  api_key = userdata.get("openweather_API_KEY")
  url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}"

  response = requests.get(url)
  data = response.json()
  if data.get("cod") == 200:
    return json.dumps({
        "location": location,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
    })
  else:
    return json.dumps({
      "oops! something went wrong."
      })
```
- `def get_weather(location):`: Defines a reusable Python function that accepts a city name.
- `api_key = userdata.get("openweather_API_KEY")`: Reads the OpenWeatherMap API key from Colab Secrets.
- `url = f"...{location}...{api_key}"`: Builds the OpenWeatherMap request URL using an f-string.
- `q={location}`: Sends the city name to the weather API.
- `units=metric`: Requests Celsius temperature values.
- `appid={api_key}`: Authenticates the request with OpenWeatherMap.
- `response = requests.get(url)`: Sends the HTTP GET request.
- `data = response.json()`: Converts the JSON response body into a Python dictionary.
- `if data.get("cod") == 200:`: Checks whether OpenWeatherMap returned a successful response.
- `data["main"]["temp"]`: Reads the current temperature from the API response.
- `data["weather"][0]["description"]`: Reads the text description of the weather condition.
- `json.dumps(...)`: Converts the simplified Python data into a JSON string so it can be sent back into the LLM flow.
- `else`: Handles failed API responses. In a stronger version, this branch should return a normal dictionary such as `{"error": "Oops! Something went wrong."}` before converting it to JSON.

This function is the actual tool. It is normal Python code, and it is executed by your program, not by the LLM.

#### **Cell 8: Test the Weather Function Directly**
```python
print(get_weather("Jaipur"))
```
- Calls `get_weather` before involving the LLM.
- This confirms that the OpenWeatherMap API key, URL, and response parsing are working.
- Testing the function directly is useful because tool calling depends on the external function being correct.

---

### The Tool Definition

#### **Cell 9: Describe the Function to the LLM**
```python
tools = [
  {
    "type": "function",
    "function": {
      "name": "get_weather",
      "description": "Get current weather for a city",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "City name like Mumbai, London"
          }},
        "required": ["location"]
      }}}
]
```
- `tools`: A list of tool definitions that will be sent to the model.
- `"type": "function"`: Tells the model that this tool represents a callable function.
- `"function"`: Contains the function metadata and parameter schema.
- `"name": "get_weather"`: The exact function name the model may request.
- `"description"`: Explains when the function should be used.
- `"parameters"`: Defines the input format using JSON Schema.
- `"type": "object"`: Means the function expects an object containing named fields.
- `"properties"`: Lists the available input fields.
- `"location"`: The only input field for this tool.
- `"type": "string"`: The location value must be text.
- `"required": ["location"]`: The model must provide `location` when requesting this tool.

The tool definition does not execute anything. It only tells the model what tool exists and what input format is valid.

---

### Conversation Messages

#### **Cell 10: Build the Message List**
```python
llm_messages = [
    {
        "role": "system",
        "content": "You are a helpful weather assistant, use get_weather function when asked about weather"
    },
    {
        "role": "user",
        "content": "What is the weather of Jaipur?"
    }
]
```
- `llm_messages`: The conversation history sent to the model.
- `"role": "system"`: Gives the model background instructions before the user request.
- `"content": "...use get_weather..."`: Tells the model that weather questions should use the weather function.
- `"role": "user"`: Represents the user's actual question.
- `"What is the weather of Jaipur?"`: The prompt that requires real-time weather data.

The model receives both the message list and the tool list in the next cell.

---

### First LLM Call

#### **Cell 11: Send Messages and Tools to Groq**
```python
response = client.chat.completions.create(
    messages = llm_messages,
    model = "llama-3.3-70b-versatile",
    tools = tools,
    tool_choice = "auto",
)
```
- `client.chat.completions.create(...)`: Sends a chat completion request to Groq.
- `messages = llm_messages`: Provides the system instruction and user question.
- `model = "llama-3.3-70b-versatile"`: Selects the Llama model hosted by Groq.
- `tools = tools`: Provides the weather tool definition.
- `tool_choice = "auto"`: Allows the model to decide whether a tool is needed.

If the model decides it can answer directly, the response will contain normal text in `response.choices[0].message.content`.

If the model decides it needs the weather function, the response will contain `tool_calls`.

---

### Handling the Tool Call

#### **Cell 12: Execute the Requested Tool**
```python
response_message = response.choices[0].message
if response_message.tool_calls:
  tool_call = response_message.tool_calls[0]
  arguments = json.loads(tool_call.function.arguments)
  location = arguments['location']
  weather_data = get_weather(location)
  # print(f"weather_data at : {location} : {weather_data}")

  llm_messages.append({
      "role" : "tool",
      "tool_call_id" : tool_call.id,
      "content" : json.dumps(weather_data)
  })

  final_response = client.chat.completions.create(
      messages = llm_messages,
      model = "llama-3.3-70b-versatile",
  )
  print(final_response.choices[0].message.content)
```
- `response_message = response.choices[0].message`: Extracts the model's message from the first response.
- `if response_message.tool_calls:`: Checks whether the model requested a tool.
- `tool_call = response_message.tool_calls[0]`: Gets the first requested tool call.
- `tool_call.function.arguments`: Contains the arguments generated by the model as a JSON string.
- `json.loads(...)`: Converts the JSON string into a Python dictionary.
- `location = arguments['location']`: Reads the city name chosen by the model.
- `weather_data = get_weather(location)`: Executes the actual Python weather function.
- `llm_messages.append(...)`: Adds the tool result to the conversation history.
- `"role": "tool"`: Marks this message as output from a tool, not a user or assistant message.
- `"tool_call_id": tool_call.id`: Links the tool result to the exact tool call requested by the model.
- `"content": json.dumps(weather_data)`: Sends the weather result back in a JSON-compatible form.
- `final_response = client.chat.completions.create(...)`: Makes a second model call using the updated message history.
- `print(final_response.choices[0].message.content)`: Prints the final natural-language answer.

The first model call decides whether a function is needed. The Python code executes the function. The second model call turns the tool result into a clean response for the user.

---

### Inspecting the Raw Tool Call

#### **Cell 13: Print the Full Response**
```python
print(response.model_dump_json(indent = 2))
```
- `response.model_dump_json(...)`: Converts the full Groq response object into formatted JSON text.
- `indent = 2`: Makes the output easier to read.

This is useful for understanding the internal structure of a tool-calling response. In the raw response, the important fields are:
- `finish_reason`: Often shows `"tool_calls"` when the model requested a tool.
- `message.tool_calls`: Contains the tool call details.
- `function.name`: Shows which function the model wants to call.
- `function.arguments`: Shows the arguments the model generated.
- `usage`: Shows token usage and timing metadata.

---

### Full Tool Calling Flow

The complete flow is:

1. The developer writes a real Python function named `get_weather`.
2. The developer describes that function to the model using a JSON tool schema.
3. The user asks for live weather information.
4. The model receives the user message and the tool definition.
5. The model returns a structured tool call for `get_weather`.
6. Python reads the tool call and executes `get_weather(location)`.
7. Python sends the tool result back to the model as a `"tool"` message.
8. The model produces the final answer in natural language.

This is the core pattern behind tool use in LLM applications.

---

### What You've Learned

After working through this project, you now understand:

1. Why normal LLM responses are limited when the question requires real-time data.
2. What tool calling is and why the LLM does not execute the function itself.
3. How to define a Python function that retrieves external API data.
4. How to describe that function to the model using a JSON schema.
5. How `tools` and `tool_choice="auto"` affect the model request.
6. How to detect and parse `tool_calls`.
7. How to send tool results back to the model for a final answer.

This project is the foundation for more advanced LLM applications involving tools, agents, and external systems.

**Maintainer**: Divya Prakash Singh Chauhan
