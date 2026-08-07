# Tokenization Demo — English vs Hindi vs Marathi

Part of my Gen AI learning journey — Phase 1: Foundations.

## What this does
Uses OpenAI's `tiktoken` library (the same tokenizer GPT-4/GPT-4o use) to show how the same sentence gets split into tokens differently across languages.

## The experiment
Same meaning, 3 languages:
- English: "The weather is really nice today."
- Hindi: "आज मौसम बहुत अच्छा है।"
- Marathi: "आज हवामान खूप छान आहे."

## Results
| Language | Token Count |
|----------|-------------|
| English  | 7 |
| Hindi    | 6 |
| Marathi  | 10 |

## Key learning
Tokenizers aren't language-neutral — they're trained on how much text of each language existed in the training data. Hindi has massive online presence (news, Wikipedia, social media), so common words got single tokens. Marathi has far less representation, so words like "हवामान" (weather) got split into 3 separate pieces instead of staying whole.

**Practical implication:** For the exact same meaning, Marathi cost ~43% more tokens than English — which directly translates to higher API costs and faster context window usage for underrepresented languages.

## How to run
```bash
pip install tiktoken
python tokenizer_demo.py
```

## What's next
Next up: Embeddings Similarity Demo — showing how AI understands word relationships (e.g. "king" is closer to "queen" than to "car").