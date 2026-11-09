"""Standalone reference implementation; no production DYSTOPIC source is included."""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from pathlib import Path
from typing import Protocol
import json
import uuid


class ThreadStatus(str, Enum):
    ACTIVE = "active"
    DORMANT = "dormant"
    RESOLVED = "resolved"


@dataclass
class StoryThread:
    title: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    status: ThreadStatus = ThreadStatus.ACTIVE
    evidence: list[str] = field(default_factory=list)
    resolution: str | None = None

    def add_evidence(self, event_id: str) -> None:
        if event_id not in self.evidence:
            self.evidence.append(event_id)

    def transition(self, target: ThreadStatus, *, evidence_id: str | None = None,
                   resolution: str | None = None) -> None:
        if self.status == ThreadStatus.RESOLVED:
            raise ValueError("Resolved threads cannot be reopened")
        if target == ThreadStatus.RESOLVED:
            if not evidence_id or evidence_id not in self.evidence or not resolution or not resolution.strip():
                raise ValueError("Resolution requires linked evidence and a reason")
            self.resolution = resolution.strip()
        elif resolution is not None:
            raise ValueError("Only resolved threads can have a resolution")
        self.status = target


@dataclass(frozen=True)
class ScenePlan:
    number: int
    thread_id: str
    objective: str
    required_fact: str


@dataclass(frozen=True)
class SceneDraft:
    text: str
    asserted_facts: tuple[str, ...]
    evidence_id: str


@dataclass(frozen=True)
class Review:
    accepted: bool
    issues: tuple[str, ...]


class Writer(Protocol):
    def write(self, plan: ScenePlan) -> SceneDraft: ...


class Director:
    def plan(self, number: int, thread: StoryThread, required_fact: str) -> ScenePlan:
        if thread.status != ThreadStatus.ACTIVE:
            raise ValueError("Director requires an active thread")
        return ScenePlan(number, thread.id, f"Advance: {thread.title}", required_fact)


class TemplateWriter:
    """Deterministic offline writer; swap for an LLM adapter in a real integration."""
    def write(self, plan: ScenePlan) -> SceneDraft:
        return SceneDraft(
            text=f"Scene {plan.number}: The team investigates {plan.objective}. "
                 f"The verified record still states: {plan.required_fact}.",
            asserted_facts=(plan.required_fact,),
            evidence_id=f"scene-{plan.number}-observation",
        )


class Judge:
    def review(self, plan: ScenePlan, draft: SceneDraft, known_facts: set[str]) -> Review:
        issues: list[str] = []
        if not draft.text.strip():
            issues.append("empty scene")
        if plan.required_fact not in draft.asserted_facts:
            issues.append("required continuity fact missing")
        if any(fact not in known_facts for fact in draft.asserted_facts):
            issues.append("unverified fact asserted")
        if not draft.evidence_id.strip():
            issues.append("missing evidence identifier")
        return Review(not issues, tuple(issues))


class JsonStore:
    """Atomic single-file replacement for this local demo, not a transactional DB."""
    def __init__(self, path: Path):
        self.path = Path(path)

    def save(self, thread: StoryThread, scenes: list[dict]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = {"thread": asdict(thread), "scenes": scenes}
        tmp = self.path.with_name(self.path.name + ".tmp")
        tmp.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        tmp.replace(self.path)

    def load(self) -> dict:
        return json.loads(self.path.read_text(encoding="utf-8"))


class Orchestrator:
    def __init__(self, writer: Writer, store: JsonStore):
        self.writer = writer
        self.store = store
        self.director = Director()
        self.judge = Judge()

    def run_scene(self, number: int, thread: StoryThread, fact: str,
                  known_facts: set[str], scenes: list[dict]) -> Review:
        plan = self.director.plan(number, thread, fact)
        draft = self.writer.write(plan)
        review = self.judge.review(plan, draft, known_facts)
        if review.accepted:
            # State changes occur only after validation.
            thread.add_evidence(draft.evidence_id)
            scenes.append({"number": number, "text": draft.text,
                           "evidence_id": draft.evidence_id})
            self.store.save(thread, scenes)
        return review
