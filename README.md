

# 🧠 🚀 Local AI System Action Engine (OpenClaw Style)

OpenClaw Local ek **secure, owner-controlled AI system** hai jo  
**Telegram / Local CLI** ke through aapke **Linux PC ko control** karta hai —  
**purely local AI (Ollama)** ke saath, bina cloud dependency.


🚀 Local AI System Action Engine


---

## 📁 Project Structure
local_ai/
│── ai/
│── memory/
│── create_folder/
│── delete_folder/
│── clean_python_project/
│── dispatcher.py
│── server.py
│── main.py
│── bot.py

This project is a modular Local Linux AI Control Engine that converts natural language into structured system actions using an LLM (Ollama).

🧠 Architecture Flow:
User → AI (Intent Extraction) → Dispatcher → Handler → System Execution → Response

The AI strictly converts human language into JSON-based intents.
The dispatcher routes intents to modular handlers.
Each handler safely executes system-level operations.

## 🚀 Features

- 🧠 Memory System (JSON based)
- 📜 Command History Tracking
- ⚠️ Error Tracking & Prediction
- 🧩 Intent-based Command Execution
- 🔁 Session Memory
- 🤖 AI Processing Layer (process engine)
- 📂 File & Folder Management
- 🧹 Python Project Cleaner
- 📶 WiFi Status Checker
- 🔄 Reboot / Shutdown System


🔥 Features Implemented:

1️⃣ create_folder  
- Creates directories  
- Converts relative paths to absolute  
- Returns created path  

2️⃣ delete_folder  
- Deletes specified directory  
- Validates existence before deletion  

3️⃣ clean_python_project  
- Removes __pycache__  
- Removes .pyc / .pyo files  
- Removes .pytest_cache  
- Removes build/ and dist/ folders  

4️⃣ check_wifi_status  
- Detects WiFi connection status  
- Displays connected SSID  
- Shows disconnected state  

5️⃣ shutdown_system  
- Initiates safe Linux system shutdown  

6️⃣ reboot_system  
- Initiates safe system reboot  

7️⃣ list_files  
- Lists directory contents  
- Defaults to user home if path missing  
- Converts relative paths to absolute  

🌐 Server Layer:
- Flask API endpoint: POST /chat
- AI → Dispatcher → Handler execution pipeline

🤖 Telegram Integration:
- Telegram messages routed to local AI server
- Real-time system control via chat interface

🏗️ Design Strengths:
✔ Modular architecture  
✔ Strict JSON intent enforcement  
✔ Safe system execution  
✔ Scalable handler structure  
✔ Production-style separation of logic  

This project demonstrates how a local LLM can be used to control a Linux system using structured intent-based execution.


Built with:
- Python
- Ollama
- Flask
- Telegram Bot API

Version: v1.0

---

# 🔥 BONUS (Pro Tip)

Push ke baad:

👉 GitHub open karo  
👉 README preview check karo  
👉 Star karo apne repo ko 😄  

---

# 💯 Final Result

Ab tera project:

- 💻 Structured hai  
- 🧠 AI-based lag raha hai  
- 🚀 GitHub-ready hai  
- 💼 Portfolio worthy hai  

---

Agar tu bole to next step me:

👉 Telegram bot ko AI se connect karenge  
👉 Natural language commands (Hinglish)  
👉 Auto install packages (gcc missing fix etc)

just say its next level AI: **“next level AI”** 😎


---

## ⚙️ Setup

```bash
git clone https://github.com/AbhishekTor55/local_ai.git
cd local_ai

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python main.py




