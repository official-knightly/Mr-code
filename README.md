<p align="center"><img src="assets/aegis-logo.svg" width="220" alt="Aegis logo"></p>

<h1 align="center">AEGIS</h1>
<p align="center"><strong>An open-source language-model research and training codebase.</strong></p>

Aegis is being developed as an independent AI project. This repository currently contains the imported Qwen research/codebase, rebranded where appropriate, plus an Aegis-owned training workflow. The upstream implementation and its license/notice files are retained; see [LICENSE](LICENSE) and [NOTICE](NOTICE).

## Current status

- [x] Imported all 144 tracked source files from the upstream Qwen repository snapshot.
- [x] Added the Aegis logo and this project README.
- [x] Added a local-data supervised fine-tuning pipeline.
- [ ] Verify every renamed identifier and run the full test suite.
- [ ] Prepare and validate a properly licensed training dataset.
- [ ] Train, evaluate, and publish Aegis model checkpoints.

**Important:** copying code does not copy pretrained model weights or train a model. No model is claimed to have been trained by this repository yet. Training requires a compatible base-model checkpoint, a real dataset, and sufficient GPU memory/compute.

## Training (local, no hosted AI API)

The training pipeline uses Hugging Face Transformers, Datasets, and PyTorch locally. It does not call Ollama or a paid model API.

1. Create a JSONL dataset where each line contains `{"text":"your training example"}`.
2. Review data quality, remove private/sensitive material, and confirm you have permission to use it.
3. Install dependencies from [training/requirements.txt](training/requirements.txt).
4. Set `AEGIS_BASE_MODEL` to a local compatible causal-language-model checkpoint and `AEGIS_TRAIN_FILE` to your JSONL file.
5. Run `python training/train.py`.

Example (Linux/macOS):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r training/requirements.txt
export AEGIS_BASE_MODEL=/path/to/local/base-model
export AEGIS_TRAIN_FILE=/path/to/train.jsonl
python training/train.py
```

Windows PowerShell:

```powershell
py -m venv .venv
.venv\\Scripts\\Activate.ps1
pip install -r training/requirements.txt
$env:AEGIS_BASE_MODEL="D:\\models\\base-model"
$env:AEGIS_TRAIN_FILE="D:\\data\\train.jsonl"
python training/train.py
```

The default script is a small smoke-test configuration, not a claim of large-scale training. Tune batch size, sequence length, precision, and LoRA settings to match your GPU. Do not expect practical LLM training on an 8 GB RAM laptop.

## Repository structure

- `training/` — local supervised fine-tuning pipeline
- `eval/` — evaluation utilities
- `examples/` — usage and tool-use examples
- `docker/` — container build and demo scripts
- `assets/` — documentation images and Aegis logo

## Dataset format

One JSON object per line:

```json
{"text":"User: Explain gravity simply.\\nAssistant: Gravity is the attraction between objects with mass."}
```

Keep a dataset card recording source, license, language, collection date, filtering, and intended use. Never treat an empty placeholder dataset as training data.

## Attribution

This repository includes upstream code and documentation. Preserve all applicable copyright, attribution, and license notices. Aegis branding does not imply ownership of upstream work or affiliation with the original authors.
