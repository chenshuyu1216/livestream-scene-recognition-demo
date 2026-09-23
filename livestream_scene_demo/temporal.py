from __future__ import annotations

from collections import Counter, defaultdict, deque

from .types import SceneCategory


class TemporalAggregator:
    """Maintains short-term stable labels and conservative room types."""

    def __init__(self, smoothing_windows: int = 3, confirmation_windows: int = 3):
        if smoothing_windows < 1 or confirmation_windows < 1:
            raise ValueError("window counts must be positive")
        self.smoothing_windows = smoothing_windows
        self.confirmation_windows = confirmation_windows
        self._recent: dict[str, deque[SceneCategory]] = defaultdict(
            lambda: deque(maxlen=smoothing_windows)
        )
        self._stable_runs: dict[str, tuple[SceneCategory | None, int]] = {}
        self._room_types: dict[str, SceneCategory] = {}

    def update(
        self, room_id: str, direct: SceneCategory
    ) -> tuple[SceneCategory | None, SceneCategory | None]:
        recent = self._recent[room_id]
        recent.append(direct)

        stable: SceneCategory | None = None
        if len(recent) == self.smoothing_windows:
            counts = Counter(recent)
            candidate, votes = counts.most_common(1)[0]
            if votes > self.smoothing_windows / 2:
                stable = candidate

        previous, run_length = self._stable_runs.get(room_id, (None, 0))
        if stable is None:
            self._stable_runs[room_id] = (None, 0)
        elif stable == previous:
            self._stable_runs[room_id] = (stable, run_length + 1)
        else:
            self._stable_runs[room_id] = (stable, 1)

        candidate, run_length = self._stable_runs[room_id]
        if candidate is not None and run_length >= self.confirmation_windows:
            self._room_types[room_id] = candidate

        return stable, self._room_types.get(room_id)

