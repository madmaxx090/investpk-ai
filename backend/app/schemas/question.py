from pydantic import BaseModel
from typing import List, Optional


class Question(BaseModel):
    id: int
    question: str
    type: str
    options: Optional[List[str]] = None