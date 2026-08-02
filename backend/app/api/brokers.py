from typing import List

from fastapi import APIRouter, Query

from app.schemas.broker import Broker
from app.services.broker_service import BrokerService

router = APIRouter()

broker_service = BrokerService()


@router.get("/brokers", response_model=List[Broker])
def get_brokers(
    search: str | None = Query(
        default=None,
        description="Search broker by name"
    ),
    min_investment: int | None = Query(
        default=None,
        description="Maximum investment amount the user can afford"
    ),
):
    return broker_service.get_brokers(
        search=search,
        min_investment=min_investment,
    )