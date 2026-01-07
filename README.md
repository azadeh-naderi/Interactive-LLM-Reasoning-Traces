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


## Quick Start
  1. Install dependencies
  pip install -r requirements.txt
  
  2. Set API key
  export OPENAI_API_KEY="YOUR_API_KEY"
  
  3. Generate reasoning outputs
  python scripts/run_generate.py
  
  4. Compare strategies
  python scripts/run_compare.py

## Output Schema

  Each model response is requested in the following JSON format:
  
  ```json
  {
    "final_answer": "...",
    "rationale": "brief explanation (no private chain-of-thought)",
    "verification": "short self-check or validation"
  }


This design supports safe, consistent parsing while avoiding exposure of private reasoning traces.



Results will be saved to the results/ directory.


