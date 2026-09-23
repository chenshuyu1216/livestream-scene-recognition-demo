from __future__ import annotations

from .classifier import KeywordMultimodalClassifier
from .temporal import TemporalAggregator
from .types import ScenePrediction, WindowInput


class ScenePipeline:
    def __init__(
        self,
        classifier: KeywordMultimodalClassifier | None = None,
        aggregator: TemporalAggregator | None = None,
    ):
        self.classifier = classifier or KeywordMultimodalClassifier()
        self.aggregator = aggregator or TemporalAggregator()

    def process(self, window: WindowInput) -> ScenePrediction:
        direct, scores = self.classifier.predict(window)
        stable, room_type = self.aggregator.update(window.room_id, direct)
        return ScenePrediction(
            room_id=window.room_id,
            window_start=window.window_start,
            current_activity=direct,
            stable_category=stable,
            room_type=room_type,
            scores=scores,
        )

