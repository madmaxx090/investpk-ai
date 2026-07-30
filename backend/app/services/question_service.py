import json
from pathlib import Path


class QuestionService:

    def get_questions(self):

        file_path = (
            Path(__file__)
            .resolve()
            .parent.parent.parent
            / "datasets"
            / "investment_questions.json"
        )

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)