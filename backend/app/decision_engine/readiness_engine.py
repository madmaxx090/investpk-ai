class ReadinessEngine:

    def calculate_score(self, data):

        score = 0

        disposable = data.monthly_income - data.monthly_expenses

        if disposable >= 30000:
            score += 25
        elif disposable >= 15000:
            score += 15
        else:
            score += 5

        if data.investment_amount >= 50000:
            score += 15
        else:
            score += 5

        if data.emergency_fund_months >= 6:
            score += 15
        elif data.emergency_fund_months >= 3:
            score += 10

        if data.debt_level.lower() == "low":
            score += 15
        elif data.debt_level.lower() == "medium":
            score += 10

        if data.investing_experience.lower() == "advanced":
            score += 15
        elif data.investing_experience.lower() == "intermediate":
            score += 10
        else:
            score += 5

        if "5" in data.investment_horizon:
            score += 15
        else:
            score += 10

        if data.risk_tolerance.lower() == "high":
            score += 15
        elif data.risk_tolerance.lower() == "medium":
            score += 10
        else:
            score += 5

        return min(score, 100)