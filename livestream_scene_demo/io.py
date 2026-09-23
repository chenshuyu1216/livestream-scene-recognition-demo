from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

from .types import ScenePrediction, WindowInput


def read_windows(path: str | Path) -> list[WindowInput]:
    windows: list[WindowInput] = []
    with Path(path).open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                windows.append(WindowInput.from_dict(json.loads(line)))
            except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
                raise ValueError(f"invalid JSONL at line {line_number}: {exc}") from exc
    return windows


def write_predictions(path: str | Path, predictions: Iterable[ScenePrediction]) -> None:
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as handle:
        for prediction in predictions:
            json.dump(prediction.to_dict(), handle, ensure_ascii=False)
            handle.write("\n")

