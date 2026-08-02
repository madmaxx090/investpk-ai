from app.services.company_service import CompanyService
from app.services.market_service import MarketService
from app.services.news_service import NewsService


class InvestmentEngine:

    def __init__(self):
        self.company_service = CompanyService()
        self.market_service = MarketService()
        self.news_service = NewsService()


    def generate_company_analysis(self, symbol, risk_tolerance, horizon):

        company = self.company_service.get_company(symbol)

        market = self.market_service.get_stock(symbol)

        news = self.news_service.get_news(
            company=symbol
        )


        reasons = []


        # Risk matching
        if risk_tolerance.lower() == "medium":
            reasons.append(
                "Suitable for balanced risk investors"
            )

        elif risk_tolerance.lower() == "high":
            reasons.append(
                "Suitable for growth-oriented investors"
            )

        else:
            reasons.append(
                "Suitable for conservative investors"
            )


        # Horizon matching
        if "5" in str(horizon):
            reasons.append(
                "Matches long-term investment horizon"
            )


        return {
            "company": company["name"],
            "symbol": company["symbol"],
            "sector": company["sector"],
            "reasons": reasons,
            "market_data": market,
            "recent_news": news[:3]
        }