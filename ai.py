
import ollama
import subprocess
import os
import json
import re

MODEL = "qwen2.5-coder:7b"

SYSTEM_PROMPT = """
You are a local OpenClaw-like AI.

RULES:
- Only return JSON when a system action is required
- No markdown, no explanation, only raw JSON

Valid actions:
- list_files
- open_app
- run_command

JSON format:
{
  "action": "<action>",
  "value": "<value>"
}
"""

# Allowed apps (STRICT + direct allowed)
APP_MAP = {
    "terminal": "gnome-terminal",
    "editor": "gedit",
    "browser": "firefox",
    "files": "nautilus"
}

# Dangerous commands (blocked)
DANGEROUS_COMMANDS = [
    "rm ",
    "shutdown",
    "reboot",
    "mkfs",
    ":(){"
]

def extract_json(text):
    match = re.search(r"\{[\s\S]*\}", text)
    if match:
        return match.group(0)
    return text.strip()

def process(prompt):
    try:
        # Ask local Ollama
        res = ollama.chat(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ]
        )

        raw = res["message"]["content"]
        clean = extract_json(raw)

        # Try JSON parse
        try:
            data = json.loads(clean)
        except:
            return raw  # normal chat reply

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

            # mapped apps
            if app in APP_MAP:
                subprocess.Popen([APP_MAP[app]])
                return f"✅ Opened {app}"

            # direct binary allowed
            try:
                subprocess.Popen([app])
                return f"✅ Opened {app}"
            except:
                return "❌ Unknown app"

        if action == "run_command":
            # block dangerous commands
            for bad in DANGEROUS_COMMANDS:
                if bad in value:
                    return "❌ Dangerous command blocked"

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

        return "❌ Unknown action"

    except Exception as e:
        return f"❌ AI Error: {e}"