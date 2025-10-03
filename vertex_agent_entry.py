from flask import Flask, request, jsonify
from agent import interact_with_agent

app = Flask(__name__)

@app.route("/", methods=["POST"])
def agent_entry():
    data = request.get_json()
    user_input = data.get("query", "")
    response_text = interact_with_agent(user_input)
    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
