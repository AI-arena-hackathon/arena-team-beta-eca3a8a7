from typing import List

# Simple policy check placeholder.
# In production this would call external services like Perspective API.
# Here we flag content containing any word from a banned list.

BANNED_WORDS: List[str] = [
    "spam",
    "scam",
    "illegal",
    "banned",
]


def is_content_safe(text: str) -> bool:
    """Return True if text does not contain any banned words (case‑insensitive)."""
    lowered = text.lower()
    return not any(banned in lowered for banned in BANNED_WORDS)
