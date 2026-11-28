"""Basic JSONL validation; this checks format, not factual quality or licensing."""
import json, sys
from pathlib import Path
if len(sys.argv) != 2:
    raise SystemExit("Usage: python training/validate_dataset.py data/train.jsonl")
p = Path(sys.argv[1])
if not p.is_file():
    raise SystemExit(f"File not found: {p}")
count = 0
empty = 0
with p.open(encoding="utf-8") as f:
    for line_no, line in enumerate(f, 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as e:
            raise SystemExit(f"Invalid JSON on line {line_no}: {e}")
        if not isinstance(row, dict) or not isinstance(row.get("text"), str):
            raise SystemExit(f"Line {line_no} must be an object with a string 'text' field.")
        count += 1
        empty += not bool(row["text"].strip())
if not count or count == empty:
    raise SystemExit("Dataset has no non-empty text examples.")
print(f"Valid JSONL: {count} rows, {empty} empty rows. Review licensing and data quality separately.")
