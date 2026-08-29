from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)

# Allow your frontend
CORS(app)

API_KEY = "ht_live_A5Rx8z5W5WY7lmOyLN5Ro3eDbFiQ24yYq1M7LBDR1odUcBBm"
URL = "https://heavstal.com.ng/api/v1/jeden"

headers = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY
}


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "online",
        "message": "AJ API is running 🚀"
    })


@app.route("/chat", methods=["POST"])
def chat():
    try:
        body = request.get_json()

        if not body or "message" not in body:
            return jsonify({
                "error": "Message is required"
            }), 400

        user_message = body["message"]

        data = {
            "prompt": user_message,
            "persona": (
                "You are AJ, a friendly, helpful AI assistant. Created by Sadiku Ahmad Adebayo,On August 26th Wednesday 2026"
                "Answer naturally, clearly and concisely."
            )
        }

        response = requests.post(
            URL,
            headers=headers,
            json=data,
            timeout=30
        )

        result = response.json()

        ai_response = result["data"]["response"]

        return jsonify({
            "response": ai_response
        })

    except requests.RequestException as e:
        return jsonify({
            "error": "Failed to connect to AI service",
            "details": str(e)
        }), 502

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
