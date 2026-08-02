from pydantic import BaseModel


class Market(BaseModel):
    symbol: str
    price: float
    change: float
    change_percent: float
    volume: int