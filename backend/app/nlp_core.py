from typing import List, Dict

from .policy_check import is_content_safe

class ContentGen:
    """Placeholder for the Content‑Gen NLP Core.
    A real implementation would fine‑tune a language model to map a trend
    descriptor to copy, hashtags and a visual prompt. For the MVP we generate
    simple deterministic outputs based on the trend string.
    """

    def generate(self, trend: str) -> Dict[str, object]:
        # Basic deterministic generation
        copy = f"Introducing our latest offering inspired by {trend}."
        # Safety check using simple policy filter
        safe = is_content_safe(copy)
        # Derive hashtags from trend words
        words = [w for w in trend.split() if w]
        hashtags = [f"#{w.lower()}" for w in words][:5]
        visual_prompt = f"Create a vibrant image representing {trend}."
        return {
            "copy": copy,
            "safe": safe,
            "hashtags": hashtags,
            "visual_prompt": visual_prompt,
        }
