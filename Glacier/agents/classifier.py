from typing import Dict, List

class ClassifierAgent:
    def __init__(self, openai_api_key: str):
        self.openai_api_key = openai_api_key

    def classify(self, article: Dict) -> Dict:
        """
        Classify the article by game, type, and region.
        Returns a dict of tags.
        """
        # TODO: Implement classification logic (OpenAI or HuggingFace)
        return {"game": None, "type": None, "region": None}