from agents.fetcher import FetcherAgent
from agents.classifier import ClassifierAgent
from agents.summarizer import SummarizerAgent
from agents.qa import QAAgent
from db.dedup import is_duplicate
from db.database import get_database
from config import TAVILY_API_KEY, OPENAI_API_KEY
from data.schema import Article, Tag, Summary, QAFeedback
from datetime import datetime


def process_news_pipeline():
    fetcher = FetcherAgent(TAVILY_API_KEY)
    classifier = ClassifierAgent(OPENAI_API_KEY)
    summarizer = SummarizerAgent(OPENAI_API_KEY)
    qa_agent = QAAgent(OPENAI_API_KEY)
    db = get_database()

    articles = fetcher.fetch_news()
    for art in articles:
        if not art.get('url') or is_duplicate(art['url']):
            continue
        tags = classifier.classify(art)
        summary_text = summarizer.summarize(art)
        qa_result = qa_agent.review_summary(art, summary_text)
        summary = Summary(text=summary_text)
        tag_obj = Tag(**tags)
        qa_feedback = []
        if qa_result['feedback'] != 'OK':
            qa_feedback.append(QAFeedback(
                article_id=art['url'],
                summary_id=art['url'],
                feedback=qa_result['feedback'],
                suggested_summary=qa_result['suggested_summary']
            ))
        article_doc = Article(
            url=art['url'],
            title=art.get('title', ''),
            content=art.get('content', ''),
            published_at=art.get('published_at', datetime.utcnow()),
            tags=[tag_obj],
            summary=summary,
            source=art.get('source', ''),
            qa_feedback=qa_feedback
        ).dict()
        db.articles.insert_one(article_doc)
        print(f"Inserted: {art.get('title')}")

if __name__ == "__main__":
    process_news_pipeline()