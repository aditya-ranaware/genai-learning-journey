# Embeddings Similarity Demo — Proving "King - Man + Woman ≈ Queen"

Part of my Gen AI learning journey — Phase 1: Foundations.

## What this does
Uses a free, local embedding model (`sentence-transformers`) to prove that AI embeddings capture real word *relationships*, not just individual word meanings — using the famous "king - man + woman = queen" example.

## The experiment
Generated embeddings (numeric vectors) for 5 words: king, queen, man, woman, car.
Then measured similarity between pairs using cosine similarity (1.0 = identical meaning, ~0.3 = unrelated).

## Results
| Pair | Similarity |
|------|-----------|
| king ↔ queen | 0.68 |
| king ↔ car | 0.29 |
| man ↔ woman | 0.33 |
| queen ↔ car | 0.30 |
| **(king - man + woman) ↔ queen** | **0.58** |

## Key learning
Took "king," removed the "man" direction, added the "woman" direction — and the resulting vector landed significantly closer to "queen" (0.58) than any unrelated pair (~0.29-0.30). This proves embeddings don't just store word meaning individually — they capture *relationships* between concepts, enabling vector arithmetic that mirrors real-world analogies.

**No paid API needed** — this ran entirely free and offline using a local open-source model (`all-MiniLM-L6-v2`), proving this core AI concept without any API cost.

## How to run
```bash
pip install sentence-transformers numpy
python embeddings_demo.py
```

## What's next
Next up: Text Generation/Sampling — testing how `temperature` changes AI output from robotic/predictable to creative/random, using the same prompt.