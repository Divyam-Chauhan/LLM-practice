# 🌍 Language Translator

A practice exercise that translates text from one language to another using Google Gemini.

### What It Does
You provide a sentence and a target language (e.g., Hindi, Spanish, French), and the model translates it.

### Code Breakdown
```python
def language_translator(user_prompt):
    response = client.models.generate_content(model="gemini-2.5-flash", contents=user_prompt)
    return response
```
- `language_translator(user_prompt)`: Identical structure to `modify_tone` and `question_generator`. Accepts a prompt and passes it directly to the model.
- The function name and prompt content are the only differences from other exercises. The SDK call is exactly the same.

### Example
```python
response = language_translator("Translate this to Hindi:'Welcome to the course Building LLm Applications'")
print(response.text)
```
The prompt contains both the target language and the text to translate in a single string. The model returns the translated output.

### Run
```bash
pip install -r requirements.txt
python LanguageTranslator.py
```
