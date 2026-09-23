from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum
from typing import Any


class SceneCategory(str, Enum):
    ECOMMERCE = "ecommerce"
    GAMING = "gaming"
    ENTERTAINMENT = "entertainment"
    CHATTING = "chatting"


@dataclass(frozen=True)
class WindowInput:
    room_id: str
    window_start: str
    asr_text: str
    visual_description: str
    label: SceneCategory | None = None

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> "WindowInput":
        label = value.get("label")
        return cls(
            room_id=str(value["room_id"]),
            window_start=str(value["window_start"]),
            asr_text=str(value.get("asr_text", "")),
            visual_description=str(value.get("visual_description", "")),
            label=SceneCategory(label) if label else None,
        )


@dataclass(frozen=True)
class ScenePrediction:
    room_id: str
    window_start: str
    current_activity: SceneCategory
    stable_category: SceneCategory | None
    room_type: SceneCategory | None
    scores: dict[str, float]

    def to_dict(self) -> dict[str, Any]:
        result = asdict(self)
        result["current_activity"] = self.current_activity.value
        result["stable_category"] = (
            self.stable_category.value if self.stable_category else None
        )
        result["room_type"] = self.room_type.value if self.room_type else None
        return result

