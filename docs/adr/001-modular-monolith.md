# ADR-001: Use a modular monolith

## Status

Accepted

## Context

I am developing an early-stage fantasy NFL platform for a small initial user base of 12 league members. I want to combine ingestion, analytics, ML and reporting functionality into one platform but have clear separation between each of those modules.

## Decision

Keep everything in one Python application/repository but organise functionality into separate modules with clear responsibilities.

## Alternatives Considered

- **Scripts:** simple initially but would make it harder to reuse and separate functionality as the platform grows.
- **Unstructured monolith:** keeps deployment simple but risks tightly coupling ingestion, analytics, ML and reporting code.
- **Microservices:** provides independent deployment and scaling but introduces unnecessary infrastructure and operational complexity for the current scale.

## Consequences

Simpler development/deployment and less infrastructure overhead than microservices, which would be overkill for the current use. The downside is that components aren't independently deployable/scalable, and we'll need discipline to maintain module boundaries.