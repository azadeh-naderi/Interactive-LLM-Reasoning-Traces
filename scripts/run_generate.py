import json
import yaml
from pathlib import Path
from engine.reasoning_generator import generate_batch, save_jsonl, GenerationConfig


def main():
    repo = Path(__file__).resolve().parents[1]

    with open(repo / "prompts" / "task_set.json", "r", encoding="utf-8") as f:
        taskset = json.load(f)

    with open(repo / "prompts" / "reasoning_strategies.yaml", "r", encoding="utf-8") as f:
        strategies_yaml = yaml.safe_load(f)

    strategies = {k: v["system_prompt"] for k, v in strategies_yaml["strategies"].items()}
    prompts = taskset["items"]

    config = GenerationConfig(model="gpt-4o-mini", temperature=0.2, max_tokens=700)
    outputs = generate_batch(prompts, strategies, config=config)

    out_path = repo / "results" / "raw_generations.jsonl"
    save_jsonl(outputs, str(out_path))
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
