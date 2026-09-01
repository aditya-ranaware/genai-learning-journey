# Fine-tuning Attempt — "Hype Coach" Style Model

Part of my Gen AI learning journey — Phase 5: Fine-tuning & Open-Source Models.

## What I attempted
Fine-tune TinyLlama (1.1B parameters) using QLoRA to always respond in an enthusiastic, motivational "hype coach" tone — regardless of the question asked.

## What worked
- Set up Google Colab with a free T4 GPU
- Installed and configured the full QLoRA fine-tuning stack (`transformers`, `peft`, `trl`, `bitsandbytes`)
- Successfully applied LoRA — trained only **0.1% of the model's parameters** (1.1 million out of 1.1 billion), proving how efficient LoRA is compared to full fine-tuning
- Training ran successfully multiple times, with loss decreasing consistently across steps (from ~3.4 down to ~2.6-2.9 depending on the run)
- Verified the base (untouched) model generated coherent output on its own — confirming the environment and model loading were correct

## What didn't work
After training, the fine-tuned model's generated text was **incoherent** (mixed languages, broken words) instead of the enthusiastic style I was aiming for — even after multiple attempts adjusting:
- Learning rate (tried 2e-4, 5e-5, 1e-4)
- Number of epochs (tried 10, 3, 5)
- Data formatting (switched from manual formatting to the tokenizer's official `apply_chat_template()`)
- A full clean runtime restart to rule out notebook state issues

## What I learned from debugging
- Loss decreasing does **not** guarantee good generation quality — I verified this directly by testing generation output, not just trusting the training metrics
- Isolating variables one at a time (data format, then learning rate, then a clean restart) is the right way to debug, even when it doesn't fully solve the issue in the time available
- Very small models (1.1B parameters) combined with very few training examples (only 8) and 4-bit quantization together may be more fragile to fine-tune than larger models — likely contributed to instability
- Real fine-tuning work often involves this kind of iterative debugging — it's not always a smooth first-try success, even for a small demo

## Tools used
- Google Colab (free T4 GPU)
- Hugging Face `transformers`, `peft`, `trl`, `bitsandbytes`
- TinyLlama-1.1B-Chat-v1.0 (open-source base model)

## Files in this folder
- `hype_coach_finetuning.ipynb` — the full notebook with all attempts and debugging steps
- `hype_coach_finetuning.pdf` — readable version of the notebook

## What's next
Documenting this honestly rather than hiding the incomplete result — real learning includes attempts that don't fully succeed. Revisiting this with a larger base model or more training examples is a good future improvement.