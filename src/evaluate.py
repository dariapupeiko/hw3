import csv
import json
from pathlib import Path

data_path = Path("data/prepared/dataset.csv")
model_path = Path("model.json")
metrics_path = Path("metrics.json")

with data_path.open("r", encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))

with model_path.open("r", encoding="utf-8") as f:
    model = json.load(f)

a = model["a"]
b = model["b"]

errors = [
    abs(float(row["y"]) - (a * float(row["x"]) + b))
    for row in rows
]

mae = sum(errors) / len(errors)
metrics = {"mae": mae}

with metrics_path.open("w", encoding="utf-8") as f:
    json.dump(metrics, f, indent=2)

print(f"MAE: {mae:.4f}")
print(f"Saved metrics to {metrics_path}")
