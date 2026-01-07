"""
Parse model outputs into a standard schema.
We ask the model to return JSON; this parser safely extracts it.
"""

from __future__ import annotations

import json
import re
from typing import Any, Dict


_JSON_BLOCK_RE = re.compile(r"\{.*\}", re.DOTALL)


def extract_json(raw_text: str) -> Dict[str, Any]:
    """
    Best-effort JSON extraction from a text response.
    """
    raw_text = raw_text.strip()

    # If it's already JSON
    try:
        return json.loads(raw_text)
    except Exception:
        pass

    # Try to find a JSON-looking block
    m = _JSON_BLOCK_RE.search(raw_text)
    if not m:
        return {"final_answer": None, "rationale": None, "verification": None, "parse_error": "no_json_found"}

    candidate = m.group(0)
    try:
        return json.loads(candidate)
    except Exception as e:
        return {"final_answer": None, "rationale": None, "verification": None, "parse_error": f"json_decode_error: {e}"}
