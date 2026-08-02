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


router = APIRouter()


question_service = QuestionService()

readiness_engine = ReadinessEngine()

recommendation_engine = RecommendationEngine()


@router.get("/questions", response_model=List[Question])
def get_questions():
    return question_service.get_questions()



@router.post("/", response_model=AssessmentResponse)
def assess(request: AssessmentRequest):

    # Calculate financial readiness score
    score = readiness_engine.calculate_score(request)


    # Generate personalized advice
    decision = recommendation_engine.generate_recommendation(
        request,
        score
    )


    return AssessmentResponse(
    readiness_score=decision["score"],
    readiness_level=decision["status"],
    recommendation=decision["recommendations"],
    warnings=decision["warnings"],
    suggested_companies=decision["suggested_companies"],
    suggested_brokers=decision["suggested_brokers"],
    explanation=(
        f"Your financial readiness score is {decision['score']}/100. "
        "The recommendation considers your income, expenses, risk profile, "
        "investment experience, and financial stability."
    ),
)