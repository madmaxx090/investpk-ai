def build_investment_prompt(
    user_data,
    companies
):

    prompt = f"""
You are InvestPK AI, a financial decision assistant for Pakistani investors.

Analyze this investor profile:

Age:
{user_data.age}

Monthly Income:
{user_data.monthly_income} PKR

Monthly Expenses:
{user_data.monthly_expenses} PKR

Investment Amount:
{user_data.investment_amount} PKR

Investment Goal:
{user_data.investment_goal}

Investment Horizon:
{user_data.investment_horizon}

Risk Tolerance:
{user_data.risk_tolerance}

Recommended Companies:
{companies}


Generate:

1. Explanation of why these companies match the investor.
2. Potential risks.
3. A simple investment strategy.

Rules:
- Do not guarantee profits.
- Mention that investments carry risk.
- Keep explanation simple for beginners.
"""

    return prompt