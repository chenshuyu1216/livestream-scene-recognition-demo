import unittest

from livestream_scene_demo.metrics import evaluate
from livestream_scene_demo.types import SceneCategory


class MetricsTests(unittest.TestCase):
    def test_accuracy_and_support(self) -> None:
        result = evaluate(
            [SceneCategory.GAMING, SceneCategory.CHATTING],
            [SceneCategory.GAMING, SceneCategory.GAMING],
        )
        self.assertEqual(result.correct, 1)
        self.assertEqual(result.total, 2)
        self.assertEqual(result.accuracy, 0.5)
        self.assertEqual(result.per_class["chatting"]["support"], 1)


if __name__ == "__main__":
    unittest.main()

