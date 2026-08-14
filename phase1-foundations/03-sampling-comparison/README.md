# Temperature/Sampling Comparison — How AI's "Creativity Dial" Works

Part of my Gen AI learning journey — Phase 1: Foundations.

## What this does
Runs the same prompt through a local LLM (Llama 3.2, via Ollama) at 3 different temperature settings, to see how temperature affects output.

## The experiment
Prompt: "Write one sentence about the ocean."
Temperatures tested: 0.1 (safe), 0.7 (moderate), 1.5 (creative)

## Results
All 3 outputs came out fairly similar in wording and structure, with only minor variation in phrasing.

## Key learning
Temperature controls how willing the model is to pick lower-probability words instead of always choosing the "safest" highest-probability word. Low temperature = predictable, high temperature = more willing to explore riskier word choices.

**Interesting finding:** temperature's visible effect depends heavily on the prompt itself. A factual prompt like "describe the ocean" naturally has few valid "creative" alternatives — true facts about the ocean don't vary much regardless of temperature. Temperature differences become much more visible on open-ended, creative prompts (e.g. story writing, brainstorming) where the model has more room to explore different word choices.

**Practical implication:** don't expect temperature to "fix" boring output on factual/constrained tasks — it's most useful for creative or open-ended generation, not for tasks with a narrow set of correct answers.

## Tools used
- Ollama (free, local LLM runner)
- Llama 3.2 (open-source model by Meta, ~2GB)
- Python `ollama` library

## How to run
```bash
ollama pull llama3.2
pip install ollama
python sampling_demo.py
```

## What's next
Wrapping up Phase 1 micro-projects — moving to Phase 2: Prompt Engineering (zero-shot, few-shot, system prompts) with hands-on API work.