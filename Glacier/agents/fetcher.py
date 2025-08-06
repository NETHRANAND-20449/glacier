import requests
from typing import List, Dict
from Glacier.config import TAVILY_API_KEY

class FetcherAgent:
    def __init__(self, tavily_api_key: str = None):
        self.tavily_api_key = tavily_api_key or TAVILY_API_KEY

    def fetch_news(self, keywords: List[str] = None) -> List[Dict]:
        """
        Fetch news articles using Tavily API (POST request).
        Returns a list of article dicts.
        """
        url = "https://api.tavily.com/search"
        headers = {
            "Authorization": f"Bearer {self.tavily_api_key}",
            "Content-Type": "application/json"
        }
        body = {
            "query": "esports news" if not keywords else " ".join(keywords),
            "topic": "news",
            "max_results": 10
        }
        try:
            response = requests.post(url, headers=headers, json=body, timeout=10)
            print(f"Tavily API status: {response.status_code}")
            print(f"Tavily API raw response: {response.text}")
            response.raise_for_status()
            data = response.json()
            print("Tavily API parsed JSON:", data)
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
            import traceback; traceback.print_exc()
            return []