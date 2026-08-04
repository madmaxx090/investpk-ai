from fastapi import FastAPI

from app.api.assessment import router as assessment_router
from app.api.brokers import router as broker_router
from app.api.market import router as market_router
from app.api.news import router as news_router
from app.api.routes.company import router as company_router

app = FastAPI(
    title="InvestPK AI",
    version="0.1.0"
)

# Assessment API
app.include_router(
    assessment_router,
    prefix="/assessment",
    tags=["Assessment"],
)

# Broker API
app.include_router(
    broker_router,
    prefix="/brokers",
    tags=["Brokers"],
)

# Company API (Real PSX Data)
app.include_router(company_router)

# Market API
app.include_router(
    market_router,
    prefix="/market",
    tags=["Market"],
)

# News API
app.include_router(
    news_router,
    prefix="/news",
    tags=["News"],
)