from pydantic import BaseModel
from typing import List


class Broker(BaseModel):
    id: int
    name: str
    type: str
    market: str
    minimum_investment: int
    features: List[str]