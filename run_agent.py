from agent import interact_with_agent

print("=== AI Debt & EMI Optimizer ===")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    print(interact_with_agent(user_input))
