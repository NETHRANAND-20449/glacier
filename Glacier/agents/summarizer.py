from typing import Dict
import openai
from Glacier.config import OPENAI_API_KEY

class SummarizerAgent:
    def __init__(self, openai_api_key: str = None):
        self.openai_api_key = openai_api_key or OPENAI_API_KEY
        openai.api_key = self.openai_api_key

    def summarize(self, article: Dict) -> str:
        """
        Summarize the article content using OpenAI.
        Returns a summary string.
        """
        prompt = (
            "Summarize the following esports news article in 1-3 sentences, "
            "preserving key details (event, player/team names, scores, context):\n"
            f"Title: {article.get('title')}\nContent: {article.get('content')}\n"
        )
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=120,
                temperature=0.3
            )
            return response.choices[0].message['content'].strip()
        except Exception as e:
            print(f"SummarizerAgent error: {e}")
            return ""