
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import requests

BOT_TOKEN = "8560430265:AAGB3stBXSB43Z8F55sqIl5FgT_V42EIo2U"  # 🔴 apna token yahan daalo

AI_SERVER_URL = "http://127.0.0.1:5000/chat"


async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text.strip()
    print(f"📩 User: {user_msg}")

    try:
        response = requests.post(
            AI_SERVER_URL,
            json={
                "text": user_msg,
                "source": "telegram"
            },
            timeout=120
        )

        # ✅ SAFE JSON HANDLING
        try:
            data = response.json()
            reply_text = data.get("reply")

            # agar reply JSON object ho (action result)
            if isinstance(reply_text, dict):
                reply_text = str(reply_text)

            if not reply_text:
                reply_text = "⚠️ Empty response from AI server"

        except Exception:
            reply_text = "⚠️ AI server returned invalid response"

    except Exception as e:
        reply_text = f"❌ Failed to connect to AI server: {e}"

    print(f"🤖 AI: {reply_text}")
    await update.message.reply_text(reply_text)


print("🚀 Starting OpenClaw Local Bot...")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

print("✅ Bot is running. Waiting for messages...")
app.run_polling()
