from __future__ import annotations

from collections import defaultdict

from .types import SceneCategory, WindowInput


KEYWORDS: dict[SceneCategory, tuple[str, ...]] = {
    SceneCategory.ECOMMERCE: (
        "add to cart",
        "buy now",
        "coupon",
        "discount",
        "product",
        "下单",
        "优惠",
        "商品",
        "链接",
    ),
    SceneCategory.GAMING: (
        "gameplay",
        "game interface",
        "match",
        "level",
        "玩家",
        "游戏",
        "对局",
        "击败",
    ),
    SceneCategory.ENTERTAINMENT: (
        "singing",
        "dancing",
        "microphone",
        "lyrics",
        "<|bgm|>",
        "唱歌",
        "跳舞",
        "歌词",
        "麦克风",
    ),
    SceneCategory.CHATTING: (
        "talking to viewers",
        "conversation",
        "answering comments",
        "聊天",
        "闲聊",
        "回答评论",
    ),
}


class KeywordMultimodalClassifier:
    """Transparent demo classifier over precomputed ASR and vision text.

    The private internship project used learned semantic features. This public
    implementation intentionally uses inspectable keyword evidence so that it
    can run without model weights or private data.
    """

    def predict(self, window: WindowInput) -> tuple[SceneCategory, dict[str, float]]:
        asr = window.asr_text.casefold()
        vision = window.visual_description.casefold()
        scores: dict[SceneCategory, float] = defaultdict(float)

        for category, keywords in KEYWORDS.items():
            for keyword in keywords:
                needle = keyword.casefold()
                if needle in asr:
                    scores[category] += 1.0
                if needle in vision:
                    scores[category] += 1.2

        # Cross-modal evidence is more reliable than a single weak cue.
        if ("<|bgm|>" in asr or "歌词" in asr or "lyrics" in asr) and any(
            cue in vision for cue in ("singing", "microphone", "唱歌", "麦克风")
        ):
            scores[SceneCategory.ENTERTAINMENT] += 2.5

        if any(cue in asr for cue in ("下单", "coupon", "discount")) and any(
            cue in vision for cue in ("product", "商品", "展示")
        ):
            scores[SceneCategory.ECOMMERCE] += 2.5

        if not scores or max(scores.values(), default=0.0) == 0.0:
            scores[SceneCategory.CHATTING] = 0.1

        winner = max(
            SceneCategory,
            key=lambda category: (scores.get(category, 0.0), -list(SceneCategory).index(category)),
        )
        normalized = {category.value: scores.get(category, 0.0) for category in SceneCategory}
        return winner, normalized

