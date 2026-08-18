# NFL ML Platform

Production-style Fantasy NFL analytics, machine learning, and AI reporting platform.

## Project Goal

Build a real, incrementally developed platform for a 12-team Sleeper fantasy league that can:

- ingest current and historical league data;
- analyse weekly performance and luck;
- model power rankings and playoff probabilities;
- generate personalised weekly reports;
- eventually support ML predictions, MLOps, cloud deployment, and AI-generated narratives.

## Initial Product

The first MVP is a trustworthy weekly league report that can be shared with league members after each fantasy week.

The platform is initially designed around the Tyneside Superb Owl league, while keeping the architecture flexible enough to support other Sleeper leagues later.

## Current Architecture

```text
Sleeper API
    ↓
Python ingestion client
    ↓
Validated domain data
    ↓
Analytics / simulation
    ↓
Weekly report
```

The project currently uses a modular monolith architecture rather than microservices.

## Current Status

Implemented:

- Python project and package structure
- isolated virtual environment
- dependency management with `pyproject.toml`
- Sleeper API client
- league, user, and matchup retrieval
- unit tests with pytest
- Git/GitHub workflow

Next:

- roster ingestion
- historical season traversal
- domain modelling and validation
- league history representation
- initial analytics

## Engineering Principles

- introduce technology only when it solves a real problem;
- keep important decisions documented;
- favour testable, modular code;
- preserve historical data accurately;
- separate raw API data from internal domain models;
- avoid premature distributed-system complexity.

## Development

```bash
python -m venv .venv
python -m pip install -e ".[dev]"
python -m pytest
```

## Roadmap

Later phases are expected to introduce:

- analytical reporting
- playoff simulation
- machine learning
- MLflow
- orchestration
- Docker
- CI/CD
- Azure
- observability
- LLM-based report generation