from typing import Optional

from fastapi import APIRouter, HTTPException

from app.schemas.market import Market
from app.services.market_service import MarketService

router = APIRouter()

market_service = MarketService()


@router.get("/", response_model=list[Market])
def get_market(
    symbol: Optional[str] = None,
):
    return market_service.get_market(symbol)


@router.get("/{symbol}", response_model=Market)
def get_stock(symbol: str):

    stock = market_service.get_stock(symbol)

    if stock is None:
        raise HTTPException(
            status_code=404,
            detail="Stock not found"
        )

    return stock