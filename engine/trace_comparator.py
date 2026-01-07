"""
Compare outputs across strategies for the same item.
We compute simple agreement stats on final_answer and correctness.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Any, Dict, List, Tuple

from .trace_parser import extract_json
from .trace_metrics import compute_metrics


def group_by_item(rows: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    groups = defaultdict(list)
    for r in rows:
        groups[str(r.get("item_id"))].append(r)
    return dict(groups)


def compare_item(rows_for_item: List[Dict[str, Any]]) -> Dict[str, Any]:
    answer_key = rows_for_item[0].get("answer_key")
    per_strategy = {}

    for r in rows_for_item:
        parsed = extract_json(r.get("raw_text", ""))
        metrics = compute_metrics(parsed, answer_key)
        per_strategy[r["strategy"]] = {
            "final_answer": metrics.final_answer,
            "is_correct": metrics.is_correct,
            "has_verification": metrics.has_verification,
            "rationale_len": metrics.rationale_len,
            "parse_error": parsed.get("parse_error")
        }

    # Agreement on final answers (stringified)
    answers = [str(v["final_answer"]) for v in per_strategy.values()]
    agreement = len(set(answers)) == 1

    return {
        "item_id": rows_for_item[0].get("item_id"),
        "domain": rows_for_item[0].get("domain"),
        "answer_key": answer_key,
        "agreement_on_final_answer": agreement,
        "per_strategy": per_strategy
    }


def compare_all(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    groups = group_by_item(rows)
    return [compare_item(v) for v in groups.values()]
