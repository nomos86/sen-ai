
from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

API_KEY = os.environ.get("OPENROUTER_API_KEY")

@app.route("/")
def index():
    return "Senli-Benli Hikaye AI uygulaması çalışıyor."

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("prompt", "")
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "openrouter/gpt-4",
        "messages": [{"role": "user", "content": user_input}]
    }
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=payload, headers=headers)
    return jsonify(response.json())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
