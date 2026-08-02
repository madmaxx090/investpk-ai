from pydantic import BaseModel
from typing import List, Any


class AssessmentRequest(BaseModel):
    age: int
    monthly_income: float
    monthly_expenses: float
    investment_amount: float
    investment_goal: str
    investment_horizon: str
    risk_tolerance: str
    emergency_fund_months: int
    debt_level: str
    investing_experience: str


class AssessmentResponse(BaseModel):
    readiness_score: int
    readiness_level: str

    recommendation: List[str]

    warnings: List[str]

    suggested_companies: List[Any]

    suggested_brokers: List[Any]

    explanation: str