# Study Notes Summarizer

Part of my Gen AI learning journey — Phase 2: Prompt Engineering.

## What this does
Takes messy, unstructured notes and turns them into a clean, structured summary (title + key points + a quiz question) using a local LLM — applying everything learned in Phase 2: system prompts, structured output, and hallucination guardrails.

## The prompt engineering techniques used
1. **System prompt** — defines the AI's role ("study assistant") and strict rules upfront, kept separate from the actual content
2. **Structured output (JSON)** — forces the model to always respond in the same predictable format, so the output can be directly used by an app (no messy text parsing)
3. **Hallucination guardrail** — explicit instruction: "only use information present in the notes, do not add outside facts"
4. **Practical bonus** — generates a quiz question, turning passive notes into an active recall tool

## Example run
**Input (messy notes):**
```
tokens r pieces of text llm split it. bpe used. embeddings = numbers 
representing meaning. king-man+woman=queen example. attention lets model
look at all words. QKV = query key value. transformer = attention + feedforward
stacked many times. temperature controls randomness low=safe high=creative
```

**Output (clean, structured):**
```json
{
  "title": "Language Model Basics",
  "key_points": [
    "Tokens are split pieces of text, and language models use BPE (subword) to split them",
    "Embeddings represent meaning as numerical values",
    "Attention mechanism allows model to look at all words",
    "Transformer architecture combines attention and feedforward networks, stacked multiple times",
    "Temperature controls randomness, with low values making it safer and high values more creative"
  ],
  "quiz_question": "What is the primary goal of the attention mechanism in a transformer model?"
}
```

## Key learning
A well-structured prompt (system role + explicit rules + JSON format request) reliably produced clean, parseable output on a small, free, local model — no hallucinated facts, and the JSON parsed successfully on the first try. This proves that good prompting matters more than model size for getting consistent, usable output.

## Tools used
- Ollama (free, local) + Llama 3.2 (open-source model)
- Python `ollama` library + `json` for parsing/validation

## How to run
```bash
ollama pull llama3.2
pip install ollama
python summarizer.py
```

## What's next
Phase 2 complete — moving to Phase 3: RAG (Retrieval Augmented Generation), building a "chat with your notes/PDF" tool.