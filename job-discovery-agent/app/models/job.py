from pydantic import BaseModel
from typing import Optional, List

class Job(BaseModel):
    id: str
    title: str
    company: str
    location: Optional[str] = None
    country: Optional[str] = None
    description: Optional[str] = None
    url: str
    source: str
    remote: bool = False
    tags: List[str] = []
    match_score: float = 0
