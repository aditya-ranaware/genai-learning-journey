# Personal AI Assistant — Capstone Project

The final project of my Gen AI learning journey — Phase 7: Capstone.

## What this does
A single AI assistant that automatically decides how to answer your question:
- If it's about company policies → answers from a document using **RAG**
- If it needs current/real-time information → searches the web using an **Agent**

Unlike earlier phase projects (which each did ONE thing), this combines multiple capabilities into one system, with the AI itself deciding which capability fits each question — no manual switching required.

## How it works — The Router
A small, separate LLM call reads the question and outputs a single word: `DOCUMENT` or `WEB`. Based on that decision, the assistant follows one of two paths:

```
User question
      ↓
Router (LLM call, constrained to one-word output)
      ↓
   ┌──────────────┴──────────────┐
DOCUMENT path                  WEB path
(RAG - Phase 3)              (Agent - Phase 4)
   ↓                              ↓
        Final answer to user
```

## Concepts combined from the whole journey
- **Phase 1 (Embeddings)** — powers the semantic search inside RAG
- **Phase 2 (Prompt Engineering)** — the router uses constrained-output prompting; both answer paths use hallucination guardrails
- **Phase 3 (RAG)** — chunking, vector database, semantic search for document questions
- **Phase 4 (Agents)** — web search tool for real-time questions

## Example run
| Question | Router Decision | Result |
|---|---|---|
| "What are the standard work hours?" | DOCUMENT | Correctly answered from the handbook |
| "What's the latest news in AI?" | WEB | Searched the web, summarized results |
| "How many leave days do I get?" | DOCUMENT | Correctly answered from the handbook |
| "What's the weather like today?" | WEB | Searched the web, honestly noted it couldn't get real-time data instead of guessing |

## Key learning
The most valuable part of this project wasn't RAG or Agents individually (already built those) — it was the **routing logic**: using the LLM itself to decide which capability a question needs, rather than hardcoding rules. This is closer to how real production AI assistants are architected — one interface, multiple capabilities, automatic decision-making.

Also notable: when the web search didn't have enough info for an accurate weather answer, the assistant was honest about its limitation instead of making something up — proof that the hallucination guardrails from Phase 2 carried through into this combined system.

## Tools used
- Ollama + Llama 3.2 (free, local) — for routing decisions and generation
- ChromaDB + sentence-transformers — for RAG
- DuckDuckGo Search (`ddgs`) — for web search
- pypdf — for document processing

## How to run
```bash
pip install chromadb pypdf sentence-transformers ollama ddgs
ollama pull llama3.2
python assistant.py
```
Place a PDF as `document.pdf` in the same folder before running.

## Journey summary
This project marks the completion of a 7-phase Gen AI learning journey — from tokenization and embeddings, through prompt engineering, RAG, agents, fine-tuning, and image generation — culminating in this capstone that combines multiple capabilities into one working assistant.