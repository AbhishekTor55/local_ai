# local_ai

# 🧠 🚀 Local AI System Action Engine

OpenClaw Local ek **secure, owner-controlled AI system** hai jo  
**Telegram / Local CLI** ke through aapke **Linux PC ko control** karta hai —  
**purely local AI (Ollama)** ke saath, bina cloud dependency.


🚀 Local AI System Action Engine

This project is a modular Local Linux AI Control Engine that converts natural language into structured system actions using an LLM (Ollama).

🧠 Architecture Flow:
User → AI (Intent Extraction) → Dispatcher → Handler → System Execution → Response

The AI strictly converts human language into JSON-based intents.
The dispatcher routes intents to modular handlers.
Each handler safely executes system-level operations.

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


