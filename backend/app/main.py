from fastapi import FastAPI

from app.api.assessment import router as assessment_router

app = FastAPI(title="InvestPK AI")

app.include_router(
    assessment_router,
    prefix="/assessment",
    tags=["Assessment"],
)