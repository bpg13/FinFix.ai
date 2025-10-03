def suggest_loan_payoff(loans):
    loans_sorted = sorted(loans, key=lambda x: x['interest'], reverse=True)
    suggestions = "Suggested payoff order (highest interest first):\n"
    for loan in loans_sorted:
        suggestions += f"- {loan['name']} (${loan['balance']}, {loan['interest']}% interest)\n"
    return suggestions
