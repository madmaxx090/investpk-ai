from fastapi import APIRouter
from typing import List

from app.services.question_service import QuestionService

from app.schemas.assessment import (
    AssessmentRequest,
    AssessmentResponse
)

from app.schemas.question import Question

from app.decision_engine.readiness_engine import ReadinessEngine
from app.decision_engine.recommendation_engine import RecommendationEngine
from app.decision_engine.investment_engine import InvestmentEngine
from app.decision_engine.company_ranking_engine import CompanyRankingEngine


router = APIRouter()


question_service = QuestionService()

readiness_engine = ReadinessEngine()
recommendation_engine = RecommendationEngine()
investment_engine = InvestmentEngine()
company_ranking_engine = CompanyRankingEngine()



@router.get("/questions", response_model=List[Question])
def get_questions():
    return question_service.get_questions()



@router.post("/", response_model=AssessmentResponse)
def assess(request: AssessmentRequest):

    # 1. Calculate financial readiness
    score = readiness_engine.calculate_score(request)


    # 2. Generate general recommendations
    decision = recommendation_engine.generate_recommendation(
        request,
        score
    )


    # 3. Rank suitable companies dynamically
    ranked_companies = company_ranking_engine.rank_companies(
        risk_tolerance=request.risk_tolerance,
        investment_horizon=request.investment_horizon
    )


    # 4. Generate detailed investment explanation
    investment_plan = []

    for company in ranked_companies:

        analysis = investment_engine.generate_company_analysis(
            symbol=company["symbol"],
            risk_tolerance=request.risk_tolerance,
            horizon=request.investment_horizon
        )

        investment_plan.append(analysis)



    return AssessmentResponse(
        readiness_score=decision["score"],
        readiness_level=decision["status"],
        recommendation=decision["recommendations"],
        warnings=decision["warnings"],
        suggested_companies=investment_plan,
        suggested_brokers=decision["suggested_brokers"],
        explanation=(
            f"Your financial readiness score is {decision['score']}/100. "
            "Companies were selected based on your risk profile, "
            "investment horizon, and financial situation."
        ),
    )