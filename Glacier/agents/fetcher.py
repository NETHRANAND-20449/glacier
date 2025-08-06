import requests
from typing import List, Dict
from Glacier.config import TAVILY_API_KEY

class FetcherAgent:
    def __init__(self, tavily_api_key: str = None):
        self.tavily_api_key = tavily_api_key or TAVILY_API_KEY

    def fetch_news(self, keywords: List[str] = None) -> List[Dict]:
        """
        Fetch news articles using Tavily API.
        Returns a list of article dicts.
        """
        url = "https://api.tavily.com/search"
        params = {
            "query": "esports news" if not keywords else " ".join(keywords),
            "topic": "news",
            "num_results": 10
        }
        headers = {"Authorization": f"Bearer {self.tavily_api_key}"}
        try:
            response = requests.get(url, params=params, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            articles = []
            for item in data.get("results", []):
                articles.append({
                    "title": item.get("title"),
                    "url": item.get("url"),
                    "content": item.get("snippet", ""),
                    "published_at": item.get("published_at"),
                    "source": item.get("source")
                })
            return articles
        except Exception as e:
            print(f"FetcherAgent error: {e}")
            return []