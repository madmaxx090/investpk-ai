import json
from pathlib import Path


class MarketService:

    def get_market(self, symbol=None):

        file_path = (
            Path(__file__).resolve().parent.parent.parent
            / "datasets"
            / "market.json"
        )

        with open(file_path, "r", encoding="utf-8") as f:
            market = json.load(f)

        if symbol:
            market = [
                stock
                for stock in market
                if stock["symbol"].lower() == symbol.lower()
            ]

        return market

    def get_stock(self, symbol: str):

        file_path = (
            Path(__file__).resolve().parent.parent.parent
            / "datasets"
            / "market.json"
        )

        with open(file_path, "r", encoding="utf-8") as f:
            market = json.load(f)

        for stock in market:
            if stock["symbol"].lower() == symbol.lower():
                return stock

        return None