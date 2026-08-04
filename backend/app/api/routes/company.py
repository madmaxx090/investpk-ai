from fastapi import APIRouter, Query
from app.services.psx_service import PSXService

router = APIRouter(prefix="/companies", tags=["Companies"])

psx = PSXService()


@router.get("/")
def get_companies():
    return psx.get_symbols()


@router.get("/search")
def search_company(q: str = Query(..., min_length=1)):
    return psx.search_company(q)


@router.get("/market-watch")
def market_watch():
    return psx.get_market_watch()


@router.get("/performers")
def performers():
    return psx.get_top_performers()


@router.get("/kse100")
def kse100():
    return psx.get_kse100_chart()