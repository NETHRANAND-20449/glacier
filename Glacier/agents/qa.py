from typing import Dict

class QAAgent:
    def __init__(self, openai_api_key: str):
        self.openai_api_key = openai_api_key

    def review_summary(self, article: Dict, summary: str) -> Dict:
        """
        Review the summary for factuality and quality. Returns feedback dict.
        """
        # TODO: Implement QA logic (OpenAI or other LLM)
        return {"feedback": "", "suggested_summary": None}