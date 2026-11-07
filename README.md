# DYSTOPIC 2067

**A modular Python desktop platform for AI-assisted storytelling and multimedia production.**

I’m Michael Cerovsek, the developer behind DYSTOPIC 2067. I started the project to write stories and built a desktop workspace for generating scenes, editing text, creating images, producing audiobooks, and preparing stories for publication.

The central engineering challenge is keeping the story consistent as multiple models and production tools work from the same scenes. A draft can read well and still contradict what a character knows. A revised scene can also leave behind voice takes or sound effects tied to an earlier version.

This repository contains selected project documentation. The application source code is private.

## What the platform does

| Area | Workflow |
| --- | --- |
| **Multi-model story orchestration** | Multiple LLMs support specialized roles. The Director guides scene development, the Writer drafts the scene, and the Judge evaluates it against narrative and continuity requirements. The Micro Repair Writer proposes targeted revisions, and the Micro Repair Judge evaluates those revisions. |
| **Persistent narrative state** | The Story Engine tracks characters, relationships, memories, world state, and story threads across scenes. Continuity checks draw on established facts and prior events. |
| **Desktop production GUI** | The graphical workspace brings together story generation, AI-assisted proofreading, image generation, and audio production. |
| **Image generation** | The image workflow can use a remote generation API or run locally with Juggernaut. |
| **Audiobook narration** | An AI stage segments and tags scene text for audio production. A text-to-speech API renders the segments using distinct voice profiles for the narrator, main characters, and supporting characters. |
| **Sound effects** | An AI stage identifies sound cues in the scene. A separate selection stage searches a local sound library for suitable assets and sends missing effects to a generation API. |
| **Publishing** | The platform supports EPUB production and publication through a web-based CMS. |

## Engineering challenges

- **Approval and persistence.** A single scene can change several parts of the narrative state. The approval and save workflow must account for rejected drafts, interrupted saves, and retries.
- **Context and continuity.** The engine has to supply each role with relevant facts about previous events, character knowledge, and unresolved threads. Evaluating those constraints is a separate task from assessing prose quality.
- **Integration and recovery.** Story text and scene identifiers give production tools a shared reference. Each workflow manages its own artifacts, such as images, voice takes, or audio mixes. During revisions and rollbacks, those tools need to distinguish assets for the active scene from assets created for an earlier version.

## My role and development workflow

I define requirements, make architecture decisions, design data flows, and integrate changes. I use AI coding assistants to explore implementation options, draft changes, and trace failures. I review proposed changes against the current code and its callers, then choose targeted checks based on the behavior affected.

My background is in IT administration, infrastructure, automation, and troubleshooting. DYSTOPIC is where I apply that experience to Python and LLM engineering, including debugging state inconsistencies and tracing failures across the desktop application and media workflows.

## Development status

DYSTOPIC has been used to produce complete stories and rendered audio. The Story Engine is in active stabilization, with current work focused on story thread lifecycle, continuity checks, and reliable state updates and recovery. The media and publishing components are at different stages of development.

## Further reading

- [Architecture](ARCHITECTURE.md) — Story Engine roles, narrative state, and media production workflows.
- [AI-assisted development workflow](AI_DEVELOPMENT_WORKFLOW.md) — How I scope changes, review AI-generated code, and investigate failures.
