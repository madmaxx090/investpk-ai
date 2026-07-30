from fastapi import APIRouter

from app.services.question_service import QuestionService
from app.schemas.assessment import AssessmentRequest, AssessmentResponse
from app.decision_engine.readiness_engine import ReadinessEngine
from typing import List
from app.schemas.question import Question

router = APIRouter()

question_service = QuestionService()
engine = ReadinessEngine()


@router.get("/questions", response_model=List[Question])
def get_questions():
    return question_service.get_questions()


@router.post("/", response_model=AssessmentResponse)
def assess(request: AssessmentRequest):

    score = engine.calculate_score(request)

    if score >= 80:
        level = "High"

    elif score >= 60:
        level = "Medium"

    else:
        level = "Low"


    return AssessmentResponse(
        readiness_score=score,
        readiness_level=level,
        recommendation=(
            "Start with diversified investments and invest regularly."
        ),
        explanation=(
            f"Your readiness score is {score}/100 based on your income, "
            "expenses, investment amount, emergency fund, debt level, "
            "investment experience, and risk tolerance."
        ),
    )