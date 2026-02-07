import ollama
import subprocess
import os
import json
import re
import platform

MODEL = "qwen2.5-coder:7b"

SYSTEM_PROMPT = """
You are a local OpenClaw-like AI.

IMPORTANT:
- If the user is asking for explanation, definition, or theory → reply in plain text.
- ONLY return JSON when the user EXPLICITLY asks to perform a system action.

Valid actions:
- list_files
- open_app
- run_command

JSON format ONLY when action is required:
{
  "action": "<action>",
  "value": "<value>"
}
"""

APP_MAP = {
    "terminal": "gnome-terminal",
    "editor": "gedit",
    "browser": "firefox",
    "files": "nautilus"
}

# 🚫 NEVER ALLOWED (SYSTEM DESTROY)
HARD_BLOCK = [
    "rm -rf /",
    "mkfs",
    "dd if=",
    "shutdown",
    "reboot",
    "poweroff",
    "init 0",
    ":(){",
    "wipefs",
    "fdisk",
    "cfdisk"
]

# ⚠️ CONFIRM REQUIRED
CONFIRM_BLOCK = [
    "rm -rf",
    "chmod -R",
    "chown -R",
    "kill -9",
    "systemctl stop",
    "systemctl disable"
]

# 🔑 Detect explicit system intent
def is_system_intent(text: str) -> bool:
    keywords = [
        "run", "execute", "open", "launch",
        "show", "check", "list",
        "command", "terminal",
        "kernel", "cpu", "memory",
        "ip", "network",
        "ls", "pwd", "cd"
    ]
    text = text.lower()
    return any(k in text for k in keywords)

# 🧠 Platform detection
def detect_platform():
    sys = platform.system().lower()
    if sys == "linux":
        return "linux"
    elif sys == "windows":
        return "windows"
    elif sys == "darwin":
        return "macos"
    return "unknown"

# 🌐 Platform-aware IP command
def get_ip_command():
    os_type = detect_platform()
    if os_type == "linux":
        return "ip a"
    elif os_type == "windows":
        return "ipconfig"
    elif os_type == "macos":
        return "ifconfig"
    return None

def extract_json(text):
    match = re.search(r"\{[\s\S]*\}", text)
    if match:
        return match.group(0)
    return None

def is_hard_blocked(cmd):
    return any(bad in cmd for bad in HARD_BLOCK)

def is_confirm_required(cmd):
    return any(bad in cmd for bad in CONFIRM_BLOCK)

def process(prompt):
    try:
        res = ollama.chat(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ]
        )

        raw = res["message"]["content"]

        # 🧠 Normal explanation mode (NO system action)
        if not is_system_intent(prompt):
            return raw

        clean_json = extract_json(raw)
        if not clean_json:
            return raw

        try:
            data = json.loads(clean_json)
        except:
            return raw

        action = data.get("action")
        value = data.get("value", "").strip()

        # ---------- ACTION HANDLERS ----------

        if action == "list_files":
            path = value if value and os.path.exists(value) else os.getcwd()
            try:
                return "\n".join(os.listdir(path))
            except Exception as e:
                return f"❌ Error listing files: {e}"

        if action == "open_app":
            app = value.lower()
            if app in APP_MAP:
                subprocess.Popen([APP_MAP[app]])
                return f"✅ Opened {app}"
            try:
                subprocess.Popen([app])
                return f"✅ Opened {app}"
            except:
                return "❌ Unknown app"

        if action == "run_command":
            cmd = value.lower()

            # 🌐 Auto-fix IP commands (platform aware)
            if any(k in cmd for k in ["ip info", "ip address", "show ip", "ipconfig"]):
                ip_cmd = get_ip_command()
                if not ip_cmd:
                    return "❌ Unsupported platform for IP info"
                value = ip_cmd
                cmd = value.lower()

            # 🚫 HARD BLOCK
            if is_hard_blocked(cmd):
                return "🚫 BLOCKED: This command can destroy the system."

            # ⚠️ CONFIRM MODE
            if is_confirm_required(cmd) and not value.startswith("CONFIRM:"):
                return (
                    "⚠️ Dangerous command detected.\n"
                    "Send again with:\n"
                    "CONFIRM: <command>"
                )

            if value.startswith("CONFIRM:"):
                value = value.replace("CONFIRM:", "", 1).strip()

            try:
                output = subprocess.check_output(
                    value,
                    shell=True,
                    stderr=subprocess.STDOUT,
                    timeout=15
                ).decode()
                return output[:4000]
            except Exception as e:
                return f"❌ Command failed: {e}"

        return raw

    except Exception as e:
        return f"❌ AI Error: {e}"
