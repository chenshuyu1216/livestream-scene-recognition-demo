from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Iterable

from .types import SceneCategory


@dataclass(frozen=True)
class EvaluationResult:
    correct: int
    total: int
    per_class: dict[str, dict[str, int]]

    @property
    def accuracy(self) -> float:
        return self.correct / self.total if self.total else 0.0


def evaluate(
    truth: Iterable[SceneCategory], predicted: Iterable[SceneCategory]
) -> EvaluationResult:
    truth_values = list(truth)
    predicted_values = list(predicted)
    if len(truth_values) != len(predicted_values):
        raise ValueError("truth and predicted lengths differ")

    correct = sum(a == b for a, b in zip(truth_values, predicted_values))
    support = Counter(category.value for category in truth_values)
    class_correct = Counter(
        actual.value
        for actual, guess in zip(truth_values, predicted_values)
        if actual == guess
    )
    per_class = {
        category.value: {
            "correct": class_correct[category.value],
            "support": support[category.value],
        }
        for category in SceneCategory
    }
    return EvaluationResult(correct=correct, total=len(truth_values), per_class=per_class)

