# ❓ Question Generator Assistant

A practice exercise that generates questions from input text using Google Gemini.

### What It Does
You provide a piece of content, and the model generates relevant questions based on that text.

### Code Breakdown
```python
def question_generator(text):
    user_prompt = "Generate questions from the following content:\n" + text
    response = client.models.generate_content(model="gemini-2.5-flash", contents=user_prompt)
    return response
```
- `question_generator(text)`: Builds a prompt from the provided content and sends it to the Gemini model.
- Uses `genai.Client` with `generate_content`, matching the same pattern as the other practice exercises.
- The prompt is the main difference: it asks the model to create questions from input text.

### Example
```python
response = question_generator("Large Language Models (LLMs) are AI systems trained on massive text data.")
print(response.text)
```
The prompt includes the instruction and the source text together. The model returns generated questions.

### Run
```bash
pip install -r requirements.txt
python QuestionGenerator.py
```
