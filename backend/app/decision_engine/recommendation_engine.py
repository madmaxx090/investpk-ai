from app.services.company_service import CompanyService
from app.services.broker_service import BrokerService


class RecommendationEngine:

    def __init__(self):

        self.company_service = CompanyService()
        self.broker_service = BrokerService()


    def generate_recommendation(self, data, score):

        recommendations = []
        warnings = []


        # Financial readiness
        if score >= 70:
            status = "Ready for investing"

        elif score >= 40:
            status = "Moderately ready"
            warnings.append(
                "Improve financial stability before increasing investment"
            )

        else:
            status = "Not ready"
            warnings.append(
                "Focus on savings and emergency fund first"
            )


        # Risk profile
        risk = data.risk_tolerance.lower()


        if risk == "high":

            recommendations.append(
                "Focus on growth-oriented PSX companies"
            )

            companies = self.company_service.get_companies(
                sector="Technology"
            )


        elif risk == "medium":

            recommendations.append(
                "Consider diversified large-cap companies"
            )

            companies = self.company_service.get_companies()


        else:

            recommendations.append(
                "Prefer stable and lower-risk investments"
            )

            companies = self.company_service.get_companies(
                sector="Banking"
            )


        # Emergency fund check

        if data.emergency_fund_months < 3:
            warnings.append(
                "Build at least 3-6 months emergency fund"
            )


        # Debt check

        if data.debt_level.lower() == "high":

            warnings.append(
                "Reduce high debt before aggressive investing"
            )


        # Broker suggestions

        brokers = self.broker_service.get_brokers(
            min_investment=data.investment_amount
        )


        return {

            "score": score,

            "status": status,

            "recommendations": recommendations,

            "warnings": warnings,

            "suggested_companies": companies[:3],

            "suggested_brokers": brokers[:3]
        }