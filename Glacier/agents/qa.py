from typing import Dict
import openai
from Glacier.config import OPENAI_API_KEY

class QAAgent:
    def __init__(self, openai_api_key: str = None):
        self.openai_api_key = openai_api_key or OPENAI_API_KEY
        openai.api_key = self.openai_api_key

    def review_summary(self, article: Dict, summary: str) -> Dict:
        """
        Review the summary for factuality and quality. Returns feedback dict.
        """
        prompt = (
            "You are a QA agent for esports news summaries. "
            "Given the article and its summary, check if the summary is accurate, clear, and includes all key facts. "
            "If the summary is good, reply with feedback: 'OK'. If not, suggest an improved summary.\n"
            f"Title: {article.get('title')}\nContent: {article.get('content')}\nSummary: {summary}\n"
        )
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=120,
                temperature=0.2
            )
            content = response.choices[0].message['content'].strip()
            if content.lower().startswith('ok'):
                return {"feedback": "OK", "suggested_summary": None}
            else:
                return {"feedback": "Needs improvement", "suggested_summary": content}
        except Exception as e:
            print(f"QAAgent error: {e}")
            return {"feedback": "Error", "suggested_summary": None}