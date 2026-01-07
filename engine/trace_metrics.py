"""
Metrics for comparing reasoning outputs.
This repo focuses on:
- Answer accuracy vs answer_key
- Consistency across strategies
- Basic structural metrics (length, presence of verification)
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class TraceMetrics:
    is_parsed: bool
    has_verification: bool
    rationale_len: int
    final_answer: Any
    is_correct: Optional[bool]


def _normalize_answer(x: Any) -> Any:
    if isinstance(x, str):
        return x.strip().lower()
    return x


def compute_metrics(parsed: Dict[str, Any], answer_key: Any) -> TraceMetrics:
    parse_error = parsed.get("parse_error")
    is_parsed = parse_error is None

    rationale = parsed.get("rationale") or ""
    verification = parsed.get("verification") or ""
    final_answer = parsed.get("final_answer")

    has_verification = isinstance(verification, str) and len(verification.strip()) > 0
    rationale_len = len(rationale.strip())

    is_correct: Optional[bool] = None
    if answer_key is not None:
        try:
            is_correct = _normalize_answer(final_answer) == _normalize_answer(answer_key)
        except Exception:
            is_correct = None

    return TraceMetrics(
        is_parsed=is_parsed,
        has_verification=has_verification,
        rationale_len=rationale_len,
        final_answer=final_answer,
        is_correct=is_correct
    )
