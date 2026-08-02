import json
from pathlib import Path


class BrokerService:

    def get_brokers(
        self,
        search: str | None = None,
        min_investment: int | None = None,
    ):

        file_path = (
            Path(__file__)
            .resolve()
            .parent.parent.parent
            / "datasets"
            / "brokers.json"
        )

        with open(file_path, "r", encoding="utf-8") as file:
            brokers = json.load(file)

        # Filter by search
        if search:
            brokers = [
                broker
                for broker in brokers
                if search.lower() in broker["name"].lower()
            ]

        # Filter by minimum investment
        if min_investment is not None:
            brokers = [
                broker
                for broker in brokers
                if broker["minimum_investment"] <= min_investment
            ]

        return brokers