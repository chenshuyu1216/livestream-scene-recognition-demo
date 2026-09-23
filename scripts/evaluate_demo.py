from __future__ import annotations

import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from livestream_scene_demo.io import read_windows
from livestream_scene_demo.metrics import evaluate
from livestream_scene_demo.pipeline import ScenePipeline


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: python scripts/evaluate_demo.py INPUT.jsonl")
    windows = read_windows(sys.argv[1])
    labeled = [window for window in windows if window.label is not None]
    pipeline = ScenePipeline()
    predictions = [pipeline.process(window) for window in labeled]
    result = evaluate(
        [window.label for window in labeled if window.label is not None],
        [prediction.current_activity for prediction in predictions],
    )
    print(
        json.dumps(
            {
                "correct": result.correct,
                "total": result.total,
                "accuracy": round(result.accuracy, 4),
                "per_class": result.per_class,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

