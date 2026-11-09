"""Run: python demo.py"""
from pathlib import Path
from tempfile import TemporaryDirectory
from engine import JsonStore, Orchestrator, SceneDraft, StoryThread, TemplateWriter


class ContradictoryWriter:
    def write(self, plan):
        return SceneDraft("A surprising claim appears.", ("The gate is open",), "false-1")


def main():
    with TemporaryDirectory() as directory:
        store = JsonStore(Path(directory) / "story.json")
        thread = StoryThread("Investigate the sealed gate")
        scenes = []
        known = {"The gate is sealed"}
        good = Orchestrator(TemplateWriter(), store)
        for number in (1, 2):
            result = good.run_scene(number, thread, "The gate is sealed", known, scenes)
            print(f"Scene {number}: {'ACCEPTED' if result.accepted else 'REJECTED'}")
        bad = Orchestrator(ContradictoryWriter(), store)
        result = bad.run_scene(3, thread, "The gate is sealed", known, scenes)
        print(f"Scene 3: {'ACCEPTED' if result.accepted else 'REJECTED'} — {', '.join(result.issues)}")
        print(f"Persisted scenes: {len(store.load()['scenes'])}")
        assert len(scenes) == 2
        assert not result.accepted


if __name__ == "__main__":
    main()
