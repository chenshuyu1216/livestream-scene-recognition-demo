import unittest

from livestream_scene_demo.temporal import TemporalAggregator
from livestream_scene_demo.types import SceneCategory


class TemporalAggregatorTests(unittest.TestCase):
    def test_room_type_requires_repeated_stable_evidence(self) -> None:
        aggregator = TemporalAggregator(smoothing_windows=3, confirmation_windows=3)
        results = [
            aggregator.update("room", SceneCategory.ENTERTAINMENT)
            for _ in range(5)
        ]
        self.assertEqual(results[1], (None, None))
        self.assertEqual(results[2], (SceneCategory.ENTERTAINMENT, None))
        self.assertEqual(results[4], (SceneCategory.ENTERTAINMENT, SceneCategory.ENTERTAINMENT))

    def test_rooms_are_isolated(self) -> None:
        aggregator = TemporalAggregator(smoothing_windows=1, confirmation_windows=1)
        _, room_a = aggregator.update("a", SceneCategory.GAMING)
        _, room_b = aggregator.update("b", SceneCategory.CHATTING)
        self.assertEqual(room_a, SceneCategory.GAMING)
        self.assertEqual(room_b, SceneCategory.CHATTING)


if __name__ == "__main__":
    unittest.main()

