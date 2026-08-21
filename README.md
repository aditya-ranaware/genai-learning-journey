# Gen AI Learning Journey

Learning Generative AI topic-by-topic, building a small project after every topic instead of just reading/watching. This repo tracks that journey — code, notes, and progress, all in one place.

**Approach:** Learn a concept → build something small to prove I understand it → post about it → move to the next concept.

Follow the journey on LinkedIn: [add your LinkedIn profile link here]

---

## Progress

| Phase | Status | Topics | Project(s) |
|---|---|---|---|
| **Phase 1: LLM Foundations** | Tokenization, Embeddings, Attention, Transformer Architecture, Text Generation/Sampling | Tokenization Demo, Embeddings Similarity Demo, Temperature/Sampling Demo |
| **Phase 2: Prompt Engineering** | Zero-shot vs Few-shot, System vs User Prompts, Structured Output, Failure Modes (Hallucination) | Study Notes Summarizer |
| **Phase 3: RAG** | Vector Databases, Chunking, Semantic Search, Retrieval + Generation Pipeline | Chat with PDF |
| **Phase 4: Agents** | Tool use, planning, multi-step reasoning, agent memory | Research Agent |
| **Phase 5: Fine-tuning & Open-Source Models** | Fine-tuning vs prompting, LoRA/QLoRA, local open models | Fine-tune a small model |
| **Phase 6: Image/Multimodal Gen AI** | Diffusion models, Stable Diffusion basics | Image generation app |
| **Phase 7: Capstone** | Combining everything | Personal AI assistant |

---

## Repo Structure

```
genai-learning-journey/
├── phase1-foundations/
│   ├── 01-tokenization-demo/
│   ├── 02-embeddings-similarity/
│   └── 03-sampling-comparison/
├── phase2-prompt-engineering/
│   └── 01-study-notes-summarizer/
├── phase3-rag/
│   └── 01-chat-with-pdf/
└── ...(more phases as I progress)
```

Each project folder has its own README explaining what it does, what I learned, and how to run it.

---

## Tools & Stack Used So Far

- **Python** — main language throughout
- **Ollama + Llama 3.2** — free, local LLM (no API cost)
- **sentence-transformers** — free local embeddings
- **ChromaDB** — free local vector database
- **tiktoken** — OpenAI's tokenizer, used to study tokenization
- **pypdf** — PDF text extraction

Everything so far has been built using **free, local, open-source tools** — no paid API required to learn or build any of these projects.

---

## Why I'm Doing This

Learning Gen AI properly means understanding what's actually happening under the hood — not just calling an API and hoping for the best. Building small, real projects after every concept forces genuine understanding, and posting publicly keeps me consistent and accountable.

---

*Notes on each phase (interview-ready, simple language) are available as PDFs within this repo / linked in my posts.*
