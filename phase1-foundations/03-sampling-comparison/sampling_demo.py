import ollama

prompt = "Write one sentence about the ocean."

temperatures = [0.1, 0.7, 1.5]

for temp in temperatures:
    print(f"\n--- Temperature: {temp} ---")
    response = ollama.generate(
        model='llama3.2',
        prompt=prompt,
        options={'temperature': temp}
    )
    print(response['response'])