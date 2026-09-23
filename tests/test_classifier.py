import unittest

from livestream_scene_demo.classifier import KeywordMultimodalClassifier
from livestream_scene_demo.types import SceneCategory, WindowInput


class ClassifierTests(unittest.TestCase):
    def setUp(self) -> None:
        self.classifier = KeywordMultimodalClassifier()

    def test_cross_modal_singing_evidence(self) -> None:
        window = WindowInput(
            room_id="room",
            window_start="2026-01-01T00:00:00Z",
            asr_text="<|BGM|> continuous lyrics",
            visual_description="A host is singing into a microphone",
        )
        category, _ = self.classifier.predict(window)
        self.assertEqual(category, SceneCategory.ENTERTAINMENT)

    def test_ecommerce_evidence(self) -> None:
        window = WindowInput(
            room_id="room",
            window_start="2026-01-01T00:00:00Z",
            asr_text="Use the coupon and buy now",
            visual_description="The host presents a product",
        )
        category, _ = self.classifier.predict(window)
        self.assertEqual(category, SceneCategory.ECOMMERCE)


if __name__ == "__main__":
    unittest.main()

