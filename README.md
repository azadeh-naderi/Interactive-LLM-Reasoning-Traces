# Interactive LLM Reasoning Traces

This repository provides a research-oriented framework for generating, parsing, and comparing
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

This repository is designed for **analysis and experimentation**, not leaderboard benchmarking.

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

