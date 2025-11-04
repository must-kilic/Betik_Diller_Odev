import csv
import json
from pathlib import Path
from dekorator import timer, required_column

@timer
@required_column({"name", "age", "city"})
def read_csv(path):
    with Path(path).open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

@timer
def write_json(path, obj):
    with Path(path).open("w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)

@timer
def write_text(path, text):
    Path(path).write_text(text, encoding="utf-8")
