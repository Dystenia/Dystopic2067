import tempfile
import unittest
from pathlib import Path
from engine import (Director, JsonStore, Judge, Orchestrator, SceneDraft,
                    StoryThread, TemplateWriter, ThreadStatus)


class EngineTests(unittest.TestCase):
    def test_resolution_requires_evidence(self):
        thread = StoryThread("Find the signal")
        with self.assertRaises(ValueError):
            thread.transition(ThreadStatus.RESOLVED, evidence_id="missing", resolution="Found")
        thread.add_evidence("e1")
        thread.transition(ThreadStatus.RESOLVED, evidence_id="e1", resolution="Found")
        self.assertEqual(thread.status, ThreadStatus.RESOLVED)
        with self.assertRaises(ValueError):
            thread.transition(ThreadStatus.ACTIVE)

    def test_judge_rejects_unverified_fact(self):
        thread = StoryThread("Find the signal")
        plan = Director().plan(1, thread, "Door locked")
        draft = SceneDraft("Door opens", ("Door open",), "e1")
        result = Judge().review(plan, draft, {"Door locked"})
        self.assertFalse(result.accepted)
        self.assertIn("unverified fact asserted", result.issues)

    def test_accepted_scene_is_persisted(self):
        with tempfile.TemporaryDirectory() as folder:
            store = JsonStore(Path(folder) / "story.json")
            thread = StoryThread("Find the signal")
            scenes = []
            result = Orchestrator(TemplateWriter(), store).run_scene(
                1, thread, "Door locked", {"Door locked"}, scenes)
            self.assertTrue(result.accepted)
            self.assertEqual(len(store.load()["scenes"]), 1)
            self.assertEqual(len(store.load()["thread"]["evidence"]), 1)

    def test_rejected_scene_does_not_mutate_state(self):
        class BadWriter:
            def write(self, plan):
                return SceneDraft("Contradiction", ("Door open",), "e2")
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "story.json"
            thread = StoryThread("Find the signal")
            scenes = []
            result = Orchestrator(BadWriter(), JsonStore(path)).run_scene(
                1, thread, "Door locked", {"Door locked"}, scenes)
            self.assertFalse(result.accepted)
            self.assertFalse(path.exists())
            self.assertEqual(thread.evidence, [])
            self.assertEqual(scenes, [])

    def test_dormant_thread_cannot_be_planned(self):
        thread = StoryThread("Find the signal")
        thread.transition(ThreadStatus.DORMANT)
        with self.assertRaises(ValueError):
            Director().plan(1, thread, "Door locked")


if __name__ == "__main__":
    unittest.main()
