# Interactive LLM Reasoning Traces

This repository provides a framework for generating, parsing, and comparing
**reasoning outputs from large language models (LLMs)** under multiple prompting strategies.

Rather than focusing on raw accuracy alone, this project analyzes **reasoning consistency,
verification behavior, and robustness across strategies**, using a structured output schema
and lightweight evaluation metrics.

---

## Motivation

Modern LLMs often produce correct answers with inconsistent or fragile reasoning.
Understanding how different prompting strategies influence reasoning behavior is critical for:

- evaluating model reliability
- diagnosing brittle or unstable reasoning
- improving reasoning robustness without retraining

---

## Key Features

- Multiple reasoning strategies evaluated on the same task set
- Structured JSON output schema for reliable parsing
- Strategy-level comparison of:
  - final answer agreement
  - correctness vs. answer keys
  - verification behavior
  - reasoning length proxies
- Model-agnostic design (API-based or local models)

---

## Reasoning Strategies

The following prompting strategies are included:

- **direct** – concise reasoning with a brief verification step  
- **decomposition** – high-level problem breakdown before answering  
- **counterexample_check** – attempts to falsify the initial answer  
- **reflect_and_verify** – independent verification using an alternative check  

All strategies are required to return responses in a standardized JSON format.

---

## Repository Structure
interactive-llm-reasoning-traces/
├── prompts/ # Prompt templates and task sets
├── engine/ # Generation, parsing, and metric computation
├── scripts/ # End-to-end experiment runners
├── notebooks/ # Analysis and visualization notebooks
├── results/ # Generated outputs and comparisons
├── requirements.txt
└── README.md


---

## Output Schema

Each model response is requested in the following JSON format:

```json
{
  "final_answer": "...",
  "rationale": "brief explanation (no private chain-of-thought)",
  "verification": "short self-check or validation"
}


This design supports safe, consistent parsing while avoiding exposure of private reasoning traces.

Quick Start
1. Install dependencies
pip install -r requirements.txt

2. Set API key
export OPENAI_API_KEY="YOUR_API_KEY"

3. Generate reasoning outputs
python scripts/run_generate.py

4. Compare strategies
python scripts/run_compare.py


Results will be saved to the results/ directory.

Analysis

The provided notebook (notebooks/trace_analysis.ipynb) supports:

strategy-wise correctness comparison

agreement analysis across strategies

inspection of parsing failures

basic robustness diagnostics

These analyses are intended to be extended with additional metrics or task domains.

Design Philosophy

Emphasis on reasoning behavior, not prompt tricks

Reproducible, structured experiments

Minimal assumptions about model internals

Compatible with future extensions (e.g., robustness tests, perturbations)

Disclaimer

This is an original, research-focused project intended for exploration and analysis.
It is not a benchmark, leaderboard, or production system.


---

### ✅ Why this README works for your profile

This README signals that you:
- understand **LLM reasoning beyond prompting**
- care about **evaluation and robustness**
- design **research-quality experiments**
- think in terms of **generalizable frameworks**

If you want, next I can:
- tailor a **short GitHub repo description**
- help you decide **which repos to pin**
- write a **GitHub profile summary** that matches these projects perfectly
