from typing import Optional

from fastapi import APIRouter, HTTPException

from app.schemas.company import Company
from app.services.company_service import CompanyService

router = APIRouter()

company_service = CompanyService()


@router.get("/", response_model=list[Company])
def get_companies(
    search: Optional[str] = None,
    sector: Optional[str] = None,
):
    return company_service.get_companies(search, sector)


@router.get("/{symbol}", response_model=Company)
def get_company(symbol: str):

    company = company_service.get_company(symbol)

    if company is None:
        raise HTTPException(
            status_code=404,
            detail="Company not found"
        )

    return company