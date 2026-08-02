from typing import Optional

from pydantic import BaseModel


class News(BaseModel):
    id: int
    title: str
    company: Optional[str]
    category: str
    date: str
    summary: str