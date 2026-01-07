"""
Generate structured reasoning outputs under multiple prompting strategies.

Design goals:
- Reproducibility (fixed config, deterministic-ish settings)
- Structured outputs (JSON)
- Model-agnostic logging
"""

from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass, asdict
from typing import Dict, Any, List, Optional

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@dataclass
class GenerationConfig:
    model: str = "gpt-4o-mini"
    temperature: float = 0.2
    max_tokens: int = 700


def generate_one(
    prompt: str,
    strategy_name: str,
    system_prompt: str,
    config: GenerationConfig
) -> Dict[str, Any]:
    resp = client.chat.completions.create(
        model=config.model,
        temperature=config.temperature,
        max_tokens=config.max_tokens,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )

    text = resp.choices[0].message.content or ""

    return {
        "ts": int(time.time()),
        "strategy": strategy_name,
        "model": config.model,
        "prompt": prompt,
        "raw_text": text,
        "config": asdict(config)
    }


def generate_batch(
    prompts: List[Dict[str, Any]],
    strategies: Dict[str, str],
    config: Optional[GenerationConfig] = None
) -> List[Dict[str, Any]]:
    config = config or GenerationConfig()
    outputs = []

    for item in prompts:
        for strat_name, sys_prompt in strategies.items():
            out = generate_one(
                prompt=item["prompt"],
                strategy_name=strat_name,
                system_prompt=sys_prompt,
                config=config
            )
            out["item_id"] = item.get("id")
            out["domain"] = item.get("domain")
            out["answer_key"] = item.get("answer_key")
            outputs.append(out)

    return outputs


def save_jsonl(rows: List[Dict[str, Any]], path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
