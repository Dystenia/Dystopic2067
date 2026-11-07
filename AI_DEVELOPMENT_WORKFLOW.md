# AI-Assisted Development Workflow

I use AI coding assistants to explore implementation options, trace failures, and draft changes for DYSTOPIC 2067. I define the expected behavior, make architecture decisions, review proposed changes, and decide what to integrate.

## How I work

1. **Describe the failure.** I start with what happened, what I expected, and which data or output was affected.
2. **Trace the current code.** I identify the entry point, follow the relevant calls, and check where the application reads or writes state. I give the assistant a scoped task based on that code.
3. **Review the proposed change.** I check the assistant’s assumptions and follow the effects across component boundaries, especially when a change touches existing data or shared interfaces.
4. **Verify the affected workflow.** Depending on the change, I reproduce the failure, run targeted tests, or inspect saved state. I keep track of which checks I ran and which behavior still needs verification.

## Example — Investigating a scene rollback

During a rollback investigation, synchronization reported media for a scene outside the active story chronology. The error pointed to a mismatch between the story state and the media visible to downstream tools.

I used a read-only audit to inspect a backup candidate and check which records and media artifacts still referred to the scene. The assistant helped trace references and formulate checks. The recovery decision depended on what the audit found in the saved data.

## My role

My background is in IT administration, infrastructure, automation, and troubleshooting. In DYSTOPIC 2067, I apply that experience to Python and LLM engineering, with responsibility for requirements, architecture, integration, and verification.

[Back to the showcase README](README.md)
