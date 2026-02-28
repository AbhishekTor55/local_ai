import json
import re
import ollama
import os

MODEL = "qwen2.5-coder:7b"

# 🔥 Auto-detect actual Linux home directory
HOME_DIR = os.path.expanduser("~")

SYSTEM_PROMPT = f"""
You are a Local AI System Action Engine.

Your job is NOT to chat.
Your job is to convert human language into structured system actions.

You MUST follow these rules:

RULE 1:
Respond ONLY with valid JSON.
No explanation.
No extra text.

RULE 2:
Supported intents ONLY:
- create_folder
- delete_folder
- clean_python_project
- check_wifi_status
- shutdown_system
- list_files
- reboot_system

RULE 3:
JSON format MUST be:
{{
  "intent": "<intent_name>",
  "args": {{}}
}}

RULE 4:
Paths must be absolute Linux paths.
If relative, convert to {HOME_DIR}/...

RULE 5:
If unsupported, return:
{{
  "intent": "unsupported",
  "args": {{}}
}}
"""

def extract_json(text: str):
    """
    Extract first JSON object from LLM output
    """
    match = re.search(r"\{[\s\S]*\}", text)
    return match.group(0) if match else None


def normalize_path(path: str) -> str:
    """
    Convert relative path to absolute HOME path
    """
    if path.startswith("/"):
        return path
    return os.path.join(HOME_DIR, path)


def process(prompt: str):
    res = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
    )

    raw = res["message"]["content"]

    # 🔎 DEBUG: exact LLM output
    print("RAW LLM OUTPUT:", raw)

    json_text = extract_json(raw)
    if not json_text:
        return {
            "intent": "unsupported",
            "args": {}
        }

    try:
        data = json.loads(json_text)

        if "intent" not in data or "args" not in data:
            raise ValueError

        # 🔧 Normalize path if present
        if "path" in data["args"]:
            data["args"]["path"] = normalize_path(data["args"]["path"])

        return data

    except Exception:
        return {
            "intent": "unsupported",
            "args": {}
        }
