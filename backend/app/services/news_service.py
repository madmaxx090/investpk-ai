import json
from pathlib import Path


class NewsService:

    def __init__(self):
        self.file_path = (
            Path(__file__).resolve().parent.parent.parent
            / "datasets"
            / "news.json"
        )

    def _load_news(self):
        with open(self.file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_news(self, company=None, category=None):
        news = self._load_news()

        if company:
            news = [
                article
                for article in news
                if article["company"].lower() == company.lower()
            ]

        if category:
            news = [
                article
                for article in news
                if article["category"].lower() == category.lower()
            ]

        return news

    def get_article(self, article_id: int):
        news = self._load_news()

        for article in news:
            if article["id"] == article_id:
                return article

        return None