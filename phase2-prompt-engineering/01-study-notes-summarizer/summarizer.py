import ollama
import json

SYSTEM_PROMPT = """You are a study assistant that turns messy notes into clean, structured summaries.
Rules:
- Only use information present in the notes given to you. Do not add outside facts.
- If the notes are unclear or incomplete, mention that instead of guessing.
- Always respond in valid JSON format, exactly like this:
{
  "title": "short title for the notes",
  "key_points": ["point 1", "point 2", "point 3"],
  "quiz_question": "one short question to test understanding"
}
"""

messy_notes = """
tokens r pieces of text llm split it. bpe used. embeddings = numbers 
representing meaning. king-man+woman=queen example. attention lets model
look at all words. QKV = query key value. transformer = attention + feedforward
stacked many times. temperature controls randomness low=safe high=creative
"""

response = ollama.generate(
    model='llama3.2',
    system=SYSTEM_PROMPT,
    prompt=f"Summarize these notes:\n\n{messy_notes}"
)

print("--- Raw Output ---")
print(response['response'])

# Try parsing as JSON to prove structured output works
try:
    parsed = json.loads(response['response'])
    print("\n--- Parsed Successfully ---")
    print(f"Title: {parsed['title']}")
    print(f"Key Points: {parsed['key_points']}")
    print(f"Quiz: {parsed['quiz_question']}")
except json.JSONDecodeError:
    print("\n(Could not parse as JSON — model didn't follow format exactly)")