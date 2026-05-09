# 🎨 Tone Modifier

A practice exercise that modifies the tone of a given sentence using Google Gemini.

### What It Does
You provide a sentence and a target tone (e.g., formal, casual, poetic), and the model rewrites the sentence in that tone.

### Code Breakdown
```python
def modify_tone(text):
    response = client.models.generate_content(model = "gemini-2.5-flash", contents = text)
    return response
```
- `modify_tone(text)`: Accepts a prompt string containing both the tone instruction and the input text.
- Uses the same `generate_content` method and `genai.Client` pattern from `app.py`.
- The only difference is the prompt — instead of generating questions, we ask the model to transform tone.

### Example
```python
response = modify_tone("Translate its tone to formal: 'Knowledge is power.'")
print(response.text)
```
The prompt embeds the instruction and the input in a single string. The model returns the rewritten sentence.

### Run
```bash
pip install -r requirements.txt
python ToneModifier.py
```
