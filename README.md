# DYSTOPIC 2067
### AI-Powered Narrative & Multimedia Production Platform

**Python Engineering | Multi-Agent AI Orchestration | Persistent State Management | Automated Multimedia Production**

DYSTOPIC 2067 is an independently developed, modular AI-powered platform designed to orchestrate complex narrative generation and multimedia production workflows.

The platform combines multiple AI-driven components with deterministic software engineering principles to coordinate story planning, narrative generation, continuity validation, persistent world states, image generation, and audiobook production.

Its architecture is designed for extensibility, maintainability, and reuse across different fictional worlds and narrative genres.

## Core Architecture

The production platform integrates several interconnected systems:

| Component | Responsibility |
|---|---|
| Narrative Director | Story planning, scene objectives, narrative progression, and pacing |
| Narrative Writer | AI-assisted scene and dialogue generation |
| Narrative Judge | Continuity validation, consistency checks, and quality control |
| Micro Repair Pipeline | Targeted identification and correction of narrative inconsistencies |
| Character & World State | Persistent character attributes, relationships, events, and environmental conditions |
| Thread Management | Narrative thread tracking, lifecycle management, and resolution |
| Persistence Layer | Structured storage, state recovery, and story continuity |
| Image Generation | Integration of local and API-based image generation workflows |
| Editorial Processing | AI-assisted text review and preparation |
| Audio Production | Text segmentation, voice synthesis, character voice profiles, and sound-effect preparation |

The narrative engine follows a world-agnostic design, separating reusable core functionality from individual fictional settings.

## AI-Assisted Software Engineering

Development combines AI-assisted programming with human-directed software architecture, debugging, integration, testing, and quality assurance.

Key engineering practices include:

- Modular Python application design
- Multi-model AI orchestration
- Structured data validation
- State and lifecycle management
- Persistent data handling
- Dependency abstraction
- Automated regression testing
- Error analysis and recovery strategies
- Git-based version control
- Iterative development and code review

## Executable Python Implementation

This repository includes an independent, executable Python reference implementation demonstrating selected architectural concepts used throughout the larger platform.

The implementation contains:

- `engine.py` — Narrative orchestration, validation, thread management, and persistence
- `demo.py` — Executable demonstration of accepted and rejected scenes
- `tests/test_engine.py` — Automated unit tests for validation, lifecycle behavior, and state integrity

### Requirements

Python 3.10 or newer. No external packages or API credentials are required.

### Run the demonstration

```bash
python demo.py
```

### Run automated tests

```bash
python -m unittest discover -s tests -v
```

### Expected demonstration output

```text
Scene 1: ACCEPTED
Scene 2: ACCEPTED
Scene 3: REJECTED — required continuity fact missing, unverified fact asserted
Persisted scenes: 2
```

The example demonstrates controlled state transitions and validation before persistence. Rejected scenes do not modify the accepted story history.

## Architecture Overview

```text
                 Narrative Director
                         |
                     Scene Plan
                         |
                    Writer Interface
                         |
                     Scene Draft
                         |
                 Judge / Validation
                         |
               +---------+---------+
               |                   |
            Rejected             Accepted
               |                   |
         No State Change      Thread Evidence
                                   |
                             State Persistence
```

## Development and Collaboration

DYSTOPIC 2067 provides a practical environment for AI-assisted software development, architectural evaluation, debugging, and collaborative code review.

The public implementation supports independent execution, modification, testing, and extension without requiring access to private infrastructure or external AI services.

The full production platform is maintained separately. This repository provides a self-contained technical implementation suitable for engineering evaluation and collaborative development.

## Additional Documentation

- [Architecture Overview](ARCHITECTURE.md)
- [AI Development Workflow](AI_DEVELOPMENT_WORKFLOW.md)

## License

This repository's original source code is made available under the **MIT License**.

Copyright (c) 2026 Dystenia.

See the [LICENSE](LICENSE) file for the complete license terms.

The separately maintained DYSTOPIC 2067 production platform, its proprietary source code, datasets, world canon, prompts, and associated assets are not included in this repository and are not covered by this repository's MIT License.
