from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Tag(BaseModel):
    game: Optional[str]
    type: Optional[str]
    region: Optional[str]

class Summary(BaseModel):
    text: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class QAFeedback(BaseModel):
    article_id: str
    summary_id: str
    feedback: str
    suggested_summary: Optional[str]
    reviewed_at: datetime = Field(default_factory=datetime.utcnow)

class Article(BaseModel):
    url: str
    title: str
    content: str
    published_at: datetime
    tags: List[Tag]
    summary: Optional[Summary]
    source: Optional[str]
    qa_feedback: List[QAFeedback] = []