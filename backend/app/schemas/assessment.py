from pydantic import BaseModel, Field


class AssessmentRequest(BaseModel):
    age: int = Field(..., ge=18, le=100)

    monthly_income: float = Field(..., ge=0)

    monthly_expenses: float = Field(..., ge=0)

    investment_amount: float = Field(..., ge=0)

    investment_goal: str

    investment_horizon: str

    risk_tolerance: str

    emergency_fund_months: int = Field(..., ge=0)

    debt_level: str

    investing_experience: str


class AssessmentResponse(BaseModel):
    readiness_score: int

    readiness_level: str

    recommendation: str

    explanation: str