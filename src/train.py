import csv
import json
from pathlib import Path

data_path = Path("data/prepared/dataset.csv")
model_path = Path("model.json")

with data_path.open("r", encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))

x_values = [float(row["x"]) for row in rows]
y_values = [float(row["y"]) for row in rows]

if len(x_values) < 2:
    raise ValueError("At least two rows are required")

x_mean = sum(x_values) / len(x_values)
y_mean = sum(y_values) / len(y_values)

denominator = sum((x - x_mean) ** 2 for x in x_values)
if denominator == 0:
    raise ValueError("All x values are identical")

a = sum(
    (x - x_mean) * (y - y_mean)
    for x, y in zip(x_values, y_values)
) / denominator

b = y_mean - a * x_mean

with model_path.open("w", encoding="utf-8") as f:
    json.dump({"a": a, "b": b}, f, indent=2)

print(f"Model trained: y = {a:.4f} * x + {b:.4f}")
print(f"Saved model to {model_path}")
