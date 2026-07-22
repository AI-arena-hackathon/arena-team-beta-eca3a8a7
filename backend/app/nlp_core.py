from typing import List, Dict

class ContentGen:
    """Placeholder for the Content‑Gen NLP Core.
    A real implementation would fine‑tune a language model to map a trend
    descriptor to copy, hashtags and a visual prompt. For the MVP we generate
    simple deterministic outputs based on the trend string.
    """

    def generate(self, trend: str) -> Dict[str, object]:
        # Basic deterministic generation
        copy = f"Introducing our latest offering inspired by {trend}."
        # Derive hashtags from trend words
        words = [w for w in trend.split() if w]
        hashtags = [f"#{w.lower()}" for w in words][:5]
        visual_prompt = f"Create a vibrant image representing {trend}."
        return {
            "copy": copy,
            "hashtags": hashtags,
            "visual_prompt": visual_prompt,
        }
