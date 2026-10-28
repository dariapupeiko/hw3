import csv
from pathlib import Path

input_path = Path("data/raw/dataset.csv")
output_path = Path("data/prepared/dataset.csv")

output_path.parent.mkdir(parents=True, exist_ok=True)

with input_path.open("r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    rows = [
        {"x": float(row["x"]), "y": float(row["y"])}
        for row in reader
    ]

with output_path.open("w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["x", "y"])
    writer.writeheader()
    writer.writerows(rows)

print(f"Prepared {len(rows)} rows: {output_path}")
