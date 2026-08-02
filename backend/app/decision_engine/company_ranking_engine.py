from app.services.company_service import CompanyService


class CompanyRankingEngine:

    def __init__(self):
        self.company_service = CompanyService()


    def rank_companies(self, risk_tolerance, investment_horizon):

        companies = self.company_service.get_companies()

        ranked = []


        for company in companies:

            score = 0
            reasons = []


            # Market cap preference
            if company["market_cap"] == "Large Cap":
                score += 20
                reasons.append(
                    "Large-cap company with relatively stable market presence"
                )


            # Risk matching
            if risk_tolerance.lower() == "medium":

                if company["sector"] in [
                    "Banking",
                    "Conglomerate",
                    "Cement"
                ]:
                    score += 20
                    reasons.append(
                        "Matches balanced risk profile"
                    )


            elif risk_tolerance.lower() == "high":

                if company["sector"] == "Technology":
                    score += 20
                    reasons.append(
                        "Suitable for growth-oriented investors"
                    )


            else:

                if company["sector"] in [
                    "Banking"
                ]:
                    score += 20
                    reasons.append(
                        "Suitable for conservative investors"
                    )


            # Long-term horizon
            if "5" in str(investment_horizon):
                score += 10
                reasons.append(
                    "Suitable for long-term investment horizon"
                )


            ranked.append(
                {
                    "symbol": company["symbol"],
                    "score": score,
                    "reasons": reasons
                }
            )


        # Highest score first
        ranked.sort(
            key=lambda x: x["score"],
            reverse=True
        )


        return ranked[:3]