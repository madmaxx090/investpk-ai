import json
from pathlib import Path


class CompanyService:

    def get_companies(self, search=None, sector=None):

        file_path = (
            Path(__file__).resolve().parent.parent.parent
            / "datasets"
            / "companies.json"
        )

        with open(file_path, "r", encoding="utf-8") as f:
            companies = json.load(f)

        # Search by company name or symbol
        if search:
            companies = [
                company
                for company in companies
                if search.lower() in company["name"].lower()
                or search.lower() in company["symbol"].lower()
            ]

        # Filter by sector
        if sector:
            companies = [
                company
                for company in companies
                if company["sector"].lower() == sector.lower()
            ]

        return companies

    def get_company(self, symbol: str):

        file_path = (
            Path(__file__).resolve().parent.parent.parent
            / "datasets"
            / "companies.json"
        )

        with open(file_path, "r", encoding="utf-8") as f:
            companies = json.load(f)

        for company in companies:
            if company["symbol"].lower() == symbol.lower():
                return company

        return None