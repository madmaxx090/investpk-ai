class LLMEngine:


    def generate_explanation(
        self,
        user_data,
        companies
    ):

        explanation = (
            f"Based on your monthly income of "
            f"{user_data.monthly_income} PKR and your "
            f"{user_data.risk_tolerance} risk profile, "
            "the system analyzed companies that match "
            "your investment goals. "
        )


        if companies:

            names = [
                company["company"]
                for company in companies
            ]

            explanation += (
                "Recommended companies include "
                + ", ".join(names)
                + ". "
            )


        explanation += (
            "These recommendations are generated "
            "using your financial readiness, risk "
            "preference, market information, and "
            "available company data."
        )


        return explanation