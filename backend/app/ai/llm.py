class LLMEngine:
    """
    Free AI explanation engine for InvestPK AI
    Compatible with assessment.py
    """

    def generate_explanation(self, request, investment_plan):

        risk = request.risk_tolerance
        horizon = request.investment_horizon
        income = request.monthly_income
        amount = request.investment_amount


        # Extract company information from list
        if investment_plan and len(investment_plan) > 0:

            first_company = investment_plan[0]

            company_name = (
                first_company.get("company")
                or first_company.get("symbol")
                or "recommended companies"
            )

            reason = (
                first_company.get("reason")
                or first_company.get("analysis")
                or "Matches your investment profile"
            )

        else:
            company_name = "No specific company"
            reason = "Based on your financial profile"



        explanation = f"""
InvestPK AI analyzed your financial profile.

Your risk tolerance:
{risk}

Investment horizon:
{horizon}

Financial capacity:
Your monthly income is PKR {income} and your planned investment amount
is PKR {amount}.

Recommended company:
{company_name}

Reason:
{reason}

Strategy:
Based on your profile, a {risk} risk strategy with a {horizon}
investment horizon is considered suitable.

InvestPK AI suggests investing gradually, maintaining an emergency fund,
and reviewing investments regularly.

Disclaimer:
Investments involve market risk. Past performance does not guarantee
future returns.
"""

        return explanation.strip()