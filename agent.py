import os
import json
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

with open("data/loans.json") as f:
    loans = json.load(f)
with open("data/credit_cards.json") as f:
    cards = json.load(f)

def suggest_loan_payoff(loans):
    loans_sorted = sorted(loans, key=lambda x: x['interest'], reverse=True)
    return "\n".join([f"- {l['name']} (${l['balance']}, {l['interest']}%)" for l in loans_sorted])

def suggest_card_usage(cards):
    best = max(cards, key=lambda x: x['points_rate'])
    return f"Use {best['name']} for max points ({best['points_rate']}%)"

def get_ai_advice(user_input):
    response = genai.chat_completions.create(
        model="chat-bison-001",
        messages=[{"author": "user", "content": user_input}]
    )
    return response.choices[0].message["content"]

def interact_with_agent(user_input):
    payoff = suggest_loan_payoff(loans)
    card = suggest_card_usage(cards)
    ai_response = get_ai_advice(user_input)
    return f"{payoff}\n{card}\nAI Advice: {ai_response}"
