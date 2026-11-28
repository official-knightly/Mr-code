# Aegis seed instruction dataset

- Dataset name/version: Aegis Seed Instructions v1.0
- Source/origin: Original examples authored for this repository; no external dataset copied.
- Collection date: 2026-11-28
- License: Apache License 2.0 for these original examples.
- Languages: English
- Approximate number of examples: 22 short instruction-response examples.
- Format: JSON Lines; each line contains one `text` field, compatible with `training/train.py`.
- Filtering and deduplication: Hand-authored, reviewed for basic formatting, and kept short. This is a small seed set, not a broad or comprehensive corpus.
- Personal/sensitive data review: No intentionally included personal or sensitive information.
- Known limitations and biases: Small English-only dataset; limited topic coverage; examples are not a substitute for large-scale, carefully curated pretraining or instruction-tuning data. Quality and model behavior must be evaluated independently.
- Intended training use: Smoke tests and initial supervised fine-tuning experiments only.
- Maintainer: Aegis contributors

## Use

Validate it with:

```bash
python training/validate_dataset.py training/aegis_seed.jsonl
```

Then set `AEGIS_TRAIN_FILE=training/aegis_seed.jsonl` when running the existing training script. The script still requires a compatible local base-model checkpoint in `AEGIS_BASE_MODEL`. Adding this file does not itself run training or produce trained weights.
