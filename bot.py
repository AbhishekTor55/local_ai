from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from ai import process

BOT_TOKEN = "8560430265:AAGB3stBXSB43Z8F55sqIl5FgT_V42EIo2U"

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text.strip()
    print(f"📩 User: {user_msg}")

    result = process(user_msg)
    print(f"🤖 AI: {result}")

    await update.message.reply_text(result)

print("🚀 Starting OpenClaw Local Bot...")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

print("✅ Bot is running. Waiting for messages...")
app.run_polling()
