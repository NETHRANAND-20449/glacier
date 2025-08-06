from Glacier.db.database import get_database

def is_duplicate(url: str) -> bool:
    db = get_database()
    return db.articles.find_one({"url": url}) is not None