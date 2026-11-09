# DYSTOPIC 2067 — AI-Assisted Python Engineering Showcase

> **Independent reference implementation.** This repository demonstrates engineering concepts used in a larger privately developed narrative production platform. It does **not** contain or reproduce the production engine, prompts, world canon, API credentials, datasets, or customer data.

## What this demonstrates

- **Modular orchestration:** Director → Writer → Judge → validated commit
- **Dependency inversion:** a `Writer` protocol allows deterministic offline execution or a separately implemented LLM adapter
- **Continuity validation:** an explicit set of verified facts; conflicting assertions are rejected
- **Thread lifecycle:** active, dormant, resolved; resolution requires linked evidence
- **Persistence:** accepted scenes are written to JSON using atomic file replacement
- **Testing:** built-in `unittest`, including rejection paths and state integrity

## Run locally

Requires Python 3.10+; no packages, accounts, or API keys required.

```bash
python demo.py
python -m unittest discover -s tests -v
```

Expected demo output:

```text
Scene 1: ACCEPTED
Scene 2: ACCEPTED
Scene 3: REJECTED — required continuity fact missing, unverified fact asserted
Persisted scenes: 2
```

## Architecture

```text
Director ── ScenePlan ──> Writer (protocol)
                              │
                          SceneDraft
                              │
                       Judge + known facts
                              │
                     accepted? ── no ──> reject without state mutation
                         │ yes
                         v
                 Thread evidence + JSON store
```

## Suggested live interview exercise

Implement a new review rule or add a lifecycle transition test with an AI coding assistant. Explain the proposed change, inspect its side effects, run regression tests, and commit the smallest verified change.

## Engineering scope and limitations

This is intentionally **not** a production-ready LLM story generator. The offline writer is deterministic; the Judge checks declared facts rather than performing semantic natural-language verification. The JSON store is suitable for a local demo, not concurrent multi-process writes or transactional persistence. There is no automatic repair, authentication, API integration, or production recovery subsystem in this example.

## Intellectual property

Copyright (c) 2026 Dystenia. All rights reserved. No license to reuse, redistribute, or commercially exploit the source is granted by default. Public visibility is not an open-source license. Contact the repository owner to discuss permission or confidential technical review.
