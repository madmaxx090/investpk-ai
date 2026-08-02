from typing import List, Optional

from fastapi import APIRouter, HTTPException

from app.schemas.news import News
from app.services.news_service import NewsService


router = APIRouter()

news_service = NewsService()


@router.get(
    "/",
    response_model=List[News],
)
def get_news(
    company: Optional[str] = None,
    category: Optional[str] = None,
):
    return news_service.get_news(
        company=company,
        category=category,
    )


@router.get(
    "/{article_id}",
    response_model=News,
)
def get_article(article_id: int):

    article = news_service.get_article(article_id)

    if article is None:
        raise HTTPException(
            status_code=404,
            detail="Article not found",
        )

    return article