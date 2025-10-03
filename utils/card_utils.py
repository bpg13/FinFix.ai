def suggest_card_usage(cards, loans):
    best_card = max(cards, key=lambda x: x['points_rate'])
    return f"Use {best_card['name']} to pay EMIs for maximum points ({best_card['points_rate']}%)."
