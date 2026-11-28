"""Local causal-LM supervised fine-tuning. Requires a local base checkpoint and JSONL text data."""
import os
from pathlib import Path
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments, DataCollatorForLanguageModeling

BASE_MODEL = os.environ.get("AEGIS_BASE_MODEL")
TRAIN_FILE = os.environ.get("AEGIS_TRAIN_FILE")
OUTPUT_DIR = os.environ.get("AEGIS_OUTPUT_DIR", "checkpoints/aegis-sft")
MAX_LENGTH = int(os.environ.get("AEGIS_MAX_LENGTH", "512"))

if not BASE_MODEL or not Path(BASE_MODEL).exists():
    raise SystemExit("Set AEGIS_BASE_MODEL to an existing local causal-LM checkpoint directory.")
if not TRAIN_FILE or not Path(TRAIN_FILE).is_file():
    raise SystemExit("Set AEGIS_TRAIN_FILE to a JSONL file containing a non-empty 'text' field per line.")

# Local files only: no remote model download is requested.
tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL, local_files_only=True, trust_remote_code=True)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL, local_files_only=True, trust_remote_code=True,
    torch_dtype="auto",
)
dataset = load_dataset("json", data_files={"train": TRAIN_FILE}, split="train")
if "text" not in dataset.column_names or len(dataset) == 0:
    raise SystemExit("Training JSONL must contain at least one row with a 'text' field.")
dataset = dataset.filter(lambda row: isinstance(row["text"], str) and bool(row["text"].strip()))
if len(dataset) == 0:
    raise SystemExit("No non-empty training examples were found.")

def tokenize(batch):
    return tokenizer(batch["text"], truncation=True, max_length=MAX_LENGTH)

tokenized = dataset.map(tokenize, batched=True, remove_columns=dataset.column_names)
args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    num_train_epochs=float(os.environ.get("AEGIS_EPOCHS", "1")),
    per_device_train_batch_size=int(os.environ.get("AEGIS_BATCH_SIZE", "1")),
    gradient_accumulation_steps=int(os.environ.get("AEGIS_GRAD_ACCUM", "8")),
    learning_rate=float(os.environ.get("AEGIS_LEARNING_RATE", "2e-5")),
    logging_steps=10, save_steps=200, save_total_limit=2,
    gradient_checkpointing=True, report_to="none",
    fp16=os.environ.get("AEGIS_FP16", "0") == "1",
)
trainer = Trainer(
    model=model, args=args, train_dataset=tokenized,
    data_collator=DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False),
)
trainer.train()
trainer.save_model(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)
print(f"Saved Aegis fine-tuned checkpoint to {OUTPUT_DIR}")
