import json
from pathlib import Path

from engine.trace_comparator import compare_all


def load_jsonl(path: Path):
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            rows.append(json.loads(line))
    return rows


def main():
    repo = Path(__file__).resolve().parents[1]
    raw_path = repo / "results" / "raw_generations.jsonl"

    rows = load_jsonl(raw_path)
    comparisons = compare_all(rows)

    out_path = repo / "results" / "comparisons.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(comparisons, f, indent=2, ensure_ascii=False)

    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
