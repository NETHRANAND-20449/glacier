from typing import Dict, List
import openai
from Glacier.config import OPENAI_API_KEY

class ClassifierAgent:
    def __init__(self, openai_api_key: str = None):
        self.openai_api_key = openai_api_key or OPENAI_API_KEY
        openai.api_key = self.openai_api_key

    def classify(self, article: Dict) -> Dict:
        """
        Classify the article by game, type, and region using OpenAI.
        Returns a dict of tags.
        """
        prompt = (
            "Classify the following esports news article. "
            "Return a JSON object with keys: game (e.g., 'Dota 2', 'CS:GO', 'LoL', 'Valorant'), "
            "type (e.g., 'Result', 'Transfer', 'Feature', 'Rumor', 'Business'), and region (e.g., 'NA', 'EU', 'Asia', 'Global').\n"
            f"Title: {article.get('title')}\nContent: {article.get('content')}\n"
        )
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=100,
                temperature=0.2
            )
            import json
            tags = json.loads(response.choices[0].message['content'])
            return tags
        except Exception as e:
            print(f"ClassifierAgent error: {e}")
            return {"game": None, "type": None, "region": None}