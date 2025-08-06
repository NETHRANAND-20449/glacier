from fastapi import FastAPI, HTTPException, Body
from typing import List, Optional
from pydantic import BaseModel
from agents.fetcher import FetcherAgent
from db.database import get_database
from bson.objectid import ObjectId

app = FastAPI()

# --- NEWS ENDPOINT ---
@app.get("/news")
def get_news(keywords: Optional[List[str]] = None):
    fetcher = FetcherAgent()
    articles = fetcher.fetch_news(keywords)
    return articles

# --- WISHLIST MODELS ---
class WishlistItem(BaseModel):
    url: str
    title: str
    content: Optional[str] = ""
    published_at: Optional[str] = None
    source: Optional[str] = None

# --- WISHLIST ENDPOINTS ---
@app.get("/wishlist")
def get_wishlist():
    db = get_database()
    items = list(db.wishlist.find())
    for item in items:
        item["id"] = str(item["_id"])
        del item["_id"]
    return items

@app.post("/wishlist")
def add_to_wishlist(item: WishlistItem):
    db = get_database()
    if db.wishlist.find_one({"url": item.url}):
        raise HTTPException(status_code=400, detail="Item already in wishlist")
    db.wishlist.insert_one(item.dict())
    return {"message": "Added to wishlist"}

@app.delete("/wishlist/{item_id}")
def remove_from_wishlist(item_id: str):
    db = get_database()
    result = db.wishlist.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Removed from wishlist"}

@app.get("/")
def root():
    return {"message": "Esports News Summarizer API"}