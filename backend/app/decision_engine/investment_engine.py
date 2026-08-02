class InvestmentEngine:

    def generate_plan(
        self,
        user,
        companies
    ):

        plan = []

        for company in companies:

            reason = []

            # Risk matching
            if user.risk_tolerance.lower() == "medium":
                reason.append(
                    "Suitable for balanced risk investors"
                )

            elif user.risk_tolerance.lower() == "high":
                reason.append(
                    "Suitable for growth-focused investors"
                )

            else:
                reason.append(
                    "Considered relatively stable"
                )


            # Investment horizon
            if "5" in user.investment_horizon:
                reason.append(
                    "Matches long-term investment horizon"
                )


            plan.append(
                {
                    "company": company["name"],
                    "symbol": company["symbol"],
                    "sector": company["sector"],
                    "reason": reason
                }
            )


        return plan