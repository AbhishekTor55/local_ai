from flask import Flask, request, jsonify
from ai import process

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    text = data.get("text", "")
    source = data.get("source", "unknown")

    print(f"[{source}] {text}")

    reply = process(text)
    return jsonify({"reply": reply})

app.run(host="127.0.0.1", port=5000)
