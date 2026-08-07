import tiktoken

# This is the tokenizer used by GPT-4 / GPT-4o models
encoding = tiktoken.encoding_for_model("gpt-4o")

sentences = {
    "English": "The weather is really nice today.",
    "Hindi": "आज मौसम बहुत अच्छा है।",
    "Marathi": "आज हवामान खूप छान आहे."
}

for lang, text in sentences.items():
    tokens = encoding.encode(text)
    print(f"\n{lang}: \"{text}\"")
    print(f"Token count: {len(tokens)}")
    print(f"Tokens: {[encoding.decode([t]) for t in tokens]}")