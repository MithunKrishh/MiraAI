import re
from collections import Counter


def _normalize(text: str) -> str:
    text = text.lower().strip()
    # Keep it lightweight: basic clean-up + whitespace normalization.
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text


# Small phrase/keyword sets. This is still lightweight, but smarter than single keywords.
_INTENT_PATTERNS: dict[str, list[str]] = {
    "summarize": [
        "summarize",
        "summary",
        "make this shorter",
        "shorten",
        "condense",
        "compress",
        "tl dr",
        "tldr",
    ],
    "save": [
        "save",
        "store",
        "remember",
        "keep",
        "write down",
        "note this",
    ],
    "retrieve": [
        "retrieve",
        "show",
        "show my tasks",
        "show tasks",
        "list",
        "get",
        "fetch",
        "what did i save",
        "last entry",
        "last task",
        "history",
    ],
}


def detect_intent(text: str) -> str:
    """Detect a user's intent using a tiny, rule-based NLP approach.

    Approach:
    1) Normalize text (lowercase + punctuation removal)
    2) Phrase match (handles multi-word intents like "make this shorter")
    3) Token scoring fallback (counts keyword hits per intent)
    """

    if not isinstance(text, str) or not text.strip():
        return "unknown"

    normalized = _normalize(text)

    # 1) Phrase match first (more precise)
    for intent, phrases in _INTENT_PATTERNS.items():
        for phrase in phrases:
            if " " in phrase and phrase in normalized:
                return intent

    # 2) Token scoring fallback
    tokens = normalized.split()
    token_counts = Counter(tokens)
    scores: dict[str, int] = {"summarize": 0, "save": 0, "retrieve": 0}

    for intent, phrases in _INTENT_PATTERNS.items():
        for phrase in phrases:
            if " " in phrase:
                continue
            if phrase in token_counts:
                scores[intent] += token_counts[phrase]

    best_intent, best_score = max(scores.items(), key=lambda x: x[1])
    return best_intent if best_score > 0 else "unknown"