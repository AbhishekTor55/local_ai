from flask import Flask, request, jsonify
from ai import process
from dispatcher import execute_action   # dispatcher.py se import

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json or {}
    text = data.get("text", "")
    source = data.get("source", "unknown")

    print(f"[{source}] {text}")

    # 🧠 Step 1: AI se intent + args nikaalo
    ai_result = process(text)

    # ❌ Unsupported intent
    if ai_result.get("intent") == "unsupported":
        return jsonify({"reply": "❌ Command not supported"})

    # ⚙️ Step 2: Dispatcher se action execute
    try:
        action_result = execute_action(ai_result)
        return jsonify({"reply": action_result})
    except Exception as e:
        print("❌ ACTION ERROR:", e)
        return jsonify({"reply": f"❌ Action failed: {e}"}), 500


if __name__ == "__main__":
    print("🚀 Starting OpenClaw AI Server on http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, threaded=True)
