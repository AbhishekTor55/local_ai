import subprocess
import sys
import time
import os

print("🚀 Starting OpenClaw Local AI System...")

# 1️⃣ Start AI Server
print("🧠 Starting AI server...")
server = subprocess.Popen(
    [sys.executable, "server.py"]
)

time.sleep(2)  # server ko startup time do

# 2️⃣ Start Telegram Bot
print("📨 Starting Telegram bot...")
telegram = subprocess.Popen(
    [sys.executable, "bot.py"]
)

time.sleep(2)

# 3️⃣ Start WhatsApp Bot (Node.js) — OPTIONAL
# print("💬 Starting WhatsApp bot...")
# whatsapp_path = os.path.join(os.getcwd(), "whatsapp_bot")
# whatsapp = subprocess.Popen(
#     ["node", "index.js"],
#     cwd=whatsapp_path
# )

print("✅ All services are running!")
print("🛑 Press CTRL+C to stop everything.")

try:
    server.wait()
    telegram.wait()
    # whatsapp.wait()
except KeyboardInterrupt:
    print("\n🛑 Shutting down all services...")
    server.terminate()
    telegram.terminate()
    # whatsapp.terminate()
    print("✅ Clean shutdown complete.")
