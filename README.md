<p align="center">
  <img src="assets/aegis-logo.webp" width="220" alt="Mr Aegis logo">
</p>

<h1 align="center">MR AEGIS</h1>
<p align="center"><strong>An open-source AI research, language-model development, and training project.</strong></p>

# Mr Aegis

Mr Aegis is an AI project focused on building and improving a capable language assistant for conversation, coding, problem-solving, reasoning, and tool-assisted tasks.

The repository provides a development foundation for working with language models: model inference, fine-tuning, dataset preparation, evaluation, tokenizer utilities, and API-compatible interfaces. The goal is to develop Mr Aegis into a reliable assistant that can understand instructions, explain ideas clearly, help write and debug code, and use tools when appropriate.

## What Mr Aegis is designed to do

- **Conversation and instruction following** — understand questions and respond with useful, structured answers.
- **Coding assistance** — explain programming concepts, generate code, and help debug errors.
- **Reasoning and problem solving** — work through multi-step tasks and explain conclusions.
- **Model training and fine-tuning** — support experiments using curated datasets and compatible model checkpoints.
- **Evaluation** — measure model behavior and track improvements with repeatable tests.
- **Tool and API integration** — provide interfaces that applications can use to communicate with the model.

## Development

Mr Aegis is under active development. Its capabilities depend on the model checkpoint, training data, runtime configuration, and evaluation results used in a given build. A training script or dataset alone does not mean that a model has already completed training.

### Prepare training data

The seed instruction dataset is located at [training/aegis_seed.jsonl](training/aegis_seed.jsonl). It is a small starter dataset for pipeline checks and early experiments, not a complete pretraining corpus.

Validate the dataset:

```bash
python training/validate_dataset.py training/aegis_seed.jsonl
```

### Fine-tune a local model checkpoint

Install the training dependencies:

```bash
pip install -r training/requirements.txt
```

Set the paths to a compatible local causal-language-model checkpoint and the training dataset, then run the training script.

Linux/macOS:

```bash
export AEGIS_BASE_MODEL=/path/to/local/model
export AEGIS_TRAIN_FILE=training/aegis_seed.jsonl
python training/train.py
```

Windows PowerShell:

```powershell
$env:AEGIS_BASE_MODEL="D:\models\base-model"
$env:AEGIS_TRAIN_FILE="training/aegis_seed.jsonl"
python training/train.py
```

The training workflow requires a compatible local checkpoint and suitable compute resources. Training quality depends on the size, quality, diversity, and licensing of the data, as well as the model and hardware configuration. Review dataset sources and permissions before use.

## Project principles

- Build useful capabilities through measurable development and evaluation.
- Be transparent about what has and has not been trained or tested.
- Use properly licensed datasets and respect third-party notices.
- Keep model behavior reliable, understandable, and safe.
- Improve the project incrementally without claiming unsupported capabilities.

## License

Original Mr Aegis contributions are covered by the Apache License 2.0 notice in [LICENSE.AEGIS](LICENSE.AEGIS). This repository also contains third-party components; their applicable copyright, attribution, and license terms remain in force. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
